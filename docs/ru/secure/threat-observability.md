---
title: Threat Observability
source: https://www.dynatrace.com/docs/secure/threat-observability
scraped: 2026-03-06T21:10:14.637105
---

# Threat Observability

# Threat Observability

* Latest Dynatrace
* Overview
* Updated on Mar 04, 2026

В мире, где объём данных безопасности постоянно растёт, команды DevSecOps теряются среди разрозненных инструментов и перегружены количеством оповещений. Это приводит к пропущенным угрозам и повышению рисков безопасности. Для сбора всех фрагментов воедино и принятия мер по результатам анализа требуется значительный объём ручной работы.

Dynatrace Threat Observability предлагает платформу, которая объединяет и обогащает данные безопасности контекстом среды выполнения. Это помогает устранить информационную изоляцию между различными инструментами и средами и способствует эффективному снижению рисков.

Используя Grail и DQL, вы можете единообразно потреблять результаты анализа безопасности, созданные как Dynatrace, так и сторонними инструментами, что открывает множество сценариев использования, способствующих:

* Приоритизации результатов с учётом контекста среды выполнения
* Визуализации данных безопасности и подготовке отчётов
* Автоматизации создания заявок и уведомлений
* Расследованию инцидентов безопасности и поиску угроз
* Обнаружению и устранению угроз

Благодаря широкому спектру интеграций безопасности и приёму данных через OpenPipeline, платформа наблюдаемости и безопасности Dynatrace взаимодействует с вашей экосистемой продуктов, обеспечивая более высокую ценность генерируемых данных.

Сценарии использования

Связанные публикации в блоге

### Мониторинг подозрительной активности входа с помощью Dynatrace

Анализируйте подозрительные и вредоносные действия при входе в систему с помощью Dynatrace.

* [Monitor suspicious sign-in activity with Dynatrace](/docs/secure/use-cases/monitor-sign-in-activity "Analyze suspicious and malicious sign-in behaviors with Dynatrace.")

### Автоматизация и оркестрация результатов безопасности

Регулярно проверяйте критические уязвимости контейнеров и получайте автоматические заявки Jira или оповещения Slack.

* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")

### Выявление пробелов в охвате результатов безопасности

Получите видимость проверок безопасности в течение жизненного цикла разработки ПО (SDLC).

* [Discover coverage gaps in security findings](/docs/secure/use-cases/discover-coverage-gaps-in-security-scans "Unveil blind spots in your Software Development Lifecycle (SDLC).")

### Приём и обработка пользовательских результатов безопасности

Непрерывно загружайте результаты сканирования контейнеров в Dynatrace.

* [Ingest and process custom security findings](/docs/secure/use-cases/ingest-and-process-custom-security-findings "Continuously ingest your container scan findings.")

### Контекстуализация результатов контейнеров в среде выполнения

Сортируйте критические уязвимости в рабочих приложениях на контейнерах с уязвимыми образами.

* [Runtime contextualization of container findings](/docs/secure/use-cases/runtime-contextualization-of-container-findings "Triage critical vulnerability findings in production applications on containers with vulnerable container images.")

### Визуализация и анализ результатов безопасности

Легко просматривайте и анализируйте результаты безопасности по продуктам и инструментам.

* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")

### Автоматизация уведомлений CSPM

Автоматически обрабатывайте, сортируйте, обогащайте и классифицируйте входящие оповещения безопасности.

* [CSPM Notification Automation](/docs/secure/use-cases/notification-automation "Improve cloud security posture by automatically processing, triaging, enriching, and classifying incoming security alerts.")

* [Ingest, enrich, and deduplicate Qualys vulnerability findings with Dynatrace](https://www.dynatrace.com/news/blog/ingest-enrich-and-deduplicate-qualys-vulnerability-findings-with-dynatrace/)
* [Smarter vulnerability remediation with Dynatrace and Atlassian Rovo Dev](https://www.dynatrace.com/news/blog/smarter-vulnerability-remediation-with-dynatrace-and-atlassian-rovo-dev/)
* [Smarter cloud security with Dynatrace and Kiro CLI](https://www.dynatrace.com/news/blog/smarter-cloud-security-with-dynatrace-and-kiro-cli/)
* [Ingest and enrich SonarQube security and quality findings with Dynatrace](https://www.dynatrace.com/news/blog/ingest-and-enrich-sonarqube-security-and-quality-findings-with-dynatrace/)
* [Hands-free vulnerability remediation with Dynatrace MCP server and GitHub Copilot coding agent](https://www.dynatrace.com/news/blog/dynatrace-mcp-server-and-github-copilot-coding-agent/)
* [Ingest and enrich Microsoft Sentinel security alerts with Dynatrace](https://www.dynatrace.com/news/blog/ingest-and-enrich-microsoft-sentinel-security-alerts-with-dynatrace/)
* [Ingest and enrich GitHub Advanced Security vulnerability findings with Dynatrace](https://www.dynatrace.com/news/blog/ingest-and-enrich-github-advanced-security-vulnerability-findings-with-dynatrace/)
* [Ingest and enrich Amazon GuardDuty security findings with Dynatrace](https://www.dynatrace.com/news/blog/ingest-and-enrich-amazon-guardduty-security-findings-with-dynatrace/)
* [Ingest and enrich Microsoft Defender for Cloud findings with Dynatrace](https://www.dynatrace.com/news/blog/ingest-and-enrich-microsoft-defender-for-cloud-findings-with-dynatrace/)
* [Dynatrace Investigations offers reputation analysis and context for IP addresses](https://www.dynatrace.com/news/blog/security-investigator-offers-reputation-analysis-and-context-for-ip-addresses/)
* [Threat detection in cloud native environments: Detecting suspicious Kubernetes service account behavior](https://www.dynatrace.com/news/blog/threat-detection-cloud-native-kubernetes/)
* [Threat detection in cloud native environments (part 2): How to automate threat management using workflows](https://www.dynatrace.com/news/blog/threat-detection-automate-using-workflows/)
* [Enrich observables with VirusTotal threat intelligence](https://www.dynatrace.com/news/blog/enrich-observables-with-virustotal-threat-intelligence/)
* [Enrich observables with AbuseIPDB threat intelligence](https://www.dynatrace.com/news/blog/enrich-observables-with-abuseipdb-threat-intelligence/)
* [Mastering sign-in log monitoring: How to secure user identity with Dynatrace](https://www.dynatrace.com/news/blog/sign-in-log-monitoring-secure-user-identity)
* [Ingest and enrich security findings delivered by Amazon EventBridge with Dynatrace](https://aws.amazon.com/blogs/apn/ingest-and-enrich-security-findings-delivered-by-amazon-eventbridge-with-dynatrace/)
* [Ingest and enrich Snyk vulnerability findings with Dynatrace](https://dt-url.net/6i230p7)
* [Ingest and enrich Harbor vulnerability findings with Dynatrace](https://dt-url.net/4603wzy)
* [Ingest and enrich AWS Security Hub findings with Dynatrace](https://dt-url.net/t703wux)
* [Ingest and enrich security findings delivered by Amazon EventBridge with Dynatrace](https://dt-url.net/xn03wga)
* [Enrich Tenable vulnerability findings with Dynatrace runtime context](https://dt-url.net/1023ww7)
* [Enrich Amazon ECR vulnerability findings with runtime context](https://dt-url.net/9763wjo)
* [Keep security findings at your fingertips with the Dynatrace mobile app](https://dt-url.net/x883wbh)
* [Break the silos: Enrich vulnerability findings with runtime context](https://dt-url.net/hla3weh)
* [Streamline vulnerability-risk communications with intuitive and automated security reporting](https://dt-url.net/chc3w9i)