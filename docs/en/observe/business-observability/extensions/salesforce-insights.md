---
title: Salesforce Insights
source: https://www.dynatrace.com/docs/observe/business-observability/extensions/salesforce-insights
scraped: 2026-02-17T21:21:36.137059
---

# Salesforce Insights

# Salesforce Insights

* Latest Dynatrace
* Extension
* 12-min read
* Updated on Oct 06, 2025

Salesforce Insights enables Salesforce administrators and IT operation teams to monitor their Salesforce environment.

## Setup

Learn how to set up Salesforce Insights and find out what kind of data it can capture.

Make sure to meet the following requirements to use the extension.

### Salesforce account

The Salesforce extension can capture four types of Salesforce data. Select each configuration for more details.

* The [Event Streaming](#event-streaming) configuration allows you to monitor the usage of your Salesforce CRM account.
* The [EventLogFile](#eventlog) configuration allows you to ingest log files from Salesforce into Dynatrace.
* The [API Queries](#soql) configuration allows you to ingest Salesforce Object Query Language (SOQL) data into Dynatrace. The data is ingested into Dynatrace as log events or Business Events.
* The [Platform Events](#platform-events) configuration allows you to subscribe to custom Salesforce Platform Events and ingest them as Business Events into Dynatrace.

### Authentication

Choose one of the three authentication methods that best suits your needs.

Connected App

User and Password

Client ID

In this mode the extension connects as a [connected appï»¿](https://dt-url.net/pv2c01v5). This is the recommended authentication mechanism.  
Technically, the app implements the [OAuth 2.0 JWT Bearer Flowï»¿](https://dt-url.net/yzs3qlb).

Dynatrace will ask for

* The **Consumer Key** of the connected app.
* The **Private Key** of the connected app.
* The **Subject** of the JWT tokenâthis is the username of a user that is part of a Profile in the connected app.

#### Requirements

* `openssl`âfor generating the certificate, not needed if you already have a certificate and a private key

  Note: on Windows, if you have `git` installed, you should also have a copy of `openssl`.  
  You should find it in a directory such as `C:\Program Files\Git\mingw64\bin` depending on your installation.

#### Certificate

The connected app must have a certificate that we later authenticate with Salesforce using this certificate's private key.

This command generates a certificate and a private key:

```
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out cert.pem
```

* The `cert.pem` file will be later added to the connected app.
* The `key.pem` file will be used by Dynatrace to authenticate with Salesforce.

#### Create the connected app

In Salesforce Lightning

1. Under **Setup** > **Apps** > **External Client Apps** > **Settings** make sure that `Allow creation of connected apps` is **On**.
2. Select **New Connected App**.

Name the app and add the contact email. Under **API (Enable OAuth Settings)**:

1. Check **Enable OAuth Settings**
2. If the Callback URL is not used, you can put in `http://localhost`
3. Check **Use digital signatures**
4. Upload the `cert.pem` file generated above under `Use digital signatures`.
5. In **Selected OAuth Scopes**, add these scopes:

   * **Manage use data via APIs (API)**
   * **Perform requests at any time (refresh\_token, offline\_access)**
6. Leave all other settings as default and select **Save**.

#### OAuth policy

1. Set up the **OAuth Policy** permitted users.
2. Under **Apps** > **App Manager**, Find the connected app and select **Manage**.
3. Click the **Edit Policies** button.
4. Under **OAuth Policies** select **Admin approved users are pre-authorized**.
5. Select **Save**.

#### Approved users

Identify users that can use the app. You can do it by adding Profiles to the **Application Profile Assignment** list.

1. On the connected app page, go to **Profiles** > **Manage Profiles**.
2. Add profiles that can use the connected app.
   Note: Later, any username from these profiles can be used as the **Subject** when configuring the extension.

Profiles need the following permissions for event streaming:

* General user permissions

  + `View Real-Time Event Monitoring Data`
* Administrative permissions

  + `Customize Application`
  + `View All Data`

To check the needed permissions documentation, see [how to Enable Access to Real-Time Event Monitoringï»¿](https://dt-url.net/5343qhf).

1. A regular Salesforce user with the permissions for the desired configuration (Event Streaming, Event Log File or SOQL).
2. The password for the user.
3. The [security tokenï»¿](https://dt-url.net/oz23qoo) for the user.

Note that this option is not recommended as user passwords and security tokens can change, it is usually used just to test the extension.

For [Client ID authenticationï»¿](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_client_credentials_flow.htm&type=5), select **Enable Client Credentials Flow** in the Connected App or the External Client App settings, and provide the **Consumer Key** and **Consumer Secret**.

You will also need to select a user to run the app as. Do this under **App Manager** > **Manage** > **Edit Policies** > **Client Credentials Flow** > **Run As**.

Note that this is not as secure as a Connected App with a certificate.

### Enable extension

To enable the Salesforce Extension, you must have an Environment ActiveGate.

1. Find the extension in Hub and activate it.
2. Select **Add monitoring configuration** on the Configuration page.
3. Select an ActiveGate group.

   * One of these servers will need to access the salesforce API, which is publicly available.
   * The login URLs are: `https://login.salesforce.com` or `https://test.salesforce.com`
   * The Pub/Sub endpoints are: `api.pubsub.salesforce.com:7443` or `api.deu.pubsub.salesforce.com:7443`
   * A proxy can be configured later if necessary.

The parameters for the monitoring configuration

| Parameter | Description |
| --- | --- |
| **Endpoint name** | Choose a helpful name to identify the endpoint |
| **Login URL** | Choose from [Productionï»¿](https://dt-url.net/lui3q3b) or [Sandboxï»¿](https://dt-url.net/okk3qle) |
| **Pub/Sub URL** | Choose from **Global Endpoint** or **Europe (Frankfurt) Endpoint** |
| **Reporting Mode** | **Business Events**, **Logs**, **OpenKit (RUM)** |
| **Custom Application ID** | The Dynatrace Custom Application ID for the app you created before (only needed if a managed environment is used and OpenKit is used as reporting mode.) |
| **Authentication type** | Choose from [username and password](#user-password-authentication) or [connected app](#connected-app-authentication) |
| **Events filtering** | Choose which real-time events you'd like to send to Dynatrace, by default all are enabled |
| **Usernames Blocklist** | Optional list of Usernames to ignore; use this to block automation/API users from reporting |
| **Proxy** | Optional proxy; in case the ActiveGate cannot connect to the Salesforce URLs |

OpenKit

If you use OpenKit, we recommend starting with the Custom Application setup.

## Salesforce Data Ingest

Choose one of the three data ingest methods based on your monitoring needs.

Event Streaming

EventLogFile

API Queries (SOQL)

Platform Events

Capture [real-time eventsï»¿](https://dt-url.net/fj03qyl) from Salesforce and send them as [Business Events](/docs/observe/business-observability/bo-basic-concepts "Basic concepts of Dynatrace Business Observability.") to Dynatrace.

[RUM ingest](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.") should only be used on Managed Environments.

1. Enable **Real-time event Streaming**.
2. In **Setup** > **Event Manager**, enable **Streaming Data** for the events you want to capture.
3. Obtain the credentials needed for the extension to connect to Salesforce.

Enable use cases such as:

* Track Session Hijack, Credential Stuffing and Anomaly Events
* Track important permission sets and changes
* What are the slowest Lightning or Classic pages response times?
* What files are being uploaded, downloaded, and by which user?
* What are the most used reports, who is running them, what queries are being used?
* What are the top API Queries being made?
* What browsers are users using?
* Where is Salesforce being accessed from?
* How many users are using the platform currently, what is the user experience?

The extension uses the [Salesforce Pub/Sub APIï»¿](https://dt-url.net/3843qs9) to list for Event Streaming Events. These events are captured and sent as Business events, or in case of OpenKit as **User Actions**, with all their respective properties sent as **Action Properties**.

For a detailed description of every event and their properties, see the [Salesforce documentationï»¿](https://dt-url.net/g1034yh).

### Currently captured events

| Events | Description |
| --- | --- |
| [ApiAnomalyEventï»¿](https://dt-url.net/ax63qn2) | Track anomalies in how users make API calls. |
| [ApiEventStreamï»¿](https://dt-url.net/1m83q6q) | Track user API queries in your organization. |
| [BulkApiResultEventï»¿](https://dt-url.net/ioc3q4t) | Track when a user downloads the results of a Bulk API request. |
| [ConcurLongRunApexErrEventï»¿](https://dt-url.net/19e3q2i) | Track when a Concurrent Long Running Apex error has occurred. |
| [CredentialStuffingEventï»¿](https://dt-url.net/avg3q25) | Track when a user successfully logs in to Salesforce during an identified credential stuffing attack. |
| [FileEventï»¿](https://dt-url.net/sui3q40) | Track file activity. For example, track when a user downloads or previews a file. |
| [LightningUriEventStreamï»¿](https://dt-url.net/bbk3quc) | Track when a user creates, accesses, updates, or deletes a record in Salesforce Lightning. |
| [ListViewEventStreamï»¿](https://dt-url.net/7a03qz2) | Track when a user accesses data with list views. |
| [LoginAsEventStreamï»¿](https://dt-url.net/o423qb0) | Track when an admin logs into your organization as another user. |
| [LoginEventStreamï»¿](https://dt-url.net/un43qqg) | Track when a user logs in to your organization. |
| [LogoutEventStreamï»¿](https://dt-url.net/7i63qh5) | Track when a user logs out in the Salesforce UI. |
| [PermissionSetEventï»¿](https://dt-url.net/ay83qje) | Track when users are assigned the Modify All Data or View All Data permission through a permission set. |
| [ReportAnomalyEventï»¿](https://dt-url.net/0ga3qkk) | Track anomalies in how users run or export reports. |
| [ReportEventStreamï»¿](https://dt-url.net/9vc3q8c) | Track when a user accesses or exports data with reports. |
| [SessionHijackingEventï»¿](https://dt-url.net/1fe3q8b) | Track when an unauthorized user gains ownership of a Salesforce userâs session with a stolen session identifier. |
| [UriEventStreamï»¿](https://dt-url.net/fig3qk1) | Track when a user creates, accesses, updates, or deletes a record in Salesforce Classic. |

The extension is limited to events that Salesforce produces as **Real-Time Events**.

Choose your reporting mode for Event Streaming data:

### Business Events

For business events, all data is ingested using the business events API.

It can be queried using DQL:

```
fetch bizevents



| filter event.type == "salesforce.ApiEventStream"
```

Visualization of a query result

![img.png](https://dt-cdn.net/images/query-event-streaming-1-1523-1e42763655.png)

Each of the events of type `salesforce.NameOfTheEvent` will have all properties documented by Salesforce.
For instance, see the [properties for an ApiEventStreamï»¿](https://dt-url.net/1m83q6q).

So we can create visualizations using all of these properties.

```
fetch bizevents



| filter event.type == "salesforce.ApiEventStream"



| summarize count(), by: {SourceIp}
```

Visualization of a query result

![img.png](https://dt-cdn.net/images/dql-event-streaming-visualization-1054-0ead02b872.png)

You can get a list of all event types with DQL:

```
fetch bizevents



| filter event.provider == "https://dynatrace--staging.sandbox.my.salesforce.com"



| summarize count(), by: {event.type}
```

Visualization of a query result

![img.png](https://dt-cdn.net/images/dql-event-streaming-event-types-1047-67bd7752e5.png)

#### Example: Get logins by user overtime

```
fetch bizevents



| filter event.type == "salesforce.LoginEventStream"



| makeTimeseries logins=count(), by:{Username}, interval: 5m



| sort logins desc
```

Visualization of a query result

![img.png](https://dt-cdn.net/images/dql-eventstreaming-users-1151-e4c2abe6c6.png)

### OpenKit

To create a custom application to receive the data:

1. In Hub, see **Digital Experience Monitoring** section. Then, select **Generic front end** > **Set up**.
2. Create your custom applicationâname it and choose an icon.
3. Select **Monitor custom application**.

![custom-app-01](https://dt-cdn.net/images/custom-app-01-1251-cec1d8931d.png)

4. In the **Custom application settings**, go to **Instrumentation wizard** and save the `Application ID` for later.

![custom-app-02](https://dt-cdn.net/images/custom-app-02-937-2cdaf63646.png)

5. Now you can enable the extension. For details, go back to the <#enable-extension> section.

The data is sent to the Frontend application that you created, so you can access:

* **Sessions Details**
* The individual properties, by selecting **User Action** > **Perform waterfall analysis**

To use these properties in [User Sessions Query Language](/docs/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more."):

1. In the application settings, go to **Session and user action properties**.
2. Create a property.
   Note: the Name must match exactly the property name, see [Salesforce eventsï»¿](https://dt-url.net/bbk3quc).

Example: Capture the rows number

![salesforce-data-04](https://dt-cdn.net/images/data-04-822-d25b8f5d10.png)

Querying the property:

```
SELECT useraction.name, SUM(longProperties.rowsprocessed) FROM useraction WHERE useraction.name STARTSWITH "Report" GROUP BY useraction.name
```

![salesforce-data-05](https://dt-cdn.net/images/data-05-1232-2127c34f50.png)

## EventLogFile

Capture [event log filesï»¿](https://dt-url.net/0a03q0q) from Salesforce and ingest them as [logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.") to Dynatrace.

* EventLogFile needs to be enabled in [Salesforceï»¿](https://dt-url.net/27u3qmr).
* The user must have set permissions to read event log files.

#### Details

1. Create a new EventLogFile configuration by selecting **Configure EventLogFile**.  
   Note that under **Events to capture** all the different Log Files will be disabled by default.
2. Select which log files you would like to ingest.

Do not expect real-time data out of this configuration. Event Log data is [delayed by several hoursï»¿](https://dt-url.net/aqm3qh5) in Salesforce.

#### Visualization

The events are sent as Log Events to Dynatrace, and can be queries using DQL:

```
fetch logs



| filter query.type == "EventLogFile"
```

Visualization of a query result

![img.png](https://dt-cdn.net/images/dql-eventlogfile-1-1058-92cd80e16c.png)

Every property for a certain Event Log File will be available.  
To find fields details, see [EventLogFile Supported Event Typesï»¿](https://dt-url.net/0a03q0q).

#### Example

Get details about `ApexExecution` events:

```
fetch logs



| filter EVENT_TYPE == "ApexExecution"



| fields TIMESTAMP_DERIVED, ENTRY_POINT, EXEC_TIME, CPU_TIME, DB_TOTAL_TIME, NUMBER_SOQL_QUERIES
```

Visualization of a query result

![img.png](https://dt-cdn.net/images/dql-eventlogfile-2-1144-a972a14519.png)

## API Queries (SOQL)

Run [SOQL queriesï»¿](https://dt-url.net/ox23q6n) against Salesforce and ingest the data as [logs](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.") or Business Events.
The user must have permissions to query the Salesforce API, and read the **Objects** that are being queried.

#### Details

To ingest Salesforce Object Query Language (SOQL) data into Dynatrace,

1. Select **Configure API queries**.
2. Add up to 100 SOQL queries to be executed at the specified interval.
   Each query has the following parameters:

   * **Query Name**âA name for the query that will help you locate this query data later in Dynatrace Logs.
   * **Query**âThe SOQL query to be executed.

     + The query **must** contain at least one datetime field.
     + The placeholder `{last_execution_timestamp}` **must** be used to filter the query results and deduplicate the data.
     + Example: `SELECT Id, CreatedDate, Field, NewValue, OldValue FROM OpportunityFieldHistory WHERE CreatedDate > {last_execution_timestamp}`
   * **Frequency**

     + The frequency can be of type **Interval** or **Cron**.
     + **Interval**âThe query will be every X minutes.
     + **Cron**âThe query will be executed based on the cron expression provided, you can use [crontab guruï»¿](https://dt-url.net/j0o3qxt) to generate the cron expression.

#### Visualization

Let's consider this query configuration:

```
Query Name: Logins



Query: SELECT UserId, COUNT(Id) from LoginHistory WHERE LoginTime > {last_execution_timestamp} GROUP BY UserId
```

![img.png](https://dt-cdn.net/images/query-logins-607-41fe169e79.png)

The results can be obtained with the DQL:

```
fetch logs



| filter query.name == "Logins"
```

Visualization of a query result

![img.png](https://dt-cdn.net/images/dql-api-query-1577-d62b4ba57b.png)

And a chart could be created with:

```
fetch logs



| filter query.name == "Logins"



| makeTimeseries sum(toDouble(expr0)), by: {UserId}, interval: 5m
```

Visualization of a query result

![img.png](https://dt-cdn.net/images/dql-api-query-chart-1139-89bb9c3aa6.png)

You can also fetch all the queries and their text configured for this Salesforce instance:

```
fetch logs



| filter event.provider == "https://dynatrace--staging.sandbox.my.salesforce.com"



| summarize count(), by: {query.name}
```

Visualization of a query result

![img.png](https://dt-cdn.net/images/dql-all-queries-1140-350b2a1991.png)

## Platform Events

Subscribe to custom [Salesforce Platform Eventsï»¿](https://developer.salesforce.com/docs/atlas.en-us.250.0.platform_events.meta/platform_events/platform_events_intro.htm) and ingest them as [Business Events](/docs/observe/business-observability/bo-basic-concepts "Basic concepts of Dynatrace Business Observability.") to Dynatrace.

Platform Events provide a powerful way to send and receive custom event notifications within Salesforce and to external systems. This configuration allows you to capture real-time event data from custom platform events, standard platform events, and change data capture events.

#### Details

To ingest Salesforce Platform Events into Dynatrace:

1. Select **Configure Platform Events**.
2. Add the topics you want to subscribe to. Topics follow these formats:

   * **Custom Platform Events**: `/event/YourCustomEvent__e`
   * **Standard Platform Events**: `/event/LoginEventStream`, `/event/LogoutEventStream`
   * **Change Data Capture**: `/data/ChangeEvents`, `/data/AccountChangeEvent`
3. Configure authentication using one of the supported methods (Connected App, User and Password, or Client ID).

#### Use Cases

Enable use cases such as:

* Monitor custom business processes and workflows
* Track changes to critical Salesforce objects with Change Data Capture
* Integrate with external systems using custom Platform Events
* Build real-time dashboards and alerts based on Salesforce events
* Correlate Salesforce events with other observability data

#### Visualization

Platform Events are sent as Business Events to Dynatrace and can be queried using DQL:

```
fetch bizevents



| filter event.type == "salesforce.YourCustomEvent__e"
```

Example: Query all Platform Events from a Salesforce instance

```
fetch bizevents



| filter event.provider == "https://yourinstance.my.salesforce.com"



| summarize count(), by: {event.type}
```

Each Platform Event will include all custom fields defined on the event, making them available for filtering, grouping, and visualization.

## Extend the retention period for Salesforce Insights data

By default, your ingested data is stored for 30 days. You can adjust the retention time by creating a custom [bucket](/docs/observe/business-observability/bo-event-processing/bo-bucket-assignment "Assign a retention period to business event data in Dynatrace via the classic pipeline.").

To create a custom bucket for a Salesforce event

1. In Dynatrace, go to **Settings** > **Business Observability** > **Bucket assignment**.
2. On the **Business event bucket assignment** page, select **Add rule** and name your rule.
3. In the **Bucket** field, choose your retention period.
4. Add a **Matcher** to your rule by typing or pasting your [matcher-specific DQL query](/docs/observe/business-observability/bo-event-processing/bo-events-processing-matcher "This is the DQL matcher in events in the classic pipeline ."). Events that match your rule will be assigned to your selected bucket. If no rules match, events will be assigned to the default bucket. To assign all your Salesforce events to your bucket, you need to use the matcher containing the `matchesValue` function and your Salesforce URL, as in the example below.

   ```
   matchesValue(event.provider, "https://environment.my.salesforce.com")
   ```
5. Select **Save changes**.

## Troubleshooting

Error logs can be obtained via Dynatrace, by navigating to the Extension page, and selecting **Status** for each monitoring configuration.

Detailed logs can be obtained by creating an [ActiveGate Diagnosis](/docs/ingest-from/dynatrace-activegate/activegate-diagnostics "Learn how to run ActiveGate diagnostics").