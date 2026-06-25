---
title: Настройка ключевых пользовательских действий для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-key-user-actions-web
scraped: 2026-05-12T11:34:26.259036
---

# Настройка ключевых пользовательских действий для веб-приложений

# Настройка ключевых пользовательских действий для веб-приложений

* How-to guide
* 1-min read
* Published Jan 27, 2023

В большинстве приложений есть пользовательские действия, особенно важные для успеха цифрового бизнеса. Примерами таких действий могут служить регистрация, оформление заказа и поиск товаров. Подобные [ключевые пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions#key-user-actions "Learn what user actions are and how they help you understand what users do with your application.") могут выполняться дольше других или иметь требование более короткой, чем в среднем, длительности.

Функция ключевых пользовательских действий позволяет [настраивать пороговые значения Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings#key-user-actions "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") для каждого из этих действий. Функцию можно использовать для мониторинга ключевых действий с помощью специального тайла дашборда и отслеживания исторических тенденций.

## Пометка пользовательского действия как ключевого

1. Перейдите в **Frontend**.
2. Выберите приложение и прокрутите страницу вниз до раздела **Top 3 user actions** или **Top 3 actions**.
3. Выберите **View full details** или **Analyze performance**.
4. Прокрутите вниз, чтобы увидеть список пользовательских действий, и выберите нужное действие.
   Откроется страница с подробными сведениями о пользовательском действии.
5. В правом верхнем углу страницы выберите **Mark as key user action**.

Можно определить до 500 ключевых пользовательских действий на среду по всем приложениям и до 100 ключевых пользовательских действий на одно приложение.

По достижении максимального предела ключевых пользовательских действий рассмотрите использование вычисляемых метрик (доступных для [веб-](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications."), [мобильных](/managed/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile "Create calculated metrics as well as custom charts based on calculated metrics for your mobile applications.") и [пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Create calculated metrics as well as custom charts based on calculated metrics for your custom applications.")), предлагающих аналогичные возможности.

## Закрепление ключевого пользовательского действия на дашборде

[Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

1. Перейдите в **Frontend**.
2. Выберите приложение и прокрутите страницу вниз до раздела **Top 3 user actions** или **Top 3 actions**.
3. Выберите **View full details** или **Analyze performance**.
4. Найдите нужное ключевое пользовательское действие и выберите его.
   Откроется страница с подробными сведениями о пользовательском действии.
5. В верхней части страницы выберите **Pin to dashboard**. Подробнее см. раздел [Закрепление тайлов на дашборде](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").

## Настройка рейтинга Apdex для ключевого пользовательского действия

Чтобы изменить пороговые значения Apdex для ключевого пользовательского действия:

1. Перейдите в **Frontend**.
2. Выберите приложение и прокрутите страницу вниз до раздела **Top 3 user actions** или **Top 3 actions**.
3. Выберите **View full details** или **Analyze performance**.
4. Найдите нужное ключевое пользовательское действие и выберите его.
   Откроется страница с подробными сведениями о пользовательском действии.
5. В правом верхнем углу страницы выполните одно из следующих действий:

   * Для веб-приложений выберите **More** (**…**) > **Edit** > **Key performance metric**.
   * Для мобильных и пользовательских приложений выберите ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") (**Expand**) > **Edit** > **Key performance metric**.
6. С помощью ползунка отрегулируйте пороговые значения Apdex.

## Связанные темы

* [Пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")