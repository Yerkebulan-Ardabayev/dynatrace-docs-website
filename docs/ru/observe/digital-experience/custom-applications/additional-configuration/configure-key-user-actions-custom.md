---
title: Configure key user actions for custom applications
source: https://www.dynatrace.com/docs/observe/digital-experience/custom-applications/additional-configuration/configure-key-user-actions-custom
scraped: 2026-03-03T21:23:18.298824
---

# Настройка ключевых действий пользователей для пользовательских приложений

# Настройка ключевых действий пользователей для пользовательских приложений

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 30 янв. 2023 г.

Большинство приложений включают действия пользователей, особенно важные для успеха вашего цифрового бизнеса. Примерами таких действий являются регистрация, оформление заказа и поиск товаров. Такие [ключевые действия пользователей](../../rum-concepts/user-actions.md#key-user-actions "Learn what user actions are and how they help you understand what users do with your application.") могут выполняться дольше, чем другие, или к ним может предъявляться требование более короткой, чем в среднем, продолжительности.

С помощью функции ключевых действий пользователей вы можете [настроить пороги Apdex](../../rum-concepts/scores-and-ratings/apdex-ratings.md#key-user-actions "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") для каждого из этих действий пользователя. Вы можете использовать эту функцию для мониторинга ключевых действий с помощью выделенной плитки дашборда и отслеживания исторических тенденций.

## Пометить действие пользователя как ключевое

1. Перейдите в раздел **Frontend**.
2. Выберите приложение и прокрутите вниз до **Top 3 user actions** или **Top 3 actions**.
3. Нажмите **View full details** или **Analyze performance**.
4. Прокрутите вниз, чтобы увидеть список действий пользователей, и выберите нужное действие.
   Откроется страница сведений о действии пользователя.
5. В правом верхнем углу страницы сведений о действии пользователя нажмите **Mark as key user action**.

Вы можете задать до 500 ключевых действий пользователей на среду для всех ваших приложений и до 100 ключевых действий пользователей на приложение.

При достижении максимального лимита ключевых действий пользователей рассмотрите использование вычисляемых метрик (доступных для ваших [веб-](../../web-applications/additional-configuration/rum-calculated-metrics-web.md "Create calculated metrics as well as custom charts based on calculated metrics for your web applications."), [мобильных](../../mobile-applications/additional-configuration/rum-calculated-metrics-mobile.md "Create calculated metrics as well as custom charts based on calculated metrics for your mobile applications.") и [пользовательских приложений](rum-calculated-metrics-custom.md "Create calculated metrics as well as custom charts based on calculated metrics for your custom applications.")), которые предлагают аналогичные возможности.

## Закрепить ключевое действие пользователя на дашборде

[Dashboards Classic](../../../../analyze-explore-automate/dashboards-classic.md "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

1. Перейдите в раздел **Frontend**.
2. Выберите приложение и прокрутите вниз до **Top 3 user actions** или **Top 3 actions**.
3. Нажмите **View full details** или **Analyze performance**.
4. Найдите нужное ключевое действие пользователя и выберите его.
   Откроется страница сведений о действии пользователя.
5. В верхней части страницы сведений о действии пользователя нажмите **Pin to dashboard**. Подробнее см. в разделе [Закрепление плиток на дашборде](../../../../analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard.md "Learn to pin tiles to your dashboards.").

## Настройка рейтинга Apdex для ключевого действия пользователя

Чтобы изменить пороги Apdex для ключевого действия пользователя:

1. Перейдите в раздел **Frontend**.
2. Выберите приложение и прокрутите вниз до **Top 3 user actions** или **Top 3 actions**.
3. Нажмите **View full details** или **Analyze performance**.
4. Найдите нужное ключевое действие пользователя и выберите его.
   Откроется страница сведений о действии пользователя.
5. В правом верхнем углу страницы сведений о действии пользователя выполните одно из следующих действий:

   * Для веб-приложений нажмите **More** (**â¦**) > **Edit** > **Key performance metric**.
   * Для мобильных и пользовательских приложений нажмите ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") (**Expand**) > **Edit** > **Key performance metric**.
6. Используйте ползунок для настройки порогов Apdex.

## Связанные темы

* [Действия пользователей](../../rum-concepts/user-actions.md "Learn what user actions are and how they help you understand what users do with your application.")
