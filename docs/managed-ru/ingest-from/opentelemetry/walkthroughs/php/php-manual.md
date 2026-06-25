---
title: Ручное инструментирование PHP-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/php/php-manual
scraped: 2026-05-12T12:15:18.706114
---

# Ручное инструментирование PHP-приложения с OpenTelemetry

# Ручное инструментирование PHP-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 4 мин
* Опубликовано: 20 апреля 2023

В этом руководстве показано, как добавить наблюдаемость в ваше PHP-приложение с помощью библиотек и инструментов OpenTelemetry PHP.

## Шаг 1 Получение данных доступа Dynatrace

### Определение базового URL API

Подробнее о том, как собрать базовый URL эндпоинта OTLP, см. [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). URL должен заканчиваться на `/api/v2/otlp`.

### Получение токена доступа к API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

В разделе [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#authentication "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") больше подробностей о формате и необходимых областях доступа.

## Шаг 2 Инструментирование приложения

1. С помощью [composer](https://getcomposer.org) установите следующие две зависимости.

   * [php-http/guzzle7-adapter](https://packagist.org/packages/php-http/guzzle7-adapter)
   * [open-telemetry/opentelemetry](https://packagist.org/packages/open-telemetry/opentelemetry)

   ```
   composer require php-http/guzzle7-adapter



   composer require open-telemetry/opentelemetry
   ```
2. Создайте новый файл `otel.php` и сохраните следующий код.

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

   Операции чтения файлов, разбирающие файлы `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."), чтобы обогатить запрос OTLP и обеспечить доступность всей релевантной информации о топологии внутри Dynatrace.
3. Настройте переменные `$DT_API_URL` и `$DT_API_TOKEN`в `otel.php`, задав [соответствующие значения](#dynatrace-docs--otlp-export).
4. Подключите `otel.php` во всех PHP-файлах, где нужно инициализировать OpenTelemetry.

   ```
   require('otel.php');
   ```

## Шаг 3 Добавление сигналов телеметрии вручную

### Создание спанов

1. Чтобы создавать новые спаны, нам сначала нужен объект tracer.

   ```
   $tracer = Globals::tracerProvider()->getTracer('my-tracer');
   ```
2. С помощью `$tracer` мы теперь можем использовать span builder для создания и запуска новых спанов.

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

   В приведённом выше коде мы:

   * Создаём новый спан и называем его "Call to /myendpoint"
   * Добавляем два атрибута в соответствии с [семантическим соглашением об именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичных для действия этого спана: сведения о методе и версии HTTP
   * Добавляем `TODO` на место будущей бизнес-логики
   * Вызываем метод `end()` спана, чтобы закрыть спан (в блоке `finally`, чтобы гарантировать вызов метода)

### Сбор метрик

1. Как и для трассировок, нам нужно получить объект meter.

   ```
   $meterProvider = Globals::meterProvider();



   $meter = $meterProvider->getMeter('my-meter');
   ```
2. С помощью `$meter` мы теперь можем создавать отдельные инструменты, например счётчик.

   ```
   $requestCounter = $meter->createCounter('request_counter');
   ```
3. Теперь мы можем вызвать метод `add()` объекта `$requestCounter`, чтобы записать новые значения счётчиком и сохранить дополнительные атрибуты (например, `action.type`).

   ```
   $requestCounter->add(1, [ 'action.type' => 'create' ]);
   ```
4. Синхронные метрики, такие как счётчик, экспортируются при вызове `forceFlush()` или `shutdown()` на провайдере meter.

   ```
   $meterProvider->forceFlush();
   ```

### Подключение логов

Поскольку переменная `$monolog` уже инициализирована и настроена (см. [инструментирование](#instrument)), мы можем вести логирование напрямую в настроенный эндпоинт OpenTelemetry в Dynatrace.

```
$monolog->info('your log info message');
```

## Шаг 4 (необязательно) Обеспечение context propagation Optional

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

Если вы используете автоматическое инструментирование и ваши сетевые библиотеки соответствуют [PSR-15](https://www.php-fig.org/psr/psr-15/) (извлечение для входящего запроса) и [PSR-18](https://www.php-fig.org/psr/psr-18/) (внедрение для исходящих запросов), context propagation будет обработан автоматически. В противном случае это должен учитывать ваш код.

### Извлечение контекста при получении запроса

В следующем примере мы предполагаем, что получили HTTP-запрос со встроенной информацией о контексте, которую мы собираемся извлечь, чтобы продолжить трассировку.

Для этого мы сначала создаём объект `request` с помощью [`ServerRequestCreator::createFromGlobals()`](https://packagist.org/packages/httpsoft/http-server-request).

Далее мы получаем объект propagator из `TraceContextPropagator` и передаём наш объект `request` в его метод `extract()`. Это возвращает объект контекста (на основе предоставленной нам через HTTP-вызов информации), который мы затем можем использовать, чтобы продолжить эту трассировку нашими собственными спанами.

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

### Внедрение контекста при отправке запросов

В следующем примере мы используем [библиотеку cURL в PHP](https://www.php.net/manual/book.curl.php), чтобы отправить HTTP-запрос другому сервису и передать наш существующий контекст как часть HTTP-заголовков нашего запроса.

Для этого мы сначала получаем экземпляр `TraceContextPropagator`, у которого вызываем метод `inject` и передаём пустой массив `$traceContext`. Этот вызов заполняет массив соответствующими данными заголовков ассоциативным образом.

Поскольку для вызова cURL нам нужен простой строковый массив, нам нужно преобразовать его перед передачей в cURL. Для этого на следующем шаге мы проходим в цикле по `$traceContext` и добавляем имена и значения в `$contextData`.

Теперь мы готовы инициализировать наш экземпляр cURL, передать `$contextData` и выполнить HTTP-вызов.

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

## Шаг 5 (необязательно) Настройка захвата данных под требования конфиденциальности Optional

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace хранятся и отображаются только значения атрибутов, указанные в allowlist. Это предотвращает случайное хранение персональных данных, поэтому вы можете соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Чтобы просматривать ваши пользовательские атрибуты, сначала нужно разрешить их в веб-интерфейсе Dynatrace. О том, как настроить хранение и маскирование атрибутов, см. [Маскирование атрибутов](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 6 Проверка приёма данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий, чтобы создать и отправить демонстрационные трассировки, метрики и логи, и убедитесь, что они корректно приняты в Dynatrace.

Чтобы сделать это для трассировок, перейдите в **Distributed Traces** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо неё **PurePaths**.

Для метрик и логов перейдите в **Metrics** или **Logs**.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")