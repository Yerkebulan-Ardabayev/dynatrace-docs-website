---
title: Приложение Anomaly Detection
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app
scraped: 2026-03-06T21:14:57.037010
---

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** -- единый обзор всех конфигураций обнаружения аномалий в среде Dynatrace.

## Предварительные требования

### Разрешения

| Разрешение | Описание |
| --- | --- |
| `settings:schemas:read` | Чтение схем настроек |
| `settings:objects:read` | Чтение объектов настроек |
| `settings:objects:write` | Запись объектов настроек |
| `iam:bindings:read/write` | Чтение/запись привязок политик авторизации |
| `iam:service-users:use` | Использование сервисных пользователей |
| `davis:analyzers:read/execute` | Чтение/выполнение анализаторов |
| `state:user-app-states:read/write` | Чтение/запись пользовательских настроек |

Разрешения настраиваются в **Account Management** > **Identity and Access Management**.

### Установка

Убедитесь, что приложение [установлено](../../manage/hub.md#install).

## Авторизация

При первом запуске включите авторизацию: **Settings** > **Authorization settings** > выберите разрешения.

## Обзор

Приложение показывает: статус конфигураций, источник, тип модели прогнозирования. Столбцы настраиваются через **Column settings**, таблица поддерживает фильтрацию.

## Обучающие модули

1. [Руководство по написанию DQL](anomaly-detection-app/davis-ad-dql-best-practice.md)
2. [Руководство по оптимизации DQL](anomaly-detection-app/davis-ad-dql-optimization.md)
3. [Настройка простого пользовательского оповещения](anomaly-detection-app/configure-a-simple-ad.md)
4. [Настройка расширенного пользовательского оповещения](../../../common/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-an-advanced-ad.md)
5. [Типы статусов Anomaly Detection](anomaly-detection-app/anomaly-detection-status-types.md)

## Акторы пользовательских оповещений

Каждое оповещение выполняется в контексте пользователя (актора). Администраторы могут выбирать между актором и сервисным пользователем.

* **Актор** -- пользователь, назначенный для выполнения оповещения. При редактировании чужого оповещения оно становится новым с разрешениями нового актора.
* **Сервисный пользователь** (рекомендуется для организаций) -- делает оповещение независимым от статуса конкретного пользователя. Разрешения следуют принципу минимальных привилегий.

## Связанные темы

* Типы статусов Anomaly Detection
* Ограничения Dynatrace Intelligence
* [[Видео] Anomaly Detection и безопасность](https://www.youtube.com/watch?v=WDZUus-VxCE)
* [[Видео] Anomaly Detection и наблюдаемость](https://www.youtube.com/watch?v=HPQi63mQg3w)
