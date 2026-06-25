---
title: Обзор конфигурации Monaco
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/configuration
scraped: 2026-05-12T11:21:33.862666
---

# Monaco configuration overview

# Monaco configuration overview

* Overview
* 5-min read
* Updated on Feb 19, 2026

Configuration as Code через Monaco состоит из набора проектов и манифеста развёртывания.

## projects

Проекты — это директории (папки), используемые для логической группировки конфигураций API. Примером проекта может служить сервис, все конфигурации которого хранятся в одной папке. Проекты могут включать несколько файлов и директорий. Подробнее см. [Управление проектом Monaco](/managed/deliver/configuration-as-code/monaco/configuration/projects "Manage a project folder with Dynatrace Configuration as Code via Monaco.").

## Манифест развёртывания

Манифесты развёртывания — это YAML-файлы, которые указывают Dynatrace Monaco CLI, какие проекты развёртывать и куда. Для корректной работы Dynatrace Monaco CLI необходим файл манифеста.

Этот файл содержит информацию о том, что и куда развёртывать.

Манифест сохраняется как YAML-файл. Он имеет три ключа верхнего уровня: `manifestVersion`, `projects` и `environmentGroups`.

Пример `manifest.yaml`:

```
manifestVersion: 1.0



projects:



- name: infra



path: shared/infrastructure



- name: general



path: general



type: grouping



environmentGroups:



- name: dev



environments:



- name: test-env-1



url:



value: https://<YOUR-DT-DEV-ENV-ID>.apps.dynatrace.com



auth:



token:



name: DEV_TOKEN



- name: test-env-2



url:



value: https://<YOUR-DT-SPRINT-ENV-ID>.apps.dynatrace.com



auth:



token:



name: SPRINT_TOKEN



- name: prod



environments:



- name: prod-env-1



url:



type: environment



value: https://<YOUR-DT-PROD-ENV-ID>.apps.dynatrace.com



auth:



token:



name: PROD_TOKEN
```

В следующих разделах каждый ключ конфигурации описан подробно.

### Версия

Манифест должен содержать `manifestVersion` в качестве ключа верхнего уровня. Это простая строка, используемая для проверки того, может ли текущая версия Monaco корректно разобрать манифест.

В настоящее время поддерживается версия манифеста `1.0`. В примечаниях к релизу будут содержаться подробности при расширении манифеста и выпуске новых версий.

### Определения проектов

Все записи под ключом верхнего уровня `projects` задают проекты для развёртывания через Monaco. Для указания `type` проекта используйте ключ `type` в элементе проекта. В настоящее время поддерживаются два типа проектов:

* `simple`
* `grouping`

#### Простые проекты

Это тип по умолчанию. Необходимо указать только свойства `name` и `path`. Если свойство `path` не указано, в качестве `path` используется `name`.

* Значение `name` не может содержать символ косой черты (`/` или `\`). Это явно отличает его от путей файловой системы.
* Значение `path` всегда должно использовать прямую косую черту (`/`) в качестве разделителя, независимо от операционной системы (Linux, Windows, Mac). Например:

```
projects:



- name: infra



path: shared/infrastructure
```

#### Группирующие проекты

Группирующие проекты предоставляют упрощённый способ объединения нескольких проектов. Отличие группирующего проекта от простого состоит в том, что группирующий проект загружает все подпапки указанного пути как простые проекты. Необходимо указать имя, которое будет использоваться как префикс для итоговых простых проектов. В качестве разделителя используется точка (`.`).

Например, при следующей структуре файлов:

```
general/



├── infrastructure/



└── zones/
```

Следующее определение проекта:

```
projects:



- name: general



path: general



type: grouping
```

породит два проекта:

* `general.infrastructure`
* `general.zones`

### Группы окружений

Если проекты — это *что*, то окружения — это *куда* для Dynatrace Monaco CLI.
[Смотрите пример manifest.yaml выше](/managed/deliver/configuration-as-code/monaco/configuration#manifest "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.").
Как видно, каждое окружение должно входить в группу и может быть только в одной группе.

Группы окружений — это механизм, позволяющий при развёртывании нацеливаться на конкретные окружения совместно или переопределять свойства конфигурации для нескольких окружений одним переопределением вместо индивидуального переопределения для каждого.

Удобно группировать и разграничивать pre-production и production окружения, как показано в примере.

### Определение окружения

Определение окружения состоит из трёх частей: `name`, `url` и `auth`.

* `name` идентифицирует окружение для Monaco. Это произвольная строка, но она должна быть уникальной.
* Раздел `url` задаёт URL окружения Dynatrace.
* Раздел `auth` определяет способ аутентификации в Dynatrace API.

#### URL окружения

Определение `url` состоит из полей `type` и `value`.

URL окружения можно указать непосредственно в манифесте как значение:

```
url:



type: value



value: https://{environment-specific-domain}
```

или как переменную окружения для загрузки URL:

```
url:



type: environment



value: YOUR_URL_ENV_VAR
```

##### Аутентификация по токену доступа

Токены доступа для Dynatrace Monaco CLI всегда требуют как минимум следующего разрешения для запроса общей информации об окружении:

* **Access problem and event feed, metrics, and topology** (`DataExport`) — API v1

В большинстве случаев потребуется токен доступа как минимум с этими разрешениями:

* **Access problem and event feed, metrics, and topology** (`DataExport`) — API v1
* **Read configuration** (`ReadConfig`) — API v1
* **Write configuration** (`WriteConfig`) — API v1
* **Read settings** (`settings.read`) — API v2
* **Write settings** (`settings.write`) — API v2

Общую информацию об аутентификации по токену доступа см. в [Dynatrace API — токены и аутентификация](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").