---
title: Instrument your Elixir application with OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/elixir
scraped: 2026-05-12T12:04:19.980203
---

# Instrument your Elixir application with OpenTelemetry

# Instrument your Elixir application with OpenTelemetry

* How-to guide
* 4-min read
* Published Apr 20, 2023

This walkthrough shows how to add observability to your Elixir application using the OpenTelemetry Elixir libraries and tools.

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

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Set up OpenTelemetry

1. Add the current versions of the [following dependenciesï»¿](https://hex.pm/packages?search=opentelemetry&sort=recent_downloads) to `mix.exs`.

   ```
   defp deps do



   [



   # Add any additional dependancies here



   {:httpoison, version: :latest},



   {:plug_cowboy, version: :latest},



   {:jason, version: :latest},



   {:plug, version: :latest},



   {:opentelemetry_exporter, version: :latest},



   {:opentelemetry_api, version: :latest},



   {:opentelemetry, version: :latest}



   ]



   end
   ```
2. Add a `release` section to the application definition in `mix.exs`.

   ```
   releases: [



   <project_name>: [



   version: "<project_version>",



   applications: [opentelemetry_exporter: :permanent, opentelemetry: :temporary]



   ]



   ]
   ```
3. Enable the context propagation dependencies with the following line in `runtime.exs`.

   ```
   text_map_propagators: [:baggage, :trace_context],
   ```
4. Add the following configuration to `config/runtime.exs` and replace `[URL]` and `[TOKEN]` with the respective values for the [Dynatrace URL](#base-url) and [access token](#access-token).

   ```
   import Config



   config :opentelemetry,



   resource: [service: %{name: "elixir-quickstart", version: "1.0.1"}], #TODO Replace with the name and version of your application



   span_processor: :batch,



   traces_exporter: :otlp,



   # Add your text map propagator from previous step here



   resource_detectors: [



   :otel_resource_app_env,



   :otel_resource_env_var,



   ExtraMetadata



   ]



   config :opentelemetry_exporter,



   otlp_protocol: :http_protobuf,



   otlp_traces_endpoint: "[URL]", #TODO Replace [URL] to your SaaS/Managed URL as mentioned in the next step



   otlp_traces_headers: [{"Authorization", "Api-Token [TOKEN]"}] #TODO Replace [TOKEN] with your API Token as mentioned in the next step
   ```
5. Save the following code in `lib/extra_metadata.ex`.

   ```
   defmodule ExtraMetadata do



   @behaviour :otel_resource_detector



   def get_resource(_) do



   metadata = read_file("/var/lib/dynatrace/enrichment/dt_metadata.properties") |> unwrap_lines



   file_path = read_file("dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties") |> unwrap_lines



   metadata2 = read_file(file_path) |> unwrap_lines



   attributes = get_attributes(Enum.concat(metadata, metadata2))



   metadata3 = read_file("/var/lib/dynatrace/enrichment/dt_host_metadata.properties") |> unwrap_lines



   attributes = get_attributes(Enum.concat(metadata, metadata2) ++ metadata3)



   :otel_resource.create(attributes)



   end



   defp unwrap_lines({:ok, metadata}), do: metadata



   defp unwrap_lines({:error, _}), do: []



   defp read_file(file_name) do



   try do



   {:ok, String.split(File.read!(file_name), "\n")}



   rescue



   File.Error ->



   {:error, "File does not exist, safe to continue"}



   end



   end



   defp get_attributes(metadata) do



   Enum.map(metadata, fn(line) ->



   if String.length(line) > 0 do



   [key, value] = String.split(line, "=")



   {key, value}



   else



   {:error, "EOF"}



   end



   end)



   end



   end
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

## Step 3 Instrument your application

### Add tracing

Spans are started with the macro [`with_span`ï»¿](https://hexdocs.pm/opentelemetry_api/OpenTelemetry.Tracer.html#with_span/3) and accept an optional list of span attributes, as well as the code block for this span. The span automatically finishes when the code block returns.

```
require OpenTelemetry.Tracer, as: Tracer



def hello do



Tracer.with_span "my-span", %{attributes: [{<<"my-key-1">>, <<"my-value-1">>}]} do #TODO add attributes at span creation



Tracer.set_attributes([{"another-key-1", "another-value-1"}]) #TODO add attributes after span creation



# Your code goes here



end



end
```

### Collect metrics

No example yet, as OpenTelemetry for Elixir does not have stable support for metrics yet.

### Connect logs

No example yet, as OpenTelemetry for Elixir does not have stable support for logs yet.

Depending on the status of the OpenTelemetry SDK, the pre-release version may nonetheless already allow the ingestion of your logs.

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

#### Extracting the context when receiving a request

To extract information on an existing context, we pass the headers to the `otel_propagator_text_map.extract` function, which parses the context information provided by the headers and sets the current context based on that.

```
# Extract headers



:otel_propagator_text_map.extract(conn.req_headers)



span_ctx = OpenTelemetry.Tracer.start_span(<<"span-name">>)



ctx = OpenTelemetry.Ctx.get_current()



task = Task.async(fn ->



OpenTelemetry.Ctx.attach(ctx)



OpenTelemetry.Tracer.set_current_span(span_ctx)



# Do work here



OpenTelemetry.Tracer.end_span(span_ctx)



end)
```

#### Injecting the context when sending requests

The following example uses `otel_propagator_text_map:inject` to provide the HTTP headers (necessary for context propagation) in `merged_headers`. The headers are then passed to `HTTPoison.get`, which allows the receiving endpoint to continue the trace with the provided information.

```
OpenTelemetry.Tracer.with_span "span-name" do



# ...



# do work here



# ...



headers = [{"content-type", "application/json"}, {"X-Custom-Header", "some-value"}]



merged_headers = :otel_propagator_text_map.inject(headers)



case HTTPoison.get(URL, merged_headers, []) do



{:ok, res} -> IO.puts("Response: #{inspect(res)}")



{:error, _} -> raise "request failed"



end



end
```

## Step 4 Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 5 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to **Distributed Traces** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or **Logs**.

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")