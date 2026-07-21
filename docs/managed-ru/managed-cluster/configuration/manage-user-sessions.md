---
title: Управление пользовательскими сессиями
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/manage-user-sessions
---

# Управление пользовательскими сессиями

# Управление пользовательскими сессиями

* Инструкция
* 1 мин на чтение
* Обновлено 18 июня 2026 г.

Чтобы управлять доступом к Dynatrace Managed, нужно просматривать активные пользовательские сессии, завершать сессии при необходимости и настраивать лимиты сессий.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Просмотр пользовательских сессий**](/managed/managed-cluster/configuration/manage-user-sessions#review-user-sessions "Learn how to define the maximum number of concurrent user sessions, terminate active sessions, and configure automatic sign-out in Dynatrace Managed.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Завершение пользовательской сессии**](/managed/managed-cluster/configuration/manage-user-sessions#terminate-user-session "Learn how to define the maximum number of concurrent user sessions, terminate active sessions, and configure automatic sign-out in Dynatrace Managed.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Настройка одновременных сессий**](/managed/managed-cluster/configuration/manage-user-sessions#configure-concurrent-sessions "Learn how to define the maximum number of concurrent user sessions, terminate active sessions, and configure automatic sign-out in Dynatrace Managed.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Обновление автоматического выхода**](/managed/managed-cluster/configuration/manage-user-sessions#update-automatic-sign-out "Learn how to define the maximum number of concurrent user sessions, terminate active sessions, and configure automatic sign-out in Dynatrace Managed.")

## Шаг 1. Просмотр пользовательских сессий

В Cluster Management Console перейти в **User authentication** > **User sessions**.

Представление пользовательских сессий показывает метод входа, время входа и IP-адрес или устройство, с которого произошёл вход.

Типы входа:

* `LOCAL`, пользователи, существующие только в базе данных Managed Cluster и локальные для Managed Cluster
* `LDAP`, пользователи LDAP
* `SSO`, вход через провайдера идентификации
* `DEVOPSTOKEN`, вход со стороны Mission Control proactive support

## Шаг 2. Завершение пользовательской сессии

Чтобы завершить сессию, выбрать ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") и подтвердить действие.

Сессия немедленно завершается, пользователь выходит из системы.

## Шаг 3. Настройка одновременных сессий

Ограничить количество одновременных сессий на учётную запись пользователя минимумом, необходимым для выполнения рабочих обязанностей.

Чтобы изменить число разрешённых одновременных пользовательских сессий, выбрать **Configure concurrent sessions**. Можно задать разные лимиты для обычных пользователей и администраторов. Учётные записи администраторов, это пользователи, входящие в любую группу с правами global cluster-admin.

Чтобы убрать все лимиты сессий для администраторов и обычных учётных записей, включить **Unlimited concurrent sessions**.

## Шаг 4. Обновление автоматического выхода

Использовать REST API для обновления политики автоматического выхода. По умолчанию автоматический выход отсутствует для пользователей, остающихся на страницах с автоматическим обновлением. См. [Update cluster user sessions configuration](/managed/dynatrace-api/cluster-api/cluster-api-v2/user-management/update-cluster-user-sessions-configuration "Learn how to update Dynatrace Cluster user sessions configuration using API.").