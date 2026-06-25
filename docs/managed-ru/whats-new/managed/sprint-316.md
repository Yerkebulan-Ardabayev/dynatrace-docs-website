---
title: Заметки о выпуске Dynatrace Managed версии 1.316
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-316
scraped: 2026-05-12T11:07:55.988528
---

# Заметки о выпуске Dynatrace Managed версии 1.316

# Заметки о выпуске Dynatrace Managed версии 1.316

* Заметки о выпуске
* Updated on Jul 04, 2025
* Rollout start on Jun 10, 2025

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.316.

## Новые функции и улучшения

Digital Experience | RUM Web

### Настройка префикса имени файла кода мониторинга RUM

Теперь можно задать пользовательский префикс для имени файла кода мониторинга RUM, что помогает предотвратить его блокировку блокировщиками рекламы.

Подробнее см. в разделе [Настройка источника кода Real User Monitoring](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source#configure-custom-monitoring-code-filename-prefix "Configure the Real User Monitoring code source for your specific requirements.").

Dynatrace Cluster

### Новое предупреждение при использовании нескольких операторов `:rollup` в селекторах метрик

Хотя ранее это было допустимо, использование нескольких операторов `:rollup` в одной цепочке преобразований может привести к нежелательному поведению.

Для предотвращения этого вводится новый механизм предупреждений, который обнаруживает применение нескольких операторов `:rollup` в одной цепочке преобразований. При обнаружении нескольких операторов `:rollup` система теперь выдаёт предупреждение, обеспечивая более чёткое понимание и более предсказуемые результаты.

Dynatrace Cluster

### Обновление сторонней функциональности веб-сервера Jetty

В рамках данного выпуска встроенная функциональность веб-сервера Jetty обновляется до версии 10.0.25 в Dynatrace Server и ActiveGate.

Вмешательство пользователя или время простоя не требуются; обновление должно выполняться посредством поэтапного (rolling) обновления в рамках обычных обновлений версии.

Dynatrace Cluster

### Улучшенная производительность Metrics API v2 для перечисления метрик

[Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") оптимизирован для перечисления всех доступных метрик. Теперь он требует значительно меньшего чтения данных для предоставления информации, и при частых вызовах ответ может возвращаться быстрее. Изменений в возвращаемой информации не ожидается.

## Несовместимые изменения

Dynatrace Cluster

### Исправлено отсутствие заголовков Content Security Policy (CSP) в процессе входа через SAML

Исправлена проблема с отсутствующими заголовками Content Security Policy (CSP) в процессе входа через SAML.

Однако если процесс входа включает перенаправления на URL-адреса, отличные от определённых в **XML metadata of a SAML 2.0 Identity Provider** (см. [Управление пользователями и группами с помощью SAML в Dynatrace Managed](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-saml "Learn how to connect your Dynatrace Server to a SAML server to import user groups or accounts that need access to your Dynatrace Managed environment.")), правило CSP `form-action` может быть нарушено, что приведёт к сбою входа.

Все дополнительные URL-адреса должны быть добавлены в соответствии с описанием в [Управление пользователями и группами с помощью SAML в Dynatrace Managed](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-saml "Learn how to connect your Dynatrace Server to a SAML server to import user groups or accounts that need access to your Dynatrace Managed environment.").

![Настройка атрибута группы пользователей для перенаправления SSO IdP.](https://dt-cdn.net/images/man-sso-idp-923-ff2e96b558.png)

Настройка атрибута группы пользователей для перенаправления SSO IdP.

Digital Experience | Synthetic

### Автовход браузерных мониторов объявлен устаревшим

Автовход в браузерных мониторах теперь является устаревшим:

* Браузерные мониторы с автовходом/аутентификацией через веб-форму больше нельзя сохранить через API v1 или веб-интерфейс.
* Аутентификация «Web form» больше недоступна при создании браузерного монитора или на странице **Advanced setup**.

Infrastructure Observability | Kubernetes

### Обнаружение аномалий: улучшенное оповещение «High CPU throttling»

Улучшено оповещение «High CPU throttling» за счёт изменения расчёта с throttling/usage на throttling/limits. Это улучшение обеспечивает более точные оповещения, особенно в сценариях с неактивными подами, снижая количество ложных срабатываний.

После этого обновления оповещение «High CPU throttling» предоставляет более надёжную и полезную информацию. Если пороговые значения для этого оповещения были настроены, рекомендуется пересмотреть их, чтобы убедиться в соответствии новому методу расчёта.

Dynatrace Cluster

### Назначение управленческих зон из контекста безопасности объявлено устаревшим

Назначение управленческих зон из контекста безопасности является устаревшим и будет удалено в Dynatrace Managed версии 1.322.

С этим изменением пункт меню **Settings** > **Preferences** > **Management zones** > **Security context settings** больше не будет доступен.

Используйте вместо этого [Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.").

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в [Журнале изменений Dynatrace API версии 1.316](/managed/whats-new/dynatrace-api/sprint-316 "Changelog for Dynatrace API version 1.316").

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