---
title: Переход с RUM Classic на новый функционал RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/transition-from-rum-classic
scraped: 2026-03-06T21:25:59.818788
---

# Переход с RUM Classic на новый функционал RUM Experience

# Переход с RUM Classic на новый функционал RUM Experience

* Последняя Dynatrace
* Описание
* 1 мин. чтения
* Обновлено 20 февраля 2026 г.

Если вы уже мониторите ваши веб- и мобильные фронтенды с помощью RUM Classic, переход на новый функционал RUM Experience не составит труда. Узнайте, как новый RUM Experience соотносится с RUM Classic и как его включить.

## Включение нового RUM Experience

Переход с RUM Classic на новый RUM Experience требует лишь изменения конфигурации. Следующие руководства описывают необходимые шаги.

[Web](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/enable-new-rum-for-web-apps) [Android](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/android/id-01-initial-setup) [iOS](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/ios/id-01-initial-setup) [React Native](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/react-native/id-01-initial-setup) [Flutter](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/flutter/id-01-initial-setup) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/maui/id-01-initial-setup) 

## Связь между новым RUM Experience и RUM Classic

Новый RUM Experience в настоящее время опирается на определённые функции RUM Classic. Вот что это означает для вас.

#### Включение нового RUM Experience

В настоящее время вы можете включить новый RUM Experience, только если RUM Classic активен. На данный момент отключение приёма данных в RUM Classic и полная миграция невозможны.

#### Конфигурация

Большинство настроек конфигурации нового RUM Experience основаны на тех, которые уже используются RUM Classic. Это означает, что:

* Изменения, сделанные в новом RUM Experience, также применяются к RUM Classic.
* И наоборот: если вы изменяете настройки в RUM Classic, которые также доступны в новом RUM Experience, эти изменения будут применены и там.

Свойства событий и сессий являются исключением — они имеют отдельную конфигурацию от свойств пользовательских действий и сессий в RUM Classic.

#### Мониторинг трафика

При включённом новом RUM Experience RUM-биконы в новом формате отправляются наряду с RUM Classic биконами на ту же конечную точку.

#### Требования к инфраструктуре

На данный момент новый RUM Experience опирается только на HTTP-заголовки и cookie, уже включённые в [ограничения файервола для RUM Classic](/docs/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum "Убедитесь, что данные мониторинга реальных пользователей проходят через ваш файервол."). Если ваши файерволы и другие компоненты инфраструктуры уже настроены для пропуска этих заголовков и cookie, дальнейшие изменения при включении нового RUM Experience не требуются.

#### Встроенные метрики

Новый RUM Experience предоставляет множество встроенных метрик. Из-за другой базовой модели данных они не являются прямыми эквивалентами [метрик RUM Classic](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#applications "Изучите полный список встроенных метрик Dynatrace."). Тем не менее, для многих метрик есть функциональные замены, перечисленные в [миграции метрик RUM](/docs/analyze-explore-automate/metrics/upgrade/rum-metric-migration "Как классические метрики RUM соотносятся с их логическими эквивалентами в Grail.").

## Связанные темы

* [Захват свойств событий и сессий для веб-фронтендов](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/event-and-session-properties "Узнайте, как захватывать свойства событий и сессий для веб-фронтендов.")
* [Захват свойств событий и сессий для мобильных фронтендов](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/additional-configuration/event-and-session-properties "Узнайте, как захватывать свойства событий и сессий для мобильных фронтендов.")
* [Ограничения файервола для RUM](/docs/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum "Убедитесь, что данные мониторинга реальных пользователей проходят через ваш файервол.")
* [Миграция метрик RUM](/docs/analyze-explore-automate/metrics/upgrade/rum-metric-migration "Как классические метрики RUM соотносятся с их логическими эквивалентами в Grail.")