---
title: Какие процессы наиболее важны?
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes
scraped: 2026-05-12T11:14:29.053198
---

# Which are the most important processes?

# Какие процессы наиболее важны?

* How-to guide
* 2-min read
* Updated on Jan 16, 2025

Для просмотра наиболее важных процессов, выполняющихся на конкретном хосте, перейдите в **Hosts** и выберите хост для перехода на страницу его обзора. Перейдите в раздел **Process analysis**, где вы найдёте графики и списки процессов, выполняющихся на выбранном хосте.

В разделе **Process analysis** также отображаются различные экземпляры групп процессов, сгруппированные по типу технологии.

Подробнее см. в разделе [Process analysis](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring#process-analysis "Monitor hosts with Dynatrace.").

Для отображения процессов в этом разделе они должны соответствовать хотя бы одному из следующих критериев:

* Процессы, являющиеся [поддерживаемыми приложениями](/managed/ingest-from/technology-support#applications-services-and-databases "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Процессы с открытым TCP-портом прослушивания.
* Процессы, для которых хотя бы одно из следующих условий выполнялось не менее чем в 3 из последних 5 одноминутных интервалов:

  + **Avg(CPU) > 5%**
  + **Max(Memory) > 5%**
  + **Network Traffic > 5%**.
* Процессы, определённые пользователем как важные, например, путём включения мониторинга журналов для процесса.

Dynatrace также предоставляет возможность [мониторинга конкретных процессов, не попадающих ни в одну из этих категорий](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").

Процессы, не соответствующие вышеуказанным критериям и поэтому не считающиеся важными, агрегируются и обозначаются как **Other processes**.

## Сведения о группе процессов

Список процессов предоставляет основную информацию о системных и сетевых ресурсах, потребляемых процессом.

| Ресурс | Описание |
| --- | --- |
| CPU usage | Процент использования CPU процессом. |
| Memory usage | Процент системной памяти, потребляемой процессом. |
| Traffic | Сетевой трафик к процессу и от него. |
| Retransmissions | Повторно переданные пакеты (в любом направлении). |
| Connectivity | Процент успешно установленных TCP-сессий минус сумма процента отклонённых TCP-соединений и процента превышений тайм-аута TCP-соединений. |

## Почему Dynatrace не отображает рабочие процессы?

Например, при работе Apache HTTP Server вы можете быть привычны к длинным спискам рабочих процессов (см. пример ниже). В данном примере на терминале Linux перечислены многочисленные процессы Apache HTTP Server. Однако для наглядности и удобства управления Dynatrace объединяет такие списки в экземпляры групп процессов. Это происходит как между хостами, так и на отдельных хостах.

![Processgroup apache2](https://dt-cdn.net/images/processgroup-apache2-460-e9af3aa576.png)

Processgroup apache2