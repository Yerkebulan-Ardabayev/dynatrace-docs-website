---
title: Метрики
source: https://docs.dynatrace.com/managed/analyze-explore-automate/metrics-classic
scraped: 2026-05-12T11:03:12.472970
---

# Метрики

# Метрики

* Обзор
* Чтение: 2 мин
* Обновлено 09 ноября 2023 г.

В Dynatrace доступны различные типы метрик:

* **Встроенные метрики**, предоставляемые OneAgent. Имеют префикс `builtin:` в ключе метрики.

* **Метрики расширений**, предоставляемые расширениями OneAgent или ActiveGate. Имеют префикс `ext:` в ключе метрики.

  Префикс `ext:` используется метриками [расширений OneAgent](/managed/ingest-from/extensions/develop-your-extensions "Разрабатывайте собственные расширения в Dynatrace.") и [расширений ActiveGate](/managed/ingest-from/extensions/develop-your-extensions "Разрабатывайте собственные расширения в Dynatrace."), а также [классическими метриками для интеграции с AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Интегрируйте метрики из Amazon CloudWatch.").

  Несмотря на схожесть названий, метрики интеграции AWS **не** основаны на расширениях.
* **Вычисляемые метрики**, которые вы создаёте сами. Имеют префикс `calc:` в ключе метрики.
* **Пользовательские USQL-метрики**: пользовательские метрики сессий (префикс `uscm.`) и пользовательские метрики действий (префикс `uacm.`). Эти метрики основаны на метаданных, извлечённых из данных пользовательских сессий и действий.
* **Пользовательские метрики**, которые можно передавать в Dynatrace через приём метрик. У них нет фиксированного префикса, так как [протокол приёма](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.") полностью гибок.

Частота сбора метрик

* Инфраструктурные и другие периодические метрики собираются каждые 10 секунд и хранятся как 1-минутные агрегаты. Как правило, включают min/max/count/sum/average измеряемой метрики.
* Метрики сервисов и веб-запросов не имеют фиксированной частоты. Dynatrace захватывает транзакции и отображает медианы и 90-й перцентиль. Страницы анализа RUM и сервисов основаны на этих данных.
* Для приёма пользовательских метрик стандартное разрешение составляет 1 минуту, однако доступны и [сводные статистики](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload-required "Узнайте, как работает протокол приёма данных для Dynatrace Metrics API.").

[### Приём

Отправляйте пользовательские данные в Dynatrace.](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.")[### Встроенные метрики

Обзор метрик, доступных из коробки.](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Изучите полный список встроенных метрик Dynatrace.")[### Метрики самомониторинга

Обзор метрик самомониторинга, доступных из коробки.](/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics "Изучите полный список метрик самомониторинга Dynatrace.")[### Браузер метрик

Обзор всех метрик, доступных в вашей среде.](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace.")

### Вычисляемые метрики

[Log Monitoring](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Узнайте, как создавать и использовать метрики журналов Dynatrace для анализа данных журналов.")

[Сервисы](/managed/observe/application-observability/services/calculated-service-metric "Узнайте, как создать вычисляемую метрику на основе веб-запросов.")

[Synthetic](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors#calculated-metrics "Узнайте, как анализировать точки данных браузерных мониторов.")

[RUM — веб-приложения](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Создавайте вычисляемые метрики и пользовательские диаграммы на их основе для веб-приложений.")

[RUM — мобильные приложения](/managed/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile "Создавайте вычисляемые метрики и пользовательские диаграммы на их основе для мобильных приложений.")

[RUM — пользовательские приложения](/managed/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Создавайте вычисляемые метрики и пользовательские диаграммы на их основе для пользовательских приложений.")

### Пользовательские USQL-метрики

[RUM — веб-приложения](/managed/observe/digital-experience/web-applications/additional-configuration/custom-metrics-from-user-sessions "При каждом закрытии пользовательской сессии Dynatrace может извлекать метрики и хранить их как временные ряды. Узнайте, как настроить и использовать пользовательские USQL-метрики для веб-приложений.")

[RUM — мобильные приложения](/managed/observe/digital-experience/mobile-applications/additional-configuration/custom-metrics-from-user-sessions-mobile-apps "При каждом закрытии пользовательской сессии Dynatrace может извлекать метрики и хранить их как временные ряды. Узнайте, как настроить и использовать пользовательские USQL-метрики для мобильных приложений.")

[RUM — пользовательские приложения](/managed/observe/digital-experience/custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps "При каждом закрытии пользовательской сессии Dynatrace может извлекать метрики и хранить их как временные ряды. Узнайте, как настроить и использовать пользовательские USQL-метрики для пользовательских приложений.")

### Источники метрик

[Открытый приём метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.")

[Метрики OpenTelemetry](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и журналы) в Dynatrace.")

[Метрики сервисов AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик.")

[Метрики сервисов Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Мониторинг сервисов Azure с помощью Dynatrace и просмотр доступных метрик.")

[Метрики для Dynatrace Runtime Vulnerability Analytics](/managed/secure/application-security/vulnerability-analytics/app-sec-metrics "Просмотр доступных метрик Application Security для Dynatrace Runtime Vulnerability Analytics.")

[Метрики журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Узнайте, как создавать и использовать метрики журналов Dynatrace для анализа данных журналов.")

### См. также

[Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.")

[Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API.")

[API вычисляемых метрик](/managed/dynatrace-api/configuration-api/calculated-metrics "Узнайте, что предлагает API конфигурации вычисляемых метрик Dynatrace.")

[События метрик для оповещения](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Узнайте о событиях метрик в Dynatrace.")