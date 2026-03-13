---
title: Investigations
source: https://www.dynatrace.com/docs/secure/investigations
scraped: 2026-03-06T21:38:04.563947
---

# Investigations

# Investigations

* Latest Dynatrace
* App
* Обновлено 09 янв. 2026

О приложении

### Что вы узнаете

* Определение и выполнение запросов с комбинированием функциональных возможностей.
* Поиск релевантной информации в логах.
* Извлечение структурированной информации из записей логов.
* Извлечение полей и получение мгновенной обратной связи по паттернам.
* Отслеживание пути, навигация к предыдущим шагам, просмотр истории расследования.
* Определение временного диапазона для запросов данных.
* Прикрепление релевантных находок в качестве доказательств с сохранением контекста расследования.
* Добавление репутационного контекста к IP-адресам с помощью [обогащения IP](/docs/secure/investigations/enhance-results#enrich "Организуйте и интерпретируйте результаты запросов в рамках расследований --- от анализа производительности до обнаружения угроз.") на основе сторонних источников разведки угроз.
* Совместная работа с коллегами над расследованиями с контролируемым доступом.
* Взаимодействие с совместимыми приложениями для получения дополнительных аналитических данных.
* Создание и использование [таблиц подстановки](/docs/secure/investigations/enhance-results#lookup "Организуйте и интерпретируйте результаты запросов в рамках расследований --- от анализа производительности до обнаружения угроз.") для обогащения расследований контекстными данными.

### Целевая аудитория

![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** поддерживает широкий спектр расследований на основе доказательств, позволяя пользователям исследовать, анализировать и решать сложные сценарии --- в области безопасности, операций, соответствия требованиям и противодействия мошенничеству.

Идеально подходит для:

* Реагирования на инциденты
* Анализа первопричин
* Поиска угроз (Threat hunting)
* Расследования мошенничества
* Цифровой криминалистики

![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** предназначено для всех, кому необходимо расследовать данные и действовать на их основе с точностью и контекстом --- включая аналитиков безопасности, SRE-инженеров, DevOps-инженеров, операционные команды, внутренних аудиторов и других специалистов.

Предварительные требования

* Для расследования загруженных логов необходимо [настроить загрузку логов](/docs/analyze-explore-automate/logs "Log Management and Analytics обеспечивает единый подход к управлению и изучению данных логов в Dynatrace.").
* Разрешения: Список необходимых разрешений доступен в **Hub**, выберите ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** и отобразите **Technical information**.
* Базовые знания

  + [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.")
  + [Dynatrace Pattern Language (DPL)](/docs/platform/grail/dynatrace-pattern-language "Используйте Dynatrace Pattern Language для описания паттернов с помощью матчеров.")

Начало работы

Сценарии использования

Дополнительные ресурсы

![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** предназначено для оптимизации расследований на основе доказательств по данным в [Grail](/docs/platform/grail "Информация о том, что и как можно запрашивать в данных Dynatrace.") --- будь то разрешение инцидентов, анализ первопричин или расследование угроз и мошенничества, благодаря

* Устранению ручных, повторяющихся задач
* Предоставлению контекстного обогащения без переключения между инструментами
* Быстрому и детальному доступу к вашим данным
* Улучшению пользовательского опыта для быстрой идентификации проблем

Приложение включает вспомогательные функции и автоматизации для ускорения и поддержки разрешения расследований, используя логи, метрики и трассировки, загруженные в Grail.

![Просматривайте весь ход расследования с возможностью вернуться к предыдущему шагу.](https://dt-cdn.net/images/investigations-01-1920-b08004a2eb.png)![Подробное представление записи показывает все поля записи одновременно; вы можете углубиться в детали поля или переключаться между записями.](https://dt-cdn.net/images/investigations-02-1920-268f03f6aa.png)![Используйте данные в результатах с точностью до символа: вы можете создавать новые доказательства или DQL-фильтры, выбирая часть поля.](https://dt-cdn.net/images/investigations-03-1920-438cb59cbe.png)![Управляйте доказательствами и фильтруйте по нескольким значениям одновременно: вы можете выбрать диапазон IP-адресов и создать DQL-фильтр на основе значений.](https://dt-cdn.net/images/investigations-04-1920-b19ac116f4.png)

1 из 4

Чтобы начать работу и создать первый сценарий расследования, откройте ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** и выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Investigation**.

Попробуйте [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Комбинируйте функциональные возможности Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.") и [поделитесь обратной связью](https://dt-url.net/qt23w3u), чтобы помочь нам улучшить продукт.

## Учебные модули

[01Выполнение запросов

* Практическое руководство
* Запускайте расследования с использованием Dynatrace Query Language в Investigations.](/docs/secure/investigations/execute-queries)[02Фильтрация логов

* Практическое руководство
* Сужайте данные до релевантных записей в Investigations.](/docs/secure/investigations/filter-logs)[03Извлечение полей с помощью DPL Architect

* Практическое руководство
* Извлекайте определенные точки данных из логов в Investigations.](/docs/secure/investigations/extract-fields)[04Управление временем

* Практическое руководство
* Настраивайте временные диапазоны для анализа данных и корреляции событий в Investigations.](/docs/secure/investigations/define-timeframes)[05Управление результатами

* Практическое руководство
* Организуйте и интерпретируйте результаты запросов в рамках расследований --- от анализа производительности до обнаружения угроз.](/docs/secure/investigations/enhance-results)[06Управление деревом запросов

* Практическое руководство
* Визуализируйте и структурируйте сложные запросы в Investigations.](/docs/secure/investigations/query-tree)[07Управление доказательствами

* Практическое руководство
* Собирайте и сохраняйте артефакты расследования в Investigations.](/docs/secure/investigations/manage-evidence)[08Управление расследованиями

* Практическое руководство
* Делитесь, дублируйте и контролируйте доступ к расследованиям между командами в Dynatrace Investigations.](/docs/secure/investigations/case-sharing)[09Управление шаблонами

* Практическое руководство
* Повторно используйте типовые запросы и рабочие процессы в Investigations.](/docs/secure/investigations/manage-templates)[10Ускорение анализа первопричин

* Практическое руководство
* Выявляйте причины быстрее и эффективнее в Investigations.](/docs/secure/investigations/accelerate-root-cause-analysis)[11Совместная работа с другими приложениями

* Практическое руководство
* Делитесь аналитическими данными и интегрируйте Investigations с другими приложениями и инструментами Dynatrace для более глубокого анализа.](/docs/secure/investigations/collaborate-with-apps)

### Поиск угроз и криминалистика

Поиск индикаторов компрометации (IoC) и проведение криминалистических расследований и мероприятий по поиску угроз.

* [Поиск угроз и криминалистика](/docs/secure/use-cases/threat-hunting "Сценарий использования для поиска угроз и криминалистики с Investigations.")

### Быстрое разрешение инцидентов с помощью шаблонов

Ускорьте расследования, связанные с логами, с помощью шаблонов ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**.

* [Быстрое разрешение инцидентов с помощью шаблонов Investigations](/docs/secure/use-cases/resolve-incidents-faster-with-templates "Ускорьте расследования, связанные с логами, с помощью шаблонов Investigations.")

### Ускорение реагирования на инциденты с помощью опорного времени

Улучшите расследования, связанные с логами, с помощью опорного времени ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**.

* [Ускорение реагирования на инциденты с помощью опорного времени Dynatrace Investigations](/docs/secure/use-cases/speed-up-incident-response-with-reference-time "Улучшите расследования, связанные с логами, с помощью опорного времени Dynatrace Investigations.")

### Операционализация результатов DQL-запросов

Создавайте DQL-запросы на основе результатов ваших запросов быстрее и удобнее с помощью ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**.

* [Операционализация результатов DQL-запросов с помощью Investigations](/docs/secure/use-cases/operationalize-query-results "Создавайте DQL-запросы на основе результатов ваших запросов быстрее и удобнее с помощью Dynatrace Investigations.")

### Анализ логов AWS CloudTrail

Анализируйте логи CloudTrail и находите потенциальные проблемы безопасности с помощью ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**.

* [Анализ логов AWS CloudTrail с помощью Investigations](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Анализируйте логи CloudTrail и находите потенциальные проблемы безопасности с помощью Dynatrace.")

### Анализ логов доступа Amazon API Gateway

Мониторинг и выявление ошибок в логах доступа Amazon API Gateway с помощью ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**.

* [Анализ логов доступа Amazon API Gateway с помощью Investigations](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Мониторинг и выявление ошибок в логах доступа Amazon API Gateway с помощью Dynatrace.")

### Обнаружение угроз для ваших AWS Secrets

Мониторинг и выявление потенциальных угроз для ваших AWS Secrets с помощью ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**.

* [Обнаружение угроз для ваших AWS Secrets с помощью Investigations](/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator "Мониторинг и выявление потенциальных угроз для ваших AWS Secrets с помощью Dynatrace.")

Ознакомьтесь с наиболее релевантными темами для начала работы с ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**.

Видео

Блоги

Учебные курсы Dynatrace University

Статьи сообщества Dynatrace

Видео

Блоги

Учебные курсы Dynatrace University

Статьи сообщества Dynatrace

* Предварительный обзор Dynatrace ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**:

  Dynatrace Investigations
* Криминалистика наблюдаемости: Поиск неизвестного в логах, метриках и трассировках:

  Finding the Unknown in Logs, Metrics, and Traces
* Подробнее о DPL Architect:

  Additional insights into DPL Architect
* Повышение уровня безопасности с Dynatrace ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**:

  Elevating Security with Dynatrace Anomaly Detection

* [От реагирования на инциденты до повседневной аналитики: представляем Dynatrace Investigations](https://www.dynatrace.com/news/blog/from-incident-response-to-everyday-analytics-introducing-dynatrace-investigations/)
* [Улучшенное реагирование на инциденты на основе анализа метрик производительности](https://www.dynatrace.com/news/blog/enhanced-incident-response-based-on-performance-metric-insights/)
* [Революция в облачной безопасности с контекстом наблюдаемости: Dynatrace Cloud Security для CADR](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Dynatrace Investigations предлагает репутационный анализ и контекст для IP-адресов](https://www.dynatrace.com/news/blog/security-investigator-offers-reputation-analysis-and-context-for-ip-addresses/)
* [Обнаружение угроз в облачных средах: выявление подозрительного поведения сервисных аккаунтов Kubernetes](https://www.dynatrace.com/news/blog/threat-detection-cloud-native-kubernetes/)
* [Возвращаясь к Spring4Shell: как Cloud Application Detection and Response (CADR) обеспечивает многоуровневую защиту](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [Ускорьте расследования безопасности на основе доказательств и поиск угроз с Dynatrace Investigations](https://dt-url.net/96038pf)
* [Ускорьте расследования безопасности с DPL Architect](https://dt-url.net/mn0380l)
* [Совместная работа с коллегами при поиске угроз безопасности](https://dt-url.net/pa03x82)
* [Дублирование расследований: новый уровень продуктивности и эффективности Dynatrace Investigations](https://dt-url.net/ij03w5y)
* [Сокращение времени реагирования на инциденты с помощью шаблонов расследований](https://dt-url.net/k723ws9)
* [Создание контекста в Dynatrace Investigations с помощью опорного времени](https://www.dynatrace.com/news/blog/create-context-in-security-investigator-with-reference-times)
* [Изменение перспективы ваших исследовательских запросов с Dynatrace Investigations](https://www.dynatrace.com/news/blog/pivot-the-perspective-of-your-investigative-queries-with-security-investigator/)
* [Генерация событий безопасности из Dynatrace Investigations через OpenPipeline](https://dt-url.net/r703qjx)
* [Контекстно-зависимое реагирование на инциденты безопасности с Dynatrace Automations и Tetragon](https://dt-url.net/he03pmt)

* [Dynatrace Investigations - Руководство практика](https://university.dynatrace.com/learn/courses/90/security-analytics/lessons/283/security-investigator)
* [Dynatrace Investigations - Изучение расследования](https://university.dynatrace.com/learn/courses/87/case-studies/lessons/476/security-investigator-explore-a-case)

* [Совет профессионала: Четыре вещи, которые вы не знали о Dynatrace Investigations](https://dt-url.net/wb03w5n)
* [Как быстрее создавать DQL-фильтры в Dynatrace Investigations](https://dt-url.net/lr03wrx)
* [Рождественский практикум: Кто украл секретный файл Санты?](https://dt-url.net/zo23wum)
* [Практикум ко Дню святого Валентина: Сбой сердцебиения](https://dt-url.net/5t03wkk)

## Связанные темы

* [Поиск угроз и криминалистика](/docs/secure/use-cases/threat-hunting "Сценарий использования для поиска угроз и криминалистики с Investigations.")
* [DPL Architect](/docs/platform/grail/dynatrace-pattern-language/dpl-architect "Извлечение полей с помощью Dynatrace Pattern Language Architect.")
* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь аналитическими данными наблюдаемости --- в едином совместном настраиваемом рабочем пространстве.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.")
* [Использование DQL-запросов](/docs/platform/grail/dynatrace-query-language/dql-guide "Узнайте, как работает DQL и каковы ключевые концепции DQL.")
* [Команды DQL](/docs/platform/grail/dynatrace-query-language/commands "Список команд DQL.")
* [Функции DQL](/docs/platform/grail/dynatrace-query-language/functions "Список функций DQL.")
* [Операторы DQL](/docs/platform/grail/dynatrace-query-language/operators "Список операторов DQL.")
* [Типы данных DQL](/docs/platform/grail/dynatrace-query-language/data-types "Список типов данных DQL.")
* [Функции преобразования и приведения типов](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions "Список функций преобразования и приведения типов DQL.")
* [Команды выборки и модификации DQL](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands "Команды выборки и модификации DQL")
