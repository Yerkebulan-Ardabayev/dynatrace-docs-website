---
title: Выбор формата фрагмента
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats
scraped: 2026-05-12T11:34:11.205023
---

# Выбор формата фрагмента

# Выбор формата фрагмента

* How-to guide
* Published Jul 01, 2025

RUM JavaScript — независимо от того, [автоматически инжектируется](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications") он или [вставляется вручную](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") в ваше веб-приложение — состоит из двух ключевых компонентов:

* **Monitoring code**: JavaScript-код, обеспечивающий RUM-возможности, такие как захват пользовательских действий.
* **Configuration**: конфигурация приложения, которую изначально использует код мониторинга. Она обновляется позднее через ответ RUM-маяка при изменении конфигурации.

Dynatrace RUM предоставляет несколько форматов фрагментов, которые интегрируют эти компоненты в страницы по-разному, каждый из которых ориентирован на удовлетворение конкретных требований.

На этой странице приведены [рекомендации](#snippet-format-recommendations) по выбору формата фрагмента, наилучшим образом отвечающего вашим требованиям, а также [подробное описание каждого формата](#snippet-format-details).

## Рекомендации по выбору формата фрагмента

Для большинства сценариев рекомендуется следующее:

* Используйте [JavaScript Tag](#js-tag) для ручной вставки.
* Используйте [OneAgent JavaScript Tag](#oneagent-js-tag) для автоматической инжекции.

Если вы хотите использовать функцию браузера Subresource Integrity (SRI) для проверки того, что код мониторинга не был изменён, используйте [OneAgent JavaScript tag with SRI](#oneagent-js-tag-sri) для ручной вставки и автоматической инжекции.

Чтобы избежать блокирующего парсинг выполнения кода мониторинга, настройте параметр **Script execution** выбранного формата фрагмента на **async** или **defer**. Инструкции по настройке этого параметра приведены в документации каждого отдельного формата ниже. Имейте в виду, что пока код мониторинга не загружен и не инициализирован полностью, некоторые тайминги и пользовательские действия будут потеряны.

## Доступные форматы фрагментов

JavaScript tag

OneAgent JavaScript tag

OneAgent JavaScript tag with SRI

Inline code

Code snippet

**JavaScript tag** ссылается на внешний файл, который содержит как код мониторинга, так и конфигурацию. JavaScript tag доступен только для ручной вставки.

[Получить JavaScript tag через API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag)

##### Обновления

Короткий срок кэширования внешнего файла обеспечивает регулярные автоматические обновления, что делает JavaScript tag идеальным выбором, если вы не хотите обновлять вставленный фрагмент при изменении конфигурации.

##### Источник кода мониторинга

Внешний файл загружается с вашего CDN.

##### Продолжительность кэширования

Внешний файл, содержащий код мониторинга и конфигурацию, обновляется в соответствии со своей продолжительностью кэширования, которая по умолчанию составляет один час и может быть настроена. Допустимые значения — низкие (несколько часов или дней) для обеспечения регулярного обновления конфигурации. Продолжительность кэширования определяет, как долго браузеры могут кэшировать файл. Если ваш CDN настроен согласно разделу [Make your cluster production ready](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring#managed-cluster-production-ready "Set up agentless monitoring for your web applications."), он кэширует файл в течение одного часа.

Чтобы настроить продолжительность кэширования:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Manual insertion**.
5. В разделе **JavaScript tag** используйте раскрывающийся список **Cache monitoring code and configuration for** для выбора необходимой продолжительности кэширования.

##### Выполнение скрипта

По умолчанию код мониторинга загружается и выполняется браузером синхронно. Для предотвращения блокирующего парсинг поведения можно настроить добавление атрибутов `async` или `defer`.

* С атрибутом `async` код мониторинга загружается параллельно с парсингом страницы и выполняется сразу после загрузки.
* С атрибутом `defer` код мониторинга также загружается параллельно, но выполнение откладывается до завершения парсинга страницы.

При использовании обоих атрибутов некоторые тайминги и пользовательские действия будут потеряны, пока код мониторинга не загружен и не инициализирован полностью.

Чтобы настроить выполнение скрипта:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Manual insertion**.
5. В разделе **JavaScript tag** задайте параметр **Script execution attribute** как **async**, **defer** или **No attribute**.
6. Скопируйте фрагмент и вставьте его в страницу.

При получении JavaScript tag через API управление выполнением скрипта осуществляется путём передачи параметра. Подробнее см. в разделе [GET JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Retrieve the most recent JavaScript tag for manual insertion.").

##### Добавление атрибута `crossorigin="anonymous"`

Включено по умолчанию

Внешний скрипт, на который ссылается JavaScript tag, обслуживается с вашего CDN, что приводит к запросу из другого источника. Для сбора подробных сообщений об ошибках JavaScript и таймингов ресурсов W3C необходимо включить атрибут `crossorigin="anonymous"` в тег скрипта.

Чтобы включить добавление атрибута `crossorigin="anonymous"`:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Manual insertion**.
5. В разделе **JavaScript tag** включите параметр **Add the crossorigin=anonymous attribute**.
6. Скопируйте фрагмент и вставьте его в страницу.

При получении JavaScript tag через API управление добавлением атрибута `crossorigin="anonymous"` осуществляется путём передачи параметра. Подробнее см. в разделе [GET JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Retrieve the most recent JavaScript tag for manual insertion.").

**OneAgent JavaScript tag** включает конфигурацию и ссылку на внешний файл с кодом мониторинга. Доступен как для ручной вставки, так и для автоматической инжекции.

[Получить OneAgent JavaScript tag через API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag)

##### Обновления

При ручной вставке OneAgent JavaScript tag необходимо обновлять вручную при каждом изменении конфигурации. Для обеспечения актуальности рекомендуется использовать его вместе с полностью автоматизированными обновлениями через API. Использование OneAgent JavaScript tag из веб-интерфейса не рекомендуется, если своевременность обновлений конфигурации критична.

При автоматической инжекции OneAgent всегда инжектирует OneAgent JavaScript tag с использованием актуальной конфигурации. Однако политика кэширования вашего приложения может влиять на частоту инжекции. Подробнее см. в разделе [Cache control header optimizations](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications").

##### Источник кода мониторинга

При агентлесс-мониторинге код мониторинга доставляется с вашего CDN. При автоматической инжекции или [ручной вставке для страниц автоматически инжектируемого приложения](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications") файл по умолчанию доставляется OneAgent, который инструментирует ваше приложение. Кроме того, возможна загрузка файла с вашего CDN — см. раздел [Request the monitoring code from your CDN](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring code source for your specific requirements.").

##### Продолжительность кэширования

Браузеры и ваш CDN могут кэшировать код мониторинга до одного года. Такая расширенная продолжительность кэширования обеспечивается за счёт включения версии RUM JavaScript и хэша активных модулей в URL файла.

##### Выполнение скрипта

По умолчанию код мониторинга загружается и выполняется браузером синхронно. Для предотвращения блокирующего парсинг поведения можно настроить добавление атрибутов `async` или `defer`.

* С атрибутом `async` код мониторинга загружается параллельно с парсингом страницы и выполняется сразу после загрузки.
* С атрибутом `defer` код мониторинга также загружается параллельно, но выполнение откладывается до завершения парсинга страницы.

При использовании обоих атрибутов некоторые тайминги и пользовательские действия будут потеряны, пока код мониторинга не загружен и не инициализирован полностью.

Чтобы настроить выполнение скрипта для автоматической инжекции:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Automatic injection**.
5. Если для параметра **Snippet format** выбрано значение **OneAgent JavaScript tag**, становится доступен параметр **Script execution attribute**. Выберите **async**, **defer** или **No attribute** из раскрывающегося списка.
6. Выберите **Save changes**.

Чтобы настроить выполнение скрипта для ручной вставки:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Manual insertion**.
5. В разделе **OneAgent JavaScript tag** задайте параметр **Script execution attribute** как **async**, **defer** или **No attribute**.
6. Скопируйте фрагмент и вставьте его в страницу.

При получении OneAgent JavaScript tag через API управление выполнением скрипта осуществляется путём передачи параметра. Подробнее см. в разделе [GET OneAgent JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Retrieve the most recent OneAgent JavaScript tag for manual insertion.").

**OneAgent JavaScript tag with SRI** позволяет использовать функцию браузера Subresource Integrity (SRI) для проверки того, что код мониторинга не был изменён, см. раздел [Use Subresource Integrity (SRI) for Real User Monitoring code](/managed/observe/digital-experience/web-applications/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring code."). Он включает конфигурацию, ссылку на внешний файл с кодом мониторинга и хэш целостности этого кода мониторинга. Поддерживается как для автоматической инжекции, так и для ручной вставки.

[Получить OneAgent JavaScript tag with SRI через API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri)

##### Обновления

При ручной вставке OneAgent JavaScript tag with SRI необходимо обновлять вручную при каждом изменении конфигурации. Для обеспечения актуальности рекомендуется использовать его вместе с полностью автоматизированными обновлениями через API. Использование OneAgent JavaScript tag with SRI из веб-интерфейса не рекомендуется, если своевременность обновлений конфигурации критична.

При автоматической инжекции OneAgent всегда инжектирует OneAgent JavaScript tag with SRI с использованием актуальной конфигурации. Однако политика кэширования вашего приложения может влиять на частоту инжекции. Подробнее см. в разделе [Cache control header optimizations](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications").

##### Источник кода мониторинга

Код мониторинга всегда доставляется с вашего CDN.

##### Продолжительность кэширования

Браузеры и ваш CDN могут кэшировать код мониторинга до одного года. Такая расширенная продолжительность кэширования обеспечивается за счёт включения версии RUM JavaScript и хэша активных модулей в URL файла.

##### Выполнение скрипта

По умолчанию код мониторинга загружается и выполняется браузером синхронно. Для предотвращения блокирующего парсинг поведения можно настроить добавление атрибутов `async` или `defer`.

* С атрибутом `async` код мониторинга загружается параллельно с парсингом страницы и выполняется сразу после загрузки.
* С атрибутом `defer` код мониторинга также загружается параллельно, но выполнение откладывается до завершения парсинга страницы.

При использовании обоих атрибутов некоторые тайминги и пользовательские действия будут потеряны, пока код мониторинга не загружен и не инициализирован полностью.

Чтобы настроить выполнение скрипта для автоматической инжекции:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Automatic injection**.
5. Если для параметра **Snippet format** выбрано значение **OneAgent JavaScript tag with SRI**, становится доступен параметр **Script execution attribute**. Выберите **async**, **defer** или **No attribute** из раскрывающегося списка.
6. Выберите **Save changes**.

Чтобы настроить выполнение скрипта для ручной вставки:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Manual insertion**.
5. В разделе **OneAgent JavaScript tag with SRI** задайте параметр **Script execution attribute** как **async**, **defer** или **No attribute**.
6. Скопируйте фрагмент и вставьте его в страницу.

При получении OneAgent JavaScript tag with SRI через API управление выполнением скрипта осуществляется путём передачи параметра. Подробнее см. в разделе [GET OneAgent JavaScript tag with SRI](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri "Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion.").

**Inline code** содержит как конфигурацию, так и код мониторинга RUM, сводя количество веб-запросов к минимуму. Обратите внимание, что код мониторинга Session Replay не инлайнится, поэтому при использовании Session Replay всё равно потребуется дополнительный запрос. Если ваш сайт состоит из большого количества отдельных страниц, использование inline code может не дать преимуществ, так как увеличивает размер каждого документа. Однако это может быть подходящим выбором для одностраничных приложений (SPA).

[Получить inline code через API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code)

##### Обновления

При ручной вставке inline code необходимо обновлять вручную при каждом изменении конфигурации. Для обеспечения актуальности рекомендуется использовать его вместе с полностью автоматизированными обновлениями через API. Использование inline code из веб-интерфейса не рекомендуется, если своевременность обновлений конфигурации критична.

При автоматической инжекции OneAgent всегда инжектирует inline code с использованием актуальной конфигурации. Однако политика кэширования вашего приложения может влиять на частоту инжекции. Подробнее см. в разделе [Cache control header optimizations](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications").

##### Источник кода мониторинга

При агентлесс-мониторинге код мониторинга Session Replay доставляется с вашего CDN. При автоматической инжекции или [ручной вставке для страниц автоматически инжектируемого приложения](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications") код мониторинга Session Replay по умолчанию доставляется OneAgent, который инструментирует ваше приложение. Кроме того, возможна загрузка с вашего CDN — см. раздел [Request the monitoring code from your CDN](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring code source for your specific requirements.").

##### Продолжительность кэширования

Поскольку код мониторинга RUM инлайнится, его продолжительность кэширования совпадает с кэшированием страницы, которое определяется настройками кэша на вашем веб-сервере. Код мониторинга Session Replay может кэшироваться до одного года браузерами и вашим CDN. Такая расширенная продолжительность кэширования обеспечивается за счёт включения версии RUM JavaScript в URL файла.

##### Выполнение скрипта

Код мониторинга загружается и выполняется браузером синхронно.

**Code snippet** содержит конфигурацию и базовую функциональность кода мониторинга. Доступен как для ручной вставки, так и для автоматической инжекции.

* При ручной вставке он внедряет в страницу ещё один элемент script, ссылающийся на внешний файл с полной функциональностью кода мониторинга.
* При автоматической инжекции этот второй элемент script инжектируется OneAgent при инжекции code snippet.

Внешний файл с полной функциональностью кода мониторинга можно настроить для загрузки синхронно или асинхронно с использованием атрибута `defer`, см. раздел [Script execution](#code-snippet-script-execution).

[Получить code snippet через API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-sync)

[Получить code snippet в отложенном режиме через API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-async)

##### Обновления

При ручной вставке обновления кода мониторинга и конфигурации становятся доступны после первой перезагрузки страницы. Для актуальности конфигурации с самого начала code snippet необходимо обновлять регулярно. Это также необходимо для гарантии совместимости между code snippet и внешним файлом, которую мы проверяем в течение одного года.

При автоматической инжекции OneAgent всегда инжектирует code snippet с использованием актуальной конфигурации. Однако политика кэширования вашего приложения может влиять на частоту инжекции. Подробнее см. в разделе [Cache control header optimizations](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications").

##### Источник кода мониторинга

При агентлесс-мониторинге внешний файл с полной функциональностью кода мониторинга доставляется с вашего CDN. При автоматической инжекции или [ручной вставке для страниц автоматически инжектируемого приложения](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications") он по умолчанию доставляется OneAgent, который инструментирует ваше приложение. Кроме того, возможна загрузка с вашего CDN — см. раздел [Request the monitoring code from your CDN](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring code source for your specific requirements.").

##### Продолжительность кэширования

Кэширование code snippet совпадает с кэшированием страницы, которое определяется конфигурацией вашего веб-сервера. Внешний файл может кэшироваться до одного года браузерами и вашим CDN. Такая расширенная продолжительность кэширования обеспечивается за счёт включения версии RUM JavaScript и хэша активных модулей в URL файла.

##### Выполнение скрипта

Внешний файл с полной функциональностью кода мониторинга можно настроить для загрузки синхронно или асинхронно с использованием атрибута `defer`. При асинхронной загрузке скрипт загружается параллельно с парсингом HTML и выполняется только после полного разбора документа. Пока код мониторинга не загружен полностью, некоторые тайминги и пользовательские действия будут потеряны.

Чтобы настроить выполнение скрипта для ручной вставки:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Manual insertion**.
5. В разделе **Code snippet** используйте раскрывающийся список **Load the monitoring code** для выбора **synchronously** или **deferred**.
6. Скопируйте фрагмент и вставьте его в страницу.

Чтобы настроить выполнение скрипта для автоматической инжекции:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Automatic injection**.
5. В разделе **Snippet format** выберите **Code snippet**.
6. В разделе **Load the monitoring code** выберите **synchronously** или **deferred**.
7. Выберите **Save changes**.