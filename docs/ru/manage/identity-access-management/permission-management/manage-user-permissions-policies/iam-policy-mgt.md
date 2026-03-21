---
title: Управление политиками IAM
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt
scraped: 2026-03-06T21:15:30.427207
---

Используйте описанные здесь процедуры в веб-интерфейсе Dynatrace для управления политиками [IAM](../manage-user-permissions-policies.md "Working with policies") Dynatrace.

Альтернатива через API

Если вы предпочитаете управлять политиками IAM через API, перейдите в [Dynatrace Account Management API 1.0](https://dt-url.net/vr03thr).

## Просмотр списка политик IAM

Для просмотра настроенных политик IAM

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Просмотрите таблицу со всеми существующими политиками, которые можно привязать к группам пользователей.

   * **Name** — название политики
   * **Description** — краткое описание политики
   * **Source** — `global`, `account` или `environment`
   * **Actions** — просмотр, редактирование или удаление политики в данной строке (доступные действия зависят от вашего уровня разрешений)

### Политики по умолчанию

Чтобы вы могли сразу приступить к работе с политиками, Dynatrace IAM поставляется со встроенными глобальными политиками.

* На странице **Policies** в столбце **Source** для всех них установлено значение `Dynatrace`
* Они предопределены и управляются Dynatrace
* Вы можете применить встроенную политику, [назначив её группе](../manage-user-permissions-policies.md "Working with policies") для всей учётной записи или для любой среды.
* Вы можете просматривать их — выберите **View policy** в столбце **Actions** — но не можете редактировать

## Создание политики

Для создания политики

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Нажмите **Create policy**.
3. Введите следующие сведения.

### Сервисы

Полный и актуальный список сервисов Dynatrace, поддерживающих управление разрешениями через политики IAM, см. в разделе [Справочник по политикам IAM](advanced/iam-policystatements.md "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Редактирование политики

Для редактирования существующей политики

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Найдите политику, которую хотите отредактировать.
   Вы можете фильтровать и сортировать таблицу.
3. Выберите **Actions** > **Edit policy**.
4. Внесите изменения и нажмите **Save**.

## Удаление политики

Для удаления политики

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Найдите политику, которую хотите удалить.
   Вы можете фильтровать и сортировать таблицу.
3. Нажмите **Actions** > **Delete** для данной политики.

## Копирование политики

Для копирования существующей политики

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Найдите политику, которую хотите скопировать.
   Вы можете фильтровать и сортировать таблицу.
3. Нажмите кнопку **Edit** для данной политики.
4. Скопируйте содержимое поля **Policy statement** в буфер обмена.
5. Вернитесь на страницу **Policies**.
6. Нажмите **Create policy**.
7. Вставьте скопированные операторы политики в поле **Policy statement**.
8. Заполните поля **Name** и необязательное **Description**.
9. Нажмите **Create policy**.

## Применение политики к группе

Чтобы применить политику к группе, необходимо привязать политику к этой группе. Подробности об управлении разрешениями групп с помощью IAM см. в разделе [Работа с политиками](../manage-user-permissions-policies.md "Working with policies").
