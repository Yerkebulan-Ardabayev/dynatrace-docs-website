---
title: Известные решения и обходные пути
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/known-solutions-and-workarounds
scraped: 2026-05-12T11:23:17.169999
---

# Известные решения и обходные пути

# Известные решения и обходные пути

* Чтение: 14 мин
* Обновлено 26 февраля 2024 г.

На этой странице описаны решённые проблемы и способы их устранения, поступившие в службу поддержки Dynatrace.

## OneAgent препятствует запуску Elasticsearch 8.18+

**Проблема:**

OneAgent препятствует запуску Elasticsearch 8.18+

**Решение:**

Подробнее см. [эту страницу](https://community.dynatrace.com/t5/Heads-up-from-Dynatrace/OneAgent-prevents-startup-of-Elasticsearch-8-18/ta-p/278744)

## OneAgent на хосте SAP HANA

**Проблема:**

OneAgent, установленный на хосте HANA, может мешать обновлениям базы данных, если включена автоматическая инъекция процессов (по умолчанию).

**Решение:**

Отключите автоматическую инъекцию процессов для OneAgent, установленного на хосте SAP HANA.

### Отключение автоматической инъекции при установке

Чтобы установить OneAgent с параметрами включения режима Infrastructure Monitoring и отключения инъекции процессов, выполните следующую команду:

```
/bin/sh Dynatrace-OneAgent-Linux-<version>.sh --set-monitoring-mode=infra-only --set-auto-injection-enabled=false
```

### Отключение автоматической инъекции после установки OneAgent

Чтобы отключить автоматическую инъекцию после установки OneAgent:

1. Откройте терминал на хосте HANA.
2. Запустите инструмент командной строки `oneagentctl` со следующими параметрами, чтобы включить режим Infrastructure Monitoring и отключить инъекцию процессов. Команда также перезапустит сервис OneAgent для автоматического применения изменений.

```
./oneagentctl --set-monitoring-mode=infra-only --set-auto-injection-enabled=false --restart-service
```

Подробнее см. [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки.")

#### Веб-интерфейс Dynatrace

1. Перейдите в **Hosts**.
2. Найдите хост HANA и выберите его.
3. Выберите **More** (**…**) > **Settings** > **Monitoring**.
4. Отключите **Full-stack monitoring** и **Auto-injection**.

## Alpine Linux/musl-libc, выделение памяти

**Проблема:**

На системах Alpine Linux на базе musl-libc каждый исполняемый файл имеет ограничения памяти, управляемые параметром `MPROTECT`. При мониторинге приложения Alpine Linux на базе musl-libc с помощью Dynatrace OneAgent процесс (например, процесс Java) может превысить заданное ограничение памяти. В таком случае последующее выделение памяти завершится ошибкой вида `There is insufficient memory for the Java Runtime Environment to continue.`

**Решение:**

Для решения таких проблем рекомендуется игнорировать параметр защиты памяти для исполняемых файлов, которые планируется мониторить с помощью Dynatrace OneAgent. Для этого необходимо установить инструмент paxctl:

`apk add paxctl`

После этого можно снять проверку памяти, например:

`paxctl -m /usr/lib/jvm/java-1.8-openjdk/jre/bin/java`

Для сторонних исполняемых файлов, не поставляемых Alpine, будет выведено сообщение:

`<file> does not have a PT_PAX_FLAGS program`

В таких случаях предварительно преобразуйте файл, например:

`paxctl -C /usr/lib/jvm/java-1.8-openjdk/jre/bin/java`

## Alpine Linux/musl-libc, пакеты совместимости с GNU C Library (glibc)

**Проблема:**

Бинарные файлы, собранные под GNU C Library (glibc) и запускаемые на системах Alpine Linux через пакет **gcompat (слой совместимости GNU C Library для musl)** или **libc6-compat (библиотеки совместимости для glibc)**, не поддерживаются.

**Решение:**

Перенесите сборочный конвейер на нативную компиляцию и упаковку под Alpine Linux.

## PHP в Apache на Windows, размер стека

**Проблема:**

По умолчанию размер стека Apache на Windows составляет 1 МБ, что значительно меньше, чем на других платформах. Поэтому дополнительная нагрузка на память при включении мониторинга Dynatrace для PHP может приводить к переполнению стека.

**Решение:**

Проблему можно решить, увеличив размер стека до 8 МБ (значение по умолчанию для Linux).

```
<IfModule mpm_winnt_module>



ThreadStackSize 8388608



</IfModule>
```

## Cloud Foundry, сборочный пакет IBM WebSphere Liberty

**Проблема:**

Рекомендуемая версия сборочного пакета IBM WebSphere Liberty изменилась с `v3.7-20170118-2046` на `v3.9-20170419-1403` из-за известных проблем: ограничения командной строки JVM до 512 символов и проблемы с завершающими слешами.

**Решение:**
Используйте сборочный пакет IBM WebSphere Liberty версии v3.9-20170419-1403 и выше.

## Хост, Ubuntu 16.10

**Проблема:**

Из-за изменений в оптимизации компилятора пакетов C runtime в Ubuntu 16.10 появились новые требования к выравниванию стека. Версии OneAgent ранее 1.103.237 не соответствуют этим требованиям. Использование OneAgent версий ранее 1.103.237 может приводить к сбоям процессов при вызовах динамического разрешения символов (`dlsym`) в C runtime.

**Решение:**

Обновите OneAgent до версии 1.103.237 или выше. Эта версия OneAgent будет доступна для всех сред Dynatrace к 20 октября 2016 года. Инструкции по обновлению OneAgent:

1. Перейдите в **Settings** > **Preferences** (видно только администраторам среды).
2. Убедитесь, что параметр **Automatically update OneAgent instances** включён. OneAgent версии 1.103.237 будет автоматически развёрнут, как только станет доступен в вашей среде.
   Если **Automatically update One Agent instances** отключён, выберите **OneAgent version 1.103.237 or higher** и нажмите **Update now**.

## Java, IBM J9

**Проблема:**

В редких случаях при реализации блока try-catch-finally и перехвате исключения множественного типа в Java 7 исключение перехватывается, однако код в блоке finally не выполняется. Эта проблема исправлена начиная с IBM J9.

**Решение:**

Исправлено начиная с IBM J9

* 7 R1 SR2 FP11 (7.1.3.0)
* 7 SR9 (7.0.9.0)
* 8 SR1 (8.0.1.0)

**Источник:**

* [IBM 1IV68110](https://www-01.ibm.com/support/docview.wss?uid=swg1IV68110)

## Java, WebSphere MQ, JMS

**Проблема:**

При использовании WebSphere MQ через JMS Dynatrace не всегда может определить имя очереди и может отображать его как «unavailable». Это происходит, когда MQ-сообщения не были должным образом сопоставлены с JMS.

**Решение:**

Следуйте документации IBM по [сопоставлению JMS-сообщений с IBM MQ-сообщениями](https://www.ibm.com/support/knowledgecenter/SSFKSJ_8.0.0/com.ibm.mq.dev.doc/q031990_.htm). После того как заголовок `MQRFH2` будет правильно сопоставлен, Dynatrace отобразит правильное имя очереди.

## Java, Oracle HotSpot/OpenJDK

**Проблема:**

Известная проблема в Oracle HotSpot и OpenJDK может приводить к взаимоблокировке JVM в `ThreadTimesClosure` или к неполным данным о времени ЦП фоновых операций. Рекомендуется обновить Oracle HotSpot до версии 6u38/7u40 или OpenJDK до версии 7u45 и выше.

**Решение:**

Исправлено в Oracle HotSpot 6u38/7u40 и OpenJDK 7u45

**Источник:**

* [Источник: Oracle HotSpot 6 (баг 7196045)](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=7196045)
* [Источник: Oracle HotSpot 7 (баг 8005479)](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=8005479)
* [Источник: OpenJDK (JDK-7196045)](https://bugs.openjdk.java.net/browse/JDK-7196045)

**Проблема:**

Известная проблема в Oracle HotSpot и OpenJDK может приводить к аварийному завершению JVM, когда загружен агент JVMTI, включён [общий доступ к данным классов](https://docs.oracle.com/en/java/javase/11/vm/class-data-sharing.html#GUID-7EAA3411-8CF0-4D19-BD05-DF5E1780AA91) и существует файл `classes.jsa`. Обычно это нехарактерно, однако происходит в средах Docker, особенно с Java 11, где общий доступ к данным классов задан как `auto`.

**Решение:**

Измените командную строку Java, добавив -Xshare:off для отключения общего доступа к данным классов.

**Источник:**

* [Источник: OpenJDK (JDK-8212200)](https://bugs.openjdk.java.net/browse/JDK-8212200)

## Java, Spring, AspectJ

**Проблема:**

Ряд пользователей сообщали о следующем `NullPointerException` при запуске приложений Java Spring или AspectJ. AspectJ устранил эту проблему в версии 1.6+. Убедитесь, что classpath обновлён для использования AspectJ 1.6+.

Сообщение: `NullPointerException at`

```
`org.aspectj.weaver.reflect.Java15AnnotationFindergetAnnotations



(Java15AnnotationFinder.java:109)`
```

**Решение:**

Исправлено начиная с Spring 2.5.4/AspectJ 1.6

**Источник:**

* [SPR-4390](https://jira.spring.io/browse/SPR-4390)

## Java/Real User Monitoring/Apigee

**Проблема:**

Real User Monitoring Java-приложений может вызывать ошибку `ClassCastException` при приведении типа к реализованному интерфейсу `HttpServletRequest`, поскольку Dynatrace заменяет исходную реализацию `HttpServletRequest` на `RequestWrapper` для автоматической инъекции RUM JavaScript.

Этот сбой также происходит у пользователей [Apigee](https://apigee.com).

**Решение:**

Доступно несколько вариантов:

1. Измените исходный код так, чтобы он не ожидал конкретной реализации интерфейса `HttpServletRequest`.
2. Если используется сторонний фреймворк, обратитесь к его поставщику.
3. Для Apigee автоматическая инъекция Real User Monitoring отключена. Ручная инъекция Real User Monitoring не затронута и может использоваться как обходное решение.
4. Можно использовать веб-сервер перед Java: веб-сервер автоматически выполнит инъекцию RUM JavaScript и тем самым позволит избежать сбоя.

**Источник:**
н/д

## Накладные расходы ЦП Java

**Проблема:**

При инструментировании Preview для JBoss периодически возникают скачки потребления ЦП или повышенная общая загрузка ЦП. Эти скачки вызываются запросами к метрикам JMX. Вызовы JMX с интервалом 10 секунд приводят к скачкам ЦП в определённых версиях, затронутых этой ошибкой JBoss. Версии 6.4.x считаются проблематичными.

**Решение:**

Обходное решение: обновить Preview для JBoss и/или обратиться в RedHat.

**Источник:**

* [Ошибка 1367784](https://bugzilla.redhat.com/show_bug.cgi?id=1367784)

## UI/Docker

**Проблема:**

В Docker версий 1.10.3 - 1.11 в интерфейсе отсутствует статистика ЦП, памяти и сети для контейнеров, поскольку запросы данных к контейнерам через `docker stats` завершаются по таймауту. Перезапуск Docker временно решает эту проблему.

**Решение:**

Исправлено начиная с Docker 1.12. Обновите Docker до версии 1.12.

**Источник:**

* [Проблема 22655](https://github.com/docker/docker/issues/22655)

## UI/IIS

**Проблема:**

Из-за отсутствия счётчиков производительности Windows вкладка **Further details** может не отображаться в интерфейсе для процессов IIS даже после перезапуска IIS. Ошибки при инъекции OneAgent не выводятся.

**Решение:**

Это может происходить из-за проблем с библиотекой счётчиков производительности в реестре Windows. Для проверки:

Используя команду Windows, убедитесь, что метрики недоступны из реестра Windows:
typeperf `"\Process(w3wp*)\ID Process" -sc 15`
Как вариант, используйте `Perfmon.exe`, чтобы проверить доступность данных для счётчиков или убедиться в их отсутствии.

Обратитесь к технической документации Microsoft для восстановления библиотек производительности в реестре.

**Источник:**

* [KB 00956](https://support.microsoft.com/en-us/kb/300956)

## .NET, IIS

**Проблема:**

Если мониторинг IIS включён для ASP.NET-приложения, использующего .NET >= 4.5 и < 4.6, в редких случаях приложение может завершать работу с необработанным `NullReferenceException`.

Сообщение: `System.NullReferenceException at`

```
`System.Web.Security.Roles.IsUserInRole(String username, String roleName)`
```

**Решение:**

Исправлено начиная с .NET 4.6.

* [Источник](https://connect.microsoft.com/VisualStudio/feedbackdetail/view/967133/roles-getrolesforuser-throw-a-nullreferenceexception-in-a-wcf-service-which-is-hosted-in-asp-net-with-the-aspnetcompatibilityenabled-define-to-false)

## .NET, Cassette

**Проблема:**

Пользователи сообщали о сбое при использовании библиотеки управления веб-ресурсами Cassette.

Сообщение: сбой в

```
`[TinyIoCResolutionException: Unable to resolve type: Cassette.Views.BundlesDocumentationer]`
```

**Решение:**

В качестве обходного решения можно использовать файловую систему в качестве кэша Cassette, указав каталог в файле `web.config`:

```
`<cassette cacheDirectory="App_Data\Cassette" />`
```

Возможно, исправлено в версии v2.4.1

**Источник:**

* [Pull 441](https://github.com/andrewdavey/cassette/pull/441)

## .NET, ConfuserEx

**Проблема:**

Использование инструмента обфускации сборок ConfuserEx иногда может приводить к сбою .NET-приложений, поскольку сборка ConfuserEx не допускает использования «профилировщиков» вроде Dynatrace.

Сообщение: сбой в

```
`System.Environment.FailFast(System.String)`
```

**Решение:**

Отключите обфускацию ConfuserEx или отключите мониторинг Dynatrace на уровне процесса.

**Источник:**

* [Источник](https://github.com/yck1509/ConfuserEx/blob/816172adcb1ea2a6c74a964274373987fc2e9fe5/Confuser.Runtime/AntiDebug.Antinet.cs)

## Real User Monitoring, Chrome

**Проблема:**

Анализ Real User Monitoring в Google Chrome может приводить к сбоям браузера, когда некоторые ресурсы не загружаются.

Сообщение: сбой в

```
`window.performance.getEntriesByType('resource')`
```

**Решение:**

До выхода исправления от Chrome убедитесь, что все ресурсы загружаются успешно (без ответов 301), или отключите **W3C resource timing for third party/CDN**.

Чтобы отключить W3C resource timing для сторонних ресурсов/CDN:

1. Перейдите в **Frontend**.
2. Выберите приложение для редактирования.
3. Нажмите кнопку **More** (**…**).
4. Нажмите **Edit**.
5. Нажмите **Content capture**.
6. Установите переключатель **W3C resource timing for third party/CDN** в положение **Off**.

**Источник:**

* [Проблема 586443](https://bugs.chromium.org/p/chromium/issues/detail?id=586443)

## Безагентный Real User Monitoring, Chrome

**Проблема:**

Пользователи могут видеть предупреждение браузера в консоли разработчика Chrome при использовании медленных подключений, например сетей 2G.

Сообщение:
`A Parser-blocking, cross-origin script, https://js-cdn.dynatrace.com/jstag/148709fdc4b/ruxitagent_2fgjqrx_10111170210093847.js, is invoked via document.write. This may be blocked by the browser if the device has poor network connectivity. See https://www.chromestatus.com/feature/5718547946799104 for more details.`

**Решение:**

1. Перейдите в **Frontend**.
2. Выберите приложение для настройки.
3. Нажмите кнопку **Browse (…)** и выберите **Edit**.
4. В разделе **Setup** выберите **Agentless monitoring setup**.
5. Отключите переключатель **Easy monitoring**.

Единственный недостаток этого изменения: при каждом изменении конфигурации потребуется скопировать и повторно внедрить RUM JavaScript. Поэтому предпочтительнее использовать REST API для получения обновлённого тега.

**Источник:**

* [Обновление 2016/08](https://developers.google.com/web/updates/2016/08/removing-document-write)

## Real User Monitoring, jQuery

**Проблема:**

При выполнении Real User Monitoring завершившиеся с ошибкой асинхронные действия пользователя JQuery приводят к таймауту действий через 180 секунд, однако ошибка не выводится. Это вызвано известным ограничением jQuery.

**Решение:**

jQuery не предоставил исправления для этой проблемы. Для её решения исправьте неработающий вызов jQuery на своей стороне (например, AJAX-запрос к несуществующему ресурсу) или отключите jQuery в настройках обнаружения XHR (Ajax) и включите базовое обнаружение XHR.

Чтобы отключить обнаружение JQuery и включить базовое обнаружение XHR:

1. Перейдите в **Frontend**.
2. Выберите приложение для редактирования.
3. Нажмите кнопку **More** (**…**).
4. Нажмите **Edit**.
5. Нажмите **XHR (Ajax)** detection.
6. Установите переключатель **JQuery, Backbone.js** в положение **Off**.
7. Установите переключатель **Basic XHR detection** в положение **On**.

**Источник:**

* [Тикет 9613](https://bugs.jquery.com/ticket/9613)

## Real User Monitoring, Ext JS

**Проблема:**

В крупных и сложных приложениях Ext JS пользователи сталкивались с деградацией времени отклика на стороне клиента, например с уведомлением браузера о зависшем скрипте. Из-за внутреннего механизма обработки событий Ext JS приложение может работать медленно, если RUM JavaScript перехватывает слишком много событий.

**Решение:**

Отключите расширенный захват событий Ext JS в настройках Real User Monitoring.

1. Перейдите в **Web**.
2. Выберите приложение для настройки.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Custom configuration properties**.
5. Выберите **Add a custom configuration property** и введите `exteventsoff=1`.

Если после этого некоторые действия пользователей не фиксируются, используйте JavaScript API для ручного запуска действий.

## Real User Monitoring, Salesforce

**Проблема:**
При [внедрении RUM](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Настройте автоматическое внедрение RUM JavaScript на страницы ваших приложений") в Salesforce приложение может зависать в состоянии «loading» при просмотре записей из результатов поиска. В этом случае отладчик браузера выводит ошибку JavaScript: `Wrong number of arguments or invalid property assignment on b.b.open,arguments,b.b`.

Это происходит, когда RUM JavaScript не является первым загружаемым на странице скриптом. JavaScript-код, загружаемый в заголовке, может негативно влиять на RUM JavaScript.

**Решение:**
Перемещение RUM JavaScript так, чтобы он загружался раньше остальных скриптов, решает эту проблему.

**Проблема:**
RUM Dynatrace не работает для приложений Salesforce на основе [Lightning Component Framework](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/intro_framework.htm).

Причина в том, что многие приложения и продукты Salesforce основаны на [Lightning Component Framework](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/intro_framework.htm). Этот фреймворк имеет архитектуру безопасности [Lightning Locker](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/security_code.htm), которая ограничивает доступ к элементам DOM и тем самым влияет на RUM JavaScript Dynatrace. Когда код Locker загружается и выполняется раньше RUM JavaScript Dynatrace, мониторинг не работает независимо от того, добавлен ли [RUM JavaScript](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Настройте автоматическое внедрение RUM JavaScript на страницы ваших приложений").

**Решение:**
На данный момент решения со стороны Dynatrace нет. Обратитесь в поддержку Salesforce. Возможно, существует способ разрешить RUM JavaScript Dynatrace.

## Real User Monitoring, Salesforce Commerce

**Проблема:**

В настоящее время существует несовместимость между безагентным RUM Dynatrace и Salesforce Commerce. Это связано с зарезервированным символом в компиляторе Salesforce.

**Решение:**

Замените `#` на `${'#'}` в RUM JavaScript Dynatrace.

## Real User Monitoring, визуальная готовность, Internet Explorer 11

**Проблема:**

Включение параметра приложения [**Visually complete**](/managed/observe/digital-experience/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics "Узнайте, как использовать метрики 'Visually complete' и 'Speed index'.") при использовании Dynatrace с Internet Explorer 11 может приводить к полному сбою или зависанию страницы в случаях, когда происходят массовые мутации DOM с элементами `<table>` или псевдотабличными элементами (с атрибутом стиля `display:table`). Это чаще происходит в одностраничных приложениях. Само по себе отслеживание мутаций с помощью MutationObserver, используемое в Visually complete, может приводить к сбою страницы после её загрузки. Вот [простой пример воспроизведения проблемы](https://jsfiddle.net/gd88q1n3/2/) со сбоем при мутации псевдотабличного элемента.

#### Дополнительные сведения о Visually complete и Speed index

Метрики Speed index и Visually complete доступны только в браузерах, поддерживающих [`mutationobservers`](https://developers.google.com/web/updates/2012/02/Detect-DOM-changes-with-Mutation-Observers). К ним относятся следующие браузеры:

* Microsoft Internet Explorer 11
* Microsoft Edge 15 и выше
* Firefox 57 и выше
* Google Chrome 61 и выше

Speed index доступен только для действий загрузки. Visually complete доступен для всех действий, включая действия загрузки, но недоступен для AJAX-запросов, не влияющих на DOM.

**Решение:**

Microsoft исправила большую часть этой проблемы для мутаций элемента `<table>` в [недавнем обновлении](https://support.microsoft.com/en-za/help/4025252/cumulative-security-update-for-internet-explorer-july-11-2017). Обновите Internet Explorer 11 до этой версии, чтобы устранить проблему в большинстве случаев.

После обновления Internet Explorer 11 элементы с атрибутом стиля `display:table` по-прежнему подвержены этой проблеме. Для этого создан флаг функции, позволяющий отключить Visually complete только в Internet Explorer 11. Чтобы включить этот флаг, обратитесь к эксперту по продукту Dynatrace через чат в вашей среде.

## Red Hat Enterprise Linux 7.4

**Проблема:**

RHEL v7.4 (обновлённый с v7.3 или при чистой установке) поставляется с пакетом stix-fonts. При установке этого пакета шрифт по умолчанию меняется с `Utopia` на `STIX`. В результате шрифты Java по умолчанию, включая семейство `sans-serif`, сопоставляются с `STIX`. Однако шрифты `STIX` несовместимы с Java (OpenJDK + IBM JDK) и вызывают исключения и некорректные вычислительные артефакты при использовании `java.awt`, что характерно для `JasperReports`.

Для Dynatrace Managed, основанного на Java, эта проблема проявлялась в Smartscape. А именно: при выборе любого элемента в Smartscape отображалось неспецифическое сообщение об ошибке.

**Решение:**

Создайте файл `/etc/fonts/local.conf` с содержимым, приведённым ниже, чтобы явно вернуть `Utopia` в качестве шрифта по умолчанию.

```
<?xml version='1.0'?>



<!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>



<fontconfig>



<alias>



<family>serif</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>sans-serif</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>monospace</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>dialog</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>dialoginput</family>



<prefer><family>Utopia</family></prefer>



</alias>



</fontconfig>
```

**Источник:**

* [Ошибка 1484079](https://bugzilla.redhat.com/show_bug.cgi?id=1484079#c8)

## IBM HTTP Server (IHS) 8.5

**Проблема:**

IHS 8.5 на Linux завершает работу с ошибкой сегментации.

**Решение:**

Отключите prelink на сервере IHS.

**Источник:**

* [Источник](https://www.google.at/search?q=prelink+crash)

## Adobe Dispatcher

**Проблема:**

При использовании Adobe Dispatcher с веб-сервером, мониторинг которого ведёт Dynatrace OneAgent, тег агента RUM JavaScript внедряется на HTML-страницу дважды. В результате агент RUM JavaScript выполняется в браузере дважды, создавая излишнюю нагрузку (например, маяки отправляются дважды и т. д.).

Причина в том, что Adobe Dispatcher по умолчанию не кэширует HTTP-заголовки ответов, поэтому заголовок X-OneAgent-JS-Injection «теряется» для уже обработанных сайтов, обслуживаемых из кэша. При отсутствии этого заголовка агент веб-сервера внедряет ещё один тег агента RUM JavaScript, даже если он уже присутствует в кэшированном содержимом.

**Решение:**

Dispatcher необходимо настроить на кэширование заголовка ответа "X-OneAgent-JS-Injection". Чтобы избежать двойного внедрения тега агента RUM JavaScript при использовании Adobe Dispatcher с веб-сервером под мониторингом Dynatrace OneAgent, добавьте "X-OneAgent-JS-Injection" в раздел `/cache/headers` конфигурации Adobe Dispatcher:

```
/cache



{



# Cache configuration



# <existing configuration>



# ...



/headers



{



"X-OneAgent-JS-Injection"



}



}
```