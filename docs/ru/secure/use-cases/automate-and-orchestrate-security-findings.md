---
title: Автоматизация и оркестрация результатов безопасности
source: https://www.dynatrace.com/docs/secure/use-cases/automate-and-orchestrate-security-findings
scraped: 2026-03-06T21:15:08.084731
---

# Автоматизация и оркестрация результатов проверок безопасности

# Автоматизация и оркестрация результатов проверок безопасности

* Latest Dynatrace
* Tutorial
* Published Aug 30, 2024

Приоритизация и устранение выявленных проблем безопасности требуют значительных ручных усилий. При большом количестве различных инструментов безопасности эффективная оркестрация результатов и сосредоточение внимания на критических проблемах становятся невозможными.

Изолированные продукты могут обеспечивать локальную автоматизацию, однако зачастую генерируют избыточный шум. В результате команды разработчиков в итоге игнорируют оповещения и задачи, а уровень защищённости снижается.

В данном контексте вы можете:

* [Ingesting security findings](../threat-observability/security-events-ingest.md "Ingest external security data into Grail.") из различных инструментов и сопоставлять их со [Словарём семантики Dynatrace](https://dt-url.net/3q03pb0).
* Автоматизировать и оркестрировать результаты проверок безопасности в разных продуктах и инструментах с помощью наших примеров автоматизации рабочих процессов, которые вы можете дополнительно настраивать с использованием мощных возможностей [Workflows](../../analyze-explore-automate/workflows.md "Automate IT processes with Dynatrace Workflows—react to events, schedule tasks, and connect services.") в соответствии с процессами оркестрации вашей организации.

## Целевая аудитория

Архитекторы и менеджеры по безопасности, стремящиеся оптимизировать процессы устранения проблем и направить усилия команд разработчиков на эффективное исправление.

Ключевые сценарии использования:

* Создание задач для устранения обнаруженных критических проблем
* Уведомление соответствующих заинтересованных сторон о критических результатах
* Формирование отчётов по электронной почте о наиболее значимых выявленных проблемах

## Предварительные условия

[Ingesting security findings](../threat-observability/security-events-ingest.md "Ingest external security data into Grail.") из стороннего продукта.

## Начало работы

1. Загрузите наш [пример рабочего процесса с GitHub](https://dt-url.net/l403xh0).

   * Для результатов, связанных с уязвимостями, вместо этого загрузите следующие примеры рабочих процессов:

     + [Пример рабочего процесса Slack](https://dt-url.net/ko43qsm)
     + [Пример рабочего процесса Jira](https://dt-url.net/od23qa1)
   * Для результатов, связанных с уязвимостями контейнеров, вместо этого загрузите следующие примеры рабочих процессов:

     + [Пример рабочего процесса Slack](https://dt-url.net/a643qqd)
     + [Пример рабочего процесса Jira](https://dt-url.net/l103p3t)

   Для некоторых интеграций, например [Amazon ECR](../threat-observability/security-events-ingest/ingest-aws-ecr-data.md "Ingest Amazon ECR container image vulnerability findings and scan events and analyze them in Dynatrace.") или [AWS Security Hub](../threat-observability/security-events-ingest/ingest-aws-security-hub.md "Ingest AWS Security Hub security findings and analyze them in Dynatrace."), примеры рабочих процессов доступны непосредственно в приложении в разделе **Try our templates** (в **Settings** найдите и выберите приложение).
2. Откройте [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](../../analyze-explore-automate/workflows.md "Automate IT processes with Dynatrace Workflows—react to events, schedule tasks, and connect services."), выберите ![Import](https://dt-cdn.net/images/dashboards-app-dashboards-page-import-6a06e645df.svg "Import") **Upload**, затем выберите загруженный файл.

Пример результата:

![email notification example](https://dt-cdn.net/images/image-54-1103-3883848f65.png)
