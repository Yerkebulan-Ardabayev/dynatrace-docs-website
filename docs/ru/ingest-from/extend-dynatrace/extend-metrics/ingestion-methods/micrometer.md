---
title: Отправка метрик Micrometer в Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer
scraped: 2026-03-06T21:16:40.252158
---

* 7 минут чтения

[Micrometer](https://dt-url.net/7u039ck) — это фреймворк инструментирования с открытым исходным кодом для метрик приложений на основе JVM. Он используется [Spring Boot](https://dt-url.net/ba239ye) для записи широкого спектра метрик. Вы можете принимать метрики Micrometer и Spring Boot и анализировать их с помощью Dynatrace Intelligence от начала до конца в контексте данных трассировки, журналов и диагностики. С Dynatrace вы получаете интеллектуальную наблюдаемость на базе ИИ и автоматический анализ первопричин для Spring Boot, 15+ предварительно инструментированных фреймворков и серверов на основе JVM и пользовательских метрик.

Вы можете использовать Micrometer в Dynatrace для:

* Приёма предварительно инструментированных метрик из приложений Spring Boot
* Приёма предварительно инструментированных метрик из фреймворков, серверов и систем кэширования на основе JVM
* Определения и приёма пользовательских метрик

Метрики, принятые из Micrometer, потребляют [DDU для пользовательских метрик](../../../../license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation.md "Узнайте, как рассчитать потребление единиц данных Davis и затраты, связанные с отслеживаемыми метриками.").

Существует два способа использования Micrometer:

* [В составе Spring Boot](#micrometer-with-spring-boot)
* [В качестве фасада метрик непосредственно в вашем коде](#directly)

## Предварительные требования

* Micrometer версии 1.8.0+
* Необязательно Spring Boot версии 2.6.0+
* Зависимость реестра должна быть добавлена в ваш проект:

  Micrometer standalone

  Spring Boot

  Gradle

  ```
  implementation 'io.micrometer:micrometer-registry-dynatrace:latest.release'
  ```

  Maven

  Замените `{micrometer.version}` последней версией Micrometer или конкретной версией, которую вы хотите использовать.
  Список выпущенных версий доступен на [Maven Central](https://dt-url.net/ay439b4).
  Рекомендуем использовать последнюю версию.

  ```
  <dependency>


  <groupId>io.micrometer</groupId>


  <artifactId>micrometer-registry-dynatrace</artifactId>


  <version>{micrometer.version}</version>


  </dependency>
  ```

  BOM Spring Boot указывает версию Micrometer, протестированную с соответствующей версией Spring Boot.
  Поэтому достаточно указать только имя зависимости без указания версии.
  Это обеспечит получение корректной, совместимой версии через Gradle или Maven.

  Gradle

  ```
  implementation 'io.micrometer:micrometer-registry-dynatrace'
  ```

  Maven

  ```
  <dependency>


  <groupId>io.micrometer</groupId>


  <artifactId>micrometer-registry-dynatrace</artifactId>


  </dependency>
  ```

## Каналы приёма данных

Для отправки метрик Micrometer можно использовать один из следующих каналов приёма:

* [OneAgent metric API](oneagent-metric-api.md "Используйте Dynatrace API для получения метрик отслеживаемых объектов.") — требуется установка OneAgent на отслеживаемом хосте.
* [Metrics API v2](../../../../dynatrace-api/environment-api/metric-v2.md "Получайте информацию о метриках через Metrics v2 API.").

## Реестр Dynatrace Micrometer

Micrometer использует концепцию реестра для экспорта метрик в системы мониторинга.

* Для Micrometer версии 1.8.0 или более поздней доступен [Dynatrace Registry v2](https://micrometer.io/docs/registry/dynatrace). Он экспортирует метрики через [Metrics API v2](../../../../dynatrace-api/environment-api/metric-v2.md "Получайте информацию о метриках через Metrics v2 API."). Все новые интеграции Micrometer и Dynatrace должны использовать эту версию.
* Более старые версии Micrometer больше не поддерживаются (см. [Реестр Dynatrace Micrometer v1 (устаревший)](#registry-v1) ниже).

## Приём метрик из приложений Spring Boot

Micrometer можно настроить через файл `.properties` или `.yaml`, используемый для конфигурации Spring Boot.
Spring Boot автоматически привязывает свойства с префиксом `management.dynatrace.metrics.export` к [объекту конфигурации Dynatrace](#dt-configuration-properties).

Вся конфигурация должна выполняться через файлы свойств. Создание `MeterRegistry` Micrometer вручную нарушает автоконфигурацию.

Имена свойств для привязки атрибутов из Spring Boot изменились в Spring Boot версии 3.0.0. Если вы используете версию Spring Boot до 3.0.0, используйте `management.metrics.export.dynatrace` вместо `management.dynatrace.metrics.export`.

С OneAgent (рекомендуется)

С Dynatrace Operator для Kubernetes

Без OneAgent

OneAgent на узлах Kubernetes не поддерживает приём метрик Micrometer напрямую. Подробнее см. в разделе [Отправка метрик из Kubernetes](#k8s-metrics). Если вы используете Dynatrace на Kubernetes, рекомендуем использовать Dynatrace Operator, который обеспечивает автоконфигурацию.

Для хостов, отслеживаемых OneAgent, доступна автоматическая конфигурация. Вам не нужно указывать конечную точку API для приёма метрики — если параметр **uri** не задан в конфигурации, метрика будет приниматься через [OneAgent metric API](oneagent-metric-api.md "Используйте Dynatrace API для получения метрик отслеживаемых объектов.").

YAML

```
management.dynatrace.metrics.export:


v2:


metric-key-prefix: "service.component"


enrich-with-dynatrace-metadata: true


default-dimensions:


stack: "prod"


region: "us-east-1"
```

.properties

```
management.dynatrace.metrics.export.v2.metric-key-prefix=service.component


management.dynatrace.metrics.export.v2.enrich-with-dynatrace-metadata=true


management.dynatrace.metrics.export.v2.default-dimensions.stack=prod


management.dynatrace.metrics.export.v2.default-dimensions.region=us-east-1
```

Dynatrace Operator настраивает реестр Dynatrace Micrometer, предоставляя URL-адрес приёма, учётные данные и метаданные Kubernetes. Примеры конфигурации см. в [примерах Dynakube](https://github.com/Dynatrace/dynatrace-operator/tree/main/assets/samples/dynakube).
Дополнительные сведения об обогащении метаданными см. в [документации по файлам обогащения](../../extend-data.md#operator-enrichment-directory "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.").

* Эта функция доступна при использовании реестра Dynatrace Micrometer версий 1.9.0 и выше.
* Приложение, использующее реестр Dynatrace Micrometer и работающее в Kubernetes с Dynatrace Operator, не требует явной конфигурации. Dynatrace Operator и реестр будут работать совместно и автоматически экспортировать метрики Micrometer в Dynatrace.
* Явное указание `management.dynatrace.metrics.export.uri` перезапишет автоматическую конфигурацию и следует избегать при использовании с Dynatrace Operator.

YAML

```
management.dynatrace.metrics.export:


v2:


metric-key-prefix: "service.component"


enrich-with-dynatrace-metadata: true


default-dimensions:


stack: "prod"


region: "us-east-1"
```

.properties

```
management.dynatrace.metrics.export.v2.metric-key-prefix=service.component


management.dynatrace.metrics.export.v2.enrich-with-dynatrace-metadata=true


management.dynatrace.metrics.export.v2.default-dimensions.stack=prod


management.dynatrace.metrics.export.v2.default-dimensions.region=us-east-1
```

Для приёма метрик с хостов, где OneAgent не установлен, таких как бессерверные развёртывания (например, AWS ECS) или другие среды, не основанные на Kubernetes, необходимо использовать [конечную точку приёма Metrics API v2](../../../../dynatrace-api/environment-api/metric-v2/post-ingest-metrics.md "Принимайте пользовательские метрики в Dynatrace через Metrics v2 API."). Сведения об использовании конечной точки см. в [примере POST ingest data points](../../../../dynatrace-api/environment-api/metric-v2/post-ingest-metrics.md#example "Принимайте пользовательские метрики в Dynatrace через Metrics v2 API."). Реестр Dynatrace Micrometer экспортирует данные в этот API, когда заданы URI и токен.

Убедитесь, что URI явно настроен, так как его отсутствие приведёт к использованию `localhost` по умолчанию, а локальный приём OneAgent недоступен в этих средах.

HTTP-клиенты, подключающиеся к непубличной конечной точке REST ActiveGate, должны доверять предоставленным сертификатам. Подробнее см. в разделе [Добавление пользовательского сертификата для ActiveGate](../../../setup-on-k8s/guides/networking-security-compliance/network-configurations.md "Настройте Dynatrace в средах с ограниченным доступом к сети, сетевые параметры и конфигурации прокси.").

Можно использовать нотацию заполнителей Spring (например, `api-token: ${YOUR_METRICS_INGEST_API_TOKEN}`), которая автоматически считывает переменную окружения и передаёт её в конфигурацию Micrometer.

YAML

```
management.dynatrace.metrics.export:


uri: "https://mySampleEnv.live.dynatrace.com/api/v2/metrics/ingest"


# Read the environment variable YOUR_METRICS_INGEST_API_TOKEN and supply the value of the env var instead.


api-token: ${YOUR_METRICS_INGEST_API_TOKEN}


v2:


metric-key-prefix: "service.component"


enrich-with-dynatrace-metadata: true


default-dimensions:


stack: "prod"


region: "us-east-1"
```

.properties

```
management.dynatrace.metrics.export.uri=https://mySampleEnv.live.dynatrace.com/api/v2/metrics/ingest


management.dynatrace.metrics.export.api-token=${YOUR_METRICS_INGEST_API_TOKEN}


management.dynatrace.metrics.export.v2.metric-key-prefix=service.component


management.dynatrace.metrics.export.v2.enrich-with-dynatrace-metadata=true


management.dynatrace.metrics.export.v2.default-dimensions.stack=prod


management.dynatrace.metrics.export.v2.default-dimensions.region=us-east-1
```

## Приём метрик непосредственно из Micrometer

С OneAgent (рекомендуется)

С Dynatrace Operator для Kubernetes

Без OneAgent

Для хостов, отслеживаемых OneAgent, доступна автоматическая конфигурация. Вам не нужно указывать конечную точку API для приёма метрики — если параметр **uri** не задан в конфигурации, метрика будет приниматься через [OneAgent metric API](oneagent-metric-api.md "Используйте Dynatrace API для получения метрик отслеживаемых объектов.").

Посмотреть код автоконфигурации

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {


@Override


@Nullable


public String get(String k) {


// This method can be used for retrieving arbitrary config items;


// null means accepting the defaults defined in DynatraceConfig


return null;


}


};


DynatraceMeterRegistry registry = DynatraceMeterRegistry.builder(config).build();
```

Dynatrace Operator настраивает реестр Dynatrace Micrometer, предоставляя URL-адрес приёма, учётные данные и метаданные Kubernetes. Примеры конфигурации см. в [примерах Dynakube](https://github.com/Dynatrace/dynatrace-operator/tree/main/assets/samples/dynakube).
Дополнительные сведения об обогащении метаданными см. в [документации по файлам обогащения](../../extend-data.md#operator-enrichment-directory "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.").

* Эта функция доступна при использовании реестра Dynatrace Micrometer версий 1.9.0 и выше.
* Приложение, использующее реестр Dynatrace Micrometer и работающее в Kubernetes с Dynatrace Operator, не требует явной конфигурации. Dynatrace Operator и реестр будут работать совместно и автоматически экспортировать метрики Micrometer в Dynatrace.
* Явное указание `management.dynatrace.metrics.export.uri` перезапишет автоматическую конфигурацию и следует избегать при использовании с Dynatrace Operator.

Посмотреть код автоконфигурации

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {


@Override


@Nullable


public String get(String k) {


// This method can be used for retrieving arbitrary config items;


// null means accepting the defaults defined in DynatraceConfig


return null;


}


};


DynatraceMeterRegistry registry = DynatraceMeterRegistry.builder(config).build();
```

Для приёма метрик с хостов, где OneAgent не установлен, таких как бессерверные развёртывания (например, AWS ECS) или другие среды, не основанные на Kubernetes, необходимо использовать [конечную точку приёма Metrics API v2](../../../../dynatrace-api/environment-api/metric-v2/post-ingest-metrics.md "Принимайте пользовательские метрики в Dynatrace через Metrics v2 API."). Сведения об использовании конечной точки см. в [примере POST ingest data points](../../../../dynatrace-api/environment-api/metric-v2/post-ingest-metrics.md#example "Принимайте пользовательские метрики в Dynatrace через Metrics v2 API."). Реестр Dynatrace Micrometer экспортирует данные в этот API, когда заданы URI и токен.

Убедитесь, что URI явно настроен, так как его отсутствие приведёт к использованию `localhost` по умолчанию, а локальный приём OneAgent недоступен в этих средах.

HTTP-клиенты, подключающиеся к непубличной конечной точке REST ActiveGate, должны доверять предоставленным сертификатам. Подробнее см. в разделе [Добавление пользовательского сертификата для ActiveGate](../../../setup-on-k8s/guides/networking-security-compliance/network-configurations.md "Настройте Dynatrace в средах с ограниченным доступом к сети, сетевые параметры и конфигурации прокси.").

Посмотреть код ручной конфигурации

В этом примере URL-адрес приёма метрик и токен доступа считываются из переменных окружения `YOUR_METRICS_INGEST_URL` и `YOUR_METRICS_INGEST_TOKEN`. Никогда не храните секреты непосредственно в коде — считывайте их из защищённого источника.

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {


@Override


public DynatraceApiVersion apiVersion() {


// Not strictly required, but makes the code more clear/explicit


return DynatraceApiVersion.V2;


}


@Override


public String uri() {


// The endpoint of the Dynatrace Metrics API v2 including path:


// "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"


String endpoint = System.getenv("YOUR_METRICS_INGEST_URL");


return endpoint != null ? endpoint : DynatraceConfig.super.uri();


}


@Override


public String apiToken() {


// Should be read from a secure source


String token = System.getenv("YOUR_METRICS_INGEST_TOKEN");


return token != null ? token : "";


}


@Override


@Nullable


public String get(String k) {


// This method can be used for retrieving arbitrary config items;


// null means accepting the defaults defined in DynatraceConfig


return null;


}


};


DynatraceMeterRegistry registry = DynatraceMeterRegistry.builder(dynatraceConfig).build();
```

## Проверка метрик

После отправки метрик проверьте данные в [Data Explorer](../../../../analyze-explore-automate/explorer.md "Делайте запросы к метрикам и преобразуйте результаты для получения нужных аналитических данных.") или [делайте запросы к ним в Grail](../../../../platform/grail/dynatrace-query-language/commands/metric-commands.md#timeseries "Команды метрик DQL").

## Свойства конфигурации

Для настройки реестра Dynatrace Micrometer можно использовать объект конфигурации Dynatrace (`DynatraceConfig`). Объект содержит параметры приёма метрик и используется для построения реестра Dynatrace (`DynatraceMeterRegistry`), который регистрируется в Micrometer для приёма метрик в Dynatrace. Можно задать следующие параметры:

Spring Boot

Непосредственно в Micrometer

При использовании Spring Boot записи в файлах `application.properties` или `application.yaml` будут автоматически сопоставляться с объектом `DynatraceConfig`.

Фрагмент кода для задания свойств

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {


@Override


public DynatraceApiVersion apiVersion() {


// Defaults to V2 if not set explicitly.


return DynatraceApiVersion.V2;


}


@Override


public String uri() {


// The endpoint of the Dynatrace Metrics API v2 including path. For example:


// "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest".


String endpoint = System.getenv("YOUR_METRICS_INGEST_URL");


return endpoint != null ? endpoint : DynatraceConfig.super.uri();


}


@Override


public String apiToken() {


// Should be read from a secure source


String token = System.getenv("YOUR_METRICS_INGEST_API_TOKEN");


return token != null ? token : "";


}


@Override


public String metricKeyPrefix() {


// Will be prepended to all metric keys


return "service.component";


}


@Override


public boolean enrichWithDynatraceMetadata() {


// On by default, but can be turned off explicitly.


return true;


}


@Override


public Map<String, String> defaultDimensions() {


// Create and return a map containing the desired key-value pairs.


Map<String, String> dims = new HashMap<>();


dims.put("dimensionKey", "dimensionValue");


return dims;


}


// Only available in Micrometer 1.9.0 and above.


@Override


public boolean useDynatraceSummaryInstruments() {


return false;


}


// Only available in Micrometer 1.12.0 and above.


@Override


public boolean exportMeterMetadata() {


return false;


}


@Override


@Nullable


public String get(String k) {


return null; // Accept the rest of the defaults


}


};
```

## Дополнительная информация

### Типы метрик

Все метрики преобразуются в соответствии с [типами протокола приёма метрик](../reference/metric-ingestion-protocol.md "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API."), используемыми Dynatrace.

Обратите внимание, что значение `count` для LongTaskTimers может вводить в заблуждение, так как оно, вероятно, будет двойным подсчётом в зависимости от частоты экспорта. В случае если вам требуется текущее количество активных задач, более надёжным способом является экспорт отдельного Gauge.

### Метаданные измерителей

Начиная с версии 1.12.0 реестра Dynatrace Micrometer, метаданные измерителей (единицы и описание) автоматически экспортируются в Dynatrace.
Для начала экспорта метаданных изменения кода не требуются.
Для отключения экспорта метаданных используйте следующую конфигурацию:

Spring Boot

Непосредственно в Micrometer

YAML

```
management:


metrics:


export:


dynatrace:


v2:


export-meter-metadata: false  # default: true
```

.properties

```
management.dynatrace.metrics.export.v2.export-meter-metadata=false
```

Метаданные измерителей были введены в Micrometer 1.12.0, который впервые был включён в Spring Boot 3.2.0.
Таким образом, описанные выше переключатели доступны начиная с Spring Boot 3.2.0.

Фрагмент кода для задания свойств

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {


// Only available in Micrometer 1.12.0 and above.


@Override


public boolean exportMeterMetadata() {


return false;


}


@Override


@Nullable


public String get(String k) {


return null; // Accept the rest of the defaults


}


};
```

Для более ранних версий Micrometer метаданные необходимо указывать вручную с помощью Dynatrace API или веб-интерфейса.
Дополнительные сведения см. в разделе [Метаданные пользовательских метрик](../reference/custom-metric-metadata.md "Предоставьте метаданные для вашей пользовательской метрики.").

### Отправка метрик из Kubernetes

OneAgent нельзя использовать для приёма метрик Micrometer на узлах Kubernetes. Можно настроить Micrometer для прямой отправки метрик в Dynatrace с помощью [Metrics API](../../../../dynatrace-api/environment-api/metric-v2.md "Получайте информацию о метриках через Metrics v2 API.").

### Захват метрик JVM в Micrometer

По умолчанию метрики JVM отключены при запуске Micrometer без Spring Boot. Сведения об их включении см. в [документации Micrometer](https://docs.micrometer.io/micrometer/reference/reference/jvm.html). После их включения и регистрации в реестре Dynatrace (`DynatraceMeterRegistry`) метрики JVM записываются и автоматически отправляются в Dynatrace.

На хостах, отслеживаемых OneAgent, эти метрики могут уже собираться OneAgent.

### Ограничение приёма определённых метрик

Spring Boot

Непосредственно в Micrometer

При запуске Micrometer в Spring Boot [множество метрик](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html#actuator.metrics.supported) автоматически создаётся и отправляется в Dynatrace, включая метрики JVM, процессов и диска.

Чтобы увидеть все метрики, созданные вашим приложением Spring Boot, перейдите к [конечной точке actuator вашего приложения Spring Boot](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html#actuator.enabling) (`/actuator/metrics`). Некоторые из этих метрик могут уже собираться OneAgent.

### Отключение метрик с помощью свойств Spring

Метрики можно отключить на основе их префикса в конфигурации Spring Boot. Чтобы узнать, какие метрики можно исключить, проверьте конечную точку actuator вашего приложения Spring Boot. Обязательно **исключите** пользовательский префикс ключа метрики (если таковой имеется, см. [`metric-key-prefix`](#dt-configuration-properties)) при использовании этой функции.

YAML

```
management.metrics.enable:


# disable jvm.memory metrics


jvm.memory: false


# disable all jvm metrics:


jvm: false
```

.properties

```
# disable jvm.memory metrics


management.metrics.enable.jvm.memory=false


# disable all jvm metrics


management.metrics.enable.jvm=false
```

Также можно сначала отключить все метрики, а затем повторно включить только нужные:

YAML

```
management.metrics.enable:


# disable all metrics


all: false


# re-enable only jvm.* metrics


jvm: true
```

.properties

```
# disable all metrics


management.metrics.enable.all=false


# re-enable jvm.* metrics


management.metrics.enable.jvm=true
```

### Отключение метрик в коде

Micrometer предоставляет [фильтры измерителей](https://docs.micrometer.io/micrometer/reference/concepts/meter-filters.html) для отключения метрик на основе различных условий. Фильтры измерителей также можно настроить через Spring Boot с аннотацией `@Configuration`.

Показать фрагмент кода

```
@Configuration(proxyBeanMethods = false)


public class MyMeterRegistryConfiguration {


@Bean


public MeterRegistryCustomizer<MeterRegistry> metricsCommonTags() {


return registry -> registry.config()


.meterFilter(MeterFilter.denyNameStartsWith("jvm.gc"));


}


}
```

Префикс метрики, настроенный для реестра Dynatrace, будет применён после фильтрации, поэтому свойства для включения или отключения метрик должны быть указаны с использованием исходного ключа метрики без этого префикса.

Зарегистрируйте фильтры MeterFilters перед созданием или [включением дополнительных метрик](#add-automatically-created-metrics), так как `MeterFilter` будет оцениваться только при добавлении метрики в `MeterRegistry`.

Можно настроить реестр для фильтрации определённых метрик по имени и/или тегам (например, метрик, уже собираемых OneAgent). Для этого используйте [фильтры измерителей](https://micrometer.io/docs/concepts#_meter_filters) Micrometer. Необходимо добавить фильтры измерителей до включения [захвата метрик JVM](#add-automatically-created-metrics), иначе фильтры будут переопределены.

Префикс метрики, настроенный для реестра Dynatrace, будет применён после фильтрации, поэтому `meterFilters` должны быть указаны с использованием исходного ключа метрики без этого префикса.

Отключение метрик в коде

```
// Disable all metrics with metric names starting with jvm.gc


registry.config()


.meterFilter(MeterFilter.denyNameStartsWith("jvm.gc"));
```

### Устранение неполадок с помощью журналов

Spring Boot

Непосредственно в Micrometer

Spring обрабатывает ведение журнала при использовании Micrometer в контексте Spring Boot. Уровень журнала для реестра Dynatrace Micrometer можно задать через свойства конфигурации.

YAML

```
logging.level.io.micrometer.dynatrace: DEBUG
```

.properties

```
logging.level.io.micrometer.dynatrace=DEBUG
```

Micrometer и реестр Dynatrace Micrometer используют [slf4j](https://www.slf4j.org/) внутри для записи событий, таких как строки, отправляемые в Dynatrace.
Если вы хотите получить эту информацию, настройте свой проект с выбранным фреймворком ведения журналов (например, [logback](https://logback.qos.ch/manual/configuration.html#automaticConf)) и установите уровень журнала `debug`.

Отладочное ведение журнала с logback

При использовании реализации logback по умолчанию отладочное ведение журнала в консоль включено по умолчанию. Чтобы добавить logback в ваш проект и записывать отладочную информацию, добавьте следующую зависимость:

```
implementation 'ch.qos.logback:logback-classic:latest.release'
```

### Специализированные инструменты Dynatrace

Начиная с Micrometer версии 1.9.x, в реестре измерителей Dynatrace для определённых инструментов суммирования используются специализированные инструменты (`DynatraceTimer` и `DynatraceDistributionSummary`). Их цель — обойти особенность того, как Micrometer записывает метрики, что в некоторых случаях приводило к отклонению метрик Dynatrace из-за недопустимого формата. Специализированные инструменты, адаптированные для приёма метрик Dynatrace, предотвращают создание недопустимых метрик.

* Они доступны начиная с версии 1.9.0 и используются как прямая замена по умолчанию. Пользователям, обновляющимся до версии 1.9.0, не требуется никаких действий.
* Если наблюдается расхождение в метриках, можно вернуться к предыдущему поведению, установив переключатель `useDynatraceSummaryInstruments` в значение `false`.

## Реестр Dynatrace Micrometer v1 Устарело

Устаревание Timeseries v1 API

[Timeseries v1 API](../../../../dynatrace-api/environment-api/metric-v1.md "Получайте информацию о метриках через Timeseries v1 API.") устарел и больше не принимает данные. Пожалуйста, выполните миграцию на поддерживаемый экспортёр, как описано на этой странице.
