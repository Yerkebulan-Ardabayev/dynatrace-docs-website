---
title: Settings API key concepts
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/key-concepts
---

# Settings API key concepts

# Settings API key concepts

* Пояснение
* Обновлено 26 марта 2026 г.

Settings API предоставляет иерархию объектов конфигурации, организованных по схеме и scope. Прежде чем начать работу с ней в промышленных масштабах, нужно понять, как API сохраняет объекты, как значения распространяются по иерархии scope и как API управляет конкурентным доступом, пагинацией и контролем доступа.

## Обзор

Схемы определяют объекты настроек; scope задаёт уровень, на котором применяется конфигурация. Каждая схема описывает структуру и ограничения типа конфигурации. API предоставляет отдельные endpoint'ы для чтения в зависимости от того, нужны ли явно сохранённые значения или те, что реально действуют.

### Схемы

**Соответствующие endpoint'ы:** [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API."), [View a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.")

Схема определяет структуру объекта настроек: его свойства, типы и ограничения, а также поведенческие атрибуты, такие как `multiObject`, `ordered` и `maxObjects`. Каждый читаемый или записываемый объект настроек ссылается на схему по `schemaId`.

* Используйте [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API."), чтобы узнать, какие схемы доступны в вашей среде.
* Используйте [View a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API."), чтобы изучить определения свойств конкретной схемы перед формированием payload. Это особенно полезно для понимания обязательных полей, перечислений и свойств типа secret.

`schemaId`, полученный из endpoint'ов схем, передаётся в параметре `schemaId` при чтении или записи объектов через [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API."), [Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") и другие object-endpoint'ы.

### Сохранённые объекты и действующие значения

API предоставляет два различных представления данных настроек:

* [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") возвращает только явно сохранённые объекты на запрошенных scope. Если для заданной комбинации схема/scope ничего не записано, ответ будет пустым.
* [View effective values](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "View an actual configuration for a settings schema via the Dynatrace API.") оценивает полную иерархию конфигурации: проходит по дереву scope вверх и применяет значения по умолчанию из схемы там, где явное значение отсутствует. Этот endpoint всегда возвращает результат для допустимой комбинации схема/scope, даже если объект никогда не сохранялся.

Используйте [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API."), когда нужно управлять или проверять состояние конфигурации. Используйте [View effective values](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "View an actual configuration for a settings schema via the Dynatrace API."), когда нужно значение, фактически действующее для заданного scope.

### Схемы с одним значением и схемы с несколькими значениями

Схемы настроек бывают двух видов, определяемых свойством `multiObject` в определении схемы:

* **С одним значением** (`multiObject: false`), на каждом scope существует не более одного объекта. Отсутствие объекта означает, что применяется значение по умолчанию из схемы или значение, установленное на родительском scope.
* **С несколькими значениями** (`multiObject: true`), на одном scope может одновременно существовать ноль и более объектов, но не более лимита, заданного `maxObjects`. Если свойство схемы `ordered` равно `true`, порядок элементов имеет семантическое значение; используйте `insertAfter` и `insertBefore` в запросах создания/обновления для управления позицией.

### Scope

Каждый объект настроек относится ровно к одному scope, который задаётся полем `scope` при создании. Фильтр `scopes` в [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") возвращает только объекты, непосредственно относящиеся к указанному scope; иерархия при этом не обходится. Например, фильтрация по `environment` не вернёт объекты, привязанные к хосту внутри этой среды.

### Внешние идентификаторы

**Соответствующие endpoint'ы:** [Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") (тело запроса), [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") (параметр запроса `externalIds`)

Поле `externalId` позволяет присвоить объекту настроек стабильный идентификатор, определяемый вызывающей стороной, при создании (максимум 500 символов). Это реализует **паттерн upsert**: если объект с указанным `externalId` уже существует на целевом scope, запрос заменяет его, а не создаёт дубликат. Также можно искать объекты по внешним идентификаторам с помощью параметра `externalIds` в [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.").

### Оптимистическая блокировка

**Соответствующие endpoint'ы:** [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API."), [View an object](/managed/dynatrace-api/environment-api/settings/objects/get-object "View a settings object via the Dynatrace API."), [Edit an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API."), [Delete an object](/managed/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.")

Поле `updateToken`, это механизм контроля конкурентного доступа. API генерирует его и возвращает с каждым запросом на получение данных. Если указать его в последующем запросе обновления или удаления, операция выполнится только при условии, что объект не изменился с момента последнего получения; если изменился, API отклонит запрос, чтобы можно было разрешить конфликт.

Если `updateToken` не указан в запросе записи или удаления, проверка пропускается и изменение применяется безусловно.

### Пагинация

**Соответствующие endpoint'ы:** [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API."), [View effective values](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "View an actual configuration for a settings schema via the Dynatrace API.")

Все list-endpoint'ы используют пагинацию на основе курсора через `nextPageKey`. Курсор появляется в ответе, когда есть ещё страницы; нужно передать его в параметре запроса `nextPageKey` для получения следующей страницы.

**Важно:** если `nextPageKey` задан, все остальные параметры запроса должны быть опущены. Фильтры, идентификаторы схем, scope и проекции полей применяются только к запросу первой страницы и кодируются в курсоре для последующих страниц.

### Пакетная запись

[Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") принимает массив объектов в одном запросе. API обрабатывает каждый объект пакета независимо и возвращает собственный HTTP-статус в теле ответа; нужно проверять коды для каждого элемента, а не полагаться на статус ответа верхнего уровня. Частичный сбой пакета не откатывает успешно обработанные элементы.

### Разреженные наборы полей (параметр `fields`)

Параметр запроса `fields` позволяет ограничить, какие поля верхнего уровня возвращаются в ответе. При наличии он полностью заменяет набор полей по умолчанию, а не дополняет его. Если указать `fields=objectId,value`, в ответе будут только эти два поля; любые другие поля из набора по умолчанию (такие как `scope` или `schemaId`) будут исключены.

По умолчанию ответы не включают `updateToken`. Если он нужен для оптимистической блокировки, запросите его явно: `fields=objectId,value,scope,updateToken`.

### Свойства типа secret

**Соответствующий endpoint:** [Edit an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.")

API маскирует свойства типа `secret` в ответах `GET`. При `PUT` можно либо передать значение в открытом виде, чтобы обновить секрет, либо вернуть маскированное значение, чтобы оставить его без изменений, если только схема не ограничивает это для конкретных несекретных свойств.

Некоторые определения несекретных свойств содержат поле `forceSecretResubmission`. При `forceSecretResubmission: true` нельзя обновить это несекретное свойство, оставив секреты маскированными: API требует передать значения в открытом виде для всех секретных свойств той же схемы вместе с этим изменением.

Это ограничение закрывает потенциальный вектор утечки данных. Рассмотрим схему, хранящую одновременно секрет (например, ключ API) и URL назначения. Без `forceSecretResubmission: true` на свойстве URL злоумышленник с правом на запись мог бы изменить только URL на подконтрольный ему сервер, оставив секреты маскированными: при следующем обращении к API сервер молча использовал бы сохранённый открытый текст, пересылая учётные данные атакующему. Требуя повторной передачи секретов при изменении URL, схема гарантирует, что вызывающая сторона уже знает секреты перед отправкой корректного обновления.

Для несекретных свойств, у которых `forceSecretResubmission` отсутствует или равно `false`, их можно обновлять свободно, возвращая маскированные значения для секретных свойств. Чтобы проверить, несёт ли конкретное несекретное свойство это ограничение, нужно изучить его определение в схеме.

### Валидация в режиме dry-run (`validateOnly`)

**Соответствующие endpoints:** [Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API."), [Edit an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.")

При `validateOnly=true` выполняется полная серверная валидация переданных объектов без сохранения чего-либо. Это позволяет проверить корректность payload перед фиксацией записи, особенно при работе с незнакомыми схемами.

### Контроль доступа на основе владельца

**Соответствующие endpoints:** [List object permissions](/managed/dynatrace-api/environment-api/settings/objects/get-permissions "View all permissions on a settings object via the Dynatrace API."), [Add accessor permission](/managed/dynatrace-api/environment-api/settings/objects/post-permission "Add permissions for a single accessor on a settings object via the Dynatrace API."), [Get accessor permission](/managed/dynatrace-api/environment-api/settings/objects/get-permission "View accessor permissions on a settings object via the Dynatrace API."), [Update accessor permission](/managed/dynatrace-api/environment-api/settings/objects/put-permission "Update accessor permissions on a settings object via the Dynatrace API."), [Delete accessor permission](/managed/dynatrace-api/environment-api/settings/objects/del-permission "Remove accessor permissions on a settings object via the Dynatrace API."), [Get all-users permission](/managed/dynatrace-api/environment-api/settings/objects/get-permission-all-users "View the all-users accessor permissions on a settings object via the Dynatrace API."), [Update all-users permission](/managed/dynatrace-api/environment-api/settings/objects/put-permission-all-users "Update the all-users accessor permissions on a settings object via the Dynatrace API."), [Delete all-users permission](/managed/dynatrace-api/environment-api/settings/objects/del-permission-all-users "Remove the all-users accessor permissions on a settings object via the Dynatrace API."), [Transfer ownership](/managed/dynatrace-api/environment-api/settings/objects/post-transfer-ownership "Transfer ownership of a settings object via the Dynatrace API.")

Некоторые схемы поддерживают контроль доступа на основе владельца. Выявить их можно, передав `ownerBasedAccessControl` в параметре `add-fields` при вызове [List schemas](/managed/dynatrace-api/environment-api/settings/schemas/get-all "View all settings schemas of your monitoring environment via the Dynatrace API."); схемы с `ownerBasedAccessControl: true` в ответе используют эту модель. Для объектов под такими схемами создатель становится владельцем, а объект по умолчанию является приватным: ни один другой пользователь или группа не имеют доступа до тех пор, пока владелец явно не предоставит его. Владелец управляет детализированными разрешениями через подресурс `/settings/objects/{objectId}/permissions`. Подресурс поддерживает два типа accessor:

* **Именованные accessor**: идентифицируются по `{accessorType}/{accessorId}` и представляют отдельного пользователя или группу. В качестве `accessor-id` нужно использовать UUID пользователя или группы; для поиска этих идентификаторов используется API управления пользователями или API управления группами.
* **Accessor all-users**, это подстановочный знак, который применяет уровень разрешений ко всем пользователям; управляется через выделенный подпуть `/permissions/all-users`.

Любой пользователь, обладающий разрешениями на чтение и запись на уровне объекта, может добавлять или обновлять разрешения на объекте. Только текущий владелец или пользователь с разрешением `settings:objects:admin` (глобально или для соответствующей схемы) может передавать владение. При передаче владения предыдущий владелец теряет доступ, если он явно не указан как accessor объекта.

Параметр запроса `adminAccess`, доступный почти на всех endpoints, позволяет обходить ограничения владения и действовать как эффективный владелец любого объекта при наличии разрешения `settings:objects:admin`. Обратите внимание, что `settings:objects:admin` не предоставляет доступ на чтение или запись объектов settings: по-прежнему необходимо иметь соответствующее разрешение `settings:objects:read` или `settings:objects:write` для успешного выполнения операции.

## Сценарии использования

* **Аудит состояния конфигурации**: используйте [List objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") для получения только явно сохранённых значений для заданной комбинации схемы и scope.
* **Получение активной конфигурации**: используйте [View effective values](/managed/dynatrace-api/environment-api/settings/objects/get-effective-values "View an actual configuration for a settings schema via the Dynatrace API.") для получения значения, действующего в данный момент, включая умолчания схемы и значения, унаследованные от родительских scope.
* **Upsert без дублирования**: назначьте `externalId` в [Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API."), чтобы заменить существующий объект вместо создания дубликата.
* **Предотвращение конфликтующих обновлений**: передавайте `updateToken` в запросах на запись и удаление для обнаружения и отклонения устаревших изменений при параллельных модификациях.
* **Тестирование перед сохранением**: используйте `validateOnly=true` в запросах на запись для выполнения полной серверной валидации без фиксации каких-либо изменений.
* **Эффективное применение массовых изменений**: передавайте несколько объектов в одном запросе [Create an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") вместо отдельного запроса на каждый объект.