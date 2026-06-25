---
title: Settings API key concepts
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/key-concepts
scraped: 2026-05-12T11:38:49.757612
---

# Settings API key concepts

# Settings API key concepts

* Explanation
* Updated on Mar 26, 2026

Settings API предоставляет иерархию объектов конфигурации, организованных по schema и scope. Перед тем как работать с ним в масштабе, убедитесь, что понимаете, как API сохраняет объекты, как значения проходят через иерархию scope и как API обрабатывает concurrency, пагинацию и управление доступом.

## Обзор

Schemas определяют settings objects; scopes определяют, на каком уровне применяется конфигурация. Каждая schema задаёт форму и ограничения типа конфигурации. API предоставляет отдельные endpoints для чтения в зависимости от того, нужны ли вам явно сохранённые значения или значения, действующие в данный момент.

### Schemas

**Релевантные endpoints:** [Список schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "Просмотр всех settings schemas вашего окружения мониторинга через Dynatrace API."), [Просмотр schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотр settings schema через Dynatrace API.")

Schema определяет структуру settings object: его свойства, их типы и ограничения, а также поведенческие атрибуты, такие как `multiObject`, `ordered` и `maxObjects`. Каждый settings object, который вы читаете или записываете, ссылается на schema по её `schemaId`.

* Используйте [Список schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "Просмотр всех settings schemas вашего окружения мониторинга через Dynatrace API."), чтобы узнать, какие schemas доступны в вашем окружении.
* Используйте [Просмотр schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотр settings schema через Dynatrace API."), чтобы изучить определения свойств конкретной schema перед составлением payload. Это особенно полезно для понимания обязательных полей, перечислений и свойств типа secret.

`schemaId`, который вы получаете из endpoints для schema, это то, что вы передаёте в качестве параметра `schemaId` при чтении или записи объектов с помощью [Список объектов](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких settings objects через Dynatrace API."), [Создать объект](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создание или валидация settings object через Dynatrace API.") и других endpoints для объектов.

### Сохранённые объекты против фактических значений

API предоставляет два разных представления данных настроек:

* [Список объектов](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких settings objects через Dynatrace API.") возвращает только объекты, которые вы явно сохранили на запрашиваемых scopes. Если вы ничего не записали для данной комбинации schema/scope, ответ пустой.
* [Просмотр фактических значений](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "Просмотр фактической конфигурации для settings schema через Dynatrace API.") вычисляет полную иерархию конфигурации: он поднимается вверх по дереву scope и применяет значения по умолчанию из schema там, где явное значение отсутствует. Этот endpoint всегда возвращает результат для валидной комбинации schema/scope, даже если вы никогда не сохраняли объект.

Используйте [Список объектов](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких settings objects через Dynatrace API."), когда вам нужно управлять состоянием конфигурации или проводить его аудит. Используйте [Просмотр фактических значений](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "Просмотр фактической конфигурации для settings schema через Dynatrace API."), когда вам нужно значение, которое фактически действует для данного scope.

### Single-value против multi-value schemas

Settings schemas бывают двух видов, что определяется свойством `multiObject` в определении schema:

* **Одно значение** (`multiObject: false`): не более одного объекта на scope. Отсутствие означает, что действует значение по умолчанию из schema или значение, заданное на родительском scope.
* **Несколько значений** (`multiObject: true`): ноль или более объектов могут сосуществовать на одном scope, вплоть до предела, заданного `maxObjects`. Когда свойство `ordered` у schema равно `true`, порядок элементов имеет семантическое значение; используйте `insertAfter` и `insertBefore` в запросах создания/обновления для управления позиционированием.

### Scopes

Каждый settings object нацелен ровно на один scope, который вы задаёте через поле `scope` при создании. Фильтр `scopes` в [Список объектов](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких settings objects через Dynatrace API.") сопоставляет только объекты, которые напрямую нацелены на указанный scope; он не обходит иерархию. Например, фильтрация по `environment` не вернёт объекты, нацеленные на хост внутри этого окружения.

### External IDs

**Релевантные endpoints:** [Создать объект](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создание или валидация settings object через Dynatrace API.") (тело запроса), [Список объектов](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких settings objects через Dynatrace API.") (query-параметр `externalIds`)

Поле `externalId` позволяет назначить стабильный, заданный вызывающей стороной идентификатор для settings object во время создания (максимум 500 символов). Это включает **паттерн upsert**: если объект с данным `externalId` уже существует на целевом scope, запрос заменяет его, а не создаёт дубликат. Вы также можете искать объекты по их external IDs с помощью параметра `externalIds` в [Список объектов](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких settings objects через Dynatrace API.").

### Оптимистичная блокировка

**Релевантные endpoints:** [Список объектов](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких settings objects через Dynatrace API."), [Просмотр объекта](/managed/dynatrace-api/environment-api/settings/objects/get-object "Просмотр settings object через Dynatrace API."), [Редактировать объект](/managed/dynatrace-api/environment-api/settings/objects/put-object "Редактирование settings object через Dynatrace API."), [Удалить объект](/managed/dynatrace-api/environment-api/settings/objects/del-object "Удаление settings object через Dynatrace API.")

Поле `updateToken` это механизм управления параллелизмом. API генерирует и возвращает его при каждом запросе на получение. Включение его в последующий запрос обновления или удаления означает, что операция выполнится только если объект не изменился с момента вашей последней выборки; если он изменился, API отклоняет запрос, чтобы вы могли согласовать конфликт.

Пропуск `updateToken` при записи или удалении обходит эту проверку и безусловно применяет изменение.

### Пагинация

**Релевантные endpoints:** [Список объектов](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких settings objects через Dynatrace API."), [Просмотр фактических значений](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "Просмотр фактической конфигурации для settings schema через Dynatrace API.")

Все endpoints со списками используют курсорную пагинацию через `nextPageKey`. Курсор появляется в ответе, когда существуют дополнительные страницы; передайте его как query-параметр `nextPageKey`, чтобы получить следующую страницу.

**Важно:** когда задан `nextPageKey`, все остальные query-параметры должны быть опущены. Фильтры, schema IDs, scopes и проекции полей применяются только к запросу первой страницы и кодируются в курсор для последующих страниц.

### Пакетная запись

[Создать объект](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создание или валидация settings object через Dynatrace API.") принимает массив объектов в одном запросе. API обрабатывает каждый объект в пакете независимо и возвращает его собственный HTTP-код состояния в теле ответа; проверяйте коды по элементам, а не полагайтесь на статус ответа верхнего уровня. Частично сбойный пакет не откатывает успешные элементы.

### Разреженные наборы полей (параметр `fields`)

Query-параметр `fields` позволяет ограничить, какие поля верхнего уровня возвращаются в ответе. Когда он указан, он полностью заменяет набор полей по умолчанию: он не аддитивный. Если вы укажете `fields=objectId,value`, вы получите только эти два поля; любые другие поля из набора по умолчанию (такие как `scope` или `schemaId`) исключаются.

Ответы по умолчанию не включают `updateToken`. Если он вам нужен для оптимистичной блокировки, запросите его явно: `fields=objectId,value,scope,updateToken`.

### Свойства типа secret

**Релевантный endpoint:** [Редактировать объект](/managed/dynatrace-api/environment-api/settings/objects/put-object "Редактирование settings object через Dynatrace API.")

API маскирует свойства типа `secret` в ответах `GET`. При `PUT` вы можете либо отправить значение в открытом виде, чтобы обновить secret, либо отправить обратно маскированное значение, чтобы оставить его без изменений: если только schema не ограничивает это для конкретных не-secret свойств.

Некоторые определения не-secret свойств несут поле `forceSecretResubmission`. Когда `forceSecretResubmission: true`, вы не можете обновить это не-secret свойство, сохраняя secrets маскированными: API требует, чтобы вы предоставили значения в открытом виде для всех secret-свойств в той же schema вместе с этим изменением.

Это ограничение закрывает потенциальный вектор эксфильтрации. Рассмотрим schema, которая хранит и secret (например, API-ключ), и URL назначения. Без `forceSecretResubmission: true` у свойства URL атакующий с правом записи мог бы изменить только URL на сервер, который он контролирует, оставив secrets маскированными: сервер тихо повторно использовал бы сохранённое значение в открытом виде при следующем вызове API, переправляя учётные данные атакующему. Требуя повторной отправки secret при изменении URL, schema гарантирует, что вызывающая сторона уже знает secrets, прежде чем сможет отправить валидное обновление.

Для не-secret свойств, где `forceSecretResubmission` отсутствует или равно `false`, вы можете обновлять их свободно, отправляя обратно маскированные значения для secret-свойств. Чтобы проверить, несёт ли конкретное не-secret свойство это ограничение, изучите его определение в schema.

### Пробная валидация (`validateOnly`)

**Релевантные endpoints:** [Создать объект](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создание или валидация settings object через Dynatrace API."), [Редактировать объект](/managed/dynatrace-api/environment-api/settings/objects/put-object "Редактирование settings object через Dynatrace API.")

Установка `validateOnly=true` запускает полную валидацию отправленных объектов на стороне сервера без сохранения чего-либо. Используйте это для проверки корректности payload перед фиксацией записи, особенно при работе с незнакомыми schemas.

### Управление доступом на основе владельца

Некоторые schemas включают управление доступом на основе владельца (`ownerBasedAccessControl: true` в определении schema). Для объектов под такими schemas создатель становится владельцем и может управлять детальными правами на чтение/запись для каждого пользователя или группы через под-ресурс `/settings/objects/{objectId}/permissions`. Не-владельцы с scope на запись всё ещё могут изменять значение объекта, но не могут изменять права.

Query-параметр `adminAccess`, доступный почти на всех endpoints, позволяет вызывающей стороне с правом `settings:objects:admin` обойти ограничения владения и действовать как фактический владелец любого объекта.

## Сценарии использования

* **Аудит состояния конфигурации**: Используйте [Список объектов](/managed/dynatrace-api/environment-api/settings/objects/get-objects "Просмотр нескольких settings objects через Dynatrace API."), чтобы получить только явно сохранённые значения для данной комбинации schema и scope.
* **Получить активную конфигурацию**: Используйте [Просмотр фактических значений](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "Просмотр фактической конфигурации для settings schema через Dynatrace API."), чтобы получить значение, действующее в данный момент, включая значения по умолчанию из schema и значения, унаследованные от родительских scopes.
* **Upsert без дублирования**: Назначьте `externalId` в [Создать объект](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создание или валидация settings object через Dynatrace API."), чтобы заменить существующий объект, а не создать дубликат.
* **Предотвратить конфликтующие обновления**: Включайте `updateToken` в запросы записи и удаления, чтобы обнаруживать и отклонять устаревшие изменения от параллельных модификаций.
* **Тест перед сохранением**: Используйте `validateOnly=true` в запросах записи, чтобы запустить полную валидацию на стороне сервера без фиксации каких-либо изменений.
* **Эффективно применять массовые изменения**: Отправляйте несколько объектов в одном запросе [Создать объект](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создание или валидация settings object через Dynatrace API.") вместо отправки одного запроса на объект.