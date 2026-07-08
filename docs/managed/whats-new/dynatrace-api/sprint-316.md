---
title: Dynatrace API changelog version 1.316
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-316
---

# Dynatrace API changelog version 1.316

# Dynatrace API changelog version 1.316

* Release notes
* Updated on Jun 06, 2025

Rollout start: Jun 3, 2025

## Environment API

### /synthetic/locations

* `GET /synthetic/locations`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticLocations** schema

        + Changed property **locations**

          - Added property:  
            **nodes**

* `GET /synthetic/locations/{locationId}/yaml` Early Access

  + Parameter:

    - Delete platform in query

### Deprecated for SaaS and Managed

* `DELETE /entities/securityContext`
* `POST /entities/securityContext`

### Deprecated for Managed

* `/timeseries`

## Cluster API

### /elastic/checkNodesVisibility

New!

* `POST /elastic/checkNodesVisibility`

### /activeGates

* `GET /activeGates`

  + Parameter:

    - Changed **osArchitecture** in query

      * Added enum value:  
        `PPCLE`
  + Return Type:

    - Changed 200 OK

      * Changed **ActiveGateList** schema

        + Changed property **activeGates**

          - Changed property **osArchitecture**

            * Added enum value:  
              `PPCLE`
* `GET /activeGates/{agId}`

  + Return Type:

    - Changed 200 OK

      * Changed **ActiveGate** schema

        + Changed property **osArchitecture**

          - Added enum value:  
            `PPCLE`

### /synthetic/locations

* `GET /synthetic/locations`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticLocations** schema

        + Changed property **locations**

          - Added property:  
            **nodes**

* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Added properties:  
        **maxActiveGateCount**  
        **minActiveGateCount**  
        **nodeSize**
* `PUT /synthetic/locations/{locationId}`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Added properties:  
        **maxActiveGateCount**  
        **minActiveGateCount**  
        **nodeSize**

## Settings API

### Deprecated for SaaS and Managed

* Security context settings schema (`builtin:security-context`)

### Deprecated for Managed

* Grail security context for monitored entities settings schema (`builtin:monitoredentities.grail.security.context`)
* Log security context settings schema (`builtin:logmonitoring.log-security-context-rules`)
* Business event security context settings schema (`builtin:bizevents-security-context-rules`)