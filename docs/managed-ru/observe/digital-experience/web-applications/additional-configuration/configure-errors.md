---
title: Настройка обнаружения ошибок для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-errors
scraped: 2026-05-12T11:34:55.477653
---

# Настройка обнаружения ошибок для веб-приложений

# Настройка обнаружения ошибок для веб-приложений

* How-to guide
* 8-min read
* Updated on Mar 05, 2026

Чтобы настроить захват ошибок, откройте редактирование приложения и разверните раздел **Errors**. Выберите нужный тип ошибки, затем настройте её захват, включение в [расчёты Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") или учёт при [обнаружении и анализе проблем Davis AI](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.").

## Типы ошибок

Dynatrace классифицирует [ошибки](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") по следующим типам.

* **Ошибки запросов** — обнаруживаются браузером и OneAgent на ваших серверах.
* **Пользовательские ошибки** — инициируются напрямую в вашем приложении через [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.").
* **Ошибки JavaScript** — обнаруженные браузером исключения JavaScript.

## Настройка ошибок запросов

По умолчанию Dynatrace считает все HTTP-коды статуса `4xx` и `5xx` ошибками запросов. Нарушения CSP и ошибки неудачных запросов изображений также фиксируются как ошибки запросов. Кроме того, RUM JavaScript может использовать [пользовательские коды статуса](#custom-status-codes) для информирования о проблемах фреймворка.

Параметры по умолчанию можно изменить, настроив правила ошибок запросов.

### Добавление правила ошибки запроса

Чтобы добавить правило ошибки запроса:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Errors** > **Request errors**.
5. Выберите **Add request error rule**.
6. Используйте хотя бы один из следующих параметров:

   * **Match by error code** — укажите отдельный HTTP-код ошибки, например `404`, или диапазон кодов ошибок, например `400-499`.
   * **Match by errors that have failed image requests**
   * **Match by errors that have CSP violations**
7. Необязательно: чтобы применять правило ошибки запроса только к определённым URL, настройте параметры в разделе **Filter settings**.
8. Укажите, следует ли **Capture this error**. Также можно включить **Include error in Apdex calculations** и **Include error in Davis AI problem detection and analysis**.

   ![Настройка правила ошибки запроса](https://dt-cdn.net/images/configure-request-error-1188-fed713c886.png)

   Настройка правила ошибки запроса

   Если выбрать включение ошибки в анализ Davis AI, Davis может зафиксировать её как новую открытую проблему.

Правила ошибок запросов выполняются в порядке их появления в списке ошибок. Зажмите **Drag row** ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") рядом с именем правила и перетащите его вверх или вниз в списке для изменения приоритета.

Также можно включить **Ignore request errors in Apdex calculations**, чтобы переопределить настройки Apdex для отдельных правил ошибок запросов.

### Управление пользовательскими кодами статуса

Помимо стандартных HTTP-кодов ошибок, RUM JavaScript может использовать пользовательские коды статуса для сигнализации об обнаруженных проблемах фреймворка.

Для приложений, созданных в Dynatrace версии 1.238 и выше, RUM JavaScript сообщает о некоторых ошибках запросов с использованием пользовательских кодов статуса `970`–`979`, когда реальный HTTP-код статуса недоступен. Обратите внимание, что эти пользовательские коды статуса не являются реальными HTTP-кодами; они лишь означают, что RUM JavaScript обнаружил ошибку, инициированную используемым фреймворком.

Влияние таких ошибок запросов на пользователей зависит от вашего приложения. Например, отменённый запрос к сервису отслеживания вряд ли повлияет на пользователей приложения. Однако неудачный запрос на оплату определённо доставит им неудобство.

RUM JavaScript использует следующие пользовательские коды статуса:

| Код | Название | Описание |
| --- | --- | --- |
| 970 | Error | Произошла неуказанная ошибка в используемом фреймворке. |
| 971 | Canceled | Запрос был отменён. |
| 972 | Timeout | Истекло время ожидания запроса. |
| 973 | Parse | Не удалось разобрать ответ. Сообщается модулями XMLHttpRequest, jQuery и MooTools. |
| 974 | Setup | Произошла ошибка при настройке запроса. Сообщается только модулем MooTools. |
| 979 | Unknown | Произошла неизвестная ошибка фреймворка. Сообщается только модулями jQuery и MooTools. |

#### Приложения, созданные начиная с версии Dynatrace 1.238

Для приложений, созданных начиная с версии Dynatrace 1.238, эти пользовательские коды статуса обнаруживаются автоматически. Они включаются в расчёты Apdex, но не учитываются в анализе Davis AI.

Если необходимо игнорировать эти пользовательские коды статуса, удалите или отключите правило ошибок запроса **HTTP 970-979**.

Чтобы удалить или отключить правило ошибок запроса **HTTP 970-979**:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Errors** > **Request errors**.
5. Найдите правило ошибки **HTTP 970-979** и выполните одно из следующих действий:

   * Выберите **Delete row** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") для полного удаления этого правила ошибки запроса.
   * Разверните правило и отключите **Capture this error**.

#### Приложения, созданные до версии Dynatrace 1.238

Для приложений, созданных в версиях Dynatrace ранее 1.238, пользовательские коды статуса не используются. Если необходимо их фиксировать, [добавьте правило ошибки запроса](#configure-request-errors) со следующими настройками:

* **Match by error code**: `970-979`
* **Capture this error**: `Enabled`
* **Include error in Apdex calculations**: `Enabled` или `Disabled` по необходимости
* **Include error in Davis AI problem detection and analysis**: `Enabled` или `Disabled` по необходимости

## Настройка пользовательских ошибок

Пользовательские ошибки позволяют обнаруживать собственные ошибки. Примером может служить ошибка, возникающая при проверке поля формы.

Для настройки пользовательской ошибки задайте, как Dynatrace должен обрабатывать ошибку, а затем инициируйте её в приложении с помощью [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.").

Чтобы добавить правило пользовательской ошибки:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Errors** > **Custom errors**.
5. Выберите **Add custom error rule**.
6. Укажите условия, по которым Dynatrace должен идентифицировать пользовательскую ошибку.

   * Используйте **Match key** и **Key pattern** для ключа `key` пользовательской ошибки.
   * Используйте **Match value** и **Value pattern** для значения `value` пользовательской ошибки.

     Правила пользовательских ошибок нечувствительны к регистру. Например, значения `mykey` и `MyKeY` считаются одинаковыми.
7. Укажите, следует ли **Capture this error**. Также можно включить **Include error in Apdex calculations** и **Include error in Davis AI problem detection and analysis**.

   ![Настройка правила пользовательской ошибки](https://dt-cdn.net/images/configure-custom-error-1188-d01572ccac.png)

   Настройка правила пользовательской ошибки

   Если выбрать включение ошибки в анализ Davis AI, Davis может зафиксировать её как новую открытую проблему.

Правила пользовательских ошибок выполняются в порядке их появления в списке ошибок. Зажмите **Drag row** ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") рядом с именем правила и перетащите его вверх или вниз в списке для изменения приоритета.

Также можно включить **Ignore custom errors in Apdex calculations**, чтобы переопределить настройки Apdex для отдельных правил пользовательских ошибок.

После добавления или исключения пользовательской ошибки в Dynatrace необходимо инициировать её в приложении с помощью метода `dtrum.reportCustomError()` [RUM JavaScript API](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.").

Например, для ошибки поля формы потребуются следующие параметры JavaScript-метода:

| Параметр | Описание | Пример |
| --- | --- | --- |
| `key` | Имя поля формы. | `custom_buying_form_number_of_travelers_field` |
| `value` | Ошибка валидации, инициированная валидатором. | `availability exceeded - e3434` |
| `hint` | Фактический ввод пользователя. | `1000` |

Для группировки и анализа пользовательских ошибок можно использовать только `key` и `value`; `hint` — необязательная информация.

Подробнее о создании отчётов о пользовательских ошибках см. [RUM JavaScript API — reportCustomError](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#reportcustomerror).

## Настройка ошибок JavaScript

Браузеры автоматически обнаруживают ошибки JavaScript, поэтому добавлять их вручную не требуется. Если настроен захват ошибок JavaScript, они автоматически включаются в расчёты Apdex и анализ Davis.

Чтобы игнорировать отдельную ошибку JavaScript, выберите **Ignore this JavaScript error** на странице с подробными сведениями об этой ошибке.

![Игнорирование ошибки JavaScript](https://dt-cdn.net/images/ignore-js-error-1217-3c39f37cfa.png)

Игнорирование ошибки JavaScript

Чтобы игнорировать все ошибки JavaScript в расчётах Apdex:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Errors** > **JavaScript errors**.
5. Включите **Ignore JavaScript errors in Apdex calculations**.

## Создание дополнительных оповещений об ошибках для Davis

Если стандартные оповещения об ошибках запросов, пользовательских и JavaScript-ошибках недостаточно чувствительны или необходимо сосредоточиться на конкретной ошибке, можно создать дополнительные оповещения.

Чтобы создать дополнительные оповещения об ошибках:

1. Перейдите в **Web** и выберите приложение для отображения страницы обзора приложения.
2. В инфографике выберите **Errors**.
3. В разделе **Errors by type** выберите **Analyze by type**.
4. В разделе **Detail analysis for selected timeframe** установите фильтры в поле **Filter by…**. Доступные фильтры в категории **Errors**: `Custom error name`, `Custom error type`, `Error type`, `Errors`, `Request error code`, `Request error resource` и `Request error type`.
5. Выберите **Create metric**.
6. В открывшемся оверлее настройте параметры метрики и выберите **Create metric**.
   Подробнее о создании и построении графиков вычисляемых метрик см. раздел [Создание вычисляемых метрик для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.").
7. Выберите **Create alert**.
8. Настройте параметры оповещения. По завершении выберите **Create custom event for alerting**.

   Подробнее о создании оповещения см. раздел [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

   Используйте статический порог равный `1`, если необходимо, чтобы Davis всегда фиксировал проблему при возникновении конкретной ошибки. Если интересны только аномалии для этой ошибки, используйте [автоматическое построение базовых линий](/managed/dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining "Learn how Dynatrace AI automatically calculates baselines based on a multi-dimensional baselining scheme.").