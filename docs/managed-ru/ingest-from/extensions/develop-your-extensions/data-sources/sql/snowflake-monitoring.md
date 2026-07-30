---
title: Настройка мониторинга базы данных Snowflake
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/snowflake-monitoring
---

# Настройка мониторинга базы данных Snowflake

# Настройка мониторинга базы данных Snowflake

* Справочник
* 2 мин. чтения
* Обновлено 28 июля 2026 г.

После определения области действия конфигурации нужно указать следующее:

* Базы данных, из которых собираются данные
* ActiveGates для запуска расширения и подключения к устройствам

## Пример payload

Пример payload для активации расширения Snowflake Database:

```
[



{



"value": {



"enabled": true,



"description": "My SnowFlake DB extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlSnowflakeRemote": {



"endpoints": [



{



"host": "sqlserver.org",



"port": 1521,



"databaseName":"SNOWFLAKE_SAMPLE_DATA",



"warehouse":"yourwarehouse",



"schema":"yourschema",



"authentication": {



"scheme": "programmaticAccessToken",



"username": "your-snowflake-username",



"token": "your-programmatic-access-token"



}



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

Если задано значение `true`, конфигурация активна и Dynatrace немедленно начинает мониторинг.

### Description

Понятное человеку описание особенностей данной конфигурации мониторинга.

### Version

Версия данной конфигурации мониторинга. Одно расширение может запускать несколько конфигураций мониторинга.

### Feature sets

Укажите список feature sets для мониторинга. Чтобы включить все feature sets, добавьте `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

В одной конфигурации мониторинга в разделе `SQLSnowflakeRemote` можно задать до 20 000 endpoints.

```
"sqlSnowflakeRemote": {



"endpoints": [



{



"host": "your-snowflake.com",



"port": 1521,



"databaseName":"SNOWFLAKE_SAMPLE_DATA",



"warehouse":"yourwarehouse",



"schema":"yourschema",



"authentication": {



"scheme": "programmaticAccessToken",



"username": "your-snowflake-username",



"token": "your-programmatic-access-token"



}



}



]



}
```

Для определения сервера Snowflake Database укажите следующие данные в разделе `endpoints`:

* Host
* Port
* Database name
* Warehouse
* Schema
* Authentication credentials

### Authentication

Данные аутентификации, переданные в Dynatrace API при активации конфигурации мониторинга, обфусцированы и их невозможно извлечь.

#### Programmatic Access Token (PAT)

Используйте Programmatic Access Tokens для более безопасной аутентификации:

```
"authentication": {



"scheme": "programmaticAccessToken",



"username": "your-snowflake-username",



"token": "your-programmatic-access-token"



}
```

#### Credential vault

Тип аутентификации credential vault обеспечивает более безопасный подход к использованию расширений за счёт надёжного хранения и управления учётными данными. Для использования необходимо быть владельцем учётных данных и иметь credential vault, соответствующий следующим критериям:

* **Credential type**, имя пользователя и пароль для Basic Authentication, а также имя пользователя и Programmatic Access Token (PAT) для аутентификации по Programmatic Access Token (PAT)
* **Credential scope**, Synthetic (при использовании внешнего vault) и Extension, scope аутентификации включены
* **Owner access only** включён только для владельцев учётных данных

```
"authentication": {



"scheme": "programmaticAccessToken",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

Basic authentication (устарел)

Basic authentication устарел. Вместо него используйте аутентификацию по Programmatic Access Token (PAT).

```
"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



}
```

### Scope

Каждый хост ActiveGate, на котором выполняется расширение, должен иметь корневой сертификат для проверки подлинности расширения. Подробнее: [Подписание расширения](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения, а также настроить права на сертификаты с помощью Dynatrace Extensions Framework.").

Scope, это группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы запустит данную конфигурацию мониторинга. При использовании одного ActiveGate назначьте его в отдельную группу. Назначить ActiveGate в группу можно во время установки или после неё. Подробнее: [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Основные концепции групп ActiveGate.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.