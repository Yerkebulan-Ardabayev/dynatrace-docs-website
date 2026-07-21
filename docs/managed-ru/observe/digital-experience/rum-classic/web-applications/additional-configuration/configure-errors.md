---
title: Настройка обнаружения ошибок для веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-errors
---

# Настройка обнаружения ошибок для веб-приложений в RUM Classic

# Настройка обнаружения ошибок для веб-приложений в RUM Classic

* Практическое руководство
* 8 минут на чтение
* Обновлено 05 марта 2026 г.

Чтобы настроить порядок захвата ошибок, отредактируй приложение и разверни раздел **Errors**. Выбери нужный тип ошибки, а затем настрой, должна ли ошибка захватываться, учитываться в [расчётах Apdex](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Узнай, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.") или учитываться при [обнаружении и анализе проблем Davis AI](/managed/dynatrace-intelligence "Узнай, как Davis® AI обнаруживает аномалии производительности, определяет первопричины и использует модели ИИ для адаптивных пороговых значений во всей среде.").

## Типы ошибок

Dynatrace группирует [ошибки](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Узнай о пользовательских событиях и событиях ошибок, а также о типах таких событий, которые захватывает Dynatrace.") по следующим типам.

* **Request errors** обнаруживаются браузером и OneAgent на серверах.
* **Custom errors** запускаются непосредственно в приложении через [RUM JavaScript API](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Узнай, как настроить Real User Monitoring Classic с помощью JavaScript API.").
* **JavaScript errors**, это обнаруженные исключения JavaScript, выброшенные браузером.

## Настройка request errors

По умолчанию Dynatrace считает request error любой HTTP-код состояния `4xx` и `5xx`. Нарушения CSP и ошибки с неудачными запросами изображений также захватываются как request errors. Кроме того, RUM JavaScript может использовать [пользовательские коды состояния](#custom-status-codes), чтобы сообщать о проблемах фреймворка.

Настройки по умолчанию можно изменить, настроив правила request error.

### Добавление правила request error

Чтобы добавить правило request error

1. Перейди в **Web**.
2. Выбери приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбери **More** (**…**) > **Edit**.
4. В настройках приложения выбери **Errors** > **Request errors**.
5. Выбери **Add request error rule**.
6. Используй хотя бы один из следующих вариантов:

   * **Match by error code**. Укажи отдельный код ошибки HTTP, например `404`, либо целый диапазон кодов ошибок, например `400-499`.
   * **Match by errors that have failed image requests**
   * **Match by errors that have CSP violations**
7. Необязательно Чтобы применить правило request error только к определённым URL, настрой параметры в разделе **Filter settings**.
8. Укажи, нужно ли **Capture this error**. Также можно включить **Include error in Apdex calculations** и **Include error in Davis AI problem detection and analysis**.

   ![Настройка правила request error](https://dt-cdn.net/images/configure-request-error-1188-fed713c886.png)

   Настройка правила request error

   Если включить учёт ошибки в анализе Davis AI, Davis может сообщить об этой ошибке как о новой открытой проблеме.

Правила request error выполняются в порядке их появления в списке ошибок. Выбери и удерживай **Drag row** ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") рядом с названием правила и перемести правило вверх или вниз по списку, чтобы изменить его приоритет.

Также можно включить **Ignore request errors in Apdex calculations**, чтобы переопределить настройки Apdex для отдельных правил request error.

### Управление пользовательскими кодами состояния

Помимо захвата стандартных кодов ошибок HTTP, RUM JavaScript может также использовать пользовательские коды состояния, чтобы сигнализировать об обнаружении проблемы фреймворка.

Для приложений, созданных в Dynatrace версии 1.238 и выше, RUM JavaScript сообщает о некоторых request errors с помощью пользовательских кодов состояния `970`–`979`, если реальный код состояния HTTP захватить не удаётся. Обрати внимание, что эти пользовательские коды состояния не являются настоящими кодами состояния HTTP: они лишь означают, что RUM JavaScript обнаружил ошибку, вызванную используемым фреймворком.

Влияют ли такие request errors на пользователей, зависит от приложения. Например, если отправляется запрос к сервису отслеживания и запрос отменяется, такая ошибка едва ли сказывается на пользователях приложения. Однако неудачный запрос на оплату определённо создаст им неудобства.

RUM JavaScript использует следующие пользовательские коды состояния:

| Код | Название | Пояснение |
| --- | --- | --- |
| 970 | Error | В используемом фреймворке произошла неуточнённая ошибка. |
| 971 | Canceled | Запрос был отменён. |
| 972 | Timeout | По запросу истекло время ожидания. |
| 973 | Parse | Не удалось разобрать ответ. Сообщается модулем XMLHttpRequest, jQuery и MooTools. |
| 974 | Setup | При настройке запроса произошла ошибка. Сообщается только модулем MooTools. |
| 979 | Unknown | Произошла неизвестная ошибка фреймворка. Сообщается только модулями jQuery и MooTools. |

#### Приложения, созданные начиная с Dynatrace версии 1.238

Для приложений, созданных начиная с Dynatrace версии 1.238, эти пользовательские коды состояния обнаруживаются автоматически. Они учитываются в расчётах Apdex, но не учитываются при анализе Davis AI.

Чтобы игнорировать эти пользовательские коды состояния, удали или отключи правило request error **HTTP 970-979**.

Чтобы удалить или отключить правило request error **HTTP 970-979**

1. Перейди в **Web**.
2. Выбери приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбери **More** (**…**) > **Edit**.
4. В настройках приложения выбери **Errors** > **Request errors**.
5. Найди правило ошибки **HTTP 970-979** и выполни одно из следующего:

   * Выбери **Delete row** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove"), чтобы полностью удалить это правило request error.
   * Разверни правило и отключи **Capture this error**.

#### Приложения, созданные до Dynatrace версии 1.238

Для приложений, созданных в версиях Dynatrace более ранних, чем 1.238, пользовательские коды состояния не используются. Чтобы захватывать эти коды, [добавь правило request error](#configure-request-errors) со следующими настройками:

* **Match by error code**: `970-979`
* **Capture this error**: `Enabled`
* **Include error in Apdex calculations**: `Enabled` или `Disabled` в зависимости от потребностей
* **Include error in Davis AI problem detection and analysis**: `Enabled` или `Disabled` в зависимости от потребностей

## Настройка custom errors

Custom errors позволяют обнаруживать собственные ошибки. Пример такой ошибки, это ошибка, возникающая при валидации поля формы.

Чтобы настроить custom error, настрой, как Dynatrace должен обрабатывать ошибку, а затем вызови ошибку в приложении с помощью [RUM JavaScript API](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Узнай, как настроить Real User Monitoring Classic с помощью JavaScript API.").

Чтобы добавить правило custom error

1. Перейди в **Web**.
2. Выбери приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбери **More** (**…**) > **Edit**.
4. В настройках приложения выбери **Errors** > **Custom errors**.
5. Выбери **Add custom error rule**.
6. Укажи условия, которые Dynatrace должен использовать для определения custom error.

   * Используй **Match key** и **Key pattern** для `key` custom error.
   * Используй **Match value** и **Value pattern** для `value` custom error.

     Правила custom error нечувствительны к регистру. Например, значения `mykey` и `MyKeY` обрабатываются одинаково.
7. Укажи, нужно ли **Capture this error**. Также можно включить **Include error in Apdex calculations** и **Include error in Davis AI problem detection and analysis**.

   ![Настройка правила custom error](https://dt-cdn.net/images/configure-custom-error-1188-d01572ccac.png)

   Настройка правила custom error

   Если включить учёт ошибки в анализе Davis AI, Davis может сообщить об этой ошибке как о новой открытой проблеме.

Правила custom error выполняются в порядке их появления в списке ошибок. Выбери и удерживай **Drag row** ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") рядом с названием правила и перемести правило вверх или вниз по списку, чтобы изменить его приоритет.

Также можно включить **Ignore custom errors in Apdex calculations**, чтобы переопределить настройки Apdex для отдельных правил custom error.

После добавления или исключения custom error в Dynatrace нужно вызвать ошибку в приложении с помощью метода `dtrum.reportCustomError()` из [RUM JavaScript API](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Узнай, как настроить Real User Monitoring Classic с помощью JavaScript API.").

Например, ошибка поля формы потребует следующих параметров метода JavaScript:

| Параметр | Пояснение | Пример |
| --- | --- | --- |
| `key` | Название поля формы. | `custom_buying_form_number_of_travelers_field` |
| `value` | Ошибка валидации, вызванная валидатором. | `availability exceeded - e3434` |
| `hint` | Фактический ввод пользователя. | `1000` |

Для группировки и анализа custom errors можно использовать только `key` и `value`; `hint`, это необязательная информация.

Подробнее о том, как сообщать о custom errors, см. [RUM JavaScript API - reportCustomError﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#reportcustomerror).

## Настройка JavaScript errors

Браузеры автоматически определяют ошибки JavaScript, поэтому добавлять их вручную не нужно. Если настроен сбор ошибок JavaScript, они автоматически учитываются в расчётах Apdex и в анализе Davis.

Чтобы игнорировать отдельную ошибку JavaScript, нужно выбрать **Ignore this JavaScript error** на странице сведений об этой ошибке JavaScript.

![Ignoring a JavaScript error](https://dt-cdn.net/images/ignore-js-error-1217-3c39f37cfa.png)

Ignoring a JavaScript error

Чтобы игнорировать все ошибки JavaScript в расчётах Apdex

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Errors** > **JavaScript errors**.
5. Включить **Ignore JavaScript errors in Apdex calculations**.

## Создание дополнительных алертов об ошибках для Davis

Если готового оповещения об ошибках запросов, пользовательских и JavaScript-ошибок недостаточно, или нужно сосредоточиться на отдельной ошибке, можно создать дополнительные алерты об ошибках.

Чтобы создать дополнительные алерты об ошибках

1. Перейти в **Web** и выбрать приложение, чтобы открыть страницу обзора приложения.
2. На инфографике выбрать **Errors**.
3. В разделе **Errors by type** выбрать **Analyze by type**.
4. В разделе **Detail analysis for selected timeframe** задать фильтры в поле **Filter by…**. В категории **Errors** доступны фильтры `Custom error name`, `Custom error type`, `Error type`, `Errors`, `Request error code`, `Request error resource` и `Request error type`.
5. Выбрать **Create metric**.
6. В открывшемся окне настроить параметры метрики и выбрать **Create metric**.  
   Подробнее о создании и построении графиков вычисляемых метрик см. [Create calculated metrics for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.").
7. Выбрать **Create alert**.
8. Настроить параметры алерта. По завершении выбрать **Create custom event for alerting**.

   Подробнее о создании алерта см. [Metric events](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

   Использовать статический порог `1`, если нужно, чтобы Davis всегда поднимал проблему при возникновении конкретной ошибки. Если интересуют только аномалии по этой ошибке, использовать [auto-baselining](/managed/dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining "Learn how Dynatrace AI automatically calculates baselines based on a multi-dimensional baselining scheme.").