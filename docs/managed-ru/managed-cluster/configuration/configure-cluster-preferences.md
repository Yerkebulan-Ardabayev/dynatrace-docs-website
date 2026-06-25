---
title: Параметры кластера
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-cluster-preferences
scraped: 2026-05-12T11:36:49.300927
---

# Параметры кластера

# Параметры кластера

* Published Nov 16, 2022

По умолчанию все параметры кластера включены. Правильная настройка зависит от уникальных потребностей вашей организации. Помимо параметров проактивной поддержки, здесь также представлены параметры, связанные с настройкой новых пользователей Community и управлением доменными именами. Подробности о доступных настройках приведены ниже.

Для настройки параметров конфиденциальности данных в вашей среде Managed перейдите в **Settings** > **Preferences**. Управлять ими также можно через [Cluster API v2](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.") и [Cluster API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1 "Find out about API for managing environments, network zones, synthetic locations, nodes, and tokens.").

Для доступа к странице **Preferences** необходимы права администратора кластера.

## Проактивная поддержка

### Сервисы поддержки Dynatrace Managed Mission Control

Dynatrace Managed обеспечивает полностью автоматизированное самоуправление, которое поддерживает систему в безопасном, надёжном и актуальном состоянии. Для этого Dynatrace необходимо отправлять определённую информацию в Dynatrace Mission Control. Данные настройки можно скорректировать, изменив соответствующие параметры в интерфейсе.

* **Report usage and billing information**

  Каждый кластер Dynatrace Managed отправляет данные о потреблении, имеющие отношение к лицензии: количество хост-юнитов, пользовательские метрики или мониторинг журналов для каждого окружения. Этот параметр отражается меткой **Report usage and billing information** в интерфейсе и не может быть изменён — для обеспечения корректного биллинга и проверки лицензии вашего развёртывания.
* **Report Dynatrace cluster health**

  Кластеры Dynatrace отправляют информацию о состоянии: идентификаторы кластера, флаги конфиденциальности, часовые пояса, уровни трафика и окна обслуживания. Состояние сервера, включая количество ядер CPU, нагрузку на CPU и использованное/свободное хранилище, сообщается в разрезе каждого кластера. Этот параметр отражается меткой **Report Dynatrace cluster health** в интерфейсе и не может быть изменён — для обеспечения поддержки вашего развёртывания.
* **Report cluster and OneAgent events to Dynatrace Mission Control**

  Для каждого события кластеры отправляют тип, уровень серьёзности, временну́ю метку и подробное описание, чтобы эксперты Dynatrace могли удалённо анализировать проблемы или несовместимости в вашей среде и устранять их. При отключении этого параметра ваша организация несёт ответственность за мониторинг системных событий и сбор файлов журналов, необходимых для решения проблем перед обращением к экспертам Dynatrace. Этот параметр управляется опцией **Report cluster and OneAgent events to Dynatrace Managed Mission Control Support Services** в интерфейсе.
* **Dynatrace deployment health and user behavior monitoring**

  Установки Dynatrace Managed включают Dynatrace OneAgent, который обеспечивает самомониторинг работоспособности кластера. Мониторинг включён в режиме Full-Stack Monitoring. В дополнение к инфраструктурным метрикам и метрикам сервисов Dynatrace захватывается следующая информация.

  + Данные о пользователях, например IP-адрес
  + Геолокация пользователей
  + Тип браузера или устройства
  + Детали действий пользователей в Dynatrace Managed, например клики или загрузка страниц
  + Журналы процессов Dynatrace Managed

  Этот параметр управляется опцией **Dynatrace deployment health monitoring** в интерфейсе.

## Удалённый доступ

* Разрешить экспертам Dynatrace удалённый доступ к настройкам мониторинга окружения.

  В случае обнаружения событий эксперты Dynatrace могут удалённо проверить настройки мониторинга конфигурации кластера. Для настройки этого параметра перейдите в **Settings** > **Remote access permissions** > **SMTP server**. Этот параметр управляется опцией **Remote access permissions** — **Allow Dynatrace Support employees remote access to this cluster's monitoring settings** в интерфейсе.
* Разрешить экспертам Dynatrace изменять конфигурацию.

  При включении эксперты Dynatrace могут удалённо оптимизировать настройки мониторинга окружения для обеспечения оптимальной производительности и стабильности. Этот параметр управляется опцией **Remote access permissions** — **Allow `option` Dynatrace employees who have appropriate permissions to access this cluster for purposes of pro-active support** в интерфейсе.

## Конфиденциальность

* Отправлять информацию об отслеживаемых технологиях и использовании функций.

  Dynatrace проактивно отправляет предупреждения о несовместимостях или рисках, специфичных для технологий, связанных с вашей средой. Dynatrace может собирать информацию об установленных версиях OneAgent, технологиях процессов, хостах, ActiveGate и других связанных объектах и конфигурациях. Полученная информация может использоваться для поддержки и улучшения предложений Dynatrace. Dynatrace может использовать эти данные (если они агрегированы и не позволяют идентифицировать конечных пользователей) для отраслевых исследований, сравнительного анализа и аналитики. Подробнее о том, как Dynatrace [отправляет информацию об отслеживаемых технологиях в вашей среде](/managed/managed-cluster/basics/mission-control-data-exchange "Review the data your Managed Cluster exchanges with Mission Control and the available opt-out options for each data category."), см. по ссылке. Этот параметр управляется опцией **Send information about monitored technologies and feature usage** в интерфейсе.
* Использовать Mission Control для отправки email-уведомлений.

  Включите собственный SMTP-сервер, чтобы контролировать способ доставки Dynatrace email-уведомлений, отчётов и других сообщений пользователям и администраторам. Для настройки SMTP-сервера перейдите в **Settings** > **Emails** > **SMTP server**. Дополнительные сведения о настройке SMTP-сервера см. в разделе [Настройка подключения к SMTP-серверу](/managed/managed-cluster/configuration/configure-smtp-server-connection "Learn how to configure an SMTP server connection and why this is recommended.").

## Dynatrace Community

Dynatrace Community — интернет-форум для клиентов и экспертов в области цифровой производительности, где они могут общаться и обмениваться идеями. Зарегистрированные пользователи могут задавать вопросы и просматривать ответы на сайте [Dynatrace Community](https://community.dynatrace.com/), а также создавать обращения в службу поддержки. Перед предоставлением пользователям доступа к Dynatrace Community убедитесь, что у них установлен действующий адрес электронной почты.

Создание учётной записи Dynatrace Community при входе в систему

1. Войдите как администратор в Cluster Management Console.
2. Перейдите в **Settings** > **Preferences**.
3. Включите параметр **Send users invitation to create a Dynatrace account on first login**.

Новые и существующие пользователи кластера получат письмо с инструкциями по созданию учётной записи Dynatrace Community. Новые пользователи получат письмо после первого успешного входа в кластер, а существующие — через несколько минут после включения параметра.

Этот параметр управляется опцией **Send users invitation to create a Dynatrace account on first login**. Имея учётную запись, пользователи получат доступ к Dynatrace Community, Dynatrace University и системе обращений в поддержку. Для улучшения самообслуживания рекомендуется включить этот параметр. Если вы его отключите, отдельные приглашения пользователям на создание учётной записи можно будет отправлять вручную со страницы сведений каждого пользователя.

## Управление доменным именем и SSL-сертификатами

### Управление доменным именем и SSL-сертификатами

Этот параметр управляется опцией **Enable management of domain name and SSL certificates**.

Включите этот параметр, чтобы создать доменное имя (поддомен `dynatrace-managed.com`) с доверенным сертификатом для кластера Dynatrace Managed. После этого все пользователи смогут получить доступ к Dynatrace по адресу `<prefix>.dynatrace-managed.com`. Центром сертификации (CA) является [Let's Encrypt](https://letsencrypt.org/). Сертификаты загружаются по HTTPS (REST API) через Mission Control.

**Enable management of domain name and SSL certificates**

Обратите внимание, что этот процесс может занять несколько минут. После завершения вы сможете получить доступ по новому URL. При отключении этого параметра SSL-сертификаты и URL кластера возвращаются к предыдущей версии. Не забудьте обновить настройки SSO IdP с этим URL.

## Управление параметрами кластера через REST API

Для управления большинством параметров кластера можно использовать [Cluster API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1 "Find out about API for managing environments, network zones, synthetic locations, nodes, and tokens."). Для изменения значения `Synchronize users' e-mail addresses, first and last name, and assigned permissions` необходимо использовать [Cluster API v2](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.") и выполнить процедуру ниже.

* [Аутентификация](#token-authentication)
* [Настройка синхронизации пользователей и разрешений](#config-users-and-permissions-sync)
* [Чтение схемы конфигурации](#read-config-schema)
* [Чтение текущей конфигурации](#read-current-config)
* [Создание объекта параметров конфиденциальности кластера](#create-settings-object)
* [Обновление параметров конфиденциальности кластера](#update-settings-object)
* [Удаление параметров конфиденциальности кластера](#delete-settings-object)

## Аутентификация

Для создания токена кластера с областями доступа **Write settings** и **Read settings**

1. Перейдите в **Settings** > **API tokens**.
2. В разделе **Cluster tokens** выберите **Generate token**.
3. Введите имя токена и задайте области доступа **Write settings** и **Read settings** для токена Cluster API.
4. Нажмите **Save**, затем **Copy** и сохраните токен в надёжном месте.

## Настройка синхронизации пользователей и разрешений

Для отправки конфигурации в виде JSON-payload используйте конечную точку [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") с токеном кластера, имеющим соответствующие [области доступа](#token-authentication). Пример ниже отключает синхронизацию:

```
[



{



"schemaId": "builtin:cluster-privacy-settings",



"scope": "cluster",



"value": {



"syncUsersAndPermissionsWithinSupportResources": false



}



}



]
```

## Чтение схемы конфигурации

Чтобы узнать JSON-формат, необходимый для отправки конфигурации, используйте конечную точку [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") с токеном кластера, имеющим соответствующие [области доступа](#token-authentication). Идентификатор схемы конфигурации (`schemaId`) — `builtin:cluster-privacy-settings`.

Подробности схемы ответа

```
{



{



"dynatrace": "1",



"schemaId": "builtin:cluster-privacy-settings",



"displayName": "Data exchange settings",



"description": "A Dynatrace Managed cluster exchange information with Dynatrace Mission Control, at least once, or periodically. You may want to opt-out of certain communications, such as allowing Dynatrace to proactively access your clusters and environments. However, some messages are mandatory and can't be switched off.",



"documentation": "Check data privacy and exchange in Dynatrace Managed deployments here: https://dt-url.net/5i035v7",



"version": "0",



"multiObject": false,



"maxObjects": 1,



"allowedScopes": [



"cluster"



],



"enums": {},



"types": {},



"properties": {



"syncUsersAndPermissionsWithinSupportResources": {



"displayName": "Synchronize users' email addresses, first and last names and assigned permissions within support resources with Mission Control",



"description": "Dispatched Dynatrace support resources will contain users' email addresses, first and last names, and assigned permissions.",



"documentation": "",



"type": "boolean",



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT",



"default": true



}



}



}
```

## Чтение текущей конфигурации

Для проверки текущей конфигурации используйте конечную точку [GET objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") (`/api/cluster/v2/settings/objects?schemaIds=builtin:cluster-privacy-settings&scopes=cluster`) с токеном кластера, имеющим соответствующие [области доступа](#token-authentication).

* Если эти настройки ранее изменялись, список items содержит один объект. Используйте `objectId` из списка для последующих обновлений.
* Если список items пуст, применяется значение по умолчанию (не отображается в Dynatrace API):

  ```
  {



  "value": {



  "syncUsersAndPermissionsWithinSupportResources": true



  }



  }
  ```

## Создание объекта параметров конфиденциальности кластера

Для создания объекта параметров конфиденциальности кластера используйте конечную точку [POST objects](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") с токеном кластера, имеющим соответствующие [области доступа](#token-authentication). Используйте ID созданного объекта для последующих обновлений настроек.

Пример объекта параметров конфиденциальности кластера

В данном примере с помощью вызова `POST` к конечной точке `/api/cluster/v2/settings/objects` и схемы `builtin:cluster-privacy-settings` создаётся объект параметров конфиденциальности кластера в настройках кластера:

```
[



{



"schemaId": "builtin:cluster-privacy-settings",



"scope": "cluster",



"value": {



"syncUsersAndPermissionsWithinSupportResources": true



}



}



]
```

## Обновление параметров конфиденциальности кластера

После создания объекта параметров конфиденциальности кластера существует два способа их обновления. В обоих случаях убедитесь, что у вас есть токен кластера с соответствующими [областями доступа](#token-authentication).

* Можно использовать тот же метод `POST`, что применялся при создании объекта настроек ([Создание объекта параметров конфиденциальности кластера](#create-settings-object)). Схема не допускает дублирование объектов настроек, поэтому при попытке создать новый объект настроек существующий будет перезаписан.
* Можно изменить существующий объект настроек, выполнив вызов `PUT` API к конечной точке `/api/cluster/v2/settings/objects/<objectId>` и передав `objectId`, полученный при создании объекта параметров конфиденциальности кластера.

  Пример обновления объекта параметров конфиденциальности кластера

  Выполните вызов `PUT` API к `/api/cluster/v2/settings/objects/<objectId>`

  ```
  {



  "value": {



  "syncUsersAndPermissionsWithinSupportResources": true



  }



  }
  ```

## Удаление параметров конфиденциальности кластера

Можно удалить существующий объект параметров конфиденциальности кластера, выполнив вызов [`DELETE`](/managed/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.") API к конечной точке `/api/cluster/v2/settings/objects/<objectId>` (с токеном кластера, имеющим соответствующие [области доступа](#token-authentication)) и передав `objectId`, полученный при создании объекта параметров конфиденциальности кластера. После удаления объекта поведение конфиденциальности кластера возвращается к значению по умолчанию: синхронизация пользователей и разрешений включена.