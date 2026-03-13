---
title: Overview of Dynatrace IAM
source: https://www.dynatrace.com/docs/manage/identity-access-management/iam-concepts
scraped: 2026-03-06T21:31:44.586811
---

# Обзор управления идентификацией и доступом (IAM) в Dynatrace

# Обзор управления идентификацией и доступом (IAM) в Dynatrace

* Последняя версия Dynatrace
* Обзор
* Время чтения: 2 мин
* Обновлено 18 июня 2025 г.

В этом руководстве описаны ключевые компоненты управления идентификацией и доступом (IAM) в Dynatrace: управление пользователями и группами, модели доступа, поставщики удостоверений, политики доступа и токены доступа. Эти компоненты обеспечивают безопасное взаимодействие, эффективную автоматизацию и бесшовную интеграцию внутри платформы.

## Управление идентификацией

Управляйте операциями жизненного цикла пользователей и групп и внедряйте автоматизированную аутентификацию с помощью поставщиков удостоверений (IdP).

[![Concepts](https://dt-cdn.net/images/concept-6e215a8350.svg "Concepts")

### Концепции

Ознакомьтесь с типами пользователей IAM, федерацией удостоверений и репозиториями пользователей.](user-and-group-management/identity-concepts.md "Понимание ключевых концепций идентификации в Dynatrace IAM")[### Локальные пользователи

Dynatrace выступает в качестве вашего хранилища удостоверений.](user-and-group-management/identity-concepts.md#users "Понимание ключевых концепций идентификации в Dynatrace IAM")[### Сервисные пользователи

Нечеловеческие удостоверения, взаимодействующие с сервисами и ресурсами.](user-and-group-management/identity-concepts.md#service-users "Понимание ключевых концепций идентификации в Dynatrace IAM")[### Федерация SAML

Делегирование аутентификации через ваш IdP.](user-and-group-management/access-saml.md "SAML")[### SCIM

Синхронизация репозиториев удостоверений.](user-and-group-management/access-scim.md "SCIM")

## Управление доступом

Определяйте детализированный доступ пользователей в Dynatrace, контролируя разрешения для защиты конфиденциальных данных и ресурсов.

[![Concepts](https://dt-cdn.net/images/concept-6e215a8350.svg "Concepts")

### Концепции

Ознакомьтесь с тем, как Dynatrace управляет группами и политиками.](permission-management/access-concepts.md "Понимание ключевых концепций доступа в Dynatrace IAM")[### Группы

Централизованное управление конфигурациями доступа.](permission-management/access-concepts.md#groups "Понимание ключевых концепций доступа в Dynatrace IAM")[### Политики

Определение настраиваемых разрешений для доступа к ресурсам.](permission-management/access-concepts.md#policies "Понимание ключевых концепций доступа в Dynatrace IAM")[### Границы политик

Масштабирование, уточнение и упрощение разрешений доступа.](permission-management/access-concepts.md#policy-boundaries "Понимание ключевых концепций доступа в Dynatrace IAM")[### Шаблоны политик

Многократно используемые политики для регулирования управления доступом.](permission-management/access-concepts.md#policy-templates "Понимание ключевых концепций доступа в Dynatrace IAM")[### Политики по умолчанию

Начните работу с политиками Dynatrace по умолчанию.](permission-management/default-policies.md "Справочник по политикам Dynatrace по умолчанию")[### Группы по умолчанию

Начните работу с группами Dynatrace по умолчанию.](user-and-group-management/default-groups.md "Справочник по группам Dynatrace по умолчанию")

## Токены и OAuth-клиенты

Внешний доступ к Dynatrace и его автоматизация с помощью защищённых токенов.

[![Concepts](https://dt-cdn.net/images/concept-6e215a8350.svg "Concepts")

### Концепции

Ознакомьтесь с тем, как Dynatrace обрабатывает API-токены и автоматизацию доступа.](access-tokens-and-oauth-clients/token-concepts.md "Понимание ключевых аспектов доступа к API и автоматизации в Dynatrace IAM")[### Токены платформы

Разрешение взаимодействия с платформой Dynatrace.](access-tokens-and-oauth-clients/platform-tokens.md "Создание персональных токенов платформы для доступа к сервисам Dynatrace через API в контексте вашего пользователя.")[### OAuth-токены

Доступ к Dynatrace через OAuth-клиенты.](access-tokens-and-oauth-clients/oauth-clients.md "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.")
