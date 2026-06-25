---
title: Конфигурация мониторинга базы данных Snowflake
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/snowflake-monitoring
scraped: 2026-05-12T12:08:41.332921
---

# Конфигурация мониторинга базы данных Snowflake

# Конфигурация мониторинга базы данных Snowflake

* Справочник
* Чтение: 2 мин
* Опубликовано 19 апреля 2023 г.

После определения области конфигурации необходимо указать следующее:

* Базы данных, из которых собираются данные
* ActiveGate для выполнения расширения и подключения к вашим устройствам

## Пример полезной нагрузки

Пример полезной нагрузки для активации расширения базы данных Snowflake:

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



"scheme": "basic",



"username": "admin",



"password": "password"



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

Понятное человеку описание особенностей этой конфигурации мониторинга.

### Version

Версия этой конфигурации мониторинга. Обратите внимание, что одно расширение может выполнять несколько конфигураций мониторинга.

### Feature sets

Добавьте список наборов функций, которые нужно отслеживать. Чтобы передавать все наборы функций, добавьте `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

В одной конфигурации мониторинга в разделе `SQLSnowflakeRemote` можно определить до 20 000 эндпоинтов.

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



"scheme": "basic",



"username": "admin",



"password": "password"



}



}



]



}
```

Чтобы задать сервер базы данных Snowflake, добавьте в раздел `endpoints` следующие сведения:

* Host
* Port
* Database name
* Warehouse
* Schema
* Учётные данные аутентификации

### Authentication

Данные аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, скрываются, и получить их невозможно.

#### Хранилище учётных данных

Тип аутентификации через хранилище учётных данных обеспечивает более безопасный подход к использованию расширений за счёт надёжного хранения учётных данных пользователя и управления ими. Чтобы использовать этот способ, нужно быть владельцем учётных данных и иметь хранилище учётных данных, отвечающее следующим критериям:

* **Тип учётных данных**: имя пользователя и пароль
* **Область доступа учётных данных**: включены области Synthetic (при использовании внешнего хранилища) и Extension authentication
* Параметр **Owner access only** включён только для владельцев учётных данных

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

### Scope

Обратите внимание, что каждому хосту ActiveGate, на котором выполняется расширение, нужен корневой сертификат для проверки подлинности расширения. Дополнительные сведения см. в разделе [Подписание расширения](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.").

Область доступа, это группа ActiveGate, которая будет выполнять расширение. Эту конфигурацию мониторинга запустит только один ActiveGate из группы. Если планируется использовать один ActiveGate, назначьте его в выделенную группу. Назначить ActiveGate в группу можно во время установки или после неё. Дополнительные сведения см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.