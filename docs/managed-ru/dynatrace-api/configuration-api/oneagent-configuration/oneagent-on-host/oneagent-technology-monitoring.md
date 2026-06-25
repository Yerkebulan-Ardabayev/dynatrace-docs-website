---
title: OneAgent on a host API - Technology monitoring configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-technology-monitoring
scraped: 2026-05-12T11:21:21.952088
---

# OneAgent on a host API - Technology monitoring configuration

# OneAgent on a host API - Technology monitoring configuration

* Reference
* Published Feb 03, 2020

Возвращает конфигурацию отслеживаемых технологий на указанном хосте.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/technologies` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/technologies` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace требуемого хоста. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [TechMonitoringConfigList](#openapi-definition-TechMonitoringConfigList) | Успех |

### Объекты тела ответа

#### Объект `TechMonitoringConfigList`

Список конфигураций мониторинга технологий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| technologies | [Technology[]](#openapi-definition-Technology) | Список конфигураций мониторинга технологий. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `Technology`

Конфигурация мониторинга технологий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoringEnabled | boolean | Мониторинг технологии включён (`true`) или отключён (`false`). |
| scope | string | Валидность конфигурации:  * `HOST`: настройка действует только для OneAgent на хосте. Другие OneAgent, подключённые к тому же серверу Dynatrace, могут иметь другую настройку. * `ENVIRONMENT`: настройка действует для всех OneAgent, подключённых к серверу Dynatrace. Возможные значения: * `ENVIRONMENT` * `HOST` |
| type | string | Тип технологии. Возможные значения: * `AIX_KERNEL_EXT` * `APACHE` * `CIM_V2` * `DOCKER` * `DOCKER_WIN` * `DOT_NET` * `DOT_NET_CORE` * `EXTENSIONS` * `EXTENSIONS_DS_GENERIC` * `EXTENSIONS_STATSD` * `GARDEN` * `GO` * `GO_STATIC` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PHP_81` * `PHP_CGI` * `PHP_CLI` * `PHP_CLI_SERVER` * `PHP_WIN` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `VARNISH` * `Z_OS` |

### JSON-модели тела ответа

```
{



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



},



"technologies": [



{



"monitoringEnabled": true,



"scope": "ENVIRONMENT",



"type": "JAVA"



}



]



}
```