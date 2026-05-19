---
title: Settings API - Kubernetes Connector schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-kubernetes-connector-connection
scraped: 2026-05-12T11:42:45.297484
---

# Settings API - Kubernetes Connector schema table

# Settings API - Kubernetes Connector schema table

* Published Oct 14, 2024

### Коннектор Kubernetes (`app:dynatrace.kubernetes.connector:connection)`

Доступные подключения для [Kubernetes Connector](https://dt-url.net/qx03q4d). Подключение привязано к кластеру Kubernetes, в котором выполняются действия workflow. Рекомендуем выполнить шаги, описанные [здесь](https://dt-url.net/mf03qvf), с помощью Dynatrace Operator, который автоматически создаёт подключение.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.kubernetes.connector:connection` | - | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.kubernetes.connector:connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.kubernetes.connector:connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.kubernetes.connector:connection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Имя EdgeConnect `name` | text | Имя развёртывания EdgeConnect | Required |
| UID кластера K8s `uid` | text | Псевдо-ID кластера, равный UID namespace kube-system | Required |
| Namespace `namespace` | text | Namespace, в котором развёрнут EdgeConnect | Required |
| Токен `token` | secret | Токен, необходимый EdgeConnect для доступа к токену ServiceAccount. | Required |