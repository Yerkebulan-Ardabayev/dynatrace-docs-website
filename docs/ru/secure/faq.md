---
title: Часто задаваемые вопросы по Application Security
source: https://www.dynatrace.com/docs/secure/faq
scraped: 2026-03-06T21:17:07.976353
---

# Часто задаваемые вопросы по Application Security


* Latest Dynatrace
* Troubleshooting
* Обновлено 23 февраля 2026 г.

Ниже вы найдёте ответы на наиболее часто задаваемые вопросы о Dynatrace Application Security, сгруппированные по темам.

Статьи по устранению неполадок, связанных с Application Security, доступны в [сообществе Dynatrace](https://dt-url.net/dy122xtf).

## Обнаружение и мониторинг

### Как я могу обнаружить риски безопасности в своих приложениях?

Latest Dynatrace

Вы можете обнаруживать, анализировать и понимать риски безопасности в своих приложениях с помощью нескольких приложений безопасности Dynatrace:

* Выявляйте, приоритизируйте и отслеживайте уязвимости в сторонних библиотеках, средах выполнения приложений и пользовательском коде в производственных и предпроизводственных средах с помощью [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](vulnerabilities.md "Prioritize and efficiently manage vulnerabilities in your monitored environments.").
* Исследуйте, сортируйте и принимайте меры по результатам обнаружения в реальном времени и оповещениям, затрагивающим ваши приложения, с помощью [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](threats-and-exploits.md "Understand, triage, and investigate detection findings and alerts.").
* Изучайте данные безопасности, выполняйте DQL-запросы, извлекайте поля и проводите более глубокие расследования по журналам, метрикам и трассировкам с помощью [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").

deprecated

* Для обнаружения и мониторинга сторонних уязвимостей [включите обнаружение сторонних уязвимостей](application-security/vulnerability-analytics.md#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."), затем перейдите в [![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**](application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities.md "Monitor the security issues of your third-party libraries.").
* Для единого представления сторонних и уязвимостей уровня кода и информации о покрытии хостов [включите Runtime Vulnerability Analytics](application-security/vulnerability-analytics.md "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."), затем перейдите в [![Security Overview](https://dt-cdn.net/images/security-overview-512-a310b17025.png "Security Overview") **Security Overview**](application-security/vulnerability-analytics/application-security-overview.md "Get an overview of the security issues of your third-party libraries.").

### В чём разница между классическими правилами мониторинга и новыми?

[Новые правила мониторинга](application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv.md#new "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.") позволяют включать или исключать процессы, узлы Kubernetes и хосты на основе атрибутов ресурсов и меток Kubernetes. Этот подход более гибкий и точный, хорошо работает в динамичных и облачно-нативных средах и поддерживает предварительный просмотр, позволяя проверить, какие объекты соответствуют правилам, до их включения. Эти правила рекомендуются и являются стандартными для более новых сред.

[Классические правила мониторинга](application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv.md#classic "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.") основаны на тегах групп процессов, тегах хостов и Management Zone. Они обеспечивают меньшую гранулярность, зависят от правильной расстановки тегов и не предоставляют такого же уровня предварительного просмотра или контроля. Классические правила по-прежнему работают, но запланированы к устареванию и не могут использоваться одновременно с новыми правилами.

### Как работают RVA и RAP?

* Сведения о механизме Runtime Vulnerability Analytics (RVA) см. в разделе [Как работает RVA](application-security/vulnerability-analytics.md#mechanism "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
* Сведения о механизме Runtime Application Protection (RAP) см. в разделе [Как работает RAP](application-security/application-protection.md#mechanism "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.").

### Каково влияние включения Application Security?

***Что следует учитывать перед включением Application Security? Может ли это на что-то повлиять?***

При включении Application Security (Runtime Vulnerability Analytics или Runtime Application Protection) учитывайте следующее:

* **Потребление**:
  **Runtime Vulnerability Analytics и Runtime Application Protection** потребляют [ГиБ-часы](../license/capabilities/application-security.md "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.") при использовании [модели лицензирования Dynatrace Platform Subscription (DPS)](../license.md "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") или [единицы Application Security (ASU)](../license/monitoring-consumption-classic/application-security-units.md "Understand how Dynatrace Application Security and Runecast SPM consumption are calculated.") при использовании [классического лицензирования Dynatrace](../license/monitoring-consumption-classic.md "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").
* **Использование сетевой полосы пропускания**:

  + **Обнаружение уязвимостей уровня кода и обнаружение атак**: ожидайте небольшого увеличения использования сети в зависимости от количества отслеживаемых приложений. В большинстве случаев эти накладные расходы незначительны.
  + **Обнаружение сторонних уязвимостей**: дополнительные накладные расходы на процессы не вводятся.

### Как отключить мониторинг безопасности?

* Для отключения Runtime Vulnerability Analytics

  1. Перейдите в **Settings** > **Analyze and alert** > **General settings**.
  2. В разделе **Third-party Vulnerability Analytics** отключите **Enable Third-party Vulnerability Analytics**.
  3. В разделе **Code-level Vulnerability Analytics** отключите **Enable Code-level Vulnerability Analytics**.
* Для отключения Runtime Application Protection

  1. Перейдите в **Settings** > **Analyze and alert** > **Application security** > **Application protection (New)**.
  2. Отключите Runtime Application Protection.

### Можно ли вручную запустить проверку безопасности?

***Выполняет ли Application Security запланированные задания? Каков интервал расписания? Можно ли вручную запустить проверку безопасности после развёртывания изменений в среде?***

Плановых проверок нет. После включения любых функций Dynatrace Application Security ваша среда автоматически непрерывно отслеживается в реальном времени на предмет выбранных функций.

## Ограничение разрешений

### Как предоставить кому-либо доступ только для просмотра уязвимостей?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

Чтобы ограничить определённых пользователей доступом только для просмотра (они могут смотреть уязвимости, но не управлять ими), см. раздел [Настройка доступа](application-security/vulnerability-analytics.md#restrict-permissions "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

## Устранение

### Устраняет ли Dynatrace уязвимости?

***Исправит ли Dynatrace уязвимости, или мне нужно самому предпринять действия для их исправления?***

Dynatrace не устраняет уязвимости. Он выявляет и отслеживает уязвимости в приложениях в производственных и предпроизводственных средах и помогает определить первопричину, предоставляя богатый контекст и информацию, которая помогает вам принять соответствующие меры. Дополнительные сведения о возможностях см. в:

* [Runtime Vulnerability Analytics: Возможности](application-security/vulnerability-analytics.md "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* Latest Dynatrace [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](vulnerabilities.md "Prioritize and efficiently manage vulnerabilities in your monitored environments.")

После устранения первопричины уязвимость устраняется автоматически. Дополнительные сведения об устранении уязвимостей см. в:

* [Сторонние уязвимости: Устранение](application-security/vulnerability-analytics/vulnerability-evaluation.md#tpv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.")
* [Уязвимости уровня кода: Устранение](application-security/vulnerability-analytics/vulnerability-evaluation.md#clv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.")

### Как исправить обнаруженные уязвимости?

Богатый и точный контекст и детали, представленные на страницах уязвимостей, помогают вам выявлять и понимать уязвимости, расставлять приоритеты по степени риска и автоматически отслеживать и оповещать о вновь обнаруженных уязвимостях. На основе этой информации вы можете определить, какие действия необходимы для исправления уязвимостей.

Например:

Latest Dynatrace

В [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](vulnerabilities.md "Prioritize and efficiently manage vulnerabilities in your monitored environments.") вы можете:

* [Применить рекомендации по исправлению от Snyk](vulnerabilities/address-remediation.md#snyk "Address remediation and optimize remediation activities.")
* [Применить исправления DSA](vulnerabilities/address-remediation.md#dsa "Address remediation and optimize remediation activities.")
* [Подключить затронутые объекты к системе отслеживания задач и следить за ходом исправления](vulnerabilities/address-remediation.md#remediation-tracking "Address remediation and optimize remediation activities.")
* [Перейти к источнику уязвимостей](vulnerabilities/address-remediation.md#source "Address remediation and optimize remediation activities.")
* [Изменить статус отключения затронутых объектов](vulnerabilities/address-remediation.md#mute-entities "Address remediation and optimize remediation activities.")

deprecated

В [![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**](application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities.md "Monitor the security issues of your third-party libraries.") вы можете:

* Использовать рекомендованные [исправления DSA](application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor.md "Get recommendations for security fixes from Davis Security Advisor.") для обновления до не уязвимой версии уязвимого компонента
* [Настроить ссылки для отслеживания затронутых объектов и следить за ходом их исправления](application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md "Track the remediation progress of vulnerabilities.")

### Когда уязвимость помечается как устранённая?

***Я удалил уязвимый компонент, но уязвимость всё равно отображается как открытая. Когда она будет устранена?***

Уязвимость помечается как `Resolved` при следующих условиях:

* Ни одна группа процессов или узел Kubernetes не сообщали об уязвимых компонентах более двух часов.
* Первопричина уязвимости больше не присутствует; например, уязвимый компонент был удалён или затронутый процесс был завершён.

  Это условие применяется независимо от того, сколько времени прошло с момента последнего отчёта.

### Почему моя уязвимость всё ещё открыта, если затронутой группы процессов больше нет?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

Уязвимость по-прежнему отображается, если она присутствует в других Management Zone. Чтобы увидеть затронутые группы процессов, выберите `All` в фильтре Management Zone.

### Может ли уязвимость быть устранена при наличии затронутых объектов?

Нет. Уязвимость считается устранённой, если затронутых объектов больше нет.

### Почему некоторые уязвимости устраняются без каких-либо мер с нашей стороны?

***После включения Runtime Vulnerability Analytics было обнаружено 19 критических уязвимостей. Теперь их осталось три — без каких-либо мер с нашей стороны. Почему некоторые уязвимости устраняются без принятия мер?***

Уязвимость устраняется автоматически, если первопричина больше не присутствует. Дополнительные сведения см. в:

* [Устранение сторонних уязвимостей](application-security/vulnerability-analytics/vulnerability-evaluation.md#tpv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.")
* [Устранение уязвимостей уровня кода](application-security/vulnerability-analytics/vulnerability-evaluation.md#clv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.")

### Почему некоторые уязвимости постоянно устраняются и открываются снова?

Уязвимость постоянно устраняется и открывается снова, когда процесс, использующий уязвимую библиотеку, работает не постоянно:

* Когда процесс завершается, уязвимость устраняется.
* Когда процесс перезапускается, уязвимость открывается снова.

Подробнее о причинах устранения и повторного открытия уязвимостей см. в разделе [Устранение](application-security/vulnerability-analytics/vulnerability-evaluation.md#tpv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.").

Чтобы определить, какие процессы затронуты, см.:

* Latest Dynatrace [Что под угрозой (затронутые и связанные объекты)](vulnerabilities/prioritize.md#affected-related "Prioritize third-party, code-level, and runtime vulnerabilities.")
* deprecated [Отслеживание исправления для процессов](application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md#process "Track the remediation progress of vulnerabilities.").

### Почему устранённые уязвимости отображаются в каждой Management Zone?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

Информация о Management Zone не привязана непосредственно к уязвимости. Она берётся от уязвимых объектов, затронутых соответствующей уязвимостью: процесс в Management Zone, использующий уязвимую библиотеку, вызывает стороннюю уязвимость в соответствующей Management Zone.

Уязвимость считается устранённой, если уязвимых объектов больше нет. В списке уязвимостей все отображаемые устранённые уязвимости больше не фильтруются по Management Zone, так как эта информация к ним не привязана.

### Почему для устранённых уязвимостей в моей Management Zone показывается ноль устранённых групп процессов?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

***Для устранённых уязвимостей мне хотелось бы изучить устранённые группы процессов, чтобы понять, какие объекты были затронуты ранее, но в моей Management Zone отображается ноль устранённых групп процессов. Почему?***

На страницах уязвимостей в разделе **Process group overview**, если для устранённой уязвимости в вашей Management Zone отображается ноль устранённых групп процессов, это означает, что ни один из ранее затронутых и устранённых объектов не находится в этой Management Zone. Чтобы найти соответствующие объекты, переключите фильтр Management Zone на `All`.

## Требуется перезапуск

### Требуется ли перезапуск после включения или отключения функции или возможности Application Security?

Ниже приведены требования к перезапуску по функциям.

* **Сторонние уязвимости**: перезапуск процесса приложения требуется в следующем случае:

  + В [**Discovery mode**](../platform/oneagent/monitoring-modes/monitoring-modes.md#discovery "Find out more about the available monitoring modes when using OneAgent.") после [включения внедрения модуля кода](../platform/oneagent/monitoring-modes/monitoring-modes.md#code-module-injection "Find out more about the available monitoring modes when using OneAgent.")
* **Уязвимости уровня кода**: перезапуск процесса приложения требуется в следующих случаях:

  + После каждого шага в [Включение обнаружения уязвимостей уровня кода](application-security/vulnerability-analytics.md#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."):

    - Включить Code-level Vulnerability Analytics
    - Настроить глобальный контроль обнаружения уязвимостей уровня кода для каждой технологии
    - Включить мониторинг OneAgent
  + После включения [правила мониторинга](application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv.md "Define rules based on specific process groups")
* **Атаки**: перезапуск процесса приложения требуется в следующих случаях:

  + После каждого шага в [Начало работы с Runtime Application Protection](application-security/application-protection.md#start "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities."):

    - Включить Runtime Application Protection
    - Определить глобальный контроль атак для каждой технологии
    - Включить мониторинг OneAgent
  + После включения [правила мониторинга](application-security/application-protection/application-protection-rules.md "Create, modify, and delete rules for specific attacks.")

### Почему на некоторых страницах Application Security отображается уведомление «Требуется перезапуск»?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

OneAgent version 1.279+

См. раздел [Как я могу узнать, что информация об уязвимых функциях устарела, и что с этим делать?](#outdated-vulnerable-functions).

## Уведомления и отчётность

### Как получать уведомления об уязвимостях?

Latest Dynatrace

Вы можете [настроить рабочий процесс](../analyze-explore-automate/workflows/simple-workflow.md "Build and run a simple workflow."), чтобы Dynatrace отправлял уведомления о [уязвимостях и результатах анализа уязвимостей](vulnerabilities.md "Prioritize and efficiently manage vulnerabilities in your monitored environments.") через предпочтительные [каналы](../analyze-explore-automate/workflows/actions.md "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems."). Параметры конфигурации дают вам точный контроль над тем, когда и как срабатывают уведомления.

* Примеры настройки рабочего процесса см. в разделе [Варианты использования Workflows](../analyze-explore-automate/workflows/use-cases.md "Explore common Workflows use cases in Dynatrace deployments.").

deprecated

Вы можете [настроить уведомления](application-security/vulnerability-analytics/security-notifications-rva.md "Integrate security notifications for vulnerabilities with Dynatrace.") через предпочтительные каналы.

* Например, вы можете настроить оповещения

  + При повторном открытии уязвимости (**Vulnerability (re)opened**)
  + Когда новая группа процессов в Management Zone затрагивается уязвимостью (**New Management zone affected**)

### Как получать уведомления об атаках?

Latest Dynatrace

Вы можете [настроить рабочий процесс](../analyze-explore-automate/workflows/simple-workflow.md "Build and run a simple workflow."), чтобы Dynatrace отправлял уведомления о [результатах обнаружения](threats-and-exploits.md "Understand, triage, and investigate detection findings and alerts.") через предпочтительные [каналы](../analyze-explore-automate/workflows/actions.md "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems."). Параметры конфигурации дают вам точный контроль над тем, когда и как срабатывают уведомления.

* Примеры настройки рабочего процесса см. в разделе [Варианты использования Workflows](../analyze-explore-automate/workflows/use-cases.md "Explore common Workflows use cases in Dynatrace deployments.").

### Как создавать отчёты и делиться ими с другими?

Latest Dynatrace

* В [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](vulnerabilities.md "Prioritize and efficiently manage vulnerabilities in your monitored environments.") вы можете:

  + [Скачать данные об уязвимостях в виде CSV-файла](vulnerabilities/collaborate-with-apps.md#dwld "Navigate between Dynatrace apps, share vulnerability data externally, and automate remediation workflows.")
  + [Скачать данные о результатах анализа уязвимостей в виде CSV-файла](vulnerabilities/explore-findings.md#collaborate "View, filter, and analyze vulnerability findings from Dynatrace and external security tools.")
* В [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](threats-and-exploits.md "Understand, triage, and investigate detection findings and alerts.") вы можете [скачать данные о результатах обнаружения в виде CSV-файла](threats-and-exploits/collaborate-with-apps.md#download "Interact with other apps for further insights and share results with stakeholders.").
* В [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability data—all in one collaborative, customizable workspace.") вы можете создавать отчёты о [событиях безопасности](threat-observability/concepts.md#security-events "Basic concepts related to Threat Observability") с помощью [Dynatrace Query Language (DQL)](../platform/grail/dynatrace-query-language.md "How to use Dynatrace Query Language."), а затем создавать [информационные панели](../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") на основе результатов.

  + Часто используемые запросы см. в разделе [Примеры DQL для данных безопасности](threat-observability/dql-examples.md#vulnerabilities-per-application "DQL examples for security data powered by Grail.").
  + Полный список запрашиваемых полей с описаниями и примерами см. в разделе [Dynatrace Semantic Dictionary: события безопасности](../semantic-dictionary/model/security-events.md "Get to know the Semantic Dictionary models related to security events.").

deprecated

* С помощью Dynatrace API вы можете строить графики [метрик Application Security](application-security/vulnerability-analytics/app-sec-metrics.md "View available Application Security metrics for Dynatrace Runtime Vulnerability Analytics.") и [прикреплять их к информационной панели](../analyze-explore-automate/dashboards-classic/metrics-browser.md#pin "Browse metrics with the Dynatrace metrics browser."). Например, вы можете получить [все проблемы безопасности, обнаруженные в ваших приложениях](../dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerabilities.md "View the list of vulnerabilities via Dynatrace API.") или [уязвимые функции проблемы безопасности](../dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerable-functions.md "View the vulnerable functions of a vulnerability via Dynatrace API.").
* С помощью [Data Explorer](../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") вы можете [поделиться результатами метрик](../analyze-explore-automate/explorer.md#share "Query for metrics and transform results to gain desired insights.") и [экспортировать их в CSV-файл](../analyze-explore-automate/explorer.md#csv "Query for metrics and transform results to gain desired insights.").

### Как прекратить получать уведомления о нерелевантной уязвимости или объекте?

Если вы считаете, что уязвимость или объект нерелевантны или являются ложным срабатыванием, вы можете:

Latest Dynatrace

Отключить (заглушить) все её затронутые объекты. Это устанавливает статус уязвимости на `Muted`. Инструкции см. в разделе [Изменение статуса затронутого объекта](vulnerabilities/address-remediation.md#mute-entities "Address remediation and optimize remediation activities.").

deprecated

* Отключить (заглушить) уязвимость. Подробнее см. в разделе [Изменение статуса сторонней уязвимости](application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities.md#mute "Organize third-party vulnerabilities for easy management and to prioritize issues.").
* Отключить (заглушить) объект. Подробнее см. в разделах [Изменение статуса уязвимости для групп процессов](application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md#status-pg "Track the remediation progress of vulnerabilities.") и [Изменение статуса уязвимости для узлов](application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md#status-node "Track the remediation progress of vulnerabilities.").

### Почему мы продолжаем получать уведомления об одной и той же уязвимости?

***Каждый день мы получаем уведомления об одном и том же идентификаторе уязвимости, с одной и той же группой процессов, именем объекта и ссылкой на объект. У нас есть другие обнаруженные уязвимости, но дополнительных уведомлений не отправляется. Почему мы продолжаем получать уведомления об одной и той же уязвимости?***

Процесс, работающий не постоянно, может использовать уязвимую библиотеку. Подробнее см. в разделе [Почему некоторые уязвимости постоянно устраняются и открываются снова?](#reopen).
Чтобы прекратить получать уведомления об этой уязвимости, вы можете:

* Исключить соответствующий процесс из мониторинга Application Security, настроив [правило мониторинга сторонних уязвимостей](application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv.md "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.")/[правило мониторинга уязвимостей уровня кода](application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv.md "Define rules based on specific process groups").
* Latest Dynatrace Отключить (заглушить) все затронутые объекты уязвимости. Это устанавливает статус уязвимости на `Muted`. Инструкции см. в разделе [Изменение статуса затронутого объекта](vulnerabilities/address-remediation.md#mute-entities "Address remediation and optimize remediation activities.").
* deprecated Отключить (заглушить) уязвимость. Подробнее см. в разделе [Изменение статуса сторонней уязвимости](application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities.md#mute "Organize third-party vulnerabilities for easy management and to prioritize issues.").

### Как получить информацию о рекомендациях по исправлению уязвимостей?

* Latest Dynatrace Для получения рекомендаций по исправлению уязвимостей используйте [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability data—all in one collaborative, customizable workspace.") для выполнения DQL-запроса, включающего поле `vulnerability.remediation.description`. Пример:

  ```
  fetch security.events


  | filter event.type == "VULNERABILITY_STATE_REPORT_EVENT"


  | filter event.level == "ENTITY"


  | fields vulnerability.risk.level, vulnerability.title, vulnerability.remediation.description
  ```

  Полный список запрашиваемых полей с описаниями и примерами см. в разделе [Dynatrace Semantic Dictionary: события безопасности](../semantic-dictionary/model/security-events.md "Get to know the Semantic Dictionary models related to security events.").
* deprecated Для получения рекомендаций по исправлению конкретной уязвимости вызовите конечную точку Dynatrace API для отдельной уязвимости. Укажите идентификатор уязвимости и запросите свойство `recommendationDescription` в ответе.

  Подробнее см. в разделе [Vulnerabilities API — GET vulnerability details](../dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerability-details.md "View details of a vulnerability via Dynatrace API.").

## Покрытие

### Как получить представление о покрытии Runtime Vulnerability Analytics в моей среде?

* Latest Dynatrace Оценивайте покрытие процессов и хостов Runtime Vulnerability Analytics в вашей среде с помощью готовой [информационной панели **Vulnerability coverage**](vulnerabilities/assess-coverage.md "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").
* deprecated Перейдите в ![Security Overview](https://dt-cdn.net/images/security-overview-512-a310b17025.png "Security Overview") **Security Overview**. В разделе **Host coverage** выберите **Monitored hosts**, чтобы перейти на страницу **Hosts**, отфильтрованную по отслеживаемым хостам. Подробнее см. в разделе [Обзор Application Security: покрытие хостов](application-security/vulnerability-analytics/application-security-overview.md#host-coverage "Get an overview of the security issues of your third-party libraries.").

### Почему я вижу уязвимость на одном хосте, но не на другом?

Обнаружение уязвимостей зависит от данных, получаемых Dynatrace с каждого хоста. Если хосту недостаёт необходимой инструментации или конфигурации, Dynatrace может не обнаружить или не подтвердить уязвимость на этом хосте. Распространённые причины включают отсутствующее внедрение OneAgent, отключённое автоматическое внедрение, устаревшие версии OneAgent или неподдерживаемые среды выполнения.

Latest Dynatrace Для выявления хостов с отсутствующим или отключённым автовнедрением вы можете выполнить DQL-запрос в [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability data—all in one collaborative, customizable workspace."), например:

```
fetch dt.entity.host


| fieldsAdd autoInjection


| fieldsAdd entity.name
```

## Ограничение мониторинга

### Как исключить определённые объекты из мониторинга Runtime Vulnerability Analytics?

Вы можете:

* [Создать правила мониторинга для сторонних уязвимостей](application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv.md "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.")
* [Создать правила мониторинга для уязвимостей уровня кода](application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv.md "Define rules based on specific process groups")

Ваши пользовательские правила переопределяют глобальную настройку контроля обнаружения сторонних уязвимостей. Любой объект, не соответствующий одному из ваших правил, будет следовать глобальной настройке обнаружения сторонних уязвимостей.

### Где найти примеры конфигураций правил мониторинга?

Если вам нужны рекомендации по настройке правил мониторинга в распространённых сценариях, таких как мониторинг только определённых хостов, процессов, пространств имён Kubernetes, узлов Kubernetes или исключение определённых процессов, вы можете обратиться к разделу [Варианты использования новых правил мониторинга](application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv.md#usecases "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes."). Там приведены практические примеры, показывающие, как настроить правила для различных сред и требований.

### Как ограничить мониторинг Runtime Vulnerability Analytics до определённой Management Zone?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

[Создайте правило мониторинга](application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv.md "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes."), которое гласит `Do not monitor`, если Management Zone не равна `<ваша-management-zone>`. После добавления, изменения или удаления правила подождите до 15 минут, пока изменения вступят в силу.

### Как включить Runtime Vulnerability Analytics только для определённых хостов или пространств имён Kubernetes?

Чтобы включить Runtime Vulnerability Analytics только для выбранных частей вашей среды, создайте правила мониторинга, применимые к конкретным хостам или пространствам имён Kubernetes, которые вы хотите отслеживать.

Вы можете воспользоваться следующими примерами вариантов использования:

* [Мониторинг только процессов на определённых хостах](application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv.md#monitor-processes-specific-host "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.")
* [Мониторинг только процессов, выполняемых в определённом пространстве имён Kubernetes](application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv.md#processes-specific-namespace "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.")

Эти примеры показывают, как отключить глобальный мониторинг и затем создать правила мониторинга на основе атрибутов ресурсов, которые избирательно включают мониторинг для выбранных объектов.

## Изменение статуса

### Если уязвимость отключена, отключаются ли также затронутые объекты?

Нет. Состояние `MUTE` не переходит автоматически на затронутые объекты; между ними нет взаимозависимости при оценке этого состояния.

Latest Dynatrace В [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](vulnerabilities.md "Prioritize and efficiently manage vulnerabilities in your monitored environments.") уязвимость отключается только в том случае, если все её затронутые объекты отключены. Подробнее см. в разделе [Изменение статуса отключения затронутых объектов](vulnerabilities/address-remediation.md#mute-entities "Address remediation and optimize remediation activities.").

## Обновления статуса

### К чему относится «последнее обновление» на страницах списка уязвимостей?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

***На странице списка сторонних уязвимостей означает ли «Last update» последнее время предоставления обновления Dynatrace? Как запросить обновление уязвимости, которая последний раз обновлялась два дня назад?***

**Last update** относится к последнему времени, когда у уязвимости произошло изменение статуса. Это не относится к последнему времени предоставления обновления Dynatrace. Подробнее см. в разделе [ЧЗВ: Можно ли вручную запустить проверку безопасности?](#start-scan).

#### Что такое изменения статуса

* Для сторонних уязвимостей изменение статуса может происходить, когда:

  + Уязвимость устраняется или открывается снова
  + Уязвимость отключается или включается снова
  + Количество затронутых групп процессов уменьшилось или увеличилось
  + Оценка рисков изменилась
  + Dynatrace Security Score изменился
  + Обнаружен новый программный компонент
* Для уязвимостей уровня кода изменение статуса может происходить, когда:

  + Уязвимость устраняется или открывается снова
  + Уязвимость отключается или включается снова
  + Оценка рисков изменилась
  + Обнаружены новые атаки на уязвимость

## Разные значения

### Почему значения на странице уязвимостей отличаются от значений в Data Explorer?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

***В ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** на странице списка **Third-party vulnerabilities**, при фильтрации по устранённым уязвимостям за последние семь дней, я получаю `3` уязвимости. Когда я использую запрос метрики (`builtin:security.securityProblem.resolved.new.global`) в Data Explorer, я получаю `25`. Почему значения на странице уязвимостей отличаются от значений в Data Explorer?***

Список уязвимостей показывает текущее состояние (общее количество уязвимостей, которые в настоящее время устранены), тогда как использование запроса метрики в [Data Explorer](../analyze-explore-automate/explorer.md "Query for metrics and transform results to gain desired insights.") показывает изменение во времени.

Например, если две уязвимости открываются и устраняются несколько раз в течение определённого периода времени, диаграмма Data Explorer показывает только один пик (максимум за данный временной интервал), тогда как страница уязвимостей показывает два (поскольку в настоящее время устранено две уязвимости).

Чтобы узнать, сколько уязвимостей было устранено за данный временной интервал с помощью запроса метрики:

1. В Data Explorer установите тип визуализации `Single value`.
2. Разверните **Settings** и установите **Fold transformation** в значение `Value`.

   Это покажет, сколько раз уязвимости были устранены в течение выбранного временного интервала.

![Пример настройки Fold transformation в Data Explorer](https://dt-cdn.net/images/2023-06-15-09-41-13-1626-bcb5aa24fb.png)

### Почему значения на страницах сторонних уязвимостей и сведений об уязвимостях отличаются?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

Существует две причины, по которым значения на этих страницах могут не совпадать:

* [Разное количество затронутых объектов](#different-affected-entities)
* [Разные факторы риска](#different-risk-factors)

#### Разное количество затронутых объектов

В ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** количество затронутых объектов (групп процессов или хостов) на странице **Third-party vulnerabilities** (в столбце **Affected entities** для конкретной уязвимости) может отличаться от количества затронутых объектов на странице сведений об уязвимости по следующим причинам:

* На странице **Third-party vulnerabilities**:

  + Затронутые объекты не фильтруются по Management Zone.
  + Вычисления выполняются каждые 15 минут.
* На странице сведений об уязвимости:

  + Затронутые объекты фильтруются по Management Zone.
  + Учитываются текущие данные.

#### Разные факторы риска

В ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** оценка факторов риска (`Public exploit`, `Public internet exposure`, `Reachable data assets`, `Vulnerable functions in use`) в инфографике на странице сведений об уязвимости и столбце **Davis Security Score** на странице **Third-party vulnerabilities** может отличаться от оценки факторов риска на странице сведений об уязвимости (в разделе **Vulnerability details**) по следующей причине:

Для инфографики на странице сведений об уязвимости и столбца **Davis Security Score** на странице **Third-party vulnerabilities** вычисления выполняются каждые 15 минут.
Для раздела **Vulnerability details** на странице сведений об уязвимости учитываются текущие данные.

### Почему у моей уязвимости другая оценка риска и DSS, чем у её затронутых объектов?

Уязвимость является агрегацией всех её затронутых объектов в вашей среде; поэтому у неё могут быть другие значения (оценка риска и DSS), чем у её затронутых объектов. Например, оценка риска затронутого объекта может быть `8.0`, тогда как оценка агрегированной уязвимости — `9.0`. В то же время, если хотя бы один затронутый объект подключён к Интернету, агрегированная уязвимость также считается подключённой к Интернету.

Latest Dynatrace В [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](vulnerabilities.md "Prioritize and efficiently manage vulnerabilities in your monitored environments.") DSS-оценка является максимальной DSS-оценкой затронутых объектов. Подробнее см. в разделе [Различия в вычислениях](vulnerabilities/concepts.md#differences "Concepts that are specific to the Dynatrace Vulnerabilities app.").

### Почему я вижу разные уязвимости в производственной и непроизводственной средах?

Одинаковые уязвимости в двух средах возможны только в том случае, если все следующее одинаково в обеих средах:

* Развёртывание (включая версию OneAgent)
* Настройки
* Использование приложения
* Трафик

### Почему количество уязвимостей отличается в классических приложениях и в приложении Vulnerabilities?

Общее количество уязвимостей, отображаемых в ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, может незначительно отличаться от счётчиков в классическом приложении **Third-party vulnerabilities**. Это различие обусловлено несколькими внутренними факторами:

* **Время**: экспорт отчётов о состоянии может занять до 15 минут. В результате уязвимости могут появляться или исчезать с задержкой в ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**.
* **Отключение**: отключённые уязвимости исключаются из отображаемого количества **vulnerabilities detected** в классических приложениях. Чтобы просмотреть их, необходимо применить фильтр по отключённым уязвимостям или обратиться к сводной панели.
* **Временной интервал**: временной интервал по умолчанию для ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** составляет 30 минут, тогда как классические приложения используют временной интервал по умолчанию в 2 часа.

Рекомендуем использовать ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** в качестве основного интерфейса для управления уязвимостями. Он отражает новейшую логику обнаружения, активно поддерживается и продолжает развиваться. Планируется поэтапный вывод классических представлений для клиентов SaaS в ближайшие годы.

## Публичное воздействие через Интернет

### Как определяется публичное воздействие через Интернет?

На хостах Linux, если информация отсутствует — что может происходить в различных режимах мониторинга или в случае ошибки — публичное воздействие через Интернет определяется с помощью eBPF. Возможные состояния: `Public network` и `Not detected`.

Full-Stack Monitoring mode

Infrastructure Monitoring mode and Discovery mode

Для определения публичного воздействия через Интернет Dynatrace:

1. Оценивает все IP-адреса, обнаруженные за последний час.
2. Отбрасывает диапазоны частных IP-адресов.
3. Группирует оставшиеся IP-адреса по подсетям.

Как только соответствующие подсети достигают определённого (низкого) порогового значения, запускается публичное воздействие через Интернет.

Публичное воздействие через Интернет не может быть оценено в операционных системах, отличных от Linux, и состояние имеет значение `Not available`.

## Уязвимые библиотеки

### Обнаруживает ли Dynatrace уязвимые библиотеки, которые не используются?

Runtime Vulnerability Analytics фокусируется на аспекте среды выполнения, стремясь предоставить приоритизированный список уязвимостей, актуальных для ваших работающих сред. Для этой цели Dynatrace сообщает только о библиотеках, которые активно используются.

### Где можно увидеть источник уязвимой библиотеки?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

На страницах отслеживания исправлений для групп процессов и процессов, затронутых уязвимостью, вы можете увидеть, откуда был загружен программный компонент.

Эта функция отображается для уязвимых программных компонентов Java, .NET, Node.js, Python и Go.

Обратите внимание, что для отображения источника программных компонентов .NET минимальная требуемая версия OneAgent — версия 1.301+.

Пример:

![load-origins-pg](https://dt-cdn.net/images/2023-08-21-15-09-46-1812-3f3a0b8200.png)

Информацию о том, как перейти туда, см. в разделе [Отслеживание исправлений](application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md "Track the remediation progress of vulnerabilities.").

## Уязвимые функции

### Как определяются уязвимые функции?

* Если Snyk предоставляет информацию об уязвимой функции и мониторинг OneAgent для уязвимых функций Java включён, OneAgent определяет, используется ли уязвимая функция.
* Если Snyk предоставляет информацию об уязвимой функции, но функция OneAgent отключена, количество уязвимых функций отображается как **Not available**.

### Почему нет информации об уязвимых функциях?

Существует два случая, когда информация об уязвимых функциях недоступна:

* Если Snyk или исследовательская группа по безопасности Dynatrace не предоставили информацию об уязвимой функции.
* Для уязвимостей среды выполнения, основанных на NVD-источнике.

### Почему данные об уязвимых функциях недоступны?

* После [включения Third-party Vulnerability Analytics](application-security/vulnerability-analytics.md#enable-tpva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") потребуется некоторое время (не более одного часа), прежде чем данные об уязвимых функциях будут отображены.
* Мониторинг OneAgent для уязвимых функций Java отключён. Чтобы включить его, см. раздел [Включение мониторинга OneAgent для уязвимых функций Java](application-security/vulnerability-analytics.md#vulnerable-function "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

  Функция OneAgent должна быть включена для всех процессов, затронутых уязвимостью. Инструкции по включению мониторинга OneAgent см. в разделе [Включение мониторинга OneAgent для уязвимых функций Java](application-security/vulnerability-analytics.md#vulnerable-function "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
* Уязвимые функции уязвимости не содержатся в релизной версии используемых сторонних библиотек (программных компонентов).
* Snyk не предоставляет уязвимых функций.
* deprecated Вам необходимо перезапустить процессы, затронутые уязвимостью, для получения обновлённой информации. Подробнее см. в разделе [ЧЗВ: Как я могу узнать, что информация об уязвимых функциях устарела, и что с этим делать?](faq.md#outdated-vulnerable-functions "Frequently asked questions about Dynatrace Application Security.").

#### Как узнать, какие процессы нужно перезапустить?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

Если вы видите уведомление **Restart required** на странице сведений об уязвимости, выполните следующие шаги, чтобы определить, какие процессы нужно перезапустить:

1. На карточке [**Process group overview**](application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities.md#pg "Monitor the security issues of your third-party libraries.") выберите **View all process groups**.
2. Фильтруйте по `Vulnerable functions: Restart required`.
3. Для каждой из полученных групп процессов выберите **Details**, затем выберите ссылку в уведомлении **Restart required**, чтобы перейти к списку процессов, требующих перезапуска.

![Выбор процессов, требующих перезапуска](https://dt-cdn.net/images/2023-12-18-13-43-19-539-175d9b3394.png)

Пример результата:

![Фильтрация по Vulnerable functions: Restart required](https://dt-cdn.net/images/2023-12-18-13-07-00-1594-7f9f9381c3.png)

После перезапуска процесса обновлённая информация отображается примерно через минуту.

Эта функция работает только при [включённом мониторинге OneAgent для уязвимых функций Java](application-security/vulnerability-analytics.md#vulnerable-function "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

#### Почему мой процесс всё ещё требует перезапуска после того, как я уже перезапустил его?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

Если вы выполнили [инструкции](#which-process-to-restart) по определению процесса и перезапустили его, а процесс всё ещё требует перезапуска (появляется то же уведомление **Restart required**, и информация об уязвимых функциях не изменилась), это может происходить в развёртываниях Kubernetes без постоянного хранилища.

Для устранения этой проблемы добавьте постоянное хранилище, подключив файловое хранилище, которое не удаляется при перезапуске модулей.

### Как я могу узнать, что информация об уязвимых функциях устарела, и что с этим делать?

Содержимое ниже относится к классическому приложению ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, которое является устаревшим.

OneAgent version 1.279+

Если доступна новая информация об уязвимых функциях уязвимости, требуется перезапуск процесса, чтобы OneAgent мог получить и использовать новые данные.
В этом случае уведомление или символ **Restart required** отображается на:

* Странице сведений об уязвимости (в [**Vulnerability details**](application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities.md#vulnerability-details "Monitor the security issues of your third-party libraries.") > **Vulnerable functions**)

  ![Уведомление Restart required на странице сведений об уязвимости](https://dt-cdn.net/images/2023-12-18-12-45-12-776-d39b330fe4.png)
* [Обзор групп процессов, связанных с уязвимостью](application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md#pg "Track the remediation progress of vulnerabilities.") (в [**Details**](application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md#details "Track the remediation progress of vulnerabilities.") > **Risk assessment**)

  ![Уведомление Restart required в обзоре групп процессов для уязвимости](https://dt-cdn.net/images/2023-12-18-12-41-00-1597-34af91fcf3.png)
* [Список процессов, связанных с уязвимостью](application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking.md#process "Track the remediation progress of vulnerabilities.") (в **Vulnerable functions** и **Details**).

  ![Уведомление Restart required в списке процессов для уязвимости](https://dt-cdn.net/images/2023-12-18-12-37-41-1570-47da22adc2.png)

## Snyk feed

### Почему для некоторых уязвимостей отсутствует ссылка на Snyk?

***Почему некоторые уязвимости не содержат ссылку на Snyk, хотя я могу найти тот же CVE в Snyk?***

Для получения данных об уязвимостях Dynatrace Application Security использует [Snyk](https://snyk.io) или [NVD](https://nvd.nist.gov/vuln) в зависимости от уязвимого компонента.

Уязвимость с CVE, которая указана в Snyk, но не содержит никакой информации, связанной со Snyk, в Dynatrace, использует NVD-источник. Дополнительные сведения см. в разделе [Источники сторонних уязвимостей](application-security/vulnerability-analytics/vulnerability-evaluation.md#vulnerability-feeds "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.").

## Механизм блокировки атак

### Как Dynatrace фактически блокирует атаки?

Выбор `Block attack` для атаки не блокирует соответствующую атаку автоматически; это переводит вас на страницу настроек, где вы можете создать правило мониторинга для блокировки этой атаки в будущем. Dynatrace настроен на блокировку будущих ситуаций с эксплойтами, а не текущих.
Запрос (поток) с эксплойтом выбрасывает исключение в выполняемом коде. Все другие пользователи, которые не атакуют, не затрагиваются.
Dynatrace обнаруживает, когда предоставленный пользователем эксплойт попадает в строку кода, которая использует небезопасный способ:

* Общения с базой данных (SQL-инъекция)
* Общения с операционной системой (инъекция команд)
* Выполнения JNDI-поиска (JNDI-инъекция, например Log4Shell)
* Выполнения HTTP-запроса (SSRF)

Уязвимость определяется с атакой или без неё. Если данные, отправленные клиентом, содержат признаки атаки, достигающей этой строки кода, это считается эксплойтом, и Dynatrace выдаёт предупреждение или блокирует его.

Дополнительные сведения о механизме Runtime Application Protection см. в разделе [Как это работает](application-security/application-protection.md#mechanism "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.").

### Как определяется IP-адрес злоумышленника?

В Runtime Application Protection для определения IP-адреса злоумышленника Dynatrace проверяет:

* Специфические HTTP-заголовки, такие как `X-Client-IP` или `X-Forwarded-For`.

* IP-адрес клиента для соединения через сокет (если упомянутые выше HTTP-заголовки недоступны).

  Подробнее см. в разделе [Определение IP-адреса клиента](threats-and-exploits.md#client-ip-address "Understand, triage, and investigate detection findings and alerts.").

## Хранение данных

### Каков период хранения данных для уязвимостей, событий и атак?

Информацию о том, как данные безопасности хранятся в Dynatrace, см. в разделе [Периоды хранения данных](../manage/data-privacy-and-security/data-privacy/data-retention-periods.md "Check retention times for various data types.").

## Потребление

### Как я могу проверить, какое потребление на моих хостах?

* При использовании [Dynatrace Platform Subscription](../license.md "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") см.:

  + [Расчёт потребления Runtime Vulnerability Analytics](../license/capabilities/application-security/runtime-vulnerability-analytics.md "Learn how your consumption of the Dynatrace Runtime Vulnerability Analytics (RVA) DPS capability is billed and charged.")
  + [Расчёт потребления Runtime Application Protection](../license/capabilities/application-security/runtime-application-protection.md "Learn how how your consumption of the Runtime Application Protection (RAP) DPS capability is billed and charged.")
  + [Расчёт потребления Security Posture Management](../license/capabilities/application-security/security-posture-management.md "Learn how your consumption of the Dynatrace Security Posture Management (SPM) DPS capability is billed and charged.")
* При использовании [классического лицензирования Dynatrace](../license/monitoring-consumption-classic.md "Understand how Dynatrace monitoring consumption is calculated for classic licensing.") см. раздел [Как возможности влияют на потребление мониторинга](../license/monitoring-consumption-classic/application-security-units.md#how-capabilities-affect-monitoring-consumption "Understand how Dynatrace Application Security and Runecast SPM consumption are calculated.").

deprecated Чтобы просмотреть, какие хосты потребляют DPS/ASU, в ![Security Overview](https://dt-cdn.net/images/security-overview-512-a310b17025.png "Security Overview") **Security Overview** перейдите в раздел **Host coverage** для сторонних и уязвимостей уровня кода и выберите **Monitored hosts**. Полученный список хостов — это хосты в вашей среде, которые потребляют DPS/ASU.
Дополнительные сведения см. в разделе [Покрытие хостов](application-security/vulnerability-analytics/application-security-overview.md#host-coverage "Get an overview of the security issues of your third-party libraries.").

### Почему Application Security всё ещё показывает использование, хотя я отключил RVA?

***Я отключил аналитику уязвимостей сторонних и уязвимостей уровня кода. На моём хосте отображается «Not analyzed», но использование всё равно появляется в моей подписке. Почему?***

Это поведение применяется как к [классическому лицензированию Dynatrace (ASU)](../license/monitoring-consumption-classic/application-security-units.md#how-capabilities-affect-monitoring-consumption "Understand how Dynatrace Application Security and Runecast SPM consumption are calculated."), так и к [Dynatrace Platform Subscription (DPS)](../license/capabilities/application-security/runtime-application-protection.md "Learn how how your consumption of the Runtime Application Protection (RAP) DPS capability is billed and charged.").

Проверьте, включён ли Runtime Application Protection (RAP). RAP зависит от Runtime Vulnerability Assessment (RVA) для определения, какую уязвимость пытается использовать атака. Поскольку RAP не может работать без RVA, любой хост с включённым RAP всегда будет потреблять ASU/DPS как для RAP, так и для RVA — даже если глобальные переключатели для обнаружения уязвимостей сторонних библиотек или уязвимостей уровня кода отключены.
