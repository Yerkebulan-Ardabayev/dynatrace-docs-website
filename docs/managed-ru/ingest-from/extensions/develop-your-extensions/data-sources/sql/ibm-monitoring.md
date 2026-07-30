---
title: Настройка мониторинга IBM Database
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring
---

# Настройка мониторинга IBM Database

# Настройка мониторинга IBM Database

* Reference
* 2-min read
* Updated on Apr 09, 2026

После определения области конфигурации нужно указать следующее:

* Базы данных, из которых будут собираться данные
* ActiveGate, которые будут выполнять расширение и подключаться к устройствам

## Пример payload

Пример payload для активации расширения IBM DB2:

```
[



{



"value": {



"enabled": true,



"description": "My IBM extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlDb2Remote": {



"endpoints": [



{



"host": "db2host",



"port": 1521,



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



},



"databaseName": "dbname",



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

Описание особенностей данной конфигурации мониторинга в читаемом виде.

### Version

Версия данной конфигурации мониторинга. Одно расширение может выполнять несколько конфигураций мониторинга.

### Feature sets

Укажите список feature sets для мониторинга. Чтобы включить отчётность по всем feature sets, добавьте `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

В разделе `sqlDb2Remote` можно задать до 20 000 endpoint'ов в одной конфигурации мониторинга.

```
"sqlDb2Remote": {



"endpoints": [



{



"host": "db2host",



"port": 1433,



"authentication": {



"scheme": "basic",



"username": "user",



"password": "password"



},



"databaseName": "dbname",



}



]



}
```

Чтобы определить сервер IBM Database, укажите следующие сведения в разделе `endpoints`:

* Host
* Port
* Учётные данные для аутентификации
* Имя базы данных

### Authentication

Данные аутентификации, переданные в Dynatrace API при активации конфигурации мониторинга, обфусцированы и не поддаются извлечению.

#### Credential vault

Тип аутентификации credential vault обеспечивает более безопасный подход к использованию расширений: учётные данные хранятся и управляются централизованно. Для работы нужно быть владельцем учётных данных и иметь credential vault, соответствующий следующим критериям:

* **Credential type**, пользователь и пароль при Basic Authentication, а также имя пользователя и Programmatic Access Token (PAT) при аутентификации через Programmatic Access Token (PAT)
* **Credential scope**, Synthetic (при использовании внешнего vault) с включёнными областями аутентификации Synthetic и Extension
* **Owner access only** включён только для владельцев учётных данных

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

ActiveGate version 1.269+

Включите SSL, чтобы источник данных проверял сертификат сервера и использовал шифрование SSL вместо встроенного.

```
"ssl": true
```

#### Включение SSL без локального truststore

Если SSL включён и цепочка сертификатов сервера публично верифицируема (например, выдана Azure или другими широко известными CA), создавать truststore вручную не нужно. Система автоматически доверяет сертификату сервера на основе доверенных CA в среде.

Если нужно использовать локальный truststore для сертификатов, не признанных глобально, или для дополнительных мер безопасности:

1. В директории `userdata` на ActiveGate, выполняющих SQL data source, вручную создайте PKCS12 truststore с именем `sqlds_truststore` и паролем `sqlds_truststore`.

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

Клиентские сертификаты не поддерживаются для SQL data sources. Для безопасной аутентификации используйте basic authentication с включённым SSL. Подробнее см. [Authentication](#authentication).

### Scope

Каждый хост ActiveGate, выполняющий расширение, должен иметь корневой сертификат для проверки подлинности расширения. Подробнее см. [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").

Scope, это группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы запустит данную конфигурацию мониторинга. Если планируется использовать один ActiveGate, назначьте его в отдельную группу. Назначить ActiveGate в группу можно во время установки или после неё. Подробнее см. [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` на фактическое имя.