---
title: Settings API - Kubernetes Telemetry Enrichment schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-kubernetes-generic-metadata-enrichment
scraped: 2026-05-12T11:47:55.869322
---

# Settings API - Kubernetes Telemetry Enrichment schema table

# Settings API - Kubernetes Telemetry Enrichment schema table

* Published Mar 17, 2025

### Обогащение телеметрии Kubernetes (`builtin:kubernetes.generic.metadata.enrichment)`

Обогащение телеметрии произвольной метадатой для Kubernetes.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:kubernetes.generic.metadata.enrichment` | * `group:cloud-and-virtualization` | `KUBERNETES_CLUSTER` - Kubernetes cluster  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:kubernetes.generic.metadata.enrichment` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:kubernetes.generic.metadata.enrichment` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:kubernetes.generic.metadata.enrichment` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| `rules` | [Rule](#Rule)[] | Обогащение телеметрии Kubernetes позволяет эффективно тегировать данные телеметрии через Kubernetes-метки и аннотации namespace. Кроме того, позволяет тегировать данные для cost allocation и управления правами.  Варианты обогащения:  * **Обогащать телеметрию label/annotation напрямую:** тегируйте данные телеметрии существующими Kubernetes-метками или аннотациями namespace. Они будут доступны как domain-specific поля (например, `k8s.namespace.label.your_key`). Это даёт гибкое pipeline-маршрутизирование, выбор bucket, сегментацию и фильтрацию. * **Security Context и Cost Allocation:** используйте существующие Kubernetes-метки или аннотации namespace как основу для security context или cost allocation. Это даёт гранулярный контроль над правами и поддерживает chargeback-функциональность.  Дополнительная информация:  * Источником могут быть только метки или аннотации уровня namespace. * Можно задать до 20 правил обогащения. * Новые правила могут вступать в силу до 45 минут. * После 45 минут требуется перезапуск pod, чтобы изменения вступили в силу.  Подробнее см. в нашей [documentation](https://dt-url.net/pn22sye). | Required |

##### Объект `Rule`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип метадаты `type` | enum | Возможные значения: * `ANNOTATION` * `LABEL` | Required |
| Источник `source` | text | Источник должен следовать синтаксису ключей Kubernetes-аннотаций и меток, описанному в [Kubernetes documentation](https://dt-url.net/2c02sbn).  `source := (prefix/)?name`  `prefix := a-z0-9 (`/[-a-z0-9]*[a-z0-9]`)?(\.a-z0-9 (`/[-a-z0-9]*[a-z0-9]`)?)*`  `name := ([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9]`  Дополнительно: имя может содержать максимум 63 символа, а общая длина source не должна превышать 75 символов. | Required |
| Обогащать телеметрию label/annotation напрямую `primaryGrailTag` | boolean | Использует ключ аннотации или метки напрямую как имя поля | Optional |
| Цель `target` | enum | Возможные значения: * `dt.security_context` * `dt.cost.product` * `dt.cost.costcenter` | Required |