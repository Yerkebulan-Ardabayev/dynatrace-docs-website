---
title: Мониторинг Azure HDInsight
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight
scraped: 2026-03-05T21:37:08.478436
---

* Latest Dynatrace
* How-to guide
* 4-min read

Dynatrace получает метрики из Azure Metrics API для Azure HDInsight. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.
На дашборде Azure HDInsight вы получаете целостное представление о ваших ресурсах Hadoop, Spark и Kafka и можете охватить все аспекты мониторинга больших данных в одном месте.

## Предварительные требования

* Dynatrace версии 1.196+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. Включение мониторинга сервиса.

## Установка OneAgent (необязательно)

Для получения дополнительных данных о Hadoop, Spark и Kafka вы можете установить OneAgent на узлы кластера Azure HDInsight.

Как установить OneAgent на кластер Azure HDInsight (Linux)

Выполните следующие шаги для установки OneAgent на кластер Azure HDInsight (Linux).

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание скрипта установки**](../../../../../ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight.md#step-1 "Мониторинг Azure HDInsight и просмотр доступных метрик.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создание кластера HDInsight**](../../../../../ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight.md#step-2 "Мониторинг Azure HDInsight и просмотр доступных метрик.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Перезапуск процессов**](../../../../../ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight.md#step-3 "Мониторинг Azure HDInsight и просмотр доступных метрик.")

### Шаг 1: Создание скрипта установки

1. В Dynatrace Hub выберите **OneAgent**.
2. Выберите **Set up** > **Linux**.

3. На странице **Install Dynatrace OneAgent on your Linux hosts** скопируйте команду из раздела **Use this command on the target host** и команду из раздела **And run the installer with root rights** в текстовый файл с именем `installdynatrace.sh` и сохраните его на локальном компьютере.

**Пример скрипта установки**

```
wget  -O Dynatrace-OneAgent-Linux-1.137.163.sh "https://YOURTENANT.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?Api-Token=YOURAPITOKEN&arch=x86&flavor=default"


/bin/sh Dynatrace-OneAgent-Linux-1.137.163.sh  --set-app-log-content-access=1
```

3. Перейдите в Microsoft Azure Storage Explorer и загрузите файл установки Dynatrace `installdynatrace.sh` в доступный контейнер Blob Storage.
4. Нажмите правой кнопкой мыши на `installdynatrace.sh` и выберите **Set public access level**. Во всплывающем окне установите уровень доступа на **Public read access for container and blobs** и нажмите **Apply**.
5. В верхнем меню окна Microsoft Azure Storage Explorer нажмите на "Copy URL" и сохраните URL локально для дальнейшего использования.

### Шаг 2: Создание кластера HDInsight

1. Войдите на портал Microsoft Azure и выберите **HDInsight clusters** в меню слева.
2. Выберите **Create hdinsight cluster**.
3. Выберите **Custom** установку.
4. Следуйте мастеру создания для настройки базовых параметров, хранилища, приложений и размера кластера.
5. В меню **Advanced settings** выберите **Script Actions**.
6. Выберите **Submit new**.
7. В меню **Submit script action** введите **Custom** для типа скрипта, выберите имя, например **Install Dynatrace**, и вставьте URL скрипта, который вы скопировали ранее, в поле **Bash script URI**. Если вы хотите установить Dynatrace OneAgent на все узлы, выберите все типы узлов (**Head**, **Worker**, **Zookeeper**).
8. Выберите **Create**, чтобы сохранить изменения и создать кластер HDInsight.

### Шаг 3: Перезапуск процессов

После завершения установки обязательно перезапустите процессы.

1. Выберите только что созданный кластер на портале Microsoft Azure. В меню **Overview** нажмите на URL-адрес вашего кластера.
2. Для каждого узла, на котором вы выбрали установку Dynatrace, перейдите в **Service Actions** и выберите **Restart All**.

Как только процессы будут перезапущены, Dynatrace начнёт собирать метрики.

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашем окружении Dynatrace как на **странице обзора пользовательского устройства**, так и на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса существует предустановленный дашборд, вы получите предустановленный дашборд для соответствующего сервиса со всеми рекомендуемыми метриками на странице **Dashboards**. Вы можете искать определённые дашборды, фильтруя по **Preset** и затем по **Name**.

Для уже мониторируемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленный дашборд появился на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure и нажмите **Save**.

Вы не можете вносить изменения непосредственно в предустановленный дашборд, но можете клонировать и отредактировать его. Для клонирования дашборда откройте контекстное меню (**...**) и выберите **Clone**.
Чтобы убрать дашборд из списка дашбордов, вы можете скрыть его. Для скрытия дашборда откройте контекстное меню (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Hdinsights azure](https://dt-cdn.net/images/hdinsights-custom-dashboard-1898-9e1893ad04.png)

### Настройка зоны управления

Для импорта дашборда для Azure HDInsight необходимо настроить зону управления для ограничения отображаемых на дашборде объектов только узлами кластера и исключения других хостов, не относящихся к сервису.

При создании зоны управления для этого дашборда:

1. Создайте правило, идентифицирующее хосты на основе общего свойства:

   * Имя хоста содержит строку `hdi`
2. Создайте правило, идентифицирующее пользовательские устройства на основе общего свойства:

   * Группа пользовательских устройств содержит строку `HDInsight`.
3. Создайте правило, идентифицирующее сервисы на основе общего свойства:

   * Технология сервиса: `Apache Hadoop`
   * Технология сервиса: `Apache Hadoop Distributed File System`
   * Технология сервиса: `Spark`

Пример

![Azure management zone](https://dt-cdn.net/images/hdinsightmanagementzone-2629-26e6039169.webp)

После создания зоны управления назначьте её вашему дашборду (из дашборда выберите **Edit** > **Settings** > **Default management zone**). Дополнительную информацию см. в разделе Временные рамки и зона управления дашборда.

## Доступные метрики

| Название | Описание | Измерения | Единица | Рекомендуемая |
| --- | --- | --- | --- | --- |
| CategorizedGatewayRequests | Количество запросов шлюза по категориям (1xx/2xx/3xx/4xx/5xx) | HttpStatus | Count |  |
| GatewayRequests | Количество запросов шлюза | HttpStatus | Count | Да |
| NumActiveWorkers | Количество активных воркеров | MetricName | Count | Да |
