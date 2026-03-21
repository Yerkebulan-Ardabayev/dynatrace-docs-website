---
title: Конфигурация мониторинга IBM Database
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring
scraped: 2026-03-06T21:36:39.137980
---

# Конфигурация мониторинга базы данных IBM


* Latest Dynatrace
* 2-min read

После определения области конфигурации необходимо определить следующее:

* Базы данных, из которых будут собираться данные
* ActiveGate для выполнения расширения и подключения к вашим устройствам

## Пример запроса

Пример запроса для активации расширения IBM DB2:

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

Человекочитаемое описание особенностей данной конфигурации мониторинга.

### Version

Версия данной конфигурации мониторинга. Обратите внимание, что одно расширение может выполнять несколько конфигураций мониторинга.

### Feature sets

Добавьте список наборов функций, которые вы хотите отслеживать. Чтобы включить все наборы функций, добавьте `all`.

```
"featureSets": [


"cpu",


"io"


]
```

### Endpoints

Вы можете определить до 20 000 конечных точек в одной конфигурации мониторинга в разделе `sqlDb2Remote`.

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

Для определения сервера базы данных IBM добавьте следующие данные в раздел `endpoints`:

* Host
* Port
* Учетные данные аутентификации
* Имя базы данных

### Authentication

Данные аутентификации, переданные в API Dynatrace при активации конфигурации мониторинга, обфусцируются и не могут быть получены обратно.

#### Credential vault

Тип аутентификации через хранилище учетных данных обеспечивает более безопасный подход к использованию расширений за счет безопасного хранения и управления пользовательскими учетными данными. Для этого вы должны быть владельцем учетных данных и иметь хранилище учетных данных, соответствующее следующим критериям:

* **Credential type** — User and password
* **Credential scope** — области Synthetic (в случае использования внешнего хранилища) и Extension authentication включены
* **Owner access only** включено только для владельцев учетных данных

```
"authentication": {


"scheme": "basic",


"useCredentialVault": true,


"credentialVaultId": "some-credential-vault-id"


}
```

### SSL

ActiveGate версии 1.269+

Включите SSL, чтобы источник данных проверял сертификат сервера и использовал SSL-шифрование вместо нативного шифрования.

```
"ssl": true
```

#### Включение SSL без локального хранилища доверенных сертификатов

Когда SSL включен и цепочка сертификатов сервера является публично верифицируемой (например, выданной Azure или другими известными центрами сертификации), нет необходимости вручную создавать хранилище доверенных сертификатов. Система автоматически доверяет сертификату сервера на основе доверенных центров сертификации в среде.

Однако, если вам необходимо использовать локальное хранилище доверенных сертификатов для сертификатов, не признанных глобально, или для дополнительных мер безопасности

1. В каталоге `userdata` на ActiveGate, выполняющих SQL-источник данных, вручную создайте хранилище доверенных сертификатов PKCS12 с именем `sqlds_truststore` и паролем `sqlds_truststore`.

   Команда для создания хранилища с keytool:

   ```
   keytool -genkey -keystore sqlds_truststore -storepass sqlds_truststore -keyalg DSA
   ```

   Расположение каталога `userdata`:

   * Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata`
   * Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`
2. Добавьте сертификат сервера в хранилище.

   Команда для импорта сертификата с keytool:

   ```
   keytool -import -keystore sqlds_truststore -file .\ora.crt -alias oracle
   ```

#### Проверка SSL-сертификатов

ActiveGate версии 1.269+

Сертификат дополнительно проверяется по имени хоста, что означает, что домен из сертификата должен совпадать с доменом из конечной точки, указанной в конфигурации мониторинга.

Включите эту опцию при подключении к базам данных с использованием пользовательских сертификатов.

```
"validateCertificates": true
```

### Scope

Обратите внимание, что каждый хост ActiveGate, выполняющий ваше расширение, нуждается в корневом сертификате для проверки подлинности расширения. Дополнительную информацию см. в разделе [Подписание расширения](../../sign-extensions.md "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.").

Область действия — это группа ActiveGate, которая будет выполнять расширение. Только один ActiveGate из группы будет выполнять данную конфигурацию мониторинга. Если вы планируете использовать один ActiveGate, назначьте его в выделенную группу. Вы можете назначить ActiveGate в группу во время или после установки. Дополнительную информацию см. в разделе [Группа ActiveGate](../../../../dynatrace-activegate/activegate-group.md "Understand the basic concepts of ActiveGate groups.").

Используйте следующий формат при определении группы ActiveGate:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Замените `<ActiveGate-group-name>` фактическим именем.
