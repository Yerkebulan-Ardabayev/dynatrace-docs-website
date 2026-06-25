---
title: FAQ по Application Security
source: https://docs.dynatrace.com/managed/secure/faq
scraped: 2026-05-12T11:13:46.543235
---

# FAQ по Application Security

# FAQ по Application Security

* Troubleshooting
* Updated on Mar 01, 2026

Ниже приведены ответы на наиболее часто задаваемые вопросы о Dynatrace Application Security, сгруппированные по темам.

Статьи по устранению неполадок, связанные с Application Security, см. в [Dynatrace Community](https://dt-url.net/dy122xtf).

## Обнаружение и мониторинг

### Как обнаруживать риски безопасности в приложениях?

С помощью [Dynatrace Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.") можно не только выявлять и отслеживать уязвимости в приложениях (сторонние библиотеки, среды выполнения приложений, пользовательский код) в производственных и предпроизводственных средах, но и автоматически обнаруживать и блокировать атаки на приложения в режиме реального времени.

Чтобы начать работу:

1. [Активируйте и включите Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.").
2. Выберите один из вариантов ниже:

* Для обнаружения и мониторинга сторонних уязвимостей [включите обнаружение сторонних уязвимостей](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Мониторинг уязвимостей сторонних библиотек."), затем перейдите в [**Third-Party Vulnerabilities**](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Мониторинг проблем безопасности сторонних библиотек.").
* Для обнаружения и мониторинга уязвимостей на уровне кода [включите обнаружение уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics#clv-detection "Мониторинг уязвимостей на уровне кода."), затем перейдите в [**Code-Level Vulnerabilities**](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/manage-code-level-vulnerabilities "Мониторинг уязвимостей на уровне кода в вашей среде.").
* Для единого представления сторонних уязвимостей и уязвимостей на уровне кода и информации о покрытии хостов [включите Runtime Vulnerability Analytics](/managed/secure/application-security/vulnerability-analytics "Мониторинг уязвимостей сторонних библиотек и на уровне кода."), затем перейдите в [**Security Overview**](/managed/secure/application-security/vulnerability-analytics/application-security-overview "Обзор проблем безопасности сторонних библиотек.").
* Для обнаружения и мониторинга атак на уязвимости [включите Runtime Application Protection](/managed/secure/application-security/application-protection "Настройка Dynatrace Runtime Application Protection."), затем перейдите в [Attacks](/managed/secure/application-security/application-protection/manage-attacks "Мониторинг атак на код приложения.").

### В чём разница между классическими и новыми правилами мониторинга?

[Новые правила мониторинга](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#new "Создание, изменение и удаление пользовательских правил мониторинга.") позволяют включать или исключать процессы, узлы Kubernetes и хосты на основе атрибутов ресурсов и меток Kubernetes. Этот подход более гибкий и точный, хорошо работает в динамичных и облачных средах и поддерживает предварительный просмотр для проверки соответствующих объектов до включения правил. Рекомендуются и устанавливаются по умолчанию для новых сред.

[Классические правила мониторинга](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#classic "Классические правила мониторинга.") основаны на тегах групп процессов, тегах хостов и зонах управления. Они менее гранулярны, зависят от правильного тегирования и не обеспечивают тот же уровень предварительного просмотра и управления. Классические правила продолжают работать, но запланированы к устареванию и не могут использоваться одновременно с новыми правилами.

### Как работают RVA и RAP?

* Подробнее о механизме Runtime Vulnerability Analytics (RVA) см. в разделе [Как работает RVA](/managed/secure/application-security/vulnerability-analytics#mechanism "Мониторинг уязвимостей сторонних библиотек и на уровне кода.").
* Подробнее о механизме Runtime Application Protection (RAP) см. в разделе [Как работает RAP](/managed/secure/application-security/application-protection#mechanism "Настройка Dynatrace Runtime Application Protection.").

### Как включение Application Security влияет на работу?

***Что следует учитывать перед включением Application Security? Может ли это повлиять на что-либо?***

При включении Application Security (Runtime Vulnerability Analytics или Runtime Application Protection) следует помнить о следующем:

* **Потребление**:  
  **Runtime Vulnerability Analytics и Runtime Application Protection** потребляют [GiB-часы](/managed/license/capabilities/application-security "Узнайте, как рассчитывается потребление Application Security.") при использовании модели лицензирования [Dynatrace Platform Subscription (DPS)](/managed/license "О модели лицензирования Dynatrace Platform Subscription.") или [единицы Application Security (ASU)](/managed/license/monitoring-consumption-classic/application-security-units "Расчёт потребления Application Security.") при использовании [классического лицензирования Dynatrace](/managed/license/monitoring-consumption-classic "Расчёт потребления мониторинга при классическом лицензировании.").
* **Использование полосы пропускания сети**:

  + **Обнаружение уязвимостей на уровне кода и обнаружение атак**: ожидается небольшое увеличение использования сети в зависимости от количества отслеживаемых приложений. В большинстве случаев эти накладные расходы незначительны.
  + **Обнаружение сторонних уязвимостей**: дополнительные накладные расходы на процессы не вводятся.

### Как отключить мониторинг безопасности?

* Для отключения Runtime Vulnerability Analytics:

  1. Перейдите в **Settings** > **Application Security** > **Vulnerability Analytics** > **General settings**.
  2. В разделе **Third-party Vulnerability Analytics** выключите **Enable Third-party Vulnerability Analytics**.
  3. В разделе **Code-level Vulnerability Analytics** выключите **Enable Code-level Vulnerability Analytics**.
* Для отключения Runtime Application Protection:

  1. Перейдите в **Settings** > **Application Security** > **Application Protection** > **General settings**.
  2. Выключите **Enable Runtime Application Protection**.

### Можно ли запустить проверку безопасности вручную?

***Выполняет ли Application Security запланированные задания? Каков интервал расписания? Можно ли вручную запустить проверку безопасности после развёртывания изменений в среде?***

Запланированных сканирований нет. После включения любой функции Dynatrace Application Security среда автоматически и непрерывно отслеживается в режиме реального времени.

## Ограничение разрешений

### Как предоставить кому-либо доступ только для просмотра уязвимостей?

Чтобы ограничить конкретных пользователей правами только на просмотр уязвимостей без возможности управления ими, см. раздел [Настройка доступа](/managed/secure/application-security/vulnerability-analytics#restrict-permissions "Мониторинг уязвимостей сторонних библиотек и на уровне кода.").

## Устранение

### Устраняет ли Dynatrace уязвимости?

***Исправляет ли Dynatrace уязвимости, или мне нужно предпринимать какие-либо действия?***

Dynatrace не устраняет уязвимости. Система выявляет и отслеживает уязвимости в приложениях в производственных и предпроизводственных средах и помогает определить первопричину, предоставляя богатый контекст и информацию для принятия необходимых мер. Подробнее о возможностях см. в разделе [Runtime Vulnerability Analytics: Возможности](/managed/secure/application-security/vulnerability-analytics "Мониторинг уязвимостей сторонних библиотек и на уровне кода.").

После устранения первопричины уязвимость закрывается автоматически. Подробнее об устранении уязвимостей см.:

* [Устранение сторонних уязвимостей](/managed/secure/application-security/vulnerability-analytics/vulnerability-evaluation#tpv-resolution "Изучите механизм генерации уязвимостей в Dynatrace.")
* [Устранение уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics/vulnerability-evaluation#clv-resolution "Изучите механизм генерации уязвимостей на уровне кода в Dynatrace.")

### Как исправить обнаруженные уязвимости?

Богатый и точный контекст и детали на страницах уязвимостей помогают выявлять и понимать уязвимости, расставлять приоритеты по риску, а также автоматически отслеживать и получать оповещения о новых уязвимостях. На основе этой информации можно определить, какие действия необходимы для устранения уязвимостей.

Например, для сторонних уязвимостей можно:

* Использовать рекомендуемые исправления от [Davis Security Advisor](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor "Получите рекомендации по исправлению от Davis Security Advisor.") для обновления уязвимого компонента до безопасной версии
* [Настроить ссылки для отслеживания затронутых объектов и следить за прогрессом их устранения](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживание прогресса устранения уязвимостей.")

### Когда уязвимость отмечается как устранённая?

***Я удалил уязвимый компонент, но уязвимость всё ещё отображается как открытая. Когда она будет устранена?***

Уязвимость отмечается как `Resolved` при следующих условиях:

* Ни одна группа процессов или узел Kubernetes не сообщали об уязвимых компонентах более двух часов.
* Первопричина уязвимости больше не существует; например, уязвимый компонент был удалён или затронутый процесс завершён.

  Это условие применяется независимо от того, сколько времени прошло с момента последнего отчёта.

### Почему уязвимость всё ещё открыта, если затронутых групп процессов больше нет?

Уязвимость всё ещё отображается, если она присутствует в других зонах управления. Чтобы увидеть затронутые группы процессов, выберите `All` в фильтре зон управления.

### Может ли уязвимость быть устранена при наличии затронутых объектов?

Нет. Уязвимость устраняется только при отсутствии затронутых объектов.

### Почему некоторые уязвимости устраняются без каких-либо действий с нашей стороны?

***После включения Runtime Vulnerability Analytics было обнаружено 19 критических уязвимостей. Теперь их стало три без каких-либо действий с нашей стороны. Почему некоторые уязвимости устраняются сами?***

Уязвимость автоматически устраняется, если первопричина больше не существует. Подробнее см.:

* [Устранение сторонних уязвимостей](/managed/secure/application-security/vulnerability-analytics/vulnerability-evaluation#tpv-resolution "Изучите механизм генерации уязвимостей в Dynatrace.")
* [Устранение уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics/vulnerability-evaluation#clv-resolution "Изучите механизм генерации уязвимостей на уровне кода в Dynatrace.")

### Почему некоторые уязвимости постоянно устраняются и повторно открываются?

Уязвимость постоянно устраняется и повторно открывается, когда процесс, использующий уязвимую библиотеку, работает не постоянно:

* Когда процесс завершается, уязвимость устраняется.
* Когда процесс перезапускается, уязвимость открывается повторно.

Подробнее о причинах устранения и повторного открытия уязвимостей см. в разделе [Устранение](/managed/secure/application-security/vulnerability-analytics/vulnerability-evaluation#tpv-resolution "Изучите механизм генерации уязвимостей в Dynatrace.").

Чтобы определить, какие процессы затронуты, обратитесь к [отслеживанию устранения для процессов](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#process "Отслеживание прогресса устранения уязвимостей.").

### Почему устранённые уязвимости отображаются во всех зонах управления?

Информация о зоне управления не привязана напрямую к уязвимости. Она производна от уязвимых объектов, затронутых данной уязвимостью: процесс в зоне управления, использующий уязвимую библиотеку, вызывает стороннюю уязвимость в соответствующей зоне.

Уязвимость устраняется при отсутствии уязвимых объектов. В списке уязвимостей все отображаемые устранённые уязвимости не фильтруются по зоне управления, так как эта информация к ним не привязана.

### Почему для устранённых уязвимостей в моей зоне управления отображается ноль устранённых групп процессов?

***Для устранённых уязвимостей я хотел бы изучить устранённые группы процессов, чтобы понять, какие объекты были затронуты ранее, но в моей зоне управления ноль устранённых групп процессов. Почему?***

На страницах уязвимостей в разделе **Process group overview**, если для устранённой уязвимости в вашей зоне управления отображается ноль устранённых групп процессов, это означает, что ни один из ранее затронутых и устранённых объектов не находится в этой зоне. Чтобы найти соответствующие объекты, переключите фильтр зоны управления на `All`.

## Требуется перезапуск

### Требуется ли перезапуск после включения или отключения функции Application Security?

Ниже приведены требования к перезапуску по функциям.

* **Third-party vulnerabilities**: перезапуск процесса приложения требуется в следующем случае:

  + В [**Discovery mode**](/managed/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Подробнее о доступных режимах мониторинга при использовании OneAgent.") после [включения инъекции code-module](/managed/platform/oneagent/monitoring-modes/monitoring-modes#code-module-injection "Подробнее о режимах мониторинга.").
* **Code-level vulnerabilities**: перезапуск процесса приложения требуется в следующих случаях:

  + После каждого шага в [включении обнаружения уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics#clv-detection "Мониторинг уязвимостей на уровне кода."):

    - Включение Code-level Vulnerability Analytics
    - Настройка глобального управления обнаружением уязвимостей на уровне кода для каждой технологии
    - Включение мониторинга OneAgent
  + После включения [правила мониторинга](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Определение правил на основе конкретных групп процессов")
* **Attacks**: перезапуск процесса приложения требуется в следующих случаях:

  + После каждого шага в [начале работы с Runtime Application Protection](/managed/secure/application-security/application-protection#start "Настройка Dynatrace Runtime Application Protection."):

    - Включение Runtime Application Protection
    - Определение глобального управления атаками для каждой технологии
    - Включение мониторинга OneAgent
  + После включения [правила мониторинга](/managed/secure/application-security/application-protection/application-protection-rules "Создание, изменение и удаление правил для конкретных атак.")

### Почему на некоторых страницах Application Security отображается уведомление «Restart required»?

OneAgent версии 1.279+

См. раздел [Как узнать, устарела ли информация об уязвимых функциях, и что с этим делать?](#outdated-vulnerable-functions).

## Уведомления и отчётность

### Как получать уведомления об уязвимостях?

Можно [настроить уведомления](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva "Интеграция уведомлений безопасности об уязвимостях с Dynatrace.") через предпочтительные каналы.

* Например, можно настроить оповещения:

  + При повторном открытии уязвимости (**Vulnerability (re)opened**)
  + При появлении новой затронутой группы процессов в зоне управления (**New Management zone affected**)

### Как получать уведомления об атаках?

Можно [настроить уведомления](/managed/secure/application-security/application-protection/security-notifications-rap "Интеграция уведомлений безопасности об атаках с Dynatrace.") через предпочтительные каналы.

### Как создавать отчёты и делиться ими?

* С помощью Dynatrace API можно создавать графики на основе [метрик Application Security](/managed/secure/application-security/vulnerability-analytics/app-sec-metrics "Просмотр доступных метрик Application Security.") и [закреплять их на дашборде](/managed/analyze-explore-automate/dashboards-classic/metrics-browser#pin "Обзор метрик с помощью Dynatrace metrics browser."). Например, можно получить [все проблемы безопасности, обнаруженные в приложениях](/managed/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerabilities "Просмотр списка уязвимостей через Dynatrace API."), или [уязвимые функции проблемы безопасности](/managed/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerable-functions "Просмотр уязвимых функций через Dynatrace API.").
* С помощью [Data Explorer](/managed/analyze-explore-automate/explorer "Запрос метрик и преобразование результатов.") можно [поделиться результатами метрик](/managed/analyze-explore-automate/explorer#share "Запрос метрик и преобразование результатов.") и [экспортировать их в файл CSV](/managed/analyze-explore-automate/explorer#csv "Запрос метрик и преобразование результатов.").

### Как прекратить получение уведомлений для нерелевантной уязвимости или объекта?

Если уязвимость или объект нерелевантны либо являются ложным срабатыванием, можно:

* Заглушить уязвимость. Подробнее см. в разделах [Изменение статуса сторонней уязвимости](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities#mute "Организуйте сторонние уязвимости для удобного управления.") и [Изменение статуса уязвимости на уровне кода](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/filter-clv-vulnerabilities#mute "Организуйте уязвимости на уровне кода для удобного управления.").
* Заглушить объект. Подробнее см. в разделах [Изменение статуса уязвимости для групп процессов](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#status-pg "Отслеживание прогресса устранения уязвимостей.") и [Изменение статуса уязвимости для узлов](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#status-node "Отслеживание прогресса устранения уязвимостей.").

### Почему мы продолжаем получать уведомления об одной и той же уязвимости?

***Мы настроили уведомления безопасности по email, но каждый день получаем уведомления об одном и том же ID уязвимости с той же группой процессов, именем объекта и ссылкой на объект. Обнаружены другие уязвимости, но по ним дополнительных уведомлений не поступает. Почему мы продолжаем получать уведомления об одной и той же уязвимости?***

Процесс, работающий не постоянно, может использовать уязвимую библиотеку. Подробнее см. в разделе [Почему некоторые уязвимости постоянно устраняются и повторно открываются?](#reopen).
Чтобы прекратить получение уведомлений об этой уязвимости, можно:

* Исключить соответствующий процесс из мониторинга Application Security, настроив [правило мониторинга сторонних уязвимостей](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Создание, изменение и удаление пользовательских правил мониторинга.") или [правило мониторинга уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Определение правил на основе конкретных групп процессов.").
* [Заглушить стороннюю уязвимость](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities#mute "Организуйте сторонние уязвимости для удобного управления.") или [заглушить уязвимость на уровне кода](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/filter-clv-vulnerabilities#mute "Организуйте уязвимости на уровне кода для удобного управления.").

### Как получить информацию о рекомендациях по исправлению уязвимостей?

Для получения рекомендаций по устранению конкретной уязвимости вызовите конечную точку Dynatrace API для отдельной уязвимости. Укажите ID уязвимости и запросите свойство `recommendationDescription` в ответе.

Подробнее см. в разделе [Vulnerabilities API - GET vulnerability details](/managed/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerability-details "Просмотр сведений об уязвимости через Dynatrace API.").

## Покрытие

### Как узнать, какие хосты охвачены Application Security?

Перейдите в **Security Overview**. В разделе **Host coverage** нажмите **Monitored hosts** для перехода на страницу **Hosts**, отфильтрованную по отслеживаемым хостам. Подробнее см. в разделе [Обзор Application Security: Покрытие хостов](/managed/secure/application-security/vulnerability-analytics/application-security-overview#host-coverage "Обзор проблем безопасности сторонних библиотек.").

### Почему уязвимость отображается на одном хосте, но не на другом?

Обнаружение уязвимостей зависит от данных, которые Dynatrace получает от каждого хоста. Если на хосте отсутствует необходимая инструментация или конфигурация, Dynatrace может не обнаружить или не подтвердить уязвимость на этом хосте. Распространённые причины: отсутствие инъекции OneAgent, отключённая автоматическая инъекция, устаревшие версии OneAgent или неподдерживаемые среды выполнения.

## Ограничение мониторинга

### Как исключить конкретные объекты из мониторинга Runtime Vulnerability Analytics?

Можно:

* [Создать правила мониторинга для сторонних уязвимостей](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Создание, изменение и удаление пользовательских правил мониторинга.")
* [Создать правила мониторинга для уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Определение правил на основе конкретных групп процессов.")

Пользовательские правила переопределяют глобальную настройку управления обнаружением сторонних уязвимостей. Любой объект, не соответствующий ни одному правилу, будет следовать глобальной настройке обнаружения сторонних уязвимостей.

### Где найти примеры конфигурации правил мониторинга?

Если вам нужны рекомендации по настройке правил мониторинга для типичных сценариев, таких как мониторинг только определённых хостов, процессов, пространств имён Kubernetes, узлов Kubernetes или исключение определённых процессов, обратитесь к разделу [Сценарии использования новых правил мониторинга](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#usecases "Создание, изменение и удаление пользовательских правил мониторинга.").

### Как ограничить мониторинг Runtime Vulnerability Analytics конкретной зоной управления?

[Создайте правило мониторинга](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Создание, изменение и удаление пользовательских правил мониторинга."), в котором задано `Do not monitor`, если зона управления не равна `<your-management-zone>`. После добавления, изменения или удаления правила подождите до 15 минут, чтобы изменения вступили в силу.

### Как включить Runtime Vulnerability Analytics только для определённых хостов или пространств имён Kubernetes?

Чтобы включить Runtime Vulnerability Analytics только для выбранных частей среды, создайте правила мониторинга для конкретных хостов или пространств имён Kubernetes.

Можно использовать следующие примеры сценариев:

* [Мониторинг только процессов на определённых хостах](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#monitor-processes-specific-host "Создание, изменение и удаление пользовательских правил мониторинга.")
* [Мониторинг только процессов в конкретном пространстве имён Kubernetes](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#processes-specific-namespace "Создание, изменение и удаление пользовательских правил мониторинга.")

## Изменение статуса

### Если уязвимость заглушена, заглушаются ли и затронутые объекты?

Нет. Состояние `MUTE` не передаётся автоматически затронутым объектам; между ними нет взаимозависимости при оценке этого состояния.

## Обновления статуса

### На что ссылается «последнее обновление» на страницах со списком уязвимостей?

***На страницах со списком сторонних уязвимостей и уязвимостей на уровне кода, относится ли «Last update» к последнему времени, когда Dynatrace предоставил обновление? Как запросить обновление для уязвимости, которая последний раз обновлялась два дня назад?***

**Last update** относится к последнему времени изменения статуса уязвимости, а не к последнему обновлению от Dynatrace. Подробнее см. в разделе [FAQ: Можно ли запустить проверку безопасности вручную?](#start-scan).

#### Что является изменением статуса

Сторонние уязвимости

Уязвимости на уровне кода

Изменение статуса происходит в следующих случаях:

* Уязвимость устранена или повторно открыта
* Уязвимость заглушена или снята с заглушки
* Количество затронутых групп процессов уменьшилось или увеличилось
* Оценка риска изменилась
* Davis Security Score изменился
* Обнаружен новый программный компонент

В примере ниже прошло восемь часов и шесть минут с момента изменения оценки риска.

![Timeframe showing the last update of a third-party vulnerability](https://dt-cdn.net/images/2024-01-03-14-04-16-843-33300229c7.png)

Timeframe showing the last update of a third-party vulnerability

Сведения об изменении статуса можно найти на странице сведений об уязвимости в разделе **Vulnerability evolution** > **Latest events**.

![Latest events for third-party vulnerabilities](https://dt-cdn.net/images/2024-01-03-14-05-01-801-d169aa9489.png)

Latest events for third-party vulnerabilities

Изменение статуса происходит в следующих случаях:

* Уязвимость устранена или повторно открыта
* Уязвимость заглушена или снята с заглушки
* Оценка риска изменилась
* Обнаружены новые атаки на уязвимость

В примере ниже прошло 23 минуты и семь секунд с момента обнаружения новых атак.

![Timeframe showing the last update of a code-level vulnerability](https://dt-cdn.net/images/2024-01-03-13-23-32-1109-5f0b2f3bca.png)

Timeframe showing the last update of a code-level vulnerability

Сведения об изменении статуса можно найти на странице сведений об уязвимости в разделе **Vulnerability evolution** > **Latest events**.

![Latest events for code-level vulnerabilities](https://dt-cdn.net/images/2024-01-03-13-32-48-797-a4a90a6804.png)

Latest events for code-level vulnerabilities

## Различные значения

### Почему значения на странице уязвимостей и в Data Explorer отличаются?

***В разделе **Third-Party Vulnerabilities** на странице со списком сторонних уязвимостей при фильтрации по устранённым уязвимостям за последние семь дней я получаю `3` уязвимости. При использовании метрического запроса (`builtin:security.securityProblem.resolved.new.global`) в Data Explorer я получаю `25`. Почему значения отличаются?***

Список уязвимостей показывает текущее состояние (общее количество уязвимостей, в настоящее время устранённых), тогда как метрический запрос в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрос метрик и преобразование результатов.") показывает изменение со временем.

Например, если две уязвимости несколько раз открываются и закрываются в течение периода времени, диаграмма Data Explorer показывает только один пик (максимальное значение за период), тогда как страница уязвимостей показывает два (поскольку в настоящее время устранено две уязвимости).

Чтобы узнать, сколько уязвимостей было устранено за данный период с помощью метрического запроса:

1. В Data Explorer установите тип визуализации `Single value`.
2. Разверните **Settings** и установите **Fold transformation** на `Value`.

   Это покажет, сколько раз уязвимости были устранены в течение выбранного периода.

![example Data Explorer fold transformation setting](https://dt-cdn.net/images/2023-06-15-09-41-13-1626-bcb5aa24fb.png)

example Data Explorer fold transformation setting

### Почему значения на страницах сторонних уязвимостей и сведений об уязвимости отличаются?

Существуют две возможные причины несоответствия значений на этих страницах:

* [Различное количество затронутых объектов](#different-affected-entities)
* [Различные факторы риска](#different-risk-factors)

#### Различное количество затронутых объектов

В разделе **Third-Party Vulnerabilities** количество затронутых объектов (групп процессов или хостов) на странице со списком сторонних уязвимостей (в столбце **Affected entities** для конкретной уязвимости) может отличаться от числа затронутых объектов на странице сведений об уязвимости по следующим причинам:

* На странице со списком сторонних уязвимостей:

  + Затронутые объекты не фильтруются по зоне управления.
  + Расчёты выполняются каждые 15 минут.
* На странице сведений об уязвимости:

  + Затронутые объекты фильтруются по зоне управления.
  + Учитываются актуальные данные.

#### Различные факторы риска

В разделе **Third-Party Vulnerabilities** оценка факторов риска (`Public exploit`, `Public internet exposure`, `Reachable data assets`, `Vulnerable functions in use`) в инфографике на странице сведений об уязвимости и в столбце **Davis Security Score** на странице со списком уязвимостей может отличаться от оценки факторов риска в разделе **Vulnerability details** на странице сведений об уязвимости по следующей причине:

Для инфографики и столбца **Davis Security Score** расчёты выполняются каждые 15 минут.
Для раздела **Vulnerability details** учитываются актуальные данные.

### Почему у моей уязвимости другая оценка риска и Davis Security Score, чем у затронутых объектов?

Уязвимость является агрегацией всех затронутых объектов в вашей среде; поэтому она может иметь отличные от них значения (оценку риска и Davis Security Score). Например, оценка риска затронутого объекта может быть `8.0`, тогда как оценка агрегированной уязвимости — `9.0`. При этом, если хотя бы один затронутый объект открыт в интернет, агрегированная уязвимость также считается открытой в интернет.

### Почему в производственной и непроизводственной средах отображаются разные уязвимости?

Одинаковые уязвимости в двух средах возможны только при полном совпадении всех следующих параметров в обеих средах:

* Развёртывание (включая версию OneAgent)
* Настройки
* Использование приложения
* Трафик

## Доступность из публичного интернета

### Как определяется доступность из публичного интернета?

На хостах Linux при отсутствии информации (что может произойти в различных режимах мониторинга или при возникновении ошибки) доступность из публичного интернета определяется через eBPF. Возможные состояния: `Public network` и `Not detected`.

Режим Full-Stack Monitoring

Режим Infrastructure Monitoring и Discovery mode

Для определения доступности из публичного интернета Dynatrace:

1. Оценивает все IP-адреса, обнаруженные за последний час.
2. Отбрасывает диапазоны приватных IP-адресов.
3. Группирует оставшиеся IP-адреса по подсети.

Как только соответствующие подсети достигают определённого (низкого) порога, фиксируется доступность из публичного интернета.

Доступность из публичного интернета не может быть оценена на операционных системах, отличных от Linux; в этом случае состояние — `Not available`.

## Уязвимые библиотеки

### Обнаруживает ли Dynatrace уязвимые библиотеки, которые не используются?

Runtime Vulnerability Analytics ориентирован на аспект среды выполнения и предоставляет приоритизированный список уязвимостей, актуальных для работающих сред. С этой целью Dynatrace сообщает только об активно используемых библиотеках.

### Где можно увидеть происхождение уязвимой библиотеки?

На страницах отслеживания устранения для групп процессов и процессов, затронутых уязвимостью, можно увидеть, откуда был загружен программный компонент.

Эта функция доступна для уязвимых программных компонентов Java, .NET, Node.js, Python и Go.

Для отображения происхождения программных компонентов .NET требуется минимальная версия OneAgent 1.301+.

Пример:

![load-origins-pg](https://dt-cdn.net/images/2023-08-21-15-09-46-1812-3f3a0b8200.png)

load-origins-pg

Для получения инструкций по навигации см. раздел [Отслеживание устранения](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Отслеживание прогресса устранения уязвимостей.").

## Уязвимые функции

### Как определяются уязвимые функции?

* Если Dynatrace Vulnerability feed предоставляет информацию об уязвимой функции и мониторинг OneAgent для уязвимых функций Java включён, OneAgent определяет, используется ли уязвимая функция.
* Если Dynatrace Vulnerability feed предоставляет информацию об уязвимой функции, но функция OneAgent отключена, количество уязвимых функций отображается как **Not available**.

Подробнее о Dynatrace Vulnerability feed см. в разделе [Фиды сторонних уязвимостей](/managed/secure/application-security/vulnerability-analytics/vulnerability-evaluation#vulnerability-feeds "Изучите механизм генерации уязвимостей в Dynatrace.").

### Почему нет информации об уязвимых функциях?

Существуют два случая, когда информация об уязвимых функциях недоступна:

* Команда исследования безопасности Dynatrace не предоставила информацию об уязвимых функциях.
* Для runtime-уязвимостей на основе NVD feed.

### Почему нет данных об уязвимых функциях?

* После [включения Third-party Vulnerability Analytics](/managed/secure/application-security/vulnerability-analytics#enable-tpva "Мониторинг уязвимостей сторонних библиотек.") может потребоваться некоторое время (не более одного часа) до отображения данных об уязвимых функциях.
* Мониторинг OneAgent для уязвимых функций Java отключён. Для включения см. раздел [Включение мониторинга OneAgent для уязвимых функций Java](/managed/secure/application-security/vulnerability-analytics#vulnerable-function "Мониторинг уязвимостей сторонних библиотек.").

  Функция OneAgent должна быть включена для всех процессов, затронутых уязвимостью.
* Ни одна из уязвимых функций не содержится в используемой версии сторонних библиотек (программных компонентов).
* Команда исследования безопасности Dynatrace не предоставила информацию об уязвимых функциях.
* Необходимо перезапустить процессы, затронутые уязвимостью, для получения обновлённой информации. Подробнее см. в разделе [FAQ: Как узнать, устарела ли информация об уязвимых функциях?](/managed/secure/faq#outdated-vulnerable-functions "Часто задаваемые вопросы о Dynatrace Application Security.").

#### Как определить, какие процессы нужно перезапустить?

Если на странице сведений об уязвимости отображается уведомление **Restart required**, выполните следующие шаги:

1. В карточке [**Process group overview**](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#pg "Мониторинг проблем безопасности сторонних библиотек.") нажмите **View all process groups**.
2. Отфильтруйте по `Vulnerable functions: Restart required`.
3. Для каждой из полученных групп процессов нажмите **Details**, затем выберите ссылку в уведомлении **Restart required** для перехода к списку процессов, требующих перезапуска.

![Select the processes that need to be restarted](https://dt-cdn.net/images/2023-12-18-13-43-19-539-175d9b3394.png)

Select the processes that need to be restarted

Пример результата:

![Filter by Vulnerable functions: Restart required](https://dt-cdn.net/images/2023-12-18-13-07-00-1594-7f9f9381c3.png)

Filter by Vulnerable functions: Restart required

После перезапуска процесса обновлённые данные отображаются примерно через минуту.

Эта функция работает только при [включённом мониторинге OneAgent для уязвимых функций Java](/managed/secure/application-security/vulnerability-analytics#vulnerable-function "Мониторинг уязвимостей сторонних библиотек.").

#### Почему процесс требует перезапуска после того, как я уже его перезапустил?

Если вы выполнили [инструкции](#which-process-to-restart) по определению нужного процесса и перезапустили его, но процесс всё ещё требует перезапуска (то же уведомление **Restart required** отображается, информация об уязвимых функциях не изменилась), это может происходить в Kubernetes-развёртываниях без постоянного хранилища.

Для решения этой проблемы добавьте постоянное хранилище, подключив файловое хранилище, которое не удаляется при перезапуске подов.

### Как узнать, устарела ли информация об уязвимых функциях, и что с этим делать?

OneAgent версии 1.279+

Если появилась новая информация об уязвимых функциях уязвимости, требуется перезапуск процесса, чтобы OneAgent мог получить и использовать новые данные.
В этом случае уведомление или значок **Restart required** отображается на:

* Странице сведений об уязвимости (в разделе [**Vulnerability details**](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#vulnerability-details "Мониторинг проблем безопасности сторонних библиотек.") > **Vulnerable functions**)

  ![Restart required on a vulnerability details page](https://dt-cdn.net/images/2023-12-18-12-45-12-776-d39b330fe4.png)

  Restart required on a vulnerability details page
* Странице [обзора групп процессов, связанных с уязвимостью](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#pg "Отслеживание прогресса устранения уязвимостей.") (в разделе [**Details**](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#details "Отслеживание прогресса устранения уязвимостей.") > **Risk assessment**)

  ![Restart required on the process groups overview related to a vulnerability](https://dt-cdn.net/images/2023-12-18-12-41-00-1597-34af91fcf3.png)

  Restart required on the process groups overview related to a vulnerability
* [Списке процессов, связанных с уязвимостью](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking#process "Отслеживание прогресса устранения уязвимостей.") (в разделе **Vulnerable functions** и **Details**)

  ![Restart required on the process list related to a vulnerability](https://dt-cdn.net/images/2023-12-18-12-37-41-1570-47da22adc2.png)

  Restart required on the process list related to a vulnerability

## Фиды уязвимостей

### Какие фиды использует Dynatrace для уязвимостей?

Для получения данных об уязвимостях Dynatrace Application Security использует [Dynatrace Vulnerability feed](https://dt-url.net/o303679) или [NVD](https://nvd.nist.gov/vuln) в зависимости от уязвимого компонента.

Подробнее см. в разделе [Фиды сторонних уязвимостей](/managed/secure/application-security/vulnerability-analytics/vulnerability-evaluation#vulnerability-feeds "Изучите механизм генерации уязвимостей в Dynatrace.").

## Механизм блокировки атак

### Как именно Dynatrace блокирует атаки?

Выбор `Block attack` для атаки не блокирует её автоматически; он переводит на страницу настроек, где можно создать правило мониторинга для блокировки таких атак в будущем. Dynatrace настроен на блокировку будущих ситуаций эксплуатации, а не текущих.
Запрос (поток) с эксплойтом вызывает исключение в выполняемом коде. Все остальные пользователи, не осуществляющие атаку, не затрагиваются.  
Dynatrace обнаруживает, когда предоставленный пользователем payload атаки достигает строки кода, использующей небезопасный способ:

* Обращения к базе данных (SQL injection)
* Обращения к операционной системе (command injection)
* Выполнения JNDI lookup (JNDI injection, например Log4Shell)
* Выполнения HTTP-запроса (SSRF)

Уязвимость выявляется как при атаке, так и без неё. Если данные, отправленные клиентом, включают признаки атаки, достигающей этой строки кода, это расценивается как эксплойт, и Dynatrace отправляет оповещение или блокирует его.

Подробнее о механизме Runtime Application Protection см. в разделе [Принцип работы](/managed/secure/application-security/application-protection#mechanism "Настройка Dynatrace Runtime Application Protection.").

### Как определяется IP-адрес злоумышленника?

В Runtime Application Protection для определения IP-адреса злоумышленника Dynatrace проверяет:

* Определённые HTTP-заголовки, такие как `X-Client-IP` или `X-Forwarded-For`.

* IP-адрес клиента соединения сокета (если вышеуказанные HTTP-заголовки недоступны).

  Подробнее см. в разделе [Определение IP-адреса клиента](/managed/secure/application-security/application-protection/manage-attacks#client-ip-address "Мониторинг атак на код приложения.").

## Хранение данных

### Каков период хранения данных для уязвимостей, событий и атак?

Информацию о том, как данные, связанные с безопасностью, хранятся в Dynatrace, см. в разделе [Периоды хранения данных](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Проверьте сроки хранения различных типов данных.").

## Потребление

### Как проверить потребление хостов?

* При использовании [Dynatrace Platform Subscription](/managed/license "О модели лицензирования Dynatrace Platform Subscription.") см.:

  + [Расчёт потребления Runtime Vulnerability Analytics](/managed/license/capabilities/application-security/runtime-vulnerability-analytics "Узнайте о выставлении счётов за потребление RVA.")
  + [Расчёт потребления Runtime Application Protection](/managed/license/capabilities/application-security/runtime-application-protection "Узнайте о выставлении счётов за потребление RAP.")
  + [Расчёт потребления Security Posture Management](/managed/license/capabilities/application-security/security-posture-management "Узнайте о выставлении счётов за потребление SPM.")
* При использовании [классического лицензирования Dynatrace](/managed/license/monitoring-consumption-classic "Расчёт потребления мониторинга при классическом лицензировании.") см. раздел [Влияние функций на потребление мониторинга](/managed/license/monitoring-consumption-classic/application-security-units#how-capabilities-affect-monitoring-consumption "Расчёт потребления Application Security.").

Чтобы увидеть, какие хосты потребляют DPS/ASU, в разделе **Security Overview** перейдите в секцию **Host coverage** для сторонних уязвимостей и уязвимостей на уровне кода и нажмите **Monitored hosts**. Полученный список хостов — это хосты в вашей среде, потребляющие DPS/ASU.
Подробнее см. в разделе [Покрытие хостов](/managed/secure/application-security/vulnerability-analytics/application-security-overview#host-coverage "Обзор проблем безопасности сторонних библиотек.").

### Почему Application Security всё ещё показывает использование, хотя я отключил RVA?

***Я отключил Third-party и Code-level Vulnerability Analytics. Мой хост показывает «Not analyzed», но использование всё ещё отображается в подписке. Почему?***

Это поведение применимо как к [классическому лицензированию Dynatrace (ASU)](/managed/license/monitoring-consumption-classic/application-security-units#how-capabilities-affect-monitoring-consumption "Расчёт потребления Application Security."), так и к [Dynatrace Platform Subscription (DPS)](/managed/license/capabilities/application-security/runtime-application-protection "Расчёт потребления RAP.").

Проверьте, включён ли Runtime Application Protection (RAP). RAP зависит от Runtime Vulnerability Assessment (RVA) для определения уязвимости, которую пытается эксплуатировать атака. Поскольку RAP не может работать без RVA, любой хост с включённым RAP всегда будет потреблять ASU/DPS как для RAP, так и для RVA — даже если глобальные переключатели обнаружения сторонних уязвимостей или уязвимостей на уровне кода отключены.