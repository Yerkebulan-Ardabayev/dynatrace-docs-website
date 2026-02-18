---
title: Trace Google Cloud Functions in Go with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go
scraped: 2026-02-18T21:28:55.925006
---

# Trace Google Cloud Functions in Go with OpenTelemetry

# Trace Google Cloud Functions in Go with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 9-min read
* Updated on Nov 13, 2023

This guide shows how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace. To learn more about how Dynatrace works with OpenTelemetry, see [OpenTelemetry and Dynatrace](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

To learn about how to monitor Google Cloud Functions with Dynatrace-enhanced OpenTelemetry traces, see [Integrate on Google Cloud Functions GoLang](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go "Monitor Google Cloud Functions with OpenTelemetry for Go and Dynatrace.").

## Prerequisites

The following prerequisites and limitations apply:

* Dynatrace version 1.222+
* W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.
* Cloud Functions Go Runtime 1.16+

## Instrument Google Cloud Functions

Dynatrace uses OpenTelemetry Trace Ingest to provide end-to-end visibility to your Google Cloud Functions.

To instrument your Google Cloud Functions

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Add OpenTelemetry dependencies**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#otel-dependencies "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Set up OpenTelemetry**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#otel-setup "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Instrument the function entry point**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#instrument-handler "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Instrument outgoing requests**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#outgoing-instrument "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.")

### Step 1 Add OpenTelemetry dependencies

Use the following commands to add the required OpenTelemetry dependencies to your function:

```
go get go.opentelemetry.io/otel



go get go.opentelemetry.io/otel/sdk



go get go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp
```

### Step 2 Set up OpenTelemetry

To make sure traces are collected, linked, and exported to Dynatrace, you need to set up and configure OpenTelemetry accordingly. For this, the Dynatrace endpoint and an authentication token are required.

To determine the endpoint

1. Open Dynatrace.
2. Check the address line of your browser. The URL will match one of the following patterns:

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/...`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/...`
3. Replace the `...` part with `api/v2/otlp` to get the URL you will need to configure the OpenTelemetry exporter.

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/api/v2/otlp`

To create an authentication token

1. Go to **Access Tokens** > **Generate new token**.
2. Provide a **Token name**.
3. In the **Search scopes** box, search for `Ingest OpenTelemetry traces` and select the checkbox.
4. Select **Generate token**.
5. Select **Copy** to copy the token to your clipboard.
6. Save the token in a safe place; you can't display it again, and you will need it to configure the OpenTelemetry exporter.

Here is how to set up the OpenTelemetry tracing pipeline:

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

To configure the exporter to your tenant, add the following environment variables when deploying your Google Cloud function:

* `OTEL_EXPORTER_OTLP_ENDPOINT`: set it to the previously determined endpoint.
* `OTEL_EXPORTER_OTLP_HEADERS`: set it to `Authorization=Api-Token <TOKEN>`, where `<TOKEN>` is the previously created authentication token.

Alternatively, the endpoint and authentication token can be configured in code by providing them as options to `otlptracehttp.NewClient`.

### Step 3 Instrument the function entry point



To instrument invocations to a Google Cloud Function with OpenTelemetry, you need to

1. Create a span around the entry point of the function to trace invocations.
2. Extract and link the parent span from the propagated context. (To learn about W3C Trace Context, see our [W3C Trace Contextï»¿](https://engineering.dynatrace.com/open-source/standards/w3c-trace-context/) introduction.)

For certain libraries, OpenTelemetry Go already provides [instrumentationsï»¿](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation) that you can use to take care of these things.

The following sections show you how to instrument certain types of Google Cloud Functions:

* [Instrument an HTTP Google Cloud Function](#instrument-http-handler)
* [Instrument a Pub/Sub Google Cloud Function](#instrument-pubsub-handler)

#### Instrument an HTTP Google Cloud Function

The entry point of an HTTP Google Cloud Function mostly matches the standard `http.Handler` interface. OpenTelemetry Go already provides an instrumentation for this interface. To add it as a dependency to your function, use the following command:

```
go get go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
```

Because this instrumentation works with an `http.Handler` interface, it requires your entry point function to have the name `ServeHTTP`. Also, because the Go Runtime might terminate right after a function invocation, spans must be exported to Dynatrace beforehand.

To take care of this, create a wrapper function that instruments your actual handler and flushes the spans after invocation:

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

Putting everything together, here is how you use it in your function:

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

When deploying your function to GCP, make sure to use `InstrumentedHandler` as the entry point to your Google Cloud Function.

#### Instrument a Pub/Sub Google Cloud Function

A Pub/Sub Google Cloud Function is triggered by the [Pub/Sub messageï»¿](https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) event. The event is unmarshalled by GCP into a message object that matches the type you defined in the entry point of your function. This type usually looks similar to the following:

```
type PubSubMessage struct {



Data        []byte            `json:"data"`



Attributes  map[string]string `json:"attributes"`



MessageId   string            `json:"messageId"`



PublishTime string            `json:"publishTime"`



OrderingKey string            `json:"orderingKey"`



}
```

OpenTelemetry currently does not provide an instrumentation for Pub/Sub, so instrumenting a Pub/Sub Google Cloud Function requires a little more work.

In the following snippet, you can see how to create a wrapper function that instruments invocations to your Pub/Sub handler. This wrapper creates the corresponding span and uses the `Attributes` map on the `PubSubMessage` to extract and link to the parent span from the propagated context.

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

Putting everything together, here is how to use the instrumented handler in your function:

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

When deploying your function to GCP, make sure to use `InstrumentedHandler` as the entry point to your Google Cloud Function.

### Step 4 Instrument outgoing requests



To achieve end-to-end tracing, it is important to also make sure your outgoing requests are instrumented.

The following sections show how to instrument certain outgoing requests:

* [Instrument outgoing HTTP requests](#outgoing-http-instrument)
* [Instrument Pub/Sub publish requests](#pubsub-publish-instrument)

OpenTelemetry Go uses `context.Context` to link a newly created span to its parent, so when using an instrumentation or creating a span manually, make sure to pass it the `context.Context` instance that was passed to your Google Cloud Function (or an instance derived from it). Otherwise, your trace will not be linked properly.

#### Instrument outgoing HTTP requests

OpenTelemetry Go provides an instrumentation for tracing outgoing HTTP calls. Add it as a dependency to your function by using the following command:

```
go get go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
```

Here is how you can use this instrumentation in your code:

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

* Do not use convenience functions such as `GET` or `POST` on the standard `http.Client`, because they do not accept a `context.Context` object. To make sure that your HTTP request is properly linked, either create a request with a context object as in the sample above, or use one of the convenience functions (such as `otelhttp.Get` or `otelhttp.Put`) of the HTTP instrumentation.
* Make sure to close or fully read the response body. Otherwise, the outgoing request will not be instrumented properly.

#### Instrument Pub/Sub publish request

For the Pub/Sub client, there is currently no instrumentation in OpenTelemetry Go. Check out the following snippet to see how you can use the OpenTelemetry Go API to instrument Pub/Sub publish operations:

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

The above snippet propagates the outgoing span by injecting it into the `Attributes` field on the Pub/Sub message. An [instrumented Pub/Sub function](#instrument-pubsub-handler) will extract this propagated span to link the trace together.

## Verify that the traces are ingested into Dynatrace

A few minutes after invoking your Google Cloud Functions, look for your spans:

* Go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab.
* Your spans will be part of an existing PurePath distributed trace if the root of your call is already being monitored by the OneAgent.

If your Google Cloud Function is not getting any traffic, there will be no traces.

## (Optional) Configure data capture to meet privacy requirements

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").