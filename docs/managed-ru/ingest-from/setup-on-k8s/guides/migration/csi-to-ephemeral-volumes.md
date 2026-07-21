---
title: Миграция с CSI-драйвера на эфемерные тома
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/csi-to-ephemeral-volumes
---

# Миграция с CSI-драйвера на эфемерные тома

# Миграция с CSI-драйвера на эфемерные тома

* Практическое руководство
* 5 минут на чтение
* Обновлено 25 июня 2026 г.

В этом руководстве описаны шаги, необходимые для миграции развёртывания Dynatrace Operator с CSI-томов на эфемерные тома. Используя значение параметра `csidriver.migrationMode` Helm, миграцию можно выполнить за один цикл перезапуска подов вместо двух, что снижает нарушение работы нагрузок.

## Режим миграции CSI

Когда режим миграции активен:

* DaemonSet CSI-драйвера продолжает работу контейнера-провизионера в режиме только очистки. Новые CSI-точки монтирования не создаются, а старые бинарники OneAgent в файловой системе узла удаляются автоматически.
* Dynatrace Operator и webhook немедленно переключаются на эфемерные тома для всех новых внедряемых подов.
* Поды CSI-драйвера продолжают работать, поэтому существующие поды с CSI-монтированием могут быть корректно размонтированы при их перезапуске.

## Предварительные требования

* Dynatrace Operator версии 1.10.0+
* Уже настроено внедрение на основе CSI (cloud-native full-stack или application monitoring с включённым CSI).
* Для установки Dynatrace Operator используется Helm. Для установок на основе манифестов сначала нужно выполнить [Миграцию с манифестов на Helm](/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-helm "Migrate from manifests to Helm for Dynatrace Operator installation.").
* Есть доступ к кластеру через CLI `kubectl`.

## Миграция на эфемерные тома

Если в DynaKube используется `codeModulesImage`, Operator автоматически переключается на [загрузку образа узла через эфемерный том](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") , шаги миграции не требуются. Для наилучшего опыта обновления нужно включить [автообновление из публичного реестра](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator") , чтобы Dynatrace Operator разрешал образы автоматически.

1. Включение режима миграции

Обновить Dynatrace Operator с включённым `csidriver.migrationMode`. Это позволяет DaemonSet CSI продолжать работу для размонтирования, при этом все новые внедрения подов переключаются на эфемерные тома.

```
helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--namespace dynatrace \



--reset-then-reuse-values \



--set csidriver.enabled=true \



--set csidriver.migrationMode=true \



--atomic
```

После этого обновления все новые внедряемые поды используют внедрение через эфемерные тома. Существующие поды продолжают использовать текущие CSI-монтирования до их перезапуска.

2. Перезапуск внедрённых нагрузок

Выполнить перезапуск всех нагрузок, которые в настоящее время используют внедрение на основе CSI. Это вызывает срабатывание webhook, который внедряет их с эфемерными томами вместо CSI-томов.

Пример перезапуска развёртываний

```
kubectl rollout restart deployment <deployment-name> -n <namespace>
```

Нужно перезапустить все внедрённые нагрузки.

3. Проверка отсутствия подов с CSI-томами

Нужно проверить, что ни один под всё ещё не использует CSI-тома Dynatrace. Для проверки оставшихся CSI-точек монтирования томов нужно выполнить следующую команду:

```
kubectl get pods --all-namespaces -o jsonpath='{range .items[?(@.spec.volumes[*].csi.driver=="csi.oneagent.dynatrace.com")]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
```

Пустой вывод означает, что все поды мигрированы. Если какие-то поды перечислены, нужно перезапустить нагрузку.

4. Отключение CSI-драйвера

Перед отключением CSI-драйвера нужно убедиться, что все нагрузки успешно мигрированы на эфемерные тома. Любые поды, которые всё ещё зависят от CSI-монтирований, перестанут работать после отключения CSI-драйвера. Нужно проверить результаты предыдущего шага проверки, прежде чем продолжить.

После подтверждения того, что CSI-томов не осталось, нужно отключить CSI-драйвер, чтобы удалить DaemonSet CSI и все связанные ресурсы.

```
helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--namespace dynatrace \



--reset-then-reuse-values \



--set csidriver.enabled=false \



--atomic
```

Это удаляет из кластера DaemonSet CSI, ServiceAccount, ресурсы RBAC и объект CSI-драйвера.