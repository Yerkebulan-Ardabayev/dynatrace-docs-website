---
title: GET cluster license and billed usage
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-license/get-cluster-license-usage
scraped: 2026-05-12T11:35:23.340597
---

# GET cluster license and billed usage

# GET cluster license and billed usage

* Reference
* Updated on Mar 06, 2026

Dynatrace Managed версии 1.326+

Получает детали лицензии кластера и оплаченное потребление.

* Этот API совместим только с классической лицензией Dynatrace.
* Возвращаемые данные о потреблении содержат только потребление текущего контракта.
* Данные оплаченного потребления отстают примерно на 2 часа от текущего потребления.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/clusterLicense`

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ClusterLicense](#openapi-definition-ClusterLicense) | Операция выполнена успешно. |

### Объекты тела ответа

#### Объект `ClusterLicense`

| Элемент | Тип | Описание |
| --- | --- | --- |
| accountName | string | Имя аккаунта |
| clusterId | string | ID кластера |
| contactEmailAddress | string | Контактный email |
| lastBillingTime | string | Время последнего обновления данных биллинга |
| licenseExpirationTime | string | Дата истечения лицензии |
| licenseKey | string | Ключ лицензии |
| licenseName | string | Имя лицензии |
| licenseStatus | string | Статус лицензии |
| licenseType | string | Тип лицензии |
| productVersion | string | Текущая версия |
| usageOfDduUnits | [LicenseUsageOfUnit](#openapi-definition-LicenseUsageOfUnit) | Потребление лицензии кластера в Davis data units (DDU) |
| usageOfDemUnits | [LicenseUsageOfUnit](#openapi-definition-LicenseUsageOfUnit) | Потребление лицензии кластера в Davis data units (DDU) |
| usageOfHostUnits | [LicenseUsageOfUnit](#openapi-definition-LicenseUsageOfUnit) | Потребление лицензии кластера в Davis data units (DDU) |

#### Объект `LicenseUsageOfUnit`

Потребление лицензии кластера в Davis data units (DDU)

| Элемент | Тип | Описание |
| --- | --- | --- |
| overageUsage | [OverageUsageOfUnit](#openapi-definition-OverageUsageOfUnit) | Превышение, если применимо |
| quota | integer | Квота лицензии кластера |
| remaining | number | Остаток квоты |
| remainingPercent | number | Остаток квоты в процентах |
| usage | number | Текущее потребление квоты |
| usagePercent | number | Текущее потребление квоты в процентах |
| usageStatus | string | Текущий статус потребления лицензии. Возможные значения: * `OVERAGE_QUOTA_REACHED` * `QUOTA_REACHED` * `USING_OVERAGE` * `USING_QUOTA` |

#### Объект `OverageUsageOfUnit`

Превышение, если применимо

| Элемент | Тип | Описание |
| --- | --- | --- |
| overageQuota | integer | Квота превышения, если задана; null если нет |
| overageUsage | number | Использованное превышение |
| overageUsagePercent | number | Использованное превышение в процентах (заполняется только если задан лимит превышения) |
| remainingOverage | number | Остаток превышения (заполняется только если задан лимит превышения) |
| remainingOveragePercent | number | Остаток превышения в процентах (заполняется только если задан лимит превышения) |

### JSON-модели тела ответа

```
{



"accountName": "string",



"clusterId": "string",



"contactEmailAddress": "string",



"lastBillingTime": "string",



"licenseExpirationTime": "string",



"licenseKey": "string",



"licenseName": "string",



"licenseStatus": "string",



"licenseType": "string",



"productVersion": "string",



"usageOfDduUnits": {



"overageUsage": {



"overageQuota": 1,



"overageUsage": 1,



"overageUsagePercent": 1,



"remainingOverage": 1,



"remainingOveragePercent": 1



},



"quota": 1,



"remaining": 1,



"remainingPercent": 1,



"usage": 1,



"usagePercent": 1,



"usageStatus": "OVERAGE_QUOTA_REACHED"



},



"usageOfDemUnits": {},



"usageOfHostUnits": {}



}
```