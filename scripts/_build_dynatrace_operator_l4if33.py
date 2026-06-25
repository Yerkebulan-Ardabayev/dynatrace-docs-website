# -*- coding: utf-8 -*-
"""L4-IF.33: 1:1 line-map builder for setup-on-k8s/how-it-works/components/dynatrace-operator.md
EN lines not in TRANS are copied byte-for-byte (blanks, code blocks, frontmatter source/scraped).
Guarantees line-parity + byte-identical YAML code blocks + exact URLs.
"""

import os

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
EN = os.path.join(
    BASE,
    "managed",
    "ingest-from",
    "setup-on-k8s",
    "how-it-works",
    "components",
    "dynatrace-operator.md",
)
RU = os.path.join(
    BASE,
    "managed-ru",
    "ingest-from",
    "setup-on-k8s",
    "how-it-works",
    "components",
    "dynatrace-operator.md",
)

TIP_PARAMS = (
    "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."
)
TIP_EDGE = "Ваш выбор недоступен в Dynatrace Managed."
TIP_SEC = (
    "Эта страница содержит обзор компонентов Dynatrace, их настроек по умолчанию "
    "и необходимых им разрешений"
)
TIP_NET = "Требования к сетевому трафику для компонентов Dynatrace Operator в кластере Kubernetes."
TIP_STOR = (
    "Полный обзор требований к хранилищу для различных режимов развёртывания "
    "Dynatrace Operator в окружениях Kubernetes"
)

# line number (1-based) -> Russian translation
TRANS = {
    2: "title: Dynatrace Operator",
    7: "# Dynatrace Operator",
    9: "# Dynatrace Operator",
    11: "* Чтение: 6 мин",
    12: "* Обновлено 5 сентября 2025 г.",
    14: "## Operator",
    16: (
        "Dynatrace Operator управляет автоматическим развёртыванием, настройкой и жизненным циклом "
        "компонентов Dynatrace. Он использует custom resources типа "
        '[DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "%s") и '
        '[EdgeConnect](/managed/upgrade/unavailable-in-managed "%s").'
        % (TIP_PARAMS, TIP_EDGE)
    ),
    18: "Окна обновления в настоящее время не применяются в окружениях Kubernetes.",
    20: (
        "Функциональность Dynatrace Operator привязана к custom resources. Эти ресурсы определяют, "
        "какие функции включены. Когда создаётся custom resource, Dynatrace Operator запускает "
        "начальное согласование, чтобы обеспечить достижение желаемого состояния. Процесс согласования "
        "регулярно обнаруживает изменения в кластере и соответствующим образом корректирует состояние. "
        "Частота согласования снижается после первоначального развёртывания, так как обычно вносится "
        "меньше изменений."
    ),
    22: (
        "При запуске Dynatrace Operator регистрирует [вебхук](#webhook) в Kubernetes API. Во время "
        "каждого цикла согласования Dynatrace Operator проверяет изменения в custom resources, чтобы:"
    ),
    24: "* Обновить статус custom resources",
    25: "* Убедиться, что первоначальный запуск управляемых компонентов соответствует требованиям",
    26: "* Управлять рабочими нагрузками",
    27: "* Зарегистрировать компоненты на сервере Dynatrace",
    29: "Эта функциональность ограничена namespace, в котором развёрнут Dynatrace Operator.",
    31: "Namespace, мониторируемые Dynatrace Operator, должны быть настроены следующим образом:",
    33: "* Маркируйте namespace в соответствии с `namespaceSelector`, чтобы вебхук мог мутировать Pod.",
    34: "* Убедитесь, что предварительные условия для инъекции выполнены в namespace с внедрением.",
    36: "### Требования к ресурсам",
    38: "Конфигурация по умолчанию:",
    40: "* 1 реплика на кластер",
    42: (
        "Одной реплики Dynatrace Operator, как правило, достаточно благодаря механизму выбора лидера. "
        "Дополнительные реплики активируются только тогда, когда текущий лидер завершает работу и "
        "избирается новый."
    ),
    44: (
        "Контейнер Dynatrace Operator имеет предопределённые запросы и лимиты CPU и памяти. Чтобы "
        "настроить эти значения при развёртывании с помощью Helm, измените файл `values.yaml`."
    ),
    46: "Настройка ресурсов с помощью Helm",
    76: "### Разрешения и привилегии",
    78: (
        "Полный список ресурсов, к которым обращается Dynatrace Operator, доступен в "
        '[документации по безопасности](/managed/ingest-from/setup-on-k8s/reference/security "%s"). '
        "Сетевой трафик и схемы описаны в "
        '[документации по сетевому трафику](/managed/ingest-from/setup-on-k8s/reference/network "%s").'
        % (TIP_SEC, TIP_NET)
    ),
    80: "## Webhook",
    82: (
        "Вебхук Dynatrace изменяет определения Pod, чтобы внедрять code modules Dynatrace для "
        "Application observability. Он также проверяет определения DynaKube и конвертирует DynaKube "
        "с устаревшими версиями API."
    ),
    84: (
        "Конфигурации вебхука управляются Dynatrace Operator и периодически обновляются. Эти обновления "
        "гарантируют, что Kubernetes API сможет продолжать взаимодействовать с вебхуком."
    ),
    86: "### Ключевые функции",
    88: (
        "* Мутация Pod: вебхук мутирует Pod, изменяя их определения для включения необходимых "
        "метаданных для Application observability."
    ),
    90: (
        "  + Присоединяет init-контейнер для загрузки (если CSI driver не используется) и настройки "
        "code modules при запуске Pod."
    ),
    91: "  + Присоединяет тома CSI, если они настроены, чтобы CSI driver мог управлять созданием томов.",
    92: "  + Изменяет определения Pod для обогащения метаданными.",
    93: (
        "* Мутация namespace: вебхук мутирует namespace, чтобы включить мониторинг Pod в этих "
        "namespace."
    ),
    95: "  + Добавляет метки в namespace, чтобы вебхук мог отслеживать события `CREATE` для Pod.",
    97: (
        "  Конфигурации вебхука поддерживают только статический селектор namespace. Необходимая метка "
        "добавляется во вновь созданные namespace."
    ),
    98: "* Проверка конфигурации",
    100: (
        "  + Проверяет, что custom resources, такие как DynaKube, содержат корректную конфигурацию "
        "при создании или обновлении"
    ),
    102: (
        "    - Разная проверка в зависимости от полей: некоторые обязательны, а некоторые должны "
        "соответствовать более специфичным правилам"
    ),
    103: "  + Предоставляет полезные предупреждения и сообщения об ошибках, если проверка не пройдена",
    105: (
        "  Подробнее о каждом поле см. в разделах "
        '[параметры DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "%s") и '
        '[параметры EdgeConnect](/managed/upgrade/unavailable-in-managed "%s")!'
        % (TIP_PARAMS, TIP_EDGE)
    ),
    106: "* Конвертация между версиями",
    108: "  + Обеспечивает совместимость между разными версиями определений custom resource",
    109: (
        "  + Конвертирует более старые версии custom resource в версию хранилища, понятную "
        "Dynatrace Operator"
    ),
    111: "### Требования к ресурсам",
    113: "Конфигурация по умолчанию:",
    115: "* 2 реплики на кластер (можно масштабировать для повышения доступности)",
    117: (
        "Для контейнера Dynatrace Webhook определены запросы и лимиты по умолчанию. Если требуется "
        "задать другие запросы или лимиты ресурсов, это можно сделать при развёртывании "
        "Dynatrace Operator с помощью Helm."
    ),
    119: "Настройка ресурсов с помощью Helm",
    121: "Чтобы задать лимиты ресурсов, измените `values.yaml`. См. конфигурацию по умолчанию ниже.",
    151: "### Разрешения и привилегии",
    153: (
        "Полный список ресурсов, к которым обращается вебхук, можно найти в разделе "
        '[безопасность Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/security "%s").'
        % TIP_SEC
    ),
    154: (
        "Входящий и исходящий трафик описан в разделе "
        '[сетевой трафик](/managed/ingest-from/setup-on-k8s/reference/network "%s").'
        % TIP_NET
    ),
    156: "## CSI driver",
    158: (
        "Dynatrace Operator CSI driver предоставляет code modules Dynatrace для Pod приложений, "
        "минимизируя при этом использование хранилища и нагрузку на окружение Dynatrace. Кроме того, "
        "он предоставляет хранилище томов с возможностью записи для OneAgent, используя "
        "[эфемерные локальные тома](https://dt-url.net/j9027w2)."
    ),
    160: (
        "* Для конфигураций `applicationMonitoring` он предоставляет необходимый двоичный файл OneAgent "
        "для мониторинга приложений на Pod каждого узла в виде монтирования **только для чтения**."
    ),
    161: (
        "* Для конфигураций `hostMonitoring` он предоставляет папку с возможностью записи для "
        "конфигураций OneAgent, когда используется файловая система хоста только для чтения."
    ),
    162: "* Для `cloudNativeFullStack` он предоставляет оба указанных выше варианта.",
    164: (
        "Минимизирует загрузки, загружая code modules один раз на узел и сохраняя их в файловой "
        "системе узла."
    ),
    166: (
        "* С CSI driver внедрение 100 Pod, распределённых по трём узлам, приведёт всего к 3 загрузкам "
        "Code Module."
    ),
    167: (
        "* Без CSI driver каждый Pod должен загружать собственные code modules, поэтому внедрение "
        "100 Pod приведёт к загрузке 100 code modules."
    ),
    169: (
        "Минимизирует использование хранилища, сохраняя code modules в файловой системе узла и создавая "
        "монтирование [OverlayFs](https://dt-url.net/hf036vi) для каждого Pod с внедрением."
    ),
    171: (
        "* С CSI driver внедрение 100 Pod, распределённых по трём узлам, приведёт к хранению всего "
        "3 code modules."
    ),
    172: (
        "* Без CSI driver каждый Pod хранит собственный Code Module, поэтому внедрение 100 Pod приведёт "
        "к хранению 100 code modules."
    ),
    174: (
        "Подробнее о том, где хранятся файлы и логи OneAgent на узлах Kubernetes (с CSI driver и без "
        "него), см. в разделе "
        '[Требования к хранилищу](/managed/ingest-from/setup-on-k8s/reference/storage "%s").'
        % TIP_STOR
    ),
    176: "### Требования к ресурсам",
    178: "Конфигурация по умолчанию:",
    180: "* 1 реплика на узел (развёртывается через DaemonSet)",
    182: (
        "Provisioner CSI driver не имеет предопределённых лимитов ресурсов. Однако, если требуется "
        "задать лимиты ресурсов или изменить их для других контейнеров CSI driver, это можно сделать "
        "при развёртывании Dynatrace Operator с помощью Helm."
    ),
    184: "Настройка ресурсов с помощью Helm",
    186: (
        "Чтобы задать лимиты ресурсов для контейнера `provisioner`, измените `values.yaml`. См. пример "
        "конфигурации ниже."
    ),
    188: (
        "* Увеличьте CPU, чтобы ускорить распаковку и установку code modules (важно для быстрого "
        "запуска и инициализации узла)"
    ),
    189: "* Увеличение памяти не влияет на производительность",
    255: "### Разрешения и привилегии",
    257: (
        "Dynatrace Operator CSI driver требует повышенных разрешений для создания монтирований "
        "в хост-системе и управления ими. В частности, разрешение "
        "[mountPropagation: Bidirectional](https://dt-url.net/90236h3) необходимо для тома, в котором "
        "CSI driver хранит code modules. Это разрешение доступно только для привилегированных "
        "контейнеров."
    ),
    259: (
        "Полный список ресурсов, к которым обращается CSI driver, можно найти в "
        '[документации по безопасности](/managed/ingest-from/setup-on-k8s/reference/security "%s").'
        % TIP_SEC
    ),
    261: (
        "Входящий и исходящий трафик описан в "
        '[документации по сетевому трафику](/managed/ingest-from/setup-on-k8s/reference/network "%s").'
        % TIP_NET
    ),
}

with open(EN, "r", encoding="utf-8", newline="") as f:
    # strip CR so output is pure LF even if working-tree EN is CRLF (autocrlf)
    en_lines = f.read().replace("\r\n", "\n").replace("\r", "\n").split("\n")

out = []
for i, line in enumerate(en_lines, start=1):
    out.append(TRANS[i] if i in TRANS else line)

# join with LF; EN had no trailing newline (last byte is content)
text = "\n".join(out)
with open(RU, "w", encoding="utf-8", newline="") as f:
    f.write(text)

print("EN lines:", len(en_lines), "RU lines:", len(out), "translated:", len(TRANS))
print("wrote", RU)
