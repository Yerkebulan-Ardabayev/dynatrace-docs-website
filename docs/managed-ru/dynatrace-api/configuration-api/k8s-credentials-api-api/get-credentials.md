---
title: Kubernetes credentials API - GET credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/get-credentials
scraped: 2026-05-12T12:14:58.186248
---

# Kubernetes credentials API - GET credentials

# Kubernetes credentials API - GET credentials

* Reference
* Published Jul 22, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema [Kubernetes connection settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "Просмотр таблицы schema builtin:cloud.kubernetes окружения мониторинга через Dynatrace API.") (`builtin:cloud.kubernetes`) и [Kubernetes platform monitoring settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "Просмотр таблицы schema builtin:cloud.kubernetes.monitoring окружения мониторинга через Dynatrace API.") (`builtin:cloud.kubernetes.monitoring`).

Возвращает конфигурацию указанных Kubernetes credentials.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID нужной конфигурации Kubernetes credentials. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [KubernetesCredentials](#openapi-definition-KubernetesCredentials) | Успех |

### Объекты тела ответа

#### Объект `KubernetesCredentials`

Конфигурация для конкретных Kubernetes credentials.

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | boolean | Мониторинг включён (`true`) или выключен (`false`) для данной конфигурации credentials.  Если не задано при создании, используется значение `true`.  Если поле опущено при обновлении, прежнее значение сохраняется. |
| activeGateGroup | string | Active Gate group для фильтрации active gates под эти credentials. |
| authToken | string | Service account bearer token для Kubernetes API server.  Передавайте токен при создании или обновлении конфигурации. По соображениям безопасности GET-запросы возвращают это поле как `null`.  Если поле опущено при обновлении, прежнее значение сохраняется. |
| certificateCheckEnabled | boolean | Проверка SSL-сертификатов включена (`true`) или выключена (`false`) для Kubernetes-кластера.  Если не задано при создании, используется значение `true`.  Если поле опущено при обновлении, прежнее значение сохраняется. |
| davisEventsIntegrationEnabled | boolean | Включение всех событий, релевантных для Davis, включено (`true`) или выключено (`false`) для Kubernetes-кластера. Если поле опущено при обновлении, прежнее значение сохраняется. |
| endpointStatus | string | Статус настроенного endpoint.  ASSIGNED: credentials назначены ActiveGate, который отвечает за обработку. UNASSIGNED: credentials ещё не назначены ActiveGate, обработка пока не идёт. DISABLED: credentials отключены пользователем. FASTCHECK\_AUTH\_ERROR: credentials невалидны. FASTCHECK\_TLS\_ERROR: TLS-сертификат endpoint невалиден. FASTCHECK\_NO\_RESPONSE: endpoint не вернул результат до таймаута. FASTCHECK\_INVALID\_ENDPOINT: URL endpoint невалиден. FASTCHECK\_AUTH\_LOCKED: credentials, похоже, заблокированы. UNKNOWN: произошла неизвестная ошибка. Возможные значения: * `ASSIGNED` * `DISABLED` * `FASTCHECK_AUTH_ERROR` * `FASTCHECK_AUTH_LOCKED` * `FASTCHECK_INVALID_ENDPOINT` * `FASTCHECK_LOW_MEMORY_ERROR` * `FASTCHECK_MISCONFIGURED_AWS_ROLE` * `FASTCHECK_MISSING_AWS_ROLE` * `FASTCHECK_NO_RESPONSE` * `FASTCHECK_TLS_ERROR` * `FASTCHECK_TOO_BIG_ENVIRONMENT` * `FASTCHECK_TOO_MANY_SUBSCRIPTIONS` * `UNASSIGNED` * `UNKNOWN` |
| endpointStatusInfo | string | Детальная информация о статусе настроенного endpoint. |
| endpointUrl | string | URL Kubernetes API server.  Должен быть уникален в рамках Dynatrace-окружения.  URL должен быть валидным по RFC 2396. Ведущие и хвостовые пробелы не допускаются. |
| eventAnalysisAndAlertingEnabled | boolean | [Deprecated] С версии 1.240 EA events monitoring устарел и заменён GA-версией events, которая делает это поле устаревшим.  Соответствует значению `eventsIntegrationEnabled`.  Поле игнорируется при обновлении, прежнее значение сохраняется. |
| eventsFieldSelectors | [KubernetesEventPattern[]](#openapi-definition-KubernetesEventPattern) | Фильтры событий Kubernetes на основе field-selectors. Если задано `null` при создании, подписка на field selectors не оформляется. Если задано `null` при обновлении, изменение сохранённых field selectors не выполняется. Чтобы очистить все field selectors, передайте пустой список. |
| eventsIntegrationEnabled | boolean | Мониторинг событий включён (`true`) или выключен (`false`) для Kubernetes-кластера. Мониторинг событий требует, чтобы active-флаг этой конфигурации был `true`.  Если не задано при создании, используется значение `false`.  Если поле опущено при обновлении, прежнее значение сохраняется. |
| id | string | ID данной конфигурации credentials. |
| label | string | Имя конфигурации Kubernetes credentials.  Допустимые символы: буквы, цифры, пробелы и `.+-_`. Ведущие и хвостовые пробелы не допускаются. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| prometheusExportersIntegrationEnabled | boolean | Интеграция Prometheus exporters включена (`true`) или выключена (`false`) для Kubernetes-кластера. Если поле опущено при обновлении, прежнее значение сохраняется. |
| workloadIntegrationEnabled | boolean | Обработка workloads и cloud applications включена (`true`) или выключена (`false`) для Kubernetes-кластера. Если поле опущено при обновлении, прежнее значение сохраняется. |

#### Объект `KubernetesEventPattern`

Один Kubernetes events field selector (= фильтр событий на основе K8s field selector).

| Элемент | Тип | Описание |
| --- | --- | --- |
| active | boolean | Включена ли подписка на этот field selector событий (значение `true`). Если выключена (`false`), Dynatrace перестанет забирать события из Kubernetes API для этого field selector |
| fieldSelector | string | Строка field selector (применяется url decoding при сохранении). |
| label | string | Метка для field selector событий. |

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

## Связанные темы

* [Explore Kubernetes in Dynatrace Hub](https://www.dynatrace.com/hub/?filter=kubernetes&utm_source=doc&utm_medium=link&utm_campaign=cross)