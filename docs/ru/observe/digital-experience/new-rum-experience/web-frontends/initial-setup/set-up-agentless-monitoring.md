---
title: Настройка безагентного RUM в новом опыте RUM
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring
scraped: 2026-03-06T21:35:10.443740
---

# Настройка безагентного RUM в New RUM Experience


* Latest Dynatrace
* How-to guide

Как описано в разделе [Выбор подходящего подхода к инструментированию](../initial-setup.md#find-suitable-instrumentation-approach "Learn how to set up the New RUM Experience for web frontends."), безагентный RUM является подходящим выбором для сценариев, где:

* У вас нет доступа к веб-серверу или ваша технология не поддерживает автоматическое внедрение.
* У вас есть доступ к коду приложения.

После подтверждения этих условий выполните приведённые ниже шаги для настройки безагентного RUM.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание фронтенда**](set-up-agentless-monitoring.md#create-frontend "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Выбор и настройка формата сниппета**](set-up-agentless-monitoring.md#select-snippet-format "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Вставка RUM JavaScript**](set-up-agentless-monitoring.md#insert-rum-javascript "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Проверка настройки**](set-up-agentless-monitoring.md#verify-setup "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Поддержание RUM JavaScript в актуальном состоянии**](set-up-agentless-monitoring.md#keep-rum-javascript-up-to-date "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")

## Шаг 1. Создание фронтенда

Для создания фронтенда для безагентного RUM:

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Выберите  **Frontend** для запуска процесса **Frontend creation**.
3. На шаге **Start monitoring** выберите тип фронтенда **Web** и укажите имя фронтенда.
4. На шаге **Select instrumentation method** выберите **Agentless**.
5. Выберите **Create**.
6. На шаге **Setup** проверьте в разделе **Select capability and settings**, включён ли **RUM**. Если он не включён, выберите  **Override** и включите его.
7. Если вы хотите захватывать [пользовательские взаимодействия](../additional-configuration/user-interactions.md "Learn how to configure and customize user interaction capturing for web frontends."), такие как клики и прокрутки, включите **User Interactions**.
8. Для обеспечения соответствия действующим нормативным требованиям по конфиденциальности данных настройте необходимые параметры в разделе **End users' data privacy**. Подробнее о доступных параметрах см. в разделе [Настройка конфиденциальности данных для веб-фронтендов](../additional-configuration/data-privacy-web.md "Learn about the available settings that help you ensure your web frontends comply with data privacy regulations.").
9. В разделе **Copy JavaScript tag** выберите  для копирования RUM JavaScript в буфер обмена.

Предоставленный RUM JavaScript имеет [формат сниппета JavaScript tag](snippet-formats.md#js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."). Этот формат рекомендуется для большинства сценариев, поскольку обеспечивает автоматическое обновление. С этим сниппетом код мониторинга загружается и выполняется синхронно.

## Шаг 2. Выбор и настройка формата сниппета (необязательно)

New RUM Experience предоставляет несколько форматов сниппетов для удовлетворения различных требований. Подробнее о доступных форматах и их настройке см. в разделе [Выбор формата сниппета в New RUM Experience](snippet-formats.md "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."). Для каждого формата сниппета доступна [конечная точка API](../../../../../dynatrace-api/environment-api/rum/rum-manual-insertion-tags.md "Learn how you can download the RUM manual insertion tags via API").

Для получения различных форматов сниппетов в интерфейсе:

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Выберите  **Web** для просмотра всех веб-фронтендов.
3. Выберите фронтенд, который вы хотите инструментировать.
4. На вкладке **Settings** выберите **Manual insertion**.
5. Прокрутите до раздела с нужным форматом сниппета. Затем выберите  для копирования RUM JavaScript в буфер обмена.

## Шаг 3. Вставка RUM JavaScript

Добавьте RUM JavaScript в элемент `<head>` каждой HTML-страницы, которую вы хотите мониторить, и убедитесь, что это первый исполняемый скрипт на странице.

В приведённом ниже примере показана простая HTML-страница до и после вставки RUM JavaScript.

До вставки

После вставки

```
<!DOCTYPE html>


<html  lang="en">


<head>


<meta charset="UTF-8">


<title>MyApp</title>


<script type="text/javascript" src="myapp.js"></script>


</head>


<body>


<form>


Username: <input type="text" name="username"/><br/>


Password: <input type="password" name="password"/><br/>


<input type="submit" value="Login">


</form>


</body>


</html>


</html>
```

```
<!DOCTYPE html>


<html  lang="en">


<head>


<meta charset="UTF-8">


<title>MyApp</title>


<script type="text/javascript" src="https://js-cdn.dynatrace.com/jstag/145e12d594f/cg36988wxq/477g8ec68708x5c1_complete.js" crossorigin="anonymous"></script>


<script type="text/javascript" src="myapp.js"></script>


</head>


<body>


<form>


Username: <input type="text" name="username"/><br/>


Password: <input type="password" name="password"/><br/>


<input type="submit" value="Login">


</form>


</body>


</html>
```

### Использование файлов шаблонов

Для веб-сайтов, использующих фреймворки или системы с шаблонами, обычно можно добавить пользовательский JavaScript на все страницы, поместив его в общий файл шаблона, обычно называемый `header.html` или аналогичным образом. Эти файлы, как правило, автоматически включаются в каждую страницу при серверной отрисовке или генерации статического сайта. Если архитектура вашего сайта поддерживает централизованные шаблоны, используйте этот подход для вставки сниппета RUM JavaScript.

### Использование менеджеров тегов

При использовании менеджеров тегов может быть сложно гарантировать, что RUM JavaScript будет первым исполняемым скриптом на странице. Если вы не можете это обеспечить, вы можете потерять информацию, такую как определённые тайминги или пользовательские события, которые доступны только при полной загрузке и инициализации кода мониторинга RUM и конфигурации.

Это ограничение более выражено, если вы настроите параметр **script execution** для [JavaScript tag](snippet-formats.md#js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."), [OneAgent JavaScript tag](snippet-formats.md#oneagent-js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.") или [OneAgent JavaScript tag with SRI](snippet-formats.md#oneagent-js-tag-sri "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.") на **async** или **defer**.

## Шаг 4. Проверка настройки

Если ваш фронтенд получает трафик, графики в [![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals**](../../experience-vitals.md "The Experience Vitals app provides an entry point for monitoring web and mobile frontends.") должны начать отображать данные в течение десяти минут.

Если данные пока не отображаются, вашей среде могут потребоваться дополнительные шаги настройки. Руководство [Завершение начальной настройки для безагентного фронтенда](finalize-initial-setup-agentless.md "Verify and complete the initial setup for your agentless frontend.") содержит серию проверок, которые помогут определить необходимую конфигурацию.

## Шаг 5. Поддержание RUM JavaScript в актуальном состоянии

Если вы вставили RUM JavaScript, используя формат сниппета [JavaScript tag](../../../web-applications/initial-setup/snippet-formats.md#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case"), код мониторинга и конфигурация обновляются автоматически. Для других форматов сниппетов вам необходимо обновлять RUM JavaScript при каждом изменении конфигурации.

Рекомендуемый подход — интегрировать вставку сниппета в процесс сборки с помощью [API тегов ручной вставки RUM](../../../../../dynatrace-api/environment-api/rum/rum-manual-insertion-tags.md "Learn how you can download the RUM manual insertion tags via API"). Это обеспечивает постоянную работу вашего приложения с актуальной конфигурацией.

## Связанные темы

* [Выбор формата сниппета в New RUM Experience](snippet-formats.md "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.")
* [API тегов ручной вставки RUM](../../../../../dynatrace-api/environment-api/rum/rum-manual-insertion-tags.md "Learn how you can download the RUM manual insertion tags via API")
* [Завершение начальной настройки для безагентного фронтенда](finalize-initial-setup-agentless.md "Verify and complete the initial setup for your agentless frontend.")