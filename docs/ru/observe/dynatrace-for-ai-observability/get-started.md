---
title: Get started
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/get-started
scraped: 2026-02-22T21:19:41.214373
---

# Get started

# Get started

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Feb 04, 2026

The Dynatrace Full-Stack observability platform combined with Traceloop's OpenLLMetry OpenTelemetry SDK can seamlessly provide comprehensive insights into large language models (LLMs) in production environments. By observing AI models, businesses can make informed decisions, optimize performance, and ensure compliance with emerging AI regulations.

## Create a Dynatrace token

Create a Dynatrace token so you can report AI observability data to your Dynatrace tenant.

Create a Dynatrace Token

To create a Dynatrace token

1. In Dynatrace, go to **Access Tokens**.  
   To find **Access Tokens**, press **Ctrl/Cmd+K** to search for and select **Access Tokens**.
2. In **Access Tokens**, select **Generate new token**.
3. Enter a **Token name** for your new token.
4. Give your new token the following permissions:
5. Search for and select all of the following scopes.

   * **Ingest metrics** (`metrics.ingest`)
   * **Ingest logs** (`logs.ingest`)
   * **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`)
6. Select **Generate token**.
7. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

## Instrument your application

Choose your instrumentation framework and language to get started.

The Dynatrace backend exclusively works with delta values and requires the respective aggregation temporality. Set the `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` environment variable to `DELTA`.

OpenLLMetry

OpenTelemetry

OpenLLMetry provides auto-instrumentation for popular AI frameworks and automatically collects GenAI semantic conventions.

Python

Node.js

We can leverage OpenTelemetry to provide autoinstrumentation that collects traces and metrics of your AI workloads, particularly [OpenLLMetryï»¿](https://dt-url.net/0sa3uau) that can be installed with the following command:

```
pip install traceloop-sdk
```

Afterward, add the following code at the beginning of your main file.

```
from traceloop.sdk import Traceloop



headers = { "Authorization": "Api-Token <YOUR_DT_API_TOKEN>" }



Traceloop.init(



app_name="<your-service>",



api_endpoint="https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp", # or OpenTelemetry Collector URL



headers=headers



)
```

We can leverage OpenTelemetry to provide autoinstrumentation that collects traces and metrics of your AI workloads, particularly [OpenLLMetryï»¿](https://dt-url.net/0sa3uau) that can be installed with the following command:

```
npm i @opentelemetry/exporter-trace-otlp-proto @traceloop/node-server-sdk
```

Afterward, add the following code at the beginning of your main file.

```
import {OTLPTraceExporter} from "@opentelemetry/exporter-trace-otlp-proto";



import * as traceloop from "@traceloop/node-server-sdk";



const exporter = new OTLPTraceExporter({



url: "https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp", // or OpenTelemetry Collector URL



headers: { Authorization: "Api-Token <YOUR_DT_API_TOKEN>" },



});



traceloop.initialize({



appName: "<your-service>",



exporter: exporter



});
```

Currently, OpenLLMetry for Node.js doesn't support Metrics.

OpenTelemetry provides flexible instrumentation that you can customize for your specific needs. For more details on the GenAI semantic conventions, see [OpenTelemetry](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

Python

Node.js

Install the required packages:

```
pip install opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
```

Configure the OpenTelemetry SDK:

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

Install the required packages:

```
npm install @opentelemetry/sdk-node @opentelemetry/api @opentelemetry/exporter-trace-otlp-proto
```

Configure the OpenTelemetry SDK:

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