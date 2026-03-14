---
title: Отправка Dynatrace уведомлений в ServiceNow
source: https://www.dynatrace.com/docs/analyze-explore-automate/notifications-and-alerting/problem-notifications/servicenow-integration
scraped: 2026-03-06T21:11:41.657451
---

# Отправка уведомлений Dynatrace в ServiceNow


* Classic
* 9 мин. чтения
* Обновлено 15 апреля 2025

Для расширенных возможностей и автоматизации рабочих процессов (например, включения целевых уведомлений и автоматического устранения проблем) см. [Коннекторы Workflows](../../workflows/actions.md "Используйте готовые действия Dynatrace для ваших рабочих процессов и интегрируйте Dynatrace со сторонними системами.").

Для подключения вашей среды мониторинга Dynatrace к экземпляру ServiceNow необходима настройка как на стороне экземпляра ServiceNow, так и в веб-интерфейсе Dynatrace.

Для ServiceNow Dynatrace предлагает:

* [Интеграцию инцидентов](#incident-integration)
* [Интеграцию управления событиями](#event-integration)
* [Интеграцию базы данных управления конфигурациями (CMDB)](#cmdb-integration)

## Интеграции инцидентов

Существует несколько вариантов интеграции для управления инцидентами:

* Dynatrace Workflows
* Приложение Dynatrace Incident Integration

После настройки интеграции инцидентов Dynatrace автоматически создаёт инцидент в вашем экземпляре ServiceNow для каждой автоматически обнаруженной проблемы.

### Dynatrace Workflows

Dynatrace Workflows позволяет моделировать процессы создания и управления инцидентами непосредственно в Dynatrace. Для получения дополнительной информации о конфигурации и использовании см. документацию рабочих процессов [ServiceNow](../../workflows/actions/service-now.md "Автоматизируйте создание инцидентов в ServiceNow на основе ваших данных мониторинга и событий.").

### Приложение Dynatrace Incident Integration

Dynatrace Incident Integration — это приложение для среды ServiceNow, которое принимает и обрабатывает проблемы Dynatrace и позволяет создавать инциденты в ServiceNow.

Если вы установили ServiceNow Service Graph Connector для Dynatrace, CI (элементы конфигурации) будут автоматически связаны с инцидентом.

#### Предварительные требования

* У вас есть активный модуль и лицензия ServiceNow ITSM
* Ваш пользователь ServiceNow имеет роли `web_service_admin` и `x_dynat_ruxit.Integration`

#### Настройка конфигурации ServiceNow

1. Перейдите на [страницу Dynatrace Incident Integration в ServiceNow Store](https://dt-url.net/fg03qnx) и выберите **Get**, чтобы установить Dynatrace Incident Integration в вашем экземпляре ServiceNow.
2. Следуйте **Guided Setup** для начальной настройки приложения.

   ![Мастер настройки](https://dt-cdn.net/images/2020-11-20-09-31-17-1232-dfc605d001.png)
3. После установки приложения перейдите в новое меню **Dynatrace Incident Integration** в вашем экземпляре ServiceNow для дальнейшей настройки (**Setup**, **Settings**) и изучения (**Problems**, **ServiceNow Incidents**) приложения.

   ![Основные модули](https://dt-cdn.net/images/2020-11-20-09-34-57-1853-d333a1780e.png)
4. Используйте модуль **Problem to Incident Transform Map** для преобразования входящих данных Dynatrace в таблице импорта **Problems** (`x_dynat_ruxit_problems`) в таблицу **Incident** ServiceNow.

   ![Карта преобразования](https://dt-cdn.net/images/2020-11-20-09-37-50-1866-f2d395ffed.png)

#### Настройка конфигурации Dynatrace

Чтобы создать уведомление о проблемах ServiceNow

1. В Dynatrace перейдите в **Settings**.
2. Выберите **Integration** > **Problem notifications**.
3. Выберите **Add notification**.
4. В поле **Notification type** выберите **ServiceNow**.
5. Введите запрашиваемую информацию:

   * **ServiceNow instance identifier** — это часть «идентификатор экземпляра» вашего URL ServiceNow (`https://<instance indentifier>.service-now.com`), которая используется при вызове API ServiceNow. Этот идентификатор экземпляра ServiceNow является взаимоисключающим с полем OnPremise URL, поэтому вы можете использовать только одно из них.
   * В поле **Description field** вы можете настроить текстовое сообщение, связанное с уведомлениями о проблемах, комбинируя любые заполнители из списка **Available placeholders** в любом порядке в соответствии с вашими потребностями.
6. Включите **Send incidents into ServiceNow ITSM**.
7. Выберите **Send test notification**, чтобы убедиться, что интеграция с ServiceNow работает.
8. Выберите **Save changes**.

## Интеграция управления событиями

Существует несколько вариантов интеграции для управления событиями, использующих уведомления о проблемах Dynatrace. Вы можете:

* Отправлять события с помощью пользовательских интеграционных уведомлений о проблемах Dynatrace
* Отправлять события с помощью уведомлений о проблемах Dynatrace ServiceNow

### Отправка событий с помощью пользовательских интеграционных уведомлений о проблемах Dynatrace

ServiceNow Event Management предоставляет API входящих событий для сторонних инструментов.

Эта конфигурация использует пользовательские интеграционные уведомления о проблемах Dynatrace. Вы можете настроить уведомления пользовательской интеграции с URL API входящих событий ServiceNow и ожидаемой полезной нагрузкой JSON.

После настройки уведомление о проблемах Dynatrace будет отправлять сгруппированные события, связанные с проблемой.

Если у вас есть **ServiceNow Service Graph Connector for Observability — Dynatrace**, см. [Настройка push-уведомлений из Dynatrace](https://www.servicenow.com/docs/bundle/xanadu-servicenow-platform/page/product/configuration-management/task/setup-push-notifications-dynatrace.html) для получения информации о настройке и использовании. В противном случае см. [Интеграция событий платформы Dynatrace](https://www.servicenow.com/docs/bundle/xanadu-it-operations-management/page/product/event-management/concept/dynatrace-events-integration.html).

### Отправка событий с помощью уведомлений о проблемах Dynatrace ServiceNow

ServiceNow Event Management предоставляет универсальный API вебхуков для приёма событий, которые заполняют таблицу событий ServiceNow ITOM (`em_event`).

Эта конфигурация использует уведомления о проблемах Dynatrace ServiceNow. Вы можете настроить уведомление ServiceNow с URL API вебхуков ServiceNow и ожидаемой полезной нагрузкой JSON. Дополнительные сведения об API вебхуков см. в документации [Отправка событий в экземпляр с помощью API веб-сервиса](https://www.servicenow.com/docs/csh?topicname=send-events-via-web-service.html).

После настройки уведомление о проблемах Dynatrace будет отправлять все события, связанные с проблемой.

#### Предварительные требования

* У вас есть активный модуль и лицензия ServiceNow ITOM
* Ваш пользователь ServiceNow имеет роль `snc_platform_rest_api_access`
* Фильтры событий и правила оповещения ServiceNow настроены для реагирования на входящие события, отправленные Dynatrace

#### Настройка конфигурации ServiceNow

Ваш модуль и лицензия ServiceNow ITOM должны быть активны для использования этого варианта интеграции.

#### Настройка конфигурации Dynatrace

1. Перейдите в **Settings**.
2. Выберите **Integration** > **Problem notifications** > **Add notification**.
3. В поле **Notification type** выберите **ServiceNow**.
4. Введите запрашиваемую информацию:

   * **ServiceNow instance identifier** — это часть «идентификатор экземпляра» вашего URL ServiceNow, которая используется при вызове API ServiceNow `https://<instance indentifier>.service-now.com`. Этот идентификатор экземпляра ServiceNow является взаимоисключающим с полем OnPremise URL, поэтому вы можете использовать только одно из них.
5. Включите **Send events into ServiceNow ITOM**
6. Выберите **Send test notification**.
7. Выберите **Save changes**.

После включения отправки событий ITOM все события для каждой обнаруженной Dynatrace проблемы будут автоматически отправляться в API событий ITOM.

### Просмотр событий

Вы можете создавать фильтры событий и правила оповещения в представлении **Event table** для гибкого реагирования на входящие события, обнаруженные Dynatrace, как показано в примере ниже:

![События SN](https://dt-cdn.net/images/2020-11-26-12-33-17-1493-31560df605.png)

## Интеграция базы данных управления конфигурациями (CMDB)

ServiceNow предлагает специализированное приложение **Service Graph Connector for Observability — Dynatrace** для извлечения информации наблюдаемости Dynatrace в вашу CMDB ServiceNow.

**Service Graph Connector for Observability — Dynatrace** извлекает следующие типы данных топологии:

* Хосты
* Процессы
* Сервисы
* Приложения

Service Graph Connector for Observability использует связи между различными приложениями, сервисами приложений и элементами инфраструктуры для создания карты сервисов (Service Map).

Некоторые типы сущностей Dynatrace не импортируются в ServiceNow. Для получения информации о настройке и использовании см. [Service Graph Connector for Observability — Dynatrace](https://www.servicenow.com/docs/bundle/xanadu-servicenow-platform/page/product/configuration-management/concept/cmdb-integration-dynatrace.html).

## Часто задаваемые вопросы

### Общие

Какие IP-адреса Dynatrace разрешены для интеграции с ServiceNow?

Для того чтобы ваш экземпляр Dynatrace мог взаимодействовать с ServiceNow, вам необходимо предоставить ServiceNow список IP-адресов Dynatrace, которым будет разрешено отправлять информацию в ServiceNow. Серверы Dynatrace распределены по различным регионам. Лучший способ убедиться, что вы получаете правильные IP-адреса для вашего региона — это выполнить команду `nslookup`. Сначала необходимо создать среду в Dynatrace, а затем выполнить `nslookup`.

Пример:

```
C:\>nslookup abc.live.dynatrace.com
```

Кроме того, вы можете просмотреть страницу загрузки OneAgent, чтобы увидеть IP-адреса для вашего региона.

### Интеграция инцидентов Dynatrace

Как работает интеграция?

Обзор интеграции инцидентов Dynatrace показан на блок-схеме ниже:

![Поток инцидентов](https://dt-cdn.net/images/1-914-942bc926e8.png)

После настройки приложения на обеих сторонах уведомления о проблемах отправляются из Dynatrace в ваш экземпляр ServiceNow.

![Создание инцидента](https://dt-cdn.net/images/2020-11-20-10-04-46-1873-71a111a8db.png)

Модуль **Scripted REST APIs** является точкой входа информации Dynatrace в ServiceNow. Он отправляет данные в таблицу импорта **Problems**.

![Уведомление о проблеме](https://dt-cdn.net/images/2020-11-20-09-46-29-1872-86d224c470.png)

Таблица импорта **Problems** автоматически преобразует любую входящую проблему, обнаруженную Dynatrace, в инцидент в таблице инцидентов ServiceNow.

![Карта преобразования](https://dt-cdn.net/images/2020-11-20-09-37-50-1866-f2d395ffed.png)

Когда проблема закрывается в Dynatrace, инцидент помечается как `Resolved` в ServiceNow.

Какие таблицы ServiceNow заполняются приложением ServiceNow Dynatrace?

* Dynatrace отправляет все обнаруженные проблемы в таблицу инцидентов ServiceNow (`incident`).
* Все отдельные события, коррелированные с обнаруженной Dynatrace проблемой, отправляются в таблицу событий ITOM (`em_event`).
* Связь между CI и обнаруженной Dynatrace проблемой отправляется в таблицу затронутых CI (`task_ci`).
* Если включено, Dynatrace синхронизирует все автоматически обнаруженные веб-сервисы в таблицу сервисов приложений CMDB (`cmdb_ci_services_discovered`).
* Все хосты и группы процессов, работающие на этих хостах, синхронизируются в таблицу серверов CMDB и производные таблицы серверов Linux и Windows (`cmdb_ci_server`), а также в связанные таблицы групп процессов в ServiceNow (`cmdb_ci_appl`).

Как изменить таблицу или поле, в которое Dynatrace отправляет данные?

Инциденты импортируются через таблицу импорта (`x_dynat_ruxit_problems`). Вы можете перенастроить стандартную карту преобразования **Problem to Incident Transformation Map** для маршрутизации информации в другие таблицы или поля.

Поддерживается ли несколько сред в интеграции Dynatrace?

Несколько сред Dynatrace могут быть настроены в таблице сред Dynatrace в ServiceNow.

### Отправка событий с помощью уведомлений о проблемах Dynatrace ServiceNow

Как работает интеграция?

Обзор интеграции инцидентов Dynatrace показан на блок-схеме ниже:

![Поток событий](https://dt-cdn.net/images/5-921-8ae4cf85e4.png)

### Интеграция базы данных управления конфигурациями (CMDB)

Какие запланированные задания извлекают информацию CMDB из Dynatrace?

Dynatrace вводит одну запланированную задачу, которая извлекает подмножество информации о топологии из Dynatrace Smartscape через регулярные интервалы. Запланированная задача SG-Dynatrace извлекает всю информацию о веб-приложениях вместе с их связями с программными сервисами, всю информацию о хостах и группах процессов, а также все программные сервисы и связи. Извлечение информации выполняется с использованием официального Dynatrace REST API.

Как автоматически объединить существующие CI с CI, обнаруженными Dynatrace?

Дедупликация выполняется через **ServiceNow CMDB Identification and Reconciliation**. Пользовательские правила идентификации CI используются для объединения идентичных CI на основе заданного атрибута (например, имён хостов).

## Устранение неполадок

Ознакомьтесь со следующими статьями на [форуме устранения неполадок в сообществе Dynatrace](https://dt-url.net/dy122xtf).

### Общие

* [События не отображаются в таблице событий ITOM](https://dt-url.net/7t42xdu)
* [Ошибка HTTP 403 Forbidden Access Restricted Not Authorized при отправке тестового уведомления](https://dt-url.net/eq62xe9)
* [Ссылка на проблему не работает в инциденте ServiceNow](https://dt-url.net/fcc2x29)

### Интеграция инцидентов Dynatrace

* [Инциденты создаются некорректно](https://dt-url.net/o682xbl)

### Интеграция базы данных управления конфигурациями (CMDB)

* [Обнаруженные Dynatrace хосты, группы процессов, приложения и сервисы не отображаются в CMDB](https://dt-url.net/km02xrc)
* [Серверы, мониторируемые Dynatrace, не отображаются в CMDB](https://dt-url.net/n222x11)
* [Входящие инциденты не сопоставляются с затронутым сервером в CMDB](https://dt-url.net/8ia2xbr)