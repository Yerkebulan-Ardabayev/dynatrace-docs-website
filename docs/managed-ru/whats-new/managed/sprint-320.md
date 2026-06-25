---
title: Заметки о выпуске Dynatrace Managed версии 1.320
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-320
scraped: 2026-05-12T11:07:52.048087
---

# Заметки о выпуске Dynatrace Managed версии 1.320

# Заметки о выпуске Dynatrace Managed версии 1.320

* Заметки о выпуске
* 10-min read
* Updated on Sep 18, 2025
* Rollout start on Aug 4, 2025

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.320.

## Объявления

Platform | Metrics

### Предстоящая нативная поддержка гистограмм OpenTelemetry и Prometheus

Начиная с версии кластера 1.324, Dynatrace вводит нативную поддержку гистограмм OpenTelemetry и Prometheus, включая автоматический расчёт процентилей. Это улучшение обеспечивает более быстрое выявление выбросов производительности и упрощает рабочие процессы наблюдаемости.

**Несовместимое изменение для существующих метрик гистограмм:**

* Существующие метрики гистограмм больше не будут обновляться, но останутся доступными для исторической визуализации на дашбордах, обеспечивая непрерывность и сохранность данных. Новые нативные метрики гистограмм будут представлены под отдельными ключами метрик с суффиксом `.histogram`.
* Если существующая метрика уже заканчивается на `.histogram` или `_histogram`, она больше не будет получать новые точки данных. Чтобы использовать новую функциональность гистограмм под тем же ключом метрики, необходимо удалить существующую метрику с помощью [Metrics API — DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API."). После удаления новая метрика гистограммы будет автоматически создана под тем же ключом.

В Dynatrace в окружении [**Local-Self-Monitoring**](/managed/managed-cluster/self-monitoring/local-self-monitoring "Learn how to use local self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.") можно использовать следующий запрос в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") для просмотра обработанных метрик гистограмм:

```
isfm:active_gate.metrics.ingest.explicit_bucket_histogram.layout.series
:splitBy(metric_key,"dt.tenant.uuid",data_source)
:sort(value(auto,descending))
:limit(100)
```

Для доступности этой метрики требуется установленная версия кластера 1.314+.

## Новые функции и улучшения

Platform | Deployment

### Массовая миграция OneAgents между Managed-окружениями

Упрощён процесс миграции нескольких OneAgents между окружениями, что обеспечивает централизованное управление и снижает объём ручной работы.

Функция поддерживает как рабочие процессы на основе веб-интерфейса, так и интеграцию через REST API, предлагая гибкость для ручных и автоматизированных операций.

Подробнее см. в разделах [Процедуры веб-интерфейса](/managed/ingest-from/bulk-configuration#web-ui-procedures "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") и [Процедуры API](/managed/ingest-from/bulk-configuration#api-procedures "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.").

Platform | Deployment

### Перенастройка IP-адреса узла кластера без полного повторного развёртывания

Администраторы теперь могут обновлять IP-адрес отдельных узлов кластера без полного повторного развёртывания. Это упрощает перенастройку сети и повышает гибкость в динамических инфраструктурных средах.

Подробнее см. в разделе [Перенастройка IP-адреса узла кластера](/managed/managed-cluster/operation/ip-reconfiguration "Learn how to reconfigure your node's IP address.").

Platform | Tags

### Определение правила, применившего тег к отслеживаемой сущности

Обновлены веб-интерфейс и Monitored entities API для предоставления информации о том, какое конкретное правило вызвало применение тега к отслеживаемой сущности.

В веб-интерфейсе можно выбрать тег для перехода непосредственно к правилу-источнику в интерфейсе Settings UI для [Automatically applied tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") или [Manually applied tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically."). Пример отображения в веб-интерфейсе:

![Пример отображения информации о тегировании в веб-интерфейсе](https://dt-cdn.net/images/screenshot-2025-07-31-at-15-23-13-914-d2778ef664.png)

Пример отображения информации о тегировании в веб-интерфейсе

[Monitored entities API v2](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") включает дополнительные поля `source` и `sourceSetting` в составе информации о теге. Поле `source` указывает, как был применён тег, а `sourceSetting` указывает связанный объект Settings. Можно использовать [Settings API](/managed/dynatrace-api/environment-api/settings/objects/get-object "View a settings object via the Dynatrace API.") для получения объекта (правила-источника).

**Пример ответа Monitored entities API v2**

```
{
"context": "CONTEXTLESS",
"key": "conditional-load-test",
"stringRepresentation": "conditional-load-test",
"source": "Auto tags",
"sourceSetting": "api/v2/settings/objects/...."
},
```

Platform | Data Explorer

### Алфавитно-цифровая сортировка измерений в селекторе метрик

В селекторе метрик доступен новый необязательный параметр для сортировки измерений. Значение по умолчанию — `lexical`, которое сортирует значения измерений в лексикографическом порядке; другой доступный вариант — `natural`, который обнаруживает цифры в измерении и сортирует по их числовому значению.

Подробнее см. в разделе [Metrics API — Metric selector: Sort transformation](/managed/dynatrace-api/environment-api/metric-v2/metric-selector#sort "Configure the metric selector for the Metric v2 API.").

Platform | Data Explorer

### Оптимизировано получение предложений по ключам метрик

Оптимизирована фильтрация предложений по ключам метрик в Data Explorer, поэтому предложения теперь появляются значительно быстрее при вводе текста. Это обеспечивает плавную работу даже при работе с большими наборами данных.

Platform | Davis

### Метаданные времени закрытия проблем теперь отображаются в классических деталях проблемы

Классическая страница деталей проблемы теперь показывает время закрытия проблемы в Dynatrace рядом с другими данными о времени жизни. Это позволяет быстро увидеть максимальное время, использованное для фильтров длительности профиля оповещения, когда проблема ещё находилась в открытом состоянии.

Digital Experience | Session Replay

### Добавлено расширение браузера Firefox для Session Replay

Для Session Replay добавлено расширение браузера Firefox. Ссылка на магазин Firefox теперь будет появляться при воспроизведении сессии, если расширение не установлено (аналогично Chrome и Edge).

Digital Experience | RUM Web

### Управление загрузкой и выполнением RUM JavaScript с помощью `defer` и `async`

Для уменьшения блокировки синтаксического анализа JavaScript теперь можно управлять загрузкой и выполнением кода мониторинга RUM с помощью атрибутов `async` или `defer`. Эти атрибуты можно применять к следующим форматам фрагментов:

* [JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case")
* [OneAgent JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case")
* [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case")

Platform

### Обновление сторонней функциональности веб-сервера Jetty до версии 12

В рамках данного выпуска встроенная функциональность веб-сервера Jetty обновляется до версии 12.0.22 в Dynatrace Server и ActiveGate.

Вмешательство пользователя или время простоя не требуются; обновление должно выполняться посредством поэтапного (rolling) обновления в рамках обычных обновлений версии.

Примечание: В определённых сценариях высокой нагрузки наблюдается незначительное увеличение использования CPU и памяти, вызванное изменениями реализации в Jetty 12. Если экземпляры ActiveGate испытывают острую нехватку ресурсов, рекомендуется незначительное их увеличение во избежание потенциальной перегрузки.

OneAgent

### Дополнительные варианты загрузки кодовых модулей через Deployment API

Вариант `multidistro` теперь можно комбинировать с архитектурой ARM при загрузке кодовых модулей через Deployment API.

Extensions

### Поддержка статуса Warning

Фреймворк Extensions 2.0 теперь понимает и может выдавать статусы `WARNING` и `PENDING`. Эти статусы добавлены к уже существующим `OK` и `ERROR`.

## Несовместимые изменения

Log Monitoring

### Приём логов через REST API строго проверяет размер полезной нагрузки запроса для сжатых данных

Приём логов через REST API теперь строго проверяет размер полезной нагрузки запроса для сжатых данных.

* Ранее некоторые запросы, содержавшие сжатые данные ниже лимита 10 МБ, при несжатом размере данных более 10 МБ принимались.
* Теперь такие запросы отклоняются с кодом HTTP-статуса 431. Независимо от того, сжаты данные или нет, размер полезной нагрузки должен быть ниже 10 МБ.

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.319](/managed/whats-new/dynatrace-api/sprint-319 "Changelog for Dynatrace API version 1.319")
* [Журнал изменений Dynatrace API версии 1.320](/managed/whats-new/dynatrace-api/sprint-320 "Changelog for Dynatrace API version 1.320")

## Поддержка операционных систем

* Добавлена поддержка [Red Hat Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.6
* Добавлена поддержка [Oracle Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.6
* Добавлена поддержка [Rocky Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.6

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