---
title: Synthetic locations API - JSON-модели
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/json-models
scraped: 2026-05-12T12:09:49.350258
---

# Synthetic locations API - JSON-модели

# Synthetic locations API - JSON-модели

* Справочник
* Опубликовано 13 июля 2020 г.

Некоторые JSON-модели API **Synthetic locations** различаются в зависимости от их **type**. Здесь приведены JSON-модели для каждой вариации.

## Вариации объекта `SyntheticLocation`

Объект `SyntheticLocation`, это база для синтетических локаций. Фактический набор полей зависит от **type** локации.

### CLUSTER и PRIVATE

PrivateSyntheticLocation

Параметры

JSON-модель

#### Объект `PrivateSyntheticLocation`

Конфигурация приватной синтетической локации.

Параметры **countryCode**, **regionCode**, **city** необязательны, так как их можно получить на основе **latitude** и **longitude** локации.

| Поле | Тип | Описание |
| --- | --- | --- |
| autoUpdateChromium | boolean | Свойство неконтейнеризированной локации. Авто-обновление Chromium включено (`true`) или отключено (`false`). |
| availabilityLocationOutage | boolean | Оповещение о недоступности локации включено (`true`) или отключено (`false`). Поддерживается только для приватных синтетических локаций. |
| availabilityNodeOutage | boolean | Оповещение о недоступности узла включено (`true`) или отключено (`false`). \n\n Если включено, недоступность *любого* узла в локации вызывает алерт. Поддерживается только для приватных синтетических локаций. |
| availabilityNotificationsEnabled | boolean | Уведомления о недоступности локации и узла включены (`true`) или отключены (`false`). Поддерживается только для приватных синтетических локаций. |
| browserExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение описывает, будут ли браузерные мониторы выполняться на этой локации:  * `false`: выполнение браузерных мониторов отключено. * `true`: выполнение браузерных мониторов включено. |
| deploymentType | string | Тип развёртывания локации:  * `STANDARD`: локация развёрнута на Windows или Linux. * `KUBERNETES`: локация развёрнута на Kubernetes. Поле может принимать значения: * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` |
| fipsMode | string | Свойство контейнеризированной локации, указывающее, включён ли на этой локации режим FIPS:  * `DISABLED`: FIPS не включён на локации. * `ENABLED`: FIPS включён на локации. * `ENABLED_WITH_CORPORATE_PROXY`: FIPS с корпоративным прокси включён на этой локации.   По умолчанию: DISABLED Поле может принимать значения: * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` |
| locationNodeOutageDelayInMinutes | integer | Алерт, если недоступность локации или узла длится дольше *X* минут. \n\n Применимо только если `availabilityLocationOutage` или `availabilityNodeOutage` установлено в `true`. Поддерживается только для приватных синтетических локаций. |
| maxActiveGateCount | integer | Свойство контейнеризированной локации. Максимальное число ActiveGate, развёрнутых для локации (требуется для Kubernetes-локации). |
| minActiveGateCount | integer | Свойство контейнеризированной локации. Минимальное число ActiveGate, развёрнутых для локации (требуется для Kubernetes-локации). |
| namExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение описывает, будут ли icmp-мониторы выполняться на этой локации:  * `false`: выполнение icmp-мониторов отключено. * `true`: выполнение icmp-мониторов включено. |
| nodeSize | string | Свойство контейнеризированной локации. Размер контейнеризированного узла, развёрнутого для локации (требуется для Kubernetes-локации). Допустимые значения:  * `XS`: extra small * `S`: small * `M`: medium   Размер узла `L` не поддерживается в контейнеризированных локациях. Поле может принимать значения: * `M` * `S` * `UNSUPPORTED` * `XS` |
| nodes | string[] | Список синтетических узлов, принадлежащих локации.  Список доступных узлов можно получить вызовом [GET all nodes](https://dt-url.net/miy3rpl). |
| useNewKubernetesVersion | boolean | Свойство контейнеризированной локации. Булево значение описывает, какая версия kubernetes будет использоваться:  * `false`: версия 1.23+, более старая чем 1.26 * `true`: версия 1.26+. |

```
{



"entityId": "SYNTHETIC_LOCATION-F23EE93163E76BE2",



"type": "PRIVATE",



"name": "Sample synthetic location",



"countryCode": "PL",



"regionCode": "82",



"city": "GdaÅsk",



"latitude": 54.389,



"longitude": 18.6255,



"status": "ENABLED",



"nodes": [



"2131628184"



]



}
```

### PUBLIC

PublicSyntheticLocation

Параметры

JSON-модель

#### Объект `PublicSyntheticLocation`

Конфигурация публичной синтетической локации.

| Поле | Тип | Описание |
| --- | --- | --- |
| browserType | string | Тип браузера, который локация использует для выполнения браузерных мониторов. |
| browserVersion | string | Версия браузера, которую локация использует для выполнения браузерных мониторов. |
| capabilities | string[] | Список возможностей локации. |
| cloudPlatform | string | Облачный провайдер, на котором размещена локация. Поле может принимать значения: * `ALIBABA` * `AMAZON_EC2` * `AZURE` * `DYNATRACE_CLOUD` * `GOOGLE_CLOUD` * `INTEROUTE` * `OTHER` * `UNDEFINED` |
| ips | string[] | Список IP-адресов, назначенных локации. |
| stage | string | Стадия локации. Поле может принимать значения: * `BETA` * `COMING_SOON` * `DELETED` * `GA` |

```
{



"name": "US Central",



"entityId": "GEOLOCATION-AA22893EF461842C",



"type": "PUBLIC",



"cloudPlatform": "GOOGLE_CLOUD",



"ips": [



"200.198.18.147",



"186.202.218.192",



"221.120.251.140"



],



"stage": "GA",



"status": "ENABLED"



}
```

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")