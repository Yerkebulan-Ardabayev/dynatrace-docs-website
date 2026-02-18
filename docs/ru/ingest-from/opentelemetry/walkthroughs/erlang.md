---
title: Instrument your Erlang application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/erlang
scraped: 2026-02-18T21:26:14.755258
---

# Instrument your Erlang application with OpenTelemetry

# Instrument your Erlang application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Apr 20, 2023

This walkthrough shows how to add observability to your Erlang application using the OpenTelemetry Erlang libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | No |
| Traces | Yes |
| Metrics | No |
| Logs | No |

## Prerequisites

* Dynatrace version 1.222+
* For tracing, W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Set up OpenTelemetry

1. Add the current versions of the [following dependenciesï»¿](https://hex.pm/packages?search=opentelemetry&sort=recent_downloads) to `rebar.config`.

   ```
   {deps, [



   %TODO add any additional dependancies here



   opentelemetry_api,



   opentelemetry,



   opentelemetry_exporter



   ]}.
   ```
2. Add the following dependencies to your `.app.src` file in the `src` directory.

   ```
   {applications, [kernel,



   stdlib,



   opentelemetry_api,



   opentelemetry,



   opentelemetry_exporter]}
   ```
3. Add the following configuration to `config/sys.config` and replace `[URL]` and `[TOKEN]` with the respective values for the [Dynatrace URL](#base-url) and [access token](#access-token).

   ```
   [



   {otel_getting_started, []},



   {opentelemetry,



   [{span_processor, batch},



   {traces_exporter, otlp},



   {resource,



   [{service,



   #{name => "erlang-quickstart", version => "1.0.1"} %%TODO Replace with the name and version of your application



   }]



   },



   {resource_detectors, [



   otel_resource_env_var,



   otel_resource_app_env,



   extra_metadata



   ]}



   ]



   },



   {opentelemetry_exporter,



   [{otlp_protocol, http_protobuf},



   {otlp_traces_endpoint, "[URL]"}, %%TODO Replace [URL] to your SaaS/Managed URL as mentioned in the next step



   {otlp_headers, [{"Authorization", "Api-Token [TOKEN]"}]} %%TODO Replace [TOKEN] with your API Token as mentioned in the next step



   ]}



   ].
   ```
4. Save the following code to `src/extra_metadata.erl`.

   ```
   -module(extra_metadata).



   -behaviour(otel_resource_detector).



   -export([get_resource/1]).



   get_resource(_) ->



   Metadata = otel_resource:create(otel_resource_app_env:parse(get_metadata("/var/lib/dynatrace/enrichment/dt_metadata.properties")), []),



   {ok, MetadataFilePath} = file:read_file("dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties"),



   Metadata2 = otel_resource:create(otel_resource_app_env:parse(get_metadata(MetadataFilePath)), []),



   Metadata3 = otel_resource:create(otel_resource_app_env:parse(get_metadata("/var/lib/dynatrace/enrichment/dt_host_metadata.properties")), []),



   otel_resource:merge(otel_resource:merge(Metadata, Metadata2), Metadata3),



   otel_resource:merge(Metadata, Metadata2).



   get_metadata(FileName) ->



   try



   {ok, MetadataFile} = file:read_file(FileName),



   Lines = binary:split(MetadataFile, <<"\n">>, [trim, global]),



   make_tuples(Lines, [])



   catch _:_ -> "Metadata not found, safe to continue"



   end.



   make_tuples([Line|Lines], Acc) ->



   [Key, Value] = binary:split(Line, <<"=">>),



   make_tuples(Lines, [{Key, Value}|Acc]);



   make_tuples([], Acc) -> Acc.
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

## Step 3 Instrument your application

### Add tracing

Spans are started with the macro [`with_span`ï»¿](https://hexdocs.pm/opentelemetry_api/OpenTelemetry.Tracer.html#with_span/3) and accept an optional list of span attributes, as well as the code block for this span. The span will automatically finish when the code block returns.

```
-export([init/2]).



-include_lib("opentelemetry_api/include/otel_tracer.hrl").



-include_lib("opentelemetry/include/otel_resource.hrl").



init( Req, State ) ->



?with_span(<<"parent_span">>, #{attributes => [ %%TODO Add span name



{<<"my-key-1">>, <<"my-value-1">>}] %%TODO Add attributes at span creation



}, fun child_function/1),



%% Your code goes here



child_function(_SpanCtx) ->



?with_span(<<"child_span">>, #{},



fun(_ChildSpanCtx) ->



?set_attributes([{<<"child-key-1">>, <<"child-value-1">>}]) %%TODO Add attributes after span creation



end).
```

### Collect metrics

No example yet, as OpenTelemetry for Erlang does not have stable support for metrics yet.

### Connect logs

No example yet, as OpenTelemetry for Erlang does not have stable support for logs yet.

Depending on the status of the OpenTelemetry SDK, the pre-release version may nonetheless already allow the ingestion of your logs.

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

#### Extracting the context when receiving a request

For extracting information on an existing context, we pass the headers to the `otel_propagator_text_map.extract` function, which parses the context information provided by the headers and sets the current context based on that.

```
%% Get Headers from incoming request



Headers = maps:get(headers, Req),



otel_propagator_text_map:extract(maps:to_list(Headers)),



SpanCtx = ?start_span(<<"span-name">>),



%% As we used `otel_propagator_text_map` the current context is from the parent span



Ctx = otel_ctx:get_current(),



proc_lib:spawn_link(fun() ->



%% Start span and set as current



otel_ctx:attach(Ctx),



?set_current_span(SpanCtx),



%% Create response



Resp = cowboy_req:reply(



200,



#{<<"content-type">> => <<"application/json">>},



<<"{\"message\": \"hello world\"}">>,



Req



),



{ok, Resp, State},



?end_span(SpanCtx)
```

#### Injecting the context when sending requests

The following example uses `otel_propagator_text_map:inject` to provide the HTTP headers (necessary for context propagation) in `NewHeaders`, which we eventually merge with the existing header object `Headers` and pass to the `httpc:request` call, which allows the receiving endpoint to continue the trace with the provided information.

```
?with_span(<<"span-name">>, #{},



fun(_ChildSpanCtx) ->



%% A custom header example



Headers = [{"content-type", "application/json"}, {"X-Custom-Header", "some-value"}],



%% We convert the traceparent information and merge the 2 headers as



%% Httpc:request requires tuples of strings



Tmp = [],



NewHeaders = headers_list(otel_propagator_text_map:inject(opentelemetry:get_text_map_injector(), Tmp)),



MergedHeaders = lists:append(Headers, NewHeaders),



{ok, Res} = httpc:request(get, {URL, MergedHeaders}, [], []),



io:format("Response: ~p~n", [Res])



end).



headers_list(Headers) ->



[{binary_to_list(Name), binary_to_list(Value)} || {Name, Value} <- Headers].
```

## Step 4 Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 5 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")