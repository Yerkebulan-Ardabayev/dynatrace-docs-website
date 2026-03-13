---
title: Segment requests to improve response time degradation
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-traces/use-cases/segment-request
scraped: 2026-03-06T21:12:14.538129
---

# Сегментация запросов для улучшения деградации времени отклика

# Сегментация запросов для улучшения деградации времени отклика

* Classic
* Руководство
* Чтение: 3 минуты
* Обновлено 17 мая 2024 г.

В вашей среде существуют тысячи запросов, каждый со своими связями и контекстом. Чтобы определить корневую причину неэффективности, необходимо сузить анализ до нужных запросов. Вы можете сегментировать запросы, [применяя фильтрацию в сервисном потоке](../../services-classic/service-flow/service-flow-filtering.md "Узнайте, как работает фильтрация сервисного потока и как ею пользоваться."), или через [анализ выбросов](../../services-classic/response-time-distribution-and-outlier-analysis.md "Получите аналитические данные о распределении времени отклика для всех запросов, включая аномально высокие и аномально низкие.").

## Сценарий

Сервис `easyTravel Customer Frontend` получил 249 000 запросов за выбранный двухчасовой период. В этом примере мы хотим выявить запросы с медленным временем отклика для данного сервиса.

## Шаги

1. Начните с сегментации запросов через **Service flow**.

   1. Чтобы открыть сервисный поток:

      1. Перейдите в ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
      2. Выберите сервис, который хотите проанализировать.
      3. На странице обзора сервиса в разделе **Understand dependencies** выберите **View service flow**.

      Нас интересуют конкретно запросы от `easyTravel Customer Frontend`, которые сначала вызывают `AuthenticationService`, а затем `easyTravel-Business`. **94%** запросов `easyTravel Customer Frontend`, вызывающих `AuthenticationService`, также вызывают `VerificationService`.
   2. Чтобы сосредоточиться на подмножестве запросов:

      1. Выберите вызываемый сервис > **Apply filter** ![Filter](https://dt-cdn.net/images/filter-icon-41ddd02d66.svg "Filter").

         ![Segmentation of transactions via service flow](https://dt-cdn.net/images/transactions-manual-segmentation-1225-210c1e1ad2.png)
      2. Чтобы добавить сервис в качестве второго параметра фильтра, выберите нужный сервис.

         ![Refine chain of calls](https://dt-cdn.net/images/service-flow-chain-of-calls-1221-12f6c53a07.png)
2. Чтобы открыть список распределённых трасс с фильтром по заданным параметрам, выберите вызывающий сервис (`easyTravel Customer Frontend`) > **Distributed traces** ![Distributed traces](https://dt-cdn.net/images/purepaths-icon-790bea38ba.svg "Distributed traces").

   Список **Most recent traces** отображает запросы, инициированные `easyTravel Customer Frontend` и соответствующие заданным критериям фильтрации. Список можно фильтровать или сортировать по **Start time**, **Name**, **Response time**, **Processing time**, **HTTP method** или **Response code**.
3. Чтобы отображать только запросы `easyTravel Customer Frontend` со временем отклика, большим или равным 80 мс:

   1. Выберите узел **easyTravel Customer Frontend**.
   2. Из списка **Filter requests** выберите **Response time**.
   3. Выберите **greater than or equal to ≥**, введите `80` в поле ввода и нажмите **Apply**.
   4. Выберите **Apply**.

   ![Filter distributed traces](https://dt-cdn.net/images/filter-distributd-traces-1621-2d6b34444e.png)

   Только **3** запроса из первоначальных 249 000 требуют углублённого анализа распределённых трасс.

   ![Detection of slow requests](https://dt-cdn.net/images/slower-requests-detection-1589-e1fc1d5a66.png)
4. Выберите трассу из уточнённого списка для последующего анализа на уровне кода.

## Вывод

Сегментировав запросы в сервисном потоке `easyTravel Customer Frontend` и сузив выборку до тех, которые удовлетворяют нашим критериям, мы сократили необходимый углублённый анализ с 249 000 до 3 запросов за выбранный двухчасовой период.

Вы можете расширить анализ:

* Чтобы увидеть, откуда пришёл запрос, выберите **More** (**...**) > [**Service backtrace**](../../services-classic/service-backtrace.md "Отслеживайте последовательность вызовов сервисов вплоть до клика в браузере, который запустил цепочку вызовов.").
* Чтобы увидеть всю трассу от первой полностью отслеживаемой группы процессов, выберите **Show full trace**.
  Каждая распределённая трасса отслеживает запрос от начала до конца. Это означает, что трассы всегда начинаются с первой полностью отслеживаемой группы процессов. С помощью этой опции вы можете изменить перспективу и сфокусироваться только на одном сервисе.
