---
title: Пользовательские messaging services
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services
scraped: 2026-05-12T12:03:10.607481
---

# Пользовательские messaging services

# Пользовательские messaging services

* How-to guide
* 8-min read
* Updated on Oct 29, 2025

Dynatrace автоматически обнаруживает обработчики очередей сообщений на основе событий. Чтобы получить информацию о приложениях, использующих нестандартные или не основанные на событиях обработчики очередей сообщений, необходимо сначала определить пользовательский messaging service для ваших потребителей.

Для Java-приложений можно включить функции [автоматической инструментации Kafka-листенеров или SQS-поллеров](#automatic-instrumentation) вместо ручного определения messaging service.

## Определение messaging service

Чтобы определить пользовательский messaging service для ваших потребителей

1. Перейдите в **Settings** > **Service detection** > **Custom service detection**.
2. Выберите, на чём основан ваш messaging service — **Java**, **.NET** или **Node.js**, — затем выберите **Define messaging service**.
3. Задайте имя вашего messaging service, выберите технологию обмена сообщениями из списка, затем выберите **Find entry point**.
4. Выберите процесс, содержащий вашу точку входа, из списка и выберите **Continue**.
5. Найдите класс для инструментации, выберите нужный класс или файл и выберите **Continue**.
6. Java .NET Для инструментации класса можно

   * **Use the selected class** — для инструментации методов только выбранного класса.
   * **Use an implemented interface or superclass** — для инструментации методов любого интерфейса или суперкласса в иерархии классов. В этом случае выберите **Load inheritance** для загрузки всех доступных суперклассов и интерфейсов, затем выберите нужный.

   Node.js Выберите файл, содержащий пользовательский сервис. Dynatrace представит список методов, которые можно использовать как пользовательский сервис. Выберите нужный метод для завершения настройки.
7. Выберите методы для инструментации и выберите **Finish**.

   Ознакомьтесь с требованиями для [Apache Kafka](#kafka), [Amazon SQS SDK](#sqs-sdk) и [Spring Cloud AWS SQS](#spring-sqs) в разделе ниже.

   На странице **Define custom service** отобразятся вновь добавленные точка входа и методы.
8. Необязательно При необходимости добавьте дополнительные точки входа.
9. Необязательно Ограничьте новый пользовательский сервис определёнными группами процессов. См. раздел [Ограничение пользовательского сервиса конкретными группами процессов](#restrict) ниже.
10. Проверьте точку входа и методы для инструментации.
11. В правом нижнем углу страницы выберите **Save**.
12. .NET Node.js Перезапустите ваше потребительское приложение, чтобы пользовательский messaging service мог быть обнаружен.

### Amazon SQS SDK

Java

.NET

Пользовательские входящие messaging services для AWS SQS SDK должны определять в вашем коде метод, отвечающий за обработку одного сообщения SQS. Только такие методы могут использоваться как точка входа для messaging services AWS SQS SDK. Определённый метод должен иметь ровно один параметр `Message` (и любое количество других параметров).

Выберите метод, имеющий один из следующих аргументов. Требуется полный путь к пакету.

* [AWS SDKv1 SQS](https://dt-url.net/4942e9a) `com.amazonaws.services.sqs.model.Message`
* [AWS SDKv2 SQS](https://dt-url.net/pd62ee9) `software.amazon.awssdk.services.sqs.model.Message`

Необходимые атрибуты трассировки для входящей маркировки (`x-dynatrace`, `traceparent` и `tracestate`) добавляются OneAgent автоматически. Чтобы отключить эту опцию,

1. Установите свойство `optionDisableSqsReceiveAutomaticTracingMessageAttributesJava` в значение `true`.
2. В API SDK установите `messageAttributeNames` в `ReceiveMessageRequest` на упомянутые выше атрибуты трассировки или на `.*` или `All` для получения всех атрибутов сообщения.

Пользовательские входящие messaging services для AWS SQS SDK должны определять в вашем коде метод, отвечающий за обработку одного сообщения SQS. Только такие методы могут использоваться как точка входа для messaging services AWS SQS SDK. Определённый метод должен иметь ровно один параметр `Message` (и любое количество других параметров).

Выберите метод, имеющий объект `Amazon.SQS.Model.Message` в качестве аргумента. Аргумент может располагаться в любом месте списка параметров.

Необходимые атрибуты трассировки для входящей маркировки (`x-dynatrace`, `traceparent` и `tracestate`) добавляются OneAgent автоматически.

### Apache Kafka

Пользовательские messaging services для Apache Kafka должны определять в вашем коде метод, отвечающий за обработку одного Kafka-сообщения. Только такие методы могут использоваться как точка входа для Kafka messaging services.

Java

.NET

Node.js

Выберите метод, имеющий [Kafka](https://dt-url.net/ka03s3d) `org.apache.kafka.clients.consumer.ConsumerRecord` в качестве аргумента. Требуется полный путь к пакету.

Выберите метод, имеющий объект Kafka `ConsumeResult` или `Message` в качестве аргумента. Аргумент может располагаться в любом месте списка параметров.

Если у выбранного метода нет аргументов, контекст будет передан через `ThreadLocal` (на .NET Framework 4.5) или через `AsyncLocal` (на .NET Framework 4.6+ и .NET Core 2.0+).

Асинхронные методы без аргументов или без аргументов типа Kafka (`ConsumeResult` или `Message`) поддерживаются только на .NET Framework 4.6+ и .NET Core 2.0+.

OneAgent версии 1.233+:

OneAgent автоматически обнаруживает обработчики сообщений, зарегистрированные через обработчик `eachMessage` в качестве аргумента для `consumer.run()`.

OneAgent версии 1.327+:

OneAgent автоматически обнаруживает обработчики сообщений, зарегистрированные через обработчик `eachBatch`, переданный в `consumer.run()`.
Чтобы включить эту функцию:

1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
2. Включите переключатель **Node.js KafkaJs Consumer Automatic Detectionn**.

Кроме того, выполняйте итерацию по массиву `batch.messages` с использованием `forEach` или `map`. Не используйте цикл `for...of` — он не поддерживается для автоматического обнаружения.

Пример с использованием автоматического обнаружения

```
await consumer.run({



/* ... */



eachBatch: async (pl: EachBatchPayload) => {



/* alternatively can be used pl.batch.messages.map(...) */



pl.batch.messages.forEach((msg) => {



/* ... */



});



},



/* ... */



});
```

Если вы включите этот новый вариант и у вас уже настроен пользовательский messaging service, отключите пользовательский сервис на уровне тенанта:

1. Перейдите в **Settings** > **Service detection** > **Custom service detection**.
2. Выберите вкладку **NodeJS Services**.
3. Отключите переключатель для существующего имени сервиса для процесса, который будет использовать это автоматическое обнаружение.

Если вам необходимо использовать цикл `for...of`, используйте вариант с пользовательским messaging service (через Custom service detection).

OneAgent версии 1.325 и ранее:

Чтобы обнаружить обработчик `eachBatch`,

1. Создайте экспортируемую функцию с `EachMessagePayload` в качестве первого аргумента и выберите эту функцию как пользовательский сервис. Обратите внимание, что для обнаружения функции она должна быть импортирована из файла, отличного от файла с обработчиком `eachBatch`.
2. Адаптируйте обработчик `eachBatch` для вызова экспортируемой функции для каждого сообщения в пакете.

Пример с использованием определённого пользовательского сервиса

```
// file: handlers.ts



export async function processSingleMessage(msg: EachMessagePayload) : Promise<void> {}



// file: eachBatchHandler.ts



import { processSingleMessage } from "./handlers";



async function eachBatchHandler(pl: EachBatchPayload): Promise<void> {



/* ... */



for (const message of pl.batch.messages) {



/* ... */



const singlePayload: EachMessagePayload = {



message: message,



topic: pl.batch.topic,



partition: pl.batch.partition



};



await processSingleMessage(singlePayload);



/* ... */



}



}
```

### Spring Cloud AWS SQS

Java

* Если вы используете аннотацию `@SqsListener` или интерфейс [MessageListener](https://dt-url.net/7p02e18), дополнительная настройка не требуется.
* Если вы используете [SqsTemplate](https://dt-url.net/kq02erd), пользовательский messaging service для входящих Spring Cloud AWS SQS должен определять в вашем коде метод, отвечающий за обработку одного сообщения SQS. Этот метод можно использовать как точку входа для Spring Cloud AWS SQS messaging services. Определённый метод должен иметь ровно один параметр `Message` (и любое количество других параметров).

Выберите метод, имеющий ровно один параметр [Spring Cloud AWS SQS](https://dt-url.net/fq02e9l) `org.springframework.messaging.Message`, без параметров [AWS SDKv1 SQS](https://dt-url.net/4942e9a) `com.amazonaws.services.sqs.model.Message` и [AWS SDKv2 SQS](https://dt-url.net/pd62ee9) `software.amazon.awssdk.services.sqs.model.Message` и с любым количеством других параметров. Требуется полный путь к пакету.

Необходимые атрибуты трассировки для входящей маркировки (`x-dynatrace`, `traceparent` и `tracestate`) добавляются OneAgent автоматически. Чтобы отключить эту опцию, установите свойство `optionDisableSqsReceiveAutomaticTracingMessageAttributesJava` в значение `true`. В Spring имена атрибутов сообщений для получения по умолчанию установлены в `All`.

## Приоритет messaging services

Если у вас определено несколько пользовательских сервисов, оценка выполняется сверху вниз и применяется первое совпавшее правило. Если по какой-либо причине один и тот же класс и метод определён в нескольких пользовательских сервисах, убедитесь, что сервисы правильно расставлены по приоритету.

## Редактирование messaging service

Пользовательский сервис можно редактировать в любое время. Чтобы изменения вступили в силу, необходимо перезапустить затронутые процессы, если только для **Java** и **PHP** не активированы обновления в реальном времени. Для **.NET** и **Node.js** необходим перезапуск процесса.

Чтобы отредактировать пользовательский сервис, выберите кнопку **Edit** сервиса в списке сервисов. Вы можете

* Активировать или деактивировать существующие точки входа.
* Добавлять или удалять точки входа.
* Добавлять или удалять методы в точках входа.
* Ограничить пользовательский сервис определёнными группами процессов. См. раздел [Ограничение пользовательского сервиса конкретными группами процессов](#restrict) ниже.

### Обновления в реальном времени

Обновления пользовательских messaging services для Java и PHP могут применяться практически в реальном времени без перезапуска процессов. Чтобы активировать эту функцию, перейдите в **Settings** > **Server-side service detection** > **Deep monitoring** > **Real-time updates to Java and PHP services** и включите соответствующие переключатели.

Обратите внимание, что при использовании обновлений в реальном времени перезапускать процессы не нужно, однако такие обновления могут вызывать скачки нагрузки на CPU при развёртывании.

## Ограничение messaging service конкретными группами процессов

Использование любого пользовательского сервиса можно ограничить определёнными группами процессов. Правила пользовательского сервиса применяются только в указанных группах процессов и игнорируются в остальных. Ограничить пользовательский сервис можно при его создании или редактировании.

Чтобы ограничить пользовательский сервис

1. На странице **Define custom service** или **Edit service** разверните выпадающее меню **Optionally restrict custom service rules by process groups**.
2. Выберите **Add process group** и укажите группу процессов, в которой должен применяться пользовательский сервис.
3. Выберите **Add**.
4. В правом нижнем углу страницы **Define custom service** или **Edit service** выберите **Save**.

## Автоматическая инструментация

Для определённых технологий Dynatrace может создать пользовательский messaging service автоматически, инструментируя метод.

### Apache Kafka

Java

1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
2. Включите **Java Kafka - discover listeners automatically [Opt-In]**.

После включения Dynatrace будет автоматически создавать трассировку для каждого сообщения, инструментируя итераторы и итерируемые объекты, возвращаемые соответствующими методами (`.iterator()` и `.records(...)`) объекта `ConsumerRecords`. Обратите внимание, что для завершённости трассировок методы `next()` и `hasNext()` возвращаемого итератора должны вызываться до полной обработки списка и возврата `hasNext()` значения `false`.

Рекомендации для завершённых трассировок

Если ваш код содержит оператор `break;` в цикле или выбрасывается `Exception`, трассировки будут неполными. Чтобы избежать неполных трассировок, можно

* Включить опцию OneAgent `enableEscapedPathClosure` для автоматического закрытия последней трассировки. Обратите внимание, что эта опция имеет значительные накладные расходы по производительности.
* Использовать следующую структуру кода для получения и обработки сообщений:

  ```
  // Example from Apache Kafka v3 using ConsumerRecords.iterator()



  private void consumeRecords(Properties props, String topic) {



  try (KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props)) {



  consumer.subscribe(Collections.singletonList(topic));



  // When Java Kafka - discover listeners automatically [Opt-In] feature is enabled, Dynatrace instruments the Iterators and Iterables from this object



  ConsumerRecords<String, String> records = consumer.poll(500);



  if (records.isEmpty()) {



  return;



  }



  // Ensure that this for-loop does NOT have a "break;" statement



  for (ConsumerRecord<String, String> record : records) {



  try {



  processSingleRecord(sqsClient, message);



  } catch (Exception ex) {



  // Handle the exception, then continue the for-loop



  }



  }



  }



  }



  private void processSingleRecord(ConsumerRecord<String, String> record) {



  // Process the message



  }
  ```

### Amazon SQS SDK

Java

1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
2. Включите **Java AWS SQS SDK - instrument pollers automatically [Opt-In]**.

После включения Dynatrace будет автоматически создавать трассировку для каждого сообщения, инструментируя итераторы и итерируемые объекты, возвращаемые соответствующими методами (`.iterator()` и `.records(...)`) объекта `ReceiveMessageResult.getMessages()` (SDK v1) или `ReceiveMessageResponse.messages()` (SDK v2). Обратите внимание, что для завершённости трассировок методы `next()` и `hasNext()` возвращаемого итератора должны вызываться до полной обработки списка и возврата `hasNext()` значения `false`.

Рекомендации для завершённых трассировок

Если ваш код содержит оператор `break;` в цикле или выбрасывается `Exception`, трассировки будут неполными. Чтобы избежать неполных трассировок, можно

* Включить опцию OneAgent `enableEscapedPathClosure` для автоматического закрытия последней трассировки. Обратите внимание, что эта опция имеет значительные накладные расходы по производительности.
* Использовать следующую структуру кода для получения и обработки сообщений:

```
// Example from AWS SDK v2



private void receiveMessages(SqsClient sqsClient) {



ReceiveMessageResponse response = sqsClient.receiveMessage(ReceiveMessageRequest.builder()



.maxNumberOfMessages(10)



.queueUrl(queueUrl)



.build());



if (response == null || !response.hasMessages()) {



return;



}



// with the feature enabled, this list will be instrumented by Dynatrace



List<Message> messages = response.messages();



// ensure that this for-loop does NOT have a "break;" statement



for (Message message : messages) {



try {



processSingleMessage(message);



} catch (Exception ex) {



// handle the exception, then continue the for-loop



}



}



}



private void processSingleMessage(Message message) {



// process the message



}
```

## Связанные темы

* [API пользовательских сервисов](/managed/dynatrace-api/configuration-api/service-api/custom-services-api "Узнайте, что предлагает Dynatrace Configuration API для пользовательских сервисов.")