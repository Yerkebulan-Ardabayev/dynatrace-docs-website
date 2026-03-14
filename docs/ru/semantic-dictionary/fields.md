---
title: Справочник глобальных полей
source: https://www.dynatrace.com/docs/semantic-dictionary/fields
scraped: 2026-03-06T21:09:59.423818
---

# Справочник глобальных полей


* Последняя версия Dynatrace
* Обзор
* Обновлено 23 февраля 2026 г.

Следующий справочник содержит список глобальных полей с чётко определённым семантическим значением в Dynatrace, которые могут использоваться в различных типах мониторинга. Поля организованы в пространства имён, разделённые точками.

### Поля верхнего уровня

Поля верхнего уровня содержат информацию, актуальную для всех данных мониторинга.

| Атрибут | Тип | Описание | Примеры |
| --- | --- | --- | --- |
| `timestamp` | timestamp | stable Время (UNIX Epoch в наносекундах), когда произошло событие, обычно когда источник его создал. Если исходная метка времени недоступна, она будет заполнена во время приёма данных. В случае коррелированного события это время может отличаться от времени event.start. | `1649822520123123123` |
| `timeframe` | record[] | stable Временной диапазон, представленный записью временного ряда. |  |
| `start_time` | timestamp | stable Время начала точки данных. Значение — UNIX Epoch в наносекундах, меньше или равно `end_time`. | `1649822520123123123` |
| `end_time` | timestamp | stable Время окончания точки данных. Значение — UNIX Epoch в наносекундах, больше или равно `start_time`. | `1649822520123123165` |
| `duration` | duration | stable Разница между `start_time` и `end_time` в наносекундах. | `42` |
| `interval` | string | stable Обозначает временной диапазон, представленный отдельными измерениями временного ряда. | `1 min` |

## Adobe

### Поля

| Атрибут | Тип | Описание | Примеры |
| --- | --- | --- | --- |
| `adobe.em.env_type` | string | resource experimental Тип среды Adobe Experience Manager (AEM). | `dev`; `stage`; `prod` |
| `adobe.em.program` | string | resource experimental Сервис Adobe Experience Manager (AEM). Содержит определённое клиентом имя среды AEM. |  |
| `adobe.em.service` | string | resource experimental Сервис Adobe Experience Manager (AEM). Содержит идентификаторы программы и среды. |  |
| `adobe.em.tier` | string | resource experimental Уровень Adobe Experience Manager (AEM). | `author`; `publish`; `preview` |

## Агрегация

OneAgent может агрегировать спаны с одним и тем же родительским спаном в один спан. Агрегированный спан содержит атрибуты, указывающие на агрегацию и позволяющие восстановить подробности.

Для агрегированных спанов `start_time` содержит самый ранний `start_time`, а `end_time` — самый поздний `end_time` всех агрегированных спанов.

### Поля

| Атрибут | Тип | Описание | Примеры |
| --- | --- | --- | --- |
| `aggregation.count` | long | stable Количество спанов, агрегированных в данный спан. Значение >1. | `3` |
| `aggregation.duration_max` | duration | stable Длительность в наносекундах самого длинного агрегированного спана. | `482` |
| `aggregation.duration_min` | duration | stable Длительность в наносекундах самого короткого агрегированного спана. | `42` |
| `aggregation.duration_samples` | duration[] | stable Массив выборочных длительностей агрегированных спанов. | `[42, 482, 301]` |
| `aggregation.duration_sum` | duration | stable Сумма длительностей в наносекундах всех агрегированных спанов. | `123` |
| `aggregation.exception_count` | long | stable Количество агрегированных спанов, содержащих исключение. | `0`; `6` |
| `aggregation.parallel_execution` | boolean | stable `true` указывает, что агрегированные спаны могли выполняться параллельно. |  |

## Apache HTTP Server

### Поля

| Атрибут | Тип | Описание | Примеры |
| --- | --- | --- | --- |
| `apache.tomcat.base` | string | resource experimental Базовый каталог сервера (CATALINA\_BASE). | `/usr/share/tomcat6` |
| `apache.tomcat.home` | string | resource experimental Домашний каталог сервера (CATALINA\_HOME). | `/usr/share/tomcat6` |
| `apache.httpd.config.path` | string | resource experimental |  |
| `apache.httpd.module.name` | string | resource experimental Имя модуля Apache HTTP Server, сгенерировавшего запись в логе. | `core`; `proxy` |
| `apache.spark.master.ip` | string | resource experimental |  |

## Приложение

Пространство имён app содержит информацию о приложении, отправляющем событие.

### Поля

| Атрибут | Тип | Описание | Примеры |
| --- | --- | --- | --- |
| `app.bundle` | string | resource stable Имя пакета, например, идентификатор пакета в iOS или `applicationId` в Android. | `com.example.easytravel` |
| `app.id` | string | resource stable Необязательный уникальный идентификатор приложения. Определяется клиентом. | `easytravel` |
| `app.short_version` | string | resource stable Публично видимый номер версии приложения, отображаемый, например, в App Store или Google Play. | `5.23` |
| `app.version` | string | resource stable Внутренний номер сборки приложения, который может включать информацию, такую как номер патча и номер сборки. | `5.23.15789`; `143542` |

## Непрерывная интеграция / непрерывное развёртывание

Пространство имён `argocd` содержит атрибуты развёртывания, специфичные для Argo CD.

### Поля

| Атрибут | Тип | Описание | Примеры |
| --- | --- | --- | --- |
| `argocd.app.health.status` | string | experimental Состояние работоспособности отслеживаемого ресурса. | `Healthy`; `Progressing`; `Degraded`; `Missing`; `Suspended`; `Unknown` |
| `argocd.sync.operation_state.outcome` | string | experimental Сообщение, связанное с операцией синхронизации. | `successfully synced (no more tasks)` |
| `argocd.sync.operation_state.phase` | string | experimental Статус операции синхронизации между источником и целью. | `Running`; `Succeeded`; `Error`; `Failed` |
| `argocd.sync.status` | string | experimental Статус синхронизации представляет текущее состояние согласования. | `SYNCED`; `OUT OF SYNC`; `UNKNOWN` |

## Артефакт

Пространство имён `artifact` содержит информацию о программных артефактах.

### Поля

| Атрибут | Тип | Описание | Примеры |
| --- | --- | --- | --- |
| `artifact.filename` | string | experimental Имя файла программного артефакта, обычно генерируемого процессом сборки. | `carts-service-amd64-0.1.1.tar.gz` |
| `artifact.hash` | string | experimental Полное хеш-значение программного артефакта. | `6c323d126547f71fafb4bffa02cdc480fb284678644ef0b6c69029f051fe5137` |
| `artifact.id` | string | experimental Идентификатор программного артефакта, обычно имя артефакта. | `carts-service` |
| `artifact.name` | string | experimental Человекочитаемое имя программного артефакта. | `Carts service` |
| `artifact.version` | string | experimental Версия программного артефакта, обычно в формате [Semantic Versioning](https://semver.org/). | `0.1.1` |

## ASP.NET Core

### Поля

| Атрибут | Тип | Описание | Примеры |
| --- | --- | --- | --- |
| `aspnetcore.appl.path` | string | resource experimental |  |

## Аудит

Поля, которые могут появляться в журналах аудита.

### Поля

| Атрибут | Тип | Описание | Примеры |
| --- | --- | --- | --- |
| `audit.action` | string | stable Аудируемое действие. | `Access to Azure Resource Manager`; `New User Created` |
| `audit.identity` | string | stable Имя пользователя, учётная запись службы или имя участника-субъекта, выполняющего аудируемое действие. | `name.surname@example.com` |
| `audit.result` | string | stable Результат аудируемого действия. | `Succeeded`; `Failed` |
| `audit.status` | string | stable Статус аудируемого действия. | `Started`; `In Progress`; `Succeeded`; `Failed` |
| `audit.time` | timestamp | experimental Метка времени аудируемого действия. | `16/01/2025, 10:34 AM` |

## Аутентификация

Тип и метод аутентификации, используемые для входа в систему Dynatrace.

### Поля

| Атрибут | Тип | Описание | Примеры |
| --- | --- | --- | --- |
| `authentication.client.id` | string | experimental Идентификатор клиента OAuth2, если тип 'CLIENT\_CREDENTIALS'. | `<DYNATRACE_TOKEN_PLACEHOLDER>` |
| `authentication.grant.type` | string | experimental Тип предоставления, используемый при аутентификации OAuth2. | `AUTHORIZATION_CODE`; `CLIENT_CREDENTIALS` |
| `authentication.token` | string | experimental Публичный идентификатор токена аутентификации типа 'TOKEN'. | `<DYNATRACE_TOKEN_PLACEHOLDER>` |
| `authentication.type` | string | experimental Метод аутентификации. | `OAUTH2` |

## Доступность

Информация о доступности сущности. Пример использования — отчёт о доступности хостов и PGI от OS Agent.
Значение availability.state может использоваться для расчёта агрегированной доступности.
