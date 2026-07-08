---
title: Dynatrace API changelog version 1.303
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-api/sprint-303
---

# Dynatrace API changelog version 1.303

# Dynatrace API changelog version 1.303

* Release notes
* Published Oct 24, 2024

Rollout start: Oct 21, 2024

## Environment API

### /entity/infrastructure/process-groups

* `GET /entity/infrastructure/process-groups`

  + Return Type:

    - Changed 200 OK

      * Changed null schema

        + Changed property **metadata**

          - Added properties:  
            **osagent.groupIdName**  
            **osagent.instanceIdName**
* `GET /entity/infrastructure/process-groups/{meIdentifier}`

  + Return Type:

    - Changed 200 OK

      * Changed **ProcessGroup** schema

        + Changed property **metadata**

          - Added properties:  
            **osagent.groupIdName**  
            **osagent.instanceIdName**

### /entity/infrastructure/processes

* `GET /entity/infrastructure/processes`

  + Return Type:

    - Changed 200 OK

      * Changed null schema

        + Changed property **metadata**

          - Added properties:  
            **osagent.groupIdName**  
            **osagent.instanceIdName**
* `GET /entity/infrastructure/processes/{meIdentifier}`

  + Return Type:

    - Changed 200 OK

      * Changed **ProcessGroupInstance** schema

        + Changed property **metadata**

          - Added properties:  
            **osagent.groupIdName**  
            **osagent.instanceIdName**

### /oneagents/autoUpdateProblems

* `GET /oneagents/autoUpdateProblems` Early Access

  + Return Type:

    - Changed 200 OK

      * Changed **AgentPotentialProblemsState** schema

        + Changed property **autoUpdateProblems**

          - Added property:  
            **architecture**

### /synthetic/locations

* `POST /synthetic/locations`

  + Request:

    - Changed **PrivateSyntheticLocation** schema

      * Added properties:  
        **countryName**  
        **regionName**
* `GET /synthetic/locations/{locationId}`

  + Return Type:

    - Changed 200 OK

      * Changed **SyntheticLocation** schema

        + Added properties:  
          **countryName**  
          **regionName**

### /credentials

* `GET /credentials`

  + Parameter:

    - Changed type in query

      * Added enum values:
        `AWS_MONITORING_KEY_BASED`  
        `AWS_MONITORING_ROLE_BASED`
      * Removed enum values:  
        `AWS_KEY_BASED`  
        `AWS_ROLE_BASED`
* `POST /credentials`

  + Request:

    - Changed **Credentials** schema ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

      * Changed property **type**

        + Added enum values:
          `AWS_MONITORING_KEY_BASED`  
          `AWS_MONITORING_ROLE_BASED`
        + Removed enum values:  
          `AWS_KEY_BASED`  
          `AWS_ROLE_BASED`
* `PUT /credentials/{id}`

  + Request:

    - Changed **Credentials** schema ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Breaking change

      * Changed property **type**

        + Added enum values:
          `AWS_MONITORING_KEY_BASED`  
          `AWS_MONITORING_ROLE_BASED`
        + Removed enum values:  
          `AWS_KEY_BASED`  
          `AWS_ROLE_BASED`

## Configuration API

### /extensions/

* `GET /extensions/{technology}/availableHosts` Early Access

  + Parameter:

    - Changed technology in path

      * Added enum values:  
        `CLR`  
        `OWIN_KATANA`  
        `WCF`

### /service/requestAttributes

* `POST /service/requestAttributes`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `CLR`  
              `OWIN_KATANA`  
              `WCF`
* `POST /service/requestAttributes/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `CLR`  
              `OWIN_KATANA`  
              `WCF`
* `GET /service/requestAttributes/{id}`

  + Return Type:

    - Changed 200 OK

      * Changed **RequestAttribute** schema

        + Changed property **dataSources**

          - Changed property **scope**

            * Changed property **serviceTechnology**

              + Added enum values:  
                `CLR`  
                `OWIN_KATANA`  
                `WCF`
* `PUT /service/requestAttributes/{id}`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `CLR`  
              `OWIN_KATANA`  
              `WCF`
* `POST /service/requestAttributes/{id}/validator`

  + Request:

    - Changed **RequestAttribute** schema

      * Changed property **dataSources**

        + Changed property **scope**

          - Changed property **serviceTechnology**

            * Added enum values:  
              `CLR`  
              `OWIN_KATANA`  
              `WCF`

## Related topics

* [SaaS Release Notes 1.303﻿](https://docs.dynatrace.com/docs/shortlink/release-notes-saas-sprint-303)