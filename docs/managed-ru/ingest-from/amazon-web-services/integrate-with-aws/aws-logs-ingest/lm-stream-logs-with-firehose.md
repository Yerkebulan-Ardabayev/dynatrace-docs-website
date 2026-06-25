---
title: Потоковая передача логов через Amazon Data Firehose (Logs Classic)
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose
scraped: 2026-05-12T12:00:12.172240
---

# Потоковая передача логов через Amazon Data Firehose (Logs Classic)

# Потоковая передача логов через Amazon Data Firehose (Logs Classic)

* How-to guide
* 1-min read
* Published Mar 13, 2024

Log Monitoring Classic

Dynatrace Cluster версии 1.288

Интеграция Dynatrace с Amazon Data Firehose предоставляет простой и безопасный способ принимать логи AWS. Чтобы включить пересылку логов AWS, создайте инстанс Amazon Data Firehose и настройте его так, чтобы пунктом назначения была ваша среда Dynatrace. После этого можно подключить ваши лог-группы CloudWatch, создав фильтр подписки, либо отправлять логи напрямую в Data Firehose из сервисов, которые это поддерживают (например, Amazon Managed Streaming for Apache Kafka). Data Firehose и другие создаваемые облачные ресурсы влекут затраты в AWS согласно стандартной тарификации AWS.
См.
[страницу о пересылке облачных логов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding#aws-log-forwarding "Узнайте, как настроить пересылку логов AWS, Azure и Google Cloud для приёма логов."), чтобы узнать обо всех вариантах приёма логов AWS.

## Предварительные требования

Ноды вашего Dynatrace Managed Cluster должны быть открыты для входящего интернет-трафика (или хотя бы для трафика AWS) и настроены с действительным CA-подписанным SSL-сертификатом, чтобы принимать логи от Amazon Data Firehose.

1. Создайте [API-токен](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.") в вашей среде Dynatrace и включите разрешение Ingest logs.
2. Определите URL API для вашей среды:

   * **Для Dynatrace Managed** Рекомендуется
     `https://<your_domain>/e/<your_environment_ID>`

   * **Для ActiveGate** ([требуется дополнительная настройка](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose#environment-activegate-support "Интеграция с Amazon Data Firehose позволяет принимать облачные логи напрямую, без дополнительной инфраструктуры и с более высокой пропускной способностью."))
     `https://<your_active_gate_IP_or_hostname>/e/<your_environment_ID>`

     Чтобы определить `<your_environment_ID>`, см. [Что такое среда мониторинга?](/managed/discover-dynatrace/get-started/monitoring-environment#environment-id "Разберитесь и узнайте, как работать со средами мониторинга.").

## Настройка потоковой передачи логов через Firehose

Поток доставки Amazon Data Firehose можно настроить через шаблон CloudFormation либо в консоли AWS. Инструкции приведены ниже.

Если вы выбираете другой способ развёртывания (например, Terraform или собственный скрипт), используйте полный URL: `https://<your_domain>/e/<your_environment_ID>/api/v2/logs/ingest/aws_firehose` в конфигурации HTTP endpoint destination для Firehose.

С помощью шаблона CloudFormation

В консоли AWS

CloudFormation позволяет развернуть поток доставки Amazon Data Firehose одной командой развёртывания, которая создаёт стек, объединяющий несколько ресурсов AWS. Такой подход быстрее и упрощает управление ресурсами AWS.

### Разверните поток доставки Amazon Data Firehose

Чтобы получить шаблон CloudFormation и развернуть его в вашей учётной записи AWS, выполните команду ниже.

Не забудьте подставить вместо `<your_API_URL>` и `<your_API_token>` ваши значения.

Описание параметров см. в таблице ниже.

| Параметр | Описание | Значение по умолчанию |
| --- | --- | --- |
| `DYNATRACE_API_URL` | Обязательно URL вашего API. Инструкции см. в разделе [Предварительные требования](#prerequisites). |  |
| `DYNATRACE_API_KEY` | Обязательно Ваш API-токен. Инструкции см. в разделе [Предварительные требования](#prerequisites). |  |
| `STACK_NAME` | Обязательно Имя вашего стека. | `dynatrace-log-delivery-stream` |

Если у вас настроен AWS CLI, можно использовать Bash-совместимую оболочку. Иначе можно использовать CloudShell, доступный в консоли AWS.

```
DYNATRACE_API_URL=<your_API_URL>



DYNATRACE_API_KEY=<your_API_token>



STACK_NAME=dynatrace-log-delivery-stream



wget -O dynatrace-firehose-log-stream.yaml https://assets.cloud.dynatrace.com/awslogstreaming/dynatrace-firehose-log-stream.yaml && \



aws cloudformation deploy --capabilities CAPABILITY_NAMED_IAM --template-file ./dynatrace-firehose-log-stream.yaml --stack-name $STACK_NAME --parameter-overrides DtApiUrl=$DYNATRACE_API_URL DtApiToken=$DYNATRACE_API_KEY
```

### Убедитесь, что поток доставки Amazon Data Firehose развёрнут корректно

Чтобы убедиться, что поток доставки Amazon Data Firehose развёрнут корректно, выполните шаги ниже:

1. В консоли AWS перейдите в **CloudFormation**.
2. Выберите стек, который вы создали при развёртывании CloudFormation.
3. На вкладке **Events** убедитесь, что все события завершились успешно и нет упавших событий.
4. На вкладке **Parameters** убедитесь, что все указанные вами параметры имеют корректные значения.
5. На вкладке **Output** запишите выходные значения:

   * `CloudWatchSubscriptionFilterRoleArn` обозначает ARN IAM-роли, используемой при создании фильтра подписки CloudWatch;
   * `FirehoseArn` обозначает ARN созданного потока доставки Firehose.

### Создайте поток доставки Amazon Data Firehose

1. В консоли AWS откройте сервис **Amazon Data Firehose**.
2. Выберите **Create Firehose stream**.
3. В поле **Source** выберите **Direct PUT**.
4. В поле **Destination** выберите **Dynatrace**.
5. Введите **Firehose stream name** (имя потока Firehose).
6. Убедитесь, что преобразование данных отключено.
7. В поле **Ingestion type** убедитесь, что выбрано **Logs**.
8. В поле **API token** введите ваш API-токен. Инструкции см. в разделе «Предварительные требования».
9. В поле **API url** введите URL вашего API. Инструкции см. в разделе «Предварительные требования».
10. В поле **Content encoding** убедитесь, что выбрано **GZIP**.
11. В поле **Retry duration** введите `900` секунд.
12. В разделе **Buffer hints** установите для **Buffer size** значение `1` MiB, а для **Buffer interval** значение `60` секунд.
13. В разделе **Backup settings** убедитесь, что выбрано **Failed data only**.
14. В поле **S3 backup bucket** выберите **Create**.
15. В разделе **Create bucket** введите имя резервного бакета S3, при желании выберите регион, затем выберите **Create bucket**.
16. Найдите и выберите созданный **S3 backup bucket**.
17. Выберите **Create Firehose Stream**.

### Создайте IAM-роль для потоковой передачи CloudWatch Logs в Firehose

Поток Data Firehose требует доверительного отношения с CloudWatch через IAM-роль. Эту роль нужно создать заранее, до создания фильтра подписки CloudWatch Logs.

1. В консоли AWS перейдите в **IAM > Policies**.
2. Выберите **Create policy**.
3. Переключитесь в JSON-редактор и вставьте приведённый ниже JSON в качестве содержимого политики.

   ```
   {



   "Version": "2012-10-17",



   "Statement": [



   {



   "Sid": "VisualEditor0",



   "Effect": "Allow",



   "Action": [



   "firehose:PutRecord", "firehose:PutRecordBatch"



   ],



   "Resource": "*"



   }



   ]



   }
   ```

   Можно заменить `*` на ARN вашего Firehose, если требуется более ограничительная политика.
4. Выберите **Next**, введите **Policy name**, при желании добавьте теги, затем выберите **Create policy**.
5. В консоли AWS перейдите в **IAM > Roles**.
6. Выберите **Create role**.
7. Выберите **Custom trust policy** и вставьте приведённый ниже JSON в качестве содержимого политики.

   ```
   {



   "Version": "2012-10-17",



   "Statement": [



   {



   "Sid": "Statement1",



   "Effect": "Allow",



   "Principal": {



   "Service": "logs.amazonaws.com"



   },



   "Action": "sts:AssumeRole"



   }



   ]



   }
   ```
8. Выберите **Next** и выберите политику записи в Firehose, созданную на шаге 4.
9. Выберите **Next**, введите **Role name**, при желании добавьте теги, затем выберите **Create role**.

## Потоковая передача логов из CloudWatch

О потоковой передаче CloudWatch Logs из лог-группы в другом регионе или другой учётной записи см. [Совместное использование данных логов между учётными записями и регионами через Firehose](https://dt-url.net/mn03w1l).

После создания потока доставки Firehose и IAM-роли нужно подписаться на лог-группы CloudWatch, логи которых требуется пересылать в Dynatrace.
Подписаться на лог-группы можно с помощью shell-скрипта либо в консоли AWS. Инструкции приведены ниже.

С помощью shell-скрипта

В консоли AWS

Чтобы получить shell-скрипт, выполните команду ниже в bash-оболочке.

```
wget -O dynatrace-firehose-logs.sh https://assets.cloud.dynatrace.com/awslogstreaming/dynatrace-firehose-logs.sh && chmod +x dynatrace-firehose-logs.sh
```

Если у вас настроен AWS CLI, можно использовать Bash-совместимую оболочку. Иначе можно использовать CloudShell, доступный в консоли AWS.

### Подписка через перечисление имён лог-групп

**Рекомендация по использованию:** используйте этот вариант, если количество лог-групп, на которые требуется подписаться, невелико.

**Чтобы подписаться:** выполните команду ниже, не забыв заменить `<your_log_group_list>` на разделённый пробелами список имён лог-групп, на которые требуется подписаться.

**Пример списка:** `/aws/lambda/my-lambda /aws/apigateway/my-api`

```
./dynatrace-firehose-logs.sh subscribe --log-groups <your_log_group_list>
```

Дополнительные параметры не требуются, если поток доставки Firehose был создан через шаблон CloudFormation с именем стека по умолчанию.

Добавьте параметр `[--stack-name <your_stack_name>]`, если вы использовали другое имя стека.

```
./dynatrace-firehose-logs.sh subscribe --log-groups <your_log_group_list> --stack-name <your_stack_name>
```

Если поток доставки Firehose был создан другим способом (через консоль AWS или иные инструменты), добавьте следующие параметры:

* `[--firehose-arn <firehose_arn>]`
* `[--role-arn <role_arn>]`

```
./dynatrace-firehose-logs.sh subscribe --log-groups <your_log_group_list> --firehose-arn <firehose_arn> --role-arn <role_arn>
```

### Подписка через чтение лог-групп из файла

**Рекомендация по использованию:** используйте этот вариант, если количество лог-групп, на которые требуется подписаться, велико.

1. Создайте файл и впишите имя каждой лог-группы на отдельной строке.
2. Сохраните файл.
3. Выполните команду ниже, не забыв заменить `<your_file_name>` на фактическое имя файла.

   ```
   ./dynatrace-firehose-logs.sh subscribe --log-groups-from-file <your_file_name>
   ```

Автоматическое обнаружение лог-групп

Чтобы упростить создание файла, можно использовать команду авто-обнаружения ниже для получения списка имён всех лог-групп в вашей учётной записи. Список можно скорректировать вручную перед подпиской.

Не забудьте заменить `<your_log_groups_file>` на имя файла, в который требуется перенаправить вывод.

```
./dynatrace-firehose-logs.sh discover-log-groups > <your_log_groups_file>
```

### Подписка с фильтром подписки по шаблону

**Рекомендация по использованию:** по умолчанию вы подписываетесь на все логи в лог-группе. Используйте этот вариант, если требуется ограничить набор логов, на которые вы подписываетесь. Подробности о синтаксисе шаблона см. в разделе [Синтаксис фильтров и шаблонов](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

**Ограничение:** на одну лог-группу можно использовать только два фильтра подписки, поэтому возможность создавать несколько фильтров с разными шаблонами ограничена. Если создать фильтр подписки, превышающий лимит, возникает исключение AWS `LimitExceededException`.

**Чтобы подписаться:** выполните команду ниже, не забыв подставить вместо `<your_log_group_list>` и `<your_filter_pattern>` ваши значения.

```
./dynatrace-firehose-logs.sh subscribe --log-groups <your_log_group_list> --filter-pattern <your_filter_pattern>
```

### Использование и параметры подписки Опционально

Дополнительные параметры подписки см. в командах ниже.

При подстановке ваших значений вместо плейсхолдеров (`<...>`) ориентируйтесь на [таблицу параметров подписки](#subscription) для приведённых ниже команд.

```
dynatrace-firehose-logs.sh subscribe {--log-groups <your_log_group_list> | --log-groups-from-file <your_file_name>}



[--stack-name <your_stack_name>] [--filter-pattern <your_filter_pattern>] [--role-arn <role_arn>] [--firehose-arn <firehose_arn>]
```

### Таблица параметров подписки

| Параметр командной строки | Переменная окружения | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `--log-groups` | `LOG_GROUPS_LIST` | Разделённый пробелами список имён лог-групп, на которые требуется подписаться. Например: `/aws/lambda/my-lambda /aws/apigateway/my-api`. |  |
| `--log-groups-from-file` | `LOG_GROUPS_FILE` | Файл со списком лог-групп, на которые требуется подписаться. В файле имя каждой лог-группы должно быть на отдельной строке. |  |
| `--filter-pattern` | `FILTER_PATTERN` | Если установлен, позволяет подписаться на отфильтрованный поток логов. | Вы подписываетесь на все логи в лог-группе. |
| `--stack-name` | `STACK_NAME` | Имя стека CloudFormation, в котором развёрнуты ресурсы. | `dynatrace-aws-logs` |
| `--firehose-arn` | `FIREHOSE_ARN` | Укажите, в какой инстанс Amazon Data Firehose должны передаваться логи, передав его ARN (Amazon Resource Name). **Рекомендация по использованию:** установите этот параметр, если для создания потока доставки вы не использовали шаблон CloudFormation. | Извлекается из выходных значений стека CloudFormation, использованного на шаге развёртывания: либо значение `$DEFAULT_STACK_NAME` по умолчанию, либо значение, указанное параметром `--stack-name <your_stack_name>`. |
| `--role-arn` | `ROLE_ARN` | ARN IAM-роли, которая даёт CloudWatch Logs разрешение доставлять принятые лог-события в целевой поток. **Рекомендация по использованию:** установите этот параметр, если для создания потока доставки вы не использовали шаблон CloudFormation. | Извлекается из выходных значений стека CloudFormation, использованного на шаге развёртывания: либо значение `$DEFAULT_STACK_NAME` по умолчанию, либо значение, указанное параметром `--stack-name <your_stack_name>`. |

## Отписка от лог-групп

Если пересылать логи в Dynatrace больше не требуется, для отписки от лог-групп используйте один из двух вариантов ниже.

### Отписка через перечисление имён лог-групп

Выполните команду ниже, не забыв заменить `<your_log_group_list>` на разделённый пробелами список имён лог-групп, от которых требуется отписаться.

```
./dynatrace-firehose-logs.sh unsubscribe --log-groups <your_log_group_list>
```

### Отписка через чтение лог-групп из файла

Выполните команду ниже, не забыв заменить `<your_file_name>` на имя файла, который вы создали для [подписки через чтение лог-групп из файла](#from-file).

```
./dynatrace-firehose-logs.sh unsubscribe --log-groups-from-file <your_file_name>
```

### Использование и параметры отписки Опционально

Дополнительные параметры отписки см. в командах ниже.

При подстановке ваших значений вместо плейсхолдеров (`<...>`) ориентируйтесь на [таблицу параметров отписки](#unsubscribe-table) для приведённых ниже команд.

```
dynatrace-firehose-logs.sh unsubscribe {--log-groups <your_log_group_list> | --log-groups-from-file <your_file_name>} [--stack-name <your_stack_name>]
```

### Таблица параметров отписки

| Параметр командной строки | Переменная окружения | Описание | Значение по умолчанию |
| --- | --- | --- | --- |
| `--log-groups` | `LOG_GROUPS_LIST` | Разделённый пробелами список имён лог-групп, от которых требуется отписаться. Например: `/aws/lambda/my-lambda /aws/apigateway/my-api`. |  |
| `--log-groups-from-file` | `LOG_GROUPS_FILE` | Файл со списком лог-групп, от которых требуется отписаться, где имя каждой лог-группы записано на отдельной строке. |  |
| `--stack-name` | `STACK_NAME` | Имя стека CloudFormation, в котором развёрнуты ресурсы. | `dynatrace-aws-logs` |

1. В консоли AWS перейдите в **CloudWatch > Logs > Log Groups**.
2. Выберите детали лог-группы.
3. Выберите **Actions > Subscription filters > Create Amazon Data Firehose subscription filter**.
4. Выберите поток доставки Firehose, созданный на предыдущих шагах.
5. Выберите IAM-роль, созданную на предыдущих шагах.
6. Введите имя фильтра подписки.
7. Выберите **Start Streaming**.

## Отправка логов из других сервисов напрямую в Firehose

Чтобы настроить логи, не сохраняемые в CloudWatch, для сервисов, которые отправляют их напрямую в Firehose, см. документацию по конкретному сервису, например:

* [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/msk-logging.html)
* [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-firehose.html)

Для логов из AWS-сервисов, которые отправляются в S3âа не в Firehose или CloudWatchâсм. [документацию на GitHub](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder).

## Просмотр логов AWS

После настройки потоковой передачи через Data Firehose вы можете просматривать и анализировать логи AWS в Dynatrace: перейдите в **Logs & Events** или **Notebooks** и отфильтруйте логи AWS. Для логов, принятых через Amazon Data Firehose, атрибут `aws.data_firehose.arn` будет содержать ARN того Firehose, который передал данные в Dynatrace. Логи AWS-сервисов с поддержкой связывания сущностей будут автоматически отображаться в приложении Cloud для контекстного анализа.

Если логи поступают, значит вам удалось успешно настроить потоковую передачу логов AWS.

Если в течение 10 минут логи не появляются, см. раздел «Поиск и устранение неполадок» на этой странице.

Amazon Data Firehose включает опциональные параметры (пары «ключ-значение») в каждый HTTP-вызов. Эти параметры инстанса помогают идентифицировать пункты назначения и управлять ими, поскольку они обрабатываются и автоматически добавляются как атрибуты к принятым записям логов.

**Поддерживаемые сервисы**

| Имя сервиса | Обогащение логов | Связывание сущностей |
| --- | --- | --- |
| AWS Lambda [1](#fn-1-1-def) | Поддерживается | Поддерживается |
| AWS App Runner | Поддерживается | Поддерживается |
| AWS CloudTrail [2](#fn-1-2-def) | Поддерживается | - |
| Amazon API Gateway | Поддерживается | - |
| Amazon SNS | Поддерживается | Поддерживается |
| Amazon RDS | Поддерживается | Поддерживается |
| Все сервисы, пишущие в CloudWatch | Поддерживается | - |
| Все сервисы, отправляющие логи напрямую в Data Firehose | - | - |

1

Имя лог-группы AWS Lambda можно изменить. Для обогащения логов используйте имя лог-группы по умолчанию `/aws/lambda/<function name>`.

2

Имя лог-группы AWS CloudTrail можно изменить. Для обогащения логов имя лог-группы должно начинаться с `aws-cloudtrail-logs`.

## Поддержка Environment ActiveGate

ActiveGate версии 1.287+

По умолчанию Environment ActiveGate слушает API-запросы на порту 9999. Однако в настоящее время для доставки данных через HTTP endpoint для Amazon Data Firehose поддерживается только порт 443.

ActiveGate должен быть настроен с действительным CA-подписанным SSL-сертификатом, чтобы принимать логи от AWS Data Firehose.

Для успешной доставки данных от Amazon Data Firehose к API-эндпоинту Environment ActiveGate рекомендуется настроить проброс портов с порта 443 на 9999 на хосте ActiveGate.

Ниже приведены несколько примеров таких конфигураций. Подробности см. в документации, относящейся к вашей операционной системе и сетевым решениям.

### Примеры конфигураций

#### Amazon Linux, RedHat Linux

`firewalld` предоставляет динамически управляемый брандмауэр. Подробности см. в [документации](https://firewalld.org/documentation/).

Чтобы добавить проброс портов через `firewalld` (примечание: эти действия выполняются с правами root):

```
firewall-cmd --zone=public --add-forward-port=port=443:proto=tcp:toport=9999 --permanent



firewall-cmd --zone=public --add-port=9999/tcp --permanent
```

#### Ubuntu Linux

Uncomplicated Firewall (`ufw`) представляет собой фронтенд для iptables. Подробности см. в [документации](https://wiki.ubuntu.com/UncomplicatedFirewall).

Чтобы добавить проброс портов через `ufw` (примечание: эти действия выполняются с правами root):

1. В файле `/etc/ufw/before.rules` добавим NAT-таблицу после filter-таблицы (таблицы, которая начинается с `*filter` и заканчивается `COMMIT`):

```
*nat



:PREROUTING ACCEPT [0:0]



-A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 9999



COMMIT
```

2. Разрешите трафик через порты 443 и 9999:

```
ufw allow 443/tcp



ufw allow 9999/tcp
```

3. Перезапустите `ufw`.

#### Windows Server 2022

Network shell (netsh) представляет собой утилиту командной строки, позволяющую настраивать и отображать состояние ролей и компонентов различных серверов сетевых коммуникаций. Подробности см. в [документации](https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh).

Чтобы добавить проброс портов через `netsh interface portproxy`:

```
netsh interface portproxy add v4tov4 listenport=443 connectport=9999 connectaddress=<the current IP address of your computer>
```

С помощью опций `netsh interface portproxy add` `v4tov6`/`v6tov4`/`v6tov6` можно создавать правила проброса портов между IPv4 и IPv6 адресами.

## Поиск и устранение неполадок

Если переданные из Data Firehose логи недоступны в вашей среде, выполните шаги ниже:

1. Убедитесь, что логи из CloudWatch отправляются в Firehose. Проверьте метрики потока доставки Firehose (Incoming put requests, Incoming bytes). Если данные в Firehose не поступают, проверьте, что лог-группа CloudWatch Logs генерирует актуальные логи, а IAM-роль, выбранная при создании фильтра подписки, имеет разрешение писать логи в Firehose.
2. Убедитесь, что логи успешно отправляются из Firehose в Dynatrace. Проверьте метрики потока доставки Firehose (HTTP endpoint delivery success, records delivered to HTTP endpoint). В случае ошибок проверьте AWS Firehose CloudWatch Logs и проверьте API-токен и URL API Dynatrace.
3. Убедитесь, что логи принимаются Dynatrace. Проверьте метрику self-monitoring Dynatrace в Data Explorer:

```
dsfm:active_gate.rest.request_count:filter(and(or(eq(operation,"POST /logs/ingest/aws_firehose")))):splitBy(response_code):sort(value(auto,descending)):limit(20)
```

Данные метрики должны присутствовать, а `response\_code` должен принимать только значение `200`.

## Ограничения

Пропускная способность приёма ограничена возможностями Amazon Data Firehose. Подробности см. в разделе [Amazon Data Firehose Quota](https://docs.aws.amazon.com/firehose/latest/dev/limits.html). Amazon может увеличить лимиты Firehose по запросу.

AWS Firehose не поддерживает подключения через VPC для HTTP-эндпоинтов.