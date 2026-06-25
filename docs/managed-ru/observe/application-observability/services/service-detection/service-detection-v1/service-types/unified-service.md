---
title: Unified services
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service
scraped: 2026-05-12T12:02:24.401298
---

# Unified services

# Unified services

* How-to guide
* 6-min read
* Updated on Oct 13, 2025

Dynatrace версии 1.274

## Обзор

Тип **Unified service** представляет сервисы, обнаруженные с помощью правил Service Detection v2 (SDv2) на основе атрибутов ресурсов.

Сервисы, использующие обнаружение SDv2, отображают **Unified service** в качестве типа сервиса в свойствах веб-интерфейса, что указывает на применение правил обнаружения SDv2.

Ключевые возможности:

* Метрики времени отклика, пропускной способности и частоты отказов
* Автоматическое обнаружение и мониторинг конечных точек

Термин «unified services» был введён до появления SDv2. Базовые правила обнаружения сервисов, конечных точек, сбоев и разделения были введены одновременно, но были жёстко закодированы. SDv2 делает эти правила настраиваемыми. Хотя в свойствах по-прежнему отображается **Unified service**, SDv2 сосредоточен на правилах обнаружения, а не на типах сервисов.

Актуальные правила обнаружения и параметры настройки см. в разделе [Service Detection v2](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Узнайте, как обнаруживать, именовать и разделять сервисы из OpenTelemetry и OneAgent spans.").

## Устаревшие span:service

Устаревшие **span:services** были автоматически перенесены в SDv2 (**Unified service**) к 1 октября 2025 года.

Это затрагивает только **span:services** (сервисы, поступающие через OTLP API), но не **span (default) services**, обнаруженные OneAgent с сенсором OpenTelemetry, которые останутся без изменений.

Подробнее см. в публикации [Service Detection V2 (SDv2) Overview](https://dt-url.net/b4030ff) в сообществе Dynatrace.

## Управление мониторингом конечных точек

Метриками конечных точек — такими как время отклика, пропускная способность и частота отказов — можно управлять, настраивая сбор метрик конечных точек на уровне окружения и переопределения на уровне сервиса.

Изменения в настройках сбора метрик конечных точек влекут за собой последствия для биллинга.

Metrics Classic billing

В следующей таблице перечислены классические метрики конечных точек; метрики, [потребляющие DDU](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе единиц данных Davis (DDU)."), тарифицируются. Для данных на основе OneAgent эти метрики не записываются.

| Ключ метрики | Название и описание | Единица | Агрегации | Потребление мониторинга |
| --- | --- | --- | --- | --- |
| builtin:service.request.count | Unified service request count Количество запросов, полученных данным сервисом. Чтобы узнать, как Dynatrace обнаруживает и анализирует сервисы, см. [Services](https://dt-url.net/am-services). | Count | autovalue | DDUs |
| builtin:service.request.failure\_count | Unified service failure count Количество неудачных запросов, полученных данным сервисом. Чтобы узнать, как Dynatrace обнаруживает и анализирует сервисы, см. [Services](https://dt-url.net/am-services). | Count | autovalue | Host units |
| builtin:service.request.response\_time | Unified service request response time Время отклика сервиса, измеренное в микросекундах на стороне сервера (измерения на стороне сервера не включают, например, время прокси и сети). Время отклика — это время до отправки ответа вызывающему приложению, процессу или другому сервису. Оно не включает дальнейшую асинхронную обработку. Чтобы узнать, как Dynatrace рассчитывает тайминги сервисов, см. [Service analysis timings](https://dt-url.net/service-timings). | Millisecond | autocountmaxmedianminpercentile | DDUs |

Чтобы управлять мониторингом конечных точек для всех unified services в вашем окружении

1. Перейдите в **Settings**.
2. Выберите **Service Detection**.
3. Выберите **Unified services endpoint metrics** и включите/выключите **Enable endpoint metrics**.

Чтобы переопределить мониторинг конечных точек для конкретного unified service

1. Перейдите в **Services**.
2. Необязательно На странице **Services** в столбце **Service type** установите флажок **Unified service**.
3. Найдите и выберите сервис, для которого требуется настроить мониторинг конечных точек.
4. На странице обзора сервиса выберите **More** (**…**) > **Settings**.
5. На странице **Service settings** выберите **Endpoint metrics**.
6. На странице **Unified services endpoint metrics** включите/выключите **Enable endpoint metrics**.