---
title: Мониторинг логов z/OS
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs
scraped: 2026-05-12T12:13:52.216822
---

# Мониторинг логов z/OS

# Мониторинг логов z/OS

* Чтение: 4 мин
* Обновлено 28 января 2026 г.

Модуль zRemote версии 1.297+ Модуль zDC версии 1.291+

Анализ логов, как правило, один из первых шагов в диагностике проблем приложений. Поэтому, когда возникает критическая проблема, важно иметь под рукой нужные логи, чтобы быстро и легко увидеть полную картину происходящего в приложениях.

Dynatrace умеет автоматически обнаруживать и собирать логи из мониторируемых регионов IBM CICS и подсистем IBM IMS. Все собранные логи обогащаются метаданными, чтобы привязать их к модели сущностей хостов z/OS (логических разделов) и процессов z/OS (регионов и подсистем). Это позволяет дополнить анализ корневых причин любой проблемы, выявленной Davis AI, логами, автоматически связанными с приложениями.

Подробнее о связанных сценариях использования см. в разделе [Log Management and Analytics](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

Поддерживаются следующие источники логов:

* Модуль CICS версии 1.291+ Оператор `MSGUSR DD` для регионов IBM CICS
* Модуль IMS версии 1.295+ Основной и дополнительный главные терминалы для подсистем IBM IMS

Log Management and Analytics требует лицензии:

* Для Dynatrace Platform Subscription, возможность [Log Management and Analytics](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").
* Для классического лицензирования Dynatrace, [Davis data units](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе Davis data units (DDU).").

## Начало работы

Сбор логов с z/OS требует [правила сбора логов](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."). Можно начать с одного из готовых встроенных правил.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Активируйте правило сбора логов**](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#ingest-rules "Мониторинг логов z/OS с Dynatrace, включая логи регионов CICS и подсистем IMS.")[![Шаг 2 опционально](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Шаг 2 опционально")

**Замаскируйте чувствительные данные логов**](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#mask-data "Мониторинг логов z/OS с Dynatrace, включая логи регионов CICS и подсистем IMS.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Анализируйте данные логов**](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-zos-logs#analyze-logs "Мониторинг логов z/OS с Dynatrace, включая логи регионов CICS и подсистем IMS.")

### Шаг 1 Активация правила сбора логов

Перейдите в **Settings** и выберите **Log Monitoring** > **Log ingest rules**.

Активируйте одно из следующих встроенных правил, чтобы собирать обнаруженные логи из регионов IBM CICS и подсистем IBM IMS в Dynatrace.

| Правило | Условие | Область |
| --- | --- | --- |
| **z/OS CICS message user** | **Log source**: `z/OS CICS message user`  **Log record level**: `ERROR` или `WARN` | Окружение |
| **z/OS IMS master terminal** | **Log source**: `z/OS IMS primary master` или `z/OS IMS secondary master`  **Log record level**: `ERROR` или `WARN` | Окружение |

![Настройки логов z/OS](https://dt-cdn.net/images/zos-log-settings-1651-077ed26fb6.png)

Настройки логов z/OS

#### Ограничение области правил

При необходимости можно ограничить область правила сбора логов конкретной группой LPAR (группой хостов) или LPAR (хостом), чтобы логи собирались только для них.

Для этого определите [правило сбора логов](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") с нужной [областью](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") (группа хостов или хост).

#### Управление тем, какие логи собираются

При необходимости можно использовать атрибуты, чтобы точно управлять тем, какие логи собираются.

Для этого определите [правило сбора логов](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") с конкретными атрибутами, чтобы собирались только логи, удовлетворяющие этим атрибутам. Например, можно использовать следующие атрибуты.

| Атрибут | Описание | Логика выпадающего списка |
| --- | --- | --- |
| **Log source** | Сопоставление по атрибуту **Log source**. Для CICS выберите `z/OS CICS message user`. Для IMS выберите один или оба варианта `z/OS IMS primary master` или `z/OS IMS secondary master`. | Можно ввести вручную. Без ограничения по времени. |
| **Log record level**[1](#fn-1-1-def) | Сопоставление по уровню записи лога. Поддерживаются следующие значения: `alert`, `critical`, `debug`, `emergency`, `error`, `info`, `none`, `notice`, `severe`, `warn`. | Можно ввести вручную. Без ограничения по времени. |
| **Log content** | Сопоставление по содержимому лога; поддерживаются подстановочные знаки в виде звёздочки. | Можно ввести вручную. Без ограничения по времени. |
| **Process group** | Сопоставление по ID группы процессов. | Перечислены сущности, видимые за последние 3 дня. |

1

Атрибут Log record level, преобразуемый OneAgent, отличается от атрибута `status` лога, преобразуемого сервером Dynatrace. Подробнее см. на странице [Автоматическое обогащение логов](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

### Шаг 2 опционально Маскирование чувствительных данных логов

Настройте маскирование чувствительных данных, как описано в разделе [Маскирование чувствительных данных в OneAgent](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

### Шаг 3 Анализ данных логов

Dynatrace Log Analytics открывает новые способы анализа телеметрии, существенно расширяя сценарии наблюдаемости для мейнфреймов IBM Z.

Например, можно быстро исследовать конкретные строки логов с ошибками в **Log Viewer**. Благодаря обогащённым данным логов строки логов связаны с соответствующей страницей **z/OS Host**.

![Логи z/OS в Log viewer](https://dt-cdn.net/images/zos-log-view-1856-7977ddf3ad.png)

Логи z/OS в Log viewer

![Логи z/OS на странице Host](https://dt-cdn.net/images/zos-log-host-1622-00c71be1be.png)

Логи z/OS на странице Host

Также можно выполнять расширенные запросы в **Notebooks** с помощью Dynatrace Query Language (DQL). Например, через DQL можно быстро запросить все abend или детализировать статистику по конкретным заданиям.

![DQL-запрос для логов z/OS](https://dt-cdn.net/images/zos-log-dql-1630-0cc40d3a7d.png)

DQL-запрос для логов z/OS

## FAQ

Какие метаданные добавляются к собранным логам z/OS?

Все собранные логи обогащаются следующими метаданными: `dt.process.name`, `host.name`, `log.source`, `os.name`, `zos.job_id`, `zos.job_name`, `zos_job_step_id`, `dt.entity.host`, `dt.entity.process_group`, `dt.entity.process_group_instance` и `dt.source_entity`.

Эти метаданные используются для привязки логов к модели сущностей процессов z/OS.