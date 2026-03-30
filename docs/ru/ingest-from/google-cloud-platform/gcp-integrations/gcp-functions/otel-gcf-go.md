---
title: Трассировка Google Cloud Functions в Go с помощью OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go
scraped: 2026-03-06T21:30:26.919461
---

# Трассировка Google Cloud Functions на Go с помощью OpenTelemetry


* Latest Dynatrace
* How-to guide
* 9-min read

Это руководство показывает, как инструментировать Google Cloud Functions на Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace. Чтобы узнать больше о том, как Dynatrace работает с OpenTelemetry, см. OpenTelemetry и Dynatrace в Dynatrace.").

Чтобы узнать о мониторинге Google Cloud Functions с помощью улучшенных Dynatrace трассировок OpenTelemetry, см. Интеграция на Google Cloud Functions GoLang.

## Предварительные требования

Применяются следующие предварительные требования и ограничения:

* Dynatrace версии 1.222+
* W3C Trace Context включён

  1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
  2. Включите **Send W3C Trace Context HTTP headers**.
* Cloud Functions Go Runtime 1.16+

## Инструментирование Google Cloud Functions

Dynatrace использует OpenTelemetry Trace Ingest для обеспечения сквозной видимости ваших Google Cloud Functions.

Чтобы инструментировать ваши Google Cloud Functions

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Добавление зависимостей OpenTelemetry**](otel-gcf-go.md#otel-dependencies "Узнайте, как инструментировать Google Cloud Functions на Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Настройка OpenTelemetry**](otel-gcf-go.md#otel-setup "Узнайте, как инструментировать Google Cloud Functions на Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Инструментирование точки входа функции**](otel-gcf-go.md#instrument-handler "Узнайте, как инструментировать Google Cloud Functions на Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Инструментирование исходящих запросов**](otel-gcf-go.md#outgoing-instrument "Узнайте, как инструментировать Google Cloud Functions на Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace.")

### Шаг 1. Добавление зависимостей OpenTelemetry

Используйте следующие команды для добавления необходимых зависимостей OpenTelemetry к вашей функции:

```
go get go.opentelemetry.io/otel


go get go.opentelemetry.io/otel/sdk


go get go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp
```

### Шаг 2. Настройка OpenTelemetry

Чтобы обеспечить сбор, связывание и экспорт трассировок в Dynatrace, необходимо соответствующим образом настроить OpenTelemetry. Для этого потребуются эндпоинт Dynatrace и токен аутентификации.

Чтобы определить эндпоинт

1. Откройте Dynatrace.
2. Проверьте адресную строку вашего браузера. URL будет соответствовать одному из следующих шаблонов:

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/...`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/...`
3. Замените часть `...` на `api/v2/otlp`, чтобы получить URL, который потребуется для настройки экспортёра OpenTelemetry.

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/api/v2/otlp`

Чтобы создать токен аутентификации

1. Перейдите в **Access Tokens** > **Generate new token**.
2. Укажите **Token name**.
3. В поле **Search scopes** найдите `Ingest OpenTelemetry traces` и установите флажок.
4. Выберите **Generate token**.
5. Выберите **Copy**, чтобы скопировать токен в буфер обмена.
6. Сохраните токен в безопасном месте; вы не сможете отобразить его повторно, и он понадобится для настройки экспортёра OpenTelemetry.

Вот как настроить конвейер трассировки OpenTelemetry:

```
package otelsetup


import (


"context"


"log"


"go.opentelemetry.io/otel"


"go.opentelemetry.io/otel/exporters/otlp/otlptrace"


"go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"


"go.opentelemetry.io/otel/propagation"


"go.opentelemetry.io/otel/sdk/resource"


sdk "go.opentelemetry.io/otel/sdk/trace"


semconv "go.opentelemetry.io/otel/semconv/v1.7.0"


)


func InitTracing(serviceName string, serviceVersion string) *sdk.TracerProvider {


client := otlptracehttp.NewClient()


exporter, err := otlptrace.New(context.Background(), client)


if err != nil {


log.Fatal(err)


}


// create resource


r, err := resource.Merge(


resource.Default(),


resource.NewWithAttributes(


// customizable resource attributes


semconv.SchemaURL,


semconv.ServiceNameKey.String(serviceName),


semconv.ServiceVersionKey.String(serviceVersion),


),


)


tracerProvider := sdk.NewTracerProvider(


sdk.WithBatcher(exporter),


sdk.WithResource(r),


)


otel.SetTracerProvider(tracerProvider)


// setup W3C trace context as global propagator


otel.SetTextMapPropagator(propagation.TraceContext{})


return tracerProvider


}
```

Для настройки экспортёра в вашу среду добавьте следующие переменные окружения при развёртывании вашей Google Cloud Function:

* `OTEL_EXPORTER_OTLP_ENDPOINT`: установите ранее определённый эндпоинт.
* `OTEL_EXPORTER_OTLP_HEADERS`: установите значение `Authorization=Api-Token <TOKEN>`, где `<TOKEN>` -- ранее созданный токен аутентификации.

Альтернативно, эндпоинт и токен аутентификации можно настроить в коде, передав их в качестве параметров в `otlptracehttp.NewClient`.

### Шаг 3. Инструментирование точки входа функции

Для инструментирования вызовов Google Cloud Function с помощью OpenTelemetry необходимо

1. Создать span вокруг точки входа функции для трассировки вызовов.
2. Извлечь и связать родительский span из распространяемого контекста. (Чтобы узнать о W3C Trace Context, см. наше [введение в W3C Trace Context](https://engineering.dynatrace.com/open-source/standards/w3c-trace-context/).)

Для некоторых библиотек OpenTelemetry Go уже предоставляет [инструментации](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation), которые вы можете использовать для решения этих задач.

В следующих разделах показано, как инструментировать определённые типы Google Cloud Functions:

* [Инструментирование HTTP Google Cloud Function](#instrument-http-handler)
* [Инструментирование Pub/Sub Google Cloud Function](#instrument-pubsub-handler)

#### Инструментирование HTTP Google Cloud Function

Точка входа HTTP Google Cloud Function в основном соответствует стандартному интерфейсу `http.Handler`. OpenTelemetry Go уже предоставляет инструментацию для этого интерфейса. Чтобы добавить её как зависимость к вашей функции, используйте следующую команду:

```
go get go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
```

Поскольку эта инструментация работает с интерфейсом `http.Handler`, она требует, чтобы ваша функция точки входа имела имя `ServeHTTP`. Также, поскольку среда выполнения Go может завершиться сразу после вызова функции, span-ы должны быть экспортированы в Dynatrace заранее.

Для этого создайте функцию-обёртку, которая инструментирует ваш фактический обработчик и сбрасывает span-ы после вызова:

```
package instrumentor


import (


"context"


"net/http"


"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"


semconv "go.opentelemetry.io/otel/semconv/v1.7.0"


"go.opentelemetry.io/otel/trace"


)


type Flush interface {


ForceFlush(context.Context) error


}


type HttpHandler = func(w http.ResponseWriter, r *http.Request)


func InstrumentedHandler(functionName string, function HttpHandler, flusher Flush) HttpHandler {


opts := []trace.SpanStartOption{


// customizable span attributes


trace.WithAttributes(semconv.FaaSTriggerHTTP),


}


// create instrumented handler


handler := otelhttp.NewHandler(


http.HandlerFunc(function), functionName, otelhttp.WithSpanOptions(opts...),


)


return func(w http.ResponseWriter, r *http.Request) {


// call the actual handler


handler.ServeHTTP(w, r)


// flush spans


flusher.ForceFlush(r.Context())


}


}
```

Собирая всё вместе, вот как вы используете это в своей функции:

```
package myfunction


import (


"net/http"


"instrumentor"


"otelsetup"


)


var InstrumentedHandler instrumentor.HttpHandler


func init() {


tracerProvider := otelsetup.InitTracing("my-service", "1.0.0")


InstrumentedHandler = instrumentor.InstrumentedHandler("my-function", Handler, tracerProvider)


}


func Handler(w http.ResponseWriter, r *http.Request) {


// Your code goes here


}
```

При развёртывании функции в GCP убедитесь, что вы используете `InstrumentedHandler` в качестве точки входа вашей Google Cloud Function.

#### Инструментирование Pub/Sub Google Cloud Function

Pub/Sub Google Cloud Function запускается событием [Pub/Sub message](https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage). Событие десериализуется GCP в объект сообщения, соответствующий типу, который вы определили в точке входа вашей функции. Этот тип обычно выглядит следующим образом:

```
type PubSubMessage struct {


Data        []byte            `json:"data"`


Attributes  map[string]string `json:"attributes"`


MessageId   string            `json:"messageId"`


PublishTime string            `json:"publishTime"`


OrderingKey string            `json:"orderingKey"`


}
```

В настоящее время OpenTelemetry не предоставляет инструментацию для Pub/Sub, поэтому инструментирование Pub/Sub Google Cloud Function требует немного больше работы.

В следующем фрагменте показано, как создать функцию-обёртку, которая инструментирует вызовы вашего обработчика Pub/Sub. Эта обёртка создаёт соответствующий span и использует карту `Attributes` объекта `PubSubMessage` для извлечения и связывания с родительским span из распространяемого контекста.

```
package instrumentor


import (


"context"


"fmt"


"go.opentelemetry.io/otel"


"go.opentelemetry.io/otel/codes"


"go.opentelemetry.io/otel/propagation"


semconv "go.opentelemetry.io/otel/semconv/v1.7.0"


"go.opentelemetry.io/otel/trace"


)


const (


instrumentationName = "my.company.com/my-pubsub-handler-instrumentation-name"


instrumentationVer  = "0.1.0"


)


type PubSubHandler = func(context.Context, PubSubMessage) error


type Flush interface {


ForceFlush(context.Context) error


}


func InstrumentedHandler(topicID string, handler PubSubHandler, flush Flush) PubSubHandler {


return func(ctx context.Context, msg PubSubMessage) error {


// create span


ctx, span := beforePubSubHandlerInvoke(ctx, topicID, msg)


defer span.End()


// call actual handler function


err := handler(ctx, msg)


// update span with handler result


afterPubSubHandlerInvoke(span, err)


// flush spans


flush.ForceFlush(ctx)


return err


}


}


func beforePubSubHandlerInvoke(ctx context.Context, topicID string, msg PubSubMessage) (context.Context, trace.Span) {


if msg.Attributes != nil {


// extract propagated span


propagator := otel.GetTextMapPropagator()


ctx = propagator.Extract(ctx, propagation.MapCarrier(msg.Attributes))


}


opts := []trace.SpanStartOption{


trace.WithSpanKind(trace.SpanKindConsumer),


trace.WithAttributes(


//customizable attributes


semconv.FaaSTriggerPubsub,


semconv.MessagingSystemKey.String("pubsub"),


semconv.MessagingDestinationKey.String(topicID),


semconv.MessagingDestinationKindTopic,


semconv.MessagingOperationProcess,


semconv.MessagingMessageIDKey.String(msg.MessageId),


),


}


tracer := otel.GetTracerProvider().Tracer(


instrumentationName, trace.WithInstrumentationVersion(instrumentationVer),


)


return tracer.Start(ctx, fmt.Sprintf("%s process", topicID), opts...)


}


func afterPubSubHandlerInvoke(span trace.Span, err error) {


if err != nil {


span.RecordError(err)


span.SetStatus(codes.Error, err.Error())


}


}
```

Собирая всё вместе, вот как использовать инструментированный обработчик в вашей функции:

```
package myfunction


import (


"context"


"instrumentor"


"otelsetup"


)


var InstrumentedHandler instrumentor.PubSubHandler


func init() {


tracerProvider := otelsetup.InitTracing("my-service", "1.0.0")


InstrumentedHandler = instrumentor.InstrumentedHandler("my-topic", Handler, tracerProvider)


}


func Handler(ctx context.Context, msg PubSubMessage) error {


// Your code goes here


return nil


}
```

При развёртывании функции в GCP убедитесь, что вы используете `InstrumentedHandler` в качестве точки входа вашей Google Cloud Function.

### Шаг 4. Инструментирование исходящих запросов

Для достижения сквозной трассировки важно также убедиться, что ваши исходящие запросы инструментированы.

В следующих разделах показано, как инструментировать определённые исходящие запросы:

* [Инструментирование исходящих HTTP-запросов](#outgoing-http-instrument)
* [Инструментирование запросов публикации Pub/Sub](#pubsub-publish-instrument)

OpenTelemetry Go использует `context.Context` для связывания вновь созданного span с его родителем, поэтому при использовании инструментации или создании span вручную убедитесь, что передаёте экземпляр `context.Context`, который был передан вашей Google Cloud Function (или экземпляр, производный от него). В противном случае ваша трассировка не будет правильно связана.

#### Инструментирование исходящих HTTP-запросов

OpenTelemetry Go предоставляет инструментацию для трассировки исходящих HTTP-вызовов. Добавьте её как зависимость к вашей функции с помощью следующей команды:

```
go get go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
```

Вот как вы можете использовать эту инструментацию в своём коде:

```
import (


"context"


"net/http"


"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"


)


func makeHttpRequest(ctx context.Context, url string) {


// create an instrumented HTTP client


client := http.Client{Transport: otelhttp.NewTransport(http.DefaultTransport)}


req, err := http.NewRequestWithContext(ctx, "GET", url, nil)


if err != nil {


// error handling


return


}


res, err := client.Do(req)


if err != nil {


// error handling


return


}


defer res.Body.Close()


// response handling code goes here


}
```

* Не используйте удобные функции, такие как `GET` или `POST`, стандартного `http.Client`, поскольку они не принимают объект `context.Context`. Чтобы убедиться, что ваш HTTP-запрос правильно связан, либо создайте запрос с объектом контекста, как в примере выше, либо используйте одну из удобных функций (таких как `otelhttp.Get` или `otelhttp.Put`) HTTP-инструментации.
* Убедитесь, что закрываете или полностью читаете тело ответа. В противном случае исходящий запрос не будет правильно инструментирован.

#### Инструментирование запроса публикации Pub/Sub

Для клиента Pub/Sub в настоящее время нет инструментации в OpenTelemetry Go. Посмотрите следующий фрагмент, чтобы увидеть, как можно использовать API OpenTelemetry Go для инструментирования операций публикации Pub/Sub:

```
import (


"context"


"fmt"


"cloud.google.com/go/pubsub"


"go.opentelemetry.io/otel"


"go.opentelemetry.io/otel/codes"


"go.opentelemetry.io/otel/propagation"


semconv "go.opentelemetry.io/otel/semconv/v1.7.0"


"go.opentelemetry.io/otel/trace"


)


const (


instrumentationName = "my.company.com/my-pubsub-instrumentation-lib"


instrumentationVer  = "0.1.0"


)


func PublishMessage(ctx context.Context, client *pubsub.Client, msg *pubsub.Message, topicID string) (string, error) {


// create span


ctx, span := beforePublishMessage(ctx, topicID, msg)


defer span.End()


// Send Pub/Sub message


messageID, err := client.Topic(topicID).Publish(ctx, msg).Get(ctx)


// enrich span with publish result


afterPublishMessage(span, messageID, err)


return messageID, err


}


func beforePublishMessage(ctx context.Context, topicID string, msg *pubsub.Message) (context.Context, trace.Span) {


opts := []trace.SpanStartOption{


trace.WithSpanKind(trace.SpanKindProducer),


trace.WithAttributes(


// customizable span attributes


semconv.MessagingSystemKey.String("pubsub"),


semconv.MessagingDestinationKey.String(topicID),


semconv.MessagingDestinationKindTopic,


),


}


tracer := otel.Tracer(


instrumentationName, trace.WithInstrumentationVersion(instrumentationVer),


)


ctx, span := tracer.Start(ctx, fmt.Sprintf("%s send", topicID), opts...)


if msg.Attributes == nil {


msg.Attributes = make(map[string]string)


}


// propagate Span across process boundaries


otel.GetTextMapPropagator().Inject(ctx, propagation.MapCarrier(msg.Attributes))


return ctx, span


}


func afterPublishMessage(span trace.Span, messageID string, err error) {


if err != nil {


span.RecordError(err)


span.SetStatus(codes.Error, err.Error())


} else {


span.SetAttributes(semconv.MessagingMessageIDKey.String(messageID))


}


}
```

Приведённый выше фрагмент распространяет исходящий span, внедряя его в поле `Attributes` сообщения Pub/Sub. [Инструментированная Pub/Sub-функция](#instrument-pubsub-handler) извлечёт этот распространяемый span для связывания трассировки воедино.

## Проверка загрузки трассировок в Dynatrace

Через несколько минут после вызова ваших Google Cloud Functions найдите свои span-ы:

* Перейдите в ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** и выберите вкладку **Ingested traces**.
* Ваши span-ы будут частью существующей распределённой трассировки PurePath, если корень вашего вызова уже мониторится OneAgent.

Если ваша Google Cloud Function не получает трафик, трассировки не будут отображаться.

## (Опционально) Настройка сбора данных для соблюдения требований конфиденциальности

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, только значения атрибутов, указанные в списке разрешённых, сохраняются и отображаются в веб-интерфейсе Dynatrace. Это предотвращает случайное хранение персональных данных, позволяя вам соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Для просмотра ваших пользовательских атрибутов необходимо сначала разрешить их в веб-интерфейсе Dynatrace. Чтобы узнать, как настроить хранение и маскирование атрибутов, см. [Редактирование атрибутов](../../../dynatrace-oneagent/oneagent-and-opentelemetry/configuration.md#attribute-redaction "Узнайте, как включить и настроить сенсор span-ов OneAgent для данных OpenTelemetry.").
