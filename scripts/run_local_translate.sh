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
#     BATCH         — сколько статей на один коммит
#     MAX           — предел статей за прогон (0 = вся очередь)
#     PUSH          — 1, чтобы запушить в main в конце (запускает пересборку сайта)
#     STALL_RETRIES — сколько раз переждать простой (лимит подписки), 0 = не ждать
#     STALL_WAIT    — пауза между попытками после простоя, секунд

set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO" || exit 1

BATCH="${BATCH:-25}"
MAX="${MAX:-0}"
PUSH="${PUSH:-0}"
STALL_RETRIES="${STALL_RETRIES:-0}"
STALL_WAIT="${STALL_WAIT:-1800}"
# Интерпретатор можно навязать снаружи (PY=...). Это нужно launchd-агенту:
# venv-питон 3.12 лежит в ~/Desktop, а питон 3.12 не наследует Full Disk Access
# от bash и падает с EPERM на любом чтении из защищённой папки. Питон 3.14 FDA
# наследует, а вся цепочка перевода обходится стандартной библиотекой, поэтому
# агенту достаточно подсунуть системный 3.14, не пересобирая venv.
if [ -z "${PY:-}" ]; then
    PY="$REPO/.venv/bin/python"
    [ -x "$PY" ] || PY="python3"
fi

LOG_DIR="$REPO/logs"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/translate-$(date +%Y%m%d-%H%M%S).log"

# Один прогон за раз: дневная джоба не должна наложиться на ручной запуск.
# Замок хранит pid владельца, иначе прогон, убитый по SIGKILL или уснувший
# вместе с машиной, оставляет каталог навсегда: trap на такое не срабатывает,
# и каждый следующий запуск молча выходит с кодом 0, выглядя здоровым.
LOCK="$REPO/.translate.lock"
if ! mkdir "$LOCK" 2>/dev/null; then
    OTHER="$(cat "$LOCK/pid" 2>/dev/null || true)"
    if [ -z "$OTHER" ]; then
        # Замок без pid оставила прежняя версия скрипта: живость не проверить,
        # поэтому считаем прогон идущим, чтобы не запустить второй поверх первого.
        echo "Замок $LOCK без pid, считаю прогон живым и выхожу. Если прогона нет, удали каталог." | tee -a "$LOG"
        exit 0
    fi
    if kill -0 "$OTHER" 2>/dev/null; then
        echo "Уже идёт другой прогон перевода (pid $OTHER), выхожу." | tee -a "$LOG"
        exit 0
    fi
    echo "Замок $LOCK остался от мёртвого процесса $OTHER, снимаю и продолжаю." | tee -a "$LOG"
    rm -rf "$LOCK"
    mkdir "$LOCK" 2>/dev/null || { echo "Не смог взять замок $LOCK, выхожу." | tee -a "$LOG"; exit 0; }
fi
echo $$ >"$LOCK/pid"
trap 'rm -rf "$LOCK" 2>/dev/null' EXIT

log() { echo "[$(date +%H:%M:%S)] $*" | tee -a "$LOG"; }

log "=== Перевод очереди: BATCH=$BATCH MAX=$MAX PUSH=$PUSH ==="

# Предполётная проверка интерпретатора. Под launchd питон 3.12 не наследует
# Full Disk Access и падает с EPERM на любом чтении из ~/Desktop, а прогон при
# этом выглядит успешным: detect_changes молчит в лог, очередь читается как 0,
# скрипт пишет «Очередь пуста» и выходит с кодом 0. Ломаемся громко и с 78
# (EX_CONFIG), чтобы поломка была видна в launchctl print, а не пряталась.
if ! "$PY" -c 'import pathlib; pathlib.Path("scripts/detect_changes.py").read_text()' >>"$LOG" 2>&1; then
    log "СТОП: интерпретатор $PY не может прочитать репозиторий."
    log "Похоже на TCC/Full Disk Access под launchd. Проверь вручную:"
    log "  $PY -c 'import pathlib; print(len(pathlib.Path(\"scripts/detect_changes.py\").read_text()))'"
    exit 78
fi

# Свежий английский корпус: его каждую ночь коммитит GitHub Actions.
git pull --ff-only >>"$LOG" 2>&1 || log "ВНИМАНИЕ: git pull не прошёл, работаю на текущем состоянии"

total_done=0
round=0
stalls=0

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

    # Ноль переводов при непустой очереди = системная причина: чаще всего упор в
    # лимит подписки, реже протухший токен или сеть. Лимит проходит сам, поэтому
    # длинный прогон пережидает окно, а не падает. Статьи в любом случае не
    # теряются: реестр хэшей их не отпустит, следующий запуск продолжит отсюда.
    if [ "$DONE" -eq 0 ]; then
        if [ "$stalls" -lt "$STALL_RETRIES" ]; then
            stalls=$((stalls + 1))
            log "простой (ошибок: $FAILED), жду ${STALL_WAIT}с и пробую снова [$stalls/$STALL_RETRIES]"
            sleep "$STALL_WAIT"
            continue
        fi
        log "СТОП: за круг не переведено ничего (ошибок: $FAILED). Смотри $LOG"
        break
    fi
    stalls=0

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
