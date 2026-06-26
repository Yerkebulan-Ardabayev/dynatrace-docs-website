---
title: Трассировка Google Cloud Functions в Go с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go
scraped: 2026-05-12T12:08:56.043316
---

# Трассировка Google Cloud Functions в Go с OpenTelemetry

# Трассировка Google Cloud Functions в Go с OpenTelemetry

* Практическое руководство
* Чтение: 9 мин
* Обновлено 13 ноября 2023 г.

В этом руководстве показано, как инструментировать Google Cloud Functions в Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace. Подробнее о том, как Dynatrace работает с OpenTelemetry, см. [OpenTelemetry и Dynatrace](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.").

Подробнее о мониторинге Google Cloud Functions с помощью улучшенных трассировок OpenTelemetry от Dynatrace см. [Интеграция OpenTelemetry на Google Cloud Functions Go](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go "Мониторинг Google Cloud Functions с помощью OpenTelemetry для Go и Dynatrace.").

## Предварительные требования

Применяются следующие предварительные требования и ограничения:

* Dynatrace версии 1.222+
* Включён W3C Trace Context

  1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
  2. Включите **Send W3C Trace Context HTTP headers**.
* Cloud Functions Go Runtime 1.16+

## Инструментирование Google Cloud Functions

Dynatrace использует OpenTelemetry Trace Ingest для обеспечения сквозной видимости ваших Google Cloud Functions.

Для инструментирования Google Cloud Functions

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Добавление зависимостей OpenTelemetry**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#otel-dependencies "Узнайте, как инструментировать Google Cloud Functions в Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка OpenTelemetry**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#otel-setup "Узнайте, как инструментировать Google Cloud Functions в Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Инструментирование точки входа функции**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#instrument-handler "Узнайте, как инструментировать Google Cloud Functions в Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Инструментирование исходящих запросов**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#outgoing-instrument "Узнайте, как инструментировать Google Cloud Functions в Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace.")

### Шаг 1 Добавление зависимостей OpenTelemetry

Используйте следующие команды для добавления необходимых зависимостей OpenTelemetry в функцию:

```
go get go.opentelemetry.io/otel



go get go.opentelemetry.io/otel/sdk



go get go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp
```

### Шаг 2 Настройка OpenTelemetry

Чтобы трассировки собирались, связывались и экспортировались в Dynatrace, необходимо настроить OpenTelemetry соответствующим образом. Для этого потребуются эндпоинт Dynatrace и токен аутентификации.

Определение эндпоинта

1. Откройте Dynatrace.
2. Проверьте адресную строку браузера. URL будет соответствовать одному из следующих шаблонов:

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/...`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/...`
3. Замените часть `...` на `api/v2/otlp`, чтобы получить URL для настройки exporter OpenTelemetry.

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/api/v2/otlp`

Создание токена аутентификации

1. Перейдите в **Access Tokens** > **Generate new token**.
2. Укажите **Token name**.
3. В поле **Search scopes** найдите `Ingest OpenTelemetry traces` и установите флажок.
4. Нажмите **Generate token**.
5. Нажмите **Copy**, чтобы скопировать токен в буфер обмена.
6. Сохраните токен в надёжном месте: повторно отобразить его не удастся, а он понадобится для настройки exporter OpenTelemetry.

Ниже показано, как настроить конвейер трассировки OpenTelemetry:

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

Для настройки exporter на ваш тенант добавьте следующие переменные окружения при развёртывании Google Cloud Function:

* `OTEL_EXPORTER_OTLP_ENDPOINT`: укажите ранее определённый эндпоинт.
* `OTEL_EXPORTER_OTLP_HEADERS`: укажите `Authorization=Api-Token <TOKEN>`, где `<TOKEN>` - ранее созданный токен аутентификации.

Кроме того, эндпоинт и токен аутентификации можно настроить в коде, передав их как параметры в `otlptracehttp.NewClient`.

### Шаг 3 Инструментирование точки входа функции

Для инструментирования вызовов Google Cloud Function с помощью OpenTelemetry необходимо:

1. Создать спан вокруг точки входа функции для трассировки вызовов.
2. Извлечь и связать родительский спан из переданного контекста. (Подробнее о W3C Trace Context см. [Введение в W3C Trace Context](https://engineering.dynatrace.com/open-source/standards/w3c-trace-context/).)

Для ряда библиотек OpenTelemetry Go уже предоставляет [библиотеки инструментирования](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation), которые берут на себя эти задачи.

В следующих разделах показано, как инструментировать определённые типы Google Cloud Functions:

* [Инструментирование HTTP Google Cloud Function](#instrument-http-handler)
* [Инструментирование Pub/Sub Google Cloud Function](#instrument-pubsub-handler)

#### Инструментирование HTTP Google Cloud Function

Точка входа HTTP Google Cloud Function в основном соответствует стандартному интерфейсу `http.Handler`. OpenTelemetry Go уже предоставляет инструментирование для этого интерфейса. Для добавления его в зависимости функции используйте следующую команду:

```
go get go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
```

Поскольку это инструментирование работает с интерфейсом `http.Handler`, функция точки входа должна называться `ServeHTTP`. Кроме того, поскольку среда выполнения Go может завершиться сразу после вызова функции, спаны необходимо экспортировать в Dynatrace заранее.

Для этого создайте функцию-обёртку, которая инструментирует основной обработчик и сбрасывает спаны после вызова:

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

Объединяя всё вместе, ниже показано, как использовать это в функции:

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

При развёртывании функции в GCP обязательно используйте `InstrumentedHandler` в качестве точки входа Google Cloud Function.

#### Инструментирование Pub/Sub Google Cloud Function

Pub/Sub Google Cloud Function запускается событием [Pub/Sub message](https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage). GCP десериализует событие в объект сообщения, соответствующий типу, определённому в точке входа функции. Обычно этот тип выглядит примерно следующим образом:

```
type PubSubMessage struct {



Data        []byte            `json:"data"`



Attributes  map[string]string `json:"attributes"`



MessageId   string            `json:"messageId"`



PublishTime string            `json:"publishTime"`



OrderingKey string            `json:"orderingKey"`



}
```

OpenTelemetry пока не предоставляет готового инструментирования для Pub/Sub, поэтому инструментирование Pub/Sub Google Cloud Function требует дополнительных действий.

В следующем фрагменте показано, как создать функцию-обёртку, инструментирующую вызовы Pub/Sub обработчика. Обёртка создаёт соответствующий спан и использует карту `Attributes` объекта `PubSubMessage` для извлечения и связывания с родительским спаном из переданного контекста.

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

Объединяя всё вместе, ниже показано, как использовать инструментированный обработчик в функции:

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

При развёртывании функции в GCP обязательно используйте `InstrumentedHandler` в качестве точки входа Google Cloud Function.

### Шаг 4 Инструментирование исходящих запросов

Для достижения сквозной трассировки важно также убедиться, что исходящие запросы инструментированы.

В следующих разделах показано, как инструментировать определённые исходящие запросы:

* [Инструментирование исходящих HTTP-запросов](#outgoing-http-instrument)
* [Инструментирование запросов публикации Pub/Sub](#pubsub-publish-instrument)

OpenTelemetry Go использует `context.Context` для связывания нового спана с родительским. При использовании инструментирования или создании спана вручную передавайте экземпляр `context.Context`, который был передан в Google Cloud Function (или производный от него). Иначе трассировка не будет корректно связана.

#### Инструментирование исходящих HTTP-запросов

OpenTelemetry Go предоставляет инструментирование для трассировки исходящих HTTP-вызовов. Добавьте его как зависимость в функцию с помощью следующей команды:

```
go get go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
```

Ниже показано, как использовать это инструментирование в коде:

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

* Не используйте вспомогательные функции `GET` или `POST` стандартного `http.Client`, так как они не принимают объект `context.Context`. Чтобы HTTP-запрос был корректно связан, создайте запрос с объектом контекста, как в примере выше, или используйте одну из вспомогательных функций HTTP-инструментирования (например, `otelhttp.Get` или `otelhttp.Put`).
* Обязательно закрывайте или полностью читайте тело ответа. Иначе исходящий запрос не будет корректно инструментирован.

#### Инструментирование запроса публикации Pub/Sub

Для Pub/Sub клиента в OpenTelemetry Go пока нет готового инструментирования. В следующем фрагменте показано, как использовать OpenTelemetry Go API для инструментирования операций публикации Pub/Sub:

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

Приведённый фрагмент распространяет исходящий спан, внедряя его в поле `Attributes` сообщения Pub/Sub. [Инструментированная Pub/Sub функция](#instrument-pubsub-handler) извлечёт этот переданный спан для связывания трассировки.

## Проверка приёма трассировок в Dynatrace

Через несколько минут после вызова Google Cloud Functions найдите спаны:

* Перейдите в **Distributed Traces** и выберите вкладку **Ingested traces**.
* Спаны войдут в состав существующей PurePath-трассировки, если корень вызова уже отслеживается OneAgent.

Если Google Cloud Function не получает трафика, трассировки отсутствуют.

## (Необязательно) Настройка захвата данных под требования конфиденциальности

Dynatrace автоматически захватывает все атрибуты OpenTelemetry, однако в веб-интерфейсе хранятся и отображаются только значения атрибутов, указанные в allowlist. Это предотвращает случайное хранение персональных данных, позволяя соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Для просмотра пользовательских атрибутов необходимо сначала разрешить их в веб-интерфейсе Dynatrace. О настройке хранения и маскирования атрибутов см. [Маскирование атрибутов](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").