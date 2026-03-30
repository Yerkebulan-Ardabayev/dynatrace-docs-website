---
title: Начало работы с OpenTelemetry и наблюдаемостью ИИ
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/get-started/opentelemetry
scraped: 2026-03-06T21:28:35.685729
---

* Последняя Dynatrace
* Руководство по началу работы
* 5 мин. чтения

OpenTelemetry предоставляет вендоронезависимый стандарт для сбора трассировок и метрик из ИИ-приложений. С помощью [семантических соглашений GenAI](https://opentelemetry.io/docs/specs/semconv/gen-ai/) OpenTelemetry определяет единый способ захвата атрибутов, специфичных для ИИ, таких как имена моделей, количество токенов, задержка и метрики стоимости для различных провайдеров LLM.

Dynatrace полностью поддерживает OpenTelemetry, позволяя отправлять данные наблюдаемости ИИ непосредственно в вашу среду Dynatrace через конечные точки OTLP API. Этот подход даёт вам гибкость в использовании любой совместимой с OpenTelemetry библиотеки инструментирования или в создании пользовательского инструментирования.

## Для кого это руководство?

Это руководство по началу работы предназначено для:

* Команд ИИ-инженерии, создающих приложения и сервисы на основе агентов и LLM.
* Инженеров по надёжности (SRE), ответственных за мониторинг ИИ-задач на гиперскейлерах.
* Инженеров платформ, интегрирующих данные OTel в Dynatrace.

## Что вы узнаете?

Следуя этому руководству, вы узнаете:

* Как настроить OpenTelemetry и получить видимость на уровне трассировок и логов для ваших ИИ-приложений.
* Как настроить и инструментировать приложение с помощью OTel.
* Как настроить экспорт OTLP в Dynatrace.
* Как сообщать атрибуты в соответствии с семантическими соглашениями GenAI.
* Какие трассировки и метрики можно отправлять в Dynatrace.
* Как обеспечить видимость на уровне трассировок и токенов для операций агентов и LLM.

## Прежде чем начать

### Предварительные требования

Для работы вам потребуется:

* Работающее ИИ-приложение или демо-приложение ИИ.
* Dynatrace с лицензией Dynatrace Platform Subscription (DPS) — модели лицензирования для всех возможностей Dynatrace."), в которой включены Traces powered by Grail."), Metrics powered by Grail и Log Analytics.
* Включённый приём OTLP, см. OpenTelemetry и Dynatrace в Dynatrace.").
* Ключ API платформы OpenAPI.
* Токен Dynatrace API со следующими областями, см. Dynatrace API — Токены и аутентификация.

  + Приём метрик (`metrics.ingest`)
  + Приём логов (`logs.ingest`)
  + Приём трассировок OpenTelemetry (`openTelemetryTrace.ingest`)

### Предварительные знания

Полезно иметь базовые знания о:

* Python или Node.js.
* Концепциях OTel, таких как SDK, спаны, экспортёры и коллекторы.
* Разрешениях Dynatrace и приёме данных.

## Начало работы с ИИ и OpenTelemetry

### 1. Инструментирование приложения для OpenTelemetry

Вы можете использовать Python или Node.js для инструментирования вашего ИИ-приложения непосредственно с помощью SDK OpenTelemetry.

Python

Node.js

1. Установите SDK OpenTelemetry и экспортёр Collector.
   Выполните следующую команду в терминале.

   ```
   pip install opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
   ```
2. Необязательно Вы также можете запустить автоинструментирование OpenTelemetry.

   ```
   pip install opentelemetry-distro opentelemetry-exporter-otlp


   opentelemetry-bootstrap -a install
   ```
3. Инициализируйте SDK OpenTelemetry.
   Добавьте следующий код в начало вашего основного файла.

   ```
   from opentelemetry import trace


   from opentelemetry.sdk.resources import Resource


   from opentelemetry.sdk.trace import TracerProvider


   from opentelemetry.sdk.trace.export import BatchSpanProcessor


   from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter


   resource = Resource.create({"service.name": "<your-service>"})


   provider = TracerProvider(resource=resource)


   trace.set_tracer_provider(provider)


   exporter = OTLPSpanExporter(


   endpoint="https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp/v1/traces",


   headers={"Authorization": "Api-Token <YOUR_DT_API_TOKEN>"},


   )


   provider.add_span_processor(BatchSpanProcessor(exporter))


   tracer = trace.get_tracer(__name__)
   ```

1. Установите SDK OpenTelemetry, API и экспортёр Collector.
   Выполните следующую команду в терминале.

   ```
   npm install @opentelemetry/sdk-node @opentelemetry/api @opentelemetry/exporter-trace-otlp-proto
   ```
2. Инициализируйте SDK OpenTelemetry.
   Добавьте следующий код в начало вашего основного файла.

   ```
   import { NodeSDK } from '@opentelemetry/sdk-node';


   import { Resource } from '@opentelemetry/resources';


   import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-proto';


   import { trace } from '@opentelemetry/api';


   const sdk = new NodeSDK({


   resource: new Resource({ 'service.name': '<your-service>' }),


   traceExporter: new OTLPTraceExporter({


   url: 'https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp/v1/traces',


   headers: { Authorization: 'Api-Token <YOUR_DT_API_TOKEN>' },


   }),


   });


   sdk.start();


   const tracer = trace.getTracer('my-tracer');
   ```

### 2. Добавление атрибутов GenAI к вашим спанам

Семантические соглашения OpenTelemetry GenAI стандартизируют атрибуты, захватываемые для операций генеративного ИИ.
Чтобы убедиться, что ваши данные телеметрии следуют этим соглашениям, добавьте следующий код в ваше приложение.

Подробнее о семантических соглашениях см. Семантические соглашения GenAI.

Python

Node.js

```
from opentelemetry.trace import SpanKind


with tracer.start_as_current_span("chat gpt-5", kind=SpanKind.CLIENT) as span:


span.set_attribute("gen_ai.operation.name", "chat")


span.set_attribute("gen_ai.provider.name", "openai")


span.set_attribute("gen_ai.request.model", "gpt-5.2")


span.set_attribute("gen_ai.request.temperature", 0.7)


response = openai_client.chat.completions.create(


model="gpt-4",


messages=messages,


temperature=0.7,


)


span.set_attribute("gen_ai.response.model", response.model)


span.set_attribute("gen_ai.response.id", response.id)


span.set_attribute("gen_ai.usage.input_tokens", response.usage.prompt_tokens)


span.set_attribute("gen_ai.usage.output_tokens", response.usage.completion_tokens)
```

```
import { SpanKind } from '@opentelemetry/api';


tracer.startActiveSpan('chat gpt-4', { kind: SpanKind.CLIENT }, async (span) => {


span.setAttribute('gen_ai.operation.name', 'chat');


span.setAttribute('gen_ai.provider.name', 'openai');


span.setAttribute('gen_ai.request.model', 'gpt-5.2');


span.setAttribute('gen_ai.request.temperature', 0.7);


const response = await openai.chat.completions.create({


model: 'gpt-4',


messages: messages,


temperature: 0.7,


});


span.setAttribute('gen_ai.response.model', response.model);


span.setAttribute('gen_ai.response.id', response.id);


span.setAttribute('gen_ai.usage.input_tokens', response.usage.prompt_tokens);


span.setAttribute('gen_ai.usage.output_tokens', response.usage.completion_tokens);


span.end();


});
```

## Поздравляем!

Теперь, когда вы настроили ваше ИИ-приложение для отправки данных наблюдаемости непосредственно в Dynatrace, вы можете:

* Изучить приложение AI Observability для визуализации ваших ИИ-задач.
* Ознакомиться с [примерами приложений](https://github.com/dynatrace-oss/dynatrace-ai-agent-instrumentation-examples) для получения дополнительных примеров.