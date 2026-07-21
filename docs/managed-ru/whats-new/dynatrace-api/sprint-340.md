---
title: Dynatrace API, журнал изменений версии 1.340
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-340
---

# Dynatrace API, журнал изменений версии 1.340

# Dynatrace API, журнал изменений версии 1.340

* Примечания к выпуску
* Обновлено 02 июня 2026 г.
* Начало развёртывания 02 июня 2026 г.

## Environment API v1

### /synthetic/monitors

Следующие endpoints признаны устаревшими:

* `GET /synthetic/monitors` Устарело
* `POST /synthetic/monitors` Устарело
* `GET /synthetic/monitors/{monitorId}` Устарело
* `PUT /synthetic/monitors/{monitorId}` Устарело
* `DELETE /synthetic/monitors/{monitorId}` Устарело

### /tokens

* `GET /tokens`

  + Параметр:

    - Изменён **permissions** в query

      * Добавлены значения enum:  
        `extensionDiscoveryPmi.read`
* `POST /tokens`

  + Запрос:

    - Изменена схема **CreateToken** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:  
          `extensionDiscoveryPmi.read`
* `POST /tokens/lookup`

  + Тип возвращаемого значения:

    - Изменено 200 OK
      Изменена схема **TokenMetadata** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:  
          `extensionDiscoveryPmi.read`
* `GET /tokens/{id}`

  + Тип возвращаемого значения:

    - Изменено 200 OK
      Изменена схема **TokenMetadata** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:  
          `extensionDiscoveryPmi.read`
* `PUT /tokens/{id}`

  + Запрос:

    - Изменена схема **UpdateToken** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:  
          `extensionDiscoveryPmi.read`

## Environment API v2

### /activeGates

Следующие endpoints признаны устаревшими:

* `GET /activeGates/autoUpdate` Устарело
* `PUT /activeGates/autoUpdate` Устарело
* `POST /activeGates/autoUpdate/validator` Устарело
* `GET /activeGates/{agId}/autoUpdate` Устарело
* `PUT /activeGates/{agId}/autoUpdate` Устарело
* `POST /activeGates/{agId}/autoUpdate/validator` Устарело

### /networkZones

Следующие endpoints признаны устаревшими:

* `PUT /networkZones/{id}` Устарело
* `DELETE /networkZones/{id}` Устарело

### /apiTokens

* `GET /apiTokens`

  + Тип возвращаемого значения:

    - Изменено 200 OK
      Изменена схема **ApiTokenList** (application/json; charset=utf-8)

      * Изменено свойство **apiTokens**

        + Изменено свойство **scopes**

          - Добавлены значения enum:  
            `extensionDiscoveryPmi.read`
* `POST /apiTokens`

  + Запрос:

    - Изменена схема **ApiTokenCreate** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:  
          `extensionDiscoveryPmi.read`
* `POST /apiTokens/lookup`

  + Тип возвращаемого значения:

    - Изменено 200 OK
      Изменена схема **ApiToken** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:  
          `extensionDiscoveryPmi.read`
* `GET /apiTokens/{id}`

  + Тип возвращаемого значения:

    - Изменено 200 OK
      Изменена схема **ApiToken** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:  
          `extensionDiscoveryPmi.read`
* `PUT /apiTokens/{id}`

  + Запрос:

    - Изменена схема **ApiTokenUpdate** (application/json; charset=utf-8)

      * Изменено свойство **scopes**

        + Добавлены значения enum:  
          `extensionDiscoveryPmi.read`

### /extensions

* `GET /extensions/discovery/pmi/processes` Ранний доступ

  + Уровень зрелости API изменён с `IN_DEVELOPMENT` на `EARLY_ADOPTER`
* `GET /extensions/discovery/pmi/processes/{process-id}` Ранний доступ

  + Уровень зрелости API изменён с `IN_DEVELOPMENT` на `EARLY_ADOPTER`

## Configuration API

### /calculatedMetrics

* `POST /calculatedMetrics/service`

  + Запрос:

    - Изменена схема **CalculatedServiceMetric** (application/json; charset=utf-8)

      * Нарушена совместимость
      * Изменено свойство **dimensionDefinition**

        + Изменено свойство **placeholders**

          - Изменено свойство **source**

            * Изменено свойство **serviceTag**

              + Тип изменён с `object` на `null`
* `POST /calculatedMetrics/service/validator`

  + Запрос:

    - Изменена схема **CalculatedServiceMetric** (application/json; charset=utf-8)

      * Нарушена совместимость
      * Изменено свойство **dimensionDefinition**

        + Изменено свойство **placeholders**

          - Изменено свойство **source**

            * Изменено свойство **serviceTag**

              + Тип изменён с `object` на `null`
* `GET /calculatedMetrics/service/{metricKey}`

  + Тип возвращаемого значения:

    - Изменено 200 OK
      Изменена схема **CalculatedServiceMetric** (application/json; charset=utf-8)

      * Нарушена совместимость
      * Изменено свойство **dimensionDefinition**

        + Изменено свойство **placeholders**

          - Изменено свойство **source**

            * Изменено свойство **serviceTag**

              + Тип изменён с `object` на `null`
* `PUT /calculatedMetrics/service/{metricKey}`

  + Запрос:

    - Изменена схема **CalculatedServiceMetric** (application/json; charset=utf-8)

      * Нарушена совместимость
      * Изменено свойство **dimensionDefinition**

        + Изменено свойство **placeholders**

          - Изменено свойство **source**

            * Изменено свойство **serviceTag**

              + Тип изменён с `object` на `null`
* `POST /calculatedMetrics/service/{metricKey}/validator`

  + Запрос:

    - Изменена схема **CalculatedServiceMetric** (application/json; charset=utf-8)

      * Нарушена совместимость
      * Изменено свойство **dimensionDefinition**

        + Изменено свойство **placeholders**

          - Изменено свойство **source**

            * Изменено свойство **serviceTag**

              + Тип изменён с `object` на `null`

### /service

* `POST /service/requestNaming`

  + Запрос:

    - Изменена схема **RequestNaming** (application/json; charset=utf-8)

      * Нарушена совместимость
      * Изменено свойство **placeholders**

        + Изменено свойство **source**

          - Изменено свойство **serviceTag**

            * Тип изменён с `object` на `null`
* `POST /service/requestNaming/validator`

  + Запрос:

    - Изменена схема **RequestNaming** (application/json; charset=utf-8)

      * Нарушена совместимость
      * Изменено свойство **placeholders**

        + Изменено свойство **source**

          - Изменено свойство **serviceTag**

            * Тип изменён с `object` на `null`
* `GET /service/requestNaming/{id}`

  + Тип возвращаемого значения:

    - Изменено 200 OK
      Изменена схема **RequestNaming** (application/json; charset=utf-8)

      * Нарушена совместимость
      * Изменено свойство **placeholders**

        + Изменено свойство **source**

          - Изменено свойство **serviceTag**

            * Тип изменён с `object` на `null`
* `PUT /service/requestNaming/{id}`

  + Запрос:

    - Изменена схема **RequestNaming** (application/json; charset=utf-8)

      * Нарушена совместимость
      * Изменено свойство **placeholders**

        + Изменено свойство **source**

          - Изменено свойство **serviceTag**

            * Тип изменён с `object` на `null`
* `POST /service/requestNaming/{id}/validator`

  + Запрос:

    - Изменена схема **RequestNaming** (application/json; charset=utf-8)

      * Нарушена совместимость
      * Изменено свойство **placeholders**

        + Изменено свойство **source**

          - Изменено свойство **serviceTag**

            * Тип изменён с `object` на `null`

## Cluster API v1

### /multiDc/migration

* `GET /multiDc/migration/clusterState` Ранний доступ

  + Тип возвращаемого значения:

    - Изменено 200 OK
      Изменена схема **SingleToMultiDcMigrationClusterState** (application/json)

      * Изменено свойство **migrationSteps**

        + Изменена схема значения словаря:

          - Изменено свойство **status**

            * Добавлены значения enum:  
              `DC_RECOVERY`
      * Изменено свойство **singleToMultiDcMigration**

        + Изменено свойство **status**

          - Добавлены значения enum:  
            `DC_RECOVERY`
* `PUT /multiDc/migration/clusterState` Ранний доступ

  + Параметр:

    - Изменён **status** в query

      * Добавлены значения enum:  
        `DC_RECOVERY`
* `GET /multiDc/migration/clusterState/{subStep}` Ранний доступ

  + Тип возвращаемого значения:

    - Изменено 200 OK
      Изменена схема **MigrationState** (application/json)

      * Изменено свойство **status**

        + Добавлены значения enum:  
          `DC_RECOVERY`
* `PUT /multiDc/migration/clusterState/{subStep}` Ранний доступ

  + Параметр:

    - Изменён **status** в query

      * Добавлены значения enum:  
        `DC_RECOVERY`
* `GET /multiDc/migration/inServerconfigState` Ранний доступ

  + Тип возвращаемого значения:

    - Изменено 200 OK
      Изменена схема **InServerConfigDatacenterMigrationState** (application/json)

      * Изменено свойство **componentMigrationStates**

        + Изменена схема значения словаря:

          - Изменено свойство **status**

            * Добавлены значения enum:  
              `DC_RECOVERY`

### /upgradeManagement

* `GET /upgradeManagement/installationFiles`

  + Тип возвращаемого значения:

    - Изменено 200 OK
      Изменена схема null (application/json; charset=utf-8)

      * Добавлены свойства:  
        **countOfTenantsUsingThisAsTargetVersion**

## Cluster API v2

### /activeGates

Следующие endpoints признаны устаревшими:

* `GET /activeGates/autoUpdate/{envId}` Устарело
* `PUT /activeGates/autoUpdate/{envId}` Устарело
* `POST /activeGates/autoUpdate/{envId}/validator` Устарело

### /environments

* `GET /environments`

  + Тип возврата:

    - Изменено 200 OK
      Изменена схема **EnvironmentList** (application/json; charset=utf-8)

      * Изменено свойство **environments**

        + Изменено свойство **storage**

          - Добавлены свойства:  
            **logMonitoringV2Retention**  
            **logMonitoringV2Storage**
* `POST /environments`

  + Запрос:

    - Изменена схема **Environment** (application/json; charset=utf-8)

      * Изменено свойство **storage**

        + Добавлены свойства:  
          `logMonitoringV2Retention`
          `logMonitoringV2Storage`
* `GET /environments/{id}`

  + Тип возврата:

    - Изменено 200 OK
      Изменена схема **Environment** (application/json; charset=utf-8)

      * Изменено свойство **storage**

        + Добавлены свойства:  
          `logMonitoringV2Retention`
          `logMonitoringV2Storage`
* `PUT /environments/{id}`

  + Запрос:

    - Изменена схема **Environment** (application/json; charset=utf-8)

      * Изменено свойство **storage**

        + Добавлены свойства:  
          `logMonitoringV2Retention`
          `logMonitoringV2Storage`

### /iam

Откатывает изменение, введённое в [API версии 1.338](/managed/whats-new/dynatrace-api/sprint-338 "Список изменений для Dynatrace API версии 1.338").

* `GET /iam/resolution/{level-type}/{level-id}/descendants/effectivepermissions`

  + Параметр:

    - Изменён **entity\_id** в запросе

      * Шаблон изменён с `^[^{}]+$` на `null`
* `GET /iam/resolution/{level-type}/{level-id}/effectivepermissions`

  + Параметр:

    - Изменён **entity\_id** в запросе

      * Шаблон изменён с `^[^{}]+$` на `null`