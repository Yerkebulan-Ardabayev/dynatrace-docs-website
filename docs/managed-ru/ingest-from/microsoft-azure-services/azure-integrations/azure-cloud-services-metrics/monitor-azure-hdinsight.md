---
title: Мониторинг Azure HDInsight
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight
scraped: 2026-05-12T11:26:41.410610
---

# Мониторинг Azure HDInsight

# Мониторинг Azure HDInsight

* Практическое руководство
* Чтение: 4 мин
* Обновлено 22 января 2026 г.

Dynatrace получает метрики из Azure Metrics API для Azure HDInsight. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.  
На дашборде Azure HDInsights вы получаете целостное представление о ресурсах Hadoop, Spark и Kafka и можете охватить мониторинг больших данных со всех сторон в одном месте.

## Предварительные требования

* Dynatrace версии 1.196+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

О том, как включить мониторинг сервиса, см. в разделе [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Установка OneAgent Необязательно

Для получения дополнительных данных мониторинга по Hadoop, Spark и Kafka можно установить OneAgent на узлы кластера Azure HDInsight.

Как установить OneAgent на кластер Azure HDInsight (Linux)

Выполните приведённые ниже шаги, чтобы установить OneAgent на кластер Azure HDInsight (Linux).

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создайте скрипт установки**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-1 "Мониторинг Azure HDInsight и просмотр доступных метрик.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создайте кластер HDInsight**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-2 "Мониторинг Azure HDInsight и просмотр доступных метрик.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Перезапустите процессы**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight#step-3 "Мониторинг Azure HDInsight и просмотр доступных метрик.")

### Шаг 1 Создайте скрипт установки

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **Linux**.

3. На странице **Install Dynatrace OneAgent on your Linux hosts** скопируйте команду под надписью **Use this command on the target host** и команду под надписью **And run the installer with root rights** в текстовый документ с именем `installdynatrace.sh` и сохраните его на локальном компьютере.

**Пример скрипта установки**

```
wget  -O Dynatrace-OneAgent-Linux-1.137.163.sh "https://YOURTENANT.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?Api-Token=YOURAPITOKEN&arch=x86&flavor=default"



/bin/sh Dynatrace-OneAgent-Linux-1.137.163.sh  --set-app-log-content-access=1
```

3. Откройте Microsoft Azure Storage Explorer и загрузите установочный файл Dynatrace `installdynatrace.sh` в доступный контейнер Blob Storage.
4. Щёлкните правой кнопкой мыши по `installdynatrace.sh` и выберите **Set public access level**. Во всплывающем окне установите уровень доступа **Public read access for container and blobs** и нажмите **Apply**.
5. В верхнем меню окна Microsoft Azure Storage Explorer нажмите "Copy URL" и сохраните ссылку локально для последующего доступа.

### Шаг 2 Создайте кластер HDInsight

1. Войдите на портал Microsoft Azure и выберите **HDInsight clusters** в меню слева.
2. Выберите **Create hdinsight cluster**.
3. Выберите установку **Custom**.
4. Следуйте мастеру создания, чтобы настроить базовые параметры, параметры хранилища, приложения и размер кластера.
5. В меню **Advanced settings** выберите **Script Actions**.
6. Выберите **Submit new**.
7. В меню **Submit script action** укажите тип скрипта **Custom**, выберите имя, например **Install Dynatrace**, и вставьте URL скопированного ранее скрипта в поле **Bash script URI**. Если вы хотите установить Dynatrace OneAgent на все узлы, выберите все типы узлов (**Head**, **Worker**, **Zookeeper**).
8. Нажмите **Create**, чтобы сохранить изменения и создать кластер HDInsight.

### Шаг 3 Перезапустите процессы

После завершения установки обязательно перезапустите процессы.

1. Выберите только что созданный кластер на портале Microsoft Azure. В меню **Overview** нажмите на URL вашего кластера.
2. Для каждого узла, где вы выбрали установку Dynatrace, перейдите в **Service Actions** и выберите **Restart All**.

Как только процессы будут перезапущены, Dynatrace начнёт собирать метрики.

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

![Hdinsights azure](https://dt-cdn.net/images/hdinsights-custom-dashboard-1898-9e1893ad04.png)

Hdinsights azure

### Настройка зоны управления

Чтобы импортировать дашборд для Azure HDInsight, необходимо [настроить зону управления](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Создание зон управления и назначение прав доступа к ним."), чтобы ограничить отображаемые на дашборде сущности только узлами кластера и исключить другие хосты, не относящиеся к сервису.

При создании зоны управления для этого дашборда:

1. Создайте правило, которое определяет хосты по общему свойству:

   * Имя хоста содержит строку `hdi`
2. Создайте правило, которое определяет пользовательские устройства по общему свойству:

   * Группа пользовательских устройств содержит строку `HDInsight`.
3. Создайте правило, которое определяет сервисы по общему свойству:

   * Service technology: `Apache Hadoop`
   * Service technology: `Apache Hadoop Distributed File System`
   * Service technology: `Spark`

Пример

![Azure management zone](https://dt-cdn.net/images/hdinsightmanagementzone-2629-26e6039169.webp)

Azure management zone

После создания зоны управления назначьте её своему дашборду (на дашборде выберите **Edit** > **Settings** > **Default management zone**). Дополнительную информацию см. в разделе [Временной интервал и зона управления дашборда](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Узнайте о настройках временного интервала и зоны управления дашбордов Dynatrace.").

## Доступные метрики

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| CategorizedGatewayRequests | Количество запросов к шлюзу по категориям (1xx/2xx/3xx/4xx/5xx) | HttpStatus | Количество |  |
| GatewayRequests | Количество запросов к шлюзу | HttpStatus | Количество | Применимо |
| NumActiveWorkers | Количество активных рабочих процессов | MetricName | Количество | Применимо |