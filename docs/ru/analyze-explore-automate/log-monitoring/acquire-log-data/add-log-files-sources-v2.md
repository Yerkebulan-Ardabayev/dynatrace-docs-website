---
title: Источники журналов и хранилище (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2
scraped: 2026-03-06T21:26:49.610500
---

# Источники и хранение логов (Logs Classic)


* 2-min read

Log Monitoring Classic

Начиная с OneAgent версии 1.243 и Dynatrace Cluster версии 1.252, мы настоятельно рекомендуем перейти на [Log Storage](log-storage.md "Configure storage of log files that are already known to OneAgent.").

С выпуском Dynatrace версии 1.285 (март 2024 года) Dynatrace автоматически преобразует ваши конфигурации [источников логов](../../logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-add-log-files-manually.md "Learn how to manually add log files for analysis.") и [хранения логов](../../logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-add-log-file-sources.md "Learn how to include and exclude log sources for analysis.") до актуальной версии.

Вы также можете самостоятельно обновить конфигурацию, выбрав **Upgrade configuration**. Все ваши текущие настройки будут полностью перенесены.

Обновлённая конфигурация (см. [Log ingest rules](../../logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration.md "Include and exclude specific log sources already known to OneAgent for storage and analysis.")), определяемая на страницах **Custom log source configuration** и **Log sources and storage**, предоставит вам:

* Большую гибкость при определении источников логов (например, путь к логу, уровень логирования, пространство имён Kubernetes, развёртывание Kubernetes)
* Гибкость в определении источников логов (с использованием областей окружения, группы хостов и хостов)
* Детализацию управления правами доступа к источникам логов
* Использование REST API для управления источниками логов
* Возможность фильтрации и маскирования данных логов при захвате

Чтобы включить или исключить определённые источники логов из хранения:

1. Перейдите в **Settings** > **Log Monitoring** > **Log sources and storage**.
2. Выберите **Include all logs**, **Include the following logs** или **Exclude the following logs** из списка.
3. Переключайтесь между вкладками для выбора логов с **Hosts perspective** или **Process groups perspective**.

Переключение вкладок

Будут сохранены только источники логов на активной (выбранной) вкладке. Источники логов, отмеченные на другой вкладке, будут проигнорированы.

4. Нажмите **Save changes**.

## Миграция на новую конфигурацию хранения

После перехода в **Settings** > **Log Monitoring** > **Log storage** автоматически запускается миграция со старого формата конфигурации хранения на новый. В вашей текущей конфигурации произойдут следующие изменения:

* **Host perspective**
  Все элементы, настроенные в разделе **Hosts perspective**, мигрируют как набор сопоставителей в соответствующую область хоста.
* **Process groups perspective**
  Мигрируют только правила, применяемые ко всей группе процессов, в область тенанта. Если группа процессов включена лишь для части хостов, соответствующие правила необходимо создать на уровне хоста.

После успешной миграции конфигурации источников логов вы сможете использовать новые элементы конфигурации и добавлять собственные сопоставители.

## Часто задаваемые вопросы

Является ли это изменение обратимым?

Нет. После изменения все старые конфигурации удаляются, поэтому убедитесь в своём решении перед его выполнением.
