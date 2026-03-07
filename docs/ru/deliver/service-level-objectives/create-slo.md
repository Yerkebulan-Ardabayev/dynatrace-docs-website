---
title: Create service-level objectives
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/create-slo
scraped: 2026-03-05T21:31:21.874741
---

# Создание целей уровня обслуживания

# Создание целей уровня обслуживания

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 4 мин
* Опубликовано 5 ноября 2024 г.

С помощью ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** вы можете настраивать новые цели уровня обслуживания (SLO) на основе шаблонов, предоставляемых Dynatrace.
Вы также можете определить свои SLO на основе пользовательского запроса [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").

## Шаги

### Создание SLO из шаблона

Чтобы создать новый SLO с использованием предопределённого шаблона

1. В **Dynatrace** найдите ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** и откройте его.
2. Выберите  **Service-level objective**.
3. В мастере SLO выберите один из следующих вариантов:

   * **Host CPU usage utilization**
   * **Service availability**
   * **Service performance**
   * **Kubernetes cluster CPU usage efficiency**
   * **Kubernetes cluster memory usage efficiency**
   * **Kubernetes namespace CPU usage efficiency**
   * **Kubernetes namespace memory usage efficiency**
4. Нажмите **Create** для одного из указанных вариантов.
5. Выберите сущности, которые должны соответствовать вашей цели. Если вы используете шаблон **Service performance**, введите значение в миллисекундах в поле **Requests should be faster than**.
6. Необязательно: выберите сегменты , укажите необходимые сегменты и нажмите **Apply**. Это сокращает количество результатов фильтрации.

   ![Добавление фильтра сегментов к SLO](https://dt-cdn.net/images/slo-level-segments-1313-399767711c.png)

   Это лишь дополнительный фильтр для необходимых сущностей. Он не применяется к оценке SLO. Чтобы добавить фильтр сегментов к оценке SLO, используйте шаг 5 в разделе [Создание пользовательского SLO](/docs/deliver/service-level-objectives/create-slo#create-a-custom-slo "Create and configure service-level objectives (SLOs).").
7. Нажмите **Next**.
8. Определите критерии вашего SLO. Заполните поле **Target** и выберите временной интервал для периода оценки с помощью выпадающего списка в поле **Over the evaluation period**.
9. Необязательно: включите **Show warning** и введите числовое значение в процентах в поле **Show warning at**.
10. Нажмите **Next**.
11. Введите имя для вашего SLO в поле **SLO Name**.
12. Необязательно: укажите понятное описание вашего SLO в поле **SLO description**.
13. Необязательно: добавьте теги для вашего SLO в разделе **Tags**, заполнив поля **Key** и **Value**. Нажмите **Add**, чтобы сохранить теги. Теги можно использовать для добавления дополнительных метаданных к вашим SLO, таких как ответственная команда или дополнительная информация о связанных сущностях или критичности вашего SLO.
14. Нажмите **Save**.

### Создание пользовательского SLO

1. В **Dynatrace** найдите ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**.
2. В обзоре **Service-Level Objectives** выберите  **Service-level objective**.
3. Выберите  **Custom SLO**.
4. Укажите ваш DQL-запрос. Ваш запрос должен включать поле "sli", как в следующем примере, чтобы обеспечить единообразную визуализацию, преобразование и агрегацию для всех ваших SLO. Поле "sli" должно возвращать массив типа `double`. DQL-запрос может быть основан на любом типе данных в Grail, например на событиях или логах. Использование [makeTimeseries](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands") позволяет создать временной ряд sli, который можно использовать для расчёта статуса SLO.

```
timeseries { total=sum(dt.service.request.count) ,failures=sum(dt.service.request.failure_count) }



, by: { dt.entity.service }



, filter: { in (dt.entity.service, { services }) }



| fieldsAdd sli=(((total[]-failures[])/total[])*(100))
```

5. Необязательно: выберите сегменты , укажите необходимые сегменты и нажмите **Apply**. Это дополнительный фильтр к запросу.

   Выбранные сегменты сохраняются вместе с определением SLO. Эти фильтры действуют при будущих изменениях сегментов и создании новых сущностей с тем же DQL-запросом.
6. Нажмите **Next**.
7. Определите критерии вашего SLO. Заполните поле **Target** и выберите временной интервал для периода оценки с помощью выпадающего списка в поле **over the evaluation period**.
8. Необязательно: включите **Show warning** и введите процентное значение в поле **Show warning at**.
9. Нажмите **Next**.
10. Укажите имя для вашего SLO в поле **SLO Name**.
11. Необязательно: укажите понятное описание вашего SLO в поле **SLO description**.
12. Необязательно: добавьте теги для вашего SLO в разделе **Tags**, заполнив поля **Key** и **Value**. Нажмите кнопку **Add**, чтобы сохранить теги. Теги можно использовать для добавления дополнительных метаданных к вашим SLO, таких как ответственная команда или дополнительная информация о связанных сущностях или критичности вашего SLO.
13. Нажмите кнопку **Save**, чтобы создать ваш SLO.

## Создание и управление SLO через API

Вы можете создавать, редактировать, просматривать, удалять и оценивать ваши SLO через API.

1. Перейдите в Dynatrace.
2. В [поиске по платформе](/docs/discover-dynatrace/get-started/dynatrace-ui#search "Navigate the latest Dynatrace") введите `API`. В результатах поиска найдите раздел **Support resources** и пункт **Dynatrace API** под ним.
3. Выберите **Dynatrace API**, чтобы получить доступ к документации Dynatrace API. Откроется новая страница с определениями Dynatrace API.
4. В правом верхнем углу перейдите к **Select a definition**.
5. Из выпадающего списка выберите нужный эндпоинт.
6. Выполните аутентификацию с помощью вашего API-токена. Подробнее см. в разделе [Аутентификация](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").
