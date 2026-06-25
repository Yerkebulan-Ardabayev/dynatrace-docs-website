---
title: Заметки о выпуске Dynatrace Managed версии 1.312
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-312
scraped: 2026-05-12T11:07:59.887613
---

# Заметки о выпуске Dynatrace Managed версии 1.312

# Заметки о выпуске Dynatrace Managed версии 1.312

* Заметки о выпуске
* Updated on Apr 24, 2025

Начало развёртывания: Apr 14, 2025

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.312.

## Новые функции и улучшения

Обновление функции · Infrastructure Observability | Log monitoring

### Обновлённые лимиты приёма логов

* Log analytics: Улучшены характеристики приёма логов с повышенной поддержкой записей логов с большими размерами полезной нагрузки.
* Все настройки логов: Обновлены лимиты приёма логов для отражения новых порогов и возможностей.

Подробную информацию см. в разделе [Лимиты Log Monitoring по умолчанию (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-limits "Default limits for the latest version of Dynatrace Log Monitoring.").

Digital Experience | RUM Web

### Оценка общей отзывчивости веб-сайта с помощью Interaction to Next Paint

Interaction to Next Paint (INP) заменил First Input Delay (FID) в Core Web Vitals от Google. Dynatrace теперь предоставляет возможность мониторинга и анализа INP для отслеживаемых веб-сайтов. В то время как FID измерял отзывчивость первого взаимодействия на веб-сайте, INP позволяет оценивать задержку всех взаимодействий на веб-сайте в ходе посещения.

Можно добавить [метрику INP](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#web-applications "Explore the complete list of built-in Dynatrace metrics.") (`builtin:apps.web.interactionToNextPaint`) на дашборды с разбивкой по различным параметрам, таким как фронтенд-приложения, браузеры и локации.

Кроме того, можно оценивать значения INP через страницу **Frontend** и другие страницы анализа, а также фильтровать веб-сайты с наихудшими значениями INP для инициирования улучшений.

![Обзор фронтенд-приложения с Interaction to Next Paint](https://dt-cdn.net/images/screenshot-2025-04-07-at-14-44-27-1733-c8a57e770e.png)

Обзор фронтенд-приложения с Interaction to Next Paint

Application Security | Vulnerabilities

### Поддержка Go в Runtime Vulnerability Analytics и Runtime Application Protection

Технология Go теперь доступна для Runtime Vulnerability Analytics (обнаружение уязвимостей на уровне кода) и Runtime Application Protection (защита от атак).

* Для включения мониторинга Runtime Vulnerability Analytics уязвимостей на уровне кода Go:

  1. [Настройте элемент управления обнаружением уязвимостей на уровне кода для Go](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
  2. [Включите мониторинг OneAgent для Go](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* Для включения мониторинга Runtime Application Protection атак в технологии Go:

  1. [Настройте элемент управления атаками для Go](/managed/secure/application-security/application-protection#config "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")
  2. [Включите мониторинг OneAgent для Go](/managed/secure/application-security/application-protection#enable-oneagent-feature "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")

Необходимые действия:

Клиентам предварительного просмотра технологии Go необходимо обновить OneAgent до версии 1.311 для повторной активации этой функциональности. После этого дополнительная настройка не требуется.

Обновление функции · Logs

### Обновление предупреждений о приёме логов

В данном выпуске EEC, Log Analysis и ActiveGate начнут устанавливать значение `attr_key_trimmed` в атрибуте `dt.ingest.warnings` событий лога, содержащих хотя бы один ключ атрибута, превышающий лимит `100` байт в представлении UTF-8. Это задокументировано в:

* [Предупреждения о приёме логов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/lmc-troubleshooting/lmc-ingest-warnings "List of log ingestion warnings")

Digital Experience | RUM Web

### Целостность подресурсов для кода мониторинга RUM

Теперь можно использовать функцию браузера Subresource Integrity для обеспечения целостности кода мониторинга RUM, который автоматически внедряется или вручную вставляется в веб-приложение.

Подробнее см. в разделе [Использование Subresource Integrity (SRI) для кода Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring code.").

Digital Experience | Synthetic

### Дополнительная поддержка аутентификации Kerberos для браузерных мониторов

Negotiate (Kerberos) теперь поддерживается для браузерных мониторов, выполняемых в приватных локациях при:

* Версии кластера 1.312
* ActiveGate версии 1.311+ Linux
* ActiveGate версии 1.311+ Containerized

Digital Experience | Synthetic

### Добавлены лимиты эфемерного хранилища в шаблон контейнерной локации

Шаблон контейнерной Synthetic-локации теперь включает запросы и лимиты эфемерного хранилища для каждого контейнера.

Platform | Davis

### Поддержка разрешения dt.source\_entity в отчётах о событиях для классического режима свойств

`dt.source_entity` теперь можно перезаписывать на событиях для классических конфигураций, поддерживающих шаблон событий (например, события логов, метрические события). Также можно извлекать значение из другого свойства через `{property}`.

Cluster

### Обновление Cassandra до версии 4.1.8

В рамках данного выпуска узлы Cassandra обновляются до версии 4.1.8 для получения исправлений ошибок и уязвимостей безопасности.

Вмешательство пользователя или время простоя не требуются; обновление должно выполняться посредством поэтапного (rolling) обновления в рамках обычных обновлений версии.

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.311](/managed/whats-new/dynatrace-api/sprint-311 "Changelog for Dynatrace API version 1.311")
* [Журнал изменений Dynatrace API версии 1.312](/managed/whats-new/dynatrace-api/sprint-312 "Changelog for Dynatrace API version 1.312")

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

#### Cluster

* Исправлена ошибка, при которой некоторые регионы Индии отсутствовали на карте мира для арендаторов с указанной страной «Индия». (DEM-5641)
* Исправлена проблема, при которой в средах premium HA подключение к Elasticsearch инициализировалось с неправильными IP-адресами. (MGD-3242)
* Страница «Calculated service metrics»: неподдерживаемые единицы измерения больше не отображаются в списке выбора «Unit». (APPOBS-5161)
* Исправлена обработка недопустимых измерений Split, переданных через URL-адреса. (APPOBS-4744)
* Исправлена функция совместного доступа к представлению распределённых трасс. (APPOBS-5276)
* Исправлена проблема в Calculated Service Metrics API, допускавшая создание неподдерживаемой метрики «Capture full service call» (`CAPTURED_FULL_SERVICE_CALLS`). (APPOBS-5311)

#### Session Replay

* Исправлено пропускание неактивности для сессий с длительным периодом неактивности. (DEM-6209)