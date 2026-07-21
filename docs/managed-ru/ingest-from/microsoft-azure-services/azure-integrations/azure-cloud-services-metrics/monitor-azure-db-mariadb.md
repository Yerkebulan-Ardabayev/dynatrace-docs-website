---
title: Мониторинг Azure Database for MariaDB
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mariadb
---

# Мониторинг Azure Database for MariaDB

# Мониторинг Azure Database for MariaDB

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 25 июня 2020 г.

На странице обзора Azure Database for MariaDB видно, заканчивается ли CPU или наблюдается высокий процент I/O, поэтому всегда понятно, какие запросы нужно оптимизировать.

## Предварительные требования

* Dynatrace версии 1.196+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

О том, как включить мониторинг сервиса, читай в разделе [Включение мониторинга сервисов](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

Дополнительно, для интеграции с OneAgent, см. [как отслеживается активность базы данных](/managed/observe/infrastructure-observability/database-services-classic/how-database-activity-is-monitored "Информация об автоматическом обнаружении и мониторинге сервисов баз данных в среде приложения.").

## Просмотр метрик сервиса

Метрики сервиса можно посмотреть в среде Dynatrace либо на **странице обзора кастомного устройства**, либо на странице **Dashboards**.

### Просмотр метрик на странице обзора кастомного устройства

Чтобы перейти на страницу обзора кастомного устройства

1. Перейти в **Technologies & Processes**.
2. Отфильтровать по названию сервиса и выбрать нужную группу кастомных устройств.
3. После выбора группы кастомных устройств откроется **страница обзора группы кастомных устройств**.
4. На **странице обзора группы кастомных устройств** перечислены все экземпляры (кастомные устройства), входящие в группу. Выбор экземпляра открывает **страницу обзора кастомного устройства**.

### Просмотр метрик на дашборде

Если для сервиса есть готовый (preset) дашборд, на странице **Dashboards** появится готовый дашборд для соответствующего сервиса со всеми рекомендуемыми метриками. Нужные дашборды можно найти, отфильтровав по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться заново сохранить учётные данные, чтобы готовый дашборд появился на странице **Dashboards**. Для этого перейти в **Settings** > **Cloud and virtualization** > **Azure**, выбрать нужный экземпляр Azure, затем нажать **Save**.

Вносить изменения напрямую в готовый дашборд нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, открыть меню обзора (**…**) и выбрать **Clone**.
Чтобы убрать дашборд из списка дашбордов, его можно скрыть. Для этого открыть меню обзора (**…**) и выбрать **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

![Mariadb dash](https://dt-cdn.net/images/azuredbformariadb-3481-86c2844045.png)

Mariadb dash

### Настройка management zone

Чтобы импортировать дашборд для Azure Database for MariaDB, нужно [настроить management zone](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Создание management zones и назначение прав доступа к ним.") и ограничить сущности, отображаемые на дашборде, теми, что относятся к этому сервису.

При создании management zone для этого дашборда:

1. Создать правило, определяющее сервисы по общему свойству:

   * Service type: `Database`
   * Technology: `MariaDB`
   * Service topology: `Opaque service`
2. Добавить условие, чтобы имя базы данных содержало строку `mariadb` (с учётом регистра).

Пример

![Management zone Azure](https://dt-cdn.net/images/azuredbformariadbmanagementzone-2686-28aa52c965.png)

Management zone Azure

После создания management zone выбрать её на своём дашборде (**Edit** > **Settings** > **Default management zone**). Подробнее см. [Период времени и management zone дашборда](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Информация о настройках периода времени и management zone дашборда Dynatrace.").

## Доступные метрики

| Название | Описание | Единица измерения | Рекомендуется |
| --- | --- | --- | --- |
| active\_connections | Активные соединения | Количество | Применимо |
| backup\_storage\_used | Использовано места для резервных копий | Байты |  |
| cpu\_percent | Процент CPU | Проценты | Применимо |
| connections\_failed | Неудавшиеся соединения | Количество | Применимо |
| io\_consumption\_percent | Процент IO | Проценты | Применимо |
| memory\_percent | Процент памяти | Проценты | Применимо |
| network\_bytes\_ingress | Входящий трафик по активным соединениям | Байты | Применимо |
| network\_bytes\_egress | Исходящий трафик по активным соединениям | Байты | Применимо |
| seconds\_behind\_master | Задержка репликации в секундах | Количество | Применимо |
| serverlog\_storage\_limit | Лимит хранилища серверных логов | Байты |  |
| serverlog\_storage\_percent | Процент хранилища серверных логов | Проценты | Применимо |
| serverlog\_storage\_usage | Использовано хранилища серверных логов | Байты |  |
| storage\_limit | Лимит хранилища | Байты |  |
| storage\_percent | Процент использования хранилища | Проценты | Применимо |
| storage\_used | Использовано хранилища | Байты |  |