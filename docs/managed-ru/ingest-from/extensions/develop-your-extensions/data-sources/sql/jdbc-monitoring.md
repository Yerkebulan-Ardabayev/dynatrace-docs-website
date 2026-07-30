---
title: Настройка мониторинга JDBC
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring
---

# Настройка мониторинга JDBC

# Настройка мониторинга JDBC

* Практическое руководство
* Чтение 3 мин
* Обновлено 09 апр. 2026

Dynatrace Extensions SQL data source позволяет запрашивать любую базу данных, поддерживающую подключение через JDBC-драйвер, в дополнение ко всем поставщикам баз данных, поддерживаемым по умолчанию. Для таких баз данных требуются дополнительные шаги.

## Предварительные требования

Поддерживаются драйверы на базе JDBC 4.0+.

## Загрузка JDBC-драйвера на ActiveGate

Нужно предоставить драйвер выбранного поставщика базы данных, чтобы ActiveGate, запускающий расширение, мог подключиться к базе данных.

Пример для MariaDB

Для MariaDB драйвер можно получить на странице [Download MariaDB﻿](https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector).

Скачайте коннектор Java 8+, независимый от платформы, а именно файл `mariadb-java-client-3.5.0.jar`.

Загрузите JDBC-драйвер на ActiveGate, принадлежащий группе, предназначенной для запуска расширения:

**Windows**: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\userdata\libs`  
**Linux**: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/libs/`

Убедитесь, что пользователь `dtuserag` имеет доступ к драйверу на чтение. Например, для Linux задайте `CHMOD` значение `775`.

## Конфигурация мониторинга

После определения области конфигурации нужно указать следующее:

* Базы данных, из которых нужно собирать данные, и их реквизиты аутентификации
* ActiveGates для выполнения расширения и подключения к устройствам. Таким ActiveGates необходим соответствующий [загруженный JDBC-драйвер](#upload).

Пример payload для активации JDBC-расширения:

```
[



{



"value": {



"enabled": true,



"description": "My JDBC extension",



"version": "0.0.1",



"featureSets": [



"statements"



],



"jdbcRemote": {



"endpoints": [



{



"host": "193.36.194.170",



"port": 3306,



"connectionString": "jdbc:mariadb://193.36.194.170/mysql",



"authentication": {



"scheme": "basic",



"useCredentialVault": false,



"username": "user",



"password": "password"



}



}



]



}



},



"scope": "ag_group-someAgGroup"



}



]
```

Обратите внимание: нужно указать и endpoint (host и port), и соответствующую строку подключения.

Параметры безопасности

Синтаксис строки подключения SQL по своей природе может раскрывать конфиденциальные данные, например учётные данные пользователя. По возможности не включайте секретные данные в строку подключения. Если строка подключения содержит конфиденциальные данные:

* Ограничьте доступ к конфигурации мониторинга JDBC на чтение и запись. Убедитесь, что только пользователи, допущенные к секрету, имеют доступ к конфигурациям на чтение и запись.
* В отличие от реквизитов аутентификации, строка подключения не хешируется. Просматривайте и редактируйте конфигурацию только в безопасной среде, недоступной для неавторизованных пользователей.

## Параметры

### Enabled

Если задано значение `true`, конфигурация активна и Dynatrace немедленно начинает мониторинг.

### Description

Метка конфигурации, содержащая базовое описание особенностей данной конфигурации мониторинга.

### Version

Версия данной конфигурации мониторинга.

### Feature sets

Укажите список feature sets, которые нужно отслеживать.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

В разделе `jdbcRemote` одной конфигурации мониторинга можно определить до 20 000 endpoints.

```
"jdbcRemote": {



"endpoints": [



{



"host": "jdbchost",



"port": 3306,



"connectionString": "jdbc:mariadb://193.36.194.170/mysql",



"authentication": {



"scheme": "basic",



"useCredentialVault": false,



"username": "admin",



"password": "password"



}



}



]



}
```

Чтобы определить JDBS Database server, добавьте следующие сведения в раздел `endpoints`:

* Host
* Port
* Connection string
* Authentication credentials

### Authentication

Реквизиты аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, обфусцируются и не поддаются восстановлению.

#### Credential vault

Тип аутентификации credential vault обеспечивает более безопасный подход к использованию расширений за счёт защищённого хранения учётных данных пользователей и управления ими. Для использования нужно быть владельцем учётных данных и иметь credential vault, соответствующий следующим критериям:

* **Credential type**: пользователь и пароль для Basic Authentication; имя пользователя и Programmatic Access Token (PAT) для аутентификации Programmatic Access Token (PAT)
* **Credential scope**: Synthetic (при использовании внешнего vault) и Extension, аутентификационные области включены
* **Owner access only** включён только для владельцев учётных данных

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

ActiveGate версии 1.295+

Включите SSL, чтобы data source проверял сертификат сервера и использовал SSL-шифрование вместо нативного.

```
"ssl": true
```

#### Включение SSL без локального truststore

Если SSL включён и цепочка сертификатов сервера публично верифицируема (например, выдана Azure или другими общеизвестными CA), создавать truststore вручную не нужно. Система автоматически доверяет сертификату сервера на основе доверенных CA в среде.

Однако если нужно использовать локальный truststore для сертификатов, не признанных глобально, или для дополнительных мер безопасности:

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

Клиентские сертификаты для SQL data sources не поддерживаются. Для безопасной аутентификации используйте basic authentication с включённым SSL. Подробности см. в разделе [Authentication](#authentication).

### Scope

Обратите внимание: каждому хосту ActiveGate, на котором запускается расширение, необходим корневой сертификат для проверки подлинности расширения. Подробнее см. [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").

Scope, это группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы будет запускать данную конфигурацию мониторинга. Если планируется использовать один ActiveGate, назначьте его в выделенную группу. Назначить ActiveGate группе можно во время или после установки. Подробнее см. [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.