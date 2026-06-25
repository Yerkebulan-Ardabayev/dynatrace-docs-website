---
title: Предоставление доступа к настройкам
source: https://docs.dynatrace.com/managed/manage/identity-access-management/use-cases/access-settings
scraped: 2026-05-12T11:24:30.055105
---

# Предоставление доступа к настройкам

# Предоставление доступа к настройкам

* Tutorial
* 11-min read
* Updated on Oct 31, 2025

В этой статье описывается, как управлять доступом пользователей к настройкам Dynatrace глобально или на уровне отдельной схемы настроек.

Все примеры в статье основаны на сервисе [`Settings 2.0`](/managed/manage/settings/settings-20 "Введение в фреймворк Settings 2.0"). Полный список сервисов, поддерживающих авторизацию на основе политик, см. в разделе [Справочник политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace.").

## Для кого предназначена эта статья

Статья предназначена для администраторов учётных записей Dynatrace, которым необходимо предоставить пользователям доступ к настройкам Dynatrace. Она также будет полезна новым пользователям Dynatrace, желающим разобраться в разрешениях на основе групп.

## Что вы узнаете

В этой статье вы узнаете, как:

* Проверять встроенные политики для администраторов учётных записей.
* Получать доступ к функциям IAM через REST API с помощью OAuth2-клиента.
* Управлять разрешениями на чтение и запись, а также предоставлять доступ к определённой схеме.

## Перед началом работы

Предварительные знания

* [Управление учётными записями](/managed/manage/account-management "Управление лицензией Dynatrace, учётными записями, внедрением платформы и работоспособностью среды.")
* [Фреймворк настроек Dynatrace](/managed/manage/settings/settings-20 "Введение в фреймворк Settings 2.0")

Предварительные условия

* Учётная запись Dynatrace с правами администратора.
* Заранее настроенные пользователи, федерации и группы пользователей.

Ключевые термины

Settings 2.0
:   Унифицированный фреймворк для управления конфигурациями через объекты настроек, определяемые схемами Dynatrace.

Схема настроек (Settings Schema)
:   Конкретная структура конфигурации в Settings 2.0; разрешения могут предоставляться на уровне отдельной схемы для чтения или записи.

REST API точки администрирования политик (PAP REST API)
:   API для управления политиками IAM, включая создание политик и их привязку к группам.

Проверка доступных политик для администраторов

Для каждой учётной записи администраторам доступны две встроенные политики для сервисов `Settings 2.0`:

* `Settings Reader`: предоставляет разрешение на чтение настроек Dynatrace
* `Settings Writer`: предоставляет разрешение на запись настроек Dynatrace

Чтобы проверить наличие этих политик

1. В Cluster Management Console перейдите в **User authentication** > **Policy management**.
2. Найдите политики `Settings Reader` и `Settings Writer` в таблице.

Аутентификация запроса к REST API

Доступ ко всем функциям IAM можно получить через REST API. Здесь рассматриваются аспекты аутентификации API-запросов.

В развёртываниях Dynatrace Managed для PAP REST API используется аутентификация на основе токенов.

Чтобы сгенерировать токен

1. В Cluster Management Console перейдите в **Settings** > **API tokens**.
2. В разделе **Cluster tokens** выберите **Generate token**.

   * Введите любое имя токена
   * Включите **Service provider API**
3. Нажмите **Save**.
4. Нажмите **Copy**, чтобы скопировать токен.
5. Добавьте заголовок `Authorization` к запросу со значением `Api-Token [сгенерированный токен]`.

## Примеры сценариев

### Пример 1: разрешения на чтение и запись

Предположим, в вашей организации есть следующие команды:

* Команда `IT`: отвечает за настройку среды Dynatrace и обеспечение её бесперебойной работы.
* Команда `Sales`: должна только просматривать настройки, но никогда не изменять их.

Команде IT необходим доступ на чтение и запись, а команде Sales — только на чтение.

#### Создание двух групп пользователей Dynatrace

Политики в примерах на этой странице демонстрируют механику фреймворка политик и предоставляют доступ только к сервису настроек. Они открывают API-доступ к сервису настроек, но не обеспечивают доступ к веб-интерфейсу Dynatrace.

Сначала создайте группу `IT` с политиками `Settings Writer` и `Settings Reader`.

Чтобы создать группу

1. В Cluster Management Console перейдите в **User authentication** > **User groups**.
2. Нажмите **Add new group**.
3. Введите **Group name** (`IT` в данном примере) и **Group description**, затем нажмите **Save**.

Чтобы привязать политики к группе

1. В Cluster Management Console перейдите в **User authentication** > **User groups**.
2. Найдите группу `IT` и щёлкните значок карандаша в столбце **Edit** для редактирования группы.  
   Форма редактирования содержит раздел **Environment permissions** со списком всех управляемых вами окружений.
3. Раскройте нужное окружение и перейдите на вкладку **Policies**.
4. В поле фильтра **Select policies to bind**:

   * Найдите и выберите политику `Settings Writer`
   * Найдите и выберите политику `Settings Reader`
5. Нажмите кнопку **Bind policies** справа для привязки политик.
6. Нажмите **Save**.

Повторите описанную процедуру для создания группы `Sales` с доступом только на чтение.

1. Укажите имя группы `Sales`.
2. Привяжите к группе только политику `Settings Reader`, так как команде Sales не нужен доступ на запись настроек Dynatrace.

#### Привязка политик через веб-интерфейс

Чтобы привязать политики к группе

1. В Cluster Management Console перейдите в **User authentication** > **User groups**.
2. Найдите группу `IT` и щёлкните значок карандаша в столбце **Edit** для редактирования группы.  
   Форма редактирования содержит раздел **Environment permissions** со списком всех управляемых вами окружений.
3. Раскройте нужное окружение и перейдите на вкладку **Policies**.
4. В поле фильтра **Select policies to bind**:

   * Найдите и выберите политику `Settings Writer`
   * Найдите и выберите политику `Settings Reader`
5. Нажмите кнопку **Bind policies** справа для привязки политик.
6. Нажмите **Save**.

### Пример 2: предоставление доступа к определённой схеме

Добавив условие к политике, можно получить более детальный контроль.

Если встроенных политик недостаточно для ваших задач, можно управлять разрешениями на уровне отдельных настроек.

Предположим, у вас есть определённая схема `Settings 2.0`, например `settings.apm.my-super-secret-schema`, и вы хотите открыть доступ к ней только для групп `Sales` и `IT`.

Вы хотите разрешить:

* Чтение схемы `settings.apm.my-super-secret-schema`
* Чтение и запись объектов, принадлежащих схеме `settings.apm.my-super-secret-schema`

Существует два способа предоставить доступ к схеме.

1. Создать политику через веб-интерфейс Dynatrace.
2. Создать политику через REST API.

#### Создание политики через веб-интерфейс Dynatrace

В этой процедуре используется веб-интерфейс Dynatrace. Для использования REST API см. раздел [Создание политики через REST API](#create-policy-rest-api).

Чтобы создать политику:

1. В Cluster Management Console перейдите в **User authentication** > **Policy management**.
2. Нажмите **Add policy**.
3. Заполните сведения о политике:

   * **Policy name**  
     Введите понятное имя.
   * **Policy description**  
     Добавьте содержательное описание.
   * **Policy statements**  
     Скопируйте следующий оператор в поле **Policy statements**.

     ```
     ALLOW settings:schemas:read WHERE settings:schemaId = "builtin:container.monitoring-rule";



     ALLOW settings:objects:read WHERE settings:schemaId = "builtin:container.monitoring-rule";



     ALLOW settings:objects:write WHERE settings:schemaId = "builtin:container.monitoring-rule";
     ```

     Поскольку в одном операторе можно использовать несколько разрешений, первые два оператора можно объединить в один:

     ```
     ALLOW settings:schemas:read, settings:objects:read WHERE settings:schemaId = "builtin:container.monitoring-rule";



     ALLOW settings:objects:write WHERE settings:schemaId = "builtin:container.monitoring-rule";
     ```
4. Нажмите **Save**.

Политика добавляется в таблицу политик, которые можно привязывать к группам.

#### Создание политики через REST API

В этой процедуре с помощью REST API выполняются те же задачи, что и в разделе [Создание политики через веб-интерфейс Dynatrace](#create-policy-web-ui).

Для создания политики используется конечная точка `/repo/{level-type}/{level-id}/policies` с методом POST.

Предположим, имя добавляемой политики — `my_policy_name`, а описание — `My policy description`. Как и прежде, предположим, что политику необходимо применить только на уровне окружения для окружения `my_tenant_id`.

Тело запроса должно быть следующим:

```
{



"name":"my_policy_name",



"description":"My policy description",



"tags":[



],



"statementQuery": "ALLOW settings:schemas:read WHERE settings:schemaId = \"builtin:container.monitoring-rule\"; ALLOW settings:objects:read WHERE settings:schemaId = \"builtin:container.monitoring-rule\"; ALLOW settings:objects:write WHERE settings:schemaId = \"builtin:container.monitoring-rule\";"



}
```

При использовании нескольких разрешений в одном операторе тело запроса должно быть следующим:

```
{



"name":"my_policy_name",



"description":"My policy description",



"tags":[



],



"statementQuery": "ALLOW settings:schemas:read, settings:objects:read WHERE settings:schemaId = \"builtin:container.monitoring-rule\"; ALLOW settings:objects:write WHERE settings:schemaId = \"builtin:container.monitoring-rule\";"



}
```

### Применение политики

**Важно:** политика не вступает в силу до тех пор, пока она не привязана к группе. Необходимо привязать этот пример к группам `IT` и `Sales`. Подробнее см. в разделах [Привязка политик через веб-интерфейс Dynatrace](#bind-web-ui) или [Привязка политик через REST API](#bind-api).

## Связанные разделы

* [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте о возможностях Dynatrace Settings API.")
* [OAuth-клиенты](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.")
* [Фреймворк настроек Dynatrace](/managed/manage/settings/settings-20 "Введение в фреймворк Settings 2.0")
* [Синтаксис и примеры операторов политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "Синтаксис операторов политик IAM.")