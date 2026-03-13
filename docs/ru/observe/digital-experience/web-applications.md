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

Поддержка Internet Explorer 11 прекращена начиная с RUM JavaScript версии 1.293. Подробнее см. [RUM JavaScript для Internet Explorer](/docs/observe/digital-experience/web-applications/additional-configuration/rum-javascript-version#rum-javascript-for-ie "Управление версией RUM JavaScript, используемой для мониторинга ваших приложений").

### Начальная настройка

* [Определение приложений для мониторинга реальных пользователей](/docs/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Узнайте, как определить приложения, используя рекомендуемый, ручной подход или правила обнаружения приложений.")
* [Настройка автоматического внедрения](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection "Настройка автоматического внедрения RUM JavaScript в страницы ваших приложений")
* [Настройка безагентного мониторинга реальных пользователей](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Настройка безагентного мониторинга для ваших веб-приложений.")
* [Выбор формата сниппета](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats "Выберите формат сниппета RUM JavaScript, наиболее подходящий для вашего случая использования")
* [Настройка мониторинга реальных пользователей для захвата XHR-действий](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Узнайте, почему необходимо активировать определённые JavaScript-фреймворки для поддержки XHR-действий, и как настроить мониторинг реальных пользователей для XHR-действий.")
* [Страницы и группы страниц](/docs/observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups "Узнайте, как использовать и определять страницы и группы страниц в Dynatrace Real User Monitoring.")
* [Создание пользовательских имён действий для веб-приложений](/docs/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Настройка автоматически генерируемых имён пользовательских действий для ваших веб-приложений.")
* [Ограничения файрвола для RUM](/docs/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum "Узнайте, как обеспечить прохождение данных мониторинга реальных пользователей через файрвол.")
* [Связывание кросс-доменных XHR-действий и их распределённых трассировок](/docs/observe/digital-experience/web-applications/initial-setup/link-cross-origin-xhrs "Включите корреляцию между кросс-доменными XHR-действиями и распределёнными трассировками.")
* [Использование Subresource Integrity (SRI) для кода мониторинга реальных пользователей](/docs/observe/digital-experience/web-applications/initial-setup/subresource-integrity "Использование браузерной функции Subresource Integrity (SRI) для обеспечения целостности кода мониторинга реальных пользователей.")
* [Проверка состояния приложения](/docs/observe/digital-experience/web-applications/initial-setup/app-health-check "Страница проверки состояния приложения позволяет анализировать состояние приложения, видеть используемые версии RUM JavaScript или подтверждать корректность внедрения RUM JavaScript.")
* [Выборочное развёртывание RUM для приложений](/docs/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout "Выборочное развёртывание RUM после установки OneAgent в режиме полного мониторинга на хостах")

### Дополнительная настройка

* [Управление версией RUM JavaScript](/docs/observe/digital-experience/web-applications/additional-configuration/rum-javascript-version "Управление версией RUM JavaScript, используемой для мониторинга ваших приложений")
* [Настройка контроля затрат и трафика для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/configure-cost-and-traffic-control-web "Используйте настройку контроля затрат и трафика в Dynatrace для снижения использования сеансов веб-приложений.")
* [Настройка конфиденциальности данных для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr "Узнайте о настройках конфиденциальности, которые Dynatrace предоставляет для обеспечения соответствия ваших веб-приложений требованиям защиты данных вашего региона.")
* [Настройка ключевых пользовательских действий для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/configure-key-user-actions-web "Пометьте действие пользователя как ключевое и настройте рейтинг Apdex для ключевых действий пользователей ваших веб-приложений.")
* [Захват дополнительных типов взаимодействий для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/capture-interaction-types "Выберите, какие типы взаимодействий RUM должен обнаруживать для ваших веб-приложений.")
* [Настройка параметров Apdex для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/configure-apdex-web "Настройка пороговых значений удовлетворённости пользователей для вашего веб-приложения и его ключевых действий.")
* [Изменение пороговых значений оценки пользовательского опыта для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/configure-user-experience-score-web "Настройте пороговые значения оценки пользовательского опыта в соответствии с конкретными требованиями вашего веб-приложения.")
* [Создание вычисляемых метрик для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Создание вычисляемых метрик и пользовательских диаграмм на основе вычисляемых метрик для ваших веб-приложений.")
* [Создание пользовательских метрик USQL для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/custom-metrics-from-user-sessions "Каждый раз при закрытии пользовательского сеанса Dynatrace может извлекать метрики и сохранять их как временные ряды. Узнайте, как настроить и использовать пользовательские метрики USQL для веб-приложений.")
* [Определение свойств действий пользователя и сеансов для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Определение пользовательских строковых, числовых и свойств даты для ваших мониторируемых веб-приложений.")
* [Настройка мониторинга реальных пользователей с помощью JavaScript API для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/customize-rum "Узнайте, как настроить мониторинг реальных пользователей с помощью JavaScript API.")
* [Настройка обнаружения ошибок для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/configure-errors "Настройте приложение для захвата или игнорирования ошибок запросов, пользовательских ошибок и ошибок JavaScript.")
* [Пометка конкретных пользователей для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Пометьте отдельных пользователей через JavaScript API для анализа сеансов.")
* [Настройка определения IP-адресов для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/customize-ip-address-detection-web "Измените способ определения клиентских IP-адресов Dynatrace для ваших веб-приложений.")
* [Сопоставление внутренних IP-адресов с местоположениями для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Настройте Dynatrace для использования локальных адресов, чтобы понимать, где находятся пользователи ваших веб-приложений.")
* [Настройка обнаружения собственных, сторонних и CDN-ресурсов для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Ручное определение сторонних и CDN-провайдеров наряду с автоматически обнаруженными провайдерами для ваших веб-приложений.")
* [Настройка домена cookie RUM для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/configure-the-cookie-domain "Узнайте, когда и как настраивать домен cookie.")
* [Настройка списка разрешённых источников бикон для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Укажите источники, с которых должны приниматься кросс-доменные RUM-биконы.")
* [Настройка эндпоинта бикон для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Измените URL-адрес эндпоинта бикон по умолчанию и отправляйте RUM-биконы в инфраструктуру Dynatrace или другой инструментированный веб-сервер.")
* [Настройка источника кода мониторинга реальных пользователей](/docs/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source "Настройте источник кода мониторинга реальных пользователей для ваших конкретных требований.")
* [Исключение IP-адресов, браузеров, ботов и пауков из мониторинга для веб-приложений](/docs/observe/digital-experience/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring "Отключение мониторинга реальных пользователей для определённых IP-адресов, браузеров, ботов и пауков.")
* [Настройка кэширующих серверов](/docs/observe/digital-experience/web-applications/additional-configuration/configure-your-caching-servers "Узнайте, как правильно настроить кэширующий сервер, чтобы избежать проблем, связанных с кэшированием.")
* [Проверка правил обнаружения приложений](/docs/observe/digital-experience/web-applications/additional-configuration/application-detection-rules "Простое понимание правил обнаружения вашего RUM-приложения.")
* [Настройка XHR для устаревших версий Internet Explorer](/docs/observe/digital-experience/web-applications/additional-configuration/configure-xhr-for-older-versions-of-ie "Узнайте, как заставить Dynatrace JavaScript работать с устаревшими версиями Internet Explorer.")
* [Мониторинг реальных пользователей для групп процессов](/docs/observe/digital-experience/web-applications/additional-configuration/rum-for-process-groups "Узнайте, как настроить мониторинг реальных пользователей для групп процессов.")
* [Изменение Content Security Policy для RUM](/docs/observe/digital-experience/web-applications/additional-configuration/modify-csp-for-rum "Узнайте, как включить и изменить CSP для ваших RUM-мониторируемых приложений.")
* [Удаление веб-приложения](/docs/observe/digital-experience/web-applications/additional-configuration/delete-application-web "Удаление веб-приложений через веб-интерфейс Dynatrace или API.")

### Анализ и использование данных RUM

* [Введение на страницу обзора приложения](/docs/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview "Обзор возможностей анализа, предлагаемых на странице обзора приложения.")
* [Анализ производительности](/docs/observe/digital-experience/web-applications/analyze-and-use/performance-analysis "Описание доступных типов анализа производительности, предоставляемых Dynatrace.")
* [Анализ поведения пользователей](/docs/observe/digital-experience/web-applications/analyze-and-use/user-behavior-analysis "Описание возможностей анализа поведения пользователей, предоставляемых Dynatrace.")
* [Многомерный анализ для веб-приложений](/docs/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Узнайте, как Dynatrace Real User Monitoring позволяет глубоко анализировать действия пользователей по множеству измерений.")
* [Водопадный анализ](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Узнайте, как анализировать все данные мониторинга действий пользователей с помощью водопадного анализа.")
* [Вид карты мира](/docs/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Узнайте, как вид карты мира предоставляет информацию о рейтингах Apdex, действиях пользователей, длительности действий и ошибках JavaScript.")
* [Работа с ключевыми показателями производительности](/docs/observe/digital-experience/web-applications/analyze-and-use/work-with-key-performance-metrics "Узнайте, как использовать правильные ключевые показатели производительности для оптимизации данных об опыте пользователей для каждого из ваших приложений.")
* [Анализ отдельных действий пользователей](/docs/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions "Описание доступа к страницам деталей действий пользователей и их анализа.")
* [Использование свойств действий пользователя и сеансов для веб-приложений](/docs/observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties "Свойства действий пользователя и сеансов -- это пары ключ-значение метаданных, которые обеспечивают дополнительную видимость и более глубокий анализ опыта конечных пользователей. Используя эти свойства для веб-приложений, вы можете фильтровать пользовательские сеансы, добавлять вычисляемые метрики, создавать диаграммы и многое другое.")
* [Определение целей конверсии](/docs/observe/digital-experience/web-applications/analyze-and-use/define-conversion-goals "Узнайте, как анализировать цели конверсии для конкретных действий пользователей, чтобы понять, насколько успешно вы достигаете контрольных точек конверсии.")
* [Использование метрик 'Visually complete' и 'Speed index'](/docs/observe/digital-experience/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics "Узнайте, как использовать метрики 'Visually complete' и 'Speed index'.")
* [Основные выводы Visually complete](/docs/observe/digital-experience/web-applications/analyze-and-use/visually-complete-top-findings "Узнайте, как использовать основные выводы Visually complete, представленные в водопадном анализе.")
* [Анализ приложений с помощью Hyperlyzer](/docs/observe/digital-experience/web-applications/analyze-and-use/application-analysis-with-hyperlyzer "Dynatrace Hyperlyzer помогает визуально запрашивать различные измерения приложения, например геолокацию, браузер, операционную систему, пропускную способность и действия пользователей.")
* [Потоки сервисов для приложений и действий пользователей](/docs/observe/digital-experience/web-applications/analyze-and-use/service-flows-for-applications-and-user-actions "Узнайте, как получить доступ к потокам сервисов для приложений и действий пользователей.")
* [Поддержка карт кода для анализа ошибок JavaScript](/docs/observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Узнайте, как карты кода упрощают анализ, воспроизведение и исправление ошибок JavaScript.")

### Устранение неполадок

[Устранение неполадок RUM для веб-приложений](/docs/observe/digital-experience/web-applications/troubleshooting "Узнайте, как устранять неполадки при использовании мониторинга реальных пользователей для веб-приложений.")
