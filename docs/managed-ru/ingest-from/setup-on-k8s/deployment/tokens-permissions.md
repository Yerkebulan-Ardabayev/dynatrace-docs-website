---
title: Токены и разрешения
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions
---

# Токены и разрешения

# Токены и разрешения

* Практическое руководство
* 4 мин на чтение
* Обновлено 15 июля 2026 г.

Токены аутентифицируют и авторизуют вызовы API, гарантируя, что взаимодействовать со средой Dynatrace могут только авторизованные сервисы. В контексте [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator "Компоненты Dynatrace Operator") для Kubernetes используются два токена:

* **Токен Operator**  
  Токен Operator (бывший токен API) позволяет Dynatrace Operator управлять настройками и жизненным циклом всех компонентов Dynatrace в кластере Kubernetes.
* **Токен Data Ingest**  
  Токен Data Ingest обогащает и отправляет дополнительные сигналы observability (например, пользовательские метрики) из кластера Kubernetes в Dynatrace.

Актуальная версия Dynatrace

Dynatrace Classic

Актуальная версия Dynatrace

Для каждого кластера Kubernetes Dynatrace Operator использует два платформенных токена, связанных с выделенным служебным пользователем:

* **Токен Operator**, назначена политика **Kubernetes Operator**. Управляет жизненным циклом всех компонентов Dynatrace в кластере.
* **Токен Data Ingest**, назначена политика **Kubernetes Ingest**. Принимает сигналы observability (метрики, логи, трассировки) из кластера.

Области действия токенов

**Токен Operator**

| Область действия | Использование |
| --- | --- |
| `fleet-management:activegate.connection-info:read` | Сбор информации для жизненного цикла ActiveGate |
| `fleet-management:activegate.tokens:create` | Создание токена аутентификации для подключения ActiveGate к Dynatrace Cluster |
| `fleet-management:container-images:read` | Чтение информации об образах для управляемых компонентов |
| `fleet-management:oneagent.connection-info:read` | Сбор информации для жизненного цикла OneAgent |
| `fleet-management:oneagents:download` | Управление жизненным циклом OneAgent |
| `settings:objects:read` | Чтение настроек для мониторинга Kubernetes API, [KSPM](/managed/upgrade/unavailable-in-managed "Выбранное недоступно в Dynatrace Managed.") и [мониторинга логов](/managed/upgrade/unavailable-in-managed "Выбранное недоступно в Dynatrace Managed.") |
| `settings:objects:write` | Управление настройками для мониторинга Kubernetes API, [KSPM](/managed/upgrade/unavailable-in-managed "Выбранное недоступно в Dynatrace Managed.") и [мониторинга логов](/managed/upgrade/unavailable-in-managed "Выбранное недоступно в Dynatrace Managed.") |

**Токен Data Ingest**

| Область действия | Использование |
| --- | --- |
| `openpipeline:logs:ingest` | Приём логов |
| `openpipeline:metrics:ingest` | Приём метрик |
| `openpipeline:traces:ingest` | Приём трассировок |
| `storage:metrics:write` | Запись метрик в Dynatrace |

Справочная информация по необходимым понятиям:

* [Локальные группы, политики](/managed/upgrade/unavailable-in-managed "Выбранное недоступно в Dynatrace Managed.")
* [Управление служебными пользователями](/managed/upgrade/unavailable-in-managed "Выбранное недоступно в Dynatrace Managed.")
* [Платформенные токены для служебных пользователей](/managed/upgrade/unavailable-in-managed "Выбранное недоступно в Dynatrace Managed.")

Платформенные токены создаются автоматически в рамках процесса [Kubernetes Onboarding](/managed/ingest-from/setup-on-k8s/quickstart "Развёртывание Dynatrace Operator в Kubernetes"), создавать их вручную не требуется, если нет такого желания. Чтобы использовать процесс onboarding, администратор аккаунта должен сначала [предоставить разрешения Kubernetes Onboarding](#grant-privileges) пользователю.

## Создание токенов

### Создание служебного пользователя

1. Перейти в [**Account Management**﻿](https://myaccount.dynatrace.com/). Если аккаунтов несколько, выбрать нужный для управления.
2. Перейти в **Identity & access management** > **Service users**.
3. На странице **Service users** выбрать  **Add service user**.
4. На странице **Create service user** ввести следующие данные служебного пользователя.

   * **Name**
   * Необязательное **Description**

   Оба поля должны быть понятны администраторам среды, чтобы им было ясно назначение служебного пользователя.
5. В разделе **Assign permissions** выбрать назначение следующих разрешений **Directly**:

   * Kubernetes Operator
   * Kubernetes Ingest
6. Выбрать **Create**.

### Создание платформенных токенов

Повторить следующие шаги для токенов Operator и Data Ingest.

1. Перейти в [My platform tokens﻿](https://myaccount.dynatrace.com/platformTokens).
2. Выбрать  **Platform token** и указать:

   * Понятное **Token Name**
   * **Expiration date**
   * **Account**
   * Environment для ограничения области действия токена конкретными средами Dynatrace
3. Выбрать области действия токена в таблице.

   * Для токена Operator включить области действия, перечисленные в разделе [Токен Operator](#operatorToken).
   * Для токена Data Ingest включить области действия, перечисленные в разделе [Токен Data Ingest](#dataIngestToken).
4. Назначить каждый токен служебному пользователю.
5. Выбрать **Generate**, чтобы создать токен.
6. Скопировать токен и сохранить его в надёжном месте. Токен показывается только один раз.
7. Выбрать **Finish and exit**.

## Предоставление пользователям разрешений Kubernetes Onboarding

Выполнить следующие шаги может только администратор аккаунта Dynatrace.

1. Перейти в [**Account Management**﻿](https://myaccount.dynatrace.com/). Если аккаунтов несколько, выбрать нужный для управления.
2. Перейти в **Identity & access management** > **Group management**.
3. На странице **Group management** выбрать  **Create group**.
4. На странице **New group** ввести следующие данные группы.

   * **Name**
   * Необязательное **Description**

   Оба поля должны быть понятны администраторам среды, чтобы им было ясно назначение группы.
5. На вкладке **Permissions** выбрать  **Add permission**.

   * Выбрать **Kubernetes Onboarding** в выпадающем списке **Permissions**, затем указать **Scope** и **Boundaries** для этой группы.
6. На вкладке **Members** выбрать  **Add members**.

   * Выбрать участников в диалоге **Add members to this group**, затем выбрать **Add**.
7. Выбрать **Create**.

## Создание токена

Повторить следующие шаги для токенов Operator и Data Ingest.

1. Перейти в **Access Tokens**.
2. Выбрать **Generate new token**.
3. Указать понятное имя токена.
4. Включить необходимые разрешения для токена.

   1. Для токена Operator выбрать шаблон в **Template** > **Kubernetes: Dynatrace Operator**. Это автоматически добавит необходимые области действия (см. [Токен Operator](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#classic-operatorToken "Настройка токенов и разрешений для мониторинга кластера Kubernetes"))
   2. Для токена Data Ingest выбрать шаблон в **Template** > **Kubernetes: Data Ingest**. Это автоматически добавит необходимые области действия (см. [Токен Data Ingest](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#classic-dataIngestToken "Настройка токенов и разрешений для мониторинга кластера Kubernetes"))
5. Выбрать **Generate token**, чтобы создать токен.
6. Скопировать токен и сохранить его в надёжном месте.

## Просмотр областей действия токена

### Токен Operator

Для токена Operator требуются следующие области действия:

| Область действия | Использование | Версия Dynatrace Operator |
| --- | --- | --- |
| PaaS - Installer (`Installer download`) | Управление жизненным циклом OneAgent и ActiveGate. | Любая версия |
| Access problem and event feed, metrics, and topology (API v1 - `DataExport`) | Уведомление Dynatrace Cluster о штатном отключении. Начиная с версии OneAgent 1.301 штатное отключение хоста обнаруживается без Dynatrace Operator. | <1.6.0 |
| Read settings (API v2 - `settings.read`) | Управление объектом ActiveGate для мониторинга Kubernetes API. [2](#fn-1-2-def) | 0.4.0+ |
| Write settings (API v2 - `settings.write`) | Управление объектом ActiveGate для мониторинга Kubernetes API. [2](#fn-1-2-def) | 0.4.0+ |
| Read entities (API v2 - `entities.read`) | Проверка существования объекта ActiveGate для мониторинга Kubernetes API. [3](#fn-1-3-def) | 0.4.0 - <1.7.0 |
| Create ActiveGate token (API v2 - `activeGateTokenManagement.create`) | Создание токена аутентификации для подключения ActiveGate к Dynatrace Cluster.[1](#fn-1-1-def) | 0.9.0+ |

1

Токен ротируется Dynatrace Operator каждые 30 дней. При ротации токена аутентификации затронутый ActiveGate автоматически удаляется и разворачивается заново.

2

Необязательно начиная с версии Dynatrace Operator v1.7.0+.

3

Больше не требуется начиная с версии Dynatrace Operator v1.7.0+

### Токен Data Ingest

Рекомендуемые области действия токена:

| Область действия | Использование | Минимальная версия DTO |
| --- | --- | --- |
| Ingest metrics (API v2 - `metrics.ingest`) | Включает обогащение метаданными для пользовательских метрик. | 0.4.0+ |
| Ingest logs (API v2 - `logs.ingest`) | Отправка логов через Log Monitoring API v2. | 0.4.0+ |
| Ingest OpenTelemetry traces (API v2 - `openTelemetryTrace.ingest`) | Отправка трассировок OpenTelemetry в Dynatrace | 0.4.0+ |