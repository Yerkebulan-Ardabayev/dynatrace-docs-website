---
title: Frequent issue detection API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/frequent-issue-detection-api/get-configuration
scraped: 2026-05-12T12:35:22.204661
---

# Frequent issue detection API - GET configuration

# Frequent issue detection API - GET configuration

* Reference
* Published Jun 28, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API."). Ищите schema **Frequent issue detection** (`builtin:anomaly-detection.frequent-issues`).

Возвращает конфигурацию frequent issue detection. Подробнее смотрите [Detection of frequent issues](/managed/dynatrace-intelligence/root-cause-analysis/detection-of-frequent-issues "Узнайте, как Dynatrace обнаруживает и управляет повторяющимися проблемными паттернами как frequent issues.").

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/frequentIssueDetection` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [FrequentIssueDetectionConfig](#openapi-definition-FrequentIssueDetectionConfig) | Успех |

### Объекты тела ответа

#### Объект `FrequentIssueDetectionConfig`

Параметры frequent issue detection. Подробнее смотрите [Detection of frequent issues](https://dt-url.net/4da3kdg) в документации Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| frequentIssueDetectionApplicationEnabled | boolean | Detection для applications включена (`true`) или выключена (`false`). |
| frequentIssueDetectionEnvironmentEnabled | boolean | Detection для environment включена (`true`) или выключена (`false`). |
| frequentIssueDetectionInfrastructureEnabled | boolean | Detection для infrastructure включена (`true`) или выключена (`false`). |
| frequentIssueDetectionServiceEnabled | boolean | Detection для services включена (`true`) или выключена (`false`). |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

### JSON-модели тела ответа

```
{



"frequentIssueDetectionApplicationEnabled": true,



"frequentIssueDetectionEnvironmentEnabled": false,



"frequentIssueDetectionInfrastructureEnabled": true,



"frequentIssueDetectionServiceEnabled": true



}
```

## Пример

В этом примере запрос возвращает текущую конфигурацию frequent issue detection.

API-токен передаётся в заголовке **Authorization**.

Конфигурация имеет следующие настройки:

![Anomaly detection configuration](https://dt-cdn.net/images/get-frequent-issue-704-93f6d04ce3.png)

Конфигурация anomaly detection

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/config/v1/frequentIssueDetection' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/frequentIssueDetection
```

#### Тело ответа

```
{



"metadata": {



"configurationVersions": [



0



],



"clusterVersion": "1.194.0.20200427-192742"



},



"frequentIssueDetectionApplicationEnabled": false,



"frequentIssueDetectionServiceEnabled": true,



"frequentIssueDetectionInfrastructureEnabled": false



}
```

#### Код ответа

200

## Связанные темы

* [Detection of frequent issues](/managed/dynatrace-intelligence/root-cause-analysis/detection-of-frequent-issues "Узнайте, как Dynatrace обнаруживает и управляет повторяющимися проблемными паттернами как frequent issues.")