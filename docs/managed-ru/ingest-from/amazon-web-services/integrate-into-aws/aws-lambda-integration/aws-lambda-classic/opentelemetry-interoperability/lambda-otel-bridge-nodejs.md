---
title: Совместимость с OpenTelemetry в Node.js
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-nodejs
scraped: 2026-05-12T12:15:12.275412
---

# Совместимость с OpenTelemetry в Node.js

# Совместимость с OpenTelemetry в Node.js

* How-to guide
* 9-min read
* Updated on Apr 28, 2026

OneAgent версии 1.229+

Совместимость с OpenTelemetry связывает [расширение Dynatrace AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Мониторинг функций Lambda, написанных на Python, Node.js и Java.") с инструментацией OpenTelemetry для Node.js, чтобы использовать пакеты инструментации и расширения. После этого можно отслеживать технологии вроде баз данных или фреймворков обмена сообщениями, которые расширение Dynatrace AWS Lambda не поддерживает «из коробки».

## Перед началом

* Убедитесь, что [совместимость с OpenTelemetry включена](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability#enable "Включение и использование совместимости с OpenTelemetry в AWS Lambda.").
* Проверьте, что установленная версия JavaScript OpenTelemetry API совместима с расширением Dynatrace AWS Lambda. В таблице ниже указаны совместимые версии:

  | Версия OneAgent | Максимальная версия OpenTelemetry API |
  | --- | --- |
  | 1.297+ | 1.9.x |
  | 1.289+ | 1.8.x |
  | 1.283+ | 1.7.x |
  | 1.279+ | 1.6.x |
  | 1.261+ | 1.4.x |
  | 1.259+ | 1.3.x |
  | 1.257+ | 1.2.x |
  | 1.241+ | 1.1.x |
  | 1.229+ | 1.0.x |

## Использование инструментации OpenTelemetry для Node.js

При использовании инструментации OpenTelemetry для Node.js настройка всех необходимых компонентов OpenTelemetry SDK и регистрация TracerProvider выполняются расширением Dynatrace AWS Lambda автоматически, поэтому регистрировать ещё один TracerProvider не требуется.

Пакеты инструментации для JavaScript можно найти в [репозитории OpenTelemetry JavaScript contributions](https://github.com/open-telemetry/opentelemetry-js-contrib). Обратите внимание:

* Некоторые инструментации могут конфликтовать с HTTP- и Lambda-инструментациями Dynatrace и автоматически подавляются. К ним относятся [@opentelemetry/instrumentation-http](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation-http) и [@opentelemetry/instrumentation-aws-lambda](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/node/opentelemetry-instrumentation-aws-lambda).
* Использовать [@opentelemetry/auto-instrumentations-node](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/instrumentation-aws-lambda-v0.26.0/metapackages/auto-instrumentations-node) не рекомендуется, поскольку он включает большое количество различных инструментаций.
* Если для инструментации [AWS SDK V3](https://github.com/aws/aws-sdk-js-v3), доступного в Lambda-средах выполнения Node.js v18 и v20, используется [`opentelemetry/instrumentation-aws-sdk`](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk), инструментация работает начиная с версии 0.36.0+.

Пример: инструментация запросов в Lambda-функции на Node.js через пакет инструментации

В примере кода ниже показано, как выполнить инструментацию запросов к [PostgreSQL](https://www.postgresql.org/) в Lambda-функции на Node.js с помощью пакета инструментации [opentelemetry-instrumentation-pg](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/node/opentelemetry-instrumentation-pg).

```
const { registerInstrumentations } = require('@opentelemetry/instrumentation');



const { PgInstrumentation } = require('@opentelemetry/instrumentation-pg');



// You must create the PgInstrumentation (and other instrumentations)



// before loading any corresponding modules, such as `require('pg')`.



registerInstrumentations({



instrumentations: [



new PgInstrumentation(),



],



});



const { Client } = require('pg');



exports.handler = async function myHandler(event, context) {



let client;



try {



client = new Client(/* DB connection information */);



await client.connect();



const result = await client.query('SELECT * FROM users;');



return result.rows;



} finally {



client?.end();



}



}
```

Для инструментации [AWS SDK для JavaScript](https://aws.amazon.com/sdk-for-javascript/) OpenTelemetry предоставляет пакет инструментации [`opentelemetry/instrumentation-aws-sdk`](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk).

Пример: инструментация AWS SDK для JavaScript, чтобы мониторить базу данных DynamoDB

В примере кода ниже показано, как пакет инструментации [`opentelemetry/instrumentation-aws-sdk`](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk) можно использовать для добавления observability к вызовам базы данных DynamoDB (Dynatrace версии 1.244+).

```
const AWS = require('aws-sdk');



const { registerInstrumentations } = require('@opentelemetry/instrumentation');



const { AwsInstrumentation } = require('@opentelemetry/instrumentation-aws-sdk');



registerInstrumentations({



instrumentations: [



new AwsInstrumentation()



]



});



exports.handler = function(event, context) {



const ddb = new AWS.DynamoDB();



const dbParamsGetDelete = {



TableName: 'E2E_test_table',



Key: {



'svnr': { N: '1234'}



}



};



ddb.getItem(dbParamsGetDelete, function(err, data) {



if (err) {



console.error('Error', err);



} else {



console.log('Success', data.Item);



}



});



};
```

## Использование OpenTelemetry Node.js API

[OpenTelemetry JavaScript](https://github.com/open-telemetry/opentelemetry-js) можно использовать в SDK-стиле для трассировки дополнительных операций, не покрытых пакетом инструментации.

```
const opentelemetry = require('@opentelemetry/api');



const tracer = opentelemetry.trace.getTracer('my-package-name');



exports.handler = function(event, context) {



// create a span using the OTel API



const span = tracer.startSpan('do some work');



span.setAttribute('foo', 'bar');



span.end();



// ...



const response = {



statusCode: 200,



body: JSON.stringify('Hello from Node.js'),



};



return response;



};
```

## Трассировка сообщений AWS SQS и SNS в Node.js

OneAgent версии 1.253+ для SQS, OneAgent версии 1.257+ для SNS

Для трассировки сообщений AWS SQS и SNS и сбора трассировок через расширение Dynatrace AWS Lambda можно использовать пакет [@opentelemetry/instrumentation-aws-sdk](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk).

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Установите необходимые зависимости**](#dependencies-node)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Настройте трассировку**](#set-up-tracing-node)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Отправьте сообщение SQS/SNS**](#sqs-message-node)[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Получите сообщение SQS/SNS**](#receive-message-node)

### Шаг 1. Установка необходимых зависимостей

```
npm install @opentelemetry/api @opentelemetry/instrumentation-aws-sdk @opentelemetry/instrumentation aws-sdk
```

### Шаг 2. Настройка трассировки

Используйте следующий код, чтобы настроить трассировку для отправки SQS-сообщений в SQS-очередь из Node.js-приложения, мониторинг которого ведётся Dynatrace:

```
const { AwsInstrumentation } = require('@opentelemetry/instrumentation-aws-sdk');



const { registerInstrumentations } = require('@opentelemetry/instrumentation');



// The instrumentation must be registered before importing the aws-sdk module!



registerInstrumentations({



instrumentations: [



new AwsInstrumentation()



]



});



// You can now import the aws-sdk module if needed:



const AWS = require('aws-sdk');
```

### Шаг 3. Отправка сообщения SQS/SNS

* Через HTTP-сервер Node.js:

  При выполнении запроса к HTTP-серверу отправляется сообщение в очередь SQS или топик SNS. Если на момент отправки сообщения корневой span трассировки ещё не существует, корневой span необходимо создать вручную. Подробности о ручном создании span см. в разделе [Использование OneAgent с данными OpenTelemetry](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.").

  Пример

  В этом примере кода корневой span трассировки для входящего HTTP-запроса создаётся самим трейсером.

  ```
  const http = require("http");



  const AWS = require('aws-sdk');



  const sqs = new AWS.SQS();



  const sns = new AWS.SNS();



  const server = http.createServer((req, res) => {



  const messageSendCallback = function (err, message) {



  if (err) {



  console.log("failed to send a message: " + err);



  res.writeHead(500);



  res.end("failure");



  } else {



  console.log("Success", message.MessageId);



  res.writeHead(200);



  res.end("success");



  }



  }



  if (req.url === "/send-sqs-message") {



  const params = {



  DelaySeconds: 10,



  MessageBody: "[your payload]",



  QueueUrl: "[your SQS-queue URL]"



  };



  sqs.sendMessage(params, messageSendCallback);



  } else if (req.url === "/send-sns-message") {



  const params = {



  Message: "[your payload]",



  TopicArn: "[your SNS-topic ARN]"



  };



  sns.publish(params, messageSendCallback);



  } else {



  res.writeHead(404);



  res.end("not found");



  }



  });



  server.on("close", () => { console.log("Closing server") });



  server.listen(8004, () => {



  console.log("server started!");



  });
  ```

  Второй узел в распределённой трассировке с именем `sqs-minimal-sample-nodejs-receiver-trigger send` представляет отправленное SQS-сообщение и генерируется инструментацией [aws-sdk](https://www.npmjs.com/package/aws-sdk).

  Поскольку пакет `aws-sdk` использует HTTP-запросы для отправки SQS-сообщений, выполняется вызов `Requests to public networks`, который перехватывается HTTP-инструментацией OneAgent. Вызов `invoke` поступает от Lambda-функции AWS, подписанной на очередь SQS, мониторинг которой ведётся расширением Dynatrace AWS Lambda.
* Через Lambda-функцию AWS

  Отправить SQS- или SNS-сообщение можно из Lambda-функции AWS, мониторинг которой ведётся расширением Dynatrace AWS Lambda.

  SQS

  SNS

  ```
  const AWS = require('aws-sdk');



  exports.handler = function (event, context, callback) {



  const sqs = new AWS.SQS();



  const params = {



  DelaySeconds: 10,



  MessageBody: "[your payload]",



  QueueUrl: "[your SQS-queue URL]"



  };



  sqs.sendMessage(params, function (err, data) {



  if (err) {



  context.succeed({



  statusCode: 500,



  body: err,



  });



  } else {



  console.log("SQS-Success", data.MessageId);



  context.succeed({



  statusCode: 200,



  body: "SQS-Success",



  });



  }



  });



  }
  ```

  ```
  const AWS = require('aws-sdk');



  exports.handler = function (event, context, callback) {



  const sns = new AWS.SNS();



  const params = {



  Message: "[your payload]",



  TopicArn: "[your SNS-topic ARN]"



  };



  sns.publish(params, function (err, data) {



  if (err) {



  context.succeed({



  statusCode: 500,



  body: err,



  });



  } else {



  console.log("SNS-Success", data.MessageId);



  context.succeed({



  statusCode: 200,



  body: "SNS-Success",



  });



  }



  });



  }
  ```

### Шаг 3. Получение сообщения SQS/SNS

SQS

SNS

Трассировать SQS-сообщения можно, когда они приходят из

* SQS-топика

  Расширение Dynatrace AWS Lambda автоматически извлекает родителя и создаёт Lambda-span, когда Lambda-функция AWS запускается через AWS SQS.
  При получении батча из нескольких сообщений учитывается только последнее сообщение, оно же используется для извлечения родителя.

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
* SNS-топика

  Для SNS-сообщений, пересылаемых в SQS, формат сообщения зависит от настройки [raw message delivery](https://docs.aws.amazon.com/sns/latest/dg/sns-large-payload-raw-message-delivery.html) у SNS-подписки.

  | Raw message delivery | Формат сообщения | Пример |
  | --- | --- | --- |
  | Включена | Атрибуты SNS-сообщения конвертируются в атрибуты SQS-сообщения, и родитель извлекается напрямую из `MessageAttributes` SQS-сообщения. | + [Получение батча из нескольких сообщений](#receive-example) |
  | Отключена | SNS-сообщение и его `MessageAttributes` доставляются как сериализованная JSON-строка в теле полученного SQS-сообщения. Чтобы корректно связать span получения, родителя нужно извлечь из `MessageAttributes` сериализованного SNS-сообщения. | + [Получение батча из нескольких сообщений](#receive-example)   Для этого примера требуется дополнительная настройка. При вызове метода `extractParent` установите значение параметра `fromSnsPayload` в `true`. |

Lambda-функции AWS, запускаемые из SNS, поддерживаются «из коробки» при мониторинге через расширение Dynatrace AWS Lambda.

SNS-топики можно настроить через подписку на пересылку сообщений в очередь SQS. Затем сообщения из очереди SQS могут потребляться Lambda-функцией. Трассировка полученных сообщений в Lambda-функции AWS, запускаемой через SQS, работает «из коробки», когда AWS Lambda мониторится расширением Dynatrace AWS Lambda. Однако tracer может выбрать только одного родителя, и если ваша Lambda-функция получает батчи из нескольких сообщений, требуется специальная обработка для отдельного отслеживания каждого сообщения.

Подробнее см. [получение SQS-сообщения](#receive-sqs-node).

## Связанные темы

* [Совместимость с OpenTelemetry](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability "Включение и использование совместимости с OpenTelemetry в AWS Lambda.")
* [Трассировка Lambda-функций на Python, Node.js и Java](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Мониторинг функций Lambda, написанных на Python, Node.js и Java.")