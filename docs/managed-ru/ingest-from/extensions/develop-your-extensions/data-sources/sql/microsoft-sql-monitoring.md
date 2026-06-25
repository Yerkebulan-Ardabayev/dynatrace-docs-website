---
title: Конфигурация мониторинга Microsoft SQL Server
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring
scraped: 2026-05-12T12:08:26.392671
---

# Конфигурация мониторинга Microsoft SQL Server

# Конфигурация мониторинга Microsoft SQL Server

* Справочник
* Чтение: 3 мин
* Обновлено 9 апреля 2026 г.

После определения области конфигурации необходимо указать следующее:

* Базы данных, из которых собираются данные
* ActiveGate для выполнения расширения и подключения к вашим устройствам

## Пример полезной нагрузки

Пример полезной нагрузки для активации расширения Microsoft SQL:

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

Понятное человеку описание особенностей этой конфигурации мониторинга.

### Version

Версия этой конфигурации мониторинга. Обратите внимание, что одно расширение может выполнять несколько конфигураций мониторинга.

### Endpoints

В одной конфигурации мониторинга в разделе `sqlServerRemote` можно определить до 20 000 эндпоинтов.

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

Чтобы задать Microsoft SQL Server, добавьте в раздел `endpoints` следующие сведения:

* Host
* Port
* Instance name
* Database name
* Учётные данные аутентификации

### Authentication

Данные аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, скрываются, и получить их невозможно.

#### Базовая аутентификация

Базовая аутентификация требует только имя пользователя и пароль.

```
"authentication": {



"scheme": "basic",



"username": "username",



"password": "password",



}
```

#### Kerberos

Требует настройки домена Active Directory. Позволяет подключиться к базе данных, указав доменное имя пользователя, пароль, центр распределения ключей (KDC) и область.

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

Требует настройки домена Active Directory. Позволяет подключиться к базе данных, указав доменное имя пользователя, доменный пароль и, при необходимости, домен.

```
"authentication": {



"scheme": "ntlm",



"username": "username",



"password": "password",



"domain": "some-domain-name"



}
```

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

### SSL

ActiveGate версии 1.251+

Включите SSL, чтобы источник данных проверял сертификат сервера и использовал шифрование SSL вместо встроенного шифрования.

```
"ssl": true
```

#### Включение SSL без локального хранилища доверенных сертификатов

Если SSL включён и цепочка сертификатов сервера является публично проверяемой (например, выдана Azure или другими известными центрами сертификации), создавать хранилище доверенных сертификатов вручную не нужно. Система автоматически доверяет сертификату сервера на основе доверенных центров сертификации в среде.

Однако если требуется использовать локальное хранилище доверенных сертификатов для сертификатов, не признанных глобально, или для дополнительных мер безопасности:

1. В каталоге `userdata` на хостах ActiveGate, выполняющих источник данных SQL, вручную создайте хранилище доверенных сертификатов PKCS12 с именем `sqlds_truststore` и паролем `sqlds_truststore`.

   Команда для создания хранилища доверенных сертификатов с помощью keytool:

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

#### Проверка SSL-сертификатов

ActiveGate версии 1.269+

Сертификат дополнительно проверяется по имени хоста, что означает: домен из сертификата должен совпадать с доменом эндпоинта, указанного в конфигурации мониторинга.

Включите этот параметр при подключении к базам данных с использованием пользовательских сертификатов.

```
"validateCertificates": true
```

Клиентские сертификаты не поддерживаются для источников данных SQL. Для безопасной аутентификации используйте базовую аутентификацию с включённым SSL. Подробнее см. в разделе [Аутентификация](#authentication).

### Scope

Обратите внимание, что каждому хосту ActiveGate, на котором выполняется расширение, нужен корневой сертификат для проверки подлинности расширения. Дополнительные сведения см. в разделе [Подписание расширения](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.").

Область доступа, это группа ActiveGate, которая будет выполнять расширение. Эту конфигурацию мониторинга запустит только один ActiveGate из группы. Если планируется использовать один ActiveGate, назначьте его в выделенную группу. Назначить ActiveGate в группу можно во время установки или после неё. Дополнительные сведения см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.