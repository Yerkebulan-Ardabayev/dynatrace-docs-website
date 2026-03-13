---
title: Dynatrace Intelligence for Notebooks
source: https://www.dynatrace.com/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/davis-for-notebooks
scraped: 2026-03-06T21:21:11.934524
---

# Dynatrace Intelligence for Notebooks

# Dynatrace Intelligence for Notebooks

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence for Notebooks запускает ряд анализаторов непосредственно в Notebooks, предоставляя результаты на месте и позволяя точно настраивать конфигурации пользовательских оповещений.

## Обнаружение аномалий

Используя ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** в сочетании с возможностями [DQL](../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language."), можно создавать мощные пользовательские конфигурации для обнаружения аномалий в метриках, логах, бизнес-данных или их комбинации. Для предварительного просмотра и тонкой настройки конфигурации обнаружения аномалий перед её развёртыванием используйте параметр анализа Dynatrace Intelligence for Notebooks:

* [Auto-adaptive threshold](../anomaly-detection/auto-adaptive-threshold.md "Как Dynatrace адаптирует пороги для нескольких сущностей в рамках конфигурации обнаружения аномалий.") — Dynatrace автоматически вычисляет порог и динамически адаптирует его к поведению данных.
* [Seasonal baseline](../reference/ai-models/seasonal-baseline.md "Как Dynatrace Intelligence предлагает пороги сезонного базового уровня для набора сущностей.") — Dynatrace создаёт доверительную полосу для данных с сезонными паттернами.
* [Static threshold](../anomaly-detection/static-thresholds.md "Когда использовать статический порог для обнаружения аномалий.") — порог, не изменяющийся со временем.

Для каждого из этих параметров можно настроить [оповещение об отсутствующих данных](../anomaly-detection/anomaly-detection-configuration.md#missing-data "Как настроить оповещение об отсутствующих измерениях."). Условия отсутствия данных и порогов объединяются логикой **OR**.

Чтобы запустить анализ обнаружения аномалий в Notebooks

1. Перейдите в **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
2. Откройте существующую тетрадь или создайте новую.
3. Добавьте раздел **Query Grail** и [запросите](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md#query-grail "Анализируйте, визуализируйте и делитесь аналитикой на основе данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.") нужные данные, либо добавьте раздел **Metrics** и выберите необходимую метрику.

   Для DQL-запроса используйте параметр `interval: 1m`, чтобы обеспечить правильное разрешение данных для анализа.
4. Нажмите **Options**.
5. На панели **Options** выберите **Analyze and alert** и активируйте анализатор.
6. Выберите нужный анализатор обнаружения аномалий и настройте его параметры.
7. Нажмите **Run analysis**.

Dynatrace Intelligence анализирует данные и показывает потенциальные оповещения. Обратите внимание, что это лишь ориентировочные симуляции — на основе данного анализа реальные оповещения не создаются.

![An example of anomaly detection on seasonal data in the Notebooks app.](https://dt-cdn.net/images/notebooks-seasonal-anomaly-detection-1920-dbbd5f3499.png)

## Анализ прогнозов

Предиктивный ИИ-анализ Dynatrace Intelligence прогнозирует будущие значения любого временного ряда числовых значений на основе накопленных данных. Чтобы запустить [анализ прогноза](../reference/ai-models/forecast-analysis.md "Узнайте, как предиктивный ИИ Dynatrace Intelligence генерирует прогнозы.")

1. Перейдите в **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
2. Откройте существующую тетрадь или создайте новую.
3. Добавьте раздел **Query Grail** и [запросите](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md#query-grail "Анализируйте, визуализируйте и делитесь аналитикой на основе данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.") нужные данные, либо добавьте раздел **Metrics** и выберите необходимую метрику.
4. Нажмите **Options**.
5. На панели **Options** выберите **Analyze and alert** и активируйте анализатор.
6. Выберите анализатор **Forecast** и настройте его параметры.
7. Нажмите **Run analysis**.

Dynatrace Intelligence вычисляет прогноз и отображает его, расширяя вашу визуализацию.

![An example of a forecast for seasonal data in the Notebooks app.](https://dt-cdn.net/images/notebooks-seasonal-prediction-1920-0137a2c619.png)

## Связанные темы

* [Notebooks](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь аналитикой на основе данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.")
* [[Video] Introduction to Anomaly Detection based on DQL](https://www.youtube.com/watch?v=-GxLlr9oGGA)
