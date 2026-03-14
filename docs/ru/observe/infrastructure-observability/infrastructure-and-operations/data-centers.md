---
title: Центры обработки данных
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations/data-centers
scraped: 2026-03-06T21:16:58.775446
---

# Data centers


* Latest Dynatrace
* Explanation
* 2-min read
* Published Nov 26, 2025

Представление **Data centers** в ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** отслеживает работоспособность и производительность ваших центров обработки данных и зон доступности.

Выберите центр обработки данных, чтобы просмотреть все отслеживаемые в нём хосты.

## Обзор

Ниже описано, что обозначает каждый столбец в представлении **Data centers**.

* **Data center**: Название или идентификатор центра обработки данных или зоны доступности.
* **Type**: Тип центра обработки данных, например:

  + AWS Availability Zone
  + GCP zone
  + Azure Region
  + Geo Location Site
* **Hosts**:

  + **Total**: Общее количество хостов в центре обработки данных.
  + **Unhealthy**: Количество хостов, испытывающих проблемы. Критические хосты выделены красным цветом.
  + **Monitored**: Процент хостов, активно отслеживаемых в центре обработки данных. Значение ниже 100% означает, что Dynatrace обнаружил неотслеживаемые экземпляры на основе подключений хостов.
* **Location**: Географическое название расположения центра обработки данных.

## Варианты использования

* Выявление критических проблем

  Проверьте столбец **Unhealthy** и примените фильтр Critical alert, чтобы быстро найти центры обработки данных с проблемами. Нажатие на индикатор предупреждения откроет отфильтрованный список хостов с фокусом на затронутых системах.
* Контроль охвата мониторинга

  Просматривайте столбец **Monitored**, чтобы обеспечить полное отслеживание всех хостов. Если вы обнаружите пробелы в мониторинге, вы можете использовать ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage** для расширения охвата и достижения полного покрытия.
