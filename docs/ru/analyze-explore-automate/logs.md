---
title: Log Analytics
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs
scraped: 2026-02-06T16:00:00.287320
---

# Журнал аналитики

# Журнал аналитики

* Последняя версия Dynatrace
* Объяснение
* 6-минутное чтение
* Обновлено 28 января 2026 г.

Управление журналами и аналитика на базе [Грааль](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.") обеспечивают унифицированный подход к раскрытию ценности данных журналов на платформе Dynatrace.

Простое управление данными журналов позволяет вам хранить [проглотить](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.") петабайт данных без схем, индексации или повторной гидратации.Все эти данные можно использовать в любое время для любой аналитической задачи.Благодаря функции чтения схемы и [Язык запросов Dynatrace (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") нет необходимости решать, что вы хотите запросить во время приема данных.Выберите период хранения ваших данных, который соответствует вашему бизнесу и требованиям соответствия требованиям, будь то для целей отладки или аудита.

Используйте Dynatrace Log Management and Analytics:

* **Улучшите унифицированное наблюдение**: интегрируйте журналы с трассировками и метриками для комплексного наблюдения в Kubernetes и облаке.Используйте Grail, DQL и ![Ноутбуки](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Блокноты** для унифицированного исследования и визуализации с помощью информационных панелей.
* **Ускорение решения проблем**: используйте журналы для подробного устранения неполадок, а Dynatrace Intelligence позволяет точно находить соответствующие журналы и сокращать среднее время ремонта.Выполняйте мгновенные запросы к Grail и DQL для быстрого решения проблем.
* **Устранение пробелов в мониторинге**: отслеживайте метрики, работоспособность, производительность и бизнес-показатели при развертывании гибридного облака и мэйнфрейма.Автоматизируйте сбор журналов с помощью OneAgent, анализируйте и обрабатывайте журналы в любом масштабе с помощью OpenPipeline и преобразуйте журналы в метрики с помощью Grail и DQL.

## Начать

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Краткое руководство**

Сделайте первые шаги по внедрению и изучению журналов.](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-real-time-observability-logs-dql "Изучите вариант использования Log Management and Analytics для наблюдения в реальном времени с помощью журналов")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Прием журналов**

Настройте сбор журналов для автоматического переноса журналов из разных источников.](/docs/analyze-explore-automate/logs/lma-log-ingestion «Потоковая передача данных журналов в Dynatrace.»)[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Настройка сегментов и разрешений**

Настройте хранилище и определите элементы управления хранением и доступом.](/docs/analyze-explore-automate/logs/lma-bucket-assignment «Данные вашего журнала могут храниться в сегментах хранения данных в зависимости от определенных периодов хранения.»)[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Настройка обработки в OpenPipeline**

Определите, как обрабатываются и сохраняются загруженные журналы.](/docs/analyze-explore-automate/logs/lma-log-processing «Используйте Dynatrace на базе Grail и DQL, чтобы изменить форму входящих данных журналов для лучшего понимания, анализа или дальнейшей обработки».)[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы** **приложение**

Узнайте, как использовать ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**.](/docs/analyze-explore-automate/logs/lma-logs-app «Ищите, фильтруйте и анализируйте журналы с помощью приложения Dynatrace Logs, чтобы быстро исследовать и делиться информацией.»)[![Шаг 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Оповещения, проблемы и автоматизация**

Создавайте обнаружение аномалий и оповещения, а также автоматизируйте процесс обнаружения.](/docs/analyze-explore-automate/logs/alerting-on-logs «Создайте или позвольте Dynatrace создавать данные журнала на основе предупреждений в мониторинге журналов Dynatrace»)

Данные журналов могут поступать из разных источников, включая Kubernetes, технологические стеки, облачные сервисы, гипермасштабирующие устройства, пользовательские интеграции API или расширения Dynatrace.Dynatrace использует OneAgent и API в качестве ключевых методов получения журналов из этих источников.

Полученные журналы передаются в Dynatrace OpenPipeline для обработки, анализа и хранения.

![Обзор платформы Dynatrace](https://dt-cdn.net/images/logs-overview-2678-9573941b3e.png)

Озеро данных Grail представляет собой единое унифицированное решение для хранения данных, в котором данные журналов взаимосвязаны в рамках модели реального времени, отражающей топологию и зависимости в контролируемой среде.

Вы можете анализировать полученные данные в ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**, выполнять запросы в ![Ноутбуки](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Блокноты**, чтобы получить полное представление о данных журнала, или использовать ![Панели мониторинга](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Панели мониторинга** для визуализации и мониторинга в реальном времени.

## Модель потребления

Модель потребления для управления журналами и аналитики основана на трех измерениях использования данных (прием и обработка, сохранение и запрос).Единицей измерения потребляемого объема данных являются гибибайты (ГиБ).Кроме того, доступен параметр **Сохранять с включенными запросами**, сочетающий параметры запроса и хранения.Подробную информацию см. в [Аналитика журналов (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

## Доступность и предыдущие версии

Управление журналами и аналитика — это новейшее предложение журналов, доступное в Dynatrace SaaS с Grail.

[![Центр](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Исследуйте в Dynatrace Hub

Принимайте более разумные и быстрые решения при устранении неполадок и измерении состояния ваших сред: автоматически объединяйте журналы, трассировки и метрики событий в режиме реального времени, отслеживайте Kubernetes, оптимизируйте затраты на хранилище за счет извлечения метрик из журналов во время приема или чтения, а также разрешайте инциденты.быстрее.](https://www.dynatrace.com/hub/?filter=log-management-and-analytics&internal_source=doc&internal_medium=link&internal_campaign=cross)

## Похожие темы

* [Обновление до управления журналами и аналитикой](/docs/analyze-explore-automate/log-monitoring/logs-upgrade/lmc-logs-upgrade-to-lma "Log Management and Analytics is the latest Dynatrace log monitoring solution. We encourage you to upgrade to this latest log monitoring offer.")
* [Варианты использования управления журналами и аналитики](/docs/analyze-explore-automate/logs/lma-use-cases "Explore common Log Management and Analytics use cases in Dynatrace deployments.")
* [Примеры входа в систему Grail](/docs/analyze-explore-automate/logs/logs-on-grail-examples "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.")
* [Язык запросов Dynatrace](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")