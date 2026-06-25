---
title: Совместимость с OpenTelemetry в Python
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-python
scraped: 2026-05-12T12:15:14.790590
---

# Совместимость с OpenTelemetry в Python

# Совместимость с OpenTelemetry в Python

* How-to guide
* 10-min read
* Updated on Apr 28, 2026

Совместимость с OpenTelemetry связывает [расширение Dynatrace AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Мониторинг функций Lambda, написанных на Python, Node.js и Java.") с инструментацией OpenTelemetry для Python, чтобы использовать пакеты инструментации и расширения. После этого можно отслеживать технологии вроде баз данных или фреймворков обмена сообщениями, которые расширение Dynatrace AWS Lambda не поддерживает «из коробки».

## Перед началом

* Убедитесь, что [совместимость с OpenTelemetry включена](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability#enable "Включение и использование совместимости с OpenTelemetry в AWS Lambda.").
* Проверьте, что установленная версия OpenTelemetry Python API совместима с расширением Dynatrace AWS Lambda. В таблицах ниже указаны совместимые версии:

  | Версия OneAgent | Максимальная версия OpenTelemetry API |
  | --- | --- |
  | 1.331+ | 1.39.x |
  | 1.329+ | 1.38.x |
  | 1.323+ | 1.36.x |
  | 1.321+ | 1.35.x |
  | 1.319+ | 1.34.x |
  | 1.315+ | 1.32.x |
  | 1.313+ | 1.31.x |
  | 1.311+ | 1.30.x |

## Использование инструментации OpenTelemetry для Python

OpenTelemetry для Python предоставляет несколько пакетов инструментации в своём [репозитории OpenTelemetry Python contributions](https://opentelemetry-python-contrib.readthedocs.io/).

Пример: инструментация пакета в Lambda-функции на Python через пакет инструментации

В примере кода ниже показано, как выполнить инструментацию запросов к [PostgreSQL](https://www.postgresql.org/) в Lambda-функции на Python с помощью пакета инструментации [aiopg](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/aiopg/aiopg.html).

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

Для инструментации [boto3](https://boto3.readthedocs.io), AWS SDK для Python, OpenTelemetry предоставляет пакет инструментации [botocore](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/botocore/botocore.html).

Пример: инструментация AWS SDK для Python для мониторинга базы данных DynamoDB

В примере кода ниже показано, как инструментацию `botocore` можно использовать для добавления observability к вызовам базы данных [DynamoDB](https://aws.amazon.com/dynamodb/) (Dynatrace версии 1.244+).

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

## Использование OpenTelemetry Python API

[OpenTelemetry Python](https://github.com/open-telemetry/opentelemetry-python) можно использовать в SDK-подобном подходе для трассировки дополнительных операций, которые не покрываются пакетом инструментации.

```
import json



from opentelemetry import trace



def lambda_handler(event, context):



tracer = trace.get_tracer(__name__)



with tracer.start_as_current_span("do work"):



# do work



with tracer.start_as_current_span("do some more work") as span:



span.set_attribute("foo", "bar")



# do some more work



return {



'statusCode': 200,



'body': json.dumps('Hello from Hello world from OpenTelemetry Python!')



}
```

## Трассировка сообщений AWS SQS и SNS в Python

OneAgent версии 1.253+ для SQS, OneAgent версии 1.257+ для SNS

Open-source пакеты инструментации позволяют трассировать сообщения AWS SQS и SNS и собирать их через расширение Dynatrace AWS Lambda.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Установите необходимые зависимости**](#dependencies-python)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Отправьте сообщение SQS/SNS**](#send-message-python)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Получите сообщение SQS/SNS**](#receive-message-python)

### Шаг 1. Установка необходимых зависимостей

SQS

SNS

```
pip install -U "opentelemetry-api>=1.12" "opentelemetry-instrumentation-boto3sqs>=0.34b0"
```

На данный момент [`opentelemetry-instrumentation-boto3sqs`](https://pypi.org/project/opentelemetry-instrumentation-boto3sqs/) представляет собой отдельный пакет от [`opentelemetry-instrumentation-botocore`](https://pypi.org/project/opentelemetry-instrumentation-botocore/). Последний инструментирует все вызовы AWS SDK, но не имеет расширенной поддержки SQS.

При установке зависимостей в Lambda-функцию или слой используйте опцию `-t`, чтобы указать целевую директорию, куда нужно скопировать установленные пакеты.

```
pip install -U "opentelemetry-instrumentation-botocore>=0.36b0"
```

### Шаг 2. Отправка сообщения SQS/SNS

Пакет [boto3](https://pypi.org/project/boto3/) доступен «из коробки», если код выполняется в AWS Lambda, но его также можно установить командой `pip install -U boto3`.

Код, определяющий функцию `lambda_handler`, можно использовать

* Внутри AWS Lambda (рекомендуется мониторить её нашим слоем AWS Lambda)
* Вне AWS Lambda (мониторинг выполняется через OpenTelemetry и экспортируется в Dynatrace по OTLP/HTTP ingest)

  Возможно, потребуется убрать параметры функции и возвращаемое значение.

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

### Шаг 3. Получение сообщения SQS/SNS

SQS

SNS

Трассировать SQS-сообщения можно, когда они приходят из

* **SQS-топика**

  Получение сообщений работает «из коробки» при использовании Lambda-функции с триггером SQS, мониторинг которой ведётся расширением Dynatrace AWS Lambda. Поскольку у span'а может быть только один родитель, при получении вашей Lambda-функцией батча из нескольких сообщений необходимо вручную создавать span'ы для обработки каждого сообщения, если требуется отслеживать их по отдельности и связывать с отправителем.

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

  Пример: получение сообщений с триггером AWS Lambda SQS

  Если вы развернули пример и вызвали отправителя, он будет автоматически запущен по SQS.

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



  # ... Here your actual processing would go...



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

  Вызванная Lambda-функция является дочерней по отношению к одному из сообщений, которыми она была запущена. Поскольку родитель может быть только один, остальные span'ы manual-triggerâprocess не связаны напрямую с тем вызовом Lambda, в котором они обрабатываются. Часто на батч сообщений приходится более одного узла вызовов Lambda. В этих случаях AWS распределяет батч по нескольким вызовам Lambda. Это может произойти, даже когда сообщения доставляются в пределах настроенного окна по времени и их число меньше настроенного размера батча.
* **SNS-топика**

  Для SNS-сообщений, пересылаемых в SQS, формат сообщения зависит от настройки [raw message delivery](https://docs.aws.amazon.com/sns/latest/dg/sns-large-payload-raw-message-delivery.html) у SNS-подписки.

  | Raw message delivery | Формат сообщения | Пример |
  | --- | --- | --- |
  | Включена | Атрибуты SNS-сообщения конвертируются в атрибуты SQS-сообщения, и родитель извлекается напрямую из `MessageAttributes` SQS-сообщения. | + [Вызов API получения SQS вручную](#manual-receive) + [Получение сообщений с триггером AWS Lambda SQS](#py-sqs-trigger). |
  | Отключена | SNS-сообщение и его `MessageAttributes` доставляются как сериализованная JSON-строка в теле полученного SQS-сообщения. Чтобы корректно связать span получения, родителя нужно извлечь из `MessageAttributes` сериализованного SNS-сообщения. | + [Вызов API получения SQS вручную](#manual-receive) + [Получение сообщений с триггером AWS Lambda SQS](#py-sqs-trigger).  Для обоих примеров требуется дополнительная настройка: при вызове метода `_extract_parent` установите значение параметра `from_sns_payload` в `True`. |

Lambda-функции AWS, запускаемые из SNS, поддерживаются «из коробки» при мониторинге через расширение Dynatrace AWS Lambda.

SNS-топики можно настроить через подписку на пересылку сообщений в очередь SQS. Затем сообщения из очереди SQS могут потребляться Lambda-функцией. Трассировка полученных сообщений в Lambda-функции AWS, запускаемой через SQS, работает «из коробки», когда AWS Lambda мониторится расширением Dynatrace AWS Lambda. Однако tracer может выбрать только одного родителя, и если ваша Lambda-функция получает батчи из нескольких сообщений, требуется специальная обработка для отдельного отслеживания каждого сообщения.

Подробнее см. [получение SQS-сообщения](#receive-sqs-python).

## Связанные темы

* [Совместимость с OpenTelemetry](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability "Включение и использование совместимости с OpenTelemetry в AWS Lambda.")
* [Трассировка Lambda-функций на Python, Node.js и Java](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Мониторинг функций Lambda, написанных на Python, Node.js и Java.")