---
title: Settings API - Connection settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes
scraped: 2026-05-12T11:49:38.404675
---

# Settings API - Connection settings schema table

# Settings API - Connection settings schema table

* Published Dec 05, 2023

### Параметры подключения (`builtin:cloud.kubernetes)`

Подключайтесь к Kubernetes или OpenShift для расширенной наблюдаемости. Подробнее о Kubernetes или OpenShift см. в нашей документации.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:cloud.kubernetes` | - | `KUBERNETES_CLUSTER` - Kubernetes cluster |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.kubernetes` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:cloud.kubernetes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.kubernetes` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя `label` | text | Переименование кластера ломает конфигурации, опирающиеся на его имя (например, management zones и alerting). | Required |
| Подключить контейнеризованный ActiveGate к локальному endpoint Kubernetes API `clusterIdEnabled` | boolean | Подробнее о мониторинге локального Kubernetes API см. [documentation](https://dt-url.net/6q62uep).  Включите этот переключатель, если ActiveGate развёрнут в тех же Kubernetes-кластерах, которые вы хотите мониторить. Отключите, если хотите мониторить другой Kubernetes-кластер. | Required |
| ID Kubernetes-кластера `clusterId` | text | Уникальный ID кластера, в котором развёрнут контейнеризованный ActiveGate. По умолчанию равен UUID namespace kube-system. ID кластера контейнеризованного ActiveGate показан на экране Deployment status. | Required |
| URL Kubernetes API `endpointUrl` | text | Получите API URL для [Kubernetes](https://dt-url.net/kz23snj "Kubernetes") или [OpenShift](https://dt-url.net/d623xgw "OpenShift"). | Required |
| Bearer-токен Kubernetes `authToken` | secret | Создайте bearer-токен для [Kubernetes](https://dt-url.net/og43szq "Kubernetes") или [OpenShift](https://dt-url.net/7l43xtp "OpenShift"). | Required |
| Группа ActiveGate `activeGateGroup` | text | - | Optional |
| Требовать валидные сертификаты для связи с API-сервером (рекомендуется) `certificateCheckEnabled` | boolean | - | Required |
| Проверять имя хоста в сертификате с URL Kubernetes API `hostnameVerificationEnabled` | boolean | - | Required |