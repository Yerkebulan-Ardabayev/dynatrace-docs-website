---
title: Поддерживаемые схемы подключения для ActiveGate
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates
scraped: 2026-03-06T21:25:14.270507
---

# Поддерживаемые схемы подключения для ActiveGates


* Latest Dynatrace
* 4-min read

Dynatrace требует, чтобы определённые порты и пути были открыты и доступны через отслеживаемую инфраструктуру, межсетевые экраны и другие компоненты. Порты [настраиваемы](configuration/configure-activegate.md#com-compuware-apm-webserver "Узнайте, какие свойства ActiveGate можно настроить в соответствии с вашими потребностями и требованиями."), а значения по умолчанию указаны ниже.

## Схема подключения Dynatrace SaaS

Ниже показаны все возможные соединения для схемы подключения SaaS с предпочтительными и альтернативными путями.

**Сплошные стрелки** указывают предпочтительные пути. Например, OneAgent будет подключаться к Environment ActiveGate, если он присутствует. Однако он подключится напрямую к кластеру Dynatrace SaaS, если подключение к Environment ActiveGate невозможно.
**Направление стрелок** на диаграммах указывает, какой компонент инициирует соединение.

![Dynatrace SaaS connectivity scheme](https://dt-cdn.net/images/connectivity-saas-003-1200-822497778d.png)

## Использование портов

* Environment ActiveGate принимает соединения на порту 9999.

* Кластер Dynatrace SaaS принимает соединения на порту 443.

Если вы запускаете [Browser monitors](../../observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location.md "Узнайте, как создать частное расположение для синтетического мониторинга.") или [HTTP monitors](../../observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic.md "Узнайте, как настроить HTTP-монитор для проверки производительности и доступности вашего сайта.") из частных расположений Synthetic, необходимо убедиться, что ActiveGate с поддержкой Synthetic имеет доступ к тестируемому ресурсу. Если вы используете расширения ActiveGate, необходимо убедиться, что ActiveGate, выполняющий расширения, имеет доступ к отслеживаемой технологии.

Соединение

Конфигурация **[сетевых зон](../../manage/network-zones.md "Узнайте, как работают сетевые зоны в Dynatrace.")** означает, что OneAgents предпочтут устанавливать соединение с ActiveGates из той же зоны, прежде чем подключаться к ActiveGates за пределами активной зоны.

## Конфигурация прокси и балансировщика нагрузки

Все компоненты Dynatrace (OneAgents, ActiveGates, кластер Dynatrace) определяют свои имена хостов и распределяют их в качестве конечных точек связи между собой для достижения максимально возможной надёжности соединения.
Это работает автоматически, если в вашей среде нет сетевых устройств (прокси, балансировщиков нагрузки), о которых Dynatrace не знает и которые необходимо учитывать.

На диаграмме ниже показаны все возможные расположения прокси и балансировщика нагрузки (обратного прокси) для развёртывания ActiveGate. Для простоты прямые соединения — те, которые не проходят через прокси или балансировщики нагрузки — не показаны на этой диаграмме. Альтернативные соединения (те, которые проходят через один или несколько прокси или балансировщиков нагрузки) показаны пунктирными линиями.

* Если между OneAgents и ActiveGate находится балансировщик нагрузки, необходимо указать адрес балансировщика нагрузки в качестве свойства [`dnsEntryPoint`](configuration/set-up-reverse-proxy-for-oneagent.md "Настройте свойства ActiveGate для настройки обратного прокси или балансировщика нагрузки для OneAgent.") в конфигурации ActiveGate.
* Если между ActiveGate и следующей конечной точкой связи, через которую должен маршрутизироваться трафик, находится балансировщик нагрузки, настройте [`seedServerUrl` и `ignoreClusterRuntimeInfo`](configuration/set-up-reverse-proxy-for-activegate.md "Узнайте, как настроить свойства ActiveGate для настройки обратного прокси или балансировщика нагрузки.").
* Если прокси используется для доступа к кластеру Dynatrace или к любому из отслеживаемых облаков, [настройте прокси](configuration/set-up-proxy-authentication-for-activegate.md "Узнайте, как настроить свойства ActiveGate для настройки прокси.").

![Proxy and load balancer placements for ActiveGate deployments](https://dt-cdn.net/images/proxy-rev-proxy-005-1018-c916f384ca.png)

## Заголовки ActiveGate

Вы можете настроить заголовки ActiveGate в своём межсетевом экране.

1

Примеры значений:
**Environment и Multi-environment ActiveGate**: `ruxit/1.229.163.20211109-103203 0x37badd8e c04442b4-7ea6-4ec4-a5c4-7f94c7cf25fa`.
**Cluster ActiveGate**: `ruxit/1.229.163.20211109-103203 0x37badd8e`.

2

Пример значения:
`DynatraceSynthetic/1.258.0.20221207-142354`.

3

Пример значения:
`Mozilla/5.0 (Windows NT 6.3;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36 RuxitSynthetic/1.258.0.20221207-142354`.

## Связанные темы

* [Сетевые зоны](../../manage/network-zones.md "Узнайте, как работают сетевые зоны в Dynatrace.")
