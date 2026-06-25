---
title: Мониторинг Azure Spring Apps
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring
scraped: 2026-05-12T11:23:57.070411
---

# Мониторинг Azure Spring Apps

# Мониторинг Azure Spring Apps

* Практическое руководство
* Чтение: 4 мин
* Опубликовано 16 июля 2021 г.

## Возможности

* Мониторинг полного стека Java на базе OneAgent
* Интеграция с [Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps "Мониторинг Azure Spring Apps и просмотр доступных метрик.")
* Автоматическое обнаружение сервисов, работающих в Azure Spring Apps

Azure Spring Apps, являясь полностью управляемой платформой хостинга, разворачивает приложения в изолированной среде, которая не допускает прямого доступа к базовой операционной системе.

Ниже описано, как интегрировать OneAgent с приложением Azure Spring Apps для мониторинга рабочих нагрузок Spring Apps с помощью Dynatrace.

## Предварительные требования

* Создайте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его области.")
* [Установите Azure CLI](https://dt-url.net/cf63rl6)

## Настройка интеграции

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Подготовьте окружение в Azure**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#prepare-env "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Определите значения необходимых переменных окружения**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#envvar "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Добавьте переменные окружения в приложение**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#add-variables "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.")

### Шаг 1. Подготовьте окружение в Azure

1. В Azure Portal создайте экземпляр Azure Spring Apps.
2. В новом экземпляре Azure Spring Apps создайте приложение, данные которого нужно передавать в Dynatrace, выполнив приведённую ниже команду.

   Обязательно замените заполнители (`<...>`) собственными значениями.

   ```
   az spring app create --name <your-application-name> --is-public true -s <your-resource-name> -g <your-resource-group-name>
   ```

### Шаг 2. Определите значения необходимых переменных окружения

Чтобы настроить интеграцию OneAgent с экземпляром Azure Spring Apps, необходимо задать три переменные окружения:

* `DT_TENANT`
* `DT_TENANTTOKEN`
* `DT_CONNECTION_POINT`.

Прежде чем начать, соберите следующие сведения:

* [Идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "Общие сведения о мониторинговых окружениях и работа с ними.")
* Аутентификация

  + **PaaS token** аутентифицирует вас как пользователя Dynatrace и необходим для определения tenant token.
  + **Tenant token** позволяет OneAgent передавать данные в Dynatrace.
    Подробнее о токенах см. в разделе [Токены доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Изучите концепцию токена доступа и его области.").

1. Значение `DT_TENANT` совпадает с [идентификатором окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "Общие сведения о мониторинговых окружениях и работа с ними.").
2. Чтобы определить значения `DT_TENANTTOKEN` и `DT_CONNECTION_POINT`, выполните API-запрос к эндпоинту [Deployment API - GET connectivity information for OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "Просмотр сведений о подключении OneAgent через Dynatrace API."). Нужные значения возвращаются как `tenantToken` и `communicationEndpoints`.

   Запрос можно отправить на URL вашего окружения (SaaS или Managed) либо на URL Environment ActiveGate.

   * **Dynatrace SaaS**:

     ```
     curl https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Замените:

     + `<your-environment-id>` на [идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "Общие сведения о мониторинговых окружениях и работа с ними.")
     + `<your_PaaS_token>` на [PaaS token](#prerequisites)
   * **Dynatrace Managed**:

     ```
     curl https://<your-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Замените:

     + `<your-domain>` на домен вашего Managed-развёртывания
     + `<your-environment-id>` на [идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "Общие сведения о мониторинговых окружениях и работа с ними.")
     + `<your_PaaS_token>` на [PaaS token](#prerequisites)
   * **Environment ActiveGate**:

     ```
     curl https://<your-activegate-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Замените

     + `<your-activegate-domain>` на домен вашего ActiveGate
     + `<your-environment-id>` на [идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "Общие сведения о мониторинговых окружениях и работа с ними.")
     + `<your_PaaS_token>` на [PaaS token](#prerequisites)

### Шаг 3. Добавьте переменные окружения в приложение

Получив значения переменных окружения, необходимых для интеграции OneAgent, можно добавить соответствующие пары «ключ/значение» в приложение через Azure Portal или Azure CLI. Инструкции для каждого из вариантов приведены ниже.

В Azure CLI

В Azure Portal

Выполните приведённую ниже команду, заменив заполнители (`<...>`) собственными значениями, определёнными на предыдущих шагах.

```
az spring app deploy --name <your-application-name> --jar-path app.jar \



-s <your-resource-name> -g <your-resource-group-name> --env DT_TENANT=<your-environment-ID> \



DT_TENANTTOKEN=<your-tenant-token> DT_CONNECTION_POINT=<your-communication-endpoint>
```

1. Откройте экземпляр Azure Spring Apps и выберите группу ресурсов, в которой будет развёрнут Dynatrace.
2. Выберите приложение, данные которого нужно передавать в Dynatrace.
3. Выберите **Configuration** и введите следующие пары «ключ/значение» для переменных окружения.

   | Ключ | Значение |
   | --- | --- |
   | `DT_TENANT` | [Идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "Общие сведения о мониторинговых окружениях и работа с ними.") |
   | `DT_TENANTTOKEN` | Ваш tenant token. Подробнее см. в разделе [Определение значений необходимых переменных окружения](#envvar). |
   | `DT_CONNECTION_POINT` | Ваш communication endpoint. Подробнее см. в разделе [Определение значений необходимых переменных окружения](#envvar). |
4. [Создайте buildpack binding](https://dt-url.net/nu036u6) для Dynatrace, указав PaaS token (API token) и API url в качестве свойств.

   | Свойство | Значение |
   | --- | --- |
   | `api-url` | [Идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "Общие сведения о мониторинговых окружениях и работа с ними.") |
   | `api-token` | [PaaS token](#prerequisites) |

При необходимости можно настроить встроенные правила обнаружения группы процессов, задав дополнительную переменную окружения `DT_CLUSTER_ID`. В качестве значения укажите имя группы процессов, которое должно отображаться в Dynatrace. Подробнее см. в разделе [Обнаружение группы процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Способы настройки обнаружения группы процессов").

## Просмотр данных в Dynatrace

После добавления переменных окружения в приложение Dynatrace начнёт собирать из него данные. Чтобы просмотреть данные приложения Azure Spring Apps, откройте **Services** и выберите нужное приложение.

Пример потока сервиса:

![AppFlow](https://dt-cdn.net/images/1-1721-67868203e3.png)

AppFlow

Пример потребления CPU:

![Diagnostic cpu](https://dt-cdn.net/images/diagnostic-cpu-1565-a403ae7a02.png)

Diagnostic cpu

Пример анализа времени отклика:

![Resposetime](https://dt-cdn.net/images/f-1486-bd826153cb.png)

Resposetime

## Обновления OneAgent

Обновления OneAgent выполняются автоматически вместе с JDK.

После обновления OneAgent необходимо перезапустить или повторно развернуть приложения, чтобы они отслеживались новой версией OneAgent. Это обусловлено тем, что некоторые компоненты OneAgent продолжают работать в процессах, отслеживаемых Dynatrace.

* До перезапуска эти процессы будут по-прежнему отслеживаться с предыдущей версией OneAgent.
* После перезапуска эти процессы будут отслеживаться с последней версией OneAgent.

## Связанные темы

* [Мониторинг Azure Spring Apps](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps "Мониторинг Azure Spring Apps и просмотр доступных метрик.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах.")