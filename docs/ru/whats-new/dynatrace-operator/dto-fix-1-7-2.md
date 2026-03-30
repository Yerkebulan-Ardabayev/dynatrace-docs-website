---
title: Примечания к выпуску Dynatrace Operator версии 1.7.2
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-2
scraped: 2026-03-06T21:34:34.185741
---

**Дата выпуска:** 12 ноября 2025

## Исправления

- OTel Collector теперь автоматически включает локальный URL ActiveGate в конфигурацию no-proxy, исключая ненужный проксированный трафик к локальному ActiveGate.

## Известные проблемы (1.7.0-1.7.2)

- Объединение монтирований в `/var/lib/dynatrace` — компоненты Dynatrace не могут внедряться вместе с OneAgent
- Classic full-stack и обогащение метаданными несовместимы в одних подах

## Устаревание

- Helm-репо `dynatrace/helm-charts` устарел — обновите на `dynatrace/dynatrace-operator`
- DynaKube API: `v1beta1`/`v1beta2` удалены; `v1beta3` будет удалена в 1.8
- Поле `.autoUpdate` устарело — используйте `.version` или закрепите версию на тенанте
- CSI sidecar бинарные файлы устарели
- OpenShift 4.10/4.11 больше не поддерживаются

## Обновление с версии 1.6

DynaKube API `v1beta1`/`v1beta2` не обслуживаются. Обновите манифесты до `v1beta5` перед обновлением.
