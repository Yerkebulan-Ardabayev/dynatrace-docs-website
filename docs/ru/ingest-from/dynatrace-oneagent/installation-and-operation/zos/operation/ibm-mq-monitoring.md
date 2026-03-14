---
title: Настройка трассировки IBM MQ на z/OS
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/ibm-mq-monitoring
scraped: 2026-03-06T21:37:49.354494
---

# Настройка трассировки IBM MQ на z/OS

# Настройка трассировки IBM MQ на z/OS

* Последняя версия Dynatrace
* Время чтения: 1 мин
* Обновлено 16 мая 2022 г.

С помощью Dynatrace вы можете обеспечить наблюдаемость для IBM MQ на z/OS:

* Модули CICS, IMS и z/OS Java могут трассировать сообщения в ваших приложениях, инициированные клиентами IBM MQ, включая их сервисы-производители и сервисы-потребители на разных уровнях. Подробнее об очередях сообщений в Dynatrace см. в разделе [Очереди](../../../../../observe/infrastructure-observability/queues.md "Monitor and analyze your message queues with Dynatrace.").
* Расширение ActiveGate может собирать метрики с серверов IBM MQ. Подробнее об этом см. в разделе [Расширение IBM MQ ActiveGate](../../../../extensions.md "Learn how to create and manage Dynatrace Extensions.").

## Трассировка

Dynatrace может автоматически создавать непрерывный [поток сервисов](../../../../../observe/application-observability/services-classic/service-flow.md "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") для IBM MQ, когда сервисы-производители и сервисы-потребители используют одно и то же имя очереди или темы. Если сервисы-производители и сервисы-потребители ссылаются на разные имена очередей или тем, для создания непрерывного потока сервисов может потребоваться настройка IBM MQ.

Без настройки IBM MQ Dynatrace всё равно может трассировать все сообщения, однако поток сервисов будет прерван.

В таблице перечислены доступные элементы конфигурации IBM MQ для очередей и тем.

## Управление конфигурацией IBM MQ

Вы можете автоматически управлять конфигурацией IBM MQ, установив [расширение IBM MQ](../../../../extensions.md "Learn how to create and manage Dynatrace Extensions.") и активировав параметр **Retrieve topology for improved transaction tracing**, чтобы получить конфигурацию IBM MQ вашей среды и отправить её в Settings API. Это также можно выполнить вручную через веб-интерфейс или Settings API.

### Ручная настройка через веб-интерфейс

Для управления конфигурацией IBM MQ через веб-интерфейс Dynatrace перейдите в **Settings** > **Mainframe**, где доступны следующие пункты меню:

* Менеджеры очередей IBM MQ
* Группы совместного использования очередей IBM MQ
* Мосты IBM MQ IMS

### Ручная настройка через Settings API

Вы можете управлять конфигурацией IBM MQ через [Settings API](../../../../../dynatrace-api/environment-api/settings.md "Find out what the Dynatrace Settings API offers.") Dynatrace.

Для использования API необходим токен доступа с областями **Read settings** (`settings.read`) и **Write settings** (`settings.write`). Чтобы узнать, как его получить, см. раздел [Создание токена доступа](../../../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.").

Settings API для трассировки IBM MQ:

* [Создание конфигурации менеджера очередей](../../../../../observe/infrastructure-observability/queues/configuration/ibm-mq-tracing.md#qm-api-create "Configure Dynatrace for IBM MQ tracing.")
* [Обновление конфигурации менеджера очередей](../../../../../observe/infrastructure-observability/queues/configuration/ibm-mq-tracing.md#qm-api-update "Configure Dynatrace for IBM MQ tracing.")
* [Создание конфигурации группы совместного использования очередей](../../../../../observe/infrastructure-observability/queues/configuration/ibm-mq-tracing.md#qsg-api-create "Configure Dynatrace for IBM MQ tracing.")
* [Обновление конфигурации группы совместного использования очередей](../../../../../observe/infrastructure-observability/queues/configuration/ibm-mq-tracing.md#qsg-api-update "Configure Dynatrace for IBM MQ tracing.")
* [Создание конфигурации моста IMS](../../../../../observe/infrastructure-observability/queues/configuration/ibm-mq-tracing.md#ims-bridge-api-create "Configure Dynatrace for IBM MQ tracing.")
* [Обновление конфигурации моста IMS](../../../../../observe/infrastructure-observability/queues/configuration/ibm-mq-tracing.md#ims-bridge-api-update "Configure Dynatrace for IBM MQ tracing.")

## Связанные темы

* [Трассировка IBM MQ](../../../../../observe/infrastructure-observability/queues/configuration/ibm-mq-tracing.md "Configure Dynatrace for IBM MQ tracing.")
