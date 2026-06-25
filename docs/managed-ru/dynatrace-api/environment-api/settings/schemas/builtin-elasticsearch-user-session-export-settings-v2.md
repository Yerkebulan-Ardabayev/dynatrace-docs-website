---
title: Settings API - User session exports schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-elasticsearch-user-session-export-settings-v2
scraped: 2026-05-12T11:48:24.723456
---

# Settings API - User session exports schema table

# Settings API - User session exports schema table

* Published Dec 05, 2023

### Экспорт user-сессий (`builtin:elasticsearch.user-session-export-settings-v2)`

User session export позволяет передавать данные real user monitoring из Dynatrace во внешний источник данных, где их можно использовать как вход для big data analytics или для увеличения срока хранения данных.

В потоковые данные входят все user sessions, user actions, события и высокоуровневые тайминги и данные об ошибках.

Используйте существующую analytics-инфраструктуру для ad-hoc анализа большого количества user-сессий и объединяйте эти данные с данными из других источников.

После включения user session export автоматически отправляет JSON-данные обо всех мониторимых user-сессиях вашего окружения на настроенный HTTPS-эндпоинт.

Также можно фильтровать по management zone отдельно для каждого user session export.
Можно задать до трёх user session export, чтобы отправлять конкретные данные на разные эндпоинты.

Подробнее см. [Configure user session exports](https://dt-url.net/user-session-exports).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:elasticsearch.user-session-export-settings-v2` | * `group:integration.external` * `group:integration` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:elasticsearch.user-session-export-settings-v2` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:elasticsearch.user-session-export-settings-v2` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:elasticsearch.user-session-export-settings-v2` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Задайте эндпоинт `endpointDefinition` | [EndpointDefinition](#EndpointDefinition) | Dynatrace будет периодически отправлять JSON-данные на этот эндпоинт. Также можно поставить эндпоинт на паузу или отключить, чтобы остановить поток данных из Dynatrace. | Required |
| Authentication `authentication` | [Authentication](#Authentication) | Dynatrace может автоматически отправлять bulk-данные в Elasticsearch. Для защиты доступа можно использовать SSL-сертификат, basic authentication или OAuth 2.0. Для установок Dynatrace SaaS instance Elasticsearch должен быть публично доступен из Dynatrace Cluster. | Required |
| Отправлять данные напрямую в Elasticsearch `sendDirect` | [SendDirect](#SendDirect) | Активируйте, если хотите экспортировать данные user-сессий в собственный кластер Elasticsearch. Если у вас Elasticsearch 7, обязательно укажите \_doc как type. Для Elasticsearch 8 type не указывайте. Если всё же хотите использовать type, добавьте include\_type\_name=true при создании индекса Elasticsearch. Подробнее в Dynatrace help. | Required |
| Scope экспорта, оповещения и расширенная настройка `exportBehavior` | [ExportBehavior](#ExportBehavior) | Задайте scope экспорта через конкретную management zone. Также можно отключить UI-уведомления о неудачных экспортах или добавить специальные параметры, предоставленные Dynatrace support для troubleshooting. | Required |

##### Объект `EndpointDefinition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| URL эндпоинта `endpointUrl` | text | - | Required |
| Включить user session export `enableUserSessionExport` | boolean | - | Required |
| Content type `contentType` | text | - | Required |
| Использовать метод POST (вместо PUT) `usePost` | boolean | - | Required |

##### Объект `Authentication`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Активировать `active` | boolean | - | Required |
| Тип аутентификации `authType` | enum | Возможные значения: * `basic` * `oauth2` | Required |
| Basic authentication `basicAuth` | [BasicAuth](#BasicAuth) | - | Required |
| OAuth 2.0 (Early Adopter) `oAuth2` | [OAuth2](#OAuth2) | - | Required |

##### Объект `SendDirect`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Активировать `active` | boolean | - | Required |
| Имя индекса, куда отправляются данные `indexName` | text | - | Required |
| Тип документов в индексе Elasticsearch `docType` | text | - | Optional |

##### Объект `ExportBehavior`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Management zone `managementZone` | setting | Ограничить экспортируемые сессии конкретной management zone | Optional |
| Отключить уведомления `disableNotification` | boolean | - | Required |
| Пользовательские свойства конфигурации `customConfiguration` | text | Здесь можно задать дополнительные свойства для этой конфигурации экспорта. Изменять эти значения может понадобиться только в редких случаях. До изменения этого поля свяжитесь с поддержкой. | Optional |

##### Объект `BasicAuth`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя пользователя `username` | text | - | Required |
| Пароль `password` | secret | - | Required |

##### Объект `OAuth2`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Grant type `grantType` | enum | Возможные значения: * `clientCredentials` | Required |
| URL access token `accessTokenUrl` | text | - | Required |
| Client ID `clientId` | text | - | Required |
| Client secret `clientSecret` | secret | - | Required |
| Scope `scope` | text | Запрашиваемый scope доступа | Optional |
| Отправлять credentials `sendCredentials` | enum | Возможные значения: * `header` | Required |