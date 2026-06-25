---
title: Kubernetes credentials API - POST new credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/post-new-credentials
scraped: 2026-05-12T12:14:54.136925
---

# Kubernetes credentials API - POST new credentials

# Kubernetes credentials API - POST new credentials

* Reference
* Published Jul 22, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema [Kubernetes connection settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "Просмотр таблицы schema builtin:cloud.kubernetes окружения мониторинга через Dynatrace API.") (`builtin:cloud.kubernetes`) и [Kubernetes platform monitoring settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "Просмотр таблицы schema builtin:cloud.kubernetes.monitoring окружения мониторинга через Dynatrace API.") (`builtin:cloud.kubernetes.monitoring`).

Создаёт новую конфигурацию Kubernetes credentials.

В теле не должно быть ID, Dynatrace Server назначает его автоматически.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [KubernetesCredentials](#openapi-definition-KubernetesCredentials) | JSON-тело запроса с параметрами новой конфигурации Kubernetes credentials. | body | Optional |

### Объекты тела запроса

#### Объект `KubernetesCredentials`

Конфигурация для конкретных Kubernetes credentials.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| active | boolean | Мониторинг включён (`true`) или выключен (`false`) для данной конфигурации credentials.  Если не задано при создании, используется значение `true`.  Если поле опущено при обновлении, прежнее значение сохраняется. | Optional |
| activeGateGroup | string | Active Gate group для фильтрации active gates под эти credentials. | Optional |
| authToken | string | Service account bearer token для Kubernetes API server.  Передавайте токен при создании или обновлении конфигурации. По соображениям безопасности GET-запросы возвращают это поле как `null`.  Если поле опущено при обновлении, прежнее значение сохраняется. | Optional |
| certificateCheckEnabled | boolean | Проверка SSL-сертификатов включена (`true`) или выключена (`false`) для Kubernetes-кластера.  Если не задано при создании, используется значение `true`.  Если поле опущено при обновлении, прежнее значение сохраняется. | Optional |
| davisEventsIntegrationEnabled | boolean | Включение всех событий, релевантных для Davis, включено (`true`) или выключено (`false`) для Kubernetes-кластера. Если поле опущено при обновлении, прежнее значение сохраняется. | Optional |
| endpointStatus | string | Статус настроенного endpoint.  ASSIGNED: credentials назначены ActiveGate, который отвечает за обработку. UNASSIGNED: credentials ещё не назначены ActiveGate, обработка пока не идёт. DISABLED: credentials отключены пользователем. FASTCHECK\_AUTH\_ERROR: credentials невалидны. FASTCHECK\_TLS\_ERROR: TLS-сертификат endpoint невалиден. FASTCHECK\_NO\_RESPONSE: endpoint не вернул результат до таймаута. FASTCHECK\_INVALID\_ENDPOINT: URL endpoint невалиден. FASTCHECK\_AUTH\_LOCKED: credentials, похоже, заблокированы. UNKNOWN: произошла неизвестная ошибка. Возможные значения: * `ASSIGNED` * `DISABLED` * `FASTCHECK_AUTH_ERROR` * `FASTCHECK_AUTH_LOCKED` * `FASTCHECK_INVALID_ENDPOINT` * `FASTCHECK_LOW_MEMORY_ERROR` * `FASTCHECK_MISCONFIGURED_AWS_ROLE` * `FASTCHECK_MISSING_AWS_ROLE` * `FASTCHECK_NO_RESPONSE` * `FASTCHECK_TLS_ERROR` * `FASTCHECK_TOO_BIG_ENVIRONMENT` * `FASTCHECK_TOO_MANY_SUBSCRIPTIONS` * `UNASSIGNED` * `UNKNOWN` | Optional |
| endpointStatusInfo | string | Детальная информация о статусе настроенного endpoint. | Optional |
| endpointUrl | string | URL Kubernetes API server.  Должен быть уникален в рамках Dynatrace-окружения.  URL должен быть валидным по RFC 2396. Ведущие и хвостовые пробелы не допускаются. | Required |
| eventAnalysisAndAlertingEnabled | boolean | [Deprecated] С версии 1.240 EA events monitoring устарел и заменён GA-версией events, которая делает это поле устаревшим.  Соответствует значению `eventsIntegrationEnabled`.  Поле игнорируется при обновлении, прежнее значение сохраняется. | Optional |
| eventsFieldSelectors | [KubernetesEventPattern[]](#openapi-definition-KubernetesEventPattern) | Фильтры событий Kubernetes на основе field-selectors. Если задано `null` при создании, подписка на field selectors не оформляется. Если задано `null` при обновлении, изменение сохранённых field selectors не выполняется. Чтобы очистить все field selectors, передайте пустой список. | Optional |
| eventsIntegrationEnabled | boolean | Мониторинг событий включён (`true`) или выключен (`false`) для Kubernetes-кластера. Мониторинг событий требует, чтобы active-флаг этой конфигурации был `true`.  Если не задано при создании, используется значение `false`.  Если поле опущено при обновлении, прежнее значение сохраняется. | Optional |
| id | string | ID данной конфигурации credentials. | Optional |
| label | string | Имя конфигурации Kubernetes credentials.  Допустимые символы: буквы, цифры, пробелы и `.+-_`. Ведущие и хвостовые пробелы не допускаются. | Required |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| prometheusExportersIntegrationEnabled | boolean | Интеграция Prometheus exporters включена (`true`) или выключена (`false`) для Kubernetes-кластера. Если поле опущено при обновлении, прежнее значение сохраняется. | Optional |
| workloadIntegrationEnabled | boolean | Обработка workloads и cloud applications включена (`true`) или выключена (`false`) для Kubernetes-кластера. Если поле опущено при обновлении, прежнее значение сохраняется. | Optional |

#### Объект `KubernetesEventPattern`

Один Kubernetes events field selector (= фильтр событий на основе K8s field selector).

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| active | boolean | Включена ли подписка на этот field selector событий (значение `true`). Если выключена (`false`), Dynatrace перестанет забирать события из Kubernetes API для этого field selector | Required |
| fieldSelector | string | Строка field selector (применяется url decoding при сохранении). | Required |
| label | string | Метка для field selector событий. | Required |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"active": true,



"activeGateGroup": "group-1",



"authToken": "abcd9876",



"certificateCheckEnabled": true,



"davisEventsIntegrationEnabled": true,



"endpointUrl": "https://k8s-api.sample.org",



"eventAnalysisAndAlertingEnabled": true,



"eventsFieldSelectors": [



{



"active": true,



"fieldSelector": "involvedObject.kind=Node",



"label": "Node events"



}



],



"eventsIntegrationEnabled": true,



"hostnameVerificationEnabled": true,



"id": "KUBERNETES_CLUSTER-CC06304728FC9396",



"label": "K8s credentials - REST example",



"prometheusExportersIntegrationEnabled": true,



"workloadIntegrationEnabled": true



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Новая конфигурация Kubernetes credentials создана. Тело ответа содержит ID конфигурации. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Связанные темы

* [Explore Kubernetes in Dynatrace Hub](https://www.dynatrace.com/hub/?filter=kubernetes&utm_source=doc&utm_medium=link&utm_campaign=cross)