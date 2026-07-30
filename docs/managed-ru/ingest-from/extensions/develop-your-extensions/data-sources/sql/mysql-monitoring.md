---
title: Конфигурация мониторинга MySQL
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/mysql-monitoring
---

# Конфигурация мониторинга MySQL

# Конфигурация мониторинга MySQL

* Справочник
* Чтение: 2 мин
* Обновлено 23 июля 2026 г.

После определения области конфигурации нужно указать следующее:

* Базы данных, из которых собираются данные
* ActiveGates для выполнения расширения и подключения к устройствам

## Пример payload

Пример payload для активации расширения MySQL:

```
[



{



"value": {



"enabled": true,



"description": "My MySQL extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlMySqlRemote": {



"endpoints": [



{



"host": "mysqlhost",



"port": 3306,



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

Описание особенностей данной конфигурации мониторинга в удобочитаемом виде.

### Version

Версия данной конфигурации мониторинга. Одно расширение может выполнять несколько конфигураций мониторинга.

### Feature sets

Добавьте список feature sets, которые нужно мониторить. Чтобы охватить все feature sets, укажите `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

В разделе `sqlMySqlRemote` можно определить до 20 000 endpoint'ов в рамках одной конфигурации мониторинга.

```
"sqlMySqlRemote": {



"endpoints": [



{



"host": "sqlserver.org",



"port": 1521,



"databaseName": "dbname",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



}



}



]



}
```

Чтобы задать сервер MySQL Database, добавьте следующие данные в раздел `endpoints`:

* Host
* Port
* Database name
* Authentication credentials

### Authentication

Данные аутентификации, переданные в Dynatrace API при активации конфигурации мониторинга, обфусцируются, и восстановить их невозможно.

#### Basic

Для Basic authentication требуются только имя пользователя и пароль.

```
"authentication": {



"scheme": "basic",



"username": "username",



"password": "password"



}
```

#### AWS IAM

ActiveGate версии 1.325+

Позволяет подключаться к базам данных Amazon RDS или Amazon Aurora с помощью аутентификации AWS IAM. Требует настроенного AWS Identity and Access Management (IAM) и IAM-идентификационной записи, доступной на хосте ActiveGate (например, подключённой IAM-роли).

ActiveGate использует назначенную ему IAM-роль для аутентификации, поэтому хранить пароль базы данных не нужно. Необходимо указать имя пользователя и регион (код региона AWS, например `eu-central-1`). Если в качестве значения региона указано `auto-detect` (ActiveGate версии 1.331+), используется регион самого ActiveGate. В противном случае регион должен совпадать с регионом размещения базы данных.

**Примечание**: аутентификация AWS IAM требует включения SSL/TLS. Установите `ssl` в значение `true` в конфигурации endpoint. Подробнее: [SSL](#ssl).

Настройка аутентификации AWS IAM:

1. Создайте IAM policy, разрешающую генерацию токенов для пользователя мониторинга (замените `<region>`, `<account-id>` и `<dbi-resource-id>` своими значениями).

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
2. Прикрепите policy к IAM-роли, назначенной хосту ActiveGate. Шаги зависят от способа размещения ActiveGate.

   EC2

   EKS

   Other

   ```
   aws iam attach-role-policy \



   --role-name <your-ec2-instance-role> \



   --policy-arn arn:aws:iam::<account-id>:policy/RdsIamConnectPolicy
   ```

   Используйте IAM Roles for Service Accounts (IRSA) для связки policy с сервисным аккаунтом пода ActiveGate:

   ```
   eksctl create iamserviceaccount \



   --name <activegate-service-account> \



   --namespace <activegate-namespace> \



   --cluster <your-cluster-name> \



   --attach-policy-arn arn:aws:iam::<account-id>:policy/RdsIamConnectPolicy \



   --approve
   ```

   Прикрепите policy к IAM-роли или идентификационной записи, связанной с хостом ActiveGate, через AWS Console или CLI. Роль должна быть доступна для принятия вычислительным ресурсом, на котором работает ActiveGate.
3. Настройте endpoint мониторинга со схемой `identity_aws`.

   ```
   "authentication": {



   "scheme": "identity_aws",



   "username": "dynatrace",



   "region": "eu-central-1"



   }
   ```

#### Credential vault

Тип аутентификации credential vault обеспечивает более безопасный подход к работе с расширениями за счёт защищённого хранения учётных данных и управления ими. Для его использования нужно быть владельцем учётных данных и иметь credential vault, отвечающий следующим требованиям:

* **Credential type**, «User and password» для Basic Authentication и имя пользователя с Programmatic Access Token (PAT) для аутентификации по PAT
* **Credential scope**: включены области Synthetic (при использовании внешнего vault) и Extension authentication
* **Owner access only** включён только для владельцев учётных данных

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

ActiveGate версии 1.269+

Включите SSL, чтобы источник данных проверял сертификат сервера и использовал SSL-шифрование вместо встроенного шифрования.

```
"ssl": true
```

#### Enable SSL without a local truststore

Если SSL включён и цепочка сертификатов сервера публично верифицируема (например, выдана Azure или другими известными CA), создавать truststore вручную не нужно. Система автоматически доверяет сертификату сервера на основе доверенных CA окружения.

Однако если требуется локальный truststore для сертификатов, не признанных глобально, или в целях дополнительной безопасности:

1. В директории `userdata` на ActiveGates, выполняющих источник данных SQL, создайте вручную PKCS12-хранилище с именем `sqlds_truststore` и паролем `sqlds_truststore`.

   Команда для создания truststore с помощью keytool:

   ```
   keytool -genkey -keystore sqlds_truststore -storepass sqlds_truststore -keyalg DSA
   ```

   Расположение директории `userdata`:

   * Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata`
   * Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`
2. Добавьте в него сертификат сервера.

   Команда для импорта сертификата с помощью keytool:

   ```
   keytool -import -keystore sqlds_truststore -file .\ora.crt -alias oracle
   ```

#### Certificate validation mode

Используйте `certificatesValidation` для управления проверкой сертификата сервера при включённом SSL. Режим по умолчанию: `full`.

| Значение | Описание |
| --- | --- |
| `full` | Проверяет цепочку сертификатов и имя хоста. Домен в сертификате должен совпадать с именем хоста endpoint. |
| `skip_hostname_validation` | Проверяет цепочку сертификатов, но пропускает проверку имени хоста. Удобно, когда CN/SAN сертификата не совпадает с именем хоста. |
| `encryption_only` | Шифрует соединение без проверки сертификата. Использовать только в окружениях, где проверка сертификата невозможна. |

```
"certificatesValidation": "full"
```

Клиентские сертификаты не поддерживаются для источников данных SQL. Для безопасной аутентификации используйте Basic Authentication с включённым SSL. Подробнее: [Authentication](#authentication).

### Scope

На каждом хосте ActiveGate, выполняющем расширение, должен быть корневой сертификат для проверки подлинности расширения. Подробнее: [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").

Область, это группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы запускает данную конфигурацию мониторинга. Если планируется использовать единственный ActiveGate, назначьте его в выделенную группу. Назначить ActiveGate в группу можно во время или после установки. Подробнее: [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.