---
title: Мониторинг Azure Spring Apps
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps
scraped: 2026-05-12T11:27:14.220545
---

# Мониторинг Azure Spring Apps

# Мониторинг Azure Spring Apps

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 19 августа 2020 г.

Dynatrace получает метрики для нескольких предварительно выбранных пространств имён, включая Azure Spring Apps. Для каждого экземпляра сервиса можно просматривать метрики, разбивать их по различным измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

* Dynatrace версии 1.200+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Активация OneAgent (рекомендуется)

Для комплексного мониторинга рабочих нагрузок Spring Apps можно [настроить интеграцию OneAgent с Azure Spring Apps](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в окружении Dynatrace на странице **custom device overview page** или на странице **Dashboards**.

### Просмотр метрик на странице custom device overview

Чтобы перейти на страницу custom device overview

1. Откройте **Technologies & Processes**.
2. Отфильтруйте по имени сервиса и выберите нужную группу пользовательских устройств.
3. После выбора группы откроется страница **custom device group overview page**.
4. На странице **custom device group overview page** перечислены все экземпляры (пользовательские устройства) группы. Выберите экземпляр, чтобы перейти на страницу **custom device overview page**.

### Просмотр метрик на дашборде

Если для сервиса существует готовый дашборд, на странице **Dashboards** появится готовый дашборд с рекомендуемыми метриками для этого сервиса. Найти нужные дашборды можно с помощью фильтров **Preset** и **Name**.

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы готовый дашборд появился на странице **Dashboards**. Для этого откройте **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.

Готовый дашборд нельзя изменить напрямую, но его можно клонировать и отредактировать. Чтобы клонировать дашборд, откройте меню просмотра (**…**) и выберите **Clone**.
Чтобы убрать дашборд из списка, его можно скрыть. Для этого откройте меню просмотра (**…**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

![Spring](https://dt-cdn.net/images/2021-03-12-11-35-07-1496-2bea71b55d.png)

Spring

## Доступные метрики

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| jvm.gc.live.data.size | Размер пула памяти старшего поколения после полного GC | AppName, Pod | Byte | Applicable |
| jvm.gc.max.data.size | Максимальный размер пула памяти старшего поколения | AppName, Pod | Byte | Applicable |
| jvm.gc.memory.allocated | Увеличивается при росте размера пула памяти младшего поколения от одного GC до начала следующего | AppName, Pod | Byte | Applicable |
| jvm.gc.memory.promoted | Количество положительных приростов размера пула памяти старшего поколения до и после GC | AppName, Pod | Byte | Applicable |
| jvm.gc.pause.total.count | Количество пауз GC | AppName, Pod | Count | Applicable |
| jvm.gc.pause.total.time | Суммарное время пауз GC | AppName, Pod | MilliSecond | Applicable |
| jvm.memory.committed | Память, выделенная JVM, в байтах | AppName, Pod | Byte | Applicable |
| jvm.memory.max | Максимальный объём памяти в байтах, доступный для управления памятью | AppName, Pod | Byte | Applicable |
| jvm.memory.used | Использованная приложением память в байтах | AppName, Pod | Byte | Applicable |
| process.cpu.usage | Процент использования CPU JVM приложением | AppName, Pod | Percent | Applicable |
| system.cpu.usage | Недавнее использование CPU для всей системы | AppName, Pod | Percent | Applicable |
| tomcat.global.error | Глобальная ошибка Tomcat | AppName, Pod | Count | Applicable |
| tomcat.global.received | Всего получено байт Tomcat | AppName, Pod | Byte | Applicable |
| tomcat.global.request.avg.time | Среднее время запроса Tomcat | AppName, Pod | MilliSecond | Applicable |
| tomcat.global.request.max | Максимальное время запроса Tomcat | AppName, Pod | MilliSecond | Applicable |
| tomcat.global.request.total.count | Суммарное количество запросов Tomcat | AppName, Pod | Count | Applicable |
| tomcat.global.request.total.time | Суммарное время запросов Tomcat | AppName, Pod | MilliSecond | Applicable |
| tomcat.global.sent | Всего отправлено байт Tomcat | AppName, Pod | Byte | Applicable |
| tomcat.sessions.active.current | Количество активных сессий Tomcat | AppName, Pod | Count | Applicable |
| tomcat.sessions.active.max | Максимальное количество активных сессий Tomcat | AppName, Pod | Count | Applicable |
| tomcat.sessions.alive.max | Максимальное время жизни сессии Tomcat | AppName, Pod | MilliSecond | Applicable |
| tomcat.sessions.created | Количество созданных сессий Tomcat | AppName, Pod | Count | Applicable |
| tomcat.sessions.expired | Количество истёкших сессий Tomcat | AppName, Pod | Count | Applicable |
| tomcat.sessions.rejected | Количество отклонённых сессий Tomcat | AppName, Pod | Count | Applicable |
| tomcat.threads.config.max | Максимальное количество потоков по конфигурации Tomcat | AppName, Pod | Count | Applicable |
| tomcat.threads.current | Текущее количество потоков Tomcat | AppName, Pod | Count | Applicable |

## Связанные темы

* [Мониторинг Azure Spring Apps](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.")