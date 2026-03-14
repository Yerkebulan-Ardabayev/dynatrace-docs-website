---
title: Настройка параметров Apdex для веб-приложений
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/configure-apdex-web
scraped: 2026-03-06T21:26:08.607908
---

# Настройка параметров Apdex для веб-приложений


* Classic
* How-to guide
* 1-min read
* Published Jan 27, 2023

[Apdex](../../rum-concepts/scores-and-ratings/apdex-ratings.md "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") — важный показатель для измерения производительности вашего приложения. Вы можете настроить пороговые значения Apdex (Satisfactory, Tolerable и Frustrating) для вашего приложения и его [ключевых пользовательских действий](../../rum-concepts/user-actions.md#key-user-actions "Learn what user actions are and how they help you understand what users do with your application."), чтобы уточнить расчёты Apdex.

## Настройка параметров Apdex для вашего приложения

1. Перейдите в **Web**.
2. Выберите приложение, которое хотите настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**...**) > **Edit**.
4. Выберите **General settings** > **Load actions** / **XHR actions** / **Custom actions**.
5. Используйте ползунки в разделе **Key performance metric thresholds**, чтобы задать значения, определяющие действие пользователя как **Satisfactory**, **Tolerable** или **Frustrating**.
6. В разделах **Load actions** и **XHR actions** воспользуйтесь выпадающим списком, чтобы выбрать ключевую метрику производительности для расчёта Apdex.

![Configure Apdex ratings](https://dt-cdn.net/images/web-apdex-configuration1-1402-98b17048e0.png)

## Настройка пороговых значений Apdex для ключевых пользовательских действий

Чтобы изменить пороговые значения Apdex для ключевого пользовательского действия:

1. Перейдите в **Frontend**.
2. Выберите приложение и прокрутите вниз до раздела **Top 3 user actions** или **Top 3 actions**.
3. Выберите **View full details** или **Analyze performance**.
4. Найдите нужное ключевое пользовательское действие и выберите его.
   Откроется страница подробностей пользовательского действия.
5. В правом верхнем углу страницы подробностей пользовательского действия выполните одно из следующих действий:

   * Для веб-приложений выберите **More** (**...**) > **Edit** > **Key performance metric**.
   * Для мобильных и пользовательских приложений выберите ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") (**Expand**) > **Edit** > **Key performance metric**.
6. Используйте ползунок для настройки пороговых значений Apdex.

## Связанные темы

* [Рейтинги Apdex](../../rum-concepts/scores-and-ratings/apdex-ratings.md "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.")
* [Контекстный анализ Apdex](../../session-segmentation/apdex-analysis.md "Check Apdex rating for a user action, location, and application.")
