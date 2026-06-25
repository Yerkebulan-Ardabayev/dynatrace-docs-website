---
title: Миграция OneAgent
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-oa
scraped: 2026-05-12T12:14:00.644731
---

# Миграция OneAgent

# Миграция OneAgent

* Published Apr 24, 2023

Для начала сбора данных в целевой среде SaaS и завершения миграции конфигурации необходимо перенести OneAgent из среды Managed.

Существует несколько способов это сделать. Выберите тот, который лучше всего подходит для вашей ситуации.

* Рекомендуется Удалённая массовая миграция с помощью удалённого управления конфигурацией
* Локальная миграция с помощью `oneagentctl`
* Использование [оркестрации развёртывания OneAgent](/managed/ingest-from/dynatrace-oneagent/deployment-orchestration "Learn how to deploy OneAgent using deployment orchestration")
* Удаление существующего OneAgent и установка из среды SaaS

## Удалённая массовая миграция с помощью удалённого управления конфигурацией

Рекомендуется

Вы можете использовать [удалённое управление конфигурацией](/managed/ingest-from/bulk-configuration#bulk-configuration-oa-communication-settings "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") для массового изменения настроек связи OneAgent в одной среде. При использовании удалённого управления конфигурацией действие по-прежнему выполняется на соответствующих хостах, однако вы запускаете и контролируете его централизованно из раздела **Deployment Status** в веб-интерфейсе Dynatrace.

Для начала перейдите в вашу среду Dynatrace Managed и выберите **Deployment Status** в меню Dynatrace.

## Локальная миграция с помощью oneagentctl

Используйте интерфейс командной строки `oneagentctl` для перенастройки OneAgent на уровне отдельного хоста. Необходимо обновить несколько параметров конфигурации связи OneAgent:

* Задать настройки связи OneAgent
* Задать ID среды
* Задать токен среды
* Задать или удалить конфигурацию прокси. Подробнее см. в разделе [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Использование oneagentctl

Требования:

* На хосте должен быть установлен `curl`

Указание некорректного параметра `--set-server` приведёт к потере OneAgent связи как с предыдущей, так и с новой средой.

Существуют два сценария в зависимости от того, как OneAgent в настоящее время подключается к среде Dynatrace Managed:

1. Автономный OneAgent напрямую подключается к узлам кластера
   В этом случае URL вашей среды SaaS является адресом связи для экземпляров OneAgent. Никакой дополнительной установки не требуется.
2. Автономный OneAgent использует Cluster ActiveGate или Environment ActiveGate
   В этом случае необходимо [установить новый Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") для целевой среды. В приведённой ниже процедуре используйте адрес ActiveGate в качестве адреса связи.

Для перенастройки OneAgent на месте выполните следующую процедуру:

В вашей целевой среде:

1. Создайте [токен доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") с областью применения **PaaS integration - Installer download**.
2. В меню пользователя справа откройте интерактивный REST API-клиент для **Environment API v1**.
3. Выполните запрос [Deployment API - View connectivity information for OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "View the connectivity information of OneAgent via Dynatrace API."), используя сгенерированный токен для аутентификации.
4. Сохраните ответ от вызова API — эти данные понадобятся на следующем шаге.
5. Войдите на целевой хост и используйте следующую команду для перенаправления OneAgent в новую среду Dynatrace:

   * Linux или AIX:  
     `./oneagentctl --set-server=https://abc123456.live.dynatrace:443 --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`
   * Windows:  
     `.\oneagentctl.exe --set-server=https://abc123456.live.dynatrace.com:443 --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`

   Параметр `--set-server` задаёт конечную точку связи OneAgent. Используйте IP-адрес или имя хоста. В зависимости от конфигурации развёртывания это может быть URL среды или ActiveGate. Можно использовать значение `formattedCommunicationEndpoints` из ответа API.

   Параметр `--set-tenant` задаёт ID среды. Можно использовать значение `tenantUUID` из ответа API.

   Параметр `--set-tenant-token` задаёт токен среды для аутентификации связи с заданной конечной точкой. Можно использовать значение `tenantToken` из ответа API.

   После успешной перенастройки OneAgent будет перезапущен. Другие параметры управления см. в разделе [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").
6. После перенастройки OneAgent необходимо перезапустить все приложения, отслеживаемые с глубоким анализом кода.
7. Перейдите в **Deployment Status** и выберите **OneAgents**, чтобы проверить, появился ли ваш OneAgent и успешно ли отслеживаются приложения. В случае ошибки повторите эти шаги для перенаправления OneAgent обратно в среду Managed.

Вопросы?

Посетите [форум Upgrade to SaaS](https://community.dynatrace.com/t5/Upgrade-to-SaaS/bd-p/upgrade_to_saas), чтобы задать вопросы, получить ответы и поделиться опытом с другими участниками.