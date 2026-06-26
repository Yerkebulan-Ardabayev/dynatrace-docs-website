---
title: Интеграция OpenTelemetry на Google Cloud Functions Go
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go
scraped: 2026-05-12T11:51:56.558434
---

# Интеграция OpenTelemetry на Google Cloud Functions Go

# Интеграция OpenTelemetry на Google Cloud Functions Go

* Практическое руководство
* Чтение: 8 мин
* Обновлено 16 июня 2023 г.

Пакет [`dynatrace-oss/opentelemetry-exporter-go`](https://dt-url.net/jq034sr) предоставляет API для трассировки кода Go на Google Cloud Functions и позволяет инструментировать код с помощью улучшенных трассировок OpenTelemetry от Dynatrace.

Рекомендуем использовать этот пакет. В качестве альтернативы можно инструментировать Google Cloud Functions с помощью стандартного OpenTelemetry, см. [Трассировка Google Cloud Functions в Go с OpenTelemetry](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go "Узнайте, как инструментировать Google Cloud Functions в Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace.").

## Предварительные требования

Перед использованием приведённых ниже пакетов убедитесь, что выполнены шаги **начальной настройки** из раздела [Настройка мониторинга OpenTelemetry для Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Мониторинг Google Cloud Functions с помощью OpenTelemetry и Dynatrace.").

* Dynatrace версии 1.222+
* Cloud Functions Go Runtime 1.16+
* Версия продукта Cloud Functions:

  + 1-го поколения
  + dynatrace-oss/opentelemetry-exporter-go версии 1.267+ 2-го поколения

## Установка

Выполните следующую команду в корневом каталоге вашего проекта Google Cloud Function для установки последней версии пакета [`dynatrace-oss/opentelemetry-exporter-go`](https://dt-url.net/jq034sr) с GitHub.

```
go get github.com/dynatrace-oss/opentelemetry-exporter-go/core
```

Обратите внимание: одного этого пакета недостаточно для получения улучшенных трассировок Dynatrace. Необходимо добавить дополнительный код инициализации и зависимости, как описано ниже.

## Использование

Следуйте приведённым ниже шагам для инструментирования Google Cloud Functions.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Установка зависимостей**](#dependencies)[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка OpenTelemetry**](#otel-setup)[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Инструментирование точки входа функции**](#instrument-handler)[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Инструментирование исходящих запросов**](#outgoing-instrument)

### Шаг 1 Установка зависимостей

Используйте следующие команды для добавления необходимых зависимостей OpenTelemetry и Google Cloud в функцию. Если проект уже содержит какие-либо из этих зависимостей, соответствующий вызов `go get` можно пропустить, иначе он обновит зависимость до последней версии.

```
go get go.opentelemetry.io/otel



go get go.opentelemetry.io/otel/sdk



go get github.com/GoogleCloudPlatform/functions-framework-go



go get cloud.google.com/go/compute
```

### Шаг 2 Настройка OpenTelemetry

Перед инструментированием Cloud Function необходимо выполнить некоторый код инициализации для настройки OpenTelemetry. Следующий фрагмент кода инициализирует необходимые экземпляры `DtTracerProvider` и `DtTextMapPropagator` и зарегистрирует их через OpenTelemetry API.

```
package otelsetup



import (



"go.opentelemetry.io/otel"



"go.opentelemetry.io/otel/attribute"



"go.opentelemetry.io/otel/sdk/resource"



sdk "go.opentelemetry.io/otel/sdk/trace"



semconv "go.opentelemetry.io/otel/semconv/v1.10.0"



dtTrace "github.com/dynatrace-oss/opentelemetry-exporter-go/core/trace"



)



func InitializeTracing() (*dtTrace.DtTracerProvider, error) {



r, err := resource.Merge(



resource.Default(),



resource.NewWithAttributes(



semconv.SchemaURL,



attribute.String("my.resource.attribute", "My Resource"),



),



)



tracerProvider, err := dtTrace.NewTracerProvider(



sdk.WithResource(r),



)



if err != nil {



// handle error



return nil, err



}



otel.SetTracerProvider(tracerProvider)



propagator, err := dtTrace.NewTextMapPropagator()



if err != nil {



// handle error



return nil, err



}



otel.SetTextMapPropagator(propagator)



return tracerProvider, nil



}
```

### Шаг 3 Инструментирование точки входа функции

Для Google Cloud Functions существует несколько типов триггеров. Ниже описано, как инструментировать Cloud Functions с [триггерами HTTP](https://dt-url.net/al234i0) и [триггерами Pub/Sub](https://dt-url.net/oq434w7).

Инструментирование триггера HTTP

Инструментирование триггера Pub/Sub

Если Cloud Function использует триггер HTTP, её можно инструментировать с помощью пакета [`otelhttp`](https://dt-url.net/6c634nr). Сначала установите пакет:

```
go get go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
```

Для удобства можно создать функцию-обёртку для точки входа. Следующие примеры кода содержат несколько вспомогательных функций, которые помогут задать необходимые атрибуты для спанов.

```
package instrumentation



import (



"net/http"



"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"



semconv "go.opentelemetry.io/otel/semconv/v1.7.0"



"go.opentelemetry.io/otel/trace"



"cloud.google.com/go/compute/metadata"



dtTrace "github.com/dynatrace-oss/opentelemetry-exporter-go/core/trace"



)



type HttpHandler = func(w http.ResponseWriter, r *http.Request)



func InstrumentHandler(



functionName string,



function HttpHandler,



tracerProvider *dtTrace.DtTracerProvider) HttpHandler {



// get project id and region from Google Compute Engine metadata



projectId, err := getProjectId()



if err != nil {



// handle error



}



region, err := getRegion()



if err != nil {



// handle error



}



// set at least these required attributes



opts := []trace.SpanStartOption{



trace.WithAttributes(



semconv.FaaSTriggerHTTP,



semconv.CloudProviderGCP,



semconv.CloudPlatformGCPCloudFunctions,



semconv.FaaSIDKey.String(createFaasId(projectId, region, functionName)),



semconv.FaaSNameKey.String(functionName),



semconv.CloudRegionKey.String(region),



),



}



// create instrumented handler



handler := otelhttp.NewHandler(



http.HandlerFunc(function), functionName, otelhttp.WithSpanOptions(opts...),



)



return func(w http.ResponseWriter, r *http.Request) {



// call your function handler



handler.ServeHTTP(w, r)



// flush spans



tracerProvider.ForceFlush(r.Context())



}



}



func getProjectId() (string, error) {



return metadata.ProjectID()



}



func getRegion() (string, error) {



// Returned string has the format "projects/<numeric-project-id>/regions/<region>"



fullRegion, err := metadata.Get("instance/region")



if err != nil {



return "", err



}



fullRegionSplit := strings.Split(fullRegion, "/")



region := fullRegionSplit[len(fullRegionSplit)-1]



return region, nil



}



func createFaasId(projectId, region, functionName string) string {



return fmt.Sprintf("//cloudfunctions.googleapis.com/projects/%s/locations/%s/functions/%s",



projectId, region, functionName)



}
```

Чтобы собрать всё воедино, инструментируйте точку входа Google Cloud Function следующим образом:

```
package myfunction



import (



"net/http"



"instrumentation"



"otelsetup"



"github.com/GoogleCloudPlatform/functions-framework-go/functions"



)



func init() {



// see https://cloud.google.com/functions/docs/configuring/env-var#runtime_environment_variables_set_automatically



functionName, ok := os.LookupEnv("K_SERVICE")



if !ok {



// function name not found; assign a default or treat as an error



}



if tracerProvider, err := otelsetup.InitializeTracing(); err == nil {



instrumentedHandler := instrumentation.InstrumentHandler(functionName, handler, tracerProvider)



functions.HTTP(functionName, instrumentedHandler)



} else {



// handle error, or register function anyway without instrumentation



}



}



func handler(w http.ResponseWriter, r *http.Request) {



// your code goes here



}
```

При использовании любой версии до [версии 0.37.0 пакета `otelhttp`](https://github.com/open-telemetry/opentelemetry-go-contrib/releases/tag/v1.12.0) необходимо явно вызывать `w.WriteHeader(...)` или `w.Write(...)` в обработчике HTTP-функции. Другие методы записи в `ResponseWriter`, например `fmt.Fprint(w, "OK")`, также допустимы. Обработчик функции должен выглядеть примерно так:

```
func handler(w http.ResponseWriter, r *http.Request) {



// your code goes here



// content or a status code must be written to the ResponseWriter



w.WriteHeader(http.StatusOK)



}
```

OpenTelemetry пока не предоставляет готового инструментирования для Pub/Sub, поэтому инструментирование Cloud Function с триггером Pub/Sub требует некоторой ручной настройки.

```
package instrumentation



import (



"context"



"fmt"



"go.opentelemetry.io/otel"



"go.opentelemetry.io/otel/codes"



"go.opentelemetry.io/otel/propagation"



semconv "go.opentelemetry.io/otel/semconv/v1.10.0"



"go.opentelemetry.io/otel/trace"



cloudevents "github.com/cloudevents/sdk-go/v2/event"



)



const (



pubSubHandlerInstrName = "my.company.com/my-pubsub-handler-instrumentation-name"



pubSubHandlerInstrVer  = "0.1.0"



)



type PubSubHandler = func(context.Context, shared.PubSubMessage) error



type CloudEventHandler = func(context.Context, cloudevents.Event) error



type Flusher interface {



ForceFlush(context.Context) error



}



// cloudevents.Event.Data() will contain a JSON object "message" containing



// an object that can be serialized to shared.PubSubMessage



// https://github.com/googleapis/google-cloudevents/blob/main/proto/google/events/cloud/pubsub/v1/data.proto



type MessagePublishedData struct {



Message PubSubMessage `json:"message"`



}



// https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage



type PubSubMessage struct {



Data        []byte            `json:"data"`



Attributes  map[string]string `json:"attributes"`



MessageId   string            `json:"messageId"`



PublishTime string            `json:"publishTime"`



OrderingKey string            `json:"orderingKey"`



}



func InstrumentTopicHandler(



functionName,



topicID string,



function PubSubHandler,



flush Flusher) CloudEventHandler {



// wrap the PubSubHandler into an instrumented CloudEventHandler



return func(ctx context.Context, e cloudevents.Event) error {



// extract PubSubMessage from event



msg, err := extractMessageFromEvent(e)



if err != nil {



return err



}



// begin instrumentation



ctx, span := beforePubSubHandlerInvoke(functionName, ctx, topicID, msg)



defer span.End()



// invoke handler function



err = function(ctx, msg)



// after instrumentation



afterPubSubHandlerInvoke(span, err)



flush.ForceFlush(ctx)



return err



}



}



func extractMessageFromEvent(e cloudevents.Event) (PubSubMessage, error) {



var msgPublishedData MessagePublishedData



if err := e.DataAs(&msgPublishedData); err != nil {



return PubSubMessage{}, fmt.Errorf("event.DataAs: %v", err)



}



return msgPublishedData.Message, nil



}



func beforePubSubHandlerInvoke(



functionName string,



ctx context.Context,



topicID string,



msg shared.PubSubMessage) (context.Context, trace.Span) {



// extract attributes from the PubSubMessage into a context



if msg.Attributes != nil {



propagator := otel.GetTextMapPropagator()



ctx = propagator.Extract(ctx, propagation.MapCarrier(msg.Attributes))



}



projectId, err := getProjectId()



if err != nil {



// handle error



}



region, err := getRegion()



if err != nil {



// handle error



}



opts := []trace.SpanStartOption{



trace.WithSpanKind(trace.SpanKindConsumer),



trace.WithAttributes(



semconv.FaaSTriggerPubsub,



semconv.CloudProviderGCP,



semconv.CloudPlatformGCPCloudFunctions,



semconv.MessagingSystemKey.String("gcp_pubsub"),



semconv.MessagingDestinationKey.String(topicID),



semconv.MessagingDestinationKindTopic,



semconv.MessagingOperationProcess,



semconv.MessagingMessageIDKey.String(msg.MessageId),



semconv.FaaSIDKey.String(createFaasId(projectId, region, functionName)),



semconv.FaaSNameKey.String(functionName),



semconv.CloudRegionKey.String(region),



),



}



tracer := otel.GetTracerProvider().Tracer(



pubSubHandlerInstrName,



trace.WithInstrumentationVersion(pubSubHandlerInstrVer),



)



return tracer.Start(ctx, fmt.Sprintf("%s process", topicID), opts...)



}



func afterPubSubHandlerInvoke(span trace.Span, err error) {



if err != nil {



span.RecordError(err)



span.SetStatus(codes.Error, err.Error())



}



}



func getProjectId() (string, error) {



return metadata.ProjectID()



}



func getRegion() (string, error) {



// Returned string has the format "projects/<numeric-project-id>/regions/<region>"



fullRegion, err := metadata.Get("instance/region")



if err != nil {



return "", err



}



fullRegionSplit := strings.Split(fullRegion, "/")



region := fullRegionSplit[len(fullRegionSplit)-1]



return region, nil



}



func createFaasId(projectId, region, functionName string) string {



return fmt.Sprintf("//cloudfunctions.googleapis.com/projects/%s/locations/%s/functions/%s",



projectId, region, functionName)



}
```

Затем инструментируйте точку входа Google Cloud Function следующим образом:

```
package myfunction



import (



"context"



"log"



"instrumentation"



"otelsetup"



"github.com/GoogleCloudPlatform/functions-framework-go/functions"



)



func init() {



// see https://cloud.google.com/functions/docs/configuring/env-var#runtime_environment_variables_set_automatically



functionName, ok := os.LookupEnv("K_SERVICE")



if !ok {



// function name not found; assign a default or treat as an error



}



if tracerProvider, err := otelsetup.InitializeTracing(); err == nil {



const topicID = "myexampletopic"



instrumentedHandler := instrumentation.InstrumentTopicHandler(functionName,



topicID, handler, tracerProvider)



functions.CloudEvent(functionName, instrumentedHandler)



} else {



// handle error, or register function anyway without instrumentation



}



}



func handler(ctx context.Context, msg instrumentation.PubSubMessage) error {



// your code goes here, e.g. extract data from the msg.Data payload



return nil



}
```

Приведённые примеры кода применяются к [функциям CloudEvent](https://dt-url.net/fm834cy). При использовании [*фоновых функций*](https://dt-url.net/83a34xp) потребуются небольшие адаптации: удаление объекта `MessagePublishedData` и десериализация данных события напрямую в объект `PubSubMessage`.

Инструкции по развёртыванию Cloud Function см. в разделе [Создание и развёртывание Cloud Function с помощью Google Cloud CLI](https://dt-url.net/l2c342b).

### Шаг 4 Инструментирование исходящих запросов

Если Cloud Function содержит исходящие запросы, их также можно инструментировать для достижения полной сквозной трассировки. Для инструментирования запросов используйте библиотеки инструментирования, предоставляемые OpenTelemetry.

Инструментирование исходящих запросов одинаково работает как с пакетом улучшенной трассировки Dynatrace, так и со стандартным OpenTelemetry. Инструкции по инструментированию исходящих запросов см. в разделе [Трассировка Google Cloud Functions в Go с OpenTelemetry](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#outgoing-instrument "Узнайте, как инструментировать Google Cloud Functions в Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace.").

## Сброс спанов

В приведённых выше фрагментах кода `ForceFlush` явно вызывается после каждого вызова функции для обеспечения корректного экспорта спанов.

Поскольку сброс спанов становится частью логики выполнения функции, это увеличивает время выполнения. Чтобы избежать этого, можно пропустить вызов `ForceFlush`: спаны всё равно будут периодически экспортироваться в фоновом режиме.

Поскольку код, выполняющийся за пределами выполнения функции, может быть завершён в любой момент, Google Cloud Functions не рекомендует такой подход.

* Google Cloud Functions 1-го поколения

  Выполнение фоновых задач после вызова функции без сброса спанов не гарантировано и может привести к потере спанов. На практике примеры показали, что отсутствие явного сброса спанов, как правило, всё равно приводит к их корректному экспорту.
* Google Cloud Functions 2-го поколения

  Google Cloud Functions 2-го поколения может обрабатывать несколько одновременных запросов в одном экземпляре функции. Операция сброса одного вызова может увеличить время выполнения другого вызова функции.
  Поскольку экземпляры функций обычно должны некоторое время оставаться в режиме ожидания для обработки нескольких одновременных запросов, можно отключить сброс спанов для повышения производительности. Подробнее см. [Жизненный цикл экземпляра](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Обратите внимание: простаивающим экземплярам функций не гарантировано выделение CPU, если их режим [выделения CPU](https://cloud.google.com/run/docs/configuring/cpu-allocation) не установлен в `CPU always allocated`.

  Подробнее см. [Временная шкала выполнения функции](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Накладные расходы Dynatrace

* Поскольку экспорт спанов и получение метаданных занимают некоторое время при холодных стартах, они увеличивают продолжительность выполнения функции и, следовательно, повышают затраты.
* Обратите внимание на редко вызываемые функции (как правило, с холодными стартами): им может потребоваться больше времени для TCP-рукопожатия при экспорте спанов.
* Любые сетевые проблемы между экспортером и бэкендом Dynatrace могут также привести к неожиданно высоким накладным расходам.

## Связанные темы

* [Настройка мониторинга OpenTelemetry для Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Мониторинг Google Cloud Functions с помощью OpenTelemetry и Dynatrace.")
* [Трассировка Google Cloud Functions в Go с OpenTelemetry](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go "Узнайте, как инструментировать Google Cloud Functions в Go с помощью OpenTelemetry и экспортировать трассировки в Dynatrace.")
* [Настройка Dynatrace на Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
* [Мониторинг Google Cloud](https://www.dynatrace.com/technologies/google-cloud-monitoring/)