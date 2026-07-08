---
title: Manually instrument your PHP application with OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/php/php-manual
---

# Manually instrument your PHP application with OpenTelemetry

# Manually instrument your PHP application with OpenTelemetry

* How-to guide
* 4-min read
* Published Apr 20, 2023

This walkthrough shows how to add observability to your PHP application using the OpenTelemetry PHP libraries and tools.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Instrument your application

1. Use [composer﻿](https://getcomposer.org) to install the following two dependencies.

   * [php-http/guzzle7-adapter﻿](https://packagist.org/packages/php-http/guzzle7-adapter)
   * [open-telemetry/opentelemetry﻿](https://packagist.org/packages/open-telemetry/opentelemetry)

   ```
   composer require php-http/guzzle7-adapter



   composer require open-telemetry/opentelemetry
   ```
2. Create a new file `otel.php` and save the following code.

   ```
   <?php



   declare(strict_types=1);



   require __DIR__ . '/vendor/autoload.php';



   // ===== OpenTelemetry Imports =====



   use Monolog\Handler\StreamHandler;



   use Monolog\Logger;



   use OpenTelemetry\Contrib\Otlp\OtlpHttpTransportFactory;



   use OpenTelemetry\Contrib\Otlp\SpanExporter;



   use OpenTelemetry\SDK\Sdk;



   use OpenTelemetry\SDK\Trace\SpanProcessor\SimpleSpanProcessor;



   use OpenTelemetry\SDK\Trace\TracerProvider;



   use OpenTelemetry\SDK\Resource\ResourceInfoFactory;



   use OpenTelemetry\SDK\Resource\ResourceInfo;



   use OpenTelemetry\SDK\Common\Attribute\Attributes;



   use OpenTelemetry\API\Trace\Propagation\TraceContextPropagator;



   use OpenTelemetry\SemConv\ResourceAttributes;



   use OpenTelemetry\SDK\Metrics\MeterProvider;



   use OpenTelemetry\Contrib\Otlp\MetricExporter;



   use OpenTelemetry\SDK\Common\Time\ClockFactory;



   use OpenTelemetry\SDK\Metrics\MetricReader\ExportingReader;



   use OpenTelemetry\Contrib\Otlp\LogsExporter;



   use OpenTelemetry\SDK\Logs\LoggerProvider;



   use OpenTelemetry\SDK\Logs\Processor\SimpleLogRecordProcessor;



   use OpenTelemetry\Contrib\Logs\Monolog\Handler;



   use Psr\Log\LogLevel;



   // ===== GENERAL SETUP =====



   $DT_API_URL = '';



   $DT_API_TOKEN = '';



   $dtMetadata = [];



   foreach (['/var/lib/dynatrace/enrichment/dt_metadata.properties',



   'dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties',



   '/var/lib/dynatrace/enrichment/dt_host_metadata.properties'] as $filePath) {



   try {



   if (file_exists($filePath)) {



   $props = str_starts_with($filePath, '/var/') ? parse_ini_file($filePath) : parse_ini_file(trim(file_get_contents($filePath)));



   $dtMetadata = array_merge($dtMetadata, $props);



   }



   } catch (Exception $e) {}



   }



   $resource = ResourceInfoFactory::defaultResource()->merge(ResourceInfo::create(Attributes::create([$dtMetadata,



   ResourceAttributes::SERVICE_NAME => 'php-quickstart'])));



   // ===== TRACING SETUP =====



   $transport = (new OtlpHttpTransportFactory())->create($DT_API_URL . '/v1/traces', 'application/x-protobuf', [ 'Authorization' => 'Api-Token ' . $DT_API_TOKEN ]);



   $exporter = new SpanExporter($transport);



   $tracerProvider =  new TracerProvider(new SimpleSpanProcessor($exporter), null, $resource);



   // ===== METRIC SETUP =====



   $reader = new ExportingReader(



   new MetricExporter((new OtlpHttpTransportFactory())->create($DT_API_URL . '/v1/metrics', 'application/x-protobuf', [ 'Authorization' => 'Api-Token ' . $DT_API_TOKEN ])),



   ClockFactory::getDefault()



   );



   $meterProvider = MeterProvider::builder()->setResource($resource)->addReader($reader)->build();



   // ===== LOG SETUP =====



   $transport = (new OtlpHttpTransportFactory())->create($DT_API_URL . '/v1/logs', 'application/x-protobuf', [ 'Authorization' => 'Api-Token ' . $DT_API_TOKEN ]);



   $exporter = new LogsExporter($transport);



   $loggerProvider = LoggerProvider::builder()



   ->addLogRecordProcessor(new SimpleLogRecordProcessor($exporter))



   ->setResource($resource)



   ->build();



   $handler = new Handler($loggerProvider, LogLevel::INFO);



   $monolog = new Logger('example', [$handler]);



   // ===== REGISTRATION =====



   Sdk::builder()



   ->setTracerProvider($tracerProvider)



   ->setMeterProvider($meterProvider)



   ->setLoggerProvider($loggerProvider)



   ->setPropagator(TraceContextPropagator::getInstance())



   ->setAutoShutdown(true)



   ->buildAndRegisterGlobal();
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.
3. Configure the variables `$DT_API_URL` and `$DT_API_TOKEN`in `otel.php` with the [respective values](#dynatrace-docs--otlp-export).
4. Include `otel.php` in all PHP files where you need to initialize OpenTelemetry.

   ```
   require('otel.php');
   ```

## Step 3 Add telemetry signals manually

### Create spans

1. To create new spans, we first need a tracer object.

   ```
   $tracer = Globals::tracerProvider()->getTracer('my-tracer');
   ```
2. With `$tracer`, we can now use a span builder to create and start new spans.

   ```
   $span = $tracer->spanBuilder('Call to /myendpoint')->startSpan();



   try



   {



   $span->setAttribute('http.method', 'GET');



   $span->setAttribute('net.protocol.version', '1.1');



   // TODO your code goes here



   }



   finally



   {



   $span->end();



   }
   ```

   In the above code, we:

   * Create a new span and name it "Call to /myendpoint"
   * Add two attributes, following the [semantic naming convention﻿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Add a `TODO` in place of the eventual business logic
   * Call the span's `end()` method to close the span (in a `finally` block to ensure the method is called)

### Collect metrics

1. As with traces, we need to obtain a meter object.

   ```
   $meterProvider = Globals::meterProvider();



   $meter = $meterProvider->getMeter('my-meter');
   ```
2. With `$meter`, we can now create individual instruments, such as a counter.

   ```
   $requestCounter = $meter->createCounter('request_counter');
   ```
3. We can now invoke the `add()` method of `$requestCounter` to record new values with the counter and save additional attributes (for example, `action.type`).

   ```
   $requestCounter->add(1, [ 'action.type' => 'create' ]);
   ```
4. Synchronous metrics like the counter are exported when `forceFlush()` or `shutdown()` are called on the meter provider.

   ```
   $meterProvider->forceFlush();
   ```

### Connect logs

With the `$monolog` variable already initialized and configured (see [instrumentation](#instrument)), we can log straight to the configured OpenTelemetry endpoint at Dynatrace.

```
$monolog->info('your log info message');
```

## Step 4 optional Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

If you are using automatic instrumentation, and your network libraries adhere to [PSR-15﻿](https://www.php-fig.org/psr/psr-15/) (extraction for inbound request) and [PSR-18﻿](https://www.php-fig.org/psr/psr-18/) (injection for outbound requests), context propagation will be automatically handled. Otherwise, your code needs to take this into account.

### Extracting the context when receiving a request

In the following example, we assume that we have received an HTTP request with embedded context information, which we are going to extract, to continue the trace.

For this, we first create a `request` object with [`ServerRequestCreator::createFromGlobals()`﻿](https://packagist.org/packages/httpsoft/http-server-request).

Next, we obtain a propagator object from `TraceContextPropagator` and pass our `request` object to its `extract()` method. This returns a context object (based on the information provided to us via the HTTP call), which we can use subsequently to continue that trace with our own spans.

```
// Create a request object based on PHP's global arrays (for example, $_SERVER)



$request = ServerRequestCreator::createFromGlobals();



// Obtain propagator instance



$tracePropagator = TraceContextPropagator::getInstance();



// Extract context information from headers and recreate context



$context = $tracePropagator->extract($request->getHeaders());



// Start new span and set received context as parent



$span = $tracer->spanBuilder("my-span")



->setParent($context)



->setSpanKind(SpanKind::KIND_SERVER)



->startSpan();



$scope = $span->activate();



try



{



// TODO your code here



}



finally



{



$span->end();



$scope->detach();



}
```

### Injecting the context when sending requests

In the following example, we use [PHP's cURL library﻿](https://www.php.net/manual/book.curl.php) to send an HTTP request to another service and provide our existing context as part of the HTTP headers of our request.

To do so, we first obtain a `TraceContextPropagator` instance, on which we call the `inject` method and pass the empty array `$traceContext`. This call populates the array with the applicable header data in an associative fashion.

As we need a plain string array for the cURL call, we need to convert that before we pass it to cURL. To do so, we loop over `$traceContext` in the next step and add the names and values to `$contextData`.

Now we are ready to initialize our cURL instance, pass `$contextData`, and execute the HTTP call.

```
$traceContext = []; $contextData = [];



$tracePropagator = TraceContextPropagator::getInstance();



$tracePropagator->inject($traceContext);



// Convert associative array into plain string array



foreach ($traceContext as $name => $value) $contextData[] = "$name: $value";



// Initialize cURL



$ch = curl_init('[URL]');



// Set propagation headers



curl_setopt($ch, CURLOPT_HTTPHEADER, $contextData);



// Execute cURL call



curl_exec($ch);
```

## Step 5 optional Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 6 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to **Distributed Traces** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or **Logs**.

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")