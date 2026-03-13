---
title: Web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications
scraped: 2026-03-06T21:14:09.923490
---

# Веб-приложения

# Веб-приложения

* Classic
* Обзор
* Чтение: 1 мин
* Обновлено 03 апр. 2024

Все HTML-страницы -- такие как статические веб-страницы или одностраничные приложения, работающие в браузере -- рассматриваются как веб-приложения.

Поддержка Internet Explorer 11 прекращена начиная с RUM JavaScript версии 1.293. Подробнее см. [RUM JavaScript для Internet Explorer](web-applications/additional-configuration/rum-javascript-version.md#rum-javascript-for-ie "Управление версией RUM JavaScript, используемой для мониторинга ваших приложений").

### Начальная настройка

* [Определение приложений для мониторинга реальных пользователей](web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder.md "Узнайте, как определить приложения, используя рекомендуемый, ручной подход или правила обнаружения приложений.")
* [Настройка автоматического внедрения](web-applications/initial-setup/rum-injection.md "Настройка автоматического внедрения RUM JavaScript в страницы ваших приложений")
* [Настройка безагентного мониторинга реальных пользователей](web-applications/initial-setup/set-up-agentless-real-user-monitoring.md "Настройка безагентного мониторинга для ваших веб-приложений.")
* [Выбор формата сниппета](web-applications/initial-setup/snippet-formats.md "Выберите формат сниппета RUM JavaScript, наиболее подходящий для вашего случая использования")
* [Настройка мониторинга реальных пользователей для захвата XHR-действий](web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions.md "Узнайте, почему необходимо активировать определённые JavaScript-фреймворки для поддержки XHR-действий, и как настроить мониторинг реальных пользователей для XHR-действий.")
* [Страницы и группы страниц](web-applications/initial-setup/pages-and-pagegroups.md "Узнайте, как использовать и определять страницы и группы страниц в Dynatrace Real User Monitoring.")
* [Создание пользовательских имён действий для веб-приложений](web-applications/initial-setup/create-custom-names-for-user-actions.md "Настройка автоматически генерируемых имён пользовательских действий для ваших веб-приложений.")
* [Ограничения файрвола для RUM](web-applications/initial-setup/firewall-constraints-for-rum.md "Узнайте, как обеспечить прохождение данных мониторинга реальных пользователей через файрвол.")
* [Связывание кросс-доменных XHR-действий и их распределённых трассировок](web-applications/initial-setup/link-cross-origin-xhrs.md "Включите корреляцию между кросс-доменными XHR-действиями и распределёнными трассировками.")
* [Использование Subresource Integrity (SRI) для кода мониторинга реальных пользователей](web-applications/initial-setup/subresource-integrity.md "Использование браузерной функции Subresource Integrity (SRI) для обеспечения целостности кода мониторинга реальных пользователей.")
* [Проверка состояния приложения](web-applications/initial-setup/app-health-check.md "Страница проверки состояния приложения позволяет анализировать состояние приложения, видеть используемые версии RUM JavaScript или подтверждать корректность внедрения RUM JavaScript.")
* [Выборочное развёртывание RUM для приложений](web-applications/initial-setup/selective-rum-rollout.md "Выборочное развёртывание RUM после установки OneAgent в режиме полного мониторинга на хостах")

### Дополнительная настройка

* [Управление версией RUM JavaScript](web-applications/additional-configuration/rum-javascript-version.md "Управление версией RUM JavaScript, используемой для мониторинга ваших приложений")
* [Настройка контроля затрат и трафика для веб-приложений](web-applications/additional-configuration/configure-cost-and-traffic-control-web.md "Используйте настройку контроля затрат и трафика в Dynatrace для снижения использования сеансов веб-приложений.")
* [Настройка конфиденциальности данных для веб-приложений](web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr.md "Узнайте о настройках конфиденциальности, которые Dynatrace предоставляет для обеспечения соответствия ваших веб-приложений требованиям защиты данных вашего региона.")
* [Настройка ключевых пользовательских действий для веб-приложений](web-applications/additional-configuration/configure-key-user-actions-web.md "Пометьте действие пользователя как ключевое и настройте рейтинг Apdex для ключевых действий пользователей ваших веб-приложений.")
* [Захват дополнительных типов взаимодействий для веб-приложений](web-applications/additional-configuration/capture-interaction-types.md "Выберите, какие типы взаимодействий RUM должен обнаруживать для ваших веб-приложений.")
* [Настройка параметров Apdex для веб-приложений](web-applications/additional-configuration/configure-apdex-web.md "Настройка пороговых значений удовлетворённости пользователей для вашего веб-приложения и его ключевых действий.")
* [Изменение пороговых значений оценки пользовательского опыта для веб-приложений](web-applications/additional-configuration/configure-user-experience-score-web.md "Настройте пороговые значения оценки пользовательского опыта в соответствии с конкретными требованиями вашего веб-приложения.")
* [Создание вычисляемых метрик для веб-приложений](web-applications/additional-configuration/rum-calculated-metrics-web.md "Создание вычисляемых метрик и пользовательских диаграмм на основе вычисляемых метрик для ваших веб-приложений.")
* [Создание пользовательских метрик USQL для веб-приложений](web-applications/additional-configuration/custom-metrics-from-user-sessions.md "Каждый раз при закрытии пользовательского сеанса Dynatrace может извлекать метрики и сохранять их как временные ряды. Узнайте, как настроить и использовать пользовательские метрики USQL для веб-приложений.")
* [Определение свойств действий пользователя и сеансов для веб-приложений](web-applications/additional-configuration/define-user-action-and-session-properties.md "Определение пользовательских строковых, числовых и свойств даты для ваших мониторируемых веб-приложений.")
* [Настройка мониторинга реальных пользователей с помощью JavaScript API для веб-приложений](web-applications/additional-configuration/customize-rum.md "Узнайте, как настроить мониторинг реальных пользователей с помощью JavaScript API.")
* [Настройка обнаружения ошибок для веб-приложений](web-applications/additional-configuration/configure-errors.md "Настройте приложение для захвата или игнорирования ошибок запросов, пользовательских ошибок и ошибок JavaScript.")
* [Пометка конкретных пользователей для веб-приложений](web-applications/additional-configuration/identify-individual-users-for-session-analysis.md "Пометьте отдельных пользователей через JavaScript API для анализа сеансов.")
* [Настройка определения IP-адресов для веб-приложений](web-applications/additional-configuration/customize-ip-address-detection-web.md "Измените способ определения клиентских IP-адресов Dynatrace для ваших веб-приложений.")
* [Сопоставление внутренних IP-адресов с местоположениями для веб-приложений](web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web.md "Настройте Dynatrace для использования локальных адресов, чтобы понимать, где находятся пользователи ваших веб-приложений.")
* [Настройка обнаружения собственных, сторонних и CDN-ресурсов для веб-приложений](web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web.md "Ручное определение сторонних и CDN-провайдеров наряду с автоматически обнаруженными провайдерами для ваших веб-приложений.")
* [Настройка домена cookie RUM для веб-приложений](web-applications/additional-configuration/configure-the-cookie-domain.md "Узнайте, когда и как настраивать домен cookie.")
* [Настройка списка разрешённых источников бикон для веб-приложений](web-applications/additional-configuration/configure-beacon-domain-allowlist.md "Укажите источники, с которых должны приниматься кросс-доменные RUM-биконы.")
* [Настройка эндпоинта бикон для веб-приложений](web-applications/additional-configuration/beacon-endpoint.md "Измените URL-адрес эндпоинта бикон по умолчанию и отправляйте RUM-биконы в инфраструктуру Dynatrace или другой инструментированный веб-сервер.")
* [Настройка источника кода мониторинга реальных пользователей](web-applications/additional-configuration/configure-monitoring-code-source.md "Настройте источник кода мониторинга реальных пользователей для ваших конкретных требований.")
* [Исключение IP-адресов, браузеров, ботов и пауков из мониторинга для веб-приложений](web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring.md "Отключение мониторинга реальных пользователей для определённых IP-адресов, браузеров, ботов и пауков.")
* [Настройка кэширующих серверов](web-applications/additional-configuration/configure-your-caching-servers.md "Узнайте, как правильно настроить кэширующий сервер, чтобы избежать проблем, связанных с кэшированием.")
* [Проверка правил обнаружения приложений](web-applications/additional-configuration/application-detection-rules.md "Простое понимание правил обнаружения вашего RUM-приложения.")
* [Настройка XHR для устаревших версий Internet Explorer](web-applications/additional-configuration/configure-xhr-for-older-versions-of-ie.md "Узнайте, как заставить Dynatrace JavaScript работать с устаревшими версиями Internet Explorer.")
* [Мониторинг реальных пользователей для групп процессов](web-applications/additional-configuration/rum-for-process-groups.md "Узнайте, как настроить мониторинг реальных пользователей для групп процессов.")
* [Изменение Content Security Policy для RUM](web-applications/additional-configuration/modify-csp-for-rum.md "Узнайте, как включить и изменить CSP для ваших RUM-мониторируемых приложений.")
* [Удаление веб-приложения](web-applications/additional-configuration/delete-application-web.md "Удаление веб-приложений через веб-интерфейс Dynatrace или API.")

### Анализ и использование данных RUM

* [Введение на страницу обзора приложения](web-applications/analyze-and-use/introduction-to-application-overview.md "Обзор возможностей анализа, предлагаемых на странице обзора приложения.")
* [Анализ производительности](web-applications/analyze-and-use/performance-analysis.md "Описание доступных типов анализа производительности, предоставляемых Dynatrace.")
* [Анализ поведения пользователей](web-applications/analyze-and-use/user-behavior-analysis.md "Описание возможностей анализа поведения пользователей, предоставляемых Dynatrace.")
* [Многомерный анализ для веб-приложений](web-applications/analyze-and-use/multi-dimensional-analysis.md "Узнайте, как Dynatrace Real User Monitoring позволяет глубоко анализировать действия пользователей по множеству измерений.")
* [Водопадный анализ](web-applications/analyze-and-use/waterfall-analysis.md "Узнайте, как анализировать все данные мониторинга действий пользователей с помощью водопадного анализа.")
* [Вид карты мира](web-applications/analyze-and-use/world-map-view.md "Узнайте, как вид карты мира предоставляет информацию о рейтингах Apdex, действиях пользователей, длительности действий и ошибках JavaScript.")
* [Работа с ключевыми показателями производительности](web-applications/analyze-and-use/work-with-key-performance-metrics.md "Узнайте, как использовать правильные ключевые показатели производительности для оптимизации данных об опыте пользователей для каждого из ваших приложений.")
* [Анализ отдельных действий пользователей](web-applications/analyze-and-use/analyze-individual-user-actions.md "Описание доступа к страницам деталей действий пользователей и их анализа.")
* [Использование свойств действий пользователя и сеансов для веб-приложений](web-applications/analyze-and-use/action-and-session-properties.md "Свойства действий пользователя и сеансов -- это пары ключ-значение метаданных, которые обеспечивают дополнительную видимость и более глубокий анализ опыта конечных пользователей. Используя эти свойства для веб-приложений, вы можете фильтровать пользовательские сеансы, добавлять вычисляемые метрики, создавать диаграммы и многое другое.")
* [Определение целей конверсии](web-applications/analyze-and-use/define-conversion-goals.md "Узнайте, как анализировать цели конверсии для конкретных действий пользователей, чтобы понять, насколько успешно вы достигаете контрольных точек конверсии.")
* [Использование метрик 'Visually complete' и 'Speed index'](web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics.md "Узнайте, как использовать метрики 'Visually complete' и 'Speed index'.")
* [Основные выводы Visually complete](web-applications/analyze-and-use/visually-complete-top-findings.md "Узнайте, как использовать основные выводы Visually complete, представленные в водопадном анализе.")
* [Анализ приложений с помощью Hyperlyzer](web-applications/analyze-and-use/application-analysis-with-hyperlyzer.md "Dynatrace Hyperlyzer помогает визуально запрашивать различные измерения приложения, например геолокацию, браузер, операционную систему, пропускную способность и действия пользователей.")
* [Потоки сервисов для приложений и действий пользователей](web-applications/analyze-and-use/service-flows-for-applications-and-user-actions.md "Узнайте, как получить доступ к потокам сервисов для приложений и действий пользователей.")
* [Поддержка карт кода для анализа ошибок JavaScript](web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis.md "Узнайте, как карты кода упрощают анализ, воспроизведение и исправление ошибок JavaScript.")

### Устранение неполадок

[Устранение неполадок RUM для веб-приложений](web-applications/troubleshooting.md "Узнайте, как устранять неполадки при использовании мониторинга реальных пользователей для веб-приложений.")
