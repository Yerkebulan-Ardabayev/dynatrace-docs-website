---
title: Working with policies
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies
scraped: 2026-03-06T21:22:27.798228
---

# Работа с политиками

# Работа с политиками

* Latest Dynatrace
* Explanation
* 9-min read
* Updated on Aug 20, 2025

Используйте управление идентификацией и доступом Dynatrace (IAM) для управления доступом пользователей к функциям Dynatrace.

С помощью IAM-фреймворка вы можете определять политики, которые чётко указывают, разрешено ли то или иное действие в Dynatrace. Когда политики привязаны к группам пользователей, они описывают шаблон доступа для группы, который применяется во время выполнения. Это даёт вам значительно более детальный контроль над тем, как ваши пользователи взаимодействуют с Dynatrace.

## Основное

[### Управление IAM-политиками

Просматривайте, создавайте, удаляйте и копируйте политики с помощью Account Management.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.")[### Создание политик

Изучите синтаксис операторов политик и ознакомьтесь с примерами пользовательских политик.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")[### Границы политик

Границы позволяют дополнительно ограничивать политики.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.")

## Дополнительно

[### Глобальные условия

Глобальные условия можно применять к любому оператору политики, поскольку они не привязаны к конкретному сервису.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-conditions "Policy global conditions")[### Глобальные атрибуты

Применяйте атрибуты к определённым глобальным условиям, доступным в синтаксисе политик без дополнительной настройки.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-attributes "Policy global attributes")[### Миграция ролевых разрешений

Политики безопасности Dynatrace теперь поддерживают классические ролевые разрешения — узнайте, как их перенести.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles "Manage access to a Dynatrace environment using security policies.")

## Справочник

[### Справочник по IAM-разрешениям

Полный список всех поддерживаемых IAM-разрешений для всех сервисов Dynatrace.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.")[### API управления политиками

Управляйте политиками в масштабе с помощью API управления политиками.](/docs/dynatrace-api/account-management-api/policy-management-api/policies "Manage access policies in your Dynatrace account via the Policy management API.")
