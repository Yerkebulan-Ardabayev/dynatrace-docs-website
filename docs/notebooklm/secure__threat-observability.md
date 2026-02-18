# Документация Dynatrace: secure/threat-observability
Язык: Русский (RU)
Сгенерировано: 2026-02-18
Файлов в разделе: 2
---

## secure/threat-observability/security-events-ingest.md

---
title: Security integrations
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest
scraped: 2026-02-06T16:21:04.179783
---

# Интеграция безопасности

# Интеграция безопасности

* Последняя версия Dynatrace
* Обзор
* Обновлено 7 января 2026 г.

Dynatrace предоставляет различные способы интеграции внешних данных безопасности из нескольких сторонних продуктов в [Грааль](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") и использования ваших данных на платформе Dynatrace.

## Прием данных

Для лучшего понимания типов интеграции см. [Типы интеграции OpenPipeline для событий безопасности](/docs/secure/threat-observability/concepts#security-ingest "Basic concepts related to Threat Observability").

Ниже приведены поддерживаемые интеграции (с инструкциями).

* [Прием пользовательских событий безопасности через API](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data "Ingest security events from custom third-party products via API.")
* [Прием журналов безопасности и событий Akamai](/docs/secure/threat-observability/security-events-ingest/ingest-akamai "Ingest Akamai security logs and events into Dynatrace as security events.")
* [Получение данных об уязвимостях контейнера Amazon ECR и событий сканирования.](/docs/secure/threat-observability/security-events-ingest/ingest-aws-ecr-data "Ingest Amazon ECR container image vulnerability findings and scan events and analyze them in Dynatrace.")
* [Получение результатов безопасности Amazon GuardDuty](/docs/secure/threat-observability/security-events-ingest/ingest-amazon-guardduty "Ingest Amazon GuardDuty security findings and analyze them in Dynatrace.")
* [Получение результатов безопасности AWS Security Hub](/docs/secure/threat-observability/security-events-ingest/ingest-aws-security-hub "Ingest AWS Security Hub security findings and analyze them in Dynatrace.")
* [Прием событий безопасности и журналов аудита GitHub Advanced Security.](/docs/secure/threat-observability/security-events-ingest/ingest-github-advanced-security "Ingest GitHub Advanced Security audit logs and security events into Dynatrace as security events.")
* [Получение данных об уязвимостях, сканирований и журналов аудита Harbor](/docs/secure/threat-observability/security-events-ingest/ingest-harbor-data "Ingest Harbor vulnerability findings, scans, and audit logs into Dynatrace as security events.")
* [Прием событий Microsoft Defender для облачной безопасности](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-defender "Ingest Microsoft Defender for Cloud security events and analyze them in Dynatrace.")
* [Прием журналов входа в систему с идентификатором Microsoft Entra ID](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-entra-id "Ingest Microsoft Entra ID sign-in logs and analyze them in Dynatrace.")
* [Прием событий безопасности Microsoft Sentinel](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-sentinel "Ingest Microsoft Sentinel security events and analyze them in Dynatrace.")
* [Получение результатов уязвимостей в формате OCSF](/docs/secure/threat-observability/security-events-ingest/ingest-ocsf-data "Ingest vulnerability findings in OCSF format from any provider and analyze them on the Dynatrace platform.")
* [Получение данных об уязвимостях Qualys, событий сканирования и журналов аудита.](/docs/secure/threat-observability/security-events-ingest/ingest-qualys "Ingest Qualys vulnerability findings, scan events, and audit logs into Dynatrace as security events.")
* [Результаты соответствия Ingest Runecast Analyser](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.")
* [Получение результатов поиска уязвимостей, сканирований и журналов аудита Snyk.](/docs/secure/threat-observability/security-events-ingest/ingest-snyk-data "Ingest Snyk vulnerability findings, scans, and audit logs into Dynatrace as security events.")
* [Принимайте события безопасности и качества SonarQube, метрики и журналы аудита.](/docs/secure/threat-observability/security-events-ingest/ingest-sonarqube-data "Ingest SonarQube security and quality events, metrics, and audit logs into Dynatrace as security events.")
* [Прием событий безопасности жизненного цикла Sonatype и журналов аудита](/docs/secure/threat-observability/security-events-ingest/ingest-sonatype "Ingest Sonatype Lifecycle security events and audit logs into Dynatrace as security events.")
* [Получение результатов обнаружения уязвимостей Tenable, событий сканирования и журналов аудита.](/docs/secure/threat-observability/security-events-ingest/ingest-tenable-data "Ingest Tenable vulnerability findings, scan events, and audit logs into Dynatrace as security events.")

## Обогащение данных

Добавьте внешние данные о репутации в наблюдаемые, используя надежные источники информации об угрозах:

* [Обогатите наблюдаемые угрозы с помощью AbuseIPDB](/docs/secure/threat-observability/security-events-ingest/abuseipdb-enrich "Enrich threat observables with AbuseIPDB and analyze them in Dynatrace.")
* [Обогатите наблюдаемые угрозы с помощью VirusTotal](/docs/secure/threat-observability/security-events-ingest/virustotal-enrich "Enrich threat observables with VirusTotal and analyze them in Dynatrace.")

После настройки источников обогащения вы можете применить их к:

* Проверка наблюдаемых данных в [![Расследования](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Расследования**](/docs/secure/investigations/enhance-results#enrich «Организация и интерпретация результатов запросов в ходе расследований — от анализа производительности до обнаружения угроз».)
* Улучшите результаты обнаружения в [![Угрозы и эксплойты](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Угрозы и эксплойты**](/docs/secure/threats-and-exploits/manage-results#enrich «Фильтрация, форматирование и сортировка результатов обнаружения».)

---

## secure/threat-observability.md

---
title: Threat Observability
source: https://www.dynatrace.com/docs/secure/threat-observability
scraped: 2026-02-06T16:20:00.546819
---

# Наблюдаемость угроз

# Наблюдаемость угроз

* Последняя версия Dynatrace
* Обзор
* Обновлено 9 декабря 2025 г.

В мире, где масштабы данных о безопасности постоянно растут, команды DevSecOps теряются в разрозненных инструментах, перегруженные количеством предупреждений.Это приводит к пропущенным угрозам и повышенным рискам безопасности.Чтобы собрать все части головоломки и принять меры в соответствии с выводами безопасности, требуется много ручных усилий.

Dynatrace Threat Observability предлагает платформу, которая объединяет и дополняет данные безопасности контекстом времени выполнения.Это помогает разрушить информационную разрозненность между различными инструментами и средами и способствует эффективному снижению рисков.

Используя Grail и DQL, вы можете единообразно использовать данные безопасности, созданные Dynatrace и сторонними организациями, что позволяет использовать несколько вариантов использования, которые способствуют:

* Приоритизация результатов с учетом контекста времени выполнения.
* Визуализация данных безопасности и отчетность.
* Автоматизация создания заявок и уведомлений.
* Расследование безопасности и поиск угроз
* Обнаружение и устранение угроз.

Благодаря широкому спектру интеграции безопасности и приему OpenPipeline платформа наблюдения и безопасности Dynatrace взаимодействует с вашей экосистемой продуктов, обеспечивая более значительную ценность сгенерированных данных.

Варианты использования

Связанные блоги

### Отслеживайте подозрительную активность входа в систему с помощью Dynatrace

Анализируйте подозрительное и вредоносное поведение при входе в систему с помощью Dynatrace.

* [Отслеживайте подозрительную активность входа в систему с помощью Dynatrace](/docs/secure/use-cases/monitor-sign-in-activity "Analyze suspicious and malicious sign-in behaviors with Dynatrace.")

### Автоматизируйте и координируйте проверки безопасности

Регулярно проверяйте критические уязвимости контейнера и получайте автоматические билеты Jira или оповещения Slack.

* [Автоматизируйте и координируйте обнаружение нарушений безопасности](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")

### Обнаружение пробелов в результатах анализа безопасности

Получите представление о проверках безопасности в течение жизненного цикла разработки программного обеспечения (SDLC).

* [Обнаружение пробелов в результатах анализа безопасности](/docs/secure/use-cases/discover-coverage-gaps-in-security-scans "Unveil blind spots in your Software Development Lifecycle (SDLC).")

### Получение и обработка пользовательских результатов безопасности

Постоянно передавайте результаты сканирования контейнеров в Dynatrace.

* [Прием и обработка пользовательских результатов безопасности](/docs/secure/use-cases/ingest-and-process-custom-security-findings "Continuously ingest your container scan findings.")

### Контекстуализация результатов контейнера во время выполнения

Отсортируйте обнаруженные критические уязвимости в производственных приложениях в контейнерах с уязвимыми образами контейнеров.

* [Контекстуализация результатов контейнера во время выполнения](/docs/secure/use-cases/runtime-contextualization-of-container-findings "Triage critical vulnerability findings in production applications on containers with vulnerable container images.")

### Визуализация и анализ результатов безопасности

Легко просматривайте и анализируйте результаты безопасности различных продуктов и инструментов.

* [Визуализация и анализ результатов безопасности](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")

### Автоматизация уведомлений CSPM

Автоматически обрабатывайте, сортируйте, обогащайте и классифицируйте входящие оповещения безопасности.

* [Автоматизация уведомлений CSPM](/docs/secure/use-cases/notification-automation "Improve cloud security posture by automatically processing, triaging, enriching, and classifying incoming security alerts.")

* [Умная облачная безопасность с Dynatrace и Kiro CLIï»¿](https://www.dynatrace.com/news/blog/smarter-cloud-security-with-dynatrace-and-kiro-cli/)
* [Получайте и обогащайте данные о безопасности и качестве SonarQube с помощью Dynatraceï»¿](https://www.dynatrace.com/news/blog/ingest-and-enrich-sonarqube-security-and-quality-findings-with-dynatrace/)
* [Устранение уязвимостей без помощи рук с помощью сервера Dynatrace MCP и агента кодирования GitHub Copilot»¿](https://www.dynatrace.com/news/blog/dynatrace-mcp-server-and-github-copilot-coding-agent/)
* [Принимайте и обогащайте оповещения безопасности Microsoft Sentinel с помощью Dynatraceï»¿](https://www.dynatrace.com/news/blog/ingest-and-enrich-microsoft-sentinel-security-alerts-with-dynatrace/)
* [Получайте и обогащайте результаты поиска уязвимостей GitHub Advanced Security с помощью Dynatraceï»¿](https://www.dynatrace.com/news/blog/ingest-and-enrich-github-advanced-security-vulnerability-findings-with-dynatrace/)
* [Получайте и обогащайте результаты безопасности Amazon GuardDuty с помощью Dynatraceï»¿](https://www.dynatrace.com/news/blog/ingest-and-enrich-amazon-guardduty-security-findings-with-dynatrace/)
* [Принимайте и обогащайте результаты Microsoft Defender for Cloud с помощью Dynatraceï»¿](https://www.dynatrace.com/news/blog/ingest-and-enrich-microsoft-defender-for-cloud-findings-with-dynatrace/)
* [Dynatrace Investigations предлагает анализ репутации и контекста IP-адресов»¿](https://www.dynatrace.com/news/blog/security-investigator-offers-reputation-analysis-and-context-for-ip-addresses/)
* [Обнаружение угроз в облачных средах: обнаружение подозрительного поведения учетной записи службы Kubernetes»¿](https://www.dynatrace.com/news/blog/threat-detection-cloud-native-kubernetes/)
* [Обнаружение угроз в облачных средах (часть 2): как автоматизировать управление угрозами с помощью рабочих процессов»¿](https://www.dynatrace.com/news/blog/threat-detection-automate-using-workflows/)
* [Обогатите наблюдаемые данные информацией об угрозах VirusTotal»¿](https://www.dynatrace.com/news/blog/enrich-observables-with-virustotal-threat-intelligence/)
* [Обогатите наблюдаемые данные информацией об угрозах AbuseIPDB»¿](https://www.dynatrace.com/news/blog/enrich-observables-with-abuseipdb-threat-intelligence/)
* [Освоение мониторинга журнала входа в систему: как защитить личность пользователя с помощью Dynatrace»¿](https://www.dynatrace.com/news/blog/sign-in-log-monitoring-secure-user-identity)
* [Получайте и обогащайте результаты безопасности, полученные от Amazon EventBridge, с помощью Dynatraceï»¿](https://aws.amazon.com/blogs/apn/ingest-and-enrich-security-findings-delivered-by-amazon-eventbridge-with-dynatrace/)
* [Получайте и обогащайте данные об уязвимостях Snyk с помощью Dynatrace»¿](https://dt-url.net/6i230p7)
* [Получайте и обогащайте данные об уязвимостях Harbour с помощью Dynatrace»¿](https://dt-url.net/4603wzy)
* [Получайте и обогащайте данные AWS Security Hub с помощью Dynatraceï»¿](https://dt-url.net/t703wux)
* [Получайте и обогащайте результаты безопасности, полученные от Amazon EventBridge, с помощью Dynatraceï»¿](https://dt-url.net/xn03wga)
* [Дополните выводы Tenable об уязвимостях контекстом времени выполнения Dynatrace»¿](https://dt-url.net/1023ww7)
* [Дополните выводы об уязвимостях Amazon ECR контекстом времени выполнения»¿](https://dt-url.net/9763wjo)
* [Держите результаты безопасности под рукой с помощью мобильного приложения Dynatrace»¿](https://dt-url.net/x883wbh)
* [Разрушьте разрозненность: дополните выводы об уязвимостях контекстом времени выполнения»¿](https://dt-url.net/hla3weh)
* [Оптимизируйте обмен информацией об уязвимостях и рисках с помощью интуитивно понятных и автоматизированных отчетов о безопасности»¿](https://dt-url.net/chc3w9i)

---
