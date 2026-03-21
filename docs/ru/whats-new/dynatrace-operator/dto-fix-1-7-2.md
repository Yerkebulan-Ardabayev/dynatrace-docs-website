---
title: Примечания к выпуску Dynatrace Operator версии 1.7.2
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-2
scraped: 2026-03-06T21:34:34.185741
---

* Latest Dynatrace
* Примечания к выпуску

Дата выпуска: 12 ноября 2025 г.

## Решённые проблемы

* Коллектор OpenTelemetry, используемый для [приёма телеметрии](../../ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest.md "Включите конечные точки приёма телеметрии Dynatrace в Kubernetes для локального приёма данных кластера."), теперь автоматически включает локальный URL-адрес сервиса ActiveGate в конфигурацию no-proxy, гарантируя, что соединения с локальным ActiveGate обходят любые настроенные прокси-серверы и исключая ненужные промежуточные соединения через прокси или связанные проблемы с подключением.

## Известные проблемы

Выявлены следующие известные проблемы с Dynatrace Operator версий 1.7.0–1.7.2. Сведения о других известных проблемах см. в разделе [Поддержка Dynatrace Operator и известные проблемы](../../ingest-from/technology-support/support-model-and-issues.md#well-known-issues "Сведения о поддержке Dynatrace для версий Kubernetes и Red Hat OpenShift, а также об известных проблемах").

* В результате оптимизации внедряемых монтирований (объединения их в `/var/lib/dynatrace`) компоненты Dynatrace больше не могут внедряться вместе с OneAgent.

* Классический полный стек и обогащение метаданными несовместимы и не могут использоваться для внедрения в одни и те же поды приложений.

## Уведомления об удалении и устаревании

* Устаревший Dynatrace OneAgent Operator удалён из каталога operatorhub.io. Используйте [Dynatrace Operator](../../ingest-from/setup-on-k8s/quickstart.md#deploy-dynatrace-operator "Развёртывание Dynatrace Operator на Kubernetes").

* Репозиторий Helm, расположенный в `dynatrace/helm-charts`, объявлен устаревшим и в будущем выпуске прекратит получать обновления. Если вы всё ещё используете его, обновите URL до `dynatrace/dynatrace-operator` или перейдите на подход на основе реестра OCI. Обновите URL репозитория Helm с помощью следующих команд:

  ```
  helm repo remove dynatrace


  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* Следующие версии API CustomResourceDefinition DynaKube удалены в Dynatrace Operator версии 1.7.0:

  + `v1beta1`
  + `v1beta2`
* Следующие версии API CustomResourceDefinition DynaKube отмечены как устаревшие и будут удалены в указанных версиях Dynatrace Operator:

  + `v1beta3` будет удалена в Dynatrace Operator версии 1.8

* Во избежание потенциальных сбоев настоятельно рекомендуется поддерживать актуальность версии API DynaKube. После объявления версии устаревшей и её удаления обновления могут значительно усложниться и потребовать срочного вмешательства.

  + Дополнительные сведения о процессе устаревания версий API DynaKube можно найти в [руководстве по миграции](../../ingest-from/setup-on-k8s/guides/migration/dynakube.md#deprecation "Мигрируйте ваш DynaKube CR на более новые apiVersions в зависимости от используемой версии Operator.").

* Поле DynaKube `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).autoUpdate` объявлено устаревшим и не должно использоваться. Этот флаг будет удалён в будущей версии Dynatrace Operator. Выполните одно из следующих действий:

  + Зафиксируйте версию OneAgent в вашем тенанте, чтобы управлять всеми подключёнными кластерами Kubernetes сразу.
  + Используйте поле `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).version`, чтобы зафиксировать версию для каждого DynaKube отдельно.

* Двоичные файлы CSI sidecar, расположенные в `/usr/local/bin/csi-node-driver-registrar` и `/usr/local/bin/livenessprobe`, объявлены устаревшими и будут удалены в будущей версии Dynatrace Operator.
* [Поддержка OpenShift 4.10 и 4.11](../../ingest-from/technology-support/support-model-and-issues.md "Сведения о поддержке Dynatrace для версий Kubernetes и Red Hat OpenShift, а также об известных проблемах") завершена в марте 2025 г. В результате Dynatrace Operator 1.7.0 больше не поддерживает эти версии.

## Обновление с Dynatrace Operator версии 1.6

В Dynatrace Operator версии 1.7 версии API DynaKube `v1beta1` и `v1beta2` больше не обслуживаются. Применение ресурсов DynaKube с использованием этих версий завершится ошибкой. Обновите манифесты DynaKube до `v1beta5` перед обновлением Dynatrace Operator. Дополнительные сведения см. в разделе [Руководство по миграции версий API DynaKube](../../ingest-from/setup-on-k8s/guides/migration/dynakube.md "Мигрируйте ваш DynaKube CR на более новые apiVersions в зависимости от используемой версии Operator.").
