"""Полная навигация из файловой системы (аудит 2026-07-08, орфаны).

Раньше nav в mkdocs.yml перечислял 58 страниц из 2697 — остальные 98% были
доступны только через поиск и встроенные ссылки (боковое меню на них пустое).
Этот хук на on_config строит nav программно из дерева docs/managed-ru при
КАЖДОЙ сборке: после ночного sync новые страницы попадают в меню сами,
меню не гниёт.

Правила:
- топ-разделы и их порядок кураторские (русские, как в старом nav);
- поддерево раздела = структура каталога: подкаталог F с соседним хабом F.md
  становится секцией с заголовком из title/H1 хаба, сам хаб — первым пунктом
  «Обзор» (не дублируем заголовок секции пунктом с тем же именем — старая
  боль с «дублями» в сайдбаре);
- листья идут без заголовка: MkDocs берёт русский title из frontmatter;
- managed-ru/index.md в nav не включаем: «Главная» сайта — docs/index.md,
  а это зеркало приветственной upstream-страницы (дубль H1).

Боковое меню остаётся лёгким: navigation.prune рендерит только активную ветку.
"""

from pathlib import Path

# Русские заголовки для каталогов БЕЗ hub-страницы (у ~170 каталогов нет
# соседнего <dir>.md, взять title неоткуда). Частые сегменты переводим,
# остальные остаются слагом как есть (cluster-api-v2 и т.п. читаются как
# технические идентификаторы, это лучше кривого "Cluster api v2").
DIR_RU = {
    "accounts-environments": "Аккаунты и окружения",
    "adaptive-traffic-management": "Адаптивное управление трафиком",
    "additional-configuration": "Дополнительная настройка",
    "advanced": "Расширенное",
    "advanced-configuration": "Расширенная настройка",
    "advanced-security-configurations": "Расширенные настройки безопасности",
    "analysis": "Анализ",
    "analysis-and-alerting": "Анализ и оповещения",
    "analyze-and-use": "Анализ и использование",
    "api-references": "Справочники API",
    "api-version-migration-guides": "Миграция версий API",
    "application-security": "Безопасность приложений",
    "apps": "Приложения",
    "aws-metrics-ingest": "Приём метрик AWS",
    "aws-platform": "Платформа AWS",
    "azure-platform": "Платформа Azure",
    "basic-concepts": "Основные понятия",
    "basics": "Основы",
    "capabilities": "Возможности",
    "charts-and-tiles": "Графики и плитки",
    "cloud-platform-monitoring": "Мониторинг облачных платформ",
    "comments": "Комментарии",
    "components": "Компоненты",
    "configuration": "Настройка",
    "configuration-and-analysis": "Настройка и анализ",
    "cost": "Стоимость",
    "cost-monitors": "Мониторы затрат",
    "cross-platform-frameworks": "Кроссплатформенные фреймворки",
    "customization": "Кастомизация",
    "dashboards": "Дашборды",
    "data-privacy": "Приватность данных",
    "data-security": "Безопасность данных",
    "data-sources": "Источники данных",
    "dem-use-cases": "Сценарии DEM",
    "detection-rules": "Правила обнаружения",
    "environments": "Окружения",
    "error-rules": "Правила ошибок",
    "general-information": "Общая информация",
    "guides": "Руководства",
    "ingestion-methods": "Способы приёма",
    "initial-setup": "Первоначальная настройка",
    "installation": "Установка",
    "instrumentation": "Инструментирование",
    "integrate-into-aws": "Интеграция в AWS",
    "integrate-with-aws": "Интеграция с AWS",
    "key-user-actions": "Ключевые действия пользователя",
    "legacy": "Устаревшее",
    "metric-definitions": "Определения метрик",
    "monitoring": "Мониторинг",
    "monitoring-and-instrumentation": "Мониторинг и инструментирование",
    "networks-classic": "Сети Classic",
    "objects": "Объекты",
    "oneagent-and-opentelemetry": "OneAgent и OpenTelemetry",
    "oneagent-troubleshooting": "Диагностика OneAgent",
    "operation": "Эксплуатация",
    "other": "Прочее",
    "other-deployment-modes": "Другие режимы развёртывания",
    "problems": "Проблемы",
    "reference": "Справочник",
    "references": "Справочники",
    "resource-management": "Управление ресурсами",
    "schemas": "Схемы",
    "service-detection": "Обнаружение сервисов",
    "service-types": "Типы сервисов",
    "setup": "Настройка",
    "subscription-and-license": "Подписка и лицензия",
    "subscriptions": "Подписки",
    "support": "Поддержка",
    "tutorials": "Учебные материалы",
    "updates-and-maintenance": "Обновления и обслуживание",
    "usage": "Использование",
    "use-cases": "Сценарии использования",
    "zosmf-installer": "Установщик z/OSMF",
}


def _page_title(md_path: Path) -> str | None:
    """title: из frontmatter, иначе первый H1."""
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for line in lines[1:30]:
            if line.strip() == "---":
                break
            if line.startswith("title:"):
                val = line[len("title:"):].strip().strip("\"'")
                if val:
                    return val
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return None


def _expand_dir(docs: Path, rel_dir: str, skip: set[str]) -> list:
    """Дерево каталога rel_dir -> список nav-элементов (рекурсивно)."""
    abs_dir = docs / rel_dir
    if not abs_dir.is_dir():
        return []
    entries = []
    files = {p.stem: p for p in abs_dir.glob("*.md")}
    subdirs = sorted(d.name for d in abs_dir.iterdir() if d.is_dir())
    used_as_hub = set()

    for name in subdirs:
        child_rel = f"{rel_dir}/{name}"
        hub = files.get(name)
        children = _expand_dir(docs, child_rel, skip)
        if hub is not None:
            used_as_hub.add(name)
        hub_rel = f"{child_rel}.md"
        if hub is not None and hub_rel not in skip:
            title = _page_title(hub) or DIR_RU.get(name, name)
            entries.append((name, {title: [{"Обзор": hub_rel}] + children}))
        elif children:
            entries.append((name, {DIR_RU.get(name, name): children}))

    for stem in sorted(files):
        if stem in used_as_hub:
            continue
        rel = f"{rel_dir}/{stem}.md"
        if rel in skip:
            continue
        entries.append((stem, rel))

    # детерминированный порядок: по слагу, секции и листья вперемешку
    entries.sort(key=lambda t: t[0])
    return [e for _, e in entries]


def on_config(config):
    docs = Path(config["docs_dir"])
    ru = "managed-ru"
    skip: set[str] = set()

    def hub_section(rel_md: str, extra_dirs: list[str] | None = None) -> list:
        """[{Обзор: hub}, *дети каталога(ов)]."""
        out = []
        if (docs / rel_md).exists():
            out.append({"Обзор": rel_md})
            skip.add(rel_md)
        for d in extra_dirs or []:
            out.extend(_expand_dir(docs, d, skip))
        return out

    def dir_title(rel_md: str, fallback: str) -> str:
        p = docs / rel_md
        return (_page_title(p) if p.exists() else None) or fallback

    nav = [
        {"Главная": "index.md"},
        {
            "Начало работы": [
                {"Быстрый старт": "ru/getting-started.md"},
                {"Обзор Dynatrace Managed": f"{ru}/managed.md"},
            ]
            + _expand_dir(docs, f"{ru}/discover-dynatrace", skip)
        },
        {
            "Кластер Managed": [
                {"Установка": f"{ru}/installation.md"},
                {"Настройка": f"{ru}/configuration.md"},
                {"Обслуживание": f"{ru}/operations.md"},
                {"Обновление": f"{ru}/update.md"},
                {"Безопасность": f"{ru}/security.md"},
                {"Резервное копирование": f"{ru}/backup.md"},
                {"Памятка по кластеру": f"{ru}/cluster.md"},
                {"Обзор кластера": f"{ru}/managed-cluster.md"},
            ]
            + _expand_dir(docs, f"{ru}/managed-cluster", skip)
            + [
                {
                    dir_title(f"{ru}/license.md", "Лицензирование Dynatrace"):
                        hub_section(f"{ru}/license.md", [f"{ru}/license"])
                },
                {
                    dir_title(f"{ru}/upgrade.md", "Переход с Managed на SaaS"):
                        hub_section(f"{ru}/upgrade.md", [f"{ru}/upgrade"])
                },
            ]
        },
        {"Источники данных": hub_section(f"{ru}/ingest-from.md", [f"{ru}/ingest-from"])},
        {"Наблюдаемость": _expand_dir(docs, f"{ru}/observe", skip)},
        {"Davis AI": hub_section(f"{ru}/dynatrace-intelligence.md", [f"{ru}/dynatrace-intelligence"])},
        {"Анализ": _expand_dir(docs, f"{ru}/analyze-explore-automate", skip)},
        {"Deliver": hub_section(f"{ru}/deliver.md", [f"{ru}/deliver"])},
        {"Безопасность приложений": _expand_dir(docs, f"{ru}/secure", skip)},
        {"Управление": _expand_dir(docs, f"{ru}/manage", skip)},
        {"Платформа": _expand_dir(docs, f"{ru}/platform", skip)},
        {"API": hub_section(f"{ru}/dynatrace-api.md", [f"{ru}/dynatrace-api"])},
        {"Что нового": hub_section(f"{ru}/whats-new.md", [f"{ru}/whats-new"])},
        {"Офлайн-документация": _expand_dir(docs, f"{ru}/offline-doc", skip)},
        {"Обучение": _expand_dir(docs, "ru/training", skip)},
        {"AI Помощник": "ai/groq.md"},
    ]

    # пустые разделы (каталог исчез) не показываем
    nav = [item for item in nav if not (
        isinstance(item, dict) and not next(iter(item.values()))
    )]

    config["nav"] = nav

    total = sum(1 for _ in _iter_pages(nav))
    print(f"[full_nav] nav построен: {total} страниц")
    return config


def _iter_pages(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, list):
        for x in node:
            yield from _iter_pages(x)
    elif isinstance(node, dict):
        for v in node.values():
            yield from _iter_pages(v)
