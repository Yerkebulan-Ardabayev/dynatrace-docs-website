---
title: Log on Grail examples
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/logs-on-grail-examples
scraped: 2026-03-06T21:15:20.149749
---

# Примеры работы с логами в Grail

# Примеры работы с логами в Grail

* Последняя версия Dynatrace
* Обзор
* 17 мин. чтения
* Обновлено 15 октября 2025 г.

Log Management and Analytics на основе Grail позволяет точно находить и извлекать любые данные логов с помощью [Dynatrace Query Language](../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language."). Ознакомившись с [основами запросов DQL](../../platform/grail/dynatrace-query-language/dql-guide.md "Узнайте, как работает DQL и каковы ключевые концепции DQL."), используйте примеры на этой странице, чтобы начать получать ответы из данных ваших логов.

Для выполнения запросов DQL с логами в Grail перейдите в ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic** > **Advanced mode**.

* [Пример 1](logs-on-grail-examples.md#logexample1 "Изучите базовые примеры Log Management and Analytics по использованию данных логов в Dynatrace на основе Grail.") — Получение распределения HTTP-кодов состояния и количества по типам ошибок.
* [Пример 2](logs-on-grail-examples.md#logexample2 "Изучите базовые примеры Log Management and Analytics по использованию данных логов в Dynatrace на основе Grail.") — Определение среднего размера корзины на основе логов.
* [Пример 3](logs-on-grail-examples.md#logexample3 "Изучите базовые примеры Log Management and Analytics по использованию данных логов в Dynatrace на основе Grail.") — Отслеживание изменений пользователей с помощью журналов аудита.
* [Пример 4](logs-on-grail-examples.md#logexample4 "Изучите базовые примеры Log Management and Analytics по использованию данных логов в Dynatrace на основе Grail.") — Создание метрики на основе логов.
* [Пример 5](logs-on-grail-examples.md#logexample5 "Изучите базовые примеры Log Management and Analytics по использованию данных логов в Dynatrace на основе Grail.") — Создание оповещения на основе логов.

### Пример 1: Коды состояния и количество

В этом примере вы получите распределение HTTP-кодов состояния и количество по типам ошибок.

Прокси-сервер записывает HTTP-коды состояния ответов. Вам нужно увидеть распределение кодов ответов за определённый временной период и сфокусироваться на ошибках.

1. Поиск релевантных логов.
   Начните с поиска логов из экземпляра HAProxy. Поскольку строка `haproxy` содержится в сообщении лога, используем функцию `contains()`.

   ```
   fetch logs



   | filter contains(content, "haproxy")
   ```

   Поиск строки `haproxy` выполняется по всем записям в указанном временном диапазоне, поэтому следует сузить его для оптимизации запроса. Если сущность, которая генерирует логи, может быть определена заранее, гораздо эффективнее искать внутри этой конкретной сущности.

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-123F4A56BCDA0EA9"
   ```

   **Таблица результатов**
2. Извлечение метрики из поля content.
   Поле content лога содержит HTTP\_STATUS коды, которые вам нужны. Теперь используем команду `parse` для создания шаблона [Dynatrace Pattern Language](../../platform/grail/dynatrace-pattern-language.md "Используйте Dynatrace Pattern Language для описания шаблонов с помощью матчеров.") со следующими элементами:

   * `LD`: начинаем с сопоставления любых [строковых данных](../../platform/grail/dynatrace-pattern-language/log-processing-lines-strings.md#line-data "Изучите синтаксис DPL для обработки строк.") в начале поля
   * `'HTTP_STATUS '`: [литеральное выражение](../../platform/grail/dynatrace-pattern-language/log-processing-literal-expression.md "Изучите синтаксис DPL для обработки литеральных выражений."), непосредственно предшествующее числовому HTTP-статусу, с учётом пробела
   * `INT:httpstatus`: [целое число](../../platform/grail/dynatrace-pattern-language/log-processing-numeric.md#int-integer "Изучите синтаксис DPL для обработки числовых данных."), которое будет извлечено как новое поле `httpstatus`

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-123F4A56BCDA0EA9"



   | parse content, "LD 'HTTP_STATUS ' INT:httpstatus"
   ```

   **Таблица результатов**
3. Фильтрация диапазона значений.
   Вы можете выбрать диапазон значений для дальнейшего анализа с помощью DQL. Выбираем только HTTP-коды состояния начиная с 400 и выше, так как они включают ошибки на стороне клиента и сервера.

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-802F3A32CECA0EA9"



   | parse content, "LD 'HTTP_STATUS ' INT:httpstatus"



   | filter httpstatus >= 400
   ```
4. Агрегация результатов.
   Необходимо агрегировать результаты с помощью count(), чтобы получить сводку того, сколько раз встречается каждый код состояния.

   ```
   fetch logs



   | filter dt.entity.process_group=="PROCESS_GROUP-802F3A32CECA0EA9"



   | parse content, "LD 'HTTP_STATUS ' INT:httpstatus"



   | filter httpstatus >= 400



   | summarize count(), by:{httpstatus}
   ```

   **Таблица результатов**

### Пример 2: Средний размер корзины

В этом примере вы определите средний размер корзины на основе логов.

Ваше приложение записывает в логи контекстные данные, релевантные для вашего бизнеса. Вам нужно извлечь эти данные из логов и создать отчёт за определённый временной период.

1. Выбор данных конкретного процесса за определённый период.
   Необходимо запросить логи за последние три часа (ваш временной период) и указать процесс, обрабатывающий действия с корзиной в вашем магазине, `cartservice cartservice-*`.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"
   ```

   **Таблица результатов**
2. Проверка типов и количества продуктов, добавленных в корзины.
   Вам нужно получить обзор типа и количества продуктов, которые пользователи добавили в корзины. Поскольку логи содержат различные события, необходимо указать события добавления товаров в корзину с помощью функции `contains()`. Для очистки таблицы результатов рекомендуется оставить только временную метку и содержимое лога.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content
   ```

   **Таблица результатов**
3. Извлечение продуктов и соответствующих количеств.
   Необходимо извлечь идентификаторы продуктов и количества из логов с помощью команды `parse`.
   Используя [Dynatrace Pattern Language](../../platform/grail/dynatrace-pattern-language.md "Используйте Dynatrace Pattern Language для описания шаблонов с помощью матчеров."), создайте шаблон и сопоставьте следующие части поля `content`:

   * `LD`: начинаем с сопоставления любых [строковых данных](../../platform/grail/dynatrace-pattern-language/log-processing-lines-strings.md#line-data "Изучите синтаксис DPL для обработки строк.") в начале поля
   * `'userId='`: [литеральное выражение](../../platform/grail/dynatrace-pattern-language/log-processing-literal-expression.md "Изучите синтаксис DPL для обработки литеральных выражений."), непосредственно предшествующее идентификатору пользователя
   * `LD:userId`: любые строковые данные, которые будут извлечены как новое поле с именем `userId`
   * `', productId='`: литеральное выражение, завершающее идентификатор пользователя и отделяющее его от идентификатора продукта
   * `LD:productId`: любые строковые данные, которые будут извлечены как новое поле с именем `productId`
   * `', quantity='`: литеральное выражение, завершающее идентификатор продукта и отделяющее его от количества
   * `INT:productQuantity`: [целое число](../../platform/grail/dynatrace-pattern-language/log-processing-numeric.md#int-integer "Изучите синтаксис DPL для обработки числовых данных."), которое будет извлечено как новое поле с именем `productQuantity`

   Оставшиеся поля игнорируются.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"
   ```

   **Таблица результатов**
4. Очистка данных.
   Поскольку идентификатор пользователя и исходная запись лога больше не нужны, очистим таблицу результатов с помощью команды `fields`.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"



   | fields productId , productQuantity
   ```

   **Таблица результатов**
5. Суммирование событий по продуктам.
   Чтобы увидеть общее количество каждого продукта, добавленного в корзину, используйте функцию `sum()`.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"



   | fields productId , productQuantity



   | summarize sum(productQuantity), by:{productId}
   ```

   **Таблица результатов**
6. Поиск самых популярных продуктов.
   Чтобы понять поведение среднего пользователя, мы хотим определить средний размер корзины для каждого продукта. Для этого используем функцию `avg()` и назовём новое поле `averageProductQuantity`. Затем сортируем средние значения от наибольшего к наименьшему и ограничиваем результаты, чтобы увидеть пять самых популярных продуктов.

   ```
   fetch logs, from:now()-3h



   | filter dt.process.name=="cartservice cartservice-*"



   | filter contains(content, "AddItemAsync")



   | fields timestamp, content



   | parse content, "LD 'userId=' LD:userId ', productId=' LD:productId ', quantity=' INT:productQuantity"



   | fields productId , productQuantity



   | summarize averageProductQuantity = avg(productQuantity), by:{productId}



   | sort averageProductQuantity desc



   | limit 5
   ```

   **Таблица результатов**

### Пример 3: Отслеживание изменений пользователей

В этом примере вы отслеживаете изменения пользователей с помощью журналов аудита. Вы хотите отследить тип и количество действий, выполненных пользователями.

1. Проверка наличия свежих журналов аудита.

   * Узнайте, появились ли журналы аудита за последние пять минут.
   * Установите временной диапазон и фильтруйте только логи, путь источника которых заканчивается вашим назначенным путём.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")
   ```

   **Таблица результатов**
2. Извлечение релевантных полей для одного пользователя.

   * Полученная таблица включает обновления, удаления и создания записей.
   * Ограничив запрос последним результатом, вы сможете понять действия, выполненные одним пользователем.

   Затем выполняем следующее:

   * Используем `parse` для преобразования поля `content` в JSON-объект
   * Используем `fieldsAdd` для извлечения релевантных полей из этого объекта
   * Используем `fields` для добавления релевантного поля
   * Используем `fieldsRemove` для получения только нужных столбцов

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | limit 1



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings
   ```

   **Таблица результатов**
3. Получение пользователей, выполнивших обновления и удаления.
   Чтобы получить только пользователей, которые выполнили обновления или удаления:

   * Удалите команду `limit`
   * Добавьте фильтр для двух типов действий: обновление и удаление.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings



   | filter in(type,array("UPDATE","DELETE"))
   ```

   **Таблица результатов**
4. Определение типов изменений и количества изменений, выполненных каждым пользователем.
   Вы можете подсчитать записи с помощью команды `summarize`.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings



   | filter in(type,array("UPDATE","DELETE"))



   | summarize count(), by:{user,type}
   ```

   **Таблица результатов**
5. Подсчёт событий по пользователям с разбивкой по типу действия (создание, обновление, удаление).
   Вы можете выполнить расчёт, объединив команду `summarize` с функцией `countIf`.

   ```
   fetch logs, from:now()-5m



   | filter endsWith(log.source,"change.log")



   | parse content, "TIMESTAMP('yyyy-MM-dd HH:mm:ss'):ts LD JSON:settings"



   | fields ts, settings



   | fieldsAdd type = settings[eventType], tenant = settings[tenantId], user = settings[userId]



   | fieldsRemove settings



   | filter in(type,array("UPDATE","DELETE"))



   | summarize {countIf(type=="CREATE"), countIf(type=="UPDATE"), countIf(type=="DELETE")}, by:{tenant, user}
   ```

   **Таблица результатов**

### Пример 4: Создание метрики на основе логов

В этом примере вам нужно подсчитать, сколько отказов в соединении зафиксировано в данных ваших логов. Для этого отфильтруйте нужные логи и преобразуйте количество вхождений в метрику на основе логов.

* [Создание метрики отказов в соединении](lma-use-cases/lma-e2e-create-log-metric.md#lma-uc-create-connections-refused-metric "Изучите сценарий использования Log Management and Analytics для создания метрики на основе логов.")

В этом примере вам нужно отслеживать атрибут ваших логов и контролировать уровни ошибок, сообщаемых в логах вашего кластера Kubernetes.

* [Создание метрики атрибутов логов](lma-use-cases/lma-e2e-create-log-metric.md#lma-uc-create-log-attribute-metric "Изучите сценарий использования Log Management and Analytics для создания метрики на основе логов.")

### Пример 5: Создание оповещения на основе логов

В этом примере вам нужно настроить оповещение на основе появления событий в логах. Узнайте, как извлечь данные из логов, создать правило обработки, сформировать оповещение на основе события лога и проверить, захватывает ли ваше оповещение логи, соответствующие заданным критериям.

* [Настройка оповещений на основе событий, извлечённых из логов](lma-use-cases/lma-alert-log-based-events.md "Как создавать и настраивать проблемы и оповещения Davis на основе событий из логов.")

### Создание метрики для обнаружения аномалий

В этом сценарии использования вам нужно автоматизировать обнаружение аномалий. Узнайте, как извлечь данные из логов, создать правило обработки, создать метрику и настроить оповещение, генерирующее уведомление при обнаружении аномалии.

* [Настройка пользовательских оповещений на основе метрик, извлечённых из логов](lma-use-cases/lma-alert-log-based-metrics.md "Как создавать и настраивать проблемы и пользовательские оповещения Davis на основе метрик из логов.")