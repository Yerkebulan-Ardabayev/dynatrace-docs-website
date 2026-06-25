---
title: Synthetic locations API v2 - JSON-модели
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models
scraped: 2026-05-12T11:24:06.547936
---

# Synthetic locations API v2 - JSON-модели

# Synthetic locations API v2 - JSON-модели

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

Часть полей наследуется от базового объекта *SyntheticLocation*.

| Поле | Тип | Описание |
| --- | --- | --- |
| autoUpdateChromium | boolean | Свойство неконтейнеризированной локации. Авто-обновление Chromium включено (`true`) или отключено (`false`). |
| availabilityLocationOutage | boolean | Оповещение о недоступности локации включено (`true`) или отключено (`false`). Поддерживается только для приватных синтетических локаций. |
| availabilityNodeOutage | boolean | Оповещение о недоступности узла включено (`true`) или отключено (`false`). \n\n Если включено, недоступность *любого* узла в локации вызывает алерт. Поддерживается только для приватных синтетических локаций. |
| availabilityNotificationsEnabled | boolean | Уведомления о недоступности локации и узла включены (`true`) или отключены (`false`). Поддерживается только для приватных синтетических локаций. |
| browserExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение описывает, будут ли браузерные мониторы выполняться на этой локации:  * `false`: выполнение браузерных мониторов отключено. * `true`: выполнение браузерных мониторов включено. |
| city | string | Город локации. |
| countryCode | string | Код страны локации.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go). |
| countryName | string | Название страны локации. |
| deploymentType | string | Тип развёртывания локации:  * `STANDARD`: локация развёрнута на Windows или Linux. * `KUBERNETES`: локация развёрнута на Kubernetes. Поле может принимать значения: * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` |
| entityId | string | Dynatrace entity ID локации. |
| fipsMode | string | Свойство контейнеризированной локации, указывающее, включён ли на этой локации режим FIPS:  * `DISABLED`: FIPS не включён на локации. * `ENABLED`: FIPS включён на локации. * `ENABLED_WITH_CORPORATE_PROXY`: FIPS с корпоративным прокси включён на этой локации.   По умолчанию: DISABLED Поле может принимать значения: * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` |
| geoLocationId | string | Dynatrace GeoLocation ID локации. |
| latitude | number | Широта локации в формате `DDD.dddd`. |
| locationNodeOutageDelayInMinutes | integer | Алерт, если недоступность локации или узла длится дольше *X* минут. \n\n Применимо только если `availabilityLocationOutage` или `availabilityNodeOutage` установлено в `true`. Поддерживается только для приватных синтетических локаций. |
| longitude | number | Долгота локации в формате `DDD.dddd`. |
| namExecutionSupported | boolean | Свойство контейнеризированной локации. Булево значение описывает, будут ли icmp-мониторы выполняться на этой локации:  * `false`: выполнение icmp-мониторов отключено. * `true`: выполнение icmp-мониторов включено. |
| name | string | Имя локации. |
| nodeNames | object | Сопоставление id и имени узлов, принадлежащих локации. |
| nodes | string[] | Список синтетических узлов, принадлежащих локации.  Список доступных узлов можно получить вызовом [GET all nodes](https://dt-url.net/miy3rpl). |
| regionCode | string | Код региона локации.  Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country](https://dt-url.net/az230x0). |
| regionName | string | Название региона локации. |
| status | string | Статус локации:  * `ENABLED`: локация отображается в UI как активная. Локации можно назначать мониторы. * `DISABLED`: локация отображается в UI как неактивная. Локации нельзя назначать мониторы. Мониторы, уже назначенные локации, останутся там и будут выполняться с этой локации. * `HIDDEN`: локация не отображается в UI. Локации нельзя назначать мониторы. Установить локацию в `HIDDEN` можно только тогда, когда ей не назначен ни один монитор. Поле может принимать значения: * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | -Поле может принимать значения: * `CLUSTER` * `PRIVATE` * `PUBLIC` |
| useNewKubernetesVersion | boolean | Свойство контейнеризированной локации. Булево значение описывает, какая версия kubernetes будет использоваться:  * `false`: версия 1.23+, более старая чем 1.26 * `true`: версия 1.26+. |

```
{



"entityId": "SYNTHETIC_LOCATION-F23EE93163E76BE2",



"type": "PRIVATE",



"status": "ENABLED",



"name": "Sample synthetic location",



"countryCode": "PL",



"regionCode": "82",



"city": "GdaÅsk",



"latitude": 54.389,



"longitude": 18.6255,



"nodes": [



"2131628184"



],



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"locationNodeOutageDelayInMillis": 5000,



"geoLocationId": "GEOLOCATION-AA22893EF461842C"



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



"entityId": "SYNTHETIC_LOCATION-00000000000001A5",



"type": "PUBLIC",



"cloudPlatform": "GOOGLE_CLOUD",



"ips": [



"210.6.226.150",



"185.77.153.103",



"153.242.5.43"



],



"stage": "BETA",



"status": "ENABLED",



"capabilities": [



"BROWSER",



"HTTP"



],



"geoLocationId": "GEOLOCATION-AA22893EF461842C"



}
```

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.")