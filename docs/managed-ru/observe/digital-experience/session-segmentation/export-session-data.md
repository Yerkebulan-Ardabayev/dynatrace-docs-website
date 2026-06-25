---
title: Экспорт сессий пользователей
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-segmentation/export-session-data
scraped: 2026-05-12T11:33:28.246047
---

# Экспорт сессий пользователей

# Экспорт сессий пользователей

* How-to guide
* 12-min read
* Updated on Sep 06, 2022

Dynatrace может непрерывно отправлять данные о сессиях пользователей на указанный webhook-эндпоинт.

Для начала получения данных о сессиях необходимо [настроить эндпоинт](#define-endpoint), а затем [настроить экспорт через интерфейс Dynatrace](#configure-export-ui) или через [Settings API](#configure-export-api).

Dynatrace отправляет данные [завершённых сессий пользователей](/managed/observe/digital-experience/rum-concepts/user-session#user-session-end "Узнайте, как определяется сессия пользователя.") пакетами на все определённые эндпоинты с периодической отправкой каждые несколько секунд, как только сессия помечена как завершённая. Передача данных происходит при выполнении одного из следующих условий:

* завершено 1000 сессий пользователей;
* размер пакета превысил 896 000 байт;
* ни одна сессия не завершилась в течение последних 30 секунд.

Для предотвращения перегрузки системы Dynatrace отменяет запрос, если ваш эндпоинт не отвечает в течение 30 секунд. Dynatrace повторяет запрос ещё три раза, прежде чем окончательно отклонить его и отправить уведомление об ошибке **Request timeout**.

## Определение эндпоинта

Сервер, предоставляющий webhook, должен прослушивать запросы `PUT` или `POST` по URL, указанному в конфигурации экспорта сессий. По соображениям безопасности Dynatrace допускает только HTTPS-эндпоинты.

* **HTTP method**: `PUT` или `POST`
* **Path**: согласно конфигурации
* **Content Type**: `application/json` или `application/x-ndjson`. При [отправке в Elasticsearch](#send-to-elasticsearch) установите `application/x-ndjson`.
* **Response status code**: `200`

Пример кода для Eclipse Jersey

Следующий пример кода использует фреймворк Jersey RESTful Web Services с открытым исходным кодом. Этот код можно использовать для настройки необходимого эндпоинта для получения данных о сессиях пользователей.

```
@Path("/export/")

public class ExportREST {

...

@PUT

@Produces(MediaType.APPLICATION_JSON)

@Path("events")

public JResponse<String> jsonEvents(final String data) {

...

// split the bulk into single documents

final String[] lines = StringUtils.split(data, '\n');

for(String line : lines) {

...

// handle the JSON-data

}

return JResponse.ok("")

.header(HttpHeaders.SERVER, "Endpoint for Dynatrace session data export")

.build();

}

}
```

## Настройка экспорта через интерфейс Dynatrace

Для настройки экспорта сессий пользователей через интерфейс Dynatrace:

1. Перейдите в **Settings** > **Integration** > **User session exports**.
2. Выберите **Add item**.
3. Укажите **Endpoint URL** и включите **Enable user session export**, если вы готовы начать получение данных.

   По соображениям безопасности Dynatrace допускает только HTTPS-эндпоинты.
4. Задайте **Content type** значение `application/json` или `application/x-ndjson`. При [отправке данных в Elasticsearch](#send-to-elasticsearch) установите `application/x-ndjson`.
5. Включите **Use POST method (instead of PUT)** при [отправке данных в Elasticsearch](#send-to-elasticsearch) или если ваш эндпоинт принимает запросы `POST`.
6. При необходимости [настройте аутентификацию](#authentication), [включите передачу данных в Elasticsearch](#send-to-elasticsearch) или [настройте область экспорта, оповещения и дополнительную конфигурацию](#export).

Вы также можете [протестировать экспорт](#test-export), [скачать образец набора данных](#download-sample-dataset) или [образец маппинга](#mapping).

Можно настроить до трёх HTTPS-эндпоинтов.

### Настройка аутентификации

Dynatrace может отправлять данные с использованием базовой аутентификации или аутентификации OAuth 2.0. Эти типы аутентификации позволяют защитить ваши эндпоинты.

При активации аутентификации для конфигурации экспорта [протестируйте конфигурацию](#test-export) перед сохранением.

По соображениям безопасности необходимо повторно вводить пароль базовой аутентификации или секрет клиента OAuth 2.0 при тестировании или редактировании существующей конфигурации.

#### Настройка базовой аутентификации

1. На странице **User session exports** разверните нужный URL эндпоинта.
2. В разделе **Authentication** включите **Activate**.
3. Установите **Basic authentication** в качестве типа аутентификации.
4. Введите имя пользователя и пароль.

Пароль шифруется и скрывается в вашей среде.

#### Настройка аутентификации OAuth 2.0

1. На странице **User session exports** разверните нужный URL эндпоинта.
2. В разделе **Authentication** включите **Activate**.
3. Установите **OAuth 2.0** в качестве типа аутентификации.
4. Введите URL токена доступа, ID клиента, секрет клиента и область действия (необязательно).

Секрет клиента шифруется и скрывается в вашей среде.

Дополнительная информация об аутентификации OAuth 2.0

OAuth 2.0 предлагает различные типы предоставления разрешений, однако Dynatrace поддерживает только тип client credentials. Шаги работы аутентификации OAuth 2.0 при экспорте сессий:

1. Dynatrace направляет запрос к вашему серверу авторизации для получения токена доступа. В запросе включаются **Access token URL**, **Client ID**, **Client secret** и **Scope** (необязательно).

   ```
   curl --insecure -w "\nHTTP Status: %{http_code}\n" \

   --location --request POST 'https://[your-access-token-url]/oauth2/token' \

   --header 'Content-Type: application/x-www-form-urlencoded' \

   --header 'Accept: application/json' \

   --data-urlencode 'client_id=[your-client-id]' \

   --data-urlencode 'client_secret=[your-client-secret]' \

   --data-urlencode 'grant_type=client_credentials' \

   --data-urlencode 'scope=[your-scope]'
   ```
2. Ваш сервер авторизации отвечает токеном доступа, например:

   ```
   {

   "scope":"session-export-api",

   "token_type":"Bearer",

   "expires_in":300,

   "access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

   }
   ```
3. Dynatrace направляет POST-запрос на настроенный **Endpoint URL**, включая данные о сессиях и токен доступа в заголовке `Authorization`.

   ```
   curl --request POST \

   --url https://[your-endpoint-url] \

   --header 'Authorization: Bearer ACCESS_TOKEN' \

   --header 'Content-type: application/json'
   ```

### Отправка данных непосредственно в Elasticsearch

Для отправки данных непосредственно в вашу установку Elasticsearch:

1. Убедитесь, что ваш экземпляр Elasticsearch доступен с сервера кластера.
2. Убедитесь, что URL экспорта имеет следующий формат: `https://<your_host>:9200/_bulk`. Замените `<your_host>` фактическим значением.
3. На странице **User session exports** разверните нужный URL эндпоинта.
4. В разделе **Define your endpoint** убедитесь, что **Content type** установлен в `application/x-ndjson` и включён **Use POST method (instead of PUT)**.
5. В разделе **Send data directly to Elasticsearch** включите **Activate**.
6. Введите [имя индекса, куда отправляются данные](#index), и [тип документов в индексе Elasticsearch](#type).

#### Индекс Elasticsearch

Создайте индекс, куда хотите отправлять данные о сессиях пользователей, и определите маппинг для вашего индекса. Подробнее о скачивании образца маппинга см. в разделе [Скачивание образца маппинга](#mapping).

Если индекс не создан до включения экспорта, Elasticsearch автоматически создаст маппинги для полей. Однако автоматический маппинг не всегда создаёт подходящие маппинги полей. Например, поля дат могут быть сопоставлены как `long`.

#### Тип индекса Elasticsearch

Elasticsearch в настоящее время удаляет поддержку типов маппинга. Рекомендуется устанавливать `_doc` в качестве типа документа независимо от версии Elasticsearch.

* **Elasticsearch версии 6**: укажите один тип на индекс. При создании индекса укажите параметр `include_type_name`.
* **Elasticsearch версии 7**: указание типов устарело. Параметр `include_type_name` по умолчанию равен `false`.
* **Elasticsearch версии 8**: указание типов больше не поддерживается. Начиная с этой версии, не указывайте тип документа.

`Type` относится к «типу индекса» в Elasticsearch и не ограничивает, какие сессии экспортируются. Вне зависимости от выбранного типа, экспортируются все данные сессий, включая действия пользователей, события и ошибки.

### Настройка области экспорта, оповещений и дополнительной конфигурации

В разделе **Export scope, alerting, and advanced configuration** вы можете сузить область экспорта, отключить уведомления и скорректировать другие настройки экспорта.

* **Export scope**: для определения области экспорта выберите нужную **Management zone**. После настройки зоны управления Dynatrace будет отправлять только те сессии, в которых хотя бы одно действие пользователя соответствует приложению в этой зоне.

  Ограничение экспорта только синтетическими сессиями в настоящее время невозможно.
* **Alerting**: включите **Disable notification**, если вы не хотите получать уведомления при сбое экспорта сессий.
* **Custom configuration**: укажите **Custom configuration properties** для тонкой настройки конфигурации экспорта. Перед изменением этого поля обратитесь к эксперту Dynatrace через чат.

## Тестирование экспорта

Для тестирования конфигурации экспорта разверните нужный URL эндпоинта на странице **User session exports** и выберите **Test export**.

Если кнопка **Test export** недоступна, вероятно, ваш **Endpoint URL** или **Access token URL** использует протокол HTTP. По соображениям безопасности Dynatrace допускает только протокол HTTPS.

Dynatrace использует текущую конфигурацию для экспорта до 50 сессий за последние семь дней. Если данные за этот период отсутствуют, тестовый экспорт недоступен. По завершении тестового экспорта вы получите уведомление о результатах.

Конфигурацию не нужно сохранять для тестирования эндпоинта.

## Скачивание образца набора данных

Чтобы увидеть, как выглядят данные о сессиях пользователей при экспорте, разверните нужный URL эндпоинта на странице **User session exports** и выберите **Download sample export data**.

Образец набора данных содержит до 50 сессий пользователей за последние семь дней. Если сессии за этот период отсутствуют, скачивание образца данных недоступно.

* Если настроен обычный эндпоинт, образец данных содержит сессии в формате JSON, разделённые символами новой строки.
* Если настроен эндпоинт для отправки данных непосредственно в Elasticsearch, образец данных также содержит строки заголовков, указывающие Elasticsearch, что делать с данными.

## Скачивание образца маппинга

Для [экспорта данных сессий непосредственно в Elasticsearch](#send-to-elasticsearch) вы можете скачать образец маппинга для ваших индексов. Разверните нужный URL эндпоинта на странице **User session exports** и выберите **Download mapping**.

Скачанный шаблонный файл маппинга содержит маппинг для каждого экспортируемого поля.

```
PUT /my-usersession-index

{

"settings": {

"index": {

"number_of_shards": 3,

"number_of_replicas": 1

}

},

"mappings": {

"properties": {

// add the mappings from the downloaded file here ...

}

}

}
```

## Настройка экспорта через API

Конфигурация экспорта сессий хранится с помощью фреймворка Settings 2.0. Это предоставляет REST API для создания, чтения, обновления и удаления конфигураций. Подробнее см. в [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.").

* Эндпоинты для доступа к Settings API:

  + Для Dynatrace Managed: `https://{your-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}`
  + Для Environment ActiveGate: `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}`
* Schema ID для конфигурации экспорта сессий: `builtin:elasticsearch.user-session-export-settings-v2`.

  Для чтения текущей конфигурации:

  ```
  GET https://{your-domain}/api/v2/settings/objects?schemaIds=builtin:elasticsearch.user-session-export-settings-v2&scopes=tenant&fields=objectId,value
  ```

Для добавления конфигурации экспорта через REST API:

```
POST https://{your-domain}/api/v2/settings/objects?schemaIds=builtin:elasticsearch.user-session-export-settings-v2&scopes=tenant

[

{

"schemaVersion": "0.0.214",

"schemaId": "builtin:elasticsearch.user-session-export-settings-v2",

"scope": "tenant",

"value": {

"endpointDefinition": {

"endpointUrl": "https://endpoint-export.dev",

"enableUserSessionExport": true,

"contentType": "application/json",

"usePost": false

},

"authentication": {

"active": false

},

"sendDirect": {

"active": false

},

"exportBehavior": {

"managementZone": null,

"disableNotification": false,

"customConfiguration": null

}

}

}

]
```

За один запрос можно добавить только одну конфигурацию. Для добавления второй конфигурации выполните новый запрос `POST`.

Подробнее об обновлении или удалении объекта настроек см. в [Settings API - PUT an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Редактируйте объект настроек через Dynatrace API.") и [Settings API - DELETE an object](/managed/dynatrace-api/environment-api/settings/objects/del-object "Удаляйте объект настроек через Dynatrace API.").

## Проверка конфигурации экспорта

Для проверки конфигурации экспорта выполните следующую команду:

```
curl -v -H "Content-Type: application/json" -X PUT -d '{"visitorId":"14804637803609BCTKP776NMJBOIF3R8OD6R0E4NQALJO","visitId":"16229530","startTime":1480463779085,"endTime":1480463784889,"visitType":"SYNTHETIC"}' http://localhost:3000/export/events
```

При необходимости добавьте следующие дополнительные флаги:

* `--insecure` для отключения проверки SSL
* `--http1.1` если команда возвращает ошибку `REFUSED_STREAM`