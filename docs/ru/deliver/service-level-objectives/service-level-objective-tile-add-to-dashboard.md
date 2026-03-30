---
title: Добавить плитку целевого показателя уровня обслуживания (SLO) на панель управления
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/service-level-objective-tile-add-to-dashboard
scraped: 2026-03-05T21:34:17.198712
---

# Добавление плитки целевого уровня обслуживания (SLO) на дашборд


С помощью ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** вы можете добавить целевой уровень обслуживания (SLO) в виде плитки на дашборд для его визуализации и мониторинга.

## Шаги

### Добавление SLO из обзора SLO

1. В **Dynatrace** найдите ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**.
2. В таблице **Service-level objectives** найдите нужный SLO и в столбце **Actions** выберите > **Add to Dashboard**.

   ![Добавление целевого уровня обслуживания](https://dt-cdn.net/images/chrome-83tpev8kjz-205-6d208f9a7d.png)
3. В окне **Select destination** выберите документ и нажмите **Confirm**, чтобы добавить плитку на существующий дашборд, или выберите **New dashboard**, чтобы создать новый дашборд для вашего SLO.

![Снимок экрана диалогового окна Select destination](https://dt-cdn.net/images/wtp95711-dev-apps-dynatracelabs-com-ui-apps-dynatrace-dashboards-intent-add-slo-to-dashboard-1-2445-1726e627fe.png)

На дашборде появится плитка SLO, отображающая статус SLO, бюджет ошибок и целевое значение.

### Добавление SLO с дашборда

Добавляйте и редактируйте SLO непосредственно из ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

1. Перейдите в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** и создайте [новый дашборд](../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md#create-dashboard "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в режиме реального времени.") или выберите [существующий](../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md#dashboard-display "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в режиме реального времени.").
2. Добавить SLO можно с помощью сочетания клавиш Shift+S или нажав значок плюса в правом верхнем углу дашборда.

   ![Добавление плитки SLO с дашборда](https://dt-cdn.net/images/chrome-ftp3kxoqkt-736-3ea4751a06.png)
3. В раскрывающемся списке **Create new tile** выберите **Service-level Objective**.

   Откроется панель **Service-level objective**.
4. На панели редактирования плитки SLO выберите нужный SLO из списка **Service-level objective**. Кроме того, вы можете добавить новый SLO или изменить существующий с помощью параметров **Add SLO** и **Edit SLO**. Все эти действия можно выполнить в одном окне, не покидая приложение Dashboards.

Имя SLO используется в качестве заголовка плитки дашборда. Вы можете изменить заголовок плитки — в этом случае заголовок плитки будет отличаться от имени SLO. (Само имя SLO при этом не изменится.)

![Снимок экрана панели Service-level objective с вкладкой Data и ссылкой на список SLO](https://dt-cdn.net/images/new-slo-in-dashboard-2907-a5f32f2b0c.png)

1. На вкладке **Visual** можно выбрать или отменить выбор столбцов **Data mapping** для отображения в SLO: **Status**, **Error budget**, **Target** и **Evaluation period**.
2. На вкладке **Visual** в разделе **Service-level objective options** можно включить параметр **Show labels** для отображения меток. Также можно выбрать, к чему применять цвет порогового статуса: к **Value** (значению) SLO или к **Background** (фону).

   ![Снимок экрана панели Service-level objective с вкладкой Visual](https://dt-cdn.net/images/wtp95711-dev-apps-dynatracelabs-com-ui-apps-dynatrace-dashboards-dashboard-f8f0ee42-e4a3-4b63-a3af-ca753060d7f7-3-2400-a36ac46dc8.png)

Плитка не будет функциональной, пока не выбран SLO. Дополнительные сведения см. в статье Редактирование плитки целевого уровня обслуживания (SLO) на дашборде.

Новая плитка SLO добавлена на дашборд.

Изменение временного диапазона дашборда не влияет на период оценки SLO; это не оказывает никакого эффекта на статус SLO, который всегда оценивается в соответствии с собственным периодом оценки.

### Добавление фильтра сегмента в SLO на дашбордах

1. Добавьте SLO на дашборд согласно разделу [Добавление SLO с дашборда](service-level-objective-tile-add-to-dashboard.md#tiles-add-from-dashboard "Визуализируйте целевые уровни обслуживания, добавляя их на дашборд.").
2. Выберите сегменты, отметьте нужные сегменты и нажмите **Apply**.

   ![Добавление фильтра сегментов в SLO на уровне дашборда](https://dt-cdn.net/images/dashboard-level-slo-segments-1971-8ef61073f5.png)
3. Визуализация SLO автоматически включит сегменты уровня дашборда в свою оценку.

Сегменты уровня дашборда и сегменты уровня SLO можно использовать одновременно. Итоговый результат будет пересечением этих двух выборок. В зависимости от выбранных сегментов, оценка SLO содержит:

1. Общий набор результатов для уровня дашборда и уровня SLO.
2. Нет результатов, если между сегментами нет пересечений.

Пример:

* Сегмент A: содержит объекты S-1 и S-2
* Сегмент B: содержит объекты S-2 и S-3

Из-за пересечения результат содержит только оценки, связанные с S-2.
