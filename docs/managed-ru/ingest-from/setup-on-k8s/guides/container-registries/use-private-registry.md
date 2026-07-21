---
title: Использование частного реестра
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry
---

# Использование частного реестра

# Использование частного реестра

* 5 минут на чтение
* Обновлено 10 июля 2026 г.

Для пользователей, которым нужен больший контроль над средой хостинга образов, Dynatrace предлагает возможность репликации образов и подписей в частные реестры.

Использование частного реестра рекомендуется для оптимальной производительности и отсутствия рисков ограничения частоты запросов в средах с высокой нагрузкой и динамичной инфраструктурой. Кроме того, для соответствия стандартам безопасности и обеспечения целостности программного обеспечения при снижении рисков цепочки поставок можно применять и рекомендуется применять сканирование образов и проверку подписей относительно образов Dynatrace.

Реплицируя образы Dynatrace в частный реестр, можно бесшовно совмещать отличную производительность доставки с гарантией безопасных, подписанных и неизменяемых образов. Кроме того, предоставляются мультиархитектурные образы для обеспечения совместимости с различными платформами, поддерживающими архитектуры процессоров ARM64 (AArch64) и x86-64 на Linux.

На этой странице приведены инструкции по использованию подписанных и неизменяемых образов контейнеров Dynatrace, размещённых в частном реестре.

## Предварительные требования

Перед началом работы нужно убедиться, что выполнены следующие предварительные требования:

* Требуется версия Dynatrace Operator v0.11 или более поздняя
* Требуемые целевые архитектуры процессора: ARM64 (AArch64) и/или x86-64
* Требуется разрешить исходящий трафик к публичному реестру
* Требуется частный реестр с сохранёнными образами Dynatrace

Рекомендации по хранению образов Dynatrace в частном реестре приведены в разделе [Хранение образов Dynatrace в частных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Хранение образов Dynatrace в частных реестрах").

## Создание секрета для извлечения образов

Если частный реестр требует аутентификации, Dynatrace Operator нужны учётные данные для извлечения образов. Эти учётные данные предоставляются в виде секрета для извлечения образов Kubernetes.

Поле `customPullSecret` в конфигурации DynaKube аутентифицирует **только компоненты, которыми Dynatrace Operator управляет в пространстве имён `dynatrace`**.

Dynatrace Operator **не** копирует этот секрет для извлечения образов в пространства имён приложений и не добавляет его в инжектируемые поды приложений. Следуя принципу минимальных привилегий и для ограничения риска раскрытия учётных данных реестра, Dynatrace Operator не реплицирует секрет для извлечения образов за пределы пространства имён `dynatrace`. Инжектируемым подам этот секрет нужен из-за добавленного init-контейнера, поэтому его нужно распределить либо на узел, либо на serviceAccount, либо напрямую на под.

### Где применяется секрет для извлечения образов

В следующей таблице показано, какой образ извлекает узел Kubernetes в каждом сценарии, покрывает ли его `customPullSecret` из DynaKube, и что нужно настроить.

| Сценарий | Образ, который узел извлекает для пода | Достаточно ли `customPullSecret`? | Что нужно настроить |
| --- | --- | --- | --- |
| Компоненты, управляемые Operator, в пространстве имён `dynatrace` | Образ Dynatrace Operator | Да | Задать `customPullSecret` в DynaKube. |
| Инжектируемые поды приложений с извлечением образа узлом ([эфемерный том](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Справочная информация о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, извлечение образа драйвером CSI и загрузку ZIP.") или [через том CSI](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#csi-node-image-pull "Справочная информация о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, извлечение образа драйвером CSI и загрузку ZIP.")) | Образ модулей кода OneAgent (init-контейнер) | Нет | Распределить секрет для извлечения образов в пространство имён приложения, на узел или на под. См. [Предоставление секретов для извлечения образов для инжектируемых рабочих нагрузок](#injected-workloads). |
| Инжектируемые поды приложений с [извлечением образа драйвером CSI](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#csi-image-pull "Справочная информация о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, извлечение образа драйвером CSI и загрузку ZIP."), [загрузкой ZIP драйвером CSI](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#csi-zip "Справочная информация о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, извлечение образа драйвером CSI и загрузку ZIP.") или [загрузкой ZIP](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#zip-download "Справочная информация о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, извлечение образа драйвером CSI и загрузку ZIP.") | Образ Dynatrace Operator (init-контейнер) | Нет | Распределить секрет для извлечения образов в пространство имён приложения, на узел или на под. См. [Предоставление секретов для извлечения образов для инжектируемых рабочих нагрузок](#injected-workloads). |

Для [извлечения образа драйвером CSI](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#csi-image-pull "Справочная информация о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, извлечение образа драйвером CSI и загрузку ZIP.") `customPullSecret` дополнительно покрывает образ модулей кода OneAgent, который драйвер CSI извлекает в пространстве имён `dynatrace`. Инжектируемым подам всё равно нужен собственный секрет для извлечения образа init-контейнера.

### Создание секрета для извлечения образов

Чтобы создать секрет для извлечения образов для компонентов, управляемых Operator, следуйте этой [документации Kubernetes﻿](https://dt-url.net/p403yu6) о том, как создать секрет Kubernetes на основе существующих учётных данных или путём указания учётных данных в командной строке. Ссылку на него нужно указать через поле `customPullSecret` в DynaKube, как показано в разделе [Настройка DynaKube для использования образов из частного реестра](#configure-dynakube).

### Предоставление секретов для извлечения образов для инжектируемых рабочих нагрузок

Инжектируемые поды запускают init-контейнер Dynatrace, образ которого узел Kubernetes должен извлечь. Поскольку Dynatrace Operator не распределяет `customPullSecret` за пределы пространства имён `dynatrace`, эти учётные данные нужно предоставить самостоятельно на одном из следующих уровней:

* **Уровень узла**: настроить аутентификацию реестра непосредственно на каждом узле.
* **Уровень пространства имён**: добавить секрет для извлечения образов в каждое пространство имён и соответствующие serviceAccount, где выполняются инжектируемые поды приложений. Секреты для извлечения образов действительны только в собственном пространстве имён, поэтому это нужно повторить для каждого пространства имён приложения.
* **Уровень пода**: настроить секрет для извлечения образов через поле `imagePullSecrets` в спецификации пода приложения.

Подробности приведены в [документации Kubernetes по извлечению образов из частных реестров﻿](https://kubernetes.io/docs/concepts/containers/images/#using-a-private-registry).

Ранее под приложения мог повторно использовать образ, который другой под уже извлёк на тот же узел, даже без собственных учётных данных. Начиная с Kubernetes 1.35, feature gate [`KubeletEnsureSecretPulledImages`﻿](https://kubernetes.io/docs/concepts/containers/images/#ensureimagepullcredentialverification) включён по умолчанию, и kubelet проверяет учётные данные для извлечения образов для каждого пода, даже для образов, уже кэшированных на узле. Если секреты для извлечения образов не распределены, как описано выше, инжектируемые поды завершаются с ошибкой `ImagePullBackOff`.

## Развёртывание Dynatrace Operator с образами из частного реестра

В этом разделе приведены инструкции по развёртыванию Dynatrace Operator с образом контейнера, поступающим из частного реестра.

Dynatrace Operator состоит из нескольких компонентов, все из которых используют один и тот же образ `dynatrace-operator` со специфическими для каждого компонента конфигурациями развёртывания.

Helm

Манифест

Следующая команда устанавливает Dynatrace Operator и настраивает извлечение образов контейнеров из частного реестра (например, "registry.my-company.com") путём задания значений `imageRef.repository`, `imageRef.tag` и `customPullSecret` (передаётся в `imagePullSecrets` спецификаций подов):

Если используется Helm версии 4.0 и выше, вместо флага `--atomic` нужно использовать `--rollback-on-failure`.

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "imageRef.repository=<your-private-registry>/dynatrace-operator" \



--set "imageRef.tag=<tag>" \



--set "customPullSecret=<secretName>" \



--create-namespace \



--namespace dynatrace \



--atomic \
```

Альтернативно уже существующую установку можно обновить следующим образом:

```
helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "imageRef.repository=<your-private-registry>/dynatrace-operator" \



--set "imageRef.tag=<tag>" \



--set "customPullSecret=<secretName>" \



--namespace dynatrace \



--reset-then-reuse-values \



--atomic \
```

Чтобы избежать утомительного и подверженного ошибкам редактирования больших файлов YAML, рекомендуется использовать Helm для генерации манифеста через `helm template`.

Если же вы предпочитаете вносить изменения напрямую, нужно обязательно скорректировать поля `image` и `imagePullSecrets` во всех контейнерах и подах, где встречается образ `dynatrace-operator`.

## Настройка DynaKube для использования образов из приватного registry

Чтобы указать оператору Dynatrace использовать образы контейнеров из приватного registry, нужно настроить соответствующие поля `image` в пользовательском ресурсе DynaKube. Настроенные образы будут развёрнуты в кластере Kubernetes для настройки компонентов мониторинга.

Следующий фрагмент DynaKube демонстрирует, как настроить [Cloud-Native Full-Stack monitoring setup](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание того, как происходит развёртывание на Kubernetes.") с использованием образов контейнеров Dynatrace из приватного registry.

```
apiVersion: dynatrace.com/v1beta6



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



...



activeGate:



...



image: <your-private-registry>/dynatrace-activegate:<tag>



...
```

После настройки необходимых полей пользовательский ресурс DynaKube нужно применить к кластеру Kubernetes.

Поле `customPullSecret` аутентифицирует только компоненты, управляемые оператором, в пространстве имён `dynatrace`. Если узел Kubernetes загружает образ code modules OneAgent для внедрённых подов приложений, secret для загрузки нужно предоставить самостоятельно. Подробности см. в разделе [Provide pull secrets for injected workloads](#injected-workloads).

Дополнительную информацию о поле `customPullSecret`, полях `image` или пользовательском ресурсе DynaKube см. в примерах ниже или на справочной странице [DynaKube parameters for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки оператора Dynatrace на Kubernetes.").

Нужны дополнительные примеры?

#### Application and Kubernetes Observability

Следующий фрагмент пользовательского ресурса описывает, как настроить DynaKube для [Application Observability and Kubernetes observability](/managed/ingest-from/setup-on-k8s/deployment "Развернуть оператор Dynatrace на Kubernetes") с образами контейнеров из приватного registry:

```
apiVersion: dynatrace.com/v1beta6



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



...



activeGate:



...



image: <your-private-registry>/dynatrace-activegate:<tag>



...
```

## Проверка подписи образа

Все неизменяемые и подписанные образы контейнеров соответствуют лучшим практикам, что повышает безопасность и защищает от атак на цепочку поставок. Чтобы узнать, как проверить подписи и гарантировать целостность программного обеспечения, см. [Verify Dynatrace image signatures](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Проверка подписей образов Dynatrace").

## Связанные темы

* [Store Dynatrace images in private registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Хранение образов Dynatrace в приватных registry")
* [Use a public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Настройка оператора Dynatrace для использования образов из публичного registry для себя и управляемых им компонентов. Это можно сделать вручную или через автоматическое разрешение из окружения Dynatrace.")