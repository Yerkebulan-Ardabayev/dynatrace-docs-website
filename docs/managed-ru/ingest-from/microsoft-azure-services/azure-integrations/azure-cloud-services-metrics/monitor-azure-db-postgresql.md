---
title: Мониторинг Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-postgresql
---

# Мониторинг Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server)

# Мониторинг Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server)

* Практическое руководство
* Чтение: 6 мин
* Опубликовано 25 июня 2020 г.

На обзорных страницах Azure Database for PostgreSQL (Single Server, Hyperscale, Flexible Server) можно увидеть различные аспекты производительности базы данных: использование CPU и памяти, активные подключения, объём хранилища и многое другое.

## Предварительные требования

* Dynatrace версии 1.196+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

О том, как включить мониторинг сервиса, рассказано в разделе [Включение мониторинга сервисов](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

Дополнительно, для интеграции с OneAgent, см. [как отслеживается активность базы данных](/managed/observe/infrastructure-observability/database-services-classic/how-database-activity-is-monitored "Узнайте об автоматическом обнаружении и мониторинге сервисов баз данных в среде приложения.").

## Просмотр метрик сервиса

Метрики сервиса в среде Dynatrace можно просматривать либо на **обзорной странице custom device**, либо на странице **Dashboards**.

### Просмотр метрик на обзорной странице custom device

Чтобы перейти на обзорную страницу custom device

1. Перейти в раздел **Technologies & Processes**.
2. Отфильтровать по названию сервиса и выбрать нужную группу custom device.
3. После выбора группы custom device открывается **обзорная страница группы custom device**.
4. На **обзорной странице группы custom device** перечислены все экземпляры (custom devices), входящие в группу. Нужно выбрать экземпляр, чтобы открыть **обзорную страницу custom device**.

### Просмотр метрик на дашборде

Если для сервиса есть готовый дашборд, на странице **Dashboards** появится преднастроенный дашборд для соответствующего сервиса со всеми рекомендованными метриками. Нужные дашборды можно найти, отфильтровав по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы преднастроенный дашборд появился на странице **Dashboards**. Для этого нужно перейти в **Settings** > **Cloud and virtualization** > **Azure**, выбрать нужный экземпляр Azure и нажать **Save**.

Изменения напрямую в преднастроенном дашборде вносить нельзя, но его можно клонировать и редактировать. Чтобы клонировать дашборд, нужно открыть меню обзора (**…**) и выбрать **Clone**.
Чтобы убрать дашборд из списка дашбордов, его можно скрыть. Для этого нужно открыть меню обзора (**…**) и выбрать **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

![Postgres dash](https://dt-cdn.net/images/azuredbforpostgresql-2976-bc0290ba6d.png)

Postgres dash

![Hyper](https://dt-cdn.net/images/azuredbforpostgresqlhyperscale-3017-95194857cf.png)

Hyper

### Настройка management zone

Чтобы импортировать дашборд для Azure Database for PostgreSQL, нужно [настроить management zone](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Создание management zone и назначение прав доступа к ним."), чтобы ограничить набор сущностей, отображаемых на дашборде, теми, что относятся к этому сервису.

При создании management zone для этого дашборда:

1. Создать правило, которое определяет сервисы по общему свойству:

   * Service topology: `Opaque service`
   * Service type: `Database`
2. Добавить условие, чтобы название базы данных содержало строку `postgres` (с учётом регистра).

Пример

![Management zone Azure](https://dt-cdn.net/images/azuredbforpostgresqlmanagementzone-2700-c85a5f89c0.webp)

Management zone Azure

В настройках правил видно, требует ли дашборд management zone.

После создания management zone нужно назначить её дашборду (на дашборде выбрать **Edit** > **Settings** > **Default management zone**). Подробнее см. в разделе [Период времени и management zone дашборда](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Узнайте о настройках периода времени и management zone дашборда Dynatrace.").

## Доступные метрики

### Azure Database for PostgreSQL (Single Server)

| Название | Описание | Единица измерения | Рекомендуется |
| --- | --- | --- | --- |
| active\_connections | Количество активных подключений к серверу | Count | Применимо |
| backup\_storage\_used | Объём используемого хранилища резервных копий. Эта метрика представляет собой сумму хранилища, потребляемого всеми полными резервными копиями базы данных, дифференциальными резервными копиями и резервными копиями журналов, хранящимися в соответствии с периодом хранения резервных копий, заданным для сервера. | Bytes |  |
| cpu\_percent | Процент используемого CPU | Percent | Применимо |
| connections\_failed | Количество установленных подключений, которые завершились ошибкой | Count | Применимо |
| io\_consumption\_percent | Процент используемого IO | Percent | Применимо |
| pg\_replica\_log\_delay\_in\_bytes | Отставание в байтах наиболее отстающей реплики | Bytes |  |
| memory\_percent | Процент используемой памяти | Percent | Применимо |
| network\_bytes\_ingress | Входящий сетевой трафик по активным подключениям | Bytes | Применимо |
| network\_bytes\_egress | Исходящий сетевой трафик по активным подключениям | Bytes | Применимо |
| pg\_replica\_log\_delay\_in\_seconds | Время с момента последней воспроизведённой транзакции. Эта метрика доступна только для серверов-реплик. | Seconds | Применимо |
| serverlog\_storage\_limit | Максимальный объём хранилища журналов сервера для данного сервера | Bytes |  |
| serverlog\_storage\_percent | Процент использования хранилища журналов сервера от максимального объёма хранилища журналов сервера | Percent | Применимо |
| serverlog\_storage\_usage | Объём используемого хранилища журналов сервера | Bytes |  |
| storage\_limit | Максимальный объём хранилища для данного сервера | Bytes |  |
| storage\_percent | Процент использования хранилища от максимального объёма сервера | Percent | Применимо |
| storage\_used | Объём используемого хранилища. Хранилище, используемое сервисом, может включать файлы базы данных, журналы транзакций и журналы сервера. | Bytes |  |

### Azure Database for PostgreSQL Hyperscale

| Название | Описание | Единица измерения | Рекомендуется |
| --- | --- | --- | --- |
| active\_connections | Количество активных подключений к серверу | Count | Применимо |
| cpu\_percent | Процент используемого CPU | Percent | Применимо |
| iops | Количество запросов, которые приложение отправляет на диски хранилища за одну секунду | Count | Применимо |
| memory\_percent | Процент используемой памяти | Percent | Применимо |
| network\_bytes\_egress | Исходящий сетевой трафик по активным подключениям | Byte | Применимо |
| network\_bytes\_ingress | Входящий сетевой трафик по активным подключениям | Byte | Применимо |
| storage\_percent | Процент использования хранилища от максимального объёма сервера | Percent | Применимо |
| storage\_used | Объём используемого хранилища. Хранилище, используемое сервисом, может включать файлы базы данных, журналы транзакций и журналы сервера. | Byte |  |

### Azure Database for PostgreSQL - Flexible Server

| Название | Описание | Единица измерения | Рекомендуется |
| --- | --- | --- | --- |
| active\_connections | Количество подключений к серверу. | Count | Применимо |
| backup\_storage\_used | Объём используемого хранилища резервных копий. Эта метрика представляет собой сумму хранилища, потребляемого всеми полными резервными копиями базы данных, дифференциальными резервными копиями и резервными копиями журналов, хранящимися в соответствии с периодом хранения резервных копий, заданным для сервера. Частота резервного копирования определяется сервисом. Для геоизбыточного хранилища объём используемого хранилища резервных копий вдвое больше, чем для локально избыточного хранилища. | Byte |  |
| connections\_failed | Подключения, завершившиеся ошибкой. | Count | Применимо |
| connections\_succeeded | Успешные подключения. | Count |  |
| cpu\_credits\_consumed | Количество кредитов, использованных flexible server. Применимо для уровня Burstable. | Count |  |
| cpu\_credits\_remaining | Количество кредитов, доступных для burst. Применимо для уровня Burstable. | Count |  |
| cpu\_percent | Процент используемого CPU. | Percent | Применимо |
| disk\_queue\_depth | Количество незавершённых операций ввода-вывода к диску данных. | Count |  |
| iops | Количество операций ввода-вывода к диску в секунду. | Count | Применимо |
| maximum\_used\_transactionIDs | Максимальный используемый ID транзакции. | Count |  |
| memory\_percent | Процент используемой памяти. | Percent | Применимо |
| network\_bytes\_ingress | Объём входящего сетевого трафика. | Byte | Применимо |
| network\_bytes\_egress | Объём исходящего сетевого трафика. | Byte | Применимо |
| read\_iops | Количество операций чтения ввода-вывода к диску данных в секунду. | Count |  |
| read\_throughput | Байт, считанных с диска в секунду. | Count | Применимо |
| storage\_free | Объём доступного пространства хранилища. | Byte |  |
| storage\_percent | Процент использования пространства хранилища. Хранилище, используемое сервисом, может включать файлы базы данных, журналы транзакций и журналы сервера. | Percent | Применимо |
| storage\_used | Хранилище, используемое сервисом, может включать файлы базы данных, журналы транзакций и журналы сервера. | Byte |  |
| txlogs\_storage\_used | Объём пространства хранилища, используемого журналами транзакций. | Byte |  |
| write\_iops | Количество операций записи ввода-вывода к диску данных в секунду. | Count |  |
| write\_throughput | Байт, записанных на диск в секунду. | Count | Применимо |