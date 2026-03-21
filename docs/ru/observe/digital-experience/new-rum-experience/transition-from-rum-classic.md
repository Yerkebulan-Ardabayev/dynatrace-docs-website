---
title: Переход с RUM Classic на новый функционал RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/transition-from-rum-classic
scraped: 2026-03-06T21:25:59.818788
---

* Последняя Dynatrace
* Описание
* 1 мин. чтения

Если вы уже мониторите ваши веб- и мобильные фронтенды с помощью RUM Classic, переход на новый функционал RUM Experience не составит труда. Узнайте, как новый RUM Experience соотносится с RUM Classic и как его включить.

## Включение нового RUM Experience

Переход с RUM Classic на новый RUM Experience требует лишь изменения конфигурации. Следующие руководства описывают необходимые шаги.

[Web](web-frontends/initial-setup/enable-new-rum-for-web-apps.md) [Android](mobile-frontends/android/id-01-initial-setup.md) [iOS](mobile-frontends/ios/id-01-initial-setup.md) [React Native](mobile-frontends/react-native/id-01-initial-setup.md) [Flutter](mobile-frontends/flutter/id-01-initial-setup.md) [![.NET MAUI](https://dt-cdn.net/images/dotnetmaui-aea483621e.svg ".NET MAUI").NET MAUI](mobile-frontends/maui/id-01-initial-setup.md) 

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

На данный момент новый RUM Experience опирается только на HTTP-заголовки и cookie, уже включённые в [ограничения файервола для RUM Classic](../web-applications/initial-setup/firewall-constraints-for-rum.md "Убедитесь, что данные мониторинга реальных пользователей проходят через ваш файервол."). Если ваши файерволы и другие компоненты инфраструктуры уже настроены для пропуска этих заголовков и cookie, дальнейшие изменения при включении нового RUM Experience не требуются.

#### Встроенные метрики

Новый RUM Experience предоставляет множество встроенных метрик. Из-за другой базовой модели данных они не являются прямыми эквивалентами [метрик RUM Classic](../../../analyze-explore-automate/metrics-classic/built-in-metrics.md#applications "Изучите полный список встроенных метрик Dynatrace."). Тем не менее, для многих метрик есть функциональные замены, перечисленные в [миграции метрик RUM](../../../analyze-explore-automate/metrics/upgrade/rum-metric-migration.md "Как классические метрики RUM соотносятся с их логическими эквивалентами в Grail.").

## Связанные темы

* [Захват свойств событий и сессий для веб-фронтендов](web-frontends/additional-configuration/event-and-session-properties.md "Узнайте, как захватывать свойства событий и сессий для веб-фронтендов.")
* [Захват свойств событий и сессий для мобильных фронтендов](mobile-frontends/additional-configuration/event-and-session-properties.md "Узнайте, как захватывать свойства событий и сессий для мобильных фронтендов.")
* [Ограничения файервола для RUM](../web-applications/initial-setup/firewall-constraints-for-rum.md "Убедитесь, что данные мониторинга реальных пользователей проходят через ваш файервол.")
* [Миграция метрик RUM](../../../analyze-explore-automate/metrics/upgrade/rum-metric-migration.md "Как классические метрики RUM соотносятся с их логическими эквивалентами в Grail.")