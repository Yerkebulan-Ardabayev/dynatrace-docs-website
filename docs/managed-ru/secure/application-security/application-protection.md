---
title: Runtime Application Protection
source: https://docs.dynatrace.com/managed/secure/application-security/application-protection
scraped: 2026-05-12T11:13:50.353848
---

# Runtime Application Protection

# Runtime Application Protection

* How-to guide
* Updated on Feb 23, 2026

Что вы найдёте на этой странице

* [Обзор возможностей Runtime Application Protection](#capabilities)
* [Как RAP обнаруживает и анализирует атаки](#mechanism)
* [Предварительные требования](#prereq)
* [Права доступа](#permissions)
* [Поддерживаемые технологии](#tech)
* [Включение и настройка RAP](#start)
* [Следующие шаги после настройки RAP](#next)
* [Лицензирование RAP](#consumption)

Dynatrace Runtime Application Protection использует аналитику на уровне кода и анализ транзакций для автоматического обнаружения и блокировки попыток эксплуатации ваших приложений в режиме реального времени.

## Возможности

* Обнаружение атак SQL injection, JNDI injection, command injection и SSRF
* Видимость на уровне кода, обеспечиваемая OneAgent
* Производительность, подходящая для production-среды
* Настраиваемая автоматическая блокировка обнаруженных атак
* Защита веб-приложений и API
* Высокая точность оповещений с богатым контекстом для оптимизации работы команды

## Принцип работы

Runtime Application Protection (RAP) использует инструментацию во время выполнения для обнаружения и опциональной блокировки попыток эксплуатации. Когда ваше приложение получает веб-запрос, [Dynatrace OneAgent](/managed/platform/oneagent "Узнайте о возможностях мониторинга OneAgent.") отслеживает пользовательский ввод и анализирует его взаимодействие с чувствительными путями кода — SQL-запросами, командами ОС или JNDI-поиском. Если поведение соответствует известному шаблону атаки, Dynatrace сообщает об этом как об угрозе безопасности. Если блокировка атак включена, OneAgent генерирует исключение для остановки вредоносного запроса до его выполнения. RAP является облегчённым и безопасным для использования в production-средах.

Краткое руководство см. в [учебном материале Dynatrace University по Runtime Application Protection](https://university.dynatrace.com/learn/course/external/view/elearning/89/runtime-application-protection).

## Предварительные требования

Перед началом работы убедитесь, что ваша среда соответствует необходимым требованиям:

* Вы используете поддерживаемую версию Dynatrace. Проверьте [примечания к выпускам](/managed/whats-new "Читайте новости продукта и примечания к выпускам, узнавайте о новых темах документации.") для получения информации о поддерживаемых версиях.
* Для правильной работы Runtime Application Protection убедитесь, что глубокий мониторинг включён в **Settings** > **Processes and containers** > **Process group monitoring**.

  Для технологий .NET, Go и Python, для которых автоматический глубокий мониторинг отключён, необходимо вручную включить глубокий мониторинг на каждом хосте. Подробнее см. в разделе [Глубокий мониторинг процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Способы настройки мониторинга групп процессов").
* Кластер Dynatrace Managed должен быть подключён к [Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control проактивно отслеживает ваш Managed Cluster, предоставляет обновления программного обеспечения и обеспечивает безопасность и надёжность установки.").

Application Security не поддерживается

* В оффлайн-режиме.
* В мобильном приложении Dynatrace ([iOS](https://itunes.apple.com/app/ruxit/id1567881685) или [Android](https://play.google.com/store/apps/details?id=com.dynatrace.alert)).

## Права доступа

Необходимо назначить разрешение **Manage security problems** группам пользователей, которым будет разрешено просматривать атаки и управлять ими.

Подробнее см. в разделах [Разрешения среды](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions#environment "Узнайте о поддерживаемых разрешениях и политиках, о том, как назначать их группам и управлять пользователями и группами.") и [Разрешения management zone](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions#mz "Узнайте о поддерживаемых разрешениях и политиках, о том, как назначать их группам и управлять пользователями и группами.").

## Поддерживаемые технологии

Dynatrace обнаруживает атаки SQL injection, JNDI injection, command injection и SSRF для следующих технологий.

| Технология | Минимальная версия OneAgent | SQL injection | Command injection | JNDI injection | SSRF |
| --- | --- | --- | --- | --- | --- |
| Java 8 или выше[1](#fn-1-1-def) | 1.241 |  |  |  |  |
| .NET[2](#fn-1-2-def)'[3](#fn-1-3-def) | 1.289 |  |  |  |  |
| Go[3](#fn-1-3-def) | 1.311 |  |  |  |  |

1

Поддерживается только на системах Windows x86 и Linux x86.

2

Поддерживаются только .NET Framework 4.5, .NET Core 3.0 или выше и 64-разрядные процессы.

3

Для технологий .NET и Go, для которых автоматический глубокий мониторинг отключён, необходимо вручную включить глубокий мониторинг на каждом хосте. Подробнее см. в разделе [Глубокий мониторинг процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Способы настройки мониторинга групп процессов").

## Начало работы

Чтобы настроить Runtime Application Protection, следуйте инструкциям ниже.

Активация Runtime Application Protection

Обратитесь к эксперту Dynatrace через чат для активации Runtime Application Protection.

Включение Runtime Application Protection

Чтобы глобально включить Runtime Application Protection в вашей среде

1. Перейдите в **Settings** и выберите **Application security** > **Application Protection** > **General settings**.
2. Выберите **Enable Runtime Application Protection**.
3. Нажмите **Save changes**.
4. Перезапустите процессы.

Настройка глобального управления атаками

Чтобы определить глобальное управление атаками для всех групп процессов

1. Перейдите в **Settings** и выберите **Application security** > **Application Protection** > **General settings**.
2. В разделе **Define global incoming attack control** выберите желаемый режим для каждой технологии:

   * **Off; incoming attacks NOT detected or blocked.** — Мониторинг отключён; атаки для выбранной технологии не обнаруживаются и не блокируются.
   * **Monitor; incoming attacks detected only.** — Мониторинг включён; атаки для выбранной технологии не блокируются.
   * **Block; incoming attacks detected and blocked.** — Мониторинг включён; атаки для выбранной технологии блокируются во время выполнения.

Если вы определяете [пользовательские правила мониторинга](/managed/secure/application-security/application-protection/application-protection-rules#handling-rules "Создание, изменение и удаление правил для конкретных атак.") для определённых групп процессов или типов уязвимостей, эти правила переопределяют глобальное управление атаками для выбранной технологии, и Runtime Application Protection продолжает отслеживать атаки в соответствии с вашими правилами.

3. Нажмите **Save**.

Включение мониторинга OneAgent

1. Перейдите в **Settings** и выберите **Preferences** > **OneAgent features**.
2. Отфильтруйте по `code-level attack evaluation` и включите функцию для технологий, которые необходимо отслеживать.
3. Нажмите **Save changes**.
4. Перезапустите процессы.

OneAgent версии 1.309 Для обнаружения SSRF-атак необходимо также включить SSRF attack evaluation. Инструкции приведены ниже.

1. Перейдите в **Settings** и выберите **Preferences** > **OneAgent features**.
2. Найдите и включите `Java SSRF code-level vulnerability and attack evaluation`.
3. Нажмите **Save changes**.
4. Перезапустите процессы.

## Следующие шаги

После настройки Runtime Application Protection вы можете:

* [Отслеживать атаки](/managed/secure/application-security/application-protection/manage-attacks "Мониторинг атак на код вашего приложения.")
* [Настраивать правила защиты от атак](/managed/secure/application-security/application-protection/application-protection-rules "Создание, изменение и удаление правил для конкретных атак.")
* [Создавать уведомления безопасности](/managed/secure/application-security/application-protection/security-notifications-rap "Интеграция уведомлений безопасности об атаках с Dynatrace.")
* [Использовать доступные метрики уязвимостей](/managed/secure/application-security/application-protection/app-sec-metrics "Просмотр доступных метрик Application Security для Dynatrace Runtime Application Protection.")

## Потребление лицензий

Потребление Runtime Application Protection зависит от вашей лицензионной модели Dynatrace:

* [Dynatrace Platform Subscription (DPS)](/managed/license "О лицензионной модели Dynatrace Platform Subscription (DPS) для всех возможностей Dynatrace."): измеряется в ГиБ-часах. Подробнее см. в разделе [Расчёт потребления Runtime Application Protection (RAP) (DPS)](/managed/license/capabilities/application-security/runtime-application-protection "Узнайте, как рассчитывается потребление возможности Runtime Application Protection (RAP) DPS.").
* [Классическое лицензирование Dynatrace](/managed/license/monitoring-consumption-classic "Понимание расчёта потребления мониторинга Dynatrace при классическом лицензировании."): измеряется в единицах Application Security (ASU). Подробнее см. в разделе [Мониторинг Application Security (ASU)](/managed/license/monitoring-consumption-classic/application-security-units "Понимание расчёта потребления Dynatrace Application Security и Runecast SPM.").

## Связанные темы

* [FAQ по Application Security](/managed/secure/faq "Часто задаваемые вопросы о Dynatrace Application Security.")