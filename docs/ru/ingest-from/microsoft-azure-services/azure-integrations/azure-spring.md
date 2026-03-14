---
title: Мониторинг Azure Spring Apps
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring
scraped: 2026-03-06T21:18:17.162329
---

# Мониторинг Azure Spring Apps

# Мониторинг Azure Spring Apps

* Latest Dynatrace
* Практическое руководство
* Чтение: 4 мин
* Опубликовано 16 июля 2021 г.

## Возможности

* Полный мониторинг Java-стека на базе OneAgent
* Интеграция с [Azure Monitor](azure-spring/monitor-azure-spring-apps.md "Мониторинг Azure Spring Apps и просмотр доступных метрик.")
* Автоматическое обнаружение сервисов, работающих в Azure Spring Apps

Поскольку Azure Spring Apps является полностью управляемой платформой хостинга, приложения развёртываются в изолированной среде, которая не предоставляет прямого доступа к базовой операционной системе.

Ниже описано, как интегрировать OneAgent с вашим приложением Azure Spring Apps для мониторинга рабочих нагрузок Spring Apps с помощью Dynatrace.

## Предварительные требования

* Создайте [PaaS-токен](../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях действия.")
* [Установите Azure CLI](https://dt-url.net/cf63rl6)

## Настройка интеграции

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Подготовьте среду в Azure**](azure-spring.md#prepare-env "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Определите значения необходимых переменных окружения**](azure-spring.md#envvar "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Добавьте переменные окружения в ваше приложение**](azure-spring.md#add-variables "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.")

### Шаг 1. Подготовка среды в Azure

1. На портале Azure создайте экземпляр Azure Spring Apps.
2. В новом экземпляре Azure Spring Apps создайте приложение, которое будет отправлять данные в Dynatrace, выполнив приведённую ниже команду.

   Обязательно замените заполнители (`<...>`) на ваши собственные значения.

   ```
   az spring app create --name <your-application-name> --is-public true -s <your-resource-name> -g <your-resource-group-name>
   ```

### Шаг 2. Определение значений необходимых переменных окружения

Для настройки интеграции OneAgent с экземпляром Azure Spring Apps необходимо сконфигурировать три переменные окружения:

* `DT_TENANT`
* `DT_TENANTTOKEN`
* `DT_CONNECTION_POINT`.

Перед началом соберите следующую информацию:

* Ваш [идентификатор среды Dynatrace](../../../discover-dynatrace/get-started/monitoring-environment.md "Понимание и работа со средами мониторинга.")
* Аутентификация

  + **PaaS-токен** аутентифицирует вас как пользователя Dynatrace и необходим для определения токена арендатора.
  + **Токен арендатора** позволяет OneAgent отправлять данные в Dynatrace.
    Дополнительную информацию о токенах см. в разделе [Токены доступа](../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md "Узнайте о концепции токена доступа и его областях действия.").

1. Значение `DT_TENANT` — это ваш [идентификатор среды Dynatrace](../../../discover-dynatrace/get-started/monitoring-environment.md "Понимание и работа со средами мониторинга.").
2. Для определения значений `DT_TENANTTOKEN` и `DT_CONNECTION_POINT` выполните API-запрос к эндпоинту [Deployment API — GET connectivity information for OneAgent](../../../dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info.md "Просмотр информации о подключении OneAgent через Dynatrace API."). Необходимые значения возвращаются в полях `tenantToken` и `communicationEndpoints`.

   Вы можете отправить запрос на URL вашей среды (SaaS или Managed) или на URL Environment ActiveGate.

   * **Dynatrace SaaS**:

     ```
     curl https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Замените:

     + `<your-environment-id>` на ваш [идентификатор среды Dynatrace](../../../discover-dynatrace/get-started/monitoring-environment.md "Понимание и работа со средами мониторинга.")
     + `<your_PaaS_token>` на ваш [PaaS-токен](#prerequisites)
   * **Dynatrace Managed**:

     ```
     curl https://<your-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Замените:

     + `<your-domain>` на домен вашего развёртывания Managed
     + `<your-environment-id>` на ваш [идентификатор среды Dynatrace](../../../discover-dynatrace/get-started/monitoring-environment.md "Понимание и работа со средами мониторинга.")
     + `<your_PaaS_token>` на ваш [PaaS-токен](#prerequisites)
   * **Environment ActiveGate**:

     ```
     curl https://<your-activegate-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Замените:

     + `<your-activegate-domain>` на домен вашего ActiveGate
     + `<your-environment-id>` на ваш [идентификатор среды Dynatrace](../../../discover-dynatrace/get-started/monitoring-environment.md "Понимание и работа со средами мониторинга.")
     + `<your_PaaS_token>` на ваш [PaaS-токен](#prerequisites)

### Шаг 3. Добавление переменных окружения в приложение

После того как вы определили значения переменных окружения, необходимых для интеграции OneAgent, вы можете добавить соответствующие пары ключ/значение в ваше приложение через портал Azure или через Azure CLI. Инструкции для каждого варианта приведены ниже.

В Azure CLI

На портале Azure

Выполните приведённую ниже команду, обязательно заменив заполнители (`<...>`) на ваши собственные значения, определённые на предыдущих шагах.

```
az spring app deploy --name <your-application-name> --jar-path app.jar \



-s <your-resource-name> -g <your-resource-group-name> --env DT_TENANT=<your-environment-ID> \



DT_TENANTTOKEN=<your-tenant-token> DT_CONNECTION_POINT=<your-communication-endpoint>
```

1. Перейдите к вашему экземпляру Azure Spring Apps и выберите группу ресурсов, в которой будет развёрнут Dynatrace.
2. Выберите приложение, для которого Dynatrace должен отправлять данные.
3. Выберите **Конфигурация** и введите следующие пары ключ/значение переменных окружения.

   | Ключ | Значение |
   | --- | --- |
   | `DT_TENANT` | [Ваш идентификатор среды Dynatrace](../../../discover-dynatrace/get-started/monitoring-environment.md "Понимание и работа со средами мониторинга.") |
   | `DT_TENANTTOKEN` | Ваш токен арендатора. Подробнее см. в разделе [Определение значений необходимых переменных окружения](#envvar). |
   | `DT_CONNECTION_POINT` | Ваша конечная точка связи. Подробнее см. в разделе [Определение значений необходимых переменных окружения](#envvar). |
4. [Создайте привязку buildpack](https://dt-url.net/nu036u6) для Dynatrace, используя PaaS-токен (API-токен) и URL API в качестве свойств.

   | Свойство | Значение |
   | --- | --- |
   | `api-url` | [Ваш идентификатор среды Dynatrace](../../../discover-dynatrace/get-started/monitoring-environment.md "Понимание и работа со средами мониторинга.") |
   | `api-token` | [PaaS-токен](#prerequisites) |

Дополнительно вы можете настроить встроенные правила обнаружения групп процессов, установив ещё одну переменную окружения `DT_CLUSTER_ID`. Значением может быть имя группы процессов, которое вы хотите видеть в Dynatrace. Подробнее см. в разделе [Обнаружение групп процессов](../../../observe/infrastructure-observability/process-groups/configuration/pg-detection.md "Способы настройки обнаружения групп процессов").

## Просмотр данных в Dynatrace

После добавления переменных окружения в приложение Dynatrace начинает собирать данные из него. Для просмотра данных вашего приложения Azure Spring Apps перейдите в раздел ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** и выберите ваше приложение.

Пример потока сервисов:

![AppFlow](https://dt-cdn.net/images/1-1721-67868203e3.png)

Пример потребления CPU:

![Diagnostic cpu](https://dt-cdn.net/images/diagnostic-cpu-1565-a403ae7a02.png)

Пример анализа времени ответа:

![Resposetime](https://dt-cdn.net/images/f-1486-bd826153cb.png)

## Обновления OneAgent

Обновления OneAgent выполняются автоматически вместе с JDK.

После обновления OneAgent необходимо перезапустить или повторно развернуть ваши приложения, чтобы они отслеживались новой версией OneAgent. Это связано с тем, что некоторые компоненты OneAgent продолжают работать в процессах, которые отслеживаются Dynatrace.

* До перезапуска эти процессы будут продолжать отслеживаться предыдущей версией OneAgent.
* После перезапуска эти процессы будут отслеживаться последней версией OneAgent.

## Связанные темы

* [Мониторинг Azure Spring Apps](azure-spring/monitor-azure-spring-apps.md "Мониторинг Azure Spring Apps и просмотр доступных метрик.")
* [Матрица поддержки платформ и возможностей OneAgent](../../technology-support/oneagent-platform-and-capability-support-matrix.md "Узнайте, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.")
