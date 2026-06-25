# -*- coding: utf-8 -*-
from _otel_canon import S, SUB, build_one, qa_one

TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."
TT_LEARN = "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."
RU_LEARN = "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."

TRANS = {
    # title / H1 (appears twice)
    "title: Use journald to ingest systemd journal logs with the OTel Collector": "title: Использование journald для приёма логов журнала systemd с помощью OTel Collector",
    "# Use journald to ingest systemd journal logs with the OTel Collector": "# Использование journald для приёма логов журнала systemd с помощью OTel Collector",
    # metadata
    "* 4-min read": "* Чтение: 4 мин",
    "* Published Mar 12, 2026": "* Опубликовано 12 марта 2026 г.",
    # intro
    "The journald receiver reads log entries from the [systemd journal](https://wiki.archlinux.org/title/Systemd/Journal) by invoking `journalctl` as a subprocess and streaming its output into the OTel Collector pipeline.": "Receiver journald читает записи логов из [журнала systemd](https://wiki.archlinux.org/title/Systemd/Journal), вызывая `journalctl` как подпроцесс и передавая его вывод потоком в конвейер OTel Collector.",
    "Each journal entry becomes an OTLP log record where journal fields are mapped to log attributes.": "Каждая запись журнала становится записью лога OTLP, в которой поля журнала сопоставляются с атрибутами лога.",
    "You can use [operators](#operators) to rename or transform these attributes to align with OpenTelemetry semantic conventions.": "Чтобы переименовать или преобразовать эти атрибуты в соответствии с семантическими соглашениями OpenTelemetry, можно использовать [операторы](#operators).",
    "Use the journald receiver when:": "Используйте receiver journald, когда:",
    "* Your Linux-based services write logs to the systemd journal rather than to separate log files.": "* Ваши сервисы на базе Linux записывают логи в журнал systemd, а не в отдельные файлы логов.",
    "* You want to centralize host-level system service logs (for example, `ssh`, `kubelet`, or `docker`) in Dynatrace without managing additional log file paths.": "* Требуется централизовать логи системных сервисов уровня хоста (например, `ssh`, `kubelet` или `docker`) в Dynatrace без управления дополнительными путями к файлам логов.",
    "* You need to filter ingestion by specific systemd units and priority levels to control data volume.": "* Требуется фильтровать приём по конкретным юнитам systemd и уровням приоритета для контроля объёма данных.",
    # prerequisites (unique: journald receiver bullet + collector-distro anchor variants)
    "* One of the following Collector distributions with the [journald receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver).": "* Один из следующих дистрибутивов Collector с [receiver journald](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver).",
    '+ [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#collector-distro "%s")'
    % TT_LEARN: '+ [Dynatrace Collector](/managed/ingest-from/opentelemetry/collector#collector-distro "%s")'
    % RU_LEARN,
    '+ [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % TT_LEARN: '+ [OpenTelemetry Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % RU_LEARN,
    '* The [Dynatrace API endpoint URL](/managed/ingest-from/opentelemetry/otlp-api "%s") to which the data should be exported.'
    % TT_OTLP: '* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "%s"), на который должны экспортироваться данные.'
    % RU_OTLP,
    "* Linux OS on the host or container where the Collector runs.": "* ОС Linux на хосте или в контейнере, где работает Collector.",
    "* The `journalctl` binary needs to be present on the host or in the container where the Collector runs.": "* Двоичный файл `journalctl` должен присутствовать на хосте или в контейнере, где работает Collector.",
    "This is because the receiver relies on `journalctl` for all journal access.": "Это связано с тем, что receiver полагается на `journalctl` для всего доступа к журналу.",
    "+ For container deployments, use an image that includes `systemd` and mount the journal directory from the host.": "+ Для развёртываний в контейнерах используйте образ, включающий `systemd`, и монтируйте каталог журнала с хоста.",
    "+ For Kubernetes-specific requirements, see [Kubernetes deployment](#kubernetes-deployment).": "+ Сведения о требованиях, специфичных для Kubernetes, см. в разделе [Развёртывание в Kubernetes](#kubernetes-deployment).",
    "* The Collector process needs permission to read the systemd journal via `journalctl`.": "* Процессу Collector требуется разрешение на чтение журнала systemd через `journalctl`.",
    "+ On a Linux OS host, add the user running the Collector to the `systemd-journal` group to grant read access to the journal.": "+ На хосте с ОС Linux добавьте пользователя, под которым работает Collector, в группу `systemd-journal`, чтобы предоставить доступ к журналу на чтение.",
    "The Collector doesn't need to run as root.": "Collector не обязательно запускать от имени root.",
    "+ For Kubernetes, the Collector must run as root because container isolation prevents group-based journal access.": "+ В Kubernetes Collector должен работать от имени root, поскольку изоляция контейнеров препятствует доступу к журналу на основе групп.",
    "For more information, see [Kubernetes deployment](#kubernetes-deployment).": "Дополнительные сведения см. в разделе [Развёртывание в Kubernetes](#kubernetes-deployment).",
    # demo configuration
    "The following configuration example shows how to:": "В следующем примере конфигурации показано, как:",
    "* Configure a Collector instance to read logs from specific systemd units.": "* Настроить экземпляр Collector для чтения логов из конкретных юнитов systemd.",
    "* Map journald fields to OpenTelemetry semantic conventions.": "* Сопоставить поля journald с семантическими соглашениями OpenTelemetry.",
    "* Send the entries to Dynatrace.": "* Отправить записи в Dynatrace.",
    # receivers section
    "Under `receivers`, we configure the `journald` receiver with the following parameters.": "В разделе `receivers` мы настраиваем receiver `journald` со следующими параметрами.",
    "#### Filtering by systemd unit": "#### Фильтрация по юниту systemd",
    "The `units` parameter restricts ingestion to entries belonging to the listed systemd units.": "Параметр `units` ограничивает приём записями, принадлежащими перечисленным юнитам systemd.",
    "Remove it to collect logs from all units on the host.": "Удалите его, чтобы собирать логи со всех юнитов на хосте.",
    "For more granular filtering use the `matches` parameter instead.": "Для более детальной фильтрации используйте вместо него параметр `matches`.",
    "For example, you can combine unit names with specific journal field values.": "Например, можно сочетать имена юнитов с конкретными значениями полей журнала.",
    "See the [journald receiver documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver#configuration) for a full parameter reference, filtering examples, and performance considerations for `start_at` and `priority`.": "Полный справочник параметров, примеры фильтрации и соображения по производительности для `start_at` и `priority` см. в [документации по receiver journald](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver#configuration).",
    "#### Operators": "#### Операторы",
    "The `operators` parameter accepts an array of [stanza operators](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/pkg/stanza/docs/operators/README.md) applied to each log entry as it enters the pipeline.": "Параметр `operators` принимает массив [операторов stanza](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/pkg/stanza/docs/operators/README.md), применяемых к каждой записи лога при её поступлении в конвейер.",
    "In this configuration, we use [`move` operators](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/pkg/stanza/docs/operators/move.md) to rename specific journal fields and promote `_EXE` to a log attribute aligned with the [OpenTelemetry process semantic conventions](https://opentelemetry.io/docs/specs/semconv/registry/attributes/process/).": "В этой конфигурации мы используем [операторы `move`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/pkg/stanza/docs/operators/move.md) для переименования конкретных полей журнала и повышения `_EXE` до атрибута лога, согласованного с [семантическими соглашениями OpenTelemetry для процессов](https://opentelemetry.io/docs/specs/semconv/registry/attributes/process/).",
    "* `body._PID` is renamed to `body.pid`.": "* `body._PID` переименовывается в `body.pid`.",
    '* `body._EXE` is renamed to `attributes["process.executable.name"]`.': '* `body._EXE` переименовывается в `attributes["process.executable.name"]`.',
    "* `body.MESSAGE` is renamed to `body.message`.": "* `body.MESSAGE` переименовывается в `body.message`.",
    # exporters: DT_ENDPOINT / DT_API_TOKEN bullets unique (trailing period)
    '* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).'
    % TT_OTLP: '* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`).'
    % RU_OTLP,
    '* `DT_API_TOKEN` contains the [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s").'
    % TT_OTLP: '* `DT_API_TOKEN` содержит [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s").'
    % RU_OTLP,
    # service pipelines body
    "Under `service`, we assemble the receiver and exporter into a logs pipeline.": "В разделе `service` мы собираем receiver и exporter в конвейер логов.",
    "The pipeline reads journal entries, applies the operator-based field transformations, and ingests the results into Dynatrace.": "Конвейер читает записи журнала, применяет преобразования полей на основе операторов и принимает результаты в Dynatrace.",
    # Kubernetes considerations
    "## Considerations for Kubernetes deployments": "## Соображения для развёртываний в Kubernetes",
    "When running the journald receiver in Kubernetes, deploy the Collector as a DaemonSet so that one Collector pod runs on every node.": "При запуске receiver journald в Kubernetes развёртывайте Collector как DaemonSet, чтобы на каждом узле работал один под Collector.",
    "A Deployment is unsuitable because each pod can only access the systemd journal of the node it is scheduled on.": "Deployment не подходит, поскольку каждый под имеет доступ только к журналу systemd того узла, на который он назначен.",
    "Scaling a Deployment to multiple replicas can cause duplicate log ingestion when more than one replica lands on the same node.": "Масштабирование Deployment до нескольких реплик может привести к дублированию приёма логов, когда несколько реплик попадают на один и тот же узел.",
    "A DaemonSet ensures complete cluster-wide log coverage and guarantees exactly one privileged, host-access pod per node.": "DaemonSet обеспечивает полный охват логов в масштабе всего кластера и гарантирует ровно один привилегированный под с доступом к хосту на узел.",
    "This limits the security footprint of running the Collector as root.": "Это ограничивает влияние на безопасность при запуске Collector от имени root.",
    "### Image requirements": "### Требования к образу",
    "As said in [Prerequisites](#prerequisites), the Collector container must include `journalctl` to access the systemd journal.": "Как сказано в разделе [Предварительные требования](#prerequisites), контейнер Collector должен включать `journalctl` для доступа к журналу systemd.",
    "For more information, see the [OTel upstream documentation](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver/examples/container).": "Дополнительные сведения см. в [вышестоящей документации OTel](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/receiver/journaldreceiver/examples/container).",
    "### Security context": "### Контекст безопасности",
    "Reading from the systemd journal requires specific Linux capabilities.": "Чтение из журнала systemd требует определённых возможностей Linux.",
    "Apply the following `securityContext` (shown in the code block below) to the Collector container.": "Примените к контейнеру Collector следующий `securityContext` (показан в блоке кода ниже).",
    "The table then describes the purpose of relevant attributes within the security context definition.": "Затем в таблице описывается назначение соответствующих атрибутов в определении контекста безопасности.",
    # security context table
    "| Setting | Reason |": "| Параметр | Причина |",
    "| `allowPrivilegeEscalation: false` | Prevents the process from gaining additional privileges beyond the declared capabilities. |": "| `allowPrivilegeEscalation: false` | Не позволяет процессу получать дополнительные привилегии сверх объявленных возможностей. |",
    "| `readOnlyRootFilesystem: true` | Makes the container root filesystem read-only to reduce the attack surface. |": "| `readOnlyRootFilesystem: true` | Делает корневую файловую систему контейнера доступной только для чтения, чтобы уменьшить поверхность атаки. |",
    "| `seccompProfile: RuntimeDefault` | Applies the default seccomp profile to restrict permitted system calls. |": "| `seccompProfile: RuntimeDefault` | Применяет стандартный профиль seccomp для ограничения разрешённых системных вызовов. |",
    "| `runAsUser: 0` | The Collector process runs as root to access the journal socket.  When you run as root, you increase the risk of granting root-level access to the node. For more information, see [Run as root](#collector-root). |": "| `runAsUser: 0` | Процесс Collector работает от имени root для доступа к сокету журнала.  При запуске от имени root повышается риск предоставления доступа к узлу на уровне root. Дополнительные сведения см. в разделе [Запуск от имени root](#collector-root). |",
    "| `DAC_READ_SEARCH` | Bypasses file-system permission checks when reading journal files. |": "| `DAC_READ_SEARCH` | Обходит проверки разрешений файловой системы при чтении файлов журнала. |",
    "| `SYS_PTRACE` | Required for process introspection used by the journald receiver. |": "| `SYS_PTRACE` | Требуется для интроспекции процессов, используемой receiver journald. |",
    # run as root
    "### Run as root": "### Запуск от имени root",
    "The journald receiver does not require that you run as root, but it is the simplest way to obtain the necessary Linux capabilities in a containerized environment.": "Receiver journald не требует запуска от имени root, но это самый простой способ получить необходимые возможности Linux в контейнеризованной среде.",
    "If your Collector runs as root, avoid co-locating network-exposed receivers (such as `otlp` bound to `0.0.0.0`) in the same instance.": "Если ваш Collector работает от имени root, избегайте размещения в том же экземпляре доступных по сети receiver (таких как `otlp`, привязанный к `0.0.0.0`).",
    "A remotely exploitable vulnerability in a network receiver would grant root-level access to the node.": "Уязвимость в сетевом receiver, эксплуатируемая удалённо, предоставила бы доступ к узлу на уровне root.",
    "To reduce risk, use a dedicated Collector instance solely for journald log collection.": "Чтобы снизить риск, используйте выделенный экземпляр Collector исключительно для сбора логов journald.",
    "If you must include additional receivers in the same instance, bind them to `127.0.0.1` (loopback) rather than `0.0.0.0` to prevent external access.": "Если необходимо включить в тот же экземпляр дополнительные receiver, привязывайте их к `127.0.0.1` (loopback), а не к `0.0.0.0`, чтобы предотвратить внешний доступ.",
    # volume mounts
    "### Volume mounts": "### Монтирование томов",
    "Mount the host's journal directory into the container as read-only.": "Смонтируйте каталог журнала хоста в контейнер в режиме только для чтения.",
    "Set `directory: /run/log/journal` in the `journald` receiver configuration to match this mount path.": "Задайте `directory: /run/log/journal` в конфигурации receiver `journald`, чтобы он соответствовал этому пути монтирования.",
    "* On traditional (non-containerized) Linux systems the persistent journal is stored at `/var/log/journal`.": "* В традиционных (неконтейнеризованных) системах Linux постоянный журнал хранится в `/var/log/journal`.",
    "* In containerized Linux environments the journal is typically written to `/run/log/journal`.": "* В контейнеризованных средах Linux журнал обычно записывается в `/run/log/journal`.",
    "This is ephemeral, in-memory storage.": "Это эфемерное хранилище в памяти.",
    # related topics (unique bullets: k8s-podlogs + transform)
    '* [Ingest Kubernetes pod logs with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-podlogs "Configure the OpenTelemetry Collector to ingest Kubernetes pod log files into Dynatrace.")': '* [Приём логов подов Kubernetes с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-podlogs "Настройте OpenTelemetry Collector для приёма файлов логов подов Kubernetes в Dynatrace.")',
    '* [Transform and filter data with the OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/transform "Configure the OpenTelemetry Collector to add, transform, and drop OpenTelemetry data.")': '* [Преобразование и фильтрация данных с помощью OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/transform "Настройте OpenTelemetry Collector для добавления, преобразования и отбрасывания данных OpenTelemetry.")',
    **S,
}

PASS = {"### Receivers", "### Exporters", "| --- | --- |"}

if __name__ == "__main__":
    build_one(SUB, "journald.md", TRANS, PASS)
    qa_one(SUB, "journald.md")
