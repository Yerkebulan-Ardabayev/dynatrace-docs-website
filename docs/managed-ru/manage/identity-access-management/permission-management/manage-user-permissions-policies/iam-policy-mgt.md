---
title: Управление политиками IAM
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt
scraped: 2026-05-12T11:49:53.325675
---

# Управление политиками IAM

# Управление политиками IAM

* How-to guide
* 7-min read
* Updated on Aug 20, 2025

Используйте эти процедуры в веб-интерфейсе Dynatrace для управления политиками [IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Работа с политиками") Dynatrace.

Альтернатива через API

Для управления политиками IAM через API перейдите в раздел [Cluster API v2](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Управление окружениями, сетевыми зонами, Synthetic-локациями, узлами и токенами в Dynatrace Managed с помощью Cluster API v2.").

## Просмотр политик IAM

Чтобы просмотреть настроенные политики IAM

1. В Cluster Management Console перейдите в **User authentication** > **Policy management**.
2. Просмотрите таблицу всех существующих политик, которые можно привязывать к группам пользователей.

   * **Policy** — имя политики
   * **Policy description** — краткое описание политики
   * **Organizational level** — `global`, `cluster` или `environment`
   * **Actions** — просмотр, редактирование или удаление политики в строке (доступные действия зависят от вашего уровня разрешений)

### Политики по умолчанию

Для немедленного начала работы с политиками IAM Dynatrace поставляется с набором встроенных глобальных политик.

* На странице **Policies** в столбце **Source** у них указано значение `Dynatrace`
* Они предопределены и управляются Dynatrace
* Встроенную политику можно применить, [назначив её группе](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Работа с политиками") для всей учётной записи или для любого окружения
* Их можно просматривать — выберите **View policy** в столбце **Actions** — но нельзя редактировать

## Создание политики

Чтобы создать политику

1. В Cluster Management Console перейдите в **User authentication** > **Policy management**.
2. Нажмите **Add policy**.
3. Введите следующие сведения.

   | Элемент | Описание |
   | --- | --- |
   | Policy name | Имя политики. |
   | Policy description | Краткое описание политики. |
   | Available for organizational level | Каждая политика имеет уровень, определяющий её область действия:  * `global`: глобальные политики предопределены и управляются Dynatrace; они применяются ко всем учётным записям и окружениям. Редактировать их нельзя. * `cluster`: политики учётной записи применяются ко всем окружениям в этой учётной записи (клиенте). Используйте их для установки корпоративных политик. * `environment`: политики окружения применяются только к одному клиентскому окружению.  В интерфейсе уровни организации ограничены уровнем `cluster` (другие уровни по-прежнему доступны через API). Это ограничение введено во избежание путаницы между *созданием* и *привязкой*. Создание нескольких идентичных политик на уровнях `environment` удобнее заменить определением одной политики на уровне `cluster` с последующей привязкой к уровням `environment`. |
   | Policy statements | Оператор, точно определяющий, что разрешает данная политика.  Пример: политика для Settings 2.0 Write  ```  ALLOW settings:objects:read;  ALLOW settings:objects:write;  ALLOW settings:schemas:read; ```  Несколько разрешений можно объединить в одном операторе. Тот же пример в виде единого оператора:  ```  ALLOW settings:objects:read, settings:objects:write, settings:schemas:read; ```  Объединение операторов особенно удобно для управления политиками со сложными условиями. |

### Сервисы

Полный и актуальный список сервисов Dynatrace, поддерживающих управление разрешениями через политики IAM, см. в [Справочнике политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace.").

## Редактирование политики

Чтобы изменить существующую политику

1. В Cluster Management Console перейдите в **User authentication** > **Policy management**.
2. Найдите политику, которую нужно изменить.  
   Таблицу можно фильтровать и сортировать.
3. Выберите **Actions** > **Edit policy**.
4. Внесите изменения и нажмите **Save**.

## Удаление политики

Чтобы удалить политику

1. В Cluster Management Console перейдите в **User authentication** > **Policy management**.
2. Найдите политику, которую нужно удалить.  
   Таблицу можно фильтровать и сортировать.
3. Нажмите кнопку **Edit** для этой политики.
4. Выберите **Delete policy**.

   Изменение вступит в силу через несколько минут.

   Чтобы изменить задержку, измените свойство `policyRefreshIntervalSeconds` в разделе `iam` конфигурационного файла.

## Копирование политики

Чтобы скопировать существующую политику

1. В Cluster Management Console перейдите в **User authentication** > **Policy management**.
2. Откройте существующую политику для редактирования.
3. Скопируйте содержимое поля **Policy statements** в буфер обмена.
4. Вернитесь на страницу **Policy management**.
5. Нажмите **Add policy**.
6. Вставьте скопированные операторы политики в поле **Policy statements**.
7. Заполните поля **Name** и необязательное **Description**.
8. Нажмите **Save**.

## Применение политики к группе

Чтобы применить политику к группе, необходимо привязать её к группе. Подробнее об управлении разрешениями группы с помощью IAM см. в разделе [Работа с политиками](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Работа с политиками").