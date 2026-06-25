---
title: Заметки о выпуске Dynatrace Operator версии 1.5.1
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-5-1
scraped: 2026-05-12T12:31:27.299698
---

# Заметки о выпуске Dynatrace Operator версии 1.5.1

# Заметки о выпуске Dynatrace Operator версии 1.5.1

* Заметки о выпуске
* Updated on Nov 20, 2025

Дата выпуска: April 25, 2025

На этой странице представлен обзор исправлений, включённых в Dynatrace Operator версии 1.5.1. Подробную информацию о новых функциях и других улучшениях см. в [заметках о выпуске версии 1.5](/managed/whats-new/dynatrace-operator/dto-fix-1-5-0 "Release notes for Dynatrace Operator, version 1.5.0").

## Исправленные ошибки

* Исправлена проблема с механизмом обработки сертификатов webhook. Эта ошибка вызывала сбои сертификатов в webhook, что могло приводить к проблемам при развёртывании DynaKube.

## Известные ошибки

* Выявлены следующие проблемы с новой функцией [получения образов узлов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") в Dynatrace Operator версии 1.5:

  + Исправлено в Dynatrace Operator версии 1.6.0 и OneAgent версии 1.317+: при использовании функции в **режиме cloud-native full-stack без CSI-драйвера** может возникать некорректное обнаружение хостов, контейнеров и сервисов, а также неточное потребление лицензий.

  + Исправлено в Dynatrace Operator версии 1.6.0: использование функции совместно с обогащением метаданными и аннотациями `metadata.dynatrace.com/<key>: <value>` на внедрённых пространствах имён приведёт к панике в webhook Operator и помешает планированию внедрённых подов.

  + Исправлено в OneAgent версии 1.315+: при использовании функции совместно с аннотациями технологий для [оптимизации хранилища без CSI-драйвера](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#storage-optimization "Configure node image pull") может возникать аварийный цикл перезапуска или некорректная работа OneAgent во внедрённых подах.

  + Исправлено в OneAgent версии 1.313.45+: известна ошибка в OneAgent версий >= 1.313.0 и < 1.313.45. При обновлении до OneAgent версии 1.313 убедитесь, что используется версия 1.313.45+.

  При переходе с использования CSI-драйвера без `codeModulesImage` на использование с [получением образов узлов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") убедитесь, что файловая система CSI-драйвера не содержит кодового модуля для указанного DynaKube. Если это так, CSI-драйвер завершит работу с ошибкой и потребует ручного вмешательства для восстановления.

  Все остальные функции Dynatrace Operator v1.5 работают корректно.

* GKE Marketplace: из-за изменения процесса выпуска [бескилючевая верификация](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature#dynatrace-operator "Verify Dynatrace image signatures") не поддерживается для Dynatrace Operator версии 1.5.1.

## Обновление с Dynatrace Operator версии 1.4

* Версия DynaKube по умолчанию в Dynatrace Operator версии 1.5.0 — теперь `v1beta4`. Убедитесь, что ваш DynaKube обновлён для использования новых функций.

* Dynatrace Operator теперь автоматически генерирует сертификаты для защищённой связи между внутрикластерным ActiveGate и другими компонентами Dynatrace. Эта функция включена по умолчанию и требует ActiveGate версии 1.307.35 или выше. Чтобы использовать её, убедитесь, что ActiveGate обновлён до версии 1.307.35+. Если вы предпочитаете отключить эту функцию, установите флаг `feature.dynatrace.com/automatic-tls-certificate: false` в конфигурации DynaKube.