---
title: Уязвимости
source: https://www.dynatrace.com/docs/secure/vulnerabilities
scraped: 2026-03-06T21:34:35.874049
---

* Latest Dynatrace

О приложении

### Что вы узнаете

* Фильтрация, форматирование и сортировка для поиска релевантной информации об уязвимостях.
* Приоритизация уязвимостей на основе Dynatrace Security Score, оценки Dynatrace, затронутых и связанных сущностей, исторического контекста, каталога CISA KEV.
* Применение исправлений, отслеживание устранения, углублённый анализ источника уязвимостей, изменение статуса отключения для затронутых сущностей.
* Взаимодействие с другими приложениями и скачивание результатов для совместного использования.
* Получение аналитики по охвату мониторинга и тенденциям воздействия с помощью панели мониторинга **Vulnerability coverage**.

### Целевая аудитория

![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** предназначено для инженеров DevSecOps.

Предварительные требования

* Ознакомьтесь с [поддерживаемыми технологиями](application-security.md#rva-tech "Получите доступ к функциям Dynatrace Application Security.").
* [Настройте Dynatrace Runtime Vulnerability Analytics](application-security/vulnerability-analytics.md#start "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и уровня кода, отслеживание прогресса устранения и создание правил мониторинга.").

Разрешения

Пользователь-администратор должен назначить следующие политики IAM группе пользователей, которые будут иметь доступ к [`vulnerability-service`](../manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements.md#vulnerability-service "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace."):

* `Read Entities`
* `Read Security Events`
* Одна из следующих пользовательских политик: `Admin User`, `Pro User`, `Standard User` (подробнее см. Стандартные политики).

Инструкции приведены ниже.

1. Создайте группу

1. В **Account Management** выберите **Identity & access management** > **Group management**.
2. Нажмите **Group**, чтобы создать группу.

   ![Добавление группы](https://dt-cdn.net/images/2024-12-05-15-57-23-1895-68ceeae80a.png)
3. Введите имя (например, `vulnerability-service`) и описание (например, `vulnerability-service group`), затем нажмите **Create**.

2. Назначьте политики группе

После создания группы вы можете просматривать подробную информацию и назначать политики.

1. Нажмите **Permission**.

   ![Назначение политик](https://dt-cdn.net/images/2024-12-05-14-52-36-1902-2b2ef3db6a.png)
2. В раскрывающемся меню **Permission name** выберите и сохраните три необходимые политики, по одной за раз.

После добавления три политики должны отображаться в вашем списке разрешений.

![Необходимые политики](https://dt-cdn.net/images/2024-12-09-19-34-41-1908-a1b779b33e.png)

3. Добавьте пользователей в группу

1. В **Account Management** выберите **Identity & access management** > **People**.
2. Нажмите **Invite user**, чтобы пригласить пользователей в новую группу.

Подробнее о политиках IAM см. Работа с политиками.

Начало работы

Связанные блоги

![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** обнаруживает, используют ли приложения в вашей среде Dynatrace уязвимые библиотеки во время выполнения или уязвимую среду выполнения для исполнения вашего кода. Приложение помогает определять приоритеты на основе контекста и воздействия, эффективно планируя действия по устранению.

Для дополнительной информации об охвате мониторинга и воздействии см. Оценка охвата.

![Таблица результатов уязвимостей на странице приоритизации](https://dt-cdn.net/images/one-1920-3b90d3d40b.png)![Подробности уязвимости](https://dt-cdn.net/images/two-1920-2dec9771f5.png)![Обзор группы процессов, связанной с уязвимостью](https://dt-cdn.net/images/three-1920-6b45726007.png)![Подробности затронутой группы процессов](https://dt-cdn.net/images/four-1920-f0bf314049.png)![Страница обзора результатов](https://dt-cdn.net/images/2025-12-17-14-29-30-1920-06cddbfea0.png)![Подробности результата](https://dt-cdn.net/images/2025-12-17-14-37-49-1920-1ecd920899.png)

1 из 6

Попробуйте ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** и [поделитесь отзывом](https://dt-url.net/up03ph5), чтобы помочь нам улучшить приложение.

## Учебные модули

[01Концепции Vulnerabilities

* Объяснение
* Концепции, специфичные для приложения Dynatrace Vulnerabilities.](vulnerabilities/concepts.md)02Управление результатами

* Фильтрация, форматирование и сортировка для поиска релевантной информации об уязвимостях.[03Устранение уязвимостей

* Устранение уязвимостей и оптимизация действий по устранению.](vulnerabilities/address-remediation.md)[04Приоритизация уязвимостей

* Приоритизация уязвимостей сторонних компонентов, уровня кода и среды выполнения.](vulnerabilities/prioritize.md)[05Изучение результатов

* Просмотр, фильтрация и анализ результатов обнаружения уязвимостей из Dynatrace и внешних инструментов безопасности.](vulnerabilities/explore-findings.md)[06Оценка охвата

* Объяснение
* Оцените процесс RVA и охват хостов в вашей среде с помощью панели мониторинга Vulnerability coverage.](vulnerabilities/assess-coverage.md)[07Интеграция аналитики уязвимостей с приложениями Dynatrace и внешними приложениями

* Навигация между приложениями Dynatrace, обмен данными об уязвимостях с внешними системами и автоматизация рабочих процессов устранения.](vulnerabilities/collaborate-with-apps.md)

* [Introducing the Dynatrace Vulnerability feed: Accurate, transparent, and threat-aware](https://www.dynatrace.com/news/blog/introducing-the-dynatrace-vulnerability-feed-accurate-transparent-and-threat-aware/)
* [Introducing findings in the Vulnerabilities app: Unified, granular insights for smarter security](https://www.dynatrace.com/news/blog/introducing-findings-in-the-vulnerabilities-app-unified-granular-insights-for-smarter-security/)
* [CVE-2025-55182: React2Shell Critical Vulnerability — what it is and what to do](https://www.dynatrace.com/news/blog/cve-2025-55182-react2shell-critical-vulnerability-what-it-is-and-what-to-do/)
* [Supply chain security: How to detect malicious software packages with Dynatrace](https://www.dynatrace.com/news/blog/supply-chain-security-how-to-detect-malicious-software-packages-with-dynatrace/)
* [Prioritize vulnerabilities based on the CISA Known Exploited Vulnerabilities Catalog](https://www.dynatrace.com/news/blog/prioritize-vulnerabilities-based-on-the-cisa-known-exploited-vulnerabilities-catalog/)
* [Revolutionizing cloud security with observability context: Dynatrace Cloud Security addressing CADR](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Empowering SREs with runtime vulnerability analytics and security posture management](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Dynatrace launches Python Vulnerability Monitoring for enhanced customer security](https://www.dynatrace.com/news/blog/dynatrace-launches-python-vulnerability-monitoring-for-enhanced-customer-security/)
* [Snyk integration for Dynatrace: Bridging development and runtime with actionable security notifications](https://www.dynatrace.com/news/blog/snyk-dynatrace-integration-actionable-notifications/)
* [Revisiting Spring4Shell: How Cloud Application Detection and Response (CADR) offers multi-layer protection](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [Discover the new Dynatrace Runtime Vulnerability Analytics experience](https://www.dynatrace.com/news/blog/discover-the-new-dynatrace-runtime-vulnerability-analytics-experience/)
* [The anatomy of broken Apache Struts 2: A technical deep dive into CVE-2024-53677](https://www.dynatrace.com/news/blog/the-anatomy-of-broken-apache-struts-2-a-technical-deep-dive-into-cve-2024-53677/)
