---
title: Конфигурация мониторинга SAP Hana Database
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/sap-hana-monitoring
scraped: 2026-05-12T12:08:32.995551
---

# Конфигурация мониторинга SAP Hana Database

# Конфигурация мониторинга SAP Hana Database

* Справочник
* Чтение: 2 мин
* Обновлено 9 апреля 2026 г.

После определения области конфигурации необходимо указать следующее:

* Базы данных, из которых собираются данные
* ActiveGate для выполнения расширения и подключения к вашим устройствам

## Пример полезной нагрузки

Пример полезной нагрузки для активации расширения SAP Hana:

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

В одной конфигурации мониторинга в разделе `sqlHanaRemote` можно определить до 20 000 эндпоинтов.

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

Данные аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, скрываются, и получить их невозможно.

#### Хранилище учётных данных

Тип аутентификации через хранилище учётных данных обеспечивает более безопасный подход к использованию расширений за счёт надёжного хранения учётных данных пользователя и управления ими. Чтобы использовать этот способ, нужно быть владельцем учётных данных и иметь хранилище учётных данных, отвечающее следующим критериям:

* **Тип учётных данных**: имя пользователя и пароль
* **Область доступа учётных данных**: включены области Synthetic (при использовании внешнего хранилища) и Extension authentication
* Параметр **Owner access only** включён только для владельцев учётных данных

```
"authentication": {



"scheme": "basic",



"useCredentialVault": "true",



"skipVerifyHttps": false,



"credentialVaultId": "some-credential-vault-id"



}
```

### SSL

ActiveGate версии 1.269+

Включите SSL, чтобы источник данных проверял сертификат сервера и использовал шифрование SSL вместо встроенного.

```
"ssl": true
```

#### Включение SSL без локального хранилища доверия

Если SSL включён и цепочка сертификатов сервера проверяется публично (например, выдана Azure или другими известными удостоверяющими центрами), создавать хранилище доверия вручную не требуется. Система автоматически доверяет сертификату сервера на основе доверенных удостоверяющих центров в среде.

Однако если требуется использовать локальное хранилище доверия для сертификатов, не признанных глобально, или в целях дополнительной защиты:

1. В каталоге `userdata` на ActiveGate, выполняющих источник данных SQL, вручную создайте хранилище доверия PKCS12 с именем `sqlds_truststore` и паролем `sqlds_truststore`.

   Команда для создания хранилища доверия с помощью keytool:

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

Сертификат дополнительно проверяется по имени хоста: домен из сертификата должен совпадать с доменом эндпоинта, указанного в конфигурации мониторинга.

Включите этот параметр при подключении к базам данных с использованием пользовательских сертификатов.

```
"validateCertificates": true
```

Клиентские сертификаты не поддерживаются для источников данных SQL. Для безопасной аутентификации используйте базовую аутентификацию с включённым SSL. Подробные сведения см. в разделе [Аутентификация](#authentication).

### Scope

Обратите внимание, что каждому хосту ActiveGate, на котором выполняется расширение, нужен корневой сертификат для проверки подлинности расширения. Дополнительные сведения см. в разделе [Подписание расширения](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.").

Область доступа, это группа ActiveGate, которая будет выполнять расширение. Эту конфигурацию мониторинга запустит только один ActiveGate из группы. Если планируется использовать один ActiveGate, назначьте его в выделенную группу. Назначить ActiveGate в группу можно во время установки или после неё. Дополнительные сведения см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.

## SAP Hana JDBC Driver

Источник данных SAP Hana требует наличия драйвера SAP Hana JDBC версии 2.14.x в Dynatrace Extension Framework 2.0.

Чтобы задать сервер SAP Hana Database, поместите файл `ngdbc.jar` в следующее расположение на хосте ActiveGate:

**Windows**: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\userdata\libs`
**Linux**: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/libs/`