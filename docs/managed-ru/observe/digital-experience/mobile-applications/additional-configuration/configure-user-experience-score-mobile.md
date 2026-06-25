---
title: Изменение порогов оценки пользовательского опыта для мобильных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-user-experience-score-mobile
scraped: 2026-05-12T11:33:06.864182
---

# Изменение порогов оценки пользовательского опыта для мобильных приложений

# Изменение порогов оценки пользовательского опыта для мобильных приложений

* How-to guide
* 1-min read
* Published Jan 30, 2023

[Оценка пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "Оценка пользовательского опыта — это метрика для классификации пользовательских сессий как Frustrating, Tolerable или Satisfying.") — важная метрика, отражающая общую производительность, удобство использования и обнаруженные ошибки в каждой сессии. Вы можете настроить пороги оценки пользовательского опыта для своих приложений.

Чтобы задать пороги оценки пользовательского опыта:

1. Перейдите в **Settings** > **Web and mobile monitoring** > **User experience score**.

   ![User experience score settings](https://dt-cdn.net/images/user-xp-score-settings-2292-03a4586d9e.png)

   User experience score settings
2. Необязательно: включите **If last user action in a session is classified as Frustrating, classify the entire session as Frustrating**, чтобы оценивать сессию по её последнему действию как Frustrating.
3. Необязательно: включите **Consider rage clicks / rage taps in score calculation**, чтобы учитывать [rage-события](/managed/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Узнайте о событиях пользователей и ошибок, а также о типах событий, захватываемых Dynatrace.") при определении оценки пользовательского опыта.
4. В поле **Threshold for Frustrating user experience** введите процент действий **Frustrating**, при превышении которого пользовательская сессия считается **Frustrating**.
5. В поле **Threshold for Satisfying user experience** введите минимальный процент действий **Satisfying**, необходимый для признания сессии **Satisfying**.

## Связанные темы

* [Оценка пользовательского опыта](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/user-experience-score "Оценка пользовательского опыта — это метрика для классификации пользовательских сессий как Frustrating, Tolerable или Satisfying.")