---
title: Поддерживаемые схемы подключения для ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates
scraped: 2026-05-12T11:08:07.634086
---

# Поддерживаемые схемы подключения для ActiveGate

# Поддерживаемые схемы подключения для ActiveGate

* 4-min read
* Published Jul 17, 2018

ActiveGate можно использовать в **[схеме подключения Dynatrace Managed](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates#managed-scheme "Узнайте о приоритетах подключения между типами ActiveGate и приоритетах между ActiveGate и OneAgent.")**. Схема подключения Dynatrace Managed может быть развёрнута в нескольких различных **[сценариях развёртывания](/managed/managed-cluster/basics/managed-deployments "Поймите, как развёртывания Dynatrace Managed развиваются от базовой внутренней конфигурации до глобально распределённой высокодоступной архитектуры.")**.

Dynatrace требует, чтобы определённые порты и пути были открыты и доступны через мониторируемую инфраструктуру, брандмауэры и другие компоненты. Порты [настраиваемы](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#com-compuware-apm-webserver "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."), а их значения по умолчанию показаны ниже.

## Схема подключения Dynatrace Managed

Все возможные подключения для схемы подключения Dynatrace Managed — во всех возможных сценариях развёртывания — показаны ниже на одной диаграмме.

**Сплошные стрелки** обозначают предпочтительные пути. Например, OneAgent будет подключаться к Environment ActiveGate, если таковой имеется. Однако он подключится к Cluster ActiveGate, если подключение к Environment ActiveGate невозможно, и даже может подключиться напрямую к кластеру Dynatrace Managed.
**Направление стрелок** на диаграммах указывает, какой компонент инициирует соединение.

![Схема подключения Dynatrace Managed](https://dt-cdn.net/images/connectivity-managed-005-1200-04934824a0.png)

Схема подключения Dynatrace Managed

## Использование портов

* Environment ActiveGate принимает подключения на порту 9999.

* Cluster ActiveGate принимает подключения на порту 9999.
* Кластер Dynatrace Managed (встроенный ActiveGate) принимает подключения на порту 443.
  Подробнее смотрите на диаграммах выше.

При запуске [Browser monitors](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.") или [HTTP monitors](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Узнайте, как настроить HTTP-монитор для проверки производительности и доступности вашего сайта.") из частных синтетических расположений необходимо убедиться, что ActiveGate с включённым Synthetic имеет доступ к тестируемому ресурсу. При использовании расширений ActiveGate необходимо убедиться, что ActiveGate, выполняющий расширения, имеет доступ к мониторируемой технологии.

Для Dynatrace Managed ActiveGate также должен иметь сетевой доступ к другим сервисам на определённых портах в зависимости от вашего [сценария развёртывания](/managed/managed-cluster/basics/managed-deployments "Поймите, как развёртывания Dynatrace Managed развиваются от базовой внутренней конфигурации до глобально распределённой высокодоступной архитектуры.").

## Иерархия подключений

ActiveGate существуют в следующей иерархии:

* Уровень 1 — Environment ActiveGate
* Уровень 2 — Cluster ActiveGate
* Уровень 3 — Встроенные ActiveGate (ActiveGate, встроенные в узлы кластера, не показаны на графиках выше).

ActiveGate может отправлять данные только на более высокие уровни иерархии. Отправка данных на тот же или более низкий уровень иерархии невозможна.

Environment ActiveGate по умолчанию подключаются напрямую к кластеру Dynatrace (если не используются пользовательские сетевые зоны). Это исключает промежуточный шаг подключения к Cluster ActiveGate. Подключение через Cluster ActiveGate необходимо, если кластер Dynatrace недоступен напрямую. Например, если Environment ActiveGate находится в другой сети или другом центре обработки данных.

Подключаемость также может зависеть от **[сетевых зон](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.")** при их настройке. Настройка сетевой зоны означает, что ActiveGate и OneAgent будут предпочитать взаимодействовать с ActiveGate из той же зоны, прежде чем подключаться к ActiveGate за пределами активной зоны.

## Настройка прокси и балансировщика нагрузки

Все компоненты Dynatrace (OneAgent, ActiveGate, кластер Dynatrace) обнаруживают свои имена хостов и распространяют их как конечные точки связи между собой для достижения максимальной устойчивости соединения.
Это работает автоматически, если в вашем окружении нет сетевых устройств (прокси, балансировщиков нагрузки), о которых Dynatrace не знает.

На диаграмме ниже показаны все возможные размещения прокси и балансировщика нагрузки (обратного прокси) для развёртывания ActiveGate. Для простоты прямые подключения — те, что не через прокси или балансировщики нагрузки, — не показаны. Альтернативные соединения (через один или несколько прокси или балансировщиков нагрузки) показаны пунктирными линиями.

* При наличии балансировщика нагрузки между OneAgent и ActiveGate следует указать адрес балансировщика нагрузки как свойство [`dnsEntryPoint`](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent "Настройте свойства ActiveGate для установки обратного прокси или балансировщика нагрузки для OneAgent.") в конфигурации ActiveGate.
* При наличии балансировщика нагрузки между ActiveGate и следующей конечной точкой связи, через которую должен маршрутизироваться трафик, настройте [`seedServerUrl` и `ignoreClusterRuntimeInfo`](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Узнайте, как настроить свойства ActiveGate для установки обратного прокси или балансировщика нагрузки.").
* При использовании прокси для доступа к кластеру Dynatrace или любому из мониторируемых облаков [настройте прокси](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Узнайте, как настроить свойства ActiveGate для установки прокси.").

![Размещения прокси и балансировщика нагрузки для развёртываний ActiveGate](https://dt-cdn.net/images/proxy-rev-proxy-005-1018-c916f384ca.png)

Размещения прокси и балансировщика нагрузки для развёртываний ActiveGate

## Заголовки ActiveGate

Вы можете настроить заголовки ActiveGate в брандмауэре.

| Заголовок | Значение |
| --- | --- |
| `User-Agent` | Environment ActiveGate: `ruxit/<dynatrace-version> <activegate-instance-id> <environment-id>`. HTTP monitors: `DynatraceSynthetic/<dynatrace-version>`. Browser monitors: `RuxitSynthetic/<dynatrace-version>` |
| `dynatrace-gateway-type` | Environment ActiveGate: `PRIVATE`. Managed or SaaS ActiveGate: `PUBLIC`. Cluster ActiveGate: `PUBLIC_MANAGED`. Multi-environment ActiveGate: `MULTI_TENANT` |
| `Authorization` | `Basic <TOKEN>` |

## Связанные темы

* [Сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.")