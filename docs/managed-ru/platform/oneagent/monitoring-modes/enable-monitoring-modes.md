---
title: Включение режимов мониторинга OneAgent
source: https://docs.dynatrace.com/managed/platform/oneagent/monitoring-modes/enable-monitoring-modes
scraped: 2026-05-12T11:07:16.766611
---

# Включение режимов мониторинга OneAgent

# Включение режимов мониторинга OneAgent

* How-to guide
* 8-min read
* Published Nov 26, 2025

По умолчанию [OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") работает в режиме мониторинга Full-Stack, обеспечивая полную видимость хостов, процессов и сервисов. Если вы предпочитаете более лёгкий подход, вы можете переключиться на один из двух альтернативных режимов, ориентированных на основные метрики инфраструктуры:

* Режим мониторинга инфраструктуры
* Режим обнаружения

## Выбор режима мониторинга по умолчанию

Вы можете определить режим мониторинга по умолчанию до установки OneAgent. Это изменит режим мониторинга **Full-Stack** по умолчанию на странице развёртывания OneAgent (для операционных систем Linux, Windows и AIX) и в приложении ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage** (при развёртывании OneAgent со страницы **Install OneAgent**).

Чтобы определить режим мониторинга по умолчанию

1. Перейдите в **Settings** > **Preferences** > **OneAgent default mode**.
2. Выберите **OneAgent default monitoring mode** из раскрывающегося списка.
3. Нажмите **Save changes**.

Выбранное значение будет установлено как значение по умолчанию для выбранного режима развёртывания OneAgent.

## Включение режима мониторинга инфраструктуры

Вы можете включить режим мониторинга инфраструктуры на уровне хоста — во время или после установки OneAgent.

Во время установки OneAgent

Чтобы включить режим мониторинга инфраструктуры во время установки OneAgent, используйте параметр `--set-monitoring-mode=infra-only`.

Для получения дополнительной информации см. документацию по [установке OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms."), специфичную для вашей среды.

После установки OneAgent

Чтобы включить режим мониторинга инфраструктуры после установки OneAgent, используйте один из следующих вариантов:

* В Dynatrace

  1. Перейдите в **Hosts** и откройте страницу обзора хоста.
  2. Нажмите **More** (**…**) > **Settings** в правом верхнем углу для отображения страницы **Host settings**.
  3. Выберите **Host monitoring**.
  4. Перейдите в **Monitoring Mode** и в раскрывающемся меню выберите **Infrastructure**.
  5. Нажмите **Save changes**.
* Используйте [интерфейс командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") для установки параметра `--set-monitoring-mode=infra-only`.
* Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") для включения режима мониторинга инфраструктуры в масштабе.
* Для загрузки схемы используйте [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") с `builtin:host.monitoring` в качестве schemaId и создайте объект конфигурации с помощью [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").

### Внедрение в процессы

Внедрение в процессы предоставляет дополнительные данные для Infrastructure Observability. Внедрение в процессы включено по умолчанию.

Если вы запускаете OneAgent в контейнере с включённым режимом мониторинга инфраструктуры, внедрение в процессы выполняться не будет.

Режим мониторинга инфраструктуры позволяет отслеживать любой компонент инфраструктуры и вспомогательный сервис, написанный на Java. Вы можете отслеживать вспомогательные сервисы, поддерживаемые по умолчанию (например, Kafka или ActiveMQ), а также создавать собственные [расширения JMX и PMI](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions "Learn how to extend Dynatrace monitoring to include applications you've instrumented with JMX.") для компонентов инфраструктуры и использовать их в режиме мониторинга инфраструктуры.

Кроме того, при внедрении в процессы режим мониторинга инфраструктуры предоставляет метрики выполнения для:

* Java
* .NET
* Node.js
* Golang
* PHP
* Веб-серверов, таких как Apache HTTP, NGINX или Microsoft IIS.

### Отключение автоматического внедрения в процессы

Мы не рекомендуем отключать автоматическое внедрение, но если вы должны сделать это из-за строгих требований безопасности, вы можете выбрать среди различных вариантов. Отключение автоматического внедрения также предотвращает обнаружение уязвимостей и отладку в реальном времени в вашей среде, даже если вы включили [Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.") или [Live Debugger](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."). Вы можете отключить автоматическое внедрение на уровне хоста или среды.

#### Отключение автоматического внедрения для одного хоста

После установки OneAgent через веб-интерфейс

1. Перейдите в **Hosts** и откройте страницу обзора хоста.
2. Нажмите **More** (**…**) > **Settings** в правом верхнем углу для отображения страницы **Host settings**.
3. Выберите **Host Monitoring**.
4. Перейдите в **Advanced settings**.
5. Отключите **ProcessAgent Injection**, затем нажмите **Save changes**.
6. Перезапустите отслеживаемые процессы на хосте.

После установки OneAgent через командную строку

Используйте [интерфейс командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") для установки параметра `--set-auto-injection-enabled=false`.

Если вы используете oneagentctl для отключения автоматического внедрения, вы не сможете управлять автоматическим внедрением в режиме мониторинга инфраструктуры с помощью веб-интерфейса Dynatrace через **Settings > Monitoring > Monitored technologies** или [API конфигурации мониторинга OneAgent](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration "Update the monitoring configuration of a OneAgent instance via the Dynatrace API.").

#### Отключение автоматического внедрения для среды

Определение пользовательских правил мониторинга процессов

Вы можете отключить внедрение в процессы для конкретных групп процессов с помощью пользовательских правил мониторинга процессов.

Пользовательские правила мониторинга процессов обеспечивают детальный контроль над тем, в какие процессы внедряется OneAgent, с подходом, который легко масштабируется в больших средах. Вам не нужно изменять конфигурацию системы, и несколько правил могут охватывать тысячи процессов.

Подробнее см. в разделе [Углублённый мониторинг процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring").

Отключение метрик выполнения

Вы можете отключить сбор метрик JMX/PMI и выполнения, что приведёт к отключению автоматического внедрения в режиме мониторинга инфраструктуры.

1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
2. В списке поддерживаемых технологий найдите запись **Java/.NET/Node.js/Golang/PHP runtime metrics + WebServer metrics in Infrastructure Mode**.
3. Нажмите значок карандаша ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") для редактирования и отключите её.
4. Перезапустите все процессы на хостах, отслеживаемых в режиме инфраструктуры.

Отключение выбранных расширений

Вы также можете отключить выбранные расширения, собирающие метрики на уровне среды.

1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
2. Поддерживаемые технологии

   Пользовательские расширения

   1. В списке поддерживаемых технологий найдите технологии, отмеченные как **JMX monitoring** в столбце **Type**.
   2. Нажмите значок карандаша ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") для редактирования выбранного расширения.
   3. Отключите **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   1. В списке пользовательских расширений найдите расширения, отмеченные как **JMX** или **PMI** в столбце **Extension type**.
   2. Выберите имя нужного расширения.
   3. Отключите **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   Настройка на уровне хоста имеет приоритет над настройками среды. Если хост настроен на **Use host configuration** для расширения и расширение не активировано на этом хосте, конфигурация среды применяться не будет. Чтобы убедиться, что расширение активно на уровне отдельного хоста:

   1. Перейдите в **Hosts** и найдите хост, отслеживаемый в режиме инфраструктуры. Вы можете использовать фильтр **Monitoring mode: Infrastructure only**.
   2. Откройте страницу хоста.
   3. Нажмите **More** (**…**) > **Settings** в правом верхнем углу для отображения страницы **Host settings**.
   4. В таблице **Monitored technologies** найдите расширения типа **JMX extension**, **JMX monitoring** или **PMI extension**.
   5. Нажмите **Edit**. Используйте элемент управления **Activate `<extension name>` on this host**.

### Фильтрация хостов по статусу внедрения

Когда вы отключаете автоматическое внедрение, вы можете найти такие хосты с помощью фильтра **Auto-injection** на странице **Deployment Status** или [OneAgent on a host - GET a list of hosts with OneAgent details](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.").

Использование веб-интерфейса Dynatrace

1. Перейдите в **Deployment Status** и выберите вкладку **OneAgents**.
2. Выберите поле **Filter by**, выберите **Auto-injection** и выберите **Disabled manually**. Вы также можете использовать один из фильтров ниже для проверки других причин. Обратите внимание, что фильтр отображается только в том случае, если в вашем развёртывании есть хост с соответствующим статусом.

* **Enabled** — автоматическое внедрение успешно включено.
* **Disabled manually** — автоматическое внедрение было отключено [после установки OneAgent](#after-install) через веб-интерфейс Dynatrace или `oneagentctl`.
* **Disabled on installation** — автоматическое внедрение было отключено [во время установки OneAgent](#during-install).
* **Disabled on sanity check** — автоматическое внедрение не было включено из-за неудачного теста, выполненного установщиком OneAgent до начала установки. Проверьте журнал установщика OneAgent для получения подробной информации.
* **Failed on installation** — автоматическое внедрение завершилось неудачей из-за ошибки во время установки OneAgent. Проверьте журнал установщика OneAgent для получения подробной информации.

Использование Dynatrace API

Выполните вызов [OneAgent on a host - GET a list of hosts with OneAgent details](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.") с параметром `autoInjection`, установленным в `DISABLED_MANUAL`. Возвращаемый ответ содержит список OneAgents с отключённым автоматическим внедрением [после установки OneAgent](#after-install) через веб-интерфейс Dynatrace или `oneagentctl`.

## Включение режима обнаружения

Вы можете включить режим обнаружения на уровне хоста — во время или после установки OneAgent.

Во время установки OneAgent

Чтобы включить режим обнаружения во время установки OneAgent, используйте параметр `--set-monitoring-mode=discovery`.

Для получения дополнительной информации см. документацию по [установке OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms."), специфичную для вашей среды.

После установки OneAgent

Чтобы включить режим обнаружения после установки OneAgent, используйте один из следующих вариантов:

* В Dynatrace

  1. Перейдите в **Hosts** и откройте страницу обзора хоста.
  2. Нажмите **More** (**…**) > **Settings** в правом верхнем углу для отображения страницы **Host settings**.
  3. Выберите **Host monitoring**.
  4. Перейдите в **Monitoring Mode** и в раскрывающемся меню выберите **Discovery**.
  5. Нажмите **Save changes**.
* Используйте [интерфейс командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") для установки параметра `--set-monitoring-mode=discovery`.

### Внедрение кодового модуля

Для работы [Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.") и [Live Debugger](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") в режиме обнаружения требуется внедрение кодового модуля. Внедрение кодового модуля отключено по умолчанию.

После [включения режима обнаружения](#enable-discovery-mode) вы можете включить внедрение кодового модуля для одного хоста.

1. Перейдите на страницу настроек нужного хоста и выберите **Host monitoring**.
2. Перейдите в **Advanced settings**.
3. Включите **CodeModule Injection**, затем нажмите **Save changes**.
4. Перезапустите отслеживаемые процессы на хосте.

Подробнее о том, как работает Application Security в режиме обнаружения, см. в разделе [Application Security: Discovery mode](/managed/secure/application-security#discovery "Access the Dynatrace Application Security functionalities.").