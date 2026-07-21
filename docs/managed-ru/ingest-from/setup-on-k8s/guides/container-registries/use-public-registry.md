---
title: Использование публичного реестра
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry
---

# Использование публичного реестра

# Использование публичного реестра

* 6 мин на чтение
* Обновлено 01 июля 2026

Чтобы учитывать разнообразные требования инфраструктуры и предпочтения организаций, образы Dynatrace доступны в отдельных публичных реестрах. Эти образы соответствуют лучшим практикам, обеспечивая неизменяемость и подписание для повышенной безопасности и устойчивости к потенциальным рискам цепочки поставок.

Изучи поддерживаемые публичные реестры с мультиархитектурными контейнерными образами Dynatrace, поддерживающими архитектуры CPU ARM64 (AArch64), x86-64, s390x и PPC64le на Linux, что обеспечивает совместимость с различными платформами.

На этой странице приведены инструкции по использованию подписанных и неизменяемых контейнерных образов Dynatrace, размещённых в поддерживаемых публичных реестрах.

Начни использовать эти защищённые образы уже сегодня для более безопасного и эффективного мониторинга в контейнерах:

* [Автоматическое разрешение образов из публичного реестра](#automatic-public-registry) для компонентов, управляемых Dynatrace Operator
* [Развёртывание Dynatrace Operator](#deploy-dynatrace-operator-with-images-from-public-registry) с контейнерными образами из публичного реестра
* [Настройка DynaKube](#configure-dynakube-to-use-images-from-public-registry) для использования контейнерных образов из публичного реестра для компонентов мониторинга

## Предварительные требования

Перед началом работы убедись, что выполнены следующие предварительные требования:

* Dynatrace SaaS версии 1.343+
* Dynatrace Operator версии 0.11+
* Целевые архитектуры CPU: ARM64 (AArch64), x86-64, s390x и/или ppc64le
* Разрешён исходящий (egress) трафик к публичному реестру

### Ограничения

Обрати внимание, что следующие конфигурации не поддерживаются в сочетании с публичными реестрами:

* Classic Full-Stack monitoring

## Поддерживаемые публичные реестры

Dynatrace публикует свои контейнерные образы в [Amazon ECR Public﻿](https://gallery.ecr.aws/dynatrace) и [Docker Hub﻿](https://hub.docker.com/u/dynatrace). При использовании [автоматического разрешения образов](#automatic-public-registry) укажи `spec.publicRegistryOverride` со значением `public.ecr.aws` для Amazon ECR Public или `registry-1.docker.io` для Docker Hub, чтобы запрашивать образы из конкретного реестра.

| Amazon ECR Public | Docker Hub |
| --- | --- |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-activegate | registry-1.docker.io/dynatrace/dynatrace-activegate |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-codemodules | registry-1.docker.io/dynatrace/dynatrace-codemodules |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-eec | registry-1.docker.io/dynatrace/dynatrace-eec |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-k8s-node-config-collector | registry-1.docker.io/dynatrace/dynatrace-k8s-node-config-collector |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-logmodule | registry-1.docker.io/dynatrace/dynatrace-logmodule |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-oneagent | registry-1.docker.io/dynatrace/dynatrace-oneagent |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-operator | registry-1.docker.io/dynatrace/dynatrace-operator |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-otel-collector | registry-1.docker.io/dynatrace/dynatrace-otel-collector |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-sql-extension-executor | registry-1.docker.io/dynatrace/dynatrace-sql-extension-executor |
| public.ecr.aws/registry-1.docker.io/dynatrace/edgeconnect | registry-1.docker.io/dynatrace/edgeconnect |

Ограничение скорости запросов

Учти, что при обращении к публичным реестрам существует потенциальный риск столкнуться с ограничением скорости запросов (rate limiting). Для более комфортной работы и снижения этого риска рекомендуется использовать приватный реестр.

Тегирование образов

Dynatrace использует тегирование образов на основе версий и **не** использует изменяемые теги образов, такие как `latest`. Дополнительную информацию о тегах можно найти в соответствующем репозитории публичного реестра.

## Автоматическое разрешение образов с Dynatrace Operator

Dynatrace Operator версии 1.10.0+

Dynatrace Operator может автоматически разрешать актуальные URI публичных образов для управляемых компонентов из среды Dynatrace без ручной настройки поля `image`.

Когда эта функция активна, Dynatrace Operator периодически синхронизирует ссылки на образы для каждого компонента из среды Dynatrace и применяет их автоматически.

### Включение автоматического разрешения образов

1. Удали поля `image` и `codeModulesImage` из DynaKube, если они заданы, их значения имеют приоритет над автоматически разрешёнными образами для соответствующего компонента.
2. Установи аннотацию `feature.dynatrace.com/use-public-registry` в DynaKube:

   ```
   apiVersion: dynatrace.com/v1beta6



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/use-public-registry: "true"



   spec:



   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



   ...
   ```

Включение автоматически с платформенным токеном

Когда DynaKube использует платформенный токен, Dynatrace Operator автоматически включает разрешение из публичного реестра. Аннотация не требуется. Можно установить `spec.publicRegistryOverride`, чтобы использовать конкретный поддерживаемый публичный реестр.

Переопределение хоста реестра

Чтобы запрашивать образы из конкретного поддерживаемого публичного реестра, установи `spec.publicRegistryOverride` в одно из значений хостов реестра, перечисленных в разделе [Поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Настройка Dynatrace Operator для использования образов публичного реестра для себя и своих управляемых компонентов. Это можно сделать вручную или через автоматическое разрешение из среды Dynatrace."), например, `public.ecr.aws` для Amazon ECR Public или `registry-1.docker.io` для Docker Hub. Dynatrace Operator передаёт хост в среду Dynatrace при разрешении URI образов.

### Что изменяется при включении функции

* **Образы компонентов**: Dynatrace Operator разрешает ссылки на образы из среды Dynatrace для OneAgent, ActiveGate и CodeModules. Компоненты без источника образа по умолчанию (Extension Execution Controller, Standalone Log Module, SQL Extension Executor) всегда требуют указания собственного образа в соответствующем поле `spec.templates`.
* **Перезапуск подов**: все поды управляемых компонентов перезапускаются при первом включении функции.
* **Внедрение в приложения**: образ init-контейнера, внедряемый в поды приложений, изменится при следующем перезапуске пода, если не используется CSI driver или если используется [загрузка образа на узел через эфемерный том](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Справка о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, загрузку образа через CSI driver и загрузку ZIP-архива."). В обоих случаях webhook переключается с режима загрузки ZIP-архива на режим самораспаковывающегося образа с использованием образа CodeModules.

### Проверка

После включения убедись, что Dynatrace Operator разрешает образы из публичного реестра:

```
kubectl get dynakube <dynakube-name> -n dynatrace -o jsonpath='{.status.activeGate.source}'
```

Значение `public-registry` подтверждает, что образ ActiveGate был разрешён из публичного реестра. Аналогично проверь `status.oneAgent.source` и `status.codeModules.source` для OneAgent и CodeModules.

## Развёртывание Dynatrace Operator с образами из публичного реестра

Чарт Helm для Dynatrace Operator доступен как OCI-артефакт как из Amazon ECR, так и из Docker Hub.
Независимо от того, из какого реестра загружается чарт, ссылки на контейнерные образы по умолчанию указывают на Amazon ECR. Если чарт устанавливается из Docker Hub и требуется, чтобы все образы также загружались из Docker Hub, можно использовать `--set imageRef.repository=docker.io/registry-1.docker.io/dynatrace/dynatrace-operator` с командой `helm install` или `helm upgrade`.

Dynatrace Operator состоит из нескольких компонентов (operator, webhook, CSI driver), все из которых используют один и тот же образ `dynatrace-operator` с определёнными конфигурациями развёртывания для каждого компонента.

Helm

Kustomize

Manifest

Если используется Helm версии 4.0+, необходимо использовать `--rollback-on-failure` вместо флага `--atomic`.

Следующая команда устанавливает Dynatrace Operator и настраивает загрузку контейнерных образов из публичного реестра:

```
helm install dynatrace-operator oci://public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-operator \



--create-namespace \



--namespace dynatrace \



--atomic
```

Альтернативно существующую установку можно обновить следующим образом:

```
helm upgrade dynatrace-operator oci://public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-operator \



--reset-then-reuse-values \



--atomic \



--namespace dynatrace
```

Используй следующую kustomization для удобной установки или обновления Dynatrace Operator путём применения необходимых манифестов.

```
apiVersion: kustomize.config.k8s.io/v1beta1



kind: Kustomization



namespace: Dynatrace



resources:



- namespace.yaml # can be created by `kubectl create namespace dynatrace --dry-run=client -oyaml > namespace.yaml`



- https://github.com/Dynatrace/dynatrace-operator/releases/download/<version>/kubernetes-csi.yaml
```

Чтобы избежать утомительного и подверженного ошибкам редактирования крупных файлов YAML, рекомендуется использовать Helm или Kustomize для управления манифестами.

Однако, если предпочтительно вносить изменения напрямую, убедись, что поле `image` скорректировано во всех контейнерах и подах, где встречается образ `dynatrace-operator`.

## Настройка DynaKube для использования образов из публичного реестра

**Classic Full-Stack** мониторинг не поддерживается в сочетании с публичным реестром.

Для архитектуры PPC64le требуется дополнительная настройка. Подробнее см. в разделе [ActiveGate container image](/managed/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "Deploy a containerized ActiveGate.").

Чтобы использовать образы из публичного реестра, нужно настроить соответствующие поля `image` в пользовательском ресурсе DynaKube. Dynatrace Operator затем развернёт настроенные образы в кластере Kubernetes для настройки компонентов мониторинга. Также Dynatrace Operator может [автоматически определять ссылки на публичные образы](#automatic-public-registry) из среды Dynatrace без ручной настройки.

Следующий фрагмент DynaKube показывает, как настроить [Cloud-Native Full-Stack monitoring setup](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "In-depth description on how the deployment on Kubernetes works."), используя публичный реестр Amazon ECR.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



...



oneAgent:



cloudNativeFullstack:



...



image: public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-oneagent:<tag>



codeModulesImage: public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-codemodules:<tag>



# version:         # has no effect - see note below



...



activeGate:



...



image: public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-activegate:<tag>



...
```

Обратите внимание: поле `version` не действует, если заданы поля `image` и/или `codeModulesImage`.

После настройки нужных полей пользовательский ресурс DynaKube нужно применить к кластеру Kubernetes.

Нужны ещё примеры?

#### Application и Kubernetes Observability с Amazon ECR

Следующий пользовательский ресурс показывает, как настроить DynaKube для [Application Observability и Kubernetes observability](/managed/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes"):

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



...



oneAgent:



applicationMonitoring:



...



codeModulesImage: public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-codemodules:<tag>



# version:         # has no effect



...



activeGate:



...



image: public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-activegate:<tag>



...
```

## Проверка подписи образа

Все неизменяемые и подписанные контейнерные образы соответствуют лучшим практикам, что повышает безопасность и защищает от атак на цепочку поставок. Чтобы узнать, как проверять подписи и гарантировать целостность программного обеспечения, см. [Verify Dynatrace image signatures](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures").

## Похожие темы

* [Use a private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")
* [Store Dynatrace images in private registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries")
* [DynaKube feature flags for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "List the feature flags to configure Dynatrace Operator on Kubernetes.")
* [Configure auto-update for Dynatrace Operator managed components](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator")