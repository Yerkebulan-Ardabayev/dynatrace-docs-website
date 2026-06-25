---
title: Примеры обработки журналов (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples
scraped: 2026-05-12T12:10:13.098670
---

# Примеры обработки журналов (Logs Classic)

# Примеры обработки журналов (Logs Classic)

* Руководство
* Чтение: 18 мин
* Обновлено 22 сентября 2025 г.

Log Monitoring Classic

В зависимости от создаваемых правил входящие данные журнала можно настраивать под конкретные потребности. Ниже приведены примеры сценариев обработки данных.

* [Пример 1](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample1 "Примеры сценариев обработки журналов.") — исправление нераспознанной временной метки и loglevel в просмотрщике журналов на основе совпадающего источника журнала.
* [Пример 2](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample2 "Примеры сценариев обработки журналов.") — определение доступного для поиска пользовательского атрибута с использованием извлечённого идентификатора из совпавшей фразы в содержимом журнала.
* [Пример 3](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample3 "Примеры сценариев обработки журналов.") — создание метрики оплачиваемой длительности для сервиса AWS на основе данных журнала.
* [Пример 4](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample4 "Примеры сценариев обработки журналов.") — извлечение конкретных полей из JSON-содержимого.
* [Пример 5](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample5 "Примеры сценариев обработки журналов.") — извлечение атрибутов из разных форматов в рамках одного шаблонного выражения.
* [Пример 6](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample6 "Примеры сценариев обработки журналов.") — несколько команд PARSE в одном правиле обработки.
* [Пример 7](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample7 "Примеры сценариев обработки журналов.") — использование специализированных matchers.
* [Пример 8](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample8 "Примеры сценариев обработки журналов.") — управление любым атрибутом журнала (не только содержимым).
* [Пример 9](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample9 "Примеры сценариев обработки журналов.") — добавление нового атрибута в текущую структуру события журнала.
* [Пример 10](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample10 "Примеры сценариев обработки журналов.") — базовые математические операции над атрибутами.
* [Пример 11](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample11 "Примеры сценариев обработки журналов.") — удаление конкретного атрибута из сообщения журнала.
* [Пример 12](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample12 "Примеры сценариев обработки журналов.") — отбрасывание всего события журнала.
* [Пример 13](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample13 "Примеры сценариев обработки журналов.") — маскирование любого атрибута.
* [Пример 14](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample14 "Примеры сценариев обработки журналов.") — переименование атрибутов.
* [Пример 15](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample15 "Примеры сценариев обработки журналов.") — типы данных входных полей.

### Пример 1: исправление нераспознанной временной метки и loglevel

Можно исправить нераспознанную временную метку и loglevel в просмотрщике журналов на основе совпадающего источника журнала. В этом примере предполагается, что в просмотрщике журналов видна сохранённая запись из приложения `log.source`, указывающего на `/var/log/myapp/application.log.#`.

Замечены две проблемы:

* Журнал содержит нераспознанный формат временной метки, который нужно считать временной меткой события журнала.
* Уровень журнала не обнаружен корректно.

Нужно преобразовать данные журнала: добавить правильные значения в поля временной метки и logLevel, а также добавить атрибут `thread.name` с корректно извлечённым значением.

Чтобы создать правило обработки:

1. Скопируйте запрос просмотрщика журналов в буфер обмена (`log.source="/var/log/myapp/application.log.#"`).
2. Перейдите в **Settings** > **Log Monitoring** > **Processing** и нажмите **Add processing rule**.
3. Введите название правила и скопированный запрос журнала.  
   **Rule name**: `MyApp log processor`  
   **Matcher**: `log.source="/var/log/myapp/application.log.#"`
4. Введите определение правила для извлечения временной метки, имени потока и уровня журнала.  
   **Rule definition**: `PARSE(content, "TIMESTAMP('MMMMM d, yyyy HH:mm:ss'):timestamp ' [' LD:thread.name '] ' UPPER:loglevel")`  
   где:

   * matcher `TIMESTAMP` используется для поиска конкретного формата даты/времени, а совпавшее значение устанавливается как существующий атрибут временной метки журнала.
   * matcher `LD` (Line Data) используется для сопоставления любых символов между литералами `' ['` и `'] '`.
   * литерал `UPPER` используется для сопоставления букв верхнего регистра.
   * Оставшаяся часть содержимого не сопоставляется.
5. Вручную введите следующий фрагмент данных журнала в текстовое поле **Log sample**.

   ```
   {



   "event.type":"LOG",



   "content":"April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",



   "status":"NONE",



   "timestamp":"1650889391528",



   "log.source":"/var/log/myapp/application.log.#",



   "loglevel":"NONE"



   }
   ```
6. Нажмите **Test the rule**.  
   Отображаются обработанные данные журнала. Поля `timestamp` и `loglevel` имеют правильные значения. Дополнительный атрибут `thread.name` также корректно извлечён.

   ```
   {



   "content":"April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",



   "timestamp":"1650794392000",



   "event.type":"LOG",



   "status":"NONE",



   "log.source":"/var/log/myapp/application.log.#",



   "loglevel":"INFO",



   "thread.name":"myPool-thread-1"



   }
   ```
7. Сохраните правило обработки журналов.

По мере поступления новых данных журналов в просмотрщике будут отображаться обработанные данные.

### Пример 2: определение доступного для поиска пользовательского атрибута

Можно определить доступный для поиска пользовательский атрибут с использованием извлечённого идентификатора из совпавшей фразы в содержимом журнала.

В этом примере в файле журнала (ещё не сохранённом в Dynatrace) видна следующая строка журнала, из которой нужно извлечь идентификатор для возможности поиска в просмотрщике журналов:

`2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet`

1. Перейдите в **Settings** > **Log Monitoring** > **Processing** и нажмите **Add processing rule**.
2. Введите название правила и запрос журнала. Для запроса журнала используйте постоянную фразу из содержимого данных журнала (`content="Critical error occurred for product ID"`).  
   **Rule name**: `MyApp product ID with error`  
   **Matcher**: `content="Critical error occurred for product ID"`
3. Введите определение правила для извлечения идентификатора.  
   **Rule definition**: `PARSE(content, "LD 'product ID:' SPACE? INT:my.product.id")`
4. Если указанная запись журнала наблюдается в просмотрщике, нажмите **Download a log sample** для автоматического заполнения текстового поля **Log sample** данными журнала.  
   `2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet`  
   Или введите запись вручную в текстовое поле **Log sample**:

   ```
   {



   "content": "2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet"



   }
   ```
5. Нажмите **Test the rule**.  
   Отображаются обработанные данные журнала, обогащённые извлечённым идентификатором продукта.

   ```
   {



   "content": "2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet",



   "timestamp": "1650961124832",



   "my.product.id": "12345678"



   }
   ```
6. Сохраните правило обработки журналов.
7. Перейдите в **Settings** > **Log Monitoring** > **Custom attributes** и нажмите **Add custom attribute**.
8. Создайте пользовательский атрибут на основе извлечённого идентификатора продукта (`my.product.id`).  
   **Key**: `my.product.id`  
   Подробнее см. в разделе [Пользовательские атрибуты журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-custom-attributes "Узнайте, как создавать и использовать пользовательские атрибуты при приёме данных журналов.").
9. Сохраните пользовательский атрибут.
10. Теперь можно искать и фильтровать данные журнала по атрибуту `my.product.id` в просмотрщике журналов.

### Пример 3: создание метрики оплачиваемой длительности для сервиса AWS

В этом примере нужно отслеживать фактическую оплачиваемую длительность для сервисов AWS. Используется атрибут `cloud.provider` со значением `aws` в данных журнала. В просмотрщике журналов видна запись со следующей строкой:

`REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc Duration: 5033.50 ms Billed Duration: 5034 ms Memory Size: 1024 MB Max Memory Used: 80 MB Init Duration: 488.08 ms`

Кроме того, эта запись содержит атрибут `cloud.provider` со значением `aws`.

1. Перейдите в **Settings** > **Log Monitoring** > **Processing** и нажмите **Add processing rule**.
2. Введите название правила и запрос журнала. Используйте постоянную фразу из содержимого для `cloud.provider="aws"` и `content="Billed Duration"`.  
   **Rule name**: `AWS services - billed duration`  
   **Matcher**: `cloud.provider="aws" and content="Billed Duration"`
3. Введите определение правила для извлечения значения оплачиваемой длительности.  
   **Rule definition**: `PARSE(content, "LD 'Billed Duration:' SPACE? INT:aws.billed.duration")`
4. Нажмите **Download a log sample** для автоматического заполнения текстового поля **Log sample** или введите следующий фрагмент данных журнала вручную:

   ```
   {



   "event.type": "LOG",



   "content": "REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc\tDuration: 5033.50 ms\tBilled Duration: 5034 ms\tMemory Size: 1024 MB\tMax Memory Used: 80 MB\t\n",



   "status": "INFO",



   "timestamp": "1651062483672",



   "cloud.provider": "aws",



   "cloud.account.id": "999999999999",



   "cloud.region": "eu-central-1",



   "aws.log_group": "/aws/lambda/aws-dev",



   "aws.log_stream": "2022/04/27/[$LATEST]0d00000daa0c0c0a0a0e0ea0eccc000f",



   "aws.region": "central-1",



   "aws.account.id": "999999999999",



   "aws.service": "lambda",



   "aws.resource.id": "aws-dev",



   "aws.arn": "arn:aws:lambda:central-1:999999999999:function:aws-dev",



   "cloud.log_forwarder": "999999999999:central-1:dynatrace-aws-logs",



   "loglevel": "INFO"



   }
   ```
5. Нажмите **Test the rule**.  
   Отображаются обработанные данные журнала, обогащённые новым атрибутом `aws.billed.duration`.

   ```
   {



   "event.type": "LOG",



   "content": "REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc\tDuration: 5033.50 ms\tBilled Duration: 5034 ms\tMemory Size: 1024 MB\tMax Memory Used: 80 MB\t\n",



   "status": "INFO",



   "timestamp": "1651062483672",



   "cloud.provider": "aws",



   "cloud.account.id": "999999999999",



   "cloud.region": "eu-central-1",



   "aws.log_group": "/aws/lambda/aws-dev",



   "aws.log_stream": "2022/04/27/[$LATEST]0d00000daa0c0c0a0a0e0ea0eccc000f",



   "aws.region": "central-1",



   "aws.account.id": "999999999999",



   "aws.service": "lambda",



   "aws.resource.id": "aws-dev",



   "aws.arn": "arn:aws:lambda:central-1:999999999999:function:aws-dev",



   "cloud.log_forwarder": "999999999999:central-1:dynatrace-aws-logs",



   "loglevel": "INFO",



   "aws.billed.duration": "5034"



   }
   ```
6. Сохраните правило обработки журналов.
7. Перейдите в **Settings** > **Log Monitoring** > **Metrics extraction** и нажмите **Add log metric**.
8. Создайте метрику журнала на основе извлечённого идентификатора продукта (`aws.billed.duration`).  
   **Key**: `log.aws.billed.duration`  
   **Query**: `cloud.provider="aws" and content="Billed Duration"`  
   **Measure**: `Attribute value`  
   **Attribute**: `aws.billed.duration`  
   Подробнее см. в разделе [Метрики журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Узнайте, как создавать и использовать метрики журналов Dynatrace для анализа данных журналов.").
9. Сохраните метрику журнала.
10. Метрика `log.aws.billed.duration` появится в Data Explorer, и её можно использовать в Dynatrace как любую другую метрику: добавлять на дашборды, включать в анализ и создавать оповещения.

    Доступность метрики журнала в Dynatrace

    Созданная метрика журнала доступна только при поступлении новых данных журналов, соответствующих запросу журнала, заданному при создании метрики. Перед использованием метрики журнала в других областях Dynatrace убедитесь, что новые данные журналов были приняты.

### Пример 4: извлечение конкретных полей из JSON-содержимого

В этом примере видна строка журнала со следующей JSON-структурой:

`{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }`

Пример журнала выглядит следующим образом:

```
{



"content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }"



}
```

* Разбор поля из JSON в плоском режиме.  
  Можно использовать JSON matcher и настроить его для извлечения нужных полей как атрибутов верхнего уровня журнала. В плоском режиме matcher создаёт атрибуты автоматически и именует их точно так же, как соответствующие поля JSON.

  Затем можно использовать команду `FIELDS_RENAME` для установки удобных имён.

  Определение правила обработки:

  ```
  PARSE(content, "JSON{STRING:stringField}(flat=true)")



  | FIELDS_RENAME(better.name: stringField)
  ```

  Результат после преобразования:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "better.name": "someValue"



  }
  ```
* Разбор вложенного поля из JSON.  
  Можно также анализировать несколько полей (включая вложенные) с помощью JSON matcher без плоского режима. В результате получается `VariantObject`, который можно обрабатывать далее: например, создать атрибут верхнего уровня из его внутренних полей.

  Определение правила обработки:

  ```
  PARSE(content, "
  JSON{
  STRING:stringField,
  JSON {STRING:nestedStringField1}:nested
  }:parsedJson")



  | FIELDS_ADD(top_level.attribute1: parsedJson["stringField"], top_level.attribute2: parsedJson["nested"]["nestedStringField1"])



  | FIELDS_REMOVE(parsedJson)
  ```

  Результат после преобразования:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "top_level.attribute1": "someValue",



  "top_level.attribute2": "someNestedValue1"



  }
  ```
* Разбор всех полей из JSON в режиме автоматического обнаружения.  
  Иногда нужны все поля JSON. Нет необходимости перечислять все атрибуты: вместо этого можно использовать JSON matcher в режиме автоматического обнаружения. В результате получается `VARIANT_OBJECT`, который можно обрабатывать далее.

  Определение правила обработки:

  ```
  PARSE(content,"JSON:parsedJson")



  | FIELDS_ADD(f1: parsedJson["intField"],



  f2:parsedJson["stringField"],



  f3:parsedJson["nested"]["nestedStringField1"],



  f4:parsedJson["nested"]["nestedStringField2"])



  | FIELDS_REMOVE(parsedJson)
  ```

  Результат после преобразования:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "f1": "13",



  "f2": "someValue",



  "f3": "someNestedValue1",



  "f4": "someNestedValue2"



  }
  ```
* Разбор любого поля из JSON, обращаясь с содержимым как с обычным текстом.  
  При таком подходе атрибут можно именовать как угодно, но правило обработки будет более сложным.

  Определение правила обработки:

  ```
  PARSE(content, "LD '"stringField"' SPACE? ':' SPACE?  DQS:newAttribute ")
  ```

  Результат после преобразования:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "newAttribute": "someValue"



  }
  ```

### Пример 5: извлечение атрибутов из разных форматов

Можно извлекать атрибуты из разных форматов в рамках одного шаблонного выражения.

В этом примере одно или несколько приложений записывают идентификатор пользователя в журнал, который нужно извлечь как отдельный атрибут. Формат журнала непоследователен, так как используются разные схемы записи идентификатора:

* `user ID=`
* `userId=`
* `userId:`
* `user ID =`

С помощью необязательного модификатора (`?`) и альтернативных групп можно охватить все подобные случаи одним шаблонным выражением:

```
PARSE(content, "
LD //matches any text within a single line
('user'| 'User') //user or User literal
SPACE? //optional space
('id'|'Id'|'ID') //matches any of these
SPACE? //optional space
PUNCT? //optional punctuation
SPACE? //optional space
INT:my.user.id
")
```

Используя такое правило, можно извлекать идентификатор пользователя из многих разных нотаций. Например:

`03/22 08:52:51 INFO user ID=1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO UserId = 1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO user id=1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO user ID:1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO User ID: 1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO userid: 1234567 Call = 0319 Result = 0`

### Пример 6: несколько команд PARSE в одном правиле обработки

Для обработки различных форматов или дополнительного разбора уже извлечённых атрибутов можно использовать несколько команд `PARSE`, соединённых символами `|`.

Например, для следующего журнала:

```
{



"content": "{"intField": 13, "message": "Error occurred for user 12345: Missing permissions", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }"



}
```

Сначала можно извлечь поле message, идентификатор пользователя и сообщение об ошибке:

```
PARSE(content, "JSON{STRING:message}(flat=true)") | PARSE(message, "LD 'user ' INT:user.id ': ' LD:error.message")
```

Результат:

```
{



"content": "{"intField": 13, "message": "Error occurred for user 12345: Missing permissions", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



"message": "Error occurred for user 12345: Missing permissions",



"user.id": "12345",



"error.message": "Missing permissions"



}
```

### Пример 7: использование специализированных matchers

Для упрощения построения шаблонов доступен полный список matchers.

Например, можно разобрать следующее событие журнала:

```
{



"content":"2022-05-11T13:23:45Z INFO 192.168.33.1 "GET /api/v2/logs/ingest HTTP/1.0" 200"



}
```

используя специализированные matchers:

```
PARSE(content, "ISO8601:timestamp SPACE UPPER:loglevel SPACE IPADDR:ip SPACE DQS:request SPACE INTEGER:code")
```

результат:

```
{



"content": "2022-05-11T13:23:45Z INFO 192.168.33.1 "GET /api/v2/logs/ingest HTTP/1.0" 200",



"timestamp": "1652275425000",



"loglevel": "INFO",



"ip": "192.168.33.1",



"request": "GET /api/v2/logs/ingest HTTP/1.0",



"code": "200"



}
```

### Пример 8: управление любым атрибутом журнала (не только содержимым)

Если не указано иное, правило обработки работает только с полем содержимого, доступным только для чтения. Для работы с другими атрибутами события журнала необходима команда `USING`.

Например, следующее правило объявляет два входных атрибута: записываемый `status` и читаемый `content`. Затем оно проверяет, равен ли `status` значению `WARN` и содержит ли `content` текст `error`. Если оба условия выполнены, правило перезаписывает `status` значением `ERROR`.

Определение правила обработки:

```
USING(INOUT status:STRING, content)



| FIELDS_ADD(status:IF_THEN(status == 'WARN' AND content CONTAINS('error'), "ERROR"))
```

Пример данных журнала:

```
{



"log.source": "using",



"timestamp": "1656011002196",



"status": "WARN",



"content":"Some error message"



}
```

Результат после преобразования:

```
{



"log.source": "using",



"timestamp": "1656011002196",



"status": "ERROR",



"content":"Some error message"



}
```

### Пример 9: добавление нового атрибута в структуру события журнала

Команду FIELDS\_ADD можно использовать для введения дополнительных атрибутов верхнего уровня журнала. Следующий скрипт добавляет два атрибута: первый хранит длину, второй — количество слов в поле `content`.

Определение правила обработки:

```
FIELDS_ADD(content.length: STRLEN(content), content.words: ARRAY_COUNT(SPLIT(content,"' '")))
```

Пример данных журнала:

```
{



"log.source": "new_attributes",



"timestamp": "1656010654603",



"content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis."



}
```

Результат после преобразования:

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis.",



"timestamp": "1656010654603",



"log.source": "new_attribute",



"content.length": "62",



"content.words": "9"



}
```

### Пример 10: базовые математические операции над атрибутами

Имея все доступные функции и операторы, легко выполнять вычисления.

В следующем примере извлекаются значения `total` и `failed`, вычисляется процент неудач и конкатенируется со знаком процента. Результат сохраняется в новом атрибуте `failed.percentage`, а временные поля удаляются.

Определение правила обработки:

```
PARSE(content,"LD 'total: ' INT:total '; failed: ' INT:failed")



| FIELDS_ADD(failed.percentage: 100.0 * failed / total + '%')



| FIELDS_REMOVE(total, failed)
```

Пример данных журнала:

```
{



"timestamp": "1656011338522",



"content":"Lorem ipsum total: 1000; failed: 250"



}
```

Результат после преобразования:

```
{



"content": "Lorem ipsum total: 1000; failed: 250",



"timestamp": "1656011338522",



"failed.percentage": "25.0%"



}
```

### Пример 11: удаление конкретного атрибута из сообщения журнала

Для удаления атрибута события, являющегося частью исходной записи, его необходимо сначала объявить как записываемый (опция `INOUT`) входной поле с помощью команды `USING`, а затем явно удалить с помощью команды `FIELDS_REMOVE`, чтобы он отсутствовал в выходных данных преобразования.

В следующем примере `redundant.attribute` объявляется как обязательный записываемый атрибут типа `STRING`, после чего удаляется.

Определение правила обработки:

```
USING(INOUT redundant.attribute:STRING)



| FIELDS_REMOVE(redundant.attribute)
```

Пример данных журнала:

```
{



"redundant.attribute": "value",



"timestamp": "1656011525708",



"content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."



}
```

Результат после преобразования:

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus.",



"timestamp": "1656011525708"



}
```

Можно использовать символ `?` для обозначения атрибута как необязательного, чтобы преобразование выполнялось и успешно завершалось, даже если атрибут отсутствует в исходном событии.

В этом случае определение будет выглядеть так:

```
USING(INOUT redundant.attribute:STRING?)



| FIELDS_REMOVE(redundant.attribute)
```

### Пример 12: отбрасывание всего события журнала

Всё событие журнала можно отбросить с помощью команды `FILTER_OUT`. Событие отбрасывается, когда выполняется условие, переданное в качестве параметра команды.

* Отбрасывание на основе predmatcher  
  В большинстве случаев достаточно отбросить каждое событие, прошедшее предварительное сопоставление.

  Например, для отбрасывания всех событий `DEBUG` и `TRACE` можно задать запрос matcher для любого из этих статусов, а затем использовать команду `FILTER_OUT` для перехвата всего остального.

  Matcher:

  ```
  status="DEBUG" or status="TRACE"
  ```

  Определение правила обработки:

  ```
  FILTER_OUT(true)
  ```

  Пример данных журнала:

  ```
  {



  "status": "DEBUG",



  "content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."



  }
  ```

  Таким образом, все журналы со статусом `DEBUG` или `TRACE` отбрасываются.
* Расширенное условие отбрасывания  
  Также возможна дополнительная логика, при которой не все предварительно совпавшие события отбрасываются.

  В следующем примере отбрасываются входящие события, где время выполнения менее 100 мс.

  Пример данных журнала:

  ```
  {



  "content":"2022-06-23 06:52:35.280 UTC INFO My monitored service call took 97ms"



  }
  ```

  Определение правила обработки:

  ```
  PARSE(content, "LD 'My monitored service call took ' INT:took 'ms'")



  | FILTER_OUT(took < 100)



  | FIELDS_REMOVE(took)
  ```

### Пример 13: маскирование любого атрибута

Если требуется изменить содержимое или любой другой атрибут, его необходимо объявить как `INOUT` (записываемый) с помощью команды `USING`. Функция `REPLACE_PATTERN` — мощный инструмент для маскирования части атрибута.

* Маскирование IP-адреса: последний октет заменяется значением 0.

  Определение правила обработки:

  ```
  USING(INOUT ip)



  | FIELDS_ADD(ip: IPADDR(ip) & 0xFFFFFF00l)
  ```

  Пример данных журнала:

  ```
  {



  "content":"Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.12"



  }
  ```

  Результат после преобразования:

  ```
  {



  "content": "Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.0"



  }
  ```
* Маскирование IP-адреса: последний октет заменяется значением `xxx`.

  Определение правила обработки:

  ```
  USING(INOUT ip)



  | FIELDS_ADD(ip: REPLACE_PATTERN(ip, "(INT'.'INT'.'INT'.'):not_masked INT", "${not_masked}xxx"))
  ```

  Пример данных журнала:

  ```
  {



  "content":"Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.12"



  }
  ```

  Результат после преобразования:

  ```
  {



  "content": "Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.xxx"



  }
  ```
* Маскирование всего адреса электронной почты с использованием `sha1`:

  Определение правила обработки:

  ```
  USING(INOUT email)



  | FIELDS_ADD(email: REPLACE_PATTERN(email, "LD:email_to_be_masked", "${email_to_be_masked|sha1}"))
  ```

  Пример данных журнала:

  ```
  {



  "content":"Lorem ipsum",



  "timestamp": "1656009924312",



  "email": "john.doe@dynatrace.com"



  }
  ```

  Результат после преобразования:

  ```
  {



  "content": "Lorem ipsum",



  "timestamp": "1656009924312",



  "email": "9940e79e41cbf7cc452b137d49fab61e386c602d"



  }
  ```
* Маскирование IP-адреса, адреса электронной почты и номера кредитной карты из поля содержимого:

  Определение правила обработки:

  ```
  USING(INOUT content)



  | FIELDS_ADD(content: REPLACE_PATTERN(content, "



  (LD 'ip: '):p1                                   // Lorem ipsum ip:



  (INT'.'INT'.'INT'.'):ip_not_masked               // 192.168.0.



  INT                                              // 12



  ' email: ':p2                                    //  email:



  LD:email_name '@' LD:email_domain                // john.doe@dynatrace.com



  ' card number: ': p3                             //  card number:



  CREDITCARD:card                                  // 4012888888881881



  ", "${p1}${ip_not_masked}xxx${p2}${email_name|md5}@${email_domain}${p3}${card|sha1}"))
  ```

  Пример данных журнала:

  ```
  {



  "timestamp": "1656010291511",



  "content": "Lorem ipsum ip: 192.168.0.12 email: john.doe@dynatrace.com card number: 4012888888881881 dolor sit amet"



  }
  ```

  Результат после преобразования:

  ```
  {



  "content": "Lorem ipsum ip: 192.168.0.xxx email: abba0b6ff456806bab66baed93e6d9c4@dynatrace.com card number: 62163a017b168ad4a229c64ae1bed6ffd5e8fb2d dolor sit amet",



  "timestamp": "1656010291511"



  }
  ```

### Пример 14: переименование атрибутов

С помощью команды `FIELDS_RENAME` можно переименовывать атрибуты, являвшиеся частью исходного события журнала, а также атрибуты, созданные внутри процессора. При изменении любого атрибута из исходного события его необходимо объявить как `INOUT` (записываемый).

В следующем примере переименовывается существующий атрибут, а также анализируется поле из JSON в плоском режиме, после чего автоматически созданный новый атрибут переименовывается.

Определение правила обработки:

```
USING(INOUT to_be_renamed, content)



| FIELDS_RENAME(better_name: to_be_renamed)



| PARSE(content,"JSON{STRING:json_field_to_be_renamed}(flat=true)")



| FIELDS_RENAME(another_better_name: json_field_to_be_renamed)
```

Пример данных журнала:

```
{



"timestamp": "1656061626073",



"content":"{"json_field_to_be_renamed": "dolor sit amet", "field2": "consectetur adipiscing elit"}",



"to_be_renamed": "Lorem ipsum"



}
```

Результат после преобразования:

```
{



"content": "{"json_field_to_be_renamed": "dolor sit amet", "field2": "consectetur adipiscing elit"}",



"timestamp": "1656061626073",



"better_name": "Lorem ipsum",



"another_better_name": "dolor sit amet"



}
```

### Пример 15: типы данных входных полей

Скрипт в определении процессора работает со строго типизированными данными: функции и операторы принимают только объявленные типы данных. Тип назначается всем входным полям, определённым в команде `USING`, а также переменным, создаваемым при разборе или использовании функций приведения типов.

Определение правила обработки:

```
USING(number:INTEGER, avg:DOUBLE, addr:IPADDR, arr:INTEGER[],bool:BOOLEAN, ts:TIMESTAMP)



| FIELDS_ADD(multi:number*10)



| FIELDS_ADD(avgPlus1:avg+1)



| FIELDS_ADD(isIP: IS_IPV6(addr))



| FIELDS_ADD(arrAvg: ARRAY_AVG(arr))



| FIELDS_ADD(negation: NOT(bool))



| FIELDS_ADD(tsAddYear: TIME_ADD_YEAR(ts,1))
```

Пример данных журнала:

```
{



"content":"Lorem ipsum",



"number":"5",



"avg":"123.5",



"addr":"2a00:1450:4010:c05::69",



"arr": ["1","2"],



"bool":"false",



"ts":"1984-11-30 22:19:59.789 +0000"



}
```

Результат после преобразования:

```
{



"content": "Lorem ipsum",



"number": "5",



"avg": "123.5",



"addr": "2a00:1450:4010:c05::69",



"arr": [



"1",



"2"



],



"bool": "false",



"ts": "1984-11-30 22:19:59.789 +0000",



"tsAddYear": "1985-11-30T22:19:59.789000000 +0000",



"negation": "true",



"arrAvg": "1.5",



"isIP": "true",



"avgPlus1": "124.5",



"multi": "50"



}
```