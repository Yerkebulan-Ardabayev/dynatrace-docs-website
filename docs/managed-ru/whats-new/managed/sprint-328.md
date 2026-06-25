---
title: Что нового в Dynatrace Managed версии 1.328
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-328
scraped: 2026-05-12T11:07:49.394800
---

# Что нового в Dynatrace Managed версии 1.328

# Что нового в Dynatrace Managed версии 1.328

* Заметки о выпуске
* Published Nov 20, 2025
* Rollout start on Dec 02, 2025

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.328. Содержимое:

* [Несовместимые изменения](#breakingchanges): 2
* [Исправления и обслуживание](#fixes): 1

## Несовместимые изменения

Application Observability

### Обеспечена согласованность данных в наблюдаемости Kubernetes

Во избежание несогласованных данных в наблюдаемости Kubernetes теперь отклоняются и модуль ОС OneAgent, и кодовые модули OneAgent, если модуль ОС устарел в конфигурации режима cloud-native full-stack. Затронутые рабочие нагрузки утратят наблюдаемость до синхронизации всех версий модулей.

**Требуемые действия:**

Обновите модуль ОС OneAgent до версии, не ниже последней версии любого кодового модуля, работающего на кластере Kubernetes.

Platform

### Добавлена подпись SAML HTTP-перенаправления

Добавлена поддержка подписи сообщений в SAML HTTP-Redirect binding.

* Если в `XML metadata of a SAML 2.0 Identity Provider` указан параметр `wantsAuthnRequestsSigned=true`, **AuthnRequest** теперь подписываются. Ранее этот параметр игнорировался.
* **LogoutRequest** и **LogoutResponse** теперь подписываются по умолчанию.

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.328](/managed/whats-new/dynatrace-api/sprint-328 "Changelog for Dynatrace API version 1.328")
* [Журнал изменений Dynatrace API версии 1.327](/managed/whats-new/dynatrace-api/sprint-327 "Changelog for Dynatrace API version 1.327")

## Исправления и обслуживание

### Исправленные ошибки в этом выпуске

* Отключён совместный доступ на основе политики IAM. (PAPA-29450)

### Исправленные ошибки (обновление 1.328.87.20251229-091620)

* Исправлена проблема с модулем проверки работоспособности NGINX, отвечающим за перенаправление трафика между узлами кластера. (MGD-9000)