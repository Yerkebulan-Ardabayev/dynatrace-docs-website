---
title: Service detection rules
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection
scraped: 2026-02-16T09:23:44.187862
---

# Service detection rules

# Service detection rules

* How-to guide
* 15-min read
* Updated on Oct 21, 2025

When monitoring with OneAgent, your deployed applications and related microservices are automatically detected by Dynatrace, based on specific properties of your application deployment and configuration, such as the application identifier, part of the URL, or the server name.

Attributes used for detection are marked with an asterisk â± on the [service](/docs/observe/application-observability/services-classic/service-analysis-new "Learn about all the service monitoring details that Dynatrace can provide.") overview page, under **Properties and tags**.

In certain cases, the quality of data available to Dynatrace might be insufficient for high-precision service detection. To tailor out-of-the-box detection to your environment, you can create new rules or setup improvements.

## Manage rule-based service detection

You can use transformation rules, for example, to remedy the following use cases:

* If the web Application IDs contain the version or build date, you can define a rule that removes the build date/ID from the web application ID.
* When server names are not properly defined in the underlying deployment (for example, with Apache HTTP or Nginx in AWS environments), you can define a stable web server name and therefore a stable cluster service containing all instances.
* You can correct the misuse of the context root in the deployed application.

  A typical web server has a concept called the context root to separate services based on the URL. For some technologies, such as Node.js, the context root is not available or it's improperly defined. You can superimpose the context root, and create separate services for each of your applications, instead of a single service containing multiple applications.
* You can ignore the port for service detection. This is helpful when the port is used dynamically, for example, in Node.js applications.

Additionally, the rules can be exported and imported from one environment to another.

Detection rules are evaluated from top to bottom, and the first matching rule applies, so be sure to place your rule in the correct position on the list.

### Prerequisites

* Familiarize yourself with the notion of a [full and external (opaque) request](/docs/discover-dynatrace/get-started/glossary#request "Get acquainted with Dynatrace terminology.").
* API onlyRequired To be able to configure rule-based service detection via the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."), you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

### Create a rule

When you define a new rule, depending on the configuration, the original services might get less traffic or no traffic at all. New monitoring data is then redirected according to the rule configuration, between the original and the newly detected services.

via web UI

via API

To define a new service detection rule via web UI

1. Go to **Settings**.
2. Expand **Service Detection** and select a request type (**Full web request rules** or **Full web service rules**, or **External web request rules** or **External web service rules**).
3. Select **Add item** and start configuring the parameters of the new rule.

   1. Type a **Rule name**.
   2. To change the service detection's behavior, enable at least one of the service identifier contributors, so that the rule's triggered.
   3. To target the rule application, in the **Conditions** section, configure restrictions related toâfor exampleâa management zone, specific conditions, or the port.
4. Select **Save changes**.

This procedure overwrites any existing configuration. If you want to modify an existing configuration, see the [**Modify a rule**](#api-update) section below.

To define a new service detection rule via API

1. Query the settings schema via the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") callâit contains the information about parameters included in the settings object.

   The ID of schema depends on the request type, as summarized in the following table.

   Request type

   Schema ID

   Full web request

   [`builtin:service-detection.full-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-request "View builtin:service-detection.full-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   Full web service

   [`builtin:service-detection.full-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-service "View builtin:service-detection.full-web-service settings schema table of your monitoring environment via the Dynatrace API.")

   External web request

   [`builtin:service-detection.external-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-request "View builtin:service-detection.external-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   External web service

   [`builtin:service-detection.external-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-service "View builtin:service-detection.external-web-service settings schema table of your monitoring environment via the Dynatrace API.")
2. Create a JSON object for your settings.

   Example JSON for a full web request rule

   ```
   [



   {



   "schemaId":"builtin:service-detection.full-web-request",



   "scope":"environment",



   "value":{



   "enabled":true,



   "name":"Detect Application,Application-1 as the same",



   "description":"Example: merge services",



   "managementZones":["-8445121454707515572"],



   "idContributors":{



   "applicationId":{



   "enableIdContributor":true,



   "serviceIdContributor":{



   "contributionType":"TransformValue",



   "transformations": [



   {



   "transformationType":"REMOVE_NUMBERS",



   "minDigitCount":1,



   "includeHexNumbers":false



   }



   ]



   }



   },



   "contextRoot":{



   "enableIdContributor":false



   },



   "serverName":{



   "enableIdContributor":false



   }



   },



   "conditions": [



   {



   "attribute":"ApplicationId",



   "compareOperationType":"StringStartsWith",



   "textValues": ["application"],



   "ignoreCase":false



   }



   ]



   }



   }



   ]
   ```
3. Use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") call to send your configuration.

### Modify a rule

When you modify a rule, some services might not be affected by it anymore. While historical data is available only for the previous service, all newly captured data is then associated with the new standalone service.

via web UI

via API

To edit an existing rule via the web UI

1. Go to **Settings**.
2. Expand **Service Detection** and select a request type (**Full web request rules** or **Full web service rules**, or **External web request rules** or **External web service rules**).
3. Expand ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") the row of the rule.
4. Edit the rule settings.
5. Select **Save changes**.

To update an existing rule via API

1. Query the settings schema via the [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") callâit contains the information about parameters included in the settings object.

   The ID of schema depends on the request type, as summarized in the following table.

   Request type

   Schema ID

   Full web request

   [`builtin:service-detection.full-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-request "View builtin:service-detection.full-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   Full web service

   [`builtin:service-detection.full-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-service "View builtin:service-detection.full-web-service settings schema table of your monitoring environment via the Dynatrace API.")

   External web request

   [`builtin:service-detection.external-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-request "View builtin:service-detection.external-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   External web service

   [`builtin:service-detection.external-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-service "View builtin:service-detection.external-web-service settings schema table of your monitoring environment via the Dynatrace API.")
2. Query the current configuration via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call.
3. Create a JSON object for your update. We recommend to use **updateToken** from previous objectâit ensures proper versioning of your settings.

   Example JSON for a full web request rule

   ```
   [



   {



   "updateToken":"vu9U3hXY3q0ATAAkOWFiNGI2ZDAtYWFhNC00M2IwLWEzZDYtNDQ2OTZkNzIyYzE5ACRmMTA1NTJlMC01M2Q5LTExZWQtODAwMS0wMTAwMDAwMDAwMDO-71TeFdjerQ",



   "value":{



   "enabled":true,



   "name":"Detect Application, Application-1 as the same",



   "description":"Example: merge services",



   "managementZones":["-8445121454707515572"],



   "idContributors":{



   "applicationId":{



   "enableIdContributor":true,



   "serviceIdContributor":{



   "contributionType":"TransformValue",



   "transformations":[



   {



   "transformationType":"REMOVE_NUMBERS",



   "minDigitCount":1,



   "includeHexNumbers":false



   }



   ]



   }



   },



   "contextRoot":{



   "enableIdContributor":false



   },



   "serverName":{



   "enableIdContributor":false



   }



   },



   "conditions":[



   {



   "attribute":"ApplicationId",



   "compareOperationType":"StringStartsWith",



   "textValues":["application"],



   ///Added condition to ignore case sensitivity for texts.



   "ignoreCase":true



   }



   ]



   }



   }



   ]
   ```
4. Use the [PUT an object](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") call to send your configuration.

### Delete a rule

If you delete a rule, all individual services are split and once again treated as standalone services.

via web UI

via API

To delete a service detection rule

1. Go to **Settings**.
2. Expand **Service Detection** and select a request type (**Full web request rules** or **Full web service rules**, or **External web request rules** or **External web service rules**).
3. In the **Delete** column for the corresponding rule row, select **Delete row** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove")

To delete a rule via API

1. Query the list of existing rules via the [GET objects](/docs/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") call. Specify the schema of your request type in the **schemaIds** query parameter.
   The ID of schema depends on the request type, as summarized in the following table.

   Request type

   Schema ID

   Full web request

   [`builtin:service-detection.full-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-request "View builtin:service-detection.full-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   Full web service

   [`builtin:service-detection.full-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-full-web-service "View builtin:service-detection.full-web-service settings schema table of your monitoring environment via the Dynatrace API.")

   External web request

   [`builtin:service-detection.external-web-request`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-request "View builtin:service-detection.external-web-request settings schema table of your monitoring environment via the Dynatrace API.")

   External web service

   [`builtin:service-detection.external-web-service`](/docs/dynatrace-api/environment-api/settings/schemas/builtin-service-detection-external-web-service "View builtin:service-detection.external-web-service settings schema table of your monitoring environment via the Dynatrace API.")
2. Find the rule you want to delete, and copy its **objectId**.
3. Delete the rule via the [DELETE an object](/docs/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.") call. Use the object ID obtained in the previous step.

### Examples

#### Separate fully monitored web request services based on URL or superimposed context root

For some technologies monitored by Dynatrace, the context root is not supported. A single service per process group is detected by default. You can change service detection by imposing a context root on a fully monitored web request.

In this example, when the URL path of a full web request starts with specific wording (`blog/`), we want to detect a service, whose ID will be transformed to the first segment of the URL.

Rule set-up

via web UI

via API

1. Go to **Settings**.
2. Expand **Service Detection** and select **Full web request rules**.
3. In the full web request rules, select **Add item**.
4. Configure the parameters as follows

   1. Enter a **Rule name**.
   2. Optional Enter a **Description**.
   3. Go to **URL context root** and turn on **Transform this value before letting it contribute to the Service ID**.

      1. From the **Contribution type** list, select **Use transformed URL path**.
      2. In **Segments to copy from URL path**, enter the number of segments of the URL to be kept (`1`).
   4. Go to **Conditions** and select **Add item**.

      1. From the **Take the value of this attribute** list, select **URL path**.
      2. From the **Apply this operation** list, select **Starts with**.
      3. Go to **Values** and select **Add item**, then enter `blog/`.
5. Select **Save changes**.

```
[



{



"schemaId":"builtin:service-detection.full-web-request",



"scope":"environment",



"value":{



"enabled":true,



"name":"Dynatrace Blog",



"description":"Detect first segment of an URL path as service when it starts with blog/",



"managementZones":[],



"idContributors":{



"applicationId":{



"enableIdContributor":false



},



"contextRoot":{



"enableIdContributor":true,



"serviceIdContributor":{



"contributionType":"TransformURL",



"segmentCount":1,



"transformations":[]



}



},



"serverName":{



"enableIdContributor":false



}



},



"conditions":[



{



"attribute":"UrlPath",



"compareOperationType":"StringStartsWith",



"textValues":["blog/"],



"ignoreCase":false



}



]



}



}



]
```

#### Merge application data into a single service, based on the application ID value

When incoming data is volatile or not specific enough, you can use service detection rules to merge services, for example, Apache HTTP clusters in AWS without a proper virtual host or web application IDs containing the build date.

In this example, we want to merge in the same service all incoming data from applications whose ID starts with `application`.

Rule set-up

via web UI

via API

1. Go to **Settings**.
2. Expand **Service Detection** and select **Full web request rules**.
3. In the full web request rules, select **Add item**.
4. Configure the parameters as follows.

   1. Enter a **Rule name**.
   2. Optional Enter a **Description**.
   3. Select **Set a management zone** and choose the management zone for the list.
   4. Go to **Application identifier** and turn on **Transform this value before letting it contribute to the Service ID**.

      1. From the **Contribution type** list, select **Use transformed value**.
      2. Go to **Transformations** and select **Add item**.

         1. From the **Transformation type** list, select **remove numbers**.
         2. Enter a **min digit count** (`1`)
   5. Go to **Conditions** and select **Add item**.

      1. From the **Take the value of this attribute** list, select **Application identifier**.
      2. From the **Apply this operation** list, select **Starts with**.
      3. Go to **Values** and select **Add item**, then enter `application`.
5. Select **Save changes**.

See the following [example JSON](#eg_appId).

#### Separate services for âpublic network servicesâ based on URL

In this example, when the top-level domain of an external web request ends with a specific wording (`dynatrace.com`), we want to detect a service, whose ID will be transformed to the first segment of the URL.

Rule set-up

via web UI

via API

1. Go to **Settings**.
2. Expand **Service Detection** and select **External web request rules**.
3. In the external web request rules, select **Add item**.
4. Configure the parameters as follows.

   1. Enter a **Rule name**.
   2. Optional Enter a **Description**.
   3. Go to **URL context root** and turn on **Transform this value before letting it contribute to the Service ID**.

      1. From the **Contribution type** list, select **Use transformed URL path**.
      2. In **Segments to copy from URL path**, enter the number of segments of the URL to be kept (`1`).
   4. Go to **Public domain name** and turn off **Port**.
   5. Go to **Conditions** and select **Add item**.

      1. From the **Take the value of this attribute** list, select **Top level domain**.
      2. From the **Apply this operation** drowpdown list, select **Ends with**.
      3. Go to **Values** and select **Add item**, then enter `dynatrace.com`.
      4. To ignore case sensitivity, turn on **Ignore case**.
5. Select **Save changes**.

```
[



{



"schemaId":"builtin:service-detection.external-web-request",



"scope":"environment",



"value":{



"enabled":true,



"name":"Dynatrace.com - based on URL",



"description":"Blog example: Dynatrace.com based on URL",



"managementZones":[],



"idContributors":{



"applicationId":{



"enableIdContributor":false



},



"contextRoot":{



"enableIdContributor":true,



"serviceIdContributor":{



"contributionType":"TransformURL",



"segmentCount":1,



"transformations":[]



}



},



"publicDomainName":{



"enableIdContributor":false



},



"portForServiceId":false



},



"conditions":[



{



"attribute":"TopLevelDomain",



"compareOperationType":"StringEndsWith",



"textValues":["dynatrace.com"],



"ignoreCase":true



}



]



}



}



]
```

#### Separate services for âpublic network servicesâ based on subdomains

If different endpoints shouldnât be combined in the same service (for example, `support.dynatrace.com` and `blog.dynatrace.com`), you can instruct Dynatrace to detect multiple services from the same domain, based on the detected hostname instead of the request's domain name.

Rule set-up

via web UI

via API

1. Go to **Settings**.
2. Expand **Service Detection** and select **External web request rules**.
3. In the external web request rules, select **Add item**.
4. Configure the parameters as follows.

   1. Enter a **Rule name**.
   2. Optional Enter a **Description**.
   3. Go to **Public domain name** and turn on **Transform this value before letting it contribute to the Service ID**.

      1. From the **Contribution type** list, select **Use the original value**.
      2. Turn on **Copy from host name**.
      3. Turn off **Port**.
   4. Go to **Conditions** and select **Add item**.

      1. From the **Take the value of this attribute** list, select **Top level domain**.
      2. From the **Apply this operation** drowpdown list, select **Ends with**.
      3. Go to **Values** and select **Add item**, then enter `dynatrace.com`.
      4. To ignore case sensitivity, turn on **Ignore case**.
5. Select **Save changes**.

```
[



{



"schemaId":"builtin:service-detection.external-web-request",



"scope":"environment",



"value":{



"enabled":true,



"name":"Dynatrace.com - based on subdomains",



"description":"Blog example: Separate services for public network services based on subdomains ",



"managementZones":[],



"idContributors":{



"applicationId":{



"enableIdContributor":false



},



"contextRoot":{



"enableIdContributor":false



},



"publicDomainName":{



"enableIdContributor":true,



"serviceIdContributor":{



"contributionType":"OriginalValue",



"copyFromHostName":true



}



},



"portForServiceId":false



},



"conditions":[



{



"attribute":"TopLevelDomain",



"compareOperationType":"StringEndsWith",



"textValues":["dynatrace.com"],



"ignoreCase":true



}



]



}



}



]
```

## Improve service detection

### Web server naming issues

* In some cases, web servers don't have well-defined virtual hosts, server names, or sites. A web server might simply be named `localhost`. This can result in multiple similar services that contain multiple website instances. To remedy such issues, adjust [process-group detection settings](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring").
* When there is no virtual host configured on an Apache HTTP server, the web server name defaults to the name of the physical host. In cloud environments, this leads to one virtual host for each physical host instance and thus one service instance. If the cloud environment starts and stops the hosts, these services will be temporary.

  To remedy such localhost scenarios, use an environment variable to define virtual host names: set `DT_LOCALTOVIRTUALHOSTNAME` for each web server process to any value. Dynatrace will pick up the names and use them in place of the existing localhost virtual host names. With this approach, you ensure that multiple physical hosts report the same virtual host and thus get one service with multiple instances, one instance per physical host.

### Define web application IDs

Some technologies don't provide unique application names. In such cases, you can define an environment variable called `DT_APPLICATIONID` to provide a unique name. This only impacts services of the respective process that don't already have application IDs. For Java applications, you can alternatively use the system property `dynatrace.application.id`.

### Rotating and anonymous ports

Dynatrace takes the listen port of each web request service into account when naming and detecting requests. In some cases, these ports are meaningless or random, changing with each restart. This is especially true if you're using a load balancer that dynamically assigns ports to application processes, as is the case in many Node.js scenarios.

To remedy this, set environment variable `DT_IGNOREDYNAMICPORT=true`. This removes the port from detection and replaces it with `*`.

## FAQ

If a service doesn't receive any new data after I create/edit/delete a rule, what happens to it?

When you create, edit, or delete a rule, data monitored after the change in service detection rules is aggregated and assigned to services, depending on the rule configuration. If a service stops receiving data, its historical data remains available (for example, for charting). You can still see the service and its traces in your environment.

## Related topics

* [Merged services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services "Consolidate multiple web-request services of the same process group into one service.")
* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")
* [Service detection API](/docs/dynatrace-api/configuration-api/service-api/detection-rules "Learn what the Dynatrace service detection rules config API offers.")
* [[Blog] New Dynatrace API enhances automatic service detection - with concrete examplesï»¿](https://www.dynatrace.com/news/blog/new-dynatrace-api-enhances-automatic-service-detection/#how-to-use-the-new-api)