---
title: Примечания к выпуску Dynatrace Operator версии 1.7.3
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-3
scraped: 2026-03-06T21:31:36.475717
---

# Примечания к выпуску Dynatrace Operator версии 1.7.3


* Latest Dynatrace
* Примечания к выпуску
* Обновлено 15 января 2026 г.

Дата выпуска: 19 января 2025 г.

## Исправленные проблемы

### Обработка удалённых версий API при обновлении Dynatrace Operator

Kubernetes записывает версии CRD в `.status.storedVersions`, но не удаляет записи при удалении версий, поэтому старые версии накапливаются и могут блокировать обновления.

В версиях Dynatrace Operator < 1.4 устаревшие `v1beta1` и `v1beta2` автоматически добавлялись в `.status.storedVersions` и никогда не очищались. Таким образом, любой кластер, на котором ранее работали версии до 1.4, затронут. Если эти версии останутся при будущем обновлении, установка CRD завершится ошибкой. В этом выпуске представлено двухэтапное решение для обеспечения плавного обновления:

1. Хук Helm для очистки CRD

   Во время обновления хук Helm запускает Job Kubernetes, который удаляет устаревшие версии API из поля `status.storedVersions` CRD DynaKube. Job сохраняет только последнюю версию API, доступную в версии Dynatrace Operator, установленной **до** обновления. Этот шаг обеспечивает плавное обновление CRD в процессе обновления Helm. См. раздел [Безопасность Dynatrace Operator](../../ingest-from/setup-on-k8s/reference/security.md#upgrade-support "На этой странице представлен обзор компонентов Dynatrace, их конфигураций по умолчанию и необходимых разрешений") для получения информации о необходимых разрешениях.
2. Миграция при запуске Dynatrace Operator

   **После** успешного обновления и ввода в эксплуатацию новой версии Dynatrace Operator 1.7.3 выполняется миграция всех существующих DynaKube на последнюю поддерживаемую версию API `v1beta5`. После миграции DynaKube поле `status.storedVersions` в CRD DynaKube обновляется, чтобы содержать только последнюю версию API `v1beta5` для обеспечения согласованности.

Важное замечание для кластеров, на которых ранее работал Dynatrace Operator версии < 1.4.0

* **Если вы использовали Dynatrace Operator версии <= 1.2, обновление до Dynatrace Operator версии 1.7.3 является обязательным промежуточным шагом перед обновлением до более поздних выпусков для обеспечения плавного и надёжного перехода.** Как общее правило, пропуск версий не рекомендуется.
* Установка на основе Helm

  При **использовании Helm** для установки или обновления с версии Dynatrace Operator >=1.3.0 дополнительных действий с вашей стороны не требуется. Необходимые корректировки будут автоматически выполнены хуком предварительного обновления Helm в процессе обновления.
* Альтернативные методы установки

  **Если вы используете один из альтернативных методов развёртывания, перечисленных ниже, обновление до Dynatrace Operator версии 1.7.3 является обязательным промежуточным шагом перед обновлением до более поздних выпусков для обеспечения плавного и надёжного перехода.**

  + Red Hat OpenShift OperatorHub
  + OperatorHub.io
  + Google Marketplace
  + Манифесты Kubernetes
* Ручной подход

  Вместо обновления до версии 1.7.3 вы можете вручную выполнить необходимые корректировки CRD:

  1. Выполните следующую команду для просмотра сохранённых версий в CRD вашего кластера.

     ```
     kubectl -n dynatrace get crd dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
     ```
  2. Продолжите процедуру, если `v1beta1` или `v1beta2` перечислены в сохранённых версиях CRD вашего кластера.
  3. Определите текущую активную версию:

     ```
     storage_version=$(kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}')
     ```
  4. Преобразуйте все DynaKube в активную версию:

     ```
     kubectl get dynakube -n dynatrace -o yaml | kubectl apply -f -
     ```
  5. Удалите все предыдущие версии, сохранив активную версию:

     ```
     kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource='status' --type='merge' -p "{\"status\":{\"storedVersions\":[\"${storage_version}\"]}}"
     ```

Обеспечение надлежащей очистки поля `.status.storedVersions` CRD крайне важно для предотвращения проблем при будущих обновлениях.

ArgoCD может отображать ресурсы, всё ещё использующие старую версию API, как "out-of-sync" (не синхронизированные).

## Известные проблемы

Мы выявили следующие известные проблемы с Dynatrace Operator версий 1.7.0--1.7.3. Другие известные проблемы см. в разделе [Поддержка и известные проблемы Dynatrace Operator](../../ingest-from/technology-support/support-model-and-issues.md#well-known-issues "Поддержка Dynatrace для версий Kubernetes и Red Hat OpenShift и известные проблемы").

* Из-за оптимизации внедряемых монтирований (объединение их в `/var/lib/dynatrace`) компоненты Dynatrace больше не могут быть внедрены с помощью OneAgent.

* Классический полный стек и обогащение метаданных несовместимы и не могут использоваться для внедрения в одни и те же поды приложений.

## Уведомления об удалении и устаревании

* Устаревший Dynatrace OneAgent Operator удалён из каталога operatorhub.io. Пожалуйста, используйте наш [Dynatrace Operator](../../ingest-from/setup-on-k8s/quickstart.md#deploy-dynatrace-operator "Развертывание Dynatrace Operator в Kubernetes").

* Репозиторий Helm, расположенный по адресу `dynatrace/helm-charts`, устарел и перестанет получать обновления в будущем выпуске! Если вы всё ещё его используете,
  пожалуйста, обновите URL на `dynatrace/dynatrace-operator` или переключитесь на подход, основанный на OCI-реестре. Обновите URL репозитория Helm с помощью следующих команд:

  ```
  helm repo remove dynatrace


  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* Следующие версии API CustomResourceDefinition DynaKube были удалены в Dynatrace Operator версии 1.7.0:

  + `v1beta1`
  + `v1beta2`
* Следующие версии API CustomResourceDefinition DynaKube отмечены как устаревшие и будут удалены в указанных версиях Dynatrace Operator:

  + `v1beta3` будет удалена в Dynatrace Operator версии 1.8

* Для предотвращения возможных нарушений мы настоятельно рекомендуем поддерживать версию API DynaKube в актуальном состоянии. После того как версия устарела и удалена, обновления могут стать значительно более сложными и критичными по времени.

  + Дополнительная информация о процессе устаревания версий API DynaKube доступна в [руководстве по миграции](../../ingest-from/setup-on-k8s/guides/migration/dynakube.md#deprecation "Перенесите ваш DynaKube CR на более новые версии apiVersion в зависимости от используемой версии Operator.").

* Поле DynaKube `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).autoUpdate` устарело и больше не должно использоваться. Флаг будет удалён в будущей версии Dynatrace Operator. Выполните одно из следующих действий:

  + Закрепите версию OneAgent на вашем тенанте для одновременного управления всеми подключёнными кластерами Kubernetes.
  + Используйте поле `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).version` для закрепления версии для каждого DynaKube отдельно.

* Бинарные файлы CSI sidecar, расположенные в `/usr/local/bin/csi-node-driver-registrar` и `/usr/local/bin/livenessprobe`, теперь устарели и будут удалены в будущей версии Dynatrace Operator.
* [Поддержка OpenShift 4.10 и 4.11](../../ingest-from/technology-support/support-model-and-issues.md "Поддержка Dynatrace для версий Kubernetes и Red Hat OpenShift и известные проблемы") завершилась в марте 2025 г. В результате Dynatrace Operator 1.7.0 больше не будет поддерживать эти версии.

## Обновление с Dynatrace Operator версии 1.6

В Dynatrace Operator версии 1.7 версии API DynaKube `v1beta1` и `v1beta2` больше не обслуживаются. Применение ресурсов DynaKube с использованием этих версий завершится ошибкой. Обновите ваши манифесты DynaKube до `v1beta5` перед обновлением Dynatrace Operator. Подробнее см. [Руководство по миграции версий API DynaKube](../../ingest-from/setup-on-k8s/guides/migration/dynakube.md "Перенесите ваш DynaKube CR на более новые версии apiVersion в зависимости от используемой версии Operator.").
