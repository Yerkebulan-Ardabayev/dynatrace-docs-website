---
title: Настройка параметров Apdex для веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-apdex-web
---

# Настройка параметров Apdex для веб-приложений в RUM Classic

# Настройка параметров Apdex для веб-приложений в RUM Classic

* Практическое руководство
* Чтение за 1 минуту
* Обновлено 04 мая 2026 г.

[Apdex](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.") это важный показатель, измеряющий производительность приложения. Можно настроить пороговые значения Apdex (Satisfactory, Tolerable и Frustrating) для приложения и для его [ключевых пользовательских действий](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#key-user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают в приложении."), чтобы уточнить расчёты Apdex.

Рейтинг Apdex, отображаемый для приложения за определённый период времени в Applications, может отличаться от значения, отображаемого для того же приложения и того же периода времени в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужных данных.") при выбранной метрике `Apdex (by geolocation, user type) [web]`.

В качестве обходного решения можно вручную реализовать стандартный расчёт Apdex по формуле:

```
(((builtin:apps.web.actionCount.category:filter(and(or(eq("Apdex category",SATISFIED)),or(in("dt.entity.application",entitySelector("type(application)"))))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))+((builtin:apps.web.actionCount.category:filter(and(or(in("dt.entity.application",entitySelector("type(application)"))),or(eq("Apdex category",TOLERATING)))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))/2)) / (builtin:apps.web.actionCount.category:filter(and(or(in("dt.entity.application",entitySelector("type(application)"))))):splitBy("dt.entity.application"):names:sort(dimension("dt.entity.application.name",descending)):limit(20))):sort(dimension("dt.entity.application.name",descending))
```

## Настройка параметров Apdex для приложения

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. Выберите **General settings** > **Load actions** / **XHR actions** / **Custom actions**.
5. С помощью ползунков в разделе **Key performance metric thresholds** выберите значения, определяющие, что пользовательское действие относится к категории **Satisfactory**, **Tolerable** или **Frustrating**.
6. В разделах **Load actions** и **XHR actions** с помощью выпадающего списка выберите ключевую метрику производительности, которая будет использоваться при расчёте Apdex.

![Configure Apdex ratings](https://dt-cdn.net/images/web-apdex-configuration1-1402-98b17048e0.png)

Настройка рейтингов Apdex

## Настройка пороговых значений Apdex для ключевых пользовательских действий

Чтобы изменить пороговые значения Apdex для ключевого пользовательского действия

1. Перейдите в **Frontend**.
2. Выберите приложение и прокрутите вниз до раздела **Top 3 user actions** или **Top 3 actions**.
3. Выберите **View full details** или **Analyze performance**.
4. Найдите нужное ключевое пользовательское действие и выберите его.  
   Откроется страница сведений о пользовательском действии.
5. В правом верхнем углу страницы сведений о пользовательском действии выполните одно из следующего:

   * Для веб-приложений выберите **More** (**…**) > **Edit** > **Key performance metric**.
   * Для мобильных и пользовательских приложений выберите ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") (**Expand**) > **Edit** > **Key performance metric**.
6. С помощью ползунка настройте пороговые значения Apdex.

## Связанные темы

* [Рейтинги Apdex в RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.")
* [Анализ Apdex на основе контекста в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/apdex-analysis "Проверьте рейтинг Apdex для пользовательского действия, местоположения и приложения.")