---
title: Integrate on Google Cloud Functions GoLang
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go
---

# Integrate on Google Cloud Functions GoLang

# Integrate on Google Cloud Functions GoLang

* How-to guide
* 8-min read
* Updated on Jun 16, 2023

The [`dynatrace-oss/opentelemetry-exporter-go`﻿](https://dt-url.net/jq034sr) package provides an API for tracing Go code on Google Cloud Functions. This package provides a way to instrument your code with Dynatrace-enhanced OpenTelemetry traces.

We recommend using this package. As an alternative, you can instrument your Google Cloud Functions with plain OpenTelemetry, see [Trace Google Cloud Functions in Go with OpenTelemetry](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.").

## Prerequisites

Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.") before using the packages below.

* Dynatrace version 1.222+
* Cloud Functions Go Runtime 1.16+
* Cloud Functions product version:

  + 1st gen
  + dynatrace-oss/opentelemetry-exporter-go version 1.267+ 2nd gen

## Installation

Run the following command in the root directory of your Google Cloud Function project to install the latest version of the [`dynatrace-oss/opentelemetry-exporter-go`﻿](https://dt-url.net/jq034sr) package from GitHub.

```
go get github.com/dynatrace-oss/opentelemetry-exporter-go/core
```

Note that this package by itself is not enough to get Dynatrace-enhanced traces. Further initialization code and dependencies need to be added, as described below.

## Usage

Follow the steps below to instrument your Google Cloud Functions.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Install dependencies**](#dependencies)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Set up OpenTelemetry**](#otel-setup)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Instrument the function entry point**](#instrument-handler)[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Instrument outgoing requests**](#outgoing-instrument)

### Step 1 Install dependencies

Use the following commands to add the required OpenTelemetry and Google Cloud dependencies to your function. If your project already contains any of these dependencies, you might want to skip the corresponding `go get` call, otherwise, it will upgrade you to the latest version of the dependency.

```
go get go.opentelemetry.io/otel



go get go.opentelemetry.io/otel/sdk



go get github.com/GoogleCloudPlatform/functions-framework-go



go get cloud.google.com/go/compute
```

### Step 2 Set up OpenTelemetry

Some initialization code is required to set up OpenTelemetry before you can start instrumenting your Cloud Function. The following code snippet will initialize the required `DtTracerProvider` and `DtTextMapPropagator` instances, and register them via the OpenTelemetry API.

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

### Step 3 Instrument the function entry point

There are several trigger types for Google Cloud Functions. See below how to instrument Cloud Functions with [HTTP triggers﻿](https://dt-url.net/al234i0) and [Pub/Sub triggers﻿](https://dt-url.net/oq434w7).

Instrument HTTP trigger

Instrument Pub/Sub trigger

When your Cloud Function has an HTTP trigger, you can instrument it with the help of the [`otelhttp`﻿](https://dt-url.net/6c634nr) package. First, install the package:

```
go get go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp
```

For ease of use, you can create a wrapper function for your entry point. The following code samples contain several utility functions which will help you set the required attributes on your spans.

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

To put everything together, instrument your Google Cloud Function entry point as follows:

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

When using any version before [version 0.37.0 of the `otelhttp` package﻿](https://github.com/open-telemetry/opentelemetry-go-contrib/releases/tag/v1.12.0), it is required to explicitly call `w.WriteHeader(...)` or `w.Write(...)` in your HTTP function handler. Other methods which write content to the `ResponseWriter`, such as `fmt.Fprint(w, "OK")`, are also valid. Your function handler should then look something like this:

```
func handler(w http.ResponseWriter, r *http.Request) {



// your code goes here



// content or a status code must be written to the ResponseWriter



w.WriteHeader(http.StatusOK)



}
```

OpenTelemetry currently doesn't provide out-of-the-box instrumentation for Pub/Sub, so instrumenting a Pub/Sub triggered Cloud Function requires some manual configuration.

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

Then, instrument your Google Cloud Function entry point as follows:

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

The code samples above apply to [CloudEvent functions﻿](https://dt-url.net/fm834cy). The code would require minor adaptations, such as removing the `MessagePublishedData` object and unmarshalling the event data directly to a `PubSubMessage` object, when using [*background functions*﻿](https://dt-url.net/83a34xp).

For instructions on how to deploy your Cloud Function, see [Create and deploy a Cloud Function by using the Google Cloud CLI﻿](https://dt-url.net/l2c342b).

### Step 4 Instrument outgoing requests

If you have any outgoing requests in your Cloud Function, you can instrument them as well to achieve full end-to-end tracing. Your requests can be instrumented by using instrumentation libraries provided by OpenTelemetry.

Instrumenting outgoing requests works equivalently with the Dynatrace-enhanced tracing package and plain OpenTelemetry. For instructions on how to instrument outgoing requests, see [Trace Google Cloud Functions in Go with OpenTelemetry](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go#outgoing-instrument "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.").

## Span flush

In the code snippets above, `ForceFlush` is explicitly called after every function invocation to ensure that spans are exported properly.

Because flushing spans becomes part of the function's execution logic, it results in longer execution times. To avoid this, you can omit the call to `ForceFlush`. Spans will still be periodically exported in the background.

Because code running outside the function execution can be terminated at any time, it's discouraged by Google Cloud Functions.

* Google Cloud Functions 1st gen

  Background task execution after function invocation is not guaranteed without flushing spans and might result in span loss. In practice, samples have shown that not explicitly flushing spans usually still results in correctly exported spans.
* Google Cloud Functions 2nd gen

  Google Cloud Functions 2nd gen can handle multiple concurrent requests in a single function instance. The flush operation of one invocation can prolong the execution time of another function invocation.
  Because function instances usually need to be kept idle for some time to handle multiple concurrent requests, you can disable the flushing of spans to improve performance. For details, see [Instance lifecycle﻿](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Note that idle function instances are not guaranteed to be allocated CPU unless their [CPU allocation﻿](https://cloud.google.com/run/docs/configuring/cpu-allocation) mode is set to `CPU always allocated`.

  For details, see [Function execution timeline﻿](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Dynatrace overhead

* Because span export and metadata fetch take some time during cold starts, they increase the duration of the function and subsequently increase costs.
* Pay attention to infrequently invoked functions (usually with cold starts), which might require more time for the TCP handshake during span export.
* Any network problem between the exporter and Dynatrace backend might also lead to unexpectedly high overhead.

## Related topics

* [Set up OpenTelemetry monitoring for Google Cloud Functions](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.")
* [Trace Google Cloud Functions in Go with OpenTelemetry](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-go "Learn how to instrument Google Cloud Functions in Go with OpenTelemetry and export the traces to Dynatrace.")
* [Set up Dynatrace on Google Cloud](/managed/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud monitoring﻿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)