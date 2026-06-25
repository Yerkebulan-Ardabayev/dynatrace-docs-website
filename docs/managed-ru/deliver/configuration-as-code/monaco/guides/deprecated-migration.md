---
title: Миграция устаревших типов конфигурации
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/guides/deprecated-migration
scraped: 2026-05-12T12:02:58.718740
---

# Migrate deprecated configuration types

# Migrate deprecated configuration types

* How-to guide
* 3-min read
* Published Oct 25, 2022

Описанная здесь миграция актуальна для версии 1.x.

Преобразование проекта версии 1.x в 2.x автоматически заменяет устаревшие типы Config API.

Если ваш проект версии 1.x всё ещё использует эти устаревшие типы, после развёртывания некоторые конфигурации могут задвоиться.
Для обеспечения плавного обновления следует мигрировать устаревшие типы до преобразования в 2.x.

Данное руководство описывает процесс миграции устаревших типов конфигурации.

## Проблема

Исходные конфигурации `dashboard`, `request-naming-service` и `app-detection-rule` были затронуты конфликтами между атрибутами имён сущностей Dynatrace.

Например, дашборды (то же относится к `request-naming-service` и `app-detection-rule`) не имеют уникального имени в пределах окружения Dynatrace. К сожалению, Dynatrace Monaco CLI зависит от уникальности имён для идентификации ресурсов. В случае дашбордов это приводило к пропущенным/некорректным загрузкам и конфликтам при развёртываниях.

Решением стала генерация пользовательских UUID на основе метаданных Dynatrace Monaco CLI. Это даёт множество преимуществ, однако недостатком является то, что Monaco потерял отслеживание уже развёрнутых дашбордов. Развёртывание дашборда поэтому приводило к повторному развёртыванию (и дублированию) потенциально десятков дашбордов в Dynatrace.

Следующая процедура описывает миграцию конфигурации `dashboard`, но в равной мере применима к конфигурациям `request-naming-service` и `app-detection-rule`.

## Миграция конфигурации

Для миграции конфигурации `dashboard`:

1. Ознакомьтесь с существующей конфигурацией.

   Существующие конфигурации `dashboard` обычно выглядят примерно так:

   `config.yaml`

   ```
   config:



   - DashboardConfigId: config.json



   DashboardConfigId:



   - name: Monaco Test



   - owner: Monaco User



   - isShared: true
   ```

   Где `DashboardConfigId` — пользовательский ключ, связывающий детали конфигурации и `config.json`. Пользовательские свойства `name`, `owner` и `isShared` подставляются в `config.json`:

   `config.json`:

   ```
   {



   "dashboardMetadata": {



   "dashboardFilter": null,



   "name": "{{ .name }}",



   "owner": "{{ .owner }}",



   "shared": {{ .isShared }},



   "tilesNameSize": null



   },



   "tiles": [



   ...



   ]



   }
   ```

   В структуре папок, похожей на эту:

   ```
   workdir/



   project/



   app-detection-rule/



   ...



   dashboard/



   config.json



   config.yaml



   environment.yaml
   ```
2. **Рекомендуется:** поскольку пользовательский ключ (в нашем примере `DashboardConfigId`) используется для автоматической генерации ID сущностей Dynatrace в версии 2, самый простой способ мигрировать существующую конфигурацию — заменить его фактическим ID сущности Dynatrace. ID сущностей дашборда можно найти через Dynatrace API или веб-интерфейс Dynatrace:

   `config.yaml`:

   ```
   config:



   - <DT entity UUID>: config.json



   <DT entity UUID>:



   - name: Monaco Test



   - owner: Monaco User



   - isShared: true
   ```

   Конфигурация теперь совместима с версией 2 типа конфигурации dashboard.

   **Альтернатива:** после того как конфигурация устаревает и предоставляется новая версия, все последующие загрузки создают конфигурации новой версии. Существующая конфигурация сохраняется, но больше не обновляется:

   ```
   workdir/



   project/



   app-detection-rule-v2/



   ...



   dashboard/



   config.json



   config.yaml



   dashboard-v2/



   config.json



   config.yaml



   environment.yaml
   ```

   Хотя загруженный `config.yaml` содержит корректные ключи конфигурации, другие пользовательские свойства (например, owner) теряются:

   `dashboard-v2/config.yaml`:

   ```
   config:



   - <DT entity UUID>: config.json



   <DT entity UUID>:



   - name: Monaco Test
   ```

   Этот метод, однако, позволяет идентифицировать экземпляры конфигурации по свойству name и копировать существующие ID сущностей Dynatrace вместо их получения через API или веб-интерфейс.
3. Для того чтобы Dynatrace Monaco CLI распознал конфигурации версии 2, к папке конфигурации необходимо добавить инкрементный номер версии: `dashboard` становится `dashboard-v2`:

   ```
   workdir/



   project/



   app-detection-rule-v2/



   ...



   dashboard-v2/



   config.json



   config.yaml



   environment.yaml
   ```

## Связанные темы

* [Миграция конфигурации с Monaco 1.x на 2.x](/managed/deliver/configuration-as-code/monaco/guides/migrating-to-v2 "Migrate existing Monaco 1.x projects to version 2.x.")