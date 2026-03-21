---
title: Пользовательские определения API
source: https://www.dynatrace.com/docs/observe/application-observability/services/customize-api-definitions
scraped: 2026-03-06T21:26:01.503322
---

* Latest Dynatrace
* How-to guide
* 1-min read

Для некоторых языков, например Node.js и Go, Dynatrace обеспечивает обнаружение на основе модулей и пакетов. Для Java и .NET используется базовый набор предопределённых API. Однако для остальных языков Dynatrace позволяет создавать пользовательские определения API для различных фреймворков в вашей среде. Пользовательские определения API используются для более детальной сегментации API и позволяют быстрее определять, в каких фреймворках сосредоточены узкие места.

Например, используя пользовательское определение API с именем `easyTravel`, Dynatrace может идентифицировать все вызовы методов, связанных с easyTravel, как часть кода, специфичного для easyTravel.

Чтобы добавить пользовательское правило обнаружения API:

1. Перейдите в **Settings** > **Server-side service monitoring** > **API detection rules**.
2. Выберите **Create API detection rule**.
3. Введите название API.
   В данном примере название API — **easyTravel**.
4. Выберите **Add new condition**.
   Шаблон для идентификации API в данном примере — `com.dynatrace.easytravel`.
5. Выберите **Confirm** для сохранения нового правила обнаружения API.

![Add API detection rule](https://dt-cdn.net/images/add-api-detection-rule-1316-08acb766e6.png)

Пользовательский API **easyTravel** теперь включён в анализ на уровне кода.

## Связанные темы

* [Settings API](../../../dynatrace-api/environment-api/settings.md "Find out what the Dynatrace Settings API offers.")
