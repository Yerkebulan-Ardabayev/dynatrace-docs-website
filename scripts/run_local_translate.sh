#!/bin/bash
# Локальный перевод очереди статей через подписку Claude (claude -p).
#
# Зачем локально, а не в GitHub Actions: headless-вызову нужен OAuth-токен
# подписки, и держать его в секретах публичного репозитория не хочется, плюс
# джоба в CI ограничена 180 минутами, а разбор бэклога идёт часами.
#
# Устойчивость к обрыву: работа идёт батчами, после каждого батча коммит.
# Очередь пересчитывается заново на каждой итерации из detect_changes.py,
# поэтому возобновление после падения = просто повторный запуск.
#
#   BATCH=25 MAX=0 PUSH=0 scripts/run_local_translate.sh
#     BATCH — сколько статей на один коммит
#     MAX   — предел статей за прогон (0 = вся очередь)
#     PUSH  — 1, чтобы запушить в main в конце (запускает пересборку сайта)

set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO" || exit 1

BATCH="${BATCH:-25}"
MAX="${MAX:-0}"
PUSH="${PUSH:-0}"
PY="$REPO/.venv/bin/python"
[ -x "$PY" ] || PY="python3"

LOG_DIR="$REPO/logs"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/translate-$(date +%Y%m%d-%H%M%S).log"

# Один прогон за раз: ночная джоба не должна наложиться на ручной запуск.
LOCK="$REPO/.translate.lock"
if ! mkdir "$LOCK" 2>/dev/null; then
    echo "Уже идёт другой прогон перевода ($LOCK), выхожу." | tee -a "$LOG"
    exit 0
fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

log() { echo "[$(date +%H:%M:%S)] $*" | tee -a "$LOG"; }

log "=== Перевод очереди: BATCH=$BATCH MAX=$MAX PUSH=$PUSH ==="

# Свежий английский корпус: его каждую ночь коммитит GitHub Actions.
git pull --ff-only >>"$LOG" 2>&1 || log "ВНИМАНИЕ: git pull не прошёл, работаю на текущем состоянии"

total_done=0
round=0

while :; do
    round=$((round + 1))

    "$PY" scripts/detect_changes.py --report changes_report.json >>"$LOG" 2>&1
    QUEUE=$("$PY" -c "import json;print(json.load(open('changes_report.json'))['total_changes'])" 2>/dev/null || echo 0)
    log "круг $round: в очереди $QUEUE, переведено за прогон $total_done"

    [ "$QUEUE" -eq 0 ] && { log "Очередь пуста."; break; }

    take="$BATCH"
    if [ "$MAX" -gt 0 ]; then
        left=$((MAX - total_done))
        [ "$left" -le 0 ] && { log "Достигнут предел прогона MAX=$MAX."; break; }
        [ "$left" -lt "$take" ] && take="$left"
    fi

    "$PY" scripts/translate_changed.py --report changes_report.json --max-articles "$take" 2>&1 | tee -a "$LOG" | tail -3

    DONE=$("$PY" -c "import json;print(json.load(open('translation_result.json'))['translated_count'])" 2>/dev/null || echo 0)
    FAILED=$("$PY" -c "import json;print(json.load(open('translation_result.json')).get('failed_count',0))" 2>/dev/null || echo 0)

    # Ноль переводов при непустой очереди = системная причина (лимит подписки,
    # протухший токен, сеть). Дальше крутиться бессмысленно, статьи не потеряются:
    # реестр хэшей их не отпустит, следующий запуск продолжит с того же места.
    if [ "$DONE" -eq 0 ]; then
        log "СТОП: за круг не переведено ничего (ошибок: $FAILED). Смотри $LOG"
        break
    fi

    "$PY" scripts/validate_translations.py --ru-dir docs/managed-ru --en-dir docs/managed \
        --report translation_result.json >>"$LOG" 2>&1
    if [ $? -ne 0 ]; then
        log "СТОП: валидация свежих переводов не прошла, ничего не коммичу. Смотри $LOG"
        break
    fi

    git add docs/managed-ru scripts/.change_tracking/hash_registry.json >>"$LOG" 2>&1
    git commit -m "docs(ru): перевод ${DONE} статей через claude -p ($(date +%Y-%m-%d))" >>"$LOG" 2>&1 \
        && log "коммит: +${DONE} статей" \
        || log "нечего коммитить"

    total_done=$((total_done + DONE))
done

log "=== Итого переведено: $total_done ==="

if [ "$PUSH" = "1" ] && [ "$total_done" -gt 0 ]; then
    if git push >>"$LOG" 2>&1; then
        log "Запушено в main, сайт пересоберётся деплоем."
    else
        log "ОШИБКА push, изменения остались локально. Смотри $LOG"
    fi
fi

log "Лог: $LOG"
