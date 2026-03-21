---
title: Amazon CloudWatch Metric Streams
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/cloudwatch-metric-streams
scraped: 2026-03-06T21:33:53.919137
---

* 10 мин. чтения

Интеграция Dynatrace с Amazon CloudWatch Metric Streams предоставляет простой и безопасный способ приёма метрик AWS. Amazon CloudWatch Metric Streams позволяет передавать все метрики, выпущенные в заданном регионе AWS, через Firehose в Dynatrace API.

### Интеграция AWS по умолчанию и AWS Metric Streams

Различия между [интеграцией AWS по умолчанию](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md "Интеграция метрик из Amazon CloudWatch.") и AWS Metric Streams.

|  | Интеграция AWS по умолчанию | AWS Metric Streams |
| --- | --- | --- |
| ActiveGate | Требуется для нестандартных сервисов или отслеживаемых сред размером более 2000 экземпляров | Не требуется |
| Firehose | Не требуется | Требуется |
| Открытость тенанта Dynatrace для входящего HTTPS-трафика из Интернета | Не требуется | Требуется |
| Доступные метрики | Выбранные метрики Amazon CloudWatch | Все доступные метрики Amazon CloudWatch |
| Выбор метрик | В Dynatrace | В консоли Amazon CloudWatch |
| Область выбора метрик | Возможен выбор отслеживаемых метрик на уровне отдельной метрики и её статистик | Возможен выбор отслеживаемых метрик только на уровне всего пространства имён |
| Префикс ключа метрики | `ext:cloud.aws.<service>` [1](#fn-1-1-def) | `cloud.aws.<service>` |
| Атрибуты топологии (сущности Dynatrace) | Доступны | Доступны после включения расширения [AWS Entities for Metric Streaming](https://dt-url.net/x6038p6) |
| Теги (сущности Dynatrace) | Доступны | Недоступны |
| Предустановленные оповещения | Доступны | Недоступны |
| Предустановленные дашборды | Доступны | Доступны |
| Поддержка PrivateLink | Недоступна | Недоступна |

1

Префикс `ext:` используется метриками из [расширений OneAgent](../../../../../ingest-from/extensions/develop-your-extensions.md "Разработка собственных расширений в Dynatrace.") и [расширений ActiveGate](../../../../../ingest-from/extensions/develop-your-extensions.md "Разработка собственных расширений в Dynatrace."), а также [классическими метриками для интеграции AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md "Интеграция метрик из Amazon CloudWatch.").
Несмотря на схожесть именования, метрики интеграции AWS **не** основаны на расширениях.

## Предварительные требования

* Создайте [API-токен](../../../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.") в вашей среде Dynatrace и включите разрешение **Ingest metrics**.
* Определите API URL для вашей среды:

  + **Для Dynatrace SaaS**
    `https://<your_environment_ID>.live.dynatrace.com`
  + **Для Dynatrace Managed**
    `https://<your_domain>/e/<your_environment_ID>`
  + **Для ActiveGate**
    `https://<your_active_gate_IP_or_hostname>:9999/e/<your_environment_ID>`

Для определения `<your_environment_ID>` см. [идентификатор среды](../../../../../discover-dynatrace/get-started/monitoring-environment.md "Узнайте, как работать со средами мониторинга.").

Для получения метрик AWS выбранный ранее эндпоинт должен быть открыт для входящего интернет-трафика. Ограничительные межсетевые экраны могут блокировать сервис потоковой передачи.

## Настройка клиента Metric Streams

Вы можете настроить клиент Metric Streams с помощью шаблона CloudFormation или в консоли AWS. Инструкции приведены ниже.

Если вы используете Terraform или другое решение для настройки инфраструктуры, необходимо установить следующие общие атрибуты экземпляра Firehose:

```
name = "dt-url"


value = <your_API_URL>
```

```
name = "require-valid-certificate"


value = "true"
```

С помощью шаблона CloudFormation

В консоли AWS

CloudFormation позволяет развернуть клиент Metric Streams с помощью одной команды развёртывания для создания стека, объединяющего несколько ресурсов AWS. Этот подход быстрее и упрощает управление ресурсами AWS.

Для каждого региона, который вы хотите отслеживать, требуется один стек клиента. После развёртывания клиент начинает передавать все метрики, генерируемые в его регионе. Вы можете [ограничить передаваемые метрики](#restrict-metrics).

### Развёртывание клиента Metric Streams для региона по умолчанию

Чтобы получить шаблон CloudFormation и развернуть его в вашей учётной записи AWS, выполните приведённую ниже команду. Обязательно замените `<your_API_URL>` и `<your_API_token>` вашими значениями. Описание параметров приведено в таблице ниже.

Если у вас настроен AWS CLI, вы можете использовать Bash-совместимую оболочку. В противном случае можно использовать CloudShell, доступную в консоли AWS.

Параметры...

| Параметр | Описание | Значение по умолчанию |
| --- | --- | --- |
| `DYNATRACE_ENV_URL` | Обязательно. Ваш API URL. Инструкции см. в [Предварительных требованиях](#prerequisites). |  |
| `DYNATRACE_API_KEY` | Обязательно. Ваш API-токен. Инструкции см. в [Предварительных требованиях](#prerequisites). |  |
| `STACK_NAME` | Обязательно. Имя вашего стека клиента. | `dynatrace-aws-metric-streams-client` |
| `REQUIRE_VALID_CERTIFICATE` | Необязательно. Если установлено в `true`, Dynatrace проверяет SSL-сертификат URL вашей среды Dynatrace. | `true` |
| `DELIVERY_ENDPOINT` | Необязательно. Один из следующих эндпоинтов Metric Streams для Dynatrace: Глобальный: `https://aws.cloud.dynatrace.com/` США: `https://us.aws.cloud.dynatrace.com/` ЕС: `https://eu.aws.cloud.dynatrace.com/` | `https://aws.cloud.dynatrace.com/` |

```
DYNATRACE_ENV_URL=<your_API_URL>


DYNATRACE_API_KEY=<your_API_token>


STACK_NAME=dynatrace-aws-metric-streams-client


DELIVERY_ENDPOINT=https://aws.cloud.dynatrace.com/


REQUIRE_VALID_CERTIFICATE=true


wget -O dynatrace-aws-metric-streams-client.yaml  https://assets.cloud.dynatrace.com/awsmetricstreaming/dynatrace-aws-metric-streams-client.yaml && \


aws cloudformation deploy --capabilities CAPABILITY_NAMED_IAM --template-file ./dynatrace-aws-metric-streams-client.yaml --stack-name $STACK_NAME --parameter-overrides DynatraceEnvironmentUrl=$DYNATRACE_ENV_URL DynatraceApiKey=$DYNATRACE_API_KEY RequireValidCertificate=$REQUIRE_VALID_CERTIFICATE FirehoseHttpDeliveryEndpoint=$DELIVERY_ENDPOINT
```

### Развёртывание клиента Metric Streams для других регионов

Приведённая выше команда использует профиль AWS CLI по умолчанию и его регион по умолчанию. Чтобы изменить профиль и регион, вы можете экспортировать дополнительные переменные, такие как `AWS_DEFAULT_REGION` и `AWS_PROFILE`, и повторно выполнить команду развёртывания. Если вы используете CloudShell, вы можете изменить регион в консоли AWS. Подробнее о настройке AWS CLI см. [Переменные окружения для настройки AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html).

Мониторинг нескольких учётных записей AWS с помощью Cross-account cross-Region CloudWatch

Для мониторинга метрик из связанных учётных записей AWS с использованием одной интеграции AWS Metric Streams необходимо установить параметр `IncludeLinkedAccountsMetrics` в значение `true` в шаблоне CloudFormation.

### Проверка корректности развёртывания клиента Metric Streams (необязательно)

Чтобы убедиться, что клиент Metric Streams развёрнут корректно:

1. В консоли AWS перейдите в **CloudFormation**.
2. Выберите стек, созданный при развёртывании CloudFormation.
3. На вкладке **Events** убедитесь, что все события завершились успешно и нет неудачных событий.
4. На вкладке **Parameters** убедитесь, что все предоставленные параметры имеют правильные значения.

### Ограничение передаваемых метрик

Если вы хотите ограничить передаваемые метрики:

1. В консоли AWS перейдите в **CloudFormation**.
2. Выберите стек, созданный при развёртывании CloudFormation.
3. На вкладке **Resources** найдите ресурс с типом `AWS::CloudWatch::MetricStream` и запишите его Physical ID.
4. Перейдите в **CloudWatch**.
5. В разделе **Metrics** выберите **Streams**.
6. В списке потоков метрик выберите тот, имя которого соответствует Physical ID, записанному на шаге 3, затем выберите **Edit**.
7. В разделе **Metrics to be streamed** выберите один из следующих вариантов:

   * **All namespaces** — если вы хотите автоматически передавать все пространства имён (вы можете вручную выбрать пространства имён для исключения).
   * **Selected namespaces** — если вы хотите вручную выбрать пространства имён для передачи.
8. В разделе **Select metrics for the metric stream** выберите один из следующих вариантов:

   * **All metrics** — если вы хотите автоматически передавать все метрики из пространств имён, выбранных на шаге 7.
   * **Exclude metrics by metric name** — если вы хотите вручную исключить метрики для каждого пространства имён.
9. Выберите **Save changes**.

Если у вас нет доступа к шаблону CloudFormation, вы можете вручную настроить клиент Metric Streams в консоли AWS. Следуйте инструкциям ниже.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание потока Data Firehose**](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/cloudwatch-metric-streams.md#step-1 "Приём метрик из ваших учётных записей AWS с помощью Amazon CloudWatch Metric Streams.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создание CloudWatch Metric Stream**](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/cloudwatch-metric-streams.md#step-2 "Приём метрик из ваших учётных записей AWS с помощью Amazon CloudWatch Metric Streams.")

Для каждого региона, который вы хотите отслеживать, необходимо повторить всю процедуру: создать поток Data Firehose и создать CloudWatch Metric Stream.

### Шаг 1. Создание потока Data Firehose

1. В консоли AWS перейдите в **Kinesis**.
2. Выберите **Create delivery stream**.

#### Шаг 1. Подшаг 1. Выбор источника и назначения

1. В поле **Source** выберите **Direct PUT**.
2. В поле **Destination** выберите **Dynatrace**.

#### Шаг 1. Подшаг 2. Имя

1. Введите имя потока и сохраните его для дальнейшего использования.

#### Шаг 1. Подшаг 3. Преобразование записей

1. Убедитесь, что **Data Transformation** отключено.

#### Шаг 1. Подшаг 4. Настройки назначения

1. В поле **Ingestion type** выберите **Metrics**.
2. В поле **HTTP endpoint URL** выберите один из доступных эндпоинтов Dynatrace (Global, EU или US).
3. В поле **API token** введите ваш API-токен. Инструкции см. в [Предварительных требованиях](#prerequisites).
4. В поле **API URL** введите ваш API URL. Инструкции см. в [Предварительных требованиях](#prerequisites).
5. В поле **Content encoding** убедитесь, что выбран **GZIP**.
6. В поле **Retry duration** введите `900`.
7. В разделе **Buffer hints** установите **Buffer size** на 3 MiB и **Buffer interval** на 60 секунд.
8. В разделе **Backup settings** убедитесь, что выбрано **Failed data only**.
9. В поле **S3 backup bucket** выберите **Create**.
10. Введите имя, при необходимости выберите регион для S3-бакета, затем выберите **Create bucket**.

#### Шаг 1. Подшаг 5. Настройка параметров

1. Используйте существующие настройки по умолчанию.
2. Необязательно: в разделе **Tags** введите теги для организации ваших ресурсов AWS.
3. Выберите **Next**.

#### Шаг 1. Подшаг 6. Проверка

1. Проверьте вашу конфигурацию.
2. Выберите **Create delivery stream**.

### Шаг 2. Создание CloudWatch Metric Stream

1. В консоли AWS перейдите в **CloudWatch**.
2. В разделе **Metrics** выберите **Streams**.
3. Выберите **Create metric stream**.
4. Выберите **Custom setup with Firehose** и введите имя Firehose, созданного в предыдущем разделе (в поле **Select your Data Firehose stream**).
5. В разделе **Change output format** выберите **OpenTelemetry 1.0**.

OpenTelemetry 0.7

Мы рекомендуем использовать OpenTelemetry 1.0, так как это версия по умолчанию, которая позволяет получать новые метрики и полностью совместима с версией 0.7, которая по-прежнему будет поддерживаться.

6. В разделе **Metrics to be streamed** выберите один из следующих вариантов:

   * **All metrics** — если вы хотите автоматически передавать все метрики из пространств имён.
   * **Select metrics** — если вы хотите вручную исключить метрики для каждого пространства имён.
7. В поле **Custom metric stream name** введите имя для вашего потока метрик.
8. Выберите **Create metric stream**.

## Просмотр метрик с помощью предустановленных дашбордов

После развёртывания клиента Metric Streams вы можете использовать [предустановленные дашборды из GitHub-репозитория](https://dt-url.net/ev03qe5) в Dynatrace для визуализации принятых данных.

Предварительные требования

* Установите [Python 3](https://www.python.org/downloads/) (дополнительные библиотеки не требуются)
* Включите разрешения **Read configuration** и **Write configuration** для вашего [API-токена](../../../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.")

Для загрузки предустановленных дашбордов из GitHub:

1. Получите `upload_dashboards.py` из GitHub-репозитория.

```
curl -o upload_dashboards.py https://raw.githubusercontent.com/Dynatrace/snippets/master/product/dashboarding/upload_dashboards.py
```

2. Создайте каталог `dashboards` рядом с `upload_dashboards.py`.
3. Добавьте любое определение дашборда из GitHub в каталог `dashboards`.

   Каждое определение дашборда представляет собой отдельный JSON-файл, расположенный в папках [GitHub-репозитория](https://dt-url.net/ev03qe5).
4. Выполните приведённый ниже скрипт. Обязательно замените `<your_dynatrace_cluster_version>`, `<your_API_token>` и `<your_API_URL>` вашими значениями. Описание параметров приведено в таблице ниже.

Параметры...

| Параметр | Описание |
| --- | --- |
| `cluster-version` | Минорная версия вашего Dynatrace Cluster. Например, для версии `1.210.1.xxxxx` необходимо указать `210`. |
| `dynatrace-api-token` | Ваш API-токен. Инструкции см. в [Предварительных требованиях](#prerequisites). |
| `dynatrace-env-url` | Ваш API URL. Инструкции см. в [Предварительных требованиях](#prerequisites). |

```
python3 upload_dashboards.py --cluster-version <your_dynatrace_cluster_version> --dynatrace-api-token <your_API_token> --dynatrace-env-url <your_API_URL>
```

Пример команды

```
python3 upload_dashboards.py --cluster-version 206 --dynatrace-api-token 123456789 --dynatrace-env-url https://my-cluster.com/e/1755ddb2-7938-41a2-b6bd-096e0fdcd3e0
```

Пользовательские метрики

Если вы хотите принимать пользовательские метрики, не включённые в предустановленные дашборды, вернитесь к [таблице сравнения интеграции AWS по умолчанию и AWS Metric Streams](#default-vs-metric-streams) и проверьте **Префикс ключа метрики**.

## Удаление клиента Metric Streams

Если вы развернули клиент Metric Streams с помощью шаблона CloudFormation:

1. В консоли AWS перейдите в **CloudFormation**.
2. Выберите стек, созданный при развёртывании CloudFormation.
3. В разделе **Resources** найдите ресурс с типом `AWS::S3::Bucket`, выберите его ссылку и в консоли S3 удалите все объекты в этом бакете.
4. Вернитесь в CloudFormation и в **Stack information** выберите **Delete**.

Если вы развернули клиент Metric Streams через консоль AWS, удалите все созданные ресурсы (S3-бакет, поток доставки Firehose, поток метрик CloudWatch).

## Ограничения Metric Streams

Метрика не будет передана, если она старше двух часов. Вы можете определить возраст метрики, построив её график в консоли CloudWatch и проверив возраст последней отображённой точки данных.

Дополнительные ограничения см. на [странице устранения неполадок Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-troubleshoot.html).