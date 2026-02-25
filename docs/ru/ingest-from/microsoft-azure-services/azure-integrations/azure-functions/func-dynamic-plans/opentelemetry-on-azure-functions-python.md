---
title: Trace Azure Functions written in Python
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python
scraped: 2026-02-25T21:25:03.469940
---

# Trace Azure Functions written in Python

# Trace Azure Functions written in Python

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Jul 13, 2022

The [`dynatrace-opentelemetry-azure-functions` packageï»¿](https://pypi.org/project/dynatrace-opentelemetry-azure-functions) provides APIs for tracing Python Azure Functions.

## Prerequisites

Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.") before using the packages below.

* dynatrace-opentelemetry-azure-functions version 1.245+

## Installation

To set up OpenTelemetry Python integration on Azure Functions, add the following line to the `requirements.txt` file of your function app:

```
dynatrace-opentelemetry-azure-functions
```

This adds the latest version of the `dynatrace-opentelemetry-azure-functions` package as a dependency to your function app. For more information about managing dependencies, consult the [Azure Functions Python developer guideï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#package-management).

## Trace export

To export traces to Dynatrace, you need to [initialize tracing](#initialize) and then [instrument your handler functions](#instrument).

### Initialize tracing

Select one of the two ways below to initialize tracing.

* `configure_dynatrace` functionâThis is the recommended option unless you need to manually set up the tracing components.
* Manual tracing setupâThis allows for a more fine-grained setup of tracing components.

Because it's possible to bundle several Azure Functions into a single Azure Function app, it's important to initialize tracing only once per Azure Function app instead of once per function. The simplest way to do this is to put the tracing setup code into a shared file as described in the [Azure Functions Python developer guideï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#folder-structure) and import it at the top of the files that define a function.

Example with `configure_dynatrace` (recommended)

```
from opentelemetry.sdk.resources import Resource



from opentelemetry.semconv.resource import ResourceAttributes



from dynatrace.opentelemetry.tracing.api import configure_dynatrace



tracer_provider = configure_dynatrace(



resource=Resource.create({"my.resource.attribute": "My Resource"})



)
```

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

#### Programming model v1

Use the `wrap_handler` decorator to instrument your handler function, as shown in the example below:

```
from azure import functions as func



# import the wrap_handler decorator



from dynatrace.opentelemetry.azure.functions import wrap_handler



@wrap_handler



def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:



# From here the created span is available in the OpenTelemetry context as the current span.



# do something ...



return  func.HttpResponse(f"Hello world.", status_code=200)
```

The [contextï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#context) parameter is optional and can be omitted from the handler's signature.

If your HTTP function handler doesn't return an explicit result and uses multiple `Out` bindings, you should provide the name of the response binding as a binding hint to the decorator, so that result attributes can be properly set on the span.

Example:

```
from azure import functions as func



# import the wrap_handler decorator



from dynatrace.opentelemetry.azure.functions import wrap_handler



@wrap_handler(http_result_param_name="res")



def main(req: func.HttpRequest, other: func.Out[str], res: func.Out[func.HttpResponse]):



# do something ...



res.set(func.HttpResponse(f"Hello world.", status_code=200))
```

#### Programming model v2

Functions implemented using the [v2 programming modelï»¿](https://dt-url.net/ix03806) can also be instrumented using the `wrap_handler` decorator.

Because the Azure functions framework for programming model V2 uses decorators to mark handler functions, the order in which the `wrap_handler` and the Azure decorators are applied is important.
The snippet below shows the correct order: the handler needs to be decorated with `wrap_handler` before the `app.route` decorator.

```
import azure.functions as func



# import the wrap_handler decorator



from dynatrace.opentelemetry.azure.functions import wrap_handler



app = func.FunctionApp()



@app.function_name("MyHttpFunc")



@app.route(route="hello")



@wrap_handler # Note: wrap_handler must be located after the app.route decorator, so it's executed first.



def main(req: func.HttpRequest) -> func.HttpResponse:



# do something ...



return func.HttpResponse("Hello world", status_code=200)
```

## Limitations

* The Azure runtime dynamically passes the [invocation contextï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#context) argument to your handler function if the handler's signature contains a parameter with name `context`. However, if there's also a binding with the name `context` in your `function.json` file, the invocation context is ignored by the binding and the binding is passed instead. The `wrap_handler` decorator won't work in this case, since it requires the invocation context to extract certain span attributes. Be sure not to use the name `context` for any binding in your `function.json` file.
* HTTP handler functions with multiple `Out` bindings and no explicit return result should provide the name of the response output binding to the function decorator, so that result span attributes can be properly set.
* `DtSpanProcessor` only works together with `DtSampler`. Make sure to set `DtSampler` as a sampler when manually setting up tracing; spans might not be exported otherwise.
* Instrumentation of [WSGI and ASGIï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?pivots=python-mode-decorator#web-frameworks) web frameworks is currently not supported for the v2 programming model because of the handler's different signature.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")
* [Azure monitoringï»¿](https://www.dynatrace.com/technologies/azure-monitoring/)