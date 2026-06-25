---
title: Изменение пороговых значений оценки пользовательского опыта для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-user-experience-score-web
scraped: 2026-05-12T11:34:49.695210
---

# Изменение пороговых значений оценки пользовательского опыта для веб-приложений

# Изменение пороговых значений оценки пользовательского опыта для веб-приложений

* How-to guide
* 1-min read
* Published Jan 27, 2023

[Оценка пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.") — важная метрика, отражающая общую производительность, удобство использования и обнаруженные ошибки в каждой сессии. Пороговые значения оценки пользовательского опыта для приложений можно корректировать.

Чтобы настроить пороговые значения оценки пользовательского опыта:

1. Перейдите в **Settings** > **Web and mobile monitoring** > **User experience score**.

   ![Настройки оценки пользовательского опыта](https://dt-cdn.net/images/user-xp-score-settings-2292-03a4586d9e.png)

   Настройки оценки пользовательского опыта
2. Необязательно: включите **If last user action in a session is classified as Frustrating, classify the entire session as Frustrating**, чтобы оценивать сессию как неудовлетворительную по её последнему действию.
3. Необязательно: включите **Consider rage clicks / rage taps in score calculation**, чтобы учитывать [rage-события](/managed/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.") при определении оценки пользовательского опыта.
4. В поле **Threshold for Frustrating user experience** введите процент **Frustrating** пользовательских действий, при превышении которого пользовательская сессия считается **Frustrating**.
5. В поле **Threshold for Satisfying user experience** введите минимальный процент **Satisfying** пользовательских действий, необходимый для того, чтобы сессия считалась **Satisfying**.

## Связанные темы

* [Оценка пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.")