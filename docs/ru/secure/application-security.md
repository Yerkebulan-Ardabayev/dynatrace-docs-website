---
title: Безопасность приложений
source: https://www.dynatrace.com/docs/secure/application-security
scraped: 2026-03-06T21:10:31.053864
---

Что вы найдёте на этой странице

* [Обзор возможностей Application Security](#start)
* [Как режимы мониторинга влияют на данные и анализ](#monitoring-modes)
* [Углубите понимание: видео, руководства, блоги](#resources)

Dynatrace Application Security обеспечивает защиту в реальном времени и глубокую видимость вашего приложения. Объединяя автоматическое обнаружение уязвимостей, защиту приложений во время выполнения и управление состоянием безопасности, она позволяет командам защищать современные облачные среды с точностью и в масштабе. Ознакомьтесь с обзорами функций, шагами настройки, режимами работы и рекомендациями по использованию.

## Начало работы

Dynatrace предоставляет следующие интегрированные возможности Application Security для защиты ваших приложений. Выберите любую, чтобы начать.

Если вы используете классическое лицензирование Dynatrace, обратитесь к эксперту Dynatrace через онлайн-чат, чтобы **активировать Application Security** перед началом работы.

* **Dynatrace Runtime Vulnerability Analytics (RVA)**: Мгновенно выявляйте критические уязвимости с помощью автоматической оценки рисков и воздействия благодаря глубокому анализу путей доступа к данным и производственному выполнению.
* **Dynatrace Runtime Application Protection (RAP)**: Защищайте приложения в реальном времени, обнаруживая и блокируя атаки с помощью передовых анализа на уровне кода и анализа транзакций.
* **Dynatrace Security Posture Management (SPM)**: Поддерживайте надёжный уровень безопасности путём эффективной оценки, приоритизации и устранения неправильных конфигураций и нарушений соответствия требованиям.

## Охват режимами мониторинга

Эффективность и глубина анализа Application Security зависят от развёрнутого режима мониторинга. В этом разделе описывается, как каждый режим влияет на сбор и анализ данных.

**Dynatrace Security Posture Management (SPM)** работает независимо от режимов мониторинга. Подробнее см. в разделе [FAQ](application-security/spm.md#monitoring "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

### Обзор поддержки

| Возможность | Full-Stack | Инфраструктура | Обнаружение |
| --- | --- | --- | --- |
| [Обнаружение уязвимостей в сторонних компонентах](application-security/vulnerability-analytics.md#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") | Зелёный фон с галочкой | [ограниченно](#tpv-infra) | [ограниченно](#clv-infra) |
| [Обнаружение уязвимостей на уровне кода](application-security/vulnerability-analytics.md#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") | Зелёный фон с галочкой | [ограниченно](#tpv-disco) | [ограниченно](#clv-disco) |
| Runtime Application Protection | Зелёный фон с галочкой | Зелёный фон с галочкой | Зелёный фон с галочкой |

Доступность в публичном интернете

На хостах Linux при отсутствии информации — что может происходить в различных режимах мониторинга или при возникновении ошибок — доступность в публичном интернете определяется через eBPF. Возможные состояния: `Public network` (Публичная сеть) и `Not detected` (Не обнаружено). Dynatrace Security Score не зависит ни от одного из этих состояний.

### Режим мониторинга Full-Stack

Рекомендуется

Режим мониторинга Full-Stack обеспечивает полный мониторинг производительности приложений, видимость на уровне кода, глубокий мониторинг процессов и мониторинг инфраструктуры (включая платформы PaaS).

### Режим мониторинга инфраструктуры

[Режим мониторинга инфраструктуры](../platform/oneagent/monitoring-modes/monitoring-modes.md#infrastructure-only "Find out more about the available monitoring modes when using OneAgent."), при котором OneAgent настроен на мониторинг физической и виртуальной инфраструктуры, обеспечивает менее полный мониторинг по сравнению с режимом Full-Stack. Предоставляются следующие функциональные возможности:

* Системные метрики (использование CPU, памяти, дискового пространства)
* [Обнаружение уязвимостей в сторонних компонентах](application-security/vulnerability-analytics.md#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* [Обнаружение уязвимостей на уровне кода](application-security/vulnerability-analytics.md#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* Runtime Application Protection

#### Характеристики

Уязвимости в сторонних компонентах

Уязвимости на уровне кода

Атаки

Уязвимости в сторонних компонентах

Уязвимости на уровне кода

Атаки

* В развёртывании с режимом мониторинга инфраструктуры Dynatrace Intelligence не может [адаптировать Dynatrace Security Score](vulnerabilities/concepts.md#dss-calculation "Concepts that are specific to the Dynatrace Vulnerabilities app."). В этом случае значение риска уязвимости не может быть пересмотрено, так как это возможно только на основе информации о топологии, извлечённой из вашей среды, и DSS будет равен базовому показателю CVSS.
* Режим мониторинга инфраструктуры не содержит информации об окружающей среде, такой как доступные ресурсы данных или доступность в публичном интернете, и ограничивает информацию о связанных объектах, например, базах данных и сервисах. Полная оценка возможна только для уязвимостей, у которых все связанные хосты находятся в режиме Full-Stack Monitoring.

  + Если связанные хосты работают в режиме мониторинга инфраструктуры, OneAgent'ы передают недостаточно данных для анализа наличия уязвимости или затронутых конфиденциальных данных, поэтому для **доступности в публичном интернете** и **достижимых ресурсов данных** устанавливается значение `Not available` (Недоступно).
  + Если все связанные хосты работают в режиме Full-Stack Monitoring, кроме одного в режиме мониторинга инфраструктуры, и уязвимость не раскрыта и не затронута (исходя из хостов в режиме Full-Stack), значения для **доступности в публичном интернете** и **достижимых ресурсов данных** устанавливаются как `Not available`. Однако если хотя бы один связанный хост работает в режиме Full-Stack Monitoring и уязвимость раскрыта или затронута, функции **доступности в публичном интернете** и **достижимых ресурсов данных** отображаются.
* В режиме мониторинга инфраструктуры поддерживается информация об уязвимых функциях.

Режим мониторинга инфраструктуры не содержит информации об окружающей среде, такой как доступные ресурсы данных или доступность в публичном интернете, и ограничивает информацию о связанных объектах, например, базах данных и сервисах. Полная оценка возможна только для уязвимостей, у которых все связанные хосты находятся в режиме Full-Stack Monitoring.

* Если связанные хосты работают в режиме мониторинга инфраструктуры, OneAgent'ы передают недостаточно данных для анализа наличия уязвимости или затронутых конфиденциальных данных, поэтому для **доступности в публичном интернете** и **достижимых ресурсов данных** устанавливается значение `Not available`.
* Если все связанные хосты работают в режиме Full-Stack, кроме одного в режиме мониторинга инфраструктуры, и уязвимость не раскрыта и не затронута (исходя из хостов в режиме Full-Stack), значения для **доступности в публичном интернете** и **достижимых ресурсов данных** устанавливаются как `Not available`. Однако если хотя бы один связанный хост работает в режиме Full-Stack и уязвимость раскрыта или затронута, функции **доступности в публичном интернете** и **достижимых ресурсов данных** отображаются.

Те же возможности, что и в режиме Full-Stack Monitoring.

#### Потребление

* Если вы используете модель лицензирования Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities."), см. Мониторинг хостов (DPS): Infrastructure Monitoring.
* Если вы используете классическое лицензирование Dynatrace, см. Мониторинг приложений и инфраструктуры (Host Units).

### Режим обнаружения

[Режим обнаружения](../platform/oneagent/monitoring-modes/monitoring-modes.md#discovery "Find out more about the available monitoring modes when using OneAgent.") — это облегчённый режим мониторинга, обеспечивающий базовый мониторинг. Предоставляются следующие функциональные возможности:

* Системные метрики (использование CPU, памяти, дискового пространства)
* [Обнаружение уязвимостей в сторонних компонентах](application-security/vulnerability-analytics.md#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* [Обнаружение уязвимостей на уровне кода](application-security/vulnerability-analytics.md#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* Runtime Application Protection

Для работы Application Security в режиме обнаружения после [включения режима обнаружения](../platform/oneagent/monitoring-modes/monitoring-modes.md#enable-discovery-mode "Find out more about the available monitoring modes when using OneAgent.") также необходимо [включить внедрение кодового модуля](../platform/oneagent/monitoring-modes/monitoring-modes.md#code-module-injection "Find out more about the available monitoring modes when using OneAgent.").

#### Характеристики

Уязвимости в сторонних компонентах

Уязвимости на уровне кода

Атаки

Уязвимости в сторонних компонентах

Уязвимости на уровне кода

Атаки

* В развёртывании с режимом обнаружения Dynatrace Intelligence не может [адаптировать Dynatrace Security Score](vulnerabilities/concepts.md#dss-calculation "Concepts that are specific to the Dynatrace Vulnerabilities app."). В этом случае значение риска уязвимости не может быть пересмотрено, так как это возможно только на основе информации о топологии, извлечённой из вашей среды, и DSS будет равен базовому показателю CVSS.
* Режим обнаружения не содержит информации об окружающей среде, такой как доступные ресурсы данных или доступность в публичном интернете, и ограничивает информацию о связанных объектах, например, базах данных и сервисах. Полная оценка возможна только для уязвимостей, у которых все связанные хосты находятся в режиме Full-Stack Monitoring.

  + Если связанные хосты работают в режиме обнаружения, OneAgent'ы передают недостаточно данных для анализа наличия уязвимости или затронутых конфиденциальных данных, поэтому значения для **доступности в публичном интернете** и **достижимых ресурсов данных** устанавливаются как `Not available`.
  + Если все связанные хосты работают в режиме Full-Stack Monitoring, кроме одного в режиме обнаружения, и уязвимость не раскрыта и не затронута (исходя из хостов в режиме Full-Stack Monitoring), значения для **доступности в публичном интернете** и **достижимых ресурсов данных** устанавливаются как `Not available`. Однако если хотя бы один связанный хост работает в режиме Full-Stack Monitoring и уязвимость раскрыта или затронута, функции **доступности в публичном интернете** и **достижимых ресурсов данных** отображаются.

  Исключение

  Доступность в публичном интернете определяется на хостах Linux, работающих в режиме обнаружения, через eBPF. Возможные состояния: `Public network` и `Not detected`. Dynatrace Security Score не зависит ни от одного из этих состояний.
* В режиме обнаружения поддерживается информация об уязвимых функциях.

Режим обнаружения не содержит информации об окружающей среде, такой как доступные ресурсы данных или доступность в публичном интернете, и ограничивает информацию о связанных объектах, например, базах данных и сервисах. Полная оценка возможна только для уязвимостей, у которых все связанные хосты находятся в режиме Full-Stack Monitoring.

* Если связанные хосты работают в режиме обнаружения, OneAgent'ы передают недостаточно данных для анализа наличия уязвимости или затронутых конфиденциальных данных, поэтому значения для **доступности в публичном интернете** и **достижимых ресурсов данных** устанавливаются как `Not available`.
* Если все связанные хосты работают в режиме Full-Stack Monitoring, кроме одного в режиме обнаружения, и уязвимость не раскрыта и не затронута (исходя из хостов в режиме Full-Stack Monitoring), значения для **доступности в публичном интернете** и **достижимых ресурсов данных** устанавливаются как `Not available`. Однако если хотя бы один связанный хост работает в режиме Full-Stack Monitoring и уязвимость раскрыта или затронута, функции **доступности в публичном интернете** и **достижимых ресурсов данных** отображаются.

Исключение

Доступность в публичном интернете определяется на хостах Linux, работающих в режиме обнаружения, через eBPF. Возможные состояния: `Public network` и `Not detected`. Dynatrace Security Score не зависит ни от одного из этих состояний.

Те же возможности, что и в режиме Full-Stack Monitoring.

#### Потребление

Режим обнаружения доступен только для модели лицензирования Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

Информацию о потреблении при мониторинге см. в разделе Мониторинг хостов (DPS): Foundation & Discovery.

## Дополнительные ресурсы

Изучите дополнительную документацию, чтобы углубить понимание и максимально использовать возможности Dynatrace Application Security.

Видео

Учебные курсы Dynatrace University

Блоги

FAQ

Видео

Учебные курсы Dynatrace University

Блоги

FAQ

* Что такое Dynatrace и как начать работу:

  Что такое Dynatrace и как начать работу
* Повышение уровня безопасности с Dynatrace ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**:

  Повышение уровня безопасности с Dynatrace Anomaly Detection
* Unguard — площадка для тестирования безопасности приложений с открытым исходным кодом:

  Unguard: площадка для тестирования безопасности приложений с открытым исходным кодом
* Обнаружение уязвимостей и автоматическая оценка рисков с Dynatrace Application Security:

  Обнаружение уязвимостей и автоматическая оценка рисков с Dynatrace AppSec
* Устранение уязвимостей наподобие Log4Shell с помощью Dynatrace:

  Устранение уязвимостей наподобие Log4Shell с помощью Dynatrace
* Защита приложений от атак:

  Защита приложений от атак
* Как обеспечить гиперстабильную облачную безопасность с Dynatrace:

  Как обеспечить гиперстабильную облачную безопасность с Dynatrace

* [Введение в концепции Application Security](https://university.dynatrace.com/learn/courses/313/introduction-to-appsec)
* [Обзор Dynatrace Application Security](https://university.dynatrace.com/learn/courses/85/introduction/lessons/484/dynatrace-application-security)
* [Активация Application Security](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/382/activating-application-security)
* [Включение Runtime Vulnerability Analytics](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/384/enabling-runtime-vulnerability-analytics)
* [Автоматизация и упрощение Application Security с Dynatrace](https://university.dynatrace.com/learn/courses/259/automate-amp-simplify-application-security-with-dynatrace)
* [Настройка уведомлений безопасности](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/378/configuring-security-notifications)
* [Runtime Application Protection](https://university.dynatrace.com/learn/courses/89/runtime-application-protection/lessons/365/runtime-application-protection)
* [Управление уязвимостями на уровне кода](https://university.dynatrace.com/learn/courses/86/runtime-vulnerability-analytics/lessons/479/managing-code-level-vulnerabilities)
* [Кейс Application Security: log4j](https://university.dynatrace.com/learn/courses/87/case-studies/lessons/478/application-security-case-study-log4j)

* [Представляем ленту уязвимостей Dynatrace: точная, прозрачная и учитывающая угрозы](https://www.dynatrace.com/news/blog/introducing-the-dynatrace-vulnerability-feed-accurate-transparent-and-threat-aware/)
* [Устранение CVE-2025-3248: как Dynatrace Application Security защищает агентские AI-приложения](https://www.dynatrace.com/news/blog/remediating-cve-2025-3248-how-dynatrace-application-security-protects-agentic-ai-applications/)
* [Безопасность цепочки поставок: как обнаружить вредоносные программные пакеты с помощью Dynatrace](https://www.dynatrace.com/news/blog/supply-chain-security-how-to-detect-malicious-software-packages-with-dynatrace/)
* [Основы безопасности Kubernetes: Неправильные конфигурации контейнеров — от теории к эксплуатации](https://www.dynatrace.com/news/blog/kubernetes-security-essentials-container-misconfigurations-from-theory-to-exploitation/)
* [Платформа третьего поколения Dynatrace: создана для мира автономного интеллекта](https://www.dynatrace.com/news/blog/dynatrace-3rd-gen-platform/)
* [Революция в облачной безопасности с контекстом наблюдаемости: Dynatrace Cloud Security и CADR](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Расширение возможностей SRE с помощью аналитики уязвимостей во время выполнения и управления состоянием безопасности](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Dynatrace запускает мониторинг уязвимостей Python для повышения безопасности клиентов](https://www.dynatrace.com/news/blog/dynatrace-launches-python-vulnerability-monitoring-for-enhanced-customer-security/)
* [Интеграция Snyk для Dynatrace: соединение разработки и среды выполнения с действенными уведомлениями безопасности](https://www.dynatrace.com/news/blog/snyk-dynatrace-integration-actionable-notifications/)
* [Обнаружение угроз в нативных облачных средах: обнаружение подозрительного поведения сервисных аккаунтов Kubernetes](https://www.dynatrace.com/news/blog/threat-detection-cloud-native-kubernetes/)
* [Обнаружение угроз в нативных облачных средах (часть 2): как автоматизировать управление угрозами с помощью рабочих процессов](https://www.dynatrace.com/news/blog/threat-detection-automate-using-workflows/)
* [Возвращение к Spring4Shell: как Cloud Application Detection and Response (CADR) обеспечивает многоуровневую защиту](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [Основы безопасности Kubernetes: пути атак через неправильные конфигурации Kubernetes и стратегии смягчения](https://www.dynatrace.com/news/blog/kubernetes-misconfiguration-attack-paths-and-mitigation/)
* [Основы безопасности Kubernetes: понимание неправильных конфигураций безопасности Kubernetes](https://www.dynatrace.com/news/blog/understanding-kubernetes-security-misconfigurations/)
* [Балансировка безопасности и производительности с бизнес-целями через наблюдаемость](https://www.dynatrace.com/news/blog/balancing-security-and-performance-with-business-goals-through-observability/)
* [Анонс защиты Java SSRF в Dynatrace Application Security](https://dt-url.net/cn03zlo)
* [Уязвимость NGINX: быстрое обнаружение и устранение уязвимостей IngressNightmare с помощью Dynatrace](https://www.dynatrace.com/news/blog/nginx-vulnerability-mitigate-ingressnightmare-with-dynatrace/)
* [Откройте для себя новый опыт работы с Dynatrace Runtime Vulnerability Analytics](https://www.dynatrace.com/news/blog/discover-the-new-dynatrace-runtime-vulnerability-analytics-experience/)
* [Новые требования к непрерывному соответствию требованиям обусловливают необходимость конвергенции наблюдаемости и безопасности](https://www.dynatrace.com/news/blog/dynatrace-for-executives-security-compliance/)
* [Что такое мониторинг безопасности приложений](https://www.dynatrace.com/news/blog/what-is-application-security-monitoring/)
* [Реагирование на инциденты безопасности с помощью автоматизации Dynatrace](https://www.dynatrace.com/news/blog/context-aware-security-incident-response/)
* [Автоматизация DevSecOps повышает безопасность приложений в мультиоблачных средах](https://www.dynatrace.com/news/blog/devsecops-automation-improves-application-security/)
* [Управление уязвимостями vs управление доступностью: предотвращение атак с помощью надёжной стратегии кибербезопасности](https://www.dynatrace.com/news/blog/exposure-management-vs-vulnerability-management/)
* [Контекстно-зависимое реагирование на инциденты безопасности с Dynatrace Automations и Tetragon](https://www.dynatrace.com/news/blog/context-aware-security-incident-response/)
* [Лучшие практики построения надёжной модели зрелости DevSecOps](https://www.dynatrace.com/news/blog/devsecops-maturity-model-best-practices/)
* [Защита организации от уязвимостей нулевого дня](https://www.dynatrace.com/news/blog/protect-against-zero-day-vulnerabilities/)
* [Находите уязвимости в вашем коде — не ждите, пока их кто-то эксплуатирует](https://www.dynatrace.com/news/blog/code-level-vulnerability-detection/)
* [Покрытие жизненного цикла DevSecOps Dynatrace со Snyk устраняет слепые зоны в безопасности](https://www.dynatrace.com/news/blog/dynatrace-and-snyk-to-unify-security-insights/)
* [Что такое безопасность приложений? И почему нужен новый подход](https://www.dynatrace.com/news/blog/davis-security-advisor-extends-dynatrace-application-security/)

FAQ по Application Security

По статьям для решения проблем, связанных с Application Security, посетите [Сообщество Dynatrace](https://dt-url.net/dy122xtf).

## Связанные темы

* [Application Security](https://www.dynatrace.com/platform/application-security/)
* [eBook по облачной безопасности приложений](https://www.dynatrace.com/resources/ebooks/cloud-application-security/)
