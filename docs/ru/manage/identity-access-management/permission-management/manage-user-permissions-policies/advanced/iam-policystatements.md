---
title: Справочник политик IAM
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements
scraped: 2026-03-06T21:31:13.383192
---

# Справочник политик IAM

# Справочник политик IAM

* Последняя версия Dynatrace
* Справочник
* Чтение 1 мин
* Опубликовано 25 марта 2021

Ниже приведен полный справочник разрешений IAM и соответствующих условий, применимых к сервисам Dynatrace. Используйте его, когда вам нужно определить политики доступа на основе детализированного набора разрешений и условий, которые могут быть применены для каждого сервиса.

## ai

AI предоставляет возможности генеративного ИИ в Dynatrace

### ai:operator:execute

Предоставляет разрешение на взаимодействие с диалоговым интерфейсом ИИ

## app-engine

AppEngine

### app-engine:apps:install

Предоставляет разрешение на установку и обновление приложений

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`
* `app-engine:app-installer` - Идентификатор пользователя, установившего приложение.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`

### app-engine:apps:run

Предоставляет разрешение на просмотр списка и запуск приложений, а также базовый доступ к Launcher

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`
* `app-engine:app-installer` - Идентификатор пользователя, установившего приложение.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`

### app-engine:apps:delete

Предоставляет разрешение на удаление приложений

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`
* `app-engine:app-installer` - Идентификатор пользователя, установившего приложение.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`

### app-engine:functions:run

Предоставляет разрешение на использование исполнителя функций

### app-engine:edge-connects:read

Предоставляет разрешение на чтение EdgeConnects

### app-engine:edge-connects:write

Предоставляет разрешение на запись EdgeConnects

### app-engine:edge-connects:delete

Предоставляет разрешение на удаление EdgeConnects

### app-engine:certificates:create

Предоставляет разрешение на создание краткосрочных сертификатов для релизов приложений

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `=`, `IN`, `startsWith`

## app-settings

Сервис настроек приложений

### app-settings:objects:read

Предоставляет разрешение на чтение объектов настроек приложений, принадлежащих схеме

#### conditions:

* `settings:schemaId` - Строка, уникально идентифицирующая одну схему настроек приложений. Идентификатор схемы можно найти в информационном блоке экрана настроек. Условие сработает, если свойство schemaId объекта совпадает.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - Строка, соответствующая идентификатору приложения. Применимо только к объектам схем, добавленных через приложения. Условие сработает, если свойство app-id объекта совпадает.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### app-settings:objects:write

Предоставляет разрешение на запись объектов настроек, принадлежащих схеме

#### conditions:

* `settings:schemaId` - Строка, уникально идентифицирующая одну схему настроек. Идентификатор схемы можно найти в информационном блоке экрана настроек. Условие сработает, если свойство schemaId объекта совпадает.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - Строка, соответствующая идентификатору приложения. Применимо только к объектам схем, добавленных через приложения. Условие сработает, если свойство app-id объекта совпадает.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### app-settings:objects:admin

Позволяет использовать режим администратора для доступа, изменения владельца и разрешений на общий доступ к любому объекту. Режим администратора обходит только проверку владельца, поэтому для выполнения полезных действий также необходимы разрешения app-settings:objects:read и/или app-settings:objects:write.

#### conditions:

* `settings:schemaId` - Строка, уникально идентифицирующая одну схему настроек приложений. Идентификатор схемы можно найти в информационном блоке экрана настроек. Условие сработает, если свойство schemaId объекта совпадает.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - Строка, соответствующая идентификатору приложения. Применимо только к объектам схем, добавленных через приложения. Условие сработает, если свойство app-id объекта совпадает.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

## automation

Сервер автоматизации

### automation:workflows:read

Предоставляет разрешение на чтение рабочих процессов

### automation:workflows:write

Предоставляет разрешение на запись рабочих процессов

#### conditions:

* `automation:workflow-type` - Строка, идентифицирующая тип рабочего процесса: SIMPLE или STANDARD
  operators: `IN`, `=`

### automation:workflows:run

Предоставляет разрешение на выполнение рабочих процессов

### automation:workflows:admin

Предоставляет административные разрешения для рабочих процессов.

### automation:rules:read

Предоставляет разрешение на чтение правил планирования

### automation:rules:write

Предоставляет разрешение на запись правил планирования

### automation:calendars:read

Предоставляет разрешение на чтение бизнес-календарей

### automation:calendars:write

Предоставляет разрешение на запись бизнес-календарей

## business-analytics

Сервис бизнес-аналитики платформы

### business-analytics:business-flows:write

Предоставляет разрешение на запись бизнес-потоков

### business-analytics:business-flows:read

Предоставляет разрешение на чтение бизнес-потоков

## data-acquisition

Прием данных

### data-acquisition:logs:ingest

Предоставляет разрешение на прием логов из поддерживаемых источников Data Acquisition

### data-acquisition:metrics:ingest

Предоставляет разрешение на прием метрик из поддерживаемых источников Data Acquisition

### data-acquisition:events:ingest

Предоставляет разрешение на прием событий из поддерживаемых источников Data Acquisition

## davis

Сервис Davis

### davis:analyzers:read

Предоставляет разрешение на просмотр анализаторов Davis

### davis:analyzers:execute

Предоставляет разрешение на выполнение анализаторов Davis

## davis-copilot

Davis CoPilot предоставляет возможности генеративного ИИ в Dynatrace

### davis-copilot:conversations:execute

Предоставляет разрешение на взаимодействие с диалоговым интерфейсом Davis CoPilot

### davis-copilot:nl2dql:execute

Предоставляет разрешение на выполнение возможности генеративного ИИ для преобразования естественного языка в DQL

### davis-copilot:dql2nl:execute

Предоставляет разрешение на выполнение навыка CoPilot «Суммаризация DQL»

### davis-copilot:document-search:execute

Предоставляет разрешение на выполнение навыка CoPilot «Поиск документов»

## deployment

Сервис развертывания

### deployment:activegates.network-zones:write

Предоставляет разрешение на запись сетевых зон ActiveGate

### deployment:activegates.groups:write

Предоставляет разрешение на запись групп ActiveGate

### deployment:oneagents.network-zones:write

Предоставляет разрешение на запись сетевых зон OneAgent

### deployment:oneagents.host-groups:write

Предоставляет разрешение на запись групп хостов OneAgent

### deployment:oneagents.host-tags:write

Предоставляет разрешение на запись тегов хостов OneAgent

### deployment:oneagents.host-properties:write

Предоставляет разрешение на запись свойств хостов OneAgent

### deployment:oneagents.communication-settings:write

Предоставляет разрешение на запись настроек коммуникации OneAgent

## dev-obs

Наблюдаемость разработчиков

### dev-obs:breakpoint:set

Предоставляет разрешение на установку точек останова с помощью live-отладчика DevObs

#### conditions:

* `dev-obs:k8s.namespace.name` - Пространства имен Kubernetes для агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.entity.process_group` - Группа процессов сущностей Dynatrace для агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.process_group.detected_name` - Обнаруженное имя группы процессов Dynatrace для агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:k8s.cluster.name` - Имя кластера агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.group` - Группа хостов агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.name` - Имя хоста агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`

### dev-obs:breakpoints:set

Предоставляет разрешение на установку точек останова с помощью live-отладчика DevObs

#### conditions:

* `dev-obs:k8s.namespace.name` - Пространства имен Kubernetes для агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.entity.process_group` - Группа процессов сущностей Dynatrace для агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.process_group.detected_name` - Обнаруженное имя группы процессов Dynatrace для агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:k8s.cluster.name` - Имя кластера агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.group` - Группа хостов агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.name` - Имя хоста агентов, в которых пользователю разрешено устанавливать точки останова
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`

### dev-obs:breakpoint:manage

Предоставляет разрешение на управление точками останова, установленными в live-отладчике DevObs

### dev-obs:breakpoints:manage

Предоставляет разрешение на управление точками останова, установленными в live-отладчике DevObs

## document

Сервис документов

### document:documents:write

Предоставляет разрешение на создание и обновление документов сервиса документов

### document:documents:read

Предоставляет разрешение на чтение документов сервиса документов

### document:documents:delete

Предоставляет разрешение на удаление документов сервиса документов

### document:documents:admin

Предоставляет административные разрешения для документов сервиса документов

### document:environment-shares:read

Предоставляет разрешение на чтение общих ресурсов среды сервиса документов

### document:environment-shares:write

Предоставляет разрешение на создание и обновление общих ресурсов среды сервиса документов

### document:environment-shares:claim

Предоставляет разрешение на получение общих ресурсов среды сервиса документов

### document:environment-shares:delete

Предоставляет разрешение на удаление общих ресурсов среды сервиса документов

### document:direct-shares:delete

Предоставляет разрешение на удаление прямых общих ресурсов сервиса документов

### document:direct-shares:read

Предоставляет разрешение на чтение прямых общих ресурсов сервиса документов

### document:direct-shares:write

Предоставляет разрешение на создание и обновление прямых общих ресурсов сервиса документов

### document:trash.documents:read

Предоставляет разрешение на чтение удаленных документов сервиса документов

### document:trash.documents:delete

Предоставляет разрешение на удаление документов из корзины сервиса документов

### document:trash.documents:restore

Предоставляет разрешение на восстановление удаленных документов из корзины сервиса документов

## email

API для отправки электронной почты

### email:emails:send

Предоставляет разрешение на отправку электронной почты с адреса @apps.dynatrace.com через API отправки

## environment

Разрешения пользователей среды и зоны управления. См. [Миграция разрешений на основе ролей в Dynatrace IAM](https://dt-url.net/3s23539) для получения дополнительной информации.

Разрешения IAM ролей работают так же, как и классические роли, что означает, что разрешение `environment:roles:viewer` является частью любого другого разрешения роли. Например, политика, предоставляющая разрешение `environment:roles:manage-settings`, также позволяет пользователю получить доступ к веб-интерфейсу.

### environment:roles:viewer

Предоставляет пользователю разрешение **Доступ к среде**.

#### conditions:

* `environment:management-zone` - Строка, уникально идентифицирующая зону управления. Применяет разрешение на уровне зоны управления для указанной зоны управления.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:manage-settings

Предоставляет пользователю разрешение **Изменение настроек мониторинга**.

#### conditions:

* `environment:management-zone` - Строка, уникально идентифицирующая зону управления. Применяет разрешение на уровне зоны управления для указанной зоны управления.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:agent-install

Предоставляет пользователю разрешение **Загрузка/установка OneAgent**. Пользователи с этим разрешением также могут просматривать данные мониторинга для всех зон управления.

### environment:roles:view-sensitive-request-data

Предоставляет пользователю разрешение **Просмотр конфиденциальных данных запросов**.

#### conditions:

* `environment:management-zone` - Строка, уникально идентифицирующая зону управления. Применяет разрешение на уровне зоны управления для указанной зоны управления.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:configure-request-capture-data

Предоставляет пользователю разрешение **Настройка захвата конфиденциальных данных**. Пользователи с этим разрешением также могут просматривать данные мониторинга для всех зон управления.

### environment:roles:replay-sessions-without-masking

Предоставляет пользователю разрешение **Воспроизведение данных сессий без маскировки**.

#### conditions:

* `environment:management-zone` - Строка, уникально идентифицирующая зону управления. Применяет разрешение на уровне зоны управления для указанной зоны управления.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:replay-sessions-with-masking

Предоставляет пользователю разрешение **Воспроизведение данных сессий**.

#### conditions:

* `environment:management-zone` - Строка, уникально идентифицирующая зону управления. Применяет разрешение на уровне зоны управления для указанной зоны управления.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:manage-security-problems

Предоставляет пользователю разрешение **Управление проблемами безопасности**.

#### conditions:

* `environment:management-zone` - Строка, уникально идентифицирующая зону управления. Применяет разрешение на уровне зоны управления для указанной зоны управления.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:view-security-problems

Предоставляет пользователю разрешение **Просмотр проблем безопасности**.

#### conditions:

* `environment:management-zone` - Строка, уникально идентифицирующая зону управления. Применяет разрешение на уровне зоны управления для указанной зоны управления.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:logviewer

Предоставляет пользователю разрешение **Просмотр логов**.

#### conditions:

* `environment:management-zone` - Строка, уникально идентифицирующая зону управления. Применяет разрешение на уровне зоны управления для указанной зоны управления.
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

## extensions

Сервис расширений

### extensions:definitions:read

Предоставляет разрешение на чтение конфигураций расширений и среды

#### conditions:

* `extensions:extension-name` - Строка, уникально идентифицирующая одно расширение
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:definitions:write

Предоставляет разрешение на запись (обновление/создание/удаление) конфигураций расширений и среды

#### conditions:

* `extensions:extension-name` - Строка, уникально идентифицирующая одно расширение
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configurations:read

Предоставляет разрешение на чтение конфигураций мониторинга расширений

#### conditions:

* `extensions:host` - Строка, уникально идентифицирующая один хост для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:host-group` - Строка, уникально идентифицирующая одну группу хостов для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:ag-group` - Строка, уникально идентифицирующая одну группу ActiveGate для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:management-zone` - Строка, уникально идентифицирующая одну зону управления для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:extension-name` - Строка, уникально идентифицирующая одно расширение
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configurations:write

Предоставляет разрешение на запись (обновление/создание/удаление) конфигураций мониторинга расширений

#### conditions:

* `extensions:host` - Строка, уникально идентифицирующая один хост для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:host-group` - Строка, уникально идентифицирующая одну группу хостов для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:ag-group` - Строка, уникально идентифицирующая одну группу ActiveGate для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:management-zone` - Строка, уникально идентифицирующая одну зону управления для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:extension-name` - Строка, уникально идентифицирующая одно расширение
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configuration.actions:write

Предоставляет разрешение на выполнение действий для расширения

#### conditions:

* `extensions:host` - Строка, уникально идентифицирующая один хост для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:host-group` - Строка, уникально идентифицирующая одну группу хостов для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:ag-group` - Строка, уникально идентифицирующая одну группу ActiveGate для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:management-zone` - Строка, уникально идентифицирующая одну зону управления для назначения конфигурации мониторинга
  operators: `IN`, `=`
* `extensions:extension-name` - Строка, уникально идентифицирующая одно расширение
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:discovery.jmx:read

Предоставляет разрешение на обнаружение запущенных Java-процессов через JMX и чтение их данных через расширения

## geolocation

Сервис геолокации

### geolocation:locations:lookup

Предоставляет разрешение на поиск геолокаций для IP-адресов.

## hub

Hub предоставляет каталогизированный контент, такой как приложения Dynatrace, расширения и технологии, в контексте среды.

### hub:catalog:read

Предоставляет разрешение на чтение каталогизированного контента Hub.

## hyperscaler-authentication

Сервис аутентификации гиперскейлеров

### hyperscaler-authentication:aws:authenticate

Предоставляет разрешение на аутентификацию в AWS.

### hyperscaler-authentication:azure:authenticate

Предоставляет разрешение на аутентификацию в Azure.

## iam

Фреймворк управления идентификацией и доступом.

### iam:service-users:use

Предоставляет разрешение на использование всех или указанных сервисных пользователей

#### conditions:

* `iam:service-user-email` - Адреса электронной почты сервисных пользователей
  operators: `IN`, `=`

### iam:service-users:create

Предоставляет разрешение на создание сервисного пользователя в среде

### iam:bindings:read

Предоставляет разрешение на чтение привязок

#### conditions:

* `iam:policyUuid` - UUID политики в URI.
  operators: `=`, `IN`
* `iam:levelType` - Тип уровня в URI.
  operators: `=`, `IN`
* `iam:boundGroup` - UUID группы в URI.
  operators: `=`, `IN`

### iam:bindings:write

Предоставляет разрешение на создание привязок

#### conditions:

* `iam:policyUuid` - UUID политики в URI.
  operators: `=`, `IN`
* `iam:levelType` - Тип уровня в URI.
  operators: `=`, `IN`
* `iam:boundGroup` - UUID группы в URI.
  operators: `=`, `IN`

### iam:policies:read

Предоставляет разрешение на чтение политик

### iam:policies:write

Предоставляет разрешение на создание политик

### iam:boundaries:read

Предоставляет разрешение на чтение границ

### iam:boundaries:write

Предоставляет разрешение на создание границ

### iam:effective-permissions:read

Предоставляет разрешение на чтение действующих разрешений

#### conditions:

* `iam-param:entity-type` - Тип сущности в параметрах запроса. Допустимые значения: `group`, `user`.
  operators: `=`
* `iam-param:entity-id` - Идентификатор сущности указанного типа в параметрах запроса.
  operators: `=`, `IN`

### iam:limits:read

Предоставляет разрешение на чтение лимитов

## insights

Сервис бизнес-аналитики

### insights:opportunities:read

Предоставляет разрешение на чтение данных из API Opportunity Insights

### insights:moments:read

Предоставляет разрешение на запрос моментов ценности и связанных данных

## mcp-gateway

MCP Gateway предоставляет возможности MCP-сервера в Dynatrace

### mcp-gateway:servers:invoke

Предоставляет разрешение на вызов API MCP Gateway

### mcp-gateway:servers:read

Предоставляет разрешение на просмотр списка доступных MCP-серверов

## notification

API для отправки уведомлений

### notification:self-notifications:read

Предоставляет разрешение на чтение собственных уведомлений.

### notification:self-notifications:write

Предоставляет разрешение на запись собственных уведомлений.

### notification:notifications:read

Предоставляет разрешение на чтение конфигураций уведомлений.

### notification:notifications:write

Предоставляет разрешение на запись конфигураций уведомлений.

## oauth2

Авторизация действий по выпуску токенов OAuth (обмен токенами)

### oauth2:clients:manage

Позволяет управлять легковесными клиентами OAuth

#### conditions:

* `oauth2:scopes` - Запрашиваемые области доступа для генерируемых клиентов OAuth
  operators: `=`, `NOT IN`

## openpipeline

OpenPipeline

### openpipeline:configurations:read

Предоставляет разрешение на чтение конфигурации OpenPipeline

### openpipeline:configurations:write

Предоставляет разрешение на запись конфигурации OpenPipeline

### openpipeline:events:ingest

Предоставляет разрешение на прием событий в OpenPipeline

### openpipeline:events.custom:ingest

Предоставляет разрешение на прием событий в пользовательские конечные точки OpenPipeline

### openpipeline:security.events:ingest

Предоставляет разрешение на прием событий безопасности в OpenPipeline

### openpipeline:security.events.custom:ingest

Предоставляет разрешение на прием событий безопасности в пользовательские конечные точки OpenPipeline

### openpipeline:events.sdlc:ingest

Предоставляет разрешение на прием событий жизненного цикла разработки ПО в OpenPipeline

### openpipeline:events.sdlc.custom:ingest

Предоставляет разрешение на прием событий жизненного цикла разработки ПО в пользовательские конечные точки OpenPipeline

## platform-token

Разрешения для токенов платформы

### platform-token:tokens:write

Позволяет записывать токены платформы пользователя.

## security-intelligence

Предоставляет API для анализа безопасности (обогащение и контекстуализация)

### security-intelligence:enrichments:run

Позволяет выполнять обогащение и обнаружение интеграционных приложений.

## session-replay

Воспроизведение сессий

### session-replay:resources:read

Предоставляет разрешение на получение ресурса воспроизведения сессии

## settings

Сервис настроек

### settings:objects:read

Позволяет читать объекты настроек, принадлежащие схеме

#### conditions:

* `settings:schemaId` - Строка, уникально идентифицирующая одну схему настроек. Идентификатор схемы можно найти через выделенную конечную точку схемы в Dynatrace Environment API или в информационном блоке экрана настроек. Условие сработает, если свойство schemaId объекта совпадает.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - Строка, соответствующая идентификатору приложения. Применимо только к объектам схем, добавленных через приложения. Условие сработает, если свойство app-id объекта совпадает.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - Группа схем, позволяющая обращаться к нескольким отдельным схемам одновременно. Группу схемы можно найти через выделенную конечную точку схемы в Dynatrace Environment API или в информационном блоке экрана настроек. Условие сработает, если у схемы объекта есть совпадающее свойство schemaGroup.
  operators: `IN`, `=`
* `settings:entity.hostGroup` - Атрибут группы хостов сущности, для которой хранится настройка. Это полезно, например, для предоставления доступа к областям настроек всех хостов, принадлежащих одной группе хостов.
  operators: `IN`, `=`, `!=`
* `settings:scope` - Точный идентификатор области, которую имеет или будет иметь объект настроек. Это условие позволяет предоставить доступ к области, например, отдельного хоста. В этом случае область равна идентификатору сущности, например, HOST-48B8F52F33098830.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `environment:management-zone` - Имя зоны управления. Это условие применимо к: любому объекту настроек, допустимому в области сущности, которая может быть сопоставлена с зоной управления, или к объектам настроек схем builtin:alerting.maintenance-window, builtin:alerting.profile, builtin:anomaly-detection.metric-events, builtin:monitoring.slo и builtin:problem.notifications.
  operators: `IN`, `=`, `startsWith`, `MATCH`
* `settings:dt.security_context` - Имя контекста безопасности. Это условие применимо к любому объекту настроек, допустимому в области сущности, которой может быть назначен контекст безопасности.
  operators: `IN`, `=`, `startsWith`

### settings:objects:write

Позволяет записывать объекты настроек, принадлежащие схеме

#### conditions:

* `settings:schemaId` - Строка, уникально идентифицирующая одну схему настроек. Идентификатор схемы можно найти через выделенную конечную точку схемы в Dynatrace Environment API или в информационном блоке экрана настроек. Условие сработает, если свойство schemaId объекта совпадает.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - Строка, соответствующая идентификатору приложения. Применимо только к объектам схем, добавленных через приложения. Условие сработает, если свойство app-id объекта совпадает.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - Группа схем, позволяющая обращаться к нескольким отдельным схемам одновременно. Группу схемы можно найти через выделенную конечную точку схемы в Dynatrace Environment API или в информационном блоке экрана настроек. Условие сработает, если у схемы объекта есть совпадающее свойство schemaGroup.
  operators: `IN`, `=`
* `settings:entity.hostGroup` - Атрибут группы хостов сущности, для которой хранится настройка. Это полезно, например, для предоставления доступа к областям настроек всех хостов, принадлежащих одной группе хостов.
  operators: `IN`, `=`, `!=`
* `settings:scope` - Точный идентификатор области, которую имеет или будет иметь объект настроек. Это условие позволяет предоставить доступ к области, например, отдельного хоста. В этом случае область равна идентификатору сущности, например, HOST-48B8F52F33098830.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `environment:management-zone` - Имя зоны управления. Это условие применимо к: любому объекту настроек, допустимому в области сущности, которая может быть сопоставлена с зоной управления, или к объектам настроек схем builtin:alerting.maintenance-window, builtin:alerting.profile, builtin:anomaly-detection.metric-events, builtin:monitoring.slo и builtin:problem.notifications.
  operators: `IN`, `=`, `startsWith`, `MATCH`
* `settings:dt.security_context` - Имя контекста безопасности. Это условие применимо к любому объекту настроек, допустимому в области сущности, которой может быть назначен контекст безопасности.
  operators: `IN`, `=`, `startsWith`

### settings:schemas:read

Позволяет читать схемы настроек

#### conditions:

* `settings:schemaId` - Строка, уникально идентифицирующая одну схему настроек. Идентификатор схемы можно найти через выделенную конечную точку схемы в Dynatrace Environment API или в информационном блоке экрана настроек. Условие сработает, если свойство schemaId схемы совпадает.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - Строка, соответствующая идентификатору приложения. Применимо только к объектам схем, добавленных через приложения. Условие сработает, если свойство app-id объекта совпадает.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - Группа схем, позволяющая обращаться к нескольким отдельным схемам одновременно. Группу схемы можно найти через выделенную конечную точку схемы в Dynatrace Environment API или в информационном блоке экрана настроек. Условие сработает, если свойство schemaId схемы совпадает.
  operators: `IN`, `=`

### settings:objects:admin

Позволяет использовать режим администратора для доступа, изменения владельца и разрешений на общий доступ к любому объекту. Режим администратора обходит только проверку владельца, поэтому для выполнения полезных действий также необходимы разрешения settings:objects:read и/или settings:objects:write.

#### conditions:

* `settings:schemaId` - Строка, уникально идентифицирующая одну схему настроек. Идентификатор схемы можно найти через выделенную конечную точку схемы в Dynatrace Environment API или в информационном блоке экрана настроек. Условие сработает, если свойство schemaId объекта совпадает.
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - Строка, соответствующая идентификатору приложения. Применимо только к объектам схем, добавленных через приложения. Условие сработает, если свойство app-id объекта совпадает.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - Группа схем, позволяющая обращаться к нескольким отдельным схемам одновременно. Группу схемы можно найти через выделенную конечную точку схемы в Dynatrace Environment API или в информационном блоке экрана настроек. Условие сработает, если у схемы объекта есть совпадающее свойство schemaGroup.
  operators: `IN`, `=`

## slo

Сервис SLO

### slo:slos:read

Предоставляет разрешение на чтение целей уровня обслуживания

### slo:slos:write

Предоставляет разрешение на запись целей уровня обслуживания

### slo:objective-templates:read

Предоставляет разрешение на чтение шаблонов целей уровня обслуживания

## state

Сервис состояния платформы

### state:app-states:read

Предоставляет разрешение на чтение состояний приложений

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:app-states:write

Предоставляет разрешение на запись состояний приложений

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:app-states:delete

Предоставляет разрешение на удаление состояний приложений

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:user-app-states:read

Предоставляет разрешение на чтение состояний приложений пользователя

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:user-app-states:write

Предоставляет разрешение на запись состояний приложений пользователя

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:user-app-states:delete

Предоставляет разрешение на удаление состояний приложений пользователя

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

## state-management

Управление состоянием - Удаление состояний приложений и состояний приложений пользователей для определенных приложений.

### state-management:app-states:delete

Предоставляет разрешение на удаление всех состояний приложений

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state-management:user-app-states:delete

Предоставляет разрешение на удаление состояний приложений текущего пользователя

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state-management:user-app-states:delete-all

Предоставляет разрешение на удаление состояний приложений всех пользователей

#### conditions:

* `shared:app-id` - Идентификатор приложения.
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

## storage

Grail

### storage:events:read

Предоставляет разрешение на чтение записей из таблицы событий

#### conditions:

* `storage:bucket-name` - Это условие ограничивает действие разрешения на уровне записей определенным списком бакетов.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Предоставляет высокоуровневую информацию о типе данных события без привязки к конкретному содержимому. Помогает определить тип записи необработанного события.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - Уникальный идентификатор типа данного события.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Источник события, например имя компонента или системы, сгенерировавшей событие.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - Имя пространства имен.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - Имя кластера.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Имя хоста.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Идентификатор группы хостов.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Идентификатор проекта Google Cloud Platform.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Идентификатор учетной записи Amazon Web Services.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Подписка Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Группа ресурсов Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:events:write

Предоставляет разрешение на запись событий в Grail

### storage:metrics:read

Предоставляет разрешение на чтение временных рядов из таблицы метрик

#### conditions:

* `storage:bucket-name` - Это условие ограничивает действие разрешения на уровне записей определенным списком бакетов.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:k8s.namespace.name` - Имя пространства имен, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - Имя кластера, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Имя хоста.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Идентификатор группы хостов.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:metric.key` - Идентификатор метрики, группирующий числовые измерения с одинаковой семантикой измерения (т.е. измеренные «одинаковым образом»).
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Идентификатор проекта Google Cloud Platform.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Идентификатор учетной записи Amazon Web Services.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Подписка Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Группа ресурсов Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:metrics:write

Предоставляет разрешения на запись метрик из классического Dynatrace в последнюю версию Dynatrace и наоборот

### storage:logs:read

Предоставляет разрешение на чтение записей из таблицы логов

#### conditions:

* `storage:bucket-name` - Это условие ограничивает действие разрешения на уровне записей определенным списком бакетов.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:k8s.namespace.name` - Имя пространства имен, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - Имя кластера, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Имя хоста.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Идентификатор группы хостов.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:log.source` - Местоположение, откуда поступает лог.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Идентификатор проекта Google Cloud Platform.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Идентификатор учетной записи Amazon Web Services.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Подписка Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Группа ресурсов Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:logs:write

Предоставляет разрешение на запись логов в Grail

### storage:entities:read

Предоставляет разрешение на чтение записей из сущностей

#### conditions:

* `storage:entity.type` - Тип сущности.
  operators: `=`, `IN`, `startsWith`
* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`

### storage:spans:read

Предоставляет разрешение на чтение записей из таблицы спанов

#### conditions:

* `storage:bucket-name` - Это условие ограничивает действие разрешения на уровне записей определенным списком бакетов.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:k8s.namespace.name` - Имя пространства имен, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - Имя кластера, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Имя хоста.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Идентификатор группы хостов.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Идентификатор проекта Google Cloud Platform.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Идентификатор учетной записи Amazon Web Services.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Подписка Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Группа ресурсов Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:bizevents:read

Предоставляет разрешение на чтение записей из таблицы бизнес-событий

#### conditions:

* `storage:bucket-name` - Это условие ограничивает действие разрешения на уровне записей определенным списком бакетов.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Предоставляет высокоуровневую информацию о типе данных события без привязки к конкретному содержимому. Помогает определить тип записи необработанного события.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - Уникальный идентификатор типа данного события.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Источник события, например имя компонента или системы, сгенерировавшей событие.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - Имя пространства имен, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - Имя кластера, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Имя хоста.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Идентификатор группы хостов.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Идентификатор проекта Google Cloud Platform.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Идентификатор учетной записи Amazon Web Services.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Подписка Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Группа ресурсов Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:smartscape:read

Предоставляет разрешение на чтение узлов и ребер Smartscape из Grail

#### conditions:

* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - Имя пространства имен, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - Имя кластера, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Имя хоста.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Идентификатор группы хостов.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Идентификатор проекта Google Cloud Platform.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Идентификатор учетной записи Amazon Web Services.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Подписка Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Группа ресурсов Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:system:read

Предоставляет разрешение на чтение записей из всех системных таблиц (например, `dt.system.events`).

#### conditions:

* `storage:bucket-name` - Это условие ограничивает действие разрешения на уровне записей определенным списком бакетов.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Предоставляет высокоуровневую информацию о типе данных события без привязки к конкретному содержимому. Помогает определить тип записи необработанного события.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - Уникальный идентификатор типа данного события.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Источник события, например имя компонента или системы, сгенерировавшей событие.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:buckets:read

Предоставляет разрешение на чтение записей из бакетов Grail. Требуется дополнительно к разрешению на таблицу.

#### conditions:

* `storage:table-name` - Имя таблицы бакета, к которому можно получить доступ.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:bucket-name` - Имя бакета, к которому можно получить доступ.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:query-consumption` - Если установлено значение `INCLUDED`, запрос возвращает данные только из настроенного включенного временного диапазона бакетов. Если установлено значение `ON_DEMAND`, возвращаются данные за весь временной диапазон. Для любого другого значения оператор IAM игнорируется. Включенный временной диапазон должен быть настроен для каждого бакета через Storage Management API.
  operators: `=`

### storage:fieldsets:read

Чтение данных из наборов полей

#### conditions:

* `storage:table-name` - Имя таблицы, из которой можно получить доступ к набору(ам) полей.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:bucket-name` - Имя бакета, из которого можно получить доступ к набору(ам) полей.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:fieldset-name` - Имя набора(ов) полей, к которым можно получить доступ.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`

### storage:bucket-definitions:read

Предоставляет разрешение на чтение определений бакетов из Grail

### storage:bucket-definitions:write

Предоставляет разрешение на запись определений бакетов в Grail

### storage:bucket-definitions:delete

Предоставляет разрешение на удаление определений бакетов из Grail

### storage:bucket-definitions:truncate

Предоставляет разрешение на удаление всех записей из бакета (но не самого бакета) в Grail.

### storage:records:delete

Удаление записей в Grail

### storage:files:read

Чтение данных из файлов.

#### conditions:

* `storage:file-path` - Путь к файлу, к которому можно получить доступ.
  operators: `=`, `startsWith`, `IN`

### storage:files:write

Прием данных через REST API

#### conditions:

* `storage:file-path` - Путь к файлу, к которому можно получить доступ.
  operators: `=`, `startsWith`, `IN`

### storage:files:delete

Удаление данных через REST API

#### conditions:

* `storage:file-path` - Путь к файлу, к которому можно получить доступ.
  operators: `=`, `startsWith`, `IN`

### storage:filter-segments:read

Чтение сегментов фильтрации из Grail

### storage:filter-segments:write

Запись сегментов фильтрации в Grail

### storage:filter-segments:share

Общий доступ к сегментам фильтрации в Grail

### storage:filter-segments:delete

Удаление собственных сегментов фильтрации в Grail

### storage:filter-segments:admin

Запись и удаление всех сегментов фильтрации в Grail

### storage:fieldset-definitions:read

Чтение определений наборов полей из Grail

### storage:fieldset-definitions:write

Запись и удаление определений наборов полей в Grail

### storage:application.snapshots:read

Чтение снимков приложений из Grail

#### conditions:

* `storage:bucket-name` - Это условие ограничивает действие разрешения на уровне записей определенным списком бакетов.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`

### storage:user.events:read

Чтение событий пользователей из Grail

#### conditions:

* `storage:bucket-name` - Это условие ограничивает действие разрешения на уровне записей определенным списком бакетов.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:frontend.name` - Имя фронтенда.
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:user.sessions:read

Чтение сессий пользователей из Grail

#### conditions:

* `storage:bucket-name` - Это условие ограничивает действие разрешения на уровне записей определенным списком бакетов.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:frontend.name` - Имя фронтенда.
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:user.replays:read

Чтение воспроизведений пользователей из Grail

#### conditions:

* `storage:bucket-name` - Это условие ограничивает действие разрешения на уровне записей определенным списком бакетов.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:security.events:read

Чтение событий безопасности из Grail

#### conditions:

* `storage:bucket-name` - Это условие ограничивает действие разрешения на уровне записей определенным списком бакетов.
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Предоставляет высокоуровневую информацию о типе данных события без привязки к конкретному содержимому. Помогает определить тип записи необработанного события.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - Уникальный идентификатор типа данного события.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Источник события, например имя компонента или системы, сгенерировавшей событие.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - Имя пространства имен, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - Имя кластера, в котором работает под.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Имя хоста.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Идентификатор группы хостов.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Пользовательское поле для контекста безопасности.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Идентификатор проекта Google Cloud Platform.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Идентификатор учетной записи Amazon Web Services.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Подписка Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Группа ресурсов Azure.
  operators: `=`, `IN`, `startsWith`, `MATCH`

## unified-analysis

Унифицированный анализ

### unified-analysis:screen-definition:read

Предоставляет разрешение на чтение определения экрана унифицированного анализа

## upgrade-assistant

Сервис помощника по обновлению SaaS

### upgrade-assistant:environments:write

Предоставляет разрешение на использование приложения помощника по обновлению SaaS

## vulnerability-service

Предоставляет API для доступа к уязвимостям, затрагивающим клиентские среды

### vulnerability-service:vulnerabilities:read

Позволяет просматривать уязвимости

### vulnerability-service:vulnerabilities:write

Позволяет изменять информацию, связанную с уязвимостями

## Связанные темы

* [Работа с политиками](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")
* [Синтаксис и примеры операторов политик IAM](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")
* [Предоставление доступа к настройкам](/docs/manage/identity-access-management/use-cases/access-settings "Grant access to Settings")
* [API управления учетной записью](/docs/dynatrace-api/account-management-api "Explore endpoints of the Account Management API.")
