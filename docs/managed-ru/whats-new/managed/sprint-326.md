---
title: Что нового в Dynatrace Managed версии 1.326
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-326
scraped: 2026-05-12T11:07:41.341201
---

# Что нового в Dynatrace Managed версии 1.326

# Что нового в Dynatrace Managed версии 1.326

* Заметки о выпуске
* Updated on Oct 20, 2025
* Rollout start on Oct 27, 2025

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.326. Содержимое:

* [Обновления функций](#updates): 2
* [Несовместимые изменения](#breaking): 2
* [Исправления и обслуживание](#fixes): 8

## Обновления функций

Platform | Davis

### Учёт праздников при корректировке базовых показателей

Государственные праздники существенно влияют на паттерны использования сервисов и приложений. Эти отклонения также влияют на точность базовых показателей сервисов и приложений. Для снижения риска ложных срабатываний оповещений определённые государственные праздники систематически исключаются из базовых показателей сервисов и приложений. Исключаемые праздники: Новый год, Пасха, День благодарения, Чёрная пятница и Рождество.

Этот параметр включён по умолчанию. Для отключения функции перейдите в **Settings** > **Anomaly Detection** > **Holiday-aware baseline modification**.

Classic licensing

### Отслеживание использования лицензии кластера через API

Теперь можно отслеживать использование лицензии для единиц хоста, единиц данных Davis (DDU) и единиц мониторинга цифрового опыта (DEM) в классическом лицензировании Dynatrace через [Cluster API v2 — Cluster license](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-license/get-cluster-license-usage "Use the API to get cluster license details and billed usage.").

Для Dynatrace Managed в **режиме онлайн**:

* `GET api/cluster/v2/clusterLicense` — получение лицензии кластера и тарифицируемого потребления
* `GET api/cluster/v2/clusterLicense/environment/total` — получение тарифицируемого потребления по окружениям, включая потребление из прошлых контрактов
* `POST api/cluster/v2/clusterLicense/key` — изменение ключа лицензии кластера

Для Dynatrace Managed в **режиме офлайн**:

* `GET api/cluster/v2/clusterLicense` — получение лицензии кластера и тарифицируемого потребления
* `POST api/cluster/v2/clusterLicense/upload` — загрузка ключа лицензии на кластер

## Несовместимые изменения

Application Observability | Services

### Автоматическая миграция span:services на SDv2

Устаревшие `span:services` (сервисы, принятые через OTLP API) будут автоматически мигрированы на тип Unified Services. Новый тип сервиса автоматически включает обнаружение аномалий Davis AI, обнаружение конечных точек и расширенные возможности мониторинга. Если ваше окружение уже мигрировало с `span:services` на Unified Services в 2023 году, это изменение вас не затронет.

### Упрощённый поиск в продукте

Встроенный поиск в продукте больше не включает документацию Dynatrace и материалы сообщества в результаты поиска. Вместо этого добавлена статическая ссылка на [search.dynatrace.com](https://search.dynatrace.com).

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.326](/managed/whats-new/dynatrace-api/sprint-326 "Changelog for Dynatrace API version 1.326")
* [Журнал изменений Dynatrace API версии 1.325](/managed/whats-new/dynatrace-api/sprint-325 "Changelog for Dynatrace API version 1.325")

## Исправления и обслуживание

Platform

### Обновление Cassandra до версии 4.1.10

В рамках этого выпуска узлы Cassandra обновляются до версии 4.1.10 для получения критических исправлений ошибок и уязвимостей безопасности.

Вмешательство пользователя или время простоя не требуются; обновление выполняется посредством поэтапного (rolling) обновления в рамках обычного обновления версии.

### Исправленные ошибки в этом выпуске

* Исправлена проблема с проверками ссылочной целостности между настройками, которая не позволяла сохранить изменения настроек, если значение содержало неизменённые секреты и ссылку на другую настройку. (PS-36658)
* Новый тип события Warning теперь можно задать в классическом шаблоне событий. (DI-23143)
* Исправлена проблема, при которой задача A связывалась с задачей B как дубликат, но задача B не содержала события из задачи A, что происходило, когда задача B достигала максимального лимита доказательств. (DI-23018)
* Исправлена проблема, появившаяся в Dynatrace версии 1.322, при которой уведомления о проблемах в текстовом формате (text/html/markdown) отображали начало и конец проблемы в UTC вместо часового пояса, настроенного для сервера Dynatrace. (DI-23006)
* Исправлены проблемы с отображением Session Replay, связанные с обработкой CSS @import (импорт другого CSS с сочетанием абсолютных и относительных путей). (DEM-15898)
* Исправлено руководство по развёртыванию: теперь предоставляется соответствующая версия новых выпусков OneAgent Lambda. (MGD-7064)
* Скорректирована логика обработки исключений так, чтобы PersistenceUnavailableException регистрировалось с уровнем INFO. (DI-22667)

Версия кластера (1.326.67.20251107-122142)

* Исправлена ошибка в хранилище отслеживаемых сущностей, которая могла приводить к пустым результатам запросов при превышении числа встроенных типов 2,5 миллиона во время воссоздания индекса атрибутов отслеживаемых сущностей. (MGD-8002)

## Поддержка операционных систем

* Добавлена поддержка [Red Hat Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 10.0
* Добавлена поддержка [SUSE Enterprise Linux](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.") 15.7

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