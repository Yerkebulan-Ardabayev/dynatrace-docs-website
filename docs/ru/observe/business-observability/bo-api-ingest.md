---
title: Приём бизнес-событий через API
source: https://www.dynatrace.com/docs/observe/business-observability/bo-api-ingest
scraped: 2026-03-06T21:14:43.341295
---

# Приём бизнес-событий через API


* Последняя версия Dynatrace
* Справочник
* 11 мин чтения
* Обновлено 20 авг. 2025 г.

Вы можете настроить внешние бизнес-системы или ИТ-системы для отправки бизнес-событий в Dynatrace через API. Кроме того, вы можете выполнять запросы к данным с помощью DQL через API.

* Business Observability предоставляет **API бизнес-событий** для загрузки данных в формате JSON в Dynatrace через [конечную точку `/bizevents/ingest`](#ingest-endpoint).
* **Grail - DQL Query API** позволяет получать доступ к записям, хранящимся в Grail, выполняя [запросы DQL через API](#dql-via-api).

## API бизнес-событий: конечная точка `/bizevents/ingest`

Business Observability предоставляет API бизнес-событий для загрузки данных JSON в Dynatrace с помощью метода POST конечной точки `/bizevents/ingest`.

Чтобы опробовать этот API в API Explorer

1. В [пользовательском меню](../../discover-dynatrace/get-started/dynatrace-ui.md#user-menu-previous-dynatrace "Навигация в последней версии Dynatrace") (предыдущая версия Dynatrace) выберите **Environment API v2**.
2. Разверните **Business events**, затем **/bizevents/ingest**.

* **URL конечной точки** — `https://{your-environment-id}.live.dynatrace.com/api/v2/bizevents/ingest`
* **Метод** — POST
* **Аутентификация** — [токен доступа](#access-token) или [OAuth](#oauth)
* **Заголовок `Content-Type`** — зависит от [формата полезной нагрузки](#payload-formats).

  + [Чистый JSON](#pure-json): `application/json`
  + [CloudEvents](#cloudevents): `application/cloudevent+json` и `application/cloudevents+json`
  + [Пакет CloudEvents](#cloudevents-batch): `application/cloudevents-batch+json` и `application/cloudevents-batch+json`
* **Тело запроса** — `{your event}` — см. примеры ниже.

Обратите внимание, что при приёме бизнес-событий Dynatrace сохраняет принятые поля верхнего уровня как поля верхнего уровня в Grail, но преобразует сложные JSON-объекты в строки — см. поле `customer` в [примере события Grail](#grail-event) ниже.

Если вы работаете в последней версии Dynatrace, вы можете получить доступ к этой конечной точке через `https://{your-environment-id}.apps.dynatrace.com/platform/classic/environment-api/v2/bizevents/ingest`. Этот URL поддерживает только аутентификацию [OAuth](#oauth).

### Поддерживаемые форматы запросов и примеры

В дополнение к [чистому JSON](#pure-json), Dynatrace предлагает форматы полезной нагрузки [CloudEvents](#cloudevents) и [пакет CloudEvents](#cloudevents-batch), указываемые в заголовке запроса `Content-Type`.

Все три формата поддерживают одинаковые полезные нагрузки запросов. API бизнес-событий ограничивает размер полезной нагрузки до 5 МБ на запрос.

#### Чистый JSON

Обязательных полей нет.

Пример полезной нагрузки в чистом JSON для приёма одного события

```
{


"id":"2",


"paymentType":"paypal",


"plannedDeliveryDate":"01.01.2024",


"event.type":"com.bizevent.single",


"event.provider":"custom.provider",


"total":234,


"customer":{


"firstName":"John",


"lastName":"Doe"


},


"orderItemsProductIDs":[


"PR-102002002",


"QZ-123232"


]


}
```

Как Grail хранит одиночное событие

Каждый атрибут верхнего уровня хранится как поле верхнего уровня в Grail; вложенные JSON-объекты хранятся как строки.

```
{


"timestamp":"2023-08-10T10:06:21.697000000+02:00",


"customer":"{\"firstName\":\"John\",\"lastName\":\"Doe\"}",


"event.id":"6f7c0c12-8386-4015-bcb2-296ba73ebd54",


"event.kind":"BIZ_EVENT",


"event.provider":"custom.provider",


"event.type":"com.bizevent.single",


"id":"2",


"orderItemsProductIDs":"[\"PR-102002002\",\"QZ-123232\"]",


"paymentType":"paypal",


"plannedDeliveryDate":"01.01.2024",


"total":234


}
```

Пример полезной нагрузки в чистом JSON для приёма нескольких событий

```
[


{


"id":"1",


"paymentType":"paypal",


"plannedDeliveryDate":"01.01.2021",


"event.provider":"custom.provider.array",


"total":234,


"customer":{


"firstName":"John",


"lastName":"Doe"


},


"orderItemsProductIDs":[


"PR-102002002",


"QZ-123232"


]


},


{


"id":"1",


"paymentType":"paypal",


"plannedDeliveryDate":"01.01.2021",


"event.provider":"custom.provider.array",


"total":234,


"customer":{


"firstName":"John",


"lastName":"Doe"


},


"orderItemsProductIDs":[


"PR-102002002",


"QZ-123232"


]


}


]
```

#### CloudEvents

В [стандарте CloudEvents](https://dt-url.net/gi02yvo) обязательные поля, указанные ниже, могут быть дополнены дополнительными полями данных.

* `specversion`
* `source` — автоматически преобразуется в `event.provider`
* `type` — автоматически преобразуется в `event.type`
* `id` — автоматически преобразуется в `event.id`

Дополнительные данные передавайте в полях объекта `data`. В примере ниже дополнительными данными являются `paymentId`, `orderId` и `person`.

Пример полезной нагрузки CloudEvents

```
{


"specversion": "1.0",


"id": "8d8c6e5d-829d-4629-86fb-23cda5496fa9",


"source": "ba.dt.local",


"type": "com.dynatrace.business",


"time": "2023-08-07T07:07:13.532Z",


"data": {


"paymentId": "110",


"orderId": "5117",


"person": {


"firstName": "Max",


"lastName": "Meyer"


}


}


}
```

#### Пакет CloudEvents

Пакетный режим CloudEvents позволяет принимать несколько событий одновременно. Как и в предыдущем примере, обязательные поля могут быть дополнены дополнительными полями данных, такими как `paymentId` и `orderId`.

Пример полезной нагрузки пакета CloudEvents

```
[


{


"specversion": "1.0",


"id": "8d8c6e5d-829d-4629-86fb-23cda5496fa9",


"source": "ba.dt.local",


"type": "com.dynatrace.business",


"time": "2023-08-07T07:07:13.532Z",


"data": {


"paymentId": "110",


"orderId": "5717"


}


},


{


"specversion": "1.0",


"id": "37d9df29-ba57-4526-8ac7-6baa6ccbc9c4",


"source": "ba.dt.local",


"type": "com.dynatrace.business",


"time": "2023-08-07T07:07:14.532Z",


"data": {


"paymentId": "111",


"orderId": "5718"


}


}


]
```

### Обогащение бизнес-событий

При отправке бизнес-событий Dynatrace обогащает их, добавляя дополнительный контекст. Например, Dynatrace добавляет информацию о вашем приложении, геолокации, устройстве и многом другом. Это относится только к данным, принятым через API бизнес-событий.

Подробнее см. [Обогащение бизнес-событий](bo-events-enrichment.md "Узнайте, какие свойства Dynatrace автоматически добавляет к отправленным бизнес-событиям.").

### Практика использования конечной точки API бизнес-событий

Если у вас есть среда Dynatrace SaaS, импортируйте наш блокнот **Hands-on Business Observability**, чтобы пошагово пройти процесс приёма бизнес-событий с помощью конечной точки API. Блокнот проведёт вас через настройку и тестирование API с использованием общедоступного источника данных.

1. Скопируйте и сохраните JSON-файл для блокнота.

   Начало работы с Business Observability — JSON-файл для внешних источников данных

   ```
   {


   "version": "5",


   "defaultTimeframe": {


   "from": "now-2h",


   "to": "now"


   },


   "sections": [


   {


   "id": "4becc036-acd5-4985-ae63-e6cad53f2000",


   "type": "markdown",


   "markdown": "# Hands on Business Observability\n\n### What you will learn\n- [x] How to ingest \"[business events](https://www.dynatrace.com/support/help/platform-modules/business-observability/bo-api-ingest)\" (a.k.a generic data) into Dynatrace without OneAgent\n- [x] What are the prerequisites\n- [x] Importance of `event.provider` and `event.type` attributes\n- [x] Automating the ingest via AutomationEngine\n- [x] Enriching the data\n- [x] Analytics, Dashboards, and more\n\nReference:\n- Online documentation: [Business Observability](https://www.dynatrace.com/support/help/platform-modules/business-observability)\n- [Basic concepts of Dynatrace Business Observability](https://www.dynatrace.com/support/help/shortlink/bo-basic-concepts)"


   },


   {


   "id": "d7488bcb-d354-46b0-b2b7-53f35ec4753d",


   "type": "markdown",


   "markdown": "## What you need to know first...\n\n### Business event\n\nAn event is an action or occurrence that takes place within a system or a \"service\". The system ***produces a signal*** when an event occurs. An event becomes a business event when it generates business-grade data.\n\n### Business events can come from many sources\n- Non-OneAgent sources, example [CloudEvents](https://cloudevents.io/)\n- OneAgent, stored in the `bizevents` Grail table as bizevents data object\n- RUM data, stored in the `bizevents` Grail table as bizevents data object\n- Generic data ingest via bizevents API endpoint, stored in the `bizevents` Grail table as bizevents data object\n- Logs, currently stored in the `logs` table, as logs data object. Enhancements coming in future to allow log data sources to be stored as bizevents data object.\n\n### Why is this important?\n\nDynatrace prioritizes business events separately from observability data to ensure business-grade data.\n\n### What is Business-grade data?\n\nPrecise data that doesn't rely on samples to report baselines, identify trends, or alert on anomalies with statistical accuracy.\n\nBusiness-grade data is often required for business decisions and reporting where ***precision is critical***.\n\nContrast this with typical IT reporting which achieves statistical accuracy through sampling and extrapolation."


   },


   {


   "id": "199c0513-b8b8-4305-9231-a6fb49e70d75",


   "type": "markdown",


   "markdown": "## Listen and watch\n--- \n##### Prerequisites\n- OAuth2 bearer token for API access\n- [JSON format in request body](https://www.dynatrace.com/support/help/shortlink/bo-api-ingest#request-body) for BizEvents API endpoint\n\n##### Note\nOAuth2 will be key to accessing more and more critical aspects of the new platform. It is important for you to know how to do this.\n\nHowever, this is somewhat like a \"do once and forget\" task, so it is not often executed and thus many will lack practice.\n\nDo practice and exchange tips with your peers.\n\n##### Resources\nWhat is OAuth?\n- [Wikipeidea](https://en.wikipedia.org/wiki/OAuth)\n- [Youtube](https://www.youtube.com/watch?v=LD3NCUP5hW4)\n\nHow is it set in Dynatrace?\n- [Online docs](https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication/account-api-authentication)\n\n##### Demo\n- Creating OAuth2 bearer token\n- Take note of the unique properties of a bearer token\n- Building the API query and using the bearer token\n- Example of data ingest via your favourite API tool"


   },


   {


   "id": "b8ca400b-f7a0-4b1c-8b0a-b0489cc3d732",


   "type": "markdown",


   "markdown": "## Follow and do\n\nOverview of the tasks\n1. Automate\n1. Build query\n1. Enriching the data\n1. Build dashboards etc."


   },


   {


   "id": "92d1de22-7f09-4385-88cf-dab3aac40ffd",


   "type": "markdown",


   "markdown": "### Step 1: Automate \n--- \n\n- Create a workflow to ingest data from a public API source\n  - Use on-demand trigger\n- Create a task to get the bearer token\n  - Copy the payload from the example workflow or from here\n  ```\n  grant_type=client_credentials&client_id=[CLIENTID goes here]client_secret=[CLIENTSECRET goes here]\n  ```\n  - Replace the strings in square brackets with your own `clientid` and `clientsecret`\n- Create a task to get the data from a public API\n  - Use `Http request`\n  - Enter the external API URL in the `URL field`\n- Create a task to insert the data via the `bizevents` Dynatrace API\n  - Use `Http request`\n  - payload\n    - enter `{{result(\"name_of_task\").json.<replace with the data structure of your JSON results> }}`\n  - ensure you set the headers\n    - Content-Type\n      - Pure JSON: no mandatory fields. Content-Type `application/json`\n      - CloudEvent: Mandatory fields are Specversion, Source, Type, Id. Content-Type `application/cloudevent+json`\n      - CloudEvent batch (batch ingest of events): Mandatory fields as above. Content-Type `cloudevent-batch+json`\n    - Authorization\n      - `Bearer {{ result(\"get_bearer_token\").json.access_token }}`\n\n##### Discussion points\n- Use `Run Javascript task` if need to do advanced \"computation\" or \"logic\" with the data. (Industry term - \"transform the data\".)\n- [Jinja templating engine](https://www.dynatrace.com/support/help/platform-modules/cloud-automation/workflows/reference) can also be used within `Http request task` to \"transform\" the payload data"


   },


   {


   "id": "15ebff0c-6205-48e6-b1cc-faccbed6426b",


   "type": "markdown",


   "markdown": "### Step 2: Validate the data\n--- \n\nLet's start by validating what data we have first.\n\n##### Discussion points\n- What do you notice when you query the data? Is it easy to find out which dataset is yours?\n- What if you would like to define how your data will be processed further?"


   },


   {


   "id": "0786560c-8c2d-4583-9550-31309840fe9a",


   "type": "dql",


   "showTitle": false,


   "state": {


   "input": {


   "value": "fetch bizevents",


   "timeframe": {


   "from": "now-2h",


   "to": "now"


   }


   },


   "state": "idle",


   "visualizationSettings": {


   "chartSettings": {


   "gapPolicy": "connect",


   "circleChartSettings": {


   "groupingThresholdType": "absolute"


   }


   },


   "singleValue": {


   "showLabel": true,


   "label": "",


   "autoscale": true


   },


   "table": {


   "rowDensity": "condensed",


   "enableSparklines": false,


   "hiddenColumns": [],


   "lineWrapIds": [],


   "firstVisibleRowIndex": 0,


   "columnWidths": {}


   }


   },


   "davisAnalytics": {


   "analyzerComponentState": {


   "resultState": {}


   }


   }


   },


   {


   "id": "85b10d2c-b709-4b34-8e71-d03b0c896738",


   "type": "markdown",


   "markdown": "### Step 3: Enriching the data\n---\n\n- [Predefined attributes](https://www.dynatrace.com/support/help/shortlink/ba-business-events-enrichment) automated if using OneAgent and RUM, further enrichment can be done\n- If using API, some important attributes require configuration\n- This is done via [Business events processing](https://www.dynatrace.com/support/help/shortlink/ba-business-events-processing)\n\nWe will enrich the incoming data set with the following 2 attributes\n- `event.provider`\n- `event.type`\n\n###### 3.1\nGo to Settings > Business Analytics > Ingest Pipeline > Processing\n\n###### 3.2\nGive the rule a name and add matcher\n\n###### 3.3\nAdd the necessary DQL under `Processor definition`.\n\n###### 3.4\nTest the rule and remember to Save\n\n###### 3.5\n- Trigger the workflow and query Dynatrace again, now with the `event.provider` attribute as a filter.\n- What do you notice now after you query for the data?"


   },


   {


   "id": "1416beec-b33f-4e5c-a054-6cb40897c7a0",


   "type": "markdown",


   "markdown": "### Step 4: Build dashboards etc.\n---\n\nNow that we have organized the data, let's see... what should we do with the data?\n\nEven if we would like to build dashboards, we need an objective, won't we?\n\nFor a start let's answer this question: ***\"Which are the most popular rental spots in the city?\"***\n\nBuild a dashboard that can visualize this data. Use category chats and switch it to horizontal. Play around with the visualization!\n\n##### Discussion points\n- From here, let's see what else can we do with the data..."


   },


   {


   "id": "1db4f97e-4ed9-4bf4-8215-885ccef7bef6",


   "type": "dql",


   "showTitle": false,


   "state": {


   "input": {


   "value": "fetch bizevents\n| summarize popular = count(), by: {RENT_NM}\n| filter popular < 1000\n| sort popular desc\n| limit 20",


   "timeframe": {


   "from": "now-2h",


   "to": "now"


   }


   },


   "state": "idle",


   "visualizationSettings": {


   "chartSettings": {


   "gapPolicy": "connect",


   "circleChartSettings": {


   "groupingThresholdType": "absolute"


   }


   },


   "singleValue": {


   "showLabel": true,


   "label": "",


   "autoscale": true


   },


   "table": {


   "rowDensity": "condensed",


   "enableSparklines": false,


   "hiddenColumns": [],


   "lineWrapIds": [],


   "firstVisibleRowIndex": 0,


   "columnWidths": {}


   }


   },


   "davisAnalytics": {


   "analyzerComponentState": {


   "resultState": {}


   }


   }


   }


   ]


   }
   ```
2. В Dynatrace перейдите в **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
3. Разверните ![Открыть панель дашбордов](https://dt-cdn.net/images/dashboards-app-dashboards-panel-open-6c03b43117.svg "Открыть панель дашбордов") боковую панель.
4. Выберите **Upload** для импорта блокнота.
5. Следуйте инструкциям руководства в блокноте.

## Запросы DQL через API

Dynatrace Grail - DQL Query API позволяет сторонним приложениям получать данные из Grail, выполняя запросы DQL через API. Через этот API можно только запрашивать данные, но не принимать их.

Чтобы просмотреть документацию Swagger и опробовать этот API в последней версии Dynatrace

1. Найдите «API» или «Dynatrace API».
2. В раскрывающемся списке в правом верхнем углу страницы выберите **Grail - DQL Query**.
3. Разверните **Query Execution** для просмотра его методов.

Чтобы выполнить запрос и получить результат, необходимо сделать два запроса с помощью отдельных методов.

1. Чтобы запросить Grail, выполните запрос [POST `/query:execute`](#query-execute).
2. Чтобы получить результат, выполните запрос [GET `/query:poll`](#query-poll).

### Метод POST /query:execute

* URL конечной точки — `https://{your-environment-id}.apps.dynatrace.com/platform/storage/query/v1/query:execute`
* Метод — POST
* Аутентификация — [OAuth](#oauth)
* Заголовок `Content-Type` — `application/json`
* Тело запроса — `{your DQL query}`

#### Пример тела запроса

```
{


"query": "fetch bizevents | summarize Count()"


}
```

#### Пример тела ответа

Вам потребуется использовать значение `requestToken` из этого ответа в запросе [`/query:poll`](#query-poll).

```
{


"state": "SUCCEEDED",


"requestToken": " +kuSj8qvRvq64GkG5CEHag==",


"progress": 100


}
```

### Метод GET /query:poll

* URL конечной точки — `https://{your-environment-id}.apps.dynatrace.com/platform/storage/query/v1/query:poll`
* Метод — GET
* Аутентификация — [OAuth](#oauth)
* Заголовок `Content-Type` — `application/json` (чистый JSON)
* GET-параметр — `request-token`, используется для идентификации выполненного POST-запроса

#### Пример URL запроса

```
https://mySampleEnv.apps.dynatrace.com/platform/storage/query/v1/query:poll?request-token=%2BkuSj8qvRvq64GkG5CEHag%3D%3D
```

#### Пример тела ответа

```
{


"state": "SUCCEEDED",


"progress": 100,


"result": {


"records": [


{


"count()": "0"


}


],


"types": [


{


"indexRange": [


0,


0


],


"mappings": {


"count()": {


"type": "long"


}


}


}


],


"metadata": {


"grail": {


"canonicalQuery": "fetch bizevents\n| summarize count()",


"timezone": "Z",


"query": "fetch bizevents | summarize Count()",


"scannedRecords": 0,


"dqlVersion": "V1_0",


"scannedBytes": 0,


"analysisTimeframe": {


"start": "2023-07-11T07:28:11.068767000Z",


"end": "2023-07-11T09:28:11.068767000Z"


},


"locale": "",


"executionTimeMilliseconds": 4155,


"notifications": [],


"queryId": "fa4b928f-caaf-46fa-bae0-6906e421076a",


"sampled": false


}


}


}


}
```

## Аутентификация

* API бизнес-событий использует [аутентификацию по токену доступа](#access-token) для URL конечной точки `bizevents/ingest` в предыдущей версии Dynatrace (`https://{your-environment-id}.live.dynatrace.com/api/v2/bizevents/ingest`).

  Если вы работаете в последней версии Dynatrace, вы можете получить доступ к этой конечной точке через `https://{your-environment-id}.apps.dynatrace.com/platform/classic/environment-api/v2/bizevents/ingest`. Этот URL поддерживает только [OAuth](#oauth) для доступа к API.
* Grail - DQL Query API использует [OAuth](#oauth) для доступа к API.

### Токен доступа

Чтобы создать новый токен доступа для конечной точки `/bizevents/ingest` API бизнес-событий, следуйте процедуре, описанной в [Dynatrace API — токены и аутентификация](../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

Вам необходимо выбрать область действия токена **Ingest bizevents**.

Чтобы аутентифицировать вызов, прикрепите токен к HTTP-заголовку `Authorization`, предваряя область `Api-Token`.

```
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

### Настройка и использование OAuth для доступа к API

Как для API бизнес-событий, так и для Grail - DQL Query API, вам сначала нужен действующий токен носителя для аутентификации, который вы запрашиваете, настроив OAuth для доступа к API.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создайте клиент OAuth**](bo-api-ingest.md#oauth-client "Настройте аутентификацию и принимайте бизнес-события через API.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создайте политику IAM**](bo-api-ingest.md#iam-policy "Настройте аутентификацию и принимайте бизнес-события через API.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Привяжите политику к группе**](bo-api-ingest.md#bind-policy "Настройте аутентификацию и принимайте бизнес-события через API.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Получите токен носителя**](bo-api-ingest.md#obtain-token "Настройте аутентификацию и принимайте бизнес-события через API.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Аутентифицируйтесь**](bo-api-ingest.md#authenticate "Настройте аутентификацию и принимайте бизнес-события через API.")

#### Шаг 1 Создайте клиент OAuth

Вы можете создавать новые клиенты OAuth на странице **Account Management** в Dynatrace.

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/). Если у вас несколько аккаунтов, выберите тот, которым хотите управлять.
2. В верхней строке меню выберите **Identity & access management** > **OAuth clients**.
3. Выберите **Create client**.
4. Укажите адрес электронной почты пользователя, которому будет принадлежать клиент.
5. Укажите описание нового клиента.
6. Убедитесь, что ваш клиент имеет необходимые разрешения, выбрав одну или несколько опций при настройке клиента. Для чтения и записи бизнес-событий вам потребуются:

   * Чтение бизнес-событий: (`storage:bizevents:read`)
   * Чтение бакетов Grail: (`storage:buckets:read`)
   * Запись/редактирование событий: (`storage:events:write`) (необходимо только при приёме данных через [API бизнес-событий](#ingest-endpoint))
7. Выберите **Create client**.
8. Сохраните сгенерированный секрет клиента в менеджере паролей для дальнейшего использования. Также вам понадобится сгенерированный идентификатор клиента при [получении токена носителя](#obtain-token).

   Секрет клиента отображается только один раз при создании, после чего хранится в зашифрованном виде и не может быть раскрыт.

#### Шаг 2 Создайте политику IAM

Чтобы использовать клиент OAuth, необходимо убедиться, что вашему пользователю назначена правильная политика IAM.

Чтобы настроить политику

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/). Если у вас несколько аккаунтов, выберите тот, которым хотите управлять.
2. В верхней строке меню выберите **Identity & access management** > **Policy management**.
3. Выберите **Create policy** и укажите название и описание политики. Эта информация понадобится вам при [привязке политики к группе пользователей](#bind-policy). Подробнее об управлении политиками читайте в [Управление политиками IAM](../../manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt.md "Создавайте, редактируйте, копируйте и удаляйте политики IAM для управления разрешениями пользователей Dynatrace.").
4. Добавьте следующие операторы политики для записи и запроса бизнес-событий.

   ```
   ALLOW storage:buckets:read WHERE storage:table-name = "bizevents";


   ALLOW storage:bizevents:read;


   ALLOW storage:events:write;
   ```
5. Выберите **Create policy**.

#### Шаг 3 Привяжите политику к группе

Вы можете назначить [созданную политику](#iam-policy) группе, к которой принадлежит ваш пользователь, или добавить пользователя в новую группу. Инструкции по привязке политик к группам см. в [Работа с политиками](../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md#add-or-remove "Работа с политиками").

#### Шаг 4 Получите токен носителя

Вы можете использовать [клиент OAuth](#oauth-client) для получения токена носителя OAuth 2.0. Используйте приведённую ниже информацию для отправки запроса на URL токена носителя. Используйте полученный в ответе токен для [аутентификации](#authenticate) в [API бизнес-событий](#ingest-endpoint) или [Grail - DQL Query API](#dql-via-api).

* URL конечной точки для запроса токена — `https://sso.dynatrace.com/sso/oauth2/token`
* Метод — POST
* Заголовок `Content-Type` — `application/x-www-form-urlencoded`
* Ключи/параметры — Вы можете отправить следующие ключи или параметры в теле запроса. Убедитесь, что все значения закодированы в формате URL.

Пример запроса API

Заголовки запроса

```
POST /sso/oauth2/token HTTP/2


Host: sso.dynatrace.com


content-type: application/x-www-form-urlencoded
```

Тело запроса

```
grant_type=client_credentials&client_id=dt0s02.****&client_secret=dt0s02.***.****&scope=storage%3Abizevents%3Aread+storage%3Aevents%3Awrite+storage%3Abuckets%3Aread
```

Пример ответа API

```
{


"scope": "storage:bizevents:read storage:events:write storage:buckets:read",


"token_type":"Bearer",


"expires_in":300,


"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjEifQ.eyJzdWIiOiI2YWUwMmFmNC01NmIwLTRhM2MtODI0OS1mYjc2ZDgyOTYwYTQiLCJyZXMiOiJ1cm46ZHRhY2NvdW50OjJiMjM2NDM4LTJhMzEtNDg3Mi04NjU1LWJjYTRmYThhZjkxNyIsIl9jbGFpbV9uYW1lcyI6eyJncm91cHMiOiIwIn0sInByZWZlcnJlZF91c2VybmFtZSI6ImRhbmllbC5tYXJzY2huaWdAZHluYXRyYWNlLmNvbSIsImd0IjoiY2MiLCJpbnQiOnRydWUsImF1ZCI6ImR0MHMwMi4zWkJZWkhWVCIsInNjb3BlIjoiYWNjb3VudC1pZG0tcmVhZCBhY2NvdW50LWlkbS13cml0ZSBhY2NvdW50LWVudi1yZWFkIGFjY291bnQtZW52LXdyaXRlIGFjY291bnQtdWFjLXJlYWQgYWNjb3VudC11YWMtd3JpdGUgaWFtLXBvbGljaWVzLW1hbmFnZW1lbnQgaWFtOnBvbGljaWVzOndyaXRlIGlhbTpwb2xpY2llczpyZWFkIGlhbTpiaW5kaW5nczp3cml0ZSBpYW06YmluZGluZ3M6cmVhZCBpYW06ZWZmZWN0aXZlLXBlcm1pc3Npb25zOnJlYWQgc3RvcmFnZTpiaXpldmVudHM6cmVhZCBzdG9yYWdlOmV2ZW50czp3cml0ZSIsIl9jbGFpbV9zb3VyY2VzIjp7IjAiOnsiZW5kcG9pbnQiOm51bGx9fSwiZXhwIjoxNjkxNjE1NTcxLCJpYXQiOjE2OTE2MTUyNzEsImp0aSI6ImJmNDZhNmFhLTRjZmItNDA1MS05ZmUzLTMzZTljMjc0OTdhZSIsImVtYWlsIjoiZGFuaWVsLm1hcnNjaG5pZ0BkeW5hdHJhY2UuY29tIn0.x3_dUuOmdqcrrsfuRyiUwKOOFSJ30fAQnpKGbJTNGy8N3qspKDO0OC36Z0GILc275bTsLY3fARzRQNBOW1Okmg",


"resource":"urn:dtaccount:2b236438-2a31-4872-8655-bca4fa8af917"


}
```

#### Шаг 5 Аутентифицируйтесь

Чтобы аутентифицировать вызов, прикрепите токен к HTTP-заголовку `Authorization`, предваряя область `Bearer`.

```
--header 'Authorization: Bearer abcdefjhij1234567890'
```
