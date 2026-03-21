---
title: Мониторинг управляемого Google Cloud Run
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun
scraped: 2026-03-06T21:18:15.453486
---

Управляемый Google [Cloud Run](https://cloud.google.com/run) — это вычислительная платформа для запуска контейнеров в бессерверной среде. Для мониторинга сервисов, работающих на управляемом Google Cloud Run, с помощью Dynatrace необходимо интегрировать OneAgent в ваше контейнеризированное приложение.

Поддержка управляемого Cloud Run в средах выполнения [первого и второго поколения](https://cloud.google.com/run/docs/about-execution-environments) в настоящее время ограничена **Java** и **Node.js**.

## Интеграция Dynatrace в ваши контейнеры

Существует несколько способов сборки и развёртывания контейнеров в Cloud Run, например, с помощью [Cloud Build](https://cloud.google.com/build).

Хотя инструкции по интеграции Dynatrace могут отличаться в зависимости от используемого технологического стека для сборки и развёртывания, интеграция Dynatrace в целом следует одному и тому же подходу:

1. Добавьте необходимые бинарные файлы OneAgent в образ контейнера (например, загрузив их через REST API или скопировав из слоя образа OneAgent).
2. Настройте OneAgent с необходимыми параметрами подключения и дополнительными опциями, такими как пользовательские теги.
3. Включите внедрение в процесс для автоматической инструментации ваших рабочих нагрузок.

### Предварительные требования

Перед началом работы необходимо выполнить следующее:

* Получите **токен доступа** для загрузки Dynatrace OneAgent с областью действия `InstallerDownload`. Подробнее о токенах доступа см. [Dynatrace API — Токены и аутентификация](../../../dynatrace-api/basics/dynatrace-api-authentication.md "Find out how to get authenticated to use the Dynatrace API.").

  В приведённых ниже процедурах замените `<DT_TOKEN>` вашим реальным токеном доступа.
* Получите **идентификатор среды**. Подробнее об идентификаторах сред см. [Что такое среда мониторинга?](../../../discover-dynatrace/get-started/monitoring-environment.md "Understand and learn how to work with monitoring environments.").

  В приведённых ниже процедурах замените `<DT_ENV_ID>` вашим реальным идентификатором среды.
* Получите конечную точку Dynatrace API, определённую вашим [URL среды](../../../discover-dynatrace/get-started/monitoring-environment.md "Understand and learn how to work with monitoring environments.") или альтернативно [адресом ActiveGate](../../dynatrace-activegate.md "Understand the basic concepts related to ActiveGate.").

  В приведённых ниже процедурах замените `<DT_ENV_FQDN>` реальной конечной точкой Dynatrace API.
* Установите [gcloud CLI](https://cloud.google.com/sdk/docs/install)

После выполнения указанных предварительных требований следуйте одной из приведённых процедур (выберите вкладку) для интеграции Dynatrace в ваши контейнеры.

Cloud build с cloudbuild.yaml

Cloud Build без cloudbuild.yaml

Jib

### Интеграция в облачную сборку с `cloudbuild.yaml`

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Добавление установщика OneAgent**](cloudrun.md#add-oneagent-installer-option-1 "Monitor Java application deployed on Google Cloud Run managed.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка Cloud Build**](cloudrun.md#configure-cloud-build-option-1 "Monitor Java application deployed on Google Cloud Run managed.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Сборка и развёртывание**](cloudrun.md#build-and-deploy-option-1 "Monitor Java application deployed on Google Cloud Run managed.")

#### Шаг 1 Добавление установщика OneAgent в Docker-образ

Требуется Docker версии 17.05+

Откройте ваш Dockerfile и добавьте следующие строки в образ приложения **после** последнего `FROM` и **перед** точкой входа контейнера.

```
# FROM ...


ARG DT_API_URL="<DT_ENV_FQDN>/api"


ARG DT_API_TOKEN="<DT_TOKEN>"


ARG DT_ONEAGENT_OPTIONS="flavor=<DT_FLAVOR&include=<DT_TECHNOLOGY>"


ENV DT_HOME="/opt/dynatrace/oneagent"


RUN apt-get update && \


apt-get install -y wget && \


apt-get install unzip && \


mkdir -p "$DT_HOME" && \


wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \


unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \


rm "$DT_HOME/oneagent.zip"


ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so


# Run the web service on container startup.


# ENTRYPOINT ...
```

Обязательно замените заполнители вашими реальными значениями.

* `<DT_ENV_FQDN>` — ваша реальная конечная точка Dynatrace API, как описано в разделе [Предварительные требования](#prerequisites).
* `<DT_TOKEN>` — ваш реальный токен, как описано в разделе [Предварительные требования](#prerequisites).
* `<DT_TECHNOLOGY>` — артефакт OneAgent, специфичный для технологического стека вашего образа, например `java` или `nodejs`.
* `<DT_FLAVOR>` — для образов на основе Alpine Linux выберите `musl`, в противном случае — `default`

Команды `wget` и `unzip` выше могут завершиться ошибкой, если они не предоставляются базовым образом.

Пример

Пример Dockerfile, предоставленный Google в руководстве по началу работы с Google Cloud Run на Java, адаптированный с учётом приведённых выше инструкций.

```
# Use the official maven/Java 11 image to create a build artifact.


# https://hub.docker.com/_/maven


FROM maven:3-jdk-11-slim AS build-env


# Set the working directory to /app


WORKDIR /app


# Copy the pom.xml file to download dependencies


COPY pom.xml .


# Copy local code to the container image.


COPY src ./src


# Download dependencies and build a release artifact.


RUN mvn package -DskipTests


# Use OpenJDK for base image.


# https://hub.docker.com/_/openjdk


# https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds


FROM openjdk:11-jre-slim


# Copy the jar to the production image from the builder stage.


COPY --from=build-env /app/target/hello-world-*.jar /hello-world.jar


# Get and enable Dynatrace


ARG DT_API_URL="<DT_ENV_FQDN>/api"


ARG DT_API_TOKEN="<DT_TOKEN>"


ARG DT_ONEAGENT_OPTIONS="flavor=default&include=java"


ENV DT_HOME="/opt/dynatrace/oneagent"


RUN apt-get update && \


apt-get install -y wget && \


apt-get install unzip && \


mkdir -p "$DT_HOME" && \


wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \


unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \


rm "$DT_HOME/oneagent.zip"


ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so


# Run the web service on container startup.


ENTRYPOINT ["java", "-jar", "/hello-world.jar"]
```

#### Шаг 2 Настройте файл конфигурации Google Cloud Build

Откройте ваш файл [cloudbuild.yaml](https://cloud.google.com/build/docs/deploying-builds/deploy-cloud-run#continuous_deployment) и добавьте следующие переменные окружения и bash-команды в шаг сборки:

```
# Build the container image


- name: 'gcr.io/cloud-builders/docker'


args: ['build', '-t', 'gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>', '.']


# Push the container image to Container Registry


- name: 'gcr.io/cloud-builders/docker'


args: ['push', 'gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>']
```

Добавьте следующие строки в аргументы вашего шага развёртывания:

```
# Deploy container image to Cloud Run


- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'


entrypoint: gcloud


args:


- beta


- run


- deploy


- $_SERVICE_NAME


- --allow-unauthenticated


- --image=gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>


- --region=$_GCP_REGION


- --execution-environment=<ENVIRONMENT>


- --project=$_PROJECT


- --set-env-vars=


DT_TAGS=$_SERVICE_NAME,


DT_LOGLEVELCON=INFO
```

Обязательно замените заполнители вашими реальными значениями.

* `<GCP_PROJECT_ID>` — имя вашего [проекта Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
* `<YOUR_IMAGE_NAME_AND_TAG>` — имя и тег вашего образа для сборки
* `<ENVIRONMENT>` — среда выполнения, которую вы хотите использовать. Допустимые варианты: `gen1` для первого поколения и `gen2` для второго поколения.

Вы можете изменить переменную окружения `DT_TAGS` на другое значение по мере необходимости.

#### Шаг 3 Сборка и развёртывание вашего сервиса Cloud Run

Отредактируйте и выполните эту команду:

```
gcloud builds submit \


<SAMPLE_NAME> \


--project <GCP_PROJECT_ID> \


--substitutions \


"_API_KEY=<DT_TOKEN>,\


_TENANT_NAME=<DT_ENV_ID>,\


_TENANT_FQDN=<DT_ENV_FQDN>,\


_IMAGE_NAME_AND_TAG=<YOUR_IMAGE_NAME_AND_TAG>,\


_SERVICE_NAME=<YOUR_SERVICE_NAME>,\


_PROJECT=<GCP_PROJECT_ID>,\


_GCP_REGION=<GCP_REGION>,\" \


--config cloudbuild.yaml
```

Обязательно замените заполнители вашими реальными значениями.

* `<SAMPLE_NAME>` — имя вашего сервиса Cloud Run
* `<GCP_PROJECT_ID>` — имя вашего [проекта Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
* `<YOUR_IMAGE_NAME_AND_TAG>` — имя и тег вашего образа для сборки

### Интеграция в облачную сборку без `cloudbuild.yaml`

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Добавление установщика OneAgent**](cloudrun.md#add-oneagent-installer-option-2 "Monitor Java application deployed on Google Cloud Run managed.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Сборка и развёртывание**](cloudrun.md#build-and-deploy-option-2 "Monitor Java application deployed on Google Cloud Run managed.")

#### Шаг 1 Добавление установщика OneAgent в Docker-образ

Требуется Docker версии 17.05+

Откройте ваш Dockerfile и добавьте следующий пример в образ приложения **после** последнего `FROM`.

```
ARG DT_API_URL="<DT_ENV_FQDN>/api"


ARG DT_API_TOKEN="<DT_TOKEN>"


ARG DT_ONEAGENT_OPTIONS="flavor=default&include=java"


ENV DT_HOME="/opt/dynatrace/oneagent"


RUN apt-get update && \


apt-get install -y wget && \


apt-get install unzip && \


mkdir -p "$DT_HOME" && \


wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \


unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \


rm "$DT_HOME/oneagent.zip"


ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so


# Run the web service on container startup.


ENTRYPOINT ["java", "-jar", "/hello-world.jar"]
```

Обязательно замените заполнители вашими реальными значениями.

* `<DT_ENV_FQDN>` — ваша реальная конечная точка Dynatrace API, как описано в разделе [Предварительные требования](#prerequisites).
* `<DT_TOKEN>` — ваш реальный токен, как описано в разделе [Предварительные требования](#prerequisites).

* Поддержка технологий включается через параметры `include`. Для сред на основе Alpine Linux используйте `flavor=musl&include=java`.
* Команды `wget` и `unzip` выше могут завершиться ошибкой, если они не предоставляются базовым образом.

Пример

Это пример Dockerfile, предоставленный Google в руководстве по началу работы с Google Cloud Run на Java, адаптированный с учётом приведённых выше инструкций.

```
# Use the official maven/Java 11 image to create a build artifact.


# https://hub.docker.com/_/maven


FROM maven:3-jdk-11-slim AS build-env


# Set the working directory to /app


WORKDIR /app


# Copy the pom.xml file to download dependencies


COPY pom.xml .


# Copy local code to the container image.


COPY src ./src


# Download dependencies and build a release artifact.


RUN mvn package -DskipTests


# Use OpenJDK for base image.


# https://hub.docker.com/_/openjdk


# https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds


FROM openjdk:11-jre-slim


# Copy the jar to the production image from the builder stage.


COPY --from=build-env /app/target/hello-world-*.jar /hello-world.jar


# Get and enable Dynatrace


ARG DT_API_URL="<DT_ENV_FQDN>/api"


ARG DT_API_TOKEN="<DT_TOKEN>"


ARG DT_ONEAGENT_OPTIONS="flavor=default&include=java"


ENV DT_HOME="/opt/dynatrace/oneagent"


RUN apt-get update && \


apt-get install -y wget && \


apt-get install unzip && \


mkdir -p "$DT_HOME" && \


wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \


unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \


rm "$DT_HOME/oneagent.zip"


ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so


# Run the web service on container startup.


ENTRYPOINT ["java", "-jar", "/hello-world.jar"]
```

#### Шаг 2 Сборка и развёртывание вашего сервиса Cloud Run

Для сборки вашего сервиса Cloud Run отредактируйте и выполните следующую команду в каталоге вашего проекта:

```
gcloud builds submit --region=<GCP_REGION> --tag gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>
```

Для развёртывания вашего сервиса Cloud Run отредактируйте и выполните следующую команду:

```
gcloud run deploy <YOUR_SERVICE_NAME> --image gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>
```

Обязательно замените заполнители вашими реальными значениями.

* `<GCP_REGION>` — имя [региона Google Cloud](https://cloud.google.com/compute/docs/regions-zones), в котором вы развёртываете
* `<GCP_PROJECT_ID>` — имя вашего [проекта Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
* `<YOUR_IMAGE_NAME_AND_TAG>` — имя и тег вашего образа для сборки
* `<YOUR_SERVICE_NAME>` — имя сервиса, которое будет отображаться в Dynatrace

### Интеграция с помощью инструмента контейнеризации Jib

[Jib](https://github.com/GoogleContainerTools/jib) от Google — это инструмент контейнеризации, который создаёт оптимизированные Docker- и OCI-образы для ваших Java-приложений без Docker-демона и без необходимости глубокого знания лучших практик Docker. Он доступен в виде плагинов для Maven и Gradle, а также как Java-библиотека.

В репозитории GitHub для Jib вы можете найти [пример интеграции для Java-агента Google StackDriver](https://github.com/GoogleContainerTools/jib/blob/master/examples/java-agent/build.gradle), который следует тому же шаблону, что и интеграция Dynatrace (Загрузка, Настройка и Внедрение). Вы можете адаптировать этот шаблон под свои нужды для интеграции Dynatrace с помощью Jib.

## Дополнительная настройка

Вы можете использовать дополнительные переменные окружения для настройки, например, параметров отладки или расширенных сетевых настроек.

| Имя | Описание |
| --- | --- |
| **Сеть** |  |
| `DT_NETWORK_ZONE` | Указывает использование сетевой зоны. Подробнее см. [Сетевые зоны](../../../manage/network-zones.md "Find out how network zones work in Dynatrace."). |
| `DT_PROXY` | При использовании прокси-сервера используйте эту переменную окружения для передачи учётных данных прокси. Подробнее см. [Настройка OneAgent на контейнерах для мониторинга только приложений](../../setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring.md "Install, update, and uninstall OneAgent on containers for application-only monitoring.") |
| **Дополнительные метаданные для группировки процессов / обнаружения сервисов** |  |
| `DT_LOCALTOVIRTUALHOSTNAME` | Несколько контейнеров иногда определяются как один экземпляр (localhost), что приводит к различным проблемам, например, в обнаружении сервисов или оповещениях о доступности. Используйте эту переменную окружения для определения уникального имени экземпляра контейнера. Подробнее см. [Обнаружение сервисов v1](../../../observe/application-observability/services/service-detection/service-detection-v1.md#adjusting-service-detection "Find out how Dynatrace Service Detection v1 detects and names different types of services.") |
| `DT_APPLICATIONID` | Некоторые технологии не предоставляют уникальных имён приложений. В таких случаях используйте эту переменную окружения для указания уникального имени. Подробнее см. [Обнаружение сервисов v1](../../../observe/application-observability/services/service-detection/service-detection-v1.md#web-server-naming-issues "Find out how Dynatrace Service Detection v1 detects and names different types of services.") |
| `DT_TAGS` | Применяет [пользовательские теги](../../../manage/tags-and-metadata/setup/define-tags-based-on-environment-variables.md "Find out how Dynatrace enables you to define tags based on environment variables.") к вашей группе процессов |
| `DT_CUSTOM_PROP` | Применяет [пользовательские метаданные](../../../observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata.md "Configure your own process-related metadata based on the unique needs of your organization or environment.") к вашей группе процессов |
| `DT_CLUSTER_ID` | Если [правила обнаружения групп процессов](../../../observe/infrastructure-observability/process-groups/configuration/pg-detection.md "Ways to customize process-group detection") не подходят для вашего случая использования, используйте эту переменную окружения для **объединения всех процессов с одинаковым значением**. |
| `DT_NODE_ID` | Если [правила обнаружения групп процессов](../../../observe/infrastructure-observability/process-groups/configuration/pg-detection.md "Ways to customize process-group detection") не подходят для вашего случая использования, используйте эту переменную окружения для **разделения экземпляров групп процессов** |
| **Устранение неполадок** |  |
| `DT_LOGSTREAM` | Установите эту переменную со значением `stdout`, чтобы настроить агент на вывод ошибок в консоль. Для просмотра дополнительных логов агента установите уровень логирования с помощью DT\_LOGLEVELCON, как описано ниже. |
| `DT_LOGLEVELCON` | Используйте эту переменную окружения для определения уровня логирования консоли. Допустимые варианты: `NONE`, `INFO`, `WARNING`, `SEVERE` в порядке увеличения уровня логирования. |
| `DT_AGENTACTIVE` | `true` или `false` для включения или отключения OneAgent. |

## Проверка успешности интеграции

После сборки и развёртывания вы должны увидеть ваш сервис Cloud Run в Dynatrace.

### Проверка через обзор сервисов

Проверьте обзор вашего сервиса в Dynatrace для инструментированного приложения.

Сервис появится в Dynatrace после запуска новой собранной версии и хотя бы одного вызова, например, через веб-запрос.

### Проверка через обзор хостов

Вы можете отфильтровать контейнеры в обзоре хостов по **Режиму мониторинга** со значением `Standalone/PaaS`.

## Известные ограничения

* **Отсутствие метрик хоста для Gen1**

  Первое поколение среды выполнения GCR, также называемое Gen1, имеет намеренно повышенные ограничения безопасности. В результате некоторые функции OneAgent не могут работать в этой среде выполнения и недоступны. Например, метрики на странице **Хосты**, такие как `CPU Usage` и `Memory Usage`, недоступны.
* **Экземпляры GCR определяются как хосты**

  Среды выполнения GCR в настоящее время отображаются на странице **Хосты** с правильным определением свойств GCP и ограничения памяти каждого из этих экземпляров среды выполнения (контейнера), а не на странице [**Группы контейнеров**](../../../observe/infrastructure-observability/container-platform-monitoring/container-groups.md "Overview on container groups monitoring"). Метрики контейнеров недоступны.
* **Возможные задержки при запуске**

  Поскольку каждая ревизия Google Cloud Run автоматически масштабируется до количества экземпляров контейнеров, необходимого для обработки входящих запросов, такие холодные запуски могут происходить чаще, чем в других средах, что увеличивает общие задержки при запуске.

## Обновление OneAgent

Каждый раз, когда вы хотите использовать новую версию Dynatrace OneAgent, необходимо выполнить повторную сборку и развёртывание.

Если вы указали версию OneAgent по умолчанию для установки на новых хостах и в приложениях с помощью [настроек обновления OneAgent](../../dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux.md "Learn about the different ways to update OneAgent on Linux."), ваше приложение будет автоматически мониториться определённой версией OneAgent по умолчанию.

## Удаление OneAgent

Для удаления OneAgent из режима мониторинга только приложений удалите ссылки из вашего приложения или Docker-образа и повторно разверните приложение.

## Связанные темы

* [Настройка Dynatrace в Google Cloud](../../google-cloud-platform.md "Monitor Google Cloud with Dynatrace.")
* [Матрица поддержки платформ и возможностей OneAgent](../../technology-support/oneagent-platform-and-capability-support-matrix.md "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
