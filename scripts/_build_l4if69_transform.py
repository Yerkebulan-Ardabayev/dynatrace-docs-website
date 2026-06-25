# -*- coding: utf-8 -*-
from _otel_canon import S, SUB, build_one, qa_one

TT_LEARN = "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry."
RU_LEARN = "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry."
TT_OTLP = "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."
RU_OTLP = "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."

TRANS = {
    # ONLY lines unique to this file (lines already in S resolve automatically)
    "title: Transform and filter data with the OTel Collector": "title: Преобразование и фильтрация данных с помощью OTel Collector",
    "# Transform and filter data with the OTel Collector": "# Преобразование и фильтрация данных с помощью OTel Collector",
    "* 4-min read": "* Чтение: 4 мин",
    "* Published Aug 19, 2024": "* Опубликовано 19 августа 2024 г.",
    "The following configuration example shows how to configure a Collector instance to transform and manipulate OTLP requests, before forwarding them to Dynatrace.": "В следующем примере конфигурации показано, как настроить экземпляр Collector для преобразования OTLP-запросов и манипуляций с ними перед их пересылкой в Dynatrace.",
    "Using the processors shown in this example (`filter` and `transform`), it is possible to streamline requests before sending them to Dynatrace and omit data possibly irrelevant to your use case, and to reduce billing costs.": "С помощью processor, показанных в этом примере (`filter` и `transform`), можно упорядочить запросы перед их отправкой в Dynatrace, опустить данные, возможно нерелевантные для вашего сценария использования, и сократить расходы на биллинг.",
    # prerequisites (unique to transform/filter)
    "* One of the following Collector distributions with the [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) and [filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor) processors": "* Один из следующих дистрибутивов Collector с processor [transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) и [filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor)",
    '+ The [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
    % TT_LEARN: '+ [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "%s")'
    % RU_LEARN,
    '+ OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % TT_LEARN: '+ OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "%s")'
    % RU_LEARN,
    '+ A [custom Builder version](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % TT_LEARN: '+ [пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "%s")'
    % RU_LEARN,
    '* The [API URL](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") of your Dynatrace environment'
    % TT_OTLP: '* [URL API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "%s") вашей среды Dynatrace'
    % RU_OTLP,
    '* An [API token](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") with the relevant access scope'
    % TT_OTLP: '* [API-токен](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "%s") с соответствующей областью доступа'
    % RU_OTLP,
    # components
    "### Receiver": "### Receiver",
    "Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.": "В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector.",
    "This is for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).": "Это сделано в демонстрационных целях. Здесь можно указать любой другой допустимый receiver (например, `zipkin`).",
    "### Processor": "### Processor",
    "#### Transform": "#### Transform",
    "Under `processors`, we specify the [`transform` processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) with a set of different attribute modification statements. `context` indicates the scope to which the statements should apply (here, `resource` for resource attributes, `span` for span attributes, and `metric` for metrics).": "В разделе `processors` мы указываем [processor `transform`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/transformprocessor) с набором различных инструкций изменения атрибутов. `context` указывает область, к которой должны применяться инструкции (здесь `resource` для атрибутов ресурса, `span` для атрибутов спана и `metric` для метрик).",
    "See the [OpenTelemetry documentation of the transform processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md) for more details on the individual configuration options.": "Подробнее об отдельных параметрах конфигурации см. в [документации OpenTelemetry по processor transform](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/transformprocessor/README.md).",
    "The sample configuration above uses the following statements:": "В приведённой выше примерной конфигурации используются следующие инструкции:",
    "| Statement | Description |": "| Инструкция | Описание |",
    "| --- | --- |": "| --- | --- |",
    "| [`keep_matching_keys`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#keep_matching_keys) | Evaluates the attribute key names and only keeps those, whose names match the given regular expressions of `^(aaa|bbb|ccc).*` for resource attributes and `(^xyz.pqr$)|(^(aaa|bbb|ccc).*)` for span attributes. |": "| [`keep_matching_keys`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#keep_matching_keys) | Оценивает имена ключей атрибутов и сохраняет только те, чьи имена соответствуют заданным регулярным выражениям `^(aaa|bbb|ccc).*` для атрибутов ресурса и `(^xyz.pqr$)|(^(aaa|bbb|ccc).*)` для атрибутов спана. |",
    "| [`set`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#set) | Adds/changes the following two span attributes:  * `svc.marker`, with the static value `purchasing` * `purchase.id`, coverting its value to uppercase, using [`ConvertCase`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#convertcase) |": "| [`set`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#set) | Добавляет/изменяет следующие два атрибута спана:  * `svc.marker` со статическим значением `purchasing` * `purchase.id`, преобразуя его значение в верхний регистр с помощью [`ConvertCase`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#convertcase) |",
    "| [`delete_key`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#delete_key) | Deletes attributes named `message`. |": "| [`delete_key`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#delete_key) | Удаляет атрибуты с именем `message`. |",
    "| [`replace_pattern`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#replace_pattern) | Matches a string against a given regular expression and perform a string substitution on all matching entries.  In our example, we first use it for traces to match the name against the regular expression `^.*(DataSubmission-\\d+).*$` and replace its content with the first capture group (`$$1`) of our expression. This essentially means, we search strings for `DataSubmission` suffixed by a number and — if found — only keep the value of the found match.  We also use the function for metrics with the regular expression `(.*)_bad$`, to change the `_bad` suffix to `_invalid`. |": "| [`replace_pattern`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#replace_pattern) | Сопоставляет строку с заданным регулярным выражением и выполняет подстановку строки для всех совпадающих записей.  В нашем примере мы сначала используем её для трассировок, чтобы сопоставить имя с регулярным выражением `^.*(DataSubmission-\\d+).*$` и заменить его содержимое первой группой захвата (`$$1`) нашего выражения. По сути это означает, что мы ищем в строках `DataSubmission` с последующим числом и, если оно найдено, сохраняем только значение найденного совпадения.  Мы также используем эту функцию для метрик с регулярным выражением `(.*)_bad$`, чтобы изменить суффикс `_bad` на `_invalid`. |",
    "#### Filter": "#### Filter",
    "In addition, we also configure an instance of the [`filter` processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor), to filter signal based on the following criteria:": "Кроме того, мы также настраиваем экземпляр [processor `filter`](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.151.0/processor/filterprocessor) для фильтрации сигнала по следующим критериям:",
    "| Signal | Description |": "| Сигнал | Описание |",
    "| Traces | Uses [`IsMatch`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#ismatch) to match the name of resource attributes against the regular expression `^my-pod-name.*`, dropping spans with attributes whose names start with `my-pod-name`. |": "| Traces | Использует [`IsMatch`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/pkg/ottl/ottlfuncs/README.md#ismatch) для сопоставления имени атрибутов ресурса с регулярным выражением `^my-pod-name.*`, отбрасывая спаны с атрибутами, имена которых начинаются с `my-pod-name`. |",
    "| Metrics | Uses [`HasAttrKeyOnDatapoint`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/filterprocessor/README.md#HasAttrKeyOnDatapoint) to evalute if datapoints have attributes with the name `bad.metric`. |": "| Metrics | Использует [`HasAttrKeyOnDatapoint`](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/filterprocessor/README.md#HasAttrKeyOnDatapoint) для оценки того, есть ли у точек данных атрибуты с именем `bad.metric`. |",
    "| Logs | Uses a strict string match of the resource attribute `service.name` against the strings `service1` and `service2`. |": "| Logs | Использует строгое строковое сопоставление атрибута ресурса `service.name` со строками `service1` и `service2`. |",
    "See the [OpenTelemetry documentation of the filter processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/filterprocessor/README.md) for more details on the individual configuration options.": "Подробнее об отдельных параметрах конфигурации см. в [документации OpenTelemetry по processor filter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.151.0/processor/filterprocessor/README.md).",
    "### Exporter": "### Exporter",
    "### Service pipeline": "### Сервисный конвейер",
    "Under `service`, we assemble our receiver, processor, and exporter objects into a traces pipeline, which accepts OTLP traces on the configured endpoints and transforms trace attributes according to the configured rules, before forwarding everything to Dynatrace using the exporter.": "В разделе `service` мы собираем наши объекты receiver, processor и exporter в конвейер трассировок, который принимает трассировки OTLP на настроенных эндпоинтах и преобразует атрибуты трассировок согласно настроенным правилам перед пересылкой всего в Dynatrace с помощью exporter.",
    **S,
}
PASS = {"### Receivers", "### Processors", "### Exporters"}
if __name__ == "__main__":
    build_one(SUB, "transform.md", TRANS, PASS)
    qa_one(SUB, "transform.md")
