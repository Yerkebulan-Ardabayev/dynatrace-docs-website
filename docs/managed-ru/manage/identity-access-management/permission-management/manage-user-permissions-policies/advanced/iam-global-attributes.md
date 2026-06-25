---
title: Глобальные атрибуты политик
source: https://docs.dynatrace.com/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-attributes
scraped: 2026-05-12T11:49:54.505224
---

# Глобальные атрибуты политик

# Глобальные атрибуты политик

* Reference
* 1-min read
* Published Dec 20, 2020

Для некоторых глобальных условий фреймворк политик предоставляет атрибуты, которые можно использовать в синтаксисе политик. Эти атрибуты не требуют дополнительной настройки в виде определения параметров привязки.

Список доступных глобальных атрибутов:

| Глобальный атрибут | Описание |
| --- | --- |
| `${global:levelId}` | [Организационный уровень](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt#list "Создание, редактирование, копирование и удаление политик IAM для управления разрешениями пользователей Dynatrace.") оценки разрешений |
| `${global:userGroup}` | Список UUID групп, в которые входит пользователь |

#### Примеры

Данная политика предоставляет пользователям доступ ко всем зонам управления, имена которых совпадают с именами назначенных им групп.

```
ALLOW environment:roles:viewer WHERE environment:management-zone IN ('${global:userGroup}');
```

Данная политика предоставляет пользователям доступ к зоне управления, имя которой совпадает с идентификатором окружения. Это может быть полезно, если соглашения об именовании основаны на идентификаторах окружений.

```
ALLOW environment:roles:viewer WHERE environment:management-zone = "${global:levelId}";
```