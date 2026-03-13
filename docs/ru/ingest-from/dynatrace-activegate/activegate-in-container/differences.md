---
title: Differences between containerized and host-based ActiveGates
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container/differences
scraped: 2026-03-05T21:37:14.955623
---

# Различия между контейнеризованными и хостовыми ActiveGate

# Различия между контейнеризованными и хостовыми ActiveGate

* Latest Dynatrace
* 1-min read
* Published Sep 01, 2023

ActiveGate, развёрнутый на хосте с помощью установщика, — в зависимости от выбранного [назначения](/docs/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") — состоит из нескольких процессов, предоставляющих различные функциональные возможности. Образ контейнера охватывает лишь подмножество из них, реализованное основным процессом ActiveGate.

## Назначения

Образ контейнера ActiveGate в настоящее время поддерживает только подмножество функций [маршрутизации и мониторинга](/docs/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Learn the capabilities and uses of ActiveGate."), а также [приватного синтетического мониторинга](/docs/ingest-from/dynatrace-activegate/capabilities#synthetic "Learn the capabilities and uses of ActiveGate.").

Для полного обзора см. [Назначения и функциональность ActiveGate](/docs/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.").

## Автоматическое обновление

[Автоматическое обновление ActiveGate](/docs/ingest-from/dynatrace-activegate/operation/update-activegate "Learn how to find out which version of ActiveGate you have installed and how you can download and install the latest version.") поддерживается только для хостовых ActiveGate, развёрнутых с помощью установщика.

В средах Kubernetes обновления ActiveGate управляются средой выполнения контейнеров.

ActiveGate обновляется автоматически при перезапуске пода при наличии новой версии, если в образе не указана конкретная версия.

## Удалённое управление конфигурацией

[Удалённое управление конфигурацией](/docs/ingest-from/bulk-configuration "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") не поддерживает контейнеризованные ActiveGate.

Конфигурация контейнеризованного ActiveGate не хранится постоянно. Она является декларативной и использует встроенные средства конфигурации Kubernetes, поэтому любые изменения, инициированные механизмом удалённого управления конфигурацией, будут утеряны при перезапуске контейнера.
