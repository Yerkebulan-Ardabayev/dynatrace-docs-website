---
title: Настройка зон управления
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones
scraped: 2026-05-12T11:54:10.993865
---

# Настройка зон управления

# Настройка зон управления

* How-to guide
* 2-min read
* Updated on Jan 29, 2023

Зоны управления состоят из правил, определяющих, к каким объектам и размерным данным (таким как журналы и метрики) можно получить доступ в рамках каждой зоны управления. Правила зон управления (как и [правила автоматического тегирования](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.")) основаны на мощном механизме условной обработки Dynatrace. В сочетании с [разрешениями пользователей и групп](/managed/manage/identity-access-management/user-and-group-management "Управление пользователями и группами") зоны управления позволяют создавать несколько перекрывающихся разделов в окружении для обеспечения наблюдаемости, совместной работы и безопасности.

## Создание зоны управления

По умолчанию в вашем окружении мониторинга Dynatrace можно создать до 5 000 зон управления. (По любым вопросам обращайтесь к специалисту Dynatrace через онлайн-чат в вашем окружении Dynatrace.)

1. Перейдите в **Settings** > **Preferences** > **Management zones** (или выберите страницу настроек **Management zones** в результатах поиска).

   ![Зоны управления](https://dt-cdn.net/images/mz-settings-page-1609-53fa2b9df7.png "Зоны управления")

2. Нажмите **Add new management zone**.
3. Укажите **Management zone name** и **Description**.
4. Создайте [правила зоны управления](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules "Определение правил для ограничения объектов, доступных в зоне управления."), регулирующие, какие объекты и данные входят в зону управления и доступны в ней. Правила для объектов и размерных данных основаны на двух подходах: подходе на основе интерфейса и текстовом подходе с использованием мощного [селектора объектов](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Настройка селектора объектов для конечных точек Environment API.") Environment API v2.

   ![Правила зоны управления](https://dt-cdn.net/images/mz-rules-1a-1227-bcb209a202.png "Правила зоны управления")

   Выберите правило (например, **Web applications** на изображении выше) > **Preview entities**, чтобы увидеть **Matching entities**.

   Подробнее:

   * О том, как данные журналов могут приниматься и автоматически назначаться зонам управления, см. в разделе [Зоны управления и принятые данные журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Узнайте, как принятые данные журналов назначаются зонам управления.").
   * О том, как [добавить сервисный уровень в зону управления](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#mz "Создание, настройка и мониторинг сервисных уровней в Dynatrace."), чтобы пользователи с доступом к зоне управления могли просматривать статус SLO и бюджет ошибок на странице **Service-level objectives**.

## Назначение прав доступа к зонам управления

После настройки зоны управления определите, какие группы пользователей должны иметь к ней доступ и на каком уровне.

В главном меню Cluster Management Console выберите **User authentication** > **User groups** > нужную группу пользователей для [назначения разрешений](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions "Узнайте о поддерживаемых разрешениях и политиках, о том, как назначать их группам и управлять пользователями и группами.").

![Группы пользователей Dynatrace Managed](https://dt-cdn.net/images/dynatracemanagedusergroups-1903-5e1be74e08.png "Группы пользователей Dynatrace Managed")

Подробнее см. в разделе [Применение и использование зон управления](/managed/manage/identity-access-management/permission-management/management-zones/apply-and-use-management-zones "Применение зон управления для организации среды Dynatrace и управления доступом пользователей к конкретным данным.").

## Связанные разделы

* [Зоны управления и принятые данные журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Узнайте, как принятые данные журналов назначаются зонам управления.")
* [Настройка и мониторинг сервисных уровней с Dynatrace](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo "Создание, настройка и мониторинг сервисных уровней в Dynatrace.")