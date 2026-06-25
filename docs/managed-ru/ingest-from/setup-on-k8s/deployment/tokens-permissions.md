---
title: Токены доступа и разрешения
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions
scraped: 2026-05-12T12:03:32.287634
---

# Токены доступа и разрешения

# Токены доступа и разрешения

* Чтение: 4 мин
* Обновлено 05 сентября 2025 г.

Токены доступа используются для аутентификации и авторизации вызовов API, гарантируя, что только авторизованные сервисы могут взаимодействовать с вашим окружением Dynatrace. В контексте Dynatrace Operator для Kubernetes обычно используются два типа токенов:

* **Operator token**
  Токен Operator (ранее API token) используется Dynatrace Operator для управления настройками и жизненным циклом всех компонентов Dynatrace в кластере Kubernetes.
* **Data Ingest token**
  Токен приёма данных используется для обогащения и отправки дополнительных сигналов observability (например, пользовательских метрик) из вашего кластера Kubernetes в Dynatrace.

## Создание токена

Повторите следующие шаги для токенов Operator и Data Ingest.

1. Перейдите в **Access Tokens**.
2. Выберите **Generate new token**.
3. Укажите осмысленное имя для токена.
4. Включите требуемые разрешения для токена.

   1. Для токена Operator выберите шаблон в **Template** > **Kubernetes: Dynatrace Operator**. Это автоматически добавит требуемые области (см. [Operator token](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#operatorToken "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes"))
   2. Для токена Data Ingest выберите шаблон в **Template** > **Kubernetes: Data Ingest**. Это автоматически добавит требуемые области (см. [Data Ingest token](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes"))
5. Выберите **Generate token**, чтобы создать токен.
6. Обязательно скопируйте токен и сохраните его в надёжном месте.

## Области токенов

### Токен Operator

Токен Operator требует следующих областей:

| Область | Использование | Версия Dynatrace Operator |
| --- | --- | --- |
| PaaS - Installer (`Installer download`) | Управляет жизненным циклом OneAgent и ActiveGate. | Любая версия |
| Access problem and event feed, metrics, and topology (API v1 - `DataExport`) | Уведомляет Dynatrace Cluster о корректном завершении работы. Начиная с версии OneAgent 1.301, корректное завершение работы хоста определяется без Dynatrace Operator. | <1.6.0 |
| Read settings (API v2 - `settings.read`) | Управление объектом ActiveGate для мониторинга Kubernetes API. [2](#fn-1-2-def) | 0.4.0+ |
| Write settings (API v2 - `settings.write`) | Управление объектом ActiveGate для мониторинга Kubernetes API. [2](#fn-1-2-def) | 0.4.0+ |
| Read entities (API v2 - `entities.read`) | Проверяет, существует ли объект ActiveGate для мониторинга Kubernetes API. [3](#fn-1-3-def) | 0.4.0 - <1.7.0 |
| Create ActiveGate token (API v2 - `activeGateTokenManagement.create`) | Создаёт токен аутентификации для подключения вашего ActiveGate к Dynatrace Cluster.[1](#fn-1-1-def) | 0.9.0+ |

1

Токен ротируется Dynatrace Operator каждые 30 дней. При ротации токена аутентификации затронутый ActiveGate автоматически удаляется и развёртывается заново.

2

Необязательно начиная с версии Dynatrace Operator v1.7.0+.

3

Больше не требуется с версией Dynatrace Operator v1.7.0+

### Токен приёма данных

Рекомендуемые области токена:

| Область | Использование | Минимальная версия DTO |
| --- | --- | --- |
| Ingest metrics (API v2 - `metrics.ingest`) | Включает обогащение метаданными для пользовательских метрик. | 0.4.0+ |
| Ingest logs (API v2 - `logs.ingest`) | Отправка логов через Log Monitoring API v2. | 0.4.0+ |
| Ingest OpenTelemetry traces (API v2 - `openTelemetryTrace.ingest`) | Отправка трассировок OpenTelemetry в Dynatrace | 0.4.0+ |

## Связанные темы

* [Токены доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Изучите концепцию токена доступа и его областей.")