---
title: Отправка уведомлений Dynatrace в ServiceNow
source: https://docs.dynatrace.com/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration
scraped: 2026-05-12T11:24:47.273920
---

# Отправка уведомлений Dynatrace в ServiceNow

# Отправка уведомлений Dynatrace в ServiceNow

* Чтение: 9 мин
* Обновлено 15 апреля 2025 г.

Для подключения среды мониторинга Dynatrace к экземпляру ServiceNow требуется настройка как на стороне ServiceNow, так и в веб-интерфейсе Dynatrace.

Для ServiceNow Dynatrace предлагает:

* [Интеграцию инцидентов](#incident-integration)
* [Интеграцию управления событиями](#event-integration)
* [Интеграцию с базой данных управления конфигурациями (CMDB)](#cmdb-integration)

## Интеграция инцидентов

Интеграция инцидентов Dynatrace передаёт инциденты из вашей среды Dynatrace в экземпляр ServiceNow.

После настройки интеграции инцидентов Dynatrace автоматически создаёт инцидент в ServiceNow для каждой автоматически обнаруженной проблемы.

### Приложение Dynatrace Incident Integration

Dynatrace Incident Integration — это приложение среды ServiceNow, которое принимает и обрабатывает проблемы Dynatrace и позволяет создавать инциденты в ServiceNow.

Если установлен ServiceNow Service Graph Connector for Dynatrace, элементы конфигурации (CI) автоматически связываются с инцидентом.

#### Предварительные требования

* У вас есть активный модуль и лицензия ServiceNow ITSM
* Пользователь ServiceNow имеет роли `web_service_admin` и `x_dynat_ruxit.Integration`

#### Настройка конфигурации ServiceNow

1. Перейдите на [страницу Dynatrace Incident Integration в ServiceNow Store](https://dt-url.net/fg03qnx) и выберите **Get** для установки приложения.
2. Выполните **Guided Setup** для первоначальной настройки приложения.

   ![Guided setup](https://dt-cdn.net/images/2020-11-20-09-31-17-1232-dfc605d001.png)

   Guided setup
3. После установки перейдите в новое меню **Dynatrace Incident Integration** в вашем экземпляре ServiceNow для дальнейшей настройки (**Setup**, **Settings**) и изучения (**Problems**, **ServiceNow Incidents**).

   ![Основные модули](https://dt-cdn.net/images/2020-11-20-09-34-57-1853-d333a1780e.png)

   Основные модули
4. Используйте модуль **Problem to Incident Transform Map** для преобразования входящих данных Dynatrace в таблице импорта **Problems** (`x_dynat_ruxit_problems`) в таблицу **Incident** ServiceNow.

   ![Transform map](https://dt-cdn.net/images/2020-11-20-09-37-50-1866-f2d395ffed.png)

   Transform map

#### Настройка конфигурации Dynatrace

Чтобы создать уведомление о проблеме ServiceNow:

1. В Dynatrace перейдите в **Settings**.
2. Выберите **Integration** > **Problem notifications**.
3. Выберите **Add notification**.
4. В поле **Notification type** выберите **ServiceNow**.
5. Введите запрошенную информацию:

   * **ServiceNow instance identifier** — идентификатор экземпляра в вашем URL ServiceNow (`https://<идентификатор_экземпляра>.service-now.com`), используемый в вызове ServiceNow API. Идентификатор экземпляра взаимоисключает поле OnPremise URL — можно использовать только одно из них.
   * В поле **Description** можно настроить текстовое сообщение для уведомлений о проблемах, комбинируя заполнители из списка **Available placeholders** в любом порядке.
6. Включите **Send incidents into ServiceNow ITSM**.
7. Выберите **Send test notification**, чтобы убедиться, что интеграция с ServiceNow работает.
8. Нажмите **Save changes**.

## Интеграция управления событиями

Существует несколько вариантов интеграции управления событиями с использованием уведомлений Dynatrace о проблемах:

* Отправка событий через уведомления о проблемах пользовательской интеграции Dynatrace
* Отправка событий через уведомления о проблемах Dynatrace ServiceNow

### Отправка событий через уведомления о проблемах пользовательской интеграции Dynatrace

ServiceNow Event Management предоставляет API входящих событий для получения событий от сторонних инструментов.

Эта конфигурация использует уведомления о проблемах пользовательской интеграции Dynatrace. Можно настроить пользовательские уведомления интеграции с URL API входящих событий ServiceNow и ожидаемой полезной нагрузкой JSON.

При настройке уведомление Dynatrace о проблеме будет отправлять сгруппированные события, связанные с проблемой.

Если у вас есть **ServiceNow Service Graph Connector for Observability - Dynatrace**, см. [инструкции по настройке push-уведомлений от Dynatrace](https://www.servicenow.com/docs/bundle/xanadu-servicenow-platform/page/product/configuration-management/task/setup-push-notifications-dynatrace.html). В противном случае см. [Интеграция событий платформы Dynatrace](https://www.servicenow.com/docs/bundle/xanadu-it-operations-management/page/product/event-management/concept/dynatrace-events-integration.html).

### Отправка событий через уведомления о проблемах Dynatrace ServiceNow

ServiceNow Event Management предоставляет универсальный API вебхука для получения событий, заполняющих таблицу событий ServiceNow ITOM (`em_event`).

Эта конфигурация использует уведомления о проблемах Dynatrace ServiceNow. Можно настроить уведомление ServiceNow с URL API вебхука ServiceNow и ожидаемой полезной нагрузкой JSON. Дополнительные сведения об API вебхука см. в разделе [Передача событий в экземпляр через API веб-сервиса](https://www.servicenow.com/docs/csh?topicname=send-events-via-web-service.html).

При настройке уведомление Dynatrace о проблеме будет отправлять все события, связанные с проблемой.

#### Предварительные требования

* У вас есть активный модуль и лицензия ServiceNow ITOM
* Пользователь ServiceNow имеет роль `snc_platform_rest_api_access`
* Фильтры событий и правила оповещений ServiceNow настроены для реагирования на входящие события от Dynatrace

#### Настройка конфигурации ServiceNow

Модуль и лицензия ServiceNow ITOM должны быть активны для использования этой интеграции.

#### Настройка конфигурации Dynatrace

1. Перейдите в **Settings**.
2. Выберите **Integration** > **Problem notifications** > **Add notification**.
3. В поле **Notification type** выберите **ServiceNow**.
4. Введите запрошенную информацию:

   * **ServiceNow instance identifier** — идентификатор экземпляра в вашем URL ServiceNow, используемый в вызове ServiceNow API `https://<идентификатор_экземпляра>.service-now.com`. Идентификатор экземпляра взаимоисключает поле OnPremise URL.
5. Включите **Send events into ServiceNow ITOM**.
6. Выберите **Send test notification**.
7. Нажмите **Save changes**.

После включения передачи событий ITOM все события для любой проблемы, обнаруженной Dynatrace, будут автоматически передаваться в ITOM event API.

### Просмотр событий

Можно создавать фильтры событий и правила оповещений в представлении **Event table** для гибкого реагирования на входящие события, обнаруженные Dynatrace, как показано в примере ниже:

![Events-SN](https://dt-cdn.net/images/2020-11-26-12-33-17-1493-31560df605.png)

Events-SN

## Интеграция с базой данных управления конфигурациями (CMDB)

ServiceNow предлагает специальное приложение **Service Graph Connector for Observability — Dynatrace** для передачи информации о наблюдаемости Dynatrace в CMDB ServiceNow.

**Service Graph Connector for Observability — Dynatrace** извлекает следующие типы данных топологии:

* Хосты
* Процессы
* Сервисы
* Приложения

Service Graph Connector for Observability использует связи между различными приложениями, прикладными сервисами и элементами инфраструктуры для создания карты сервисов.

Некоторые типы сущностей Dynatrace не импортируются в ServiceNow. Сведения о настройке и использовании см. в разделе [Service Graph Connector for Observability - Dynatrace](https://www.servicenow.com/docs/bundle/xanadu-servicenow-platform/page/product/configuration-management/concept/cmdb-integration-dynatrace.html).

## FAQ

### Общие вопросы

Какие IP-адреса Dynatrace разрешены для интеграции с ServiceNow?

Чтобы экземпляр Dynatrace мог взаимодействовать с ServiceNow, необходимо предоставить ServiceNow список IP-адресов Dynatrace, которым разрешено отправлять информацию в ServiceNow. Серверы Dynatrace распределены по различным регионам. Лучший способ получить правильные IP-адреса для вашего региона — выполнить команду `nslookup`. Сначала необходимо создать среду в Dynatrace, а затем выполнить `nslookup`.

Пример:

```
C:\>nslookup abc.live.dynatrace.com
```

Опционально можно просмотреть страницу загрузки OneAgent, чтобы увидеть IP-адреса для вашего региона.

### Интеграция инцидентов Dynatrace

Как работает интеграция?

Обзор интеграции инцидентов Dynatrace представлен на схеме ниже:

![Поток инцидентов](https://dt-cdn.net/images/1-914-942bc926e8.png)

Поток инцидентов

После настройки приложения с обеих сторон уведомления о проблемах передаются из Dynatrace в экземпляр ServiceNow.

![Создание инцидента](https://dt-cdn.net/images/2020-11-20-10-04-46-1873-71a111a8db.png)

Создание инцидента

Модуль **Scripted REST APIs** является точкой входа информации Dynatrace в ServiceNow. Он передаёт данные в таблицу импорта **Problems** (`x_dynat_ruxit_problems`).

![Уведомление о проблеме](https://dt-cdn.net/images/2020-11-20-09-46-29-1872-86d224c470.png)

Уведомление о проблеме

Таблица импорта **Problems** автоматически преобразует любую входящую проблему, обнаруженную Dynatrace, в инцидент в таблице инцидентов ServiceNow.

![Transform map](https://dt-cdn.net/images/2020-11-20-09-37-50-1866-f2d395ffed.png)

Transform map

При закрытии проблемы в Dynatrace инцидент в ServiceNow помечается как `Resolved`.

Какие таблицы ServiceNow заполняются приложением Dynatrace?

* Dynatrace отправляет все обнаруженные проблемы в таблицу инцидентов ServiceNow (`incident`).
* Все отдельные события, коррелирующие с проблемой Dynatrace, отправляются в таблицу событий ITOM (`em_event`).
* Связь между CI и проблемой Dynatrace передаётся в таблицу затронутых CI (`task_ci`).
* При включении Dynatrace синхронизирует все автоматически обнаруженные веб-сервисы в таблицу прикладных сервисов CMDB (`cmdb_ci_services_discovered`).
* Все хосты и группы процессов, работающие на этих хостах, синхронизируются в таблицу серверов CMDB и производные таблицы серверов Linux и Windows (`cmdb_ci_server`), а также в связанные таблицы групп процессов ServiceNow (`cmdb_ci_appl`).

Как изменить таблицу или поле, в которое Dynatrace передаёт данные?

Инциденты импортируются через таблицу импорта (`x_dynat_ruxit_problems`). Можно перенастроить стандартную карту преобразования **Problem to Incident Transformation Map** для направления информации в другие таблицы или поля.

Поддерживается ли несколько сред Dynatrace в интеграции?

Несколько сред Dynatrace можно настроить в таблице сред Dynatrace в ServiceNow.

### Отправка событий через уведомления о проблемах Dynatrace ServiceNow

Как работает интеграция?

Обзор интеграции инцидентов Dynatrace представлен на схеме ниже:

![Поток событий](https://dt-cdn.net/images/5-921-8ae4cf85e4.png)

Поток событий

### Интеграция с CMDB

Какие плановые задания извлекают информацию CMDB из Dynatrace?

Dynatrace вводит одно плановое задание, которое с регулярными интервалами извлекает подмножество топологической информации из Dynatrace Smartscape. Плановое задание SG-Dynatrace извлекает всю информацию о веб-приложениях и их связях с программными сервисами, информацию обо всех хостах и группах процессов, а также всех программных сервисах и связях. Извлечение информации выполняется с использованием официального REST API Dynatrace.

Как автоматически объединить существующие CI с CI, обнаруженными Dynatrace?

Дедупликация выполняется через **ServiceNow CMDB Identification and Reconciliation**. Пользовательские правила идентификации CI используются для объединения идентичных CI на основе заданного атрибута (например, имён хостов).

## Устранение неполадок

Ознакомьтесь со следующими статьями на [форуме по устранению неполадок сообщества Dynatrace](https://dt-url.net/dy122xtf).

### Общие

* [События не отображаются в таблице событий ITOM](https://dt-url.net/7t42xdu)
* [HTTP 403 Forbidden при отправке тестового уведомления](https://dt-url.net/eq62xe9)
* [Ссылка на проблему повреждена в инциденте ServiceNow](https://dt-url.net/fcc2x29)

### Интеграция инцидентов Dynatrace

* [Инциденты создаются некорректно](https://dt-url.net/o682xbl)

### Интеграция с CMDB

* [Хосты, группы процессов, приложения и сервисы, обнаруженные Dynatrace, не отображаются в CMDB](https://dt-url.net/km02xrc)
* [Серверы, отслеживаемые Dynatrace, не отображаются в CMDB](https://dt-url.net/n222x11)
* [Входящие инциденты не сопоставляются с затронутым сервером в CMDB](https://dt-url.net/8ia2xbr)