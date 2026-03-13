---
title: Automated threat-alert triaging
source: https://www.dynatrace.com/docs/secure/use-cases/automated-threat-alert-triaging
scraped: 2026-03-06T21:32:55.922343
---

# Автоматизированная сортировка оповещений об угрозах

# Автоматизированная сортировка оповещений об угрозах

* Latest Dynatrace
* Учебное руководство
* Обновлено 26 июн. 2025 г.

Команды безопасности сталкиваются с необходимостью просеивать огромные объёмы данных безопасности, чтобы выявлять потенциальные угрозы и реагировать на них, расставлять приоритеты оповещений и оценивать серьёзность событий. В отсутствие контекста аналитики тратят ценное время на сортировку шума, переключение между инструментами и рискуют упустить важную информацию, что приводит к задержкам реагирования и неэффективности в операциях безопасности.

Платформа Dynatrace решает эту проблему, предоставляя возможности контекстуализации безопасности, такие как обогащение данными разведки угроз. Различные результаты обнаружения безопасности на платформе Dynatrace содержат наблюдаемые объекты, например IP-адреса. Теперь эти объекты можно обогащать данными о репутации и другим контекстом угроз, что позволяет:

* Классифицировать и расставлять приоритеты оповещений
* Снижать уровень шума
* Быстро реагировать на оповещения об угрозах

## Целевая аудитория

Эта статья предназначена для команд реагирования на инциденты, которые хотят автоматизировать сортировку новых обнаружений с помощью разведки угроз.

## Сценарий

* Новый результат обнаружения безопасности из [Amazon GuardDuty](https://aws.amazon.com/guardduty/) загружается на платформу Dynatrace.
* Команда безопасности хочет получать уведомления в Slack только о новых критических обнаружениях от субъекта, чей IP-адрес классифицирован как вредоносный источником разведки угроз [AbuseIPDB](https://www.abuseipdb.com/).

Тот же сценарий применим к другим поддерживаемым интеграциям для обогащения и загрузки данных безопасности.

## Предварительные требования

* [Установите и настройте интеграцию Amazon GuardDuty](../threat-observability/security-events-ingest/ingest-amazon-guardduty.md "Ingest Amazon GuardDuty security findings and analyze them in Dynatrace.") (или любую другую [поддерживаемую интеграцию загрузки данных](../threat-observability/security-events-ingest.md#ingest "Ingest external security data into Grail.")).
* [Установите и настройте обогащение AbuseIPDB](../threat-observability/security-events-ingest/abuseipdb-enrich.md "Enrich threat observables with AbuseIPDB and analyze them in Dynatrace.") (или любую другую [поддерживаемую интеграцию обогащения](../threat-observability/security-events-ingest.md#enrich "Ingest external security data into Grail.")).
* Пользователи должны иметь разрешение `security-intelligence:enrichments:run` для запуска обогащений.

## Начало работы

1. Импорт рабочего процесса

Импортируйте образец рабочего процесса, доступный как шаблон в приложении **AbuseIPDB**.

1. В Dynatrace откройте **Settings**, затем найдите и выберите **AbuseIPDB**.
2. В разделе **Templates** выберите и импортируйте образец рабочего процесса.

2. Включение обогащения

Для запуска действия рабочего процесса обогащения необходимо включить разрешение `security-intelligence:enrichments:run`.

1. Перейдите в меню настроек в правом верхнем углу ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** и выберите **Authorization settings**.
2. В разделе **Secondary permissions** найдите и выберите разрешение `security-intelligence:enrichments:run`.
3. Нажмите **Save**.

3. Настройка рабочего процесса

Настройте действие DQL-запроса или сообщение уведомления Slack под свои нужды.

![customize workflow](https://dt-cdn.net/images/image-20250602-114203-2544-00ee8d9d9a.png)

4. Тестирование рабочего процесса

Запустите рабочий процесс для его тестирования.

Пример уведомления:

![test workflow](https://dt-cdn.net/images/image-20250602-115603-977-1c24ffce39.png)

5. Сохранение рабочего процесса

Запланируйте и сохраните рабочий процесс для автоматического запуска.

## Связанные темы

* [Оповещения и уведомления](../../analyze-explore-automate/alerting-and-notifications.md "Utilize anomaly detection, problem detection, and workflows for external notifications to ensure that critical problems never go unnoticed.")
