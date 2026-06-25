---
title: Мониторинг логов через AWS log forwarder
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder
scraped: 2026-05-12T11:35:40.596484
---

# Мониторинг логов через AWS log forwarder

# Мониторинг логов через AWS log forwarder

* How-to guide
* 13-min read
* Updated on May 08, 2024
* Deprecated

Прекращение поддержки AWS log forwarder

Dynatrace AWS log forwarder теперь устарел в пользу нового решения [Потоковая передача логов через Amazon Data Firehose (Logs Classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Интеграция с Amazon Data Firehose позволяет принимать облачные логи напрямую, без дополнительной инфраструктуры и с более высокой пропускной способностью."), которое позволяет принимать облачные логи напрямую, без дополнительной инфраструктуры и с увеличенной пропускной способностью.

Прекращение поддержки Dynatrace AWS log forwarder запланировано на 31 декабря 2024 года.

Потребление DDU для Log Monitoring

К облачному Log Monitoring применяется тарификация DDU. Подробности см. в разделе [DDU для Log Monitoring](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.").

Пересылка логов AWS позволяет передавать логи из Amazon CloudWatch в логи Dynatrace через ActiveGate.

## Необходимые ресурсы

Чтобы включить пересылку логов AWS, в вашу учётную запись AWS требуется развернуть специальный CloudFormation-стек. Стек состоит из инстанса Kinesis Firehose и Lambda-функции. Эти ресурсы влекут затраты в AWS согласно стандартной тарификации AWS. То же относится к включённым в стек ресурсам самомониторинга (дашборды и метрики CloudWatch).

**Поддерживаемые сервисы**

| Имя сервиса | Пересылка логов CloudWatch | Обогащение логов | Связывание сущностей |
| --- | --- | --- | --- |
| AWS Lambda | Поддерживается | Поддерживается | Поддерживается |
| AWS App Runner | Поддерживается | Поддерживается | Поддерживается |
| AWS CloudTrail [1](#fn-1-1-def) | Поддерживается | Поддерживается | - |
| Amazon API Gateway | Поддерживается | Поддерживается | - |
| Amazon SNS | Поддерживается | Поддерживается | Поддерживается |
| Amazon RDS | Поддерживается | Поддерживается | Поддерживается |
| Все сервисы, пишущие в CloudWatch | Поддерживается | Поддерживается | - |

1

Имя лог-группы AWS CloudTrail выбирается пользователем. Для обогащения логов имя лог-группы должно начинаться с `aws-cloudtrail-logs`.

## Ограничения

В конфигурации по умолчанию AWS log forwarder обрабатывает не более 1 ГБ данных в час.

* Чтобы измерить пропускную способность, посмотрите следующие метрики Kinesis в CloudWatch или проверьте дашборды, предоставляемые развёрнутым стеком: `Delivery - log entries` и `Delivery - data volume`.
* Чтобы измерить задержку, посмотрите метрику `Kinesis - record age`.

Рекомендации по масштабированию см. в [руководстве ниже](#scalingguide).

## Предварительные требования

Если вы используете более раннюю версию Dynatrace, инструкции приведены в разделе [Альтернативные варианты развёртывания](#alternative).

### Dynatrace

* [Включите универсальный приём логов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace принимает данные логов и каковы потенциальные ограничения такого приёма.")
* [Создайте API-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Изучите концепцию токена доступа и его областей применения.") с правом **Ingest logs** (API v2)

### CLI

* Развёртывание можно запустить из AWS CloudShell или с любой машины с установленным AWS CLI, которая поддерживает выполнение Bash-скриптов.

Скрипт развёртывания использует конфигурацию профиля AWS CLI по умолчанию. Профиль определяет учётную запись и регион AWS. Чтобы сменить учётную запись или регион:

* Используйте другой профиль, в этом случае требуется [обновить ваш файл конфигурации](https://dt-url.net/le03r5f).
* Временно переопределите профиль по умолчанию (этот вариант ограничен рамками текущей shell-сессии) через [переменные окружения](https://dt-url.net/3823r6v).

### Политика прав доступа

Для запуска скрипта развёртывания требуются следующие права:

Политика прав для развёртывания

```
{



"Version": "2012-10-17",



"Statement": [



{



"Effect": "Allow",



"Action": [



"cloudformation:CreateChangeSet",



"cloudformation:ExecuteChangeSet",



"cloudformation:DescribeChangeSet",



"cloudformation:DescribeStackEvents",



"cloudformation:DescribeStacks",



"cloudformation:GetTemplateSummary",



"ec2:DescribeImages",



"s3:CreateBucket",



"s3:PutLifecycleConfiguration",



"s3:PutBucketPublicAccessBlock",



"iam:GetRole",



"iam:CreateRole",



"iam:AttachRolePolicy",



"iam:PutRolePolicy",



"iam:GetRolePolicy",



"iam:PassRole",



"lambda:CreateFunction",



"lambda:UpdateFunctionCode",



"lambda:GetFunction",



"lambda:GetFunctionCodeSigningConfig",



"cloudwatch:PutDashboard",



"cloudwatch:GetDashboard",



"firehose:DescribeDeliveryStream",



"firehose:CreateDeliveryStream",



"firehose:ListTagsForDeliveryStream",



"logs:DeleteSubscriptionFilter",



"logs:DescribeLogGroups",



"logs:PutSubscriptionFilter",



"ssm:GetParameters"



],



"Resource": "*"



}



]



}
```

## Развёртывание

1. Задайте следующие переменные окружения, заменив плейсхолдеры (`<...>`) на собственные значения.

   * Для `TARGET_URL` укажите URL вашей среды: `https://<your_environment_ID>.live.dynatrace.com`. Как определить ID среды для SaaS или Managed-развёртывания, см. в разделе [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Изучите и научитесь работать с мониторинговыми средами.").
   * Для `TARGET_API_TOKEN` укажите ваш API-токен. Инструкции см. в разделе [Предварительные требования](#dynatrace).
   * Опционально Для `STACK_NAME` значение по умолчанию: `dynatrace-aws-logs`. Чтобы задать другое имя CloudFormation-стека, в котором требуется развернуть ресурсы, замените значение по умолчанию на своё.

   ```
   TARGET_URL=<your_environment_URL>



   TARGET_API_TOKEN=<your_API_token>



   STACK_NAME=dynatrace-aws-logs
   ```
2. Скачайте скрипт и разверните инфраструктуру.

   ```
   wget -O dynatrace-aws-log-forwarder.zip https://github.com/dynatrace-oss/dynatrace-aws-log-forwarder/releases/latest/download/dynatrace-aws-log-forwarder.zip \



   && unzip -qo dynatrace-aws-log-forwarder.zip \



   && ./dynatrace-aws-logs.sh deploy --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --stack-name $STACK_NAME --require-valid-certificate true
   ```

## Подписка на лог-группы

После развёртывания инфраструктуры необходимо подписаться на лог-группы, логи которых вы хотите пересылать в Dynatrace.

Для подписки на лог-группы доступны варианты, описанные ниже.

Параметр `[--stack-name <your_stack_name>]` указывайте, если при развёртывании вы изменили значение по умолчанию.

### Подписка с указанием имён лог-групп

**Когда использовать:** этот вариант подходит, если количество лог-групп, на которые требуется подписаться, невелико.

**Чтобы подписаться:** выполните команду ниже, заменив `<your_log_group_list>` на разделённый пробелами список имён лог-групп, на которые требуется подписаться.

**Пример списка:** `/aws/lambda/my-lambda /aws/apigateway/my-api`

```
./dynatrace-aws-logs.sh subscribe --log-groups <your_log_group_list>
```

### Подписка через чтение лог-групп из файла

**Когда использовать:** этот вариант подходит, если количество лог-групп, на которые требуется подписаться, велико.

1. Создайте файл и впишите каждое имя лог-группы на отдельной строке.
2. Сохраните файл.
3. Выполните команду ниже, заменив `<your_file_name>` на фактическое имя файла.

   ```
   ./dynatrace-aws-logs.sh subscribe --log-groups-from-file <your_file_name>
   ```

Автообнаружение лог-групп

Чтобы упростить создание файла, можно воспользоваться командой автообнаружения ниже, которая выведет имена всех лог-групп в вашей учётной записи. Список можно вручную скорректировать перед подпиской.

Обязательно замените `<your_log_groups_file>` на имя файла, в который требуется перенаправить вывод.

```
./dynatrace-aws-logs.sh discover-log-groups > <your_log_groups_file>
```

### Подписка с шаблоном фильтра подписки

**Когда использовать:** по умолчанию подписка распространяется на все логи в лог-группе. Этот вариант используйте, если требуется ограничить набор логов, на которые вы подписываетесь. Подробности о синтаксисе шаблонов см. в [Filter and Pattern Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

**Ограничение:** на одну лог-группу допускается только два фильтра подписки, поэтому возможности создавать несколько фильтров с разными шаблонами ограничены. Если фильтр подписки превышает лимит, возникает исключение AWS `LimitExceededException`.

**Чтобы подписаться:** выполните команду ниже, заменив `<your_log_group_list>` и `<your_filter_pattern>` на собственные значения.

```
./dynatrace-aws-logs.sh subscribe --log-groups <your_log_group_list> --filter-pattern <your_filter_pattern>
```

Использование подписки и параметры

Дополнительные параметры подписки приведены в командах ниже.

При замене плейсхолдеров (`<...>`) на собственные значения для команд ниже сверяйтесь с [таблицей подписки](#subscription).

```
dynatrace-aws-logs.sh subscribe {--log-groups <your_log_group_list> | --log-groups-from-file <your_file_name>}



[--stack-name <your_stack_name>] [--filter-pattern <your_filter_pattern>] [--role-arn ROLE_ARN] [--firehose-arn FIREHOSE_ARN]
```

### Таблица подписки

| Параметр командной строки | Переменная окружения | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `--log-groups` | `LOG_GROUPS_LIST` | Разделённый пробелами список имён лог-групп, на которые требуется подписаться. Например: `/aws/lambda/my-lambda /aws/apigateway/my-api`. |  |
| `--log-groups-from-file` | `LOG_GROUPS_FILE` | Файл со списком лог-групп, на которые требуется подписаться. Каждое имя лог-группы должно быть на отдельной строке. |  |
| `--filter-pattern` | `FILTER_PATTERN` | Если задан, позволяет подписаться на отфильтрованный поток логов. | Подписка распространяется на все логи в лог-группе. |
| `--stack-name` | `STACK_NAME` | Имя CloudFormation-стека, в котором развёрнуты ресурсы. | `dynatrace-aws-logs` |
| `--firehose-arn` | `FIREHOSE_ARN` | Укажите, в какой Amazon Data Firehose должны передаваться логи, передав его ARN (Amazon Resource Name). **Когда использовать:** задайте этот параметр, если у вас возникают проблемы с правами доступа или производительностью при использовании CloudFormation. | Значение извлекается из вывода CloudFormation-стека, использованного на шаге развёртывания: либо значение по умолчанию `$DEFAULT_STACK_NAME`, либо имя, указанное через параметр `--stack-name <your_stack_name>`. |
| `--role-arn` | `ROLE_ARN` | ARN IAM-роли, которая разрешает CloudWatch Logs доставлять принимаемые события логов в целевой поток. **Когда использовать:** задайте этот параметр, если у вас возникают проблемы с правами доступа или производительностью при использовании CloudFormation. | Значение извлекается из вывода CloudFormation-стека, использованного на шаге развёртывания: либо значение по умолчанию `$DEFAULT_STACK_NAME`, либо имя, указанное через параметр `--stack-name <your_stack_name>`. |

## Отписка от лог-групп

Если вы больше не хотите пересылать логи в Dynatrace, для отписки от лог-групп используйте один из двух вариантов ниже.

### Отписка с указанием имён лог-групп

Выполните команду ниже, заменив `<your_log_group_list>` на разделённый пробелами список имён лог-групп, от которых требуется отписаться.

```
./dynatrace-aws-logs.sh unsubscribe --log-groups <your_log_group_list>
```

### Отписка через чтение лог-групп из файла

Выполните команду ниже, заменив `<your_file_name>` на имя файла, который вы создали для [подписки через чтение лог-групп из файла](#from-file).

```
./dynatrace-aws-logs.sh unsubscribe --log-groups-from-file <your_file_name>
```

Использование отписки и параметры

Дополнительные параметры отписки приведены в командах ниже.

При замене плейсхолдеров (`<...>`) на собственные значения для команд ниже сверяйтесь с [таблицей отписки](#unsubscribe-table).

```
dynatrace-aws-logs.sh unsubscribe {--log-groups <your_log_group_list> | --log-groups-from-file <your_file_name>} [--stack-name <your_stack_name>]
```

### Таблица отписки

| Параметр командной строки | Переменная окружения | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `--log-groups` | `LOG_GROUPS_LIST` | Разделённый пробелами список имён лог-групп, от которых требуется отписаться. Например: `/aws/lambda/my-lambda /aws/apigateway/my-api`. |  |
| `--log-groups-from-file` | `LOG_GROUPS_FILE` | Файл со списком лог-групп, от которых требуется отписаться. Каждое имя лог-группы должно быть на отдельной строке. |  |
| `--stack-name` | `STACK_NAME` | Имя CloudFormation-стека, в котором развёрнуты ресурсы. | `dynatrace-aws-logs` |

## Обновление до новой версии

Чтобы заменить старый стек на новую версию стека AWS log forwarder, разверните новый стек с теми же параметрами, которые вы использовали ранее (особенно имя стека, если оно было изменено относительно значения по умолчанию).

## Альтернативные варианты развёртывания

Если вы не хотите использовать прямой приём через Cluster API, потребуется существующий ActiveGate версии 1.217+. ActiveGate должен быть публично доступен. В этом случае стек будет создан без выделенного ActiveGate.

Хотя Log Forwarder продолжит работать и без метрик самомониторинга, рекомендуется также принимать их в CloudWatch. Поэтому требуется доступ к AWS-эндпоинтам через интернет.

Инструкции приведены ниже.

### Развёртывание с существующим ActiveGate

Предварительные требования

Dynatrace версии 1.217+

* [Требования к Dynatrace](#dynatrace)
* [Требования к CLI](#cli)
* Требуется следующая политика прав:

Политика прав для развёртывания с существующим ActiveGate

```
{



"Version": "2012-10-17",



"Statement": [



{



"Effect": "Allow",



"Action": [



"cloudformation:CreateChangeSet",



"cloudformation:ExecuteChangeSet",



"cloudformation:DescribeChangeSet",



"cloudformation:DescribeStackEvents",



"cloudformation:DescribeStacks",



"cloudformation:GetTemplateSummary",



"ec2:DescribeImages",



"s3:CreateBucket",



"s3:PutLifecycleConfiguration",



"s3:PutBucketPublicAccessBlock",



"iam:GetRole",



"iam:CreateRole",



"iam:AttachRolePolicy",



"iam:PutRolePolicy",



"iam:GetRolePolicy",



"iam:PassRole",



"lambda:CreateFunction",



"lambda:UpdateFunctionCode",



"lambda:GetFunction",



"lambda:GetFunctionCodeSigningConfig",



"cloudwatch:PutDashboard",



"cloudwatch:GetDashboard",



"firehose:DescribeDeliveryStream",



"firehose:CreateDeliveryStream",



"firehose:ListTagsForDeliveryStream",



"logs:DeleteSubscriptionFilter",



"logs:DescribeLogGroups",



"logs:PutSubscriptionFilter",



"ssm:GetParameters"



],



"Resource": "*"



}



]



}
```

1. Задайте следующие переменные окружения, заменив плейсхолдеры (`<...>`) на собственные значения, как указано ниже.

   * Для `TARGET_URL` укажите API URL эндпоинта вашего ActiveGate: `https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`. Как определить ID среды, см. в разделе [environment ID](https://dt-url.net/ej43qge).
   * Для `TARGET_API_TOKEN` укажите ваш API-токен. Инструкции см. в разделе [Предварительные требования](#dynatrace).

   Если требуется, чтобы Dynatrace проверял SSL-сертификат URL вашей среды Dynatrace, можно установить для `REQUIRE_VALID_CERTIFICATE` значение `true`.

   ```
   TARGET_URL=<your_API_URL>



   TARGET_API_TOKEN=<your_API_token>



   REQUIRE_VALID_CERTIFICATE=false
   ```
2. Скачайте скрипт и разверните инфраструктуру.

   ```
   wget -O dynatrace-aws-log-forwarder.zip https://github.com/dynatrace-oss/dynatrace-aws-log-forwarder/releases/latest/download/dynatrace-aws-log-forwarder.zip \



   && unzip -qo dynatrace-aws-log-forwarder.zip \



   && ./dynatrace-aws-logs.sh deploy --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --require-valid-certificate $REQUIRE_VALID_CERTIFICATE
   ```

Использование развёртывания и параметры

Дополнительные параметры развёртывания приведены в команде ниже.

```
dynatrace-aws-logs.sh deploy --target-url <your_API_URL> --target-api-token <your_API_token> [--require-valid-certificate {true|false}] [--stack-name <your_stack_name>] [--max-log-length <max_log_content_length>] [--tags <value> [<value>...] ]
```

Полный список параметров приведён в таблице развёртывания ниже.

### Таблица развёртывания

| **Параметр командной строки** | **Переменная окружения** | **Описание** | **Значение по умолчанию** |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `--target-url` | `TARGET_URL` | Обязательный API URL целевого приёмника логов вашей SaaS-среды Dynatrace. Если вы используете существующий environment ActiveGate, задайте URL эндпоинта вашего ActiveGate: `https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>` **Примечание:** Как определить `<your_environment_ID>`, см. в разделе [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Изучите и научитесь работать с мониторинговыми средами."). |  |  |  |  |  |
| `--target-api-token` | `TARGET_API_TOKEN` | Обязательный Ваш API-токен. Инструкции см. в разделе [Предварительные требования](#dynatrace). |  |  |  |  |  |
| `--require-valid-certificate` | `REQUIRE_VALID_CERTIFICATE` | Опциональный Если `true`, Lambda-функция log forwarder проверяет SSL-сертификат URL вашей среды Dynatrace. | `false` |  |  |  |  |
| `--stack-name` | `STACK_NAME` | Опциональный Имя CloudFormation-стека, в котором требуется развернуть ресурсы. | `dynatrace-aws-logs` |  |  |  |  |
| `--max-log-length` | `MAX_LOG_CONTENT_LENGTH` | Опциональный Максимальная длина содержимого лога. Если лог превышает эту длину, он будет обрезан. Для значений свыше 8192 также требуется изменение настроек в Dynatraceâобратитесь к продуктовому эксперту Dynatrace через live chat в вашей среде. | `8192` |  |  |  |  |
| `--tags` | `TAGS` | Опциональный Список тегов, которые требуется привязать к создаваемому или обновляемому стеку. Синтаксис: TagKey1=TagValue1 TagKey2=TagValue2 â¦ |  |  |  |  |  |

## Проверка

Чтобы устранить проблемы при неуспешном развёртывании, можно воспользоваться описанными ниже методами проверки.

### Проверка статуса развёртывания

Чтобы проверить корректность развёртывания

1. В консоли AWS перейдите в CloudFormation.
2. В списке слева выберите ваш стек log forwarder по имени стека (значение по умолчанию: `dynatrace-aws-logs`).
3. Если в каких-либо полях ниже обнаружены проблемы или расхождения, нажмите **Delete**, чтобы удалить стек, и затем повторите процесс развёртывания.

   * В **Stack info** проверьте статус стека: он должен быть `CREATE_COMPLETE`.
   * В **Parameters** проверьте, соответствуют ли значения параметров тем, что были указаны при развёртывании.
   * В **Events** поищите события со статусом ошибки.

### Проверка статуса подключения

Чтобы проверить подключение AWS log forwarder и просмотреть операционные логи

1. В консоли AWS перейдите в CloudWatch Dashboards.
2. Найдите дашборд самомониторинга для пересылки логов AWS. У него будет имя вида `DynatraceLogForwarder-SelfMonitoring-eu-north-1-dynatrace-aws-logs`, где средняя часть обозначает регион AWS, а последняя часть содержит имя выбранного вами стека (по умолчанию: `dynatrace-aws-logs`).
3. Просмотрите дашборд на наличие явных проблем.
4. Перейдите в CloudFormation.
5. В списке слева выберите ваш стек log forwarder по имени стека (значение по умолчанию: `dynatrace-aws-logs`).
6. Выберите вкладку **Resources** и затем перейдите по ссылке рядом с `Lambda`.
7. На экране Lambda выберите вкладку **Monitor** и затем **Logs**.
8. Выберите один из перечисленных лог-потоков и поищите исключения в логах.

## Руководство по масштабированию

Чтобы повысить пропускную способность относительно значения по умолчанию, рекомендуется увеличить память Lambda-функции и количество одновременно запускаемых инстансов. Подходящие значения зависят от фактической нагрузки. Ниже приведены максимальные протестированные и поддерживаемые значения.

| **Максимальная пропускная способность** | **Память Lambda** | **Количество инстансов** |
| --- | --- | --- |
| до `15 MB/minute` (1 GB/hour) | `256 MB` | `1` |
| до `500 MB/minute` (30 GB/hour) | `1024 MB` | `5` |

В крайнем случае выполните горизонтальное масштабирование: разверните больше интеграций и подпишите каждую на отдельный набор лог-групп, чтобы распределить нагрузку.

## Удаление AWS log forwarding

Чтобы удалить AWS log forwarding

1. Отпишитесь от всех лог-групп. Можно воспользоваться методом автообнаружения лог-групп, описанным в разделе [Подписка через чтение лог-групп из файла](#from-file), и передать файл с результатом автообнаружения команде отписки. Подробности см. в разделе [Отписка от лог-групп](#unsubscribe).
2. В консоли AWS перейдите к вашему CloudFormation-стеку.
3. Выберите вкладку **Resources** и перейдите к S3-бакету `DeliveryBucket`.
4. Удалите все объекты в бакете.
5. Вернитесь к CloudFormation-стеку и нажмите **Delete**.