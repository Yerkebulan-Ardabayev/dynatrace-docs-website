---
title: Конфигурация мониторинга Oracle Database
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring
scraped: 2026-05-12T12:08:28.508759
---

# Конфигурация мониторинга Oracle Database

# Конфигурация мониторинга Oracle Database

* Справочник
* Чтение: 5 мин
* Обновлено 9 апреля 2026 г.

После определения области конфигурации необходимо указать базы данных, из которых нужно собирать данные, и ActiveGate, которые будут выполнять расширение и подключаться к устройствам.

Убедитесь, что все ActiveGate из группы ActiveGate, определённой как область, могут подключиться к соответствующему источнику данных. Назначить ActiveGate в группу можно во время установки или после неё. Дополнительные сведения см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

Конфигурация мониторинга представляет собой JSON-полезную нагрузку, определяющую сведения о подключении, учётные данные и наборы функций для мониторинга. Подробные сведения см. в разделе [Запуск мониторинга](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

Пример полезной нагрузки для активации расширения Oracle SQL:

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

Когда начальный файл YAML расширения будет готов, упакуйте его, подпишите и загрузите в среду Dynatrace. Подробные сведения см. в разделе [Управление жизненным циклом расширения](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

Мастер активации расширений на основе Dynatrace Hub содержит динамически обновляемую JSON-полезную нагрузку с конфигурацией мониторинга.

Также можно использовать Dynatrace API для загрузки схемы расширения, которая поможет сформировать JSON-полезную нагрузку для конфигурации мониторинга.

Используйте эндпоинт [GET an extension schema](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "Просмотрите схему расширения с помощью Dynatrace Extensions 2.0 API.").

Выполните следующий запрос:

```
curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/{extension-name}/{extension-version}/schema" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Замените `{extension-name}` и `{extension-version}` значениями из YAML-файла расширения. При успешном вызове возвращается JSON-схема.

## Область доступа

Обратите внимание, что каждому хосту ActiveGate, на котором выполняется расширение, нужен корневой сертификат для проверки подлинности расширения. Дополнительные сведения см. в разделе [Подписание расширения](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.").

Область доступа, это группа ActiveGate, которая будет выполнять расширение. Эту конфигурацию мониторинга запустит только один ActiveGate из группы. Если планируется использовать один ActiveGate, назначьте его в выделенную группу. Назначить ActiveGate в группу можно во время установки или после неё. Дополнительные сведения см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").

При определении группы ActiveGate используйте следующий формат:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.

## Version

Версия этой конфигурации мониторинга. Обратите внимание, что одно расширение может выполнять несколько конфигураций мониторинга.

## Description

Понятное человеку описание особенностей этой конфигурации мониторинга.

## Enabled

Если задано значение `true`, конфигурация активна и Dynatrace немедленно начинает мониторинг.

## Endpoints

В одной конфигурации мониторинга в разделе `SQLOracleRemote` можно определить до 20 000 эндпоинтов.

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

Источник данных Oracle SQL требует наличия драйвера Oracle JDBC, распространяемого Dynatrace. Установив свойство `licenceAccepted` в значение `true`, вы подтверждаете, что ознакомились с [лицензионным соглашением Dynatrace на распространение Oracle JDBC Driver](https://dt-url.net/0s1n0pw9) и принимаете его.

Чтобы задать сервер Oracle Database, добавьте в раздел `endpoints` следующие сведения:

* Host
* Port
* Идентификатор базы данных: `serviceName` или `sid`.
* Учётные данные аутентификации

Версия драйвера Oracle JDBC, поставляемая с Extension Framework: `ojdbc11`.

## Authentication

Данные аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, скрываются, и получить их невозможно.

### Хранилище учётных данных

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

## Feature sets

Добавьте список наборов функций, которые нужно отслеживать. Чтобы передавать все наборы функций, добавьте `all`.

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

Это группирует запросы topN по сущности. Запросы отображаются на странице событий и на единой странице анализа для сущности Oracle-сервера.

### Multitenancy

Набор функций `multitenancy` расширяет возможности мониторинга путём запроса и получения сведений о контейнерных базах данных (CDB), подключаемых базах данных (PDB) и сервисах, связанных с указанной базой данных в конфигурации мониторинга.

```
"featureSets": [



"multitenancy"



]
```

Пример навигации

Для навигации по структуре сущностей Oracle:

1. Откройте **Dashboards** и откройте дашборд **Oracle Database Overview**.
2. В разделе **Hosts** дашборда выберите хост в столбце **Oracle DB host**.
3. На странице **Oracle DB server** выберите CDB.

   ![Oracle Database multitenancy: CDBs](https://dt-cdn.net/images/cbds-1640-8c7671e235.png)

   Oracle Database multitenancy: CDBs
4. На странице **CDB** выберите подключаемую базу данных.

   ![Oracle Database multitenancy: Pluggable databases](https://dt-cdn.net/images/pluggable-databases-1611-2ce2521bef.png)

   Oracle Database multitenancy: Pluggable databases
5. На странице **PDB** отображается список сервисов.

   ![Oracle Database multitenancy: Services](https://dt-cdn.net/images/services-1621-d3ca42e060.png)

   Oracle Database multitenancy: Services

## Тайм-аут тяжёлого запроса

ActiveGate версии 1.275+

Добавьте параметр `long-running-query-timeout` для настройки тайм-аута длительных SQL-запросов. Параметр необязателен; если он не задан, применяется тайм-аут по умолчанию в 10 секунд.

```
"vars": {



"long-running-query-timeout": null



}
```

## SSL

ActiveGate версии 1.251+

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

## Потребление ресурсов

Потребление ресурсов зависит от числа эндпоинтов Oracle. Первый эндпоинт потребляет 110 МБ ОЗУ и 0,1–0,5% ЦП. Каждый следующий эндпоинт потребляет 0,5–1,0 МБ ОЗУ и ~0,01% ЦП.

| Эндпоинты | Среднее ЦП | Макс. ЦП | ОЗУ (МБ) | Хост (тип EC2) |
| --- | --- | --- | --- | --- |
| 100 | 0,6% | 0,6% (всплеск в начале) | 160 | XS (`c5.large`) |
| 1 | 0,1% | 0,5% (всплеск в начале) | 110 | XS (`c5.large`) |