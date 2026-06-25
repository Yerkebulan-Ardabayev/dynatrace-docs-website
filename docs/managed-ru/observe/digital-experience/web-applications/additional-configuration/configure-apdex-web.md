---
title: Настройка параметров Apdex для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-apdex-web
scraped: 2026-05-12T11:34:53.503147
---

# Настройка параметров Apdex для веб-приложений

# Настройка параметров Apdex для веб-приложений

* How-to guide
* 1-min read
* Updated on May 04, 2026

[Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") — важная метрика, измеряющая производительность приложения. Можно скорректировать пороговые значения Apdex (Satisfactory, Tolerable и Frustrating) для приложения и его [ключевых пользовательских действий](/managed/observe/digital-experience/rum-concepts/user-actions#key-user-actions "Learn what user actions are and how they help you understand what users do with your application."), чтобы уточнить расчёт Apdex.

Рейтинг Apdex, отображаемый для вашего приложения за определённый период в разделе Applications, может отличаться от значения, отображаемого для того же приложения и того же периода в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") при выборе метрики `Apdex (by geolocation, user type) [web]`.

В качестве временного решения можно вручную реализовать стандартный расчёт Apdex по следующей формуле:

```
(((builtin:apps.web.actionCount.category:filter(and(or(eq("Apdex category",SATISFIED)),or(in("dt.entity.application",entitySelector("type(application)"))))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))+((builtin:apps.web.actionCount.category:filter(and(or(in("dt.entity.application",entitySelector("type(application)"))),or(eq("Apdex category",TOLERATING)))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))/2)) / (builtin:apps.web.actionCount.category:filter(and(or(in("dt.entity.application",entitySelector("type(application)"))))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))):sort(dimension("dt.entity.application.name",descending))
```

## Настройка параметров Apdex для приложения

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. Выберите **General settings** > **Load actions** / **XHR actions** / **Custom actions**.
5. С помощью ползунков в разделе **Key performance metric thresholds** выберите значения, при которых пользовательское действие считается **Satisfactory**, **Tolerable** или **Frustrating**.
6. В разделах **Load actions** и **XHR actions** используйте раскрывающийся список для выбора ключевой метрики производительности, которая должна использоваться при расчёте Apdex.

![Настройка рейтингов Apdex](https://dt-cdn.net/images/web-apdex-configuration1-1402-98b17048e0.png)

Настройка рейтингов Apdex

## Настройка пороговых значений Apdex для ключевых пользовательских действий

Чтобы изменить пороговые значения Apdex для ключевого пользовательского действия:

1. Перейдите в **Frontend**.
2. Выберите приложение и прокрутите страницу вниз до раздела **Top 3 user actions** или **Top 3 actions**.
3. Выберите **View full details** или **Analyze performance**.
4. Найдите нужное ключевое пользовательское действие и выберите его.
   Откроется страница с подробными сведениями о пользовательском действии.
5. В правом верхнем углу страницы пользовательского действия выполните одно из следующих действий:

   * Для веб-приложений выберите **More** (**…**) > **Edit** > **Key performance metric**.
   * Для мобильных и пользовательских приложений выберите ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") (**Expand**) > **Edit** > **Key performance metric**.
6. С помощью ползунка отрегулируйте пороговые значения Apdex.

## Связанные темы

* [Рейтинги Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.")
* [Контекстный анализ Apdex](/managed/observe/digital-experience/session-segmentation/apdex-analysis "Check Apdex rating for a user action, location, and application.")