---
title: Настройка мониторинга PostgreSQL
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/postgresql-monitoring
---

# Настройка мониторинга PostgreSQL

# Настройка мониторинга PostgreSQL

* Reference
* 2 мин. на чтение
* Обновлено 23 июл. 2026

После определения области конфигурации нужно указать следующее:

* Базы данных, из которых собираются данные
* ActiveGates для выполнения расширения и подключения к устройствам

## Пример payload

Пример payload для активации расширения PostgreSQL:

```
[



{



"value": {



"enabled": true,



"description": "My PostgreSQL extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlPostgresRemote": {



"endpoints": [



{



"host": "psqlserver.org",



"port": 1521,



"databaseName": "dbname",



"authentication": {



"scheme": "basic",



"username": "user",



"password": "password"



},



"ssl": false



}



]



}



},



"scope": "ag_group-default"



}



]
```

## Параметры

### Enabled

Если установлено значение `true`, конфигурация активна и Dynatrace немедленно начинает мониторинг.

### Description

Описание в удобочитаемом виде для данной конфигурации мониторинга.

### Version

Версия данной конфигурации мониторинга. Одно расширение может выполнять несколько конфигураций мониторинга.

### Feature sets

Укажите список feature sets для мониторинга. Чтобы отслеживать все feature sets, добавьте `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

В одной конфигурации мониторинга в секции `sqlPostgresRemote` можно задать до 20 000 endpoints.

```
"sqlPostgresRemote": {



"endpoints": [



{



"host": "psqlserver.org",



"port": 1433,



"databaseName": "dbname",



"authentication": {



"scheme": "basic",



"username": "user",



"password": "password"



}



}



]



}
```

Чтобы задать сервер баз данных PostgreSQL, добавьте в секцию `endpoints` следующие сведения:

* Host
* Port
* Database name
* Authentication credentials

### Authentication

Данные аутентификации, переданные в Dynatrace API при активации конфигурации мониторинга, обфусцируются и недоступны для просмотра.

#### Basic

Базовая аутентификация требует только имени пользователя и пароля.

```
"authentication": {



"scheme": "basic",



"username": "username",



"password": "password"



}
```

#### AWS IAM

ActiveGate version 1.325+

Позволяет подключаться к базам данных Amazon RDS или Amazon Aurora с использованием аутентификации AWS IAM. Требует настроенного AWS Identity and Access Management (IAM) и доступной для хоста ActiveGate идентификационной записи AWS IAM (например, прикреплённой IAM role).

ActiveGate использует назначенную ему IAM role для аутентификации, что исключает необходимость хранить пароль базы данных. Указываются имя пользователя и регион (код региона AWS, например `eu-central-1`). Если в качестве значения региона указано `auto-detect` (ActiveGate version 1.331+), используется регион ActiveGate. В противном случае регион должен совпадать с регионом, в котором размещена база данных.

**Примечание**: аутентификация AWS IAM требует включённого SSL/TLS. Установите `ssl` в значение `true` в конфигурации endpoint. Подробнее см. [SSL](#ssl).

Настройка аутентификации AWS IAM:

1. Создайте IAM policy, разрешающую генерацию токенов для пользователя мониторинга (замените `<region>`, `<account-id>` и `<dbi-resource-id>` актуальными значениями).

   ```
   {



   "Version": "2012-10-17",



   "Statement": [



   {



   "Effect": "Allow",



   "Action": "rds-db:connect",



   "Resource": "arn:aws:rds-db:<region>:<account-id>:dbuser:<dbi-resource-id>/dynatrace"



   }



   ]



   }
   ```
2. Прикрепите policy к IAM role, назначенной хосту ActiveGate. Шаги зависят от способа размещения ActiveGate.

   EC2

   EKS

   Other

   ```
   aws iam attach-role-policy \



   --role-name <your-ec2-instance-role> \



   --policy-arn arn:aws:iam::<account-id>:policy/RdsIamConnectPolicy
   ```

   Используйте IAM Roles for Service Accounts (IRSA) для связи policy с service account пода ActiveGate:

   ```
   eksctl create iamserviceaccount \



   --name <activegate-service-account> \



   --namespace <activegate-namespace> \



   --cluster <your-cluster-name> \



   --attach-policy-arn arn:aws:iam::<account-id>:policy/RdsIamConnectPolicy \



   --approve
   ```

   Прикрепите policy к IAM role или идентификационной записи, связанной с хостом ActiveGate, через AWS Console или CLI. Роль должна быть принимаемой вычислительным ресурсом, на котором работает ActiveGate.
3. Настройте endpoint мониторинга с использованием схемы `identity_aws`.

   ```
   "authentication": {



   "scheme": "identity_aws",



   "username": "dynatrace",



   "region": "eu-central-1"



   }
   ```

#### Credential vault

Тип аутентификации credential vault обеспечивает более защищённый подход к использованию расширений за счёт безопасного хранения и управления учётными данными. Для использования нужно быть владельцем учётных данных и иметь credential vault, соответствующий следующим требованиям:

* **Credential type**: имя пользователя и пароль для Basic Authentication, имя пользователя и Programmatic Access Token (PAT) для аутентификации с помощью PAT
* **Credential scope**: включены области Synthetic (при использовании внешнего vault) и Extension authentication
* **Owner access only** включено только для владельцев учётных данных

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

ActiveGate version 1.269+

Включение SSL заставляет источник данных проверять сертификат сервера и использовать SSL-шифрование вместо встроенного.

```
"ssl": true
```

#### Enable SSL without a local truststore

Если SSL включён и цепочка сертификатов сервера публично верифицируема (например, выдана Azure или другими известными CA), создавать truststore вручную не требуется. Система автоматически доверяет сертификату сервера на основании доверенных CA в среде.

Однако если необходим локальный truststore для сертификатов, не признанных глобально, или для дополнительных мер безопасности

1. В каталоге `userdata` на ActiveGates, запускающих SQL data source, вручную создайте PKCS12 truststore с именем `sqlds_truststore` и паролем `sqlds_truststore`.

   Команда для создания truststore с помощью keytool:

   ```
   keytool -genkey -keystore sqlds_truststore -storepass sqlds_truststore -keyalg DSA
   ```

   Расположение каталога `userdata`:

   * Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata`
   * Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`
2. Добавьте в него сертификат сервера.

   Команда для импорта сертификата с помощью keytool:

   ```
   keytool -import -keystore sqlds_truststore -file .\ora.crt -alias oracle
   ```

#### Certificate validation mode

Параметр `certificatesValidation` управляет проверкой сертификата сервера при включённом SSL. Режим по умолчанию: `full`.

| Значение | Описание |
| --- | --- |
| `full` | Проверяет цепочку сертификатов и имя хоста. Домен в сертификате должен совпадать с именем хоста endpoint. |
| `skip_hostname_validation` | Проверяет цепочку сертификатов, но пропускает сопоставление имени хоста. Полезно, когда CN/SAN сертификата не совпадает с именем хоста. |
| `encryption_only` | Шифрует соединение без проверки сертификата. Использовать только в средах, где проверка сертификата невозможна. |

```
"certificatesValidation": "full"
```

Клиентские сертификаты не поддерживаются для SQL data sources. Для безопасной аутентификации используйте basic authentication с включённым SSL. Подробнее см. [Authentication](#authentication).

### Scope

Каждый хост ActiveGate, выполняющий расширение, должен иметь корневой сертификат для проверки подлинности расширения. Подробнее см. [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения для сертификатов с помощью Dynatrace Extensions Framework.").

Scope, это группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы запускает данную конфигурацию мониторинга. Если планируется использовать единственный ActiveGate, назначьте его в отдельную группу. Назначить ActiveGate в группу можно во время установки или после неё. Подробнее см. [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Общие сведения о группах ActiveGate.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.