---
title: Unified analysis tutorial
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-tutorial
---

# Unified analysis tutorial

# Unified analysis tutorial

* 5-min read
* Published Apr 19, 2023

This is a step-by-step tutorial on how to upload the custom topology to your Dynatrace environment and build an extension to define the topology types and relationships between them.

You can then define your unified analysis pages to analyze data from multiple sources, including logs, metrics, and traces in a unified view. You can also include various data sources and dimensions, apply filters, and drill down into specific details.

## Prerequisites

* Dynatrace CLI

  + Python 3.8 or 3.9
  + Access to pip package installer for Python
  + Install dt-cli

    ```
    pip install dt-cli
    ```

    For more information, see [Sign extensions](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").
* Token with the following permissions:

  + **Read credential vault entries** (`credentialVault.read`)
  + **Write credential vault entries** (`credentialVault.write`)
  + **Read entities** (`entities.read`)
  + **Write entities** (`entities.write`)
  + **Ingest events** (`events.ingest`)
  + **Ingest metrics** (`metrics.ingest`)
  + **Ingest logs** (`logs.ingest`)
  + **Read extensions** (`extensions.read`)
  + **Write extensions** (`extensions.write`)

## Upload sample observability data to your environment

In this example, we use **Easy Taxis Fleet Simulator**—an interactive CLI app that simulates a fleet of smart taxis sending observability data to the Dynatrace environment.

1. Based on your operating system, download the appropriate file from the list of [EasyTaxis executables﻿](https://dt-url.net/13434et) and run it.
2. Type `help` to list all available commands.
3. Use the command below to start up the fleet simulation.

   ```
   start -e <your-environment-url> -t <your-api-token>
   ```

   Be sure to replace `<your-environment-url>` and `<your-api-token>` with the actual values.

   For more information about the arguments and flags, use `start help` command.

The simulation ingests metrics, logs, and events to your Dynatrace environment.

## Build and upload the extension

1. Go to the GitHub page and download the [Observability Clinic Materials﻿](https://dt-url.net/sl034x0).
2. Open the `extensions-project-starter` folder in your preferred code environment.
3. Go to the `scripts` folder and open the `config.yaml` file. You need to complete three mandatory fields with your environment URL, token, and schema version.

   ```
   tenant_url: <your-environment-url>



   api_token: <your-api-token>



   schema_version: 1.265
   ```
4. From the `scripts` directory, execute the following command to generate certificates.

   ```
   python initialize.py
   ```

   The generated certificates now can be found in the `certs` folder.
5. Execute the following command to download the schemas for version 1.265.

   ```
   python download_schemas.py
   ```
6. Go to the `extension` folder and create the `extension.yaml` file. For more information about extension scope, see [Extension YAML file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml#start-extension-yaml-file "Learn how to create an extension YAML file using the Extensions framework.").
7. Use the following extension example of the defined topology. For more information about topology scope, see [WMI tutorial - custom topology](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-04 "Learn about WMI extensions in the Extensions framework.").

   ```
   name: custom:ua.example



   version: 1.0.0



   minDynatraceVersion: "1.238"



   author:



   name: Joe Doe



   topology:



   types:



   - enabled: true



   name: easytaxis:smart_fleet



   displayName: Smart Fleet



   rules:



   - idPattern: fleet_{fleet.id}



   instanceNamePattern: Smart Fleet ({fleet.id})



   iconPattern: cluster



   sources:



   - sourceType: Metrics



   condition: $prefix(custom.easytaxis.fleet)



   attributes:



   - key: FleetID



   pattern: "{fleet.id}"



   - key: Location



   pattern: "{fleet.location}"



   role: default



   - idPattern: fleet_{fleet.id}



   instanceNamePattern: Smart Fleet ({fleet.id})



   iconPattern: cluster



   sources:



   - sourceType: Metrics



   condition: $prefix(custom.easytaxis.taxi)



   - sourceType: Logs



   role: default



   - enabled: true



   name: easytaxis:smart_taxi



   displayName: Smart Taxi



   rules:



   - idPattern: taxi_{fleet.id}_{taxi.id}



   instanceNamePattern: Smart Taxi ({taxi.id})



   sources:



   - sourceType: Metrics



   condition: $prefix(custom.easytaxis.taxi)



   attributes:



   - key: TaxiID



   pattern: "{taxi.id}"



   - key: RegistrationNumber



   pattern: "{taxi.registration}"



   - key: Class



   pattern: "{taxi.class}"



   role: default



   relationships:



   - enabled: true



   sources:



   - sourceType: Metrics



   condition: $prefix(custom.easytaxis)



   fromType: easytaxis:smart_taxi



   typeOfRelation: CHILD_OF



   toType: easytaxis:smart_fleet
   ```
8. Execute the following command to sign the extension and upload it to the environment.

   ```
   python build_and_upload.py
   ```

## Verify your progress

If you now go to **Settings** > **Topology model** > **Generic types**, you'll see that the **Smart Fleet** and **Smart taxi** types have been created. You can also see the defined relationship between them in the **Generic relationships** section.

* For a list of Smart Fleet instances, go to `<your-environment>/ui/entity/list/easytaxis:smart_fleet`.

  ![Smart Fleet instance](https://dt-cdn.net/images/smart-fleet-1239-e7365be7f8.png)

  Smart Fleet instance
* For a list of Smart Taxi instances, go to `<your-environment>/ui/entity/list/easytaxis:smart_taxi`.

  ![Smart Taxi instance](https://dt-cdn.net/images/smart-taxi-1231-2e3fcf1c19.png)

  Smart Taxi instance

## Configure unified analysis pages

You can now customize your entity pages by creating a page definition in the `extension.yaml` file.

```
screens:



- entityType: easytaxis:smart_fleet



detailsSettings:



staticContent:



showProblems: true



showProperties: true



showTags: true



showGlobalFilter: true



showAddTag: true



layout:



autoGenerate: false



cards:



- type: ENTITIES_LIST



key: fleet-list-taxis



entitiesListCards:



- key: fleet-list-taxis



displayName: Taxis part of this fleet



pageSize: 5



entitiesLimit: 500



displayCharts: false



enableDetailsExpandability: true



numberOfVisibleCharts: 2



displayIcons: true



entitySelectorTemplate: type(easytaxis:smart_taxi),fromRelationships.isChildOf($(entityConditions))



columns:



- type: ATTRIBUTE



attribute:



key: Class



displayName: Class



- type: ATTRIBUTE



attribute:



key: RegistrationNumber



displayName: Registration



charts:



- displayName: Engine Temperature



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: custom.easytaxis.taxi.engine.temperature



visualizationType: GRAPH_CHART



- displayName: Speed



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: custom.easytaxis.taxi.speed



visualizationType: GRAPH_CHART



- entityType: easytaxis:smart_taxi



propertiesCard:



properties:



- type: RELATION



relation:



entitySelectorTemplate: type(easytaxis:smart_fleet),toRelationships.isChildOf($(entityConditions))



displayName: Mother Fleet



detailsSettings:



staticContent:



showTags: true



showProperties: true



showProblems: true



showAddTag: true



showGlobalFilter: true



layout:



autoGenerate: false



cards:



- type: CHART_GROUP



key: taxi-metrics



chartsCards:



- key: taxi-metrics



displayName: Smart Taxi Metrics



numberOfVisibleCharts: 3



charts:



- displayName: Engine Temperature



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: custom.easytaxis.taxi.engine.temperature



visualizationType: GRAPH_CHART



- displayName: Speed



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: custom.easytaxis.taxi.speed



visualizationType: GRAPH_CHART



- displayName: Days to revision



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: custom.easytaxis.taxi.engine.daystorevision



visualizationType: GRAPH_CHART



listSettings:



staticContent:



showGlobalFilter: true



layout:



autoGenerate: true
```

* For the Smart Taxi entity, this definition includes three charts with data on speed, engine temperature and days to revision.

  Smart Taxi entity page

  ![UA page example](https://dt-cdn.net/images/screenshot-2023-04-19-at-6-32-21-pm-1061-c102f4ffd1.png)

  UA page example
* For the Smart Fleet entity, this definition includes the list of the taxis that are a part of this fleet. You can expand each taxi entity and see two graphs with speed and engine temperature data.

  Smart Fleet entity page

  ![Smart fleet example](https://dt-cdn.net/images/fleet-1-1455-ccb222479c.png)

  Smart fleet example

  ![Smart fleet expand](https://dt-cdn.net/images/fleet-2-1417-2b62cf52f0.png)

  Smart fleet expand

## Related topics

* [About Extensions](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.")