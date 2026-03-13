---
title: Monitor Azure Spring Apps
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps
scraped: 2026-03-02T21:27:05.548728
---

# Мониторинг Azure Spring Apps

# Мониторинг Azure Spring Apps

* Latest Dynatrace
* Практическое руководство
* Время чтения: 3 мин
* Опубликовано 19 авг. 2020

Dynatrace собирает метрики для нескольких предварительно выбранных пространств имён, включая Azure Spring Apps. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

* Dynatrace версии 1.200+
* ActiveGate среды версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Активация OneAgent (рекомендуется)

Для получения сквозного представления о ваших рабочих нагрузках Spring Apps вы можете [настроить интеграцию OneAgent с Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса имеется предустановленный дашборд, вы получите предустановленный дашборд для соответствующего сервиса со всеми рекомендованными метриками на странице **Dashboards**. Вы можете искать конкретные дашборды, фильтруя по **Preset**, а затем по **Name**.

Для существующих отслеживаемых сервисов может потребоваться повторно сохранить ваши учётные данные, чтобы предустановленный дашборд появился на странице **Dashboards**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем выберите **Save**.

Вы не можете вносить изменения непосредственно в предустановленный дашборд, но можете его клонировать и отредактировать. Чтобы клонировать дашборд, откройте меню обзора (**...**) и выберите **Clone**.
Чтобы удалить дашборд из списка дашбордов, вы можете его скрыть. Чтобы скрыть дашборд, откройте меню обзора (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Клонирование и скрытие Azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Spring](https://dt-cdn.net/images/2021-03-12-11-35-07-1496-2bea71b55d.png)

## Доступные метрики

| Имя | Описание | Измерения | Единица измерения | Рекомендовано |
| --- | --- | --- | --- | --- |
| jvm.gc.live.data.size | Размер пула памяти старого поколения после полной сборки мусора | AppName, Pod | Byte | Применимо |
| jvm.gc.max.data.size | Максимальный размер пула памяти старого поколения | AppName, Pod | Byte | Применимо |
| jvm.gc.memory.allocated | Увеличение размера пула памяти молодого поколения после одной сборки мусора до следующей | AppName, Pod | Byte | Применимо |
| jvm.gc.memory.promoted | Количество положительных увеличений размера пула памяти старого поколения до и после сборки мусора | AppName, Pod | Byte | Применимо |
| jvm.gc.pause.total.count | Количество пауз сборки мусора | AppName, Pod | Count | Применимо |
| jvm.gc.pause.total.time | Общее время пауз сборки мусора | AppName, Pod | MilliSecond | Применимо |
| jvm.memory.committed | Память, выделенная JVM, в байтах | AppName, Pod | Byte | Применимо |
| jvm.memory.max | Максимальный объём памяти в байтах, который может использоваться для управления памятью | AppName, Pod | Byte | Применимо |
| jvm.memory.used | Используемая память приложения в байтах | AppName, Pod | Byte | Применимо |
| process.cpu.usage | Процент использования CPU JVM приложения | AppName, Pod | Percent | Применимо |
| system.cpu.usage | Текущее использование CPU для всей системы | AppName, Pod | Percent | Применимо |
| tomcat.global.error | Глобальные ошибки Tomcat | AppName, Pod | Count | Применимо |
| tomcat.global.received | Общее количество полученных байт Tomcat | AppName, Pod | Byte | Применимо |
| tomcat.global.request.avg.time | Среднее время запроса Tomcat | AppName, Pod | MilliSecond | Применимо |
| tomcat.global.request.max | Максимальное время запроса Tomcat | AppName, Pod | MilliSecond | Применимо |
| tomcat.global.request.total.count | Общее количество запросов Tomcat | AppName, Pod | Count | Применимо |
| tomcat.global.request.total.time | Общее время запросов Tomcat | AppName, Pod | MilliSecond | Применимо |
| tomcat.global.sent | Общее количество отправленных байт Tomcat | AppName, Pod | Byte | Применимо |
| tomcat.sessions.active.current | Текущее количество активных сессий Tomcat | AppName, Pod | Count | Применимо |
| tomcat.sessions.active.max | Максимальное количество активных сессий Tomcat | AppName, Pod | Count | Применимо |
| tomcat.sessions.alive.max | Максимальное время жизни сессии Tomcat | AppName, Pod | MilliSecond | Применимо |
| tomcat.sessions.created | Количество созданных сессий Tomcat | AppName, Pod | Count | Применимо |
| tomcat.sessions.expired | Количество истёкших сессий Tomcat | AppName, Pod | Count | Применимо |
| tomcat.sessions.rejected | Количество отклонённых сессий Tomcat | AppName, Pod | Count | Применимо |
| tomcat.threads.config.max | Максимальное количество потоков в конфигурации Tomcat | AppName, Pod | Count | Применимо |
| tomcat.threads.current | Текущее количество потоков Tomcat | AppName, Pod | Count | Применимо |

## Связанные темы

* [Мониторинг Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.")
