---
title: Изменение порогов оценки пользовательского опыта в пользовательских приложениях
source: https://docs.dynatrace.com/managed/observe/digital-experience/custom-applications/additional-configuration/configure-user-experience-score-custom
scraped: 2026-05-12T11:33:45.282862
---

# Изменение порогов оценки пользовательского опыта в пользовательских приложениях

# Изменение порогов оценки пользовательского опыта в пользовательских приложениях

* How-to guide
* 1-min read
* Published Jan 30, 2023

[Оценка пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "Оценка пользовательского опыта — метрика, используемая для классификации сессий пользователей как Frustrating, Tolerable или Satisfying.") — важная метрика, отражающая общую производительность, удобство использования и обнаруженные ошибки каждой сессии. Вы можете скорректировать пороги оценки пользовательского опыта для ваших приложений.

Чтобы настроить пороги оценки пользовательского опыта:

1. Перейдите в **Settings** > **Web and mobile monitoring** > **User experience score**.

   ![Настройки оценки пользовательского опыта](https://dt-cdn.net/images/user-xp-score-settings-2292-03a4586d9e.png)

   Настройки оценки пользовательского опыта
2. Необязательно: включите **If last user action in a session is classified as Frustrating, classify the entire session as Frustrating**, чтобы оценивать сессию как Frustrating по последнему действию.
3. Необязательно: включите **Consider rage clicks / rage taps in score calculation**, чтобы учитывать [rage-события](/managed/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Узнайте о событиях пользователей и ошибках, а также о типах событий, фиксируемых Dynatrace.") при определении оценки пользовательского опыта.
4. В поле **Threshold for Frustrating user experience** введите процент действий с оценкой **Frustrating**, при превышении которого сессия считается **Frustrating**.
5. В поле **Threshold for Satisfying user experience** введите минимальный процент действий с оценкой **Satisfying**, необходимый для того, чтобы сессия считалась **Satisfying**.

## Связанные темы

* [Оценка пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "Оценка пользовательского опыта — метрика, используемая для классификации сессий пользователей как Frustrating, Tolerable или Satisfying.")