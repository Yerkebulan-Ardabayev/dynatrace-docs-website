---
title: Мониторинг Azure Application Gateway
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-gateway
scraped: 2026-05-12T11:25:19.783120
---

# Мониторинг Azure Application Gateway

# Мониторинг Azure Application Gateway

* Практическое руководство
* Чтение: 4 мин
* Обновлено 15 ноября 2023 г.

Информацию о различиях между классическими службами и другими службами см. в разделе [Миграция с классических служб Azure (ранее «встроенных») на облачные службы](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Перенос классических служб Azure на их новые версии.").

Dynatrace получает метрики из Azure Metrics API для Azure Application Gateway. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные условия

* Dynatrace версии 1.199+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

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

Этот сервис отслеживает часть Azure Application Gateway (Microsoft.Network/applicationGateways). Пока этот сервис настроен, вы не можете включить сервис Azure Application Gateway.

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| Throughput | Количество байтов в секунду, обслуженных Application Gateway |  | Байт в секунду | Применимо |
| Unhealthy host count | Количество неработоспособных хостов бэкенда | Backend pool HTTP settings | Количество | Применимо |
| Healthy host count | Количество работоспособных хостов бэкенда | Backend pool HTTP settings | Количество | Применимо |
| Total requests | Количество успешных запросов, обслуженных Application Gateway | Backend pool HTTP settings | Количество |  |
| Requests per minute per healthy host | Среднее количество запросов в минуту на работоспособный хост бэкенда в пуле | Backend pool HTTP settings | Количество |  |
| Failed requests | Количество неудачных запросов, обслуженных Application Gateway | Backend pool HTTP settings | Количество | Применимо |
| Response status | Статус HTTP-ответа, возвращённый Application Gateway | HTTP status | Количество | Применимо |
| Current connections | Количество текущих подключений, установленных с Application Gateway |  | Количество | Применимо |
| CPU utilization | Текущее использование ЦП Application Gateway |  | Процент |  |
| New connections per second | Новые подключения в секунду, установленные с Application Gateway |  | В секунду |  |
| Current capacity units | Потреблённые единицы ёмкости |  | Количество |  |
| Fixed billable capacity units | Минимальные единицы ёмкости, за которые будет начислена плата |  | Количество |  |
| Estimated billed capacity units | Расчётные единицы ёмкости, за которые будет начислена плата |  | Количество |  |
| Current compute units | Потреблённые вычислительные единицы |  | Количество |  |
| Backend response status | Количество кодов HTTP-ответов, сгенерированных участниками бэкенда. Не включает коды ответов, сгенерированные Application Gateway. | Backend server, Backend pool, Backend HTTP setting, HTTP status | Количество |  |
| Client TLS protocol | Количество TLS- и не-TLS-запросов, инициированных клиентом, установившим подключение с Application Gateway. Для просмотра распределения протоколов TLS отфильтруйте по измерению TLS Protocol. | Listener, TLS protocol | Количество |  |
| Bytes sent | Общее количество байтов, отправленных Application Gateway клиентам | Listener | Байт |  |
| Bytes received | Общее количество байтов, полученных Application Gateway от клиентов | Listener | Байт |  |
| Client RTT | Время кругового пути между клиентами и Application Gateway. Эта метрика показывает, сколько времени занимает установка подключений и возврат подтверждений | Listener | Миллисекунда |  |
| Application gateway total time | Время, которое требуется для обработки запроса и отправки его ответа. Это интервал от момента, когда Application Gateway получает первый байт HTTP-запроса, до момента завершения операции отправки ответа. Важно отметить, что обычно это включает время обработки Application Gateway, время прохождения пакетов запроса и ответа по сети и время, которое потребовалось серверу бэкенда для ответа. | Listener | Миллисекунда |  |
| Backend connect time | Время, затраченное на установку подключения с сервером бэкенда | Listener, Backend server, Backend pool, Backend HTTP setting | Миллисекунда |  |
| Backend first byte response time | Интервал времени между началом установки подключения к серверу бэкенда и получением первого байта заголовка ответа, приблизительно соответствующий времени обработки сервером бэкенда | Listener, Backend server, Backend pool, Backend HTTP setting | Миллисекунда |  |
| Backend last byte response time | Интервал времени между началом установки подключения к серверу бэкенда и получением последнего байта тела ответа | Listener, Backend server, Backend pool, Backend HTTP setting | Миллисекунда |  |
| Matched count | Общее распределение правил Web Application Firewall для входящего трафика | Rule group, Rule ID | Количество |  |
| Blocked count | Распределение правил Web Application Firewall по заблокированным запросам | Rule group, Rule ID | Количество |  |