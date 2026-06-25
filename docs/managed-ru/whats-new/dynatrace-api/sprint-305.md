---
title: Журнал изменений Dynatrace API версии 1.305
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-305
scraped: 2026-05-12T11:35:39.128164
---

# Журнал изменений Dynatrace API версии 1.305

# Журнал изменений Dynatrace API версии 1.305

* Заметки о выпуске
* Published Dec 05, 2024

Rollout start: Dec 3, 2024

## Environment API

### /extensions/{technology}/availableHosts

* `GET /extensions/{technology}/availableHosts` Early Access

  Параметр:

  + Changed technology in path

    - Добавлено значение перечисления:  
      `RABBITMQ_CLIENT`

### /service/requestAttributes

* `POST /service/requestAttributes`

  Запрос:

  Изменена схема **RequestAttribute**

  + Изменено свойство **dataSources**

    - Изменено свойство **scope**

      * Изменено свойство **serviceTechnology**

        + Добавлено значение перечисления:  
          `RABBITMQ_CLIENT`
* `POST /service/requestAttributes/validator`

  Запрос:

  Изменена схема **RequestAttribute**

  + Изменено свойство **dataSources**

    - Изменено свойство **scope**

      * Изменено свойство **serviceTechnology**

        + Добавлено значение перечисления:  
          `RABBITMQ_CLIENT`
* `GET /service/requestAttributes/{id}`

  Возвращаемый тип:

  + Changed 200 OK
    Изменена схема **RequestAttribute**

    - Изменено свойство **dataSources**

      * Изменено свойство **scope**

        + Изменено свойство **serviceTechnology**

          - Добавлено значение перечисления:  
            `RABBITMQ_CLIENT`
* `PUT /service/requestAttributes/{id}`

  Запрос:

  Изменена схема **RequestAttribute**

  + Изменено свойство **dataSources**

    - Изменено свойство **scope**

      * Изменено свойство **serviceTechnology**

        + Добавлено значение перечисления:  
          `RABBITMQ_CLIENT`
* `POST /service/requestAttributes/{id}/validator`

  Запрос:

  Изменена схема **RequestAttribute**

  + Изменено свойство **dataSources**

    - Изменено свойство **scope**

      * Изменено свойство **serviceTechnology**

        + Добавлено значение перечисления:  
          `RABBITMQ_CLIENT`

### /entity/infrastructure/

* `GET /entity/infrastructure/process-groups`

  Возвращаемый тип:

  + Changed 200 OK
    Изменена схема null

    - Изменено свойство **metadata**

      * Добавлено свойство:  
        **declarativeConfigRuleId**
* `GET /entity/infrastructure/process-groups/{meIdentifier}`

  Возвращаемый тип:

  + Changed 200 OK
    Изменена схема ProcessGroup

    - Изменено свойство **metadata**

      * Добавлено свойство:  
        **declarativeConfigRuleId**
* `GET /entity/infrastructure/processes`

  Возвращаемый тип:

  + Changed 200 OK
    Изменена схема null

    - Изменено свойство **metadata**

      * Добавлено свойство:  
        **declarativeConfigRuleId**
* `GET /entity/infrastructure/processes/{meIdentifier}`

  Возвращаемый тип:

  + Changed 200 OK
    Изменена схема ProcessGroupInstance

    - Изменено свойство **metadata**

      * Добавлено свойство:  
        **declarativeConfigRuleId**

### /timeseries

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

* Удалён `PUT /timeseries`. Используйте [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API.") вместо него.

## Configuration API

### /extensions/{technology}/availableHosts

* `GET /extensions/{technology}/availableHosts` Early Access

  Параметр:

  + Changed technology in path

    - Добавлено значение перечисления:  
      `RABBITMQ_CLIENT`

### /service/requestAttributes

* `POST /service/requestAttributes`

  Запрос:

  Изменена схема **RequestAttribute**

  + Изменено свойство **dataSources**

    - Изменено свойство **scope**

      * Изменено свойство **serviceTechnology**

        + Добавлено значение перечисления:  
          `RABBITMQ_CLIENT`
* `POST /service/requestAttributes/validator`

  Запрос:

  Изменена схема **RequestAttribute**

  + Изменено свойство **dataSources**

    - Изменено свойство **scope**

      * Изменено свойство **serviceTechnology**

        + Добавлено значение перечисления:  
          `RABBITMQ_CLIENT`
* `GET /service/requestAttributes/{id}`

  Возвращаемый тип:

  + Changed 200 OK
    Изменена схема **RequestAttribute**

    - Изменено свойство **dataSources**

      * Изменено свойство **scope**

        + Изменено свойство **serviceTechnology**

          - Добавлено значение перечисления:  
            `RABBITMQ_CLIENT`
* `PUT /service/requestAttributes/{id}`

  Запрос:

  Изменена схема **RequestAttribute**

  + Изменено свойство **dataSources**

    - Изменено свойство **scope**

      * Изменено свойство **serviceTechnology**

        + Добавлено значение перечисления:  
          `RABBITMQ_CLIENT`
* `POST /service/requestAttributes/{id}/validator`

  Запрос:

  Изменена схема **RequestAttribute**

  + Изменено свойство **dataSources**

    - Изменено свойство **scope**

      * Изменено свойство **serviceTechnology**

        + Добавлено значение перечисления:  
          `RABBITMQ_CLIENT`

## Связанные темы

* [Заметки о выпуске SaaS 1.305](https://docs.dynatrace.com/docs/shortlink/release-notes-saas-sprint-305)