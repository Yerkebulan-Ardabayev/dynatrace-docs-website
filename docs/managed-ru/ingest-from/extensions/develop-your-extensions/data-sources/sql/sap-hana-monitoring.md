---
title: Настройка мониторинга базы данных SAP Hana
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/sap-hana-monitoring
---

# Настройка мониторинга базы данных SAP Hana

# Настройка мониторинга базы данных SAP Hana

* Справочник
* 2 мин чтения
* Обновлено 09 апр. 2026

После определения области действия конфигурации нужно указать следующее:

* базы данных, из которых собираются данные
* ActiveGates для выполнения расширения и подключения к устройствам

## Пример payload

Пример payload для активации расширения SAP Hana:

```
[



{



"value": {



"enabled": true,



"description": "My SAP Hana extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlHanaRemote": {



"endpoints": [



{



"host": "hanahost",



"port": 1521,



"authentication": {



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

Удобочитаемое описание особенностей данной конфигурации мониторинга.

### Version

Версия данной конфигурации мониторинга. Учтите, что одно расширение может запускать несколько конфигураций мониторинга.

### Feature sets

Добавьте список feature sets для мониторинга. Чтобы включить в отчёт все feature sets, добавьте `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

В разделе `sqlHanaRemote` можно задать до 20 000 endpoints в рамках одной конфигурации мониторинга.

```
"sqlHanaRemote": {



"endpoints": [



{



"host": "hanahost",



"port": 1521,



"authentication": {



"username": "user",



"password": "password"



}



}



]



}
```

### Authentication

Данные аутентификации, передаваемые Dynatrace API при активации конфигурации мониторинга, обфусцируются, и извлечь их невозможно.

#### Credential vault

Тип аутентификации credential vault обеспечивает более безопасный подход к работе с расширениями благодаря защищённому хранению и управлению учётными данными пользователя. Для использования этого типа нужно быть владельцем учётных данных и иметь credential vault, отвечающий следующим критериям:

* **Credential type**: User and password для Basic Authentication, а также имя пользователя и Programmatic Access Token (PAT) для аутентификации через Programmatic Access Token (PAT)
* **Credential scope**: Synthetic (при использовании внешнего vault) и Extension, области аутентификации включены
* **Owner access only** включён только для владельцев учётных данных

```
"authentication": {



"scheme": "basic",



"useCredentialVault": "true",



"skipVerifyHttps": false,



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

Если SSL включён и цепочка сертификатов сервера поддаётся публичной проверке (например, выдана Azure или другими широко известными CA), создавать truststore вручную не нужно. Система автоматически будет доверять сертификату сервера на основании доверенных CA в окружении.

Однако если нужно использовать локальный truststore для сертификатов, не распознаваемых глобально, или в целях дополнительной безопасности:

1. В директории `userdata` на ActiveGates, запускающих SQL data source, вручную создайте PKCS12 truststore с именем `sqlds_truststore` и паролем `sqlds_truststore`.

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

Клиентские сертификаты для SQL data sources не поддерживаются. Для безопасной аутентификации используйте basic authentication с включённым SSL. Подробнее см. [Authentication](#authentication).

### Scope

Каждому хосту ActiveGate, запускающему расширение, нужен корневой сертификат для подтверждения подлинности расширения. Подробнее см. [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").

Scope, это группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы запустит данную конфигурацию мониторинга. Если планируется использовать один ActiveGate, назначьте его в отдельную группу. Назначить ActiveGate в группу можно во время или после установки. Подробнее см. [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` на фактическое имя.

## SAP Hana JDBC Driver

Для источника данных SAP Hana нужно разместить драйвер SAP Hana JDBC версии 2.14.x в Dynatrace Extension Framework 2.0.

Чтобы задать сервер базы данных SAP Hana, поместите файл `ngdbc.jar` в следующее расположение на хосте ActiveGate:

**Windows**: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\userdata\libs`  
**Linux**: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/libs/`