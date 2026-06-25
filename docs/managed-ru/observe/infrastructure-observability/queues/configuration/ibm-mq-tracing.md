---
title: Трассировка IBM MQ
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing
scraped: 2026-05-12T12:07:29.763711
---

# Трассировка IBM MQ

# Трассировка IBM MQ

* How-to guide
* 6-min read
* Updated on Jun 21, 2022

Dynatrace может автоматически создавать непрерывный [поток сервисов](/managed/observe/application-observability/services-classic/service-flow "Узнайте, как Dynatrace помогает трассировать последовательность вызовов сервисов, инициированных каждым запросом к сервису в вашей среде.") для IBM MQ, когда сервисы-производители и потребители используют одно и то же имя очереди или топика. Если сервисы-производители и потребители ссылаются на разные имена очередей или топиков, может потребоваться настройка IBM MQ для создания непрерывного потока сервисов.

Без настройки IBM MQ Dynatrace по-прежнему может трассировать все сообщения, однако поток сервисов будет прерван.

| Технология | Сообщение IBM MQ | Требуется настройка IBM MQ |
| --- | --- | --- |
| z/OS Java .NET |  | Применимо |
| IBM App Connect EnterpriseIBM Integration Bus | Папка `MQRFH2.usr` отсутствует  Папка `MQRFH2.usr` присутствует | Применимо  Не применимо |

Пример непрерывного потока сервисов IBM MQ

![Поток сервисов IBM MQ](https://dt-cdn.net/images/ibm-mq-service-flow-1938-06750bfc7d.png)

Поток сервисов IBM MQ

Пример распределённой трассировки IBM MQ

![Распределённая трассировка IBM MQ](https://dt-cdn.net/images/ibmmq-distributed-traces-3772-59101a2b00.png)

Распределённая трассировка IBM MQ

### ЧЗВ

Нужно ли создавать заголовок MQRFH2, если он отсутствует в сообщениях IBM MQ?

Рекомендуется создавать заголовок `MQRFH2` для сообщений IBM MQ. Наличие заголовка `MQRFH2` в сообщениях IBM MQ позволяет Dynatrace использовать [идентификаторы вместо уникальных ключей](/managed/observe/infrastructure-observability/queues/queue-concepts#producer-consumer-service "Основные концепции мониторинга очередей сообщений в Dynatrace.") для трассировки сообщений через очереди и топики IBM App Connect Enterprise и IBM Integration Bus.

Преимущества создания заголовка `MQRFH2` для сообщений IBM MQ включают:

* Последовательное [Adaptive Traffic Management](/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed "Улучшение состояния и производительности среды Dynatrace Managed с помощью адаптивных функций управления трафиком, снижения нагрузки и управления захватом.") во всей среде мониторинга, снижающее объём трассировок IBM MQ.
* Точный и непрерывный поток сервисов без необходимости настройки сопоставления IBM MQ, когда сообщения обрабатываются исключительно IBM App Connect Enterprise и IBM Integration Bus.

Как создать заголовок MQRFH2, если он отсутствует в сообщениях IBM MQ?

Когда заголовок `MQRFH2` присутствует в сообщениях до вызова узла `MQOutput` в IBM App Connect Enterprise или IBM Integration Bus, Dynatrace использует [идентификаторы вместо уникальных ключей](/managed/observe/infrastructure-observability/queues/queue-concepts#producer-consumer-service "Основные концепции мониторинга очередей сообщений в Dynatrace.") для трассировки сообщений IBM MQ.

Если это не так в вашей среде, можно создать пустой заголовок `MQRFH2`, например выполнив следующую команду ESQL через предшествующий узел `Compute`:

```
CREATE LASTCHILD of OutputRoot DOMAIN 'MQRFH2';
```

Для Dynatrace пустого заголовка `MQRFH2` достаточно для автоматического создания папки `usr` и добавления в неё идентификаторов Dynatrace. Если папка `usr` уже существует, Dynatrace повторно её использует.

Спецификации

* Dynatrace создаёт папку `usr` внутри существующего заголовка `MQRFH2`, а не сам заголовок `MQRFH2`.
* При создании папки `usr` Dynatrace добавляет её в начало заголовка `MQRFH2`.
* Если папка `usr` существует, Dynatrace добавляет свои идентификаторы в её начало.

## Управление конфигурацией IBM MQ

Управлять конфигурацией IBM MQ можно автоматически, установив [расширение IBM MQ](/managed/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace и управлять ими.") и активировав **Retrieve topology for improved transaction tracing** для получения конфигурации IBM MQ вашей среды и отправки её в Settings API. Это также можно сделать вручную через веб-интерфейс или Settings API.

### Ручная настройка через веб-интерфейс

Для управления конфигурацией IBM MQ через веб-интерфейс Dynatrace перейдите в **Settings** > **Mainframe**, где можно найти следующие пункты меню:

* IBM MQ queue managers
* IBM MQ queue sharing groups
* IBM MQ IMS bridges

### Ручная настройка через Settings API

Управлять конфигурацией IBM MQ можно через Dynatrace [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.").

Для использования API необходим токен доступа с областями действия **Read settings** (`settings.read`) и **Write settings** (`settings.write`). Чтобы узнать, как его получить, см. раздел [Создание токена доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

## Элементы конфигурации

В таблице перечислены доступные элементы конфигурации IBM MQ для очередей и топиков.

| Элемент | Описание | Ваши действия |
| --- | --- | --- |
| Менеджер очередей | Менеджер очередей со своими очередями | Определите менеджеры очередей, включая очереди-псевдонимы, удалённые очереди и кластерные очереди в рамках одного элемента конфигурации. |
| Группа совместных очередей z/OS | Группа менеджеров очередей, имеющих доступ к одним и тем же совместным очередям | Укажите, какие менеджеры очередей и совместные очереди принадлежат группе совместных очередей в рамках одного элемента конфигурации. |
| Мост IMS z/OS | Компонент IBM MQ, обеспечивающий прямой доступ к системе IMS | Укажите, какие менеджеры очередей и очереди принадлежат мосту IMS в рамках одного элемента конфигурации. |

Выполните приведённые ниже процедуры для создания или обновления элемента конфигурации. Обратите внимание, что область действия этих элементов всегда является окружением. Перед началом ознакомьтесь с форматом объекта настроек, запросив его схему через вызов [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотр схемы настроек через Dynatrace API.").

Создание элемента конфигурации

Обновление существующего элемента конфигурации

### Новый менеджер очередей

Идентификатор схемы менеджера очередей: `builtin:ibmmq.queue-managers`.

1. Создайте JSON-объект для ваших настроек.

   Объект `aliasQueues` может быть локальной очередью, принадлежащей данному менеджеру очередей, локальным определением удалённой очереди или кластерной очередью, видимой данным менеджером очередей, но принадлежащей другому менеджеру.

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
2. Используйте конечную точку [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создание или проверка объекта настроек через Dynatrace API.") для отправки конфигурации.

### Новая группа совместных очередей

Идентификатор схемы группы совместных очередей: `builtin:ibmmq.queue-sharing-group`.

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
2. Используйте конечную точку [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создание или проверка объекта настроек через Dynatrace API.") для отправки конфигурации.

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
2. Используйте конечную точку [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создание или проверка объекта настроек через Dynatrace API.") для отправки конфигурации.

### Обновление менеджера очередей

Идентификатор схемы менеджера очередей: `builtin:ibmmq.queue-managers`.

Объект `aliasQueues` может быть локальной очередью, принадлежащей данному менеджеру очередей, локальным определением удалённой очереди или кластерной очередью, видимой данным менеджером, но принадлежащей другому менеджеру очередей.

1. Запросите текущую конфигурацию через вызов [GET objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких объектов настроек через Dynatrace API.").
2. Создайте JSON для вашего обновления.

   * Используйте значение **updateToken** из предыдущего шага.
   * При необходимости измените значения.

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
3. Используйте конечную точку [PUT an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Редактирование объекта настроек через Dynatrace API.") для отправки конфигурации.

### Обновление группы совместных очередей

Идентификатор схемы группы совместных очередей: `builtin:ibmmq.queue-sharing-group`.

1. Запросите текущую конфигурацию через вызов [GET objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких объектов настроек через Dynatrace API.").
2. Создайте JSON для вашего обновления.

   * Используйте значение **updateToken** из предыдущего шага.
   * При необходимости измените значения.
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
3. Используйте конечную точку [PUT an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Редактирование объекта настроек через Dynatrace API.") для отправки конфигурации.

### Обновление моста IMS

Идентификатор схемы моста IMS: `builtin:ibmmq.ims-bridges`.

1. Запросите текущую конфигурацию через вызов [GET objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких объектов настроек через Dynatrace API.").
2. Создайте JSON для вашего обновления.

   * Используйте значение **updateToken** из предыдущего шага.
   * При необходимости измените значения.

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
3. Используйте конечную точку [PUT an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Редактирование объекта настроек через Dynatrace API.") для отправки конфигурации.

## Связанные темы

* [Настройка трассировки IBM MQ на z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/ibm-mq-monitoring "Трассировка сообщений IBM MQ с помощью Dynatrace на z/OS.")