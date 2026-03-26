---
title: Log Monitoring Classic
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring
scraped: 2026-03-06T21:35:33.825630
---

С Log Monitoring как частью платформы Dynatrace вы получаете прямой доступ к содержимому журналов всех ваших критически важных приложений, инфраструктуры и облачных платформ. Вы можете создавать пользовательские метрики журналов для более умного и быстрого устранения неполадок. Вы сможете понимать данные журналов в контексте всего стека, включая влияние на реальных пользователей.

Прекращение поддержки Log Monitoring Classic

Log Monitoring Classic, доступный для развёртываний SaaS и Managed, прекратит поддержку к 2027 году. Подробности см. в объявлении о [прекращении поддержки Log Monitoring Classic](../../whats-new/saas/sprint-328.md#log-monitoring-classic-end-of-life "Примечания к выпуску Dynatrace SaaS, версия 1.328") в наших примечаниях к выпуску.

Мы рекомендуем заблаговременно [перейти на Log Management and Analytics](../../analyze-explore-automate/logs/logs-upgrade/logs-upgrade-to-lma.md "Log Management and Analytics — это новейшее решение Dynatrace для мониторинга журналов. Мы рекомендуем перейти на это новейшее решение для мониторинга журналов.").

![LMC - Обзор каналов приёма данных](https://dt-cdn.net/images/lmc-ingestion-channel-overview-2500-abfee3614c.png)

[### Приём и обработка данных

Настройте автоматический сбор журналов и извлекайте ценность с помощью обработки журналов.](../../analyze-explore-automate/log-monitoring/acquire-log-data.md "Узнайте, как получать данные журналов в Dynatrace Log Monitoring.")[### Анализ

Анализируйте значимые события журналов в нескольких журналах, в различных частях окружения (продакшен) и потенциально за более длительный период времени.](../../analyze-explore-automate/log-monitoring/analyze-log-data.md "Узнайте, как анализировать данные журналов в Dynatrace Log Monitoring.")[### Оповещения

Определяйте шаблоны, события и пользовательские метрики журналов для получения проактивных уведомлений.](../../analyze-explore-automate/log-monitoring/alert-log-data.md "Создавайте или позвольте Dynatrace создавать оповещения на основе данных журналов в Dynatrace Log Monitoring.")[### API

Используйте Dynatrace API для отправки данных журналов в Dynatrace и быстрого поиска, агрегации или экспорта содержимого журналов.](../../dynatrace-api/environment-api/log-monitoring-v2.md "Узнайте, что можно делать с помощью Log Monitoring API v2.")

#### Конфигурация

[Получите последнюю версию Log Monitoring](../../analyze-explore-automate/log-monitoring/logs-upgrade/lmc-logs-upgrade-to-lma.md "Log Management and Analytics — это новейшее решение Dynatrace для мониторинга журналов. Мы рекомендуем перейти на это новейшее решение для мониторинга журналов.")

[Настройте вашу конфигурацию](../../analyze-explore-automate/log-monitoring/log-monitoring-configuration.md "Узнайте, как настроить Dynatrace Log Monitoring.")

[Лимиты по умолчанию](../../analyze-explore-automate/log-monitoring/log-monitoring-limits.md "Лимиты по умолчанию для последней версии Dynatrace Log Monitoring.")

[Поддерживаемые форматы данных журналов](../../analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-data-format.md "В этом разделе перечислены все форматы журналов, поддерживаемые Log Monitoring.")

[Связывание данных журналов с трассировками](../../analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment.md "Узнайте, как связать входящие данные журналов с трассировками для более точного анализа в Dynatrace.")

[Правила приёма журналов](../../analyze-explore-automate/log-monitoring/acquire-log-data/log-storage.md "Настройте хранение файлов журналов, уже известных OneAgent.")

[Часто задаваемые вопросы по Log Monitoring](../../analyze-explore-automate/log-monitoring/lmc-troubleshooting.md "Устранение проблем, связанных с настройкой и конфигурацией Log Monitoring Classic.")

#### Получение данных журналов

[Автообнаружение](../../analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2.md "Узнайте об автоматическом обнаружении содержимого журналов и требованиях для автообнаружения.")

[Добавление файлов журналов вручную](../../analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2.md "Узнайте, как вручную добавить файлы журналов для анализа.")

[Общий приём журналов](../../analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api.md "Узнайте, как Dynatrace принимает данные журналов и какие существуют ограничения.")

[Пересылка журналов из облака](../../analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding.md "Узнайте, как настроить пересылку журналов из AWS, Azure и Google Cloud для приёма журналов.")

[Журналы из Kubernetes](../../analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes.md "Узнайте, как мониторить журналы в Kubernetes.")

[Добавление источников журналов](../../analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2.md "Узнайте, как включать и исключать источники журналов для анализа.")

[Обработка журналов](../../analyze-explore-automate/log-monitoring/log-processing.md "Создавайте правила обработки журналов, которые преобразуют входящие данные журналов для лучшего анализа или дальнейшей обработки.")

#### Анализ данных журналов

[Просмотрщик журналов](../../analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer.md "Узнайте, как использовать просмотрщик журналов Dynatrace для анализа данных журналов.")

[События журналов](../../analyze-explore-automate/log-monitoring/analyze-log-data/log-events.md "Узнайте, как создавать и использовать события журналов Dynatrace для анализа данных журналов.")

[Метрики журналов](../../analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics.md "Узнайте, как создавать и использовать метрики журналов Dynatrace для анализа данных журналов.")

[Пользовательские атрибуты журналов](../../analyze-explore-automate/log-monitoring/analyze-log-data/log-custom-attributes.md "Узнайте, как создавать и использовать пользовательские атрибуты при приёме данных журналов.")

[Зоны управления](../../analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring.md "Узнайте, как принятые данные журналов назначаются зонам управления.")

## Связанные темы

* [Мониторинг журналов](https://www.dynatrace.com/platform/log-monitoring/)
* [DDU для Log Monitoring Classic](../../license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption.md "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.")
