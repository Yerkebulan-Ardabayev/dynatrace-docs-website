---
title: Monitor suspicious sign-in activity with Dynatrace
source: https://www.dynatrace.com/docs/secure/use-cases/monitor-sign-in-activity
scraped: 2026-03-06T21:15:04.248703
---

# Мониторинг подозрительной активности входа с помощью Dynatrace

# Мониторинг подозрительной активности входа с помощью Dynatrace

* Latest Dynatrace
* Руководство
* Обновлено 28 января 2026

По мере внедрения организациями облачных технологий мониторинг логов входа в систему становится критически важным для обнаружения аномалий, расследования подозрительной активности и обеспечения соответствия нормативным требованиям. Видимость поведения при входе в реальном времени помогает быстро реагировать на риски безопасности, защищать идентификацию пользователей и обеспечивать безопасность критически важных ресурсов. Это также предоставляет практическую информацию о скомпрометированных учётных записях, злоумышленниках внутри организации и паттернах поведения пользователей, помогая принимать стратегические решения по управлению доступом, политикам устройств и использованию приложений.

Хотя следующий сценарий фокусируется на логах Microsoft Entra ID в качестве примера, описанный подход универсально применим к любому облачному провайдеру, провайдеру доступа или идентификации, интегрированному с Dynatrace. Это стало возможным благодаря Semantic Dictionary и стандартизированному отображению данных на определённую [семантическую модель](/docs/semantic-dictionary/model/log "Познакомьтесь с моделями Semantic Dictionary, связанными с анализом логов.").

При условии, что логи входа от поддерживаемого провайдера идентификации загружены в Dynatrace, вы можете следовать описанным ниже шагам для эффективного мониторинга этих логов.

## Целевая аудитория

Администраторы безопасности и команды безопасности, отвечающие за защиту облачной среды и активности пользователей организации.

## Сценарий

Ваша организация использует Microsoft Entra ID в качестве централизованного провайдера идентификации, предоставляющего пользователям единый вход (SSO) в различные приложения и сервисы компании.
Логи входа Microsoft Entra ID пересылаются в Dynatrace и хранятся в Grail для обеспечения более глубокой видимости активности пользователей, создавая единый центр данных для мониторинга и анализа.

Как администратор безопасности, ваша обязанность —

* Защищать идентификацию пользователей вашей организации
* Мониторить доступ пользователей и отслеживать паттерны для быстрого обнаружения необычного поведения
* Выявлять и расследовать потенциальные угрозы или аномальные события входа
* Оперативно начинать действия по реагированию на инциденты для минимизации ущерба в случае компрометации учётной записи пользователя

### Цели

* Достичь всеобъемлющей видимости облачной среды и активности пользователей через единый интерфейс.
* Продемонстрировать, как мониторить логи входа и активность пользователей Microsoft Entra ID для обнаружения потенциальных проблем безопасности и аномального поведения.

## Предварительные требования

* Знание [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.") и [как использовать DQL-запросы](/docs/platform/grail/dynatrace-query-language/dql-guide "Узнайте, как работает DQL и каковы ключевые концепции DQL.").
* Отправка логов входа Microsoft Entra ID в Dynatrace. Есть два варианта потоковой передачи логов:

  + [Azure Native Dynatrace Service](/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration "Настройте и сконфигурируйте среду Dynatrace SaaS через Azure Marketplace.")
  + [Azure Log Forwarder](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Используйте пересылку логов Azure для загрузки логов Azure.")
* Следуйте инструкциям в разделе [Создание конвейера для обработки](/docs/platform/openpipeline/use-cases/tutorial-technology-processor#pipeline "Настройте конвейер обработки для структурирования технологических логов в соответствии с Dynatrace Semantic Dictionary.") для настройки среды OpenPipeline. Выберите **Azure Entra ID Audit Logs** в качестве встроенного процессора.

## Начало работы

1. Импорт дашборда

Используйте наш пример дашборда для просмотра активности входа пользователей в ваших облачных средах.

1. Скачайте [пример дашборда с GitHub](https://dt-url.net/ur03wvb).
2. Откройте [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени."), выберите ![Import](https://dt-cdn.net/images/dashboards-app-dashboards-page-import-6a06e645df.svg "Import") **Upload**, затем выберите скачанный файл.

2. Настройка фильтров

1. В **Product** отфильтруйте по `Azure` для отображения логов входа Microsoft Entra ID, поступающих из подключённой среды Azure.
2. Используйте селектор временного диапазона для сужения расследования до релевантных инцидентов, выявления трендов или аномалий в этом окне и эффективного мониторинга активности пользователей или подозрительного поведения в критические моменты.

   ![filtering](https://dt-cdn.net/images/2025-03-26-18-28-55-1865-3328587bcd.png)
3. Для более точного расследования рассмотрите настройку дополнительных фильтров. Например:

   * **User** — для анализа индивидуальных трендов входа, устройств и местоположений конкретных пользователей, что помогает выявить необычные паттерны доступа или целевые атаки.
   * **User IP address** — для расследования активности с определённых IP-адресов, обнаружения повторяющихся неудачных входов или необычных источников доступа.
   * **Device OS** — для отслеживания операционных систем, используемых при входе, что помогает обнаружить устаревшие или неавторизованные устройства.
   * **Country** — для проверки входов по географическому расположению с целью обнаружения доступа из неожиданных или ограниченных регионов.
   * **Target service** — для определения, к каким сервисам или приложениям осуществляется доступ, что полезно для мониторинга конфиденциальных ресурсов.
   * **Result code** — для просмотра результатов попыток входа с целью обнаружения аномалий, таких как чрезмерное количество неудачных попыток, указывающих на потенциальные атаки методом перебора.
   * **Client application** — для определения, какие приложения используются для входа, что полезно для выявления неавторизованного или подозрительного использования приложений.

3. Обзор активности и трендов

В разделе **Sign-in activity monitoring** вы можете

* Анализировать тренды входа
* Определять пиковые периоды активности
* Расследовать паттерны доступа по расположению или IP-адресу

Это позволяет получить чёткое представление о распределении пользователей и быстро обнаружить нерегулярную активность из неожиданных регионов, помогая улучшить безопасность и эффективно реагировать на потенциальные риски.

![An overview dashboard example](https://dt-cdn.net/images/image-50-2540-6620ffd45d.png)

Выполнить запрос

Вы можете воспроизвести график **Sign-in activity outcomes over time** в [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Объедините функциональность Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь информацией из данных наблюдаемости — всё в одном совместном, настраиваемом рабочем пространстве.") с помощью следующего фрагмента DQL:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



| makeTimeseries {



Success = countIf(audit.result=="Succeeded", default:0),



Failure = countIf(audit.result!="Succeeded", default:0)



}, time:audit.time
```

4. Детальный анализ

В разделе **Top sign-in activity breakdown** вы можете изучить детальную информацию об активности входа пользователей и по IP-адресам.

**Пример 1**: В **Top 10 sign-in users** вы можете определить

* Аномалии, такие как блокировки учётных записей или потенциальные атаки методом перебора
* Пользователей с наибольшим количеством попыток входа, категоризированных по успешным и неудачным попыткам
* Пользователей с наибольшим количеством неудачных попыток, с указанием IP-адресов и клиентских приложений

![sign-in users](https://dt-cdn.net/images/2025-03-26-14-46-19-1359-17c6e4d12e.png)

Выполнить запрос

Топ-10 пользователей по входам

Топ-10 пользователей по неудачным попыткам входа

Вы можете воспроизвести график **Top 10 sign-in users** в [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Объедините функциональность Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь информацией из данных наблюдаемости — всё в одном совместном, настраиваемом рабочем пространстве.") с помощью следующего фрагмента DQL:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



| summarize {



Success = countIf(audit.result=="Succeeded" or isNull(result.code)),



Failure = countIf(audit.result!="Succeeded", by:{User=audit.identity



}



| sort Success+Failure desc



| limit 10
```

Вы можете воспроизвести таблицу **Top 10 users by failed sign-in attempts** в [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Объедините функциональность Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь информацией из данных наблюдаемости — всё в одном совместном, настраиваемом рабочем пространстве.") с помощью следующего фрагмента DQL:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



and audit.result!="Succeeded"



| summarize {



Failures = count(),



`Client applications` = collectDistinct(client.app.name),



`IPs` = collectDistinct(client.ip)



}, by:{User=audit.identity}



| sort Failures desc



| limit 10
```

**Пример 2**: В **Top 10 sign-in IPs** вы можете

* Обнаружить необычные паттерны, которые могут указывать на вредоносную активность, например повторяющиеся неудачные попытки с одного IP-адреса или множество пользователей, входящих с одного IP-адреса
* Просмотреть рейтинги IP-адресов с наибольшим количеством попыток входа, а также тех, которые связаны с множеством пользователей или сервисов

![sign-in-ip](https://dt-cdn.net/images/2025-03-26-17-26-56-1644-34f2135bb6.png)

Выполнить запрос

Топ-10 IP-адресов по входам

Топ-10 адресов по неудачным попыткам входа

Вы можете воспроизвести график **Top 10 sign-in IPs** в [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Объедините функциональность Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь информацией из данных наблюдаемости — всё в одном совместном, настраиваемом рабочем пространстве.") с помощью следующего фрагмента DQL:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



| summarize {



Success = countIf(audit.result=="Succeeded" or isNull(result.code)),



Failure = countIf(audit.result!="Succeeded")



}, by:{IP=client.ip}



| sort Success+Failure desc



| limit 10
```

Вы можете воспроизвести таблицу **Top 10 addresses by failed sign-in attempts** в [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Объедините функциональность Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь информацией из данных наблюдаемости — всё в одном совместном, настраиваемом рабочем пространстве.") с помощью следующего фрагмента DQL:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



and audit.result!="Succeeded"



| summarize {



Failures = count(), Users = collectDistinct(audit.identity),



`Target services` = collectDistinct(client.app.name)



}, by:{`Client IP`=client.ip, City=actor.geo.city.name}



| sort Failures desc



| limit 10
```

5. Анализ данных

Dynatrace Intelligence автоматически выявляет аномальные тренды и отклонения в логах входа, значительно повышая способность вашей организации быстро обнаруживать потенциальные угрозы. Dynatrace Intelligence непрерывно анализирует паттерны входа пользователей, предоставляя проактивные оповещения при обнаружении аномалий.

Для обнаружения аномальных пиков в наблюдаемых логах входа с помощью Dynatrace Intelligence

1. Выберите любой из графиков на основе временных рядов, затем выберите **Open with**.

   ![open-with](https://dt-cdn.net/images/sssssss-1102-25711b87e5.png)
2. Выберите **Notebooks**.
3. В открывшемся документе notebook выберите **Options**.
4. На панели **Options** выберите **Analyze and alert** и активируйте анализатор.
5. Выберите анализатор и настройте его параметры.
6. Выберите **Run analysis**.

Например, вы можете выбрать авто-адаптивный порог для применения динамического подхода на основе прошлых трендов входа.

![An example of AI data analysis in the Notebooks app.](https://dt-cdn.net/images/2025-03-27-12-52-08-1920-d8b53c4e4a-1444-3573714c33.png)

## Итоги

Мониторинг активности входа в облачных средах необходим для обнаружения аномалий, защиты критически важных ресурсов и обеспечения соответствия требованиям. Интеграция логов входа в платформу Dynatrace централизует видимость паттернов доступа пользователей. Анализируя такие метрики, как топ пользователей, IP-адреса, клиентские приложения и местоположения, команды безопасности могут быстро выявить подозрительное поведение и устранить потенциальные угрозы. Параметры фильтрации дашборда позволяют проводить целевые расследования, улучшая обнаружение угроз и ускоряя реагирование на инциденты.