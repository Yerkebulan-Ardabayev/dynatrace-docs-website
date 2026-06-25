---
title: Заметки о выпуске Dynatrace Operator версии 1.4.0
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-4-0
scraped: 2026-05-12T12:31:17.659711
---

# Заметки о выпуске Dynatrace Operator версии 1.4.0

# Заметки о выпуске Dynatrace Operator версии 1.4.0

* Заметки о выпуске
* Published Dec 10, 2024

Дата выпуска: Dec 9, 2024

## Объявления

* [Kubernetes Security Posture Management (KSPM)](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") теперь доступен через Dynatrace Operator. Подробнее см. в разделе [Security Posture Management](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

* Dynatrace version 1.310+ OneAgent version 1.309+ Dynatrace Operator version 1.4.2+ Новый раздел `logMonitoring` в DynaKube обеспечивает простую настройку сбора логов для OneAgent и нового Log Module OneAgent. Раздел `logMonitoring` можно использовать совместно с любым режимом развёртывания: `cloudNativeFullStack` или `applicationMonitoring`.

* Доступно в будущей версии Dynatrace (CQ2/2025). Используйте расширения Dynatrace в Kubernetes для интеграции и мониторинга технологий с помощью Dynatrace. Изучайте и подключайте технологии, активируя расширения через Dynatrace Hub или соответствующие экраны в продукте. Настроив поле `extensions` в DynaKube, Dynatrace Operator будет развёртывать и управлять компонентами расширений, включая Dynatrace OpenTelemetry Collector и Extension Execution Controller, в вашей среде Kubernetes.

## Новые функции и улучшения

* В DynaKube версии `v1beta3` поле `useCSIDriver` удалено из раздела `spec`. Теперь Operator получает этот параметр из конфигурации развёртывания Dynatrace Operator. Существующие DynaKube продолжат работать, игнорируя данное поле.

* Init-контейнер переименован с `install-oneagent` на `dynatrace-operator` для отражения его расширенной функциональности и назначения.

* Использование ActiveGate API упрощено: теперь всегда создаются сервисы как для HTTP, так и для HTTPS портов.

* Экспериментальный флаг функции `feature.dynatrace.com/multiple-osagents-on-node` удалён.

* Если поле `image` для ActiveGate или OneAgent не указано, используются образы из встроенного реестра Dynatrace, которые поддерживают только архитектуру CPU x86-64. Соответственно, сходство узлов (node affinity) для ActiveGate и OneAgent по умолчанию задаётся как x86-64, если поле `image` не задано. Если требуется другая архитектура CPU или мультиарх-образы, обратитесь к документации по [публичному реестру](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Use a public registry").

* Поле `version` теперь влияет на версии, используемые для OneAgent и OneAgent Code Modules в режимах cloud-native full-stack и мониторинга приложений. Поля `image` имеют приоритет над полем `version`.

* Поле `apiUrl` DynaKube теперь является неизменяемым (immutable). Чтобы изменить его, удалите существующий DynaKube и создайте новый.

* Dynatrace придерживается принципа наименьших привилегий. Чтобы избежать предоставления излишних разрешений, Helm-чарт Dynatrace Operator позволяет настраивать разрешения Kubernetes RBAC через раздел `rbac` в файле значений Helm. Для управления ресурсами RBAC обратитесь к этому разделу в Helm-чарте.

## Исправленные ошибки

* Исправлена ошибка в проверке DynaKube, при которой поле версии OneAgent неправильно отклоняло стандартные строки версий (например, 1.200.0.20240501-085142).

* Исправлена проблема с полем `highAvailability` в Helm-чарте, из-за которой PodDisruptionBudget создавался для Webhook Dynatrace Operator даже при значении `highAvailability: false`.

* Исправлена проблема, при которой метки и аннотации пользовательского ресурса EdgeConnect не передавались в поды EdgeConnect.

* Исправлена проблема, при которой статус EdgeConnect в пользовательском ресурсе некорректно отражал состояние отказа пода.

## Уведомления об удалении и прекращении поддержки (deprecation)

* Событие «Mark for Termination» объявлено устаревшим и будет удалено в будущей версии Operator. Данная функциональность стала избыточной, так как заменена событиями доступности хоста при завершении работы и перезагрузке, появившимися в OneAgent версии 1.301.

* Helm-репозиторий по адресу `dynatrace/helm-charts` объявлен устаревшим и прекратит получать обновления в будущем выпуске. Если вы всё ещё используете его, обновите URL до `dynatrace/dynatrace-operator` или перейдите на подход на основе OCI-реестра. Обновите URL Helm-репозитория следующими командами:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* Поскольку Dynatrace OneAgent Operator достиг конца жизненного цикла 1 апреля 2023 года, мы прекращаем его поддержку в ряде маркетплейсов OLM: certified-operators, redhat-marketplace-operators, community-operators и community-operators-prod. Инструкции по миграции см. в статье [Migrating from OneAgent Operator to Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto "Detailed instructions how to migrate from deprecated OneAgent Operator to Dynatrace Operator using kubectl/oc").

## Обновление с Dynatrace Operator версии 1.3

* Манифесты: при установке Dynatrace Operator с помощью манифестов файл `kubernetes-csi.yaml` теперь включает все компоненты Operator, в том числе CSI-драйвер. Это делает использование `kubernetes.yaml` излишним — он **больше не должен применяться**. Ранее `kubernetes-csi.yaml` содержал только компонент CSI-драйвера. Последовательное применение обоих манифестов, как требовалось прежде, приведёт к ошибке. Webhook Dynatrace будет отклонять DynaKube, требующие CSI-драйвер (даже если CSI-драйвер корректно запущен).