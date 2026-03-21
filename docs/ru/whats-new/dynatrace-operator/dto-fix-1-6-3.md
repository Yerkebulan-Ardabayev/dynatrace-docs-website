---
title: Примечания к выпуску Dynatrace Operator версии 1.6.3
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-6-3
scraped: 2026-03-06T21:34:29.094701
---

* Latest Dynatrace
* Release notes

Дата выпуска: 20 сентября 2025 г.

На этой странице представлен обзор исправлений, включённых в Dynatrace Operator версии 1.6.3. Подробную информацию о новых функциях и других улучшениях см. в [примечаниях к выпуску версии 1.6](dto-fix-1-6-0.md "Release notes for Dynatrace Operator, version 1.6.0").

## Устранённые проблемы

* Восстановлено событие `mark for termination`, которое ранее было удалено в [Dynatrace Operator версии 1.6.0](dto-fix-1-6-0.md#removal-and-deprecation-notices "Release notes for Dynatrace Operator, version 1.6.0"), для устранения [проблем](dto-fix-1-6-0.md#known-issues "Release notes for Dynatrace Operator, version 1.6.0") с надёжным обнаружением завершения работы узлов в средах с автоматическим масштабированием. Для использования этой функции у вашего API-токена должна быть область `DataExport`.

## Известные проблемы

В Dynatrace Operator версии 1.6.3 выявлены следующие известные проблемы.

При переключении с использования CSI-драйвера без `codeModulesImage` на его использование с [node image pull](../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull.md "Configure node image pull") убедитесь, что файловая система CSI-драйвера не содержит модуля кода для указанного DynaKube. Если такой модуль присутствует, CSI-драйвер завершится с ошибкой и потребует ручного вмешательства для восстановления.

## Обновление с Dynatrace Operator версии 1.5

Критических изменений нет.
