---
title: Distributed Tracing
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing
scraped: 2026-02-06T16:18:48.568683
---

# Распределенная трассировка

# Распределенная трассировка

* Последняя версия Dynatrace
* Приложение
* 3-минутное чтение
* Опубликовано 15 июля 2024 г.

Предварительные условия

* [Подписка на платформу Dynatrace (DPS)](/docs/license "About Dynatrace Platform Subscription (DPS), модель лицензирования для всех возможностей Dynatrace.")

### Разрешения

В следующей таблице описаны необходимые разрешения.

Разрешение

Описание

хранилище: ведра: читать

Чтение данных сегментов

хранилище: промежутки: чтение

Чтение данных диапазона

хранилище: объекты: чтение

Чтение данных сущностей

хранилище: журналы: чтение

Чтение журналов

состояние: пользовательское-приложение-состояния: чтение

Чтение состояния приложения пользователя

состояние: пользовательское приложение-состояния: запись

Запись состояния приложения пользователя

состояние: пользовательское приложение-состояния: удалить

Удалить состояние приложения пользователя

хранилище: наборы полей: чтение

Чтение маскированных/чувствительных полей

хранилище: фильтр-сегменты: чтение

Чтение сегментов фильтра

хранилище: Smartscape: читать

Чтение узлов и ребер Smartscape

10

строк на странице

Страница

1

из 1

## Установка

Убедитесь, что это приложение [установлен в вашей среде](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Начать

Концепции

Варианты использования

Распределенная трассировка на базе Grail помогает максимально эффективно использовать данные трассировки в Dynatrace.Он позволяет принимать и обрабатывать петабайты данных трассировки, позволяя отслеживать и устранять ошибки и проблемы с производительностью в сложных распределенных программных системах в любом масштабе.Данные трассировки следуют за Dynatrace [модель данных трассировки](#distributed-tracing-concepts), поэтому анализ всей связанной информации и атрибутов интуитивно понятен и может быть выполнен с помощью приложения ![Распределенная трассировка](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") Distributed Tracing и языка запросов Dynatrace (DQL).Данные трассировки хранятся в Grail, поэтому вы можете использовать возможности Grail для анализа даже неизвестных неизвестных.

Удобный интерфейс приложения Distributed Tracing ![Распределенная трассировка](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") разработан с учетом требований инженеров, SRE и архитекторов производительности, что позволяет сразу же легко визуально анализировать данные трассировки.

![Быстро оцените время отклика и ошибки с помощью инструментов динамической визуализации, таких как гистограммы.](https://cdn.hub.central.dynatrace.com/hub/1_LwL2KfK.png)![Погрузитесь в детали трассировки и изучите связанные журналы.](https://cdn.hub.central.dynatrace.com/hub/2_WV8DuOY.png)![Легко отслеживайте все исключения в пределах диапазона благодаря четким взаимосвязям и цепочкам исключений, показывающим основную причину.](https://cdn.hub.central.dynatrace.com/hub/3_5iXpQnz.png)![Выявляйте и анализируйте исключения в трассировках с помощью читаемых трассировок стека, агрегированных данных и визуальных маркеров, выделяющих проблемные интервалы.](https://cdn.hub.central.dynatrace.com/hub/4_Qscx7Vl.png)

1 из 4Быстро определите время отклика и ошибки с помощью инструментов динамической визуализации, таких как гистограммы.

## Учебные модули

Чтобы научиться использовать распределенную трассировку, выполните следующий процесс:

[01Анализ исключений

* Учебник
* Анализ исключений помогает более эффективно обнаруживать, исследовать и разрешать исключения в Dynatrace.](/docs/observe/application-observability/distributed-tracing/Exception-anaанализ)[02Ingest трассировки

* Практическое руководство
* Оснастите свои приложения OneAgent или OpenTelemetry, чтобы начать принимать данные трассировки в Dynatrace.](/docs/observe/application-observability/distributed-tracing/ingest-traces)[03Настройте разрешения Grail для распределенной трассировки

* Практическое руководство
* Управление разрешениями для распределенной трассировки на базе Grail.](/docs/observe/application-observability/distributed-tracing/permissions)[04Настройка хранения и хранения данных для распределенной трассировки

* Практическое руководство
* Управляйте хранением и хранением данных для распределенной трассировки на базе Grail.](/docs/observe/application-observability/distributed-tracing/storage)[05Распространение диапазона и контекста трассировки

* Ссылка
* Понимание распространения контекста промежутка и трассировки в Dynatrace и способы их настройки.](/docs/observe/application-observability/distributed-tracing/tracking-transactions)[06Используйте трассировки, DQL и журналы для выявления закономерностей.

* Учебник
* Используйте трассировки, журналы и DQL для визуализации необработанных данных и выявления аномальных закономерностей.](/docs/observe/application-observability/distributed-tracing/use-traces-and-dql-to-spot-patterns)[07Приложение Distributed Tracing

* Объяснение
* Откройте для себя функциональные возможности нового приложения Distributed Tracing.](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app)[08Расширенная аналитика отслеживания на базе Grail

* Учебник
* Изучите расширенные возможности анализа трассировки в Grail.](/docs/observe/application-observability/distributed-tracing/advanced-tracing-analytics).

## Концепции распределенной трассировки

### Распределенная трассировка

Распределенная трассировка — это последовательность интервалов, идентифицируемая уникальным идентификатором трассировки, которая следует по пути одного запроса при его прохождении через различные службы и компоненты в распределенной системе.В современной микросервисной среде она обычно охватывает несколько сервисов, предоставляя подробное представление о пути и производительности запроса.Трассировка содержит семантически разные атрибуты, которые позволяют интерпретировать и понимать собранные данные, помогая выявлять узкие места, ошибки и проблемы с задержкой для эффективного устранения неполадок и оптимизации.

![Следы и услуги](https://dt-cdn.net/images/traces-services-1920-59a6506038.png)

### Варианты использования

* Понимать, как запросы распространяются по распределенным системам и микросервисам.
* Используйте для анализа запросов высококачественные данные, генерируемые распределенными системами и микросервисами.
* Быстро понять, как работает каждый микросервис.
* Следуйте [Подробный анализ первопричин Dynatrace Intelligence](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts."), чтобы определить причинно-следственные связи между событиями.

### Охватывать

Промежуток представляет собой одну операцию в распределенной трассировке, фиксирующую детали прохождения запроса через несколько служб.Каждый диапазон включает такие атрибуты, как имя, временная метка начала, список событий диапазона (например, исключений), идентификатор родительского диапазона и тип диапазона.Эта информация — **контекст диапазона** — помогает поместить все диапазоны и события в контекст друг друга, чтобы вы могли отслеживать и понимать производительность и поведение отдельных операций в распределенной системе.

В пределах трассировки, когда действие — *родительский диапазон* — завершается, следующее действие переходит к его *дочернему диапазону*.Диапазон без родительского диапазона называется *корневым диапазоном* трассировки и указывает на начало трассировки.

На изображении ниже показана трассировка, проходящая через три сервиса и создающая запрос для каждого сервиса.Каждый запрос имеет корневой диапазон, один из которых также является корнем трассировки.

* A — это и первый диапазон трассировки, и первый диапазон запроса в рамках первой службы;кроме того, A — это диапазон без родительского элемента.A является одновременно корнем трассировки и запроса.
* C — первый диапазон запроса внутри второго сервиса;кроме того, у C есть родительский элемент (B).C — корень второго запроса.
* E не является первым диапазоном запроса в рамках третьего сервиса.Родитель E (D) является корнем третьего запроса.

![Трассировка анатомии](https://dt-cdn.net/images/trace-anatomy-1920-6ba49e1863.png)

Узнайте больше о [охватывать семантические поля](/docs/semantic-dictionary/fields#span "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

Контекст диапазона позволяет дочернему диапазону относиться к трассировке и его родительскому диапазону.Следовательно, контекст необходимо распространять внутри службы (по разным потокам), а также между службами и границами процессов.Обычно это происходит через заголовки HTTP (например, [Контекст трассировки W3C»¿](https://www.w3.org/TR/trace-context/)) или через уникальные идентификаторы в системах обмена сообщениями.Чтобы узнать больше о распространении контекста, см. [Распространение контекста интервала и трассировки](/docs/observe/application-observability/distributed-tracing/tracking-transactions "Understand span and trace context propagation in Dynatrace and how to set them up.").

### Атрибут

Атрибуты — это пары «ключ-значение», которые предоставляют подробную информацию о диапазоне, запросе или ресурсе, например коды ответов, методы HTTP и URL-адреса.С помощью атрибутов вы можете группировать, запрашивать, находить и анализировать трассировки и интервалы.

### Варианты использования

Dynatraces использует метаданные атрибутов для

* [Обнаружение и присвоение имен службам](/docs/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.").
* Соберите данные о контексте трассировки и связях с другими объектами для [Топология Smartscape](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.").
* Подключите данные журнала к трассировкам для [Журналы](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.") или [Бревна Классик](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment "Learn how you can connect your incoming log data to traces for more precise Dynatrace analysis.").
* Поймите, как [график обслуживания](/docs/observe/application-observability/services-classic/service-analysis-timing "Find out what each time in service analysis means.") влияет на продолжительность интервала (например, время процессора, время сети или просто ожидание других потоков) и проанализируйте, какой код был выполнен в контексте интервала.

### Лучшие практики

Если вы собираете данные трассировки через

* OpenTelemetry, определите [захваченные настройки атрибутов](/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings "Learn how to configure span settings for OpenTelemetry and OpenTracing.").
* OneAgent, определите [запрашивает настройки атрибутов](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

Узнайте больше о семантических полях [атрибуты запроса](/docs/semantic-dictionary/fields#request-attributes "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") и [захваченные атрибуты](/docs/semantic-dictionary/fields#captured-attributes "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

### Услуга

Сервисы распространяются по распределенным трассировкам.В службах с горизонтальным масштабированием каждый диапазон обрабатывается конкретными **экземплярами служб**.Службы определяются и именуются на основе доступных атрибутов или свойств, которые собираются вместе с интервалами.

### Варианты использования

* [Сегментируйте запросы для уменьшения снижения времени ответа](/docs/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").

### Сбор данных и распространение контекста

Вы можете интегрировать OpenTelemetry и OneAgent для сбора данных трассировки, таких как статус запроса, время ответа, версии, информация об инфраструктуре и другие соответствующие метаданные в качестве атрибутов.Контекст трассировки, включая уникальный идентификатор трассировки, затем распространяется по вашим приложениям и микросервисам.

### Лучшие практики

Прежде чем приступить к распределенной трассировке, узнайте, чем отличаются настройка и сбор данных трассировки между OpenTelemetry и OneAgent.Ниже приводится обзор основных отличий.

OpenTelemetry

OneAgent

Настраивать

Автоматический или ручной

Автоматический

Захват

Автоматический сбор разрешенных атрибутов диапазона.

Автоматический сбор нескольких атрибутов запроса, включая метод HTTP, URL-адрес, коды ответов, данные топологии и сведения о базовых технологиях.

Контекст

Автоматически или вручную контекстуализированные записи журнала, в зависимости от библиотеки инструментов.

Автоматически контекстуализируется

* Записи журнала, созданные известными платформами журналов.
* Следы в Smartscape и Dynatrace Intelligence.

Для начала см.

* [Автоматическая настройка с помощью OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Инструментирование с помощью OpenTelemetry](/docs/ingest-from/opentelemetry/getting-started "How to get your OpenTelemetry data into Dynatrace.")
* [Расширение распределенной трассировки](/docs/ingest-from/extend-dynatrace/extend-tracing "Learn how to extend trace observability in Dynatrace.")

Используйте OpenTelemetry в сочетании с OneAgent, чтобы улучшить зону наблюдения, используя лучшее из обоих.

## Варианты использования

Используйте ![Распределенная трассировка](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") распределенную трассировку для:

* Устранение неполадок: узнайте, почему запросы не выполняются, и предотвратите проблемы в будущем.
* Оптимизация производительности. Изучите [производительность системы](/docs/observe/application-observability/distributed-tracing/detect-performance-issues "Analyze your trace data and detected which requests are slow and why with the Distributed Tracing app.") и выявите узкие места, чтобы повысить надежность и удобство для пользователей.
* Подробный анализ: просмотрите отдельные детали трассировки для более глубокого понимания.
* Исследовательский анализ. Используйте анализ в свободной форме, чтобы на лету обнаруживать и исследовать неизвестные неизвестные.
* Обнаружение неизвестных неизвестных: будьте готовы к неизвестному, используя анализ в свободной форме для исследования и анализа данных на лету.
* Синтез трассировок и сигналов мониторинга: просматривайте данные трассировки в контексте других сигналов, таких как журналы, бизнес-события или показатели.

![Центр](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

## Исследуйте в Dynatrace Hub

Анализируйте и нарезайте распределенные трассировки по любому атрибуту и ​​из любого источника.

[Dynatrace Hubï»¿](https://www.dynatrace.com/hub/detail/distributed-tracing/?internal_source=doc&internal_medium=link&internal_campaign=cross)

## ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ

Почему я вижу сообщение «Новый интерфейс трассировки скоро появится в вашей среде!»при запуске приложения распределенной трассировки?

Новый интерфейс отслеживания внедряется поэтапно, чтобы расширить доступ для клиентов Dynatrace SaaS DPS до марта 2025 года. Сроки доступности зависят от географического региона и общего объема отслеживания вашей учетной записи.Для получения дополнительной информации обратитесь к своему менеджеру по работе с клиентами.

Доступны ли трассировки в классических представлениях Distributed Traces?

Да.Начав анализировать трассировки в приложении Distributed Tracing, вы можете продолжать использовать Distributed Traces Classic одновременно.

Какой пакет лицензирования охватывает распределенную трассировку?

DPS FullStack и/или Custom Traces Classic.При использовании нового приложения Distributed Tracing никаких дополнительных затрат не взимается.

Я изменил грани.Могу ли я сбросить их рекомендуемым способом?

Да.Перейдите в раздел **Распределенная трассировка** ![Распределенная трассировка](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") и выберите **Показать фасеты** > **Восстановить значения по умолчанию**.

Как удалить ссылки span.kind с нулевой длительностью?

Обновите OneAgent до последней версии.

Не все трассировки, доступные в Distributed Traces Classic, видны в приложении Distributed Tracing.

* Убедитесь, что у вас установлена ​​последняя версия OneAgent.
* Убедитесь, что [Функция OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **расширение контекста трассировки тега пересылки 4** включено;это гарантирует совместимость трассировок, собранных OneAgent, со стандартом контекста трассировки W3C.

Я вижу неполные сквозные трассировки в приложении Distributed Tracing, которые отображаются полными в Distributed Traces Classic.

* Убедитесь, что у вас установлена ​​последняя версия OneAgent.
* Убедитесь, что [Функция OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **расширение контекста трассировки тега пересылки 4** включено;это гарантирует совместимость трассировок, собранных OneAgent, со стандартом контекста трассировки W3C.

Как я могу фильтровать трассировки, собранные OneAgent или полученные через OpenTelemetry?

1. Перейдите к разделу **Распределенная трассировка** ![Распределенная трассировка](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing").
2. В списке фасетов введите `span source` и выберите интересующий вас источник.

Поддерживает ли новый опыт распределенной трассировки межсредовую трассировку?

Еще нет.

## Похожие темы

* [Язык запросов Dynatrace](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Что такое Dynatrace Grail?](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.")
* [Распространение контекста интервала и трассировки](/docs/observe/application-observability/distributed-tracing/tracking-transactions "Understand span and trace context propagation in Dynatrace and how to set them up.")