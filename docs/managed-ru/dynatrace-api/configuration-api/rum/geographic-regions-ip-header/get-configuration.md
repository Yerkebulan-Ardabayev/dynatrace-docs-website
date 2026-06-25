---
title: IP mapping header rules - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-header/get-configuration
scraped: 2026-05-12T11:20:16.674493
---

# IP mapping header rules - GET configuration

# IP mapping header rules - GET configuration

* Reference
* Published Sep 24, 2020

Возвращает список заголовков определения IP.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipDetectionHeaders` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipDetectionHeaders` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [IpDetectionHeaders](#openapi-definition-IpDetectionHeaders) | Успех |

### Объекты тела ответа

#### Объект `IpDetectionHeaders`

Конфигурация пользовательских клиентских IP-заголовков.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ipDetectionHeaders | string[] | Список пользовательских клиентских IP-заголовков.  Заголовки оцениваются сверху вниз; применяется первый подходящий заголовок. |

### JSON-модели тела ответа

```
{



"ipDetectionHeaders": [



"string"



]



}
```

## Связанные темы

* [Настройка определения IP-адресов для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/customize-ip-address-detection-web "Измените способ, которым Dynatrace определяет клиентские IP-адреса для ваших веб-приложений.")
* [Настройка определения IP-адресов для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/customize-ip-address-detection-mobile "Измените способ, которым Dynatrace определяет клиентские IP-адреса для ваших мобильных приложений.")
* [Настройка определения IP-адресов в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/customize-ip-address-detectio-custom "Измените способ, которым Dynatrace определяет клиентские IP-адреса для ваших пользовательских приложений.")