---
title: Самомониторинг интеграции Dynatrace с GCP
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8/self-monitoring-gcp
scraped: 2026-05-12T11:51:36.733054
---

# Самомониторинг интеграции Dynatrace с GCP

# Самомониторинг интеграции Dynatrace с GCP

* Практическое руководство
* Чтение: 4 мин
* Опубликовано 16 июля 2021 г.

Самомониторинг позволяет быстро провести диагностику и определить, правильно ли функция самомониторинга обрабатывает и отправляет логи в Dynatrace

## Включение самомониторинга

Выполните приведённые ниже шаги в соответствии с вашим сценарием развёртывания.

### Включение самомониторинга для развёртывания GKE

1. Подключитесь к кластеру Kubernetes, в котором запущено развёртывание GCP Monitor.
2. Отредактируйте configmap.

   ```
   kubectl -n dynatrace edit configmaps dynatrace-gcp-monitor-config
   ```
3. Измените значение параметра `SELF_MONITORING_ENABLED` на `true`.
4. Перезапустите GKE GCP Monitor.

   ```
   kubectl -n dynatrace rollout restart deployment dynatrace-gcp-monitor
   ```

### Включение самомониторинга для развёртывания GCP Monitor

1. В консоли Google Cloud перейдите в **Cloud Functions**.
2. Выберите **dynatrace-gcp-monitor**.
3. Выберите **Edit**.
4. В разделе **Runtime, build and connection settings** измените значение runtime-переменной окружения `SELF_MONITORING_ENABLED` на `true`.
5. Выберите **Next**, затем выберите **Deploy**, чтобы применить новые настройки.

## Метрики самомониторинга

Развёртывание Dynatrace GCP Monitor передаёт метрики самомониторинга как метрики Google Cloud. Ниже приведён список метрик самомониторинга для приёма метрик/логов.

### Метрики самомониторинга для развёртывания GKE

**Приём метрик**

| Метрика | Описание |
| --- | --- |
| MINT lines ingested | Количество точек данных (метрик с измерениями), принятых Dynatrace Metrics API v2 за заданный интервал. |
| Dynatrace connectivity | Состояние подключения (`1` = **OK**) между функцией мониторинга и Dynatrace. Подключение может быть нарушено из-за неверного URL Dynatrace, неверного API-токена или проблем с сетевым подключением. |
| Dynatrace failed requests count | Количество запросов, отклонённых Dynatrace Metrics API v2. Причиной отказа может быть то, что значение точки данных не соответствует [синтаксису протокола приёма метрик](https://dt-url.net/0903q6o) или что [превышен лимит на приём метрик](https://dt-url.net/fx03vuq). |
| Dynatrace requests count | Количество запросов, отправленных в Dynatrace. |

**Приём логов**

| Метрика | Описание |
| --- | --- |
| All requests | Все запросы, отправленные в Dynatrace |
| Dynatrace connectivity failures | Количество неудачных запросов на подключение к Dynatrace |
| Too old records | Количество записей логов, оказавшихся недействительными из-за слишком старой временной метки |
| Too long content size | Количество записей с содержимым, превышающим максимальную длину содержимого |
| Parsing errors | Количество ошибок, возникших при разборе логов |
| Processing time | Общее время обработки логов |
| Sending time | Общее время отправки логов |
| Sent logs entries | Количество записей логов, отправленных в Dynatrace |
| Log ingest payload size | Размер полезной нагрузки логов, отправленной в Dynatrace (в КБ) |

### Метрики самомониторинга для развёртывания GCP Monitor

**Приём метрик**

| Метрика | Описание |
| --- | --- |
| MINT lines ingested | Количество точек данных (метрик с измерениями), принятых Dynatrace Metrics API v2 за заданный интервал. |
| Dynatrace connectivity | Состояние подключения (`1` = **OK**) между функцией мониторинга и Dynatrace. Подключение может быть нарушено из-за неверного URL Dynatrace, неверного API-токена или проблем с сетевым подключением. |
| Dynatrace failed requests count | Количество запросов, отклонённых Dynatrace Metrics API v2. Причиной отказа может быть то, что значение точки данных не соответствует [синтаксису протокола приёма метрик](https://dt-url.net/0903q6o) или что [превышен лимит на приём метрик](https://dt-url.net/fx03vuq). |
| Dynatrace requests count | Количество запросов, отправленных в Dynatrace. |

## Просмотр метрик самомониторинга

Дашборды самомониторинга отображают множество метрик, связанных с состоянием подключения к Dynatrace, объёмом обработанных данных и временем выполнения.

Чтобы просмотреть дашборды с метриками самомониторинга

1. В консоли GCP перейдите к сервису GCP Monitoring.
2. Выберите **Dashboards**.
3. В зависимости от выбранного типа развёртывания найдите

   * Дашборд `dynatrace-gcp-monitor log self monitoring` (для логов)
   * Дашборд `dynatrace-gcp-monitor self monitoring` (для метрик)

Пример дашборда:

![Самомониторинг](https://dt-cdn.net/images/self-monitoring-1343-1ba18f72fc.png)

Самомониторинг

## Связанные темы

* [Настройка Dynatrace на Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")