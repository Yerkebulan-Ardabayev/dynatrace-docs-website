---
title: Новый опыт Real User Monitoring
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience
scraped: 2026-03-06T21:14:03.737862
---

# Новый опыт мониторинга реальных пользователей


* Пояснение

Новый опыт мониторинга реальных пользователей (New Real User Monitoring, RUM) привносит возможности RUM в последнюю версию Dynatrace и позволяет вам:

* Получить детальную видимость действий пользователей в интерфейсе через [пользовательские события](new-rum-experience/concepts/data-model.md#user-events "Ознакомьтесь с моделью данных, лежащей в основе нового опыта RUM.").
* Исследовать отдельные пользовательские пути и понимать паттерны поведения пользователей через [пользовательские сессии](new-rum-experience/concepts/data-model.md#user-sessions "Ознакомьтесь с моделью данных, лежащей в основе нового опыта RUM.").
* Ранний доступ: автоматически фиксировать [пользовательские взаимодействия](new-rum-experience/concepts/data-model.md#user-interactions "Ознакомьтесь с моделью данных, лежащей в основе нового опыта RUM."), такие как клики, нажатия, прокрутка и ввод данных, для получения сведений о поведении пользователей.
* Использовать платформенные приложения, такие как ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, а также предустановленные [приложения для RUM](#new-rum-experience-apps).
* Использовать [OpenPipeline](../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.") для настройки полученных пользовательских событий и сессий, а также для извлечения данных и метрик.
* Исследовать и анализировать пользовательские события и сессии с помощью [Dynatrace Query Language](../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.").

## Уже используете RUM Classic?

Переход на новый опыт RUM прост и открывает расширенные возможности мониторинга.

[Узнать больше](new-rum-experience/transition-from-rum-classic.md)

## Приложения нового опыта RUM

[![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals")

#### Experience Vitals

Приложение Experience Vitals служит отправной точкой для мониторинга веб- и мобильных интерфейсов.

Experience Vitals](new-rum-experience/experience-vitals.md)[![Users & Sessions](https://dt-cdn.net/images/users-sessions-149-f84e0b9b20.png "Users & Sessions")

#### Users & Sessions

Приложение Users & Sessions предоставляет сведения об отдельных пользовательских путях и паттернах поведения.

Users & Sessions](new-rum-experience/users-and-sessions.md)[![Error Inspector](https://dt-cdn.net/images/error-inspector-256-c849b18430.png "Error Inspector")

#### Error Inspector

Error Inspector помогает разработчикам и IT-специалистам обнаруживать, отслеживать и исследовать ошибки интерфейса в веб- и мобильных приложениях.

Error Inspector](new-rum-experience/error-inspector.md)

## Обзор нового опыта RUM

[#### Концепции нового опыта RUM

Изучите ключевые концепции нового опыта RUM.](new-rum-experience/concepts.md "Изучите ключевые концепции нового опыта RUM.")[#### Веб-интерфейсы

Узнайте, как настроить и использовать новый опыт RUM для веб-интерфейсов.](new-rum-experience/web-frontends.md "Ознакомьтесь с ключевыми концепциями веб-интерфейсов и узнайте, как настроить их в новом опыте RUM.")[#### Мобильные интерфейсы

Узнайте, как настроить и использовать новый опыт RUM для мобильных интерфейсов.](new-rum-experience/mobile-frontends.md "Узнайте, как настроить и использовать новый опыт RUM для мобильных интерфейсов.")[#### Разрешения нового опыта RUM

Узнайте, какие разрешения необходимы для настройки нового опыта RUM.](new-rum-experience/permissions.md "Узнайте, какие разрешения необходимы для настройки нового опыта RUM.")[#### Конфиденциальность данных

Убедитесь, что ваша конфигурация RUM соответствует нормам защиты данных вашего региона.](new-rum-experience/data-privacy.md "Узнайте, как убедиться, что ваша конфигурация RUM соответствует нормам защиты данных вашего региона.")[![Use cases](https://dt-cdn.net/images/icon-use-cases-9ac91e0c53.svg "Use cases")

#### Варианты использования

Используйте новый опыт RUM и инструменты платформы Dynatrace для ключевых сценариев использования.](new-rum-experience/use-cases.md "Узнайте, как новый опыт RUM помогает решать ключевые задачи.")[#### Метрики нового опыта RUM

Изучите метрики интерфейсов, предоставляемые новым опытом RUM.](../../analyze-explore-automate/metrics/upgrade/rum-metric-migration.md "Узнайте, как метрики RUM Classic сопоставляются с их логическими эквивалентами в Grail.")

## Смотрите также

* [Пользовательские события](../../semantic-dictionary/model/rum/user-events.md "Пользовательские события обеспечивают глубокую видимость и понимание опыта, поведения, производительности и ошибок ваших клиентов и конечных пользователей в режиме реального времени.")
* [Grail](../../platform/grail.md "Информация о том, что и как можно запрашивать в данных Dynatrace.")
* [OpenPipeline](../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.")
* [Dynatrace Query Language](../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
