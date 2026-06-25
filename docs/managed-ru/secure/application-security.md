---
title: Application Security
source: https://docs.dynatrace.com/managed/secure/application-security
scraped: 2026-05-12T11:04:01.930182
---

# Application Security

# Application Security

* How-to guide
* Updated on Feb 23, 2026

Что вы найдёте на этой странице

* [Обзор возможностей Application Security](#start)
* [Как режимы мониторинга влияют на данные и анализ](#monitoring-modes)
* [Дополнительные материалы: видео, обучение, блоги](#resources)

Dynatrace Application Security обеспечивает защиту в реальном времени и глубокую видимость вашего приложения. Сочетая автоматическое обнаружение уязвимостей, защиту от угроз во время выполнения и управление состоянием безопасности, эта функция позволяет командам защищать современные cloud-native среды с высокой точностью и масштабом. Изучите обзоры функций, шаги настройки, режимы работы и руководства по использованию.

## Начало работы

Чтобы начать работу с Dynatrace Application Security, следуйте инструкциям ниже.

Активация Application Security

Чтобы активировать Application Security, обратитесь к эксперту Dynatrace через чат.

Настройка возможностей Application Security

Dynatrace предоставляет следующие встроенные возможности Application Security для защиты ваших приложений. Выберите нужную, чтобы начать.

* [**Dynatrace Runtime Vulnerability Analytics (RVA)**](/managed/secure/application-security/vulnerability-analytics "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание прогресса устранения и создание правил мониторинга."): Мгновенное обнаружение критических уязвимостей с автоматической оценкой риска и воздействия благодаря глубокому анализу путей доступа к данным и выполнения в production-среде.
* [**Dynatrace Runtime Application Protection (RAP)**](/managed/secure/application-security/application-protection "Настройка и конфигурирование Dynatrace Runtime Application Protection для мониторинга атак и уязвимостей на уровне кода, генерируемых атаками."): Защита приложений в реальном времени путём обнаружения и блокировки атак с помощью глубокого анализа на уровне кода и транзакций.

## Охват режимов мониторинга

Эффективность и глубина аналитики Application Security зависят от используемого режима мониторинга. В этом разделе объясняется, как каждый режим влияет на сбор и анализ данных.

### Обзор поддержки

| Возможность | Full-Stack | Infrastructure | Discovery |
| --- | --- | --- | --- |
| [Обнаружение уязвимостей сторонних компонентов](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание прогресса устранения и создание правил мониторинга.") | Green background check mark | [ограниченно](#tpv-infra) | [ограниченно](#clv-infra) |
| [Обнаружение уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics#clv-detection "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание прогресса устранения и создание правил мониторинга.") | Green background check mark | [ограниченно](#tpv-disco) | [ограниченно](#clv-disco) |
| [Runtime Application Protection](/managed/secure/application-security/application-protection "Настройка и конфигурирование Dynatrace Runtime Application Protection для мониторинга атак и уязвимостей на уровне кода, генерируемых атаками.") | Green background check mark | Green background check mark | Green background check mark |

Доступность из публичного интернета

На хостах Linux, при отсутствии данных (что возможно в различных режимах мониторинга или в случае сбоя), доступность из публичного интернета определяется через eBPF. Возможные состояния: `Public network` и `Not detected`. Davis Security Score не зависит ни от одного из этих состояний.

### Режим Full-Stack Monitoring

Рекомендуется

Режим Full-Stack Monitoring обеспечивает полный мониторинг производительности приложений, видимость на уровне кода, глубокий мониторинг процессов и Infrastructure Monitoring (включая платформы PaaS).

### Режим Infrastructure Monitoring

[Режим Infrastructure Monitoring](/managed/platform/oneagent/monitoring-modes/monitoring-modes#infrastructure-only "Узнайте подробнее о доступных режимах мониторинга при использовании OneAgent."), в котором OneAgent настроен на обеспечение мониторинга физической и виртуальной инфраструктуры, обеспечивает менее полный мониторинг по сравнению с режимом Full-Stack Monitoring. Предоставляются следующие функциональные возможности:

* Системные метрики (использование CPU, памяти, диска)
* [Обнаружение уязвимостей сторонних компонентов](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание прогресса устранения и создание правил мониторинга.")
* [Обнаружение уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics#clv-detection "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание прогресса устранения и создание правил мониторинга.")
* [Runtime Application Protection](/managed/secure/application-security/application-protection "Настройка и конфигурирование Dynatrace Runtime Application Protection для мониторинга атак и уязвимостей на уровне кода, генерируемых атаками.")

#### Характеристики

Уязвимости сторонних компонентов

Уязвимости на уровне кода

Атаки

* В режиме Infrastructure Monitoring Davis® AI не может [адаптировать Davis Security Score](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score#score "Расчёт Davis Security Score и прогнозирование потенциальных рисков уязвимостей с помощью Davis AI."). В этом случае значение риска уязвимости не может быть переоценено, так как это возможно только на основе топологической информации, извлечённой из вашей среды, и DSS будет равен базовому показателю CVSS.
* В режиме Infrastructure Monitoring отсутствует информация о среде, такая как доступность из публичного интернета или наличие доступных активов данных, и ограничена информация о связанных сущностях — базах данных и сервисах. Полная оценка может быть выполнена только для уязвимостей, все связанные хосты которых находятся в режиме Full-Stack Monitoring.

  + Если связанные хосты работают в режиме Infrastructure Monitoring, OneAgent передаёт недостаточно данных для проверки наличия риска воздействия или затронутых конфиденциальных данных; в этом случае значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`.
  + Если все связанные хосты работают в режиме Full-Stack Monitoring, кроме одного, работающего в режиме Infrastructure Monitoring, и уязвимость не является exposed или affected (на основе хостов в режиме Full-Stack), значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`. Однако если хотя бы один связанный хост работает в режиме Full-Stack Monitoring и уязвимость является exposed или affected, функции **public internet exposure** и **reachable data assets** отображаются.
* В режиме Infrastructure Monitoring поддерживается информация об уязвимых функциях.

В режиме Infrastructure Monitoring отсутствует информация о среде, такая как доступность из публичного интернета или наличие доступных активов данных, и ограничена информация о связанных сущностях — базах данных и сервисах. Полная оценка может быть выполнена только для уязвимостей, все связанные хосты которых находятся в режиме Full-Stack Monitoring.

* Если связанные хосты работают в режиме Infrastructure Monitoring, OneAgent передаёт недостаточно данных для проверки наличия риска воздействия или затронутых конфиденциальных данных; в этом случае значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`.
* Если все связанные хосты работают в режиме Full-Stack, кроме одного в режиме Infrastructure Monitoring, и уязвимость не является exposed или affected (на основе хостов в режиме Full-Stack), значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`. Однако если хотя бы один связанный хост работает в режиме Full-Stack и уязвимость является exposed или affected, функции **public internet exposure** и **reachable data assets** отображаются.

Те же возможности, что и в режиме Full-Stack Monitoring.

#### Потребление лицензий

* Если вы используете [лицензионную модель Dynatrace Platform Subscription (DPS)](/managed/license "О лицензионной модели Dynatrace Platform Subscription (DPS) для всех возможностей Dynatrace."), см. [Мониторинг хостов (DPS): Infrastructure Monitoring](/managed/license/capabilities/app-infra-observability/infrastructure-monitoring "Узнайте, как рассчитывается потребление возможности Dynatrace Infrastructure Monitoring DPS.").
* Если вы используете [классическое лицензирование Dynatrace](/managed/license/monitoring-consumption-classic "Понимание расчёта потребления мониторинга Dynatrace при классическом лицензировании."), см. [Application and Infrastructure Monitoring (Host Units)](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Понимание расчёта потребления мониторинга приложений и инфраструктуры Dynatrace на основе единиц хостов.").

### Режим Discovery

[Режим Discovery](/managed/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Узнайте подробнее о доступных режимах мониторинга при использовании OneAgent.") — это облегчённый режим мониторинга, обеспечивающий базовый мониторинг. Предоставляются следующие функциональные возможности:

* Системные метрики (использование CPU, памяти, диска)
* [Обнаружение уязвимостей сторонних компонентов](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание прогресса устранения и создание правил мониторинга.")
* [Обнаружение уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics#clv-detection "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание прогресса устранения и создание правил мониторинга.")
* [Runtime Application Protection](/managed/secure/application-security/application-protection "Настройка и конфигурирование Dynatrace Runtime Application Protection для мониторинга атак и уязвимостей на уровне кода, генерируемых атаками.")

Для работы Application Security в режиме Discovery после [включения режима Discovery](/managed/platform/oneagent/monitoring-modes/monitoring-modes#enable-discovery-mode "Узнайте подробнее о доступных режимах мониторинга при использовании OneAgent.") необходимо также [включить внедрение кодового модуля](/managed/platform/oneagent/monitoring-modes/monitoring-modes#code-module-injection "Узнайте подробнее о доступных режимах мониторинга при использовании OneAgent.").

#### Характеристики

Уязвимости сторонних компонентов

Уязвимости на уровне кода

Атаки

* В режиме Discovery Davis AI не может [адаптировать Davis Security Score](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score#score "Расчёт Davis Security Score и прогнозирование потенциальных рисков уязвимостей с помощью Davis AI."). В этом случае значение риска уязвимости не может быть переоценено, так как это возможно только на основе топологической информации, извлечённой из вашей среды, и DSS будет равен базовому показателю CVSS.
* В режиме Discovery отсутствует информация о среде, такая как доступность из публичного интернета или наличие доступных активов данных, и ограничена информация о связанных сущностях — базах данных и сервисах. Полная оценка может быть выполнена только для уязвимостей, все связанные хосты которых находятся в режиме Full-Stack Monitoring.

  + Если связанные хосты работают в режиме Discovery, OneAgent передаёт недостаточно данных для проверки наличия риска воздействия или затронутых конфиденциальных данных; в этом случае значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`.
  + Если все связанные хосты работают в режиме Full-Stack Monitoring, кроме одного в режиме Discovery, и уязвимость не является exposed или affected (на основе хостов в режиме Full-Stack Monitoring), значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`. Однако если хотя бы один связанный хост работает в режиме Full-Stack Monitoring и уязвимость является exposed или affected, функции **public internet exposure** и **reachable data assets** отображаются.

  Исключение

  На хостах Linux в режиме Discovery доступность из публичного интернета определяется через eBPF. Возможные состояния: `Public network` и `Not detected`. Davis Security Score не зависит ни от одного из этих состояний.
* В режиме Discovery поддерживается информация об уязвимых функциях.

В режиме Discovery отсутствует информация о среде, такая как доступность из публичного интернета или наличие доступных активов данных, и ограничена информация о связанных сущностях — базах данных и сервисах. Полная оценка может быть выполнена только для уязвимостей, все связанные хосты которых находятся в режиме Full-Stack Monitoring.

* Если связанные хосты работают в режиме Discovery, OneAgent передаёт недостаточно данных для проверки наличия риска воздействия или затронутых конфиденциальных данных; в этом случае значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`.
* Если все связанные хосты работают в режиме Full-Stack Monitoring, кроме одного в режиме Discovery, и уязвимость не является exposed или affected (на основе хостов в режиме Full-Stack Monitoring), значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`. Однако если хотя бы один связанный хост работает в режиме Full-Stack Monitoring и уязвимость является exposed или affected, функции **public internet exposure** и **reachable data assets** отображаются.

Исключение

На хостах Linux в режиме Discovery доступность из публичного интернета определяется через eBPF. Возможные состояния: `Public network` и `Not detected`. Davis Security Score не зависит ни от одного из этих состояний.

Те же возможности, что и в режиме Full-Stack Monitoring.

#### Потребление лицензий

Режим Discovery доступен только при использовании [лицензионной модели Dynatrace Platform Subscription (DPS)](/managed/license "О лицензионной модели Dynatrace Platform Subscription (DPS) для всех возможностей Dynatrace.").

Сведения о потреблении мониторинга см. в разделе [Мониторинг хостов (DPS): Foundation & Discovery](/managed/license/capabilities/app-infra-observability/foundation-and-discovery "Узнайте, как рассчитывается потребление возможности Dynatrace Foundation & Discovery DPS.").

## Дополнительные ресурсы

Изучите дополнительную документацию для более глубокого понимания и максимально эффективного использования Dynatrace Application Security.

Видео

Учебные материалы Dynatrace University

Блоги

FAQ

* Что такое Dynatrace и как начать работу:

  What is Dynatrace and how to get started
* Повышение уровня безопасности с помощью Dynatrace Davis Anomaly Detection:

  Elevating Security with Dynatrace Davis Anomaly Detection
* Unguard — игровая площадка для безопасности приложений с открытым исходным кодом:

  Unguard: An open source application security playground
* Обнаружение уязвимостей и автоматическая оценка рисков с помощью Dynatrace Application Security:

  Vulnerability Detection and Automated Risk Assessment with Dynatrace AppSec
* Устранение уязвимостей типа Log4Shell с помощью Dynatrace:

  Remediate Vulnerabilities like Log4Shell with Dynatrace
* Защита приложений от атак:

  Protecting your applications against attacks
* Как достичь cloud-native гиперасштабируемой безопасности с помощью Dynatrace:

  How to achieve cloud native hyperscale security with Dynatrace

* [Introduction to Application Security concepts](https://university.dynatrace.com/learn/courses/313/introduction-to-appsec)
* [Dynatrace Application Security overview](https://university.dynatrace.com/learn/courses/85/introduction/lessons/484/dynatrace-application-security)
* [Activate Application Security](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/382/activating-application-security)
* [Enable Runtime Vulnerability Analytics](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/384/enabling-runtime-vulnerability-analytics)
* [Automate and simplify Application Security with Dynatrace](https://university.dynatrace.com/learn/courses/259/automate-amp-simplify-application-security-with-dynatrace)
* [Configure security notifications](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/378/configuring-security-notifications)
* [Runtime Application Protection](https://university.dynatrace.com/learn/courses/89/runtime-application-protection/lessons/365/runtime-application-protection)
* [Manage code-level vulnerabilities](https://university.dynatrace.com/learn/courses/86/runtime-vulnerability-analytics/lessons/479/managing-code-level-vulnerabilities)
* [Application Security case study: log4j](https://university.dynatrace.com/learn/courses/87/case-studies/lessons/478/application-security-case-study-log4j)

* [Remediating CVE-2025-3248: How Dynatrace Application Security protects Agentic AI applications](https://www.dynatrace.com/news/blog/remediating-cve-2025-3248-how-dynatrace-application-security-protects-agentic-ai-applications/)
* [Supply chain security: How to detect malicious software packages with Dynatrace](https://www.dynatrace.com/news/blog/supply-chain-security-how-to-detect-malicious-software-packages-with-dynatrace/)
* [Kubernetes security essentials: Container misconfigurations — From theory to exploitation](https://www.dynatrace.com/news/blog/kubernetes-security-essentials-container-misconfigurations-from-theory-to-exploitation/)
* [Dynatrace 3rd-generation platform: Built for the world of Autonomous Intelligence](https://www.dynatrace.com/news/blog/dynatrace-3rd-gen-platform/)
* [Revolutionizing cloud security with observability context: Dynatrace Cloud Security addressing CADR](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Empowering SREs with runtime vulnerability analytics and security posture management](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Dynatrace launches Python Vulnerability Monitoring for enhanced customer security](https://www.dynatrace.com/news/blog/dynatrace-launches-python-vulnerability-monitoring-for-enhanced-customer-security/)
* [Snyk integration for Dynatrace: Bridging development and runtime with actionable security notifications](https://www.dynatrace.com/news/blog/snyk-dynatrace-integration-actionable-notifications/)
* [Threat detection in cloud native environments: Detecting suspicious Kubernetes service account behavior](https://www.dynatrace.com/news/blog/threat-detection-cloud-native-kubernetes/)
* [Threat detection in cloud native environments (part 2): How to automate threat management using workflows](https://www.dynatrace.com/news/blog/threat-detection-automate-using-workflows/)
* [Revisiting Spring4Shell: How Cloud Application Detection and Response (CADR) offers multi-layer protection](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [Kubernetes security essentials: Kubernetes misconfiguration attack paths and mitigation strategies](https://www.dynatrace.com/news/blog/kubernetes-misconfiguration-attack-paths-and-mitigation/)
* [Kubernetes security essentials: Understanding Kubernetes security misconfigurations](https://www.dynatrace.com/news/blog/understanding-kubernetes-security-misconfigurations/)
* [Balancing security and performance with business goals through observability](https://www.dynatrace.com/news/blog/balancing-security-and-performance-with-business-goals-through-observability/)
* [Announcing Java SSRF protection in Dynatrace Application Security](https://dt-url.net/cn03zlo)
* [NGINX vulnerability: Quickly detect and mitigate IngressNightmare vulnerabilities with Dynatrace](https://www.dynatrace.com/news/blog/nginx-vulnerability-mitigate-ingressnightmare-with-dynatrace/)
* [Discover the new Dynatrace Runtime Vulnerability Analytics experience](https://www.dynatrace.com/news/blog/discover-the-new-dynatrace-runtime-vulnerability-analytics-experience/)
* [New continuous compliance requirements drive the need to converge observability and security](https://www.dynatrace.com/news/blog/dynatrace-for-executives-security-compliance/)
* [What is application security monitoring](https://www.dynatrace.com/news/blog/what-is-application-security-monitoring/)
* [Security incident response with Dynatrace automations](https://www.dynatrace.com/news/blog/context-aware-security-incident-response/)
* [DevSecOps automation improves application security in multicloud environments](https://www.dynatrace.com/news/blog/devsecops-automation-improves-application-security/)
* [Exposure management vs. vulnerability management: Preventing attacks with a robust cybersecurity strategy](https://www.dynatrace.com/news/blog/exposure-management-vs-vulnerability-management/)
* [Context-aware security incident response with Dynatrace Automations and Tetragon](https://www.dynatrace.com/news/blog/context-aware-security-incident-response/)
* [Best practices for building a strong DevSecOps maturity model](https://www.dynatrace.com/news/blog/devsecops-maturity-model-best-practices/)
* [Protect your organization from zero-day vulnerabilities](https://www.dynatrace.com/news/blog/protect-against-zero-day-vulnerabilities/)
* [Find vulnerabilities in your code — don't wait for someone to exploit them](https://www.dynatrace.com/news/blog/code-level-vulnerability-detection/)
* [Dynatrace DevSecOps Lifecycle Coverage with Snyk eliminates security coverage blind spots](https://www.dynatrace.com/news/blog/dynatrace-and-snyk-to-unify-security-insights/)
* [Davis Security Advisor extends Application Security](https://www.dynatrace.com/news/blog/davis-security-advisor-extends-dynatrace-application-security/)

[FAQ по Application Security](/managed/secure/faq "Часто задаваемые вопросы о Dynatrace Application Security.")

Статьи по устранению неполадок Application Security можно найти в [Dynatrace Community](https://dt-url.net/dy122xtf).

## Связанные темы

* [Application Security](https://www.dynatrace.com/platform/application-security/)
* [Cloud Application Security eBook](https://www.dynatrace.com/resources/ebooks/cloud-application-security/)