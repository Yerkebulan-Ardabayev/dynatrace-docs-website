---
title: Использование публичного реестра
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry
scraped: 2026-05-12T12:09:14.443467
---

# Использование публичного реестра

# Использование публичного реестра

* Чтение: 5 мин
* Обновлено 5 сентября 2025 г.

Чтобы удовлетворить разнообразные требования к инфраструктуре и организационные предпочтения, образы Dynatrace доступны в избранных публичных реестрах. Эти образы соответствуют лучшим практикам, обеспечивая неизменяемость и подписание для повышения безопасности и устойчивости к потенциальным рискам цепочки поставок.

Ознакомьтесь с поддерживаемыми нами публичными реестрами, где размещены мультиархитектурные образы контейнеров Dynatrace с поддержкой архитектур ЦП ARM64 (AArch64), x86-64, s390x и PPC64le на Linux, что обеспечивает совместимость с различными платформами.

На этой странице приведены инструкции по использованию подписанных и неизменяемых образов контейнеров Dynatrace, размещённых в поддерживаемых публичных реестрах.

## Предварительные требования

Прежде чем начать, убедитесь, что выполнены следующие предварительные требования:

* Обязательно Версия Dynatrace Operator: v0.11 или новее
* Обязательно Целевые архитектуры ЦП: ARM64 (AArch64), x86-64, s390x и/или ppc64le
* Обязательно Разрешите исходящий трафик к публичному реестру

#### Ограничения

Обратите внимание, что следующие конфигурации не поддерживаются в сочетании с публичными реестрами:

* Application monitoring без CSI-драйвера
* Host monitoring без CSI-драйвера
* Classic Full-Stack monitoring. В качестве альтернативы используйте частный реестр для [Classic Full-Stack monitoring](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry#classic-full-stack "Хранение образов Dynatrace в частных реестрах")

Начните использовать эти защищённые образы уже сегодня для более безопасного и эффективного мониторинга в контейнерах:

* [Разверните Dynatrace Operator](#deploy-dynatrace-operator-with-images-from-public-registry) с образами контейнеров из публичного реестра
* [Настройте DynaKube](#configure-dynakube-to-use-images-from-public-registry) на использование образов контейнеров из публичного реестра для компонентов мониторинга

## Поддерживаемые публичные реестры

Dynatrace публикует свои образы контейнеров в [Amazon ECR](https://gallery.ecr.aws/dynatrace) и [Docker Hub](https://hub.docker.com/u/dynatrace):

| Amazon ECR | Docker Hub |
| --- | --- |
| public.ecr.aws/dynatrace/dynatrace-activegate | dynatrace/dynatrace-activegate |
| public.ecr.aws/dynatrace/dynatrace-codemodules | dynatrace/dynatrace-codemodules |
| public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector | dynatrace/dynatrace-k8s-node-config-collector |
| public.ecr.aws/dynatrace/dynatrace-logmodule | dynatrace/dynatrace-logmodule |
| public.ecr.aws/dynatrace/dynatrace-oneagent | dynatrace/dynatrace-oneagent |
| public.ecr.aws/dynatrace/dynatrace-operator[1](#fn-1-1-def) | dynatrace/dynatrace-operator |
| public.ecr.aws/dynatrace/dynatrace-otel-collector | dynatrace/dynatrace-otel-collector |
| public.ecr.aws/dynatrace/edgeconnect | dynatrace/edgeconnect |

1

Доступно с версии Dynatrace Operator 1.0.0

Ограничение частоты запросов

Учтите, что при обращении к публичным реестрам существует потенциальный риск столкнуться с ограничением частоты запросов. Чтобы обеспечить более стабильную работу и снизить этот риск, мы рекомендуем использовать частный реестр или проходить аутентификацию в соответствующем реестре.

Тегирование образов

Dynatrace применяет тегирование образов на основе версий и **не** использует изменяемые теги образов, такие как `latest`. Дополнительные сведения о тегах см. в репозитории соответствующего публичного реестра.

## Развёртывание Dynatrace Operator с образами из публичного реестра

По умолчанию образ Dynatrace Operator `dynatrace/dynatrace-operator` предоставляется публичным реестром на AWS ECR.

Dynatrace Operator состоит из нескольких компонентов (operator, webhook, CSI driver), каждый из которых использует один и тот же образ `dynatrace-operator` со специфичной конфигурацией развёртывания для каждого компонента.

Helm

Kustomize

Manifest

Если вы используете Helm версии 4.0+, необходимо указывать `--rollback-on-failure` вместо флага `--atomic`.

Следующая команда устанавливает Dynatrace Operator и настраивает загрузку образов контейнеров из публичного реестра:

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--create-namespace \



--namespace dynatrace \



--atomic \
```

Кроме того, существующую установку можно обновить следующим образом:

```
helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--reuse-values \



--atomic \



--namespace dynatrace
```

Используйте следующую kustomization, чтобы удобно установить или обновить Dynatrace Operator, применив необходимые манифесты.

```
apiVersion: kustomize.config.k8s.io/v1beta1



kind: Kustomization



namespace: Dynatrace



resources:



- namespace.yaml # can be created by `kubectl create namespace dynatrace --dry-run=client -oyaml > namespace.yaml`



- https://github.com/Dynatrace/dynatrace-operator/releases/download/<version>/kubernetes-csi.yaml
```

Чтобы избежать утомительного и подверженного ошибкам редактирования больших YAML-файлов, мы рекомендуем использовать Helm или Kustomize для работы с манифестами.

Если же вы предпочитаете вносить изменения напрямую, обязательно скорректируйте поля `image` во всех контейнерах и подах, где встречается образ `dynatrace-operator`.

## Настройка DynaKube на использование образов из публичного реестра

Мониторинг **Classic Full-Stack** не поддерживается в сочетании с публичным реестром.

Для архитектуры PPC64le требуется дополнительная настройка. Подробнее см. [Образ контейнера ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "Развёртывание контейнеризированного ActiveGate.").

Dynatrace Operator можно легко настроить на использование образов из публичного реестра, задав соответствующие поля `image` в пользовательском ресурсе DynaKube. Настроенные образы будут развёрнуты в вашем кластере Kubernetes для настройки компонентов мониторинга.

Следующий фрагмент DynaKube демонстрирует, как настроить [Cloud-Native Full-Stack monitoring](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание того, как работает развёртывание в Kubernetes.") с использованием публичного реестра Amazon ECR.

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



image: public.ecr.aws/dynatrace/dynatrace-oneagent:<tag>



codeModulesImage: public.ecr.aws/dynatrace/dynatrace-codemodules:<tag>



# version:         # has no effect - see note below



...



activeGate:



...



image: public.ecr.aws/dynatrace/dynatrace-activegate:<tag>



...
```

Обратите внимание, что поле `version` не действует, если заданы поля `image` и/или `codeModulesImage`.

После настройки необходимых полей пользовательский ресурс DynaKube нужно применить к кластеру Kubernetes.

Нужно больше примеров?

#### Application and Kubernetes Observability с Amazon ECR

Следующий пользовательский ресурс описывает, как настроить DynaKube для [Application Observability и Kubernetes observability](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes"):

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



codeModulesImage: public.ecr.aws/dynatrace/dynatrace-codemodules:<tag>



# version:         # has no effect



...



activeGate:



...



image: public.ecr.aws/dynatrace/dynatrace-activegate:<tag>



...
```

## Проверка подписи образа

Все наши неизменяемые и подписанные образы контейнеров соответствуют лучшим практикам, повышая безопасность и защищая от атак на цепочку поставок. О том, как проверять подписи и гарантировать целостность ПО, см. [Проверка подписей образов Dynatrace](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Проверка подписей образов Dynatrace").

## Связанные темы

* [Использование частного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование частного реестра")
* [Хранение образов Dynatrace в частных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Хранение образов Dynatrace в частных реестрах")