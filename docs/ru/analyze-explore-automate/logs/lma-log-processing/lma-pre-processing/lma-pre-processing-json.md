---
title: JSON обработка журналов с неэкранированными вложенными JSON строками
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing/lma-pre-processing/lma-pre-processing-json
scraped: 2026-03-06T21:28:23.371162
---

# Обработка JSON-логов с неэкранированными вложенными строками JSON


* Latest Dynatrace
* Explanation
* 2-min read

Предварительная обработка JSON-логов обнаруживает управляющие символы в строках JSON и преобразует их в структурированные объекты JSON для дальнейшей обработки и более глубокого анализа. Затем вы можете запрашивать неэкранированное JSON-поле с помощью функций DQL [jsonField](../../../../platform/grail/dynatrace-query-language/functions/string-functions.md#jsonField "A list of DQL string functions.") и [jsonPath](../../../../platform/grail/dynatrace-query-language/functions/string-functions.md#jsonPath "A list of DQL string functions.") для точного извлечения и фильтрации атрибутов логов.

## Преимущества

Преимущества предварительной обработки JSON-логов:

* Упрощённые запросы и визуализация вложенных JSON-логов.
* Автоматическая обработка экранированных строк JSON.
* Нет необходимости разбирать экранированные строки JSON вручную.

## Примечания по настройке

* В Dynatrace SaaS версии 1.331 и выше предварительная обработка JSON-логов включена по умолчанию. Её нельзя отключить или настроить, и она доступна только для новых сред.
* В Dynatrace SaaS версии 1.330 и ниже предварительная обработка JSON-логов недоступна.

## Снятие экранирования вложенных строк JSON

Многие инструменты пересылки логов оборачивают исходное сообщение лога в строки JSON внутри поля `content` с использованием управляющих символов.

Предварительная обработка JSON-логов выполняет следующие шаги.

1. Обнаруживает и снимает экранирование управляющих символов в строке JSON.
2. Преобразует строки JSON в структурированные объекты JSON. Преобразование происходит в процессе предварительной обработки логов, что делает результаты доступными для дальнейшей обработки в пользовательских конвейерах.

   Пример до предварительной обработки логов

   ```
   {


   "content": {


   "loglevel": "ERROR",


   "event": "{\\\"type\\\":\\\"db_error\\\",\\\"code\\\":\\\"CONN_FAIL\\\"}"


   },


   "source": "fluentbit",


   "host.name": "app-server-01"


   }
   ```

   Пример после предварительной обработки логов

   ```
   {


   "content": {


   "loglevel": "ERROR",


   "event": {


   "type": "db_error",


   "code": "CONN_FAIL"


   }


   },


   "source": "fluentbit",


   "host.name": "app-server-01"


   }
   ```

## Запрос неэкранированного JSON с помощью DQL

Вы можете запрашивать неэкранированное JSON-поле для точного извлечения и фильтрации атрибутов логов с помощью следующих функций DQL.

* Функция [jsonField](../../../../platform/grail/dynatrace-query-language/functions/string-functions.md#jsonField "A list of DQL string functions.") для извлечения значения по его фактическому имени.

  Пример извлечения `loglevel` с помощью `jsonField`.

  ```
  fetch logs


  | fieldsAdd logLevel = jsonField(content, "loglevel")


  | filter logLevel == "ERROR"
  ```
* Функция [jsonPath](../../../../platform/grail/dynatrace-query-language/functions/string-functions.md#jsonPath "A list of DQL string functions.") для извлечения значения по выражению `JSONPath`.

  Пример извлечения `eventType` с помощью `jsonPath`.

  ```
  fetch logs


  | fieldsAdd eventType = jsonPath(content, "$.event.type")


  | filter eventType == "db_error"
  ```

Неверный JSON

Снятие экранирования — например, удаление обратной косой черты — пропускается, если JSON является недействительным. Исходное содержимое остаётся без изменений.

## Связанные темы

* Обработка логов с OpenPipeline
