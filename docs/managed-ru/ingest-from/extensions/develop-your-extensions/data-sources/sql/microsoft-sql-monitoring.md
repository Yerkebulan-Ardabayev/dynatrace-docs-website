---
title: Настройка мониторинга Microsoft SQL Server
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring
---

# Настройка мониторинга Microsoft SQL Server

# Настройка мониторинга Microsoft SQL Server

* Reference
* 3 минуты чтения
* Обновлено 30 июня 2026 г.

После определения области конфигурации нужно указать следующее:

* Базы данных, из которых будут собираться данные
* ActiveGates для выполнения расширения и подключения к устройствам

## Пример payload

Пример payload для активации расширения Microsoft SQL:

```
{



"value": {



"enabled": true,



"description": "My Microsoft SQL extension",



"version": "1.0.1",



"sqlServerRemote": {



"endpoints": [



{



"host": "localhost",



"port": 1521,



"instanceName": "some-instanceName",



"databaseName": "some-databaseName",



"authentication": {



"scheme": "basic",



"username": "username",



"password": "password"



},



"ssl": false



}



]



}



},



"scope": "ag_group-default"



}
```

## Параметры

### Enabled

Если задано значение `true`, конфигурация активна и Dynatrace немедленно начинает мониторинг.

### Description

Понятное человеку описание особенностей данной конфигурации мониторинга.

### Version

Версия данной конфигурации мониторинга. Одно расширение может выполнять несколько конфигураций мониторинга.

### Endpoints

В разделе `sqlServerRemote` можно определить до 20 000 endpoints в рамках одной конфигурации мониторинга.

```
"sqlServerRemote": {



"endpoints": [



{



"host": "sqlserver.org",



"port": 1433,



"instanceName": "instance",



"databaseName": "database",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



}



}



]



}
```

Чтобы определить Microsoft SQL Server, добавьте в раздел `endpoints` следующие данные:

* Host
* Port
* Instance name
* Database name
* Учётные данные для аутентификации

### Authentication

Данные аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, скрываются и извлечь их невозможно.

#### Basic

Basic-аутентификация требует только имя пользователя и пароль.

```
"authentication": {



"scheme": "basic",



"username": "username",



"password": "password",



}
```

#### Kerberos

Требует настроенного домена Active Directory. Позволяет подключаться к базе данных, указав доменное имя пользователя, пароль, Key Distribution Center (KDC) и realm.

```
"authentication": {



"scheme": "kerberos",



"username": "username",



"password": "password",



"realm": "realm",



"kdc": "kdc"



}
```

#### NTLM

Только Windows

Требует настроенного домена Active Directory. Позволяет подключаться к базе данных, указав доменное имя пользователя, доменный пароль и, при необходимости, домен.

```
"authentication": {



"scheme": "ntlm",



"username": "username",



"password": "password",



"domain": "some-domain-name"



}
```

#### Credential vault

Тип аутентификации через credential vault обеспечивает более безопасный подход к использованию расширений: учётные данные хранятся и управляются безопасно. Для этого нужно быть владельцем учётных данных и иметь credential vault, отвечающий следующим критериям:

* **Credential type**: имя пользователя и пароль в случае Basic Authentication, а также имя пользователя и Programmatic Access Token (PAT) в случае аутентификации через Programmatic Access Token (PAT)
* **Credential scope**: Synthetic (при использовании внешнего vault) и Extension, области аутентификации включены
* **Owner access only** включён только для владельцев учётных данных

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

ActiveGate version 1.251+

Включите SSL, чтобы источник данных проверял сертификат сервера и использовал SSL-шифрование вместо собственного шифрования.

```
"ssl": true
```

#### Включение SSL без локального truststore

Если SSL включён и цепочка сертификатов сервера общедоступно проверяема (например, выдана Azure или другими широко известными CA), вручную создавать truststore не нужно. Система автоматически доверяет сертификату сервера на основании доверенных CA в среде.

Если же нужно использовать локальный truststore для сертификатов, не признанных глобально, или в целях дополнительной безопасности:

1. В директории `userdata` на ActiveGates, выполняющих SQL data source, вручную создайте PKCS12 truststore с именем `sqlds_truststore` и паролем `sqlds_truststore`.

   Команда для создания truststore с помощью keytool:

   ```
   keytool -genkey -keystore sqlds_truststore -storepass sqlds_truststore -keyalg DSA
   ```

   Расположение директории `userdata`:

   * Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata`
   * Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`
2. Добавьте сертификат сервера в truststore.

   Команда для импорта сертификата с помощью keytool:

   ```
   keytool -import -keystore sqlds_truststore -file .\ora.crt -alias oracle
   ```

#### Проверка SSL-сертификатов

ActiveGate version 1.269+

Сертификат также проверяется по имени хоста. Это означает, что домен в сертификате должен совпадать с доменом endpoint, указанным в конфигурации мониторинга.

Включайте эту опцию при подключении к базам данных с использованием пользовательских сертификатов.

```
"validateCertificates": true
```

Клиентские сертификаты для SQL data sources не поддерживаются. Для безопасной аутентификации используйте basic-аутентификацию с включённым SSL. Подробнее: [Authentication](#authentication).

### Scope

Каждый хост ActiveGate, выполняющий расширение, должен иметь корневой сертификат для проверки подлинности расширения. Подробнее: [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения, а также настроить права доступа к сертификатам с помощью Dynatrace Extensions Framework.").

Scope, это группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы будет выполнять данную конфигурацию мониторинга. Если планируется использовать один ActiveGate, назначьте его в отдельную группу. Назначить ActiveGate в группу можно во время или после установки. Подробнее: [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Ознакомьтесь с базовыми концепциями групп ActiveGate.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.