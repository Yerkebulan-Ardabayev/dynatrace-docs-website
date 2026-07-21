---
title: Концепции распределённой трассировки
source: https://docs.dynatrace.com/managed/observe/application-observability/distributed-traces/concepts
---

# Концепции распределённой трассировки

# Концепции распределённой трассировки

* Пояснение
* 1 минута на чтение
* Обновлено 04 мая 2026 г.

В этой статье описаны основные концепции и терминология распределённой трассировки в Dynatrace.

![Relation between Services and Traces and Spans](https://cdn.bfldr.com/B686QPH3/as/6tgs79c9ngqvpxcq4bw2bt6/Distributed_traces_concepts_-_Light_Mode?auto=webp&format=png&position=1)

Связь между Services, Traces и Spans

### Distributed trace

Distributed trace, это последовательность span'ов, идентифицируемая уникальным trace ID, которая отслеживает путь одного запроса по мере его прохождения через различные сервисы и компоненты распределённой системы. В современной микросервисной среде трасса обычно охватывает несколько сервисов, предоставляя детальное представление о пути запроса и его производительности. Трасса содержит семантически различные атрибуты, которые позволяют интерпретировать и понимать собранные данные, помогая выявлять узкие места, ошибки и проблемы с задержками для эффективного устранения неполадок и оптимизации.

#### Сценарии использования

* Понять, как запросы распространяются через распределённые системы и микросервисы.
* Использовать высококачественные данные, генерируемые распределёнными системами и микросервисами, для анализа запросов.
* Быстро понять, как работает каждый микросервис.
* Использовать [детализацию анализа первопричин Dynatrace Intelligence](/managed/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") для выявления причинно-следственных связей между событиями.

### Span

Span представляет собой отдельную операцию в рамках distributed trace, фиксируя детали пути запроса через несколько сервисов. Каждый span включает такие атрибуты, как имя, временная метка начала, список событий span'а (например, исключения), идентификатор родительского span'а и тип span'а (span kind). Эта информация, **span context**, помогает сопоставить все span'ы и события друг с другом, что позволяет отслеживать и понимать производительность и поведение отдельных операций в распределённой системе.

В рамках трассы, когда активность (*parent span*) завершена, следующая активность переходит к его *child span*. Span без родительского span'а называется *root span* трассы и обозначает начало трассы.

Span context позволяет child span соотноситься с трассой и её родительским span'ом. Поэтому контекст нужно передавать не только внутри сервиса (между разными потоками), но и между сервисами и границами процессов. Обычно это происходит через HTTP-заголовки (например, [W3C trace context](https://www.w3.org/TR/trace-context/)) или через уникальные ID в системах обмена сообщениями. Подробнее о передаче контекста см. [Передача span и trace context в Distributed Traces Classic](/managed/observe/application-observability/distributed-traces/context-propagation "Understand span and trace context propagation in Dynatrace and how to set them up.").

### Атрибут

Атрибуты, это пары «ключ-значение», предоставляющие детали о span'е, запросе или ресурсе, такие как коды ответов, HTTP-методы и URL. С помощью атрибутов можно группировать, запрашивать, находить и анализировать трассы и span'ы.

#### Сценарии использования

Dynatrace использует метаданные атрибутов для следующих целей:

* [Обнаружение и именование сервисов](/managed/observe/application-observability/services/service-detection "Understand the two approaches that Dynatrace uses for service detection.").
* Сбор данных о контексте трассы и связях с другими сущностями для [топологии Smartscape](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment.").
* Связывание данных логов с трассами для [Logs Classic](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment "Learn how you can connect your incoming log data to traces for more precise Dynatrace analysis.").
* Понимание того, как на длительность span'а влияют [тайминги сервиса](/managed/observe/application-observability/services-classic/service-analysis-timing "Find out what each time in service analysis means.") (например, время CPU, сетевое время или просто ожидание других потоков), а также анализ того, какой код выполнялся в контексте span'а.

#### Рекомендации

Если данные трассировки собираются через

* OpenTelemetry, нужно задать [настройки захватываемых атрибутов](/managed/ingest-from/extend-dynatrace/extend-tracing/span-settings "Learn how to configure span settings for OpenTelemetry and OpenTracing.").
* OneAgent, нужно задать [настройки атрибутов запросов](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

### Сервис

Сервисы проходятся distributed trace. На горизонтально масштабируемых сервисах каждый span обрабатывается конкретным **Service Instance**. Сервисы определяются и именуются на основе доступных атрибутов или свойств, собираемых вместе со span'ами.

#### Сценарии использования

* [Сегментация запросов для улучшения деградации времени отклика](/managed/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").

### Сбор данных и передача контекста

Можно интегрировать OpenTelemetry и OneAgent для сбора данных трассировки, таких как статус запроса, время отклика, версии, информация об инфраструктуре и другие релевантные метаданные в виде атрибутов. Контекст трассы, включая уникальный trace ID, затем передаётся между приложениями и микросервисами.

#### Рекомендации

Перед началом работы с распределённой трассировкой нужно понять, чем отличается настройка и сбор данных трассировки между OpenTelemetry и OneAgent. Ниже приведён обзор ключевых различий.

|  | OpenTelemetry | OneAgent |
| --- | --- | --- |
| Настройка | Автоматическая или ручная | Автоматическая |
| Захват данных | Автоматический сбор разрешённых атрибутов span'а. | Автоматический сбор нескольких атрибутов запроса, включая HTTP-метод, URL, коды ответов, топологические данные и детали об используемых технологиях. |
| Контекст | Автоматически или вручную контекстуализированные записи логов, в зависимости от библиотеки инструментирования. | Автоматически контекстуализированные  * Записи логов, создаваемые популярными фреймворками логирования. * Трассы в Smartscape и Dynatrace Intelligence. |

Для начала работы см.

* [Автоматическая настройка с OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Инструментирование с помощью OpenTelemetry](/managed/ingest-from/opentelemetry/getting-started "How to get your OpenTelemetry data into Dynatrace.")
* [Расширение распределённой трассировки](/managed/ingest-from/extend-dynatrace/extend-tracing "Learn how to extend trace observability in Dynatrace.")

Используйте OpenTelemetry в сочетании с OneAgent, чтобы расширить покрытие observability, задействовав лучшее из обоих подходов.

### Технология PurePath®

Dynatrace запатентовал технологию PurePath® для распределённой трассировки ещё в 2006 году. Технология PurePath® объединяет информацию распределённой трассировки с дополнительными сведениями, такими как информация о пользовательском опыте, логи, метрики, топологическая информация, метаданные и даже данные профилирования на уровне кода, обеспечивая наивысший уровень точности и детализации данных.

#### Сценарии использования

Анализ данных вплоть до уровня деталей кода без потери полного контекста об окружении при детализации, с наивысшим уровнем детализации и точности данных отслеживаемых транзакций.