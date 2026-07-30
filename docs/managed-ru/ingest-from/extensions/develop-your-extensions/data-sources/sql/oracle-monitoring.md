---
title: Конфигурация мониторинга Oracle Database
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring
---

# Конфигурация мониторинга Oracle Database

# Конфигурация мониторинга Oracle Database

* Справочник
* 5 мин чтения
* Обновлено 09 апр. 2026

После определения области конфигурации нужно выбрать базы данных, из которых требуется собирать данные, и определить ActiveGate, которые будут выполнять расширение и подключаться к устройствам.

Убедитесь, что все ActiveGate из группы ActiveGate, которую планируется определить как область действия, могут подключаться к соответствующему источнику данных. Назначить ActiveGate в группу можно во время или после установки. Подробнее см. [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Конфигурация мониторинга, это JSON payload, определяющий параметры подключения, учётные данные и наборы функций, которые требуется отслеживать. Подробнее см. [Start monitoring](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

Пример payload для активации расширения Oracle SQL:

```
[



{



"value": {



"enabled": true,



"description": "My Oracle SQL extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlOracleRemote": {



"licenseAccepted": true,



"endpoints": [



{



"host": "sqlserver.org",



"port": 1521,



"databaseIdentifier": "serviceName",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



},



"serviceName": "some-serviceName"



"ssl": false



}



]



}



},



"scope": "ag_group-default"



}



]
```

Когда начальный YAML расширения готов, упакуйте его, подпишите и загрузите в среду Dynatrace. Подробнее см. [Manage extension lifecyle](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

Мастер активации расширений на основе Dynatrace Hub содержит динамически обновляемый JSON payload с конфигурацией мониторинга

Также можно воспользоваться Dynatrace API для загрузки схемы расширения, которая поможет создать JSON payload для конфигурации мониторинга.

Используйте конечную точку [GET an extension schema](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "View the schema of an extension the Dynatrace Extensions 2.0 API.").

Отправьте следующий запрос:

```
curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/{extension-name}/{extension-version}/schema" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Замените `{extension-name}` и `{extension-version}` значениями из файла YAML расширения. При успешном вызове возвращается схема JSON.

## Область действия

Обратите внимание: каждый хост ActiveGate, выполняющий расширение, должен иметь корневой сертификат для проверки подлинности расширения. Подробнее см. [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").

Область действия, это группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы будет выполнять данную конфигурацию мониторинга. Если планируется использовать один ActiveGate, назначьте его в выделенную группу. Назначить ActiveGate в группу можно во время или после установки. Подробнее см. [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.

## Версия

Версия данной конфигурации мониторинга. Одно расширение может выполнять несколько конфигураций мониторинга.

## Описание

Описание в произвольной форме, содержащее сведения об особенностях данной конфигурации мониторинга.

## Активация

Если установлено значение `true`, конфигурация активна и Dynatrace немедленно начинает мониторинг.

## Конечные точки

В разделе `SQLOracleRemote` одной конфигурации мониторинга можно определить до 20 000 конечных точек.

```
"sqlOracleRemote": {



"licenseAccepted": true,



"endpoints": [



{



"host": "sqlserver.org",



"port": 1521,



"databaseIdentifier": "serviceName",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



},



"serviceName": "some-serviceName"



"ssl": false



}



]



}



}
```

### Oracle JDBC Driver

Источник данных Oracle SQL требует наличия Oracle JDBC driver, распространяемого Dynatrace. Устанавливая свойство `licenceAccepted` в значение `true`, вы подтверждаете, что ознакомились и согласились с [лицензионным соглашением Dynatrace на распространение Oracle JDBC Driver﻿](https://dt-url.net/0s1n0pw9).

Для определения сервера Oracle Database добавьте следующие сведения в раздел `endpoints`:

* Хост
* Порт
* Идентификатор базы данных: `serviceName` или `sid`.
* Учётные данные для аутентификации

Версия Oracle JDBC driver, поставляемая с Extension Framework, это `ojdbc11`.

## Аутентификация

Данные аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, обфусцированы и не могут быть получены.

### Credential vault

Тип аутентификации credential vault обеспечивает более безопасный подход к использованию расширений за счёт надёжного хранения учётных данных пользователей и управления ими. Для использования этого типа необходимо быть владельцем учётных данных и иметь credential vault, соответствующий следующим критериям:

* **Credential type**, имя пользователя и пароль для Basic Authentication; имя пользователя и Programmatic Access Token (PAT) для аутентификации через Programmatic Access Token (PAT)
* **Credential scope**, для Synthetic (при использовании внешнего vault) и Extension должны быть включены области аутентификации
* **Owner access only** включён только для владельцев учётных данных

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

## Наборы функций

Добавьте список наборов функций, которые требуется отслеживать. Чтобы включить отчёт по всем наборам функций, укажите `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### TopN

Набор функций `topN` включает мониторинг наиболее ресурсоёмких запросов. Включён по умолчанию.

```
"featureSets": [



"topN"



]
```

Запросы topN группируются по сущности. Они отображаются на странице событий и на единой странице анализа для сущности Oracle server.

### Multitenancy

Набор функций `multitenancy` расширяет возможности мониторинга: выполняется запрос и получение сведений о Container Databases (CDB), Pluggable Databases (PDB) и сервисах, связанных с указанной базой данных в конфигурации мониторинга.

```
"featureSets": [



"multitenancy"



]
```

Пример навигации

Навигация по структуре сущностей Oracle

1. Откройте **Dashboards** и перейдите к дашборду **Oracle Database Overview**.
2. В разделе **Hosts** дашборда выберите хост в столбце **Oracle DB host**.
3. На странице **Oracle DB server** выберите CDB.

   ![Oracle Database multitenancy: CDBs](https://dt-cdn.net/images/cbds-1640-8c7671e235.png)

   Oracle Database multitenancy: CDBs
4. На странице **CDB** выберите pluggable database.

   ![Oracle Database multitenancy: Pluggable databases](https://dt-cdn.net/images/pluggable-databases-1611-2ce2521bef.png)

   Oracle Database multitenancy: Pluggable databases
5. На странице **PDB** отображается список сервисов.

   ![Oracle Database multitenancy: Services](https://dt-cdn.net/images/services-1621-d3ca42e060.png)

   Oracle Database multitenancy: Services

## Тайм-аут длительных запросов

ActiveGate version 1.275+

Добавьте параметр `long-running-query-timeout`, чтобы настроить продолжительность ожидания для длительных SQL-запросов. Параметр необязательный: если не задан, применяется тайм-аут по умолчанию в 10 секунд.

```
"vars": {



"long-running-query-timeout": null



}
```

## SSL

ActiveGate version 1.251+

Включите SSL, чтобы принудить источник данных проверять сертификат сервера и использовать SSL-шифрование вместо встроенного.

```
"ssl": true
```

#### Включение SSL без локального truststore

Если SSL включён и цепочка сертификатов сервера общедоступно верифицируема (например, выдана Azure или другими известными CA), создавать truststore вручную не нужно. Система автоматически доверяет сертификату сервера на основе доверенных CA среды.

Однако, если требуется использовать локальный truststore для сертификатов, не признанных глобально, или для дополнительных мер безопасности

1. В директории `userdata` на ActiveGate, выполняющих источник данных SQL, вручную создайте PKCS12 truststore с именем `sqlds_truststore` и паролем `sqlds_truststore`.

   Команда создания truststore с помощью keytool:

   ```
   keytool -genkey -keystore sqlds_truststore -storepass sqlds_truststore -keyalg DSA
   ```

   Расположение директории `userdata`:

   * Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata`
   * Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`
2. Добавьте в него сертификат сервера.

   Команда импорта сертификата с помощью keytool:

   ```
   keytool -import -keystore sqlds_truststore -file .\ora.crt -alias oracle
   ```

Клиентские сертификаты для источников данных SQL не поддерживаются. Для безопасной аутентификации используйте basic authentication с включённым SSL. Подробнее см. [Authentication](#authentication).

## Потребление ресурсов

Потребление ресурсов зависит от количества конечных точек Oracle. Первая конечная точка потребляет 110 МБ ОЗУ и 0,1–0,5% ЦПУ. Каждая последующая конечная точка потребляет 0,5–1,0 МБ ОЗУ и ~0,01% ЦПУ.

| Конечные точки | Среднее ЦПУ | Макс. ЦПУ | ОЗУ (МБ) | Хост (тип инстанса EC2) |
| --- | --- | --- | --- | --- |
| 100 | 0,6% | 0,6% (скачок в начале) | 160 | XS (`c5.large`) |
| 1 | 0,1% | 0,5% (скачок в начале) | 110 | XS (`c5.large`) |