---
title: Integrate on Google Cloud Functions Python
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python
scraped: 2026-02-15T09:06:02.149376
---

# Integrate on Google Cloud Functions Python

# Integrate on Google Cloud Functions Python

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Jun 16, 2023

The `dynatrace-opentelemetry-gcf` [packageï»¿](https://pypi.org/project/dynatrace-opentelemetry-gcf) provides APIs for tracing Python Google Cloud Functions (GCF).

## Prerequisites

Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.") before using the packages below.

* dynatrace-opentelemetry-gcf version 1.247+
* Cloud Functions product version: 1st gen, 2nd gen

## Installation

To set up OpenTelemetry Python integration on Google Cloud Functions, add the following line to the `requirements.txt` file of your function:

```
dynatrace-opentelemetry-gcf
```

This adds the latest version of the `dynatrace-opentelemetry-gcf` package as a dependency to your function. For more information about managing dependencies, consult the [GCF documentation for Pythonï»¿](https://cloud.google.com/functions/docs/writing/specifying-dependencies-python).

## Trace export

To export traces to Dynatrace, you need to [initialize tracing](#initialize) and then [instrument your handler function](#instrument).

### Initialize tracing

Select one of the following ways to initialize tracing:

* `configure_dynatrace` functionâThis is the recommended option unless you need to manually set up tracing components.

  Example with `configure_dynatrace` (recommended)

  ```
  from opentelemetry.sdk.resources import Resource



  from opentelemetry.semconv.resource import ResourceAttributes



  from dynatrace.opentelemetry.tracing.api import configure_dynatrace



  tracer_provider = configure_dynatrace(



  resource=Resource.create({"my.resource.attribute": "My Resource"})



  )
  ```
* Manual tracing setupâThis allows for a more fine-grained setup of tracing components.

  Example with manual tracing setup

  ```
  from opentelemetry.propagate import set_global_textmap



  from opentelemetry.sdk.resources import Resource



  from opentelemetry.sdk.trace import TracerProvider



  from opentelemetry.semconv.resource import ResourceAttributes



  from opentelemetry.trace import set_tracer_provider



  from dynatrace.opentelemetry.tracing.api import (



  DtSampler,



  DtSpanProcessor,



  DtTextMapPropagator,



  )



  span_processor = DtSpanProcessor()



  tracer_provider = TracerProvider(



  sampler=DtSampler(),



  resource=Resource.create({"my.resource.attribute": "My Resource"}),



  )



  tracer_provider.add_span_processor(span_processor)



  set_global_textmap(DtTextMapPropagator())



  set_tracer_provider(tracer_provider)
  ```

The tracing setup code should be implemented to set up tracing only once before any other third-party module is imported. If you use `isort` to sort your imports, we suggest that you [deactivate itï»¿](https://pycqa.github.io/isort/docs/configuration/action_comments.html#isort-off) while importing the tracing setup module, as shown in the following example:

```
# isort: off



import setup_tracing  # import the module containing your setup code



# isort: on



# import other modules
```

### Instrument a handler function

Use the `wrap_handler` decorator to instrument your handler function as shown in the following example:

```
import flask



from dynatrace.opentelemetry.gcf import wrap_handler



@wrap_handler



def handler(request: flask.Request) -> flask.Response:



# From here the created span is available in the OpenTelemetry context as the current span.



# do something ...



return flask.Response("Hello World", 200)
```

## Cold start

When the wrapped handler is invoked for the first time after [cold startï»¿](https://cloud.google.com/functions/docs/concepts/exec#cold_starts), the decorator will make additional HTTP requests to fetch metadata from your [Google Cloud environmentï»¿](https://cloud.google.com/compute/docs/metadata/overview). This metadata is used to set the required attributes for Dynatrace to process the span.

## Span flush

By default, the `wrap_handler` decorator automatically performs a flush operation when the decorated function exits to ensure that spans are exported properly. However, flushing spans results in longer execution time, because this operation becomes part of the function's execution logic.

By providing an additional parameter to the decorator, `@wrap_handler(flush_on_exit=False)`, you can disable the flushing after every invocation. Spans will still be periodically exported in the background.

Because code running outside the function execution can be terminated at any time, it's discouraged by Google Cloud Functions.

* Google Cloud Functions 1st gen

  Background task execution after function invocation is not guaranteed without flushing spans and might result in span loss. In practice, samples have shown that not explicitly flushing spans usually still results in correctly exported spans.
* Google Cloud Functions 2nd gen

  Google Cloud Functions 2nd gen can handle multiple concurrent requests in a single function instance. The flush operation of one invocation can prolong the execution time of another function invocation.
  Because function instances usually need to be kept idle for some time to handle multiple concurrent requests, you can disable the flushing of spans to improve performance. For details, see [Instance lifecycleï»¿](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Note that idle function instances are not guaranteed to be allocated CPU unless their [CPU allocationï»¿](https://cloud.google.com/run/docs/configuring/cpu-allocation) mode is set to `CPU always allocated`.

  For details, see [Function execution timelineï»¿](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Dynatrace overhead

* Because span export and metadata fetch take some time during cold starts, they increase the duration of the function and subsequently increase costs.
* Pay attention to infrequently invoked functions (usually with cold starts), which might require more time for the TCP handshake during span export.
* Any network problem between the exporter and Dynatrace backend might also lead to unexpectedly high overhead.

## Limitations

* `DtSpanProcessor` only works together with `DtSampler`. Make sure to set `DtSampler` as a sampler when manually setting up tracing; spans might not be exported otherwise.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud monitoringï»¿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)