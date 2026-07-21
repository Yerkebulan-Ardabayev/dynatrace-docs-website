---
title: Настройка агентless Real User Monitoring Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring
---

# Настройка агентless Real User Monitoring Classic

# Настройка агентless Real User Monitoring Classic

* Практическое руководство
* 8 мин на чтение
* Обновлено 28 апр. 2026 г.

Агентless Real User Monitoring Classic предназначен для использования, когда нет доступа к веб-серверу (и поэтому невозможно установить OneAgent), но есть доступ к коду приложения.

Полные преимущества Real User Monitoring можно получить только после установки Dynatrace OneAgent. Подробнее см. [Рекомендуется установка OneAgent](#oneagent-is-better).

## Предварительные требования

Вот что понадобится для настройки агентless Real User Monitoring Classic:

* Доступ к исходному коду HTML приложения, чтобы можно было вставить RUM JavaScript
* RUM JavaScript, пользовательский тег JavaScript, код или сниппет, сгенерированный Dynatrace

* CDN для доставки RUM JavaScript, чтобы предотвратить проблемы с производительностью веб-страницы во время периодов обслуживания Dynatrace Managed Server или сбоев локальной сети

## Настройка агентless мониторинга

Для настройки агентless мониторинга нужно выполнить следующие действия.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Настроить URL Cluster ActiveGate**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring#managed-configure-ag-url "Настройка агентless мониторинга для веб-приложений.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создать приложение и вставить RUM JavaScript**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring#managed-create-app-add-code "Настройка агентless мониторинга для веб-приложений.")[![Шаг 3, необязательный](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Шаг 3, необязательный")

**Выбрать другой формат сниппета RUM JavaScript**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring#managed-choose-insertion-format "Настройка агентless мониторинга для веб-приложений.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Поддерживать RUM JavaScript в актуальном состоянии**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring#managed-keep-code-updated "Настройка агентless мониторинга для веб-приложений.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Подготовить кластер к продуктивной эксплуатации**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring#managed-cluster-production-ready "Настройка агентless мониторинга для веб-приложений.")

### Шаг 1 Настроить URL Cluster ActiveGate

1. Установить [Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Установите Cluster ActiveGate на Linux или Windows для маршрутизации трафика OneAgent или запуска Synthetic-мониторов, и подключите его к Managed-кластеру.").
2. Перейти в **Settings** > **Public endpoints**.
3. В поле **Cluster ActiveGate URL** ввести URL, по которому доступен новый ActiveGate.  
   URL должен быть [публично доступен и способен принимать HTTPS-запросы](/managed/managed-cluster/basics/managed-deployments "Узнайте, как развёртывания Dynatrace Managed эволюционируют от базовой внутренней настройки до глобально распределённой архитектуры высокой доступности.").

Этот URL используется для отправки данных Real User Monitoring на Managed-кластер Dynatrace.

По умолчанию Cluster ActiveGate слушает порт `9999`. Если это нежелательно, можно изменить порт в [конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."). Также можно использовать порт по своему выбору, а затем перенаправлять трафик на порт `9999` с помощью настроек брандмауэра.

### Шаг 2 Создать приложение и вставить RUM JavaScript

1. Перейти в **Deploy Dynatrace**.
2. Выбрать **Set up agentless monitoring**.

3. Ввести имя приложения и выбрать **Add web application**. Для приложения будет сгенерирован пользовательский сниппет JavaScript-кода.
4. Выбрать **Copy code snippet**, чтобы скопировать сгенерированный JavaScript-код в буфер обмена. Код, сгенерированный после создания приложения, представлен в формате [JavaScript tag](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#js-tag "Выберите формат сниппета RUM JavaScript, который лучше всего подходит для конкретного случая использования").

   Dynatrace предлагает несколько форматов сниппета RUM JavaScript. Если рассматривается использование другого формата сниппета, рекомендации приведены в следующем шаге.
5. Вставить сниппет JavaScript-кода в элемент `<head>` всех HTML-страниц, которые нужно отслеживать в приложении. Нужно убедиться, что RUM JavaScript является первым исполняемым скриптом на каждой странице.

   Для многих веб-сайтов можно добавить пользовательский JavaScript сразу на все страницы, вставив код для повторного использования в централизованный файл `header.html`. По возможности стоит использовать этот файл для вставки RUM JavaScript, чтобы избежать лишней работы.

Следующий пример показывает код простой страницы до и после вставки RUM JavaScript.

До вставки

После вставки

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

Если уже есть приложение, настроенное для агентless мониторинга, на шаге 3 приведённых выше инструкций нужно выбрать **Applications currently set up for agentless monitoring** вместо ввода имени приложения. После этого можно просмотреть список приложений, уже настроенных для агентless мониторинга, и соответствующие им теги, коды или сниппеты JavaScript. Это полезно, когда RUM JavaScript уже добавлен на некоторые страницы и требуется расширить видимость мониторинга на другие страницы.

### Шаг 3, необязательный Выбрать другой формат сниппета RUM JavaScript Необязательно

Хотя формат JavaScript tag является оптимальным выбором для большинства случаев использования, Dynatrace предлагает несколько форматов сниппета RUM JavaScript, чтобы удовлетворить самые разные требования. Нужно выбрать формат, который лучше всего подходит приложению и отвечает требованиям. Подробные описания всех форматов см. в разделе [Выбор формата сниппета в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats "Выберите формат сниппета RUM JavaScript, который лучше всего подходит для конкретного случая использования").

Чтобы получить другой формат сниппета RUM JavaScript

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Injection** > **Manual insertion**.
5. Выбрать нужный формат сниппета, затем выбрать **Copy**, чтобы скопировать его в буфер обмена.

### Шаг 4 Поддерживать RUM JavaScript в актуальном состоянии

Если требуется, чтобы RUM JavaScript обновлялся автоматически, нужно выбрать [формат сниппета JavaScript tag](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#js-tag "Выберите формат сниппета RUM JavaScript, который лучше всего подходит для конкретного случая использования"). Для других форматов сниппетов RUM JavaScript нужно обновлять вручную.

Dynatrace предлагает REST API, который позволяет получить последнюю версию RUM JavaScript для приложения. Можно автоматически внедрять последнюю версию RUM JavaScript во время сборки приложения. Подробнее о том, как использовать API, см. в разделе [API тегов ручной вставки RUM](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Узнайте, как можно загрузить теги ручной вставки RUM через API").

### Шаг 5 Подготовить кластер к продуктивной эксплуатации

#### Балансировка нагрузки на несколько ActiveGate

Для мониторинга продуктивной среды с высокой нагрузкой и строгими требованиями к отказоустойчивости используй несколько ActiveGate Cluster с балансировкой нагрузки и добавь кэширующий прокси или CDN для раздачи RUM JavaScript.

При таком подходе нужно указать URL балансировщика нагрузки и URL CDN в настройках.

1. Перейди в **Settings** > **Public endpoints**.
2. В поле **Cluster ActiveGate URL** введи URL балансировщика нагрузки.
3. В поле **CDN for JavaScript tag** введи URL CDN.

Запросы, которые балансировщик нагрузки перенаправляет на ActiveGate Cluster, выглядят следующим образом.

Запросы `GET` и `POST` для передачи информации о сессии в Dynatrace Managed:

```
<http|https>://<ClusterActiveGateHostname>/bf/<EnvironmentID>?<internalQueryParameters>
```

Запросы `GET` для RUM JavaScript:

```
http[s]://<ClusterActiveGateHostname>/jstag/<ManagedClusterID>/<EnvironmentID>/<InternalApplicationID>/bs.js



http[s]://<ClusterActiveGateHostname>/jstag/<ManagedClusterID>/ruxitagent<configInfo>_<version>.js
```

Обязательно настрой балансировщик нагрузки так, чтобы он устанавливал заголовок `X-Forwarded-For` для всех перенаправляемых запросов. Этот заголовок содержит IP-адрес исходного запроса. Dynatrace нужна эта информация, чтобы определить, откуда пришёл запрос.

Балансировщик нагрузки должен завершать SSL-соединение, поскольку эта операция очень затратна для ActiveGate Cluster. Для повышения производительности, если это допускают требования безопасности, трафик можно передавать от балансировщика нагрузки на ActiveGate Cluster по обычному HTTP.

#### Кэширование RUM JavaScript

Для поддержки сценариев с высокой нагрузкой при использовании балансировщика нагрузки рекомендуется кэшировать RUM JavaScript, загружаемый с ActiveGate Cluster, с помощью кэширующего прокси или CDN.

CDN или кэширующий прокси должны перенаправлять все запросы `<cdnurl>/jstag/` на `http[s]://<ActiveGateHostname>/jstag/`, чтобы быть готовыми к изменениям конфигурации и обновлениям. Поскольку существует несколько [форматов сниппета RUM JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case"), URL могут меняться в зависимости от настроек приложения.

CDN или кэширующий прокси должны учитывать политику кэширования, заданную заголовками ответа, которая отличается для разных форматов сниппета. В частности, в ответах присутствует заголовок `Cache-Control`, который может задавать такие директивы, как `max-age`, `s-maxage`, `public` и `immutable`. Кроме того, в качестве запасного варианта включён заголовок `Expires`.

#### Раздача RUM JavaScript через CDN

Когда RUM JavaScript раздаётся с CDN, запросы `GET` для RUM JavaScript направляются на CDN.

Чтобы раздавать RUM JavaScript через CDN

1. Перейди в **Settings** > **Public endpoints**.
2. В поле **CDN for JavaScript tag** введи корневой путь CDN.

## Что нужно учитывать

### Рекомендуется установка OneAgent

Установка Dynatrace OneAgent предпочтительнее мониторинга без агента по следующим причинам:

* При мониторинге без агента нужно вручную вставлять RUM JavaScript на каждую страницу приложения, что может быть сложно. Dynatrace OneAgent выполняет вставку RUM JavaScript автоматически.
* Если для мониторинга без агента не используется [формат сниппета](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") **JavaScript tag**, RUM JavaScript, встроенный в страницы приложения, не обновляется автоматически при изменении настроек мониторинга приложения. Код придётся обновлять вручную.

Список технологий и серверов, поддерживающих автоматическое встраивание RUM JavaScript, приведён в разделе [Поддержка технологий - Real User Monitoring - Веб-серверы и приложения](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Для некоторых технологий [автоматическое встраивание RUM JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#automatic-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications") не поддерживается, даже если установка OneAgent возможна. Например, OneAgent может отслеживать серверную часть приложения Heroku, но не может встраивать RUM JavaScript на страницы приложения. В этом случае RUM JavaScript нужно добавить на страницы приложения вручную.

### Влияние на производительность

Чтобы минимизировать влияние RUM JavaScript на время загрузки страницы, стоит загружать скрипты как можно позже. Используй блокирующие теги скрипта, чтобы гарантировать выполнение RUM JavaScript именно там, где он размещён. Если скрипт нужно выполнить как можно раньше, отложить его выполнение нельзя.

Один из способов избежать дополнительных блокирующих запросов при загрузке страницы, это встроить код скрипта в документ (inline). Код скрипта нужно встраивать в каждый документ, тем самым распространяя данные одного кэшированного файла на каждую страницу приложения. Комбинируя оба подхода, можно получить встроенный (inline) сниппет JavaScript, который выполняет необходимую инициализацию и откладывает загрузку основного кода до второго скрипта.

### Затраты на обслуживание

Мониторинг без агента требует самостоятельной вставки RUM JavaScript, поэтому стоит убедиться, что это требует минимальных ручных усилий. Если код менять при каждом изменении настроек мониторинга приложения или при выходе новой версии RUM JavaScript не хочется, стоит выбрать [формат сниппета](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") **JavaScript tag**.

### Стандарты и политики безопасности

Некоторые стандарты разработки, созданные для повышения безопасности и скорости приложений, вводят также новые ограничения.

Например, стандарт [Content Security Policy (CSP)﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), введённый для снижения риска стать жертвой межсайтового скриптинга, запрещает встроенный (inline) код JavaScript. Это значит, что может понадобиться использовать [формат сниппета RUM JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") **JavaScript tag**.

### Связь действий пользователя с распределёнными трассировками

При мониторинге без агента возможность связывать действия пользователей и [распределённые трассировки](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") зависит от технологий, используемых в приложении.

* Если приложение инструментировано OneAgent, но [Real User Monitoring не поддерживается для его технологии](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), то распределённые трассировки, захваченные этим OneAgent, нельзя связать с действиями пользователей.
* Если приложение выполняет XHR-вызовы к [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-rum "Monitor Lambda functions written in Python, Node.js, and Java.") или к другому инструментированному веб- или серверу приложений, использующему [поддерживаемые технологии](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), то связать действия пользователей и распределённые трассировки возможно. Однако такие веб-запросы обычно являются кросс-доменными (cross-origin), поэтому для достижения корреляции действий пользователя с распределённой трассировкой требуется дополнительная настройка. Подробнее см. [Связывание кросс-доменных действий пользователя XHR и их распределённых трассировок в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/link-cross-origin-xhrs "Enable the correlation between cross-origin XHR actions and distributed traces.").

### Использование менеджеров тегов

Рекомендуется убедиться, что RUM JavaScript является первым выполняемым скриптом на каждой странице, что может быть непросто при использовании менеджера тегов. Если гарантировать это невозможно, часть информации, например определённые тайминги или действия пользователей, может быть потеряна: она доступна только тогда, когда код мониторинга RUM и конфигурация полностью загружены и инициализированы.

Этот риск усиливается при использовании [сниппета кода](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#code-snippet "Select a format for the RUM JavaScript snippet that best fits your specific use case") в отложенном режиме (deferred) или при настройке параметра **Script execution** для [JavaScript tag](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case"), [OneAgent JavaScript tag](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") или [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case") на **async** или **defer**.

## Проверка настройки мониторинга без агента

Чтобы выяснить проблемы, с которыми можно столкнуться при работе agentless Real User Monitoring Classic, нужно проверить следующее:

* Страницы, за которыми ведётся мониторинг, содержат RUM JavaScript.
* RUM JavaScript корректно загружается браузером (если не используется inline-инъекция).

  Нужно использовать инструменты разработчика браузера, чтобы проверить, что ответ для RUM JavaScript имеет код `200` и что тело ответа содержит RUM JavaScript.

* Получение и вставка RUM JavaScript выполняются только после полной настройки публичной конечной точки, например балансировщика нагрузки. Это гарантирует, что публичная конечная точка корректно указана в RUM JavaScript.

* Ответ конечной точки beacon начинается с `OK(BF)`.
* Приложение в веб-интерфейсе Dynatrace отображает данные.

Дополнительную информацию также можно найти в разделе [Web applications: Issues with RUM JavaScript﻿](https://dt-url.net/up03l19).