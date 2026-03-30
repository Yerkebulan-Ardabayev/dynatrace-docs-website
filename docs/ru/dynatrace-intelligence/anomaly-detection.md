---
title: Обнаружение аномалий
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection
scraped: 2026-03-06T21:11:03.759228
---

Dynatrace непрерывно отслеживает все компоненты среды, автоматически строит базовые линии метрик с учётом геолокации, браузеров, ОС и других переменных. Это позволяет обнаруживать аномалии на детальном уровне и уведомлять в реальном времени. Пороговые значения можно настраивать через изменение чувствительности или задание статических порогов.

## Варианты использования

* Создание пользовательских оповещений о проблемах в среде.
* Ручная настройка или использование адаптивных порогов для обнаружения аномалий.
* Настройка оповещений для пользовательских событий.

## Концепции

* [Адаптивные пороговые значения](anomaly-detection/auto-adaptive-threshold.md) -- динамическая адаптация порогов для нескольких сущностей.
* [Статические пороговые значения](anomaly-detection/static-thresholds.md) -- когда использовать фиксированный порог.
* [Конфигурация обнаружения аномалий](anomaly-detection/anomaly-detection-configuration.md) -- настройка оповещений об отсутствующих измерениях.
* [Автоматическое многомерное построение базовых линий](anomaly-detection/automated-multidimensional-baselining.md) -- расчёт базовых линий по многомерной схеме.
* [Типы статусов обнаружения аномалий](anomaly-detection/anomaly-detection-app/anomaly-detection-status-types.md)

## Начало работы

* [Настройка чувствительности обнаружения аномалий](anomaly-detection/adjust-sensitivity-anomaly-detection.md)
* [Приложение Anomaly Detection](anomaly-detection/anomaly-detection-app.md) -- единый обзор всех конфигураций.
* [Метрические события](anomaly-detection/metric-events.md)
* [Автоматизация оповещений через API](anomaly-detection/set-up-anomaly-detectors-via-api.md)
