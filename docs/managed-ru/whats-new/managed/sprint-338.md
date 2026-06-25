---
title: Что нового в Dynatrace Managed 1.338
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-338
scraped: 2026-05-12T11:07:48.166241
---

# Что нового в Dynatrace Managed 1.338

# Что нового в Dynatrace Managed 1.338

* Заметки о выпуске
* 3-min read
* Published Apr 21, 2026
* Rollout start on May 11, 2026

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.338. Содержимое:

* [Обновления функций](#updates): 4
* [Несовместимые изменения](#breaking): 1
* [Исправления и обслуживание](#fixes): 10 (1 уязвимость)

Platform | Dashboards

## Новый тип диаграммы для метрик гистограмм

Dynatrace Managed теперь поддерживает специализированную диаграмму гистограмм в **Data Explorer** и **Dashboards** для визуализации метрик гистограмм.

С помощью этого нового типа диаграммы можно:

* Изучать распределение значений метрик, например времени ответа или размеров запросов.
* Определять распределения значений, процентили и выбросы с первого взгляда.

Это улучшение повышает наблюдаемость формы и разброса данных, дополняя существующие типы диаграмм, такие как линейные и столбчатые.

![Диаграмма гистограмм в Dashboards](https://dt-cdn.net/images/dashboard-1260-3a410212b9.png)

Диаграмма гистограмм в Dashboards

![Диаграмма гистограмм в Data Explorer](https://dt-cdn.net/images/data-explorer-1590-1be3bb1b48.png)

Диаграмма гистограмм в Data Explorer

## Обновления функций

Platform

### Обновление Cassandra до версии 4.1.11

В рамках этого выпуска узлы Cassandra обновляются до версии 4.1.11 для получения критических исправлений ошибок и уязвимостей безопасности.

Вмешательство пользователя или время простоя не требуются; обновление выполняется посредством поэтапного (rolling) обновления в рамках обычного обновления версии.

Platform

### Конвертация офлайн-кластеров Dynatrace Managed в онлайн

Теперь можно конвертировать существующий офлайн-кластер Dynatrace Managed в онлайн-кластер без повторного развёртывания. Ранее режим подключения выбирался при развёртывании и впоследствии не мог быть изменён. Теперь вместе с Dynatrace Managed поставляется скрипт конвертации, позволяющий администраторам изменять этот режим подключения.

Подробнее см. в разделе [Конвертация кластера Dynatrace Managed из офлайн в онлайн](/managed/managed-cluster/installation/cluster-offline-to-online "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.").

Platform

### Идентификатор отслеживаемой сущности теперь отображается в веб-интерфейсе

В веб-интерфейсе Dynatrace (например, на странице сведений о хосте, контейнере или сервисе) выберите **Properties and tags**, чтобы найти идентификатор отслеживаемой сущности в качестве первого свойства. Этот идентификатор полезен при запросе конкретной отслеживаемой сущности с помощью селектора сущностей.

![Идентификатор отслеживаемой сущности в разделе свойств](https://dt-cdn.net/images/properties-1722-c53cb871d1.png)

Идентификатор отслеживаемой сущности в разделе свойств

Platform | Settings

### Некоторые конечные пункты Configuration API объявлены устаревшими

Многие конечные пункты [Configuration API](/managed/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.") теперь охвачены [конечными пунктами Settings](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") в Environment API v2. Затронутые конечные пункты Configuration API теперь имеют уведомления об устаревании.

* Немедленных действий с вашей стороны не требуется.
* Затронутые конечные пункты остаются полностью активными.
* Хотя дата прекращения поддержки ещё не установлена, эти конечные пункты могут быть удалены в будущем выпуске.

Рекомендуется перейти на конечные пункты Environment API v2 для более надёжной интеграции. Ознакомьтесь со справочником Configuration API, чтобы определить затронутые конечные пункты, и запланируйте переход на Environment API v2.

## Несовместимые изменения

Digital Experience | Synthetic

### Параметр конфигурации удалён из схемы нового браузерного монитора и API

Параметр `performanceMetric` удалён из схемы `builtin:synthetic.browser.enablement` и из `EnablementDto` в [Environment API v2](/managed/dynatrace-api/environment-api "Find out what you need to use the environment section of the Dynatrace API.") для Synthetic Monitors. Этот параметр определял, какая метрика использовалась для отображения диаграмм производительности в веб-интерфейсе Dynatrace и проверки нарушений порогов производительности.

Оповещения о производительности продолжают использовать метрику `dt.synthetic.browser(.step).duration` без изменений в функциональности.

## Исправления и обслуживание

### Исправленные ошибки в этом выпуске

* **Уязвимость**: Обновлена сторонняя библиотека Jetty до версии 12.0.33 для получения критических исправлений ошибок и уязвимостей безопасности. Вмешательство пользователя или время простоя не требуются; обновление выполняется посредством поэтапного (rolling) обновления в рамках обычного обновления версии. (MGD-10719)
* Исправлена проблема, при которой конечный пункт **GET account audits** Account Management API возвращал ошибку `500` вместо `504` в случае тайм-аута. (LIMA-43865)
* Уведомления ServiceNow, завершившиеся с кодом HTTP-ошибки `429 Too Many Requests`, теперь повторяются до двух раз с интервалом 15 минут. Это снижает вероятность того, что проблемы останутся открытыми в ServiceNow, когда ServiceNow не может первоначально обработать уведомления. (DI-27261)
* Исправлена проблема, из-за которой локальное синтетическое воспроизведение показывало ошибки на страницах, инструментированных версией RUM JavaScript ниже 1.337. (DEM-25634)
* Улучшено определение целевого URL для вложенных действий загрузки. (DEM-24346)
* Исправлена некорректная ссылка на образ ActiveGate в сгенерированном шаблоне `synthetic.yaml` для OpenShift, которая указывала на несуществующий образ (`dynatrace/activegate:<version>`) вместо правильного (`dynatrace/dynatrace-activegate:<version>`). (DEM-24277)
* Исправлена проблема в **Mobile** > **Web request error details**, при которой фильтрация по `appVersion` возвращала ошибки `HTTP 400`. (DEM-23630)
* Исправлено поведение, при котором изменения размера страницы не учитывались при воспроизведении RUM-сессий через Session Replay (перемотка рендерера назад во времени). (DEM-21951)
* Исправлено форматирование идентификатора ActiveGate в данных, создаваемых расширениями Dynatrace. (DAQ-23179)
* Исправлена фильтрация раздела **Data Forwarding** на дашборде **OpenPipeline usage overview** по переменной дашборда **Configuration**. (PPX-10704)

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

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.338](/managed/whats-new/dynatrace-api/sprint-338 "Changelog for Dynatrace API version 1.338")
* [Журнал изменений Dynatrace API версии 1.337](/managed/whats-new/dynatrace-api/sprint-337 "Changelog for Dynatrace API version 1.337")