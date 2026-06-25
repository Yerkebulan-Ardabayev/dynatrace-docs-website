---
title: Настройки мониторинга сервисов
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-settings
scraped: 2026-05-12T11:21:59.603131
---

# Настройки мониторинга сервисов

# Настройки мониторинга сервисов

* Reference
* 2-min read
* Updated on Feb 17, 2026

Настройки сервисов можно изменять как глобально — для всех сервисов в окружении — так и для отдельных сервисов.

Окружение

Для глобального определения настроек сервисов перейдите в **Settings** > **Server-side service monitoring**.

Сервис

Чтобы определить настройки для отдельного сервиса

1. Перейдите в **Services**.
2. Выберите сервис для настройки.
3. На странице обзора сервиса выберите **More** (**…**) > **Settings**.

Для большинства настроек доступны API.

Правила и настройки на уровне сервиса переопределяют глобально определённые.

| Настройка | Глобально (веб-интерфейс) | API | На уровне сервиса (веб-интерфейс) |
| --- | --- | --- | --- |
| [Обнаружение сбоев](/managed/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection "Узнайте, какие типы ошибок сервисов Dynatrace обнаруживает автоматически, и узнайте, как настроить параметры обнаружения сбоев.") | Применимо | Применимо | Применимо |
| [Ключевые запросы](/managed/observe/application-observability/services-classic/monitor-key-requests "Узнайте, как тщательно отслеживать запросы, критически важные для вашего бизнеса.") | Применимо | Применимо | Применимо |
| [Заглушение запросов](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-monitoring-mute "Отключайте мониторинг определённых запросов сервисов, чтобы сосредоточиться на производительности запросов, влияющих на ваших клиентов.") | Применимо | Применимо | Применимо |
| [Обнаружение аномалий](/managed/dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services "Узнайте, как адаптировать чувствительность обнаружения проблем для сервисов.") | Применимо | Применимо | Применимо |
| [Пользовательские правила обнаружения сервисов](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Используйте правила обнаружения для настройки и улучшения автоматического обнаружения ваших сервисов.") | Применимо | Применимо | Неприменимо |
| [Пользовательские правила именования сервисов](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-naming "Используйте правила именования для настройки и улучшения автоматического именования ваших сервисов.") | Применимо | Применимо | Неприменимо |
| [Пользовательские сервисы](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Определяйте точки входа (метод, класс или интерфейс) для пользовательских сервисов, не использующих стандартные протоколы.") | Применимо | Применимо | Неприменимо |
| [Messaging services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services "Настраивайте пользовательские messaging services для трассировки очередей сообщений.") | Применимо | Применимо | Неприменимо |
| [Объединённые сервисы](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services "Объедините несколько сервисов веб-запросов одной группы процессов в один сервис.") Устарело [1](#fn-1-1-def) | Применимо | Неприменимо | Неприменимо |
| [Unified services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service "Определяйте сервисы на основе сигналов наблюдаемости, принятых через Trace ingest API.") | Применимо | Применимо | Применимо |
| [Атрибуты запросов](/managed/observe/application-observability/services/request-attributes "Поймите, что такое атрибуты запросов, и узнайте, как использовать их на всех уровнях всех представлений анализа сервисов.") | Применимо | Применимо | Неприменимо |
| [Пользовательские определения API](/managed/observe/application-observability/services/customize-api-definitions "Настройте правила обнаружения для настройки API в вашем окружении.") | Применимо | Применимо | Неприменимо |
| [Вычисляемая метрика сервиса](/managed/observe/application-observability/services/calculated-service-metric "Узнайте, как создать вычисляемую метрику на основе веб-запросов.") | Применимо | Применимо | Неприменимо |
| [Правила именования запросов](/managed/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Настройте именование запросов и определите операции, предлагаемые вашими сервисами.") | Неприменимо | Применимо | Применимо |
| [Мониторинг сторонних сервисов](/managed/observe/application-observability/services/service-detection/service-detection-v1/monitor-3rd-party-services "Настройте способ мониторинга сторонних сервисов в Dynatrace.") | Неприменимо | Применимо | Применимо |

1

Эквивалент объединённого сервиса можно создать через [Пользовательские правила обнаружения сервисов](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Используйте правила обнаружения для настройки и улучшения автоматического обнаружения ваших сервисов."). Существующие объединённые сервисы можно просматривать и редактировать через веб-интерфейс Dynatrace.