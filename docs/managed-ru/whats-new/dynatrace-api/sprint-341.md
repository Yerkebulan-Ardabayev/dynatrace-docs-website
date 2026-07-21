---
title: Список изменений API Dynatrace API, версия 1.341
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-341
---

# Список изменений API Dynatrace API, версия 1.341

# Список изменений API Dynatrace API, версия 1.341

* Примечания к выпуску
* Опубликовано 9 июня 2026 г.
* Начало развёртывания 16 июня 2026 г.

## Environment API

### GET /deployment/installer/agent/{osType}/{installerType}

* `GET /deployment/installer/agent/{osType}/{installerType}/latest`

  + Параметр:

    - Изменён **include** в query

      * Добавлены значения enum:
        `ruby`
* `GET /deployment/installer/agent/{osType}/{installerType}/version/{version}`

  + Параметр:

    - Изменён **include** в query

      * Добавлены значения enum:
        `ruby`
* `GET /deployment/installer/agent/{osType}/{installerType}/version/{version}/checksum`

  + Параметр:

    - Изменён **include** в query

      * Добавлены значения enum:
        `ruby`

### Добавлены пользовательские разрешения для эндпоинта приёма данных Smartscape

* `GET /tokens`

  + Параметр:

    - Изменён **permissions** в query

      * Добавлены значения enum:
        `openpipeline.events_smartscape`
* `POST /tokens`

  + Запрос:

    - Изменена схема **CreateToken** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:
          `openpipeline.events_smartscape`
* `POST /tokens/lookup`

  + Тип возврата:

    - Изменён 200 OK
      Изменена схема **TokenMetadata** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:
          `openpipeline.events_smartscape`
* `GET /tokens/{id}`

  + Тип возврата:

    - Изменён 200 OK
      Изменена схема **TokenMetadata** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:
          `openpipeline.events_smartscape`
* `PUT /tokens/{id}`

  + Запрос:

    - Изменена схема **UpdateToken** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:
          `openpipeline.events_smartscape`
* `GET /apiTokens`

  + Тип возврата:

    - Изменён 200 OK
      Изменена схема **ApiTokenList** (application/json; charset=utf-8)

      * Изменено свойство **apiTokens**

        + Изменено свойство **scopes**

          - Добавлены значения enum:
            `openpipeline.events_smartscape`
* `POST /apiTokens`

  + Запрос:

    - Изменена схема **ApiTokenCreate** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:
          `openpipeline.events_smartscape`
* `POST /apiTokens/lookup`

  + Тип возврата:

    - Изменён 200 OK
      Изменена схема **ApiToken** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:
          `openpipeline.events_smartscape`
* `GET /apiTokens/{id}`

  + Тип возврата:

    - Изменён 200 OK
      Изменена схема **ApiToken** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:
          `openpipeline.events_smartscape`
* `PUT /apiTokens/{id}`

  + Запрос:

    - Изменена схема **ApiTokenUpdate** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:
          `openpipeline.events_smartscape`

### Провайдер ассетов для страниц как документов

* `GET /extensions/{extensionName}/environmentConfiguration/assets`

  + Тип возврата:

    - Изменён 200 OK
      Изменена схема **ExtensionAssetsDto** (application/json; charset=utf-8)

      * Изменено свойство **assets**

        + Изменено свойство **type**

          - Добавлены значения enum:
            `DOCUMENT_SCREEN`