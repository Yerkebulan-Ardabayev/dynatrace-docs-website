---
title: Создание подключения AWS через настройки
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/create-an-aws-connection/aws-connection-app-settings
scraped: 2026-03-06T21:24:53.493213
---

Подключите вашу учетную запись AWS за несколько шагов, которые сгенерируют готовый к развертыванию шаблон CloudFormation.

Стек CloudFormation развернет основные обязательные ресурсы внутри вашей учетной записи AWS (IAM-роль мониторинга Dynatrace, секреты AWS, Lambda-функцию интеграции с API Dynatrace).

После успешного развертывания будет создано подключение от Dynatrace к вашей учетной записи AWS. Затем Dynatrace будет выполнять вызовы API к вашей учетной записи AWS для опроса и отправки телеметрии в вашу среду Dynatrace.

Новая интеграция не развертывает и не использует вычислительные ресурсы ActiveGate внутри вашей учетной записи AWS для опроса или отправки телеметрии.

Процесс прозрачен и полностью управляется Dynatrace.

## Обзор

### Общие рекомендации

Мы настоятельно не рекомендуем подключать учетные записи AWS, которые активно мониторятся нашей классической интеграцией с AWS. Подключение таких учетных записей может повысить вероятность троттлинга API AWS, что потенциально приведет к перебоям в работе сервисов.

### Ограничения

* Разделы GovCloud и China не поддерживаются.
* Dynatrace предназначен для поддержки крупных и сложных сред AWS. По умолчанию среда Dynatrace может вместить до 3 000 подключений AWS (каждое подключение представляет одну учетную запись AWS).

  Это мягкий лимит. Если вы планируете его превысить (в рамках одной среды Dynatrace), пожалуйста, откройте запрос в службу поддержки для увеличения этого лимита.

* AWS не поддерживает назначения API EventBridge во всех регионах. Поэтому прием событий недоступен в регионах, которые его не поддерживают. Подробности см. в разделе [Доступность функций EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html#feature-availability-apid).

## Предварительные требования

Только администратор учетной записи Dynatrace и администратор AWS могут успешно выполнить начальные предварительные требования.

### 1. AWS

Действия в этом разделе могут и (должны) выполняться только администратором AWS. Все необходимые [разрешения AWS](#aws-permissions) должны быть предоставлены для успешного развертывания стеков CloudFormation и связанных ресурсов AWS.

В средах с полным разделением обязанностей мы рекомендуем, чтобы администратор Dynatrace передавал шаблоны команде платформы/администраторам AWS.

#### Основные стеки CFN

Текущая последняя рабочая версия: v1.0.0

* [Основной стек развертывания](https://dynatrace-data-acquisition.s3.us-east-1.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-activation.yaml)

  + [Вложенный стек клиента API](https://dynatrace-data-acquisition.s3.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-nested-dt-api-function.yaml)
  + [Вложенный стек интеграции](https://dynatrace-data-acquisition.s3.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-nested-integration.yaml)
  + [Вложенный стек IAM-роли мониторинга](https://dynatrace-data-acquisition.s3.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-nested-monitoring-role.yaml)

#### Условные (вложенные) стеки CFN

Развертываются на основе выбора пользователя при подключении

* [Вложенные роли StackSet](https://dynatrace-data-acquisition.s3.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-stack-logs.yaml)
* [Вложенный стек потоков логов Firehose](https://dynatrace-data-acquisition.s3.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-stack-logs.yaml)
* [Вложенный стек интеграции AWS EventBridge](https://dynatrace-data-acquisition.s3.amazonaws.com/aws/deployment/cfn/v1.0.0/da-aws-stack-events.yaml)

Ресурсы AWS, создаваемые шаблонами CloudFormation

##### Уровень 1: Ресурсы основного шаблона (`da-aws-activation.yaml`)

Прямые ресурсы, создаваемые в регионе развертывания:

1. `DynatraceApiClientStack` (`AWS::CloudFormation::Stack`)

   * Вложенный стек, создающий функцию клиента API (взаимодействие с API Dynatrace, создание/удаление подключения)
   * Ссылка: `da-aws-nested-dt-api-function.yaml`
2. `ReportStartedStatusResource` (`Custom::DynatraceApiAccessFunction`)

   * Пользовательский ресурс для передачи статуса начала развертывания в Dynatrace
3. `DynatraceIntegrationStack` (`AWS::CloudFormation::Stack`)

   * Вложенный стек для основной интеграции
   * Ссылка: `da-aws-nested-integration.yaml`
4. `DynatraceStackSetRoleStack` (`AWS::CloudFormation::Stack`)

   * Условный: создается только при включении приема логов или событий
   * Создает роли администрирования и выполнения StackSet
   * Ссылка: `da-aws-nested-stackset-role.yaml`
5. `DynatraceLogIngestStackSet` (`AWS::CloudFormation::StackSet`)

   * Условный: только если `pDtLogsIngestEnabled = 'TRUE'`
   * Развертывает инфраструктуру приема логов в указанных регионах
   * Ссылка: `da-aws-stack-logs.yaml`
6. `DynatraceEventIngestStackSet` (`AWS::CloudFormation::StackSet`)

   * Условный: только если `pDtEventsIngestEnabled = 'TRUE'`
   * Развертывает инфраструктуру приема событий в указанных регионах
   * Ссылка: `da-aws-stack-events.yaml`
7. `ReportCompleteStatusResource` (`Custom::DynatraceApiAccessFunction`)

   * Пользовательский ресурс для передачи статуса завершения развертывания в Dynatrace

##### Уровень 2: Ресурсы вложенных стеков

Из `DynatraceApiClientStack` (`da-aws-nested-dt-api-function.yaml`) -- ожидаемые ресурсы:

* **Lambda-функция**: функция клиента API Dynatrace
* **IAM-роль**: роль выполнения Lambda
* **Секрет Secrets Manager**: хранилище токена API Dynatrace
* **Ключ KMS** (условный): управляемый клиентом ключ, если `pUseCMK = 'TRUE'`
* **Псевдоним KMS** (условный): псевдоним для CMK
* **Группа логов Lambda**: логи CloudWatch для Lambda-функции

Из `DynatraceIntegrationStack` (`da-aws-nested-integration.yaml`) -- ожидаемые ресурсы:

* **IAM-роль**: роль мониторинга Dynatrace с доверительным отношением к учетной записи Dynatrace
* **IAM-политика**: политика разрешений мониторинга
* **Пользовательский ресурс**: для установления подключения с Dynatrace

Из `DynatraceStackSetRoleStack` (`da-aws-nested-stackset-role.yaml`) -- ожидаемые ресурсы:

* **IAM-роль**: роль администрирования StackSet
* **IAM-роль**: роль выполнения StackSet
* **IAM-политики**: прикрепленные к обеим ролям

##### Уровень 3: Развертываемые основные ресурсы (регион управления)

Минимальные ресурсы (без включенного приема логов/событий), развертываемые только в одном регионе (регион управления):

* **Два пользовательских ресурса**: передача статуса начала и завершения развертывания
* **Lambda-функция** + IAM-роли + **Secrets Manager**: создание/удаление подключения, хранение токенов платформы Dynatrace в Secrets Manager
* **IAM-роль мониторинга Dynatrace**: роль мониторинга Dynatrace с доверительным отношением к учетной записи Dynatrace

#### Уровень 4: Ресурсы, развертываемые через StackSet (условные, для каждого региона)

Из `DynatraceLogIngestStackSet` (`da-aws-stack-logs.yaml`); развертывается в каждом регионе из списка `pDtLogsIngestRegions`. Ожидаемые ресурсы на регион:

* **Поток доставки Kinesis Data Firehose**: для пересылки логов в Dynatrace
* **IAM-роль**: роль доставки Firehose
* **Корзина S3**: резервная/буферная корзина для неудачных доставок
* **Секрет Secrets Manager**: хранилище токена приема Dynatrace
* **Ключ KMS** (условный): если `pUseCMK = 'TRUE'`

Из `DynatraceEventIngestStackSet` (`da-aws-stack-events.yaml`); развертывается в каждом регионе из списка `pDtEventsIngestRegions`. Ожидаемые ресурсы на регион:

* **Правило EventBridge**: для перехвата событий AWS
* **Назначение API EventBridge**: конечная точка Dynatrace
* **Подключение EventBridge**: аутентификация для назначения API
* **IAM-роль**: роль выполнения EventBridge
* **Секрет Secrets Manager**: хранилище токена приема Dynatrace

#### Политика разрешений AWS IAM для развертывания стеков CloudFormation

Убедитесь, что пользователю или роли AWS, используемым для развертывания стеков CloudFormation, предоставлены следующие (минимальные) политики разрешений.

Для обеспечения минимальных привилегий -- ограничения пользователей, создающих подключения AWS по определенному шаблону именования, используйте значение для `<Deployment-Stack-Name-Prefix>`. Это гарантирует, что любое создаваемое подключение должно соответствовать этому точному [соглашению об именовании](#conn-model).

```
{


"Version": "2012-10-17",


"Statement": [


{


"Sid": "cloudformation0",


"Effect": "Allow",


"Action": [


"cloudformation:CreateStack",


"cloudformation:DescribeStacks",


"cloudformation:UpdateStack",


"cloudformation:ListStacks",


"cloudformation:DescribeStackResources",


"cloudformation:DeleteStack",


"cloudformation:CreateChangeSet",


"cloudformation:DescribeChangeSet",


"cloudformation:ExecuteChangeSet",


"cloudformation:CreateStackInstances",


"cloudformation:ListStackInstances",


"cloudformation:DescribeStackInstance",


"cloudformation:DeleteStackInstances",


"cloudformation:CreateStackSet",


"cloudformation:UpdateStackSet",


"cloudformation:DescribeStackSet",


"cloudformation:DescribeStackSetOperation",


"cloudformation:ListStackSetOperationResults",


"cloudformation:DeleteStackSet",


"cloudformation:TagResource",


"cloudformation:UntagResource"


],


"Resource": [


"arn:aws:cloudformation:*:<AWS-Account-ID>:stackset-target/*",


"arn:aws:cloudformation:<Deployment-Region>:<AWS-Account-ID>:stackset/Dynatrace*:*",


"arn:aws:cloudformation:<Deployment-Region>:<AWS-Account-ID>:stack/<Deployment-Stack-Name-Prefix>*/*",


"arn:aws:cloudformation:*:<AWS-Account-ID>:stack/StackSet-Dynatrace*/*",


"arn:aws:cloudformation:*:<AWS-Account-ID>:type/resource/*"


]


},


{


"Sid": "cloudformation1",


"Effect": "Allow",


"Action": [


"cloudformation:GetTemplate",


"cloudformation:ValidateTemplate",


"cloudformation:GetTemplateSummary"


],


"Resource": [


"*"


]


},


{


"Sid": "lambda",


"Effect": "Allow",


"Action": [


"lambda:CreateFunction",


"lambda:UpdateFunctionCode",


"lambda:UpdateFunctionConfiguration",


"lambda:GetFunction",


"lambda:InvokeFunction",


"lambda:DeleteFunction",


"lambda:TagResource",


"lambda:UntagResource"


],


"Resource": [


"arn:aws:lambda:<Deployment-Region>:<AWS-Account-ID>:function:DynatraceApiClientFunction*"


]


},


{


"Sid": "iam",


"Effect": "Allow",


"Action": [


"iam:CreatePolicy",


"iam:CreatePolicyVersion",


"iam:DeletePolicyVersion",


"iam:DeletePolicy",


"iam:CreateRole",


"iam:UpdateRole",


"iam:DeleteRole",


"iam:PassRole",


"iam:AttachRolePolicy",


"iam:PutRolePolicy",


"iam:DetachRolePolicy",


"iam:GetRole",


"iam:GetPolicy",


"iam:ListPolicyVersions",


"iam:TagPolicy",


"iam:TagRole",


"iam:UntagPolicy",


"iam:UntagRole",


"iam:GetRolePolicy",


"iam:UpdateAssumeRolePolicy",


"iam:DeleteRolePolicy"


],


"Resource": [


"arn:aws:iam::<AWS-Account-ID>:policy/<Deployment-Stack-Name-Prefix>*",


"arn:aws:iam::<AWS-Account-ID>:role/<Deployment-Stack-Name-Prefix>*",


"arn:aws:iam::<AWS-Account-ID>:role/Dynatrace*",


"arn:aws:iam::<AWS-Account-ID>:policy/Dynatrace*"


]


},


{


"Sid": "s3",


"Effect": "Allow",


"Action": [


"s3:GetObject",


"s3:CreateBucket",


"s3:DeleteBucket",


"s3:PutLifecycleConfiguration",


"s3:PutBucketTagging"


],


"Resource": [


"arn:aws:s3:::dynatrace*"


]


},


{


"Sid": "secretsmanager",


"Effect": "Allow",


"Action": [


"secretsmanager:CreateSecret",


"secretsmanager:DescribeSecret",


"secretsmanager:UpdateSecret",


"secretsmanager:GetSecretValue",


"secretsmanager:PutSecretValue",


"secretsmanager:TagResource",


"secretsmanager:DeleteSecret",


"secretsmanager:PutResourcePolicy",


"secretsmanager:DeleteResourcePolicy"


],


"Resource": [


"arn:aws:secretsmanager:<Deployment-Region>:<AWS-Account-ID>:secret:DynatraceAPIAccessToken*",


"arn:aws:secretsmanager:<Deployment-Region>:<AWS-Account-ID>:secret:DynatraceAPIPlatformToken*",


"arn:aws:secretsmanager:<Deployment-Region>:<AWS-Account-ID>:secret:/dynatrace/*"


]


},


{


"Sid": "kms0",


"Effect": "Allow",


"Action": [


"kms:CreateKey",


"kms:TagResource",


"kms:UntagResource"


],


"Resource": "*",


"Condition": {


"StringEquals": {


"aws:RequestTag/dt:CreatedBy": "Dynatrace"


}


}


},


{


"Sid": "kms1",


"Effect": "Allow",


"Action": [


"kms:CreateGrant",


"kms:RevokeGrant",


"kms:DescribeKey",


"kms:GetKeyPolicy",


"kms:PutKeyPolicy",


"kms:ScheduleKeyDeletion"


],


"Resource": "*",


"Condition": {


"StringEquals": {


"aws:ResourceTag/dt:CreatedBy": "Dynatrace"


}


}


},


{


"Sid": "kms2",


"Effect": "Allow",


"Action": [


"kms:CreateAlias",


"kms:DeleteAlias",


"kms:UpdateAlias"


],


"Resource": [


"arn:aws:kms:<Deployment-Region>:<AWS-Account-ID>:key/*"


],


"Condition": {


"StringEquals": {


"aws:ResourceTag/dt:CreatedBy": "Dynatrace"


}


}


},


{


"Sid": "kms3",


"Effect": "Allow",


"Action": [


"kms:CreateAlias",


"kms:DeleteAlias",


"kms:UpdateAlias"


],


"Resource": "arn:aws:kms:<Deployment-Region>:<AWS-Account-ID>:alias/dynatrace/*/keys/aws/integration/*"


},


{


"Sid": "logs0",


"Effect": "Allow",


"Action": [


"logs:DescribeLogGroups"


],


"Resource": "*"


},


{


"Sid": "logs1",


"Effect": "Allow",


"Action": [


"logs:DeleteLogGroup",


"logs:CreateLogGroup",


"logs:DeleteLogStream",


"logs:CreateLogStream",


"logs:DescribeLogStreams",


"logs:PutRetentionPolicy",


"logs:ListTagsForResource",


"logs:DescribeIndexPolicies",


"logs:AssociateKmsKey",


"logs:DisassociateKmsKey",


"logs:PutLogEvents",


"logs:TagResource"


],


"Resource": [


"arn:aws:logs:<Deployment-Region>:<AWS-Account-ID>:log-group:/aws/lambda/<Deployment-Stack-Name-Prefix>*",


"arn:aws:logs:<Deployment-Region>:<AWS-Account-ID>:log-group:/aws/lambda/DynatraceApiClientFunction-*"


]


}


]


}
```

На этом все базовые предварительные требования AWS IAM выполнены. Имейте в виду, что разрешения IAM-роли/пользователя необходимы для каждой подключаемой учетной записи AWS.

Мы рекомендуем, чтобы администратор AWS предварительно создавал эти IAM-конструкции программным способом.

### 2. Dynatrace

Действия в этом разделе могут и (должны) выполняться только администратором учетной записи Dynatrace.

Новый мониторинг платформы AWS был интегрирован с основной архитектурой управления идентификацией и доступом (IAM) Dynatrace.

Узнайте больше об основных концепциях:

* Пользователи, сервисные пользователи
* Локальные группы, политики
* [Токены платформы для сервисных пользователей](../../../manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens.md#allow-users-to-generate-platform-tokens-against-service-users "Создание персонализированных токенов платформы для доступа к сервисам Dynatrace через API в контексте вашего пользователя.")

В контексте данного раздела документации:

Администратор учетной записи Dynatrace
:   Встроенный пользователь с разрешением `View and manage users and groups`.

CloudsAdmins
:   Пользовательская IAM-группа, созданная клиентом, члены которой смогут создавать и управлять подключениями AWS в ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки**.

CloudAdmin
:   IAM-пользователь, член группы `CloudsAdmins`. Имя используется здесь только для контекста; можно использовать любого IAM-пользователя Dynatrace.

Сервисный пользователь
:   Неинтерактивная IAM-идентичность, для которой будут созданы токены платформы.

Токен платформы
:   Секреты аутентификации и авторизации, используемые для установления безопасной связи с API Dynatrace.
    В нашем контексте необходимо создать два токена платформы:

    * `Settings PT` -- позволяет создавать и управлять подключением AWS.
    * `Ingest PT` -- позволяет программный прием push-телеметрии из AWS.

Приложение Data-Acquisition AWS Integration
:   Встроенная IAM-политика, созданная Dynatrace, которая содержит все области разрешений (с минимальными привилегиями), необходимые для поддержки создания и управления подключением AWS из ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки**. При использовании мастера нового подключения автоматически создается новый сервисный пользователь и связанные токены платформы. Также будут привязаны все необходимые разрешения для создания и управления подключением, а также приема телеметрии из AWS (логи Firehose и события EventBridge).

#### Интерактивная IAM-идентичность (IAM-пользователь)

1. Создайте группу `CloudsAdmins`.

   После создания группы `CloudsAdmins` выберите **Permissions** > **Scope** и добавьте политики `Data-Acquisition AWS Integration App` и `Standard User`.

   Примените **Account-Wide** или **Environment-Wide**, затем выберите **Save**.

   Проверка: раздел **Permissions** группы `CloudsAdmins` должен отображать:

   * `Data-Acquisition AWS Integration App`
   * `Standard User`
2. Назначьте вашего IAM-пользователя CloudAdmin (или любого другого IAM-пользователя Dynatrace) членом группы `CloudsAdmins`.

## Подключение

Перед началом убедитесь, что все [предварительные требования](#prerequisites) выполнены.

1. Войдите в Dynatrace как IAM-пользователь (член IAM-группы `CloudsAdmins`) и откройте ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки**.
2. Перейдите в **Collect and capture** > **Cloud and virtualization** > **AWS** и выберите **New connection**.

Если кнопка неактивна, это означает, что у вас нет соответствующих разрешений для создания подключения. Пожалуйста, свяжитесь с вашим администратором.

### 1. Выбор модели подключения

1. Введите понятное имя подключения, которое должно быть уникальным (например, `MyEastProd3Account`).
2. Введите **AWS Account ID**, где вы планируете развернуть подключение.
3. Выберите **Deployment region**.

   Регион развертывания -- это регион AWS, из которого будет развернут стек CloudFormation.

   Если вы планируете использовать опцию приема событий, убедитесь, что выбран регион развертывания, поддерживающий [назначения API EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/feature-availability.html#feature-availability-apid).
4. Выберите **Next**.

### 2. Выбор варианта наблюдаемости

1. Выберите **рекомендуемый** путь наблюдаемости. В настоящее время поддерживаются два пути:

   * **Recommended**: конфигурация мониторинга -- это предустановленный (неизменяемый) вариант, настраиваются только отслеживаемые регионы. Для каждой учетной записи-участника AWS этот поток обеспечивает:

     + Инвентаризацию ресурсов учетной записи AWS с помощью ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** (для поддерживаемых сервисов AWS).
     + Топологию ресурсов учетной записи AWS, представленную в виде расширенных сущностей ресурсов с помощью ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds** (для поддерживаемых сервисов AWS).
     + Опрос метрик Amazon CloudWatch API (для каждого включенного региона) для наших рекомендуемых сервисов (автоматически включены).
     + Регионы, которые были выбраны, позволяющие администратору AWS развернуть потоки Amazon Data Firehose для приема логов в виде наборов стеков в консоли AWS Organizations.
   * **Advanced**: наиболее детальный путь конфигурации мониторинга. Позволяет полностью настроить любые параметры мониторинга для продвинутых сценариев.

   Независимо от выбранного пути, настройка всех поддерживаемых параметров мониторинга возможна после подключения.

   Сигнал топологии включен автоматически; его нельзя отключить.
2. Выберите отслеживаемые **регионы AWS**, которые вы хотите мониторить.

   Отслеживаемые регионы -- это регионы AWS, в которых Dynatrace может безопасно опрашивать метрики, топологию и отправлять логи.

   Вам необходимо включить `us-east-1` независимо от желаемых отслеживаемых регионов, поскольку глобальные ресурсы AWS находятся в `us-east-1`.
3. Выберите **Next**.

После успешного подключения вы сможете настроить отслеживаемые регионы AWS и все другие поддерживаемые параметры мониторинга для каждой учетной записи-участника AWS.

### 3. Получение токенов платформы для сервисных пользователей

Генерация токенов на этом шаге автоматически создает сервисного пользователя, токены платформы и привязывает все необходимые политики.

1. Сгенерируйте токены настроек и приема. Альтернативно вы можете вставить уже существующие токены.
2. Выберите **Download** и **Next**.

   Если кнопка загрузки неактивна, это означает, что поля токенов Dynatrace не заполнены токенами платформы.

### 4. Завершение

1. Перейдите в консоль AWS и войдите в назначенную учетную запись AWS с IAM-пользователем AWS, имеющим все необходимые разрешения для развертывания стеков CloudFormation.
2. Выберите **Deploy the CloudFormation in AWS Console**.

Если вы практикуете разделение обязанностей ролей, администратор Dynatrace может не иметь доступа/разрешений к среде AWS.

В этом случае выберите **Copy Deployment Link**.

Поделитесь этой глубокой ссылкой и загруженным CSV-файлом токенов платформы с вашей командой платформы и/или администраторами AWS.

Это позволит им развернуть стек CloudFormation с конфигурациями мастера, которые вы установили.

3. Скопируйте токены настроек и приема из загруженного CSV-файла (имя файла будет соответствовать понятному имени подключения) и вставьте их в соответствующие параметры CloudFormation (токен настроек, токен приема).
4. Разверните стек.
5. Когда развертывание стеков CloudFormation завершится успешно (что может занять до 15 минут), вернитесь в мастер и подтвердите.

Если развертывание стека CloudFormation не удалось, см. [Устранение неполадок](#troubleshooting).

### 5. Настройка оповещений о состоянии и предупреждающих сигналов (необязательно)

Вы можете настроить оповещения о состоянии и предупреждающие сигналы сейчас или [позже](../../../observe/infrastructure-observability/cloud-platform-monitoring/clouds-app.md#alerting "Мониторинг всех облачных платформ в одном месте.").

Оповещения о состоянии и предупреждающие сигналы помогают мониторить вашу инфраструктуру, предоставляя четкие, действенные аналитические данные. Эти функции снижают шум от проблем инфраструктуры и улучшают возможности оповещения, чтобы вы могли сосредоточиться на самом важном. Это достигается за счет лучшей категоризации обнаруженных неисправностей.

* Для критических событий создается оповещение о состоянии, запускающее расследование проблем Dynatrace.
* Для некритических ситуаций предупреждающий сигнал информирует вас о потенциальной проблеме.

Успешное подключение включает два элемента:

* В ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** > **Collect and capture** > **Cloud and virtualization** > **AWS** новое подключение AWS имеет статус `Healthy`.
* В консоли AWS CloudFormation стеки CloudFormation находятся в статусе `CREATE_COMPLETE`.

## Что дальше?

* Перейдите в [![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**](../../../observe/infrastructure-observability/cloud-platform-monitoring/clouds-app.md "Мониторинг всех облачных платформ в одном месте."). Ресурсы AWS с телеметрией должны скоро появиться.
* См. Управление подключениями AWS, чтобы узнать, как управлять вновь созданным подключением.
* Настройте подписки на группы логов CloudWatch.

## Устранение неполадок

Функция нового подключения отключена. При наведении на нее я вижу сообщение, что у меня нет разрешений.

Убедитесь, что ваш IAM-пользователь Dynatrace имеет соответствующие области разрешений для создания и управления подключением. Подробности см. в разделе [Создание базовой конфигурации IAM Dynatrace](#iam-baseline).

Стек CloudFormation не завершился успешно. Как найти причину?

Если развертывание CloudFormation не удается, это часто связано с недостатком разрешений AWS IAM, достижением лимитов сервисов AWS или политиками управления сервисами (Service Control Policies), настроенными в вашей организации AWS Organizations.

Для запуска нашего вспомогательного скрипта устранения неполадок для обнаружения причины

1. Откройте AWS CloudShell в **консоли управления AWS**.

   Альтернативно вы можете запустить bash с установленным AWS CLI.
2. Загрузите скрипт:

   ```
   wget -q https://dynatrace-data-acquisition.s3.us-east-1.amazonaws.com/aws/deployment/cfn/da-activation-check.sh -O da-activation-check.sh && chmod +x ./da-activation-check.sh
   ```
3. Запустите скрипт для анализа причины сбоя и вывода скрипта `./da-activation-check.sh --stack-name <activation-stack-name>`.

   Имя основного стека активации соответствует имени подключения AWS, указанному в списке подключений Dynatrace, например, имя подключения: `MyEastProd3Account`

Для ручного поиска причины сбоя

1. Перейдите в **консоль управления AWS** > события стека **CloudFormation** и найдите причину.
2. Также проверьте вложенные стеки и экземпляры наборов стеков (если был включен прием логов/событий) на наличие неудачных событий.

Если вы столкнулись с ошибкой, которую не можете решить самостоятельно, [откройте тикет поддержки Dynatrace](https://www.dynatrace.com/services-support/dynatrace-one/), предоставив вывод скрипта.

Причина сбоя развертывания CloudFormation -- недействительный или истекший токен. Что делать?

Лучший способ решить эту проблему -- удалить неудавшийся стек и повторить развертывание, указав действительные токены в качестве параметров. Вы можете начать развертывание из веб-интерфейса ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** Dynatrace, чтобы сгенерировать новый токен API.

Причины сбоя развертывания CloudFormation связаны с разрешениями, так как я вижу сообщения о том, что я не авторизован для выполнения X или Y. Что делать?

Если вы видите в сообщениях об ошибках стека CloudFormation, например, `"User: arn:aws: <...> is not authorized to perform: <...> on resource: <...>"`, это означает, что вы не включили необходимые разрешения пользователя/роли из нашей политики. Обновите настройку, добавив необходимые [разрешения AWS](#aws-permissions), очистите текущую настройку и перезапустите процесс.

Чтобы узнать, как очистить текущую настройку, см. [Стек CloudFormation не завершился успешно. Я исправил проблему. Как очистить текущую настройку и начать заново?](#clean-setup)

Причина сбоя развертывания CloudFormation -- 'Account XXX has not enabled Region-XYZ'. Что делать?

Если вы видите в сообщениях об ошибках стека CloudFormation, например, `"Account XXX has not enabled [Region-XYZ]: ..."`, очистите текущую настройку, включите этот регион или удалите его из параметров развертывания и перезапустите процесс.

Чтобы узнать, как очистить текущую настройку, см. [Стек CloudFormation не завершился успешно. Я исправил проблему. Как очистить текущую настройку и начать заново?](#clean-setup)

Причина сбоя развертывания CloudFormation -- создание потока доставки Firehose. Что делать?

Если вы видите в сообщениях об ошибках стека CloudFormation, например, `"You are not subscribed to this service"` или `"The AWS Access key Id needs a subscription for the service (Service Firehose)"`, это связано с тем, что новые сервисы, такие как Firehose, требуют активации для некоторых новых учетных записей. См. [как решить проблемы при доступе к сервису в консоли управления AWS](https://repost.aws/knowledge-center/error-access-service).

После активации очистите текущую настройку и перезапустите процесс.

Чтобы узнать, как очистить текущую настройку, см. [Стек CloudFormation не завершился успешно. Я исправил проблему. Как очистить текущую настройку и начать заново?](#clean-setup)

Причины сбоев развертывания CloudFormation -- ошибки 404 или 400. Что делать?

Пожалуйста, свяжитесь с нами по адресу `awscloudmonitoring-preview@dynatrace.com` или откройте тикет поддержки Dynatrace, предоставив описание ошибок.

Стек CloudFormation не завершился успешно. Я исправил проблему. Как очистить текущую настройку и начать заново?

В консоли AWS CloudFormation удалите основной стек Dynatrace. Имя основного стека соответствует имени подключения, в нашем примере `MyEastProd3Account`. Следуйте [руководству AWS по удалению стеков](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html).

После полного удаления стека и его вложенных стеков

1. В Dynatrace перейдите в ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** > **Cloud and virtualization** > **AWS (Preview)**.
2. Найдите и выберите меню действий подключения справа.
3. Выберите **Delete**.
4. Теперь вы можете запустить мастер и создать новое подключение.

Не все созданные ресурсы правильно помечены тегами в Dynatrace.

Даже если ваша организация требует тегирования через политики управления сервисами или IAM, некоторые ресурсы, созданные CloudFormation, не поддерживают распространение тегов. Подробности см. в [тегировании ресурсов AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).

Я включил push-прием логов через Firehose, но не могу найти записи логов в Dynatrace.

Просмотрев вкладку **Destination error logs** (консоль AWS Firehose), если вы получаете это сообщение:

`Delivery to the endpoint was unsuccessful. See Troubleshooting HTTP Endpoints in the Firehose documentation for more information. Response received with status code. 403: "requestId":"xxxx,"errorMessage":"The authorization token does not provide the necessary permissions. details: missing_scopes=[data-acquisition:logs:ingest]`

Проверьте, что

1. Токену платформы для приема назначена правильная область разрешений (`data-acquisition:logs:ingest`).
2. Сервисному пользователю Dynatrace, связанному с токеном, также назначена та же область разрешений токена (`data-acquisition:logs:ingest`).
3. Токен платформы для приема не истек и не был удален.
4. Сервисный пользователь не был удален.
5. Область среды токена платформы настроена на правильную среду Dynatrace.

При создании токена платформы, почему опция "сервисный пользователь" неактивна?

Ваш IAM-пользователь может не иметь разрешения на создание токенов платформы для (существующих) сервисных пользователей. Свяжитесь с администратором Dynatrace, чтобы узнать, были ли выполнены [предварительные требования](#prerequisitesuisites). В этом случае необходимо предоставить [определенную область разрешений](../../../manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens.md#allow-users-to-generate-platform-tokens-against-service-users "Создание персонализированных токенов платформы для доступа к сервисам Dynatrace через API в контексте вашего пользователя.").

## Поделитесь отзывом

Процесс подключения -- это развивающаяся основная функция продукта. Мы постоянно работаем над сбором отзывов.

В период предварительного доступа мы будем обращаться к вам за отзывами. Мы высоко ценим вашу готовность поделиться любыми предложениями.
Вы также можете поделиться отзывом на нашем [специальном канале сообщества Dynatrace](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-new-Cloud-Platform-Monitoring-PREVIEWS/m-p/286886/thread-id/4853#M4853)