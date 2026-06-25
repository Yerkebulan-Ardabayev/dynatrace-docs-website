---
title: Публичные расположения Synthetic
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations
scraped: 2026-05-12T11:32:01.515716
---

# Публичные расположения Synthetic

# Публичные расположения Synthetic

* Reference
* 8-min read
* Updated on Feb 08, 2024

Dynatrace предоставляет глобальную сеть публичных расположений Synthetic Monitoring из коробки. С помощью Dynatrace Synthetic Monitoring вы можете запускать мониторы из публичных расположений, базирующихся на инфраструктуре крупнейших облачных провайдеров: Alibaba Cloud, Amazon AWS, Google Cloud и Microsoft Azure.

Обратите внимание:

* Вы также можете [создавать частные расположения Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.") в собственной сетевой инфраструктуре. Все публичные и частные расположения Synthetic могут запускать как [браузерные, так и HTTP-мониторы](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Узнайте о типах синтетических мониторов Dynatrace.").
* Для запуска синтетических мониторов из публичных расположений необходимо настроить Cluster ActiveGate с публичным IP-адресом.

## Стадии выпуска расположений

Расположения выпускаются в одной из следующих прогрессивных стадий: **Coming soon**, **Early Access** или **GA**. Расположения также могут быть **Deprecated**. Описание стадий:

| Стадия | Описание |
| --- | --- |
| **Coming soon** | Расположение создано; выполняются финальные тесты производительности перед открытием доступа. |
| **Deprecated** | Расположение будет удалено; назначить новые мониторы на такое расположение нельзя. |
| **Early Access** | Расположение готово к работе и полностью поддерживается. Его дальнейшая доступность зависит от интереса пользователей и факторов на стороне провайдера. |
| **GA** | Расположение общедоступно и полностью поддерживается. |

## IP-адреса расположений

Если ваша политика безопасности требует добавления IP-адреса расположения в список разрешённых адресов, или эта информация нужна по иным причинам, определить IP-адрес расположения можно одним из следующих способов.

* При создании или изменении мониторов все расположения и их IP-адреса отображаются в таблице на странице **Frequency and locations**. Выберите одно или несколько расположений, прокрутите страницу вниз и нажмите **Copy IPs to clipboard** или **Download IPs**, чтобы скопировать или скачать соответствующие IP-адреса.
* Используйте API-запрос [Synthetic locations API - GET all locations](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/get-all-locations "Просматривайте все синтетические расположения через Synthetic v1 API."), который возвращает все расположения, доступные для вашего окружения, вместе с IP-адресами.

## Расположения

**Все публичные расположения Synthetic работают по координированному всемирному времени (UTC)**.

Уведомление об изменении расположений

**Публичные расположения Alibaba Sydney и Mumbai будут отключены к концу марта 2024 года**.

Alibaba объявила о закрытии дата-центров в Австралии и Индии к концу марта 2024 года.

В связи с этим, если вы используете расположения Alibaba Sydney или Mumbai, рекомендуется переназначить мониторы на альтернативные расположения, чтобы тесты продолжали работать. Если вы не хотите делать это самостоятельно, начиная с марта 2024 года мы автоматически перенесём ваши мониторы на альтернативные публичные расположения, указанные ниже.

**Сводка изменений**

| Расположение, устаревающее к концу марта 2024 | Рекомендуемое альтернативное расположение |
| --- | --- |
| **Sydney (Alibaba)** | **Sydney (AWS)** |
| **Mumbai (Alibaba)** | **Mumbai (AWS)** |

Перенос мониторов

Если ваши синтетические мониторы назначены на расположения Sydney (Alibaba) или Mumbai (Alibaba), которые скоро устареют, рекомендуется назначить их на другие расположения. Альтернативные расположения Sydney (AWS) и Mumbai (AWS) будут наиболее подходящим выбором, но вы можете выбрать и другие.

1. Перейдите в **Synthetic Classic** и выберите монитор.
2. На странице деталей монитора нажмите **Edit**.
3. Выберите **Frequency and locations**.
4. Снимите флажки с **Sydney** (Alibaba) и **Mumbai** (Alibaba) и выберите альтернативные расположения.
5. **Save changes**.

Для массовой настройки можно также использовать [Synthetic Monitors API](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors "Управляйте синтетическими мониторами через Synthetic v1 API.").

Дополнительные действия для обновления правил брандмауэра

Несмотря на то что мы стараемся сделать переход максимально прозрачным, некоторые задачи мы не можем выполнить за вас, поэтому могут потребоваться дополнительные действия.

* Если вы являетесь пользователем Dynatrace Managed с кластерами, защищёнными брандмауэром, обновите конфигурацию, чтобы разрешить альтернативному расположению взаимодействовать с Cluster ActiveGate.

* Если ваши приложения отслеживаются с помощью Dynatrace Synthetic Monitoring, может потребоваться скорректировать конфигурацию брандмауэра, чтобы разрешить входящий трафик с выбранных альтернативных расположений к вашим сайтам.
* После конца марта 2024 года публичные расположения Alibaba Sydney и Mumbai больше не будут доступны. Соответственно, также нужно будет удалить IP-адреса этих расположений из конфигурации брандмауэра.

Информацию о новых адресах см. в разделе [IP-адреса расположений](#ip-addresses).

### Африка

| Расположение | Платформа | Стадия |
| --- | --- | --- |
| Cape Town | Microsoft Azure | GA |
| Cape Town | Amazon AWS | GA |
| Johannesburg | Microsoft Azure | GA |

### Австралия

| Расположение | Платформа | Стадия |
| --- | --- | --- |
| Canberra | Microsoft Azure | GA |
| New South Wales | Microsoft Azure | GA |
| Sydney[1](#fn-1-1-def) | Alibaba Cloud | Early Access |
| Sydney | Amazon AWS | GA |
| Sydney | Google Cloud | GA |
| Victoria | Microsoft Azure | GA |

1

См. [Уведомление об изменении расположений](#location-change).

### Азия

| Расположение | Платформа | Стадия |
| --- | --- | --- |
| Abu Dhabi | Microsoft Azure | GA |
| Bahrain | Amazon AWS | GA |
| Beijing | Alibaba Cloud | Early Access |
| Busan | Microsoft Azure | GA |
| Chennai | Microsoft Azure | GA |
| Dubai | Alibaba Cloud | Early Access |
| Dubai | Microsoft Azure | GA |
| Hohhot | Alibaba Cloud | Early Access |
| Mumbai | Alibaba Cloud | Early Access |
| Hangzhou | Alibaba Cloud | Early Access |
| Hong Kong | Alibaba Cloud | Early Access |
| Hong Kong | Microsoft Azure | GA |
| Hong Kong | Google Cloud | GA |
| Mumbai | Amazon AWS | GA |
| Mumbai | Microsoft Azure | GA |
| Pune | Microsoft Azure | GA |
| Osaka | Microsoft Azure | GA |
| Qingdao | Alibaba Cloud | Early Access |
| Seoul | Amazon AWS | GA |
| Seoul | Microsoft Azure | GA |
| Shanghai | Alibaba Cloud | Early Access |
| Shenzhen | Alibaba Cloud | Early Access |
| Singapore | Alibaba Cloud | Early Access |
| Singapore | Amazon AWS | GA |
| Taiwan | Google Cloud | GA |
| Tokyo | Alibaba Cloud | Early Access |
| Tokyo | Amazon AWS | GA |
| Tokyo | Microsoft Azure | GA |
| Zhangjiakou | Alibaba Cloud | Early Access |

### Европа

| Расположение | Платформа | Стадия |
| --- | --- | --- |
| Amsterdam | Microsoft Azure | GA |
| Belgium West | Google Cloud | GA |
| Berlin | Microsoft Azure | GA |
| Cardiff | Microsoft Azure | GA |
| Dublin | Amazon AWS | GA |
| Dublin | Microsoft Azure | GA |
| Finland South | Google Cloud | GA |
| Frankfurt | Alibaba Cloud | Early Access |
| Frankfurt | Amazon AWS | GA |
| Frankfurt | Microsoft Azure | GA |
| Groningen | Google Cloud | GA |
| London | Alibaba Cloud | Early Access |
| London | Amazon AWS | GA |
| London | Microsoft Azure | GA |
| Madrid | Google Cloud | Early Access |
| Marseille | Microsoft Azure | GA |
| Milan | Amazon AWS | GA |
| Paris | Amazon AWS | GA |
| Paris | Microsoft Azure | GA |
| Oslo | Microsoft Azure | GA |
| Stavanger | Microsoft Azure | GA |
| Stockholm | Amazon AWS | GA |
| Zurich | Microsoft Azure | GA |
| Zurich | Google Cloud | GA |

### Северная Америка

| Расположение | Платформа | Стадия |
| --- | --- | --- |
| Cheyenne | Microsoft Azure | GA |
| Chicago | Microsoft Azure | GA |
| Des Moines | Microsoft Azure | GA |
| Iowa | Google Cloud | GA |
| Las Vegas | Google Cloud | GA |
| Los Angeles | Google Cloud | GA |
| Montreal | Amazon AWS | GA |
| Montreal | Google Cloud | GA |
| N. California | Amazon AWS | GA |
| N. Virginia | Amazon AWS | GA |
| Ohio | Amazon AWS | GA |
| Oregon | Amazon AWS | GA |
| Oregon | Google Cloud | GA |
| Quebec City | Microsoft Azure | GA |
| Salt Lake City | Google Cloud | GA |
| San Jose | Microsoft Azure | GA |
| Seattle | Microsoft Azure | GA |
| Silicon Valley | Alibaba Cloud | Early Access |
| South Carolina | Google Cloud | GA |
| Texas | Microsoft Azure | GA |
| Toronto | Microsoft Azure | GA |
| Virginia | Alibaba Cloud | Early Access |
| Virginia | Microsoft Azure | GA |

### Южная Америка

| Расположение | Платформа | Стадия |
| --- | --- | --- |
| Sao Paulo | Amazon AWS | GA |
| Sao Paulo | Microsoft Azure | GA |

## Связанные темы

* [Создать частное расположение Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.")
* [Synthetic locations API - GET all locations](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/get-all-locations "Просматривайте все синтетические расположения через Synthetic v1 API.")