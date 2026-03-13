---
title: Azure SCIM configuration for Dynatrace
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure
scraped: 2026-03-06T21:33:48.651906
---

# Настройка Azure SCIM для Dynatrace

# Настройка Azure SCIM для Dynatrace

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Aug 06, 2024

На этой странице описывается настройка на стороне IdP (**Azure**) для конфигурации SSO с использованием **SCIM**, а не на стороне Dynatrace. Используйте данное руководство как часть полной [процедуры настройки SCIM](../access-scim.md "SCIM") для Dynatrace SaaS, если вы используете Azure.

Мы делаем всё возможное, чтобы предоставить вам актуальную информацию, однако Dynatrace не контролирует изменения, которые могут быть внесены сторонними поставщиками. Всегда обращайтесь к официальной документации вашего IdP как к основному источнику информации по сторонним продуктам.

Для настройки SCIM для вашего домена

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание приложения SCIM в Azure**](scim-azure.md#create-scim-app "Learn how to configure Dynatrace SCIM in Azure.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Настройка провизионирования**](scim-azure.md#provisioning "Learn how to configure Dynatrace SCIM in Azure.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Настройка сопоставления групп**](scim-azure.md#configure-group-mappings "Learn how to configure Dynatrace SCIM in Azure.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Настройка сопоставления пользователей**](scim-azure.md#configure-user-mappings "Learn how to configure Dynatrace SCIM in Azure.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Назначение пользователей и групп**](scim-azure.md#assign-users-and-groups "Learn how to configure Dynatrace SCIM in Azure.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Включение SCIM**](scim-azure.md#enable-scim "Learn how to configure Dynatrace SCIM in Azure.")

## Шаг 1. Создание приложения SCIM в Azure

В **Microsoft Entra ID**

1. В левом меню выберите **Manage** > **Enterprise applications**.
2. Выберите **New application** > **Create your own application**.
3. Во всплывающем окне справа введите **Input name** для вашего приложения.

   Убедитесь, что выбран вариант **Integrate any other application you don't find in the gallery (Non-gallery)**.
4. Выберите **Create**.

## Шаг 2. Настройка провизионирования

Для настройки провизионирования в Azure вам потребуются базовый URL-адрес Dynatrace SCIM и секретный токен, полученные в процедуре [Получение конечной точки Dynatrace SCIM и создание секретного токена](../access-scim.md#scim-endpoint-secret-token "SCIM").

В **Microsoft Entra ID** с выбранным приложением

1. Если вы уже находитесь на странице **Overview** приложения, выберите **3. Provision User Accounts** в разделе **Getting Started**.

   Либо в левом меню выберите **Manage** > **Provisioning**.
2. Если вы делаете это впервые, выберите **Get started**.
3. В **Provisioning Mode** выберите **Automatic**.
4. Разверните **Admin Credentials**.
5. Введите учётные данные администратора:

   * **Tenant URL**
     Пример: `https://api.sso.dynatrace.com/idm/public/scim/<YOUR_ACCOUNT_ID>/v2`
   * **Secret Token**
     Этот токен вы получили из Dynatrace.
6. Выберите **Test Connection**, чтобы проверить конечную точку и учётные данные.
7. Если тест пройден успешно, выберите **Save** в верхнем левом углу страницы для генерации сопоставлений.

   Если тест не пройден, проверьте настройки:

   * **Tenant URL**
     Пример: `https://api.sso.dynatrace.com/idm/public/scim/<YOUR_ACCOUNT_ID>/v2`
   * **Secret Token**
     Вы создали его ранее в процедуре [Получение секретного токена](../access-scim.md#scim-endpoint-secret-token "SCIM").

## Шаг 3 (необязательный). Настройка сопоставления групп

Выполните этот шаг, если вам нужно провизионировать только определённые группы в Dynatrace.

В **Microsoft Entra ID** с выбранным приложением

1. На странице **Provisioning** разверните **Mappings**.
2. Выберите **Synchronize Azure Active Directory Groups to customappsso**.

   Убедитесь, что переключатель **Enabled** установлен в положение **Yes**.
3. В **Source Object Scope** выберите **All records**.
4. Выберите **Add new filter group**.
5. Заполните поля.
6. Выберите **Apply** в нижнем левом углу.
7. Вы можете оставить все **Target Object Actions** выбранными.
   Dynatrace SCIM поддерживает все эти действия.
8. Настройте **Attribute Mappings** следующим образом:
9. Выберите **Save** на странице **Attribute Mapping**.

## Шаг 4. Настройка сопоставления пользователей

Необходимо ограничить область пользователей, провизионируемых через SCIM, только теми, чьи домены электронной почты совпадают, чтобы ваши SCIM-запросы не были отклонены.

Для создания правила фильтрации пользователей

1. На странице **Provisioning** разверните **Mappings**.
2. Выберите **Synchronize Azure Active Directory Users to customappsso**.
3. Выберите ваш **Source Object Scope**.
4. Выберите **Add new filter group**.
5. В **Add Scoping Filter** заполните поля следующим образом:

   * Source Attribute: `mail`
   * Operator: `ENDS_WITH`
   * Clause value: `@<YOUR_DOMAIN>` (например, `@example.com`)

   Имейте в виду, что поддомены должны быть верифицированы для учётной записи отдельно. Поэтому символ `@` в строке домена обязателен и гарантирует, что ваши запросы не будут отклонены из-за недействительного домена пользователя.
6. Выберите **Apply** в нижнем левом углу.
7. Вы можете оставить все **Target Object Actions** выбранными.
   Dynatrace SCIM поддерживает все эти действия.
8. Ограничьте **Attribute Mappings** следующими:
9. Выберите **Show advanced options** в **Attribute Mappings**, затем выберите **Edit attribute list for customappsso**.
10. Убедитесь, что отмечены следующие флажки.

    * Для **id** — выберите **Primary Key?** и **Required?**
    * Для **userName** — выберите **Required?**
11. Выберите **Save** на странице **Edit Attribute List**.
12. Выберите **Save** на странице **Attribute Mapping**.

## Шаг 5. Назначение пользователей и групп

Чтобы назначить пользователей или группы вашему приложению и отправить их через SCIM в Dynatrace, в **Microsoft Entra ID**

1. Если вы уже находитесь на странице **Overview** приложения, выберите **1. Assign users and groups** в разделе **Getting Started**.

   Либо в левом меню выберите **Manage** > **Users**.
2. Выберите **Add user/group**.
3. Выберите **Users and groups**, которые вы хотите синхронизировать.
4. Выберите **Assign**.

## Шаг 6. Включение SCIM

Для включения провизионирования SCIM

1. Перейдите на страницу **Provisioning** и разверните **Settings**.
2. В списке **Scope** выберите **Sync only assigned users and groups**.
3. Включите **Provisioning Status**.

В Azure начальная синхронизация занимает больше времени, чем последующие, которые выполняются приблизительно каждые 40 минут, пока служба запущена.

## Устранение неполадок

Я случайно удалил синхронизированного через SCIM пользователя в Dynatrace в моей учётной записи. Можно ли повторно синхронизировать пользователя через SCIM в Azure?

Да, вы можете перезапустить синхронизацию SCIM. Для этого перейдите на вкладку **Overview** приложения SCIM и выберите **Restart provisioning**.