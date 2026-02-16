---
title: ServiceNow
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/service-now
scraped: 2026-02-16T21:21:36.675105
---

# ServiceNow

# ServiceNow

* Latest Dynatrace
* 7-min read
* Updated on Nov 18, 2025

Your Dynatrace environment can integrate with a ServiceNow environment using ServiceNow Connector ![ServiceNow for Workflows](https://dt-cdn.net/images/servicenow-for-workflows-257-9349ea0329.png "ServiceNow for Workflows"), enabling you to create incidents based on your monitoring data and events automatically.
Furthermore, you can retrieve groups from ServiceNow and import them as [Ownership teams](/docs/deliver/ownership/ownership-teams#import-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.").

## Configure the integration

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Grant permissions to Workflows**](/docs/analyze-explore-automate/workflows/actions/service-now#permissions "Automate creation of incidents in ServiceNow based on your monitoring data and events.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create ServiceNow authentication credentials**](/docs/analyze-explore-automate/workflows/actions/service-now#authentication "Automate creation of incidents in ServiceNow based on your monitoring data and events.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure ServiceNow connection**](/docs/analyze-explore-automate/workflows/actions/service-now#connection "Automate creation of incidents in ServiceNow based on your monitoring data and events.")

### Step 1 Grant permissions to Workflows

Some permissions are required by Workflows to run actions on your behalf. Other permissions are required by actions that come bundled with ServiceNow Connector itself.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** and select **Settings** > **Authorization settings**.
2. Select the following permissions besides the general Workflows permission.

   * Permissions needed for ServiceNow workflow actions:

     + `app-settings:objects:read`

For more on general Workflows user permissions, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

### Step 2 Create ServiceNow authentication credentials

Sign in to your ServiceNow instance and create basic authentication credentials with the following permissions. You will need these credentials in the next step.

ServiceNow user permissions:

* Search, create and update incidents (table incident)
* Read categories (table sys\_choice, element category)
* Read subcategories (table sys\_choice, element subcategory)
* Read assignment groups (table sys\_user\_group)
* Read resolution codes (table sys\_choice, element close\_code)

### Step 3 Configure ServiceNow connection

You need a configured connection for each of your ServiceNow environments.

To configure a connection

1. Go to **Settings** and select **Connections** > **Connectors** > **ServiceNow**.
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Connection**
3. Describe your ServiceNow connection.

   * **Connection name**: Provide a meaningful name for your connection.
   * **ServiceNow Instance URL**: Add the URL of your ServiceNow environment.
   * **Type** Either use basic authentication or client credentials.

     + For **Basic Authentication**, provide your username and password.
     + For **Client Credentials**, provide your client id and client secret.
4. Select **Create**.

## Available actions

The following workflow actions are available for the ServiceNow integration. Each action corresponds to an endpoint of the ServiceNow API.

Action

Description

ServiceNow API endpoint

**Create Incident**

Creates an incident in your ServiceNow environment. An incident represents a problem or an issue that needs to be addressed and resolved.

`POST /api/now/v2/table/incident`

**Create a vulnerability item**

Creates a vulnerability item in your ServiceNow environment.

`POST /api/now/v2/table/sn_vul_vulnerable_item`

**Get Groups**

Get groups from your ServiceNow environment.

`GET /api/now/v2/table/sys_user_group`

**Comment**

Create a comment on an entry in your ServiceNow environment.

`PUT /api/now/v2/table/${tableName}/${sysId}`

**Comment on an incident**

Add a new comment to a ServiceNow incident record.

`PUT /api/now/v2/table/incident/${sys_id}`

**Search**

Generic search action that allows searching your ServiceNow environment.

`GET /api/now/v2/table/${tableName}`

**Search incidents**

Query ServiceNow to retrieve a list of incidents matching specified criteria.

`GET /api/now/v2/table/incident`

**Resolve incident**

Update a ServiceNow incident to mark it as resolved.

`PUT /api/now/v2/table/incident/${sys_id}`

**Create record**

Create a new record in a specified ServiceNow table.

`POST /api/now/v2/table/${tableName}`

**Update record**

Update an existing record in a specified ServiceNow table.

`PUT /api/now/v2/table/${tableName}/${sys_id}`

## Create a ServiceNow incident

To raise a ServiceNow incident in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Create Incident**.
2. In the **Create Incident** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Correlation ID** | Unique identifier (in most cases, this is the Dynatrace event ID). | Optional |
   | **Caller** | The user who reports the incident. | Optional |
   | **Category** | The category of the incident. Category options are derived by querying the `sys_choice` table with `sysparm_query: 'name=incident^element=category^inactive=false'`. | Required |
   | **Subcategory** | The subcategory of the incident. Subcategory options are derived by querying the `sys_choice` table with `sysparm_query: 'name=incident^element=subcategory^inactive=false^dependent_value=${category}'`. | Required |
   | **Impact** | The impact of the incident. | Required |
   | **Urgency** | The urgency of the incident. | Required |
   | **Assignment Group** | The group that will work on the incident. Assignment groups options are derived by querying the `sys_user_group` table with `sysparm_display_value: 'all'`. | Required |
   | **Configuration item** | The affected entity. | Optional |
   | **Short description** | A brief description of the incident. | Optional |
   | **Description** | A detailed description of the incident. | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Create a vulnerability item in ServiceNow

To create a ServiceNow vulnerability item in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Create a vulnerability item**.
2. In the **Create a vulnerability item** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **External ID** | ID which is associated with the vulnerable item | Optional |
   | **Description** | A detailed description of the vulnerability item | Optional |
   | **Short description** | A brief description of the vulnerability item | Optional |
   | **Risk score** | The risk score of the vulnerability item | Optional |
   | **Risk rating** | The risk rating of the vulnerability item | Optional |
   | **Source** | The source which detected the vulnerable item | Optional |
   | **Source risk score** | The risk score in the source system of the vulnerability item | Optional |
   | **Configuration item** | The affected entity | Optional |
   | **First found** | The date of the detection | Optional |
   | **Priority** | The priority of the vulnerability item | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Get Groups from ServiceNow

To fetch groups from ServiceNow in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Get Groups**.
2. In the **Get Group** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **SysParm Query** | An encoded query used to filter the result set | Optional |
   | **Limit** | Maximum number of results to return (Default: 100) | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Create comment in ServiceNow

To create a comment on an entry in a ServiceNow table in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Create Comment**.
2. In the **Create Comment** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Table** | The table name of the entry to comment on | Required |
   | **Unique record identifier (sys\_id)** | The sys\_id of the entry to comment on | Required |
   | **Comment** | The comment that will be created | Required |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Comment on an incident in ServiceNow

To comment on an incident in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Comment on an incident**.
2. In the **Comment on an incident** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Incident Number** | The number of the incident to comment on | Required |
   | **Comment** | The comment that will be created | Required |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Search in ServiceNow

To search ServiceNow in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Search**.
2. In the **Search** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Table** | Select the table in which to search | Required |
   | **SysParm Query** | An encoded query used to filter the result set | Optional |
   | **SysParm Fields** | Comma-separated list of fields that limit the result | Optional |
   | **Query category** | Category to filter search results. | Optional |
   | **Limit** | Maximum number of results to return (Default: 100) | Optional |
   | **Offset** | Records to skip (Default: 0) | Optional |
   | **Order by asc** | Field name to sort results in ascending order | Optional |
   | **Order by desc** | Field name to sort results in descending order | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Search incidents in ServiceNow

To search for incidents in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Search incidents**.
2. In the **Search incidents** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **SysParm Query** | An encoded query used to filter the result set | Optional |
   | **SysParm Fields** | Comma-separated list of fields that limit the result | Optional |
   | **Limit** | Maximum number of results to return (Default: 100) | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Resolve incident in ServiceNow

To resolve an incident in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Resolve incident**.
2. In the **Resolve incident** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Incident Number** | The number of the incident to resolve | Required |
   | **Resolution Notes** | Add notes for the resolution of the incident | Required |
   | **Resolution Code** | The close code for the resolution | Required |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Create record

To create a record in a ServiceNow Table from your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Create Record**.
2. In the **Create Record** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Table** | The name of the table in which to create a record | Required |
   | **Payload Fields** | Key-value pairs of table field names and their values | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Update record

To update a record in ServiceNow from your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Update Record**.
2. In the **Update Record** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Table** | The name of the table in which to create a record | Required |
   | **Unique record identifier (sys\_id)** | The sys\_id of the entry to comment on | Required |
   | **Payload Fields** | Key-value pairs of table field names and their values | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Troubleshooting

The following is a solution to a problem some people have.

* [ServiceNow for Workflows: Insufficient permissions errorï»¿](https://dt-url.net/hj637wm)