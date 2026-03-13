---
title: Create a new AWS connection
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/cloud-platform-monitoring/clouds-app/create-aws-connection
scraped: 2026-03-06T21:24:56.840993
---

# Create a new AWS connection

# Создание нового подключения AWS

* Latest Dynatrace
* Практическое руководство
* Чтение: 1 мин
* Опубликовано 19 августа 2025 г.
* Preview

Если вы впервые создаёте подключение, сначала ознакомьтесь с [инструкциями по первоначальной настройке](../../../../ingest-from/amazon-web-services/create-an-aws-connection.md "See the differences between creating your AWS connections via API or ::app-settings::.") и её предварительными требованиями.

Если у вас есть существующее классическое подключение и вы хотите начать использовать новый мониторинг облачных платформ, сначала удалите классическое подключение, и только после этого создайте новое облачное подключение для соответствующей учётной записи AWS.

Чтобы настроить новое подключение AWS

1. Перейдите в ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.
2. В правом верхнем углу страницы выберите **Create connection** > **AWS New**.

   Примечание: если это ваше первое облачное подключение, вы также можете выбрать **Create connection** > **AWS New** на странице Overview.
3. Следуйте шагам в разделе **New connection**, чтобы начать процесс подключения нового облачного соединения AWS.

   ![Clouds app | Create a new AWS connection](https://dt-cdn.net/images/clouds-app-create-an-aws-connection-3840-485c4caab2.png)
4. После успешного развёртывания стека CloudFormation в AWS потребуется до 15 минут, чтобы ваш облачный инвентарь появился на новой вкладке **Explorer New** в разделе ![Clouds](https://dt-cdn.net/images/clouds-1025-170946931c.png "Clouds") **Clouds**.
5. Необязательно Проверьте состояние и работоспособность вашего облачного подключения в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.

   1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Cloud and virtualization**.
   2. Выберите **AWS**.
6. Необязательно Настройте оповещения о состоянии работоспособности и предупреждающие сигналы в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.

   1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Analyze and alert** > **Alerts** > **Cloud services**.
   2. Выберите **New Alerts**.
   3. Следуйте шагам мастера для создания оповещений о состоянии работоспособности для вашей только что подключённой учётной записи AWS.

   ![Settings | Ready-made alerts](https://dt-cdn.net/images/settings-ready-made-alerts-3840-d19f21a2a8.png)![Settings | Health alert details](https://dt-cdn.net/images/settings-health-alert-details-3840-f4fc0982c7.png)

   1 of 2
