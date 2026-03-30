---
title: Передача журналов с Cloudflare
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-push-logs-with-cloudflare
scraped: 2026-03-06T21:29:58.548826
---

# Отправка логов через Cloudflare


* Latest Dynatrace

Cloudflare Logpush поддерживает прямую отправку логов в Dynatrace.
Вы можете настроить Logpush через панель управления Cloudflare или через API.

## Предварительные требования

Перед настройкой Cloudflare Logpush вам потребуется следующее:

* Токен API Dynatrace с областью действия `logs.ingest`.
  Подробнее о токенах, их генерации и областях действия см. Dynatrace API — токены и аутентификация.
* Базовый URL-адрес для приёма HTTP-логов Dynatrace.
  Пример базового URL-адреса: `https://abc123.live.dynatrace.com`.

  Это требуется только при настройке Logpush через API.
* Роль Cloudflare с правами редактирования **Log Share**.
  Подробнее см. [Roles](https://developers.cloudflare.com/logs/logpush/permissions/#roles).

Подробнее об API приёма логов Dynatrace см. Log Monitoring API v2 — POST ingest logs.

## Шаги

Настройте Logpush через панель управления Cloudflare или через API.

Назначение API Dynatrace может быть несовместимо с более старыми заданиями.

* Если вы планируете отправлять логи напрямую в Dynatrace, рекомендуется создать новое задание вместо изменения существующего.
* При попытке изменить назначение в существующем задании вы можете столкнуться с ошибками.

### Настройка через панель управления Cloudflare

1. Создание задания Logpush

1. Войдите в [панель управления Cloudflare](https://dash.cloudflare.com/login).
2. Выберите учётную запись Enterprise или домен/зону, которые вы хотите использовать с Logpush.

   * Учётная запись: у вас есть доступ к [наборам данных уровня учётной записи](https://developers.cloudflare.com/logs/reference/log-fields/account/).
   * Домен/зона: у вас есть доступ к [наборам данных уровня зоны](https://developers.cloudflare.com/logs/reference/log-fields/zone/).
3. Перейдите в **Analytics & Logs** > **Logpush**.
4. Нажмите **Create a Logpush job**.

2. Определение конечной точки API Dynatrace

1. Находясь в панели управления Cloudflare, выберите набор данных, который вы хотите отправить в сервис хранения.
2. В разделе **Select a destination** выберите **HTTP Destination** (или **Dynatrace**, если доступно).
3. Введите данные назначения: конечную точку API приёма HTTP-логов Dynatrace для вашей среды, с токеном API Dynatrace и необходимыми заголовками, предоставленными в качестве параметров запроса.

   Пример назначения показан ниже.

   ```
   https://<YOUR_DYNATRACE_ENVIRONMENT>.live.dynatrace.com/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE_API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare
   ```
4. Нажмите **Continue**

3. Конфигурация задания Logpush

1. Находясь в панели управления Cloudflare, выберите набор данных, который вы хотите отправить в сервис хранения.
2. Настройте задание Logpush.

   * **Job name**: введите имя по вашему выбору.
   * **If logs match**: выберите события, которые вы хотите включить или исключить из принимаемых логов.
     Эта опция доступна не для всех наборов данных.
     Подробнее см. [Filters](https://developers.cloudflare.com/logs/logpush/logpush-job/filters/).
   * **Send the following fields**: выберите, какие логи отправлять — все или только определённые поля.
   * **Advanced Options**:

     + Выберите формат временных меток в логах.
       Варианты: `RFC33339` (по умолчанию), `Unix` или `UnixNano`.
     + Выберите определённую частоту выборки или отправляйте случайно выбранный процент логов.
       Подробнее см. [Sampling rate](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#sampling-rate).
     + Включите редактирование для `CVE-2021-44228`.
       Это заменит каждое вхождение `${` на `x{`.
3. После завершения настройки задания нажмите **Submit**.

### Настройка через API

1. Создание задания

Чтобы создать задание, отправьте `POST`-запрос на конечную точку заданий Logpush.
Пример запроса с использованием `cURL` показан в блоке кода ниже:

```
$ curl -s https://api.cloudflare.com/client/v4/zones/<ZONE_TAG>/logpush/jobs -X \


-H "X-Auth-Email: <CLOUDFLARE_EMAIL>" \


-H "X-Auth-Key: <CLOUDFLARE_API_KEY>" \


POST -d '{


"name": "dynatrace",


"logpull_options": "fields=ClientIP,EdgeStartTimestamp,EdgeResponseStatus,EdgeResponseBytes,ClientRequestURI,ClientRequestHost,ClientRequestMethod,ClientRequestPath&timestamps=rfc3339",


"destination_conf": "https://<DYNATRACE_BASE_URL>/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare",


"dataset": "http_requests",


"enabled": true,


"output_options": { "output_type": "ndjson", "batch_prefix": "[", "batch_suffix": "]", "record_delimiter": ","}


}'
```

Замените следующие заполнители соответствующими значениями:

* `name`: используйте имя вашего домена в качестве имени задания. Необязательно.
* `destination_conf`: конечная точка API приёма HTTP-логов Dynatrace для вашей среды, с токеном API Dynatrace и необходимыми заголовками, предоставленными в качестве параметров запроса.

  + `<ZONE_TAG>`: шестнадцатеричный идентификатор, доступный в Cloudflare.
  + `<CLOUDFLARE_EMAIL>`: адрес электронной почты Cloudflare.
  + `<CLOUDFLARE_API_KEY>`: ключ API Cloudflare.
  + `<CLOUDFLARE_BASIC_AUTHORIZATION>`: ключ авторизации Cloudflare.
  + `<DYNATRACE_BASE_URL>`: конечная точка приёма HTTP-логов Dynatrace для вашей среды, как описано в [Предварительных требованиях](#prerequisites).
  + `<DYNATRACE_API_TOKEN>`: токен API с областью действия `logs.ingest`, как описано в [Предварительных требованиях](#prerequisites).
* `dataset`: категория логов, которые вы хотите получать.
  Полный список поддерживаемых наборов данных см. в [Datasets](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/).
* `output_options`: настройка полей, частоты выборки и формата временных меток. Необязательно.
  Подробнее см. [Log Output Options](https://developers.cloudflare.com/logs/logpush/logpush-job/log-output-options/).

Пример JSON-ответа показан в блоке кода ниже.

```
{


"errors": [],


"messages": [],


"result": {


"id": <JOB_ID>,


"dataset": "http_requests",


"enabled": false,


"name": "<DOMAIN_NAME>",


"output_options": {


"field_names": [ "ClientIP", "ClientRequestHost", "ClientRequestMethod", "ClientRequestURI", "ClientRequestPath", "EdgeEndTimestamp", "EdgeResponseBytes", "EdgeResponseStatus", "EdgeStartTimestamp", "RayID"],


"timestamp_format": "rfc3339"


},


"destination_conf": "https://<DYNATRACE_BASE_URL>/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare",


"last_complete": null,


"last_error": null,


"error_message": null


},


"success": true


}
```

2. Активация задания

Чтобы активировать задание, отправьте `PUT`-запрос на конечную точку заданий Logpush.

Пример запроса с использованием `cURL` показан в блоке кода ниже.

* Используйте `<JOB_ID>` из JSON-ответа, как показано в разделе [Создание задания](#create).
* Отправьте `{"enabled": true}` в теле запроса.

```
$ curl --request PUT \


https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/logpush/jobs/{JOB_ID} \


--header "X-Auth-Email: <CLOUDFLARE_EMAIL>" \


--header "X-Auth-Key: <CLOUDFLARE_API_KEY>" \


--header "Content-Type: application/json" \


--data '{


"enabled": true


}'
```

Пример JSON-ответа показан в блоке кода ниже.

```
{


"errors": [],


"messages": [],


"result": {


"id": <JOB_ID>,


"dataset": "http_requests",


"enabled": true,


"name": "<DOMAIN_NAME>",


"output_options": {


"field_names": [ "ClientIP", "ClientRequestHost", "ClientRequestMethod", "ClientRequestURI", "ClientRequestPath", "EdgeEndTimestamp", "EdgeResponseBytes", "EdgeResponseStatus", "EdgeStartTimestamp", "RayID"],


"timestamp_format": "rfc3339"


},


"destination_conf": "https://<YOUR_DYNATRACE_ENVIRONMENT>.live.dynatrace.com/api/v2/logs/ingest?header_Authorization=Api-Token%20<DYNATRACE_API_TOKEN>&header_accept=application/json&header_content-type=application/json&dt.ingest.origin=cloudflare",


"last_error": null,


"error_message": null


},


"success": true


}
```
