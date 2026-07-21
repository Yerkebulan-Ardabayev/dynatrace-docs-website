---
title: Изменение пороговых значений оценки пользовательского опыта для веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-user-experience-score-web
---

# Изменение пороговых значений оценки пользовательского опыта для веб-приложений в RUM Classic

# Изменение пороговых значений оценки пользовательского опыта для веб-приложений в RUM Classic

* Практическое руководство
* Чтение за 1 минуту
* Опубликовано 27 января 2023 г.

[Оценка пользовательского опыта](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.") это важная метрика, отражающая общую производительность, удобство использования и обнаруженные ошибки каждой сессии. Пороговые значения оценки пользовательского опыта для приложений можно настраивать.

Чтобы настроить пороговые значения оценки пользовательского опыта

1. Перейти в **Settings** > **Web and mobile monitoring** > **User experience score**.

   ![User experience score settings](https://dt-cdn.net/images/user-xp-score-settings-2292-03a4586d9e.png)

   User experience score settings
2. Опционально включить **If last user action in a session is classified as Frustrating, classify the entire session as Frustrating**, чтобы оценивать неудовлетворительную сессию по её последнему действию.
3. Опционально включить **Consider rage clicks / rage taps in score calculation**, чтобы учитывать [события возмущения](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.") при определении оценки пользовательского опыта.
4. В поле **Threshold for Frustrating user experience** указать процент действий пользователя с оценкой **Frustrating**, при превышении которого сессия пользователя считается **Frustrating**.
5. В поле **Threshold for Satisfying user experience** указать минимальный процент действий пользователя с оценкой **Satisfying**, необходимый для того, чтобы сессия считалась **Satisfying**.

## Похожие темы

* [Оценка пользовательского опыта в RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/user-experience-score "User experience score is a metric used to categorize user sessions as Frustrating, Tolerable, or Satisfying.")