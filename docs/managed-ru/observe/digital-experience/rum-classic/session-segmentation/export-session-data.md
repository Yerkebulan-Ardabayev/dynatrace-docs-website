---
title: Экспорт пользовательских сессий в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/session-segmentation/export-session-data
---

# Экспорт пользовательских сессий в RUM Classic

# Экспорт пользовательских сессий в RUM Classic

* Практическое руководство
* 12 минут чтения
* Обновлено 06 сентября 2022 г.

Dynatrace может непрерывно отправлять данные пользовательских сессий на указанную конечную точку webhook.

Чтобы начать получать данные пользовательских сессий, нужно [настроить конечную точку](#define-endpoint) и затем [настроить экспорт сессий через веб-интерфейс Dynatrace](#configure-export-ui) или через [Settings API](#configure-export-api).

Dynatrace отправляет данные о [завершённых пользовательских сессиях](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#user-session-end "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") пакетами на все заданные конечные точки, с выгрузкой каждые несколько секунд, чтобы экспортировать данные сразу после того, как пользовательская сессия помечена как завершённая. Передача данных происходит, как только выполняется одно из следующих условий:

* завершилось 1000 пользовательских сессий;
* размер пакета превышает 896 000 байт;
* за последние 30 секунд не завершилось ни одной пользовательской сессии.

Чтобы предотвратить перегрузку системы, Dynatrace отменяет запрос, если конечная точка не отвечает в течение 30 секунд. Dynatrace повторяет попытку ещё три раза, прежде чем окончательно отклонить запрос и отправить оповещение с сообщением об ошибке **Request timeout**.

## Настройка конечной точки

Сервер, предоставляющий webhook, должен прослушивать запросы `PUT` или `POST` по URL, указанному в конфигурации экспорта сессий. Кроме того, из соображений безопасности Dynatrace допускает только HTTPS-конечные точки.

* **Метод HTTP**: `PUT` или `POST`
* **Путь**: как настроено
* **Тип содержимого**: `application/json` или `application/x-ndjson`. При [отправке в Elasticsearch](#send-to-elasticsearch) установить `application/x-ndjson`.
* **Код состояния ответа**: `200`

Пример кода для Eclipse Jersey

Следующий пример кода использует open-source фреймворк Jersey RESTful Web Services. Этот код можно использовать для настройки конечной точки, необходимой для приёма данных пользовательских сессий.

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

## Настройка экспорта сессий через веб-интерфейс Dynatrace

Чтобы настроить экспорт пользовательских сессий через веб-интерфейс Dynatrace

1. Перейти в **Settings** > **Integration** > **User session exports**.
2. Выбрать **Add item**.
3. Указать **Endpoint URL** и включить **Enable user session export**, если готово начать получение данных пользовательских сессий.

   Из соображений безопасности Dynatrace допускает только HTTPS-конечные точки.
4. Установить **Content type** в значение `application/json` или `application/x-ndjson`. При [отправке данных сессий в Elasticsearch](#send-to-elasticsearch) установить `application/x-ndjson`.
5. Включить **Use POST method (instead of PUT)** при [отправке данных сессий в Elasticsearch](#send-to-elasticsearch) или если конечная точка настроена на приём запросов `POST`.
6. При необходимости [настроить аутентификацию](#authentication), [включить передачу данных в Elasticsearch](#send-to-elasticsearch) или [настроить область экспорта, оповещения и расширенную конфигурацию](#export).

Также можно [протестировать экспорт пользовательских сессий](#test-export), а также [скачать образец набора данных](#download-sample-dataset) или [образец сопоставления](#mapping).

Можно настроить до трёх HTTPS-конечных точек.

### Настройка аутентификации

Dynatrace может отправлять данные пользовательских сессий с использованием базовой аутентификации или OAuth 2.0. Эти типы аутентификации позволяют защитить конечные точки.

При включении аутентификации для конфигурации экспорта сессий [протестировать конфигурацию](#test-export) перед сохранением.

Из соображений безопасности при тестировании конфигурации экспорта сессий нужно повторно ввести пароль базовой аутентификации или секрет клиента OAuth 2.0. Также нужно повторно ввести пароль или секрет при редактировании существующей конфигурации экспорта сессий с включённой аутентификацией.

#### Настройка базовой аутентификации

Чтобы настроить экспорт пользовательских сессий с базовой аутентификацией

1. На странице **User session exports** развернуть нужный URL конечной точки.
2. В разделе **Authentication** включить **Activate**.
3. Установить **Basic authentication** в качестве типа аутентификации.
4. Ввести имя пользователя и пароль.

Пароль шифруется и маскируется в среде.

#### Настройка аутентификации OAuth 2.0

Чтобы настроить экспорт пользовательских сессий с аутентификацией по учётным данным клиента OAuth 2.0

1. На странице **User session exports** развернуть нужный URL конечной точки.
2. В разделе **Authentication** включить **Activate**.
3. Установить **OAuth 2.0** в качестве типа аутентификации.
4. Ввести URL для получения токена доступа, ID клиента, секрет клиента и область (необязательно).

Секрет клиента шифруется и маскируется в среде.

Дополнительная информация об аутентификации OAuth 2.0

[OAuth 2.0﻿](https://auth0.com/intro-to-iam/what-is-oauth-2/) предлагает различные типы предоставления доступа (grant types), но Dynatrace поддерживает только тип client credentials. Информацию об этом типе см. в следующих ресурсах:

* [Client Credentials Flow﻿](https://auth0.com/docs/get-started/authentication-and-authorization-flow/client-credentials-flow)
* [Call Your API Using the Client Credentials Flow﻿](https://auth0.com/docs/get-started/authentication-and-authorization-flow/call-your-api-using-the-client-credentials-flow)
* [The OAuth 2.0 Authorization Framework | Client Credentials Grant﻿](https://www.rfc-editor.org/rfc/rfc6749.html#section-4.4)

Чтобы отправлять данные пользовательских сессий с использованием аутентификации OAuth 2.0, нужно настроить сервер авторизации OAuth2 с конечной точкой для получения токена доступа. Также нужно убедиться, что **Endpoint URL** работает с токеном доступа.

Ниже описано, как работает аутентификация OAuth 2.0 для экспорта пользовательских сессий.

1. Dynatrace отправляет запрос на сервер авторизации для получения токена доступа. В запрос включаются **Access token URL**, **Client ID**, **Client secret** и **Scope** (необязательно).

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
2. Сервер авторизации отвечает токеном доступа, например:

   ```
   {



   "scope":"session-export-api",



   "token_type":"Bearer",



   "expires_in":300,



   "access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2V4YW1wbGUuYXV0aDAuY29tLyIsImF1ZCI6Imh0dHBzOi8vYXBpLmV4YW1wbGUuY29tL2NhbGFuZGFyL3YxLyIsInN1YiI6InVzcl8xMjMiLCJpYXQiOjE0NTg3ODU3OTYsImV4cCI6MTQ1ODg3MjE5Nn0.CA7eaHjIHz5NxeIJoFK9krqaeZrPLwmMmgI_XiQiIkQ"



   }
   ```
3. Dynatrace отправляет запрос POST на настроенный **Endpoint URL**. Запрос включает данные пользовательской сессии, а также токен доступа, полученный на предыдущем шаге, который передаётся как Bearer-токен в заголовке `Authorization`.

   ```
   curl --request POST \



   --url https://[your-endpoint-url] \



   --header 'Authorization: Bearer ACCESS_TOKEN' \



   --header 'Content-type: application/json'
   ```

### Отправка данных напрямую в Elasticsearch

Чтобы отправлять данные напрямую в развёрнутый Elasticsearch

1. Убедиться, что экземпляр Elasticsearch доступен с сервера кластера.
2. Убедиться, что URL экспорта имеет следующий формат: `https://<your_host>:9200/_bulk`. Заменить `<your_host>` на фактическое значение.
3. На странице **User session exports** развернуть нужный endpoint URL.
4. В разделе **Define your endpoint** убедиться, что **Content type** установлен в `application/x-ndjson`, а **Use POST method (instead of PUT)** включён.
5. В разделе **Send data directly to Elasticsearch** включить **Activate**.
6. Указать [название индекса, в который отправляются данные](#index) и [тип документов в индексе Elasticsearch](#type).

#### Индекс Elasticsearch

Создать индекс, в который нужно отправлять данные пользовательских сессий, и определить маппинг для этого индекса. Подробнее о том, как скачать пример маппинга для конфигурации экспорта пользовательских сессий, см. [Download a sample mapping](#mapping).

Если индекс не создан до включения экспорта пользовательских сессий, развёрнутый Elasticsearch автоматически создаёт маппинги для полей. Такое автоматическое создание маппингов не всегда даёт подходящие маппинги полей. Например, поля дат отображаются как `long`.

#### Тип индекса Elasticsearch

В настоящее время Elasticsearch убирает поддержку типов маппинга. Способ создания индексов и настройки типов зависит от версии Elasticsearch. Подробности ниже.

Рекомендуется указывать `_doc` в качестве типа документа независимо от версии Elasticsearch.

* **Elasticsearch версии 6**

  + Указывать один единственный тип на индекс.
  + При создании индекса указывать параметр строки запроса `include_type_name`, чтобы запросы и ответы включали имя типа. По умолчанию этот параметр равен `true`. Если его не задать, появляется предупреждение об устаревании (deprecation warning). Если при создании индекса не указан тип, используется `_doc`.
* **Elasticsearch версии 7**

  + Указание типов в этой версии Elasticsearch устарело. Параметр `include_type_name` по умолчанию равен `false`.
  + Можно принудительно заставить Elasticsearch использовать имя типа, установив параметр в `true`, что приводит к предупреждению об устаревании.
* **Elasticsearch версии 8**

  + Указание типов больше не поддерживается. Начиная с этой версии тип документа нужно опускать. Подробнее см. [Removal of mapping types﻿](https://www.elastic.co/guide/en/elasticsearch/reference/current/removal-of-types.html).

`Type` означает "тип индекса", используемый в Elasticsearch, и не ограничивает то, какие пользовательские сессии экспортируются. Независимо от выбранного типа, экспортируются все данные пользовательских сессий, включая действия пользователя, события и ошибки.

Чтобы ограничить экспортируемые пользовательские сессии, можно определить management zone. См. раздел [Set up export scope, alerting, and advanced configuration](#export) ниже.

### Настройка области экспорта, оповещений и расширенной конфигурации

В разделе **Export scope, alerting, and advanced configuration** для эндпоинта можно сузить область экспорта сессий, отключить уведомления и настроить некоторые другие параметры экспорта пользовательских сессий.

* **Export scope**: чтобы определить область экспорта пользовательских сессий, выбрать нужную **Management zone**. После настройки management zone Dynatrace отправляет только те пользовательские сессии, которые содержат хотя бы одно действие пользователя с совпадающим приложением.

  Ограничить экспорт сессий только синтетическими пользовательскими сессиями в настоящее время невозможно.
* **Alerting**: включить **Disable notification**, если не нужно получать уведомления при сбое экспорта пользовательских сессий.
* **Custom configuration**: указать **Custom configuration properties**, чтобы дополнительно настроить конфигурацию экспорта пользовательских сессий. Перед изменением этого поля нужно связаться с экспертом по продукту Dynatrace через живой чат.

При любых проблемах с экспортом пользовательских сессий нужно связаться с экспертом по продукту Dynatrace через живой чат, прежде чем настраивать дополнительные параметры.

## Тестирование экспорта

Чтобы протестировать конфигурацию экспорта пользовательских сессий, нужно развернуть нужный endpoint URL на странице **User session exports** и выбрать **Test export**.

Если кнопка **Test export** неактивна, вероятная причина в том, что **Endpoint URL** или **Access token URL** указан по протоколу HTTP. Из соображений безопасности Dynatrace допускает только протокол HTTPS.

Dynatrace использует текущую конфигурацию экспорта пользовательских сессий, чтобы экспортировать до 50 пользовательских сессий за последние семь дней.
Если за этот период данные недоступны, тестовый экспорт недоступен. Как только тестовый экспорт завершится, придёт уведомление о результатах.

Сохранять конфигурацию для тестирования эндпоинта не нужно.

При настройке эндпоинта, защищённого [аутентификацией](#authentication):

* Протестировать конфигурацию перед сохранением.
* Повторно ввести пароль базовой аутентификации или OAuth 2.0 client secret при тестировании конфигурации.

## Скачивание образца набора данных

Чтобы посмотреть, как выглядят данные пользовательских сессий при экспорте на конечные точки, на странице **User session exports** нужно развернуть требуемый URL конечной точки и выбрать **Download sample export data**.

Образец набора данных состоит максимум из 50 пользовательских сессий, отслеженных в среде за последние семь дней. Если за этот период не было пользовательских сессий, скачивание образца данных недоступно.

* Если для экспорта пользовательских сессий настроена обычная конечная точка, образец данных содержит пользовательские сессии в формате JSON, разделённые символами новой строки.

  Пример: три сессии, отправленные пакетом в виде трёх строк

  ```
  {"tenantId":"umsaywsjuo","userSessionId":"1394_1008","startTime":1511441593539,"endTime":1511441716896,"duration":123357,"internalUserId":"1394","userType":"REAL_USER","applicationType":"MOBILE_APPLICATION","bounce":false,"newUser":false,"userActionCount":1,"totalErrorCount":1,"ip":"2001:1800:ffff:eac2:63f5:568e:b3c6:6c54","geolocationContinentName":"North America","geolocationCountryName":"United States","geolocationRegionName":"Florida","geolocationCityName":"Delray Beach","osFamilyName":"Windows","osVersionName":"Windows 10.0 Mobile","manufacturer":"Nokia","device":"L-930","userId":"fearghasbag","screenHeight":1920,"screenWidth":1080,"screenOrientation":"PORTRAIT","displayResolution":"FHD","hasCrash":true,"isp":"SWCP-AS - Southwest Cyberport","stringTags":{ },"numTags":{ },"dateTags":{ },"userActions":[ { "name":"Checkout","type":"Custom","startTime":1511441593539,"endTime":1511441593562,"duration":23,"application":"easyTravel Demo","speedIndex":null,"errorCount":0,"apdexCategory":"UNKNOWN","networkTime":null,"serverTime":null,"frontendTime":null,"documentInteractiveTime":null,"failedImages":null,"failedXhrRequests":null,"httpRequestsWithErrors":null,"thirdPartyResources":null,"thirdPartyBusyTime":0,"cdnResources":null,"cdnBusyTime":0,"firstPartyResources":null,"firstPartyBusyTime":0,"hasCrash":false,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":null,"requestStart":null,"responseStart":null,"responseEnd":null,"visuallyCompleteTime":null } ],"events":[ { "type":"UserTag","name":"fearghasbag","startTime":1511441593562,"application":"MOBILE_APPLICATION-752C288D59734C79" } ],"errors":[ { "type":"Crash","name":"ThrowAsync","startTime":1511441716896,"application":"MOBILE_APPLICATION-752C288D59734C79"}]}



  {"tenantId":"umsaywsjuo","userSessionId":"1394_1008","startTime":1511441593539,"endTime":1511441716896,"duration":123357,"internalUserId":"1394","userType":"REAL_USER","applicationType":"MOBILE_APPLICATION","bounce":false,"newUser":false,"userActionCount":1,"totalErrorCount":1,"ip":"2001:1800:ffff:eac2:63f5:568e:b3c6:6c54","geolocationContinentName":"North America","geolocationCountryName":"United States","geolocationRegionName":"Florida","geolocationCityName":"Delray Beach","osFamilyName":"Windows","osVersionName":"Windows 10.0 Mobile","manufacturer":"Nokia","device":"L-930","userId":"fearghasbag","screenHeight":1920,"screenWidth":1080,"screenOrientation":"PORTRAIT","displayResolution":"FHD","hasCrash":true,"isp":"SWCP-AS - Southwest Cyberport","stringTags":{ },"numTags":{ },"dateTags":{ },"userActions":[ { "name":"Checkout","type":"Custom","startTime":1511441593539,"endTime":1511441593562,"duration":23,"application":"easyTravel Demo","speedIndex":null,"errorCount":0,"apdexCategory":"UNKNOWN","networkTime":null,"serverTime":null,"frontendTime":null,"documentInteractiveTime":null,"failedImages":null,"failedXhrRequests":null,"httpRequestsWithErrors":null,"thirdPartyResources":null,"thirdPartyBusyTime":0,"cdnResources":null,"cdnBusyTime":0,"firstPartyResources":null,"firstPartyBusyTime":0,"hasCrash":false,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":null,"requestStart":null,"responseStart":null,"responseEnd":null,"visuallyCompleteTime":null } ],"events":[ { "type":"UserTag","name":"fearghasbag","startTime":1511441593562,"application":"MOBILE_APPLICATION-752C288D59734C79" } ],"errors":[ { "type":"Crash","name":"ThrowAsync","startTime":1511441716896,"application":"MOBILE_APPLICATION-752C288D59734C79"}]}



  {"tenantId":"umsaywsjuo","userSessionId":"1394_1008","startTime":1511441593539,"endTime":1511441716896,"duration":123357,"internalUserId":"1394","userType":"REAL_USER","applicationType":"MOBILE_APPLICATION","bounce":false,"newUser":false,"userActionCount":1,"totalErrorCount":1,"ip":"2001:1800:ffff:eac2:63f5:568e:b3c6:6c54","geolocationContinentName":"North America","geolocationCountryName":"United States","geolocationRegionName":"Florida","geolocationCityName":"Delray Beach","osFamilyName":"Windows","osVersionName":"Windows 10.0 Mobile","manufacturer":"Nokia","device":"L-930","userId":"fearghasbag","screenHeight":1920,"screenWidth":1080,"screenOrientation":"PORTRAIT","displayResolution":"FHD","hasCrash":true,"isp":"SWCP-AS - Southwest Cyberport","stringTags":{ },"numTags":{ },"dateTags":{ },"userActions":[ { "name":"Checkout","type":"Custom","startTime":1511441593539,"endTime":1511441593562,"duration":23,"application":"easyTravel Demo","speedIndex":null,"errorCount":0,"apdexCategory":"UNKNOWN","networkTime":null,"serverTime":null,"frontendTime":null,"documentInteractiveTime":null,"failedImages":null,"failedXhrRequests":null,"httpRequestsWithErrors":null,"thirdPartyResources":null,"thirdPartyBusyTime":0,"cdnResources":null,"cdnBusyTime":0,"firstPartyResources":null,"firstPartyBusyTime":0,"hasCrash":false,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":null,"requestStart":null,"responseStart":null,"responseEnd":null,"visuallyCompleteTime":null } ],"events":[ { "type":"UserTag","name":"fearghasbag","startTime":1511441593562,"application":"MOBILE_APPLICATION-752C288D59734C79" } ],"errors":[ { "type":"Crash","name":"ThrowAsync","startTime":1511441716896,"application":"MOBILE_APPLICATION-752C288D59734C79"}]}
  ```
* Если конечная точка настроена на [прямую отправку данных в Elasticsearch](#send-to-elasticsearch), образец данных также содержит строки заголовков, как показано в примере ниже. Они сообщают Elasticsearch, что делать с данными.

  Пример: сессия, отправленная в Elasticsearch

```
{ "index" : { "_index" : "my-index", "_type" : "_doc", "_id" : "umsaywsjuo-744377345-1622107543233" } }



{"tenantId":"umsaywsjuo","userSessionId":"744377345","startTime":1622107543233,"endTime":1622107578205,"duration":34972,"internalUserId":"744377345","userType":"SYNTHETIC","applicationType":"WEB_APPLICATION","bounce":false,"newUser":true,"userActionCount":12,"totalErrorCount":5,"totalLicenseCreditCount":0,"matchingConversionGoalsCount":0,"ip":"157.25.19.100","continent":"Europe","country":"Poland","region":"synthetic","city":"Bydgoszcz","browserType":"Synthetic Agent","browserFamily":"Synthetic monitor","browserMajorVersion":"Synthetic monitor","osFamily":"Linux","osVersion":"Linux","screenHeight":1080,"screenWidth":1920,"screenOrientation":"LANDSCAPE","displayResolution":"FHD","hasSessionReplay":false,"isp":"T-Mobile Czech Republic","clientType":"Synthetic Agent","browserMonitorId":"SYNTHETIC_TEST-18B209EFE2F438F8","browserMonitorName":"mySampleEnv.dynatrace.com - browser monitor - analysis","stringProperties":[],"longProperties":[],"doubleProperties":[],"dateProperties":[],"userActions":[{"name":"/rest/cvalidation/validate/%2fvalidateappmetrickey?input=<masked>&appmetrickey=<masked>&gtf=<masked>","domain":"mySampleEnv.dynatrace.com","targetUrl":"https://mySampleEnv.dynatrace.com/#monitoranalysiskpm;webcheckId=SYNTHETIC_TEST-67444FBB89C6F11B;actionType=Load;splitting=event;analysisTf=custom1622103968000to1622107568000;mode=performance;analysisActionType=Load;gtf=l_2_HOURS","type":"Xhr","startTime":1622107568648,"endTime":1622107569320,"duration":672,"application":"mySampleEnv.dynatrace.com - browser monitor - analysis - 1620645163422","internalApplicationId":"APPLICATION-A8894472DACEDA0E","speedIndex":null,"apdexCategory":"FRUSTRATED","matchingConversionGoals":[],"networkTime":5,"serverTime":58,"frontendTime":609,"documentInteractiveTime":null,"thirdPartyResources":1,"thirdPartyBusyTime":659,"cdnResources":0,"cdnBusyTime":null,"firstPartyResources":9,"firstPartyBusyTime":333,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":1622107568730,"requestStart":2,"responseStart":60,"responseEnd":63,"visuallyCompleteTime":null,"syntheticEvent":"click on \"Analyze performance\"","syntheticEventId":"SYNTHETIC_TEST_STEP-7D9201BEB990247E","keyUserAction":false,"stringProperties":[],"longProperties":[],"doubleProperties":[],"dateProperties":[],"userActionPropertyCount":0,"customErrorCount":0,"javascriptErrorCount":0,"requestErrorCount":1,"largestContentfulPaint":null,"firstInputDelay":null,"totalBlockingTime":null,"cumulativeLayoutShift":null},{"name":"/rest/webcheckdetails/overviewdata/browsermonitoranalysis/synthetic_<masked>?selectedtimeframe=<masked>&actiontype=<masked>&analysistf=<masked>&analysismode=<masked>&analysisoverviewsplitting=<masked>&analysisactiontype=<masked>&parts_details=<masked>&parts_chart=<masked>&parts=<masked>&timeframe=<m","domain":"mySampleEnv.dynatrace.com","targetUrl":"https://mySampleEnv.dynatrace.com/#monitoranalysiskpm;webcheckId=SYNTHETIC_TEST-67444FBB89C6F11B;actionType=Load;splitting=event;analysisTf=custom1622103968000to1622107568000;mode=performance;analysisActionType=Load;gtf=l_2_HOURS","type":"Xhr","startTime":1622107569821,"endTime":1622107570083,"duration":262,"application":"mySampleEnv.dynatrace.com - browser monitor - analysis - 1620645163422","internalApplicationId":"APPLICATION-A8894472DACEDA0E","speedIndex":null,"apdexCategory":"FRUSTRATED","matchingConversionGoals":[],"networkTime":5,"serverTime":65,"frontendTime":192,"documentInteractiveTime":null,"thirdPartyResources":0,"thirdPartyBusyTime":null,"cdnResources":0,"cdnBusyTime":null,"firstPartyResources":5,"firstPartyBusyTime":223,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":1622107569826,"requestStart":3,"responseStart":68,"responseEnd":70,"visuallyCompleteTime":null,"syntheticEvent":"click on \"Analyze performance\"","syntheticEventId":"SYNTHETIC_TEST_STEP-7D9201BEB990247E","keyUserAction":false,"stringProperties":[],"longProperties":[],"doubleProperties":[],"dateProperties":[],"userActionPropertyCount":0,"customErrorCount":0,"javascriptErrorCount":0,"requestErrorCount":1,"largestContentfulPaint":null,"firstInputDelay":null,"totalBlockingTime":null,"cumulativeLayoutShift":null},{"name":"/rest/webcheckdetails/overviewdata/browsermonitoranalysis/synthetic_<masked>?selectedtimeframe=<masked>&actiontype=<masked>&analysistf=<masked>&analysismode=<masked>&analysisoverviewsplitting=<masked>&visitid=<masked>&timestamp=<masked>&analysisactiontype=<masked>&parts=<masked>&timeframe=<masked>&g","domain":"mySampleEnv.dynatrace.com","targetUrl":"https://mySampleEnv.dynatrace.com/#monitoranalysiskpm;webcheckId=SYNTHETIC_TEST-67444FBB89C6F11B;actionType=Load;splitting=event;analysisTf=custom1622103968000to1622107568000;ensureAnalysisTimeframe=true;mode=performance;visitId=623513409;analysisActionType=Load;gtf=l_2_HOURS","type":"Xhr","startTime":1622107572811,"endTime":1622107572911,"duration":100,"application":"mySampleEnv.dynatrace.com - browser monitor - analysis - 1620645163422","internalApplicationId":"APPLICATION-A8894472DACEDA0E","speedIndex":null,"apdexCategory":"SATISFIED","matchingConversionGoals":[],"networkTime":14,"serverTime":61,"frontendTime":25,"documentInteractiveTime":null,"thirdPartyResources":0,"thirdPartyBusyTime":null,"cdnResources":0,"cdnBusyTime":null,"firstPartyResources":2,"firstPartyBusyTime":167,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":1622107572831,"requestStart":12,"responseStart":73,"responseEnd":75,"visuallyCompleteTime":null,"syntheticEvent":"open first execution","syntheticEventId":"SYNTHETIC_TEST_STEP-3A281F8FB8AB3C37","keyUserAction":false,"stringProperties":[],"longProperties":[],"doubleProperties":[],"dateProperties":[],"userActionPropertyCount":0,"customErrorCount":0,"javascriptErrorCount":0,"requestErrorCount":0,"largestContentfulPaint":null,"firstInputDelay":null,"totalBlockingTime":null,"cumulativeLayoutShift":null}],"events":[],"errors":[],"syntheticEvents":[{"name":"navigate to details screen","syntheticEventId":"SYNTHETIC_TEST_STEP-09D1E2CC97B5878B","sequenceNumber":1,"timestamp":1622107547988,"type":"navigate"},{"name":"keystrokes on \"user\"","syntheticEventId":"SYNTHETIC_TEST_STEP-0FCD20FF925F44B1","sequenceNumber":2,"timestamp":1622107550155,"type":"keystrokes"},{"name":"click on next","syntheticEventId":"SYNTHETIC_TEST_STEP-84854E56BAA53321","sequenceNumber":3,"timestamp":1622107551834,"type":"click"},{"name":"keystrokes on \"password\"","syntheticEventId":"SYNTHETIC_TEST_STEP-6CB903FD28430FE6","sequenceNumber":4,"timestamp":1622107553985,"type":"keystrokes"},{"name":"click on login button","syntheticEventId":"SYNTHETIC_TEST_STEP-6400C0C04B6B76E3","sequenceNumber":5,"timestamp":1622107564154,"type":"click"},{"name":"open first event","syntheticEventId":"SYNTHETIC_TEST_STEP-395A7BBE253C8C8C","sequenceNumber":6,"timestamp":1622107566364,"type":"click"},{"name":"select performance part","syntheticEventId":"SYNTHETIC_TEST_STEP-A53F6787F97741F7","sequenceNumber":7,"timestamp":1622107568548,"type":"click"},{"name":"click on \"Analyze performance\"","syntheticEventId":"SYNTHETIC_TEST_STEP-7D9201BEB990247E","sequenceNumber":8,"timestamp":1622107572734,"type":"click"},{"name":"open first execution","syntheticEventId":"SYNTHETIC_TEST_STEP-3A281F8FB8AB3C37","sequenceNumber":9,"timestamp":1622107574905,"type":"click"},{"name":"open screenshot","syntheticEventId":"SYNTHETIC_TEST_STEP-DF43A9A21ADE0E10","sequenceNumber":10,"timestamp":1622107576588,"type":"click"}],"endReason":"END_EVENT","numberOfRageClicks":0,"userExperienceScore":"TOLERATED","connectionType":"UNKNOWN","hasError":true}
```

## Скачивание примера отображения

Чтобы [экспортировать данные пользовательских сессий напрямую в собственный экземпляр Elasticsearch](#send-to-elasticsearch), можно скачать пример отображения (mapping) для индексов. Разверни нужный URL конечной точки на странице **User session exports** и выбери **Download mapping**. Скачанный файл шаблона отображения содержит маппинг для каждого экспортируемого поля.

Созданный пример отображения отражает текущие настройки, поэтому его можно использовать при создании индекса, в который будут экспортироваться данные пользовательских сессий.

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

Пример

```
{



"mappings" : {



"dynamic_templates" : [ {



"string_fields" : {



"match" : "*",



"match_mapping_type" : "string",



"mapping" : {



"norms" : "false",



"type" : "keyword"



}



}



} ],



"properties" : {



"applicationType" : {



"type" : "keyword"



},



"appVersion" : {



"type" : "keyword"



},



// ...



}



}



}
```

## Настройка экспорта сессий через API

Конфигурация экспорта пользовательских сессий хранится с использованием фреймворка Settings 2.0. Он предоставляет REST API, который можно использовать для создания, чтения, обновления и удаления конфигураций экспорта сессий. Подробности см. в разделе [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

* Конечные точки для доступа к Settings API:

  + Для развёртываний Dynatrace Managed: `https://{your-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}`
  + Для Environment ActiveGate: `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}`
* Адрес документации OpenAPI: `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/index.jsp?urls.primaryName=Environment%20API%20v2#/Settings%20-%20Objects`.
* ID схемы для конфигурации экспорта пользовательских сессий: `builtin:elasticsearch.user-session-export-settings-v2`.  
  С этим ID схемы можно, например, прочитать текущую конфигурацию экспорта пользовательских сессий с помощью любого REST-клиента.

  ```
  GET https://{your-domain}/api/v2/settings/objects?schemaIds=builtin:elasticsearch.user-session-export-settings-v2&scopes=tenant&fields=objectId,value
  ```

Чтобы добавить конфигурацию экспорта сессий через REST API

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

За один запрос можно добавить только одну конфигурацию экспорта пользовательских сессий. Если нужно добавить вторую конфигурацию экспорта сессий, отправь новый запрос `POST`.

Подробности об обновлении или удалении объекта настроек см. в разделах [Settings API - PUT an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") и [Settings API - DELETE an object](/managed/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.").

## Проверка конфигурации экспорта сессий

Чтобы проверить конфигурацию экспорта сессий, выполни команду ниже.

```
curl -v -H "Content-Type: application/json" -X PUT -d '{"visitorId":"14804637803609BCTKP776NMJBOIF3R8OD6R0E4NQALJO","visitId":"16229530","startTime":1480463779085,"endTime":1480463784889,"visitType":"SYNTHETIC"}' http://localhost:3000/export/events
```

При необходимости можно задать следующие дополнительные флаги.

* `--insecure` для отключения проверки SSL
* `--http1.1`, если команда возвращает ошибку `REFUSED_STREAM`