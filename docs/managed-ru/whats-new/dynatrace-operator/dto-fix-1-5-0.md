---
title: Заметки о выпуске Dynatrace Operator версии 1.5.0
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-5-0
scraped: 2026-05-12T12:34:43.716211
---

# Заметки о выпуске Dynatrace Operator версии 1.5.0

# Заметки о выпуске Dynatrace Operator версии 1.5.0

* Заметки о выпуске
* Published Apr 01, 2025

Дата выпуска: April 24, 2025

Важное уведомление

Если вы используете Dynatrace Operator версии 1.5.0, рекомендуется обновиться до версии 1.5.1 для получения последних важных исправлений.

## Предстоящие изменения

### Изменение имён измерений Kubernetes

Имена измерений Kubernetes (`dt.kubernetes.cluster.id`, `dt.kubernetes.workload.kind`, `dt.kubernetes.workload.name`) станут недоступны начиная с Dynatrace Operator версии 1.8.0.

Если вы всё ещё используете их, как можно скорее обновите конфигурации, запросы и другие ссылки, заменив их на новые имена.

| Устаревшее имя | Новое имя |
| --- | --- |
| `dt.kubernetes.cluster.id` | `k8s.cluster.uid` |
| `dt.kubernetes.workload.kind` | `k8s.workload.kind` |
| `dt.kubernetes.workload.name` | `k8s.workload.name` |

## Новые функции и улучшения

* Новая функция получения образов узлов (node image pull) вводит расширенные возможности получения образов, повышает производительность, безопасность и гибкость в Dynatrace Operator. Подробнее о функции см. в руководстве по настройке [получения образов узлов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull").

* Для `cloudNativeFullStack` и `hostMonitoring`: OneAgent (модуль хоста) больше не зависит от CSI-драйвера. Если CSI-драйвер не развёрнут, вместо него используется том `hostPath`. Путь по умолчанию (`/var/opt/dynatrace`) можно переопределить через поле `storageHostPath`.

* Теперь можно добавить PersistentVolumeClaim (PVC) к контейнеризированному ActiveGate, чтобы избежать потери данных при непредвиденных перезапусках. Рекомендуется добавить PVC при использовании [`log_analytics_collector`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "Learn which ActiveGate properties you can configure based on your needs and requirements."). Узнайте, как настроить PVC, в [руководстве](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "Set up a persistent storage for containerized ActiveGate to be used as temporary storage for ingested data.") и защитите данные логов от потери.

* [Live Debugger](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") теперь можно включить, добавив `debugging` в [`.spec.activeGate.capabilities`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#active-gate "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

* [Модуль логов OneAgent](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") и CSI-драйвер теперь поддерживаются на GKE Autopilot.

## Исправленные ошибки

* Модуль логов не мог получить метаданные из Kubernetes API. Проблема решена путём предоставления токена сервисного аккаунта с соответствующими разрешениями поду OneAgent.

* Теперь токены тенанта можно вручную ротировать с помощью [Dynatrace API](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Rotate Dynatrace tenant tokens."). Процесс упрощён: перезапуск ActiveGate и OneAgent для использования нового токена теперь выполняется автоматически, что исключает необходимость ручного перезапуска.

* Исправлена проблема, при которой посторонние логи Operator случайно включались в бинарный zip-вывод при создании архива поддержки, что приводило к повреждению zip-файла на не-Linux-системах.

* Передача пользовательских аргументов в OneAgent ([.spec.oneagent.\*.args](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#one-agent "List the available parameters for setting up Dynatrace Operator on Kubernetes.")) могла приводить к дублированию. Во избежание непредвиденных побочных эффектов дубликаты теперь исключаются, кроме аргументов `--set-host-property` и `--set-host-tag`.

  *Примечание:* Указывать `--set-host-tag` несколько раз с одинаковым значением тега не допускается. Такая конфигурация DynaKube будет отклонена.

* Свойства хоста обычно передаются в OneAgent в формате пар `key=value` с помощью аргументов `--set-host-property`. Исправлена ошибка, из-за которой конфигурации DynaKube отклонялись; теперь необходимые свойства хоста задаются успешно.

* Переключатель `.debug` в Helm теперь принимает строковые значения, которые корректно интерпретируются.

* Монтирование каталога хоста `/var/logs` теперь доступно только для чтения, что обеспечивает доступ к логам journald и kubelet.

## Уведомления об удалении и прекращении поддержки (deprecation)

* Событие «Mark for Termination» объявлено устаревшим и будет удалено в будущей версии Operator. Данная функциональность стала избыточной, так как заменена событиями доступности хоста при завершении работы и перезагрузке, появившимися в OneAgent версии 1.301.

* Helm-репозиторий по адресу `dynatrace/helm-charts` объявлен устаревшим и прекратит получать обновления в будущем выпуске. Если вы всё ещё используете его, обновите URL до `dynatrace/dynatrace-operator` или перейдите на подход на основе OCI-реестра. Обновите URL Helm-репозитория следующими командами:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

## Обновление с Dynatrace Operator версии 1.4

* Версия DynaKube по умолчанию в Dynatrace Operator версии 1.5.0 — теперь `v1beta4`. Убедитесь, что ваш DynaKube обновлён для использования новых функций.

* Dynatrace Operator теперь автоматически генерирует сертификаты для защищённой связи между внутрикластерным ActiveGate и другими компонентами Dynatrace. Эта функция включена по умолчанию и требует ActiveGate версии 1.307.35 или выше. Чтобы использовать её, убедитесь, что ActiveGate обновлён до версии 1.307.35+. Если вы предпочитаете отключить эту функцию, установите флаг `feature.dynatrace.com/automatic-tls-certificate: false` в конфигурации DynaKube.