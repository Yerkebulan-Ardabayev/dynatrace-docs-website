---
title: Настройка агентлесс Real User Monitoring
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring
scraped: 2026-05-12T11:25:03.725140
---

# Настройка агентлесс Real User Monitoring

# Настройка агентлесс Real User Monitoring

* How-to guide
* 8-min read
* Updated on Apr 28, 2026

Агентлесс Real User Monitoring предназначен для случаев, когда у вас нет доступа к веб-серверу (и поэтому вы не можете установить OneAgent), но есть доступ к коду приложения.

Все преимущества Real User Monitoring можно получить только после установки Dynatrace OneAgent. Подробнее см. в разделе [OneAgent installation is recommended](#oneagent-is-better).

## Предварительные условия

Для настройки агентлесс Real User Monitoring необходимо следующее:

* Доступ к исходному HTML-коду приложения для вставки RUM JavaScript
* RUM JavaScript — пользовательский JavaScript-тег, код или фрагмент, сгенерированный Dynatrace

* CDN для обслуживания RUM JavaScript во избежание проблем с производительностью веб-страниц во время технического обслуживания Dynatrace Managed Server или сбоев локальной сети

## Настройка агентлесс-мониторинга

Выполните следующие действия для настройки агентлесс-мониторинга.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Configure Cluster ActiveGate URL**](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring#managed-configure-ag-url "Set up agentless monitoring for your web applications.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create an application and insert RUM JavaScript**](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring#managed-create-app-add-code "Set up agentless monitoring for your web applications.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Choose another RUM JavaScript snippet format**](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring#managed-choose-insertion-format "Set up agentless monitoring for your web applications.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Keep RUM JavaScript up-to-date**](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring#managed-keep-code-updated "Set up agentless monitoring for your web applications.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Make your cluster production ready**](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring#managed-cluster-production-ready "Set up agentless monitoring for your web applications.")

### Шаг 1: Настройте URL Cluster ActiveGate

1. Установите [Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.").
2. Перейдите в **Settings** > **Public endpoints**.
3. В поле **Cluster ActiveGate URL** введите URL, по которому доступен ваш новый ActiveGate.  
   URL должен быть [публично доступен и поддерживать HTTPS-запросы](/managed/managed-cluster/basics/managed-deployments "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture.").

Этот URL используется для отправки данных Real User Monitoring в ваш Dynatrace Managed Cluster.

По умолчанию Cluster ActiveGate прослушивает порт `9999`. Если это нежелательно, изменить порт можно в [конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements."). Кроме того, можно использовать порт по вашему выбору и перенаправить трафик на порт `9999` с помощью настроек брандмауэра.

### Шаг 2: Создайте приложение и вставьте RUM JavaScript

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Set up agentless monitoring**.

3. Введите имя приложения и выберите **Add web application**. Для вашего приложения будет сгенерирован пользовательский фрагмент JavaScript-кода.
4. Выберите **Copy code snippet** для копирования сгенерированного JavaScript-кода в буфер обмена. Код, сгенерированный после создания приложения, имеет формат [JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case").

   Dynatrace предлагает несколько форматов фрагментов RUM JavaScript. Если вы рассматриваете использование другого формата, обратитесь к следующему шагу.
5. Вставьте фрагмент JavaScript-кода в элемент `<head>` всех HTML-страниц, которые вы хотите отслеживать в своём приложении. Убедитесь, что RUM JavaScript является первым исполняемым скриптом на каждой странице.

   Для многих сайтов можно добавить пользовательский JavaScript на все страницы сразу, вставив повторно используемый код в централизованный файл `header.html`. Если возможно, используйте этот файл для вставки RUM JavaScript, чтобы избежать лишней работы.

Следующий пример показывает код простой страницы до и после вставки RUM JavaScript.

Before injection

After injection

```
<html>



<head>



<title>MyApp</title>



<script type="text/javascript" src="myapp.js"></script>



</head>



<body>



<form>



Username: <input type="text name="username"/><br/>



Password: <input type="password" name="password"/><br/>



<input type="submit" value="Login">



</form>
```

```
<html>



<head>



<title>MyApp</title>



<script type="text/javascript" src="https://js-cdn.dynatrace.com/jstag/145e12d594f/cg36988wxq/477g8ec68708x5c1_complete.js" crossorigin="anonymous"></script>



<script type="text/javascript" src="myapp.js"></script>



</head>



<body>



<form>



Username: <input type="text name="username"/><br/>



Password: <input type="password" name="password"/><br/>



<input type="submit" value="Login">



</form>
```

Если у вас уже есть приложение, настроенное для агентлесс-мониторинга, на шаге 3 приведённых выше инструкций выберите **Applications currently set up for agentless monitoring** вместо ввода имени приложения. После этого вы сможете просмотреть список приложений, уже настроенных для агентлесс-мониторинга, и соответствующие JavaScript-теги, коды или фрагменты. Это полезно, когда RUM JavaScript уже добавлен на некоторые страницы и вы хотите расширить охват мониторинга на другие страницы.

### Шаг 3 (необязательный): Выберите другой формат фрагмента RUM JavaScript

Хотя формат JavaScript tag идеально подходит для большинства сценариев, Dynatrace предлагает несколько форматов фрагментов RUM JavaScript для удовлетворения различных требований. Выберите формат, наилучшим образом подходящий для вашего приложения и отвечающий вашим требованиям. Подробное описание всех форматов см. в разделе [Select a snippet format](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case").

Чтобы получить другой формат фрагмента RUM JavaScript:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Manual insertion**.
5. Выберите необходимый формат фрагмента, затем выберите **Copy** для копирования в буфер обмена.

### Шаг 4: Поддерживайте актуальность RUM JavaScript

Если вы хотите, чтобы RUM JavaScript обновлялся автоматически, выберите [формат фрагмента JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case"). Для других форматов фрагментов обновление RUM JavaScript необходимо выполнять вручную.

Dynatrace предоставляет REST API, позволяющий получить последнюю версию RUM JavaScript для вашего приложения. Вы можете автоматически подставлять последнюю версию RUM JavaScript во время сборки приложения. Подробнее об использовании API см. в разделе [RUM manual insertion tags API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API").

### Шаг 5: Подготовьте кластер к использованию в продуктивной среде

#### Балансировка нагрузки нескольких ActiveGate

Для продуктивного мониторинга с повышенной нагрузкой и строгими требованиями к отказоустойчивости используйте несколько Cluster ActiveGate с балансировкой нагрузки и добавьте кэширующий прокси или CDN для обслуживания RUM JavaScript.

При таком подходе укажите URL балансировщика нагрузки и URL CDN в настройках.

1. Перейдите в **Settings** > **Public endpoints**.
2. В поле **Cluster ActiveGate URL** введите URL вашего балансировщика нагрузки.
3. В поле **CDN for JavaScript tag** введите URL вашего CDN.

Запросы, которые балансировщик нагрузки перенаправляет на Cluster ActiveGate, выглядят следующим образом.

`GET`- и `POST`-запросы для передачи информации о сессии в Dynatrace Managed:

```
<http|https>://<ClusterActiveGateHostname>/bf/<EnvironmentID>?<internalQueryParameters>
```

`GET`-запросы для RUM JavaScript:

```
http[s]://<ClusterActiveGateHostname>/jstag/<ManagedClusterID>/<EnvironmentID>/<InternalApplicationID>/bs.js



http[s]://<ClusterActiveGateHostname>/jstag/<ManagedClusterID>/ruxitagent<configInfo>_<version>.js
```

Обязательно настройте балансировщик нагрузки для установки заголовка `X-Forwarded-For` во всех перенаправляемых запросах. Этот заголовок содержит IP-адрес исходного запроса. Dynatrace нуждается в этой информации для определения источника запроса.

Балансировщик нагрузки должен завершать SSL, так как это очень ресурсоёмко для Cluster ActiveGate. Для повышения производительности и при условии соответствия требованиям безопасности трафик может передаваться через обычный HTTP от балансировщика нагрузки до Cluster ActiveGate.

#### Кэширование RUM JavaScript

Для поддержки сценариев с повышенной нагрузкой при использовании балансировщика нагрузки рекомендуется кэшировать RUM JavaScript, загружаемый с Cluster ActiveGate, с помощью кэширующего прокси или CDN.

CDN или кэширующий прокси должен перенаправлять все запросы к `<cdnurl>/jstag/` на `http[s]://<ActiveGateHostname>/jstag/` для подготовки к изменениям конфигурации и обновлениям. Поскольку существует несколько [форматов фрагментов RUM JavaScript](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case"), URL могут изменяться в зависимости от настроек приложения.

CDN или кэширующий прокси должен соблюдать политику кэширования, определённую заголовками ответа, которая варьируется для разных форматов фрагментов. В частности, ответы содержат заголовок `Cache-Control`, который может включать директивы `max-age`, `s-maxage`, `public` и `immutable`. Кроме того, в качестве запасного варианта включается заголовок `Expires`.

#### Обслуживание RUM JavaScript через CDN

Когда RUM JavaScript обслуживается с вашего CDN, `GET`-запросы для RUM JavaScript направляются на ваш CDN.

Чтобы обслуживать RUM JavaScript с вашего CDN:

1. Перейдите в **Settings** > **Public endpoints**.
2. В поле **CDN for JavaScript tag** введите корневой путь вашего CDN.

## Дополнительные сведения

### Рекомендуется установка OneAgent

Установка Dynatrace OneAgent предпочтительнее агентлесс-мониторинга по следующим причинам:

* При агентлесс-мониторинге необходимо вручную вставлять RUM JavaScript в каждую страницу приложения, что может быть сложным. Dynatrace OneAgent автоматически выполняет вставку RUM JavaScript.
* Если только вы не используете [формат фрагмента](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") **JavaScript tag** для агентлесс-мониторинга, RUM JavaScript, встроенный в страницы вашего приложения, не обновляется автоматически при изменении настроек мониторинга. Обновлять код придётся вручную.

Список технологий и серверов, поддерживающих автоматическую инжекцию RUM JavaScript, см. в разделе [Technology support - Real User Monitoring - Web servers and applications](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Для некоторых технологий [автоматическая инжекция RUM JavaScript](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#automatic-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications") не поддерживается даже при наличии OneAgent. Например, OneAgent может отслеживать серверную сторону приложения Heroku, но не может инжектировать RUM JavaScript в страницы приложения. В таких случаях добавьте RUM JavaScript в страницы приложения вручную.

### Влияние на производительность

Для минимизации влияния RUM JavaScript на время загрузки страницы может потребоваться как можно более поздняя загрузка скриптов. Используйте блокирующие теги скрипта, чтобы RUM JavaScript выполнялся именно там, где вы его разместили. Если скрипт должен выполняться как можно раньше, выполнение нельзя отложить.

Один из способов избежать дополнительных блокирующих запросов при загрузке страницы — инлайнить код скрипта. Код скрипта необходимо инлайнить в каждый документ, тем самым распространяя данные одного кэшированного файла на каждую страницу вашего приложения. Комбинируя оба подхода, можно получить встроенный фрагмент JavaScript, выполняющий необходимую инициализацию и откладывающий загрузку объёмного кода до второго скрипта.

### Затраты на обслуживание

Агентлесс-мониторинг требует самостоятельной вставки RUM JavaScript, поэтому постарайтесь свести ручные усилия к минимуму. Если вы не хотите изменять код при каждом изменении настроек мониторинга или выходе новой версии RUM JavaScript, выберите [формат фрагмента](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") **JavaScript tag**.

### Стандарты и политики безопасности

Некоторые стандарты разработки, созданные для повышения безопасности и быстродействия приложений, вводят новые ограничения.

Например, [стандарт Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), введённый для снижения риска межсайтового скриптинга, запрещает встроенный JavaScript-код. Это означает, что может потребоваться использование [формата фрагмента](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") **JavaScript tag** для RUM JavaScript.

### Корреляция пользовательских действий с распределёнными трассировками

При агентлесс-мониторинге возможность связывания пользовательских действий с [распределёнными трассировками](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") зависит от технологий, используемых в вашем приложении.

* Если ваше приложение инструментировано OneAgent, но [Real User Monitoring не поддерживается для его технологии](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), то распределённые трассировки, захваченные этим OneAgent, не могут быть связаны с пользовательскими действиями.
* Если ваше приложение выполняет XHR-вызовы к [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-rum "Monitor Lambda functions written in Python, Node.js, and Java.") или к другому инструментированному веб-серверу или серверу приложений, использующему [поддерживаемые технологии](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), то связывание пользовательских действий с распределёнными трассировками возможно. Однако такие веб-запросы обычно являются запросами между разными источниками, поэтому для достижения корреляции требуется дополнительная настройка. Подробнее см. в разделе [Link cross-origin XHR user actions and their distributed traces](/managed/observe/digital-experience/web-applications/initial-setup/link-cross-origin-xhrs "Enable the correlation between cross-origin XHR actions and distributed traces.").

### Использование менеджеров тегов

Рекомендуется обеспечить, чтобы RUM JavaScript был первым исполняемым скриптом на каждой странице, что может быть затруднено при использовании менеджера тегов. Если это не гарантируется, могут быть потеряны данные — например, определённые тайминги или пользовательские действия, — доступные только при полной загрузке и инициализации кода мониторинга RUM и конфигурации.

Этот риск усиливается при использовании [code snippet](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#code-snippet "Select a format for the RUM JavaScript snippet that best fits your specific use case") в отложенном режиме или при настройке параметра **Script execution** для [JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case"), [OneAgent JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") или [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case") на значение **async** или **defer**.

## Проверка настройки агентлесс-мониторинга

Для устранения проблем, которые могут возникнуть при агентлесс Real User Monitoring, убедитесь в следующем:

* Страницы, подлежащие мониторингу, содержат RUM JavaScript.
* RUM JavaScript корректно загружается браузером (при условии, что вы не используете встроенную инжекцию).

  Используйте инструменты разработчика браузера, чтобы проверить, что ответ для RUM JavaScript имеет статус `200` и тело ответа содержит RUM JavaScript.

* Вы получаете и вставляете RUM JavaScript только после полной настройки публичной конечной точки, например балансировщика нагрузки. Это гарантирует, что публичная конечная точка правильно указана в RUM JavaScript.

* Ответ конечной точки маяка начинается с `OK(BF)`.
* Приложение в веб-интерфейсе Dynatrace отображает данные.

Дополнительную информацию см. также в разделе [Web applications: Issues with RUM JavaScript](https://dt-url.net/up03l19).