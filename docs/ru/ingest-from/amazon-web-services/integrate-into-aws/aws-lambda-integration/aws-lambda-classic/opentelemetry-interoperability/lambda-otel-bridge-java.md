---
title: Совместимость OpenTelemetry в Java
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-java
scraped: 2026-03-05T21:29:34.371827
---

# Совместимость с OpenTelemetry в Java

# Совместимость с OpenTelemetry в Java

* Classic
* Reference
* 7 мин. чтения
* Обновлено 19 сентября 2024 г.

OneAgent версии 1.225+

Совместимость с OpenTelemetry связывает [расширение Dynatrace AWS Lambda](../aws-lambda-extension.md "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.") с OpenTelemetry Java API для использования пакетов инструментирования и расширений. Это позволяет отслеживать технологии, такие как базы данных или фреймворки обмена сообщениями, которые не поддерживаются расширением Dynatrace AWS Lambda по умолчанию.

## Прежде чем начать

Убедитесь, что [совместимость с OpenTelemetry включена](../opentelemetry-interoperability.md#enable "Включение и использование совместимости с OpenTelemetry в AWS Lambda.").

## Использование инструментирования OpenTelemetry Java

OpenTelemetry для Java предоставляет несколько пакетов инструментирования в своём [репозитории инструментирования OpenTelemetry Java](https://github.com/open-telemetry/opentelemetry-java-instrumentation), которые можно использовать совместно с расширением Dynatrace AWS Lambda для дополнительной видимости определённых технологий.

Пример: инструментирование AWS SDK для Java для мониторинга базы данных DynamoDB

Dynatrace версии 1.277+ Следующий пример показывает, как пакеты [инструментирования OpenTelemetry AWS SDK](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/aws-sdk) можно использовать для мониторинга вызовов к базе данных DynamoDB.

В зависимости от используемой версии AWS SDK добавьте один из следующих пакетов в конфигурацию вашего менеджера пакетов (например, Maven или Gradle).

После добавления пакета в качестве зависимости инструментирование для перехвата запросов к DynamoDB добавляется автоматически.

Чтобы инструментирование перехватило элемент, запросите его из DynamoDB с помощью AWS SDK, как показано в примере кода ниже.

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

После запуска приведённого выше примера кода вы увидите базу данных DynamoDB и отдельные запросы в соответствующем сервисе базы данных.

![Экран сервиса DynamoDB.](https://dt-cdn.net/images/mytable-1080-8529dae1d2.png)

## Использование OpenTelemetry Java API

[OpenTelemetry Java](https://opentelemetry.io/docs/instrumentation/java/) можно использовать в подходе, аналогичном SDK, для трассировки дополнительных операций, которые не покрываются Dynatrace по умолчанию.

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

Расширение Dynatrace AWS Lambda перехватывает только спаны, созданные через трассировщики из `GlobalOpenTelemetry`, и может не работать, если вы попытаетесь вручную (пере)настроить `GlobalOpenTelemetry`.

## Трассировка сообщений AWS SQS с помощью Java

OneAgent версии 1.267+

Вы можете использовать пакеты инструментирования с открытым исходным кодом для трассировки сообщений AWS SQS и SNS и сбора их через расширение Dynatrace AWS Lambda.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Установите необходимые зависимости**](#dependencies-java)[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Отправьте сообщение SQS/SNS**](#send-message-java)[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Получите сообщение SQS/SNS**](#receive-message-java)

### Шаг 1 Установите необходимые зависимости

Чтобы включить автоматическое инструментирование сообщений SQS, убедитесь, что установлено следующее.

1. AWS SDK версии 2.2+ для отправки сообщений.

   Вы можете использовать SDK v1 и v2 в одной Lambda-функции, если в вашей функции необходима версия v1.
2. [io.opentelemetry.instrumentation:opentelemetry-aws-sdk-2.2-autoconfigure](https://central.sonatype.com/artifact/io.opentelemetry.instrumentation/opentelemetry-aws-sdk-2.2-autoconfigure/1.27.0-alpha) версии 1.27+, добавленный как зависимость только для среды выполнения.

   Полный набор зависимостей, используемых в примерах, в формате Gradle выглядит следующим образом.

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

### Шаг 2 Отправьте сообщение SQS

Пример ниже показывает обработчик Lambda, который отправляет сообщение SQS.

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

Обратите внимание, что дополнительный код для трассировки не требуется, поскольку зависимость `runtimeOnly`, добавленная на первом
шаге, автоматически устанавливает обработчик, который создаёт спан в фоновом режиме при вызове `sendMessage`, используя
OpenTelemetry API, а OneAgent автоматически перехватывает этот спан.

Кроме того, необходимо [включить интеграцию OneAgent с OpenTelemetry](#before-you-start) и установить переменную окружения
[`OTEL_INSTRUMENTATION_AWS_SDK_EXPERIMENTAL_USE_PROPAGATOR_FOR_MESSAGING`](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/instrumentation/aws-sdk/README.md#settings-for-the-aws-sdk-instrumentation) в значение `true` в конфигурации вашей Lambda-функции.

### Шаг 3 Получение сообщения SQS/SNS

Получение сообщений работает из коробки при использовании AWS Lambda с триггером SQS, отслеживаемым через расширение Dynatrace AWS Lambda.

Поскольку спан может иметь только одного родителя, если ваша Lambda-функция получает пакет из нескольких сообщений, вам необходимо вручную создавать спаны для обработки каждого сообщения, если вы хотите отслеживать их отдельно и связывать с отправителем.

* Если этого достаточно, или у вас настроен максимальный размер пакета равный одному, или вы отправляете сообщения редко, дополнительный код или конфигурация не требуются.
* Если вы хотите получить больше информации в сценарии пакетной обработки с несколькими сообщениями, сначала необходимо применить определённую конфигурацию, позволяющую переопределить родительский спан.

  Чтобы [настроить расширение Dynatrace AWS Lambda](../aws-lambda-extension.md#lambda-cfg-method "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.") для ручной установки родительских спанов:

  + Для метода конфигурации через переменные окружения установите переменную окружения `DT_OPEN_TELEMETRY_ALLOW_EXPLICIT_PARENT` в значение `true`:

    ```
    DT_OPEN_TELEMETRY_ALLOW_EXPLICIT_PARENT=true
    ```
  + Для метода конфигурации через JSON-файл в файле `dtconfig.json` установите следующее поле в значение `true`:

    ```
    {



    ...other configuration properties...



    "OpenTelemetry": {



    "AllowExplicitParent": "true"



    }



    }
    ```

  После этого можно создавать новые спаны с родительским спаном, извлечённым из каждого полученного сообщения SQS.

Следующий код обрабатывает сообщения по одному и связывает их с отправителем в качестве родительского спана.

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

Когда вы развернёте обе Lambda-функции, добавите OneAgent, создадите очередь SQS, в которую `MessageSender` отправляет сообщения, и добавите триггер для `MessageIngress` для получения сообщений из этой очереди, а затем вызовете функцию `MessageSender` (например, используя тестовое событие по умолчанию), вы получите распределённую трассировку, которая выглядит примерно так:

![Снимок экрана распределённой трассировки, показывающей AWS Lambda, отправляющую сообщение SQS, и другую Lambda, получающую его, а также вручную созданный спан обработки](https://dt-cdn.net/images/pp-sqs-java-doc-1202-337e331f59.png)

Вы можете задаться вопросом, почему и принимающая функция, и спан обработки являются прямыми дочерними элементами спана `Sqs.SendMessage`, а не спан обработки является дочерним элементом вызова принимающей Lambda-функции.

Такая структура необходима для обеспечения готовности к пакетному приёму. Когда вы быстро отправляете несколько сообщений в очередь, ваш получатель может обработать пакет из максимум 10 сообщений одновременно. В этом случае существует несколько спанов отправителя из разных трассировок, и структура трассировки, реализованная в примере кода, гарантирует, что каждый спан обработки связан со спаном `Sqs.SendMessage` соответствующего сообщения. Поскольку спан может иметь только одного родителя, спан вызова принимающей Lambda может быть дочерним элементом только одного (случайного) отправителя.

## Связанные темы

* [Совместимость с OpenTelemetry](../opentelemetry-interoperability.md "Включение и использование совместимости с OpenTelemetry в AWS Lambda.")
* [Трассировка Lambda-функций на Python, Node.js и Java](../aws-lambda-extension.md "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")
