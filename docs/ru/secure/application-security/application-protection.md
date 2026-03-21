---
title: Защита приложений в runtime
source: https://www.dynatrace.com/docs/secure/application-security/application-protection
scraped: 2026-03-06T21:17:12.113649
---

# Runtime Application Protection


* Latest Dynatrace
* How-to guide

Что вы найдёте на этой странице

* [Изучите возможности Runtime Application Protection](#capabilities)
* [Как RAP обнаруживает и анализирует атаки](#mechanism)
* [Ознакомьтесь с предварительными требованиями](#prereq)
* [Проверьте поддерживаемые технологии](#tech)
* [Как включить и настроить RAP](#start)
* [Что делать с RAP дальше](#next)
* [Узнайте о лицензировании RAP](#consumption)

Dynatrace Runtime Application Protection использует анализ на уровне кода и анализ транзакций для автоматического обнаружения и блокировки попыток эксплуатации ваших приложений в режиме реального времени.

## Возможности

* Обнаружение атак SQL-инъекций, JNDI-инъекций, инъекций команд и SSRF
* Видимость на уровне кода, обеспечиваемая OneAgent
* Минимальное влияние на производительность, готовое к использованию в продуктивных средах
* Настраиваемая автоматическая блокировка обнаруженных атак
* Защита веб-приложений и API
* Высокая точность оповещений с богатым контекстом для оптимизации работы вашей команды

## Как это работает

[Runtime Application Protection (RAP)](application-protection.md "Настройте Dynatrace Runtime Application Protection для мониторинга атак и уязвимостей на уровне кода, генерируемых атаками.") использует инструментирование среды выполнения для обнаружения и, при необходимости, блокировки попыток эксплуатации. Когда ваше приложение получает веб-запрос, [Dynatrace OneAgent](../../platform/oneagent.md "Узнайте о возможностях мониторинга OneAgent.") отслеживает пользовательский ввод и анализирует его взаимодействие с критическими путями кода, такими как SQL-запросы, команды ОС или JNDI-запросы. Если поведение соответствует известному шаблону атаки, Dynatrace сообщает об этом как о результате обнаружения безопасности. Если блокировка атак включена, OneAgent генерирует исключение для остановки вредоносного запроса до его выполнения. RAP является легковесным и безопасным для использования в продуктивных средах.

## Предварительные требования

Перед началом работы убедитесь, что ваша среда соответствует необходимым требованиям:

* Вы используете поддерживаемую версию Dynatrace. Ознакомьтесь с [заметками о выпуске](../../whats-new.md "Ознакомьтесь с новостями продукта и заметками о выпуске, узнайте, какие темы документации являются новыми.") для актуальных поддерживаемых версий.
* Для правильной работы Runtime Application Protection убедитесь, что глубокий мониторинг включён в **Settings** > **Process and contextualize** > **Process groups** > **Process group monitoring**.

  Для технологий .NET, Go и Python, для которых автоматический глубокий мониторинг отключён, необходимо вручную включить глубокий мониторинг на каждом хосте. Подробнее см. [Глубокий мониторинг процессов](../../observe/infrastructure-observability/process-groups/configuration/pg-monitoring.md "Способы настройки мониторинга групп процессов").

## Поддерживаемые технологии

Dynatrace обнаруживает атаки SQL-инъекций, JNDI-инъекций, инъекций команд и SSRF в следующих технологиях.

| Технология | Минимальная версия OneAgent | SQL-инъекция | Инъекция команд | JNDI-инъекция | SSRF |
| --- | --- | --- | --- | --- | --- |
| Java 8 или выше[1](#fn-1-1-def) | 1.241 |  |  |  |  |
| .NET[2](#fn-1-2-def)'[3](#fn-1-3-def) | 1.289 |  |  |  |  |
| Go[3](#fn-1-3-def) | 1.311 |  |  |  |  |

1

Поддерживается только на системах Windows x86 и Linux x86.

2

Поддерживаются только .NET Framework 4.5, .NET Core 3.0 или выше и 64-битные процессы.

3

Для технологий .NET и Go, для которых автоматический глубокий мониторинг отключён, необходимо вручную включить глубокий мониторинг на каждом хосте. Подробнее см. [Глубокий мониторинг процессов](../../observe/infrastructure-observability/process-groups/configuration/pg-monitoring.md "Способы настройки мониторинга групп процессов").

## Начало работы

Чтобы настроить Runtime Application Protection, следуйте приведённым ниже инструкциям.

Для использования функций предварительного просмотра, пожалуйста, свяжитесь с экспертом по продуктам Dynatrace через чат, чтобы **активировать Runtime Application Protection** перед продолжением.

Включение Runtime Application Protection

Чтобы включить Runtime Application Protection глобально в вашей среде

1. Перейдите в **Settings** > **Analyze and alert** > **Application security** > **Application protection (New**).
2. Включите Runtime Application Protection.
3. Нажмите **Enable**.
4. Перезапустите ваши процессы.

Определение глобального управления атаками

Чтобы определить глобальное управление атаками для всех групп процессов

1. Перейдите в **Settings** > **Analyze and alert** > **Application security** > **Application protection (New)** > **Monitoring rules** > **Default rules**.
2. Отредактируйте управление атаками для каждой технологии:

* **Off; incoming attacks NOT detected or blocked.** -- Мониторинг отключён; атаки по выбранной технологии не регистрируются.
* **Monitor; incoming attacks detected only.** -- Мониторинг включён; атаки по выбранной технологии не блокируются.
* **Block; incoming attacks detected and blocked.** -- Мониторинг включён; атаки по выбранной технологии блокируются во время выполнения.

Если вы определите [пользовательские правила мониторинга](application-protection/application-protection-rules.md#handling-rules "Создание, изменение и удаление правил для конкретных атак.") на основе определённых групп процессов или типов уязвимостей, пользовательские правила переопределяют глобальное управление атаками для выбранной технологии, и Runtime Application Protection продолжает мониторинг атак на основе ваших правил.

3. Нажмите **Save**.
4. Перезапустите ваши процессы.

Включение мониторинга OneAgent

1. Перейдите в **Settings** и выберите **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Отфильтруйте по `code-level attack evaluation` и включите функцию для технологий, которые вы хотите мониторить.
3. Нажмите **Save changes**.
4. Перезапустите ваши процессы.

OneAgent версии 1.309. Для обнаружения атак SSRF необходимо также включить оценку атак SSRF. Инструкции приведены ниже.

1. Перейдите в **Settings** и выберите **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Найдите и включите `Java SSRF code-level vulnerability and attack evaluation`.
3. Нажмите **Save changes**.
4. Перезапустите ваши процессы.

## Дальнейшие действия

После настройки Runtime Application Protection вы можете

* Оценивать, сортировать и исследовать результаты с помощью [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](../threats-and-exploits.md "Анализируйте, сортируйте и исследуйте результаты обнаружения и оповещения.").
* [Настроить правила мониторинга Runtime Application Protection](application-protection/application-protection-rules.md "Создание, изменение и удаление правил для конкретных атак.").

## Потребление

Потребление Runtime Application Protection зависит от вашей модели лицензирования Dynatrace:

* [Dynatrace Platform Subscription (DPS)](../../license.md "О Dynatrace Platform Subscription (DPS), модели лицензирования для всех возможностей Dynatrace."): измеряется в ГиБ-часах. Подробнее см. [Расчёт потребления Runtime Application Protection (RAP) (DPS)](../../license/capabilities/application-security/runtime-application-protection.md "Узнайте, как рассчитывается и оплачивается потребление возможности Runtime Application Protection (RAP) DPS.").
* [Классическое лицензирование Dynatrace](../../license/monitoring-consumption-classic.md "Узнайте, как рассчитывается потребление мониторинга Dynatrace при классическом лицензировании."): измеряется в единицах Application Security (ASU). Подробнее см. [Мониторинг Application Security (ASU)](../../license/monitoring-consumption-classic/application-security-units.md "Узнайте, как рассчитывается потребление Dynatrace Application Security и Runecast SPM.").

## Связанные темы

* [Часто задаваемые вопросы по Application Security](../faq.md "Часто задаваемые вопросы о Dynatrace Application Security.")
