---
title: Create a new request naming rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/request-naming-api/create-a-new-request-naming-rule
scraped: 2026-05-12T12:02:32.173138
---

# Create a new request naming rule

# Create a new request naming rule

* Reference
* Published Mar 05, 2019

Этот сценарий использования показывает, как с помощью API **Request naming** создать новое правило именования запросов.

Именование запросов сервиса позволяет объединять или уточнять запросы в нескольких сервисах. Кроме того, можно синхронизировать эти правила между несколькими окружениями Dynatrace.

Предположим, у нас есть два запроса из Drupal (CMS с открытым исходным кодом) с именами `/node/1` и `/node/1/edit`. Последние части обоих имён (`/1` и `/1/edit`) не несут полезной информации. Мы можем убрать эти части и объединить два отдельных запроса в один с именем `/node`. Для этого нужно правило именования запросов, переименовывающее каждый запрос, URL которого **начинается с** `/node`, просто в `/node`, тем самым объединяя их.

Конфигурация такого правила выглядит так:

```
{



"enabled": true,



"namingPattern": "/node",



"conditions": [



{



"attribute": "WEBREQUEST_URL_PATH",



"comparisonInfo": {



"type": "STRING",



"comparison": "BEGINS_WITH",



"value": "/node",



"negate": false,



"isCaseSensitive": false



}



}



],



"placeholders": []



}
```

Важные компоненты:

* **conditions**: определяет, какие запросы будут переименованы.
* **namingPattern**: определяет результирующее имя.

Описания других полей смотрите в разделе **Parameters** темы [**POST a new request naming rule**](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/post-new-rule "Создание правила именования запросов через Dynatrace API.").

Теперь отправим эту конфигурацию в API-вызове. Способ выполнения REST-вызовов на ваше усмотрение: можно использовать любой REST-клиент или написать скрипт вроде приведённого ниже. Также можно использовать [API Explorer](/managed/dynatrace-api#api-explorer "Узнайте, что нужно для использования Dynatrace API.") Dynatrace, чтобы ознакомиться с эндпоинтами и выполнить все необходимые запросы.

REST-клиент

Dynatrace API Explorer

1. Сгенерируйте новый [токен доступа для Dynatrace API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API."). Обязательно назначьте ему scope **Read configuration** и **Write configuration**.
2. Выполните запрос [**POST a new request naming rule**](/managed/dynatrace-api/configuration-api/service-api/request-naming-api/post-new-rule "Создание правила именования запросов через Dynatrace API.") с токеном, созданным на первом шаге, и JSON-конфигурацией правила именования запросов из примера выше в качестве payload.

1. Сгенерируйте новый [токен доступа для Dynatrace API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API."). Обязательно назначьте ему scope **Read configuration** и **Write configuration**.
2. Откройте [меню пользователя](/managed/discover-dynatrace/get-started/dynatrace-ui#user "Навигация по платформе Dynatrace Managed") в прежнем веб-интерфейсе Dynatrace и выберите **Dynatrace API > Configuration API**.

   ![Доступ к API Explorer](https://dt-cdn.net/images/mz-1-1313-ec4939b8c8.png)

   Доступ к API Explorer
3. В API Explorer выберите **Authorize**.  
   Появится диалог **Available authorizations**.
4. Вставьте свой токен в поля **ReadConfigToken** и **WriteConfigToken** и нажмите **Authorize**.
5. Разверните запрос **POST /service/requestNaming/** и нажмите **Try it out**.

   ![Try it out](https://dt-cdn.net/images/create-rnr-1-1460-fa51d43874.png)

   Try it out
6. Вставьте JSON-конфигурацию правила именования запросов (см. выше) в поле **body** и нажмите **Execute**.

   ![Payload](https://dt-cdn.net/images/create-rnr-2-1441-10b7c61eb9.png)

   Payload
7. Успешный запрос возвращает код **201** и краткое представление правила именования запросов.

   ![Успешный запрос](https://dt-cdn.net/images/create-rnr-3-1346-7baeb4f45b.png)

   Успешный запрос

## Связанные темы

* [Настройка именования запросов](/managed/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Настройте именование запросов и определите операции, предоставляемые вашими сервисами.")