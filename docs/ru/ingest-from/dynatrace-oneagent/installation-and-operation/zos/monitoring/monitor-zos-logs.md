---
title: Monitor z/OS logs
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs
scraped: 2026-03-06T21:37:55.780096
---

# Мониторинг логов z/OS

# Мониторинг логов z/OS

* Последняя версия Dynatrace
* Чтение: 4 мин
* Обновлено 28 января 2026 г.

Модуль zRemote версии 1.297+, модуль zDC версии 1.291+

Анализ логов обычно является одним из первых шагов при устранении неполадок приложений. При возникновении критической проблемы крайне важно иметь нужные логи, чтобы быстро и легко понять полную картину происходящего в ваших приложениях.

Dynatrace может автоматически обнаруживать и собирать логи из отслеживаемых регионов IBM CICS и подсистем IBM IMS. Все собранные логи обогащаются метаданными для их сопоставления с моделью сущностей хостов z/OS (логических разделов) и процессов z/OS (регионов и подсистем). Это позволяет расширить анализ основных причин для любой проблемы, выявленной каузальным ИИ Dynatrace Intelligence, с помощью логов, автоматически связанных с вашими приложениями.

Чтобы узнать больше о связанных сценариях использования, см. [Log Management and Analytics](/docs/analyze-explore-automate/logs/lma-use-cases "Explore common Log Management and Analytics use cases in Dynatrace deployments.").

Поддерживаются следующие источники логов:

* Модуль CICS версии 1.291+: оператор MSGUSR DD для регионов IBM CICS
* Модуль IMS версии 1.295+: основной и вторичный главный терминал для подсистем IBM IMS

Log Management and Analytics требует лицензию:

* Для Dynatrace Platform Subscription — возможность [Log Management and Analytics](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").
* Для классического лицензирования Dynatrace — [единицы данных Davis](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).").

## Начало работы

Сбор логов из z/OS требует [правила приёма логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis."). Вы можете начать, используя одно из существующих встроенных правил.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Активация правила приёма логов**](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#ingest-rules "Monitor your z/OS logs with Dynatrace, including logs from CICS regions and IMS subsystems.")[![Шаг 2 (необязательный)](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Маскирование конфиденциальных данных в логах**](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#mask-data "Monitor your z/OS logs with Dynatrace, including logs from CICS regions and IMS subsystems.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Анализ данных логов**](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#analyze-logs "Monitor your z/OS logs with Dynatrace, including logs from CICS regions and IMS subsystems.")

### Шаг 1. Активация правила приёма логов

Перейдите в **Settings** и выберите **Log Monitoring** > **Log ingest rules**.

Активируйте одно из следующих встроенных правил для приёма обнаруженных логов из ваших регионов IBM CICS и подсистем IBM IMS в Dynatrace.

![Настройки логов z/OS](https://dt-cdn.net/images/zos-log-settings-1651-077ed26fb6.png)

#### Ограничение области действия правил

При необходимости вы можете ограничить область действия правила приёма логов определённой группой LPAR (группой хостов) или конкретным LPAR (хостом), чтобы логи принимались только для них.

Для этого определите [правило приёма логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.") с необходимой [областью действия](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration#scopes "Include and exclude specific log sources already known to OneAgent for storage and analysis.") (группа хостов или хост).

#### Управление приёмом логов

При необходимости вы можете использовать атрибуты для точного управления тем, какие логи принимаются.

Для этого определите [правило приёма логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.") с конкретными атрибутами, чтобы принимались только логи, соответствующие этим атрибутам. Например, вы можете использовать следующие атрибуты.

1

Атрибут уровня записи лога, преобразованный OneAgent, отличается от атрибута `status` лога, преобразованного сервером Dynatrace. Подробнее см. на странице [Автоматическое обогащение логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa#transform-all-types-of-logs "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.").

### Шаг 2 (необязательный). Маскирование конфиденциальных данных в логах

Настройте маскирование конфиденциальных данных, как описано в разделе [Маскирование конфиденциальных данных в OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking "Mask sensitive information in your log data using Log Management and Analytics.").

### Шаг 3. Анализ данных логов

Dynatrace Log Analytics предоставляет новые способы анализа телеметрических данных, значительно расширяя сценарии наблюдаемости для мейнфреймов IBM Z.

Например, вы можете быстро исследовать конкретные строки логов с ошибками в **Log Viewer**. Благодаря обогащённым данным логов строки логов связаны с соответствующей страницей **z/OS Host**.

![Логи z/OS в Log Viewer](https://dt-cdn.net/images/zos-log-view-1856-7977ddf3ad.png)

![Логи z/OS на странице хоста](https://dt-cdn.net/images/zos-log-host-1622-00c71be1be.png)

Вы также можете выполнять расширенные запросы в **Notebooks** с помощью Dynatrace Query Language (DQL). Например, с помощью DQL вы можете быстро запросить все аварийные завершения (abend) или детализировать статистику конкретных заданий.

![DQL-запрос для логов z/OS](https://dt-cdn.net/images/zos-log-dql-1630-0cc40d3a7d.png)

## Часто задаваемые вопросы

Какие метаданные добавляются к принятым логам z/OS?

Все принятые логи обогащаются следующими метаданными: `dt.process.name`, `host.name`, `log.source`, `os.name`, `zos.job_id`, `zos.job_name`, `zos_job_step_id`, `dt.entity.host`, `dt.entity.process_group`, `dt.entity.process_group_instance` и `dt.source_entity`.

Эти метаданные используются для сопоставления логов с моделью сущностей процессов z/OS.