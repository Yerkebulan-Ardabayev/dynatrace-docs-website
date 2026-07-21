---
title: Настройка параметров Apdex для пользовательских приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/configure-apdex-custom
---

# Настройка параметров Apdex для пользовательских приложений в RUM Classic

# Настройка параметров Apdex для пользовательских приложений в RUM Classic

* Практическое руководство
* Чтение за 1 минуту
* Опубликовано 30 января 2023 г.

[Apdex](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.") это важный показатель, измеряющий производительность приложения. Можно настроить пороговые значения Apdex (Satisfactory, Tolerable и Frustrating) для приложения и его [ключевых пользовательских действий](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#key-user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с приложением."), чтобы уточнить расчёт Apdex.

Оценка Apdex, отображаемая для приложения за определённый период времени в Applications, может отличаться от значения, отображаемого для того же приложения и того же периода времени в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты, чтобы получить нужную аналитику.") при использовании метрики `Apdex (by geolocation, user type) [web]`.

В качестве обходного решения можно вручную реализовать стандартный расчёт Apdex по формуле:

```
(((builtin:apps.web.actionCount.category:filter(and(or(eq("Apdex category",SATISFIED)),or(in("dt.entity.application",entitySelector("type(application)"))))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))+((builtin:apps.web.actionCount.category:filter(and(or(in("dt.entity.application",entitySelector("type(application)"))),or(eq("Apdex category",TOLERATING)))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))/2)) / (builtin:apps.web.actionCount.category:filter(and(or(in("dt.entity.application",entitySelector("type(application)"))))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))):sort(dimension("dt.entity.application.name",descending))
```

## Настройка параметров Apdex для приложения

1. Перейдите в **Frontend**.
2. Выберите приложение, которое нужно настроить.
3. Выберите **More** (**…**) > **Edit** в правом верхнем углу плитки с названием приложения.
4. В настройках приложения выберите **General** > **Key performance metrics**.
5. С помощью ползунков задайте пороговые значения удовлетворённости пользователей (Satisfactory, Tolerable и Frustrating) для метрики **User action duration**.
6. Необязательно Включите **Consider reported errors / web request errors in Apdex calculations**, чтобы оценивать пользовательские действия с зафиксированными ошибками или ошибками веб-запросов как Frustrating.

## Настройка пороговых значений Apdex для ключевых пользовательских действий

Чтобы изменить пороговые значения Apdex для ключевого пользовательского действия

1. Перейдите в **Frontend**.
2. Выберите приложение и прокрутите вниз до **Top 3 user actions** или **Top 3 actions**.
3. Выберите **View full details** или **Analyze performance**.
4. Найдите нужное ключевое пользовательское действие и выберите его.  
   Откроется страница сведений о пользовательском действии.
5. В правом верхнем углу страницы сведений о пользовательском действии выполните одно из следующих действий:

   * Для веб-приложений выберите **More** (**…**) > **Edit** > **Key performance metric**.
   * Для мобильных и пользовательских приложений выберите ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") (**Expand**) > **Edit** > **Key performance metric**.
6. С помощью ползунка настройте пороговые значения Apdex.

## Смежные темы

* [Оценки Apdex в RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.")
* [Контекстный анализ Apdex в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/apdex-analysis "Проверьте оценку Apdex для пользовательского действия, местоположения и приложения.")