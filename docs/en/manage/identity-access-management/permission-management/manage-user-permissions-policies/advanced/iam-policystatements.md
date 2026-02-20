---
title: IAM policy reference
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements
scraped: 2026-02-20T21:23:20.783138
---

# IAM policy reference

# IAM policy reference

* Latest Dynatrace
* Reference
* 1-min read
* Published Mar 25, 2021

The following is a complete reference of IAM permissions and corresponding conditions applicable to Dynatrace services. Refer to it when you need to define access policies based on a fine-grained set of permissions and conditions that can be enforced per service.

## ai

AI exposes generative AI capabilities in Dynatrace

### ai:operator:execute

Grants permission to interact with the AI conversational interface

## app-engine

AppEngine

### app-engine:apps:install

Grants permission to install and update apps

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`
* `app-engine:app-installer` - The ID of the user that installed the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`

### app-engine:apps:run

Grants permission to list and run apps and gives basic access to the Launcher

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`
* `app-engine:app-installer` - The ID of the user that installed the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`

### app-engine:apps:delete

Grants permission to uninstall apps

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`
* `app-engine:app-installer` - The ID of the user that installed the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`

### app-engine:functions:run

Grants permission to use the function-executor

### app-engine:edge-connects:read

Grants permission to read EdgeConnects

### app-engine:edge-connects:write

Grants permission to write EdgeConnects

### app-engine:edge-connects:delete

Grants permission to delete EdgeConnects

### app-engine:certificates:create

Grants permission to create short-living certificates for app releases

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `=`, `IN`, `startsWith`

## app-settings

App Settings service

### app-settings:objects:read

Grants permission to read app settings objects belonging to the schema

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single app settings schema. The identifier of a schema can be found in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### app-settings:objects:write

Grants permission to write settings objects belonging to the schema

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can be found in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### app-settings:objects:admin

Enables using admin-mode to access, change ownership and share permissions of any object. Admin-mode only bypasses the ownership check - so to do anything useful, app-settings:objects:read and/or app-settings:objects:write are needed as well.

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single app settings schema. The identifier of a schema can be found in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

## automation

Automation Server

### automation:workflows:read

Grants permission to read workflows

### automation:workflows:write

Grants permission to write workflows

#### conditions:

* `automation:workflow-type` - A string that identifies a workflow type either SIMPLE or STANDARD  
  operators: `IN`, `=`

### automation:workflows:run

Grants permission to execute workflows

### automation:workflows:admin

Grant admin permissions for workflows.

### automation:rules:read

Grants permission to read scheduling rules

### automation:rules:write

Grants permission to write scheduling rules

### automation:calendars:read

Grants permission to read business calendars

### automation:calendars:write

Grants permission to write business calendars

## business-analytics

Platform Business Analytics Service

### business-analytics:business-flows:write

Grants permission to write business-flows

### business-analytics:business-flows:read

Grants permission to read business-flows

## data-acquisition

Data Acquisition Ingest

### data-acquisition:logs:ingest

Grants permission to ingest logs from Data Acquisition supported sources

### data-acquisition:metrics:ingest

Grants permission to ingest metrics from Data Acquisition supported sources

### data-acquisition:events:ingest

Grants permission to ingest events from Data Acquisition supported sources

## davis

Davis service

### davis:analyzers:read

Grants permission to view Davis analyzers

### davis:analyzers:execute

Grants permission to execute Davis analyzers

## davis-copilot

Davis CoPilot exposes generative AI capabilities in Dynatrace

### davis-copilot:conversations:execute

Grants permission to interact with the Davis CoPilot conversational interface

### davis-copilot:nl2dql:execute

Grants permission to execute the Natural Language to DQL generative AI capability

### davis-copilot:dql2nl:execute

Grants permission to execute the CoPilot skill 'Summarize DQL'

### davis-copilot:document-search:execute

Grants permission to execute the CoPilot skill 'Document Search'

## deployment

Deployment service

### deployment:activegates.network-zones:write

Grants permission to write ActiveGate network zones

### deployment:activegates.groups:write

Grants permission to write ActiveGate groups

### deployment:oneagents.network-zones:write

Grants permission to write OneAgent network zones

### deployment:oneagents.host-groups:write

Grants permission to write OneAgent host groups

### deployment:oneagents.host-tags:write

Grants permission to write OneAgent host tags

### deployment:oneagents.host-properties:write

Grants permission to write OneAgent host properties

### deployment:oneagents.communication-settings:write

Grants permission to write OneAgent communication settings

## dev-obs

Developer Observability

### dev-obs:breakpoint:set

Grants permission to set breakpoint using DevObs live debugger

#### conditions:

* `dev-obs:k8s.namespace.name` - Kubernetes namespaces of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.entity.process_group` - Dynatrace entity process group of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.process_group.detected_name` - Dynatrace process group detected name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:k8s.cluster.name` - Cluster name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.group` - Host group of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.name` - Host name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`

### dev-obs:breakpoints:set

Grants permission to set breakpoint using DevObs live debugger

#### conditions:

* `dev-obs:k8s.namespace.name` - Kubernetes namespaces of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.entity.process_group` - Dynatrace entity process group of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.process_group.detected_name` - Dynatrace process group detected name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:k8s.cluster.name` - Cluster name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.group` - Host group of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.name` - Host name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`

### dev-obs:breakpoint:manage

Grants permission to manage breakpoints set in DevObs live debugger

### dev-obs:breakpoints:manage

Grants permission to manage breakpoints set in DevObs live debugger

## document

Document service

### document:documents:write

Grants permission to create and update documents of the document service

### document:documents:read

Grants permission to read documents of the document service

### document:documents:delete

Grants permission to delete documents of the document service

### document:documents:admin

Grants admin permissions for documents of the document service

### document:environment-shares:read

Grants permission to read environment shares of the document service

### document:environment-shares:write

Grants permission to create and update environment shares of the document service

### document:environment-shares:claim

Grants permission to claim environment shares of the document service

### document:environment-shares:delete

Grants permission to delete environment shares of the document service

### document:direct-shares:delete

Grants permission to delete direct shares of the document service

### document:direct-shares:read

Grants permission to read direct shares of the document service

### document:direct-shares:write

Grants permission to create and update direct shares of the document service

### document:trash.documents:read

Grants permission to read deleted documents of the document service

### document:trash.documents:delete

Grants permission to remove deleted documents from the trash of the document service

### document:trash.documents:restore

Grants permission to restore deleted documents from the trash of the document service

## email

API for sending emails

### email:emails:send

Grants permission to send emails from @apps.dynatrace.com with send email API

## environment

Environment and management zone user permissions. See [Migrate role-based permissions to Dynatrace IAMï»¿](https://dt-url.net/3s23539) for more information.

Role IAM permissions work the same way as classic roles do, which means that the `environment:roles:viewer` permission is a part of any other role permission. For example, a policy granting `environment:roles:manage-settings` permission also allows a user to access the web UI.

### environment:roles:viewer

Grants user the **Access environment** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on the management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:manage-settings

Grants user the **Change monitoring settings** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:agent-install

Grants user the **Download/install OneAgent** permission. Users who have this permission assigned are also able to view monitoring data for all management zones.

### environment:roles:view-sensitive-request-data

Grants user the **View sensitive request data** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:configure-request-capture-data

Grants user the **Configure capture of sensitive data** permission. Users who have this permission assigned are also able to view monitoring data for all management zones.

### environment:roles:replay-sessions-without-masking

Grants user the **Replay session data without masking** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:replay-sessions-with-masking

Grants user the **Replay session data** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:manage-security-problems

Grants user the **Manage security problems** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:view-security-problems

Grants user the **View security problems** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:logviewer

Grants user the **View logs** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

## extensions

Extensions service

### extensions:definitions:read

Grants permission to read extension and environment configurations

#### conditions:

* `extensions:extension-name` - A string that uniquely identifies a single extension  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:definitions:write

Grants permission to write (update/create/delete) extension and environment configurations

#### conditions:

* `extensions:extension-name` - A string that uniquely identifies a single extension  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configurations:read

Grants permission to read extension monitoring configurations

#### conditions:

* `extensions:host` - A string that uniquely identifies a single host for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:host-group` - A string that uniquely identifies a single host group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:ag-group` - A string that uniquely identifies a single ActiveGate group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:management-zone` - A string that uniquely identifies a single management zone for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:extension-name` - A string that uniquely identifies a single extension  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configurations:write

Grants permission to write (update/create/delete) extension monitoring configurations

#### conditions:

* `extensions:host` - A string that uniquely identifies a single host for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:host-group` - A string that uniquely identifies a single host group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:ag-group` - A string that uniquely identifies a single ActiveGate group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:management-zone` - A string that uniquely identifies a single management zone for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:extension-name` - A string that uniquely identifies a single extension  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configuration.actions:write

Grants permission to execute actions for extension

#### conditions:

* `extensions:host` - A string that uniquely identifies a single host for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:host-group` - A string that uniquely identifies a single host group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:ag-group` - A string that uniquely identifies a single ActiveGate group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:management-zone` - A string that uniquely identifies a single management zone for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:extension-name` - A string that uniquely identifies a single extension  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:discovery.jmx:read

Grants permission to discover running Java processes via JMX and read their data through extensions

## geolocation

Geolocation Service

### geolocation:locations:lookup

Grants permission to lookup geolocations for IP adresses.

## hub

Hub provides catalog content, such as Dynatrace Apps, Extensions, and Technologies, in the context of the environment.

### hub:catalog:read

Grants permission to read the hub catalog content.

## hyperscaler-authentication

Hyperscaler authentication service

### hyperscaler-authentication:aws:authenticate

Grants permission to authenticate against AWS.

### hyperscaler-authentication:azure:authenticate

Grants permission to authenticate against Azure.

## iam

Identity and Access Management Framework.

### iam:service-users:use

Grants permission to use all or specified service users

#### conditions:

* `iam:service-user-email` - Service users emails  
  operators: `IN`, `=`

### iam:service-users:create

Grants permission to create a service user in the environment

### iam:bindings:read

Grants permission to read bindings

#### conditions:

* `iam:policyUuid` - Policy uuid in the URI.  
  operators: `=`, `IN`
* `iam:levelType` - Level type in the URI.  
  operators: `=`, `IN`
* `iam:boundGroup` - Group uuid in the URI.  
  operators: `=`, `IN`

### iam:bindings:write

Grants permission to create bindings

#### conditions:

* `iam:policyUuid` - Policy uuid in the URI.  
  operators: `=`, `IN`
* `iam:levelType` - Level type in the URI.  
  operators: `=`, `IN`
* `iam:boundGroup` - Group uuid in the URI.  
  operators: `=`, `IN`

### iam:policies:read

Grants permission to read policies

### iam:policies:write

Grants permission to create policies

### iam:boundaries:read

Grants permission to read boundaries

### iam:boundaries:write

Grants permission to create boundaries

### iam:effective-permissions:read

Grants permission to read effective permissions

#### conditions:

* `iam-param:entity-type` - Entity type in the query parameters. Allowed values: `group`, `user`.  
  operators: `=`
* `iam-param:entity-id` - Entity id of given entity-type in the query parameters.  
  operators: `=`, `IN`

### iam:limits:read

Grants permission to read limits

## insights

Business Insights Service

### insights:opportunities:read

Grants permission to read data from the Opportunity Insights API

### insights:moments:read

Grants permission to query value moments and related data

## mcp-gateway

MCP Gateway exposes MCP server capabilities in Dynatrace

### mcp-gateway:servers:invoke

Grants permission to invoke the MCP Gateway API

### mcp-gateway:servers:read

Grants permission to list the available MCP servers

## notification

API for sending notifications

### notification:self-notifications:read

Grants permission to read self notifications.

### notification:self-notifications:write

Grants permission to write self notifications.

### notification:notifications:read

Grants permission to read notification configurations.

### notification:notifications:write

Grants permission to write notification configurations.

## oauth2

Authorization of OAuth token issuing actions (token exchange)

### oauth2:clients:manage

Allows management of light OAuth clients

#### conditions:

* `oauth2:scopes` - Requested scopes for the generated OAuth clients  
  operators: `=`, `NOT IN`

## openpipeline

OpenPipeline

### openpipeline:configurations:read

Grants permission to read the OpenPipeline configuration

### openpipeline:configurations:write

Grants permission to write the OpenPipeline configuration

### openpipeline:events:ingest

Grants permission to ingest events into OpenPipeline

### openpipeline:events.custom:ingest

Grants permission to ingest events into custom endpoints of OpenPipeline

### openpipeline:security.events:ingest

Grants permission to ingest security events into OpenPipeline

### openpipeline:security.events.custom:ingest

Grants permission to ingest security events into custom endpoints of OpenPipeline

### openpipeline:events.sdlc:ingest

Grants permission to ingest software development lifecycle events into OpenPipeline

### openpipeline:events.sdlc.custom:ingest

Grants permission to ingest software development lifecycle events into custom endpoints of OpenPipeline

## platform-token

Permissions for platform-tokens

### platform-token:tokens:write

Enables write user's platform tokens.

## security-intelligence

Provides APIs for security intelligence (enrichment and contextualization)

### security-intelligence:enrichments:run

Allows execution of enrichments and discovery of integration apps.

## session-replay

Session Replay

### session-replay:resources:read

Grants permission to retrieve a session replay resource

## settings

Settings service

### settings:objects:read

Enables reading of settings objects belonging to the schema

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - A schema group that allows to address multiple individual schemas at once. The group of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema of the object has a schemaGroup property that matches.  
  operators: `IN`, `=`
* `settings:entity.hostGroup` - The host group attribute of an entity for which a setting is stored. This is e.g. useful to grant access to settings scopes of all hosts which belong to the same host group.  
  operators: `IN`, `=`, `!=`
* `settings:scope` - The exact scope identifier a setting object has or will have. This condition allows to grant access to the scope of e.g., an individual host. In this case the scope equals the entity identifier, e.g. HOST-48B8F52F33098830.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `environment:management-zone` - The name of a management zone. This condition is applicable to either: any settings object that is allowed on the scope of an entity that can be matched into a management zone or settings objects of the schemas builtin:alerting.maintenance-window, builtin:alerting.profile, builtin:anomaly-detection.metric-events, builtin:monitoring.slo and builtin:problem.notifications.  
  operators: `IN`, `=`, `startsWith`, `MATCH`
* `settings:dt.security_context` - The name of a security context. This condition is applicable to any settings object that is allowed on the scope of an entity that can have a security context assigned.  
  operators: `IN`, `=`, `startsWith`

### settings:objects:write

Enables writing of settings objects belonging to the schema

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - A schema group that allows to address multiple individual schemas at once. The group of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema of the object has a schemaGroup property that matches.  
  operators: `IN`, `=`
* `settings:entity.hostGroup` - The host group attribute of an entity for which a setting is stored. This is e.g. useful to grant access to settings scopes of all hosts which belong to the same host group.  
  operators: `IN`, `=`, `!=`
* `settings:scope` - The exact scope identifier a setting object has or will have. This condition allows to grant access to the scope of e.g., an individual host. In this case the scope equals the entity identifier, e.g. HOST-48B8F52F33098830.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `environment:management-zone` - The name of a management zone. This condition is applicable to either: any settings object that is allowed on the scope of an entity that can be matched into a management zone or settings objects of the schemas builtin:alerting.maintenance-window, builtin:alerting.profile, builtin:anomaly-detection.metric-events, builtin:monitoring.slo and builtin:problem.notifications.  
  operators: `IN`, `=`, `startsWith`, `MATCH`
* `settings:dt.security_context` - The name of a security context. This condition is applicable to any settings object that is allowed on the scope of an entity that can have a security context assigned.  
  operators: `IN`, `=`, `startsWith`

### settings:schemas:read

Enables reading settings schemas

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema's schemaId property of the schema matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - A schema group that allows to address multiple individual schemas at once. The group of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema's schemaId property of the schema matches.  
  operators: `IN`, `=`

### settings:objects:admin

Enables using admin-mode to access, change ownership and share permissions of any object. Admin-mode only bypasses the ownership check - so to do anything useful, settings:objects:read and/or settings:objects:write are needed as well.

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - A schema group that allows to address multiple individual schemas at once. The group of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema of the object has a schemaGroup property that matches.  
  operators: `IN`, `=`

## slo

SLO service

### slo:slos:read

Grants permission to read Service-Level Objectives

### slo:slos:write

Grants permission to write Service-Level Objectives

### slo:objective-templates:read

Grants permission to read Service-Level Objectives Templates

## state

Platform State Service

### state:app-states:read

Grants permission to read app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:app-states:write

Grants permission to write app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:app-states:delete

Grants permission to delete app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:user-app-states:read

Grants permission to read user-app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:user-app-states:write

Grants permission to write user-app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:user-app-states:delete

Grants permission to delete user-app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

## state-management

State Management - Clear app-states and user-app-states of specific apps.

### state-management:app-states:delete

Grants permission to delete all app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state-management:user-app-states:delete

Grants permission to delete user-app-states of the current user

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state-management:user-app-states:delete-all

Grants permission to delete user-app-states of all users

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

## storage

Grail

### storage:events:read

Grants permission to read records from the events-table

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Gives high-level information about what kind of information the event contains, without being specific to the contents of the event. Helps to determine the record type of a raw event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - The unique type identifier of a given event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Source of the event, for example the name of the component or system that generated the event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:events:write

Grants permission to write events to Grail

### storage:metrics:read

Grants permission to read timeseries from the metrics-table

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:metric.key` - The identifier of a metric, grouping numeric measurements that share the same measurement semantics (i.e. were measured "the same way".)  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:metrics:write

Grants permissions to write metrics from Dynatrace classic to latest Dynatrace and vice versa

### storage:logs:read

Grants permission to read records from the logs-table

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:log.source` - The location where the log comes from.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:logs:write

Grants permission to write logs to Grail

### storage:entities:read

Grants permission to read records from entities

#### conditions:

* `storage:entity.type` - The type of the entity.  
  operators: `=`, `IN`, `startsWith`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`

### storage:spans:read

Grants permission to read records from the spans-table

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:bizevents:read

Grants permission to read records from the bizevents-table

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Gives high-level information about what kind of information the event contains, without being specific to the contents of the event. Helps to determine the record type of a raw event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - The unique type identifier of a given event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Source of the event, for example the name of the component or system that generated the event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:smartscape:read

Grants permission to read smartscape nodes and edges from Grail

#### conditions:

* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:system:read

Grants permission to read records from all system tables (for example, `dt.system.events`).

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Gives high-level information about what kind of information the event contains, without being specific to the contents of the event. Helps to determine the record type of a raw event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - The unique type identifier of a given event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Source of the event, for example the name of the component or system that generated the event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:buckets:read

Grants permission to read records from Grail buckets. Required additionally to a table permission.

#### conditions:

* `storage:table-name` - Table name of the bucket that can be accessed.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:bucket-name` - Name of the bucket that can be accessed.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:query-consumption` - If it is set to `INCLUDED`, the query returns data only from the configured included timeframe of buckets. If set to `ON_DEMAND`, it returns data from the entire timeframe. For any other value, the IAM statement is ignored. The included timeframe must be configured per bucket via the Storage Management API.  
  operators: `=`

### storage:fieldsets:read

Read data from fieldsets

#### conditions:

* `storage:table-name` - Name of the table from which fieldset(s) can be accessed.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:bucket-name` - Name of the bucket from which fieldset(s) can be accessed.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:fieldset-name` - Name of the fieldset(s) which can be accessed.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`

### storage:bucket-definitions:read

Grants permission to read bucket definitions from Grail

### storage:bucket-definitions:write

Grants permission to write bucket definitions to Grail

### storage:bucket-definitions:delete

Grants permission to delete bucket definitions from Grail

### storage:bucket-definitions:truncate

Grants permission to delete all records from a bucket (not delete the bucket itself) in Grail.

### storage:records:delete

Delete records in grail

### storage:files:read

Read data from files.

#### conditions:

* `storage:file-path` - Path of the file which can be accessed.  
  operators: `=`, `startsWith`, `IN`

### storage:files:write

Ingest data via REST API

#### conditions:

* `storage:file-path` - Path of the file which can be accessed.  
  operators: `=`, `startsWith`, `IN`

### storage:files:delete

Delete data via REST API

#### conditions:

* `storage:file-path` - Path of the file which can be accessed.  
  operators: `=`, `startsWith`, `IN`

### storage:filter-segments:read

Read filter-segments from grail

### storage:filter-segments:write

Write filter-segments in grail

### storage:filter-segments:share

Share filter-segments in grail

### storage:filter-segments:delete

Delete own filter-segments in grail

### storage:filter-segments:admin

Write and delete all filter-segments in grail

### storage:fieldset-definitions:read

Read fieldset definitions from grail

### storage:fieldset-definitions:write

Write and delete fieldset definitions in grail

### storage:application.snapshots:read

Read application.snapshots from grail

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`

### storage:user.events:read

Read user.events from grail

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:frontend.name` - The name of the frontend.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:user.sessions:read

Read user.sessions from grail

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:frontend.name` - The name of the frontend.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:user.replays:read

Read user.replays from grail

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:security.events:read

Read security.events from grail

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Gives high-level information about what kind of information the event contains, without being specific to the contents of the event. Helps to determine the record type of a raw event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - The unique type identifier of a given event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Source of the event, for example the name of the component or system that generated the event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

## unified-analysis

Unified analysis

### unified-analysis:screen-definition:read

Grants permission to read the screen definition of a unified analysis screen

## upgrade-assistant

SaaS Upgrade Assistant service

### upgrade-assistant:environments:write

Grants permission to use the SaaS Upgrade Assistant app

## vulnerability-service

Provides APIs to access vulnerabilities that are affecting customer environments

### vulnerability-service:vulnerabilities:read

Allows viewing vulnerabilities

### vulnerability-service:vulnerabilities:write

Allows modifying vulnerability related information

## Related topics

* [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")
* [IAM policy statement syntax and examples](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")
* [Grant access to Settings](/docs/manage/identity-access-management/use-cases/access-settings "Grant access to Settings")
* [Account Management API](/docs/dynatrace-api/account-management-api "Explore endpoints of the Account Management API.")