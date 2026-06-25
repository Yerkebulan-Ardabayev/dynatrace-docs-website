---
title: Использование частного реестра
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry
scraped: 2026-05-12T12:06:16.974828
---

# Использование частного реестра

# Использование частного реестра

* Чтение: 5 мин
* Обновлено 27 января 2026 г.

Для пользователей, которым нужен больший контроль над средой размещения образов, Dynatrace предлагает возможность реплицировать образы и подписи в частные реестры.

Мы рекомендуем использовать частный реестр для оптимальной производительности и отсутствия рисков ограничения частоты запросов в условиях высокой нагрузки и динамичных сред. Кроме того, для соответствия стандартам безопасности и обеспечения целостности ПО при снижении рисков цепочки поставок можно применять сканирование образов и проверку подписей образов Dynatrace, что и рекомендуется.

Реплицируя образы Dynatrace в свой частный реестр, вы беспрепятственно сочетаете отличную производительность доставки с гарантией безопасных, подписанных и неизменяемых образов. Кроме того, мы предоставляем мультиархитектурные образы для обеспечения совместимости с различными платформами с поддержкой архитектур ЦП ARM64 (AArch64) и x86-64 на Linux.

На этой странице приведены инструкции по использованию подписанных и неизменяемых образов контейнеров Dynatrace, размещённых в частном реестре.

## Предварительные требования

Прежде чем начать, убедитесь, что выполнены следующие предварительные требования:

* Обязательно Версия Dynatrace Operator: v0.11 или новее
* Обязательно Целевые архитектуры ЦП: ARM64 (AArch64) и/или x86-64
* Обязательно Разрешите исходящий трафик к публичному реестру
* Обязательно Частный реестр с сохранёнными образами Dynatrace

Указания по хранению образов Dynatrace в частном реестре см. в разделе [Хранение образов Dynatrace в частных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Хранение образов Dynatrace в частных реестрах").

## Создание pull secret

Когда образы контейнеров Dynatrace предоставляются частным реестром, требующим аутентификации, pull secret **обязателен**, если не используется загрузка образов на узле и выполняется любое из следующих условий:

* DynaKube настроен для Full Observability (мониторинг [Cloud-Native Full-Stack](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание того, как работает развёртывание в Kubernetes."))
* DynaKube настроен для Application Observability (мониторинг [Application-Only](/managed/ingest-from/setup-on-k8s/how-it-works#auto "Подробное описание того, как работает развёртывание в Kubernetes.")) **с** включённым CSI driver

Начиная с Dynatrace Operator версии 0.14.0, поле `customPullSecret` обязательно, если не используется функция [загрузки образов на узле](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка загрузки образов на узле").

Pull secret (поле `customPullSecret` в конфигурации DynaKube) обычно используется для аутентификации в частном реестре и доступа к его артефактам (образам). В следующих пунктах подробнее описаны требования к pull secret:

* Когда настроен мониторинг Cloud-Native Full-Stack или Application-Only с CSI driver, CSI driver требует pull secret для доступа к частному реестру, так как он пытается напрямую загрузить образ Dynatrace Code Modules из частного реестра.
* При использовании [функции загрузки образов на узле](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка загрузки образов на узле") без CSI driver поле `customPullSecret` влияет только на компоненты, управляемые Dynatrace Operator (в пространстве имён `dynatrace`). Для внедряемых подов приложений необходимо вручную настроить pull secret на уровне узла, пространства имён или пода. Подробнее см. [предварительные требования для загрузки образов на узле](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Настройка загрузки образов на узле").

Чтобы создать pull secret, следуйте этой [документации Kubernetes](https://dt-url.net/p403yu6) о том, как создать секрет Kubernetes на основе существующих учётных данных или путём указания учётных данных в командной строке.

## Развёртывание Dynatrace Operator с образами из частного реестра

В этом разделе описано развёртывание Dynatrace Operator, образ контейнера которого берётся из частного реестра.

Dynatrace Operator состоит из нескольких компонентов (operator, webhook, CSI driver), каждый из которых использует один и тот же образ `dynatrace-operator` со специфичной конфигурацией развёртывания для каждого компонента.

Helm

Manifest

Следующая команда устанавливает Dynatrace Operator и настраивает загрузку образов контейнеров из частного реестра (например, "registry.my-company.com"), задавая значения `imageRef.repository`, `imageRef.tag` и `customPullSecret` (распространяется в `imagePullSecrets` спецификаций подов):

Если вы используете Helm версии 4.0+, необходимо указывать `--rollback-on-failure` вместо флага `--atomic`.

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "imageRef.repository=<your-private-registry>/dynatrace-operator" \



--set "imageRef.tag=<tag>" \



--set "customPullSecret=<secretName>" \



--create-namespace \



--namespace dynatrace \



--atomic \
```

Кроме того, уже существующую установку можно обновить следующим образом:

```
helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "imageRef.repository=<your-private-registry>/dynatrace-operator" \



--set "imageRef.tag=<tag>" \



--set "customPullSecret=<secretName>" \



--namespace dynatrace \



--reuse-values



--atomic \
```

Чтобы избежать утомительного и подверженного ошибкам редактирования больших YAML-файлов, мы рекомендуем использовать Helm для генерации манифестов через `helm template`.

Если же вы предпочитаете вносить изменения напрямую, обязательно скорректируйте поля `image` и `imagePullSecrets` во всех контейнерах и подах, где встречается образ `dynatrace-operator`.

## Настройка DynaKube на использование образов из частного реестра

Чтобы Dynatrace Operator использовал образы контейнеров из частного реестра, просто настройте pull secret через поле `customPullSecret` для аутентификации в реестре и соответствующие поля `image` в пользовательском ресурсе DynaKube. Настроенные образы будут развёрнуты в вашем кластере Kubernetes для настройки компонентов мониторинга.

Следующий фрагмент DynaKube демонстрирует, как настроить [Cloud-Native Full-Stack monitoring](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание того, как работает развёртывание в Kubernetes.") с использованием образов контейнеров Dynatrace из частного реестра.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



...



customPullSecret: <secretName>



oneAgent:



cloudNativeFullstack:



...



image: <your-private-registry>/dynatrace-oneagent:<tag>



codeModulesImage: <your-private-registry>/dynatrace-codemodules:<tag>



# version:         # no effect - see note below



...



activeGate:



...



image: <your-private-registry>/dynatrace-activegate:<tag>



...
```

Обратите внимание, что поле `version` не действует, если заданы поля `image` и/или `codeModulesImage`.

После настройки необходимых полей пользовательский ресурс DynaKube нужно применить к кластеру Kubernetes.

Дополнительные сведения о поле `customPullSecret`, полях `image` или пользовательском ресурсе DynaKube см. в примерах ниже или на справочной странице [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.").

Нужно больше примеров?

#### Application и Kubernetes Observability

Следующий фрагмент пользовательского ресурса описывает, как настроить DynaKube для [Application Observability и Kubernetes observability](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes") с образами контейнеров из вашего частного реестра:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



...



customPullSecret: <secretName>



oneAgent:



applicationMonitoring:



...



codeModulesImage: <your-private-registry>/dynatrace-codemodules:<tag>



# version:         # has no effect



...



activeGate:



...



image: <your-private-registry>/dynatrace-activegate:<tag>



...
```

## Проверка подписи образа

Все наши неизменяемые и подписанные образы контейнеров соответствуют лучшим практикам, повышая безопасность и защищая от атак на цепочку поставок. О том, как проверять подписи и гарантировать целостность ПО, см. [Проверка подписей образов Dynatrace](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Проверка подписей образов Dynatrace").

## Связанные темы

* [Хранение образов Dynatrace в частных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Хранение образов Dynatrace в частных реестрах")
* [Использование публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Использование публичного реестра")