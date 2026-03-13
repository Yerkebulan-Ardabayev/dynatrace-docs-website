---
title: Relationship between the New RUM Experience and RUM Classic
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/relationship-to-rum-classic
scraped: 2026-02-23T21:26:20.516474
---

# Взаимосвязь между новым RUM Experience и RUM Classic

# Взаимосвязь между новым RUM Experience и RUM Classic

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Jan 23, 2026

Новый RUM Experience в настоящее время опирается на определённые функции RUM Classic. Вот что это означает для вас.

#### Включение нового RUM Experience

На данный момент новый RUM Experience можно включить только при активном RUM Classic. В настоящее время отключение приёма данных в RUM Classic и полная миграция невозможны.

#### Конфигурация

Большинство параметров конфигурации нового RUM Experience основаны на параметрах, уже используемых в RUM Classic. Это означает, что:

* Изменения, внесённые в новом RUM Experience, также применяются к RUM Classic.
* И наоборот: если вы изменяете настройки в RUM Classic, которые также доступны в новом RUM Experience, эти изменения будут применены и там.

Свойства событий и сессий являются исключением — они имеют отдельную конфигурацию от свойств действий пользователей и сессий в RUM Classic.

#### Мониторинг трафика

Когда новый RUM Experience включён, RUM-маяки в новом формате отправляются вместе с маяками RUM Classic на тот же конечный адрес.

#### Требования к инфраструктуре

На данный момент новый RUM Experience опирается только на HTTP-заголовки и файлы cookie, уже охватываемые [ограничениями брандмауэра для RUM Classic](/docs/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum "Find out how to make sure that Real User Monitoring data passes through your firewall."). Если ваши брандмауэры и другие компоненты инфраструктуры уже настроены для пропуска этих заголовков и файлов cookie, при включении нового RUM Experience никаких дополнительных изменений не потребуется.

## Связанные темы

* [Capture event and session properties for web frontends](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/event-and-session-properties "Learn how to capture event and session properties for web frontends.")
* [Capture event and session properties for mobile frontends](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/additional-configuration/event-and-session-properties "Learn how to capture event and session properties for mobile frontends.")
* [Firewall constraints for RUM](/docs/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum "Find out how to make sure that Real User Monitoring data passes through your firewall.")
