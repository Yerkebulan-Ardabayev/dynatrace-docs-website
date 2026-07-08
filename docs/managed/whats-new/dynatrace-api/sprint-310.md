---
title: Dynatrace API changelog version 1.310
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-310
---

# Dynatrace API changelog version 1.310

# Dynatrace API changelog version 1.310

* Release notes
* Published Mar 11, 2025

Rollout start: Mar 11, 2025

## Environment API

### /deployment/installer/agent/

* `GET /deployment/installer/agent/{osType}/{installerType}/latest`

  + Parameter:

    - Changed include in query

      * Added enum value:  
        `python`
* `GET /deployment/installer/agent/{osType}/{installerType}/version/{version}`

  + Parameter:

    - Changed include in query

      * Added enum value:  
        `python`
* `GET /deployment/installer/agent/{osType}/{installerType}/version/{version}/checksum`

  + Parameter:

    - Changed include in query

      * Added enum value:  
        `python`

### /extensions/

* `GET /extensions/{extensionName}/{extensionVersion}`

  + Return Type:

    - Changed 200 OK

      * Added `application/yaml`

### /extensions/

* `GET /extensions/{extensionName}/{extensionVersion}/schema`

  + Return Type:

    - Changed 200 OK

      * Changed **SchemaDefinitionRestDto** schema

        + Changed property **properties**

          - Changed schema of dictionary value:

            * Changed property **constraints**

              + Added property:  
                **disallowDangerousRegex**
            * Changed property **items**

              + Changed property **constraints**

                - Added property:  
                  **disallowDangerousRegex**
        + Changed property **types**

          - Changed schema of dictionary value:

            * Changed property **properties**

              + Changed schema of dictionary value:

                - Changed property **constraints**

                  * Added property:  
                    **disallowDangerousRegex**
                - Changed property **items**

                  * Changed property **constraints**

                    + Added property:  
                      **disallowDangerousRegex**
* `GET /settings/schemas/{schemaId}`

  + Return Type:

    - Changed 200 OK

      * Changed SchemaDefinitionRestDto schema

        + Changed property **properties**

          - Changed schema of dictionary value:

            * Changed property **constraints**

              + Added property:  
                **disallowDangerousRegex**
            * Changed property **items**

              + Changed property **constraints**

                - Added property:  
                  **disallowDangerousRegex**
        + Changed property **types**

          - Changed schema of dictionary value:

            * Changed property **properties**

              + Changed schema of dictionary value:

                - Changed property **constraints**

                  * Added property:  
                    **disallowDangerousRegex**
                - Changed property **items**

                  * Changed property **constraints**

                    + Added property:  
                      **disallowDangerousRegex**

### /settings/objects/

* `GET /settings/objects/{objectId}/permissions`

  + Return Type:

    - Changed 200 OK

      * Changed **AccessorPermissionsList** schema

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

          - Type changed from array to object

## Configuration API

### /calculatedMetrics/service/metricsOnGrail

New!

* `GET /calculatedMetrics/service/metricsOnGrail`
* `PUT /calculatedMetrics/service/metricsOnGrail/{metricKey}`

## Cluster API

### /cluster/

New!

* `POST /cluster/configuration/refresh`
* `GET /cluster/configuration/refresh/status/{requestId}`
* `GET /cluster/health/ipMigration`

### /settings/schemas/

* `GET /settings/schemas/{schemaId}`

  + Return Type:
  + Changed 200 OK

    - Changed **SchemaDefinitionRestDto** schema

      * Changed property **properties**

        + Changed schema of dictionary value:

          - Changed property **constraints**

            * Added property:  
              **disallowDangerousRegex**
          - Changed property **items**

            * Changed property **constraints**

              + Added property:  
                **disallowDangerousRegex**
      * Changed property **types**

        + Changed schema of dictionary value:

          - Changed property **properties**

            * Changed schema of dictionary value:

              + Changed property **constraints**

                - Added property:  
                  **disallowDangerousRegex**
              + Changed property **items**

                - Changed property **constraints**

                  * Added property:  
                    **disallowDangerousRegex**