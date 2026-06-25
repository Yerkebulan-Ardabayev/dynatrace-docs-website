---
title: Совместимость с OpenTelemetry в Java
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-java
scraped: 2026-05-12T12:13:54.425664
---

# Совместимость с OpenTelemetry в Java

# Совместимость с OpenTelemetry в Java

* Reference
* 7-min read
* Updated on Apr 28, 2026

OneAgent версии 1.225+

Совместимость с OpenTelemetry связывает [расширение Dynatrace AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Мониторинг функций Lambda, написанных на Python, Node.js и Java.") с OpenTelemetry Java API, чтобы использовать пакеты инструментации и расширения. После этого можно отслеживать технологии вроде баз данных или фреймворков обмена сообщениями, которые расширение Dynatrace AWS Lambda не поддерживает «из коробки».

## Перед началом

Убедитесь, что [совместимость с OpenTelemetry включена](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability#enable "Включение и использование совместимости с OpenTelemetry в AWS Lambda.").

## Использование инструментации OpenTelemetry для Java

OpenTelemetry для Java предоставляет несколько пакетов инструментации в своём [репозитории инструментации OpenTelemetry Java](https://github.com/open-telemetry/opentelemetry-java-instrumentation), которые можно использовать вместе с расширением Dynatrace AWS Lambda для дополнительной наблюдаемости отдельных технологий.

Пример: инструментация AWS SDK для Java, чтобы мониторить базу данных DynamoDB

Dynatrace версии 1.277+ В примере ниже показано, как пакеты [инструментации OpenTelemetry для AWS SDK](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/aws-sdk) можно использовать для мониторинга вызовов базы данных DynamoDB.

В зависимости от используемой версии AWS SDK добавьте один из следующих пакетов в конфигурацию вашего пакетного менеджера (например, Maven или Gradle).

| Версия AWS SDK | Пакет для добавления | Примечания |
| --- | --- | --- |
| v1 | [opentelemetry-aws-sdk-1.11-autoconfigure](https://central.sonatype.com/artifact/io.opentelemetry.instrumentation/opentelemetry-aws-sdk-1.11-autoconfigure) | Экспериментальные атрибуты span необходимо включить через системное свойство (`otel.instrumentation.aws-sdk.experimental-span-attributes=true`) или переменную окружения (`OTEL_INSTRUMENTATION_AWS_SDK_EXPERIMENTAL_SPAN_ATTRIBUTES=true`). |
| v2 | [opentelemetry-aws-sdk-2.2-autoconfigure](https://central.sonatype.com/artifact/io.opentelemetry.instrumentation/opentelemetry-aws-sdk-2.2-autoconfigure) |  |

После добавления пакета в зависимости инструментация автоматически захватывает запросы к DynamoDB.

Чтобы инструментация захватила элемент, запросите его из DynamoDB с помощью AWS SDK, как показано в примере кода ниже.

```
import java.util.Map;



import com.amazonaws.services.lambda.runtime.Context;



import com.amazonaws.services.lambda.runtime.RequestHandler;



import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPEvent;



import com.amazonaws.services.lambda.runtime.events.APIGatewayV2HTTPResponse;



import software.amazon.awssdk.services.dynamodb.DynamoDbClient;



import software.amazon.awssdk.services.dynamodb.model.AttributeValue;



import software.amazon.awssdk.services.dynamodb.model.GetItemRequest;



public class SimpleDynamoDBSample implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse> {



public APIGatewayV2HTTPResponse handleRequest(APIGatewayV2HTTPEvent input, Context context) {



GetItemRequest request = GetItemRequest.builder()



.key(Map.of("mykey", AttributeValue.fromN("42")))



.tableName("MyTable")



.build();



try (DynamoDbClient dynamoDbClient = DynamoDbClient.builder().build()) {



dynamoDbClient.getItem(request);



} catch (Exception e) {



return APIGatewayV2HTTPResponse.builder().withBody("error!").withStatusCode(500).build();



}



return APIGatewayV2HTTPResponse.builder().withBody("success!").withStatusCode(200).build();



}



}
```

## Использование OpenTelemetry Java API

[OpenTelemetry Java](https://opentelemetry.io/docs/instrumentation/java/) можно использовать в SDK-стиле для трассировки дополнительных операций, не покрытых Dynatrace «из коробки».

```
@Override



public String handleRequest(Object input, Context context) {



Tracer tracer = GlobalOpenTelemetry.getTracer("instrumentation-library-name", "1.0.0");



Span span = tracer.spanBuilder("do some work").startSpan();



try {



span.setAttribute("foo", "bar");



// ....



return "Hello from OpenTelemetry Java!";



} finally {



span.end();



}



}
```

Расширение Dynatrace AWS Lambda захватывает только те span'ы, которые создаются через трейсеры из `GlobalOpenTelemetry`, и может не работать при попытке вручную (пере)настроить `GlobalOpenTelemetry`.

## Трассировка сообщений AWS SQS в Java

OneAgent версии 1.267+

Open-source пакеты инструментации позволяют трассировать сообщения AWS SQS и SNS и собирать их через расширение Dynatrace AWS Lambda.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Установите необходимые зависимости**](#dependencies-java)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Отправьте сообщение SQS/SNS**](#send-message-java)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Получите сообщение SQS/SNS**](#receive-message-java)

### Шаг 1. Установка необходимых зависимостей

Чтобы включить автоматическую инструментацию SQS-сообщений, убедитесь, что установлено следующее.

1. AWS SDK версии 2.2+ для отправки сообщений.

   В одной Lambda-функции можно использовать v1 и v2 SDK одновременно, если вам нужна версия v1.
2. [io.opentelemetry.instrumentation:opentelemetry-aws-sdk-2.2-autoconfigure](https://central.sonatype.com/artifact/io.opentelemetry.instrumentation/opentelemetry-aws-sdk-2.2-autoconfigure/1.27.0-alpha) версии 1.27+, добавленный как runtime-only зависимость.

   Полный набор зависимостей, используемых в примерах, в формате Gradle выглядит так.

   ```
   dependencies {



   // Instrumentation for SQS dependencies



   implementation(platform('io.opentelemetry.instrumentation:opentelemetry-instrumentation-bom-alpha:1.27.0-alpha'))



   runtimeOnly('io.opentelemetry.instrumentation:opentelemetry-aws-sdk-2.2-autoconfigure')



   // Only needed if you want to trace messages from batches separately



   implementation('io.opentelemetry:opentelemetry-api') // (Version taken from otel-instrumentation BOM)



   // Dependencies for the AWS SDK itself -- you should already have this in your Lambda if you send SQS messages



   implementation(platform('software.amazon.awssdk:bom:2.20.85'))



   implementation('software.amazon.awssdk:sqs') // Uses version from above BOM



   // Basic AWS Lambda dependencies -- you should already have this in your Lambda



   implementation('com.amazonaws:aws-lambda-java-events:3.6.0') // SQSEvent input, etc



   implementation('com.amazonaws:aws-lambda-java-core:1.2.1') // RequestHandler interface, etc



   }
   ```

### Шаг 2. Отправка SQS-сообщения

В примере ниже показан Lambda-обработчик, отправляющий SQS-сообщение.

```
package com.dynatrace.example.lambda;



import com.amazonaws.services.lambda.runtime.Context;



import com.amazonaws.services.lambda.runtime.RequestHandler;



import software.amazon.awssdk.services.sqs.SqsClient;



import software.amazon.awssdk.services.sqs.model.SendMessageResponse;



public class MessageSender implements RequestHandler<Object, Void> {



private static final SqsClient client = SqsClient.create();



@Override



public Void handleRequest(Object input, Context context) {



final SendMessageResponse resp = client.sendMessage(builder -> builder



.queueUrl("[your SQS-queue URL]")



.messageBody("[your payload]")



);



System.out.printf("Sent message with ID %s (send request ID %s)%n",



resp.messageId(),



resp.responseMetadata().requestId());



return null;



}



}
```

Дополнительный код для трассировки не нужен: зависимость `runtimeOnly`, добавленная на первом
шаге, автоматически устанавливает обработчик, который скрыто создаёт span внутри вызова `sendMessage`
с помощью OpenTelemetry API, и OneAgent подхватывает этот span автоматически.

Дополнительно нужно [включить интеграцию OneAgent с OpenTelemetry](#before-you-start) и установить переменную окружения
[`OTEL_INSTRUMENTATION_AWS_SDK_EXPERIMENTAL_USE_PROPAGATOR_FOR_MESSAGING`](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/aws-sdk/README.md#settings-for-the-aws-sdk-instrumentation) в значение `true` в конфигурации вашей Lambda-функции.

### Шаг 3. Получение сообщения SQS/SNS

Получение сообщений работает «из коробки» при использовании AWS Lambda с триггером SQS, мониторинг которой ведётся расширением Dynatrace AWS Lambda.

Поскольку у span'а может быть только один родитель, при получении вашей Lambda-функцией батча из нескольких сообщений необходимо вручную создавать span'ы для обработки каждого сообщения, если требуется отслеживать их по отдельности и связывать с отправителем.

* Если этого достаточно, либо если у вас настроен максимальный размер батча 1, либо сообщения отправляются редко, никакой дополнительный код или конфигурация не требуются.
* Если требуется больше деталей в сценарии с батчем из нескольких сообщений, сначала нужно применить настройку, позволяющую переопределить родительский span.

  Чтобы [настроить расширение Dynatrace AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Мониторинг функций Lambda, написанных на Python, Node.js и Java.") и разрешить ручную установку родительских span'ов:

  + Для метода конфигурации через переменные окружения установите переменную окружения `DT_OPEN_TELEMETRY_ALLOW_EXPLICIT_PARENT` в значение `true`:

    ```
    DT_OPEN_TELEMETRY_ALLOW_EXPLICIT_PARENT=true
    ```
  + Для метода конфигурации через JSON-файл в `dtconfig.json` установите следующее поле в `true`:

    ```
    {



    ...other configuration properties...



    "OpenTelemetry": {



    "AllowExplicitParent": "true"



    }



    }
    ```

  После этого новые span'ы можно создавать с родительским span'ом, извлечённым из каждого полученного SQS-сообщения.

Следующий код обрабатывает сообщения по одному и связывает их с отправителем как с родительским span'ом.

```
package com.dynatrace.example.lambda;



import java.util.Map;



import com.amazonaws.services.lambda.runtime.Context;



import com.amazonaws.services.lambda.runtime.RequestHandler;



import com.amazonaws.services.lambda.runtime.events.SQSEvent;



import io.opentelemetry.api.GlobalOpenTelemetry;



import io.opentelemetry.api.trace.Span;



import io.opentelemetry.api.trace.Tracer;



import io.opentelemetry.context.Scope;



import io.opentelemetry.context.propagation.TextMapGetter;



public class MessageIngress implements RequestHandler<SQSEvent, Void> {



private static final Tracer tracer = GlobalOpenTelemetry.getTracer("message-ingress-app");



@Override



public Void handleRequest(SQSEvent input, Context context) {



for (SQSEvent.SQSMessage message: input.getRecords()) {



Span span = tracer



.spanBuilder(message.getEventSource() + " process")



.setSpanKind(SpanKind.CONSUMER) // MUST be either CONSUMER or SERVER



.setParent(GlobalOpenTelemetry



.getPropagators()



.getTextMapPropagator()



.extract(



io.opentelemetry.context.Context.current(),



message.getMessageAttributes(),



SqsMessageRecordGetter.INSTANCE))



.startSpan();



try (Scope ignored = span.makeCurrent()) {



handleMessage(message);



} catch (Throwable e) {



span.recordException(e);



throw e;



} finally {



span.end();



}



}



return null;



}



private void handleMessage(SQSEvent.SQSMessage message) {



// This is where your actual handling code would go



System.out.printf("Handling message with ID %s...%n", message.getMessageId());



}



private enum SqsMessageRecordGetter implements TextMapGetter<Map<String, SQSEvent.MessageAttribute>> {



INSTANCE;



@Override



public Iterable<String> keys(Map<String, SQSEvent.MessageAttribute> carrier) {



return carrier.keySet();



}



@Override



public String get(Map<String, SQSEvent.MessageAttribute> carrier, String key) {



if (carrier == null) {



return null;



}



SQSEvent.MessageAttribute messageAttribute = carrier.get(key);



return messageAttribute == null ? null : messageAttribute.getStringValue();



}



}



}
```

Этот код требует зависимости от OpenTelemetry Java API и включения интеграции OpenTelemetry в OneAgent, как описано выше в разделе [Использование OpenTelemetry Java API](#use-opentelemetry-java-api).

Может возникнуть вопрос, почему и принимающая функция, и span обработки являются прямыми потомками span'а `Sqs.SendMessage`,
вместо того чтобы span обработки был потомком span'а принимающей Lambda-функции.

Такая структура необходима, чтобы поддерживать приём батчами. Если вы быстро отправляете в очередь несколько сообщений, ваш получатель может обработать батч до 10 сообщений за раз. В этом случае существует несколько отправляющих span'ов из разных трассировок, и структура трассировки, реализованная в примере, гарантирует, что каждый span обработки связан со span'ом `Sqs.SendMessage` соответствующего сообщения. Поскольку у span'а может быть только один родитель, span вызова принимающей Lambda-функции может быть потомком только одного (случайного) отправителя.

## Связанные темы

* [Совместимость с OpenTelemetry](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability "Включение и использование совместимости с OpenTelemetry в AWS Lambda.")
* [Трассировка Lambda-функций на Python, Node.js и Java](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Мониторинг функций Lambda, написанных на Python, Node.js и Java.")