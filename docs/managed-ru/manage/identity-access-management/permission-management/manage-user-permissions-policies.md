---
title: Работа с политиками
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies
scraped: 2026-05-12T11:10:07.961637
---

# Работа с политиками

# Работа с политиками

* Explanation
* 9-min read
* Updated on Aug 20, 2025

Используйте управление идентификацией и доступом Dynatrace (IAM) для управления доступом пользователей к функциям Dynatrace.

Фреймворк IAM позволяет определять политики, которые чётко указывают, разрешено ли то или иное действие в Dynatrace. Когда политики привязываются к группам пользователей, они описывают паттерн доступа для группы, применяемый во время выполнения. Это обеспечивает значительно более детальный контроль над тем, как пользователи взаимодействуют с Dynatrace.

## Базовый уровень

[### Управление политиками IAM

Просматривайте, создавайте, удаляйте и копируйте политики в Account Management.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Создание, редактирование, копирование и удаление политик IAM для управления разрешениями пользователей Dynatrace.")[### Создание политик

Ознакомьтесь с синтаксисом операторов политик и примерами пользовательских политик.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "Синтаксис операторов политик IAM.")

## Расширенный уровень

[### Глобальные условия

Глобальные условия можно применять к любому оператору политики, поскольку они не привязаны к конкретному сервису.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-conditions "Глобальные условия политик")[### Глобальные атрибуты

Применяйте атрибуты к определённым глобальным условиям — их можно использовать в синтаксисе политик без дополнительной настройки.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-attributes "Глобальные атрибуты политик")[### Миграция разрешений на основе ролей

Политики безопасности Dynatrace теперь поддерживают классические разрешения на основе ролей — узнайте, как их перенести.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles "Управление доступом к среде Dynatrace с помощью политик безопасности.")

## Справочник

[### Справочник разрешений IAM

Полный список всех поддерживаемых разрешений IAM для всех сервисов Dynatrace.](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace.")