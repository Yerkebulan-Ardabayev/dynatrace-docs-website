---
title: Обновление разрешений на основе ролей до политик Dynatrace IAM
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles
scraped: 2026-05-12T11:37:03.067298
---

# Обновление разрешений на основе ролей до политик Dynatrace IAM

# Обновление разрешений на основе ролей до политик Dynatrace IAM

* 11-min read
* Updated on Aug 20, 2025

Dynatrace версии 1.252+

Начиная с Dynatrace версии 1.252+, Dynatrace поддерживает определение разрешений пользователей и групп с помощью политик IAM наряду с классическим управлением доступом на основе ролей. На этой странице описано использование разрешений уровня окружения в операторах политик, что обеспечивает детальный контроль доступа по зонам управления, группам хостов и расширениям. Политики безопасности Dynatrace поддерживают [разрешения на основе ролей](/managed/manage/identity-access-management/permission-management/role-based-permissions "Разрешения на основе ролей"), позволяя управлять всем доступом к окружению. Политики безопасности можно использовать для определения разрешений пользователей/групп в окружении через веб-интерфейс Dynatrace или Dynatrace API.

Политики не ограничивают классические разрешения на основе ролей

При переносе разрешений на основе ролей в фреймворк IAM учитывайте, что разрешения на основе ролей и политики безопасности являются аддитивными. Например, если пользователю назначено разрешение окружения, а затем он добавлен в группу IAM с ролью на основе политики, ограниченной зоной управления, разрешение окружения по-прежнему предоставляет доступ ко всему окружению, включая все зоны управления.

## Разрешения окружения

Для упрощения миграции на политики безопасности можно использовать существующие [разрешения окружения](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Разрешения на основе ролей") в операторах политик и привязывать их к группам.

### Пример 1: политика для разработчика приложений

Например, для создания политики для типичного разработчика приложений необходимо предоставить ему набор разрешений, показанных в следующих примерах кода:

* Доступ ко всем настройкам в `dev` и `hardening`

  ```
  ALLOW environment:roles:manage-settings



  WHERE environment:management-zone IN ("dev", "hardening");
  ```
* Доступ на чтение в `prod`

  ```
  ALLOW environment:roles:viewer



  WHERE environment:management-zone IN ("prod");
  ```

### Пример 2: мониторинг частей окружения

1. Создайте политику, предоставляющую полный доступ к окружению.

   ```
   ALLOW environment:roles:viewer, environment:roles:manage-settings;
   ```

   Пользователь из группы, к которой привязана эта политика, имеет полный доступ к окружению.

   ![Полный доступ](https://dt-cdn.net/images/roles-808-c081787446.png "Полный доступ")

2. Измените политику, чтобы ограничить доступ выбранными зонами управления по префиксу имени (в данном примере `«[Kubernetes]»`).

   ```
   ALLOW environment:roles:viewer, environment:roles:manage-settings



   WHERE environment:management-zone startsWith "[Kubernetes]";
   ```

   Теперь пользователь имеет доступ только к зонам управления, имена которых начинаются с `«[Kubernetes]»`.

   ![Ограниченный доступ на основе ролей](https://dt-cdn.net/images/roles-limit-808-c095b9bcf9.png "Ограниченный доступ на основе ролей")

Узнайте, как [создавать политики](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Создание, редактирование, копирование и удаление политик IAM для управления разрешениями пользователей Dynatrace.").

## Разрешения зоны управления

Для создания политики, ограниченной определённой зоной управления, используйте атрибут `environment:management-zone` в операторе политики. Например, чтобы ограничить просмотр журналов определённой зоной управления, используйте следующий оператор:

```
ALLOW environment:roles:logviewer



WHERE environment:management-zone IN ("my-management-zone");
```

## Имена ролей

Используйте следующие имена ролей в операторах политик.

| Текущее имя роли | Имя роли IAM | Условие зоны управления |
| --- | --- | --- |
| View environment | `roles:viewer` | GA |
| Manage monitoring settings | `roles:manage-settings` | GA |
| Manage capturing of sensitive request data | `roles:configure-request-capture-data` |  |
| Install OneAgent | `roles:agent-install` |  |
| Manage security problems | `roles:manage-security-problems` | GA |
| View security problems | `roles:view-security-problems` | GA |
| Replay sessions without masking | `roles:replay-sessions-without-masking` | GA |
| Replay sessions with masking | `roles:replay-sessions-with-masking` | GA |
| View logs | `roles:logviewer` | GA |
| View sensitive request data | `roles:view-sensitive-request-data` | GA |

Как и в случае с классическими разрешениями на основе ролей, роль `viewer` неявно включена во все роли. Например, политика с ролью `manage-settings` также разрешает пользователю доступ к веб-интерфейсу.

## Синтаксис операторов политик

В простейшей форме оператор политики для разрешений окружения начинается с ключевого слова ALLOW, за которым следуют `environment:roles`, имя роли и имя зоны управления.

```
ALLOW environment:roles:<role name> WHERE environment:management-zone = "<name of management zone>";
```

Оператор может включать необязательное условие зоны управления, разрешающее роль в нескольких зонах управления.

```
ALLOW environment:roles:<role name> WHERE environment:management-zone IN ("<name of management zone 1>", "<name of management zone n>");
```

## Связанные разделы

* [Работа с политиками](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Работа с политиками")
* [Синтаксис и примеры операторов политик IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "Синтаксис операторов политик IAM.")