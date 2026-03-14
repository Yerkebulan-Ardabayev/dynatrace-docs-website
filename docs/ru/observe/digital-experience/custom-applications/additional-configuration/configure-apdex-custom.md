---
title: Настройка параметров Apdex для пользовательских приложений
source: https://www.dynatrace.com/docs/observe/digital-experience/custom-applications/additional-configuration/configure-apdex-custom
scraped: 2026-03-05T21:33:03.715778
---

# Настройка параметров Apdex для пользовательских приложений


* Classic
* How-to guide
* 1-min read
* Published Jan 30, 2023

[Apdex](../../rum-concepts/scores-and-ratings/apdex-ratings.md "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") — важный показатель, измеряющий производительность вашего приложения. Вы можете настроить пороговые значения Apdex (Удовлетворительно, Допустимо и Неудовлетворительно) для вашего приложения и его [ключевых действий пользователей](../../rum-concepts/user-actions.md#key-user-actions "Learn what user actions are and how they help you understand what users do with your application."), чтобы уточнить расчёты Apdex.

## Настройка параметров Apdex для вашего приложения

1. Перейдите в раздел **Frontend**.
2. Выберите приложение, которое вы хотите настроить.
3. Выберите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **General** > **Key performance metrics**.
5. Используйте ползунки для установки порогов удовлетворённости пользователей (Удовлетворительно, Допустимо и Неудовлетворительно) для метрики **User action duration**.
6. Необязательно. Включите **Consider reported errors / web request errors in Apdex calculations**, чтобы оценивать действия пользователей с сообщёнными ошибками или ошибками веб-запросов как неудовлетворительные.

## Настройка пороговых значений Apdex для ключевых действий пользователей

Чтобы изменить пороговые значения Apdex для ключевого действия пользователя

1. Перейдите в раздел **Frontend**.
2. Выберите приложение и прокрутите вниз до раздела **Top 3 user actions** или **Top 3 actions**.
3. Выберите **View full details** или **Analyze performance**.
4. Найдите нужное ключевое действие пользователя и выберите его.
   Откроется страница подробностей действия пользователя.
5. В правом верхнем углу страницы подробностей действия пользователя выполните одно из следующих действий:

   * Для веб-приложений выберите **More** (**…**) > **Edit** > **Key performance metric**.
   * Для мобильных и пользовательских приложений выберите ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") (**Expand**) > **Edit** > **Key performance metric**.
6. Используйте ползунок для настройки пороговых значений Apdex.

## Связанные темы

* [Рейтинги Apdex](../../rum-concepts/scores-and-ratings/apdex-ratings.md "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.")
* [Контекстный анализ Apdex](../../session-segmentation/apdex-analysis.md "Check Apdex rating for a user action, location, and application.")
