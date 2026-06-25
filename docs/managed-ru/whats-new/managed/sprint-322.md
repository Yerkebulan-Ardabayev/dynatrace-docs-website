---
title: Заметки о выпуске Dynatrace Managed версии 1.322
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-322
scraped: 2026-05-12T11:07:58.627277
---

# Заметки о выпуске Dynatrace Managed версии 1.322

# Заметки о выпуске Dynatrace Managed версии 1.322

* Заметки о выпуске
* 10-min read
* Updated on Sep 18, 2025
* Rollout start on Sep 1, 2025

Начало развёртывания: Sep 1, 2025

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.322.

## Объявления

Platform | Metrics

### Предстоящая нативная поддержка гистограмм OpenTelemetry и Prometheus

Начиная с версии кластера 1.324, Dynatrace вводит нативную поддержку гистограмм OpenTelemetry и Prometheus, включая автоматическое вычисление перцентилей. Это улучшение обеспечивает более быстрое обнаружение выбросов производительности и упрощает рабочие процессы наблюдаемости.

**Несовместимое изменение для существующих метрик гистограмм:**

* Существующие метрики гистограмм больше не будут обновляться, однако останутся доступными для исторической визуализации на дашбордах, обеспечивая преемственность и сохранность данных. Новые нативные метрики гистограмм будут доступны под отдельными ключами метрик с суффиксом `.histogram`.
* Если существующая метрика уже заканчивается на `.histogram` или `_histogram`, она перестанет получать новые точки данных. Чтобы использовать новую функциональность гистограмм под тем же ключом метрики, необходимо удалить существующую метрику с помощью [Metrics API — DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API."). После удаления новая метрика гистограммы будет автоматически создана под тем же ключом.

В Dynatrace, в вашем [окружении **Local-Self-Monitoring**](/managed/managed-cluster/self-monitoring/local-self-monitoring "Learn how to use local self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health."), можно использовать следующий запрос в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") для просмотра ingested-метрик гистограмм:

```
isfm:active_gate.metrics.ingest.explicit_bucket_histogram.layout.series



:splitBy(metric_key,"dt.tenant.uuid",data_source)



:sort(value(auto,descending))



:limit(100)
```

Для выполнения этого запроса требуется версия кластера 1.314+ и наличие соответствующей метрики.

## Новые функции и улучшения

Application Observability | Services

### Определение пользовательских сервисов для кратковременных процессов Go через веб-интерфейс

Теперь можно определить пользовательский сервис для кратковременных процессов Go через веб-интерфейс. Функция **Define entry point manually** теперь доступна для Go, аналогично Java.

Ранее определение пользовательского сервиса для кратковременных процессов Go было возможно только через [Configuration API](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services#go-service-via-api "Define entry points (a method, class, or interface) for custom services that don't use standard protocols.").

Подробнее см. в разделе [Правила обнаружения сервисов](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Use detection rules to customize and enhance the automated detection of your services.").

Digital Experience | Session Replay

### Session Replay: улучшение мобильного браузерного интерфейса и обработки iframe

Сессия, записанная из мобильного браузера, теперь отображает незаписанные промежутки на экране вместо поддельных элементов интерфейса (клавиатура, навигационная панель).

Сессии, записанные на десктопе из не-top-уровневого iframe с длинным разрешением, масштабируются до области взаимодействия.

Digital Experience | Session Replay

### Добавлены новые заполнители для элементов frameset и canvas

Session Replay теперь имеет заполнители для замены неподдерживаемых элементов frameset и canvas.

Также добавлены пояснения для обоих заполнителей в блок легенды заполнителей изображений.

Infrastructure Observability | Hosts

### Добавлены поля Python module и script в группу процессов

Поля Python module и script теперь доступны для групп процессов и процессов Python.

Infrastructure Observability | Extensions

### Extension Execution Controller включён по умолчанию

Extension Execution Controller (EEC) теперь включён по умолчанию в новых окружениях. Для существующих окружений изменений нет.

Platform | Dashboards

### Совместный доступ к дашбордам с пользователями и группами на основе политик IAM

В дополнение к предоставлению доступа к дашбордам пользователям и группам на основе ролей теперь можно предоставлять доступ пользователям и группам на основе политик IAM через настройку совместного доступа к конкретному дашборду.

Platform | Metrics

### Увеличен лимит измерений метрик по умолчанию для модели аномалии со статическим порогом

Лимит измерений метрик по умолчанию для конфигураций статического порога увеличен с `1,000` до `2,000`.

## Несовместимые изменения

Application Observability | Services

### Service Detection v2: правила обнаружения конечных точек обновлены

В этом выпуске конечными точками становятся только точки входа сервиса (серверные/потребительские span), исключая исходящие вызовы к другим сервисам. Имена конечных точек также изменятся — теперь они будут включать метод HTTP.

Результаты:

* Метрики сосредоточены на реальной работоспособности сервиса, а не на совокупной активности системы.
* Количество конечных точек сокращается, а представление производительности сервисов улучшается.

Доступность:

* Новые окружения получают эти новые правила автоматически.
* Существующие окружения должны подключить функцию через Settings.

Для предварительного просмотра изменений перед подключением используйте дашборд, прикреплённый к сообщению [Dynatrace Community](https://dt-url.net/lv031sg).

Подробнее см. в разделе [Service Detection v2](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.").

Digital Experience | RUM Web

### Мониторинг AMP-приложений больше не поддерживается

Поддержка мониторинга приложений AMP (Accelerated Mobile Pages) прекращена. В результате AMP-приложения больше не доступны в окружениях.

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.321](/managed/whats-new/dynatrace-api/sprint-321 "Changelog for Dynatrace API version 1.321")
* [Журнал изменений Dynatrace API версии 1.322](/managed/whats-new/dynatrace-api/sprint-322 "Changelog for Dynatrace API version 1.322")

## Поддержка операционных систем

### Предстоящие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы перестанут поддерживаться с 01 June 2026

* Linux: Oracle Linux 9.6

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.6

  + x86-64
  + [Объявление поставщика](https://endoflife.date/rocky-linux)

##### Следующие операционные системы перестанут поддерживаться с 01 July 2026

* Linux: SUSE Enterprise Linux 15.3

  + x86-64
  + [Объявление поставщика](https://www.suse.com/lifecycle/)

##### Следующие операционные системы перестанут поддерживаться с 01 November 2026

* Linux: Red Hat Enterprise Linux 9.4, 9.7

  + x86-64
  + [Объявление поставщика](https://access.redhat.com/support/policy/updates/errata)
* Linux: Ubuntu 16.04

  + x86-64
  + [Объявление поставщика](https://ubuntu.com/about/release-cycle)

##### Следующие операционные системы перестанут поддерживаться с 01 January 2027

* Linux: Amazon Linux 2

  + x86-64
  + [Объявление поставщика](https://aws.amazon.com/linux/)

### Прошедшие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы больше не поддерживаются с 01 December 2025

* Linux: Red Hat Enterprise Linux 8.8, 9.2, 9.5

  + x86-64
  + [Объявление поставщика](https://access.redhat.com/support/policy/updates/errata)
* Linux: Oracle Linux 9.5

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.5

  + x86-64
  + [Объявление поставщика](https://endoflife.date/rocky-linux)

##### Следующие операционные системы больше не поддерживаются с 01 January 2026

* Linux: Debian 10

  + x86-64
  + [Объявление поставщика](https://wiki.debian.org/DebianReleases)

## Исправленные ошибки