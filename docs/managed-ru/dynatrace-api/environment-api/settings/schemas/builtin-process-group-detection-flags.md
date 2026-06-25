---
title: Settings API - Built-in detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-group-detection-flags
scraped: 2026-05-12T11:49:46.876638
---

# Settings API - Built-in detection rules schema table

# Settings API - Built-in detection rules schema table

* Опубликовано 05 декабря 2023 г.

### Встроенные правила обнаружения (`builtin:process-group.detection-flags)`

Включает или отключает флаги обнаружения process group

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:process-group.detection-flags` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.detection-flags` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-group.detection-flags` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.detection-flags` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Игнорировать версии, сборки, даты и GUID в именах каталогов процессов `ignoreUniqueIdentifiers` | boolean | Для определения уникальной идентичности каждого обнаруженного процесса и для генерации уникального имени Dynatrace анализирует имя каталога, в котором лежит binary процесса. Для application containers вроде Tomcat и JBoss Dynatrace анализирует важные каталоги, такие как CATALINA\_HOME и JBOSS\_HOME. В некоторых сценариях автоматического деплоя имена таких каталогов обновляются автоматически: добавляются номера версий, сборок, даты или GUID. Включите этот параметр, чтобы автоматические переименования каталогов не приводили к тому, что Dynatrace регистрирует уже существующие процессы как новые. | Required |
| Использовать CATALINA\_BASE для идентификации Tomcat cluster nodes `useCatalinaBase` | boolean | По умолчанию Tomcat-кластеры идентифицируются и именуются по имени каталога CATALINA\_HOME. Этот параметр включает использование имени каталога CATALINA\_BASE для идентификации нескольких Tomcat-нод внутри Tomcat-кластера. Если параметр отключён, каждая комбинация CATALINA\_HOME+CATALINA\_BASE будет считаться отдельным Tomcat-кластером, иначе говоря, у Tomcat-кластера не может быть нескольких нод на одном хосте. | Required |
| Использовать имя Docker-контейнера для различения нескольких контейнеров `useDockerContainerName` | boolean | **Только для Docker вне container platforms.** По умолчанию Dynatrace использует имена образов как идентификаторы process group, по одному инстансу process-group на хост. В обычном случае имена Docker-контейнеров не подходят как стабильные идентификаторы инстансов process group, поскольку они переменные и автогенерируемые. Однако имена контейнеров можно назначить вручную, и тогда они становятся надёжными идентификаторами инстансов process-group. Этот флаг указывает Dynatrace использовать имена, выданные Docker, чтобы различать несколько инстансов одного образа. Если флаг не применён и на одном хосте запущено несколько контейнеров одного образа, соответствующие процессы будут схлопнуты в одно process view. **Применяйте флаг с осторожностью.** | Required |
| Автоматически обнаруживать Cassandra-кластеры `autoDetectCassandraClusters` | boolean | Включение флага приведёт к обнаружению отдельных Cassandra process groups по настроенному имени Cassandra cluster. | Required |
| Использовать имя Node.js-скрипта для различения процессов, запущенных из одного каталога, в дополнение к application id. `addNodeJsScriptName` | boolean | В старых версиях Node.js-приложения различались по имени каталога, имя скрипта не учитывалось. Изменение параметра может изменить общее поведение Node.js process groups. Если сомневаетесь, оставьте как есть. | Required |
| Автоматически обнаруживать TIBCO BusinessWorks engines `autoDetectTibcoEngines` | boolean | Включение флага приведёт к обнаружению отдельных TIBCO BusinessWorks process groups по каждому engine property file. | Required |
| Идентифицировать и именовать JBoss-серверы по system property jboss.server.name `identifyJbossServerBySystemProperty` | boolean | Включение флага приведёт к определению имени JBoss server по system property jboss.server.name=, только если не задан -D[Server:]. | Required |
| Автоматически обнаруживать webMethods Integration Server `autoDetectWebMethodsIntegrationServer` | boolean | Включение флага приведёт к обнаружению webMethods Integration Server, включая специфические свойства, такие как install root и product name. | Required |
| Автоматически обнаруживать Spring Boot-приложения `autoDetectSpringBoot` | boolean | Включение флага приведёт к обнаружению Spring Boot process groups по командной строке и файлам конфигурации приложений. | Required |
| Автоматически обнаруживать TIBCO BusinessWorks Container Edition engines `autoDetectTibcoContainerEditionEngines` | boolean | Включение флага приведёт к обнаружению отдельных TIBCO BusinessWorks process groups по каждому engine property file. | Required |
| Группировать процессы Oracle database по SID `splitOracleDatabasePG` | boolean | Включите, чтобы группировать и отдельно анализировать процессы каждой Oracle DB. Каждая process group получает уникальное имя по SID Oracle DB. | Required |
| Группировать процессы Oracle listener по имени `splitOracleListenerPG` | boolean | Включите, чтобы группировать и отдельно анализировать процессы каждого Oracle Listener. Каждая process group получает уникальное имя по имени Oracle Listener. На Windows этот параметр поддерживает listeners, запущенные вручную или работающие под Windows virtual account. | Required |
| Автоматически обнаруживать WebSphere Liberty-приложение `autoDetectWebSphereLibertyApplication` | boolean | Включение флага приведёт к обнаружению отдельных WebSphere Liberty process groups по командной строке java. | Required |
| Мониторить короткоживущие процессы `shortLivedProcessesMonitoring` | boolean | Включите, чтобы мониторить использование CPU и памяти короткоживущими процессами, которые иначе теряются при классическом мониторинге. | Required |
| Группировать процессы IBM MQ по имени queue manager `groupIBMMQbyInstanceName` | boolean | Включите, чтобы группировать и отдельно анализировать процессы каждого инстанса IBM MQ Queue manager. Каждая process group получает уникальное имя по имени инстанса queue manager. | Required |
| Автоматически обнаруживать security-софт `securitySoftwareDetectionEnabled` | boolean | Этот флаг включает обнаружение security-софта, например антивирусной защиты. Сейчас обнаруживаются Carbon Black EDR (только Windows), CrowdStrike Falcon XDR и Trellix Endpoint Security (бывший McAfee). | Required |
| Группировать процессы DB2 database по DB2 Instances `splitDb2GroupingByInstances` | boolean | Включите, чтобы группировать и отдельно анализировать процессы каждого DB2 Instance. Каждый процесс получает уникальное имя по имени DB2 Instance. | Required |