---
title: Мониторинг журналов с помощью AWS log forwarder
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder
scraped: 2026-03-06T21:32:20.716773
---

# Мониторинг журналов с помощью AWS log forwarder

# Мониторинг журналов с помощью AWS log forwarder

* Classic
* Практическое руководство
* 13 минут чтения
* Обновлено 08 мая 2024 г.
* Устарело

Прекращение поддержки AWS log forwarder

Dynatrace AWS log forwarder теперь устарел в пользу нового решения [Потоковая передача журналов через Amazon Data Firehose](lma-stream-logs-with-firehose.md "Интеграция Amazon Data Firehose позволяет принимать облачные журналы напрямую, без дополнительной инфраструктуры и с более высокой пропускной способностью."), которое позволяет получать облачные журналы напрямую без какой-либо дополнительной инфраструктуры и с увеличенной пропускной способностью. Чтобы ознакомиться с доступными альтернативными интеграциями, см. [Настройка Dynatrace на Amazon Web Services](../../../amazon-web-services.md "Настройка и конфигурация мониторинга для Amazon Web Services.").

Прекращение поддержки Dynatrace AWS log forwarder запланировано на 31 декабря 2024 г.

Потребление DDU для мониторинга журналов

Тарификация DDU применяется к облачному мониторингу журналов. Подробности см. в разделе [DDU для мониторинга журналов](../../../../license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption.md "Понять, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.").

Перенаправление журналов AWS позволяет передавать журналы из Amazon CloudWatch в журналы Dynatrace через ActiveGate.

## Необходимые ресурсы

Для включения перенаправления журналов AWS необходимо развернуть специализированный стек CloudFormation в вашей учётной записи AWS. Стек состоит из экземпляра Kinesis Firehose и функции Lambda. Эти ресурсы влекут за собой расходы AWS согласно стандартной политике тарификации AWS. То же относится к включённым ресурсам самомониторинга (дашборды и метрики CloudWatch).

**Поддерживаемые сервисы**

| Название сервиса | Перенаправление журналов CloudWatch | Обогащение журналов | Привязка к сущностям |
| --- | --- | --- | --- |
| AWS Lambda | Применяется | Применяется | Применяется |
| AWS App Runner | Применяется | Применяется | Применяется |
| AWS CloudTrail [1](#fn-1-1-def) | Применяется | Применяется | - |
| Amazon API Gateway | Применяется | Применяется | - |
| Amazon SNS | Применяется | Применяется | Применяется |
| Amazon RDS | Применяется | Применяется | Применяется |
| Все сервисы, записывающие в CloudWatch | Применяется | Применяется | - |

1

Имя группы журналов AWS CloudTrail выбирается пользователем. Для обогащения журналов имя группы журналов должно начинаться с `aws-cloudtrail-logs`.

## Ограничения

AWS log forwarder поддерживает максимум 1 ГБ обработки данных в час при стандартной конфигурации.

* Для измерения пропускной способности ищите следующие метрики Kinesis в CloudWatch или проверяйте дашборды, предоставляемые развёрнутым стеком: `Delivery - log entries` и `Delivery - data volume`.
* Для измерения задержки ищите `Kinesis - record age`.

Рекомендации по масштабированию см. в [руководстве по масштабированию](#scalingguide) ниже.

## Предварительные требования

Если вы используете более раннюю версию Dynatrace, см. раздел [Альтернативные развёртывания](#alternative) для получения инструкций.

### Dynatrace

* [Включите приём общих журналов](../../../../analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api.md "Узнайте, как Dynatrace принимает данные журналов и каковы возможные ограничения такого приёма.")
* [Создайте токен API](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Узнайте о концепции токена доступа и его областях действия.") с разрешением **Ingest logs** (API v2)

### CLI

* Развёртывание можно запустить из AWS CloudShell или с любого компьютера с установленным AWS CLI, поддерживающего выполнение Bash-скриптов.

Скрипт развёртывания использует конфигурацию профиля AWS CLI по умолчанию. Профиль определяет учётную запись и регион AWS. Чтобы изменить учётную запись или регион:

* Используйте другой профиль — в этом случае необходимо [обновить файл конфигурации](https://dt-url.net/le03r5f).
* Временно перезапишите профиль по умолчанию (этот вариант ограничен текущей сессией командной оболочки) с помощью [переменных окружения](https://dt-url.net/3823r6v).

### Политика разрешений

Для выполнения скрипта развёртывания необходимы следующие разрешения:

Политика разрешений для развёртывания

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

1. Задайте следующие переменные окружения, заменив заполнители (`<...>`) своими значениями.

   * Для `TARGET_URL` введите URL вашей среды: `https://<your_environment_ID>.live.dynatrace.com`. Чтобы узнать, как определить идентификатор вашей среды для развёртывания SaaS или Managed, см. [идентификатор среды](../../../../discover-dynatrace/get-started/monitoring-environment.md "Понимание и работа со средами мониторинга.").
   * Для `TARGET_API_TOKEN` введите ваш токен API. Инструкции см. в разделе [Предварительные требования](#dynatrace).
   * Необязательно Для `STACK_NAME` значение по умолчанию — `dynatrace-aws-logs`. Чтобы задать другое имя для стека CloudFormation, в котором вы хотите развернуть ресурсы, замените значение по умолчанию своим.

   ```
   TARGET_URL=<your_environment_URL>



   TARGET_API_TOKEN=<your_API_token>



   STACK_NAME=dynatrace-aws-logs
   ```
2. Загрузите скрипт и разверните инфраструктуру.

   ```
   wget -O dynatrace-aws-log-forwarder.zip https://github.com/dynatrace-oss/dynatrace-aws-log-forwarder/releases/latest/download/dynatrace-aws-log-forwarder.zip \



   && unzip -qo dynatrace-aws-log-forwarder.zip \



   && ./dynatrace-aws-logs.sh deploy --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --stack-name $STACK_NAME --require-valid-certificate true
   ```

## Подписка на группы журналов

После развёртывания инфраструктуры необходимо подписаться на группы журналов, журналы которых вы хотите пересылать в Dynatrace.

Для подписки на группы журналов воспользуйтесь одним из описанных ниже способов.

Используйте параметр `[--stack-name <your_stack_name>]` в случае, если вы изменили значение по умолчанию во время развёртывания.

### Подписка путём перечисления имён групп журналов

**Рекомендация по использованию:** Используйте этот вариант, если количество групп журналов, на которые вы хотите подписаться, невелико.

**Для подписки:** Выполните команду ниже, заменив `<your_log_group_list>` списком имён групп журналов, разделённых пробелами, на которые вы хотите подписаться.

**Пример списка:** `/aws/lambda/my-lambda /aws/apigateway/my-api`

```
./dynatrace-aws-logs.sh subscribe --log-groups <your_log_group_list>
```

### Подписка путём чтения групп журналов из файла

**Рекомендация по использованию:** Используйте этот вариант, если количество групп журналов, на которые вы хотите подписаться, велико.

1. Создайте файл и введите каждое имя группы журналов на отдельной строке.
2. Сохраните файл.
3. Выполните команду ниже, заменив `<your_file_name>` фактическим именем файла.

   ```
   ./dynatrace-aws-logs.sh subscribe --log-groups-from-file <your_file_name>
   ```

Автообнаружение групп журналов

Для упрощения создания файла можно воспользоваться командой автообнаружения ниже, чтобы получить список имён всех групп журналов в вашей учётной записи. Перед подпиской список можно скорректировать вручную.

Обязательно замените `<your_log_groups_file>` именем файла, в который вы хотите перенаправить вывод.

```
./dynatrace-aws-logs.sh discover-log-groups > <your_log_groups_file>
```

### Подписка с фильтром шаблона подписки

**Рекомендация по использованию:** По умолчанию вы подписываетесь на все журналы в группе журналов. Используйте этот вариант, если хотите ограничить журналы, на которые вы подписываетесь. Подробности о синтаксисе шаблонов см. в [синтаксисе фильтров и шаблонов](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

**Ограничение:** На каждую группу журналов можно использовать только два фильтра подписки, поэтому возможность создания нескольких фильтров с разными шаблонами ограничена. Если вы создадите фильтр подписки, превышающий лимит, произойдёт ошибка AWS `LimitExceededException`.

**Для подписки:** Выполните команду ниже, заменив `<your_log_group_list>` и `<your_filter_pattern>` своими значениями.

```
./dynatrace-aws-logs.sh subscribe --log-groups <your_log_group_list> --filter-pattern <your_filter_pattern>
```

Использование и параметры подписки

Дополнительные параметры подписки см. в командах ниже.

При замене заполнителей (`<...>`) своими значениями обращайтесь к [таблице подписки](#subscription).

```
dynatrace-aws-logs.sh subscribe {--log-groups <your_log_group_list> | --log-groups-from-file <your_file_name>}



[--stack-name <your_stack_name>] [--filter-pattern <your_filter_pattern>] [--role-arn ROLE_ARN] [--firehose-arn FIREHOSE_ARN]
```

### Таблица подписки

| Параметр командной строки | Переменная окружения | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `--log-groups` | `LOG_GROUPS_LIST` | Список имён групп журналов, разделённых пробелами, на которые вы хотите подписаться. Например: `/aws/lambda/my-lambda /aws/apigateway/my-api`. |  |
| `--log-groups-from-file` | `LOG_GROUPS_FILE` | Файл со списком групп журналов, на которые вы хотите подписаться. Файл должен содержать каждое имя группы журналов на отдельной строке. |  |
| `--filter-pattern` | `FILTER_PATTERN` | Если задан, позволяет подписаться на отфильтрованный поток журналов. | Вы подписываетесь на все журналы в группе журналов. |
| `--stack-name` | `STACK_NAME` | Имя стека CloudFormation, в котором были развёрнуты ресурсы. | `dynatrace-aws-logs` |
| `--firehose-arn` | `FIREHOSE_ARN` | Укажите, в какой Amazon Data Firehose должны передаваться журналы, указав его ARN (Amazon Resource Name). **Рекомендация по использованию:** Задайте этот параметр, если у вас возникают проблемы с разрешениями или производительностью CloudFormation. | Будет извлечено из вывода стека CloudFormation, использованного на шаге развёртывания: либо значение по умолчанию `$DEFAULT_STACK_NAME`, либо значение, указанное с помощью параметра `--stack-name <your_stack_name>`. |
| `--role-arn` | `ROLE_ARN` | ARN роли IAM, которая предоставляет CloudWatch Logs разрешение на доставку принятых событий журнала в целевой поток. **Рекомендация по использованию:** Задайте этот параметр, если у вас возникают проблемы с разрешениями или производительностью CloudFormation. | Будет извлечено из вывода стека CloudFormation, использованного на шаге развёртывания: либо значение по умолчанию `$DEFAULT_STACK_NAME`, либо значение, указанное с помощью параметра `--stack-name <your_stack_name>`. |

## Отписка от групп журналов

Если вы больше не хотите пересылать журналы в Dynatrace, воспользуйтесь одним из двух способов ниже для отписки от групп журналов.

### Отписка путём перечисления имён групп журналов

Выполните команду ниже, заменив `<your_log_group_list>` списком имён групп журналов, разделённых пробелами, от которых вы хотите отписаться.

```
./dynatrace-aws-logs.sh unsubscribe --log-groups <your_log_group_list>
```

### Отписка путём чтения групп журналов из файла

Выполните команду ниже, заменив `<your_file_name>` именем файла, который вы создали для [подписки путём чтения групп журналов из файла](#from-file).

```
./dynatrace-aws-logs.sh unsubscribe --log-groups-from-file <your_file_name>
```

Использование и параметры отписки

Дополнительные параметры отписки см. в командах ниже.

При замене заполнителей (`<...>`) своими значениями обращайтесь к [таблице отписки](#unsubscribe-table).

```
dynatrace-aws-logs.sh unsubscribe {--log-groups <your_log_group_list> | --log-groups-from-file <your_file_name>} [--stack-name <your_stack_name>]
```

### Таблица отписки

| Параметр командной строки | Переменная окружения | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `--log-groups` | `LOG_GROUPS_LIST` | Список имён групп журналов, разделённых пробелами, от которых вы хотите отписаться. Например: `/aws/lambda/my-lambda /aws/apigateway/my-api`. |  |
| `--log-groups-from-file` | `LOG_GROUPS_FILE` | Файл со списком групп журналов, от которых вы хотите отписаться, с каждым именем группы журналов на отдельной строке. |  |
| `--stack-name` | `STACK_NAME` | Имя стека CloudFormation, в котором были развёрнуты ресурсы. | `dynatrace-aws-logs` |

## Обновление до новой версии

Чтобы заменить старый стек новой версией стека AWS log forwarder, разверните новый стек, используя те же параметры, что и раньше (особенно имя стека, если вы изменили его со значения по умолчанию).

## Альтернативные развёртывания

Если вы не хотите использовать прямой приём через Cluster API, необходимо использовать существующий ActiveGate версии 1.217+. ActiveGate должен быть общедоступен. Стек будет создан без выделенного ActiveGate, если вы выберете этот вариант.

Хотя Log Forwarder будет работать и без метрик самомониторинга, рекомендуется также принимать их в CloudWatch. Поэтому требуется доступ в интернет к конечным точкам AWS.

Инструкции см. ниже.

### Развёртывание с существующим ActiveGate

Предварительные требования

Dynatrace версии 1.217+

* [Требования Dynatrace](#dynatrace)
* [Требования CLI](#cli)
* Необходима следующая политика разрешений:

Политика разрешений для развёртывания с существующим ActiveGate

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

1. Задайте следующие переменные окружения, заменив заполнители (`<...>`) своими значениями.

   * Для `TARGET_URL` введите URL API вашей конечной точки ActiveGate: `https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`. Чтобы узнать, как определить идентификатор среды, см. [идентификатор среды](https://dt-url.net/ej43qge).
   * Для `TARGET_API_TOKEN` введите ваш токен API. Инструкции см. в разделе [Предварительные требования](#dynatrace).

   Если вы хотите, чтобы Dynatrace проверял SSL-сертификат URL вашей среды Dynatrace, установите для `REQUIRE_VALID_CERTIFICATE` значение `true`.

   ```
   TARGET_URL=<your_API_URL>



   TARGET_API_TOKEN=<your_API_token>



   REQUIRE_VALID_CERTIFICATE=false
   ```
2. Загрузите скрипт и разверните инфраструктуру.

   ```
   wget -O dynatrace-aws-log-forwarder.zip https://github.com/dynatrace-oss/dynatrace-aws-log-forwarder/releases/latest/download/dynatrace-aws-log-forwarder.zip \



   && unzip -qo dynatrace-aws-log-forwarder.zip \



   && ./dynatrace-aws-logs.sh deploy --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --require-valid-certificate $REQUIRE_VALID_CERTIFICATE
   ```

Использование и параметры развёртывания

Дополнительные параметры развёртывания см. в команде ниже.

```
dynatrace-aws-logs.sh deploy --target-url <your_API_URL> --target-api-token <your_API_token> [--require-valid-certificate {true|false}] [--stack-name <your_stack_name>] [--max-log-length <max_log_content_length>] [--tags <value> [<value>...] ]
```

Полный список параметров см. в таблице развёртывания ниже.

### Таблица развёртывания

| **Параметр командной строки** | **Переменная окружения** | **Описание** | **Значение по умолчанию** |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `--target-url` | `TARGET_URL` | Обязательно URL API целевого сервера приёма журналов вашей среды Dynatrace SaaS. Если вы используете существующий Environment ActiveGate, укажите конечную точку ActiveGate: `https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>` **Примечание:** Чтобы определить `<your_environment_ID>`, см. [идентификатор среды](../../../../discover-dynatrace/get-started/monitoring-environment.md "Понимание и работа со средами мониторинга."). |  |  |  |  |  |
| `--target-api-token` | `TARGET_API_TOKEN` | Обязательно Ваш токен API. Инструкции см. в разделе [Предварительные требования](#dynatrace). |  |  |  |  |  |
| `--require-valid-certificate` | `REQUIRE_VALID_CERTIFICATE` | Необязательно Если `true`, функция Lambda log forwarder проверяет SSL-сертификат URL вашей среды Dynatrace. | `false` |  |  |  |  |
| `--stack-name` | `STACK_NAME` | Необязательно Имя стека CloudFormation, в котором вы хотите развернуть ресурсы. | `dynatrace-aws-logs` |  |  |  |  |
| `--max-log-length` | `MAX_LOG_CONTENT_LENGTH` | Необязательно Максимальная длина содержимого журнала. Если журнал превышает эту длину, он будет усечён. Для значений выше 8192 также требуется изменение настроек Dynatrace — необходимо связаться с экспертом Dynatrace через чат в вашей среде. | `8192` |  |  |  |  |
| `--tags` | `TAGS` | Необязательно Список тегов для сопоставления с создаваемым или обновляемым стеком. Синтаксис: TagKey1=TagValue1 TagKey2=TagValue2 … |  |  |  |  |  |

## Проверка

Вы можете использовать описанные ниже методы проверки для устранения неудачного развёртывания.

### Проверка статуса развёртывания

Для проверки корректности развёртывания

1. В консоли AWS перейдите в CloudFormation.
2. Выберите стек log forwarder из списка слева по имени стека (значение по умолчанию — `dynatrace-aws-logs`).
3. Если в любом из полей ниже обнаружены проблемы или несоответствия, нажмите **Delete** для удаления стека, а затем повторите процесс развёртывания.

   * В **Stack info** проверьте статус стека; он должен быть `CREATE_COMPLETE`.
   * В **Parameters** убедитесь, что значения параметров соответствуют значениям, указанным при развёртывании.
   * В **Events** проверьте наличие событий с неудачным статусом.

### Проверка статуса подключения

Для проверки подключения AWS log forwarder и просмотра операционных журналов

1. В консоли AWS перейдите в CloudWatch Dashboards.
2. Найдите дашборд самомониторинга для перенаправления журналов AWS. Его имя будет иметь вид `DynatraceLogForwarder-SelfMonitoring-eu-north-1-dynatrace-aws-logs`, где средняя часть — регион AWS, а последняя часть — выбранное вами имя стека (по умолчанию `dynatrace-aws-logs`).
3. Проверьте дашборд на наличие очевидных проблем.
4. Перейдите в CloudFormation.
5. Выберите стек log forwarder из списка слева по имени стека (значение по умолчанию — `dynatrace-aws-logs`).
6. Выберите вкладку **Resources**, затем выберите ссылку рядом с `Lambda`.
7. На экране Lambda выберите вкладку **Monitor**, затем нажмите **Logs**.
8. Выберите один из перечисленных потоков журналов и проверьте журналы на наличие исключений.

## Руководство по масштабированию

Для увеличения пропускной способности по умолчанию рекомендуется увеличить объём памяти функции Lambda и количество подготовленных экземпляров для параллельного выполнения. Используемые значения зависят от фактической нагрузки. Ниже приведены максимальные проверенные и поддерживаемые значения.

| **Максимальная пропускная способность** | **Память Lambda** | **Количество экземпляров** |
| --- | --- | --- |
| до `15 МБ/мин` (1 ГБ/час) | `256 МБ` | `1` |
| до `500 МБ/мин` (30 ГБ/час) | `1024 МБ` | `5` |

В крайнем случае масштабируйте горизонтально: разверните несколько интеграций и подпишите каждую из них на разные группы журналов для распределения нагрузки.

## Удаление перенаправления журналов AWS

Для удаления перенаправления журналов AWS

1. Отпишитесь от всех групп журналов. Вы можете использовать метод автообнаружения групп журналов, описанный в разделе [Подписка путём чтения групп журналов из файла](#from-file), и передать файл вывода автообнаружения в команду отписки. Подробности см. в разделе [Отписка от групп журналов](#unsubscribe).
2. В консоли AWS перейдите к стеку CloudFormation.
3. Выберите вкладку **Resources** и перейдите к бакету S3 `DeliveryBucket`.
4. Удалите все объекты из бакета.
5. Вернитесь к стеку CloudFormation и нажмите **Delete**.
