---
title: Настройка трассировки IBM MQ на z/OS
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/ibm-mq-monitoring
scraped: 2026-05-12T12:14:19.097486
---

# Настройка трассировки IBM MQ на z/OS

# Настройка трассировки IBM MQ на z/OS

* Чтение: 1 мин
* Обновлено 16 мая 2022 г.

С Dynatrace можно получить наблюдаемость для IBM MQ на z/OS:

* Модули CICS, IMS и z/OS Java могут трассировать сообщения в ваших приложениях, инициируемые клиентами IBM MQ, включая их сервисы-производители и сервисы-потребители на разных уровнях. Чтобы узнать больше об очередях сообщений в Dynatrace, см. [Очереди](/managed/observe/infrastructure-observability/queues "Мониторинг и анализ ваших очередей сообщений с Dynatrace.").
* Расширение ActiveGate может собирать метрики с серверов IBM MQ. Подробнее см. [Расширение ActiveGate для IBM MQ](/managed/ingest-from/extensions "Узнайте, как создавать и управлять расширениями Dynatrace.").

## Трассировка

Dynatrace может автоматически создавать непрерывный [service flow](/managed/observe/application-observability/services-classic/service-flow "Узнайте, как Dynatrace помогает проследить последовательность вызовов сервисов, инициируемых каждым запросом сервиса в вашем окружении.") для IBM MQ, когда сервисы-производители и сервисы-потребители используют одно и то же имя очереди или топика. Если сервисы-производители и сервисы-потребители ссылаются на разные имена очередей или топиков, для создания непрерывного service flow может потребоваться настройка IBM MQ.

Без настройки IBM MQ Dynatrace всё равно может трассировать все сообщения, но service flow будет прерывистым.

Таблица перечисляет доступные элементы конфигурации IBM MQ для очередей и топиков.

| Элемент | Описание | Ваше действие |
| --- | --- | --- |
| Queue manager | Менеджер очередей со своими очередями | Определите своих менеджеров очередей, включая псевдонимы очередей, удалённые очереди и кластерные очереди в одном элементе конфигурации. |
| z/OS Queue sharing group | Группа менеджеров очередей, имеющих доступ к одним и тем же общим очередям | Укажите, какие менеджеры очередей и общие очереди принадлежат группе совместного использования очередей в одном элементе конфигурации. |
| z/OS IMS bridge | Компонент IBM MQ, обеспечивающий прямой доступ к системе IMS | Укажите, какие менеджеры очередей и очереди относятся к мосту IMS в одном элементе конфигурации. |

## Управление конфигурацией IBM MQ

Конфигурацией IBM MQ можно управлять автоматически, установив [расширение IBM MQ](/managed/ingest-from/extensions "Узнайте, как создавать и управлять расширениями Dynatrace.") и активировав **Retrieve topology for improved transaction tracing**, чтобы получить конфигурацию IBM MQ вашего окружения и отправить её в Settings API. Это также можно сделать вручную через веб-интерфейс или Settings API.

### Ручная настройка через веб-интерфейс

Чтобы управлять конфигурацией IBM MQ через веб-интерфейс Dynatrace, перейдите в **Settings** > **Mainframe** и найдите следующие пункты меню:

* IBM MQ queue managers
* IBM MQ queue sharing groups
* IBM MQ IMS bridges

### Ручная настройка через Settings API

Конфигурацией IBM MQ можно управлять через [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Settings API Dynatrace.") Dynatrace.

Чтобы использовать API, нужен токен доступа со скоупами **Read settings** (`settings.read`) и **Write settings** (`settings.write`). Чтобы узнать, как его получить, см. [Создание токена доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API.").

Settings API для трассировки IBM MQ:

* [Создание конфигурации менеджера очередей](/managed/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qm-api-create "Настройка Dynatrace для трассировки IBM MQ.")
* [Обновление конфигурации менеджера очередей](/managed/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qm-api-update "Настройка Dynatrace для трассировки IBM MQ.")
* [Создание конфигурации группы совместного использования очередей](/managed/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qsg-api-create "Настройка Dynatrace для трассировки IBM MQ.")
* [Обновление конфигурации группы совместного использования очередей](/managed/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#qsg-api-update "Настройка Dynatrace для трассировки IBM MQ.")
* [Создание конфигурации моста IMS](/managed/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#ims-bridge-api-create "Настройка Dynatrace для трассировки IBM MQ.")
* [Обновление конфигурации моста IMS](/managed/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing#ims-bridge-api-update "Настройка Dynatrace для трассировки IBM MQ.")

## Связанные темы

* [Трассировка IBM MQ](/managed/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing "Настройка Dynatrace для трассировки IBM MQ.")