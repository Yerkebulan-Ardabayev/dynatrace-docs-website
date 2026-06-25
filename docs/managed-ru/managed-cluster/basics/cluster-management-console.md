---
title: Cluster Management Console
source: https://docs.dynatrace.com/managed/managed-cluster/basics/cluster-management-console
scraped: 2026-05-12T11:08:41.103410
---

# Cluster Management Console

# Cluster Management Console

* Explanation
* 5-min read
* Updated on May 08, 2026

Cluster Management Console — это административный интерфейс Managed Cluster. Используйте его для управления инфраструктурой Managed Cluster и всеми размещёнными на нём средами. Cluster Management Console отделена от интерфейса среды мониторинга. Доступ к ней имеют только пользователи с правами администратора кластера.

![Cluster Management Console](https://dt-cdn.net/images/screenshot-2026-03-12-at-10-30-21-1837-e8bbf2f12e.png)

Cluster Management Console

## Home

**Home** отображает **обзор развёртывания Dynatrace Managed** с графическим представлением вашего развёртывания.

* [Environments](#environments) — отображает количество активных сред. Ссылка на [Environments](#environments).
* [ActiveGates](#deployment-status-ag) — отображает количество Cluster ActiveGate и Environment ActiveGate. Ссылка на [Deployment status](#deployment-status).
* [Cluster nodes](#deployment-status-cluster-nodes) — отображает количество узлов кластера.
* [Last backup](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.") — отображает дату и место хранения последней резервной копии.
* [Events](#events) — отображает количество событий в журнале.
* [Users](#user-authentication) — отображает количество пользователей и групп пользователей.
* [Dynatrace Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") — предоставляет доступ к проактивной поддержке Mission Control.

## Deployment status

**Deployment status** содержит обзор инфраструктуры кластера.

### Cluster nodes

* Для просмотра сведений об узле кластера разверните его строку.
* Для установки узла кластера выберите **Install cluster node** в правом верхнем углу.

### ActiveGates

* Для просмотра сведений об ActiveGate разверните его строку.
* Для установки Cluster ActiveGate выберите **Install Cluster ActiveGate** в правом верхнем углу.

### Network zones

* Для просмотра сведений о сетевой зоне выберите её имя в таблице.

## Environments

**Environments** отображает таблицу всех сред Dynatrace, которыми вы управляете.

* Для поиска среды используйте фильтры слева.
* Для открытия экрана сведений о среде выберите её имя.

  + Для изменения конкретного параметра среды выберите соответствующий параметр.  
    Разделы включают:

    - Настройки возможностей (Capability settings)
    - Настройки хранилища (Storage settings)
    - Настройки предотвращения перегрузки кластера (Cluster overload prevention settings)
    - Назначение разрешений среды группам пользователей
  + Для перехода в выбранную среду Dynatrace выберите **Go to environment** в правом верхнем углу.
  + Для отключения выбранной среды Dynatrace выберите ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Disable environment** в правом верхнем углу.
  + Для экспорта конфигурации выбранной среды Dynatrace выберите ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Export configuration** в правом верхнем углу.

## Events

**Events** содержит список событий журнала с сообщениями и временными метками.

* Фильтруйте таблицу по:

  + Уровню серьёзности
  + Временному периоду
  + Текстовому поиску
* Перемещайтесь по таблице с помощью элементов управления под таблицей.

## User authentication

**User authentication** содержит ссылки на настройки, связанные с пользователями.

* **User accounts** — список учётных записей пользователей. Выберите пользователя для просмотра сведений, назначений групп и разрешений. Подробности см. в разделе [Управление пользователями и группами](/managed/manage/identity-access-management/user-and-group-management "User and group management").
* **User groups** — список групп пользователей. Выберите группу для настройки имени группы, разрешений и политик. Подробности см. в разделе [Управление пользователями и группами](/managed/manage/identity-access-management/user-and-group-management "User and group management").
* **Policy management** — список политик. Выберите политику в столбце **Actions** для просмотра или редактирования.
* **User sessions** — список пользовательских сеансов. Подробности см. в разделе [Пользовательские сеансы](/managed/managed-cluster/configuration/configure-manage-user-sessions "Learn how to define the maximum number of concurrent user sessions for Dynatrace Managed.").
* **Password policy** — подробности см. в разделе [Правила сложности пароля](/managed/managed-cluster/configuration/password-complexity-rules "Learn how to configure password complexity rules for Dynatrace Managed.").
* **User repository** — просмотр и редактирование настроек репозитория пользователей. Подробности см. в разделе [LDAP](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-ldap "Learn how to connect your Dynatrace Server to an LDAP server to import user groups or accounts that need access to your Dynatrace Managed environment.").
* **Single sign-on settings** — подробности см. в разделе [Настройки SAML](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-saml "Learn how to connect your Dynatrace Server to a SAML server to import user groups or accounts that need access to your Dynatrace Managed environment.") и [Настройки OpenID Connect](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-openid "Learn how to use OpenID as an SSO IdP for the management of users and groups.").
* **Login screen** — подробности см. в разделе [Настройка страницы входа](/managed/managed-cluster/configuration/sign-in-customization "Learn how to customize the sign-in page in Dynatrace Managed.").

## Settings

**Settings** содержит ссылки на настройки кластера.

* **Public endpoints**
* **Internet proxy** — подробности см. в разделе [Настройка интернет-прокси для кластера](/managed/managed-cluster/configuration/internet-proxy "Configure a proxy connection for your Managed Cluster if you don't have direct internet access.").
* **Emails**

  + **SMTP server** — настройка доставки email-уведомлений кластера. Подробности см. в разделе [Настройка подключения к SMTP-серверу](/managed/managed-cluster/configuration/configure-smtp-server-connection "Learn how to configure an SMTP server connection and why this is recommended.").
  + **Email notifications** — настройка получателей email-уведомлений.
* **Preferences** — подробности см. в разделе [Параметры кластера](/managed/managed-cluster/configuration/configure-cluster-preferences "Configure cluster preferences and privacy settings").
* **Remote access permissions** — подробности см. в разделе [Удалённый доступ к кластеру](/managed/managed-cluster/configuration/cluster-remote-access "Learn how to grant permission for remote access.").
* **API tokens** — подробности см. в разделе [Cluster API — токены и аутентификация](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").
* **Backup** — подробности см. в разделе [Резервное копирование и восстановление кластера](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.").
* **Service Providers**
* **Automatic update** — подробности см. в разделе [Обновление кластера](/managed/managed-cluster/operation/update-cluster "Learn how to update a Managed cluster and how to schedule an automatic update.").

## Licensing

**Licensing** отображает сведения об учётной записи и лицензировании.

Для проверки подключения к [Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") выберите ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Check Mission Control connection** в правом верхнем углу.

## Audit log

**Audit log** содержит список событий, инициированных кластером, и выбранных изменений конфигурации для всех сред.

В этой таблице отображаются только изменения, связанные с общекластерной конфигурацией, лицензированием, квотами хранилища и разрешениями. Для просмотра всех записей журнала аудита среды используйте [Audit Logs API](/managed/dynatrace-api/environment-api/audit-logs/get-log "View full audit log via Dynatrace API.").