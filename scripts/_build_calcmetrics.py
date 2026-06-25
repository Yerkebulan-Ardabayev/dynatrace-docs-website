# -*- coding: utf-8 -*-
"""L4O builder: configuration-api/calculated-metrics/ top parent +
mobile-app-metrics/ (6) + rum-metrics/ (6) + synthetic-metrics/ (6) = 19 files.
service-metrics/ DEFERRED (json-models.md 932 = L42, post/put 767/798 big).

Splice method (L98/L100): start from EN, CRLF->LF, strip BOM, apply ordered
exact-string canon replacements -> byte-identical JSON + line parity.
ACTIVE API (no deprecated banner, L89/L90). No env-api calc twin ->
L103 case (b): anchor = config-api L99 (reports-api RU) + k8s-credentials RU
shared objects (StubList/EntityShortRepresentation/Error/ConstraintViolation).
Domain corpus-dominant (158x вычисляем* vs 13 расчётн* vs 45 EN):
"calculated metric"->"вычисляемая метрика"; "mobile app"->"мобильное
приложение", "web application"->"веб-приложение", "synthetic metric"->
"синтетическая метрика" (only RU precedent), "synthetic monitor"->EN
(229 EN dominant), "clickpath"->EN (80 EN dominant). Object-names/enum
EN-lock (L99). Related-topics link-text = target RU H1 (L4M/L4L canon)."""

import os, io

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
CM = "calculated-metrics"

FILES = [
    f"{CM}.md",
    f"{CM}/mobile-app-metrics.md",
    f"{CM}/mobile-app-metrics/del-metric.md",
    f"{CM}/mobile-app-metrics/get-all.md",
    f"{CM}/mobile-app-metrics/get-metric.md",
    f"{CM}/mobile-app-metrics/post-metric.md",
    f"{CM}/mobile-app-metrics/put-metric.md",
    f"{CM}/rum-metrics.md",
    f"{CM}/rum-metrics/del-metric.md",
    f"{CM}/rum-metrics/get-all.md",
    f"{CM}/rum-metrics/get-metric.md",
    f"{CM}/rum-metrics/post-metric.md",
    f"{CM}/rum-metrics/put-metric.md",
    f"{CM}/synthetic-metrics.md",
    f"{CM}/synthetic-metrics/del-metric.md",
    f"{CM}/synthetic-metrics/get-all.md",
    f"{CM}/synthetic-metrics/get-metric.md",
    f"{CM}/synthetic-metrics/post-metric.md",
    f"{CM}/synthetic-metrics/put-metric.md",
]

# Ordered (EN, RU): specific/longer first; global "element can hold" LAST.
R = [
    # ---------- (A) Related-topics title-attrs (longest first) ----------
    (
        "Create calculated metrics as well as custom charts based on calculated metrics for your mobile applications.",
        "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших мобильных приложений.",
    ),
    (
        "Create calculated metrics as well as custom charts based on calculated metrics for your custom applications.",
        "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших пользовательских приложений.",
    ),
    (
        "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.",
        "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших веб-приложений.",
    ),
    (
        "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.",
        "Узнайте о Synthetic Monitoring и о том, как создать браузерный монитор одного URL, браузерный clickpath или HTTP-монитор.",
    ),
    (
        "Learn how to analyze browser-monitor data points.",
        "Узнайте, как анализировать точки данных браузерных мониторов.",
    ),
    # ---------- (B) Related-topics link-text (= target RU H1; L4M/L4L) ----------
    # Synthetic Monitoring / Multidimensional... target RU H1 still EN -> keep EN
    (
        "[Create calculated metrics for mobile applications]",
        "[Создание вычисленных метрик для мобильных приложений]",
    ),
    (
        "[Create calculated metrics for custom applications]",
        "[Создание вычисляемых метрик для пользовательских приложений]",
    ),
    (
        "[Create calculated metrics for web applications]",
        "[Создание вычисляемых метрик для веб-приложений]",
    ),
    # ---------- (C) top-parent / sub-parent card title-attrs (X via the Dynatrace API.) ----------
    (
        "View all calculated mobile apps metrics of your environment via the Dynatrace API.",
        "Просмотр всех вычисляемых метрик мобильных приложений вашего окружения мониторинга через Dynatrace API.",
    ),
    (
        "View all calculated service metrics of your environment via the Dynatrace API.",
        "Просмотр всех вычисляемых метрик сервиса вашего окружения мониторинга через Dynatrace API.",
    ),
    (
        "View all calculated synthetic metrics of your environment via the Dynatrace API.",
        "Просмотр всех вычисляемых синтетических метрик вашего окружения мониторинга через Dynatrace API.",
    ),
    (
        "View all calculated web application metrics of your environment via the Dynatrace API.",
        "Просмотр всех вычисляемых метрик веб-приложений вашего окружения мониторинга через Dynatrace API.",
    ),
    (
        "View a calculated mobile apps metric via the Dynatrace API.",
        "Просмотр вычисляемой метрики мобильного приложения через Dynatrace API.",
    ),
    (
        "View a calculated service metric via the Dynatrace API.",
        "Просмотр вычисляемой метрики сервиса через Dynatrace API.",
    ),
    (
        "View a calculated synthetic metric via the Dynatrace API.",
        "Просмотр вычисляемой синтетической метрики через Dynatrace API.",
    ),
    (
        "View a calculated web application metric via the Dynatrace API.",
        "Просмотр вычисляемой метрики веб-приложения через Dynatrace API.",
    ),
    (
        "Create a calculated mobile apps metric via the Dynatrace API.",
        "Создание вычисляемой метрики мобильного приложения через Dynatrace API.",
    ),
    (
        "Create a calculated service metric via the Dynatrace API.",
        "Создание вычисляемой метрики сервиса через Dynatrace API.",
    ),
    (
        "Create a calculated synthetic metric via the Dynatrace API.",
        "Создание вычисляемой синтетической метрики через Dynatrace API.",
    ),
    (
        "Create a calculated web application metric via the Dynatrace API.",
        "Создание вычисляемой метрики веб-приложения через Dynatrace API.",
    ),
    (
        "Edit a calculated mobile apps metric via the Dynatrace API.",
        "Редактирование вычисляемой метрики мобильного приложения через Dynatrace API.",
    ),
    (
        "Edit a calculated synthetic metric via the Dynatrace API.",
        "Редактирование вычисляемой синтетической метрики через Dynatrace API.",
    ),
    (
        "Edit a calculated web application metric via the Dynatrace API.",
        "Редактирование вычисляемой метрики веб-приложения через Dynatrace API.",
    ),
    (
        "Update a calculated service metric via the Dynatrace API.",
        "Обновление вычисляемой метрики сервиса через Dynatrace API.",
    ),
    (
        "Delete a calculated mobile apps metric via the Dynatrace API.",
        "Удаление вычисляемой метрики мобильного приложения через Dynatrace API.",
    ),
    (
        "Delete a calculated service metric via the Dynatrace API.",
        "Удаление вычисляемой метрики сервиса через Dynatrace API.",
    ),
    (
        "Delete a calculated synthetic metric via the Dynatrace API.",
        "Удаление вычисляемой синтетической метрики через Dynatrace API.",
    ),
    (
        "Delete a calculated web application metric via the Dynatrace API.",
        "Удаление вычисляемой метрики веб-приложения через Dynatrace API.",
    ),
    # ---------- (D) top-parent bullet link-text ----------
    ("[View all mobile apps metrics]", "[Просмотр всех метрик мобильных приложений]"),
    ("[View a mobile apps metric]", "[Просмотр метрики мобильного приложения]"),
    ("[Edit a mobile apps metric]", "[Редактирование метрики мобильного приложения]"),
    ("[Delete a mobile apps metric]", "[Удаление метрики мобильного приложения]"),
    ("[View all service metrics]", "[Просмотр всех метрик сервиса]"),
    ("[View a service metric]", "[Просмотр метрики сервиса]"),
    ("[Create a service metric]", "[Создание метрики сервиса]"),
    ("[Edit a service metric]", "[Редактирование метрики сервиса]"),
    ("[Delete a service metric]", "[Удаление метрики сервиса]"),
    ("[View all synthetic metrics]", "[Просмотр всех синтетических метрик]"),
    ("[View a synthetic metric]", "[Просмотр синтетической метрики]"),
    ("[Create a synthetic metric]", "[Создание синтетической метрики]"),
    ("[Edit a synthetic metric]", "[Редактирование синтетической метрики]"),
    ("[Delete a synthetic metric]", "[Удаление синтетической метрики]"),
    ("[View all web application metrics]", "[Просмотр всех метрик веб-приложений]"),
    ("[View a web application metric]", "[Просмотр метрики веб-приложения]"),
    ("[Edit a web application metric]", "[Редактирование метрики веб-приложения]"),
    ("[Delete a web application metric]", "[Удаление метрики веб-приложения]"),
    # top-parent group headings (common nouns translated; Synthetic EN feature)
    ("### Mobile apps\n", "### Мобильные приложения\n"),
    ("### Service\n", "### Сервис\n"),
    ("### Web application\n", "### Веб-приложение\n"),
    # ---------- (E) sub-parent card titles + descriptions ----------
    ("### List all metrics", "### Список всех метрик"),
    ("### View a metric", "### Просмотр метрики"),
    ("### Create a metric", "### Создание метрики"),
    ("### Edit a metric", "### Редактирование метрики"),
    ("### Delete a metric", "### Удаление метрики"),
    (
        "Get an overview of all calculated mobile app metrics stored in your environment.",
        "Обзор всех вычисляемых метрик мобильных приложений, хранящихся в вашем окружении.",
    ),
    (
        "Get an overview of all calculated web application metrics stored in your environment.",
        "Обзор всех вычисляемых метрик веб-приложений, хранящихся в вашем окружении.",
    ),
    (
        "Get an overview of all calculated synthetic metrics stored in your environment.",
        "Обзор всех вычисляемых синтетических метрик, хранящихся в вашем окружении.",
    ),
    (
        "Get the descriptor of a calculated mobile app metric by metric key.",
        "Получить дескриптор вычисляемой метрики мобильного приложения по ключу метрики.",
    ),
    (
        "Get the descriptor of a calculated web application metric by metric key.",
        "Получить дескриптор вычисляемой метрики веб-приложения по ключу метрики.",
    ),
    (
        "Get the descriptor of a calculated synthetic metric by metric key.",
        "Получить дескриптор вычисляемой синтетической метрики по ключу метрики.",
    ),
    (
        "Create a calculated mobile app metric.",
        "Создать вычисляемую метрику мобильного приложения.",
    ),
    (
        "Create a calculated web application metric.",
        "Создать вычисляемую метрику веб-приложения.",
    ),
    (
        "Create a calculated synthetic metric.",
        "Создать вычисляемую синтетическую метрику.",
    ),
    (
        "Update a calculated mobile app metric.",
        "Обновить вычисляемую метрику мобильного приложения.",
    ),
    (
        "Update a calculated web application metric.",
        "Обновить вычисляемую метрику веб-приложения.",
    ),
    (
        "Update a calculated synthetic metric.",
        "Обновить вычисляемую синтетическую метрику.",
    ),
    (
        "Delete a metric that you no longer need.",
        "Удалить метрику, которая вам больше не нужна.",
    ),
    # ---------- (F) endpoint intro one-liners ----------
    (
        "Lists all calculated mobile app metrics.",
        "Выводит список всех вычисляемых метрик мобильных приложений.",
    ),
    (
        "Lists all calculated web application metrics.",
        "Выводит список всех вычисляемых метрик веб-приложений.",
    ),
    (
        "Lists all calculated synthetic metrics.",
        "Выводит список всех вычисляемых синтетических метрик.",
    ),
    (
        "Gets the descriptor of the specified calculated mobile app metric.",
        "Возвращает дескриптор указанной вычисляемой метрики мобильного приложения.",
    ),
    (
        "Gets the descriptor of the specified calculated web application metric.",
        "Возвращает дескриптор указанной вычисляемой метрики веб-приложения.",
    ),
    (
        "Gets the descriptor of the specified calculated synthetic metric.",
        "Возвращает дескриптор указанной вычисляемой синтетической метрики.",
    ),
    (
        "Creates a new calculated mobile app metric.",
        "Создаёт новую вычисляемую метрику мобильного приложения.",
    ),
    (
        "Creates a new calculated web application metric.",
        "Создаёт новую вычисляемую метрику веб-приложения.",
    ),
    (
        "Creates a new calculated synthetic metric.",
        "Создаёт новую вычисляемую синтетическую метрику.",
    ),
    (
        "Updates the descriptor of the specified calculated mobile app metric.",
        "Обновляет дескриптор указанной вычисляемой метрики мобильного приложения.",
    ),
    (
        "Updates the descriptor of the specified calculated web application metric.",
        "Обновляет дескриптор указанной вычисляемой метрики веб-приложения.",
    ),
    (
        "Updates the descriptor of the specified calculated synthetic metric.",
        "Обновляет дескриптор указанной вычисляемой синтетической метрики.",
    ),
    (
        "Deletes the specified calculated mobile app metric. Deletion cannot be undone!",
        "Удаляет указанную вычисляемую метрику мобильного приложения. Удаление невозможно отменить!",
    ),
    (
        "Deletes the specified calculated web application metric. Deletion cannot be undone!",
        "Удаляет указанную вычисляемую метрику веб-приложения. Удаление невозможно отменить!",
    ),
    (
        "Deletes the specified calculated synthetic metric. Deletion cannot be undone!",
        "Удаляет указанную вычисляемую синтетическую метрику. Удаление невозможно отменить!",
    ),
    # ---------- (G) standard phrases (config-api L99) ----------
    (
        "The request consumes and produces an `application/json` payload.",
        "Запрос принимает и возвращает payload `application/json`.",
    ),
    (
        "The request produces an `application/json` payload.",
        "Запрос возвращает payload `application/json`.",
    ),
    (
        "The request consumes an `application/json` payload.",
        "Запрос принимает payload `application/json`.",
    ),
    (
        "To execute this request, you need an access token with `WriteConfig` scope.",
        "Для выполнения этого запроса нужен access token со scope `WriteConfig`.",
    ),
    (
        "To execute this request, you need an access token with `ReadConfig` scope.",
        "Для выполнения этого запроса нужен access token со scope `ReadConfig`.",
    ),
    (
        "To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
        "Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
    ),
    (
        "The request doesn't provide any configurable parameters.",
        "В запросе нет настраиваемых параметров.",
    ),
    (
        "This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.",
        "Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.",
    ),
    (
        "We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.",
        "Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.",
    ),
    # ---------- (H) headings (newline-anchored; ## Validate payload EN) ----------
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n### Authentication\n", "\n### Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
    ("\n## Response\n", "\n## Ответ\n"),
    ("\n### Response\n", "\n### Ответ\n"),
    ("\n### Response codes\n", "\n### Коды ответа\n"),
    ("\n#### Response codes\n", "\n#### Коды ответа\n"),
    ("\n### Request body objects\n", "\n### Объекты тела запроса\n"),
    ("\n### Response body objects\n", "\n### Объекты тела ответа\n"),
    ("\n#### Response body objects\n", "\n#### Объекты тела ответа\n"),
    ("\n### Request body JSON model\n", "\n### JSON-модель тела запроса\n"),
    ("\n### Response body JSON models\n", "\n### JSON-модели тела ответа\n"),
    ("\n#### Response body JSON models\n", "\n#### JSON-модели тела ответа\n"),
    ("\n## Related topics\n", "\n## Связанные темы\n"),
    # ---------- (I) object headings ----------
    (
        "#### The `CalculatedMobileMetricUserActionFilter` object",
        "#### Объект `CalculatedMobileMetricUserActionFilter`",
    ),
    (
        "#### The `CalculatedMobileMetricDimension` object",
        "#### Объект `CalculatedMobileMetricDimension`",
    ),
    (
        "#### The `CalculatedMobileMetricUpdate` object",
        "#### Объект `CalculatedMobileMetricUpdate`",
    ),
    (
        "#### The `CalculatedMobileMetric` object",
        "#### Объект `CalculatedMobileMetric`",
    ),
    (
        "#### The `WebApplicationDimensionDefinition` object",
        "#### Объект `WebApplicationDimensionDefinition`",
    ),
    (
        "#### The `WebApplicationMetricDefinition` object",
        "#### Объект `WebApplicationMetricDefinition`",
    ),
    (
        "#### The `WebApplicationMetricUpdate` object",
        "#### Объект `WebApplicationMetricUpdate`",
    ),
    (
        "#### The `WebApplicationMetric` object",
        "#### Объект `WebApplicationMetric`",
    ),
    (
        "#### The `UserActionPropertyFilter` object",
        "#### Объект `UserActionPropertyFilter`",
    ),
    ("#### The `UserActionFilter` object", "#### Объект `UserActionFilter`"),
    (
        "#### The `SyntheticMetricDimension` object",
        "#### Объект `SyntheticMetricDimension`",
    ),
    (
        "#### The `SyntheticMetricFilter` object",
        "#### Объект `SyntheticMetricFilter`",
    ),
    (
        "#### The `SyntheticMetricUpdate` object",
        "#### Объект `SyntheticMetricUpdate`",
    ),
    (
        "#### The `CalculatedSyntheticMetric` object",
        "#### Объект `CalculatedSyntheticMetric`",
    ),
    ("#### The `StubList` object", "#### Объект `StubList`"),
    (
        "#### The `EntityShortRepresentation` object",
        "#### Объект `EntityShortRepresentation`",
    ),
    ("#### The `ErrorEnvelope` object", "#### Объект `ErrorEnvelope`"),
    ("#### The `Error` object", "#### Объект `Error`"),
    ("#### The `ConstraintViolation` object", "#### Объект `ConstraintViolation`"),
    # ---------- (J) object / section descriptions ----------
    (
        "Definition of the calculated metric for mobile or custom app.",
        "Определение вычисляемой метрики для мобильного или пользовательского приложения.",
    ),
    (
        "User actions filter of the calculated metric for mobile or custom app.",
        "Фильтр пользовательских действий вычисляемой метрики для мобильного или пользовательского приложения.",
    ),
    (
        "Update of the calculated mobile or custom metric.",
        "Обновление вычисляемой метрики мобильного или пользовательского приложения.",
    ),
    (
        "Dimension of the calculated mobile metric.",
        "Измерение вычисляемой метрики мобильного приложения.",
    ),
    (
        "Descriptor of the calculated web application metric.",
        "Дескриптор вычисляемой метрики веб-приложения.",
    ),
    (
        "Dimension of the calculated web application metrics.",
        "Измерение вычисляемых метрик веб-приложений.",
    ),
    (
        "Definition of the web application metric.",
        "Определение метрики веб-приложения.",
    ),
    (
        "The update of the calculated web application metric.",
        "Обновление вычисляемой метрики веб-приложения.",
    ),
    (
        "User actions filter of the calculated web application metric.",
        "Фильтр пользовательских действий вычисляемой метрики веб-приложения.",
    ),
    (
        "Only user actions matching the provided criteria are used for metric calculation.",
        "Для расчёта метрики используются только пользовательские действия, соответствующие заданным критериям.",
    ),
    (
        "A user action must match **all** the criteria.",
        "Пользовательское действие должно соответствовать **всем** критериям.",
    ),
    ("User action property filter.", "Фильтр свойств пользовательского действия."),
    (
        "Definition of the calculated synthetic metric.",
        "Определение вычисляемой синтетической метрики.",
    ),
    (
        "Dimension of the calculated synthetic metric.",
        "Измерение вычисляемой синтетической метрики.",
    ),
    (
        "Filter of the calculated synthetic metric.",
        "Фильтр вычисляемой синтетической метрики.",
    ),
    (
        "The update of the calculated synthetic metric.",
        "Обновление вычисляемой синтетической метрики.",
    ),
    (
        "An ordered list of short representations of Dynatrace entities.",
        "Упорядоченный список кратких представлений сущностей Dynatrace.",
    ),
    (
        "The short representation of a Dynatrace entity.",
        "Краткое представление сущности Dynatrace.",
    ),
    # ---------- (K) shared k8s/config canon (EntityShortRep / Error) ----------
    (
        "A short description of the Dynatrace entity.",
        "Краткое описание сущности Dynatrace.",
    ),
    ("The ID of the Dynatrace entity.", "ID сущности Dynatrace."),
    ("The name of the Dynatrace entity.", "Имя сущности Dynatrace."),
    ("The HTTP status code", "HTTP-код статуса"),
    ("A list of constraint violations", "Список нарушений ограничений"),
    ("The error message", "Сообщение об ошибке"),
    # ---------- (L) table headers (longest first) ----------
    (
        "| Parameter | Type | Description | In | Required |",
        "| Параметр | Тип | Описание | Где | Обязательный |",
    ),
    (
        "| Element | Type | Description | Required |",
        "| Элемент | Тип | Описание | Обязательный |",
    ),
    ("| Element | Type | Description |", "| Элемент | Тип | Описание |"),
    ("| Code | Type | Description |", "| Код | Тип | Описание |"),
    ("| Code | Description |", "| Код | Описание |"),
    # ---------- (M) response-code cells (L101: period BY SOURCE; period-variant first) ----------
    ("| Failed. The input is invalid. |", "| Сбой. Невалидный ввод. |"),
    ("| Failed. The input is invalid |", "| Сбой. Невалидный ввод |"),
    (" | Success |", " | Успех |"),
    (
        "Success. The calculated mobile metric has been created. Response contains its key and name.",
        "Успех. Вычисляемая метрика мобильного приложения создана. Тело ответа содержит её ключ и имя.",
    ),
    (
        "Success. The calculated synthetic metric has been created. Response contains its key and name.",
        "Успех. Вычисляемая синтетическая метрика создана. Тело ответа содержит её ключ и имя.",
    ),
    (
        "Success. The metric has been created. Response contains its key and name.",
        "Успех. Метрика создана. Тело ответа содержит её ключ и имя.",
    ),
    (
        "Validated. The submitted calculated synthetic metric is valid. The response doesn't have a body.",
        "Validated. Переданная вычисляемая синтетическая метрика валидна. Ответ без тела.",
    ),
    (
        "Validated. The submitted metric is valid. The response doesn't have a body.",
        "Validated. Переданная метрика валидна. Ответ без тела.",
    ),
    (
        "Success. The calculated synthetic metric has been updated. Response doesn't have a body.",
        "Успех. Вычисляемая синтетическая метрика обновлена. Ответ без тела.",
    ),
    (
        "Success. The metric has been updated. Response doesn't have a body.",
        "Успех. Метрика обновлена. Ответ без тела.",
    ),
    (
        "Deleted. Response doesn't have a body.",
        "Удалено. Ответ без тела.",
    ),
    # ---------- (N) parameter (path/body) cell descriptions ----------
    (
        "The JSON body of the request. Contains the definition of the new calculated metric for mobile or custom app.",
        "JSON-тело запроса. Содержит определение новой вычисляемой метрики для мобильного или пользовательского приложения.",
    ),
    (
        "The JSON body of the request. Contains the descriptor of the new calculated web application metric.",
        "JSON-тело запроса. Содержит дескриптор новой вычисляемой метрики веб-приложения.",
    ),
    (
        "The JSON body of the request. Contains definition of the new calculated synthetic metric.",
        "JSON-тело запроса. Содержит определение новой вычисляемой синтетической метрики.",
    ),
    (
        "The JSON body of the request. Contains the updated definition of the calculated mobile metric.",
        "JSON-тело запроса. Содержит обновлённое определение вычисляемой метрики мобильного приложения.",
    ),
    (
        "The JSON body of the request. Contains the updated parameters of the calculated web application metric.",
        "JSON-тело запроса. Содержит обновлённые параметры вычисляемой метрики веб-приложения.",
    ),
    (
        "The JSON body of the request. Contains the update to the calculated synthetic metric.",
        "JSON-тело запроса. Содержит обновление вычисляемой синтетической метрики.",
    ),
    (
        "The key of the calculated synthetic metric to be deleted.",
        "Ключ вычисляемой синтетической метрики, которую нужно удалить.",
    ),
    (
        "The key of the calculated web application metric to be updated.",
        "Ключ вычисляемой метрики веб-приложения, которую нужно обновить.",
    ),
    (
        "The key of the calculated synthetic metric to be updated.",
        "Ключ вычисляемой синтетической метрики, которую нужно обновить.",
    ),
    (
        "The key of the required calculated synthetic metric.",
        "Ключ требуемой вычисляемой синтетической метрики.",
    ),
    ("The key of the metric to be deleted.", "Ключ метрики, которую нужно удалить."),
    ("The key of the metric to be updated.", "Ключ метрики, которую нужно обновить."),
    ("The key of the required metric.", "Ключ требуемой метрики."),
    # ---------- (O) element cell descriptions (shared) ----------
    (
        "The metric is enabled (`true`) or disabled (`false`).",
        "Метрика включена (`true`) или отключена (`false`).",
    ),
    (
        "The unique key of the metric.  The key must have the `calc:apps` prefix.",
        "Уникальный ключ метрики.  Ключ должен иметь префикс `calc:apps`.",
    ),
    (
        "The unique key of the metric.  The key must have the `calc:synthetic` prefix.",
        "Уникальный ключ метрики.  Ключ должен иметь префикс `calc:synthetic`.",
    ),
    (
        "The Dynatrace entity ID of the application to which the metric belongs.",
        "ID сущности Dynatrace приложения, которому принадлежит метрика.",
    ),
    (
        "The Dynatrace entity ID of the synthetic monitor to which the metric belongs.",
        "ID сущности Dynatrace synthetic monitor, которому принадлежит метрика.",
    ),
    ("A list of metric dimensions.", "Список измерений метрики."),
    (
        "The name of the metric, displayed in the UI.",
        "Имя метрики, отображаемое в UI.",
    ),
    ("The displayed name of the metric.", "Отображаемое имя метрики."),
    (
        "The number of top values to be calculated.",
        "Количество верхних значений для расчёта.",
    ),
    ("The type of the metric.", "Тип метрики."),
    ("The dimension of the metric.", "Измерение метрики."),
    (
        "The type of the web application metric.",
        "Тип метрики веб-приложения.",
    ),
    ("The type of the synthetic metric.", "Тип синтетической метрики."),
    (
        "The key of the user action property.  Only applicable for the `StringProperty` dimension.",
        "Ключ свойства пользовательского действия.  Применимо только для измерения `StringProperty`.",
    ),
    (
        "The key of the user action property.  Only applicable for `DoubleProperty` and `LongProperty` metrics.",
        "Ключ свойства пользовательского действия.  Применимо только для метрик `DoubleProperty` и `LongProperty`.",
    ),
    # ---------- (P) mobile UserActionFilter field descriptions ----------
    (
        "Only actions with a duration more than or equal to this value (in milliseconds) are included in the metric calculation.",
        "В расчёт метрики включаются только действия с длительностью больше или равной этому значению (в миллисекундах).",
    ),
    (
        "Only actions with a duration less than or equal to this value (in milliseconds) are included in the metric calculation.",
        "В расчёт метрики включаются только действия с длительностью меньше или равной этому значению (в миллисекундах).",
    ),
    (
        "Only actions with the specified Apdex score are included in the metric calculation.",
        "В расчёт метрики включаются только действия с указанной оценкой Apdex.",
    ),
    (
        "Only actions coming from this app version are included in the metric calculation.  The EQUALS operator applies.",
        "В расчёт метрики включаются только действия из этой версии приложения.  Применяется оператор EQUALS.",
    ),
    (
        "Only actions coming from this carrier type are included in the metric calculation.",
        "В расчёт метрики включаются только действия от оператора связи этого типа.",
    ),
    (
        "Only actions of users from this city are included in the metric calculation.  Specify geolocation ID here.",
        "В расчёт метрики включаются только действия пользователей из этого города.  Укажите здесь ID геолокации.",
    ),
    (
        "Only actions coming from this connection type are included in the metric calculation.",
        "В расчёт метрики включаются только действия из этого типа соединения.",
    ),
    (
        "Only actions of users from this continent are included in the metric calculation.  Specify geolocation ID here.",
        "В расчёт метрики включаются только действия пользователей с этого континента.  Укажите здесь ID геолокации.",
    ),
    (
        "Only actions of users from this country are included in the metric calculation.  Specify geolocation ID here.",
        "В расчёт метрики включаются только действия пользователей из этой страны.  Укажите здесь ID геолокации.",
    ),
    (
        "The HTTP error status of the actions to be included in the metric calculation:  * `true`: Only actions with HTTP errors are included. * `false`: All actions are included.",
        "Статус HTTP-ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с HTTP-ошибками. * `false`: включаются все действия.",
    ),
    (
        "The error status of the actions to be included in the metric calculation:  * `true`: Only actions with reported errors are included. * `false`: All actions are included.",
        "Статус ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с зарегистрированными ошибками. * `false`: включаются все действия.",
    ),
    (
        "Only actions coming from this internet service provider are included in the metric calculation.  The EQUALS operator applies.",
        "В расчёт метрики включаются только действия от этого интернет-провайдера.  Применяется оператор EQUALS.",
    ),
    (
        "Only actions coming from devices of this manufacturer are included in the metric calculation.  The EQUALS operator applies.",
        "В расчёт метрики включаются только действия с устройств этого производителя.  Применяется оператор EQUALS.",
    ),
    ("Filter by network technology", "Фильтр по сетевой технологии"),
    (
        "Only actions coming from devices with this display orientation are included in the metric calculation.",
        "В расчёт метрики включаются только действия с устройств с этой ориентацией экрана.",
    ),
    (
        "Only actions coming from this OS family are included in the metric calculation.  Specify the OS ID here.",
        "В расчёт метрики включаются только действия из этого семейства ОС.  Укажите здесь ID ОС.",
    ),
    (
        "Only actions coming from this OS version are included in the metric calculation.  Specify the OS ID here.",
        "В расчёт метрики включаются только действия из этой версии ОС.  Укажите здесь ID ОС.",
    ),
    (
        "Only actions of users from this region are included in the metric calculation.  Specify geolocation ID here.",
        "В расчёт метрики включаются только действия пользователей из этого региона.  Укажите здесь ID геолокации.",
    ),
    (
        "Only actions coming from devices with this display resolution are included in the metric calculation.",
        "В расчёт метрики включаются только действия с устройств с этим разрешением экрана.",
    ),
    (
        "Only actions with this name are included in the metric calculation.  The EQUALS operator applies.",
        "В расчёт метрики включаются только действия с этим именем.  Применяется оператор EQUALS.",
    ),
    # ---------- (Q) rum UserActionFilter / UserActionPropertyFilter ----------
    (
        "Only user actions coming from the specified browser family are included in the metric calculation.  The EQUALS operator applies.",
        "В расчёт метрики включаются только пользовательские действия из указанного семейства браузеров.  Применяется оператор EQUALS.",
    ),
    (
        "Only user actions coming from the specified browser type are included in the metric calculation.  The EQUALS operator applies.",
        "В расчёт метрики включаются только пользовательские действия из указанного типа браузера.  Применяется оператор EQUALS.",
    ),
    (
        "Only user actions coming from the specified browser version are included in the metric calculation.  The EQUALS operator applies.",
        "В расчёт метрики включаются только пользовательские действия из указанной версии браузера.  Применяется оператор EQUALS.",
    ),
    (
        "The status of custom actions in the metric calculation:  * `true`: Custom actions are included. * `false`: All actions are included.",
        "Статус кастомных действий в расчёте метрики:  * `true`: включаются кастомные действия. * `false`: включаются все действия.",
    ),
    (
        "The custom error name of the actions to be included in the metric calculation.",
        "Имя кастомной ошибки действий, включаемых в расчёт метрики.",
    ),
    (
        "The custom error type of the actions to be included in the metric calculation.",
        "Тип кастомной ошибки действий, включаемых в расчёт метрики.",
    ),
    (
        "Only user actions coming from the specified domain are included in the metric calculation.  The EQUALS operator applies.",
        "В расчёт метрики включаются только пользовательские действия из указанного домена.  Применяется оператор EQUALS.",
    ),
    (
        "The error status of the actions to be included in the metric calculation:  * `true`: Only actions that have any errors are included. * `false`: All actions are included.",
        "Статус ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с любыми ошибками. * `false`: включаются все действия.",
    ),
    (
        "The custom error status of the actions to be included in the metric calculation:  * `true`: Only actions with custom errors are included. * `false`: All actions are included.",
        "Статус кастомных ошибок действий, включаемых в расчёт метрики:  * `true`: включаются только действия с кастомными ошибками. * `false`: включаются все действия.",
    ),
    (
        "The request error status of the actions to be included in the metric calculation:  * `true`: Only actions with request errors (HTTP errors, failed images, CSP rule violations) are included. * `false`: All actions are included.",
        "Статус ошибок запросов действий, включаемых в расчёт метрики:  * `true`: включаются только действия с ошибками запросов (HTTP-ошибки, неудавшиеся изображения, нарушения правил CSP). * `false`: включаются все действия.",
    ),
    (
        "The JavaScript error status of the actions to be included in the metric calculation:  * `true`: Only actions with JavaScript errors are included. * `false`: All actions are included.",
        "Статус ошибок JavaScript действий, включаемых в расчёт метрики:  * `true`: включаются только действия с ошибками JavaScript. * `false`: включаются все действия.",
    ),
    (
        "The HTTP error status code of the actions to be included in the metric calculation.",
        "Код статуса HTTP-ошибки действий, включаемых в расчёт метрики.",
    ),
    (
        "Can be used in combination with `httpErrorCode` to define a range of error codes that will be included in the metric calculation.",
        "Можно использовать вместе с `httpErrorCode` для задания диапазона кодов ошибок, которые будут включены в расчёт метрики.",
    ),
    (
        "The request path that has been determined to be the origin of an HTTP error of the actions to be included in the metric calculation.",
        "Путь запроса, определённый как источник HTTP-ошибки действий, включаемых в расчёт метрики.",
    ),
    (
        "Only actions coming from this IP address are included in the metric calculation.  The EQUALS operator applies.",
        "В расчёт метрики включаются только действия с этого IP-адреса.  Применяется оператор EQUALS.",
    ),
    (
        "The IPv6 status of the actions to be included in the metric calculation:  * `true`: Only actions coming from IPv6 are included. * `false`: All actions are included.",
        "Статус IPv6 действий, включаемых в расчёт метрики:  * `true`: включаются только действия по IPv6. * `false`: включаются все действия.",
    ),
    (
        "The status of load actions in the metric calculation:  * `true`: Load actions are included. * `false`: All actions are included.",
        "Статус load-действий в расчёте метрики:  * `true`: включаются load-действия. * `false`: включаются все действия.",
    ),
    (
        "The status of actions coming from real users in the metric calculation:  * `true`: Only actions from real users are included. * `false`: All actions are included.",
        "Статус действий от реальных пользователей в расчёте метрики:  * `true`: включаются только действия реальных пользователей. * `false`: включаются все действия.",
    ),
    (
        "The status of actions coming from robots in the metric calculation:  * `true`: Only actions from robots are included. * `false`: All actions are included.",
        "Статус действий от роботов в расчёте метрики:  * `true`: включаются только действия роботов. * `false`: включаются все действия.",
    ),
    (
        "The status of actions coming from synthetic monitors in the metric calculation:  * `true`: Only actions from synthetic monitors are included. * `false`: All actions are included.",
        "Статус действий от synthetic monitors в расчёте метрики:  * `true`: включаются только действия от synthetic monitors. * `false`: включаются все действия.",
    ),
    (
        "Only actions on the specified group of views are included in the metric calculation.",
        "В расчёт метрики включаются только действия на указанной группе представлений.",
    ),
    (
        "Specifies the match type of the view group filter, e.g. using `Contains` or `Equals`. Defaults to `Equals`.",
        "Указывает тип совпадения для фильтра группы представлений, например с помощью `Contains` или `Equals`. По умолчанию `Equals`.",
    ),
    (
        "Only actions on the specified view are included in the metric calculation.",
        "В расчёт метрики включаются только действия на указанном представлении.",
    ),
    (
        "Specifies the match type of the view name filter, e.g. using `Contains` or `Equals`. Defaults to `Equals`.",
        "Указывает тип совпадения для фильтра имени представления, например с помощью `Contains` или `Equals`. По умолчанию `Equals`.",
    ),
    (
        "Only actions with the specified properties are included in the metric calculation.",
        "В расчёт метрики включаются только действия с указанными свойствами.",
    ),
    (
        "The status of XHR actions in the metric calculation:  * `true`: XHR actions are included. * `false`: All actions are included.",
        "Статус XHR-действий в расчёте метрики:  * `true`: включаются XHR-действия. * `false`: включаются все действия.",
    ),
    (
        "The status of route change actions in the metric calculation:  * `true`: Route change actions are included. * `false`: All actions are included.",
        "Статус действий смены маршрута в расчёте метрики:  * `true`: включаются действия смены маршрута. * `false`: включаются все действия.",
    ),
    (
        "Only actions that have a value greater than or equal to this are included in the metric calculation.  Only applicable to numerical values.",
        "В расчёт метрики включаются только действия со значением больше или равным этому.  Применимо только к числовым значениям.",
    ),
    (
        "The key of the action property we're checking.",
        "Ключ проверяемого свойства действия.",
    ),
    (
        "Specifies the match type of a string filter, e.g. using `Contains` or `Equals`.  Only applicable to string values.",
        "Указывает тип совпадения для строкового фильтра, например с помощью `Contains` или `Equals`.  Применимо только к строковым значениям.",
    ),
    (
        "Only actions that have a value less than or equal to this are included in the metric calculation.  Only applicable to numerical values.",
        "В расчёт метрики включаются только действия со значением меньше или равным этому.  Применимо только к числовым значениям.",
    ),
    (
        "Only actions that have this value in the specified property are included in the metric calculation.  Only applicable to string values.",
        "В расчёт метрики включаются только действия, у которых это значение в указанном свойстве.  Применимо только к строковым значениям.",
    ),
    # ---------- (R) synthetic SyntheticMetricFilter field descriptions ----------
    (
        "Only user actions of the specified type are included in the metric calculation.",
        "В расчёт метрики включаются только пользовательские действия указанного типа.",
    ),
    (
        "Only executions finished with the specified error code are included in the metric calculation.",
        "В расчёт метрики включаются только выполнения, завершившиеся с указанным кодом ошибки.",
    ),
    (
        "Only the specified browser clickpath event is included in the metric calculation.  Specify the Dynatrace entity ID of the event here. You can fetch the list of clickpath events of the monitor with the [GET a synthetic monitor](https://dt-url.net/4oe3kka) request from the Environment API",
        "В расчёт метрики включается только указанное событие browser clickpath.  Укажите здесь ID сущности Dynatrace события. Список clickpath-событий монитора можно получить запросом [GET a synthetic monitor](https://dt-url.net/4oe3kka) из Environment API",
    ),
    (
        "The execution status of the monitors to be included in the metric calculation:  * `true`: Only failed executions are included. * `false`: All executions are included.",
        "Статус выполнения мониторов, включаемых в расчёт метрики:  * `true`: включаются только неудавшиеся выполнения. * `false`: включаются все выполнения.",
    ),
    (
        "Only executions from the specified location are included in the metric calculation.  Specify the Dynatrace entity ID of the location here. You can fetch the list of locations the monitor is running from with the [GET a synthetic monitor](https://dt-url.net/4oe3kka) request from the Environment API.",
        "В расчёт метрики включаются только выполнения из указанной локации.  Укажите здесь ID сущности Dynatrace локации. Список локаций, из которых работает монитор, можно получить запросом [GET a synthetic monitor](https://dt-url.net/4oe3kka) из Environment API.",
    ),
    # ---------- (Z) global LAST: element-can-hold -> Возможные значения: (L99) ----------
    ("The element can hold these values", "Возможные значения:"),
]


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    with io.open(src, "r", encoding="utf-8", newline="") as f:
        t = f.read()
    t = t.replace("\r\n", "\n")  # EN is CRLF; RU corpus convention is LF
    t = t.replace("﻿", "").replace("ï»¿", "")  # BOM-mojibake guard (L4M)
    for en, ru in R:
        t = t.replace(en, ru)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return dst


if __name__ == "__main__":
    for rel in FILES:
        print("wrote", build(rel))
