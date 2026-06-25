---
title: Serverless Functions Classic (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/platform-extensions/serverless-functions-classic
scraped: 2026-05-12T12:13:07.647138
---

# Serverless Functions Classic (DPS)

# Serverless Functions Classic (DPS)

* Explanation
* 3-min read
* Updated on Jan 12, 2026

На этой странице описано, как потребляется и тарифицируется DPS-возможность Serverless Functions Classic.
Обзор возможности и основных функций см. в [Serverless Functions Classic](/managed/license/capabilities/platform-extensions#functions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: вызовы

Трассировка бессерверных функций — AWS Lambda, Azure Functions и Google Functions, работающих по модели потребления, — основана на общем количестве мониторируемых вызовов функции.
Термин «вызов функции» эквивалентен понятиям «запрос функции» или «выполнение функции».

Облачные функции, мониторируемые с помощью метрик через интеграции с облачными провайдерами (Amazon CloudWatch, Azure Monitor или Google Cloud Operations), потребляют пользовательские метрики в Dynatrace.
Подробнее см. в [пользовательские метрики](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

Пример потребления: трассировка AWS Lambda

Для интеграции трассировки AWS Lambda потребление мониторинга основано на общем числе мониторируемых вызовов (запросов) функций.

Предположим, что каждая Lambda-функция вызывается в среднем 1 000 раз в месяц. Мониторинг 100 Lambda-функций даёт итого 100 000 вызовов в месяц.
Каждый вызов засчитывается как одна единица потребления из вашего бюджета DPS согласно прайс-листу.

Пример потребления: трассировка Azure Functions

Azure Functions предоставляет множество различных вариантов размещения с разными возможностями интеграции трассировки.
Трассировка Azure Functions на плане App Service (dedicated) эквивалентна [Full-Stack Monitoring](/managed/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") и потребляет GiB-часы (в зависимости от объёма памяти и длительности мониторинга App Service).

Для трассировки Azure Functions на плане потребления (consumption plan) потребление мониторинга основано на общем числе мониторируемых вызовов функций.

Предположим, что каждая Azure-функция вызывается в среднем 1 000 раз в месяц. Мониторинг 100 Azure-функций даёт итого 100 000 вызовов в месяц.
Каждый вызов вычитается из доступного бюджета Dynatrace Platform Subscription согласно прайс-листу.

Пример потребления: трассировка Google Functions

### Трассировка Google Functions

Для интеграции трассировки Google Functions потребление мониторинга основано на общем числе мониторируемых вызовов функций.

Предположим, что каждая Google-функция вызывается в среднем 1 000 раз в месяц. Мониторинг 100 Google-функций даёт итого 100 000 вызовов в месяц.
Каждый вызов вычитается из доступного бюджета Dynatrace Platform Subscription согласно прайс-листу.

Если платформенный хост Serverless Functions мониторируется с помощью OneAgent (потребляя GiB-часы), все мониторируемые вызовы функций входят в пакет Full-Stack Monitoring и не влекут дополнительного потребления.

## Отслеживание потребления

В этом разделе описаны различные инструменты Dynatrace для отслеживания потребления и затрат.

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет встроенные метрики использования для анализа потребления Serverless Functions Classic в вашей организации.

Для использования в Data Explorer введите DPS в поле **Search**.
Эти метрики также доступны через Environment API и связаны в Account Management (**Usage summary** > **Serverless Functions Classic** > **Actions** > **View details**).
В таблице ниже перечислены метрики для мониторинга потребления Serverless Functions Classic в вашей организации.

(DPS) Total Serverless Functions Classic billing usage
:   Ключ: `builtin:billing.serverless_functions_classic.usage`

    Измерение: count

    Разрешение: 1 мин

    Описание: Количество тарифицируемых вызовов бессерверных функций, агрегированных по всем мониторируемым сущностям.

(DPS) Serverless Functions Classic billing usage by function
:   Ключ: `builtin:billing.serverless_functions_classic.usage_by_function`

    Измерение: `function\[STRING]`

    Разрешение: 1 мин

    Описание: Количество тарифицируемых вызовов бессерверных функций с разбивкой по функциям.

(DPS) Serverless Functions Classic billing usage by monitored entity
:   Ключ: `builtin:billing.serverless_functions_classic.usage_by_entity`

    Измерение: `dt.entity.monitored_entity\[ME:MONITORED_ENTITY]`

    Разрешение: 1 мин

    Описание: Количество тарифицируемых вызовов бессерверных функций с разбивкой по мониторируемой сущности.

Суммарное количество тарифицируемых вызовов бессерверных функций за различные интервалы в любом выбранном периоде можно отслеживать с помощью метрики «(DPS) Total Custom Traces Classic billing usage».
В примере ниже показано потребление, агрегированное в 1-часовых интервалах.
С 11:00 до 14:00 каждый час потреблялось около 900 вызовов бессерверных функций.

![Serverless Functions Classic (DPS)](https://dt-cdn.net/images/image064-907-fcdf87929d.png)

Serverless Functions Classic (DPS)

Для просмотра количества вызовов с разбивкой по бессерверной функции используйте метрику «(DPS) Serverless Functions Classic billing usage by function».
В примере ниже показан список бессерверных функций и количество вызовов с 12:00 до 13:00.

![Serverless Functions Classic (DPS)](https://dt-cdn.net/images/image066-905-edf3744b25.png)

Serverless Functions Classic (DPS)

Для просмотра количества вызовов с разбивкой по мониторируемой сущности используйте метрику «(DPS) Serverless Functions Classic billing usage by monitored entity».
В примере ниже показан список сущностей и количество вызовов с 12:00 до 13:00.

![Serverless Functions Classic (DPS)](https://dt-cdn.net/images/image068-905-abb9ca1dda.png)

Serverless Functions Classic (DPS)

## Связанные темы

* [Обзор расширений платформы (DPS)](/managed/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)