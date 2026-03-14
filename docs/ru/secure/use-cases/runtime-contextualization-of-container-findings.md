---
title: Контекстуализация во время выполнения результатов контейнеров
source: https://www.dynatrace.com/docs/secure/use-cases/runtime-contextualization-of-container-findings
scraped: 2026-03-06T21:15:09.804438
---

# Контекстуализация результатов анализа контейнеров во время выполнения

# Контекстуализация результатов анализа контейнеров во время выполнения

* Latest Dynatrace
* Tutorial
* Обновлено 30 сентября 2025 г.

Сканирование образов контейнеров обычно выполняется в репозиториях артефактов, таких как [AWS Elastic Container Registry (ECR)](https://dt-url.net/mu03pcw), [GCP Artifact Registry](https://dt-url.net/9g03udo) и [Microsoft Azure Container Registry](https://dt-url.net/mn23u20). После развёртывания образов в продуктивной среде непрерывная переоценка образов контейнеров необходима для того, чтобы убедиться, что они не подвержены вновь появляющимся критическим уязвимостям.

Количество обнаруженных уязвимостей растёт вместе с количеством хранящихся образов контейнеров, и команда разработки может быть перегружена количеством критических результатов. Некоторые из образов контейнеров никогда не будут развёрнуты в вашей продуктивной среде. Они могут быть частью ваших тестовых сред или устареть и оставаться в репозитории как устаревшие.

В этом контексте Dynatrace помогает вам:

* Снизить усталость от оповещений
* Сосредоточить усилия по устранению на критических результатах уязвимостей, которые существенно влияют на ваши продуктивные приложения

![Обзор сокращения оповещений об уязвимостях](https://dt-cdn.net/images/final-final-v3-last-final-teo-500-f2e05b1ca1.png)

## Целевая аудитория

Инженеры по надёжности (SRE) и владельцы приложений, которые хотят поддерживать гигиену безопасности и работоспособность своих приложений.

## Сценарий

* Команда разработки хранит образы контейнеров в Amazon ECR. Впоследствии эти образы развёртываются в средах подготовки и продуктивных средах, работающих на Kubernetes.
* Вы мониторите работоспособность ваших приложений с помощью Dynatrace OneAgent в Kubernetes.
* Несколько новых критических уязвимостей были недавно обнаружены Amazon ECR в образах контейнеров.

### Запрос

* Автоматическая сортировка критических уязвимостей и оценка ситуации.
* Автоматическое создание заявок и уведомлений для вновь появляющихся критических уязвимостей, угрожающих вашему продуктивному приложению.

### Цель

Предотвратить воздействие критических уязвимостей на продуктивные приложения в контейнерах с уязвимыми образами контейнеров.

### Результат

Наше решение позволяет:

* Фильтровать критические результаты в продуктивных приложениях на контейнерах с уязвимыми образами контейнеров
* Создавать рабочие процессы автоматизации уведомлений на основе этих результатов

## Предварительные условия

* [Настройка наблюдаемости Kubernetes с Dynatrace Operator](../../ingest-from/setup-on-k8s/deployment/other/classic-full-stack.md "Развёртывание Dynatrace Operator в классическом режиме full-stack в Kubernetes")
* [Приём результатов сканирования уязвимостей и событий сканирования Amazon ECR](../threat-observability/security-events-ingest/ingest-aws-ecr-data.md "Приём результатов сканирования уязвимостей образов контейнеров Amazon ECR и событий сканирования и их анализ в Dynatrace.")
* [Использование тегов продукта/стадии релиза Dynatrace](../../deliver/release-monitoring/version-detection-strategies.md "Метаданные для определения версий в различных технологиях") для ваших контейнеров

## Начало работы

1. Визуализация

Для просмотра сводного и унифицированного списка недавних результатов сканирования уязвимостей, полученных из Amazon ECR

1. Откройте [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Создание интерактивных, настраиваемых представлений для визуализации, анализа и обмена данными наблюдаемости в режиме реального времени.") и перейдите в **Ready-made**.
2. Найдите и выберите **Container Vulnerability Findings** для интеграции с Amazon ECR.

Пример дашборда:

![Пример дашборда уязвимостей контейнеров](https://dt-cdn.net/images/new-dashboard-4308-b95f9d6ec2.png)

2. Фильтрация

1. Фильтруйте по `RuntimeStatus`, чтобы отобразить контекстуализированные результаты, влияющие на ваши работающие контейнеры.

   ![Фильтр по статусу выполнения](https://dt-cdn.net/images/2024-11-04-10-10-45-1835-6e0d130070.png)
2. Фильтруйте по `ProductStage`, чтобы отобразить контекстуализированные результаты, влияющие на ваши продуктивные сервисы и приложения.

   ![Фильтр по стадии продукта](https://dt-cdn.net/images/2024-11-04-10-12-42-1829-24210337bc.png)

3. Автоматизация

Вы можете адаптировать наши примеры рабочих процессов автоматизации для обогащения и фильтрации внешних результатов уязвимостей образов контейнеров с учётом контекста выполнения. Подробности см. в [Автоматизация и оркестрация результатов безопасности](automate-and-orchestrate-security-findings.md "Регулярная проверка критических результатов безопасности и автоматическое создание заявок Jira или оповещений Slack.").

Пример запроса для получения новых критических уязвимостей образов контейнеров со списком затронутых образов контейнеров и работающих контейнеров:

Этот запрос был обновлён для соответствия новой таблице событий безопасности Grail. Полный список обновлений и действий, необходимых для выполнения миграции, см. в [Руководстве по миграции таблицы безопасности Grail](../threat-observability/migration.md "Понимание изменений в новой таблице безопасности Grail и обучение миграции.").

```
// The query has a rolling window of 7 days and the last 24hrs.



// Vulnerability finding events which have already been reported



// before the current 24hr window will not be reported again.



fetch security.events, from: now() - 7d



| filter dt.system.bucket == "default_securityevents"



AND object.type == "CONTAINER_IMAGE"



AND event.type == "VULNERABILITY_FINDING"



AND dt.security.risk.level == "CRITICAL"



// now enrich the runtime context



| join [



fetch dt.entity.container_group_instance, from:now()-3h



| fieldsAdd entity.name, containerImageDigest, containerImageName, workloadName, containerStatus, processes=contains[dt.entity.process_group_instance]



| expand dt.entity.process=processes



| fieldsRemove processes



| join [



fetch dt.entity.process_group_instance, from:now()-3h



], on:{left[dt.entity.process]==right[id]}, kind:leftOuter, fields:{releasesProduct, releasesStage}



], on:{left[container_image.digest]==right[containerImageDigest]}, kind:leftOuter,



fields:{container_instance.id=id, container_instance.name=entity.name, container_image.name=containerImageName,



releasesProduct, releasesStage, containerStatus}



// summarize and filter



| dedup {object.id, vulnerability.id, component.name, component.version,



container_image.registry, container_image.repository}, sort: {timestamp desc}



| parse containerStatus, """LD* "state=" LD:containerStatus ("}" | ",")"""



| fieldsAdd containerStatus=if(isNull(containerStatus),"not running",else:containerStatus)



| fieldsAdd releasesStage=if(isNull(releasesStage), "None", else:releasesStage)



| filter containerStatus=="running" AND releasesStage=="production"



// Aggregate vulnerability findings per vulnerability, repository,



// component and component version.



| summarize {



affected_images_count = count(),



vulnerability_finding_events = collectArray(



record(



object.id = object.id,



event.provider = event.provider,



container_image.registry = container_image.registry,



container_image.repository = container_image.repository,



component.version = component.version,



component.name = component.name,



dt.security.risk.level = dt.security.risk.level,



ingest_time = timestamp



)



)



}, by:{ vulnerability.id, vulnerability.title, event.provider, container_image.registry, container_image.repository, component.name, component.version }



// Filter out, if this vulnerability for the repository and the component



// and version was already reported before the last 24 hours.



// For example, if the same vulnerability was reported multiple times



// during the last 7 days, don't report it again.



| filterOut iAny(vulnerability_finding_events[][ingest_time] < now() - 24h)



// Expand and deduplicate for repetitive findings if they



// were reported more than once in the last 24 hours.



| expand vulnerability_finding_events



| dedup { vulnerability.id, vulnerability.title, vulnerability_finding_events[object.id], vulnerability_finding_events[component.name], vulnerability_finding_events[component.version] }



// Aggregate again to count the unique affected images within each repository.



| summarize {



affected_images_count = count(),



vulnerability_finding_events = collectArray(



vulnerability_finding_events



)



}, by:{ vulnerability.id, vulnerability.title, event.provider, container_image.registry, container_image.repository, component.name, component.version }



| sort vulnerability_finding_events[][ingest_time] desc
```

Пример результата:

![Пример результата](https://dt-cdn.net/images/2024-11-04-09-48-57-1764-c397b99b5c.png)

4. Отслеживание сокращения оповещений

Для отслеживания процесса сокращения оповещений на основе прогрессивной фильтрации на [шаге 2](#filter)

1. Откройте [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Создание интерактивных, настраиваемых представлений для визуализации, анализа и обмена данными наблюдаемости в режиме реального времени.") и перейдите в **Ready-made**.
2. Найдите и выберите **Container image alert reduction** для интеграции с Amazon ECR.

Пример результата:

![Воронковый дашборд, показывающий сокращение оповещений](https://dt-cdn.net/images/funnel-dashboard-4308-16c82e5aa3.png)
