---
title: Снижение кардинальности на основе span и метрик
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/reduce-span-metric-cardinality
scraped: 2026-03-06T21:10:39.754758
---

# Снижение кардинальности спанов и метрик


* Latest Dynatrace

Обработка OpenPipeline позволяет нормализовать данные спанов и метрик для предотвращения проблем высокой кардинальности, которые могут сделать агрегации и анализ непригодными для использования.

Следующие сценарии использования показывают, как снизить кардинальность в трёх различных представлениях в [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](../../../observe/application-observability/services/services-app.md "Обеспечьте централизованный контроль над здоровьем, производительностью и ресурсами сервисов с помощью приложения Services."):

* [Исходящие вызовы](#outbound-calls)
* [Запросы к базе данных](#database-queries): эта вкладка показывает агрегированные метрики для вызовов базы данных, выполняемых вашим сервисом.
* [Обработка сообщений](../../../observe/application-observability/services/monitor-service-message-processing.md "Мониторинг обработки сообщений сервиса")

## Исходящие вызовы

### Высокая кардинальность в исходящих вызовах

Вкладка **Outbound calls** отображает агрегированные метрики для внешних вызовов, выполняемых вашим сервисом. Высокая кардинальность возникает, когда URL содержат уникальные идентификаторы в пути, например `/users/12345` или `/orders/abc-def-123`, что приводит к созданию множества различных значений.

Правила обработки помогают преобразовать их в нормализованные шаблоны, такие как `/users/*` или `/orders/*`, оптимизируя данные исходящих вызовов.

### Создание правила нормализации исходящих вызовов

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans**.
2. Перейдите на вкладку **Pipelines**. Выберите  **Pipeline** и введите имя (например, `Outbound call normalization`) для создания нового пайплайна.
3. Перейдите в **Processing** >  **Processor** > **DQL** и настройте новое правило обработки для снижения кардинальности URL.
4. Введите следующий новый DQL-процессор для нормализации URL:

   * **Name**: URL или любое предпочтительное имя.
   * **Matching Condition**: следующее условие совпадает со всеми исходящими HTTP-вызовами.

     ```
     span.kind == "client" and isNotNull(url.full)
     ```
   * **DQL processor definition**

     ```
     fieldsAdd url.full.orig = url.full


     | fieldsAdd path_normalized = replacePattern(url.path, "UUIDSTRING", "[UUID]")


     | fieldsAdd path_normalized = replacePattern(path_normalized, "[/]LONG", "/[Number]")


     | fieldsAdd port = if(isNotNull(server.port), concat(":", server.port),   else:null)


     | fieldsAdd url.full = concat(url.scheme, "://", server.address, port, path_normalized)
     ```

### Активация процессора

Теперь, когда мы определили и сохранили процессор, мы можем активировать его, подключив к OpenPipeline через новый динамический маршрут, чтобы ваш пайплайн получал данные спанов.

1. На странице **Spans** перейдите на вкладку **Dynamic routing**.
2. Выберите  **Dynamic route**.
3. Определите динамический маршрут.

   * **Name**: имя, которое вы дали процессору ранее.
   * **Matching Condition**: следующее условие совпадает со всеми исходящими HTTP-вызовами.

     ```
     span.kind =="client" and isNotNull(url.full)
     ```
   * **Pipeline**: выберите ранее созданный пайплайн из списка.
4. Выберите **Save**.

## Запросы к базе данных

Операторы Redis часто содержат уникальные идентификаторы или значения, например `GET user:12345`, `GET user:12346` и `GET user:12347` или `SET order:123`, `SET order:124` и `SET order:125`. Эта высокая кардинальность приводит к тысячам различных записей, отображаемых в представлении [**Database queries**](../../../observe/application-observability/services/services-app.md#database-queries "Обеспечьте централизованный контроль над здоровьем, производительностью и ресурсами сервисов с помощью приложения Services.") в ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.

В отличие от параметризованных баз данных SQL, где OneAgent или OpenTelemetry автоматически обрабатывают нормализацию, команды Redis требуют ручной обработки кардинальности через пайплайн OpenPipeline. В этом разделе мы используем правило обработки для преобразования этих команд в нормализованные шаблоны, такие как `GET` или `SET`, делая данные запросов Redis более пригодными для анализа.

### 1. Создание пайплайна

Сначала создадим пайплайн, содержащий правило обработки для снижения кардинальности операторов Redis. Поскольку ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** использует атрибут `db.query.text`, вы будете настраивать этот конкретный атрибут для нормализации операторов Redis, отображаемых в представлении **Database queries**.

Для создания пайплайна

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Spans**.
2. Перейдите на вкладку **Pipelines** и выберите  **Pipeline**.
3. Введите **DB statement normalization** в качестве имени пайплайна.
4. На вкладке **Processing** выберите >  **Processor** > **DQL** и настройте новый DQL-процессор:

   * **Name**: **Redis**
   * **Matching condition**:

     ```
     db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))
     ```

     Пояснение условия совпадения

     + `db.system == "redis"`: совпадение со всеми системами баз данных `redis`.
     + `(isNotNull(db.statement) or isNotNull(db.query.text))`: требование, чтобы в спанах базы данных Redis использовался либо старый атрибут `db.statement`, либо новый `db.query.text`.

       `db.statement` по-прежнему часто встречается в некоторых инструментациях OpenTelemetry.
   * **DQL processor definition**:

     ```
     fieldsAdd db.query.text = coalesce(db.query.text, db.statement)


     | fieldsAdd db.query.text.orig = db.query.text


     | fieldsAdd blankPos = indexOf(db.query.text.orig, " ")


     | fieldsAdd db.query.text = if (blankPos > 0, substring(db.query.text, from: 0, to: blankPos), else: "*")
     ```

     Пояснение определения процессора

     + `fieldsAdd db.query.text = coalesce(db.query.text, db.statement)`: обеспечивает работу условия совпадения как со старым атрибутом `db.statement`, так и с новым `db.query.text`.

       Многие инструментации OpenTelemetry по-прежнему используют `db.statement` вместо `db.query.text`. Эта строка гарантирует, что оба поля учитываются, так как `coalesce()` возвращает первый ненулевой аргумент.
     + `fieldsAdd db.query.text.orig = db.query.text`: сохранение исходного значения атрибута `db.query.text`.

       Хотя низкая кардинальность `db.query.text` важна в ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, сохранение исходного значения атрибута `db.query.text` весьма полезно и может использоваться для дальнейшей детализации.
     + `fieldsAdd blankPos = indexOf(db.query.text.orig, " ")` и `fieldsAdd db.query.text = if (blankPos > 0, substring(db.query.text, from: 0, to: blankPos), else: "*")`: упрощение атрибута `db.query.text` путём извлечения нового значения от начала текста до первого пробела.

       Запрос базы данных Redis — это значение до первого пробела оператора, поэтому этот пробел находится, а затем в качестве `db.query.text` сохраняется только часть до этого пробела.
5. Выберите **Save** в правом верхнем углу страницы.

Вы должны увидеть пайплайн **DB statement normalization** в списке пайплайнов.

Если у вас есть другие базы данных с операторами высокой кардинальности, добавьте дополнительные DQL-процессоры в пайплайн **DB statement normalization**. Настройте процессоры в соответствии с вашей ситуацией. Дополнительные примеры см. в разделе [Другие DQL-процессоры](#db-queries-dql-processor-examples).

### 2. Создание динамического маршрута

Теперь, когда вы создали новый пайплайн и определили DQL-процессор для снижения кардинальности, активируйте этот процессор, подключив его к OpenPipeline через динамический маршрут. Таким образом ваш пайплайн сможет получать данные спанов.

Для создания динамического маршрута

1. На странице **Spans** перейдите на вкладку **Dynamic routing**.
2. Выберите  **Dynamic route**.
3. Определите динамический маршрут:

   * **Name**: **DB statement normalization**
   * **Matching condition**:

     ```
     isNotNull(db.statement) and (isNotNull(db.statement) or isNotNull(db.query.text))
     ```
   * **Pipeline**: выберите ранее созданный пайплайн **DB statement normalization** из списка пользовательских пайплайнов.
4. Выберите **Add**, а затем **Save**.

Вы должны увидеть динамический маршрут **DB statement normalization** в списке динамических маршрутов.

### 3. Другие DQL-процессоры (необязательно)

Как упоминалось ранее, вы можете добавлять дополнительные DQL-процессоры при обнаружении запросов к базе данных с высокой кардинальностью.

Ознакомьтесь с разделами ниже для трёх дополнительных примеров DQL-процессора. При добавлении нового процессора установите **Matching condition** в `db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))`, а **DQL processor definition** — в значение, указанное в одном из примеров ниже.

Перед внедрением нового DQL-процессора можно использовать ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** для проверки того, как DQL-процессор преобразует ваши данные.

1. Перейдите в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. Выберите  **Notebook** в заголовке приложения для создания нового блокнота.
3. Откройте меню  (**Add**) и выберите  **DQL**.
4. В разделе запроса введите необходимый DQL-запрос.
5. Выберите  **Run** для выполнения DQL-запроса.

Оригинал: Полная кардинальность

Используйте следующий DQL-запрос для подсчёта исходного количества операторов Redis (до снижения кардинальности).

**DQL-запрос в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****:

```
fetch spans


| filter db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))


| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)


| summarize count(), by: { db.query.text }


| sort `count()` desc
```

Run in Playground

Вариант 1: Сокращённый

Этот DQL-процессор заменяет `db.query.text` первыми 15 символами + `*`. Этот вариант хорош для быстрого снижения кардинальности независимо от формата содержимого.

**DQL processor definition**:

```
| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)


| fieldsAdd db.query.text.orig = db.query.text


| fieldsAdd db.query.text = concat(substring(db.query.text, from: 0, to: 15), "*")
```

**DQL-запрос в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****:

```
fetch spans


| filter db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))


| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)


| fieldsAdd db.query.text.orig = db.query.text


| fieldsAdd db.query.text = concat(substring(db.query.text, from: 0, to: 15), "*")


| summarize count(), by: { db.query.text }


| sort `count()` desc
```

Run in Playground

Вариант 2: Только команда Redis

Этот DQL-процессор извлекает первое слово в `db.query.text`, обрезая по первому пробелу. Этот вариант отлично подходит для получения только команд Redis, например `GET` или `SET`.

**DQL processor definition**:

```
| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)


| fieldsAdd db.query.text.orig = db.query.text


| fieldsAdd blankPos = indexOf(db.query.text.orig, " ")


| fieldsAdd db.query.text = if(blankPos > 0, substring(db.query.text, from: 0, to: blankPos), else: "*")
```

**DQL-запрос в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****:

```
fetch spans


| filter db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))


| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)


| fieldsAdd db.query.text.orig = db.query.text


| fieldsAdd blankPos = indexOf(db.query.text.orig, " ")


| fieldsAdd db.query.text = if(blankPos > 0, substring(db.query.text, from: 0, to: blankPos), else: "*")


| summarize count(), by: { db.query.text }


| sort `count()` desc
```

Run in Playground

Вариант 3: Имя операции БД

Этот DQL-процессор устанавливает `db.query.text` в значение `db.operation.name`. Используйте этот вариант, когда вы хотите видеть операцию Redis вместо текста запроса к базе данных.

**DQL processor definition**:

```
| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)


| fieldsAdd db.query.text.orig = db.query.text


| fieldsAdd db.query.text = if(isNotNull(db.operation.name), db.operation.name, else: "*")
```

**DQL-запрос в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks****:

```
fetch spans


| filter db.system == "redis" and (isNotNull(db.statement) or isNotNull(db.query.text))


| fieldsAdd db.query.text = coalesce(db.query.text, db.operation.name)


| fieldsAdd db.query.text.orig = db.query.text


| fieldsAdd db.query.text = if(isNotNull(db.operation.name), db.operation.name, else: "*")


| summarize count(), by: { db.query.text }


| sort `count()` desc
```

Run in Playground

После создания пайплайна **DB statement normalization** и его активации путём создания динамического маршрута вы должны увидеть, что кардинальность ваших операторов Redis значительно снизилась при просмотре представления **Database queries** в ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**. Например, операторы вида `GET as:1:swuq:abc-677d3b`, `SET as:1:rl:wf:d1d42f` или `DECRBY as:1:paec:wis70158` теперь отображаются как `GET`, `SET` и `DECRBY`. Такие нормализованные запросы Redis обеспечивают более простой и эффективный анализ.

## Обработка сообщений

![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** включает представление **Message processing**, которое агрегирует метрики для операций обмена сообщениями. Высокая кардинальность возникает, когда создаются временные очереди с уникальными идентификаторами в именах (такие как `amq.gen-6dggtCpu`, `async-job-2jrmsi5y` или `orders-reply-2n68vy4g`), что генерирует тысячи различных имён очередей, делающих агрегации непригодными.

Большинство инструментаций поддерживают низкую кардинальность `messaging.destination.name`, используя нестандартные поля вроде `messaging.temp.queue.hash` для данных высокой кардинальности или устанавливая `messaging.destination.temporary`. Однако, когда инструментация не следует этим практикам, правила обработки OpenPipeline могут нормализовать имена временных очередей в шаблоны или пометить их как временные.

### Высокая кардинальность в обработке сообщений

Перед внедрением правил нормализации запросите свои спаны для выявления систем обмена сообщениями с высоким процентом уникальных имён назначений.

1. Перейдите в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и выберите  **Notebooks** для создания нового блокнота.
2. Выберите  **New section** > **DQL**.
3. Скопируйте и вставьте следующий запрос в поле редактирования и выберите  **Run**.

   ```
   fetch spans


   | filter isNotNull(messaging.system) and isNotNull(messaging.destination.name)


   | summarize count=count(), distinctCount=countDistinct(messaging.destination.name), by:{messaging.system, messaging.destination.temporary}


   | fieldsAdd cardinality_ratio = toDouble(distinctCount) / toDouble(count)
   ```
4. Изучите результаты на предмет высоких коэффициентов кардинальности.

   Системы с высоким коэффициентом кардинальности (выше `0.5`) без установленного `messaging.destination.temporary` указывают на очереди, которые:

   * Приведут к чрезмерному количеству метрик с минимальной аналитической ценностью.
   * Выиграют от нормализации, описанной ниже.

### Создание правила нормализации обработки сообщений

Вы можете использовать правила обработки OpenPipeline для нормализации имён временных очередей в шаблоны или пометки их как временных.

Для создания правила

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** и выберите **Process and contextualize** > **OpenPipeline** > **Spans**.
2. Перейдите на вкладку **Pipelines** и создайте новый пайплайн, выбрав  **Pipeline** и введя имя (например, `Queue handling`).
3. Выберите, нормализовать ли имена временных очередей в шаблоны или пометить их как временные.

   Пометить как временные

   Заменить имя очереди

   На вкладке **Processing** выберите  **Processor** и выберите **DQL**.

   Для добавления/переопределения флага временной очереди определите следующий новый DQL-процессор:

   * **Name**: `Temporary queue selector` (или любое имя по вашему выбору)
   * **Matching Condition**: следующее условие совпадает со всеми спанами обмена сообщениями, обнаруженными как невременные, и соответствующими определённому шаблону назначения `odaRequestQueue*`, который мы хотим переопределить как временный.

     ```
     messaging.destination.temporary == false and


     matchesPhrase(messaging.destination.name, "odaRequestQueue*")
     ```
   * **DQL processor definition**: единственное действие — перезаписать существующее значение с false на true.

     ```
     fieldsAdd messaging.destination.temporary = true
     ```

   На вкладке **Processing** выберите  **Processor** и выберите **Add fields**.

   Для переименования назначений обмена сообщениями определите следующий новый DQL-процессор:

   * **Name**: `Destination renamer` (или любое имя по вашему выбору)
   * **Matching Condition**: следующее условие совпадает со всеми спанами, связанными с назначениями обмена сообщениями, начинающимися с `odaRequestQueue`.

     ```
     matchesPhrase(messaging.destination.name, "odaRequestQueue*")
     ```
   * **Add fields**: для замены исходного содержимого можно просто добавить поле снова с исправленным значением. В данном случае исходная строка, заканчивающаяся последовательными числами, заменяется статической строкой, содержащей только первую, постоянную часть имени назначения.

     Введите следующее и выберите **Add**:

     + **Name**: `messaging.destination.name`
     + **Value**: `odaRequestQueue`
4. Выберите **Save**.

### Активация процессора

Теперь, когда мы определили и сохранили процессор, мы можем активировать его, подключив к OpenPipeline через новый динамический маршрут, чтобы ваш пайплайн получал данные спанов.

1. Оставаясь на странице **Spans**, перейдите на вкладку **Dynamic routing**.
2. Выберите  **Dynamic route**.
3. Определите динамический маршрут.

   * **Name**: имя, которое вы дали процессору ранее.
   * **Matching Condition**: следующее условие совпадает со всеми спанами, связанными с назначениями обмена сообщениями, начинающимися с `odaRequestQueue`.

     ```
     matchesPhrase(messaging.destination.name, "odaRequestQueue*")
     ```
   * **Pipeline**: выберите из списка.
4. Выберите **Save**.

После применения этих правил очереди с высокой кардинальностью будут иметь либо установленный флаг `messaging.destination.temporary` в true, либо нормализованные имена, что значительно снизит кардинальность метрик в представлении обработки сообщений. Для проверки см. раздел [Как определить высокую кардинальность](#identify-high-cardinality) выше.
