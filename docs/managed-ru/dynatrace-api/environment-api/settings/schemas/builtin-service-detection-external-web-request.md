---
title: Settings API - Service detection rules for External Web Requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-request
scraped: 2026-05-12T11:45:25.152716
---

# Settings API - Service detection rules for External Web Requests schema table

# Settings API - Service detection rules for External Web Requests schema table

* Опубликовано 05 декабря 2023 г.

### Правила обнаружения сервисов для External Web Requests (`builtin:service-detection.external-web-request)`

Правила оцениваются сверху вниз, применяется первое совпавшее. Условия правил оцениваются до применения Service Id Contributors. Учтите, что условия не модифицируют атрибуты requests. Если условия совпадают, применяются Service Id Contributors. **Все Contributors, кроме порта, применяются всегда.** Вклад порта можно исключить переключателем. Можно включить трансформацию значений других Service Id Contributors, чтобы управлять тем, какие Services создаются.  
Подробнее о Service detection rules см. [here](https://dt-url.net/9i03b79).

| Schema ID | Группы схемы | Scope |
| --- | --- | --- |
| `builtin:service-detection.external-web-request` | * `group:service-detection` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection.external-web-request` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:service-detection.external-web-request` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:service-detection.external-web-request` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Включено `enabled` | boolean | - | Required |
| Имя правила `name` | text | - | Required |
| Описание `description` | text | - | Optional |
| Management zones `managementZones` | set | Задайте management zone process group, для которого создаётся это правило обнаружения сервиса. Note: в случае external requests/services PG может быть известен не всегда. См. [here](https://dt-url.net/9i03b79) | Required |
| Contributors для идентификатора сервиса `idContributors` | [idContributorsType](#idContributorsType) | Contributors для вычисления Service Identifier. Все Contributors, кроме порта, применяются всегда. Вклад порта можно исключить переключателем. | Required |
| Условия `conditions` | [condition](#condition)[] | Список условий, необходимых для применения правила. Если задано несколько условий, для применения правила должны совпасть **все** для Request. Если условий нет вовсе, правило применяется всегда. Условия оцениваются по атрибутам, но не модифицируют их. | Required |

##### Объект `idContributorsType`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Идентификатор приложения `applicationId` | [serviceIdContributor](#serviceIdContributor) | - | Required |
| URL context root `contextRoot` | [contextIdContributor](#contextIdContributor) | - | Required |
| Публичное доменное имя `publicDomainName` | [publicDomainIdContributor](#publicDomainIdContributor) | - | Required |
| Порт `portForServiceId` | boolean | Позволить порту вносить вклад в Service Id | Required |

##### Объект `condition`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Взять значение этого атрибута `attribute` | text | - | Required |
| Применить эту операцию `compareOperationType` | text | - | Required |
| Значения `textValues` | set | Если задано несколько значений, для совпадения условия должно совпасть хотя бы одно | Required |
| Значения `tagValues` | set | Если задано несколько значений, для совпадения условия должно совпасть хотя бы одно | Required |
| Значение `intValue` | integer | - | Required |
| Значения `intValues` | set | - | Required |
| От `ipRangeFrom` | text | - | Required |
| До `ipRangeTo` | text | - | Required |
| Технология `framework` | Set<[frameworkType](#frameworkType)> | Возможные значения: * `AXIS` * `CXF` * `HESSIAN` * `JAX_WS_RI` * `JBOSS` * `JERSEY` * `PROGRESS` * `RESTEASY` * `RESTLET` * `SPRING` * `TIBCO` * `WEBLOGIC` * `WEBMETHODS` * `WEBSPHERE` * `WINK` | Required |
| Игнорировать регистр `ignoreCase` | boolean | Игнорировать регистр для текстов. | Required |

##### Объект `serviceIdContributor`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Преобразовать это значение перед вкладом в Service Id `enableIdContributor` | boolean | - | Required |
| `serviceIdContributor` | [transformationSet](#transformationSet) | - | Required |

##### Объект `contextIdContributor`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Преобразовать это значение перед вкладом в Service Id `enableIdContributor` | boolean | - | Required |
| `serviceIdContributor` | [contextRoot](#contextRoot) | - | Required |

##### Объект `publicDomainIdContributor`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Преобразовать это значение перед вкладом в Service Id `enableIdContributor` | boolean | - | Required |
| `serviceIdContributor` | [publicDomainTransformationSet](#publicDomainTransformationSet) | - | Required |

##### Объект `transformationSet`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип вклада `contributionType` | enum | Определяет, использовать исходное значение или применить набор преобразований, чтобы переопределить или трансформировать его. Возможные значения: * `OriginalValue` * `OverrideValue` * `TransformValue` | Required |
| Переопределение значения `valueOverride` | [valueOverride](#valueOverride) | Значение, которое будет использовано вместо обнаруженного. | Required |
| Преобразования `transformations` | [transformation](#transformation)[] | Выберите, как трансформировать значение перед вкладом в Service Id. Учтите, все Transformations применяются всегда. Transformations применяются в заданном порядке, выход предыдущей трансформации поступает на вход следующей. Итоговое значение вносит вклад в Service Id и доступно на **Service overview page** в **Properties and tags**. | Required |

##### Объект `contextRoot`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип вклада `contributionType` | enum | Определяет, использовать исходное значение или применить набор преобразований, чтобы переопределить или трансформировать его. Возможные значения: * `OriginalValue` * `OverrideValue` * `TransformValue` * `TransformURL` | Required |
| Переопределение значения `valueOverride` | [valueOverride](#valueOverride) | Значение, которое будет использовано вместо обнаруженного. | Required |
| Сегменты, копируемые из URL path `segmentCount` | integer | Количество сегментов URL, которые сохраняются. URL делится слешами (/), индексация начинается с 1 у context root. Например, если задать 2 для URL `www.dynatrace.com/support/help/dynatrace-api/`, используется значение `support/help`. | Required |
| Преобразования `transformations` | [reducedTransformation](#reducedTransformation)[] | Выберите, как трансформировать значение перед вкладом в Service Id. Учтите, все Transformations применяются всегда. Transformations применяются в заданном порядке, выход предыдущей трансформации поступает на вход следующей. Итоговое значение вносит вклад в Service Id и доступно на **Service overview page** в **Properties and tags**. | Required |

##### Объект `publicDomainTransformationSet`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип вклада `contributionType` | enum | Определяет, использовать исходное значение или применить набор преобразований, чтобы переопределить или трансформировать его. Возможные значения: * `OriginalValue` * `OverrideValue` * `TransformValue` | Required |
| Переопределение значения `valueOverride` | [valueOverride](#valueOverride) | Значение, которое будет использовано вместо обнаруженного. | Required |
| Брать из имени хоста `copyFromHostName` | boolean | Использовать обнаруженное host name вместо доменного имени request. | Required |
| Преобразования `transformations` | [transformation](#transformation)[] | Выберите, как трансформировать значение перед вкладом в Service Id. Учтите, все Transformations применяются всегда. Transformations применяются в заданном порядке, выход предыдущей трансформации поступает на вход следующей. Итоговое значение вносит вклад в Service Id и доступно на **Service overview page** в **Properties and tags**. | Required |

##### Объект `valueOverride`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Значение `value` | text | - | Required |

##### Объект `transformation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип преобразования `transformationType` | enum | Определяет, какой тип преобразования применяется к исходному значению. Возможные значения: * `BEFORE` * `AFTER` * `BETWEEN` * `REPLACE_BETWEEN` * `REMOVE_NUMBERS` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` * `SPLIT_SELECT` * `TAKE_SEGMENTS` | Required |
| префикс `prefix` | text | - | Optional |
| суффикс `suffix` | text | - | Optional |
| замена `replacementValue` | text | - | Optional |
| разделить по `splitDelimiter` | text | - | Optional |
| индекс выбора `selectIndex` | integer | - | Required |
| минимальное количество цифр `minDigitCount` | integer | - | Required |
| включая шестнадцатеричные числа `includeHexNumbers` | boolean | - | Required |
| количество сегментов `segmentCount` | integer | Сколько сегментов нужно взять. | Required |
| брать с конца `takeFromEnd` | boolean | - | Required |

##### Объект `reducedTransformation`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Тип преобразования `transformationType` | enum | Определяет, какой тип преобразования применяется к исходному значению. Возможные значения: * `BEFORE` * `REPLACE_BETWEEN` * `REMOVE_NUMBERS` * `REMOVE_CREDIT_CARDS` * `REMOVE_IBANS` * `REMOVE_IPS` | Required |
| префикс `prefix` | text | - | Optional |
| суффикс `suffix` | text | - | Optional |
| замена `replacementValue` | text | - | Optional |
| минимальное количество цифр `minDigitCount` | integer | - | Required |
| включая шестнадцатеричные числа `includeHexNumbers` | boolean | - | Required |