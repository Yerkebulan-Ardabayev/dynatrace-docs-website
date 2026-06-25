---
title: Настройка параметров Apdex для мобильных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-apdex-mobile
scraped: 2026-05-12T11:32:29.071246
---

# Настройка параметров Apdex для мобильных приложений

# Настройка параметров Apdex для мобильных приложений

* How-to guide
* 1-min read
* Published Jan 30, 2023

[Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.") — важный показатель, измеряющий производительность вашего приложения. Вы можете настроить пороги Apdex (Satisfactory, Tolerable и Frustrating) для вашего приложения и для его [ключевых пользовательских действий](/managed/observe/digital-experience/rum-concepts/user-actions#key-user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают в вашем приложении."), чтобы уточнить расчёты Apdex.

Рейтинг Apdex, отображаемый для вашего приложения за определённый период времени в Applications, может отличаться от того, что отображается для того же приложения и того же периода в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") с выбранной метрикой `Apdex (by geolocation, user type) [web]`.

В качестве обходного решения вы можете вручную реализовать стандартный расчёт Apdex, используя формулу:

```
(((builtin:apps.web.actionCount.category:filter(and(or(eq("Apdex category",SATISFIED)),or(in("dt.entity.application",entitySelector("type(application)"))))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))+((builtin:apps.web.actionCount.category:filter(and(or(in("dt.entity.application",entitySelector("type(application)"))),or(eq("Apdex category",TOLERATING)))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))/2)) / (builtin:apps.web.actionCount.category:filter(and(or(in("dt.entity.application",entitySelector("type(application)"))))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))):sort(dimension("dt.entity.application.name",descending))
```

## Настройка параметров Apdex для приложения

1. Перейдите в **Frontend**.
2. Выберите приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **General** > **Key performance metrics**.
5. С помощью ползунков задайте пороги удовлетворённости (Satisfactory, Tolerable и Frustrating) для метрики **User action duration**.
6. Необязательно: включите **Consider reported errors / web request errors in Apdex calculations**, чтобы оценивать пользовательские действия с зафиксированными ошибками или ошибками веб-запросов как Frustrating.

## Настройка порогов Apdex для ключевых пользовательских действий

Чтобы изменить пороги Apdex для ключевого пользовательского действия:

1. Перейдите в **Frontend**.
2. Выберите приложение и прокрутите вниз до раздела **Top 3 user actions** или **Top 3 actions**.
3. Нажмите **View full details** или **Analyze performance**.
4. Найдите нужное ключевое пользовательское действие и выберите его.  
   Откроется страница с подробной информацией о пользовательском действии.
5. В правом верхнем углу страницы с подробностями выполните одно из следующих действий:

   * Для веб-приложений: нажмите **More** (**…**) > **Edit** > **Key performance metric**.
   * Для мобильных и пользовательских приложений: нажмите ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") (**Expand**) > **Edit** > **Key performance metric**.
6. Используйте ползунок для регулировки порогов Apdex.

## Связанные темы

* [Рейтинги Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.")
* [Контекстный анализ Apdex](/managed/observe/digital-experience/session-segmentation/apdex-analysis "Проверьте рейтинг Apdex для пользовательского действия, местоположения и приложения.")