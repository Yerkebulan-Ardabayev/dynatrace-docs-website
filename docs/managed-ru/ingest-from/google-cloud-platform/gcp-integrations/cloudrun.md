---
title: Мониторинг Google Cloud Run (управляемый)
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun
scraped: 2026-05-12T11:24:00.043583
---

# Мониторинг Google Cloud Run (управляемый)

# Мониторинг Google Cloud Run (управляемый)

* Практическое руководство
* Чтение: 11 мин
* Обновлено 22 апреля 2026 г.

Google [Cloud Run](https://cloud.google.com/run) managed, это вычислительная платформа для запуска контейнеров в бессерверной среде. Для мониторинга сервисов, работающих на Google Cloud Run managed, с помощью Dynatrace необходимо интегрировать OneAgent в контейнерное приложение.

Поддержка Cloud Run managed в средах выполнения [первого и второго поколения](https://cloud.google.com/run/docs/about-execution-environments) в настоящее время ограничена **Java** и **Node.js**.

## Интеграция Dynatrace в контейнеры

Существует несколько способов сборки и развёртывания контейнеров в Cloud Run, например с помощью [Cloud Build](https://cloud.google.com/build).

Хотя инструкции по интеграции Dynatrace могут отличаться в зависимости от используемого технологического стека, сама интеграция Dynatrace следует одному подходу:

1. Добавьте необходимые бинарные файлы OneAgent в образ контейнера (например, загрузив через REST API или скопировав из слоя образа OneAgent).
2. Настройте OneAgent с необходимыми параметрами подключения и дополнительными параметрами, такими как пользовательские теги.
3. Включите инъекцию процесса для автоматической инструментации рабочих нагрузок.

### Предварительные требования

Перед началом работы выполните следующие шаги:

* Получите **токен доступа** для загрузки Dynatrace OneAgent с областью `InstallerDownload`. Подробности о токенах доступа см. в разделе [Dynatrace API - Токены и аутентификация](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

  В следующих процедурах замените `<DT_TOKEN>` на фактический токен доступа.
* Получите **идентификатор среды**. Подробности см. в разделе [Что такое среда мониторинга?](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте о средах мониторинга и принципах работы с ними.").

  В следующих процедурах замените `<DT_ENV_ID>` на фактический идентификатор среды.
* Получите эндпоинт Dynatrace API, заданный через [URL среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте о средах мониторинга и принципах работы с ними.") или через [адрес ActiveGate](/managed/ingest-from/dynatrace-activegate "Ознакомьтесь с основными концепциями ActiveGate.").

  В следующих процедурах замените `<DT_ENV_FQDN>` на фактический эндпоинт Dynatrace API.
* Установите [gcloud CLI](https://cloud.google.com/sdk/docs/install)

После выполнения указанных предварительных требований следуйте одной из приведённых ниже процедур (выберите вкладку) для интеграции Dynatrace в контейнеры.

Cloud Build с cloudbuild.yaml

Cloud Build без cloudbuild.yaml

Jib

### Интеграция при сборке через `cloudbuild.yaml`

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Добавить установщик OneAgent**](/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun#add-oneagent-installer-option-1 "Мониторинг Java-приложения, развёрнутого на Google Cloud Run managed.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настроить Cloud Build**](/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun#configure-cloud-build-option-1 "Мониторинг Java-приложения, развёрнутого на Google Cloud Run managed.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Собрать и развернуть**](/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun#build-and-deploy-option-1 "Мониторинг Java-приложения, развёрнутого на Google Cloud Run managed.")

#### Шаг 1 Добавление установщика OneAgent в Docker-образ

Требуется Docker версии 17.05+

Откройте Dockerfile и добавьте следующие строки в образ приложения **после** последнего `FROM` и **перед** точкой входа контейнера.

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

Обязательно замените заполнители фактическими значениями.

* `<DT_ENV_FQDN>`: фактический эндпоинт Dynatrace API, как описано в разделе [Предварительные требования](#prerequisites).
* `<DT_TOKEN>`: фактический токен, как описано в разделе [Предварительные требования](#prerequisites).
* `<DT_TECHNOLOGY>`: артефакт OneAgent, специфичный для технологического стека образа: `java` или `nodejs`.
* `<DT_FLAVOR>` Для образов на основе Alpine Linux выбирайте `musl`, иначе `default`.

Команды `wget` и `unzip` могут завершиться ошибкой, если базовый образ их не предоставляет.

Пример

Пример Dockerfile от Google из руководства по началу работы с Google Cloud Run на Java, адаптированный с учётом приведённых выше инструкций.

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

#### Шаг 2 Настройка файла конфигурации Google Cloud Build

Откройте файл [cloudbuild.yaml](https://cloud.google.com/build/docs/deploying-builds/deploy-cloud-run#continuous_deployment) и добавьте следующие переменные среды и bash-команды в шаг сборки:

```
# Build the container image



- name: 'gcr.io/cloud-builders/docker'



args: ['build', '-t', 'gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>', '.']



# Push the container image to Container Registry



- name: 'gcr.io/cloud-builders/docker'



args: ['push', 'gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>']
```

Добавьте следующие строки в раздел args шага развёртывания:

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

Обязательно замените заполнители фактическими значениями.

* `<GCP_PROJECT_ID>`: имя [проекта Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects).
* `<YOUR_IMAGE_NAME_AND_TAG>`: имя и тег собираемого образа.
* `<ENVIRONMENT>`: используемая среда выполнения. Допустимые значения: `gen1` для первого поколения и `gen2` для второго.

Переменную среды `DT_TAGS` можно изменить на другое значение при необходимости.

#### Шаг 3 Сборка и развёртывание сервиса Cloud Run

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

Обязательно замените заполнители фактическими значениями.

* `<SAMPLE_NAME>`: имя сервиса Cloud Run.
* `<GCP_PROJECT_ID>`: имя [проекта Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects).
* `<YOUR_IMAGE_NAME_AND_TAG>`: имя и тег собираемого образа.

### Интеграция при сборке без `cloudbuild.yaml`

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Добавить установщик OneAgent**](/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun#add-oneagent-installer-option-2 "Мониторинг Java-приложения, развёрнутого на Google Cloud Run managed.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Собрать и развернуть**](/managed/ingest-from/google-cloud-platform/gcp-integrations/cloudrun#build-and-deploy-option-2 "Мониторинг Java-приложения, развёрнутого на Google Cloud Run managed.")

#### Шаг 1 Добавление установщика OneAgent в Docker-образ

Требуется Docker версии 17.05+

Откройте Dockerfile и добавьте следующий пример в образ приложения **после** последнего `FROM`.

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

Обязательно замените заполнители фактическими значениями.

* `<DT_ENV_FQDN>`: фактический эндпоинт Dynatrace API, как описано в разделе [Предварительные требования](#prerequisites).
* `<DT_TOKEN>`: фактический токен, как описано в разделе [Предварительные требования](#prerequisites).

* Поддержка технологии задаётся через параметры `include`. Для сред на основе Alpine Linux используйте `flavor=musl&include=java`.
* Команды `wget` и `unzip` могут завершиться ошибкой, если базовый образ их не предоставляет.

Пример

Это пример Dockerfile от Google из руководства по началу работы с Google Cloud Run на Java, адаптированный с учётом приведённых выше инструкций.

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

#### Шаг 2 Сборка и развёртывание сервиса Cloud Run

Чтобы собрать сервис Cloud Run, отредактируйте и выполните следующую команду в директории проекта:

```
gcloud builds submit --region=<GCP_REGION> --tag gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>
```

Чтобы развернуть сервис Cloud Run, отредактируйте и выполните следующую команду:

```
gcloud run deploy <YOUR_SERVICE_NAME> --image gcr.io/<GCP_PROJECT_ID>/<YOUR_IMAGE_NAME_AND_TAG>
```

Обязательно замените заполнители фактическими значениями.

* `<GCP_REGION>`: название [региона Google Cloud](https://cloud.google.com/compute/docs/regions-zones) для развёртывания.
* `<GCP_PROJECT_ID>`: имя [проекта Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects).
* `<YOUR_IMAGE_NAME_AND_TAG>`: имя и тег собираемого образа.
* `<YOUR_SERVICE_NAME>`: имя сервиса, которое будет отображаться в Dynatrace.

### Интеграция с помощью инструмента Jib

Инструмент [Jib](https://github.com/GoogleContainerTools/jib) от Google собирает оптимизированные Docker- и OCI-образы для Java-приложений без Docker daemon и без необходимости глубокого знания рекомендаций по работе с Docker. Он доступен как плагин для Maven и Gradle, а также как Java-библиотека.

В репозитории Jib на GitHub находится [пример интеграции для агента Google StackDriver Java](https://github.com/GoogleContainerTools/jib/blob/master/examples/java-agent/build.gradle), который следует тому же шаблону, что и интеграция Dynatrace (загрузка, настройка и внедрение). Этот шаблон можно адаптировать для интеграции Dynatrace с помощью jib.

## Дополнительная настройка

Для настройки, например, параметров диагностики или расширенных сетевых параметров, можно использовать дополнительные переменные среды.

### Сеть

| Имя | Описание |
| --- | --- |
| `DT_NETWORK_ZONE` | Задаёт использование сетевой зоны. Подробности см. в разделе [Сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace."). |
| `DT_PROXY` | При использовании прокси передавайте учётные данные прокси через эту переменную среды. Подробности см. в разделе [Настройка OneAgent на контейнерах для мониторинга только приложений](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Установка, обновление и удаление OneAgent на контейнерах для мониторинга только приложений.") |

### Дополнительные метаданные для группировки процессов и обнаружения сервисов

| Имя | Описание |
| --- | --- |
| `DT_LOCALTOVIRTUALHOSTNAME` | Несколько контейнеров иногда обнаруживаются как один экземпляр (localhost), что приводит к проблемам, например при обнаружении сервисов или оповещениях о доступности. Используйте эту переменную среды для задания уникального имени экземпляра контейнера. Подробности см. в разделе [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1#adjusting-service-detection "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов.") |
| `DT_APPLICATIONID` | Некоторые технологии не предоставляют уникальных имён приложений. В таких случаях используйте эту переменную среды для задания уникального имени. Подробности см. в разделе [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1#web-server-naming-issues "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов.") |
| `DT_TAGS` | Применяет [пользовательские теги](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Узнайте, как Dynatrace позволяет задавать теги на основе переменных среды.") к группе процессов |
| `DT_CUSTOM_PROP` | Применяет [пользовательские метаданные](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Настройте собственные метаданные, связанные с процессами, в соответствии с потребностями вашей организации или среды.") к группе процессов |
| `DT_CLUSTER_ID` | Если [правила обнаружения группы процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Способы настройки обнаружения группы процессов") не подходят для вашего сценария, используйте эту переменную среды для **группировки всех процессов с одинаковым значением**. |
| `DT_NODE_ID` | Если [правила обнаружения группы процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Способы настройки обнаружения группы процессов") не подходят для вашего сценария, используйте эту переменную среды для **разделения экземпляров группы процессов** |

### Устранение неполадок

| Имя | Описание |
| --- | --- |
| `DT_LOGSTREAM` | Установите значение `stdout`, чтобы агент записывал ошибки в консоль. Для просмотра дополнительных логов агента задайте уровень логирования с помощью DT\_LOGLEVELCON, как описано ниже. |
| `DT_LOGLEVELCON` | Используйте эту переменную среды для задания уровня логирования в консоль. Допустимые значения для повышения уровня логирования: `NONE`, `INFO`, `WARNING`, `SEVERE`. |

### Переменные для .NET

Этот раздел содержит переменные, актуальные только для **сред .NET**.

| Параметр | Описание |
| --- | --- |
| `DT_AGENTACTIVE` | Переменная для настройки мониторинга OneAgent приложений .NET Framework и .NET Core. Мониторинг .NET OneAgent активен по умолчанию (`true`). Чтобы деактивировать его, установите `DT_AGENTACTIVE` в `false`. При настройке мониторинга .NET через переменные среды профилировщика .NET необходимо установить `DT_AGENTACTIVE` в `true` для его активации. |

## Проверка успешности интеграции

После сборки и развёртывания сервис Cloud Run начнёт отображаться в Dynatrace.

### Проверка через обзор сервисов

Проверьте обзор сервиса в Dynatrace для инструментированного приложения.

Сервис появится в Dynatrace после запуска новой сборки и хотя бы одного обращения к нему, например, через веб-запрос.

### Проверка через обзор хостов

В обзоре хостов можно фильтровать контейнеры по **Monitoring Mode** со значением `Standalone/PaaS`.

## Известные ограничения

* **Нет метрик хоста для Gen1**

  Среда выполнения GCR первого поколения (Gen1) имеет намеренно повышенные ограничения безопасности. В результате некоторые функции OneAgent недоступны в этой среде выполнения. Например, недоступны метрики на странице **Hosts**, такие как `CPU Usage` и `Memory Usage`.
* **Экземпляры GCR отображаются как хосты**

  Среды выполнения GCR в настоящее время отображаются на странице **Hosts** с правильным определением свойств GCP и лимита памяти каждого из этих экземпляров среды выполнения (контейнера), а не на странице [**Container groups**](/managed/observe/infrastructure-observability/container-platform-monitoring/container-groups "Обзор мониторинга групп контейнеров"). Метрики контейнеров недоступны.
* **Возможные накладные расходы при запуске**

  Поскольку каждая редакция Google Cloud Run автоматически масштабируется до необходимого количества экземпляров контейнеров для обработки входящих запросов, холодные запуски могут происходить чаще, чем в других средах, увеличивая накладные расходы при запуске.

## Обновление OneAgent

Для использования новой версии Dynatrace OneAgent необходимо пересобрать и повторно развернуть приложение.

Если задана версия установки OneAgent по умолчанию для новых хостов и приложений с помощью [параметров обновления OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Узнайте о различных способах обновления OneAgent на Linux."), приложение будет автоматически отслеживаться указанной версией OneAgent по умолчанию.

## Удаление OneAgent

Для удаления OneAgent из режима мониторинга только приложений удалите ссылки из приложения или Docker-образа и повторно разверните приложение.

## Связанные темы

* [Настройка Dynatrace в Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживает OneAgent на различных операционных системах и платформах.")