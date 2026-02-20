---
title: Connecting log data to traces (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment
scraped: 2026-02-20T21:08:09.037768
---

# Connecting log data to traces (Logs Classic)

# Connecting log data to traces (Logs Classic)

* 9-min read
* Updated on Nov 25, 2025

Log Monitoring Classic

Dynatrace can enrich your ingested log data with additional information that helps Dynatrace to recognize, correlate, and evaluate the data. Log enrichment results in a more refined analysis of your logs.

For the newest Dynatrace version, see [Connect log data to traces](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.").

Log enrichment enables you to:

* Seamlessly switch context and analyze individual spans, transactions, or entire workloads
* Empower development teams by making it easier and faster for them to detect and pinpoint problems

## Enrich logs automatically

You can enable log enrichment for a particular technology used to create log data and let Dynatrace automatically inject additional attributes into every log record received. This method is recommended for structured log data of known technologies.

Limiting log enrichment

Use **Process group override** to limit log enrichment to a specific process group or a process within a process group.

### Enable/disable log enrichment for a specific technology

To enable log enrichment for a specific technology:

Globally

Process group override in OneAgent

Kubernetes namespace

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Filter for **enrichment**.
3. Enable/disable each log enrichment for each technology that you use to generate ingested log data.
4. Select **Save changes** to save your configuration.

1. Open the Process group you are looking for.
2. Select **More** (**â¦**) > **OneAgent features**.
3. Filter for **enrichment**.
4. Enable/disable each log enrichment for each technology that you use to generate ingested log data.
5. Select **Save changes** to save your configuration.

1. Go to **Infrastructure Observability** > **Kubernetes**.
2. Select the **Namespaces** value for your Kubernetes cluster.
3. Select the Kubernetes namespace record that you're interested in.
4. On the top left of the page, go to **More** (**â¦**) > **Settings** > **OneAgent features**.
5. Select **Add override**.
6. Select the log enrichment technology from the **Feature** dropdown list, and make sure that the feature override toggle is turned on.
7. Select **Save and close**.

### What does automatic log enrichment do?

Log enrichment modifies your ingested log data and adds the following information to each detected log record:

* `dt.trace_id`
* `dt.span_id`
* `dt.entity.process_group_instance`

## Supported frameworks

To see the supported frameworks for trace/span log context enrichment, go to [Technology support](/docs/ingest-from/technology-support#web-servers "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Structured log data

For structured log data such as JSON, XML, and well-defined text log formats, Dynatrace adds an attribute field to the log record entry.

### Example of enriched log data in JSON format

Log data in JSON format is enriched with additional `<dt.trace_id>`, `<dt.span_id>`, and `dt.entity.process_group_instance` properties.

```
{



"severity": "error",



"time": 1638957438023,



"pid": 1,



"hostname": "paymentservice-788946fdcd-42lgq",



"name": "paymentservice-charge",



"dt.trace_id": "d04b42bc9f4b6ecdbf6bc9f4b6ecdbc",



"dt.span_id": "9adc716eb808d428",



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-27204EFED3D8466E",



"message": "Unsupported card type for cardNumber=************0454"



}
```

### Example of enriched log data in XML format

Log data in XML format is enriched with additional `<dt.trace_id>`, `<dt.span_id>`, and `<dt.entity.process_group_instance>` nodes.

```
<?xml version="1.0" encoding="windows-1252" standalone="no"?>



<record>



<date>2021-08-24T14:41:36.565218700Z</date>



<millis>1629816096565</millis>



<nanos>218700</nanos>



<sequence>0</sequence>



<logger>com.apm.testapp.logging.jul.XMLLoggingSample</logger>



<level>INFO</level>



<class>com.apm.testapp.logging.jul.BaseLoggingSample</class>



<method>info</method>



<thread>1</thread>



<message>Update completed successfully.</message>



<dt.trace_id>513fcd4e9b08792fcd4e9b08792</dt.trace_id>



<dt.span_id>125840e3125840e3</dt.span_id>



<dt.entity.process_group_instance>PROCESS_GROUP_INSTANCE-27204EFED3D8466E</dt.entity.process_group_instance>



</record>
```

## Unstructured log data

Check if Dynatrace log enrichment has an impact on your existing log data pipeline before using automatic log enrichment on unstructured log data.

Unstructured log data is typically made of raw plain text that is sequentially ordered and is designed to be read by people. Dynatrace does not automatically enrich unstructured log data. Dynatrace is able to enrich unstructured log data, but appending additional information to log data may have an impact on third-party tools that consume that same log data.

### Example of enriched log data in raw text format

Log data in raw text is enriched with an additional `[!dt dt.trace_id=$trace_id, dt.span_id=$span_id, dt.entity.process_group_instance=$dt.entity.process_group_instance]` string (attributes and their value).

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=aa764ee37ebaa764ee37eaa764ee37e,dt.span_id=b93ede8b93ede8, dt.entity.process_group_instance=PROCESS_GROUP_INSTANCE-27204EFED3D8466E]
```

## Enrich logs manually

OneAgent version 1.239+

You can manually enrich your Dynatrace ingested log data by defining a log pattern to include the `dt.span_id`, `dt.trace_id`, `dt.trace_sampled`, and `dt.entity.process_group_instance` fields. You can enable manual log enrichment for a specific technology by following the [Log enrichment steps](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment#enableenr "Learn how you can connect your incoming log data to traces for more precise Dynatrace analysis.").

Be sure to follow these rules for the format of the enriched fields in an unstructured log:

* Fields must be encapsulated in square brackets (`[]`) with a `!dt` prefix.  
  For example, `[!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id, dt.entity.process_group_instance=$dt.entity.process_group_instance]`
* Fields must be formatted without double quotes.
* Any invalid characters for the field and field value must be escaped.
* Any control characters like `\n` must be excluded from the enrichment definition.

### Example of manually enriching NGINX log data

Suppose you want to manually enrich your NGINX log data with `dt.trace_id`, `dt.span_id` and `dt.trace_sampled`. The NGINX configuration file contains numerous standard NGINX variables, your log format definition must be in the `log_format` section. For example:

```
log_format custom '$remote_addr - [$time_local] $request $status $body_bytes_sent [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled]';



access_log logs/access.log custom;
```

The result will be an `access.log` file containing the enriched log records:

```
127.0.0.1 - [22/Mar/2022:08:50:45 +0100] GET /index.htm HTTP/1.1 200 30 [!dt dt.trace_id=b9e5c9ec08be5fab5071d76f427be7da,dt.span_id=43c5bb9432593963,dt.trace_sampled=true]



127.0.0.1 - [22/Mar/2022:08:50:45 +0100] GET /index.htm HTTP/1.1 200 30 [!dt dt.trace_id=01e52950b145d97bf22345e68c5e6c58,dt.span_id=de819d856eecb236,dt.trace_sampled=true]
```

For OneAgent version 1.237 and earlier, the NGINX variables used are different. For example:

```
log_format custom '$remote_addr - [$time_local] $request $status $body_bytes_sent [!dt dt.trace_id=$trace_id,dt.span_id=$span_id]'; access_log logs/access.log custom
```

The result will be an `access.log` file containing the enriched log records:

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=e1c0afeb0b8a91d7748139aa764ee37e,dt.span_id=e5e6748fab93ede8]



127.0.0.1 - [21/Oct/2021:10:33:31 +0200] GET /index.html HTTP/1.1 200 1056 [!dt dt.trace_id=81fe7816ba6c38f7aa09aef3684cd941,dt.span_id=3bdacc466ae073cd]
```

If you use a logging framework and log formatter that allows custom log patterns, you can adapt the pattern in the log formatter and directly access the Dynatrace enrichment attributes.

### Example of manually enriching Log4j log data

In the **Log4j** PatternFormatter, you can specify a pattern like this to include Dynatrace enrichment information:

```
<PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} dt.trace_id=%X{dt.trace_id} dt.span_id=%X{dt.span_id} dt.entity.process_group_instance=%X{dt.entity.process_group_instance} - %msg%n"/>
```

### Example of manually enriching Logstash Logback encoder



Logback is a successor to the log4j project. Logstash Logback is an extension that provides logback encoders, layouts, and appenders to log in JSON and other formats supported by Jackson.

The following is an example of manual enrichment using the Logstash encoder. Note the additional `mdc` property in the configuration file, where you can include MDC variables.

```
<appender name="COMPOSITEJSONENCODER" class="ch.qos.logback.core.FileAppender">



<file>compositejsonencoder.log</file>



<encoder class="net.logstash.logback.encoder.LoggingEventCompositeJsonEncoder">



<providers>



<timestamp>



<fieldName>timestamp</fieldName>



<timeZone>UTC</timeZone>



</timestamp>



<loggerName>



<fieldName>logger</fieldName>



</loggerName>



<logLevel>



<fieldName>level</fieldName>



</logLevel>



<threadName>



<fieldName>thread</fieldName>



</threadName>



<mdc>



<includeMdcKeyName>dt.span_id</includeMdcKeyName>



<includeMdcKeyName>dt.trace_id</includeMdcKeyName>



<includeMdcKeyName>dt.entity.host</includeMdcKeyName>



</mdc>



<stackTrace>



<fieldName>stackTrace</fieldName>



<!-- maxLength - limit the length of the stack trace -->



<throwableConverter class="net.logstash.logback.stacktrace.ShortenedThrowableConverter">



<maxDepthPerThrowable>200</maxDepthPerThrowable>



<maxLength>14000</maxLength>



<rootCauseFirst>true</rootCauseFirst>



</throwableConverter>



</stackTrace>



<message />



<throwableClassName>



<fieldName>exceptionClass</fieldName>



</throwableClassName>



</providers>



</encoder>



</appender>
```

### Example of manually enriching log data for winston (Node.js)

To enable log enrichment for winston, turn on the [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **Node.js - Trace/span context enrichment for unstructured logs**. You can adapt the winston transport to control the exact location where the enrichment should be added, as in the code example below.

```
const winston = require("winston");



const Transport = require("winston-transport");



class CustomTransport extends Transport {



log(info, next) {



let myLogLine = `MyLogLine: ${info.timestamp} level=${info.level}: ${info.message}`;



// this is important as above line only picks timestamp, level and message but nothing else from metadata



if (info["dt.trace_id"]) {



myLogLine = `[!dt dt.trace_id=${info["dt.trace_id"]},dt.span_id=${info["dt.span_id"]},dt.trace_sampled=${info["dt.trace_sampled"]}] ${myLogLine}`;



}



console.log(myLogLine);



next();



}



}



const logger = winston.createLogger({



level: "info",



format: winston.format.timestamp(),



transports: [



new CustomTransport(),



// this transport includes all metadata (including dynatrace added traceId,..)



new winston.transport.Console({



format: winston.format.simple()



})



]



})
```

## NGINX ingress with Kubernetes

You can enrich your logs using NGINX ingress with Kubernetes in two steps:

1. Execute the [ingress-nginx on Kubernetes](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx "Instrument ingress-nginx on Kubernetes") instrumentation instructions.
2. Add the command below to the `configmap.yaml` file for NGINX ingress.

   Adding the `main-snippet` line enables OneAgent ingestion and is optional if you have followed the manual instrumentation instructions already.

```
main-snippet: load_module /opt/dynatrace/oneagent/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;



log-format-upstream: '$remote_addr - $remote_user [$time_local] "$request" [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled] $status $body_bytes_sent  "$http_referer" "$http_user_agent" $request_length'
```

Example of configmap.yaml file

```
apiVersion: v1



kind: Namespace



metadata:



name: prod-ingress-nginx



labels:



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



---



# Source: ingress-nginx/templates/controller-serviceaccount.yaml



apiVersion: v1



kind: ServiceAccount



metadata:



labels:



helm.sh/chart: ingress-nginx-4.0.6



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



app.kubernetes.io/version: 1.0.4



app.kubernetes.io/managed-by: Helm



app.kubernetes.io/component: controller



name: ingress-nginx



namespace: prod-ingress-nginx



automountServiceAccountToken: true



---



# Source: ingress-nginx/templates/controller-configmap.yaml



apiVersion: v1



kind: ConfigMap



metadata:



labels:



helm.sh/chart: ingress-nginx-4.0.6



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



app.kubernetes.io/version: 1.0.4



app.kubernetes.io/managed-by: Helm



app.kubernetes.io/component: controller



name: ingress-nginx-controller



namespace: prod-ingress-nginx



data:



allow-snippet-annotations: 'true'



main-snippet: load_module /opt/dynatrace/oneagent/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;



log-format-upstream: '$remote_addr - $remote_user [$time_local] "$request" [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled] $status $body_bytes_sent  "$http_referer" "$http_user_agent" $request_length'



...
```

## Retrieve span and trace IDs



To have Dynatrace match logs to corresponding traces, you can include the span and trace IDs in your log messages, using the `[!dt]` notation.

The following examples show how to obtain the span and trace IDs with OpenTelemetry or the OneAgent SDK:

Python with OpenTelemetry

JavaScript (Node.js) with OpenTelemetry

Java with OpenTelemetry

Go with the OneAgent SDK

In the example below, a `dt_log` function has been created to enrich a given log message with `trace_id` and `span_id` information. Printing this enriched message to the configured log sink associates the log message with the currently active span in the Dynatrace web UI.

```
import logging



from opentelemetry import trace



def dt_log(self, record):



if (not self.disabled) and self.filter(record):



ctx = trace.get_current_span().get_span_context()



if ctx.is_valid:



trace_id = "{0:032X}".format(ctx.trace_id)



span_id = "{0:016X}".format(ctx.span_id)



record.msg = f"[!dt dt.trace_id={trace_id},dt.span_id={span_id}] - {record.msg}"



self.callHandlers(record)



logging.Logger.handle = dt_log



def lambda_handler(event, context):



logger = logging.getLogger()



logger.warning("Hello world")



return {



"statusCode": 200,



"body": "Hello from lambda"



}
```

In the example below, a `dt_log` function has been created to enrich a given log message with `trace_id` and `span_id` information. Printing this enriched message to `stdout` associates the log message with the currently active span in the Dynatrace web UI.

```
const opentelemetry = require('@opentelemetry/api');



function dtLog(msg) {



const spanContext = opentelemetry.trace.getSpanContext(opentelemetry.context.active()) ?? opentelemetry.INVALID_SPAN_CONTEXT;



console.log(`[!dt dt.trace_id=${spanContext.traceId},dt.span_id=${spanContext.spanId}] - ${msg}`);



}



exports.handler = function(event, context) {



const msg = "Hello World"



dtLog(msg);



context.succeed({



statusCode: 200,



body: msg



});



};
```

In the example below, a `dtLog` method has been created to enrich a given log message with `TraceId` and `SpanId` information. Printing this enriched message via `System.out` associates the log message with the currently active span in the Dynatrace web UI.

```
package com.amazonaws.lambda.demo;



import com.amazonaws.services.lambda.runtime.Context;



import com.amazonaws.services.lambda.runtime.RequestHandler;



import io.opentelemetry.api.trace.Span;



import io.opentelemetry.api.trace.SpanContext;



public class HelloJava implements RequestHandler<Object, String> {



private static void dtLog(final String msg) {



SpanContext spanContext = Span.current().getSpanContext();



System.out.printf(



"[!dt dt.trace_id=%s,dt.span_id=%s] - %s%n",



spanContext.getTraceId(),



spanContext.getSpanId(),



msg



);



}



@Override



public String handleRequest(Object input, Context context) {



String msg = "Hello World";



dtLog(msg);



return msg;



}



}
```

In the example below, the HTTP handler uses `Printf()` to log the response to standard output and enriches that information with the trace and span IDs, obtained from `oneagentsdk.GetTraceContextInfo()`. Printing this enriched message associates the log message with the currently active span in the Dynatrace web UI.

```
package main



import (



"fmt"



"log"



"net/http"



"github.com/Dynatrace/OneAgent-SDK-for-Go/sdk"



)



func main() {



// Create OneAgent SDK API instance



var oneagentsdk = sdk.CreateInstance()



http.HandleFunc("/", func(w http.ResponseWriter, _ *http.Request) {



// Get TraceContextInfo within the incoming HTTP request



// to obtain Trace ID and Span ID of the active distributed trace context



traceContext := oneagentsdk.GetTraceContextInfo()



msg := "Hello World"



// Log to console



fmt.Printf("[!dt dt.trace_id=%s,dt.span_id=%s] - %s\n", traceContext.GetTraceId(), traceContext.GetSpanId(), msg)



// Write HTTP body



fmt.Fprintf(w, msg)



})



fmt.Println("Starting HTTP server at port 8080...")



log.Fatal(http.ListenAndServe(":8080", nil))



}
```

For details on configuration, see [AWS Lambda logs in context of traces](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/log-enrichment "Configure log message enrichment with OpenTelemetry on AWS Lambda.").

For instructions on how to source these attributes via OneAgent SDK:

* **Go:** see the [GO documentation on GitHubï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-Go)
* **.NET:** see the [.NET documentation on GitHubï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-dotnet#trace-context)

## Retrieve process group instance ID

You can get the `dt.entity.process_group_instance` field using the OpenTelemetry Python command containing `merged`. The `process_group_instance` is retrieved as one of the attributes delivered in `merged`, as shown in the example below:

With OneAgent, you can simply point to a local endpoint without an authentication token to enable trace ingestion.

```
import json



from opentelemetry import trace as OpenTelemetry



from opentelemetry.exporter.otlp.proto.http.trace_exporter import (



OTLPSpanExporter,



)



from opentelemetry.sdk.resources import Resource



from opentelemetry.sdk.trace import TracerProvider, sampling



from opentelemetry.sdk.trace.export import (



BatchSpanProcessor,



)



merged = dict()



for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.json", "/var/lib/dynatrace/enrichment/dt_metadata.json"]:



try:



data = ''



with open(name) as f:



data = json.load(f if name.startswith("/var") else open(f.read()))



merged.update(data)



except:



pass



merged.update({



"service.name": "python-quickstart", #TODO Replace with the name of your application



"service.version": "1.0.1", #TODO Replace with the version of your application



})



resource = Resource.create(merged)



tracer_provider = TracerProvider(sampler=sampling.ALWAYS_ON, resource=resource)



OpenTelemetry.set_tracer_provider(tracer_provider)



tracer_provider.add_span_processor(



BatchSpanProcessor(OTLPSpanExporter(



endpoint="http://localhost:14499/otlp/v1/traces"



)))
```

When using OneAgent, make sure to enable the public [Extension Execution Controller](/docs/ingest-from/extensions/concepts#eec "Learn more about the concept of Dynatrace Extensions.") in your Dynatrace Settings, otherwise no data will be sent.

Go to **Settings** > **Preferences** > **Extension Execution Controller**. The toggles **Enable Extension Execution Controller** and **Enable local PIPE/HTTP metric and Log Ingest API** should be active.

For details on configuration, see [Instrument your Python application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/python "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.")

## Related topics

* [Leverage log enrichment for traces to resolve problems](/docs/observe/application-observability/distributed-traces/use-cases/problems-logs-traces "Use the log enrichment to view related log entries in the distributed traces view and enhance your analysis capabilities.")