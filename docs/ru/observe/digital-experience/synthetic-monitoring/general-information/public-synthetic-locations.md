---
title: Публичные точки Synthetic-мониторинга
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations
scraped: 2026-03-06T21:24:46.338930
---

Dynatrace предлагает глобальную сеть публичных точек Synthetic Monitoring, доступных сразу после установки. С помощью Dynatrace Synthetic Monitoring вы можете запускать мониторы из публичных точек, расположенных на инфраструктуре следующих крупных облачных провайдеров: Alibaba Cloud, Amazon AWS, Google Cloud и Microsoft Azure.

Обратите внимание, что вы также можете [создавать приватные точки Synthetic-мониторинга](../private-synthetic-locations/create-a-private-synthetic-location.md "Узнайте, как создать приватную точку для Synthetic-мониторинга.") в рамках собственной сетевой инфраструктуры. Все публичные и приватные точки Synthetic-мониторинга поддерживают как [браузерные, так и HTTP-мониторы](types-of-synthetic-monitors.md "Узнайте о типах синтетических мониторов Dynatrace.").

## Стадии выпуска точек

Точки выпускаются на одной из следующих прогрессивных стадий: **Coming soon**, **Early Adopter** или **GA**. Точки также могут быть в статусе **Deprecated**. Ознакомьтесь с описанием стадий:

| Стадия | Описание |
| --- | --- |
| **Coming soon** | Точка уже создана; мы проводим финальное тестирование производительности перед тем, как сделать её доступной. |
| **Deprecated** | Точка скоро будет удалена; назначить новые мониторы на устаревшую точку нельзя. |
| **Early Adopter** | Точка готова к использованию в производственной среде и полностью поддерживается. Её дальнейшая доступность зависит от интереса к данной точке и факторов, зависящих от провайдера. |
| **GA** | Точка общедоступна и полностью поддерживается. |

## IP-адреса точек

Если ваша политика безопасности требует добавления IP-адреса точки в список разрешённых адресов или вам нужна эта информация для других целей, вы можете определить IP-адрес точки одним из следующих способов.

* При создании или изменении мониторов все точки и их IP-адреса отображаются в таблице на странице **Frequency and locations**. Выберите одну или несколько точек, прокрутите страницу вниз и нажмите **Copy IPs to clipboard** или **Download IPs**, чтобы скопировать или скачать соответствующие IP-адреса.
* Используйте API-вызов [Synthetic locations API - GET all locations](../../../../dynatrace-api/environment-api/synthetic/synthetic-locations/get-all-locations.md "Получение списка всех точек Synthetic-мониторинга через Synthetic v1 API."), который возвращает все доступные для вашей среды точки вместе с их IP-адресами.

## Точки

**Все публичные точки Synthetic-мониторинга настроены на Coordinated Universal Time (UTC)**.

Уведомление об изменении точек

**Публичные точки Alibaba Sydney и Mumbai будут выведены из эксплуатации до конца марта 2024 года**.

Alibaba объявила о закрытии дата-центров в Австралии и Индии, которое запланировано на конец марта 2024 года.

В связи с этим изменением, если вы используете точки Alibaba Sydney или Mumbai, мы рекомендуем переназначить ваши мониторы на альтернативные точки, чтобы обеспечить работоспособность тестов. Если вы предпочитаете не делать этого самостоятельно, начиная с марта 2024 года мы автоматически перенесём ваши мониторы на альтернативные публичные точки, указанные ниже.

**Краткое описание изменений**

| Точка, выводимая из эксплуатации к концу марта 2024 | Рекомендуемая альтернативная точка |
| --- | --- |
| **Sydney (Alibaba)** | **Sydney (AWS)** |
| **Mumbai (Alibaba)** | **Mumbai (AWS)** |

Перенос мониторов

Если у вас есть синтетические мониторы, назначенные на скоро выводимые из эксплуатации точки Sydney (Alibaba) или Mumbai (Alibaba), мы рекомендуем назначить их на другие точки. Альтернативные точки Sydney (AWS) и Mumbai (AWS) будут естественным первым выбором, но вы, конечно, можете выбрать и другие точки.

1. Перейдите в **Synthetic Classic** и выберите монитор.
2. На странице деталей монитора нажмите **Edit**.
3. Выберите **Frequency and locations**.
4. Снимите флажки **Sydney** (Alibaba) и **Mumbai** (Alibaba) и выберите альтернативные точки.
5. **Save changes**.

Вы также можете использовать [Synthetic Monitors API](../../../../dynatrace-api/environment-api/synthetic/synthetic-monitors.md "Управление синтетическими мониторами через Synthetic v1 API.") для массовой настройки.

Дополнительные действия для обновления правил межсетевого экрана

Мы стремимся сделать этот переход максимально плавным, однако есть определённые задачи, которые мы не можем выполнить за вас, поэтому вам, возможно, потребуется предпринять дополнительные действия.

* Если ваши приложения мониторятся с помощью Dynatrace Synthetic Monitoring, вам может потребоваться изменить конфигурацию межсетевого экрана, чтобы разрешить входящий трафик с выбранных альтернативных точек к вашим веб-сайтам.
* После окончания марта 2024 года публичные точки Alibaba Sydney и Mumbai станут недоступны. Соответственно, вам также потребуется удалить связанные IP-адреса этих точек из конфигурации межсетевого экрана.

Для получения информации о новых адресах смотрите раздел [IP-адреса точек](#ip-addresses).

### Африка

| Точка | Платформа | Стадия |
| --- | --- | --- |
| Cape Town | Microsoft Azure | GA |
| Cape Town | Amazon AWS | GA |
| Johannesburg | Microsoft Azure | GA |

### Австралия

| Точка | Платформа | Стадия |
| --- | --- | --- |
| Canberra | Microsoft Azure | GA |
| New South Wales | Microsoft Azure | GA |
| Sydney[1](#fn-1-1-def) | Alibaba Cloud | Early Adopter |
| Sydney | Amazon AWS | GA |
| Sydney | Google Cloud | GA |
| Victoria | Microsoft Azure | GA |

1

Смотрите [Уведомление об изменении точек](#location-change).

### Азия

| Точка | Платформа | Стадия |
| --- | --- | --- |
| Abu Dhabi | Microsoft Azure | GA |
| Bahrain | Amazon AWS | GA |
| Beijing | Alibaba Cloud | Early Adopter |
| Busan | Microsoft Azure | GA |
| Chennai | Microsoft Azure | GA |
| Dubai | Alibaba Cloud | Early Adopter |
| Dubai | Microsoft Azure | GA |
| Hohhot | Alibaba Cloud | Early Adopter |
| Mumbai | Alibaba Cloud | Early Adopter |
| Hangzhou | Alibaba Cloud | Early Adopter |
| Hong Kong | Alibaba Cloud | Early Adopter |
| Hong Kong | Microsoft Azure | GA |
| Hong Kong | Google Cloud | GA |
| Mumbai | Amazon AWS | GA |
| Mumbai | Microsoft Azure | GA |
| Pune | Microsoft Azure | GA |
| Osaka | Microsoft Azure | GA |
| Qingdao | Alibaba Cloud | Early Adopter |
| Seoul | Amazon AWS | GA |
| Seoul | Microsoft Azure | GA |
| Shanghai | Alibaba Cloud | Early Adopter |
| Shenzhen | Alibaba Cloud | Early Adopter |
| Singapore | Alibaba Cloud | Early Adopter |
| Singapore | Amazon AWS | GA |
| Taiwan | Google Cloud | GA |
| Tokyo | Alibaba Cloud | Early Adopter |
| Tokyo | Amazon AWS | GA |
| Tokyo | Microsoft Azure | GA |
| Zhangjiakou | Alibaba Cloud | Early Adopter |

### Европа

| Точка | Платформа | Стадия |
| --- | --- | --- |
| Amsterdam | Microsoft Azure | GA |
| Belgium West | Google Cloud | GA |
| Berlin | Microsoft Azure | GA |
| Cardiff | Microsoft Azure | GA |
| Dublin | Amazon AWS | GA |
| Dublin | Microsoft Azure | GA |
| Finland South | Google Cloud | GA |
| Frankfurt | Alibaba Cloud | Early Adopter |
| Frankfurt | Amazon AWS | GA |
| Frankfurt | Microsoft Azure | GA |
| Groningen | Google Cloud | GA |
| London | Alibaba Cloud | Early Adopter |
| London | Amazon AWS | GA |
| London | Microsoft Azure | GA |
| Madrid | Google Cloud | Early Adopter |
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

| Точка | Платформа | Стадия |
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
| Silicon Valley | Alibaba Cloud | Early Adopter |
| South Carolina | Google Cloud | GA |
| Texas | Microsoft Azure | GA |
| Toronto | Microsoft Azure | GA |
| Virginia | Alibaba Cloud | Early Adopter |
| Virginia | Microsoft Azure | GA |

### Южная Америка

| Точка | Платформа | Стадия |
| --- | --- | --- |
| Sao Paulo | Amazon AWS | GA |
| Sao Paulo | Microsoft Azure | GA |

## Связанные темы

* [Создание приватной точки Synthetic-мониторинга](../private-synthetic-locations/create-a-private-synthetic-location.md "Узнайте, как создать приватную точку для Synthetic-мониторинга.")
* [Synthetic locations API - GET all locations](../../../../dynatrace-api/environment-api/synthetic/synthetic-locations/get-all-locations.md "Получение списка всех точек Synthetic-мониторинга через Synthetic v1 API.")
