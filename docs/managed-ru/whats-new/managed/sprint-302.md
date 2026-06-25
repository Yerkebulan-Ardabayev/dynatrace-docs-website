---
title: Заметки о выпуске Dynatrace Managed версии 1.302
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-302
scraped: 2026-05-12T11:07:57.374620
---

# Заметки о выпуске Dynatrace Managed версии 1.302

# Заметки о выпуске Dynatrace Managed версии 1.302

* Заметки о выпуске
* Updated on Dec 05, 2024

Начало развёртывания: Oct 14, 2024

## Новые функции и улучшения

### Premium HA: отказоустойчивость с несколькими центрами обработки данных

Новый механизм отказоустойчивости Premium High Availability (HA) с несколькими центрами обработки данных автоматически обнаруживает сбои узлов Elasticsearch или Cassandra. После восстановления работоспособности узлов автоматически запускается восстановление всех узлов, которые были недоступны в период сбоя.

Подробнее см. в разделе [managed-auto-repair](/managed/managed-cluster/high-availability/auto-repair).

### Улучшение производительности CPU Cassandra в некоторых развёртываниях

Скорректированы параметры настройки Cassandra для устранения высокой нагрузки на CPU Cassandra в некоторых развёртываниях Dynatrace Managed.

### Поддержка IPv6 для Network Availability Monitors

Digital Experience | Synthetic

ActiveGate версии 1.301+ Dynatrace версии 1.302+

NAM улучшен за счёт добавления поддержки IPv6. Теперь можно использовать NAM для проверки доступности сети и устройств в IPv6-сетях.

### Улучшена страница кластера Kubernetes

Infrastructure Observability | Kubernetes

На странице кластера Kubernetes теперь отображается версия продукта ActiveGate (вместо версии сборки), что обеспечивает согласованность со страницей **Deployment status**.

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.302](/managed/whats-new/dynatrace-api/sprint-302 "Changelog for Dynatrace API version 1.302")

## Поддержка операционных систем

* Добавлена поддержка [Red Hat Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.5
* Добавлена поддержка [Oracle Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.5
* Добавлена поддержка [Rocky Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 9.5

### Текущие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы перестанут поддерживаться с 01 November 2024

* Linux: Oracle Linux 9.0, 9.3

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
  + Последняя совместимая версия: 1.302
* Linux: Rocky Linux 9.0, 9.3

  + x86-64
  + [Объявление поставщика](https://endoflife.date/rocky-linux)
  + Последняя совместимая версия: 1.302

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

* [Общая доступность (версия сборки 1.302.76)](#managed-sprint-302-ga)
* [Обновление 102 (сборка 1.302.102)](#managed-sprint-302-102)

### Общая доступность (версия сборки 1.302.76)

Выпуск 1.302 GA содержит 12 исправленных ошибок.

| Компонент | Исправленные ошибки |
| --- | --- |
| [Cluster](#managed-sprint-302-ga-Cluster) | 10 |
| [Session Replay](#managed-sprint-302-ga-Session Replay) | 2 |

#### Cluster

* Улучшено преобразование агрегации в MDA для встроенных и вычисляемых метрик сервисов. (TI-14032)
* Исправлены проверки разрешений для извлечения сервисов. (TI-14133)
* Исправлены несоответствия аутентификации для триггеров событий в рабочих процессах при запуске с событиями, отличными от bizevents. Проверьте разрешения актора рабочего процесса, если вы замечаете изменения в поведении триггеров. (PPX-2982)
* Список блокировки исполняемых файлов Process Agent для Windows расширен: `"SEARCHINDEXER.EXE", "LSM.EXE", "WINLOGO.EXE", "SPOOLSV.EXE", "TASKHOST.EXE", "SPPSVC.EXE", "SEARCHFILTERHOST.EXE", "MMC.EXE", "MQSVC.EXE", "WMIPRVSE.EXE", "WININIT.EXE", "SERVICES.EXE", "EXPLORER.EXE", "SEARCHPROTOCOLHOST.EXE", "POWERSHELL.EXE", "SDIAGNHOST.EXE", "TASKHOSTW.EXE", "SIHOST.EXE", "TASKMGR.EXE"`. (OA-35354)
* Исправлена проблема, при которой политика IAM, запрещающая доступ на запись к группе схем `group:privacy-settings`, не позволяла создавать мобильные приложения RUM. (RUM-21513)
* Исправлена диаграмма пропускной способности для вызываемых/вызывающих сервисов на странице обзора сервиса. (TI-14156)
* Улучшена чувствительность прокрутки в представлении одиночной трассировки распределённых трасс. (TI-13794)
* Подсказка с IP-адресом клиента больше не отображается, если IP-адрес клиента недоступен. (TI-13978)
* В событиях Davis в Grail, вызванных обнаружением аномалий сервисов, `endpoint.name` теперь записывается в виде массива. (DI-16285)
* Исправлена отсутствующая конфигурация VictorOps в офлайн-кластерах. (CLD-12248)

#### Session Replay

* Добавлена минимальная высота для контейнера плеера, чтобы избежать слишком маленького отображения сессий. (SR-5941)
* Некоторые длинные разбитые сессии слишком долго загружались; для улучшения времени загрузки пропускаются операции, которые можно пропустить до начала воспроизведения. (SR-6017)

### Обновление 102 (сборка 1.302.102)

Это накопительное обновление содержит 1 исправленную ошибку и все ранее выпущенные обновления для выпуска 1.302.

#### Cluster

* Устранена проблема, вызванная новыми настройками по умолчанию в Firewalld в Red Hat Enterprise Linux 9.5, которые блокировали правила брандмауэра Dynatrace. (MGD-1220)