---
title: Безопасность приложений
source: https://docs.dynatrace.com/managed/secure/application-security
---

# Безопасность приложений

# Безопасность приложений

* Практическое руководство
* Обновлено 23 февраля 2026 г.

Что можно найти на этой странице

* [Возможности Application Security](#start)
* [Как режимы мониторинга влияют на данные и анализ](#monitoring-modes)
* [Углубить знания: видео, руководства, блоги](#resources)

Dynatrace Application Security обеспечивает защиту в реальном времени и глубокую видимость приложений. За счёт сочетания автоматического обнаружения уязвимостей, предотвращения угроз во время выполнения и управления состоянием защищённости эта функция помогает командам обеспечивать безопасность современных облачных сред с высокой точностью и на любом масштабе. Здесь собраны обзоры возможностей, шаги настройки, режимы работы и рекомендации по использованию.

## Начало работы

Чтобы начать работу с Dynatrace Application Security, выполни следующие шаги.

Активация Application Security

Чтобы активировать Application Security, нужно обратиться к эксперту по продукту Dynatrace через онлайн-чат.

Настройка возможностей Application Security

Dynatrace предоставляет следующие интегрированные возможности Application Security для защиты приложений. Выбери одну из них, чтобы начать.

* [**Dynatrace Runtime Vulnerability Analytics (RVA)**](/managed/secure/application-security/vulnerability-analytics "Отслеживание, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание хода устранения и создание правил мониторинга."): позволяет мгновенно выявлять критические уязвимости благодаря автоматическим оценкам риска и влияния, основанным на глубоком анализе путей доступа к данным и выполнения в production.
* [**Dynatrace Runtime Application Protection (RAP)**](/managed/secure/application-security/application-protection "Настройка и конфигурация Dynatrace Runtime Application Protection для отслеживания атак и вызванных атаками уязвимостей на уровне кода."): защищает приложения в реальном времени, обнаруживая и блокируя атаки благодаря глубокому анализу кода и транзакций.

## Охват режимами мониторинга

Эффективность и глубина анализа Application Security зависят от развёрнутого режима мониторинга. В этом разделе объясняется, как каждый режим влияет на сбор данных и анализ.

### Обзор поддержки

| Возможность | Full-Stack | Infrastructure | Discovery |
| --- | --- | --- | --- |
| [Обнаружение уязвимостей сторонних компонентов](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Отслеживание, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание хода устранения и создание правил мониторинга.") | Зелёная галочка на фоне | [ограниченно](#tpv-infra) | [ограниченно](#clv-infra) |
| [Обнаружение уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics#clv-detection "Отслеживание, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание хода устранения и создание правил мониторинга.") | Зелёная галочка на фоне | [ограниченно](#tpv-disco) | [ограниченно](#clv-disco) |
| [Runtime Application Protection](/managed/secure/application-security/application-protection "Настройка и конфигурация Dynatrace Runtime Application Protection для отслеживания атак и вызванных атаками уязвимостей на уровне кода.") | Зелёная галочка на фоне | Зелёная галочка на фоне | Зелёная галочка на фоне |

Публичная доступность из интернета

На хостах Linux, если информации нет (это может происходить в разных режимах мониторинга или из-за сбоя), публичная доступность из интернета определяется через eBPF. Возможные состояния: `Public network` и `Not detected`. Ни одно из этих состояний не влияет на Davis Security Score.

### Режим Full-Stack Monitoring

Рекомендуется

Режим Full-Stack Monitoring обеспечивает полный мониторинг производительности приложений, видимость на уровне кода, глубокий мониторинг процессов и мониторинг инфраструктуры (включая PaaS-платформы).

### Режим Infrastructure Monitoring

[Режим Infrastructure Monitoring](/managed/platform/oneagent/monitoring-modes/monitoring-modes#infrastructure-only "Подробнее о доступных режимах мониторинга при использовании OneAgent."), при котором OneAgent настроен на мониторинг, ориентированный на физическую и виртуальную инфраструктуру, обеспечивает менее полный мониторинг, чем режим Full-Stack Monitoring. Доступны следующие функции:

* Системные метрики (использование CPU, использование памяти, использование диска)
* [Обнаружение уязвимостей сторонних компонентов](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Отслеживание, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание хода устранения и создание правил мониторинга.")
* [Обнаружение уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics#clv-detection "Отслеживание, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание хода устранения и создание правил мониторинга.")
* [Runtime Application Protection](/managed/secure/application-security/application-protection "Настройка и конфигурация Dynatrace Runtime Application Protection для отслеживания атак и вызванных атаками уязвимостей на уровне кода.")

#### Характеристики

Уязвимости сторонних компонентовУязвимости сторонних компонентов

Уязвимости на уровне кодаУязвимости на уровне кода

АтакиАтаки

Уязвимости сторонних компонентов

Уязвимости на уровне кода

Атаки

* В развёртывании с Infrastructure Monitoring Davis® AI не может [адаптировать Davis Security Score](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score#score "Расчёт Davis Security Score и прогнозирование потенциальных рисков уязвимостей с помощью Davis AI."). В этом случае значение риска уязвимости не может быть пересчитано, поскольку это возможно только на основе информации о топологии, извлечённой из среды, и DSS будет совпадать с базовой оценкой CVSS.
* В режиме Infrastructure Monitoring отсутствует информация об окружении, такая как доступные ресурсы данных или публичная доступность из интернета, а также ограничена информация о связанных сущностях, таких как базы данных и сервисы. Полная оценка возможна только для уязвимостей, у которых все связанные хосты работают под Full-Stack Monitoring.

  + Если связанные хосты работают в режиме Infrastructure Monitoring, данных, отправляемых OneAgent, недостаточно для проверки наличия доступности или затронутых чувствительных данных, поэтому значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`.
  + Если все связанные хосты работают в режиме Full-Stack Monitoring, кроме одного, работающего в режиме Infrastructure Monitoring, и уязвимость не подвержена доступности или воздействию (на основе хостов в режиме Full-Stack), значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`. Однако если хотя бы один связанный хост работает в режиме Full-Stack Monitoring и уязвимость подвержена доступности или воздействию, функции **public internet exposure** и **reachable data assets** отображаются.
* В режиме Infrastructure Monitoring информация об уязвимых функциях поддерживается.

В режиме Infrastructure Monitoring отсутствует информация об окружении, такая как доступные ресурсы данных или публичная доступность из интернета, а также ограничена информация о связанных сущностях, таких как базы данных и сервисы. Полная оценка возможна только для уязвимостей, у которых все связанные хосты работают под Full-Stack Monitoring.

* Если связанные хосты работают в режиме Infrastructure Monitoring, данных, отправляемых OneAgent, недостаточно для проверки наличия доступности или затронутых чувствительных данных, поэтому значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`.
* Если все связанные хосты работают в режиме Full-Stack, кроме одного, работающего в режиме Infrastructure Monitoring, и уязвимость не подвержена доступности или воздействию (на основе хостов в режиме Full-Stack), значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`. Однако если хотя бы один связанный хост работает в режиме Full-Stack и уязвимость подвержена доступности или воздействию, функции **public internet exposure** и **reachable data assets** отображаются.

Те же возможности, что и у режима Full-Stack Monitoring.

#### Потребление

* При использовании [модели лицензирования Dynatrace Platform Subscription (DPS)](/managed/license "Dynatrace Platform Subscription, тарифные карты возможностей, гибридное лицензирование и предыдущие модели лицензирования.") см. [Мониторинг хостов (DPS): Infrastructure Monitoring](/managed/license/capabilities/app-infra-observability/infrastructure-monitoring "Узнать, как рассчитывается потребление Infrastructure Monitoring, как отслеживать и анализировать использование и как оптимизировать расходы.").
* При использовании [классического лицензирования Dynatrace](/managed/license/monitoring-consumption-classic "Понять, как рассчитывается классическое потребление мониторинга Dynatrace, включая host units, DDU, DEM units и Application Security units.") см. [Application and Infrastructure Monitoring (Host Units)](/managed/license/classic-licensing/application-and-infrastructure-monitoring "Понять, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе host units.").

### Discovery mode

[Discovery mode](/managed/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Find out more about the available monitoring modes when using OneAgent.") это облегчённый режим мониторинга, обеспечивающий базовое наблюдение. Доступны следующие функции:

* системные метрики (использование CPU, памяти, диска)
* [обнаружение уязвимостей сторонних компонентов](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* [обнаружение уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* [Runtime Application Protection](/managed/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")

Чтобы Application Security работал в Discovery mode, после [включения Discovery mode](/managed/platform/oneagent/monitoring-modes/monitoring-modes#enable-discovery-mode "Find out more about the available monitoring modes when using OneAgent.") нужно также [включить внедрение код-модулей](/managed/platform/oneagent/monitoring-modes/monitoring-modes#code-module-injection "Find out more about the available monitoring modes when using OneAgent.").

#### Характеристики

Уязвимости сторонних компонентовУязвимости сторонних компонентов

Уязвимости на уровне кодаУязвимости на уровне кода

АтакиАтаки

Уязвимости сторонних компонентов

Уязвимости на уровне кода

Атаки

* При развёртывании в Discovery mode Davis AI не может [адаптировать Davis Security Score](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score#score "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI."). В этом случае значение риска уязвимости нельзя переоценить, поскольку это возможно только на основе информации о топологии, извлечённой из окружения, поэтому DSS будет совпадать с базовой оценкой CVSS.
* В Discovery mode не хватает информации об окружении, такой как доступные ресурсы данных или доступность из интернета, и ограничена информация о связанных сущностях, таких как базы данных и сервисы. Полная оценка возможна только для уязвимостей, у которых все связанные хосты находятся под Full-Stack Monitoring.

  + Если связанные хосты работают в Discovery mode, OneAgent не отправляет достаточно данных, чтобы определить наличие доступности извне или затронутых чувствительных данных, поэтому значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`.
  + Если все связанные хосты работают в режиме Full-Stack Monitoring, кроме одного, который работает в Discovery mode, и уязвимость не является доступной или затронутой (на основе хостов в Full-Stack Monitoring), значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`. Однако, если хотя бы один связанный хост работает в режиме Full-Stack Monitoring и уязвимость является доступной или затронутой, функции **public internet exposure** и **reachable data assets** отображаются.

  Исключение

  Доступность из интернета обнаруживается на хостах Linux, работающих в Discovery mode, через eBPF. Возможные состояния: `Public network` и `Not detected`. Ни одно из этих состояний не влияет на Davis Security Score.
* В Discovery mode информация об уязвимых функциях поддерживается.

В Discovery mode не хватает информации об окружении, такой как доступные ресурсы данных или доступность из интернета, и ограничена информация о связанных сущностях, таких как базы данных и сервисы. Полная оценка возможна только для уязвимостей, у которых все связанные хосты находятся под Full-Stack Monitoring.

* Если связанные хосты работают в Discovery mode, OneAgent не отправляет достаточно данных, чтобы определить наличие доступности извне или затронутых чувствительных данных, поэтому значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`.
* Если все связанные хосты работают в режиме Full-Stack Monitoring, кроме одного, который работает в Discovery mode, и уязвимость не является доступной или затронутой (на основе хостов в Full-Stack Monitoring), значения **public internet exposure** и **reachable data assets** устанавливаются в `Not available`. Однако, если хотя бы один связанный хост работает в режиме Full-Stack Monitoring и уязвимость является доступной или затронутой, функции **public internet exposure** и **reachable data assets** отображаются.

Исключение

Доступность из интернета обнаруживается на хостах Linux, работающих в Discovery mode, через eBPF. Возможные состояния: `Public network` и `Not detected`. Ни одно из этих состояний не влияет на Davis Security Score.

Те же возможности, что и в режиме Full-Stack Monitoring.

#### Потребление

Discovery mode доступен только для лицензионной модели [Dynatrace Platform Subscription (DPS)](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models.").

Информацию о потреблении при мониторинге см. в разделе [Host monitoring (DPS): Foundation & Discovery](/managed/license/capabilities/app-infra-observability/foundation-and-discovery "Learn how your consumption of the Dynatrace Foundation & Discovery DPS capability is billed and charged.").

## Дополнительные ресурсы

Ознакомься с дополнительной документацией, чтобы углубить понимание и получить максимум от Dynatrace Application Security.

VideosVideos

Dynatrace University tutorialsDynatrace University tutorials

BlogsBlogs

FAQFAQ

Видео

Учебные материалы Dynatrace University

Блоги

Вопросы и ответы

* What is Dynatrace and how to get started:

  What is Dynatrace and how to get started
* Elevate security with Dynatrace Davis Anomaly Detection:

  Elevating Security with Dynatrace Davis Anomaly Detection
* Unguard - An open source application security playground:

  Unguard: An open source application security playground
* Vulnerability detection and automated risk assessment with Dynatrace Application Security:

  Vulnerability Detection and Automated Risk Assessment with Dynatrace AppSec
* Remediate vulnerabilities like Log4Shell with Dynatrace:

  Remediate Vulnerabilities like Log4Shell with Dynatrace
* Protect your applications against attacks:

  Protecting your applications against attacks
* How to achieve cloud native hyperscale security with Dynatrace:

  How to achieve cloud native hyperscale security with Dynatrace

* [Introduction to Application Security concepts﻿](https://university.dynatrace.com/learn/courses/313/introduction-to-appsec)
* [Обзор Dynatrace Application Security﻿](https://university.dynatrace.com/learn/courses/85/introduction/lessons/484/dynatrace-application-security)
* [Активация Application Security﻿](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/382/activating-application-security)
* [Включение Runtime Vulnerability Analytics﻿](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/384/enabling-runtime-vulnerability-analytics)
* [Автоматизация и упрощение Application Security с Dynatrace﻿](https://university.dynatrace.com/learn/courses/259/automate-amp-simplify-application-security-with-dynatrace)
* [Настройка уведомлений безопасности﻿](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/378/configuring-security-notifications)
* [Runtime Application Protection﻿](https://university.dynatrace.com/learn/courses/89/runtime-application-protection/lessons/365/runtime-application-protection)
* [Управление уязвимостями уровня кода﻿](https://university.dynatrace.com/learn/courses/86/runtime-vulnerability-analytics/lessons/479/managing-code-level-vulnerabilities)
* [Практический пример Application Security: log4j﻿](https://university.dynatrace.com/learn/courses/87/case-studies/lessons/478/application-security-case-study-log4j)

* [Remediating CVE-2025-3248: How Dynatrace Application Security protects Agentic AI applications﻿](https://www.dynatrace.com/news/blog/remediating-cve-2025-3248-how-dynatrace-application-security-protects-agentic-ai-applications/)
* [Supply chain security: How to detect malicious software packages with Dynatrace﻿](https://www.dynatrace.com/news/blog/supply-chain-security-how-to-detect-malicious-software-packages-with-dynatrace/)
* [Kubernetes security essentials: Container misconfigurations – From theory to exploitation﻿](https://www.dynatrace.com/news/blog/kubernetes-security-essentials-container-misconfigurations-from-theory-to-exploitation/)
* [Dynatrace 3rd-generation platform: Built for the world of Autonomous Intelligence﻿](https://www.dynatrace.com/news/blog/dynatrace-3rd-gen-platform/)
* [Revolutionizing cloud security with observability context: Dynatrace Cloud Security addressing CADR﻿](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Empowering SREs with runtime vulnerability analytics and security posture management﻿](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Dynatrace launches Python Vulnerability Monitoring for enhanced customer security﻿](https://www.dynatrace.com/news/blog/dynatrace-launches-python-vulnerability-monitoring-for-enhanced-customer-security/)
* [Snyk integration for Dynatrace: Bridging development and runtime with actionable security notifications﻿](https://www.dynatrace.com/news/blog/snyk-dynatrace-integration-actionable-notifications/)
* [Threat detection in cloud native environments: Detecting suspicious Kubernetes service account behavior﻿](https://www.dynatrace.com/news/blog/threat-detection-cloud-native-kubernetes/)
* [Threat detection in cloud native environments (part 2): How to automate threat management using workflows﻿](https://www.dynatrace.com/news/blog/threat-detection-automate-using-workflows/)
* [Revisiting Spring4Shell: How Cloud Application Detection and Response (CADR) offers multi-layer protection﻿](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [Kubernetes security essentials: Kubernetes misconfiguration attack paths and mitigation strategies﻿](https://www.dynatrace.com/news/blog/kubernetes-misconfiguration-attack-paths-and-mitigation/)
* [Kubernetes security essentials: Understanding Kubernetes security misconfigurations﻿](https://www.dynatrace.com/news/blog/understanding-kubernetes-security-misconfigurations/)
* [Balancing security and performance with business goals through observability﻿](https://www.dynatrace.com/news/blog/balancing-security-and-performance-with-business-goals-through-observability/)
* [Announcing Java SSRF protection in Dynatrace Application Security﻿](https://dt-url.net/cn03zlo)
* [NGINX vulnerability: Quickly detect and mitigate IngressNightmare vulnerabilities with Dynatrace﻿](https://www.dynatrace.com/news/blog/nginx-vulnerability-mitigate-ingressnightmare-with-dynatrace/)
* [Discover the new Dynatrace Runtime Vulnerability Analytics experience﻿](https://www.dynatrace.com/news/blog/discover-the-new-dynatrace-runtime-vulnerability-analytics-experience/)
* [New continuous compliance requirements drive the need to converge observability and security﻿](https://www.dynatrace.com/news/blog/dynatrace-for-executives-security-compliance/)
* [What is application security monitoring﻿](https://www.dynatrace.com/news/blog/what-is-application-security-monitoring/)
* [Security incident response with Dynatrace automations﻿](https://www.dynatrace.com/news/blog/context-aware-security-incident-response/)
* [DevSecOps automation improves application security in multicloud environments﻿](https://www.dynatrace.com/news/blog/devsecops-automation-improves-application-security/)
* [Exposure management vs. vulnerability management: Preventing attacks with a robust cybersecurity strategy﻿](https://www.dynatrace.com/news/blog/exposure-management-vs-vulnerability-management/)
* [Context-aware security incident response with Dynatrace Automations and Tetragon﻿](https://www.dynatrace.com/news/blog/context-aware-security-incident-response/)
* [Best practices for building a strong DevSecOps maturity model﻿](https://www.dynatrace.com/news/blog/devsecops-maturity-model-best-practices/)
* [Protect your organization from zero-day vulnerabilities﻿](https://www.dynatrace.com/news/blog/protect-against-zero-day-vulnerabilities/)
* [Find vulnerabilities in your code-don’t wait for someone to exploit them﻿](https://www.dynatrace.com/news/blog/code-level-vulnerability-detection/)
* [Dynatrace DevSecOps Lifecycle Coverage with Snyk eliminates security coverage blind spots﻿](https://www.dynatrace.com/news/blog/dynatrace-and-snyk-to-unify-security-insights/)
* [Davis Security Advisor extends Application Security﻿](https://www.dynatrace.com/news/blog/davis-security-advisor-extends-dynatrace-application-security/)

[Application Security FAQ](/managed/secure/faq "Часто задаваемые вопросы об Dynatrace Application Security.")

Статьи по устранению неполадок Application Security можно найти в [Dynatrace Community﻿](https://dt-url.net/dy122xtf).

## Похожие темы

* [Application Security﻿](https://www.dynatrace.com/platform/application-security/)
* [Cloud Application Security eBook﻿](https://www.dynatrace.com/resources/ebooks/cloud-application-security/)