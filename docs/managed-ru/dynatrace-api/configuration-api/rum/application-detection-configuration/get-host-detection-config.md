---
title: Applications detection rules API - GET host detection headers
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/application-detection-configuration/get-host-detection-config
scraped: 2026-05-12T11:16:08.846691
---

# Applications detection rules API - GET host detection headers

# Applications detection rules API - GET host detection headers

* Reference
* Published Sep 24, 2020

Возвращает список заголовков определения хоста.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/hostDetection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applicationDetectionRules/hostDetection` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ApplicationDetectionRulesHostDetectionSettings](#openapi-definition-ApplicationDetectionRulesHostDetectionSettings) | Успех |

### Объекты тела ответа

#### Объект `ApplicationDetectionRulesHostDetectionSettings`

Конфигурация заголовков определения хоста.

| Элемент | Тип | Описание |
| --- | --- | --- |
| hostDetectionHeaders | string[] | Упорядоченный список заголовков определения хоста.  Заголовки оцениваются сверху вниз; применяется первый подходящий заголовок. |
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



"hostDetectionHeaders": [



"X-Host",



"X-Forwarded-Host"



],



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



}



}
```

## Связанные темы

* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о мониторинге реальных пользователей, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")
* [Определение приложений для Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Узнайте, как определять приложения с использованием предложенного, ручного подхода или правил обнаружения приложений.")