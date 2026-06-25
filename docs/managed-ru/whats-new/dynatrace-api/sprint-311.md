---
title: Журнал изменений Dynatrace API версии 1.311
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-311
scraped: 2026-05-12T11:36:10.357165
---

# Журнал изменений Dynatrace API версии 1.311

# Журнал изменений Dynatrace API версии 1.311

* Заметки о выпуске
* Published Mar 27, 2025

Rollout start: Mar 25, 2025

## Environment API

### /synthetic/monitors

* `POST /synthetic/monitors`

  + Запрос:

    - Изменена схема **SyntheticMonitorUpdate**

      ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

      * Изменено свойство **anomalyDetection**

        + Изменено свойство **loadingTimeThresholds**

          - Изменено свойство **thresholds**

            * Изменено свойство **eventIndex**

              + Минимум изменён с `1` на `0`
            * Изменено свойство **requestIndex**

              + Минимум изменён с `1` на `0`
* `GET /synthetic/monitors/{monitorId}`

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **SyntheticMonitor**

        + Изменено свойство **anomalyDetection**

          - Изменено свойство **loadingTimeThresholds**

            * Изменено свойство **thresholds**

              + Изменено свойство **eventIndex**

                - Минимум изменён с `1` на `0`
              + Изменено свойство **requestIndex**

                - Минимум изменён с `1` на `0`
* `PUT /synthetic/monitors/{monitorId}`

  + Запрос:

    - Изменена схема **SyntheticMonitorUpdate**

      ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

      * Изменено свойство **anomalyDetection**

        + Изменено свойство **loadingTimeThresholds**

          - Изменено свойство **thresholds**

            * Изменено свойство **eventIndex**

              + Минимум изменён с `1` на `0`
            * Изменено свойство **requestIndex**

              + Минимум изменён с `1` на `0`

### /activeGates

* `GET /activeGates`

  + Параметр:

    - Changed **enabledModule** in query

      * Добавлено значение перечисления:  
        `DEBUGGING`
    - Changed **disabledModule** in query

      * Добавлено значение перечисления:  
        `DEBUGGING`
  + Возвращаемый тип:

    - Changed 200 OK
    - Изменена схема **ActiveGateList**

      * Изменено свойство **activeGates**

        + Изменено свойство **modules**

          - Изменено свойство **type**

            * Добавлено значение перечисления:  
              `DEBUGGING`
* `GET /activeGates/{agId}`

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **ActiveGate**

        + Изменено свойство **modules**

          - Изменено свойство **type**

            * Добавлено значение перечисления:  
              `DEBUGGING`

## Configuration API

### /extensions

* `GET /extensions/{technology}/availableHosts` Early Access

  + Параметр:

    - Changed technology in path

      * Добавлено значение перечисления: `APACHE_PEKKO`

### /service/requestAttributes

* `POST /service/requestAttributes`

  + Запрос:

    - Изменена схема **RequestAttribute**

      * Изменено свойство **dataSources**

        + Изменено свойство **scope**

          - Изменено свойство **serviceTechnology**

            * Добавлено значение перечисления:  
              `APACHE_PEKKO`
* `POST /service/requestAttributes/validator`

  + Запрос:

    - Изменена схема **RequestAttribute**

      * Изменено свойство **dataSources**

        + Изменено свойство **scope**

          - Изменено свойство **serviceTechnology**

            * Добавлено значение перечисления:  
              `APACHE_PEKKO`
* `GET /service/requestAttributes/{id}`

  + Возвращаемый тип:

    - Changed 200 OK

      * Изменена схема **RequestAttribute**

        + Изменено свойство **dataSources**

          - Изменено свойство **scope**

            * Изменено свойство **serviceTechnology**

              + Добавлено значение перечисления:  
                `APACHE_PEKKO`
* `PUT /service/requestAttributes/{id}`

  + Запрос:

    - Изменена схема **RequestAttribute**

      * Изменено свойство **dataSources**

        + Изменено свойство **scope**

          - Изменено свойство **serviceTechnology**

            * Добавлено значение перечисления:  
              `APACHE_PEKKO`
* `POST /service/requestAttributes/{id}/validator`

  + Запрос:

    - Изменена схема **RequestAttribute**

      * Изменено свойство **dataSources**

        + Изменено свойство **scope**

          - Изменено свойство **serviceTechnology**

            * Добавлено значение перечисления:  
              `APACHE_PEKKO`