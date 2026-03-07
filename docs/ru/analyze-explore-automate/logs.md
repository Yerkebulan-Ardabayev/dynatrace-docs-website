---
title: Log Analytics
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs
scraped: 2026-03-06T21:10:16.285435
---

# Аналитика логов

# Аналитика логов

* Последняя версия Dynatrace
* Описание
* Чтение: 6 мин
* Обновлено 28 января 2026 г.

Управление и аналитика логов на основе [Grail](/docs/platform/grail/dynatrace-grail "Grail — это хранилище данных Dynatrace, специально разработанное для данных наблюдаемости и безопасности, выступающее единым унифицированным хранилищем для логов, метрик, трассировок, событий и многого другого.") обеспечивает унифицированный подход к извлечению ценности из данных логов на платформе Dynatrace.

Простое управление данными логов позволяет [загружать](/docs/analyze-explore-automate/logs/lma-log-ingestion "Потоковая передача данных логов в Dynatrace.") петабайты данных без схем, индексации или регидратации. Все эти данные доступны в любое время для любых аналитических задач. Благодаря схеме при чтении и [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.") нет необходимости решать, что вы хотите запрашивать, на этапе загрузки данных. Выберите период хранения данных, соответствующий вашим бизнес-требованиям и требованиям соответствия, будь то для отладки или аудита.

Используйте Dynatrace Log Management and Analytics:

* **Улучшение унифицированной наблюдаемости**: интегрируйте логи с трассировками и метриками для комплексной наблюдаемости в Kubernetes и облаке. Используйте Grail, DQL и ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** для унифицированного исследования и визуализации с помощью дашбордов.
* **Ускорение решения проблем**: используйте логи для детального устранения неполадок, применяя Dynatrace Intelligence для определения релевантных логов и сокращения среднего времени восстановления. Выполняйте мгновенные запросы с помощью Grail и DQL для быстрого решения проблем.
* **Устранение пробелов в мониторинге**: отслеживайте метрики, состояние, производительность и бизнес-показатели из гибридных облачных и мейнфрейм-развертываний. Автоматизируйте сбор логов с помощью OneAgent, анализируйте и обрабатывайте логи в масштабе с OpenPipeline и преобразуйте логи в метрики с помощью Grail и DQL.

## Начало работы

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Краткое руководство по началу работы**

[Сделайте первые шаги для подключения и изучения ваших логов.](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-real-time-observability-logs-dql "Изучите сценарий использования Log Management and Analytics для наблюдаемости логов в реальном времени.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Загрузка логов**

[Настройте сбор логов для автоматического получения логов из различных источников.](/docs/analyze-explore-automate/logs/lma-log-ingestion "Потоковая передача данных логов в Dynatrace.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Настройка бакетов и разрешений**

[Сконфигурируйте хранилище и определите сроки хранения и контроль доступа.](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Данные логов могут храниться в бакетах хранения данных на основе определенных сроков хранения.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Настройка обработки в OpenPipeline**

[Определите, как загруженные логи обрабатываются и хранятся.](/docs/analyze-explore-automate/logs/lma-log-processing "Используйте Dynatrace на основе Grail и DQL для преобразования входящих данных логов для лучшего понимания, анализа или дальнейшей обработки.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Приложение** **Logs**

Узнайте, как использовать ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.](/docs/analyze-explore-automate/logs/lma-logs-app "Поиск, фильтрация и анализ логов с помощью приложения Dynatrace Logs для быстрого исследования и обмена результатами.")[![Шаг 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Шаг 6")

**Оповещения, проблемы и автоматизация**

[Создавайте обнаружение аномалий и оповещения, а также автоматизируйте процесс обнаружения.](/docs/analyze-explore-automate/logs/alerting-on-logs "Создавайте или позвольте Dynatrace создавать оповещения на основе данных логов в системе мониторинга логов Dynatrace")

Данные логов могут поступать из различных источников, включая Kubernetes, технологические стеки, облачные сервисы, гиперскейлеры, пользовательские API-интеграции или расширения Dynatrace. Dynatrace использует OneAgent и API как основные методы загрузки логов из этих источников.

Загруженные логи направляются в Dynatrace OpenPipeline для обработки, анализа и хранения.

![Обзор платформы Dynatrace](https://dt-cdn.net/images/logs-overview-2678-9573941b3e.png)

Хранилище данных Grail служит единым унифицированным решением для хранения, где данные логов взаимосвязаны в рамках модели реального времени, отражающей топологию и зависимости в контролируемой среде.

Вы можете анализировать загруженные данные в ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**, выполнять запросы в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** для получения полного представления о данных логов или использовать ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** для визуализации и мониторинга в реальном времени.

## Модель потребления

Модель потребления для Log Management and Analytics основана на трех измерениях использования данных (загрузка и обработка, хранение и запросы). Единицей измерения потребляемого объема данных являются гибибайты (GiB). Кроме того, доступна опция **Хранение с включенными запросами**, объединяющая измерения запросов и хранения. Подробнее см. в разделе [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Узнайте, как рассчитывается потребление Dynatrace Log Analytics с использованием модели подписки Dynatrace Platform Subscription.").

## Доступность и предыдущие версии

Log Management and Analytics — это новейшее предложение для работы с логами, доступное в Dynatrace SaaS с Grail.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Изучите в Dynatrace Hub

[Принимайте более обоснованные и быстрые решения при устранении неполадок и оценке состояния ваших сред: автоматически объединяйте логи, трассировки и метрики событий в реальном времени, отслеживайте Kubernetes, оптимизируйте затраты на хранение, извлекая метрики из логов при загрузке или чтении, и быстрее решайте инциденты.](https://www.dynatrace.com/hub/?filter=log-management-and-analytics&internal_source=doc&internal_medium=link&internal_campaign=cross)

## Связанные темы

* [Обновление до Log Management and Analytics](/docs/analyze-explore-automate/log-monitoring/logs-upgrade/lmc-logs-upgrade-to-lma "Log Management and Analytics — это новейшее решение для мониторинга логов Dynatrace. Мы рекомендуем перейти на это последнее предложение мониторинга логов.")
* [Сценарии использования Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-use-cases "Изучите распространенные сценарии использования Log Management and Analytics в развертываниях Dynatrace.")
* [Примеры логов на Grail](/docs/analyze-explore-automate/logs/logs-on-grail-examples "Изучите базовые примеры Log Management and Analytics по использованию данных логов в Dynatrace на основе Grail.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.")
