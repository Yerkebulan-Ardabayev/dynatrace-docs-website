---
title: Сбор логов AWS Lambda
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector
scraped: 2026-05-12T12:00:13.526654
---

# Сбор логов AWS Lambda

# Сбор логов AWS Lambda

* Практическое руководство
* Чтение: 7 мин
* Обновлено 17 декабря 2025 г.

Dynatrace версия 1.263

Вы можете собирать логи напрямую из ваших функций AWS Lambda и отправлять их в Dynatrace для анализа. Это решение является альтернативой [пересылке логов через CloudWatch](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder "Используйте пересылку логов AWS для приёма логов AWS.") с преимуществами в части стоимости и задержки, а также проще в настройке, особенно если трассировка AWS Lambda уже настроена. В рамках процесса установки OneAgent эта функция предоставляет упрощённое решение для сбора логов из ваших функций Lambda.

## Предварительные условия

* Для слоёв с версией OneAgent 1.263 и ранее, Environment ActiveGate должен иметь доверенный (не самоподписанный) сертификат. Подробнее см. [Пользовательский SSL-сертификат для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на вашем ActiveGate.").

* ActiveGate с включённым модулем Log analytics collector. См. [Log Monitoring API v2 - POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Отправляйте пользовательские логи в Dynatrace через Log Monitoring API v2.").

## Развёртывание

Для функций Lambda на Python, Node.js и Java Dynatrace предоставляет единый Lambda layer, который обеспечивает сбор и трассировки, и логов. Для .NET Dynatrace предоставляет отдельный layer, который собирает только логи.

Сбор логов для функций Lambda на Python, Node.js и Java

Чтобы развернуть Dynatrace Lambda extension, следуйте инструкциям из [Трассировка функций Lambda на Python, Node.js и Java](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Мониторинг функций Lambda, написанных на Python, Node.js и Java.") со следующими двумя отличиями:

1. В разделе **I want to enable** выберите **Traces and Logs**.
2. Либо нажмите **Create token**, чтобы создать новый access token, либо введите [существующий access token с правом `logs.ingest`](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.") в поле **Access Token**.

Если вы ранее использовали Dynatrace Lambda extension без логирования, вам нужно адаптировать Lambda Layer Arn, а также конфигурацию, предоставленную в мастере, добавив необходимые расширения для сборщика логов.

Сбор логов для функций Lambda на .NET

Для функций Lambda на .NET следуйте шагам, описанным в [Мониторинг AWS Lambda с OpenTelemetry](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup "Предварительные условия для мониторинга AWS Lambda с OpenTelemetry") со следующими двумя отличиями:

1. В разделе **I want to enable** выберите **Logs**.
2. Либо нажмите **Create token**, чтобы создать новый access token, либо введите [существующий access token с областью `logs.ingest`](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.") в поле **Access Token**.

Если вы ранее использовали интеграцию трассировки без логирования, вам нужно адаптировать конфигурацию, как указано в мастере, добавив необходимые расширения для сборщика логов.

Отключение Firehose log streaming или CloudWatch log forwarding

Если вы используете их в данный момент, необходимо отключить Firehose log streaming или CloudWatch log forwarding для функций, на которых вы хотите использовать эту функцию сбора логов, чтобы избежать дублирования экспорта логов. См. [Мониторинг логов через AWS log forwarder](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder#unsubscribe "Используйте пересылку логов AWS для приёма логов AWS.") или (lm-stream-logs-with-firehose#unsubscribe).

## Использование

После развёртывания собранные логи для каждого будущего вызова и инициализации функции можно найти в карточке **Related logs** на странице сервиса функции Lambda в Dynatrace, а также в **Log viewer**. Вы можете изучить детали лога, чтобы найти тип лога в атрибуте `telemetryevent.type`, среди прочих метаданных. Обратите внимание, что содержимое логов `platform` будет в формате JSON, а содержимое логов `function` будет в виде простого текста.

### Логи в контексте трассировок

Чтобы коррелировать и видеть логи приложения с трассировками в Dynatrace, необходимо обогащать логи идентификаторами трассировок. Подробнее см. [Логи в контексте трассировок](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/log-enrichment "Настройка обогащения сообщений логов с OpenTelemetry на AWS Lambda.").

## Конфигурация

### Типы событий логов

Dynatrace собирает два [типа событий логов](https://dt-url.net/xd038u5): события platform и логи function. Чтобы настроить, какие типы событий логов собираются, используйте следующий синтаксис.

| Настраивается через | Расположение | Значение по умолчанию | Синтаксис |
| --- | --- | --- | --- |
| JSON-файл | `EventTypes` (свойство в объекте `LogCollection`) | `["platform", "function"]` | Массив строк, например `"function"`[1](#fn-1-1-def) |
| Переменные окружения | `DT_LOG_COLLECTION_EVENT_TYPES` | `platform:function` | Список типов событий логов, разделённый двоеточием, например `function`[1](#fn-1-1-def) |

1

Установите значение `["function"]` (или `function`), чтобы собирать только логи function.

### Endpoint

OneAgent версия 1.275+

Endpoint, используемый для экспорта логов, выводится из base URL вашей конфигурации [экрана развёртывания](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Мониторинг функций Lambda, написанных на Python, Node.js и Java."). Вы можете переопределить значение по умолчанию, установив в override-value location полный URL endpoint, включающий также путь.

| Настраивается через | Default-value location | Override-value location |
| --- | --- | --- |
| JSON-файл | `Connection.BaseUrl` | Добавьте свойство `Endpoint` в объект `LogCollection`. |
| Переменные окружения | `DT_CONNECTION_BASE_URL` | `DT_LOG_COLLECTION_ENDPOINT` |

Environment ActiveGate и значение по умолчанию

Если вы используете Environment ActiveGate, убедитесь, что [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment#environment-id "Поймите, что такое среды мониторинга и как с ними работать.") включён в default value location, или установите его значение в полный URL endpoint приёма логов (например, `https://{activegate-host}:9999/e/{your-environment-id}/api/v2/logs/ingest`).

Если вы используете Environment ActiveGate (что обычно так и есть, если вы развернули ActiveGate самостоятельно) и у вас нет `/e/{your-environment-id}` в составе `DT_CONNECTION_BASE_URL` (`Connection.BaseUrl`), вам нужно установить либо

* переменную окружения `DT_LOG_COLLECTION_ENDPOINT`
* либо JSON-свойство `LogCollection.Endpoint`

в полный URL endpoint приёма логов (т.е. `https://{activegate-host}:9999/e/{your-environment-id}/api/v2/logs/ingest`).
[Идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment#environment-id "Поймите, что такое среды мониторинга и как с ними работать.") обычно совпадает с tenant ID.

### Получение токена из AWS Secrets Manager

OneAgent версия 1.295+

Вместо явного указания токена аутентификации в конфигурации, вы можете настроить OneAgent на получение токена, хранящегося в [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager).

Предварительные условия

* Убедитесь, что вы предоставили разрешение `secretsmanager:GetSecretValue` для ARN секрета токена аутентификации функции Lambda, мониторируемой OneAgent. Подробности см. в [Authentication and access control for AWS Secrets Manager](https://dt-url.net/7n03p10) в документации AWS Secrets Manager.
* Убедитесь, что значение секрета содержит только plaintext-значение токена аутентификации (без кавычек). Обратите внимание, что

  + Секреты со структурой JSON не поддерживаются. Подробности см. в [Create an AWS Secrets Manager secret](https://dt-url.net/fy23pdx) в документации AWS Secrets Manager.
  + При получении значения секрета Secrets Manager по умолчанию возвращает только текущую версию секрета (метка `AWSCURRENT`). Подробности см. в [What's in a Secrets Manager secret?](https://dt-url.net/1f43pq8) в документации AWS Secrets Manager.

Чтобы получить токен для сбора логов, установите ARN секрета токена либо в переменную окружения `DT_LOG_COLLECTION_AUTH_TOKEN_SECRETS_MANAGER_ARN`, либо в JSON-свойство `LogCollection.AuthTokenSecretsManagerArn`.

Эта опция всегда переопределяет `DT_LOG_COLLECTION_AUTH_TOKEN` (`LogCollection.AuthToken`). Если получение не удастся, сборщик логов не сможет экспортировать данные логов.

Получение обращается к AWS Secrets Manager только один раз, во время фазы инициализации функции Lambda; это вызывает увеличение длительности холодного старта функции Lambda.

Чтобы [получить токен для соединения трассировки](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#aws-secrets-manager "Мониторинг функций Lambda, написанных на Python, Node.js и Java."), настройте другое получение.

### Фильтрация

OneAgent версия 1.291+

По умолчанию логи для настроенных типов событий собираются для всех следующих уровней логирования, отсортированных от низшего к высшему:

* `TRACE`
* `DEBUG`
* `INFO`
* `WARN`
* `ERROR`
* `FATAL`

Подробнее см. [AWS log-level filtering](https://dt-url.net/h503n1u).

Чтобы настроить, с какого уровня начинать сбор логов, например, начиная с уровня `WARN`, установите фильтр, используя следующий синтаксис.

| Настраивается через | Расположение | Синтаксис |
| --- | --- | --- |
| JSON-файл | `LogCollection.Filter.MinLevel` (объект `LogCollection` имеет свойство `Filter`, которое имеет свойство `MinLevel`) | `<Log level>`  **Пример:** `{"LogCollection": {"Filter": {"MinLevel": "WARN" }}}` |
| Переменные окружения | `DT_LOG_COLLECTION_FILTER_MIN_LEVEL` | `<Log level>`  **Пример:** `WARN` |

Например, если `<Log level>` равен `WARN`

* Логи уровней `TRACE`, `DEBUG` и `INFO` не собираются.
* Логи уровней `WARN`, `ERROR` и `FATAL` собираются.

Чтобы настроить фильтры сбора логов непосредственно в AWS, см. [Using Amazon CloudWatch Logs with AWS Lambda](https://dt-url.net/h503n1u). Учтите, что при этой опции

* Логи не отображаются в CloudWatch.
* Dynatrace не будет собирать логи, которые уже отфильтрованы в AWS.

## Ограничения

* Тип события `extension` в настоящее время не поддерживается: если вы попытаетесь настроить тип события `extension`, будет показана ошибка и сбор логов не начнётся.
* В классической интеграции AWS Lambda логи, собранные сборщиком логов, не связываются с трассировками и не отображаются в представлении трассировки на вкладке **Logs**, а будут показаны только в карточке **Related logs** или в **Log viewer**. Однако вы можете использовать [ручное обогащение логов](/managed/upgrade/unavailable-in-managed "Этот вариант недоступен в Dynatrace Managed."), чтобы связать логи функции с вашими трассировками. См. [Логи AWS Lambda в контексте трассировок](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/log-enrichment "Настройка обогащения сообщений логов с OpenTelemetry на AWS Lambda.") для примеров ручного обогащения логов по конкретным языкам.
* При использовании актуальной интеграции AWS Lambda автоматическое обогащение логов доступно для структурированных логов, выводимых поддерживаемыми фреймворками логирования.
* Если событие лога AWS не имеет уровня лога, а сообщение лога содержит строку `[error]` или `[ERROR]`, уровень лога будет установлен в `ERROR`. В противном случае используется уровень `INFO`.
* Мы не рекомендуем комбинировать отдельный слой сборщика с слоем OneAgent. Если вам нужны трассировка и сбор логов для ваших функций Lambda, используйте вместо этого комбинированный слой **Traces and Logs**.

* Переменную окружения `DT_CONNECTION_BASE_URL` нельзя скопировать с экрана развёртывания. Вместо этого значение `DT_CONNECTION_BASE_URL` должно быть установлено в URL вида `https://{activegate-host}:9999/e/{your-environment-id}`.

## Устранение неполадок

* [Dynatrace does not ingest logs (HTTP 429)](https://dt-url.net/hm23mng)

## Связанные темы

* [Трассировка функций Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions "Мониторинг функций AWS Lambda.")
* [Мониторинг логов через AWS log forwarder](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder "Используйте пересылку логов AWS для приёма логов AWS.")