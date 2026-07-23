---
title: Обогащение принятых данных полями, специфичными для Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-data
---

# Обогащение принятых данных полями, специфичными для Dynatrace

# Обогащение принятых данных полями, специфичными для Dynatrace

* Чтение: 4 мин.
* Опубликовано 26 апр. 2021

В отличие от автоматического приёма данных через OneAgent, данные, отправленные напрямую в ActiveGate (например, через ingest APIs), не обогащаются автоматически информацией, связанной с хостом. Это может повлечь дополнительные расходы, поскольку возможные включённые [DDU-квоты](/managed/license/classic-licensing/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU).") не учитываются.

Различные варианты развёртывания Dynatrace предоставляют несколько файлов свойств в стиле Java и JSON-файлов с наборами атрибутов, которые можно использовать для обогащения запросов к Dynatrace и обеспечения сопоставления данных с инфраструктурой.

## Каталог обогащения

Dynatrace использует следующие каталоги для хранения файлов `.json` и `.properties` с данными обогащения:

* На Unix: `/var/lib/dynatrace/enrichment`
* На Windows: `%ProgramData%\dynatrace\enrichment`

## Dynatrace OneAgent

Стандартная установка OneAgent предоставляет следующие файлы с характеристиками хоста в [каталоге обогащения](#enrichment-directory):

* `dt_host_metadata.json`
* `dt_host_metadata.properties`

Оба файла содержат одинаковый набор атрибутов ресурсов уровня хоста, которые OneAgent использует для обогащения артефактов мониторинга данного хоста. Это также включает теги и свойства в формате «ключ-значение», установленные через [oneagentctl](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Узнайте, как задавать теги и дополнительные свойства для отслеживаемого хоста.") или через [Remote configuration management](/managed/ingest-from/bulk-configuration "Выполните настройку OneAgent и ActiveGate на хостах со страницы статуса развёртывания или в масштабе с помощью Dynatrace API.").

Если телеметрические данные передаются по каналам, отличным от OneAgent (например, через OpenTelemetry), необходимо вручную обогатить их этими атрибутами для корректного сопоставления с хостом.

Пример загрузки JSON-файла см. в разделе [Пример на Python](#python-example) ниже.

### Виртуальные файлы OneAgent

Когда OneAgent отслеживает приложение, оно также может обращаться к следующим виртуальным файлам:

* `dt_metadata_e617c525669e072eebe3d0f08212e8f2.json`
* `dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties`

Эти файлы не привязаны к каталогу обогащения и физически не существуют в файловой системе, однако предоставляются инструментацией OneAgent. Оба файла возвращают одни и те же данные, а расширение файла (`.json`/`.properties`) определяет лишь формат вывода.

В контексте [Dynatrace Operator](#operator-enrichment-directory) виртуальный файл также содержит атрибуты файлов `dt_metadata.{json,properties}`.

#### Как получить доступ к виртуальным файлам

1. Используйте стандартную функцию чтения файлов платформы, чтобы открыть и прочитать один из следующих файлов:

   * `dt_metadata_e617c525669e072eebe3d0f08212e8f2.json`
   * `dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties`

   Выбранное расширение файла важно для шага 4. Нужно использовать только имя файла без указания дополнительного пути.
2. Содержимое файла, это одна строка с абсолютным путём к файлу (считайте его временным значением и не сохраняйте, не кешируйте этот путь для последующего использования).
3. Откройте файл по пути, полученному на предыдущем шаге, и прочитайте всё его содержимое.
4. Формат содержимого, полученного на предыдущем шаге, соответствует расширению файла, выбранному на шаге 1 (свойства в стиле Java или JSON).

Если на шаге 1 возникает ошибка «файл не найден», убедитесь, что приложение инструментировано OneAgent.

#### Ограничения

* Поддерживается для процессов с полным стеком и процессов с глубоким мониторингом только приложения.
* Проверки `stat` и другие проверки `if (exists)` завершаются ошибкой для этих файлов. Для работы механизма эти проверки не требуются.
* Прямое использование `syscalls` для доступа к файлам не поддерживается. Это также означает, что Go-приложения, используемые для приёма метрик, не поддерживаются, если не применяется OneAgent SDK, как описано в разделе [Инструментация Go-приложения с помощью OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/go "Узнайте, как инструментировать Go-приложение с помощью OpenTelemetry и Dynatrace.").

### Пример на Python

В следующем примере показано, как загрузить данные обогащения в виде JSON на Python в Unix.

```
# Initialize dictionary variable



enrich_attrs = dict()



# Iterate over the potential data files and try reading them



for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.json", "/var/lib/dynatrace/enrichment/dt_metadata.json", "/var/lib/dynatrace/enrichment/dt_host_metadata.json"]:



try:



data = ''



with open(name) as f:



data = json.load(f if name.startswith("/var") else open(f.read()))



enrich_attrs.update(data)



except:



pass # An exception indicates the file was not available



# Use enrich_attrs here to enrich your requests to Dynatrace.



# For example, when instrumenting with OpenTelemetry, add the data as resource attributes.
```

Пример инициализирует пустой словарь для импортированных атрибутов, затем перебирает массив имён `.json`-файлов и загружает содержимое каждого файла как JSON-документ, добавляя ключи в словарь. Исключения при работе с файлами означают, что соответствующий файл недоступен, и игнорируются.

## Dynatrace Operator

Когда `metadataEnrichment` включён в DynaKube, Dynatrace Operator добавляет следующие файлы в [каталог обогащения](#enrichment-directory) каждого пода:

* `dt_metadata.json`
* `dt_metadata.properties`

Оба файла содержат одинаковые метаданные Kubernetes в разных форматах. Пример загрузки JSON-файла см. в разделе [Пример на Python](#python-example) выше. При включённом OneAgent эти файлы применяются автоматически; без OneAgent их нужно загрузить и применить вручную.

`metadataEnrichment` включается автоматически (явная настройка DynaKube не требуется) при использовании [OneAgent injection](/managed/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "Подробное описание наблюдаемости полного стека с помощью Dynatrace Operator.") (`cloudNativeFullStack` или `applicationMonitoring`) или [OTLP exporter auto-configuration](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Автоматическая настройка OTLP exporter в приложениях, инструментированных с помощью OpenTelemetry SDKs и Dynatrace Operator.").

Включение metadataEnrichment в DynaKube

Добавьте `metadataEnrichment` в спецификацию DynaKube:

```
spec:



metadataEnrichment:



enabled: true
```

Чтобы ограничить обогащение конкретными пространствами имён, добавьте `namespaceSelector`:

```
spec:



metadataEnrichment:



enabled: true



namespaceSelector:



matchLabels:



team: finance
```

Содержимое файлов обогащения

Оба файла предоставляют следующие атрибуты:

```
{



"k8s.cluster.name": "<cluster-name>",



"k8s.cluster.uid": "<cluster-uid>",



"k8s.namespace.name": "<namespace-name>",



"k8s.node.name": "<node-name>",



"k8s.pod.name": "<pod-name>",



"k8s.pod.uid": "<pod-uid>",



"k8s.container.name": "<container-name>",



"k8s.workload.kind": "<workload-kind>",



"k8s.workload.name": "<workload-name>",



"dt.entity.kubernetes_cluster": "<kubernetes-cluster-id>",



"dt.kubernetes.cluster.id": "<cluster-id>",



"dt.kubernetes.workload.kind": "<workload-kind>",



"dt.kubernetes.workload.name": "<workload-name>"



}
```

Чтобы убедиться в корректной работе обогащения, проверьте `/var/lib/dynatrace/enrichment` внутри инжектированного пода и убедитесь, что оба файла присутствуют.