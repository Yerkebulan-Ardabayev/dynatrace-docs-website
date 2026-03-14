---
title: Мониторинг AWS Fargate
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate
scraped: 2026-03-06T21:18:01.703557
---

# Мониторинг AWS Fargate


* Classic
* Практическое руководство
* 1 мин. чтения
* Обновлено 14 октября 2025 г.

Для развёртывания OneAgent на AWS Fargate ознакомьтесь с инструкциями ниже.

## Предварительные требования

* [Создайте API-токен](../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Узнайте о концепции токена доступа и его областях.") в вашей среде Dynatrace и включите следующие разрешения:

  + **Access problem and event feed, metrics, and topology** (API v1)
  + **PaaS integration - Installer download**
* Ознакомьтесь со списком [поддерживаемых приложений и версий](../../technology-support.md "Техническая информация о поддержке Dynatrace конкретных платформ и фреймворков разработки.").

## Интеграция OneAgent в образ вашего приложения

Существует три способа интеграции OneAgent с приложениями AWS Fargate.

### Автоматическое внедрение EKS

С автоматическим внедрением вы можете управлять обновлениями и жизненным циклом.

Kubernetes версии 1.20+

На AWS Fargate поддерживается только развёртывание `applicationMonitoring` без драйвера CSI.

Перед началом установки убедитесь, что у вас есть работающий кластер AWS Fargate. Подробнее см. [Начало работы с AWS Fargate с использованием Amazon EKS](https://dt-url.net/zg034ha).

1. Добавьте профиль Fargate для определения развёртывания Dynatrace Operator.

   Убедитесь, что он соответствует пространству имён `dynatrace`, где будет развёрнут Dynatrace Operator.
2. Создайте пространство имён `dynatrace`.

   ```
   kubectl create namespace dynatrace
   ```
3. Установите Dynatrace Operator.

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/kubernetes.yaml
   ```
4. Создайте секрет, содержащий API-токен для аутентификации в кластере Dynatrace.

   Обязательно замените `<API_TOKEN>` на ваше значение.

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<API_TOKEN>"
   ```
5. Скачайте [предварительно настроенный пример пользовательского ресурса DynaKube с GitHub](https://dt-url.net/dynakube-applicationmonitoring).
6. Ознакомьтесь с [доступными параметрами](../../setup-on-k8s/reference/dynakube-parameters.md "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") и адаптируйте пользовательский ресурс DynaKube в соответствии с вашими требованиями.
7. Примените пользовательский ресурс DynaKube.

   ```
   kubectl apply -f applicationMonitoring.yaml
   ```

### Внедрение на этапе сборки EKS и ECS

С внедрением на этапе сборки вы можете встроить OneAgent в образ контейнера.

Многоэтапная сборка образов Docker

Классическая интеграция

Для использования этого варианта вам потребуется:

* Docker версии 17.05+
* OneAgent версии 1.155+

1. Войдите в Docker, используя идентификатор среды Dynatrace в качестве имени пользователя и PaaS-токен в качестве пароля.

   ```
   docker login -u <your-environment-id> <your-environment-url>
   ```

* Замените `<your-environment-url>` на URL или IP-адрес вашей среды или вашего ActiveGate.

  + Dynatrace SaaS {your-environment-id}.live.dynatrace.com[1](#fn-1-1-def)
  + Dynatrace Managed {your-domain}/e/{your-environment-id}[1](#fn-1-1-def)

    1

    Если вы используете собственный ActiveGate среды, используйте формат `<ip-address>:9999` или `<hostname>:9999`.
* Добавьте две дополнительные строки кода в образ приложения после последней команды `FROM`:

  ```
  COPY --from=<your-environment-url>/linux/oneagent-codemodules:<technology> / /


  ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
  ```

* Замените `<technology>` на модуль кода, необходимый для вашего приложения. Допустимые значения: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `python`, `sdk` и `go`. Вы можете указать несколько модулей кода, разделённых дефисом (`-`), например `java-go`. Указание конкретных технологий вместо поддержки всех приводит к уменьшению размера пакета OneAgent.

Что если мой Docker-образ основан на Alpine Linux?

Dynatrace OneAgent поддерживает среды на базе Alpine Linux. Используйте следующий синтаксис:

```
COPY --from=<your-activegate>/linux/oneagent-codemodules-musl:<technology> / /


ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
```

Допустимые значения: `all`, `go`, `java`, `apache`, `nginx`, `nodejs` и `python`.

3. Соберите образ приложения.

   Соберите Docker-образ из вашего Dockerfile для использования в среде Kubernetes:

   ```
   docker build -t yourapp .
   ```

   Вы можете отслеживать контейнеры приложений с помощью другой среды Dynatrace. Для этого прочитайте инструкции ниже:

   Для OneAgent версии 1.139+, если у вас уже есть образ приложения с добавленными модулями кода OneAgent для определённой среды Dynatrace, вы можете настроить OneAgent на отправку данных в другую среду Dynatrace без пересборки образа приложения.

   Для этого нужно выполнить вызов REST-эндпоинта вашей второй среды Dynatrace. Обязательно адаптируйте соответствующие заполнители `<your-environment-id>` и `<your-paas-token>`.

   ```
   curl "https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your-paas-token>"
   ```

   В ответ вы получите JSON-объект с необходимой информацией, которую нужно передать как переменные окружения контейнеру приложения. Убедитесь, что переменные окружения контейнера приложения установлены следующим образом:

   * `DT_TENANT`: соответствует `tenantUUID`
   * `DT_TENANTTOKEN`: соответствует `tenantToken`
   * `DT_CONNECTION_POINT`: список `communicationEndpoints`, разделённых точкой с запятой

Для использования образов distroless (сокращённых версий обычных Docker-образов, содержащих только необходимое для запуска приложения) OneAgent необходимо вызывать в исполняемой форме с помощью инструкции `CMD` вместо `ENTRYPOINT`.

1. Установите следующие переменные окружения.

   * `DT_API_URL="https://<your-environment-id>.live.dynatrace.com/api"`
   * `DT_API_TOKEN="<your-paas-token>"`
   * `ARCH="<x86|arm>"`
   * `DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"`
   * `DT_HOME="/opt/dynatrace/oneagent"`

   Переменные окружения необходимо установить:

   * В вашем текущем Dockerfile для интеграции OneAgent и активации инструментирования приложения.
     Определите переменные с необязательными значениями по умолчанию с помощью инструкций `ARG`.
     Блок кода ниже предоставляет шаблон для установки этих переменных окружения.
   * В контейнере внедрения во время выполнения.

   ```
   ARG DT_API_URL="https://<your-environment-id>.live.dynatrace.com/api"


   ARG DT_API_TOKEN="<your-paas-token>"


   ARG ARCH="<x86|arm>"


   ARG DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"


   ENV DT_HOME="/opt/dynatrace/oneagent"


   RUN mkdir -p "$DT_HOME" && \


   wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?arch=$ARCH&Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \


   unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \


   rm "$DT_HOME/oneagent.zip"


   ENTRYPOINT [ "/opt/dynatrace/oneagent/dynatrace-agent64.sh" ]


   CMD [ "executable", "param1", "param2" ] # команда вашего приложения, например, Java
   ```

   * Команды выше, использующие `wget` и `unzip`, могут завершиться ошибкой, если они не предоставляются базовым образом.
   * Замените `<your-paas-token>` на ваш PaaS-токен.
   * `DT_ONEAGENT_OPTIONS` — это вариант (допустимые значения: `default` или `musl` для образов Alpine) и технология (модуль кода).

     + Синтаксис для `default`: `flavor=default&include=all`.
     + Синтаксис для `musl`: `flavor=musl&include=all`.

   **Что если мой Docker-образ основан на Alpine Linux?**

   Dynatrace OneAgent поддерживает вариант `musl` для сред на базе Alpine Linux. Допустимые значения для `flavor=musl`: `all`, `go`, `java`, `apache`, `nginx` и `nodejs`.
2. Соберите образ приложения.

   Соберите Docker-образ из вашего Dockerfile для использования в среде Kubernetes:

   ```
   docker build -t yourapp .
   ```

   Вы можете отслеживать контейнеры приложений с помощью другой среды Dynatrace. Для этого прочитайте инструкции ниже:

   Для OneAgent версии 1.139+, если у вас уже есть образ приложения с добавленными модулями кода OneAgent для определённой среды Dynatrace, вы можете настроить OneAgent на отправку данных в другую среду Dynatrace без пересборки образа приложения.

   Для этого нужно выполнить вызов REST-эндпоинта вашей второй среды Dynatrace. Обязательно адаптируйте соответствующие заполнители `<your-environment-id>` и `<your-paas-token>`.

   ```
   curl "https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your-paas-token>"
   ```

   В ответ вы получите JSON-объект с необходимой информацией, которую нужно передать как переменные окружения контейнеру приложения. Убедитесь, что переменные окружения контейнера приложения установлены следующим образом:

   * `DT_TENANT`: соответствует `tenantUUID`
   * `DT_TENANTTOKEN`: соответствует `tenantToken`
   * `DT_CONNECTION_POINT`: список `communicationEndpoints`, разделённых точкой с запятой

### Внедрение во время выполнения ECS

С внедрением во время выполнения вы можете загрузить OneAgent при старте контейнера. Для установки Dynatrace OneAgent во время выполнения необходимо развернуть приложение с использованием задачи с двумя определениями контейнеров. Один предназначен для загрузки и распаковки OneAgent в общий том, другой — это контейнер вашего приложения, который должен монтировать тот же том.

Для внедрения во время выполнения выполните следующие шаги.

1. Перейдите в **Fargate Task Definition** > **Create New Task Definition** и выберите **AWS Fargate** в разделе **Infrastructure requirements > Launch type**.
2. Назовите задачу, при необходимости настройте роли и размеры, затем прокрутите вниз до **Storage - optional** > **Volumes** и выберите **Add volume**. Добавьте том типа `Bind Mount` с именем `oneagent`.

   Вы должны создать том **до** создания определений контейнеров, чтобы установить общий том в каждом контейнере.
3. Прокрутите до конца **Container - 1** и выберите **Add container**.

   * В подразделе **Container details**:

     + Добавьте контейнер с именем `install-oneagent`
     + Установите образ Alpine версии 3.8+ ("alpine:3")
     + Выберите **No** в поле **Essential container**
   * В подразделе **Resource allocation limits - conditional**:

     + Выберите лимиты CPU и памяти.

   Существует два типа лимитов памяти: мягкий и жёсткий. ECS требует определения лимита хотя бы для одного типа памяти. Рекомендуется использовать настройку по умолчанию (мягкий лимит 128 MiB), так как она менее ограничительна, но вы можете настроить её по необходимости.
4. В подразделе **Docker configuration - optional**:

   * В поле **Entry point** введите `/bin/sh,-c`.
   * В поле **Command** введите `ARCHIVE=$(mktemp) && wget -O $ARCHIVE "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?arch=$ARCH&Api-Token=$DT_PAAS_TOKEN&$DT_ONEAGENT_OPTIONS" && unzip -o -d /opt/dynatrace/oneagent $ARCHIVE && rm -f $ARCHIVE`.
5. В подразделе **Environment variables** определите:

   * `DT_API_URL` — URL API вашей среды Dynatrace.

     + Для SaaS: `https://<your-environment-id>.live.dynatrace.com/api`
     + Для Managed: `https://<cluster>/e/<your-environment-id>/api`
     + Для ActiveGate: `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api`.
   * `DT_ONEAGENT_OPTIONS` — вариант (допустимые значения: `default` или `musl` для образов Alpine) и технология (модуль кода).

     + Синтаксис для `default`: `flavor=default&include=all`.
     + Синтаксис для `musl`: `flavor=musl&include=all`.
   * `DT_PAAS_TOKEN` — ваш PaaS-токен для загрузки модулей кода OneAgent.
   * `ARCH` — процессорная архитектура.

     + для x86\_64: `x86`
     + для arm64: `arm`

       Автоматическое определение архитектуры

       Используйте следующий скрипт для определения процессорной архитектуры в Linux.

       ```
       ARCH=$(uname -p);


       export ARCH;


       if [ "$ARCH" = "arm" ] || [ "$ARCH" = "arm64" ] || [ "$ARCH" = "aarch64" ]; then


       export ARCH="arm";


       else


       export ARCH="x86";


       fi
       ```
6. Снова выберите **Add container**, на этот раз для определения вашего приложения, и заполните поля в подразделе **Standard** в соответствии с требованиями вашего приложения.
7. Прокрутите до **Environment** и в **Environment variable** определите `LD_PRELOAD` со значением `/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so`.
8. Прокрутите до **Startup Dependency Ordering** и введите имя контейнера `install-oneagent` и условие `Complete`.
9. Прокрутите до раздела **Storage - optional**.

   * Создайте новый том и назовите его `oneagent`
   * Создайте точку монтирования:

     + Выберите **Add mount point**
     + Выберите `install-oneagent` в поле **Container**
     + Выберите `oneagent` в поле **Source volume**
     + Установите `/opt/dynatrace/oneagent` в **Container path**
10. Выберите **Create** внизу экрана, чтобы создать определение задачи и развернуть его на вашем кластере ECS.

Проверьте вкладку **Logs**

* Для контейнера `install-oneagent` вы увидите, как ZIP-файл модулей кода загружается wget и распаковывается.
* Для контейнера рабочей нагрузки вашего приложения вы увидите, как модуль кода загружается процессом.

В Dynatrace контейнер рабочей нагрузки Fargate вашего приложения будет отображаться в разделе **Hosts**. Инструментированный процесс будет отображаться в **Processes** как типичный Docker-контейнер.

![Fargate](https://dt-cdn.net/images/fargate-1165-0748c0cf29.png)

Подход с внедрением во время выполнения требует Fargate версии 1.3+. Для более ранних версий выберите подход с внедрением на этапе сборки.

### Настройка сетевых зон (необязательно)

Вы можете настроить сетевые зоны как переменную окружения:

* `DT_NETWORK_ZONE`: равно `your.network.zone`

Подробнее см. [сетевые зоны](../../../manage/network-zones.md "Узнайте, как работают сетевые зоны в Dynatrace.").

## Потребление мониторинга

Для AWS Fargate потребление мониторинга основано на единицах хостов. Чтобы узнать, как единицы хостов рассчитываются для мониторинга приложений и инфраструктуры Dynatrace, см. [Мониторинг приложений и инфраструктуры (Host Units)](../../../license/monitoring-consumption-classic/application-and-infrastructure-monitoring.md "Узнайте, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе единиц хостов.").

## Устранение неполадок

* [Проблемы интеграции OneAgent в образ приложения](https://dt-url.net/yu23mli)

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](../../technology-support/oneagent-platform-and-capability-support-matrix.md "Узнайте, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.")