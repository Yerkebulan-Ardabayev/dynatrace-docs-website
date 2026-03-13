---
title: Dynatrace Operator release notes version 1.7.1
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-1
scraped: 2026-03-05T21:39:34.642707
---

# Примечания к выпуску Dynatrace Operator версии 1.7.1

# Примечания к выпуску Dynatrace Operator версии 1.7.1

* Latest Dynatrace
* Release notes
* Updated on Jan 22, 2026

Дата выпуска: 20 сентября 2025 г.

На этой странице представлен обзор исправлений, включённых в Dynatrace Operator версии 1.7.1. Подробную информацию о новых функциях и других улучшениях см. в [примечаниях к выпуску версии 1.7](/docs/whats-new/dynatrace-operator/dto-fix-1-7-0 "Release notes for Dynatrace Operator, version 1.7.0").

## Решённые проблемы

* Повторно введено событие `mark for termination`, которое было ранее удалено в [Dynatrace Operator версии 1.6.0](/docs/whats-new/dynatrace-operator/dto-fix-1-6-0#removal-and-deprecation-notices "Release notes for Dynatrace Operator, version 1.6.0"), для устранения [проблем](/docs/whats-new/dynatrace-operator/dto-fix-1-7-0#known-issues "Release notes for Dynatrace Operator, version 1.7.0"), связанных с надёжным обнаружением завершения работы узлов в конфигурациях с автоматическим масштабированием. Для этой функции необходимо, чтобы ваш токен API имел область `DataExport`.

## Известные проблемы

Нами выявлены следующие известные проблемы в Dynatrace Operator версий 1.7.0–1.7.2. Другие известные проблемы см. в разделе [Поддержка и известные проблемы Dynatrace Operator](/docs/ingest-from/technology-support/support-model-and-issues#well-known-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

* Вследствие оптимизации внедряемых монтирований (объединения их в `/var/lib/dynatrace`) компоненты Dynatrace больше не могут быть внедрены совместно с OneAgent.

* Classic full-stack и обогащение метаданными несовместимы и не могут использоваться для внедрения в одни и те же поды приложений.

## Уведомления об удалении и устаревании

* Устаревший Dynatrace OneAgent Operator был удалён из каталога operatorhub.io. Пожалуйста, используйте вместо него [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/quickstart#deploy-dynatrace-operator "Deploy Dynatrace Operator on Kubernetes").

* Репозиторий Helm, расположенный в `dynatrace/helm-charts`, устарел и в будущем выпуске перестанет получать обновления! Если вы всё ещё используете его,
  пожалуйста, обновите URL на `dynatrace/dynatrace-operator` или перейдите на подход на основе реестра OCI. Обновите URL репозитория Helm с помощью следующих команд:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* Следующие версии API определения пользовательского ресурса DynaKube были удалены в Dynatrace Operator версии v1.7:

  + `v1beta1`
  + `v1beta2`
* Следующие версии API определения пользовательского ресурса DynaKube отмечены как устаревшие и будут удалены в указанных версиях Dynatrace Operator:

  + `v1beta3` будет удалена в Dynatrace Operator версии 1.8

* Во избежание возможных сбоев мы настоятельно рекомендуем поддерживать актуальную версию API DynaKube. После того как версия будет объявлена устаревшей и удалена, обновления могут стать значительно более сложными и срочными.

  + Дополнительную информацию о процессе устаревания версий API DynaKube можно найти в [руководстве по миграции](/docs/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").

* Поле DynaKube `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).autoUpdate` устарело и больше не должно использоваться. В будущей версии Dynatrace Operator этот флаг будет удалён. Выполните одно из следующих действий:

  + Зафиксируйте версию OneAgent на вашем тенанте, чтобы управлять всеми подключёнными кластерами Kubernetes одновременно.
  + Используйте поле `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).version` для фиксации версии на уровне каждого DynaKube.

* Бинарные файлы CSI sidecar, расположенные в `/usr/local/bin/csi-node-driver-registrar` и `/usr/local/bin/livenessprobe`, теперь устарели и будут удалены в будущей версии Dynatrace Operator.
* [Поддержка OpenShift 4.10 и 4.11](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") завершилась в марте 2025 года. В связи с этим Dynatrace Operator 1.7 больше не поддерживает эти версии.

## Обновление с Dynatrace Operator версии 1.6

В Dynatrace Operator версии 1.7 версии API DynaKube `v1beta1` и `v1beta2` больше не обслуживаются. Применение ресурсов DynaKube с использованием этих версий завершится ошибкой. Перед обновлением Dynatrace Operator обновите манифесты DynaKube до `v1beta5`. Дополнительную информацию см. в [руководстве по миграции версий API DynaKube](/docs/ingest-from/setup-on-k8s/guides/migration/dynakube "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.").
