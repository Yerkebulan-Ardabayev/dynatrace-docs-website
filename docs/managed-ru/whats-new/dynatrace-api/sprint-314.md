---
title: Журнал изменений Dynatrace API версии 1.314
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-314
scraped: 2026-05-12T11:36:15.242872
---

# Журнал изменений Dynatrace API версии 1.314

# Журнал изменений Dynatrace API версии 1.314

* Заметки о выпуске
* Published May 08, 2025

Rollout start: May 6, 2025

## Environment API

### /extensions/

* `GET /extensions/{extensionName}/environmentConfiguration/assets`

  + Return Type:

    - Changed 200 OK

      * Changed **ExtensionAssetsDto** schema

        + Changed property **assets**

          - Changed property **type**

            * Added enum value:  
              `PROCESS_GROUPING_RULES`

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

* `GET /extensions/{extensionName}/{extensionVersion}/schema`

  + Security Requirements:

    - Changed

      * from `[ssoAuth=[environment-api:extension-configurations:read]]`
      * to `[ssoAuth=[environment-api:extensions:read]]`
  + Extensions:

    - Token scopes changed from `[extensionConfigurations.read]` to `[extensions.read]`

## Cluster API

### Новые эндпоинты

* `GET /cassandra/cluster/isNodeFullyConnected/{nodeIpToCheck}`
* `GET /cluster/clusterMultiDatacenterMigrationState`
* `GET /cluster/clusterState`
* `GET /cluster/configuration/validate`
* `POST /cluster/migrateIp`

### Удалённые эндпоинты

* `POST /cluster/configuration/refresh`
* `GET /cluster/configuration/refresh/status/{requestId}`
* `GET /cluster/health/ipMigration`

### Изменённые эндпоинты

* `POST /cluster/configuration`

  + Request:

    - Changed **ClusterNodesConfigDtoNodeResponsibilitiesConfigDto** schema

      * Changed property **clusterNodes**

        + Removed properties:  
          **datacenter**  
          **kubernetesRole**
* `POST /elastic/reloadEsClientOnAllNodes`

  + Request:

    - Changed **ClusterNodesConfigDtoNodeConfigDto** schema

      * Changed property **clusterNodes**

        + Added property:  
          **ipAddress**
* `POST /firewallManagement/addClusterNode`

  + Request:

    - Changed **NodeConfigDto** schema

      * Added property:  
        **ipAddress**
* `GET /firewallManagement/clusterNodes`

  + Return Type:

    - Changed 200 OK

      * Changed **ClusterNodesConfigDto** schema

        + ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Несовместимое изменение

          - Changed property **clusterNodes**

            * Removed properties:  
              **agent**  
              **datacenter**  
              **kubernetesRole**  
              **webUI**

* `POST /iam/resolution/{level-type}/{level-id}/effectivepermissions:dry-run`

* `GET /settings/schemas/{schemaId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SchemaDefinitionRestDto** schema

        + Changed property **schemaConstraints**

          - Added property:  
            **byteLimit**
          - Changed property **type**

            * Added enum value:  
              `BYTE_SIZE_LIMIT`