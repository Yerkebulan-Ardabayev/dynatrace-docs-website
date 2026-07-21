---
title: Хранение образов Dynatrace в приватных реестрах
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry
---

# Хранение образов Dynatrace в приватных реестрах

# Хранение образов Dynatrace в приватных реестрах

* 7 минут на чтение
* Опубликовано 29 февр. 2024

Для пользователей, которым нужен больший контроль над средой хостинга образов, Dynatrace предлагает возможность реплицировать образы и подписи в приватные реестры.

Для оптимальной производительности и отсутствия рисков ограничения частоты запросов в высоконагруженных и динамичных средах рекомендуется использовать приватный реестр. Кроме того, для соответствия стандартам безопасности и обеспечения целостности ПО при снижении рисков цепочки поставок рекомендуется применять сканирование образов и проверку подписи по образам Dynatrace.

Реплицируя образы Dynatrace в приватный реестр, можно совместить отличную производительность доставки с гарантией безопасных, подписанных и неизменяемых образов. Предоставляются мультиархитектурные образы для обеспечения совместимости с различными платформами, поддерживающими архитектуры процессоров ARM64 (AArch64) и x86-64 на Linux.

На этой странице приведены рекомендации по безопасному хранению неизменяемых образов Dynatrace в приватном реестре. В неё включены инструкции по загрузке образов, проверке подписей образов и отправке их в выбранный приватный реестр.

## Предварительные требования

Перед началом работы необходимо убедиться в выполнении следующих предварительных требований:

* Обязательно: приватный реестр
* Обязательно: доступ на запись к репозиториям образов Dynatrace
* Опционально: [Skopeo﻿](https://github.com/containers/skopeo/blob/main/install.md) для удобного копирования наших мультиархитектурных образов
* Опционально: [Cosign﻿](https://docs.sigstore.dev/system_config/installation/) для проверки подписи образов

## Образы контейнеров Dynatrace

Неизменяемые и подписанные образы контейнеров Dynatrace доступны в различных реестрах контейнеров. Подробнее о репозиториях и информации о тегах см. в разделе [поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Настройка Dynatrace Operator для использования образов из публичного реестра для себя и управляемых им компонентов. Это можно сделать вручную или через автоматическое разрешение из среды Dynatrace.").

Настоятельно рекомендуется выбрать один из поддерживаемых публичных реестров, из которого будет выполняться копирование образов контейнеров.

Не следует использовать встроенный реестр Dynatrace для копирования образов в приватные реестры.

Исключение составляет образ OneAgent для Classic Full-Stack, который **обязательно** должен копироваться из встроенного реестра, чтобы работать корректно.

### Варианты observability

В зависимости от выбранных [вариантов observability](/managed/ingest-from/setup-on-k8s/deployment#observability-options-for-kubernetes "Развёртывание Dynatrace Operator на Kubernetes") может потребоваться скопировать только необходимые образы. В следующей таблице показаны связи между образами Dynatrace и вариантами observability.

| Вариант observability | Dynatrace Operator | Dynatrace ActiveGate | Dynatrace Code Module | Dynatrace OneAgent |
| --- | --- | --- | --- | --- |
| Полная observability  (Classic Full-Stack) | обязательно | обязательно | - | обязательно [1](#fn-1-1-def) |
| Полная observability  (Cloud-Native Full-Stack) | обязательно | обязательно | обязательно | обязательно |
| Observability для Kubernetes | обязательно | обязательно | - | - |
| Application Observability | обязательно | обязательно | обязательно | - |

1

Должен быть реплицирован из встроенного реестра Dynatrace. Подробнее см. в разделе [Поддержка мониторинга Classic Full-Stack](#classic-full-stack).

### Теги образов

Чтобы показать, как версионирование напрямую связано с тегированием образов, в следующей таблице приведены реальные примеры тегов образов для образов контейнеров Dynatrace.

Обратите внимание, что Dynatrace ActiveGate, Code Modules и OneAgent используют схожий подход к версионированию, тогда как Dynatrace Operator, который следует отдельному циклу выпусков, использует другой подход к версионированию.

Во всех случаях для образов контейнеров применяется тегирование на основе версий. Изменяемые теги образов, такие как «latest», не используются.

| Образ контейнера | Тег образа |
| --- | --- |
| dynatrace-operator | `docker.io/dynatrace/dynatrace-operator:v1.5.0` |
| dynatrace-activegate | `public.ecr.aws/dynatrace/dynatrace-activegate:1.301.70.20241127-162512` |
| dynatrace-codemodules | `public.ecr.aws/dynatrace/dynatrace-codemodules:1.301.70.20241127-162512` |
| dynatrace-oneagent | `public.ecr.aws/dynatrace/dynatrace-oneagent:1.301.70.20241127-162512` |
| dynatrace-k8s-node-config-collector | `public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector:1.0.0` |

### Проверка подписи образов

Все неизменяемые и подписанные образы контейнеров соответствуют лучшим практикам, повышающим безопасность и защиту от атак на цепочку поставок. Чтобы узнать, как проверять подписи и гарантировать целостность ПО, см. [Проверка подписей образов Dynatrace](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Проверка подписей образов Dynatrace").

## Копирование образов контейнеров Dynatrace

В следующем руководстве описано, как скопировать образы контейнеров Dynatrace из публичного Amazon ECR в приватный реестр на следующем примере атрибутов.

|  |  |
| --- | --- |
| Адрес приватного реестра контейнеров | `registry.my-company.com` |
| Репозиторий Dynatrace Operator | `dynatrace-operator` |
| Репозиторий Dynatrace ActiveGate | `dynatrace-activegate` |
| Репозиторий Dynatrace Code Modules | `dynatrace-codemodules` |
| Репозиторий Dynatrace OneAgent | `dynatrace-oneagent` |
| Репозиторий Dynatrace K8s Node Config Collector | `dynatrace-k8s-node-config-collector` |

Ниже приведены инструкции по копированию образов контейнеров в приватный реестр:

Skopeo (рекомендуется)

Интерфейс командной строки Docker

Рекомендуется

Благодаря поддержке удобного копирования мультиархитектурных образов и подписей[1](#fn-2-1-def) настоятельно рекомендуется использовать Skopeo CLI для копирования образов контейнеров. Подробнее о Skopeo CLI см. в репозитории [Skopeo GitHub﻿](https://github.com/containers/skopeo).

В приведённых ниже инструкциях всегда заменяйте `<tag>` на доступную версию (см. раздел [Поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Настройка Dynatrace Operator для использования образов из публичного реестра для себя и управляемых им компонентов. Это можно сделать вручную или через автоматическое разрешение из среды Dynatrace.")).

#### Копирование образа Dynatrace Operator

Следующая команда показывает, как скопировать образ Dynatrace Operator в приватный реестр:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-operator:<tag> \



docker://registry.my-company.com/dynatrace-operator:<tag>
```

#### Копирование образа Dynatrace ActiveGate

Следующая команда показывает, как скопировать образ Dynatrace ActiveGate в приватный реестр:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-activegate:<tag> \



docker://registry.my-company.com/dynatrace-activegate:<tag>
```

#### Копирование образа Dynatrace Code Modules

Следующая команда показывает, как скопировать образ Dynatrace Code Modules в приватный реестр:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-codemodules:<tag> \



docker://registry.my-company.com/dynatrace-codemodules:<tag>
```

#### Копирование образа Dynatrace OneAgent

Следующая команда показывает, как скопировать образ Dynatrace OneAgent в приватный реестр:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-oneagent:<tag> \



docker://registry.my-company.com/dynatrace-oneagent:<tag>
```

#### Копирование образа Dynatrace K8s Node Config Collector

Следующая команда показывает, как скопировать образ Dynatrace K8s Node Config Collector в приватный реестр:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector:<tag> \



docker://registry.my-company.com/dynatrace-k8s-node-config-collector:<tag>
```

1

Требует, чтобы параметр `use-sigstore-attachments` был установлен в значение `true` в конфигурации [реестров контейнеров﻿](https://github.com/containers/image/blob/main/docs/containers-registries.d.5.md#individual-configuration-sections) *Skopeo*.

Настоятельно рекомендуется использовать Skopeo CLI вместо Docker CLI для копирования образов контейнеров Dynatrace из публичных реестров в приватные, так как Docker CLI не предоставляет удобного способа копирования мультиархитектурных образов и подписей.

Если всё же требуется использовать Docker CLI, обратитесь к [официальной документации Docker CLI﻿](https://docs.docker.com/engine/reference/commandline/cli/).

### Поддержка Classic Full-Stack monitoring

[Classic Full-Stack monitoring](/managed/ingest-from/setup-on-k8s/how-it-works#classic "In-depth description on how the deployment on Kubernetes works.") требует предварительно настроенного образа Dynatrace OneAgent, который доступен **только** через встроенный реестр Dynatrace.

Следовательно, образ OneAgent нужно реплицировать через встроенный реестр Dynatrace, как описано ниже.

Предварительные требования

#### Перед началом работы

Убедитесь, что выполнены следующие предварительные требования:

* Обязательные необязательные предварительные требования сверху
* Обязательные учётные данные для встроенного реестра Dynatrace

#### Получение учётных данных встроенного реестра Dynatrace

Поскольку встроенный реестр Dynatrace требует аутентификации, нужно знать ID своей среды мониторинга и указать PaaS-токен для входа:

* Чтобы определить `<your-environment-id>`, см. [ID среды](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").
* Чтобы определить `<your-paas-token>`, см. [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

Пример входа с помощью CLI *Skopeo*:

```
skopeo login -u <your-environment-id> -p <your-paas-token> <your-environment-url>
```

Обратите внимание, что этот раздел касается только конфигураций Classic Full-Stack monitoring.

#### Копирование образа Dynatrace OneAgent для Classic Full-Stack monitoring

Встроенный реестр Dynatrace поддерживает только архитектуры x86-64 под управлением Linux. Поэтому рекомендуется явно задать/переопределить архитектуру и операционную систему.

Как определить тег образа OneAgent

Встроенный реестр Dynatrace предоставляет следующие форматы тегов образа OneAgent:

* `latest`
* `latest-raw`
* `<major>.<minor>.<revision>`
* `<major>.<minor>.<revision>-raw`

Для репликации образов рекомендуется копировать raw-образы (образы с суффиксом тега `-raw`).

Чтобы понять, какие версии OneAgent доступны для репликации, можно использовать следующие Deployment API:

* [Список доступных версий OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "List available versions of OneAgent via Dynatrace API.") для обзора доступных версий OneAgent.
* [Просмотр последней версии OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-version-latest "View the latest version of OneAgent via Dynatrace API."), если нужно понять, какая версия OneAgent скрывается за `latest`, или автоматизировать репликацию образа OneAgent.

В следующих примерах показано, как версии OneAgent преобразуются в теги образов, доступные во встроенном реестре Dynatrace:

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

Подробнее о настройке пользовательского ресурса DynaKube см. примеры того, как [использовать частные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

## Похожие темы

* [Использование частного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")
* [Проверка подписей образов Dynatrace](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures")