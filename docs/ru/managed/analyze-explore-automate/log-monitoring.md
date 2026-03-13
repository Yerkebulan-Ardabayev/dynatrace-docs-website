---
title: Log Monitoring Classic
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring
scraped: 2026-03-06T21:35:33.825630
---

# Log Monitoring Classic

# Log Monitoring Classic

* Classic
* Чтение: 2 мин
* Обновлено 20 ноября 2025 г.

С Log Monitoring как частью платформы Dynatrace вы получаете прямой доступ к содержимому журналов всех ваших критически важных приложений, инфраструктуры и облачных платформ. Вы можете создавать пользовательские метрики журналов для более умного и быстрого устранения неполадок. Вы сможете понимать данные журналов в контексте всего стека, включая влияние на реальных пользователей.

Прекращение поддержки Log Monitoring Classic

Log Monitoring Classic, доступный для развёртываний SaaS и Managed, прекратит поддержку к 2027 году. Подробности см. в объявлении о [прекращении поддержки Log Monitoring Classic](/docs/whats-new/saas/sprint-328#log-monitoring-classic-end-of-life "Примечания к выпуску Dynatrace SaaS, версия 1.328") в наших примечаниях к выпуску.

Мы рекомендуем заблаговременно [перейти на Log Management and Analytics](/docs/analyze-explore-automate/logs/logs-upgrade/logs-upgrade-to-lma "Log Management and Analytics — это новейшее решение Dynatrace для мониторинга журналов. Мы рекомендуем перейти на это новейшее решение для мониторинга журналов.").

![LMC - Обзор каналов приёма данных](https://dt-cdn.net/images/lmc-ingestion-channel-overview-2500-abfee3614c.png)

[### Приём и обработка данных

Настройте автоматический сбор журналов и извлекайте ценность с помощью обработки журналов.](/docs/analyze-explore-automate/log-monitoring/acquire-log-data "Узнайте, как получать данные журналов в Dynatrace Log Monitoring.")[### Анализ

Анализируйте значимые события журналов в нескольких журналах, в различных частях окружения (продакшен) и потенциально за более длительный период времени.](/docs/analyze-explore-automate/log-monitoring/analyze-log-data "Узнайте, как анализировать данные журналов в Dynatrace Log Monitoring.")[### Оповещения

Определяйте шаблоны, события и пользовательские метрики журналов для получения проактивных уведомлений.](/docs/analyze-explore-automate/log-monitoring/alert-log-data "Создавайте или позвольте Dynatrace создавать оповещения на основе данных журналов в Dynatrace Log Monitoring.")[### API

Используйте Dynatrace API для отправки данных журналов в Dynatrace и быстрого поиска, агрегации или экспорта содержимого журналов.](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Узнайте, что можно делать с помощью Log Monitoring API v2.")

#### Конфигурация

[Получите последнюю версию Log Monitoring](/docs/analyze-explore-automate/log-monitoring/logs-upgrade/lmc-logs-upgrade-to-lma "Log Management and Analytics — это новейшее решение Dynatrace для мониторинга журналов. Мы рекомендуем перейти на это новейшее решение для мониторинга журналов.")

[Настройте вашу конфигурацию](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration "Узнайте, как настроить Dynatrace Log Monitoring.")

[Лимиты по умолчанию](/docs/analyze-explore-automate/log-monitoring/log-monitoring-limits "Лимиты по умолчанию для последней версии Dynatrace Log Monitoring.")

[Поддерживаемые форматы данных журналов](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-data-format "В этом разделе перечислены все форматы журналов, поддерживаемые Log Monitoring.")

[Связывание данных журналов с трассировками](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment "Узнайте, как связать входящие данные журналов с трассировками для более точного анализа в Dynatrace.")

[Правила приёма журналов](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage "Настройте хранение файлов журналов, уже известных OneAgent.")

[Часто задаваемые вопросы по Log Monitoring](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Устранение проблем, связанных с настройкой и конфигурацией Log Monitoring Classic.")

#### Получение данных журналов

[Автообнаружение](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2 "Узнайте об автоматическом обнаружении содержимого журналов и требованиях для автообнаружения.")

[Добавление файлов журналов вручную](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2 "Узнайте, как вручную добавить файлы журналов для анализа.")

[Общий приём журналов](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace принимает данные журналов и какие существуют ограничения.")

[Пересылка журналов из облака](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding "Узнайте, как настроить пересылку журналов из AWS, Azure и Google Cloud для приёма журналов.")

[Журналы из Kubernetes](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes "Узнайте, как мониторить журналы в Kubernetes.")

[Добавление источников журналов](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2 "Узнайте, как включать и исключать источники журналов для анализа.")

[Обработка журналов](/docs/analyze-explore-automate/log-monitoring/log-processing "Создавайте правила обработки журналов, которые преобразуют входящие данные журналов для лучшего анализа или дальнейшей обработки.")

#### Анализ данных журналов

[Просмотрщик журналов](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Узнайте, как использовать просмотрщик журналов Dynatrace для анализа данных журналов.")

[События журналов](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Узнайте, как создавать и использовать события журналов Dynatrace для анализа данных журналов.")

[Метрики журналов](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Узнайте, как создавать и использовать метрики журналов Dynatrace для анализа данных журналов.")

[Пользовательские атрибуты журналов](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-custom-attributes "Узнайте, как создавать и использовать пользовательские атрибуты при приёме данных журналов.")

[Зоны управления](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Узнайте, как принятые данные журналов назначаются зонам управления.")

## Связанные темы

* [Мониторинг журналов](https://www.dynatrace.com/platform/log-monitoring/)
* [DDU для Log Monitoring Classic](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.")
