---
title: Пользовательские приложения
source: https://www.dynatrace.com/docs/observe/digital-experience/custom-applications
scraped: 2026-03-06T21:14:00.392814
---

# Пользовательские приложения

# Пользовательские приложения

* Classic
* Обзор
* Чтение: 1 мин
* Опубликовано 6 февраля 2023

Пользовательские приложения охватывают все цифровые точки взаимодействия в вашей среде — от традиционных клиентских приложений до умных IoT-приложений и даже навыков Alexa. Такие приложения поддерживаются с помощью [Dynatrace OpenKit](../../ingest-from/extend-dynatrace/openkit.md "Узнайте, как инструментировать ваше приложение с помощью OpenKit, как использовать методы API Dynatrace OpenKit и многое другое.").

### Начальная настройка

[Начальная настройка RUM для пользовательских приложений](custom-applications/custom-rum-initial-setup.md "Включите и настройте мониторинг реальных пользователей для пользовательских приложений.")

### Настройка

* [Библиотеки Dynatrace OpenKit на GitHub](../../ingest-from/extend-dynatrace/openkit/dynatrace-openkit-libraries-on-github.md "Ознакомьтесь с библиотеками Dynatrace OpenKit на GitHub.")
* [Методы API Dynatrace OpenKit](../../ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods.md "Узнайте, как использовать Dynatrace OpenKit с точки зрения разработчика.")
* [Логирование Dynatrace OpenKit](../../ingest-from/extend-dynatrace/openkit/dynatrace-openkit-logging.md "Узнайте, как работает логирование в OpenKit.")

### Анализ и использование данных RUM

* [Анализ пользовательских сеансов пользовательских приложений](custom-applications/analyze-and-use/user-session-analysis-custom.md "Фильтруйте пользовательские сеансы, просматривайте сеансы отдельного пользователя и изучайте сбои, ошибки запросов и ошибки отчётов для ваших пользовательских приложений.")
* [Проверка метрик пользовательского опыта для пользовательских приложений](custom-applications/analyze-and-use/check-usage-metrics-custom.md "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта вашего пользовательского приложения.")
* [Анализ веб-запросов для пользовательских приложений](custom-applications/analyze-and-use/analyze-web-requests-custom.md "Используйте Dynatrace для мониторинга веб-запросов ваших пользовательских приложений.")
* [Просмотр отчётов о сбоях для пользовательских приложений](custom-applications/analyze-and-use/crash-reports-custom.md "Просматривайте последние отчёты о сбоях для ваших пользовательских приложений.")
* [Использование свойств действий пользователя и сеансов для пользовательских приложений](custom-applications/analyze-and-use/action-and-session-properties-custom.md "Свойства действий пользователя и сеансов — это пары ключ-значение метаданных, которые обеспечивают дополнительную видимость и более глубокий анализ опыта конечных пользователей. Используя эти свойства для ваших приложений, вы можете фильтровать пользовательские сеансы, добавлять вычисляемые метрики, создавать графики и многое другое.")

### Устранение неполадок

[Устранение неполадок RUM для пользовательских приложений](custom-applications/troubleshooting.md "Устраните проблемы, связанные с RUM для ваших пользовательских приложений.")

### Дополнительная конфигурация

* [Настройка контроля стоимости и трафика для пользовательских приложений](custom-applications/additional-configuration/configure-cost-and-traffic-control-custom.md "Используйте настройку контроля стоимости и трафика в Dynatrace для сокращения использования сеансов пользовательских приложений.")
* [Игнорирование ошибок веб-запросов для пользовательских приложений](custom-applications/additional-configuration/web-request-errors-custom.md "Прекратите обработку определённых кодов ответа HTTP как ошибок для ваших пользовательских приложений.")
* [Создание пользовательских имён действий для пользовательских приложений](custom-applications/additional-configuration/naming-rules-custom.md "Настройте автоматически сгенерированные имена действий пользователя для ваших пользовательских приложений.")
* [Настройка ключевых действий пользователя для пользовательских приложений](custom-applications/additional-configuration/configure-key-user-actions-custom.md "Отметьте действие пользователя как ключевое и настройте рейтинг Apdex для ключевых действий пользователя ваших пользовательских приложений.")
* [Настройка параметров Apdex для пользовательских приложений](custom-applications/additional-configuration/configure-apdex-custom.md "Настройте пороги производительности удовлетворённости пользователей для вашего пользовательского приложения и его ключевых действий.")
* [Изменение порогов оценки пользовательского опыта для пользовательских приложений](custom-applications/additional-configuration/configure-user-experience-score-custom.md "Настройте пороги оценки пользовательского опыта в соответствии с конкретными требованиями вашего пользовательского приложения.")
* [Создание вычисляемых метрик для пользовательских приложений](custom-applications/additional-configuration/rum-calculated-metrics-custom.md "Создавайте вычисляемые метрики и пользовательские графики на основе вычисляемых метрик для ваших пользовательских приложений.")
* [Создание пользовательских метрик USQL для пользовательских приложений](custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps.md "Каждый раз при закрытии пользовательского сеанса Dynatrace может извлекать метрики и сохранять их как временные ряды. Узнайте, как настроить и использовать пользовательские метрики USQL для пользовательских приложений.")
* [Определение свойств действий пользователя и сеансов для пользовательских приложений](custom-applications/additional-configuration/define-custom-action-and-session-properties.md "Отправляйте метаданные в Dynatrace и определяйте свойства действий и сеансов для ваших отслеживаемых пользовательских приложений.")
* [Настройка определения IP-адресов для пользовательских приложений](custom-applications/additional-configuration/customize-ip-address-detectio-custom.md "Измените способ определения IP-адресов клиентов в Dynatrace для ваших пользовательских приложений.")
* [Сопоставление внутренних IP-адресов с местоположениями для пользовательских приложений](custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom.md "Настройте Dynatrace для использования локальных адресов, чтобы определить, где находятся пользователи ваших пользовательских приложений.")
* [Настройка обнаружения собственных, сторонних и CDN-ресурсов для пользовательских приложений](custom-applications/additional-configuration/configure-third-party-and-cdn-content-detection-custom.md "Вручную определите сторонних и CDN-провайдеров наряду с автоматически обнаруженными провайдерами для ваших пользовательских приложений.")
* [Использование OneAgent в качестве конечной точки для маяков пользовательских приложений](custom-applications/additional-configuration/oneagent-as-beacon-forwarder-custom.md "Используйте Dynatrace OneAgent в качестве конечной точки для маяков пользовательских приложений.")
* [Удаление пользовательского приложения](custom-applications/additional-configuration/delete-application-custom.md "Удалите ваши пользовательские приложения через веб-интерфейс Dynatrace или API.")
