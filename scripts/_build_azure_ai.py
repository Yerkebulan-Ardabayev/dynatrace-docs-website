#!/usr/bin/env python3
"""Build RU translations for the 21 monitor-azure-ai-* metric files.

Byte-safe substring replacement on each EN source so that frontmatter
(source/scraped), duplicate H1, the double-encoded mojibake ellipsis
(c3 a2 c2 80 c2 a6 between the browse-menu parens) and the hard-break
trailing spaces all pass through untouched. Only translatable phrases,
headings, the intro, version lines, the enable-monitoring link and the
metrics-table cells (Description/Unit/Recommended) are replaced.

Canon: L4-IF.7 (Prerequisites -> Предварительные условия), grep-confirmed
dominant corpus patterns (step-4 boilerplate 33x, link text 32x), style
guide (bold UI labels kept EN incl. **Dashboards**). Dimensions + metric
Names stay EN (Azure Metrics API identifiers).
"""

from pathlib import Path

EN_DIR = Path(
    "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
)
RU_DIR = Path(
    "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
)

# --- per-file English title (== both H1 lines) -> Russian title ---
TITLE_MAP = {
    "monitor-azure-ai-all-in-one.md": (
        "Azure AI - All In One monitoring",
        "Мониторинг Azure AI - All In One",
    ),
    "monitor-azure-ai-anomaly-detector.md": (
        "Azure AI - Anomaly Detector monitoring",
        "Мониторинг Azure AI - Anomaly Detector",
    ),
    "monitor-azure-ai-bing-autosuggest.md": (
        "Azure AI - Bing Autosuggest monitoring",
        "Мониторинг Azure AI - Bing Autosuggest",
    ),
    "monitor-azure-ai-bing-custom-search.md": (
        "Azure AI - Bing Custom Search monitoring",
        "Мониторинг Azure AI - Bing Custom Search",
    ),
    "monitor-azure-ai-bing-entity-search.md": (
        "Azure AI - Bing Entity Search monitoring",
        "Мониторинг Azure AI - Bing Entity Search",
    ),
    "monitor-azure-ai-bing-search.md": (
        "Azure AI - Bing Search monitoring",
        "Мониторинг Azure AI - Bing Search",
    ),
    "monitor-azure-ai-bing-spell-check.md": (
        "Azure AI - Bing Spell Check monitoring",
        "Мониторинг Azure AI - Bing Spell Check",
    ),
    "monitor-azure-ai-computer-vision.md": (
        "Azure AI - Computer Vision monitoring",
        "Мониторинг Azure AI - Computer Vision",
    ),
    "monitor-azure-ai-content-moderator.md": (
        "Azure AI Content Moderator monitoring",
        "Мониторинг Azure AI Content Moderator",
    ),
    "monitor-azure-ai-custom-vision-prediction.md": (
        "Azure AI - Custom Vision Prediction monitoring",
        "Мониторинг Azure AI - Custom Vision Prediction",
    ),
    "monitor-azure-ai-custom-vision-training.md": (
        "Azure AI - Custom Vision monitoring",
        "Мониторинг Azure AI - Custom Vision",
    ),
    "monitor-azure-ai-face.md": (
        "Azure AI - Face monitoring",
        "Мониторинг Azure AI - Face",
    ),
    "monitor-azure-ai-immersive-reader.md": (
        "Azure AI - Immersive Reader monitoring",
        "Мониторинг Azure AI - Immersive Reader",
    ),
    "monitor-azure-ai-language-understanding-authoring.md": (
        "Azure AI - Language Understanding (LUIS) Authoring monitoring",
        "Мониторинг Azure AI - Language Understanding (LUIS) Authoring",
    ),
    "monitor-azure-ai-language-understanding.md": (
        "Azure AI - Language Understanding (LUIS) monitoring",
        "Мониторинг Azure AI - Language Understanding (LUIS)",
    ),
    "monitor-azure-ai-openai.md": ("Azure OpenAI", "Azure OpenAI"),
    "monitor-azure-ai-personalizer.md": (
        "Azure AI - Personalizer monitoring",
        "Мониторинг Azure AI - Personalizer",
    ),
    "monitor-azure-ai-qna-maker.md": (
        "Azure AI - QnA Maker monitoring",
        "Мониторинг Azure AI - QnA Maker",
    ),
    "monitor-azure-ai-speech.md": (
        "Azure AI - Speech monitoring",
        "Мониторинг Azure AI - Speech",
    ),
    "monitor-azure-ai-text-analytics.md": (
        "Azure AI - Text Analytics monitoring",
        "Мониторинг Azure AI - Text Analytics",
    ),
    "monitor-azure-ai-translator.md": (
        "Azure AI - Translator monitoring",
        "Мониторинг Azure AI - Translator",
    ),
}

# --- date strings present in this batch ---
DATE_MAP = {
    "* Published Sep 22, 2020": "* Опубликовано 22 сентября 2020 г.",
    "* Published Mar 25, 2024": "* Опубликовано 25 марта 2024 г.",
}

# --- whole-text phrase replacements (ordered, longest/most-specific first
# where overlap is possible). None of these keys contain the mojibake. ---
PROSE = [
    # tag line
    ("* How-to guide", "* Практическое руководство"),
    ("* 1-min read", "* Чтение: 1 мин"),
    ("* 2-min read", "* Чтение: 2 мин"),
    ("* 4-min read", "* Чтение: 4 мин"),
    # prerequisites + version lines
    ("## Prerequisites", "## Предварительные условия"),
    ("Dynatrace version ", "Dynatrace версии "),
    ("Environment ActiveGate version ", "Environment ActiveGate версии "),
    # intro paragraph (prefix + suffix; service name in between stays EN)
    (
        "Dynatrace ingests metrics from Azure Metrics API for ",
        "Dynatrace получает метрики из Azure Metrics API для ",
    ),
    (
        ". You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.",
        ". Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.",
    ),
    # enable monitoring
    ("## Enable monitoring", "## Включение мониторинга"),
    (
        "To learn how to enable service monitoring, see [Enable service monitoring](",
        "Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](",
    ),
    (
        "Enable Azure monitoring in Dynatrace.",
        "Включение мониторинга Azure в Dynatrace.",
    ),
    # ----- View service metrics boilerplate (identical in every file) -----
    ("## View service metrics", "## Просмотр метрик сервиса"),
    (
        "You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.",
        "Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.",
    ),
    (
        "### View metrics on the custom device overview page",
        "### Просмотр метрик на странице обзора пользовательского устройства",
    ),
    (
        "To access the custom device overview page",
        "Чтобы перейти на страницу обзора пользовательского устройства:",
    ),
    (
        "1. Go to **Technologies & Processes**.",
        "1. Перейдите в **Technologies & Processes**.",
    ),
    (
        "2. Filter by service name and select the relevant custom device group.",
        "2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.",
    ),
    (
        "3. Once you select the custom device group, you're on the **custom device group overview page**.",
        "3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.",
    ),
    (
        "4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.",
        "4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.",
    ),
    ("### View metrics on your dashboard", "### Просмотр метрик на дашборде"),
    (
        "If the service has a preset dashboard, you'll get a preset dashboard for the respective service containing all recommended metrics on your **Dashboards** page. You can look for specific dashboards by filtering by **Preset** and then by **Name**.",
        "Если для сервиса предусмотрен предустановленный дашборд, он появится на вашей странице **Dashboards** с набором всех рекомендуемых метрик. Искать конкретные дашборды можно с помощью фильтрации по **Preset**, а затем по **Name**.",
    ),
    (
        "For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **Azure**, select the desired Azure instance, then select **Save**.",
        "Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд отобразился на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.",
    ),
    # the two mojibake lines: replace the prose around (** ... **) only
    (
        "You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (",
        "Вы не можете вносить изменения непосредственно в предустановленный дашборд, но можете клонировать его и редактировать. Чтобы клонировать дашборд, откройте меню обзора (",
    ),
    (") and select **Clone**.", ") и выберите **Clone**."),
    (
        "To remove a dashboard from the dashboards list, you can hide it. To hide a dashboard, open the browse menu (",
        "Чтобы убрать дашборд из списка, его можно скрыть. Чтобы скрыть дашборд, откройте меню обзора (",
    ),
    (") and select **Hide**.", ") и выберите **Hide**."),
    (
        "Hiding a dashboard doesn't affect other users.",
        "Скрытие дашборда не затрагивает других пользователей.",
    ),
    # metrics section heading + table header
    ("## Available metrics", "## Доступные метрики"),
    (
        "| Name | Description | Dimensions | Unit | Recommended |",
        "| Имя | Описание | Измерения | Единица измерения | Рекомендуется |",
    ),
]

# --- metrics table cell maps ---
DESC_MAP = {
    "Number of calls that exceeded rate or quota limit": "Количество вызовов, превысивших лимит частоты или квоты",
    "Number of calls with client side error (HTTP response code `4xx`)": "Количество вызовов с ошибкой на стороне клиента (код ответа HTTP `4xx`)",
    "Number of calls with client-side error (HTTP response code `4xx`)": "Количество вызовов с ошибкой на стороне клиента (код ответа HTTP `4xx`)",
    "Size of incoming data in bytes": "Размер входящих данных в байтах",
    "Size of outgoing data in bytes": "Размер исходящих данных в байтах",
    "Latency in milliseconds": "Задержка в миллисекундах",
    "Number of calls with service internal error (HTTP response code `5xx`)": "Количество вызовов с внутренней ошибкой сервиса (код ответа HTTP `5xx`)",
    "Number of calls with service internal error (HTTP response code 5xx)": "Количество вызовов с внутренней ошибкой сервиса (код ответа HTTP 5xx)",
    "Number of successful calls": "Количество успешных вызовов",
    "Total number of calls": "Общее количество вызовов",
    "Total number of calls with error response (HTTP response code `4xx` or `5xx`)": "Общее количество вызовов с ответом об ошибке (код ответа HTTP `4xx` или `5xx`)",
    "Total number of token calls": "Общее количество вызовов токенов",
    "Total number of characters trained": "Общее количество обученных символов",
    "Total number of characters in incoming text request": "Общее количество символов во входящем текстовом запросе",
    "Total number of transactions": "Общее количество транзакций",
    # OpenAI-specific
    "Availability rate": "Уровень доступности",
    "Blocked calls": "Заблокированные вызовы",
    "Client errors": "Клиентские ошибки",
    "Data in": "Входящие данные",
    "Data out": "Исходящие данные",
    "Number of generated completion tokens": "Количество сгенерированных токенов завершения",
    "Latency": "Задержка",
    "Processed fine tuned training hours": "Обработанные часы тонкой настройки обучения",
    "Processed inference tokens": "Обработанные токены инференса",
    "Processed prompt tokens": "Обработанные токены промпта",
    "Ratelimit": "Ограничение частоты запросов",
    "Number of server errors": "Количество ошибок сервера",
    "Number of calls": "Количество вызовов",
    "Number of errors": "Количество ошибок",
}
UNIT_MAP = {
    "Count": "Количество",
    "Byte": "Байт",
    "Bytes": "Байты",
    "Percent": "Процент",
    "MilliSecond": "Миллисекунда",
}
REC_MAP = {"Applicable": "Применимо", "": ""}

RU_HEADER_FIRST = "Имя"  # to skip the (already translated) header row
warnings = []


def tr_table_row(line, fname):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) != 5:
        warnings.append(f"{fname}: row not 5 cells -> {line!r}")
        return line
    name, desc, dims, unit, rec = cells
    if name in (RU_HEADER_FIRST, "Name") or set(desc) == {"-"}:
        return line
    if desc not in DESC_MAP:
        warnings.append(f"{fname}: untranslated DESC -> {desc!r}")
    if unit not in UNIT_MAP:
        warnings.append(f"{fname}: unmapped UNIT -> {unit!r}")
    if rec not in REC_MAP:
        warnings.append(f"{fname}: unmapped REC -> {rec!r}")
    return (
        "| "
        + " | ".join(
            [
                name,
                DESC_MAP.get(desc, desc),
                dims,
                UNIT_MAP.get(unit, unit),
                REC_MAP.get(rec, rec),
            ]
        )
        + " |"
    )


def build_one(fname):
    en = (EN_DIR / fname).read_bytes().decode("utf-8")
    en_title, ru_title = TITLE_MAP[fname]
    text = en
    # title + both H1 (full-line string unique to title/H1)
    if en_title != ru_title:
        text = text.replace(en_title, ru_title)
    for k, v in DATE_MAP.items():
        text = text.replace(k, v)
    for k, v in PROSE:
        text = text.replace(k, v)
    # table rows: only inside the metrics table, leave separator alone
    out_lines = []
    in_table = False
    for line in text.split("\n"):
        if line.startswith("## Доступные метрики"):
            in_table = True
            out_lines.append(line)
            continue
        if in_table and line.startswith("|") and "---" not in line:
            out_lines.append(tr_table_row(line, fname))
        else:
            out_lines.append(line)
    result = "\n".join(out_lines)
    out_path = RU_DIR / fname
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(result.encode("utf-8"))
    return en, result


def main():
    n_lines_ok = 0
    for fname in TITLE_MAP:
        en, ru = build_one(fname)
        en_n, ru_n = en.count("\n"), ru.count("\n")
        status = "OK" if en_n == ru_n else f"LINE MISMATCH {en_n} != {ru_n}"
        if en_n == ru_n:
            n_lines_ok += 1
        print(f"{status:>20}  {fname}  ({ru_n + 1} lines)")
    print(f"\nline-parity OK: {n_lines_ok}/{len(TITLE_MAP)}")
    if warnings:
        print("\n=== WARNINGS ===")
        for w in warnings:
            print(" ", w)
    else:
        print("no warnings")


if __name__ == "__main__":
    main()
