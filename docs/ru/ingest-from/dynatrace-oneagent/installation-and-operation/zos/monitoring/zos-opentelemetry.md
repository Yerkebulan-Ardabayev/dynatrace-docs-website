---
title: Расширение трассировок с помощью OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-opentelemetry
scraped: 2026-03-06T21:19:43.227674
---

* Latest Dynatrace
* 7-min read

[OpenTelemetry](https://dt-url.net/y903u4j) — это набор инструментов, API и SDK, которые позволяют использовать данные телеметрии (распределённые трассировки, метрики и логи) для получения информации о производительности и поведении вашего приложения.

OpenTelemetry с Java-модулем z/OS позволяет обогащать или расширять распределённые трассировки.

* Обогащение распределённых трассировок проектно-специфичными дополнениями (например, вы можете добавлять в трассировки данные, релевантные для бизнеса, или фиксировать диагностическую информацию для разработчиков).
* Расширение распределённых трассировок (например, вы можете захватывать Java Transport, который не поддерживается Dynatrace «из коробки», или заполнять пробелы в наблюдаемости между приложениями для достижения транзакционной прозрачности).

Метрики и логи OpenTelemetry в настоящее время не поддерживаются Java-модулем z/OS.

Лицензирование

* Распределённые трассировки OpenTelemetry, захваченные Java-модулем z/OS, включены в лицензию на мейнфрейм.

## Совместимость с OpenTelemetry

OpenTelemetry версии 1.0+

Включение совместимости с OpenTelemetry связывает Java-модуль z/OS с API OpenTelemetry. При включении модуль перенаправляет определённые вызовы API OpenTelemetry (например, `GlobalOpenTelemetry`) на внутренний SDK Dynatrace OpenTelemetry.

Java-модуль z/OS передаёт захваченные [спаны OpenTelemetry](https://opentelemetry.io/docs/concepts/signals/traces/#spans-in-opentelemetry) через [подсистему zDC](../installation/install-zos-java.md "Set up Java monitoring on z/OS using the Java module.") и [модуль zRemote](../installation/install-zremote.md "Prepare and install the zRemote for z/OS monitoring.") в вашу среду Dynatrace.

![z/OS Java OpenTelemetry](https://dt-cdn.net/images/zos-java-otel-1369-e7b35738b0.png)

Рекомендация: избегайте использования SDK OpenTelemetry в ваших приложениях совместно с совместимостью Dynatrace OpenTelemetry, так как это может привести к конфликтам.

### Включение совместимости с OpenTelemetry

Совместимость с OpenTelemetry отключена по умолчанию. Чтобы включить её, добавьте атрибут `OpenTelemetry: EnableIntegration` в файл `dtconfig.json`, как показано в следующем примере.

Как правило, вы создали файл `dtconfig.json` во время [установки Java-модуля z/OS](../installation/install-zos-java.md#download "Set up Java monitoring on z/OS using the Java module.") и установили атрибуты `Tenant`, `ClusterID` и `zdcName` для вашей среды.

```
{
"OpenTelemetry": {
"EnableIntegration": true
}
}
```

В качестве альтернативы вы можете добавить параметр `open-telemetry-enable-integration` в аргумент JVM Java-модуля z/OS:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=open-telemetry-enable-integration=true
```

## Примеры инструментирования OpenTelemetry

Для поддержки различных сценариев использования OpenTelemetry позволяет добавлять вендоро-нейтральное пользовательское инструментирование в ваши приложения. Инструментирование приложений с помощью OpenTelemetry требует знаний программирования и доступа к коду приложения. Чтобы узнать, как инструментировать приложение, обратитесь к [документации OpenTelemetry](https://dt-url.net/7603uf3) и [документации OpenTelemetry Java](https://dt-url.net/n823ur4).

Ниже приведены примеры использования [OpenTelemetry Java](https://dt-url.net/yo43um9).

Обогащение трассировок проектно-специфичными дополнениями

В этом примере показано, как можно захватить дополнительную операцию в Java-приложении, работающем на WebSphere Application Server, который мониторится Dynatrace.

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
2. Используйте `Tracer` для захвата операции, включая некоторые атрибуты.

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

![z/OS OpenTelemetry code-level](https://dt-cdn.net/images/zos-opentelemetry-1-1926-e67ad2add3.png)

Расширение сквозных трассировок

В этом примере показано, как можно трассировать сервис аудита, работающий на WebSphere Application Server (мониторится Dynatrace), который использует Java-транспорт, не поддерживаемый «из коробки». В качестве примера такого неподдерживаемого Java-транспорта мы используем Java-сериализацию (потоки вывода объектов).

Чтобы узнать больше о распространении контекста, обратитесь к официальной [документации по распространению контекста OpenTelemetry](https://dt-url.net/j503uhz).

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

**Service B** читает запись аудита из `ObjectInputStream`:

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

Dynatrace отображает полную сквозную трассировку как распределённую трассировку, содержащую `auditEntry` в качестве метода сервиса, включающего захваченные атрибуты и измеренное время выполнения. Метод сервиса `auditEntry` является результатом трассировки метода `receivedAuditEntry` с его новым спаном. То, что он отображается как дочерний элемент метода сервиса `/orderReceived`, является результатом вызовов `inject` и `extract` в `TextMapPropagator`.

![z/OS OpenTelemetry service](https://dt-cdn.net/images/zos-opentelemetry-2-1926-9f66be4562.png)

## Подавление спанов от определённых инструментариев

Вы можете подавить спаны, поступающие от определённой области инструментирования/библиотеки. Для этого добавьте имя библиотеки в параметр `OpenTelemetry: DisabledSensors` в файле `dtconfig.json`. Вы можете использовать звёздочку (`*`) для исключения всех имён областей инструментирования/библиотек, начинающихся с указанной строки. Нельзя использовать звёздочку в начале или в середине имени библиотеки.

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

В качестве альтернативы вы можете добавить параметр `open-telemetry-disabled-sensors` в аргумент JVM Java-модуля z/OS:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=open-telemetry-disabled-sensors=com.example.MyLib:opentelemetry.urllib3*
```

Если вы указываете исключения в командной строке, исключения в файле `dtconfig.json` игнорируются.

Используйте двоеточие `:` в качестве разделителя имён областей инструментирования/библиотек в командной строке.

Приведённые выше примеры подавляют спаны от области инструментирования/библиотеки `com.example.MyLib` и спаны от всех библиотек, начинающихся с имени `opentelemetry.urllib3`.

## Правила для спанов, которые Dynatrace будет передавать

В зависимости от `SpanKind` Dynatrace подавляет некоторые спаны OpenTelemetry:

* Спан должен быть либо типа `SpanKind.SERVER` или `SpanKind.CONSUMER`, либо иметь другой спан (`SpanContext`) в качестве нелокального родителя. Обычно это обеспечивается сенсором Servlet Dynatrace, который создаёт спан типа `SERVER` и устанавливает его как текущий активный спан.
* Дочерние спаны спанов типа `SpanKind.CLIENT` или `SpanKind.PRODUCER` будут подавлены. Например, после того как Dynatrace создаёт спан типа `SpanKind.CLIENT` для синхронного исходящего HTTP-вызова, все спаны, созданные в потоке, будут подавлены до завершения HTTP-вызова и, соответственно, HTTP-спана. Вы, конечно, можете создавать новые спаны в вызываемом сервисе, и они будут связаны корректно.

Подавленные спаны не будут видны в распределённых трассировках.

## Определение атрибута запроса для атрибутов спана

Вы можете определить [атрибут запроса](../../../../../observe/application-observability/services/request-attributes.md "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") для любого захваченного атрибута спана. Для этого

1. Перейдите в **Settings** > **Server-side service monitoring** > **Request attributes**.
2. Выберите **Define a new request attribute** и введите имя и тип данных вашего атрибута запроса.
3. Выберите **Add new data source** и выберите `Span attribute` в качестве **Request attribute source**.
4. Введите ваш **Attribute key**.
5. Выберите **Save**.

Чтобы узнать больше об атрибутах спанов и о том, как их захватывать, см. [Span settings](../../../../extend-dynatrace/extend-tracing/span-settings.md "Learn how to configure span settings for OpenTelemetry and OpenTracing.").

![Use Span attribute as a request attribute](https://dt-cdn.net/images/screenshot-2022-09-30-at-09-24-35-1883-e2f2b63693.png)

Вы можете найти **Attribute key** ваших спанов на странице [Distributed traces](../../../../../observe/application-observability/distributed-traces.md "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") на вкладке **Code level** в разделе **Span attributes**.

![Span attributes](https://dt-cdn.net/images/span-attributes-1916-1967c4e21e.png)
