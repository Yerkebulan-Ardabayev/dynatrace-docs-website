---
title: Создание целей уровня обслуживания
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/create-slo
scraped: 2026-03-05T21:31:21.874741
---

Создавайте SLO на основе шаблонов Dynatrace или пользовательских DQL-запросов.

## Создание SLO из шаблона

1. Откройте **Service-Level Objectives** > **Service-level objective**.
2. Выберите шаблон: Host CPU usage, Service availability, Service performance, Kubernetes CPU/memory efficiency.
3. Нажмите **Create**.
4. Выберите сущности. Для шаблона Service performance укажите пороговое значение в мс.
5. Опционально: добавьте фильтр сегментов.
6. **Next** > задайте **Target** и **Evaluation period**.
7. Опционально: включите **Show warning**.
8. **Next** > введите **SLO Name**, опционально описание и теги.
9. **Save**.

## Создание пользовательского SLO

1. Откройте **Service-Level Objectives** > **Service-level objective** > **Custom SLO**.
2. Укажите DQL-запрос с полем `sli` (массив `double`):

```
timeseries { total=sum(dt.service.request.count) ,failures=sum(dt.service.request.failure_count) }
, by: { dt.entity.service }
, filter: { in (dt.entity.service, { services }) }
| fieldsAdd sli=(((total[]-failures[])/total[])*(100))
```

3. Опционально: добавьте фильтр сегментов (сохраняется с определением SLO).
4. **Next** > задайте **Target** и **Evaluation period**.
5. Опционально: включите **Show warning**.
6. **Next** > введите **SLO Name**, описание и теги.
7. **Save**.

## Управление SLO через API

1. В Dynatrace найдите **Dynatrace API** через поиск по платформе.
2. Перейдите к **Select a definition** и выберите нужный эндпоинт.
3. Аутентифицируйтесь API-токеном.
