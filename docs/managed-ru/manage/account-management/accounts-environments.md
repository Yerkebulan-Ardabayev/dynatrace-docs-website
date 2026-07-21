---
title: О лицензиях, аккаунтах, средах и пользователях Dynatrace
source: https://docs.dynatrace.com/managed/manage/account-management/accounts-environments
---

# О лицензиях, аккаунтах, средах и пользователях Dynatrace

# О лицензиях, аккаунтах, средах и пользователях Dynatrace

* Пояснение
* 2 минуты на чтение
* Опубликовано 16 марта 2026 г.

На этой странице описано, как Dynatrace работает с различными административными понятиями, организованными по иерархическим уровням.
Вот они, от самого общего к самому конкретному:

* Лицензия: одну лицензию могут использовать один или несколько аккаунтов.
* Аккаунт: у каждого аккаунта может быть одна или несколько сред.
* Environment: к каждой среде могут получить доступ один или несколько пользователей.
* Пользователь: вход в среду Dynatrace выполняется от имени пользователя.

Доступ к каждому из этих уровней регулируется правами доступа.
У каждого пользователя Dynatrace есть определённые права: одни пользователи могут иметь доступ только к данным в конкретных средах, другие, к данным на уровне аккаунта.

Использование рассчитывается на уровне среды.

## Что такое лицензия Dynatrace?

Лицензия Dynatrace Platform Subscription позволяет среде потреблять функции мониторинга Dynatrace.

В большинстве случаев ровно один аккаунт (через связанные с ним среды) потребляет ресурсы одной подписки.
С [DPS for Hybrid](/managed/license/dps-for-hybrid "DPS for Hybrid lets you share one subscription across multiple accounts."), в определённых случаях также возможно, чтобы несколько аккаунтов потребляли ресурсы одной подписки.

Администраторы аккаунта могут использовать **Account Management** для просмотра информации о лицензиях или подписках.
Подробнее см. [Subscription (DPS) or License (classic license)](/managed/manage/account-management/license-subscription "View your Dynatrace license information, including budgets, cost analysis, and historical usage, for all license models.").
Использование постоянно измеряется, можно отслеживать потребление, прогнозировать расходы и управлять бюджетами по средам и аккаунтам.

## Что такое аккаунт Dynatrace?

Аккаунт Dynatrace предоставляет единое место для управления лицензиями и подписками, пользователями и доступом через SSO.

Аккаунт может содержать одну или несколько сред, например `test`, `pre-prod` и `production`.

## Что такое среда Dynatrace?

Среда Dynatrace, это способ взаимодействия с функциями мониторинга Dynatrace.

* Вход выполняется в среду.
* Внутри среды можно просматривать данные мониторинга и оповещения.
* Запросы выполняются к данным, которые находятся в среде.

Каждая среда определяется уникальным ID, который можно найти как в интерфейсе Dynatrace, так и в URL.
Подробнее см. [ID Environment](/managed/discover-dynatrace/get-started/monitoring-environment#environment-id "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").
Пример ID среды: `abc12345`.

В Dynatrace использование рассчитывается на уровне среды.

Подробнее о том, как среда работает технически, см. [Что такое среда мониторинга?](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").

## Что такое пользователь Dynatrace?

Вход в среду Dynatrace выполняется от имени пользователя Dynatrace.

Права доступа предоставляются пользователям Dynatrace.
Права позволяют пользователям, например, администрировать аккаунты Dynatrace, настраивать развёртывания Dynatrace или выполнять запросы к данным Grail.

Права предоставляются либо на уровне аккаунта, либо на уровне среды.
Права на уровне аккаунта применяются ко всем средам этого аккаунта, а права на уровне среды, только к этой среде.

Подробнее о правах доступа см. [Identity and access management (IAM)](/managed/manage/identity-access-management "Configure users, groups and permissions.").

## Смежные темы

* [License Dynatrace](/managed/license "Dynatrace Platform Subscription, capability rate cards, hybrid licensing, and previous license models.")
* [Account Management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.")
* [Your license lifecycle](/managed/manage/account-management/accounts-environments/license-lifecycle "Understand your Dynatrace DPS or Classic license lifecycle, and how it affects your consumption of Dynatrace services.")
* [Access management](/managed/manage/identity-access-management/permission-management "Permission management")
* [User and group management](/managed/manage/identity-access-management/user-and-group-management "User and group management")