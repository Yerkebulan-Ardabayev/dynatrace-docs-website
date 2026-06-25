---
title: Мониторинг Azure Database for MySQL Flexible Servers
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql-flexible-servers
scraped: 2026-05-12T11:26:18.720978
---

# Мониторинг Azure Database for MySQL Flexible Servers

# Мониторинг Azure Database for MySQL Flexible Servers

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 27 августа 2024 г.

С 16 сентября 2024 г. Azure Database for MySQL Flexible Servers заменяет [Azure Database for MySQL Single Server](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql "Мониторинг Azure DB for MySQL и просмотр доступных метрик.").

Страница обзора Azure Database for MySQL Flexible Servers служит комплексным обзором ваших серверов MySQL и экземпляров баз данных. Здесь вы можете получить полную видимость и проверить, работоспособна ли ваша база данных, снижена ли её производительность и есть ли неудачные подключения.

## Предварительные условия

* Dynatrace версии 1.298+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

При желании для интеграции OneAgent см. [как отслеживается активность баз данных](/managed/observe/infrastructure-observability/databases/database-services-classic/how-database-activity-is-monitored "Узнайте об автоматическом обнаружении и мониторинге сервисов баз данных в среде вашего приложения.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в **Technologies & Processes**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса предусмотрен предустановленный дашборд, он появится на вашей странице **Dashboards** с набором всех рекомендуемых метрик. Искать конкретные дашборды можно с помощью фильтрации по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд отобразился на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вы не можете вносить изменения непосредственно в предустановленный дашборд, но можете клонировать его и редактировать. Чтобы клонировать дашборд, откройте меню обзора (**…**) и выберите **Clone**.  
Чтобы убрать дашборд из списка, его можно скрыть. Чтобы скрыть дашборд, откройте меню обзора (**…**) и выберите **Hide**.

Скрытие дашборда не затрагивает других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

## Доступные метрики

| Имя | Описание | Единица измерения | Рекомендуется |
| --- | --- | --- | --- |
| aborted\_connections | Прерванные подключения | Количество | Применимо |
| active\_connections | Активные подключения | Количество | Применимо |
| active\_transactions | Активные транзакции | Количество |  |
| backup\_storage\_used | Использованное хранилище резервных копий | Байт |  |
| binlog\_storage\_used | Использованное хранилище binlog | Байт |  |
| cpu\_credits\_consumed | Израсходованные кредиты ЦП | Количество |  |
| cpu\_credits\_remaining | Оставшиеся кредиты ЦП | Количество |  |
| Com\_alter\_table | Com alter table | Количество |  |
| Com\_create\_db | Com create DB | Количество |  |
| Com\_create\_table | Com create table | Количество |  |
| Com\_delete | Com delete | Количество |  |
| Com\_drop\_db | Com drop DB | Количество |  |
| Com\_drop\_table | Com drop table | Количество |  |
| Com\_insert | Com insert | Количество |  |
| Com\_select | Com select | Количество |  |
| Com\_update | Com update | Количество |  |
| data\_storage\_used | Использованное хранилище данных | Байт |  |
| HA\_IO\_status | Статус ввода-вывода Ha | Количество |  |
| HA\_SQL\_status | Статус SQL Ha | Количество |  |
| HA\_replication\_lag | Задержка репликации Ha | Секунда |  |
| cpu\_percent | Процент использования ЦП хоста | Процент | Применимо |
| network\_bytes\_ingress | Входящий сетевой трафик хоста | Байт | Применимо |
| network\_bytes\_egress | Исходящий сетевой трафик хоста | Байт | Применимо |
| ibdata1\_storage\_used | Использованное хранилище Ibdata1 | Байт |  |
| Innodb\_buffer\_pool\_pages\_data | Страницы данных буферного пула Innodb | Количество |  |
| Innodb\_buffer\_pool\_pages\_dirty | Грязные страницы буферного пула Innodb | Количество |  |
| Innodb\_buffer\_pool\_pages\_flushed | Сброшенные страницы буферного пула Innodb | Количество |  |
| Innodb\_buffer\_pool\_pages\_free | Свободные страницы буферного пула Innodb | Количество |  |
| Innodb\_buffer\_pool\_reads | Чтения буферного пула Innodb | Количество |  |
| Innodb\_data\_writes | Записи данных Innodb | Количество |  |
| Innodb\_row\_lock\_time | Время блокировки строк Innodb | Миллисекунда |  |
| Innodb\_row\_lock\_waits | Ожидания блокировки строк Innodb | Количество |  |
| memory\_percent | Процент использования памяти | Процент | Применимо |
| trx\_rseg\_history\_len | Длина списка истории Mysql | Количество |  |
| lock\_deadlocks | Взаимоблокировки Mysql | Количество |  |
| lock\_timeouts | Тайм-ауты блокировок Mysql | Количество |  |
| Uptime | Время работы Mysql | Секунда |  |
| others\_storage\_used | Использованное прочее хранилище | Байт |  |
| Queries | Запросы | Количество |  |
| Replica\_IO\_Running | Статус ввода-вывода реплики | Количество |  |
| Replica\_SQL\_Running | Статус SQL реплики | Количество |  |
| replication\_lag | Задержка репликации в секундах | Секунда | Применимо |
| serverlog\_storage\_limit | Лимит хранилища журналов сервера | Байт |  |
| serverlog\_storage\_percent | Процент использования хранилища журналов сервера | Процент | Применимо |
| serverlog\_storage\_usage | Использованное хранилище журналов сервера | Байт |  |
| Slow\_queries | Медленные запросы | Количество |  |
| storage\_io\_count | Количество операций ввода-вывода хранилища | Количество |  |
| io\_consumption\_percent | Процент ввода-вывода хранилища | Процент | Применимо |
| storage\_limit | Лимит хранилища | Байт |  |
| storage\_percent | Процент использования хранилища | Процент |  |
| storage\_used | Использованное хранилище | Байт |  |
| Threads\_running | Работающие потоки | Количество |  |
| total\_connections | Всего подключений | Количество |  |