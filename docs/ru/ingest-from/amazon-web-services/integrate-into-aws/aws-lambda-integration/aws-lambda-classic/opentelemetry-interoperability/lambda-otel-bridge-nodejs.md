---
title: Совместимость OpenTelemetry в Node.js
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-nodejs
scraped: 2026-03-05T21:31:32.532091
---

# Совместимость с OpenTelemetry в Node.js


OneAgent версии 1.229+

Совместимость с OpenTelemetry связывает [расширение Dynatrace AWS Lambda](../aws-lambda-extension.md "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.") с инструментированием OpenTelemetry Node.js для использования пакетов инструментирования и расширений. Это позволяет отслеживать технологии, такие как базы данных или фреймворки обмена сообщениями, которые не поддерживаются расширением Dynatrace AWS Lambda из коробки.

## Перед началом

* Убедитесь, что [совместимость с OpenTelemetry включена](../opentelemetry-interoperability.md#enable "Включение и использование совместимости с OpenTelemetry в AWS Lambda.").
* Убедитесь, что установленная версия JavaScript OpenTelemetry API совместима с расширением Dynatrace AWS Lambda. В следующей таблице перечислены совместимые версии:

  | Версия OneAgent | Максимальная версия OpenTelemetry API |
  | --- | --- |
  | 1.229+ | 1.0.x |
  | 1.241+ | 1.1.x |
  | 1.257+ | 1.2.x |
  | 1.259+ | 1.3.x |
  | 1.261+ | 1.4.x |
  | 1.279+ | 1.6.x |
  | 1.283+ | 1.7.x |
  | 1.289+ | 1.8.x |
  | 1.297+ | 1.9.x |

## Использование инструментирования OpenTelemetry Node.js

При использовании инструментирования OpenTelemetry Node.js конфигурация всех необходимых компонентов SDK OpenTelemetry и регистрация TracerProvider автоматически выполняются расширением Dynatrace AWS Lambda, поэтому вам не нужно регистрировать другой TracerProvider.

Пакеты инструментирования для JavaScript можно найти в [репозитории дополнений OpenTelemetry JavaScript](https://github.com/open-telemetry/opentelemetry-js-contrib). Обратите внимание, что:

* Некоторые инструментирования могут конфликтовать с HTTP- и Lambda-инструментированием Dynatrace и автоматически подавляются. К ним относятся [@opentelemetry/instrumentation-http](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation-http) и [@opentelemetry/instrumentation-aws-lambda](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/node/opentelemetry-instrumentation-aws-lambda).
* Использование [@opentelemetry/auto-instrumentations-node](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/instrumentation-aws-lambda-v0.26.0/metapackages/auto-instrumentations-node) не рекомендуется, так как он включает множество различных инструментирований.
* Если [`opentelemetry/instrumentation-aws-sdk`](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk) используется для инструментирования [AWS SDK V3](https://github.com/aws/aws-sdk-js-v3), предоставляемого средами выполнения Node.js v18 и v20 Lambda, он будет работать для версии инструментирования 0.36.0+.

Пример: Инструментирование вызовов в Node.js Lambda-функции через пакет инструментирования

Следующий пример кода показывает, как инструментировать вызовы к [PostgreSQL](https://www.postgresql.org/) в Node.js Lambda-функции с помощью пакета инструментирования [opentelemetry-instrumentation-pg](https://github.com/open-telemetry/opentelemetry-js-contrib/tree/main/plugins/node/opentelemetry-instrumentation-pg).

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

Для инструментирования [AWS SDK для JavaScript](https://aws.amazon.com/sdk-for-javascript/) OpenTelemetry предоставляет пакет инструментирования [`opentelemetry/instrumentation-aws-sdk`](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk).

Пример: Инструментирование AWS SDK для JavaScript для мониторинга базы данных DynamoDB

Следующий пример кода показывает, как пакет инструментирования [`opentelemetry/instrumentation-aws-sdk`](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk) можно использовать для добавления наблюдаемости вызовов к базе данных DynamoDB (Dynatrace версии 1.244+).

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

После запуска приведённого выше фрагмента кода страница сервиса DynamoDB выглядит следующим образом.

![Экран сервиса DynamoDB.](https://dt-cdn.net/images/dynamodb-python-nodejs-954-c0c7c41ba8.png)

## Использование OpenTelemetry Node.js API

[OpenTelemetry JavaScript](https://github.com/open-telemetry/opentelemetry-js) можно использовать в подходе, подобном SDK, для трассировки дополнительных операций, не охваченных пакетами инструментирования.

```
const opentelemetry = require('@opentelemetry/api');


const tracer = opentelemetry.trace.getTracer('my-package-name');


exports.handler = function(event, context) {


// создание спана с помощью OTel API


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

## Трассировка сообщений AWS SQS и SNS с Node.js

OneAgent версии 1.253+ для SQS, OneAgent версии 1.257+ для SNS

Вы можете использовать пакет [@opentelemetry/instrumentation-aws-sdk](https://www.npmjs.com/package/@opentelemetry/instrumentation-aws-sdk) для трассировки сообщений AWS SQS и SNS и сбора трассировок через расширение Dynatrace AWS Lambda.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Установка необходимых зависимостей**](#dependencies-node)[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка трассировки**](#set-up-tracing-node)[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Отправка сообщения SQS/SNS**](#sqs-message-node)[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Получение сообщения SQS/SNS**](#receive-message-node)

### Шаг 1: Установка необходимых зависимостей

```
npm install @opentelemetry/api @opentelemetry/instrumentation-aws-sdk @opentelemetry/instrumentation aws-sdk
```

### Шаг 2: Настройка трассировки

Используйте следующий код для настройки трассировки отправки SQS-сообщений в очередь SQS из приложения Node.js, отслеживаемого Dynatrace:

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

### Шаг 3: Отправка сообщения SQS/SNS

* Через HTTP-сервер Node.js:

  При выполнении запроса к HTTP-серверу сообщение отправляется в очередь SQS или топик SNS. Если вы отправляете сообщение до создания корневого спана трассировки, убедитесь, что корневой спан трассировки создан вручную. Подробнее о ручном создании спанов с OpenTelemetry см. [Использование OneAgent с данными OpenTelemetry](../../../../../dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel.md "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.").

  Пример

  В этом примере кода корневой спан трассировки для входящего HTTP-запроса создаётся трейсером.

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

  Запрос к пути `/send-sqs-message` должен создать трассировки, как показано ниже.

  ![Пример SQS PurePath с OneAgent](https://dt-cdn.net/images/oneagent-sqs-example-1952-4d30da5989.png)

  Второй узел в распределённой трассировке с именем `sqs-minimal-sample-nodejs-receiver-trigger send` представляет отправленное SQS-сообщение и генерируется инструментированием [aws-sdk](https://www.npmjs.com/package/aws-sdk).

  Поскольку пакет `aws-sdk` использует HTTP-запросы для отправки SQS-сообщений, присутствует вызов `Requests to public networks`, которые перехватываются HTTP-инструментированием OneAgent. Вызов `invoke` исходит от Lambda-функции AWS, подписанной на очередь SQS, которая отслеживается расширением Dynatrace AWS Lambda.
* Через Lambda-функцию AWS

  Вы можете отправить SQS- или SNS-сообщение из Lambda-функции AWS, отслеживаемой расширением Dynatrace AWS Lambda.

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

  Результирующая распределённая трассировка аналогична примеру приложения Node.js:

  ![Пример PurePath для трассировки SQS между двумя Lambda-функциями](https://dt-cdn.net/images/sqs-lambda-to-lambda-2111-453f468beb.png)

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

### Шаг 3: Получение сообщения SQS/SNS

SQS

SNS

Вы можете трассировать SQS-сообщения, перенаправленные из

* Топика SQS

  Расширение Dynatrace AWS Lambda автоматически извлекает родительский элемент и создаёт спан Lambda, когда Lambda-функция AWS запускается AWS SQS. Однако, когда получается пакет из нескольких сообщений, учитывается только последнее сообщение и используется для распространения родительского элемента. Для распространения родителей из пакета нескольких входящих сообщений вы можете, например, вручную создать спаны с родителем из каждого сообщения.

  Чтобы [настроить расширение Dynatrace AWS Lambda](../aws-lambda-extension.md#lambda-cfg-method "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.") для ручной установки родительских спанов:

  + Для метода конфигурации через переменные окружения установите переменную окружения `DT_OPEN_TELEMETRY_ALLOW_EXPLICIT_PARENT` в `true`:

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

  Затем можно создавать новые спаны с родительским спаном, извлечённым из каждого полученного SQS-сообщения.

  Пример: Получение пакета из нескольких сообщений

  ```
  const { propagation, ROOT_CONTEXT, trace, SpanKind } = require("@opentelemetry/api");


  const { MessagingOperationValues, SemanticAttributes } = require("@opentelemetry/semantic-conventions");


  const AWS = require("aws-sdk");


  const queueUrl = "[sqs queue url]";


  const tracer = trace.getTracer("my-receiver");


  exports.handler = async (event) => {


  const sqs = new AWS.SQS();


  await new Promise((resolve, reject) => {


  const receiveParams = {


  MaxNumberOfMessages: 10,


  QueueUrl: queueUrl,


  // MessageAttributeNames not needed if @opentelemetry/instrumentation-aws-sdk is used


  MessageAttributeNames: propagation.fields()


  };


  sqs.receiveMessage(receiveParams, function (err, data) {


  if (err) {


  console.log("ERROR: ", err);


  reject(err);


  } else if (data.Messages?.length) {


  data.Messages.forEach((msg) => {


  console.log("message received:", msg.MessageId)


  // manual span creation


  const ctx = extractParent(msg, /*fromSnsPayload=*/ false);


  const spanAttributes = {


  [SemanticAttributes.MESSAGING_MESSAGE_ID]: msg.MessageId,


  [SemanticAttributes.MESSAGING_URL]: queueUrl,


  [SemanticAttributes.MESSAGING_SYSTEM]: "aws.sqs",


  [SemanticAttributes.MESSAGING_OPERATION]: MessagingOperationValues.PROCESS,


  };


  const span = tracer.startSpan("received message", { kind: SpanKind.CONSUMER, attributes: spanAttributes }, ctx);


  // ... Здесь располагается ваша логика обработки...


  span.end();


  const deleteParams = {


  QueueUrl: queueUrl,


  ReceiptHandle: msg.ReceiptHandle


  };


  sqs.deleteMessage(deleteParams, function (err, data) {


  if (err) {


  console.log("Delete Error", err);


  } else {


  console.log("Message Deleted", data);


  }


  });


  });


  }


  resolve();


  });


  });


  };


  function extractParent(msg, fromSnsPayload=false) {


  let valueKey = "StringValue"


  if (fromSnsPayload) {


  valueKey = "Value";


  try {


  msg = JSON.parse(msg.Body)


  } catch {


  msg = {}


  }


  }


  const carrier = {};


  Object.keys(msg.MessageAttributes || {}).forEach((attrKey) => {


  carrier[attrKey] = msg.MessageAttributes[attrKey]?.[valueKey];


  });


  return propagation.extract(ROOT_CONTEXT, carrier)


  };
  ```

  В приведённом выше примере `aws-sdk` используется для подписки и получения сообщений из очереди SQS. Для каждого входящего сообщения родительский спан извлекается из атрибутов сообщения, и создаётся новый спан `received message` с извлечённым родителем. Если ваша очередь SQS подписана на топик SNS, приведённый выше пример может потребовать адаптации. Подробнее см. [Трассировка SQS-сообщений, перенаправленных из топика SNS](#sns-to-sqs-node).

  Результирующая распределённая трассировка с двумя сообщениями, отправленными в очередь, выглядит следующим образом.

  ![Пример PurePath для вручную созданных спанов получения SQS-сообщений](https://dt-cdn.net/images/sqs-manual-receiving-1727-9fcf0717f4.png)
* Топика SNS

  Для SNS-сообщений, перенаправленных в SQS, формат сообщения зависит от конфигурации [доставки необработанных сообщений](https://docs.aws.amazon.com/sns/latest/dg/sns-large-payload-raw-message-delivery.html) на подписке SNS.

Lambda-функции AWS, запускаемые SNS, поддерживаются из коробки при мониторинге с помощью расширения Dynatrace AWS Lambda.

SNS-топики можно настроить через подписку для перенаправления сообщений в очередь SQS. Сообщения в очереди SQS затем могут быть обработаны Lambda-функцией. Трассировка полученных сообщений в Lambda-функции, запущенной SQS, работает из коробки при мониторинге AWS Lambda с помощью расширения Dynatrace AWS Lambda. Однако трейсер может выбрать только одного родителя, и если ваша Lambda-функция получает пакеты из нескольких сообщений, требуется специальная обработка для отслеживания каждого сообщения отдельно.

Подробнее см. [получение SQS-сообщения](#receive-sqs-node).

## Связанные темы

* [Совместимость с OpenTelemetry](../opentelemetry-interoperability.md "Включение и использование совместимости с OpenTelemetry в AWS Lambda.")
* [Трассировка Python, Node.js и Java Lambda-функций](../aws-lambda-extension.md "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")
