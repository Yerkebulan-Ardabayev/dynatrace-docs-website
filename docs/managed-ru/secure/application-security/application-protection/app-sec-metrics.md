---
title: Классические метрики для Dynatrace Runtime Application Protection
source: https://docs.dynatrace.com/managed/secure/application-security/application-protection/app-sec-metrics
scraped: 2026-05-12T11:25:14.396989
---

# Классические метрики для Dynatrace Runtime Application Protection

# Классические метрики для Dynatrace Runtime Application Protection

* Reference
* Updated on Nov 06, 2025

## Доступные метрики

Следующие метрики Application Security доступны для Runtime Application Protection.

### Атаки

| Название метрики | Версия Dynatrace | Описание |
| --- | --- | --- |
| New attacks | 1.271+ | Количество атак, обнаруженных в недавнем времени (на основе момента сохранения атак в кластере Dynatrace; в результате между временной меткой сообщаемой метрики атак и временной меткой атак, обнаруженных OneAgent, могут быть незначительные расхождения). Метрика учитывает management zones на основе измерения группы процессов. |

#### Измерения, используемые в метриках атак

* Статус (`Blocked`, `Allowlisted`, `Exploited`)
* Тип (`SQL injection`, `CMD injection`, `JNDI injection`, `SSRF`)
* Группа процессов (`builtin` — основная сущность для выбора management zone)

## Просмотр

Чтобы просмотреть метрики Application Security

1. Перейдите в **Metrics**.
2. Отфильтруйте нужную метрику.

   * Если результаты не отображаются, отключите **Only show metrics reported after the start of the selected timeframe**.
   * Можно добавить дополнительные фильтры (`Tag`, `Unit`, `Favorites`). Подробнее см. в разделе [Фильтрация и сортировка таблицы](/managed/analyze-explore-automate/dashboards-classic/metrics-browser#filter "Просмотр метрик с помощью браузера метрик Dynatrace.").
3. Разверните **Details** для любой метрики, чтобы увидеть её подробности и график за выбранный период. Подробнее см. в разделе [Браузер метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просмотр метрик с помощью браузера метрик Dynatrace.").

   Пример сведений о метрике:

   ![example metric attacks](https://dt-cdn.net/images/2024-03-18-16-42-03-1638-09c79cbcb9.png)

   example metric attacks

## Использование

Метрики Application Security можно использовать для:

* [Создания графиков и их закрепления на дашбордах](/managed/analyze-explore-automate/dashboards-classic/metrics-browser#pin "Просмотр метрик с помощью браузера метрик Dynatrace.")
* [Запроса данных в Data Explorer](/managed/analyze-explore-automate/explorer#query-components-and-concepts "Запрос метрик и преобразование результатов для получения нужных аналитических данных.")

### Пример

Чтобы отслеживать количество атак с течением времени, создайте график для метрики `New attacks` и закрепите его на дашборде.

## Экспорт и публикация

После выполнения запроса в Data Explorer вы можете:

* [Поделиться результатами метрик](/managed/analyze-explore-automate/explorer#share "Запрос метрик и преобразование результатов для получения нужных аналитических данных.")
* [Экспортировать результаты метрик](/managed/analyze-explore-automate/explorer#csv "Запрос метрик и преобразование результатов для получения нужных аналитических данных.")
* [Использовать результаты метрик в запросах API](/managed/analyze-explore-automate/explorer#api "Запрос метрик и преобразование результатов для получения нужных аналитических данных.")

## Связанные темы

* [Метрики для Dynatrace Runtime Vulnerability Analytics](/managed/secure/application-security/vulnerability-analytics/app-sec-metrics "Просмотр доступных метрик Application Security для Dynatrace Runtime Vulnerability Analytics.")
* [FAQ по Application Security](/managed/secure/faq "Часто задаваемые вопросы о Dynatrace Application Security.")