---
title: Примеры обработки OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/processing-examples
scraped: 2026-03-06T21:13:48.584554
---

* Latest Dynatrace
* Tutorial
* 13-min read

Эта статья посвящена сценариям обработки данных и содержит отдельные примеры настройки процессоров OpenPipeline для достижения результата.

## Настройка нового процессора

Чтобы настроить новый процессор в OpenPipeline

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** и выберите тип данных.
2. Найдите существующий конвейер или создайте новый.
3. Выберите этап.
4. Выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** и выберите процессор.
5. Настройте процессор, заполнив обязательные поля. Обратите внимание, что обязательные поля различаются в зависимости от процессора и отмечены в пользовательском интерфейсе.
6. Сохраните конвейер.

## Примеры

Разверните шаги для следующих примеров, чтобы узнать, как настроить процессоры.

### Исправление нераспознанной метки времени и уровня логирования на основе совпавшего источника логов

Сохранённое событие от приложения (`myLogSource`) в средстве просмотра логов не имеет корректной метки времени и уровня логирования. Вы можете извлечь эту информацию из источника и разобрать её для достижения следующего:

* Преобразовать нераспознанную метку времени в метку времени события лога.
* Отобразить уровень логирования для лога.
* Извлечь имя потока из строки лога в новый атрибут (`thread.name`).

### Шаги

1. Найдите условие совпадения.

   1. Перейдите в **Logs and events** ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") и включите **Advanced mode**.
   2. Введите следующий DQL-запрос для фильтрации данных логов из источника логов. Убедитесь, что заменили `myLogSource` на источник логов.

      ```
      fetch logs


      | filter matchesValue(log.source, "myLogSource")
      ```
   3. Выполните запрос и, когда результат фильтрации вас устроит, скопируйте функцию `matchesValue()`.

      ```
      matchesValue(log.source, "myLogSource")
      ```
2. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines** и выберите (или создайте) конвейер для источника загрузки логов.
3. Настройте процессор **DQL** на этапе **Processing** следующим образом.
4. Сохраните конвейер.

Заключение

Обработанная запись лога отображается с метаданными, включая `timestamp` и атрибут `loglevel` с корректными значениями, а также извлечённый атрибут `thread.name`. После загрузки новых данных обработанные записи содержат метку времени, уровень логирования и имя потока как отдельные атрибуты. Вы можете визуализировать новый формат, например, в блокноте.

**До**

```
{


"content":"April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",


"status":"NONE",


"timestamp":"1650889391528",


"log.source":"myLogSource",


"loglevel":"NONE"


}
```

**После**

```
{


"results":


[


{


"matched": true,


"record": {


"loglevel": "INFO",


"log.source": "myLogSource",


"thread.name": "myPool-thread-1",


"content": "April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",


"timestamp": "2022-04-24T09:59:52.000000000Z",


"status": "NONE"


}


}


]


}
```

### Разбор поля, содержащего JSON в виде необработанной строки

Запись имеет поле `content` (`String`), содержащее JSON-ввод, из которого вы хотите извлечь информацию. Вы можете обработать определённые поля, вложенные поля или все поля, и обработать их как обычный текст или вывести на верхний уровень без знания схемы JSON.

### Шаги

В зависимости от типа поля, которое вы хотите извлечь, настройте процессор **DQL** на этапе **Processing** с **определением процессора DQL**, скопированным из одного из следующих вариантов:

Определённые поля

Вложенные поля

Все поля без перечисления

Любое поле из JSON как обычный текст

Все поля с выводом на верхний уровень

```
parse content, "JSON{STRING:stringField:new.name}(flat=true)"


// Parses out a string field from raw record data into a standalone top-level attribute via a DPL JSON matcher.


// `flat=true` automatically creates attributes named as specified in the JSON. To rename the field, provide a new name inline after an additional `:`.
```

Заключение

**До**

```
{


"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"


}
```

**После**

```
{


"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",


"new.name": "stringFieldValue"


}
```

```
parse content, "JSON{STRING:stringField, JSON {STRING:nestedStringField1}:nested}:parsedJson"


| fieldsAdd new.attribute1 = parsedJson[stringField]


| fieldsAdd new.attribute2 = parsedJson[nested][nestedStringField1]


| fieldsRemove parsedJson


// Parses out multiple string fields, including nested one, from raw record data into standalone top-level attributes, via a DPL JSON matcher.
```

Заключение

Вы можете продолжить обработку записи; например, вы можете создать атрибут верхнего уровня из его вложенных полей.

**До**

```
{


"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"


}
```

**После**

```
{


"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",


"new.attribute1": "stringFieldValue",


"new.attribute2": "NestedValue1"


}
```

```
parse content, "JSON:parsedJson"


| fieldsAdd new.field1 = parsedJson[intField],


new.field2 = parsedJson[stringField],


new.field3 = parsedJson[nested][nestedStringField1],


new.field4 = parsedJson[nested][nestedStringField2]


| fieldsRemove parsedJson


// Parses out all JSON fields without listing the attributes, via a DPL JSON matcher.
```

Заключение

Вы можете продолжить обработку записи; например, вы можете создать атрибут верхнего уровня из его вложенных полей.

**До**

```
{


"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"


}
```

**После**

```
{


"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",


"new.field1": "13",


"new.field2": "stringFieldValue",


"new.field3": "NestedValue1",


"new.field4": "NestedValue2"


}
```

```
parse content, """LD '"stringField"' SPACE? ':' SPACE?  DQS:newAttribute"""


// Treats fields as plain text and renames any string that matches as specified.
```

Заключение

**До**

```
{


"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"


}
```

**После**

```
{


"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",


"newAttribute": "stringField"


}
```

```
parse content, "JSON:parsedJson"


| fieldsFlatten parsedJson, prefix: "j"


// Parses out all fields without enumerating them and creates top-level fields from the JSON string without the need to enumerate the field names. It can be applied to multiple JSON objects.
```

Заключение

**До**

```
{


"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"


}
```

**После**

```
{


"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",


"j.stringField": "stringFieldValue",


"j.intField": 13,


"j.nested":"{\"nestedStringField1\":\"NestedValue1\", \"nestedStringField2\":\"NestedValue2\"}"


}
```

### Извлечение атрибутов с различными форматами

Приложения записывают идентификатор пользователя с различными схемами (`user ID=`, `userId=`, `userId:`, `user ID =`). Вы можете извлечь атрибуты с различными форматами с помощью одного выражения шаблона, которое использует модификатор опциональности (`?`) и `Alternative Groups`.

### Шаги

Чтобы извлечь идентификатор пользователя как отдельный атрибут лога, настройте процессор **DQL** на этапе **Processing** со следующим **определением процессора DQL**.

```
parse content, "

LD // Matches any text within a single line

('user'| 'User') // Matches specified literals

SPACE? // Matches optional punctuation

('id'|'Id'|'ID')

SPACE?

PUNCT?

SPACE?

INT:my.user.id"
```

Заключение

С помощью одного определения вы извлекли идентификатор пользователя из различных схем логирования и применили стандартизированный формат, который можно использовать на последующих этапах.

**До**

```
03/22 08:52:51 INFO user ID=1234567 Call = 0319 Result = 0


03/22 08:52:51 INFO UserId = 1234567 Call = 0319 Result = 0


03/22 08:52:51 INFO user id=1234567 Call = 0319 Result = 0


03/22 08:52:51 INFO User ID: 1234567 Call = 0319 Result = 0


03/22 08:52:51 INFO userid: 1234567 Call = 0319 Result = 0
```

**После**

```
"my.user.id":"1234567"
```

### Использование специализированных DPL-сопоставителей

JSON-файл содержит информацию, которую вы хотите извлечь и создать для неё новые выделенные поля на основе формата. Вы можете использовать сопоставители Dynatrace Pattern Language (DPL) для упрощения построения шаблонов.

### Шаги

Чтобы использовать DPL-сопоставители для идентификации и создания новых выделенных полей для метки времени, уровня логирования, IP-адреса, эндпоинта и кода ответа из содержимого JSON-файла, настройте процессор **DQL** на этапе **Processing** со следующим определением.

```
parse content, "ISO8601:timestamp SPACE UPPER:loglevel SPACE IPADDR:ip SPACE DQS:request SPACE INTEGER:code"
```

Заключение

Вы создали новые поля для метки времени, уровня логирования, IP-адреса, эндпоинта и кода ответа на основе формата, используемого в вашем JSON-файле.

**До**

```
{


"content": "2022-05-11T13:23:45Z INFO 192.168.33.1 GET /api/v2/logs/ingest HTTP/1.0 200"


}
```

**После**

```
{


"request": "GET /api/v2/logs/ingest HTTP/1.0",


"code": 200,


"loglevel": "INFO",


"ip": "192.168.33.1",


"timestamp": "2022-05-11T13:23:45.000000000Z",


"content": "2022-05-11T13:23:45Z INFO 192.168.33.1 GET /api/v2/logs/ingest HTTP/1.0 200"


}
```

### Выполнение базовых математических операций с атрибутами

Вы можете извлечь определённые значения из JSON-файла, выполнить вычисления и отформатировать результаты, используя функции и операторы DQL.

### Шаги

Настройте процессор **DQL** на этапе **Processing** со следующим определением.

```
parse content, "LD 'total: ' INT:total '; failed: ' INT:failed" // Parses `total` and `failed` field values.


| fieldsAdd failed.percentage = 100.0 * failed / total // Calculates the failure percentage, formats the result to be a percentage, and stores it in a new attribute (`failed.percentage`).


| fieldsRemove total, failed // Removes temporary fields that are no longer needed from the JSON file.
```

Заключение

Вы рассчитали процент неудач на основе содержимого JSON и создали новое выделенное поле.

**До**

```
{


"content": "Lorem ipsum total: 1000; failed: 255",


}
```

**После**

```
{


"content": "Lorem ipsum total: 1000; failed: 255",


"failed.percentage": 25.5


}
```

### Добавление новых атрибутов

Вы можете добавить атрибуты со статическими или динамическими значениями, используя различные процессоры, с DQL-запросами и без них.

### Шаги

Чтобы добавить атрибуты, настройте один из следующих процессоров на этапе **Processing**.

Add fields

DQL

Этот процессор не использует DQL-запросы. Вы можете использовать его для добавления атрибутов со статическими значениями.

Например, вы можете добавить `company.team.name` со значением `my-team` и `company.branch.name` со значением `New York`. Эти пары ключ-значение будут добавлены ко всем совпавшим записям.

Заключение

Вы добавили новые поля верхнего уровня, хранящие название команды (`company.team.name`) и местоположение филиала (`company.branch.name`) в JSON-файл. Значения остаются статическими до их ручного изменения.

**До**

```
{


"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis."


}
```

**После**

```
{


"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis.",


"company.team.name": "my-team",


"company.branch.name": "New York"


}
```

Вы можете использовать его для добавления атрибутов с динамическими значениями. Используйте определение, содержащее команду `fieldsAdd`, например:

```
fieldsAdd content.length = stringLength(content), content.words = arraySize(splitByPattern(content, "' '"))
```

Заключение

Вы добавили новые поля верхнего уровня, хранящие длину (`content.length`) и количество слов (`content.words`) JSON-поля. Значения адаптируются к содержимому записи.

**До**

```
{


"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis."


}
```

**После**

```
{


"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis.",


"content.length": "62",


"content.words": "9"


}
```

### Удаление атрибутов

Вы можете удалить атрибуты, используя различные процессоры, с DQL-запросами и без них.

### Шаги

Чтобы удалить определённые поля

* Настройте процессор **Remove fields** на этапе **Processing**, указав имена полей. Этот процессор не использует DQL-запросы.
* Настройте процессор **DQL** на этапе **Processing**, введя определение, содержащее команду `fieldsRemove`, например:

  ```
  fieldsRemove redundant.attribute
  ```

Заключение

**До**

```
{


"redundant.attribute": "value",


"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."


}
```

**После**

```
{


"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."


}
```

### Переименование атрибутов

Вы можете переименовать атрибуты, используя различные процессоры, с DQL-запросами и без них.

### Шаги

Чтобы переименовать атрибут совпавшей записи в статическое значение,

* Настройте процессор **Rename fields** на этапе **Processing**, указав имена полей, которые вы хотите переименовать, и новые имена. Этот процессор не использует DQL-запросы.
* Настройте процессор **DQL** на этапе **Processing**, введя определение, содержащее команду `fieldsRename`, например:

  ```
  fieldsRename better_name = field // Renames a field to a static value
  ```

Заключение

**До**

```
{


"content": {"field": "Lorem ipsum"}


}
```

**После**

```
"content": {"better_name": "Lorem ipsum"}
```

### Отбрасывание записей

Вы можете отбрасывать загруженные записи на различных этапах, используя различные процессоры.

### Шаги

Чтобы отбросить загруженную запись

* До её обработки настройте процессор **Drop record** на этапе **Processing**, указав запрос-сопоставитель.
* После её обработки настройте процессор **No storage assignment** на этапе **Storage**, указав запрос-сопоставитель.

Заключение

Совпавшие записи не будут сохранены в Grail.

### Маскирование данных

Вы можете маскировать части атрибута, используя `replacePattern` в сочетании с другими функциями DQL.

### Шаги

В этом сценарии вы хотите замаскировать часть IP-адреса. Настройте процессор **DQL** на этапе **Processing** с одним из следующих определений, в зависимости от части, которую вы хотите замаскировать.

Заданные биты

Шаблон

Повторяющиеся шаблоны

Часть поля

Следующий пример использует функцию `ipMask` для установки последнего октета в значение `0`.

```
fieldsAdd ip = ipMask(ip, 24)
```

Заключение

**До**

```
{


"ip": "192.168.1.12"


}
```

**После**

```
{


"ip": "192.168.1.0"


}
```

Следующий пример использует функцию [`replacePattern`](../../grail/dynatrace-query-language/functions/string-functions.md#replacePattern "Список строковых функций DQL.") вместе с DPL-сопоставителями и модификатором `Lookaround` behind.")(`<<`) для сопоставления определённой части (последнего октета) IP-адреса и установки его в `xxx`.

```
fieldsAdd ip = replacePattern(ip, "<< (INT'.'INT'.'INT'.') INT", "xxx")
```

Заключение

**До**

```
{


"ip": "192.168.1.12"


}
```

**После**

```
{


"ip": "192.168.1.xxx"


}
```

Следующий пример использует функцию [`replacePattern`](../../grail/dynatrace-query-language/functions/string-functions.md#replacePattern "Список строковых функций DQL.") для маскирования всех IP-адресов в одном поле.

```
fieldsAdd content=replacePattern(content, "IPADDR", "xxx.xxx.xxx.xxx")
```

Заключение

**До**

```
{


"content" : "Lorem ipsum client_ip: 192.168.1.12 email: john.doe@dynatrace.com card number: 4012888888881881 server_ip: 215.131.189.194  dolor sit amet"


}
```

**После**

```
{


"content": "Lorem ipsum client_ip: xxx.xxx.xxx.xxx email: john.doe@dynatrace.com card number: 4012888888881881 server_ip: xxx.xxx.xxx.xxx dolor sit amet"


}
```

Следующий пример извлекает имя пользователя из адреса электронной почты и использует функцию [`replaceString`](../../grail/dynatrace-query-language/functions/string-functions.md#replaceString "Список строковых функций DQL.") для замены его статическим значением.

```
parse content, "LD 'email: ' LD:user '@'"


| fieldsAdd content = replaceString(content, user, "xxx")


| fieldsRemove user
```

Заключение

**До**

```
{


"content" : "Lorem ipsum client_ip: 192.168.1.12 email: john.doe@dynatrace.com card number: 4012888888881881 server_ip: 215.131.189.194 dolor sit amet"


}
```

**После**

```
{


"content": "Lorem ipsum client_ip: 192.168.1.12 email: xxx@dynatrace.com card number: 4012888888881881 server_ip: 215.131.189.194 dolor sit amet"


}
```

## Связанные темы

* Настройка конвейера обработки
* Обработка в OpenPipeline
