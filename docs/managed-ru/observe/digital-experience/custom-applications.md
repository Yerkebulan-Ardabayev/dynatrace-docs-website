---
title: Пользовательские приложения
source: https://docs.dynatrace.com/managed/observe/digital-experience/custom-applications
scraped: 2026-05-12T11:07:25.869031
---

# Пользовательские приложения

# Пользовательские приложения

* Overview
* 1-min read
* Published Feb 06, 2023

Пользовательские приложения охватывают все цифровые точки взаимодействия в вашей среде: от традиционных rich client-приложений до интеллектуальных IoT-приложений и даже Alexa Skills. Поддержка таких приложений реализована через [Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit "Узнайте, как инструментировать приложение с помощью OpenKit, как использовать методы Dynatrace OpenKit API и многое другое.").

### Начальная настройка

[Начальная настройка RUM для пользовательских приложений](/managed/observe/digital-experience/custom-applications/custom-rum-initial-setup "Включите и настройте мониторинг реальных пользователей для пользовательских приложений.")

### Настройка

* [Библиотеки Dynatrace OpenKit на GitHub](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-libraries-on-github "Ознакомьтесь с библиотеками Dynatrace OpenKit на GitHub.")
* [Методы API Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods "Узнайте, как использовать Dynatrace OpenKit с точки зрения разработчика.")
* [Логирование Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-logging "Узнайте, как работает логирование с OpenKit.")

### Анализ и использование RUM-данных

* [Анализ пользовательских сессий в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/analyze-and-use/user-session-analysis-custom "Фильтруйте сессии пользователей, просматривайте сессии отдельного пользователя и анализируйте сбои, ошибки запросов и зафиксированные ошибки в пользовательских приложениях.")
* [Проверка метрик пользовательского опыта в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/analyze-and-use/check-usage-metrics-custom "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта вашего пользовательского приложения.")
* [Анализ веб-запросов в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/analyze-and-use/analyze-web-requests-custom "Используйте Dynatrace для мониторинга веб-запросов в пользовательских приложениях.")
* [Просмотр отчётов о сбоях в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/analyze-and-use/crash-reports-custom "Проверьте последние отчёты о сбоях в ваших пользовательских приложениях.")
* [Использование свойств действий и сессий пользователей в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/analyze-and-use/action-and-session-properties-custom "Свойства действий и сессий пользователей — это метаданные в формате «ключ-значение», которые обеспечивают дополнительную видимость и более глубокий анализ взаимодействия конечных пользователей. Используя эти свойства, вы можете фильтровать сессии, добавлять вычисляемые метрики, создавать диаграммы и многое другое.")

### Устранение проблем

[Устранение проблем RUM для пользовательских приложений](/managed/observe/digital-experience/custom-applications/troubleshooting "Устраните проблемы, связанные с RUM для ваших пользовательских приложений.")

### Дополнительная настройка

* [Настройка контроля затрат и трафика для пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-cost-and-traffic-control-custom "Используйте настройку контроля затрат и трафика в Dynatrace для сокращения потребления сессий в пользовательских приложениях.")
* [Игнорирование ошибок веб-запросов в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/web-request-errors-custom "Прекратите считать определённые HTTP-коды ответов ошибками в пользовательских приложениях.")
* [Создание пользовательских имён действий в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/naming-rules-custom "Настройте автоматически генерируемые имена действий пользователей в ваших пользовательских приложениях.")
* [Настройка ключевых действий пользователей в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-key-user-actions-custom "Обозначьте действие пользователя как ключевое и настройте рейтинг Apdex для ключевых действий в пользовательских приложениях.")
* [Настройка параметров Apdex для пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-apdex-custom "Настройте пороги производительности удовлетворённости пользователей для вашего пользовательского приложения и его ключевых действий.")
* [Изменение порогов оценки пользовательского опыта в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-user-experience-score-custom "Скорректируйте пороги оценки пользовательского опыта под требования вашего пользовательского приложения.")
* [Создание вычисляемых метрик для пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Создавайте вычисляемые метрики и пользовательские диаграммы на их основе для ваших пользовательских приложений.")
* [Создание пользовательских USQL-метрик для пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/custom-metrics-from-user-sessions-custom-apps "При каждом закрытии сессии пользователя Dynatrace может извлекать метрики и сохранять их как временные ряды. Узнайте, как настраивать и использовать пользовательские USQL-метрики для пользовательских приложений.")
* [Определение свойств действий и сессий пользователей в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/define-custom-action-and-session-properties "Отправляйте метаданные в Dynatrace и определяйте свойства действий и сессий для ваших пользовательских приложений.")
* [Настройка определения IP-адресов в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/customize-ip-address-detectio-custom "Измените способ определения Dynatrace IP-адресов клиентов в пользовательских приложениях.")
* [Сопоставление внутренних IP-адресов с местоположениями в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Настройте Dynatrace на использование локальных адресов для определения местонахождения пользователей ваших пользовательских приложений.")
* [Настройка обнаружения сторонних ресурсов, ресурсов первой стороны и CDN в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-third-party-and-cdn-content-detection-custom "Вручную определите сторонних провайдеров и CDN вместе с автоматически обнаруженными провайдерами для ваших пользовательских приложений.")
* [Использование OneAgent в качестве конечной точки beacon для пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/oneagent-as-beacon-forwarder-custom "Используйте Dynatrace OneAgent в качестве конечной точки beacon для пользовательских приложений.")
* [Удаление пользовательского приложения](/managed/observe/digital-experience/custom-applications/additional-configuration/delete-application-custom "Удаляйте пользовательские приложения через веб-интерфейс Dynatrace или API.")