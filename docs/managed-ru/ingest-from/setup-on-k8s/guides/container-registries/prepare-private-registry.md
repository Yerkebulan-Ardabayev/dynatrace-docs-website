---
title: Хранение образов Dynatrace в частных реестрах
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry
scraped: 2026-05-12T11:36:37.178163
---

# Хранение образов Dynatrace в частных реестрах

# Хранение образов Dynatrace в частных реестрах

* Чтение: 7 мин
* Опубликовано 29 февраля 2024 г.

Для пользователей, которым нужен больший контроль над средой размещения образов, Dynatrace предлагает возможность реплицировать образы и подписи в частные реестры.

Мы рекомендуем использовать частный реестр для оптимальной производительности и отсутствия рисков ограничения частоты запросов в условиях высокой нагрузки и динамичных сред. Кроме того, для соответствия стандартам безопасности и обеспечения целостности ПО при снижении рисков цепочки поставок можно применять сканирование образов и проверку подписей образов Dynatrace, что и рекомендуется.

Реплицируя образы Dynatrace в свой частный реестр, вы беспрепятственно сочетаете отличную производительность доставки с гарантией безопасных, подписанных и неизменяемых образов. Мы предоставляем мультиархитектурные образы для обеспечения совместимости с различными платформами с поддержкой архитектур ЦП ARM64 (AArch64) и x86-64 на Linux.

На этой странице приведены указания по безопасному хранению неизменяемых образов Dynatrace в частном реестре. Она включает инструкции по загрузке образов, проверке подписей образов и их отправке в выбранный вами частный реестр.

## Предварительные требования

Прежде чем начать, убедитесь, что выполнены следующие предварительные требования:

* Обязательно Частный реестр
* Обязательно Доступ на запись к репозиториям образов для образов Dynatrace
* Необязательно [Skopeo](https://github.com/containers/skopeo/blob/main/install.md) для удобного копирования наших мультиархитектурных образов
* Необязательно [Cosign](https://docs.sigstore.dev/system_config/installation/) для проверки подписи образов

## Образы контейнеров Dynatrace

Неизменяемые и подписанные образы контейнеров Dynatrace доступны в различных реестрах контейнеров. Подробнее о репозиториях и тегах см. в наших [поддерживаемых публичных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использование публичного реестра").

Мы настоятельно рекомендуем выбрать один из поддерживаемых нами публичных реестров, из которого копировать образы контейнеров.

Пожалуйста, не используйте встроенный реестр Dynatrace для копирования образов в частные реестры.

Исключение составляет образ OneAgent для Classic Full-Stack, где соответствующий образ **необходимо** копировать из встроенного реестра для корректной работы.

### Опции наблюдаемости

В зависимости от выбранных [опций наблюдаемости](/managed/ingest-from/setup-on-k8s/deployment#observability-options-for-kubernetes "Развёртывание Dynatrace Operator в Kubernetes") можно скопировать только необходимые образы. В следующей таблице показаны связи между образами Dynatrace и опциями наблюдаемости.

| Опция наблюдаемости | Dynatrace Operator | Dynatrace ActiveGate | Dynatrace Code Module | Dynatrace OneAgent |
| --- | --- | --- | --- | --- |
| Full observability  (Classic Full-Stack) | требуется | требуется | - | требуется [1](#fn-1-1-def) |
| Full observability  (Cloud-Native Full-Stack) | требуется | требуется | требуется | требуется |
| Kubernetes Observability | требуется | требуется | - | - |
| Application Observability | требуется | требуется | требуется | - |

1

Необходимо реплицировать из встроенного реестра Dynatrace. Подробнее см. [Поддержка мониторинга Classic Full-Stack](#classic-full-stack).

### Теги образов

Чтобы показать, как версионирование напрямую связано с тегированием образов, в следующей таблице приведены реальные примеры тегов образов контейнеров Dynatrace.

Обратите внимание, что Dynatrace ActiveGate, Code Modules и OneAgent используют схожий подход к версионированию, тогда как Dynatrace Operator, который следует отдельному циклу выпусков, использует другой подход к версионированию.

Во всех случаях для образов контейнеров применяется тегирование на основе версий. Изменяемые теги образов, такие как 'latest', не используются.

| Образ контейнера | Тег образа |
| --- | --- |
| dynatrace-operator | `docker.io/dynatrace/dynatrace-operator:v1.5.0` |
| dynatrace-activegate | `public.ecr.aws/dynatrace/dynatrace-activegate:1.301.70.20241127-162512` |
| dynatrace-codemodules | `public.ecr.aws/dynatrace/dynatrace-codemodules:1.301.70.20241127-162512` |
| dynatrace-oneagent | `public.ecr.aws/dynatrace/dynatrace-oneagent:1.301.70.20241127-162512` |
| dynatrace-k8s-node-config-collector | `public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector:1.0.0` |

### Проверка подписи образов

Все наши неизменяемые и подписанные образы контейнеров соответствуют лучшим практикам, повышая безопасность и защищая от атак на цепочку поставок. О том, как проверять подписи и гарантировать целостность ПО, см. [Проверка подписей образов Dynatrace](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Проверка подписей образов Dynatrace").

## Копирование образов контейнеров Dynatrace

В следующем руководстве описано, как копировать образы контейнеров Dynatrace из публичного Amazon ECR в наш частный реестр со следующими примерными атрибутами.

|  |  |
| --- | --- |
| Адрес частного реестра контейнеров | `registry.my-company.com` |
| Репозиторий Dynatrace Operator | `dynatrace-operator` |
| Репозиторий Dynatrace ActiveGate | `dynatrace-activegate` |
| Репозиторий Dynatrace Code Modules | `dynatrace-codemodules` |
| Репозиторий Dynatrace OneAgent | `dynatrace-oneagent` |
| Репозиторий Dynatrace K8s Node Config Collector | `dynatrace-k8s-node-config-collector` |

Инструкции ниже по копированию образов контейнеров в ваш частный реестр:

Skopeo (рекомендуется)

Docker CLI

Рекомендуется

Благодаря поддержке удобного копирования мультиархитектурных образов и подписей[1](#fn-2-1-def) мы настоятельно рекомендуем использовать Skopeo CLI для копирования образов контейнеров. Подробнее о Skopeo CLI см. в [репозитории Skopeo на GitHub](https://github.com/containers/skopeo).

В следующих инструкциях обязательно всегда заменяйте `<tag>` доступной версией (см. раздел [Поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использование публичного реестра")).

#### Копирование образа Dynatrace Operator

Следующая команда показывает, как скопировать образ Dynatrace Operator в наш частный реестр:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-operator:<tag> \



docker://registry.my-company.com/dynatrace-operator:<tag>
```

#### Копирование образа Dynatrace ActiveGate

Следующая команда показывает, как скопировать образ Dynatrace ActiveGate в наш частный реестр:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-activegate:<tag> \



docker://registry.my-company.com/dynatrace-activegate:<tag>
```

#### Копирование образа Dynatrace Code Modules

Следующая команда показывает, как скопировать образ Dynatrace Code Modules в наш частный реестр:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-codemodules:<tag> \



docker://registry.my-company.com/dynatrace-codemodules:<tag>
```

#### Копирование образа Dynatrace OneAgent

Следующая команда показывает, как скопировать образ Dynatrace OneAgent в наш частный реестр:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-oneagent:<tag> \



docker://registry.my-company.com/dynatrace-oneagent:<tag>
```

#### Копирование образа Dynatrace K8s Node Config Collector

Следующая команда показывает, как скопировать образ Dynatrace K8s Node Config Collector в наш частный реестр:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector:<tag> \



docker://registry.my-company.com/dynatrace-k8s-node-config-collector:<tag>
```

1

Требует установки `use-sigstore-attachments` в `true` в конфигурации [реестров контейнеров](https://github.com/containers/image/blob/main/docs/containers-registries.d.5.md#individual-configuration-sections) *Skopeo*.

Мы настоятельно рекомендуем использовать Skopeo CLI вместо Docker CLI для копирования образов контейнеров Dynatrace из публичных реестров в частные, так как Docker CLI не предоставляет удобного способа копировать мультиархитектурные образы и подписи.

Если вы всё же хотите использовать Docker CLI, обратитесь к [официальной документации Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).

### Поддержка мониторинга Classic Full-Stack

[Classic Full-Stack monitoring](/managed/ingest-from/setup-on-k8s/how-it-works#classic "Подробное описание того, как работает развёртывание в Kubernetes.") требует предварительно настроенного образа Dynatrace OneAgent, который доступен **только** через встроенный реестр Dynatrace.

Следовательно, образ OneAgent необходимо реплицировать через встроенный реестр Dynatrace, как описано ниже.

Предварительные требования

#### Прежде чем начать

Убедитесь, что выполнены следующие предварительные требования:

* Обязательно Все требования из начала страницы, кроме необязательных
* Обязательно Учётные данные для встроенного реестра Dynatrace

#### Получение учётных данных встроенного реестра Dynatrace

Поскольку встроенный реестр Dynatrace требует аутентификации, вам нужно знать ID вашей среды мониторинга и указать токен PaaS для входа:

* Чтобы определить `<your-environment-id>`, см. [ID среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, как работать со средами мониторинга.").
* Чтобы определить `<your-paas-token>`, см. [токен PaaS](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите понятие токена доступа и его областей действия.").

Пример входа с помощью *Skopeo* CLI:

```
skopeo login -u <your-environment-id> -p <your-paas-token> <your-environment-url>
```

Обратите внимание, что этот раздел касается только конфигураций мониторинга Classic Full-Stack.

#### Копирование образа Dynatrace OneAgent для мониторинга Classic Full-Stack

Встроенный реестр Dynatrace поддерживает только архитектуры x86-64 под управлением Linux. Поэтому мы рекомендуем явно задавать/переопределять архитектуру и операционную систему.

Как определить тег образа OneAgent

Встроенный реестр Dynatrace предоставляет следующие форматы тегов образа OneAgent:

* `latest`
* `latest-raw`
* `<major>.<minor>.<revision>`
* `<major>.<minor>.<revision>-raw`

Для репликации образов мы рекомендуем копировать raw-образы (образы с суффиксом тега `-raw`).

Чтобы понять, какие версии OneAgent доступны для репликации, можно использовать следующие Deployment API:

* [Список доступных версий OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "Список доступных версий OneAgent через Dynatrace API.") для обзора доступных версий OneAgent.
* [Просмотр последней версии OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-version-latest "Просмотр последней версии OneAgent через Dynatrace API."), если вы хотите понять, какая версия OneAgent скрывается за `latest`, или автоматизировать репликацию образа OneAgent.

Следующие примеры показывают, как версии OneAgent соотносятся с тегами образов, доступными во встроенном реестре Dynatrace:

| Версия OneAgent | Тег образа OneAgent |
| --- | --- |
| latest | **latest-raw** |
| 1.283.114.20240129-173640 | **1.283.114-raw** |

Перед выполнением следующей команды обязательно замените `<tag-with-raw-suffix>` и `<environment-id>`:

```
skopeo copy --override-arch amd64 --override-os linux



docker://<your_environment_domain_name>/linux/oneagent:<tag-with-raw-suffix> \



docker://registry.my-company.com/dynatrace-oneagent-classic:<tag-with-raw-suffix>
```

Дополнительные сведения о настройке пользовательского ресурса DynaKube см. в наших примерах того, как [использовать частные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование частного реестра").

## Связанные темы

* [Использование частного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование частного реестра")
* [Проверка подписей образов Dynatrace](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Проверка подписей образов Dynatrace")