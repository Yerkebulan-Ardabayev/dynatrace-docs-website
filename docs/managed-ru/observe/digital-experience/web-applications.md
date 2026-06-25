---
title: Веб-приложения
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications
scraped: 2026-05-12T11:07:27.005486
---

# Веб-приложения

# Веб-приложения

* Overview
* 1-min read
* Updated on Apr 03, 2024

Все HTML-страницы — статические веб-сайты или одностраничные приложения (SPA), работающие в браузере, — считаются веб-приложениями.

Поддержка Internet Explorer 11 прекращена начиная с RUM JavaScript версии 1.293. Подробнее см. раздел [RUM JavaScript для Internet Explorer](/managed/observe/digital-experience/web-applications/additional-configuration/rum-javascript-version#rum-javascript-for-ie "Control the RUM JavaScript version used to monitor your applications").

### Начальная настройка

* [Определение приложений для мониторинга Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.")
* [Настройка автоматической инъекции](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications")
* [Настройка безагентного мониторинга Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.")
* [Выбор формата сниппета](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case")
* [Настройка Real User Monitoring для захвата XHR-действий](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.")
* [Страницы и группы страниц](/managed/observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups "Learn how to use and define pages and page groups in Dynatrace Real User Monitoring.")
* [Создание пользовательских имён для действий пользователей в веб-приложениях](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.")
* [Ограничения фаервола для RUM](/managed/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum "Find out how to make sure that Real User Monitoring data passes through your firewall.")
* [Связывание межисточниковых XHR-действий с распределёнными трассировками](/managed/observe/digital-experience/web-applications/initial-setup/link-cross-origin-xhrs "Enable the correlation between cross-origin XHR actions and distributed traces.")
* [Использование Subresource Integrity (SRI) для кода Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring code.")
* [Проверка состояния приложения](/managed/observe/digital-experience/web-applications/initial-setup/app-health-check "The Application health check page allows you to analyze the health of your application, see which RUM JavaScript versions are currently in use, or confirm that the RUM JavaScript is injected correctly.")
* [Поэтапное развёртывание RUM для приложений](/managed/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

### Дополнительная конфигурация

* [Управление версией RUM JavaScript](/managed/observe/digital-experience/web-applications/additional-configuration/rum-javascript-version "Control the RUM JavaScript version used to monitor your applications")
* [Настройка управления стоимостью и трафиком для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-cost-and-traffic-control-web "Leverage the cost and traffic control setting in Dynatrace to reduce session usage for web applications.")
* [Настройка параметров конфиденциальности данных для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.")
* [Настройка ключевых пользовательских действий для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-key-user-actions-web "Mark a user action as a key user action and configure Apdex rating for key user actions of your web applications.")
* [Захват дополнительных типов взаимодействий для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/capture-interaction-types "Choose which interaction types RUM should detect for your web applications.")
* [Настройка параметров Apdex для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-apdex-web "Configure the user-satisfaction performance thresholds for your web application and its key user actions.")
* [Изменение пороговых значений оценки пользовательского опыта для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-user-experience-score-web "Adjust the user experience score thresholds to meet the specific requirements of your web application.")
* [Создание вычисляемых метрик для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.")
* [Создание пользовательских метрик USQL для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/custom-metrics-from-user-sessions "Every time a user session is closed, Dynatrace can extract metrics and store them as time series. Learn how to set up and use USQL custom metrics for web applications.")
* [Определение свойств пользовательских действий и сессий для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.")
* [Настройка Real User Monitoring с помощью JavaScript API для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.")
* [Настройка обнаружения ошибок для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-errors "Configure your application to capture or ignore request, custom, and JavaScript errors.")
* [Тегирование отдельных пользователей для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Tag individual users via the JavaScript API for session analysis.")
* [Настройка определения IP-адресов для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/customize-ip-address-detection-web "Change the way Dynatrace determines client IP addresses for your web applications.")
* [Сопоставление внутренних IP-адресов с расположениями для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Configure Dynatrace to use local addresses to understand where the users of your web applications are.")
* [Настройка обнаружения ресурсов первой, сторонних сторон и CDN для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Manually define third-party and CDN providers along with auto-detected providers for your web applications.")
* [Настройка атрибутов RUM cookie](/managed/observe/digital-experience/web-applications/additional-configuration/configure-cookie-attributes "Learn which RUM cookie attributes you can configure and how.")
* [Настройка allowlist источников маяков для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.")
* [Настройка конечной точки маяка для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.")
* [Настройка источника кода Real User Monitoring](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source "Configure the Real User Monitoring code source for your specific requirements.")
* [Исключение IP-адресов, браузеров, ботов и поисковых роботов из мониторинга для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring "Disable Real User Monitoring for certain IP addresses, browsers, bots, and spiders.")
* [Настройка серверов кэширования](/managed/observe/digital-experience/web-applications/additional-configuration/configure-your-caching-servers "Learn how to configure your caching server correctly to avoid cache-related problems.")
* [Проверка правил обнаружения приложений](/managed/observe/digital-experience/web-applications/additional-configuration/application-detection-rules "Easily understand the detection rules of your RUM application.")
* [Настройка XHR для устаревших версий Internet Explorer](/managed/observe/digital-experience/web-applications/additional-configuration/configure-xhr-for-older-versions-of-ie "Learn how to make Dynatrace JavaScript work with outdated versions of Internet Explorer.")
* [Real User Monitoring для групп процессов](/managed/observe/digital-experience/web-applications/additional-configuration/rum-for-process-groups "Learn how to configure Real User Monitoring for process groups.")
* [Изменение Content Security Policy для RUM](/managed/observe/digital-experience/web-applications/additional-configuration/modify-csp-for-rum "Learn how to enable and modify CSP for your RUM-monitored applications.")
* [Удаление веб-приложения](/managed/observe/digital-experience/web-applications/additional-configuration/delete-application-web "Delete your web applications via the Dynatrace web UI or API.")

### Анализ и использование данных RUM

* [Обзор страницы анализа приложений](/managed/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview "Read an overview of the analysis options offered on the application overview page.")
* [Анализ производительности](/managed/observe/digital-experience/web-applications/analyze-and-use/performance-analysis "Understand the available types of performance analysis that are provided by Dynatrace.")
* [Анализ поведения пользователей](/managed/observe/digital-experience/web-applications/analyze-and-use/user-behavior-analysis "Understand the user behavior analysis options that are provided by Dynatrace.")
* [Многомерный анализ для веб-приложений](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.")
* [Waterfall-анализ](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.")
* [Вид на карте мира](/managed/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors.")
* [Работа с ключевыми метриками производительности](/managed/observe/digital-experience/web-applications/analyze-and-use/work-with-key-performance-metrics "Learn how to use the right key performance metrics to optimize user experience data for each of your applications.")
* [Анализ отдельных пользовательских действий](/managed/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions "Understand how you can access user action detail pages and analyze user actions.")
* [Использование свойств пользовательских действий и сессий для веб-приложений](/managed/observe/digital-experience/web-applications/analyze-and-use/action-and-session-properties "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your web applications, you can filter user sessions, add calculated metrics, create charts, and more.")
* [Определение целей конверсии](/managed/observe/digital-experience/web-applications/analyze-and-use/define-conversion-goals "Learn how to analyze conversion goals for specific user actions to understand how successfully you're meeting your conversion milestones.")
* [Использование метрик «Visually complete» и «Speed index»](/managed/observe/digital-experience/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics "Learn how to use 'Visually complete' and 'Speed index' metrics.")
* [Главные выводы по «Visually complete»](/managed/observe/digital-experience/web-applications/analyze-and-use/visually-complete-top-findings "Lean how to leverage Visually complete top findings provided in the waterfall analysis.")
* [Анализ приложений с помощью Hyperlyzer](/managed/observe/digital-experience/web-applications/analyze-and-use/application-analysis-with-hyperlyzer "Dynatrace Hyperlyzer helps you visually query different application dimensions, for example, geolocation, browser, operating system, bandwidth, and user actions.")
* [Потоки сервисов для приложений и пользовательских действий](/managed/observe/digital-experience/web-applications/analyze-and-use/service-flows-for-applications-and-user-actions "Learn how to access service flows for applications and user actions.")
* [Поддержка source map для анализа ошибок JavaScript](/managed/observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Learn how source maps make it easy to analyze, reproduce, and fix JavaScript errors.")

### Устранение неполадок

[Устранение неполадок RUM для веб-приложений](/managed/observe/digital-experience/web-applications/troubleshooting "Learn how to troubleshoot issues when you use Real User Monitoring for your web applications.")