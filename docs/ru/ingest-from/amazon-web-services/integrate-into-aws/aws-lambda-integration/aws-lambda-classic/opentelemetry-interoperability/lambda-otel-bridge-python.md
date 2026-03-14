---
title: Совместимость OpenTelemetry в Python
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-python
scraped: 2026-03-05T21:34:24.324026
---

# Совместимость с OpenTelemetry в Python

# Совместимость с OpenTelemetry в Python

* Classic
* Руководство
* Чтение: 10 мин
* Обновлено 19 февраля 2026 г.

Совместимость с OpenTelemetry связывает [расширение Dynatrace AWS Lambda](../aws-lambda-extension.md "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.") с инструментированием OpenTelemetry Python для использования пакетов инструментирования и расширений. Это позволяет отслеживать технологии, такие как базы данных или фреймворки обмена сообщениями, которые не поддерживаются расширением Dynatrace AWS Lambda из коробки.

## Перед началом

* Убедитесь, что [совместимость с OpenTelemetry включена](../opentelemetry-interoperability.md#enable "Включение и использование совместимости с OpenTelemetry в AWS Lambda.").
* Убедитесь, что установленная версия OpenTelemetry Python API совместима с расширением Dynatrace AWS Lambda. В следующих таблицах перечислены совместимые версии:

  | Версия OneAgent | Максимальная версия OpenTelemetry API |
  | --- | --- |
  | 1.331+ | 1.39.x |
  | 1.329+ | 1.38.x |
  | 1.323+ | 1.36.x |

### Более ранние версии

| Версия OneAgent | Максимальная версия OpenTelemetry API |
| --- | --- |
| 1.321+ | 1.35.x |
| 1.319+ | 1.34.x |
| 1.315+ | 1.32.x |
| 1.313+ | 1.31.x |
| 1.311+ | 1.30.x |
| 1.307+ | 1.29.x |
| 1.303+ | 1.27.x |
| 1.299+ | 1.26.x |
| 1.295+ | 1.25.x |
| 1.291+ | 1.24.x |
| 1.285+ | 1.22.x |
| 1.281+ | 1.21.x |
| 1.277+ | 1.20.x |
| 1.273+ | 1.19.x |
| 1.269+ | 1.18.x |
| 1.265+ | 1.17.x |
| 1.259+ | 1.15.x |
| 1.257+ | 1.14.x |
| 1.253+ | 1.13.x |
| 1.249+ | 1.12.x |
| 1.243+ | 1.11.x |
| 1.239+ | 1.9.x |
| 1.235+ | 1.8.x |
| 1.233+ | 1.7.x |

## Использование инструментирования OpenTelemetry Python

OpenTelemetry для Python предоставляет несколько пакетов инструментирования в [репозитории дополнений OpenTelemetry Python](https://opentelemetry-python-contrib.readthedocs.io/).

Пример: Инструментирование пакета в Python Lambda-функции через пакет инструментирования

Следующий пример кода показывает, как инструментировать запросы к [PostgreSQL](https://www.postgresql.org/) в Python Lambda-функции с помощью пакета инструментирования [aiopg](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/aiopg/aiopg.html).

```
import json



import aiopg



from opentelemetry.instrumentation.aiopg import AiopgInstrumentor



AiopgInstrumentor().instrument()



def lambda_handler(event, context):



return {



'statusCode': 200,



'body': json.dumps(execute_query())



}



def execute_query():



result = []



with aiopg.connect(database='my_db') as conn:



with conn.cursor() as cur:



cur.execute("SELECT 'hello db';")



for row in cur:



result.append(row)



return result
```

Для инструментирования [boto3](https://boto3.readthedocs.io), AWS SDK для Python, OpenTelemetry предоставляет пакет инструментирования [botocore](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/botocore/botocore.html).

Пример: Инструментирование AWS SDK для Python для мониторинга базы данных DynamoDB

Пример кода ниже показывает, как инструментирование `botocore` может быть использовано для добавления наблюдаемости вызовов к базе данных [DynamoDB](https://aws.amazon.com/dynamodb/) (Dynatrace версии 1.244+).

```
import boto3



import json



from opentelemetry.instrumentation.botocore import BotocoreInstrumentor



BotocoreInstrumentor().instrument()



dynamodb = boto3.resource('dynamodb')



table = dynamodb.Table('MyTable')



def lambda_handler(event, handler):



result = table.get_item(Key={'mykey': 42})



return {



"statusCode": 200,



"answer": json.dumps(result.get("Item"))



}
```

![Экран сервиса DynamoDB](https://dt-cdn.net/images/dynamodb-python-nodejs-954-c0c7c41ba8.png)

## Использование OpenTelemetry Python API

[OpenTelemetry Python](https://github.com/open-telemetry/opentelemetry-python) можно использовать в подходе, подобном SDK, для трассировки дополнительных операций, не охваченных пакетами инструментирования.

```
import json



from opentelemetry import trace



def lambda_handler(event, context):



tracer = trace.get_tracer(__name__)



with tracer.start_as_current_span("do work"):



# выполнение работы



with tracer.start_as_current_span("do some more work") as span:



span.set_attribute("foo", "bar")



# выполнение дополнительной работы



return {



'statusCode': 200,



'body': json.dumps('Hello from Hello world from OpenTelemetry Python!')



}
```

Эти спаны отображаются на вкладке **Code level**.

![OpenTelemetry lambda](https://dt-cdn.net/images/2021-08-26-17-01-15-1618-ffa40d6d97.png)

## Трассировка сообщений AWS SQS и SNS с Python

OneAgent версии 1.253+ для SQS, OneAgent версии 1.257+ для SNS

Вы можете использовать пакеты инструментирования с открытым исходным кодом для трассировки сообщений AWS SQS и SNS и сбора их через расширение Dynatrace AWS Lambda.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Установка необходимых зависимостей**](#dependencies-python)[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Отправка сообщения SQS/SNS**](#send-message-python)[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Получение сообщения SQS/SNS**](#receive-message-python)

### Шаг 1: Установка необходимых зависимостей

SQS

SNS

```
pip install -U "opentelemetry-api>=1.12" "opentelemetry-instrumentation-boto3sqs>=0.34b0"
```

На данный момент [`opentelemetry-instrumentation-boto3sqs`](https://pypi.org/project/opentelemetry-instrumentation-boto3sqs/) является отдельным пакетом от [`opentelemetry-instrumentation-botocore`](https://pypi.org/project/opentelemetry-instrumentation-botocore/). Последний инструментирует все вызовы AWS SDK, но не имеет расширенной поддержки SQS.

Если вы устанавливаете зависимости в Lambda-функцию или слой, вы можете использовать опцию `-t` для указания целевой директории, куда будут скопированы установленные пакеты.

```
pip install -U "opentelemetry-instrumentation-botocore>=0.36b0"
```

### Шаг 2: Отправка сообщения SQS/SNS

Пакет [boto3](https://pypi.org/project/boto3/) доступен из коробки, если код выполняется в AWS Lambda, но вы также можете установить его с помощью `pip install -U boto3`.

Этот код, определяющий функцию `lambda_handler`, можно использовать

* Внутри AWS Lambda (мы рекомендуем мониторинг с помощью нашего слоя AWS Lambda)
* Вне AWS Lambda (мониторинг выполняется с помощью OpenTelemetry и экспортируется в Dynatrace через OTLP/HTTP ingest)

  Вы можете удалить параметры функции и возвращаемое значение.

SQS

SNS

```
from opentelemetry.instrumentation.boto3sqs import Boto3SQSInstrumentor



Boto3SQSInstrumentor().instrument()



import json



import boto3



from datetime import datetime



QUEUE_URL = "<Your SQS Queue URL>"



sqs = boto3.client("sqs")



def lambda_handler(event, context):



sent = []



for i in range(5):



res = sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=f"hello #{i} at {datetime.now()}")



sent.append(res["MessageId"])



return {



"statusCode": 200,



"body": json.dumps({"produced_messages": sent})



}
```

```
from opentelemetry.instrumentation.botocore import BotocoreInstrumentor



BotocoreInstrumentor().instrument()



import json



import boto3



from datetime import datetime



TOPIC_ARN = "<Your SNS topic ARN>"



sns = boto3.client("sns")



def lambda_handler(event, context):



res = sns.publish(TopicArn=TOPIC_ARN, Message=f"hello at {datetime.now()}")



return {



"statusCode": 200,



"body": json.dumps({"produced_message": res["MessageId"]})



}
```

### Шаг 3: Получение сообщения SQS/SNS

SQS

SNS

Вы можете трассировать сообщения SQS, перенаправленные из

* **Топика SQS**

  Получение сообщений работает из коробки при использовании AWS Lambda с триггером SQS, отслеживаемым расширением Dynatrace AWS Lambda. Поскольку спан может иметь только одного родителя, если ваша Lambda-функция получает пакет из нескольких сообщений, необходимо вручную создать спаны для обработки каждого отдельного сообщения, если вы хотите отслеживать их раздельно и связать с отправителем.

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

  Пример: Получение сообщений с триггером AWS Lambda SQS

  Если вы вызовете отправителя и развернули пример, он будет вызван автоматически SQS.

  ```
  from pprint import pformat



  import boto3



  import json



  from opentelemetry import trace, propagate



  from opentelemetry.semconv.trace import SpanAttributes, MessagingOperationValues



  tracer = trace.get_tracer("lambda-sqs-triggered")



  def lambda_handler(event, context):



  recvcount = 0



  print("Trigger", pformat(event))



  messages = event.get("Records") or ()



  # Lambda SQS event uses lowerCamelCase in its attribute names



  for msg in messages:



  recvcount += 1



  print("Processing", msg["messageId"])



  parent = _extract_parent(msg, from_sns_payload=False)



  with tracer.start_as_current_span("manual-trigger-process", context=parent, kind=trace.SpanKind.CONSUMER, attributes={



  SpanAttributes.MESSAGING_MESSAGE_ID : msg["messageId"],



  SpanAttributes.MESSAGING_URL : msg["eventSourceARN"],



  SpanAttributes.MESSAGING_SYSTEM : msg["eventSource"],



  SpanAttributes.MESSAGING_OPERATION : MessagingOperationValues.PROCESS.value,



  }):



  # ... Здесь располагается ваша логика обработки...



  pass



  print("Processed", recvcount, "messages")



  def _extract_parent(msg, from_sns_payload=False):



  if from_sns_payload:



  try:



  body = json.loads(msg.get("body", "{}"))



  except json.JSONDecodeError:



  body = {}



  carrier = {key: value["Value"] for key, value in body.get("MessageAttributes", {}).items() if "Value" in value}



  else:



  carrier = {key: value["stringValue"] for key, value in msg.get("messageAttributes", {}).items() if "stringValue" in value}



  return propagate.extract(carrier)
  ```

  Результирующий путь выглядит следующим образом:

  ![Подробное представление распределённой трассировки, показывающее отправленные сообщения AWS SQS, которые запускают Lambda, где они обрабатываются.](https://dt-cdn.net/images/triggered-invoke-1636-a740dc26ec.png)

  Вызванная Lambda-функция является дочерним элементом одного из сообщений, которыми она была запущена. Поскольку может быть только один родитель, другие спаны manual-trigger-process не связаны напрямую с вызовом Lambda, в котором они обрабатываются. Часто для пакета сообщений существует более одного узла вызова Lambda. В таких случаях AWS распределил пакет по нескольким вызовам Lambda. Это может произойти, даже если сообщения доставлены в пределах настроенного окна пакетной обработки и их количество меньше настроенного размера пакета.

  Пример: Вызов API SQS receive вручную

  Если вы развернули пример, использующий API `receive` в коде, вам нужно вызвать его вручную, и он попытается прочитать все сообщения из очереди.

  Этот пример использует инструментирование boto3sqs. Если вы не хотите его использовать, необходимо раскомментировать аргумент `MessageAttributeNames` в функции `receive_message`, иначе SQS опустит данные, необходимые для связи сообщения с отправителем, из полученных данных.

  Этот код также можно использовать вне Lambda-функции и [отслеживать с помощью OpenTelemetry](../../../../../opentelemetry/walkthroughs/python.md "Узнайте, как инструментировать ваше Python-приложение с помощью OpenTelemetry и Dynatrace.") без расширения Dynatrace AWS Lambda.

  ```
  from opentelemetry.instrumentation.boto3sqs import Boto3SQSInstrumentor



  Boto3SQSInstrumentor().instrument()



  from pprint import pformat



  import boto3



  import json



  from opentelemetry import trace, propagate



  from opentelemetry.semconv.trace import SpanAttributes, MessagingOperationValues



  QUEUE_URL = '<Your SQS Queue URL>'



  sqs = boto3.client("sqs")



  tracer = trace.get_tracer("lambda-receive-function")



  def lambda_handler(event, context):



  recvcount = 0



  while True:



  msg_receive_result = sqs.receive_message(



  MaxNumberOfMessages=10,



  QueueUrl=QUEUE_URL,



  WaitTimeSeconds=1, # WaitTime of zero would use sampled receive, may return empty even if there is a message



  # This argument is only required if you do not use the boto3sqs instrumentation:



  #MessageAttributeNames=list(propagate.get_global_textmap().fields)



  )



  print("Received", pformat(msg_receive_result))



  if not msg_receive_result.get('Messages'):



  break



  messages = msg_receive_result.get("Messages")



  # receive result uses PascalCase in its attribute names



  for msg in messages:



  recvcount += 1



  print("Processing", msg["MessageId"])



  parent = _extract_parent(msg, from_sns_payload=False)



  with tracer.start_as_current_span("manual-receive-process", context=parent, kind=trace.SpanKind.CONSUMER, attributes={



  SpanAttributes.MESSAGING_MESSAGE_ID: msg["MessageId"],



  SpanAttributes.MESSAGING_URL: QUEUE_URL,



  SpanAttributes.MESSAGING_SYSTEM: "aws.sqs",



  SpanAttributes.MESSAGING_OPERATION: MessagingOperationValues.PROCESS.value,



  }):



  # ... Здесь располагается ваша логика обработки...



  print("Delete result", sqs.delete_message(



  QueueUrl=QUEUE_URL,



  ReceiptHandle=msg['ReceiptHandle'],



  ))



  print("Processed", recvcount, "messages")



  def _extract_parent(msg, from_sns_payload=False):



  if from_sns_payload:



  try:



  body = json.loads(msg.get("Body", "{}"))



  except json.JSONDecodeError:



  body = {}



  carrier = {key: value["Value"] for key, value in body.get("MessageAttributes", {}).items() if "Value" in value}



  else:



  carrier = {key: value["StringValue"] for key, value in msg.get("MessageAttributes", {}).items() if "StringValue" in value}



  return propagate.extract(carrier)
  ```

  Ручное создание спана `manual-receive-process` необходимо, поскольку инструментирование boto3sqs не устанавливает отправителя в качестве родителя для спана обработки, а использует [ссылки OpenTelemetry](https://opentelemetry.io/docs/concepts/signals/traces/#span-links), которые в настоящее время не поддерживаются Dynatrace. Для корректной работы связи спана `manual-receive-process` необходимо настроить расширение Dynatrace AWS Lambda для ручной установки родительских спанов. См. [предыдущий пример](#py-sqs-trigger) для руководства.

  Вызов сначала кода, отправляющего SQS-сообщения, а затем кода ручного получения, развёрнутых как Lambda-функции, приводит к двум трассировкам:

  + Первая трассировка показывает путь сообщения от отправителя к обработчику:

    ![Подробное представление распределённой трассировки, показывающее отправленные и обработанные сообщения AWS SQS в другом процессе.](https://dt-cdn.net/images/sdk-send-process-1643-dc267e8011.png)

    Присутствуют дополнительные узлы `Requests to public networks`, поскольку пакет boto3 использует HTTP-запросы для отправки SQS-сообщений, которые перехватываются HTTP-инструментированием Dynatrace.

    Вы заметите, что узлы вызова и получения второго вызова Lambda отсутствуют в этой трассировке, хотя узлы `manual-receive-process` присутствуют. Это связано с тем, что Lambda-функция была запущена независимо от потока сообщений и просто получила сообщение в рамках своего кода обработчика.
  + Вторая трассировка в Dynatrace показывает вызов Lambda до того, как он разделяется на две части установкой явного родителя:

    ![Подробное представление распределённой трассировки, показывающее полученные сообщения AWS SQS с помощью Python boto3 SDK.](https://dt-cdn.net/images/sdk-receive-1637-72b227938f.png)
* **Топика SNS**

  Для SNS-сообщений, перенаправленных в SQS, формат сообщения зависит от конфигурации [доставки необработанных сообщений](https://docs.aws.amazon.com/sns/latest/dg/sns-large-payload-raw-message-delivery.html) на подписке SNS.

Lambda-функции AWS, запускаемые SNS, поддерживаются из коробки при мониторинге с помощью расширения Dynatrace AWS Lambda.

SNS-топики можно настроить через подписку для перенаправления сообщений в очередь SQS. Сообщения в очереди SQS затем могут быть обработаны Lambda-функцией. Трассировка полученных сообщений в Lambda-функции, запущенной SQS, работает из коробки при мониторинге AWS Lambda с помощью расширения Dynatrace AWS Lambda. Однако трейсер может выбрать только одного родителя, и если ваша Lambda-функция получает пакеты из нескольких сообщений, требуется специальная обработка для отслеживания каждого сообщения отдельно.

Подробнее см. [получение SQS-сообщения](#receive-sqs-python).

## Связанные темы

* [Совместимость с OpenTelemetry](../opentelemetry-interoperability.md "Включение и использование совместимости с OpenTelemetry в AWS Lambda.")
* [Трассировка Python, Node.js и Java Lambda-функций](../aws-lambda-extension.md "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")
