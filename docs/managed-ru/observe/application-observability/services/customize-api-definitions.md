---
title: Пользовательские определения API
source: https://docs.dynatrace.com/managed/observe/application-observability/services/customize-api-definitions
scraped: 2026-05-12T12:02:39.663830
---

# Пользовательские определения API

# Пользовательские определения API

* How-to guide
* 1-min read
* Published Nov 22, 2018

Для некоторых языков, таких как Node.js и Go, Dynatrace обеспечивает обнаружение на основе модулей и пакетов. Для Java и .NET используется базовый набор предопределённых API. Для других языков Dynatrace позволяет создавать пользовательские определения API для различных фреймворков в вашем окружении. Пользовательские определения API используются для дальнейшей сегментации разбивки API и упрощения быстрого выявления того, какие фреймворки содержат горячие точки.

Например, используя пользовательское определение API `easyTravel`, Dynatrace может идентифицировать все вызовы методов, связанных с easyTravel, как часть кода, специфичного для easyTravel.

Чтобы добавить пользовательское правило обнаружения API:

1. Перейдите в **Settings** > **Server-side service monitoring** > **API detection rules**.
2. Выберите **Create API detection rule**.
3. Введите имя API.
   В данном примере имя API — **easyTravel**.
4. Выберите **Add new condition**.
   В данном примере шаблон для идентификации API — `com.dynatrace.easytravel`.
5. Выберите **Confirm** для сохранения нового правила обнаружения API.

![Добавление правила обнаружения API](https://dt-cdn.net/images/add-api-detection-rule-1316-08acb766e6.png)

Добавление правила обнаружения API

Пользовательский API **easyTravel** теперь включён в анализ на уровне кода.

## Связанные темы

* [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.")