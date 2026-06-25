---
title: Расширение трассировок с помощью OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-opentelemetry
scraped: 2026-05-12T11:06:19.794008
---

# Расширение трассировок с помощью OpenTelemetry

# Расширение трассировок с помощью OpenTelemetry

* Чтение: 7 мин
* Обновлено 23 сентября 2022 г.

[OpenTelemetry](https://dt-url.net/y903u4j): набор инструментов, API и SDK, позволяющих использовать данные телеметрии (распределённые трассировки, метрики и логи) для анализа производительности и поведения приложения.

OpenTelemetry совместно с кодовым модулем z/OS Java позволяет обогащать или расширять распределённые трассировки.

* Обогащать распределённые трассировки данными, специфичными для проекта (например, добавлять бизнес-релевантные данные в трассировки или захватывать диагностику для разработчиков).
* Расширять распределённые трассировки (например, захватывать Java Transport, не поддерживаемый Dynatrace из коробки, или устранять пробелы в наблюдаемости между приложениями для получения транзакционной аналитики).

Метрики и логи OpenTelemetry в настоящее время не поддерживаются кодовым модулем z/OS Java.

Лицензирование

* Распределённые трассировки OpenTelemetry, захваченные кодовым модулем z/OS Java, включены в лицензию мейнфрейма.

## Совместимость с OpenTelemetry

OpenTelemetry версии 1.0+

При включении совместимости с OpenTelemetry кодовый модуль z/OS Java подключается к OpenTelemetry API. После включения модуль перенаправляет определённые обращения к OpenTelemetry API (например, `GlobalOpenTelemetry`) во внутренний Dynatrace OpenTelemetry SDK.

Кодовый модуль z/OS Java передаёт захваченные [спаны OpenTelemetry](https://opentelemetry.io/docs/concepts/signals/traces/#spans-in-opentelemetry) через [подсистему zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java "Настройка мониторинга Java на z/OS с помощью модуля Java.") и [модуль zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS.") в окружение Dynatrace.

![z/OS Java OpenTelemetry](https://dt-cdn.net/images/zos-java-otel-1369-e7b35738b0.png)

z/OS Java OpenTelemetry

Рекомендация: не используйте OpenTelemetry SDK в приложениях совместно с механизмом совместимости Dynatrace OpenTelemetry, поскольку это может привести к конфликтам.

### Включение совместимости с OpenTelemetry

Совместимость с OpenTelemetry отключена по умолчанию. Чтобы включить её, добавьте атрибут `OpenTelemetry: EnableIntegration` в файл `dtconfig.json`, как показано в следующем примере.

Как правило, файл `dtconfig.json` создаётся при [установке кодового модуля z/OS Java](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Настройка мониторинга Java на z/OS с помощью модуля Java.") с указанием атрибутов `Tenant`, `ClusterID` и `zdcName` для вашего окружения.

```
{



"OpenTelemetry": {



"EnableIntegration": true



}



}
```

Альтернативно можно добавить параметр `open-telemetry-enable-integration` в аргумент JVM кодового модуля z/OS Java:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=open-telemetry-enable-integration=true
```

## Примеры инструментирования OpenTelemetry

Для поддержки различных сценариев использования OpenTelemetry позволяет добавлять независимое от поставщика пользовательское инструментирование в приложения. Инструментирование приложений с помощью OpenTelemetry требует знания программирования и доступа к коду приложения. Инструкции по инструментированию приложения см. в [документации OpenTelemetry](https://dt-url.net/7603uf3) и [документации OpenTelemetry Java](https://dt-url.net/n823ur4).

Ниже приведены примеры использования [OpenTelemetry Java](https://dt-url.net/yo43um9).

Обогащение трассировок данными, специфичными для проекта

Этот пример показывает, как захватить дополнительную операцию в Java-приложении, работающем на WebSphere Application Server под мониторингом Dynatrace.

1. Определите `Tracer`.

   ```
   import io.opentelemetry.api.GlobalOpenTelemetry;



   import io.opentelemetry.api.trace.Tracer;



   public final class RestaurantOpenTelemetry {



   public static Tracer getTracer() {



   return GlobalOpenTelemetry.getTracer("restaurant", "0.0.1");



   }



   }
   ```
2. Используйте `Tracer` для захвата операции вместе с атрибутами.

   ```
   import io.opentelemetry.api.trace.Span;



   import io.opentelemetry.api.trace.SpanKind;



   import io.opentelemetry.context.Scope;



   public class MenuDao {



   public Order newOrder(String customer) {



   // OpenTelemetry: create a span and define it's scope



   Span span = RestaurantOpenTelemetry.getTracer().spanBuilder("MenuDao.newOrder")



   .setSpanKind(SpanKind.INTERNAL)



   .setAttribute("customer", customer)



   .startSpan();



   try (Scope scope = span.makeCurrent()) {



   // Your application code: create a new order



   Order order = new Order();



   order.setCustomer(customer);



   order.setStatus("pending");



   // OpenTelemetry: add order ID to the span



   span.setAttribute("newOrderId", order.getId());



   return order;



   } finally {



   // OpenTelemetry: close the span



   span.end();



   }



   }



   }
   ```

Операция `MenuDao.newOrder` отображается как спан на вкладке **Code level** в веб-интерфейсе Dynatrace с захваченными атрибутами спана (`customer`, `newOrderId`) и измеренным временем выполнения.

![z/OS OpenTelemetry: уровень кода](https://dt-cdn.net/images/zos-opentelemetry-1-1926-e67ad2add3.png)

z/OS OpenTelemetry: уровень кода

Расширение сквозных трассировок

Этот пример показывает, как трассировать сервис аудита на WebSphere Application Server (под мониторингом Dynatrace), использующий Java-транспорт, не поддерживаемый из коробки. В качестве примера такого неподдерживаемого транспорта используется Java serialization (потоки вывода объектов).

Подробнее о распространении контекста см. в официальной [документации OpenTelemetry Context Propagation](https://dt-url.net/j503uhz).

**Service A** записывает запись аудита в `ObjectOutputStream`:

```
import io.opentelemetry.api.GlobalOpenTelemetry;



import io.opentelemetry.context.Context;



import io.opentelemetry.context.propagation.TextMapPropagator;



public class AuditService {



public static void sendAuditEntry(Order order) {



// Your application code: declare an audit entry



Map<String, String> auditEntry = new HashMap<>();



auditEntry.put("name", order.getId().toString());



auditEntry.put("description", order.getCustomer());



// OpenTelemetry: Inject current context of audit entry and propagate it



TextMapPropagator propagator = GlobalOpenTelemetry.getPropagators().getTextMapPropagator();



propagator.inject(



Context.current(),



auditEntry,



Map::put



);



// Your application code: write audit entry to objectOutputStream (Socket)



Socket socket = new Socket(host, port);



ObjectOutputStream objectOutputStream = new ObjectOutputStream(socket.getOutputStream())) {



objectOutputStream.writeObject(auditEntry);



}



}
```

**Service B** считывает запись аудита из `ObjectInputStream`:

```
import io.opentelemetry.api.GlobalOpenTelemetry;



import io.opentelemetry.api.trace.Span;



import io.opentelemetry.api.trace.SpanKind;



import io.opentelemetry.context.Context;



import io.opentelemetry.context.Scope;



import io.opentelemetry.context.propagation.TextMapGetter;



public class AuditService {



private static void receivedAuditEntry(Map<String, String> auditEntry) {



// OpenTelemetry: declare the tracer, create a span and define it's scope



Span span = GlobalOpenTelemetry.getTracer("auditing-center", "0.0.1")



.spanBuilder("auditEntry")



.setSpanKind(SpanKind.SERVER)



.setAttribute("auditName", auditEntry.get("name"))



.startSpan();



try (Scope scope = span.makeCurrent()) {



// Your application code: process audit entry



// ...



}



span.end();



}



public static void readAuditEntryFromSocket(Socket socket) {



ObjectInputStream objectInputStream = new ObjectInputStream(socket.getInputStream());



Object input = objectInputStream.readObject();



// OpenTelemetry: extract context of audit entry



Context context = GlobalOpenTelemetry.getPropagators().getTextMapPropagator()



.extract(



Context.current(),



input,



new TextMapGetter<Map<String, String>>(){ /* ... */ });



try (Scope scope = context.makeCurrent()) {



receivedAuditEntry((Map<String, String>) input);



}



// ...



}



}
```

Dynatrace отображает полную сквозную трассировку как распределённую трассировку, содержащую `auditEntry` в качестве метода сервиса с захваченными атрибутами и измеренным временем выполнения. Метод сервиса `auditEntry` является результатом трассировки метода `receivedAuditEntry` с его новым спаном. Отображение в качестве дочернего элемента метода сервиса `/orderReceived` является результатом вызовов `inject` и `extract` компонента `TextMapPropagator`.

![z/OS OpenTelemetry: сервис](https://dt-cdn.net/images/zos-opentelemetry-2-1926-9f66be4562.png)

z/OS OpenTelemetry: сервис

## Подавление спанов из определённых инструментирований

Можно подавлять спаны из определённой области инструментирования/библиотеки. Для этого добавьте имя библиотеки в параметр `OpenTelemetry: DisabledSensors` файла `dtconfig.json`. Допускается использование звёздочки (`*`) для исключения всех имён областей инструментирования/библиотек, начинающихся с указанной строки. Использование звёздочки в начале или середине имени библиотеки не допускается.

```
{



"OpenTelemetry": {



"EnableIntegration": true,



"DisabledSensors": [



"com.example.MyLib",



"opentelemetry.urllib3*"



]



}



}
```

Альтернативно можно добавить параметр `open-telemetry-disabled-sensors` в аргумент JVM кодового модуля z/OS Java:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=open-telemetry-disabled-sensors=com.example.MyLib:opentelemetry.urllib3*
```

Если исключения указаны в командной строке, исключения в файле `dtconfig.json` игнорируются.

В командной строке используйте двоеточие `:` в качестве разделителя имён областей инструментирования/библиотек.

Приведённые примеры подавляют спаны из области инструментирования/библиотеки `com.example.MyLib`, а также спаны из всех библиотек, имя которых начинается с `opentelemetry.urllib3`.

## Правила отбора спанов для отчётности Dynatrace

В зависимости от `SpanKind`, Dynatrace подавляет часть спанов OpenTelemetry:

* Спан должен иметь тип `SpanKind.SERVER` или `SpanKind.CONSUMER`, либо иметь другой спан (`SpanContext`) в качестве нелокального (non-remote) родителя. Как правило, это обеспечивает Dynatrace Servlet sensor, который создаёт спан типа `SERVER` и устанавливает его как текущий активный спан.
* Дочерние спаны спанов типа `SpanKind.CLIENT` или `SpanKind.PRODUCER` будут подавляться. Например, после того как Dynatrace создаёт спан типа `SpanKind.CLIENT` для синхронного исходящего HTTP-вызова, все спаны, создаваемые в потоке, подавляются до завершения HTTP-вызова и соответствующего HTTP Span. В вызываемом сервисе можно создавать новые спаны, которые будут связаны корректно.

Подавленные спаны не будут отображаться в распределённых трассировках.

## Определение атрибута запроса для атрибутов спана

Для любого захваченного атрибута спана можно определить [атрибут запроса](/managed/observe/application-observability/services/request-attributes "Узнайте, что такое атрибуты запросов, и научитесь использовать их на всех уровнях представлений анализа сервисов."). Для этого:

1. Перейдите в **Settings** > **Server-side service monitoring** > **Request attributes**.
2. Нажмите **Define a new request attribute** и укажите имя и тип данных атрибута запроса.
3. Нажмите **Add new data source** и выберите `Span attribute` в качестве **Request attribute source**.
4. Введите **Attribute key**.
5. Нажмите **Save**.

Подробнее об атрибутах спана и их захвате см. в разделе [Настройки span](/managed/ingest-from/extend-dynatrace/extend-tracing/span-settings "Узнайте, как настраивать параметры span для OpenTelemetry и OpenTracing.").

![Использование атрибута спана как атрибута запроса](https://dt-cdn.net/images/screenshot-2022-09-30-at-09-24-35-1883-e2f2b63693.png)

Использование атрибута спана как атрибута запроса

**Attribute key** спанов можно найти на странице [Distributed traces](/managed/observe/application-observability/distributed-traces "Получите наблюдаемость высокораспределённых cloud-native архитектур для эффективной трассировки и анализа транзакций в режиме реального времени.") на вкладке **Code level** в разделе **Span attributes**.

![Атрибуты span](https://dt-cdn.net/images/span-attributes-1916-1967c4e21e.png)

Атрибуты span