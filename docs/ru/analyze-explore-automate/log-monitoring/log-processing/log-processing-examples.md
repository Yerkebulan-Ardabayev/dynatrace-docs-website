---
title: Примеры обработки логов (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples
scraped: 2026-03-03T21:30:43.699782
---

Log Monitoring Classic

В зависимости от создаваемых вами правил вы можете настроить входящие лог-данные в соответствии с вашими потребностями. Ниже приведены примеры сценариев обработки данных.

* [Пример 1](log-processing-examples.md#lpexample1 "Примеры сценариев обработки логов.") -- Исправление нераспознанной метки времени и уровня логирования, отображаемых в просмотрщике логов, на основе сопоставленного источника лога.
* [Пример 2](log-processing-examples.md#lpexample2 "Примеры сценариев обработки логов.") -- Определение доступного для поиска пользовательского атрибута с использованием извлеченного идентификатора из сопоставленной фразы в содержимом лога.
* [Пример 3](log-processing-examples.md#lpexample3 "Примеры сценариев обработки логов.") -- Создание метрики тарифицированной длительности для сервиса AWS с использованием лог-данных.
* [Пример 4](log-processing-examples.md#lpexample4 "Примеры сценариев обработки логов.") -- Извлечение определенных полей из содержимого JSON.
* [Пример 5](log-processing-examples.md#lpexample5 "Примеры сценариев обработки логов.") -- Извлечение атрибутов из различных форматов в рамках одного выражения шаблона.
* [Пример 6](log-processing-examples.md#lpexample6 "Примеры сценариев обработки логов.") -- Несколько команд PARSE в одном правиле обработки.
* [Пример 7](log-processing-examples.md#lpexample7 "Примеры сценариев обработки логов.") -- Использование специализированных сопоставителей.
* [Пример 8](log-processing-examples.md#lpexample8 "Примеры сценариев обработки логов.") -- Манипулирование любым атрибутом лога (не только содержимым).
* [Пример 9](log-processing-examples.md#lpexample9 "Примеры сценариев обработки логов.") -- Добавление нового атрибута в текущую структуру лог-события.
* [Пример 10](log-processing-examples.md#lpexample10 "Примеры сценариев обработки логов.") -- Базовая математика с атрибутами.
* [Пример 11](log-processing-examples.md#lpexample11 "Примеры сценариев обработки логов.") -- Удаление определенного атрибута из сообщения лога.
* [Пример 12](log-processing-examples.md#lpexample12 "Примеры сценариев обработки логов.") -- Удаление всего лог-события.
* [Пример 13](log-processing-examples.md#lpexample13 "Примеры сценариев обработки логов.") -- Маскировка любого атрибута.
* [Пример 14](log-processing-examples.md#lpexample14 "Примеры сценариев обработки логов.") -- Переименование атрибутов.
* [Пример 15](log-processing-examples.md#lpexample15 "Примеры сценариев обработки логов.") -- Типы данных входных полей.

### Пример 1: Исправление нераспознанной метки времени и уровня логирования

Вы можете исправить нераспознанные метку времени и уровень логирования, отображаемые в просмотрщике логов, на основе сопоставленного источника лога.
Для этого примера предположим, что вы видите сохраненное событие в просмотрщике логов из приложения `log.source`, установленного в `/var/log/myapp/application.log.#`

Вы замечаете несколько вещей, которые хотите исправить:

* Лог содержит нераспознанный формат метки времени, который вы хотите использовать в качестве метки времени лог-события.
* Нет правильно определенного уровня логирования (logLevel).

Вы хотите преобразовать лог-данные, чтобы они содержали правильные значения в полях timestamp и logLevel, а также добавить новый атрибут `thread.name`, содержащий правильно извлеченное значение.

Чтобы создать правило обработки:

1. Скопируйте запрос просмотрщика логов в буфер обмена (`log.source="/var/log/myapp/application.log.#"`).
2. Перейдите в **Settings** > **Log Monitoring** > **Processing** и выберите **Add processing rule**.
3. Введите имя правила и скопированный запрос лога из буфера обмена.
   **Rule name**: `MyApp log processor`
   **Matcher**: `log.source="/var/log/myapp/application.log.#"`
4. Введите определение правила для извлечения метки времени, имени потока и уровня логирования.
   **Rule definition**: `PARSE(content, "TIMESTAMP('MMMMM d, yyyy HH:mm:ss'):timestamp ' [' LD:thread.name '] ' UPPER:loglevel")`
   где:

   * Сопоставитель `TIMESTAMP` используется для поиска определенного формата даты и времени, и сопоставленное значение устанавливается как существующий атрибут timestamp лога.
   * Сопоставитель `LD` (Line Data) используется для сопоставления любых символов между литералами `' ['` и `'] '`.
   * Литерал `UPPER` используется для сопоставления заглавных букв.
   * Оставшаяся часть содержимого не сопоставляется.
5. Введите следующий фрагмент лог-данных вручную в текстовое поле **Log sample**.

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
6. Выберите **Test the rule**.
   Отображаются обработанные лог-данные. Поля `timestamp` и `loglevel` имеют правильные значения. Дополнительный атрибут `thread.name` также правильно извлечен.

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
7. Сохраните правило обработки логов.

По мере приема новых лог-данных вы сможете видеть обработанные лог-данные в просмотрщике логов.

### Пример 2: Определение доступного для поиска пользовательского атрибута

Вы можете определить доступный для поиска пользовательский атрибут, используя извлеченный идентификатор из сопоставленной фразы в содержимом лога.

В этом примере вы видите следующую строку лога в лог-файле (еще не сохраненную в Dynatrace) и хотите извлечь идентификатор из этой строки лога, чтобы сделать его доступным для поиска в просмотрщике логов.

`2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet`

1. Перейдите в **Settings** > **Log Monitoring** > **Processing** и выберите **Add processing rule**.
2. Введите имя правила и запрос лога. Для запроса лога используйте постоянную фразу из содержимого лог-данных (`content="Critical error occurred for product ID"`)
   **Rule name**: `MyApp product ID with error`
   **Matcher**: `content="Critical error occurred for product ID"`
3. Введите определение правила для извлечения идентификатора.
   **Rule definition**: `PARSE(content, "LD 'product ID:' SPACE? INT:my.product.id")`
4. Если вы наблюдали следующую запись лога в просмотрщике логов, вы можете выбрать **Download a log sample** и автоматически заполнить текстовое поле **Log sample** вашими лог-данными.
   `2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet`
   Или вы можете вставить наблюдаемую запись лога как содержимое записи лога вручную в текстовое поле **Log sample**:

   ```
   {


   "content": "2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet"


   }
   ```
5. Выберите **Test the rule**.
   Отображаются обработанные лог-данные. Обработанные лог-данные обогащены извлеченным идентификатором продукта.

   ```
   {


   "content": "2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet",


   "timestamp": "1650961124832",


   "my.product.id": "12345678"


   }
   ```
6. Сохраните правило обработки логов.
7. Перейдите в **Settings** > **Log Monitoring** > **Custom attributes** и выберите **Add custom attribute**.
8. Создайте пользовательский атрибут на основе извлеченного идентификатора продукта (`my.product.id`).
   **Key**: `my.product.id`
   Подробнее см. Пользовательские атрибуты логов (Logs Classic).
9. Сохраните пользовательский атрибут.
10. Теперь вы можете искать и фильтровать лог-данные по атрибуту `my.product.id` в просмотрщике логов.

### Пример 3: Создание метрики тарифицированной длительности для сервиса AWS с использованием лог-данных

В этом примере вы хотите отслеживать фактическую тарифицированную длительность ваших сервисов AWS. Вы хотите использовать атрибут `cloud.provider` со значением `aws` в ваших лог-данных. В просмотрщике логов вы видите запись лога, содержащую следующую строку:

`REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc Duration: 5033.50 ms Billed Duration: 5034 ms Memory Size: 1024 MB Max Memory Used: 80 MB Init Duration: 488.08 ms`

Кроме того, эта запись лога содержит атрибут `cloud.provider` со значением `aws`.

1. Перейдите в **Settings** > **Log Monitoring** > **Processing** и выберите **Add processing rule**.
2. Введите имя правила и запрос лога. Для запроса лога используйте постоянную фразу из содержимого лог-данных для `cloud.provider="aws"` и `content="Billed Duration"`
   **Rule name**: `AWS services - billed duration`
   **Matcher**: `cloud.provider="aws" and content="Billed Duration"`
3. Введите определение правила для извлечения значения тарифицированной длительности.
   **Rule definition**: `PARSE(content, "LD 'Billed Duration:' SPACE? INT:aws.billed.duration")`
4. Если вы наблюдали следующую запись лога в просмотрщике логов, вы можете выбрать **Download a log sample** и автоматически заполнить текстовое поле **Log sample** вашими лог-данными.
   `REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc Duration: 5033.50 ms Billed Duration: 5034 ms Memory Size: 1024 MB Max Memory Used: 80 MB Init Duration: 488.08 ms`
   Или вы можете ввести следующий фрагмент лог-данных (содержащий другие дополнительные атрибуты) вручную в текстовое поле **Log sample**:

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
5. Выберите **Test the rule**.
   Отображаются обработанные лог-данные. Обработанные лог-данные обогащены новым атрибутом `aws.billed.duration`.

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
6. Сохраните правило обработки логов.
7. Перейдите в **Settings** > **Log Monitoring** > **Metrics extraction** и выберите **Add log metric**.
8. Создайте метрику лога на основе извлеченного идентификатора продукта (`aws.billed.duration`).
   **Key**: `log.aws.billed.duration`
   **Query**: `cloud.provider="aws" and content="Billed Duration"`
   **Measure**: `Attribute value`
   **Attribute**: `aws.billed.duration`
   Подробнее см. Метрики логов (Logs Classic).
9. Сохраните метрику лога.
10. Метрика `log.aws.billed.duration` видна в Data Explorer, и вы можете использовать ее в Dynatrace как любую другую метрику. Вы можете добавить ее на панель мониторинга, включить в анализ и даже использовать для создания оповещений.

    Доступность метрики лога в Dynatrace

    Созданная метрика лога доступна только при приеме новых лог-данных, соответствующих запросу лога, определенному при создании метрики лога. Убедитесь, что новые лог-данные были приняты, прежде чем использовать метрику лога в других областях Dynatrace.

### Пример 4: Извлечение определенных полей из содержимого JSON

В этом примере вы видите строку лога со следующей структурой JSON:

`{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }`

Пример лога будет выглядеть так:

```
{


"content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }"


}
```

* Извлечение поля из JSON в плоском режиме.
  Вы можете использовать сопоставитель JSON и настроить его для извлечения нужных полей в качестве атрибутов верхнего уровня лога. Сопоставитель в плоском режиме создает атрибуты автоматически и называет их точно так же, как соответствующие имена полей JSON.

  Затем вы можете использовать команду `FIELDS_RENAME`, чтобы установить подходящие имена.

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
* Извлечение вложенного поля из JSON.
  Вы также можете извлечь больше полей (включая вложенные) с помощью сопоставителя JSON без плоского режима. В результате вы получите `VariantObject`, который можно обработать дальше. Например, вы можете создать атрибут верхнего уровня из его внутренних полей.

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
* Извлечение всех полей из JSON в режиме автообнаружения.
  Иногда вас интересуют все поля JSON. Вам не нужно перечислять все атрибуты. Вместо этого сопоставитель JSON можно использовать в режиме автообнаружения. В результате вы получите `VARIANT_OBJECT`, который можно обработать дальше. Например, вы можете создать атрибут верхнего уровня из его внутренних полей.

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
* Извлечение любого поля из JSON, обрабатывая содержимое как простой текст.
  При таком подходе вы можете назвать атрибут как угодно, но правило обработки будет более сложным.

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

### Пример 5: Извлечение атрибутов из различных форматов

Вы можете извлечь атрибуты из различных форматов в рамках одного выражения шаблона.

В этом примере одно или несколько приложений логируют идентификатор пользователя, который вы хотите извлечь как отдельный атрибут лога. Формат лога непоследователен, поскольку включает различные схемы записи ID пользователя:

* `user ID=`
* `userId=`
* `userId:`
* `user ID =`

С необязательным модификатором (вопросительный знак `?`) и `Alternative Groups` вы можете охватить все такие случаи одним выражением шаблона:

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

Используя такое правило, вы можете извлечь идентификатор пользователя из множества различных записей. Например:

`03/22 08:52:51 INFO user ID=1234567 Call = 0319 Result = 0`
`03/22 08:52:51 INFO UserId = 1234567 Call = 0319 Result = 0`
`03/22 08:52:51 INFO user id=1234567 Call = 0319 Result = 0`
`03/22 08:52:51 INFO user ID:1234567 Call = 0319 Result = 0`
`03/22 08:52:51 INFO User ID: 1234567 Call = 0319 Result = 0`
`03/22 08:52:51 INFO userid: 1234567 Call = 0319 Result = 0`

### Пример 6: Несколько команд PARSE в одном правиле обработки

Вы можете обрабатывать различные форматы или выполнять дополнительный парсинг уже извлеченных атрибутов с помощью нескольких команд `PARSE`, соединенных конвейерами (`|`).

Например, для следующего лога:

```
{


"content": "{"intField": 13, "message": "Error occurred for user 12345: Missing permissions", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }"


}
```

Сначала вы можете извлечь поле message, ID пользователя и сообщение об ошибке.

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

### Пример 7: Использование специализированных сопоставителей

Мы предоставляем полный список сопоставителей, упрощающих построение шаблонов.

Например, вы можете обработать следующий пример лог-события:

```
{


"content":"2022-05-11T13:23:45Z INFO 192.168.33.1 "GET /api/v2/logs/ingest HTTP/1.0" 200"


}
```

используя специализированные сопоставители:

```
PARSE(content, "ISO8601:timestamp SPACE UPPER:loglevel SPACE IPADDR:ip SPACE DQS:request SPACE INTEGER:code")
```

и результат:

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

### Пример 8: Манипулирование любым атрибутом лога (не только содержимым)

Если не указано иное, правило обработки работает только с полем содержимого, доступным только для чтения. Чтобы оно работало с другими атрибутами лог-события, необходимо использовать команду `USING`.

Например, следующее правило объявляет два входных атрибута: записываемый status и содержимое, доступное только для чтения.
Затем оно проверяет, является ли status `WARN` и содержит ли содержимое текст `error`. Если оба условия верны, правило перезаписывает `status` значением `ERROR`.

Определение правила обработки:

```
USING(INOUT status:STRING, content)


| FIELDS_ADD(status:IF_THEN(status == 'WARN' AND content CONTAINS('error'), "ERROR"))
```

Пример лог-данных:

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

### Пример 9: Добавление нового атрибута в текущую структуру лог-события

Команда FIELDS\_ADD может использоваться для добавления дополнительных атрибутов верхнего уровня лога.
Следующий скрипт добавляет два атрибута: первый сохраняет длину, а второй -- количество слов в поле содержимого.

Определение правила обработки:

```
FIELDS_ADD(content.length: STRLEN(content), content.words: ARRAY_COUNT(SPLIT(content,"' '")))
```

Пример лог-данных:

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

### Пример 10: Базовая математика с атрибутами

С помощью всех доступных функций и операторов легко выполнять вычисления.

В следующем примере мы извлекаем значения `total` и `failed`, вычисляем процент неудачных, конкатенируем значение со знаком процента и сохраняем его в новом атрибуте `failed.percentage`, затем удаляем временные поля.

Определение правила обработки:

```
PARSE(content,"LD 'total: ' INT:total '; failed: ' INT:failed")


| FIELDS_ADD(failed.percentage: 100.0 * failed / total + '%')


| FIELDS_REMOVE(total, failed)
```

Пример лог-данных:

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

### Пример 11: Удаление определенного атрибута из сообщения лога

Чтобы удалить атрибут события, являющийся частью исходной записи, сначала нужно объявить его как записываемый (опция `INOUT`) входное поле с помощью команды `USING`, а затем явно удалить его командой `FIELDS_REMOVE`, чтобы он не присутствовал в выходных данных преобразования.

В следующем примере мы объявляем `redundant.attribute` как обязательный записываемый атрибут типа `STRING`, а затем удаляем его.

Определение правила обработки:

```
USING(INOUT redundant.attribute:STRING)


| FIELDS_REMOVE(redundant.attribute)
```

Пример лог-данных:

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

Мы можем использовать символ `?`, чтобы пометить атрибут как необязательный, тогда преобразование все равно будет выполнено и завершится успешно, даже если атрибут отсутствует в исходном событии.

В этом случае определение будет выглядеть так:

```
USING(INOUT redundant.attribute:STRING?)


| FIELDS_REMOVE(redundant.attribute)
```

### Пример 12: Удаление всего лог-события

Все лог-событие может быть удалено командой `FILTER_OUT`. Событие удаляется, когда условие, переданное как параметр команды, выполнено.

* Удаление на основе предварительного сопоставления.
  В большинстве случаев достаточно удалить каждое предварительно сопоставленное событие.

  Например, если мы хотим удалить все события `DEBUG` и `TRACE`, мы можем установить запрос сопоставления для соответствия любому из этих статусов, а затем использовать команду `FILTER_OUT` для перехвата всего.

  Сопоставитель:

  ```
  status="DEBUG" or status="TRACE"
  ```

  Определение правила обработки:

  ```
  FILTER_OUT(true)
  ```

  Пример лог-данных:

  ```
  {


  "status": "DEBUG",


  "content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."


  }
  ```

  Таким образом, все логи со статусом `DEBUG` или `TRACE` удаляются.
* Расширенное условие удаления.
  Также возможно иметь дополнительную логику и не удалять все предварительно сопоставленные события.

  В следующем примере мы удаляем входящие события, где время выполнения менее 100 мс.

  Пример лог-данных:

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

### Пример 13: Маскировка любого атрибута

Когда содержимое или любой другой атрибут должен быть изменен, его необходимо объявить как `INOUT` (записываемый) с помощью команды `USING`. `REPLACE_PATTERN` -- это мощная функция, полезная для маскировки части атрибута.

* В следующем примере мы маскируем IP-адрес, устанавливая значение 0 для последнего октета.

  Определение правила обработки:

  ```
  USING(INOUT ip)


  | FIELDS_ADD(ip: IPADDR(ip) & 0xFFFFFF00l)
  ```

  Пример лог-данных:

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
* В следующем примере мы маскируем IP-адрес, устанавливая значение `xxx` для последнего октета.

  Определение правила обработки:

  ```
  USING(INOUT ip)


  | FIELDS_ADD(ip: REPLACE_PATTERN(ip, "(INT'.'INT'.'INT'.'):not_masked INT", "${not_masked}xxx"))
  ```

  Пример лог-данных:

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
* В следующем примере мы маскируем весь адрес электронной почты с помощью `sha1` (алгоритм безопасного хеширования).

  Определение правила обработки:

  ```
  USING(INOUT email)


  | FIELDS_ADD(email: REPLACE_PATTERN(email, "LD:email_to_be_masked", "${email_to_be_masked|sha1}"))
  ```

  Пример лог-данных:

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
* В следующем примере мы маскируем IP-адрес, адрес электронной почты и номер кредитной карты из поля содержимого.

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

  Пример лог-данных:

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

### Пример 14: Переименование атрибутов

С помощью команды `FIELDS_RENAME` мы можем переименовывать атрибуты, которые были частью исходного лог-события, и атрибуты, созданные в процессоре.
Когда мы хотим изменить любой атрибут из исходного события, нам нужно объявить его как `INOUT` (записываемый).

В следующем примере мы переименовываем существующий атрибут. Кроме того, мы извлекаем поле из JSON в плоском режиме и переименовываем новый атрибут, созданный автоматически с именем поля JSON.

Определение правила обработки:

```
USING(INOUT to_be_renamed, content)


| FIELDS_RENAME(better_name: to_be_renamed)


| PARSE(content,"JSON{STRING:json_field_to_be_renamed}(flat=true)")


| FIELDS_RENAME(another_better_name: json_field_to_be_renamed)
```

Пример лог-данных:

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

### Пример 15: Типы данных входных полей

Скрипт в определении процессора работает со строго типизированными данными: функции и операторы принимают только объявленные типы данных. Тип назначается всем входным полям, определенным в команде `USING`, а также переменным, созданным при парсинге или использовании функций приведения типов.

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

Пример лог-данных:

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
