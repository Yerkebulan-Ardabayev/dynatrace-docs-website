---
title: Dynatrace Intelligence для Notebooks
source: https://www.dynatrace.com/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/davis-for-notebooks
scraped: 2026-02-17T21:22:45.689629
---

# Dynatrace Intelligence для Notebooks

# Dynatrace Intelligence для Notebooks

* Последняя версия Dynatrace
* Руководство по настройке
* 2-минутное чтение
* Обновлено 28 января 2026 г.

Dynatrace Intelligence для Notebooks запускает ряд анализаторов直接 в Notebooks, предоставляя результаты на месте и позволяя вам тонко настраивать ваши пользовательские конфигурации оповещений.

## Обнаружение аномалий

С помощью ![Обнаружение аномалий - новое](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Обнаружение аномалий - новое") **Обнаружение аномалий**, объединенного с возможностями [DQL](/docs/platform/grail/dynatrace-query-language "Как использовать язык запросов Dynatrace."), вы можете создавать мощные конфигурации для обнаружения аномалий в метриках, журналах, бизнес-данных или их комбинации. Чтобы предварительно просмотреть и тонко настроить вашу конфигурацию Обнаружения аномалий перед развертыванием ее в действие, используйте опцию анализа Dynatrace Intelligence для Notebooks:

* [Автоадаптивный порог](/docs/dynatrace-intelligence/anomaly-detection/auto-adaptive-threshold "Как Dynatrace адаптирует пороги для нескольких сущностей в рамках конфигурации обнаружения аномалий.") — Dynatrace рассчитывает порог автоматически и адаптирует его динамически к поведению ваших данных.
* [Сезонная базовая линия](/docs/dynatrace-intelligence/reference/ai-models/seasonal-baseline "Как Dynatrace Intelligence предлагает сезонную базовую линию для области сущностей.") — Dynatrace создает доверительный интервал для данных с сезонными закономерностями
* [Статический порог](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds "Когда использовать статический порог для вашего обнаружения аномалий.") — порог, который не меняется со временем.

Для каждой из этих опций вы можете настроить [оповещение о пропущенных данных](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#missing-data "Как настроить оповещение о пропущенных измерениях."). Пропущенные данные и условия порога объединяются логикой **ИЛИ**.

Чтобы запустить анализ обнаружения аномалий в Notebooks

1. Перейдите в **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
2. Откройте вашу тетрадь или создайте новую.
3. Добавьте раздел **Query Grail** и [запросите](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#query-grail "Анализируйте, визуализируйте и делитесь идеями из ваших данных наблюдаемости — все в одном совместном, настраиваемом рабочем пространстве.") данные, которые вас интересуют, или добавьте раздел **Metrics** и выберите необходимую метрику.

   Для запроса DQL используйте параметр `interval: 1m`, чтобы обеспечить правильное разрешение данных для анализа.
4. Выберите **Options**.
5. В панели **Options** выберите **Анализ и оповещение** и активируйте анализатор.
6. Выберите необходимый анализатор обнаружения аномалий и настройте его параметры.
7. Выберите **Run analysis**.

Dynatrace Intelligence анализирует данные и показывает потенциальные оповещения. Обратите внимание, что это всего лишь симуляции — реальные оповещения не срабатывают на основе этого анализа.

![Пример обнаружения аномалий на сезонных данных в приложении Notebooks.](https://dt-cdn.net/images/notebooks-seasonal-anomaly-detection-1920-dbbd5f3499.png)

## Анализ прогноза

Прогнозный анализ Dynatrace Intelligence предсказывает будущие значения любой временной серии числовых значений на основе накопленных данных. Чтобы запустить [анализ прогноза](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Узнайте, как Dynatrace Intelligence генерирует прогнозы с помощью прогнозного ИИ.")

1. Перейдите в **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
2. Откройте вашу тетрадь или создайте новую.
3. Добавьте раздел **Query Grail** и [запросите](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#query-grail "Анализируйте, визуализируйте и делитесь идеями из ваших данных наблюдаемости — все в одном совместном, настраиваемом рабочем пространстве.") данные, которые вас интересуют, или добавьте раздел **Metrics** и выберите необходимую метрику.
4. Выберите **Options**.
5. В панели **Options** выберите **Анализ и оповещение** и активируйте анализатор.
6. Выберите анализатор **Прогноз** и настройте его параметры.
7. Выберите **Run analysis**.

Dynatrace Intelligence рассчитывает прогноз и показывает его, расширяя вашу визуализацию.

![Пример прогноза для сезонных данных в приложении Notebooks.](https://dt-cdn.net/images/notebooks-seasonal-prediction-1920-0137a2c619.png)

## Связанные темы

* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь идеями из ваших данных наблюдаемости — все в одном совместном, настраиваемом рабочем пространстве.")
* [[Видео] Введение в обнаружение аномалий на основе DQL](https://www.youtube.com/watch?v=-GxLlr9oGGA)