---
title: Мониторинг AWS Fargate
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate
scraped: 2026-05-12T11:11:07.901539
---

# Мониторинг AWS Fargate

# Мониторинг AWS Fargate

* Практическое руководство
* Чтение: 1 мин
* Обновлено 14 октября 2025 г.

Чтобы развернуть OneAgent в AWS Fargate, ознакомьтесь с приведёнными ниже инструкциями.

## Предварительные требования

* [Создайте API-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Изучите концепцию токена доступа и его области действия.") в вашей среде Dynatrace и включите следующие разрешения:

  + **Access problem and event feed, metrics, and topology** (API v1)
  + **PaaS integration - Installer download**
* Ознакомьтесь со списком [поддерживаемых приложений и версий](/managed/ingest-from/technology-support "Найдите технические сведения о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").

## Интеграция OneAgent в образ приложения

Существует три способа интеграции OneAgent с приложениями AWS Fargate.

### Автоматическое внедрение EKS

При автоматическом внедрении вы можете управлять обновлениями и жизненным циклом.

Kubernetes версии 1.20+

В AWS Fargate поддерживается только развёртывание `applicationMonitoring` без CSI-драйвера.

Прежде чем приступить к установке, убедитесь, что у вас есть работающий кластер AWS Fargate. Подробнее см. в разделе [Начало работы с AWS Fargate на базе Amazon EKS](https://dt-url.net/zg034ha).

1. Добавьте Fargate profile для определения развёртывания Dynatrace Operator.

   Убедитесь, что он соответствует namespace `dynatrace`, в котором будет развёрнут Dynatrace Operator.
2. Создайте namespace `dynatrace`.

   ```
   kubectl create namespace dynatrace
   ```
3. Установите Dynatrace Operator.

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes.yaml
   ```
4. Создайте secret с API-токеном для аутентификации в кластере Dynatrace.

   Не забудьте заменить `<API_TOKEN>` своим значением.

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<API_TOKEN>"
   ```
5. Скачайте [предварительно настроенный пример файла custom resource DynaKube с GitHub](https://dt-url.net/dynakube-applicationmonitoring).
6. Изучите [доступные параметры](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") и адаптируйте custom resource DynaKube под свои требования.
7. Примените custom resource DynaKube.

   ```
   kubectl apply -f applicationMonitoring.yaml
   ```

### Внедрение на этапе сборки EKS и ECS

При внедрении на этапе сборки вы можете встроить OneAgent в образ контейнера.

Многоэтапная сборка Docker-образов

Классическая интеграция

Для использования этого варианта вам потребуется:

* Docker версии 17.05+
* OneAgent версии 1.155+

1. Войдите в Docker, используя ID вашей среды Dynatrace в качестве имени пользователя и PaaS-токен в качестве пароля.

   ```
   docker login -u <your-environment-id> <your-environment-url>
   ```

* Замените `<your-environment-url>` URL-адресом или IP-адресом вашей среды или ActiveGate.

  + Dynatrace SaaS {your-environment-id}.live.dynatrace.com[1](#fn-1-1-def)
  + Dynatrace Managed {your-domain}/e/{your-environment-id}[1](#fn-1-1-def)

    1

    Если вы используете собственный environment ActiveGate, используйте формат `<ip-address>:9999` или `<hostname>:9999`.
* Добавьте две дополнительные строки кода в образ приложения после последней команды `FROM`:

  ```
  COPY --from=<your-environment-url>/linux/oneagent-codemodules:<technology> / /



  ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
  ```

* Замените `<technology>` кодовым модулем, необходимым для вашего приложения. Допустимые варианты: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `python`, `sdk` и `go`. Можно указать несколько кодовых модулей через дефис (`-`), например `java-go`. Выбор конкретных опций поддержки технологий вместо поддержки всех технологий даёт меньший пакет OneAgent.

Что если мой Docker-образ основан на Alpine Linux?

Dynatrace OneAgent поддерживает окружения на базе Alpine Linux. Используйте следующий синтаксис:

```
COPY --from=<your-activegate>/linux/oneagent-codemodules-musl:<technology> / /



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
```

Допустимые варианты здесь: `all`, `go`, `java`, `apache`, `nginx`, `nodejs` и `python`.

3. Соберите образ вашего приложения.

   Соберите Docker-образ из вашего dockerfile, чтобы использовать его в Kubernetes-окружении:

   ```
   docker build -t yourapp .
   ```

   Вы можете мониторить контейнеры вашего приложения с другой средой Dynatrace. Для этого ознакомьтесь с инструкциями ниже:

   Для OneAgent версии 1.139+, если у вас уже есть образ приложения, в который добавлены кодовые модули OneAgent для определённой среды Dynatrace, вы можете заставить OneAgent отправлять данные в другую среду Dynatrace без пересборки образа приложения.

   Для этого нужно сделать вызов к REST-endpoint вашей второй среды Dynatrace. Не забудьте заменить плейсхолдеры `<your-environment-id>` и `<your-paas-token>`.

   ```
   curl "https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your-paas-token>"
   ```

   В ответ вы получите JSON-объект, содержащий требуемую информацию, которую необходимо передать в виде переменных окружения в контейнер приложения. Убедитесь, что вы установили следующие переменные окружения контейнера приложения:

   * `DT_TENANT`: равно `tenantUUID`
   * `DT_TENANTTOKEN`: равно `tenantToken`
   * `DT_CONNECTION_POINT`: список `communicationEndpoints` через точку с запятой

Чтобы использовать distroless-образы (урезанные версии обычных Docker-образов, содержащие только самое необходимое для запуска приложения), OneAgent должен вызываться в исполняемой форме через инструкцию `CMD`, а не `ENTRYPOINT`.

1. Установите следующие переменные окружения.

   * `DT_API_URL="https://<your-environment-id>.live.dynatrace.com/api"`
   * `DT_API_TOKEN="<your-paas-token>"`
   * `ARCH="<x86|arm>"`
   * `DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"`
   * `DT_HOME="/opt/dynatrace/oneagent"`

   Переменные окружения нужно установить:

   * В вашем текущем Dockerfile, чтобы интегрировать OneAgent и активировать инструментацию вашего приложения.
     Определите переменные с опциональными значениями по умолчанию через инструкции `ARG`.
     В блоке кода ниже приведён шаблон для установки этих переменных окружения.
   * В контейнере runtime injection.

   ```
   ARG DT_API_URL="https://<YourDynatraceServerURL>/e/<your-environment-id>/api"



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

   * Команды выше, использующие `wget` и `unzip`, могут завершиться сбоем, если они не предоставляются базовым образом.
   * Замените `<your-paas-token>` своим PaaS-токеном.
   * `DT_ONEAGENT_OPTIONS`, это flavor (допустимые варианты: `default` или `musl` для Alpine-образов) и технология (кодовый модуль).

     + Синтаксис для `default`: `flavor=default&include=all`.
     + Синтаксис для `musl`: `flavor=musl&include=all`.

   **Что если мой Docker-образ основан на Alpine Linux?**

   Dynatrace OneAgent поддерживает flavor `musl` для окружений на базе Alpine Linux. Допустимые варианты для `flavor=musl`: `all`, `go`, `java`, `apache`, `nginx` и `nodejs`.
2. Соберите образ вашего приложения.

   Соберите Docker-образ из вашего dockerfile, чтобы использовать его в Kubernetes-окружении:

   ```
   docker build -t yourapp .
   ```

   Вы можете мониторить контейнеры вашего приложения с другой средой Dynatrace. Для этого ознакомьтесь с инструкциями ниже:

   Для OneAgent версии 1.139+, если у вас уже есть образ приложения, в который добавлены кодовые модули OneAgent для определённой среды Dynatrace, вы можете заставить OneAgent отправлять данные в другую среду Dynatrace без пересборки образа приложения.

   Для этого нужно сделать вызов к REST-endpoint вашей второй среды Dynatrace. Не забудьте заменить плейсхолдеры `<your-environment-id>` и `<your-paas-token>`.

   ```
   curl "https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your-paas-token>"
   ```

   В ответ вы получите JSON-объект, содержащий требуемую информацию, которую необходимо передать в виде переменных окружения в контейнер приложения. Убедитесь, что вы установили следующие переменные окружения контейнера приложения:

   * `DT_TENANT`: равно `tenantUUID`
   * `DT_TENANTTOKEN`: равно `tenantToken`
   * `DT_CONNECTION_POINT`: список `communicationEndpoints` через точку с запятой

### Runtime injection ECS

При runtime injection OneAgent загружается при запуске контейнера. Чтобы установить Dynatrace OneAgent во время выполнения, нужно развернуть приложение через задачу с двумя определениями контейнеров. Один используется для загрузки и распаковки OneAgent в общий том, другой, это ваш контейнер приложения, который должен монтировать тот же том.

Для runtime injection выполните следующие шаги.

1. Перейдите в **Fargate Task Definition** > **Create New Task Definition** и выберите **AWS Fargate** в разделе **Infrastructure requirements > Launch type**.
2. Задайте имя задачи, при необходимости установите роли и размеры, затем прокрутите вниз до **Storage - optional** > **Volumes** и нажмите **Add volume**. Добавьте том типа `Bind Mount` с именем `oneagent`.

   Том необходимо создать **до** создания определений контейнеров, чтобы установить общий том в каждом контейнере.
3. Прокрутите до низа **Container - 1** и нажмите **Add container**.

   * В подразделе **Container details**:

     + Добавьте контейнер с именем `install-oneagent`
     + Установите образ в Alpine версии 3.8+ ("alpine:3")
     + выберите **No** в поле **Essential container**
   * В подразделе **Resource allocation limits - conditional**:

     + Выберите лимиты CPU и памяти.

   Существует два типа лимитов памяти: soft и hard. ECS требует, чтобы вы определили лимит хотя бы для одного типа памяти. Мы рекомендуем использовать настройку по умолчанию (soft-лимит 128 MiB), так как она менее ограничительна, но вы можете изменить её при необходимости.
4. В подразделе **Docker configuration - optional**:

   * В поле **Entry point** введите `/bin/sh,-c`.
   * В поле **Command** введите `ARCHIVE=$(mktemp) && wget -O $ARCHIVE "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?arch=$ARCH&Api-Token=$DT_PAAS_TOKEN&$DT_ONEAGENT_OPTIONS" && unzip -o -d /opt/dynatrace/oneagent $ARCHIVE && rm -f $ARCHIVE`.
5. В подразделе **Environment variables** определите:

   * `DT_API_URL`, это API URL вашей среды Dynatrace.

     + Для SaaS: `https://<your-environment-id>.live.dynatrace.com/api`
     + Для Managed: `https://<cluster>/e/<your-environment-id>/api`
     + Для ActiveGate: `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api`.
   * `DT_ONEAGENT_OPTIONS`, это flavor (допустимые варианты: `default` или `musl` для Alpine-образов) и технология (кодовый модуль).

     + Синтаксис для `default`: `flavor=default&include=all`.
     + Синтаксис для `musl`: `flavor=musl&include=all`.
   * `DT_PAAS_TOKEN`, это ваш PaaS-токен для загрузки кодовых модулей OneAgent.
   * `ARCH`, архитектура CPU.

     + для x86\_64: `x86`
     + для arm64: `arm`

       Автоматическое определение архитектуры

       Используйте следующий скрипт для определения архитектуры CPU на Linux.

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
10. Нажмите **Create** внизу экрана, чтобы создать определение задачи и развернуть его в ECS-кластере.

Проверьте вкладку **Logs**

* Для контейнера `install-oneagent` вы увидите, как ZIP-файл кодовых модулей загружается через wget и распаковывается.
* Для контейнера рабочей нагрузки вашего приложения вы увидите, как кодовый модуль загружается процессом.

В Dynatrace контейнер рабочей нагрузки вашего Fargate-приложения отобразится в разделе **Hosts**. Инструментированный процесс отобразится в **Processes** как типичный Docker-контейнер.

![Fargate](https://dt-cdn.net/images/fargate-1165-0748c0cf29.png)

Fargate

Подход с runtime требует Fargate версии 1.3+. Для более ранних версий выберите подход build-time.

### Настройка сетевых зон Опционально

Сетевые зоны можно настроить через переменную окружения:

* `DT_NETWORK_ZONE`: равно `your.network.zone`

Подробнее см. в разделе [сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").

## Потребление ресурсов мониторинга

Для AWS Fargate потребление ресурсов мониторинга рассчитывается на основе host units. Чтобы узнать, как рассчитываются host units для мониторинга приложений и инфраструктуры Dynatrace, см. [Мониторинг приложений и инфраструктуры (Host Units)](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Узнайте, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе host units.").

## Устранение неполадок

* [Проблемы интеграции OneAgent в образ приложения](https://dt-url.net/yu23mli)

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на различных платформах.")