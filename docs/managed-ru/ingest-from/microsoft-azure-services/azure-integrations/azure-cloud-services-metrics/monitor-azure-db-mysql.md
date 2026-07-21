---
title: Мониторинг Azure Database for MySQL
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql
---

# Мониторинг Azure Database for MySQL

# Мониторинг Azure Database for MySQL

* Практическое руководство
* 2 минуты чтения
* Опубликовано 25 июня 2020 г.

Уведомление об устаревании

16 сентября 2024 года Azure Database for MySQL будет выведен из эксплуатации. Azure представил новый сервис, см. [Мониторинг Azure Database for MySQL Flexible Servers](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql-flexible-servers "Мониторинг Azure DB for Database for MySQL Flexible Servers и просмотр доступных метрик.").

Страница обзора Azure Database for MySQL служит исчерпывающим обзором серверов MySQL и экземпляров баз данных. Здесь можно получить полную видимость и проверить, работоспособна ли база данных, не снижена ли её производительность и нет ли неудачных подключений.

## Предварительные требования

* Dynatrace версии 1.196+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервисов](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

Дополнительно, для интеграции с OneAgent, см. [как отслеживается активность базы данных](/managed/observe/infrastructure-observability/database-services-classic/how-database-activity-is-monitored "Узнайте об автоматическом обнаружении и мониторинге сервисов баз данных в среде вашего приложения.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в среде Dynatrace либо на **странице обзора custom device**, либо на странице **Dashboards**.

### Просмотр метрик на странице обзора custom device

Чтобы перейти на страницу обзора custom device

1. Перейдите в **Technologies & Processes**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу custom device.
3. После выбора группы custom device откроется **страница обзора группы custom device**.
4. На **странице обзора группы custom device** перечислены все экземпляры (custom device), входящие в группу. Выберите экземпляр, чтобы открыть **страницу обзора custom device**.

### Просмотр метрик на дашборде

Если для сервиса есть готовый дашборд, на странице **Dashboards** появится готовый дашборд для соответствующего сервиса со всеми рекомендованными метриками. Нужные дашборды можно найти, отфильтровав по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы готовый дашборд появился на странице **Dashboards**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вносить изменения напрямую в готовый дашборд нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, откройте меню обзора (**…**) и выберите **Clone**.  
Чтобы убрать дашборд из списка дашбордов, его можно скрыть. Чтобы скрыть дашборд, откройте меню обзора (**…**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

![Mysql dash](https://dt-cdn.net/images/azuredbformysql-1920-eef37d7ad6.png)

Mysql dash

### Настройка management zone

Чтобы импортировать дашборд для Azure Database for MySQL, нужно [настроить management zone](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Создание management zone и назначение прав доступа к ним."), чтобы ограничить сущности, отображаемые на дашборде, только теми, что относятся к этому сервису.

При создании management zone для этого дашборда:

1. Создайте правило, определяющее сервисы по общему свойству:

   * Тип сервиса равен `Database`
   * Топология сервиса равна `Opaque service`
2. Добавьте условие, чтобы имя базы данных содержало строку `mysql` (с учётом регистра).

Пример

![Management zone для Azure](https://dt-cdn.net/images/azuredbformysqlmanagementzone-2662-467d58e129.webp)

Management zone для Azure

После создания management zone назначьте её дашборду (на дашборде выберите **Edit** > **Settings** > **Default management zone**). Подробнее см. [Временной диапазон дашборда и management zone](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Узнайте о настройках временного диапазона дашборда Dynatrace и management zone.").

## Доступные метрики

| Название | Описание | Единица измерения | Рекомендовано |
| --- | --- | --- | --- |
| active\_connections | Активные подключения | Count | Применимо |
| backup\_storage\_used | Использовано места для резервных копий | Bytes |  |
| cpu\_percent | Процент использования CPU | Percent | Применимо |
| connections\_failed | Неудачные подключения | Count | Применимо |
| io\_consumption\_percent | Процент IO | Percent | Применимо |
| memory\_percent | Процент использования памяти | Percent | Применимо |
| network\_bytes\_ingress | Входящий трафик по активным подключениям | Bytes | Применимо |
| network\_bytes\_egress | Исходящий трафик по активным подключениям | Bytes | Применимо |
| seconds\_behind\_master | Задержка репликации в секундах | Count | Применимо |
| serverlog\_storage\_limit | Лимит места для журналов сервера | Bytes |  |
| serverlog\_storage\_percent | Процент использования места для журналов сервера | Percent | Применимо |
| serverlog\_storage\_usage | Использовано места для журналов сервера | Bytes |  |
| storage\_limit | Лимит места хранения | Bytes |  |
| storage\_percent | Процент использования места хранения | Percent | Применимо |
| storage\_used | Использовано места хранения | Bytes |  |