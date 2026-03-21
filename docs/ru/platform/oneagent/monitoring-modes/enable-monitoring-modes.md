---
title: Включение режимов мониторинга OneAgent
source: https://www.dynatrace.com/docs/platform/oneagent/monitoring-modes/enable-monitoring-modes
scraped: 2026-03-06T21:15:38.957990
---

* Latest Dynatrace
* 8 мин. чтения

По умолчанию [OneAgent](../../../ingest-from/dynatrace-oneagent.md "Узнайте основные концепции OneAgent и как устанавливать и эксплуатировать OneAgent на различных платформах.") работает в режиме Full-Stack мониторинга, обеспечивая полную видимость хостов, процессов и сервисов. Если вы предпочитаете более лёгкий подход, вы можете переключиться на один из двух альтернативных режимов, которые сосредоточены на основных метриках инфраструктуры:

* Режим мониторинга инфраструктуры (Infrastructure monitoring mode)
* Режим обнаружения (Discovery mode)

## Выбор режима мониторинга по умолчанию

Вы можете определить режим мониторинга по умолчанию перед установкой OneAgent. Это изменит стандартный режим мониторинга **Full-Stack** на странице развёртывания OneAgent (для операционных систем Linux, Windows и AIX) и в приложении ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage** (при развёртывании OneAgent со страницы **Install OneAgent**).

Чтобы определить режим мониторинга по умолчанию

1. Перейдите в **Settings** > **Preferences** > **OneAgent default mode**.
2. Выберите **OneAgent default monitoring mode** из выпадающего списка.
3. Выберите **Save changes**.

Выбранное значение будет установлено как значение по умолчанию для выбранного режима развёртывания OneAgent.

## Включение режима мониторинга инфраструктуры

Вы можете включить режим мониторинга инфраструктуры на уровне хоста, как во время, так и после установки OneAgent.

Во время установки OneAgent

Чтобы включить режим мониторинга инфраструктуры во время установки OneAgent, используйте параметр `--set-monitoring-mode=infra-only`.

Дополнительную информацию см. в документации по [установке OneAgent](../../../ingest-from/dynatrace-oneagent.md "Узнайте основные концепции OneAgent и как устанавливать и эксплуатировать OneAgent на различных платформах.") для вашей конкретной среды.

После установки OneAgent

Чтобы включить режим мониторинга инфраструктуры после установки OneAgent, используйте один из следующих вариантов:

* В Dynatrace

  1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** и откройте страницу обзора хоста.
  2. Выберите **More** (**...**) > **Settings** в правом верхнем углу для отображения страницы **Host settings**.
  3. Выберите **Host monitoring**.
  4. Перейдите к **Monitoring Mode** и в выпадающем меню выберите **Infrastructure**.
  5. Выберите **Save changes**.
* Используйте [интерфейс командной строки OneAgent](../../../ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md "Узнайте, как выполнять некоторые задачи конфигурации OneAgent без необходимости переустановки OneAgent.") для установки параметра `--set-monitoring-mode=infra-only`.
* Используйте [Settings API](../../../dynatrace-api/environment-api/settings.md "Узнайте, что предлагает Dynatrace Settings API.") для включения режима мониторинга инфраструктуры в масштабе.
* Для загрузки схемы используйте [GET a schema](../../../dynatrace-api/environment-api/settings/schemas/get-schema.md "Просмотрите схему настроек через Dynatrace API.") с `builtin:host.monitoring` в качестве schemaId и создайте объект конфигурации с помощью [POST an object](../../../dynatrace-api/environment-api/settings/objects/post-object.md "Создайте или проверьте объект настроек через Dynatrace API.").

### Внедрение в процессы

Внедрение в процессы предоставляет вам дополнительные данные для наблюдаемости инфраструктуры. Внедрение в процессы включено по умолчанию.

Если вы запускаете OneAgent как контейнер с включённым режимом мониторинга инфраструктуры, внедрение в процессы не будет выполняться.

Режим мониторинга инфраструктуры позволяет мониторить любой компонент инфраструктуры и вспомогательный сервис, написанный на Java. Вы можете мониторить вспомогательные сервисы, поддерживаемые по умолчанию (например, Kafka или ActiveMQ), а также можете создавать собственные [расширения JMX и PMI](../../../ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions.md "Узнайте, как расширить мониторинг Dynatrace для включения приложений, инструментированных с помощью JMX.") для компонентов инфраструктуры и использовать их в режиме мониторинга инфраструктуры.

Кроме того, с внедрением в процессы режим мониторинга инфраструктуры предоставляет метрики времени выполнения для:

* Java
* .NET
* Node.js
* Golang
* PHP
* Веб-серверов, таких как Apache HTTP, NGINX или Microsoft IIS.

### Отключение автоматического внедрения в процессы

Мы не рекомендуем отключать автоматическое внедрение, но если вам это необходимо из-за строгих требований безопасности, вы можете выбрать один из нескольких вариантов. Отключение автоматического внедрения также предотвращает обнаружение Dynatrace уязвимостей и отладку в реальном времени в вашей среде, даже если вы включите [Application Security](../../../secure/application-security.md "Доступ к функциональности Dynatrace Application Security.") или [Live Debugger](../../../observe/application-observability/live-debugger.md "Познакомьтесь с возможностями Live Debugger в Dynatrace."). Вы можете отключить автоматическое внедрение на уровне хоста или среды.

#### Отключение автоматического внедрения для отдельного хоста

После установки OneAgent через интерфейс

1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** и откройте страницу обзора хоста.
2. Выберите **More** (**...**) > **Settings** в правом верхнем углу для отображения страницы **Host settings**.
3. Выберите **Host Monitoring**.
4. Перейдите в **Advanced settings**.
5. Отключите **ProcessAgent Injection**, затем выберите **Save changes**.
6. Перезапустите мониторируемые процессы на хосте.

После установки OneAgent через командную строку

Используйте [интерфейс командной строки OneAgent](../../../ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md "Узнайте, как выполнять некоторые задачи конфигурации OneAgent без необходимости переустановки OneAgent.") для установки параметра `--set-auto-injection-enabled=false`.

Если вы используете oneagentctl для отключения автоматического внедрения, вы не сможете управлять автоматическим внедрением в режиме мониторинга инфраструктуры через веб-интерфейс Dynatrace в разделе **Settings > Monitoring > Monitored technologies** или через [API конфигурации мониторинга OneAgent](../../../dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration.md "Обновите конфигурацию мониторинга экземпляра OneAgent через Dynatrace API.").

#### Отключение автоматического внедрения для среды

Определение пользовательских правил мониторинга процессов

Вы можете отключить внедрение в процессы для определённых групп процессов с помощью пользовательских правил мониторинга процессов.

Пользовательские правила мониторинга процессов дают вам детальный контроль над тем, в какие процессы OneAgent выполняет внедрение, с подходом, который легко масштабируется в больших средах. Вам не нужно изменять конфигурацию системы, и несколько правил могут охватить тысячи процессов.

Дополнительные сведения см. в разделе [Глубокий мониторинг процессов](../../../observe/infrastructure-observability/process-groups/configuration/pg-monitoring.md#rules "Способы настройки мониторинга групп процессов").

Отключение метрик времени выполнения

Вы можете отключить сбор метрик JMX/PMI и метрик времени выполнения, что приведёт к отключению автоматического внедрения в режиме мониторинга инфраструктуры.

1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
2. В списке поддерживаемых технологий найдите запись **Java/.NET/Node.js/Golang/PHP runtime metrics + WebServer metrics in Infrastructure Mode**.
3. Выберите значок карандаша ![Редактировать](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Редактировать"), чтобы отредактировать её, а затем отключите её.
4. Перезапустите все процессы на хостах с мониторингом инфраструктуры.

Отключение выбранных расширений

Вы также можете отключить выбранные расширения, собирающие метрики, на уровне среды.

1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
2. Поддерживаемые технологии

   Пользовательские расширения

   1. В списке поддерживаемых технологий найдите технологии, помеченные как **JMX monitoring** в столбце **Type**.
   2. Выберите значок карандаша ![Редактировать](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Редактировать"), чтобы отредактировать выбранное расширение.
   3. Отключите **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   1. В списке пользовательских расширений найдите расширения, помеченные как **JMX** или **PMI** в столбце **Extension type**.
   2. Выберите имя нужного расширения.
   3. Отключите **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   Настройка на уровне хоста имеет приоритет над настройками среды. Если хост настроен на **Use host configuration** для расширения и расширение не активировано на этом хосте, конфигурация среды не будет применена. Чтобы убедиться, что расширение активно на уровне отдельного хоста:

   1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** и найдите хост с мониторингом инфраструктуры. Вы можете фильтровать по **Monitoring mode: Infrastructure only**.
   2. Откройте страницу хоста.
   3. Выберите **More** (**...**) > **Settings** в правом верхнем углу для отображения страницы **Host settings**.
   4. В таблице **Monitored technologies** найдите расширения типа **JMX extension**, **JMX monitoring** или **PMI extension**.
   5. Выберите **Edit**. Используйте элемент управления **Activate `<extension name>` on this host**.

### Фильтрация хостов по статусу внедрения

Когда вы отключаете автоматическое внедрение, вы можете найти такие хосты с помощью фильтра **Auto-injection** на странице **Deployment Status** или через [OneAgent on a host — GET a list of hosts with OneAgent details](../../../dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents.md "Проверьте конфигурацию экземпляров OneAgent на ваших хостах через Dynatrace API.").

Использование веб-интерфейса Dynatrace

1. Перейдите в **Deployment Status**, затем выберите вкладку **OneAgents**.
2. Выберите поле **Filter by**, выберите **Auto-injection** и выберите **Disabled manually**. Вы также можете использовать один из фильтров ниже для проверки других причин. Обратите внимание, что фильтр отображается только при наличии хоста с соответствующим статусом в вашем развёртывании.

* **Enabled**
  Автоматическое внедрение было успешно включено.
* **Disabled manually**
  Автоматическое внедрение было отключено [после установки OneAgent](#after-install), через веб-интерфейс Dynatrace или `oneagentctl`.
* **Disabled on installation**
  Автоматическое внедрение было отключено [во время установки OneAgent](#during-install).
* **Disabled on sanity check**
  Автоматическое внедрение не было включено из-за неудачного теста, выполненного установщиком OneAgent перед началом установки. Подробности см. в журнале установщика OneAgent.
* **Failed on installation**
  Автоматическое внедрение не удалось из-за ошибки во время установки OneAgent. Подробности см. в журнале установщика OneAgent.

Использование Dynatrace API

Выполните вызов [OneAgent on a host — GET a list of hosts with OneAgent details](../../../dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents.md "Проверьте конфигурацию экземпляров OneAgent на ваших хостах через Dynatrace API.") с параметром `autoInjection`, установленным в `DISABLED_MANUAL`. Возвращаемая полезная нагрузка содержит список экземпляров OneAgent с автоматическим внедрением, отключённым [после установки OneAgent](#after-install) через веб-интерфейс Dynatrace или `oneagentctl`.

## Включение режима обнаружения (Discovery)

Вы можете включить режим обнаружения на уровне хоста, как во время, так и после установки OneAgent.

Во время установки OneAgent

Чтобы включить режим обнаружения во время установки OneAgent, используйте параметр `--set-monitoring-mode=discovery`.

Дополнительную информацию см. в документации по [установке OneAgent](../../../ingest-from/dynatrace-oneagent.md "Узнайте основные концепции OneAgent и как устанавливать и эксплуатировать OneAgent на различных платформах.") для вашей конкретной среды.

После установки OneAgent

Чтобы включить режим обнаружения после установки OneAgent, используйте один из следующих вариантов:

* В Dynatrace

  1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** и откройте страницу обзора хоста.
  2. Выберите **More** (**...**) > **Settings** в правом верхнем углу для отображения страницы **Host settings**.
  3. Выберите **Host monitoring**.
  4. Перейдите к **Monitoring Mode** и в выпадающем меню выберите **Discovery**.
  5. Выберите **Save changes**.
* Используйте [интерфейс командной строки OneAgent](../../../ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md "Узнайте, как выполнять некоторые задачи конфигурации OneAgent без необходимости переустановки OneAgent.") для установки параметра `--set-monitoring-mode=discovery`.

### Внедрение модуля кода

Для работы [Application Security](../../../secure/application-security.md "Доступ к функциональности Dynatrace Application Security.") и [Live Debugger](../../../observe/application-observability/live-debugger.md "Познакомьтесь с возможностями Live Debugger в Dynatrace.") в режиме обнаружения требуется внедрение модуля кода. Внедрение модуля кода отключено по умолчанию.

После [включения режима обнаружения](#enable-discovery-mode) вы можете включить внедрение модуля кода для отдельного хоста.

1. Перейдите на страницу настроек нужного хоста и выберите **Host monitoring**.
2. Перейдите в **Advanced settings**.
3. Включите **CodeModule Injection**, затем выберите **Save changes**.
4. Перезапустите мониторируемые процессы на хосте.

Подробную информацию о работе Application Security в режиме обнаружения см. в разделе [Application Security: режим обнаружения](../../../secure/application-security.md#discovery "Доступ к функциональности Dynatrace Application Security.").