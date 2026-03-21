---
title: Трассировка IBM MQ
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing
scraped: 2026-03-06T21:26:53.183725
---

* How-to guide
* 6-min read

Dynatrace может автоматически создавать непрерывный [поток сервисов](../../../application-observability/services-classic/service-flow.md "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") для IBM MQ, когда сервисы-производители и сервисы-потребители используют одно и то же имя очереди или темы. Если сервисы-производители и потребители обращаются к разным именам очередей или тем, для создания непрерывного потока сервисов может потребоваться настройка IBM MQ.

Без настройки IBM MQ Dynatrace по-прежнему может трассировать все сообщения, но поток сервисов будет прерван.

Пример непрерывного потока сервисов IBM MQ

![IBM MQ service flow](https://dt-cdn.net/images/ibm-mq-service-flow-1938-06750bfc7d.png)

Пример распределённой трассировки IBM MQ

![IMB MQ distributed trace](https://dt-cdn.net/images/ibmmq-distributed-traces-3772-59101a2b00.png)

### Часто задаваемые вопросы

Нужно ли создавать заголовок MQRFH2, если он отсутствует в моих сообщениях IBM MQ?

Мы рекомендуем создавать заголовок `MQRFH2` для сообщений IBM MQ. Наличие заголовка `MQRFH2` в сообщениях IBM MQ позволяет Dynatrace использовать [идентификаторы вместо уникальных ключей](../queue-concepts.md#producer-consumer-service "Basic concepts of message queue monitoring in Dynatrace.") для трассировки сообщений между очередями и темами IBM App Connect Enterprise и IBM Integration Bus.

Преимущества создания заголовка `MQRFH2` для сообщений IBM MQ:

* Согласованное [адаптивное управление трафиком](../../../../ingest-from/dynatrace-oneagent/adaptive-traffic-management.md "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume.") во всей среде мониторинга, снижающее объём трассировок IBM MQ.
* Точный и непрерывный поток сервисов без необходимости настройки маппинга IBM MQ, когда сообщения обрабатываются исключительно через IBM App Connect Enterprise и IBM Integration Bus.

Как создать заголовок MQRFH2, если он отсутствует в моих сообщениях IBM MQ?

Когда заголовок `MQRFH2` присутствует в сообщениях до вызова узла `MQOutput` в IBM App Connect Enterprise или IBM Integration Bus, Dynatrace использует [идентификаторы вместо уникальных ключей](../queue-concepts.md#producer-consumer-service "Basic concepts of message queue monitoring in Dynatrace.") для трассировки сообщений IBM MQ.

Если в вашей среде это не так, вы можете создать пустой заголовок `MQRFH2`, например, выполнив следующую ESQL-команду в предшествующем узле `Compute`:

```
CREATE LASTCHILD of OutputRoot DOMAIN 'MQRFH2';
```

Для Dynatrace пустого заголовка `MQRFH2` достаточно, чтобы автоматически создать папку `usr` и добавить в неё идентификаторы Dynatrace. Если папка `usr` уже существует, Dynatrace повторно использует её.

Спецификации

* Dynatrace создаёт папку `usr` внутри существующего заголовка `MQRFH2`, а не сам заголовок `MQRFH2`.
* При создании папки `usr` Dynatrace добавляет её в начало заголовка `MQRFH2`.
* Если папка `usr` существует, Dynatrace добавляет свои идентификаторы в начало папки `usr`.

## Управление конфигурацией IBM MQ

Вы можете управлять конфигурацией IBM MQ автоматически, установив [расширение IBM MQ](../../../../ingest-from/extensions.md "Learn how to create and manage Dynatrace Extensions.") и активировав **Retrieve topology for improved transaction tracing** для получения конфигурации IBM MQ вашей среды и отправки её в Settings API. Это также можно сделать вручную через веб-интерфейс или Settings API.

### Ручная настройка через веб-интерфейс

Для управления конфигурацией IBM MQ через веб-интерфейс Dynatrace перейдите в **Settings** > **Mainframe**, где доступны следующие пункты меню:

* IBM MQ queue managers
* IBM MQ queue sharing groups
* IBM MQ IMS bridges

### Ручная настройка через Settings API

Вы можете управлять конфигурацией IBM MQ через [Settings API](../../../../dynatrace-api/environment-api/settings.md "Find out what the Dynatrace Settings API offers.") Dynatrace.

Для использования API вам потребуется токен доступа с областями действия **Read settings** (`settings.read`) и **Write settings** (`settings.write`). Чтобы узнать, как его получить, см. [Create an access token](../../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.").

## Элементы конфигурации

В таблице перечислены доступные элементы конфигурации IBM MQ для очередей и тем.

Следуйте приведённым ниже процедурам для создания или обновления элемента конфигурации. Обратите внимание, что область действия этих элементов всегда является средой. Перед началом изучите формат объекта настроек, запросив его схему через вызов [GET a schema](../../../../dynatrace-api/environment-api/settings/schemas/get-schema.md "View a settings schema via the Dynatrace API.").

Создание элемента конфигурации

Обновление существующего элемента конфигурации

### Новый менеджер очередей

Идентификатор схемы менеджера очередей: `builtin:ibmmq.queue-managers`.

1. Создайте JSON-объект для ваших настроек.

   Объект `aliasQueues` может быть локальной очередью, принадлежащей этому менеджеру очередей, локальным определением удалённой очереди или кластерной очередью, видимой этим менеджером очередей, но принадлежащей другому менеджеру очередей.

   Пример JSON

   ```
   [
   {
   "schemaId": "builtin:ibmmq.queue-managers",
   "scope": "environment",
   "value": {
   "name": "Queue Manager 1",
   "clusters": [
   "Name of the cluster this Queue Manager 1 is part of"
   ],
   "aliasQueues": [
   {
   "aliasQueue": "Alias Queue",
   "baseQueue": "Base queue which the Alias Queue should point to",
   "clusterVisibility": [
   "Name of a cluster this Alias Queue should be visible in (the queue manager must be part of this cluster)"
   ]
   }
   ],
   "remoteQueues": [
   {
   "localQueue": "Local definition of the Remote Queue",
   "remoteQueue": "Remote Queue",
   "remoteQueueManager": "Remote Queue Manager",
   "clusterVisibility": [
   "Name of a cluster this local definition of the Remote Queue should be visible in (the queue manager must be part of this cluster)"
   ]
   }
   ],
   "clusterQueues": [
   {
   "localQueue": "Local Queue",
   "clusterVisibility": [
   "Name of a cluster this Local Queue should be visible in (the queue manager must be part of this cluster)"
   ]
   }
   ]
   }
   }
   ]
   ```
2. Используйте эндпоинт [POST an object](../../../../dynatrace-api/environment-api/settings/objects/post-object.md "Create or validate a settings object via the Dynatrace API.") для отправки вашей конфигурации.

### Новая группа совместного использования очередей

Идентификатор схемы группы совместного использования очередей: `builtin:ibmmq.queue-sharing-group`.

1. Создайте JSON-объект для ваших настроек.

   Пример JSON

   ```
   [
   {
   "schemaId": "builtin:ibmmq.queue-sharing-group",
   "scope": "environment",
   "value": {
   "name": "Queue Sharing Group",
   "queueManagers": [
   "Queue Manager 1",
   "Queue Manager 2"
   ],
   "sharedQueues": [
   "Shared Queue 1",
   "Shared Queue 2"
   ]
   }
   }
   ]
   ```
2. Используйте эндпоинт [POST an object](../../../../dynatrace-api/environment-api/settings/objects/post-object.md "Create or validate a settings object via the Dynatrace API.") для отправки вашей конфигурации.

### Новый мост IMS

Идентификатор схемы моста IMS: `builtin:ibmmq.ims-bridges`.

1. Создайте JSON-объект для ваших настроек.

   Пример JSON

   ```
   [
   {
   "schemaId": "builtin:ibmmq.ims-bridges",
   "scope": "environment",
   "value": {
   "name": "IMS Bridge",
   "queueManagers": [
   {
   "name": "Queue Manager",
   "queueManagerQueue": [
   "Queue 1",
   "Queue 2"
   ]
   }
   ]
   }
   }
   ]
   ```
2. Используйте эндпоинт [POST an object](../../../../dynatrace-api/environment-api/settings/objects/post-object.md "Create or validate a settings object via the Dynatrace API.") для отправки вашей конфигурации.

### Обновление менеджера очередей

Идентификатор схемы менеджера очередей: `builtin:ibmmq.queue-managers`.

Объект `aliasQueues` может быть локальной очередью, принадлежащей этому менеджеру очередей, локальным определением удалённой очереди или кластерной очередью, видимой этим менеджером очередей, но принадлежащей другому менеджеру очередей.

1. Запросите текущую конфигурацию через вызов [GET objects](../../../../dynatrace-api/environment-api/settings/objects/get-objects.md "View multiple settings objects via the Dynatrace API.").
2. Создайте JSON для обновления.

   * Используйте значение **updateToken** из предыдущего шага.
   * Измените значения по мере необходимости.

     Пример JSON

     ```
     {
     "updateToken": "vu9U3hXY3q0ATAAkMG",
     "value": {
     "name": "Queue Manager A",
     "clusters": [
     "Name of a cluster this Queue Manager A is part of"
     ],
     "aliasQueues": [
     {
     "aliasQueue": "Alias Queue",
     "baseQueue": "Base queue which the Alias Queue should point to",
     "clusterVisibility": [
     "Name of a cluster this Alias Queue should be visible in (the queue manager must be part of this cluster)"
     ]
     }
     ],
     "remoteQueues": [
     {
     "localQueue": "Local definition of the Remote Queue",
     "remoteQueue": "Remote Queue",
     "remoteQueueManager": "Remote Queue Manager",
     "clusterVisibility": [
     "Name of a cluster this local definition of the Remote Queue should be visible in (the queue manager must be part of this cluster)"
     ]
     }
     ],
     "clusterQueues": [
     {
     "localQueue": "Local Queue",
     "clusterVisibility": [
     "Name of a cluster this Local Queue should be visible in (the queue manager must be part of this cluster)"
     ]
     }
     ]
     }
     }
     ```
3. Используйте эндпоинт [PUT an object](../../../../dynatrace-api/environment-api/settings/objects/put-object.md "Edit a settings object via the Dynatrace API.") для отправки вашей конфигурации.

### Обновление группы совместного использования

Идентификатор схемы группы совместного использования очередей: `builtin:ibmmq.queue-sharing-group`.

1. Запросите текущую конфигурацию через вызов [GET objects](../../../../dynatrace-api/environment-api/settings/objects/get-objects.md "View multiple settings objects via the Dynatrace API.").
2. Создайте JSON для обновления.

   * Используйте значение **updateToken** из предыдущего шага.
   * Измените значения по мере необходимости.
     Пример JSON

     ```
     {
     "updateToken": "vu9U3hXY3q0ATAAkMG",
     "value": {
     "name": "Queue Sharing Group",
     "queueManagers": [
     "Queue Manager A",
     "Queue Manager B"
     ],
     "sharedQueues": [
     "Shared Queue A",
     "Shared Queue B"
     ]
     }
     }
     ```
3. Используйте эндпоинт [PUT an object](../../../../dynatrace-api/environment-api/settings/objects/put-object.md "Edit a settings object via the Dynatrace API.") для отправки вашей конфигурации.

### Обновление моста IMS

Идентификатор схемы моста IMS: `builtin:ibmmq.ims-bridges`.

1. Запросите текущую конфигурацию через вызов [GET objects](../../../../dynatrace-api/environment-api/settings/objects/get-objects.md "View multiple settings objects via the Dynatrace API.").
2. Создайте JSON для обновления.

   * Используйте значение **updateToken** из предыдущего шага.
   * Измените значения по мере необходимости.

     Пример JSON

     ```
     {
     "updateToken": "vu9U3hXY3q0ATAAkMG",
     "value": {
     "name": "IMS Bridge",
     "queueManagers": [
     {
     "name": "Queue Manager",
     "queueManagerQueue": [
     "Queue A",
     "Queue B"
     ]
     }
     ]
     }
     }
     ```
3. Используйте эндпоинт [PUT an object](../../../../dynatrace-api/environment-api/settings/objects/put-object.md "Edit a settings object via the Dynatrace API.") для отправки вашей конфигурации.

## Связанные темы

* [Set up IBM MQ tracing on z/OS](../../../../ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/ibm-mq-monitoring.md "Trace IBM MQ messages with Dynatrace on z/OS.")
