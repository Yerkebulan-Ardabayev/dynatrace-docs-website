---
title: Global field reference
source: https://www.dynatrace.com/docs/semantic-dictionary/fields
scraped: 2026-02-27T21:11:42.318549
---

# Global field reference

# Global field reference

* Latest Dynatrace
* Overview
* Updated on Feb 23, 2026

The following reference contains a list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types. The fields are organized in namespaces that are separated with dots.

### Top level fields

The top level fields contain generally relevant information for all monitoring data

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `timestamp` | timestamp | stable The time (UNIX Epoch time in nanoseconds) when the event originated, typically when the source created it. If no original timestamp is available, it will be populated at ingest time and required for all events. In the case of a correlated event (for example, ITIL events), this time could be different from the event.start time, as this time represents the actual timestamp when the "update" for the event was created. | `1649822520123123123` |
| `timeframe` | record[] | stable The timeframe represented by a timeseries record. |  |
| `start_time` | timestamp | stable Start time of a data point. Value is a UNIX Epoch time in nanoseconds and less than or equal to the `end_time`. | `1649822520123123123` |
| `end_time` | timestamp | stable End time of a data point. Value is a UNIX Epoch time in nanoseconds and greater than or equal to the `start_time`. | `1649822520123123165` |
| `duration` | duration | stable The difference between `start_time` and `end_time` in nanoseconds. | `42` |
| `interval` | string | stable Denotes the timeframe of represented by individual timeseries measurements returned by a timeseries record. | `1 min` |

## Adobe

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `adobe.em.env_type` | string | resource experimental Adobe Experience Manager (AEM) environment type. | `dev`; `stage`; `prod` |
| `adobe.em.program` | string | resource experimental Adobe Experience Manager (AEM) service. Contains the customer defined name of the AEM environment. |  |
| `adobe.em.service` | string | resource experimental Adobe Experience Manager (AEM) service. Contains the program and environment IDs the customer is exposed to. |  |
| `adobe.em.tier` | string | resource experimental Adobe Experience Manager (AEM) tier. | `author`; `publish`; `preview` |

## Aggregation

OneAgent might aggregate spans that have the same parent span into a single span. The aggregated span contains attributes to indicate the aggregation and to allow reconstructing details.

For aggregated spans the `start_time` holds the earliest `start_time`, `end_time` holds the latest `end_time` of all aggregated spans.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `aggregation.count` | long | stable The number of spans aggregated into this span. Because this span represents multiple spans, the value is >1. | `3` |
| `aggregation.duration_max` | duration | stable The duration in nanoseconds for the longest aggregated span. | `482` |
| `aggregation.duration_min` | duration | stable The duration in nanoseconds for the shortest aggregated span. | `42` |
| `aggregation.duration_samples` | duration[] | stable Array of reservoir sampled span durations of the aggregated spans. The duration samples can be used to estimate a more accurate duration distribution of aggregated spans rather than the average value. | `[42, 482, 301]` |
| `aggregation.duration_sum` | duration | stable The duration sum in nanoseconds for all aggregated spans. | `123` |
| `aggregation.exception_count` | long | stable The number of aggregated spans that included an exception. | `0`; `6` |
| `aggregation.parallel_execution` | boolean | stable `true` indicates that aggregated spans may have been executed in parallel. Therefore, `start_time + duration_sum` may exceed `end_time`. |  |

## Apache HTTP Server

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `apache.tomcat.base` | string | resource experimental The server's base directory. This is what usually is referred to as CATALINA\_BASE. | `/usr/share/tomcat6` |
| `apache.tomcat.home` | string | resource experimental The server's home directory. This is what usually is referred to as CATALINA\_HOME. | `/usr/share/tomcat6` |

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `apache.httpd.config.path` | string | resource experimental |  |
| `apache.httpd.module.name` | string | resource experimental The name of the Apache HTTP Server module that generated the log entry. | `core`; `proxy` |

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `apache.spark.master.ip` | string | resource experimental |  |

## App

The app namespace contains information on the application sending the event.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `app.bundle` | string | resource stable The name of the bundle, for example, the bundle identifier on iOS or the `applicationId` on Android. | `com.example.easytravel` |
| `app.id` | string | resource stable An optional unique application identifier. Chosen by the customer | `easytravel` |
| `app.short_version` | string | resource stable The application's publicly visible version number, as, for example, displayed in App Store or Google Play. Usually this is just the major and minor version with no patch number. | `5.23` |
| `app.version` | string | resource stable The application's internal build number, which can include information such as patch number and build number. | `5.23.15789`; `143542` |

## Continuous Integration/Continuous Deployment

The `argocd` namespace contains Argo CD specific deployment attributes.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `argocd.app.health.status` | string | experimental The health state of the tracked resource. [1](#fn-1-1-def) | `Healthy`; `Progressing`; `Degraded`; `Missing`; `Suspended`; `Unknown` |
| `argocd.sync.operation_state.outcome` | string | experimental Message associated with synchronization operation. [2](#fn-1-2-def) | `successfully synced (no more tasks)`; `Operation terminated (retried 4 times)` |
| `argocd.sync.operation_state.phase` | string | experimental Status of the synchronization operation between source and target. [3](#fn-1-3-def) | `Running`; `Succeeded`; `Error`; `Failed` |
| `argocd.sync.status` | string | experimental The sync status represents the current state of reconciliation. [4](#fn-1-4-def) | `SYNCED`; `OUT OF SYNC`; `UNKNOWN` |

1

The value is equal to the `app.status.health.status` value in Argo CD.

2

The value is equal to the `app.status.operationState.message` value in Argo CD.

3

The value is equal to the `app.status.operationState.phase` value in Argo CD.

4

The value is equal to the `app.status.sync.status` value in Argo CD.

## Artifact

The `artifact` namespace contains information about software artifacts.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `artifact.attestation.filename` | string | experimental The provenance filename of the built attestation. It directly relates to the `artifact.filename`. | `carts-service-amd64-0.1.1.tar.gz.intoto.json1` |
| `artifact.attestation.hash` | string | experimental The full hash value of the built attestation. | `b4e370270ac4fe8d728b845ab8d190a7c931f09ff7b0156dd4d6abf797f1fe6a` |
| `artifact.attestation.id` | string | experimental The ID of the build [software attestationï»¿](https://slsa.dev/attestation-model). | `1337` |
| `artifact.filename` | string | experimental The filename of the software artifact, typically generated by the build process. This is similar to the `artifact.id`, but can contain the `artifact.version` and other data like file extension. | `carts-service-amd64-0.1.1.tar.gz` |
| `artifact.hash` | string | experimental The full hash value of the software artifact. This value is used to verify the integrity of the software artifact. | `6c323d126547f71fafb4bffa02cdc480fb284678644ef0b6c69029f051fe5137` |
| `artifact.id` | string | experimental The identifier of the software artifact, typically the name of the artifact. | `carts-service` |
| `artifact.name` | string | experimental The human-readable name of the software artifact. | `Carts service` |
| `artifact.purl` | string | experimental The [Package URLï»¿](https://github.com/package-url/purl-spec) of the package artifact. This value is used to identify and locate the artifact. | `pkg:npm/%40dynatrace/backstage@2.0.0`; `pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie` |
| `artifact.version` | string | experimental The version of the software artifact, typically in [Semantic Versioningï»¿](https://semver.org/) format. | `0.1.1` |

## ASP.NET Core

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `aspnetcore.appl.path` | string | resource experimental |  |

## Audit

Fields that can come from audit logs.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `audit.action` | string | stable Audited action. | `Access to Azure Resource Manager`; `New User Created`; `User added to Group` |
| `audit.identity` | string | stable User name, service account name, or principal name that executes audited action. | `name.surname@example.com` |
| `audit.result` | string | stable Result of the audited action. | `Succeeded`; `Failed` |
| `audit.status` | string | stable Status of the audited action. | `Started`; `In Progress`; `Succeeded`; `Failed`; `Active`; `Resolved` |
| `audit.time` | timestamp | experimental Timestamp of the audited action. | `16/01/2025, 10:34 AM` |

## Authentication

Authentication type and method used to login to a Dynatrace system.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `authentication.client.id` | string | experimental The OAuth2 client id if of type 'CLIENT\_CREDENTIALS'. | `<DYNATRACE_TOKEN_PLACEHOLDER>` |
| `authentication.grant.type` | string | experimental The grant type used during OAuth2 authentication. | `AUTHORIZATION_CODE`; `CLIENT_CREDENTIALS` |
| `authentication.token` | string | experimental The public token identifier of authentication.type 'TOKEN'. | `<DYNATRACE_TOKEN_PLACEHOLDER>` |
| `authentication.type` | string | experimental The method of authentication. | `OAUTH2` |

`authentication.grant.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `AUTHORIZATION_CODE` | The [OAuth 2.0 "Authorization Code" grant typeï»¿](https://oauth.net/2/grant-types/authorization-code/) |
| `CLIENT_CREDENTIALS` | The [OAuth 2.0 "Client Credentials" grant typeï»¿](https://oauth.net/2/grant-types/client-credentials/) |

`authentication.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `DEVOPSTOKEN` | Authenticated via DevOps token |
| `NONE` | Not authenticated (authentication not necessary) |
| `OAUTH2` | The [OAuth 2.0 authentication type grant typeï»¿](https://oauth.net/2/) |
| `TOKEN` | Authenticated via API access token or personal access token |

`authentication.client.id` and `authentication.token` MUST follow the Dynatrace token format definition.

Specifically, `authentication.client.id` MUST be prefixed with `dt0s02.`

## Availability

Information about entity availability. Sample usage is reporting hosts and PGI-s availability by OS Agent.
Value of availability.state can be used for calculating aggregate availability (dividing count of "successful" requests by count of all requests).
With constant frequency of requests it can be treated as a time-base availability, showing percentage of time that the monitored entity was available.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `availability.state` | string | stable State of entity (host or PGI) availability. | `up` |

`availability.state` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `available` | [PGI] PGI is available and reported. |
| `no_data` | [HOST] Host is working, agent active but no data are sent. |
| `no_data_agent_inactive` | [HOST] Host is working, agent inactive (disabled manually in configuration). No data are sent. |
| `reboot_graceful` | [HOST] Host has started after graceful shutdown. |
| `reboot_ungraceful` | [HOST] Host has started after ungraceful shutdown. |
| `shutdown_host` | [HOST] Host has been shut down. |
| `unavailable` | [PGI] PGI is unavailable and not reported. |
| `unimportant` | [PGI] PGI is available but not reported because it became unimportant. |
| `unmonitored_agent_stopped` | [HOST] Host is unmonitored because agent stopped. |
| `unmonitored_agent_uninstalled` | [HOST] Host is unmonitored because agent has been uninstalled. |
| `unmonitored_agent_upgrade` | [HOST] Host is unmonitored because agent is upgrading. |
| `up` | [HOST] Host is working, agent active and sending data. |

## Amazon Web Services (AWS)

Fields that can come from applications running on AWS.

### Fields

#### Resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `aws.account.id` | string | resource stable The 12-digit number, such as 123456789012, that uniquely identifies an AWS account. Tags: `permission` `primary-field` | `123456789012` |
| `aws.account.name` | string | resource experimental Name associated with the AWS account. | `example.com` |
| `aws.alb.name` | string | resource experimental Application load balancer name that instance is behind. | `my-alb` |
| `aws.arn` | string | resource stable Amazon Resource Name (ARN). | `arn:aws:lambda:us-east-1:478983378254:function:acceptanceWeatherBackend` |
| `aws.availability_zone` | string | resource stable A specific availability zone or array of zones in given AWS region. | `us-east-1a`; `us-east-1b` |
| `aws.availability_zone.id` | string | resource experimental ID for the availability zone. | `use1-az1`; `use1-az2`; `use1-az3` |
| `aws.cloudfront.detailed_result_type` | string | resource experimental Extends the aws.cloudfront.result\_type with additional states. [See full list under x-edge-detailed-result-type.ï»¿](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/standard-logs-reference.html) | `OriginShieldHit`; `MissGeneratedResponse`; `InvalidRequest` |
| `aws.cloudfront.response.result_type` | string | resource experimental How the server classified the response just before returning the response to the viewer. | `Hit`; `Miss`; `LimitExceeded` |
| `aws.cloudfront.result_type` | string | resource experimental How the server classified the response after the last byte left the server. | `Hit`; `Miss`; `LimitExceeded` |
| `aws.ecr.account.id` | string | resource experimental |  |
| `aws.ecr.region` | string | resource experimental |  |
| `aws.ecs.cluster` | string | resource experimental |  |
| `aws.ecs.container.arn` | string | resource experimental The full Amazon Resource Name (ARN) of the container. | `arn:aws:ecs:us-west-2:111122223333:container/05966557-f16c-49cb-9352-24b3a0dcd0e1` |
| `aws.ecs.container.name` | string | resource experimental |  |
| `aws.ecs.docker.id` | string | resource experimental The Docker ID for the container. | `cd189a933e5849daa93386466019ab50-2495160603` |
| `aws.ecs.docker.name` | string | resource experimental The name of the container supplied to Docker. | `curl-image` |
| `aws.ecs.family` | string | resource experimental |  |
| `aws.ecs.revision` | string | resource experimental |  |
| `aws.ecs.task.arn` | string | resource experimental The full Amazon Resource Name (ARN) of the task to which the container belongs. | `arn:aws:ecs:us-west-2:111122223333:task/default/cd189a933e5849daa93386466019ab50` |
| `aws.execution_environment` | string | resource experimental The runtime identifier, prefixed by AWS\_Lambda\_. Lambda supports multiple languages through the use of runtimes. A runtime provides a language-specific environment that relays invocation events, context information, and responses between Lambda and the function. | `AWS_Lambda_java8` |
| `aws.fle.fields_number` | long | resource experimental The number of field-level encryption fields that the server encrypted and forwarded to the origin. | `12`; `27` |
| `aws.fle.status` | string | resource experimental When field-level encryption is configured for a distribution, this field contains a code that indicates whether the request body was successfully processed. | `FieldLengthLimitClientError` |
| `aws.lambda.function.name` | string | resource experimental |  |
| `aws.lambda.initialization_type` | string | resource experimental The AWS Lambda initialization type. Same string value as available in [AWS\_LAMBDA\_INITIALIZATION\_TYPEï»¿](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime). | `snap_start` |
| `aws.log_group` | string | resource experimental Amazon CloudWatch group of log streams that share the same retention, monitoring, and access control settings. | `/aws/lambda/a-SomeFunction-1AWHD6W1QC5DH` |
| `aws.log_stream` | string | resource experimental A sequence of log events that share the same source. | `2021/01/04/[$LATEST]b2e34f11da04232cb9f9d3d5799a5c12` |
| `aws.region` | string | resource stable A specific geographical AWS Cloud location. Tags: `primary-field` | `us-east-1` |
| `aws.resource.id` | string | resource stable Unique, immutable, identifier assigned to the AWS cloud resource. | `i-0922cda4579db3a45` |
| `aws.resource.name` | string | resource stable Name of the resource for named resources, value of the "Name" tag in AWS for non-named resources (if unavailable, same as aws.resource.id). | `my-ec2-instance` |
| `aws.resource.type` | string | resource experimental The name of a resource type in CloudFormation format. | `AWS::EC2::Instance`; `AWS::S3::Bucket`; `AWS::Lambda::Function` |
| `aws.service` | string | resource experimental The service that identifies the AWS product. | `s3` |
| `aws.tags.__tag_key__` | string | resource experimental Contains the value for the tag with the tag key named `__tag_key__` defined in the tag enrichment configuration. | `dt_owner_mail` |

`aws.fle.status` MUST be one of the following:

| Value | Description |
| --- | --- |
| `FieldLengthLimitClientError` | A field that is configured to be encrypted exceeds the maximum length allowed. |
| `FieldNumberLimitClientError` | A request that the distribution is configured to encrypt contains more than the number of fields allowed. |
| `ForwardedByContentType` | The server forwarded the request to the origin without parsing or encryption because no content type was configured. |
| `ForwardedByQueryArgs` | The server forwarded the request to the origin without parsing or encryption because the request contains a query argument that wasn't in the configuration for field-level encryption. |
| `ForwardedDueToNoProfile` | The server forwarded the request to the origin without parsing or encryption because no profile was specified in the configuration for field-level encryption. |
| `MalformedContentTypeClientError` | The server rejected the request and returned an HTTP 400 status code to the viewer because the value of the Content-Type header was in an invalid format. |
| `MalformedInputClientError` | The server rejected the request and returned an HTTP 400 status code to the viewer because the request body was in an invalid format. |
| `MalformedQueryArgsClientError` | The server rejected the request and returned an HTTP 400 status code to the viewer because a query argument was empty or in an invalid format. |
| `Processed` | The server successfully processed the request body, encrypted values in the specified fields, and forwarded the request to the origin. |
| `RejectedByContentType` | The server rejected the request and returned an HTTP 400 status code to the viewer because no content type was specified in the configuration for field-level encryption. |
| `RejectedByQueryArgs` | The server rejected the request and returned an HTTP 400 status code to the viewer because no query argument was specified in the configuration for field-level encryption. |
| `RequestLengthLimitClientError` | The length of the request body exceeded the maximum length allowed when field-level encryption is configured. |
| `ServerError` | The origin server returned an error. |

`aws.lambda.initialization_type` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `on-demand` | On demand |
| `provisioned-concurrency` | Provisioned concurrency |
| `snap-start` | SnapStart |

#### Span attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `aws.kinesis.arn` | string | experimental Amazon resource name (ARN) of a Kinesis stream or consumer. | `arn:aws:kinesis:us-east-2:123456789012:stream/MyKinesisStream`; `arn:aws:kinesis:us-west-2:123456789012:stream/MyKinesisStream/consumer/MyKinesisConsumer:1616044553` |
| `aws.kinesis.consumer.arn` | string | experimental Amazon resource name (ARN) of a Kinesis consumer. | `arn:aws:kinesis:us-west-2:123456789012:stream/MyKinesisStream/consumer/MyKinesisConsumer:1616044553` |
| `aws.kinesis.consumer.name` | string | experimental Name of a Kinesis consumer. | `MyKinesisConsumer` |
| `aws.kinesis.stream.arn` | string | experimental Amazon resource name (ARN) of a Kinesis stream. | `arn:aws:kinesis:us-east-2:123456789012:stream/MyKinesisStream` |
| `aws.kinesis.stream.name` | string | experimental Name of a Kinesis stream. | `MyKinesisStream` |
| `aws.lambda.invoked_arn` | string | experimental The full invoked ARN as provided on the `Context` passed to the function (`Lambda-Runtime-Invoked-Function-Arn` response header from the request to `/runtime/invocation/next`). | `arn:aws:lambda:us-east-1:123456789012:function:acceptanceWeatherBackend:production` |
| `aws.request_id` | string | experimental The AWS request ID (e.g., value of `x-amzn-requestid`, `x-amzn-request-id`, or `x-amz-request-id` HTTP header, `awsRequestId` field in AWS lambda context object). | `0e7bc729-a468-57e8-8143-98f2eec5c925` |
| `aws.s3.bucket` | string | experimental Name of an S3 bucket. | `amzn-s3-demo-bucket`; `amzn-s3-demo-bucket1-a1b2c3d4-5678-90ab-cdef-example11111` |
| `aws.s3.key` | string | experimental Key name of the object. | `Development/Projects.xls`; `Finance/statement1.pdf`; `s3-dg.pdf` |
| `aws.s3.object_version` | string | experimental Version ID for the specific version of the object. | `3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo` |
| `aws.s3.part_number` | long | experimental Part number in a multi-part upload. | `3456` |
| `aws.s3.source.bucket` | string | experimental Name of the bucket containing the object to copy. | `amzn-s3-source-bucket` |
| `aws.s3.source.key` | string | experimental Key of the object to copy. | `Finance/statement1.pdf` |
| `aws.s3.source.object_version` | string | experimental Version of the source object to copy. By default, the latest version is copied. | `3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo` |
| `aws.s3.upload_id` | string | experimental Upload ID identifying the multipart upload targeted by an operation (abort/complete/upload/â¦). | `dfRtDYWFbkRONycy.Yxwh66Yjlx.cph0gtNBtJ` |
| `aws.xray.trace_id` | string | experimental Contains the [AWS X-Rayï»¿](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) trace id (e.g., value of the `x-amzn-trace-id` HTTP header, `_X_AMZN_TRACE_ID` environment variable on AWS lambda) | `Root=1-63441c4a-abcdef012345678912345678`; `Self=1-63441c4a-12456789abcdef012345678;Root=1-67891233-abcdef012345678912345678` |

#### Log attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `aws.route53.edge_location_id` | string | experimental The Route 53 edge location that responded to the query. Each edge location is identified by a three-letter code and an arbitrary number. | `FRA54-SN1`; `DFW3` |
| `aws.route53.hostedzone_id` | string | experimental The ID of the hosted zone that is associated with all the DNS queries in this log. | `Z1234567890ABCDEFGHIJ` |
| `aws.route53.resolver_ip_address` | string | experimental The IP address of the DNS resolver that submitted the request to Route 53. | `192.168.1.1`; `2001:db8::1234` |
| `dns.question.name` | string | experimental The domain or subdomain that was specified in the request. | `example.com`; `support.dynatrace.com/` |
| `dns.question.type` | string | experimental Either the DNS record type that was specified in the request, or ANY. | `A`; `AAAA`; `CNAME`; `TXT`; `ANY` |
| `dns.response_code` | string | experimental The DNS response code that Route 53 returned in response to the DNS query. | `NOERROR`; `NXDOMAIN` |

## Azure Resource

Fields that can come from applications running on Azure.

### Fields

#### Resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `azure.availability_zones` | string[] | resource experimental Availability zones of Azure Cloud resource. | `['1']` |
| `azure.class_name` | string | resource experimental The fully qualified name of the class executing an Azure function. | `Host.Functions` |
| `azure.container_app.dnssuffix` | string | resource experimental The DNS suffix for the Container Apps environment. | `redbeach-0f8a3e63.northeurope.azurecontainerapps.io` |
| `azure.container_app.hostname` | string | resource experimental The revision-specific hostname of the container app. | `kapitan-bomba-demo--nk4tc46.redbeach-0f8a3e63.northeurope.azurecontainerapps.io` |
| `azure.container_app.name` | string | resource experimental The name of the container app. | `kapitan-bomba-demo` |
| `azure.container_app.replica.name` | string | resource experimental The name of the container app replica. | `kapitan-bomba-demo--nk4tc46-5d568c5df6-49px7` |
| `azure.event_hub_namespace.name` | string | resource experimental Azure Event Hub Namespace name. | `my-event-hub` |
| `azure.location` | string | resource stable A specific geographical location of Azure Cloud resource. Tags: `primary-field` | `westeurope` |
| `azure.management_group` | string | resource experimental A group of Azure subscriptions used for governance use cases. | `Tenant Root Group`; `My Custom Group` |
| `azure.resource.group` | string | resource stable A resource group is a container that holds related resources for an Azure solution. Tags: `permission` `primary-field` | `demo-backend-rg` |
| `azure.resource.id` | string | resource experimental A unique, immutable identifier assigned to each Azure cloud resource. | `/subscriptions/27e9b03f-04d2-2b69-b327-32f433f7ed21/resourceGroups/demo-backend-rg/providers/Microsoft.ContainerService/managedClusters/demo-aks` |
| `azure.resource.name` | string | resource experimental User-provided name of the Azure cloud resource. | `demo-aks` |
| `azure.resource.type` | string | resource experimental The name of a resource type in the format: {resource-provider}/{resource-type}. | `Microsoft.ContainerService/managedClusters` |
| `azure.service_bus_namespace.name` | string | resource experimental Azure Service Bus name. | `my-service-bus` |
| `azure.site_name` | string | resource experimental Globally unique deployment information about an Azure function. | `dt-function-scripted` |
| `azure.sql_elastic_pool.name` | string | resource experimental Azure SQL Server Elastic Pool name. | `contoso-elastic-pool` |
| `azure.sql_server.name` | string | resource experimental Azure SQL Server name. | `contoso-sql-server` |
| `azure.subscription` | string | resource stable An Azure subscription is a logical container used to provision resources in Azure. Tags: `permission` `primary-field` | `27e9b03f-04d2-2b69-b327-32f433f7ed21` |
| `azure.tags.__tag_key__` | string | resource experimental Contains the value for the tag with the tag key named `__tag_key__` defined in the tag enrichment configuration. | `dt_owner_mail` |
| `azure.tenant.id` | string | resource experimental Unique, immutable identifier assigned to the Azure tenant. | `37c4add3-612a-483d-8b24-cccbb35d3306` |
| `azure.tenant.name` | string | resource experimental Name assigned to the Azure tenant. | `MyAzureTenant` |
| `azure.vm.name` | string | resource experimental Azure Virtual Machine name. | `my-virtual-machine` |
| `azure.vm_scale_set.name` | string | resource experimental Azure Virtual Machine Scale Set name. | `my-vmss` |
| `azure.vmid` | string | resource experimental Azure Virtual Machine unique 128bits identifier | `090556DA-D4FA-764F-A9F1-63614EDA019A` |

## Bizflow

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `bizflow.id` | string | experimental Internal ID from the business flow configured in the Business Flow app. |  |
| `bizflow.priority` | string | experimental The priority of a business process. | `critical`; `high`; `medium`; `low` |
| `bizflow.url` | string | experimental URL to explore the business flow in the Business Flow app from a result in a DQL query against Smartscape nodes. |  |

## BOSH

Fields that are integral to applications managed by BOSH.

### Fields

#### Resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `bosh.availability_zone` | string | resource experimental A specific geographical BOSH location. | `us-east-1a` |
| `bosh.deployment.id` | string | resource stable BOSH depoloyment ID, retrievied from /var/vcap on monitored host. | `cf-c32ffe771e4ad26b9711` |
| `bosh.instance.name` | string | resource stable BOSH instance name, retrievied from /var/vcap on monitored host. | `diego_database` |
| `bosh.instance_id` | string | resource experimental A unique identifier assigned to each deployed instance. | `af318409-9e9d-4a18-aca4-0fb52bbdc526` |
| `bosh.name` | string | resource experimental A unique identifier to a deployment or instance. | `isolated_diego_cell_devima` |
| `bosh.stemcell.version` | string | resource stable Version of BOSH stemcell, retrievied from /var/vcap on monitored host. | `621.448` |

## Browser

The browser namespace contains information on the browser running an application.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `browser.frame.instance_id` | uid | experimental A unique ID generated by RUM JavaScript to identify the browser frame. The `browser.frame.instance_id` is an 8-byte ID and hex-encoded if shown as a string. | `f76281848bd8288c` |
| `browser.frame.parent_instance_id` | uid | experimental A unique ID generated by RUM JavaScript to identify the browser's next-higher frame (if that frame exists and is reachable). The `browser.frame.parent_instance_id` is an 8-byte ID and hex-encoded if shown as a string. | `f76281848bd8288c` |
| `browser.tab.instance_id` | uid | experimental A unique ID generated by RUM JavaScript to identify the browser tab. The `browser.tab.instance_id` is an 8-byte ID and hex-encoded if shown as a string. | `f76281848bd8288c` |
| `browser.window.device_pixel_ratio` | double | experimental The ratio of the resolution in physical pixels to the resolution in CSS pixels for the current display device. | `1.0` |
| `browser.window.height` | long | experimental The browser window's inner height, in pixels. | `384` |
| `browser.window.width` | long | experimental The browser window's inner width, in pixels. | `2048` |

#### Resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `browser.is_webdriver` | boolean | resource experimental If set to `true`, WebDriver controls the browser according to the `navigator.webdriver` property. | `true` |
| `browser.name` | string | resource stable The browser name. | `Chrome` |
| `browser.type` | string | resource stable The browser type. | `desktop`; `mobile`; `tablet`; `robot`; `other` |
| `browser.user_agent` | string | resource stable The full user agent string as provided by the browser in the HTTP `User-Agent` request header. | `Chrome/Version 142.0.7444.176 (Official Build) (arm64)` |
| `browser.version` | string | resource stable The browser version. | `Version 142.0.7444.176` |

## Captured Attributes

Span scoped attributes (e.g. method parameters, return values, class names, â¦) captured by the OneAgent based on a request attribute rule.
The actual name of the attribute is the prefix "captured\_attribute" plus the "request attribute name" defined in the request attributes configuration.
In contrast to request attributes, captured attributes contain the raw values reported by the OneAgent at the location (i.e. on the active span) where they appeared.
No aggregation (first/last value, distinct values, ...), type conversion or normalization is performed on them.
They are the basis for request attributes.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `captured_attribute.__attribute_name__` | array | stable Contains the span scoped raw values that were captured under the name `__attribute_name__` defined by the request attribute configuration. The values are mapped as an array according to the type of the captured attributes, so either boolean, double, long, or string. If the captured attributes have mixed types (e.g. long and string, or double and long, etc.), all attributes are converted to string and stored as string array. | `[42]`; `['Platinum']`; `[32, 16, 8]`; `['Special Offer', '1702']`; `['18.35', '16']` |

## Cassandra

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cassandra.cluster.name` | string | resource experimental |  |

## Continuous Integration/Continuous Deployment

The `cicd` namespace contains information about Continuous Integration and Continuous Deployment systems.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cicd.deployment.id` | string | experimental The identifier of the deployment. | `1337` |
| `cicd.deployment.name` | string | experimental The name of the deployment. | `deploy frontend app`; `deploy cart service` |
| `cicd.deployment.namespace` | string | experimental The destination namespace where the deployment resource is created. | `default` |
| `cicd.deployment.release_stage` | string | experimental The name of the deployment environment, also known as deployment tier. | `development`; `staging`; `production` |
| `cicd.deployment.server.url.full` | string | experimental The deployment server URL. | `https://kubernetes.default.svc` |
| `cicd.deployment.service.id` | string | experimental The identifier of the service that is deployed. | `92ba59d6-379e-4ffd-a67e-d544a9c24dea` |
| `cicd.deployment.status` | string | experimental The status of the deployment. | `failed`; `succeeded` |
| `cicd.pipeline.id` | string | experimental The CI/CD pipeline's identifier, which is unique within one CI/CD system. | `12345` |
| `cicd.pipeline.name` | string | experimental The human-readable name of the CI/CD pipeline. | `CI pipeline for main branch` |
| `cicd.pipeline.run.id` | string | experimental An identifier for a pipeline run, which is unique within one CI/CD system. | `9876` |
| `cicd.pipeline.run.outcome` | string | experimental The outcome of one pipeline run. | `success` |
| `cicd.pipeline.run.queued.duration` | duration | experimental How long was the pipeline run queued before it was started, in nanoseconds. | `1234` |
| `cicd.pipeline.run.url.full` | string | experimental The URL pointing to one specific pipeline run. | `https://github.com/ACME/ACME-repo/actions/runs/9876` |
| `cicd.pipeline.url.full` | string | experimental The CI/CD pipeline's full URL. | `https://github.com/ACME/ACME-repo/actions/workflows/ci-build.yml` |
| `cicd.upstream_pipeline.id` | string | experimental The identifier of the upstream CI/CD pipeline. If a pipeline run was triggered by another pipeline, this attribute is used to reference the triggering pipeline. | `12345` |
| `cicd.upstream_pipeline.run.id` | string | experimental The identifier of the upstream CI/CD pipeline run. If a pipeline run was triggered by another pipeline, this attribute is used to reference the triggering pipeline run. | `1337` |

`cicd.deployment.status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `failed` | The deployment failed. |
| `succeeded` | The deployment succeeded. |

`cicd.pipeline.run.outcome` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `canceled` | The pipeline run was canceled and did not complete. |
| `error` | The pipeline run failed with an error. |
| `failure` | The pipeline run failed. |
| `skipped` | The pipeline did not run, but was skipped. |
| `success` | The pipeline run completed successfully. |
| `timed_out` | The pipeline run timed out, and therefore did not complete. |
| `warning` | The pipeline run completed with at least one warning. |

## Client

The client namespace contains information on the initiator of a network connection.
When observered from the server side, and when communicating through an intermediary,
`client.ip` and `client.port` typically represent the client information behind any intermediaries (such as proxies) if it's available.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `client.address` | string | experimental Client address - domain name if available without reverse DNS lookup; otherwise, IP address or Unix domain socket name. | `client.example.com`; `10.1.2.80`; `[local]` |
| `client.app.name` | string | experimental The name of the client application used to perform the request. | `MS Outlook` |
| `client.ip` | ipAddress | experimental The IP address of the client that makes the request. This can be IPv4 or IPv6. Tags: `sensitive-spans` `sensitive-user-events` | `194.232.104.141`; `2a01:468:1000:9::140` |
| `client.ip.is_public` | boolean | experimental Indicates whether IP is a public IP. | `true` |
| `client.isp` | string | experimental The name of the Internet Service Provider (ISP) associated with the client's IP address. | `Internet Service Provider Name` |
| `client.port` | long | stable Client port number. | `65123`; `80` |

## Cloud

Fields related to cloud deployments that can be used across different providers.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cloud.account.id` | string | resource deprecated Deprecated in favor of cloud specific fields, such as aws.account.id, azure.subscription, gcp.project.id, etc. | `111111111111`; `opentelemetry` |
| `cloud.availability_zone` | string | resource deprecated Deprecated in favor of cloud specific fields, such as aws.availability\_zone, azure.availability\_zones, gcp.zone, etc. | `us-east-1a` |
| `cloud.platform` | string | resource deprecated Deprecated, no replacement available. [1](#fn-2-1-def) | `alibaba_cloud_ecs` |
| `cloud.provider` | string | resource stable Name of the cloud provider. | `alibaba_cloud` |
| `cloud.region` | string | resource deprecated Deprecated in favor of cloud specific fields, such as aws.region, azure.location, gcp.region, etc. | `us-east-1` |
| `cloud.resource_id` | string | resource deprecated Deprecated in favor of cloud specific fields, such as aws.arn, azure.resource.id, gcp.resource.name, etc. | `arn:aws:lambda:REGION:ACCOUNT_ID:function:my-function`; `//run.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/services/SERVICE_ID`; `/subscriptions/<SUBSCIPTION_GUID>/resourceGroups/<RG>/providers/Microsoft.Web/sites/<FUNCAPP>/functions/<FUNC>` |

1

The prefix of the service matches the one specified in `cloud.provider`.

`cloud.platform` MUST be one of the following:

| Value | Description |
| --- | --- |
| `alibaba_cloud_ecs` | Alibaba Cloud Elastic Compute Service |
| `alibaba_cloud_fc` | Alibaba Cloud Function Compute |
| `alibaba_cloud_openshift` | Red Hat OpenShift on Alibaba Cloud |
| `aws_app_runner` | AWS App Runner |
| `aws_ec2` | AWS Elastic Compute Cloud |
| `aws_ecs` | AWS Elastic Container Service |
| `aws_eks` | AWS Elastic Kubernetes Service |
| `aws_elastic_beanstalk` | AWS Elastic Beanstalk |
| `aws_lambda` | AWS Lambda |
| `aws_openshift` | Red Hat OpenShift on AWS (ROSA) |
| `azure_aks` | Azure Kubernetes Service |
| `azure_app_service` | Azure App Service |
| `azure_container_instances` | Azure Container Instances |
| `azure_functions` | Azure Functions |
| `azure_openshift` | Azure Red Hat OpenShift |
| `azure_vm` | Azure Virtual Machines |
| `gcp_app_engine` | Google Cloud App Engine (GAE) |
| `gcp_cloud_functions` | Google Cloud Functions (GCF) |
| `gcp_cloud_run` | Google Cloud Run |
| `gcp_compute_engine` | Google Cloud Compute Engine (GCE) |
| `gcp_kubernetes_engine` | Google Cloud Kubernetes Engine (GKE) |
| `gcp_openshift` | Red Hat OpenShift on Google Cloud |
| `ibm_cloud_openshift` | Red Hat OpenShift on IBM Cloud |
| `tencent_cloud_cvm` | Tencent Cloud Cloud Virtual Machine (CVM) |
| `tencent_cloud_eks` | Tencent Cloud Elastic Kubernetes Service (EKS) |
| `tencent_cloud_scf` | Tencent Cloud Serverless Cloud Function (SCF) |

`cloud.provider` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `alibaba_cloud` | Alibaba Cloud |
| `aws` | Amazon Web Services |
| `azure` | Microsoft Azure |
| `gcp` | Google Cloud Platform |
| `heroku` | Heroku Platform as a Service |
| `ibm_cloud` | IBM Cloud |
| `tencent_cloud` | Tencent Cloud |

#### Span attributes

Fields related to operations related to a cloud.

The `cloud.target` namespace provides information on the entity targeted by outgoing requests.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cloud.target.account.id` | string | experimental The cloud account ID used to access a cloud resource. | `111111111111`; `984398786124` |
| `cloud.target.provider` | string | experimental Name of the cloud provider. | `alibaba_cloud` |
| `cloud.target.region` | string | experimental Identifier of the cloud vendor's data center geographic region. | `us-east-1` |
| `cloud.target.resource_id` | string | experimental Cloud provider-specific native identifier of the accessed cloud resource (for example, an ARN on AWS, a fully qualified resource ID on Azure, or a complete resource name on GCP). If the value is not directly extractable for instrumentation, it can be constructed from its components. | `arn:aws:lambda:REGION:ACCOUNT_ID:function:my-function`; `//run.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/services/SERVICE_ID`; `/subscriptions/<SUBSCIPTION_GUID>/resourceGroups/<RG>/providers/Microsoft.Web/sites/<FUNCAPP>/functions/<FUNC>` |

`cloud.target.provider` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `alibaba_cloud` | Alibaba Cloud |
| `aws` | Amazon Web Services |
| `azure` | Microsoft Azure |
| `gcp` | Google Cloud Platform |
| `heroku` | Heroku Platform as a Service |
| `ibm_cloud` | IBM Cloud |
| `tencent_cloud` | Tencent Cloud |

The `cloud.origin` namespace provides information on the entity from which incoming requests originate.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cloud.origin.account.id` | string | experimental The cloud account ID used to access a cloud resource. | `111111111111`; `984398786124` |
| `cloud.origin.provider` | string | experimental Name of the cloud provider. | `alibaba_cloud` |
| `cloud.origin.region` | string | experimental Identifier of the cloud vendor's data center geographic region. | `us-east-1` |
| `cloud.origin.resource_id` | string | experimental Cloud provider-specific native identifier of the accessed cloud resource (for example, an ARN on AWS, a fully qualified resource ID on Azure, or a complete resource name on GCP). If the value is not directly extractable for instrumentation, it can be constructed from its components. | `arn:aws:lambda:REGION:ACCOUNT_ID:function:my-function`; `//run.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/services/SERVICE_ID`; `/subscriptions/<SUBSCIPTION_GUID>/resourceGroups/<RG>/providers/Microsoft.Web/sites/<FUNCAPP>/functions/<FUNC>` |

`cloud.origin.provider` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `alibaba_cloud` | Alibaba Cloud |
| `aws` | Amazon Web Services |
| `azure` | Microsoft Azure |
| `gcp` | Google Cloud Platform |
| `heroku` | Heroku Platform as a Service |
| `ibm_cloud` | IBM Cloud |
| `tencent_cloud` | Tencent Cloud |

## Cloudfoundry

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cloudfoundry.application.id` | string | resource experimental |  |
| `cloudfoundry.application.name` | string | resource experimental |  |
| `cloudfoundry.instance.index` | string | resource experimental |  |
| `cloudfoundry.space.id` | string | resource experimental |  |
| `cloudfoundry.space.name` | string | resource experimental |  |

## Code

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `code.call_stack` | string | experimental The call stack of the `code.function`. The call stack starts with the `code.function`, and the stack frames are separated by a line feed. | `com.example.SampleClass.doProcessing(SampleClass.java) com.example.SampleClass.doSomeWork(SampleClass.java) com.example.SampleClass.main(SampleClass.java)` |
| `code.filepath` | string | experimental The source code file name that identifies the code unit as uniquely as possible. | `/usr/local/MyApplication/content_root/app/index.php` |
| `code.function` | string | experimental The method or function name, or equivalent (usually the rightmost part of the code unit's name). Represents the name of the function that is represented by this span. | `serveRequest` |
| `code.invoked.filepath` | string | experimental Like `code.filepath`, only it represents the file path of the function that was active when a span has been started. Typically, it is the function that has been instrumented. It should only be set if it differs from `code.filepath`. | `/usr/local/MyApplication/content_root/app/index.php` |
| `code.invoked.function` | string | experimental Like `code.function`, only it represents the function that was active when a span has been started. Typically, it's the function that has been instrumented. The spans duration does not reflect the duration of this function execution. It should only be set if it differs from `code.function`. | `invoke` |
| `code.invoked.namespace` | string | experimental Like `code.namespace`, only it represents the namespace of the function that was active when a span has been started. Typically, it's the function that has been instrumented. It should only be set if it differs from `code.namespace`. | `com.sun.xml.ws.server.InvokerTube$2` |
| `code.line.number` | long | experimental The line number within the source code file. | `1337` |
| `code.namespace` | string | experimental The namespace within which `code.function` is defined. Usually, the qualified class or module name, such that `code.namespace` + some separator + `code.function` forms a unique identifier for the code unit. | `com.example.MyHttpService` |

## Coldfusion

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `coldfusion.jvm.config.file` | string | resource experimental |  |
| `coldfusion.service.name` | string | resource experimental |  |

## Compilation Timings

For some technologies compilation of code might be a significant contributor to request execution time. Compilation timings provide insight into this, where available.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `compilation_timings.compilation_count` | long | experimental The number of compilations contributing to `compilation_timings.duration_sum`. | `7` |
| `compilation_timings.duration_sum` | duration | experimental The total duration in nanoseconds spent compiling. | `6723` |
| `compilation_timings.top_compilations` | record | experimental The top N compilations contributing to `compilation_timings.duration_sum`, represented as map from compilation unit name to duration in nanoseconds spent. | `{'/home/user/test/php/build/tmp/php-htdocs/memcached/memcachedCli.php': 1952, '/home/user/test/php/build/tmp/php-htdocs/curl_cli_uri_filtering.php': 1306}` |

## Container

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `container.id` | string | resource experimental Container ID. Usually a UUID, as for example used to [identify Docker containersï»¿](https://docs.docker.com/engine/containers/run/#container-identification). The UUID might be abbreviated. | `a3bf90e006b2` |
| `container.image.digest` | string | resource experimental Immutable SHAâ256 hash of an image that uniquely identifies the exact image content in a registry. | `sha256:aa1ed41571fa937da61b5bcd7cf842981c7f026b516c18655bc2f3a9362b1fa5` |
| `container.image.name` | string | resource experimental Name of the image the container was built on. | `gcr.io/opentelemetry/operator` |
| `container.image.version` | string | resource experimental | `0.1` |
| `container.name` | string | resource experimental Container name used by container runtime. | `opentelemetry-autoconf` |

## CICS Transaction Gateway

CTG (shorthand for "CICS Transaction Gateway") is a connector for enterprise modernization of CICS assets. It empowers various application
platforms, such as Java servlets, to incorporate CICS programs.

CICS (shorthand for "Customer Information Control System") is a middleware
to support rapid, high-volume online transaction processing on IBM mainframe systems on z/OS. CTG features a client and a server, which
communicate via so-called GatewayRequests.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `ctg.request.call_type` | long | experimental Integer representing the call type of the CTG GatewayRequest. The set of possible values varies per request type. [1](#fn-3-1-def) | `2` |
| `ctg.request.commarea_length` | long | experimental Length of the COMMAREA. Only set when the request type is ECI. | `0` |
| `ctg.request.extend_mode` | long | experimental Integer representing the extended mode of the CTG GatewayRequest. Only set when the request type is ECI. [2](#fn-3-2-def) | `11` |
| `ctg.request.flow_type` | long | experimental Integer representing the flow type of the CTG GatewayRequest. [3](#fn-3-3-def) | `5` |
| `ctg.request.gateway_url` | string | experimental URL of the gateway. Only set on client-side spans. | `tcp://1.2.3.4:5678/` |
| `ctg.request.object_name` | string | experimental Name of the request object. Only set when the request type is ADMIN. |  |
| `ctg.request.server_id` | string | experimental ID of the server. Not set for all request types. | `IPICTEST` |
| `ctg.request.term_id` | string | experimental Name of the terminal resource. Only set when the request type is EPI. | `CN02` |
| `ctg.request.type` | string | experimental Type of the CTG GatewayRequest. | `BASE` |
| `ctg.response.code` | long | experimental CTG response code. The set of possible values varies per request type. [4](#fn-3-4-def) | `-23` |

1

[https://www.ibm.com/docs/api/v1/content/SSZHFX\_9.3.0/basejavadoc/constant-values.htmlï»¿](https://www.ibm.com/docs/api/v1/content/SSZHFX_9.3.0/basejavadoc/constant-values.html)

2

[https://www.ibm.com/docs/api/v1/content/SSZHFX\_9.3.0/basejavadoc/constant-values.htmlï»¿](https://www.ibm.com/docs/api/v1/content/SSZHFX_9.3.0/basejavadoc/constant-values.html)

3

The values are defined in the IBM CTG API source code.

4

[https://www.ibm.com/docs/api/v1/content/SSZHFX\_9.3.0/basejavadoc/constant-values.htmlï»¿](https://www.ibm.com/docs/api/v1/content/SSZHFX_9.3.0/basejavadoc/constant-values.html)

`ctg.request.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `ADMIN` | Admin request. |
| `AUTH` | Authentication request. |
| `BASE` | Base. A base GatewayRequest without a further subtype. [1](#fn-4-1-def) |
| `ECI` | External Call Interface. Enables a client application to call a CICS program synchronously or asynchronously. [2](#fn-4-2-def) |
| `EPI` | External Presentation Interface. Enables a user application to install a virtual IBM 3270 terminal into a CICS server. [3](#fn-4-3-def) |
| `ESI` | External Security Interface. Enables user applications to perform security-related tasks. [4](#fn-4-4-def) |
| `XA` | CICS Request Exit. It can be used for request retry, dynamic server selection, and rejecting non-valid requests. [5](#fn-4-5-def) |

1

[https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=classes-gatewayrequestï»¿](https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=classes-gatewayrequest)

2

[https://www.ibm.com/docs/en/cics-tg-zos/9.1.0?topic=applications-external-call-interface-eciï»¿](https://www.ibm.com/docs/en/cics-tg-zos/9.1.0?topic=applications-external-call-interface-eci)

3

[https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=guide-external-presentation-interface-epiï»¿](https://www.ibm.com/docs/en/cics-tg-multi/8.1?topic=guide-external-presentation-interface-epi)

4

[https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-external-security-interface-esiï»¿](https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-external-security-interface-esi)

5

[https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-creating-cics-request-exitï»¿](https://www.ibm.com/docs/en/cics-tg-zos/9.3.0?topic=applications-creating-cics-request-exit)

## Custom Services

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `custom_service.method` | string | experimental The service method of a custom service. This field only exists if a custom service was created via Dynatrace OneAgent SDK. | `startTask`; `run`; `authenticate` |
| `custom_service.name` | string | experimental The name of a custom service. This field only exists if a custom service was created via Dynatrace OneAgent SDK. | `MyCustomService`; `AuthenticationComponent` |

## Database

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `db.affected_item_count` | long | experimental The number of items (rows, documents,â¦) affected. | `32` |
| `db.collection.name` | string | stable The name of a collection (table, container) within the database. | `customers`; `public.users` |
| `db.connection_string` | string | experimental The connection string for a database connection. Tags: `sensitive-spans` | `jdbc:dynamodb:Access Key=XXX;Secret Key=XXX;Domain=amazonaws.com;Region` |
| `db.cosmosdb.request_charge` | double | experimental The cost of the request in [Azure Cosmos DB request units (RU)ï»¿](https://learn.microsoft.com/en-us/azure/cosmos-db/request-units). | `4.95`; `2.0` |
| `db.dynamodb.table_names` | string[] | experimental The list of tables the request targets. | `['Cats', 'Dogs']` |
| `db.namespace` | string | stable The name of the database, fully qualified within the server address and port. | `customers`; `test.users` |
| `db.operation.name` | string | stable The name of the operation or command executed, for example the MongoDB command name, SQL keyword, Redis command name,â¦ [1](#fn-5-1-def) | `drop`; `findAndModify`; `SELECT`; `PREPARE`; `GetItem`; `set`; `LPUSH`; `mutateIn`; `ReadItems` |
| `db.query.parameters` | record[] | experimental The query parameters used in db.query.text represented as a key and value map. For database systems without named keys, the map key is the string representation of the index starting with 0. Several database requests may get aggregated into a single span. Each entry in the array holds the bind parameters for one database request. Tags: `sensitive-spans` | `[{'name': 'paul', 'age': '23'}, {'name': 'mary', 'age': '32'}]`; `[{'0': 'paul', '1': '23'}, {'0': 'mary', '1': '32'}]` |
| `db.query.text` | string | stable The database query being executed. [2](#fn-5-2-def) | `SELECT * FROM wuser_table`; `SET mykey "WuValue"` |
| `db.result.duration_max` | duration | experimental The maximum duration in nanoseconds used for fetching the result. | `345` |
| `db.result.duration_min` | duration | experimental The minimum duration in nanoseconds used for fetching the result. | `123` |
| `db.result.duration_sum` | duration | experimental The total duration in nanoseconds used for fetching the result. | `234` |
| `db.result.exception_count` | long | experimental The number of exceptions encountered while fetching the result. | `2` |
| `db.result.execution_count` | long | experimental The number of operations executed on the result (for example, fetches from SQL result set, MongoDB cursor operations). | `12` |
| `db.result.roundtrip_count` | long | experimental The number of round-trips triggered by fetching the result. | `2` |
| `db.system` | string | experimental An identifier for the database management system (DBMS) product being used. See below for a list of well-known identifiers. | `mongodb`; `mysql` |

1

Depending on the data provided on ingest, this attribute may be derived by e.g., parsing `db.query.text`. Parsing might fail, or the result might be inaccurate.

2

The value may be sanitized to exclude sensitive information.

`db.system` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `adabas` | Adabas (Adaptable Database System) |
| `amazon-documentdb` | Amazon DocumentDB |
| `aurora-mysql` | Amazon Aurora MySQL |
| `aurora-postgresql` | Amazon Aurora PostgreSQL |
| `cache` | InterSystems CachÃ© |
| `cassandra` | Apache Cassandra |
| `clickhouse` | ClickHouse |
| `cloudscape` | Cloudscape |
| `cockroachdb` | CockroachDB |
| `coldfusion` | ColdFusion IMQ |
| `cosmosdb` | Microsoft Azure Cosmos DB |
| `couchbase` | Couchbase |
| `couchdb` | CouchDB |
| `db2` | IBM Db2 |
| `derby` | Apache Derby |
| `dl/i` | IBM DL/I |
| `dynamodb` | Amazon DynamoDB |
| `edb` | EnterpriseDB |
| `elasticsearch` | Elasticsearch |
| `filemaker` | FileMaker |
| `firebird` | Firebird |
| `firstsql` | FirstSQL |
| `geode` | Apache Geode |
| `h2` | H2 |
| `hanadb` | SAP HANA |
| `hbase` | Apache HBase |
| `hive` | Apache Hive |
| `hsqldb` | HyperSQL DataBase |
| `informix` | Informix |
| `ingres` | Ingres |
| `instantdb` | InstantDB |
| `interbase` | InterBase |
| `keyspaces-cassandra` | Amazon Keyspaces for Apache Cassandra |
| `mariadb` | MariaDB |
| `maxdb` | SAP MaxDB |
| `memcached` | Memcached |
| `mongodb` | MongoDB |
| `mssql` | Microsoft SQL Server |
| `mssqlcompact` | Microsoft SQL Server Compact |
| `mysql` | MySQL |
| `neo4j` | Neo4j |
| `neptune` | Amazon Neptune |
| `netezza` | Netezza |
| `opensearch` | OpenSearch |
| `oracle` | Oracle Database |
| `other_sql` | Some other SQL database. Fallback only. See notes. |
| `pervasive` | Pervasive PSQL |
| `pointbase` | PointBase |
| `postgresql` | PostgreSQL |
| `progress` | Progress Database |
| `redis` | Redis |
| `redshift` | Amazon Redshift |
| `spanner` | Cloud Spanner |
| `sqlite` | SQLite |
| `sybase` | Sybase |
| `teradata` | Teradata |
| `valkey` | Valkey |
| `vertica` | Vertica |

## Deployment Attributes

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `deployment.release_build_version` | string | resource experimental The build version of the deployed product. | `2021-03-24` |
| `deployment.release_product` | string | resource experimental The name of the deployed product. | `WoGo Main` |
| `deployment.release_stage` | string | resource experimental The stage the product is deployed to. | `production` |
| `deployment.release_version` | string | resource experimental The version of the deployed product. | `0.4.1` |

## Device

The device namespace contains information on the device running an application. This should only be used for end-user devices or devices outside of a private infrastructure. In line with the naming conventions and guidelines, we are in this case adhering to the emerging Open Telemetry convention around this, with some additions.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `device.battery.level` | long | experimental The device's battery level in the range 0% (discharged) to 100% (fully charged). | `100` |
| `device.orientation` | string | experimental The device orientation. | `landscape` |

`device.orientation` MUST be one of the following:

| Value | Description |
| --- | --- |
| `landscape` | The device was in landscape mode. |
| `portrait` | The device was in portrait mode. |

#### Resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `device.is_rooted` | boolean | resource experimental If set to `true`, the device is rooted or jailbroken. | `false` |
| `device.manufacturer` | string | resource experimental The device manufacturer. | `Apple` |
| `device.model.identifier` | string | resource experimental The device model identifier. | `iPhone 17 Max Pro` |
| `device.screen.height` | long | resource experimental The device's screen height in its natural orientation. | `1152` |
| `device.screen.width` | long | resource experimental The device's screen width in its natural orientation. | `2048` |

## Disk

Fields describing a disk.

### Fields

#### Resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `disk.all_mountpoints` | string[] | resource experimental List of all mountpoints | `['/mnt/storage', '/home', '/var/log']` |
| `disk.device_name` | string | resource experimental Disk device name (Linux, AIX) | `sda` |
| `disk.mountpoint` | string | resource experimental Primary mountpoint | `/mnt/storage` |
| `disk.remote_disk_id` | long | resource stable Unique identifier of remote disk | `0`; `16864135562327138441`; `18446744073709551615` |

## DL/I Database Attachment

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `db.dli.pcb` | string | experimental The name of the program communication block associated with this DL/I method. | `3`; `MYPCBNAM` |
| `db.dli.pcb_type` | string | experimental The PCB type. | `DC`; `DL/I`; `F/P` |
| `db.dli.processing_options` | string | experimental The PCB processing options. | `GR` |
| `db.dli.segment_level` | string | experimental The hierarchical level of the segment that was matched or returned. | `3`; `24` |
| `db.dli.segment_name` | string | experimental The name of the last segment that was matched or returned. | `PARTROOT` |
| `db.dli.status_code` | string | experimental The DL/I status code. | `QC` |
| `db.dli.terminal_name` | string | experimental The DL/I database or logical terminal name associated with this DL/I method. | `HWSAM5ZD`; `10505` |

`db.dli.pcb_type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `DC` | Data communications. |
| `DL/I` | DL/I db. |
| `F/P` | Fast Path. |

## Dotnet

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dotnet.dll.file` | string | resource experimental Filename of main dotnet assembly. |  |
| `dotnet.dll.path` | string | resource experimental Filepath of main dotnet assembly. |  |

## Dynatrace ActiveGate

Metadata with ActiveGate realated information.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.active_gate.group.name` | string | resource experimental The name of a group that the ActiveGate instance belongs to. | `GdanskLab` |
| `dt.active_gate.id` | string | resource experimental Hexadecimal identifier of the ActiveGate prefixed with `0x` | `0xef3d21c3` |
| `dt.active_gate.module_name` | string | resource experimental The name of ActiveGate module | `autoupdate` |
| `dt.active_gate.working_mode` | string | resource experimental Working mode of the ActiveGate | `cluster` |

`dt.active_gate.working_mode` MUST be one of the following:

| Value | Description |
| --- | --- |
| `cluster` | Cluster ActiveGate |
| `embedded` | Embedded ActiveGate |
| `environment` | Environment ActiveGate |
| `multitenant` | Multitenant ActiveGate |

### API connector fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.active_gate.api_connector.config_id` | string | resource experimental Config long id of the endpoint configuration as a string. | `123`; `9276` |
| `dt.active_gate.api_connector.pipeline_identifier` | string | resource experimental String identifier of an api connector pipeline | `Kubernetes/Topology` |
| `dt.active_gate.api_connector.pipeline_status` | string | resource experimental Status of an api connector pipeline run | `failed` |
| `dt.active_gate.api_connector.technology_id` | string | resource experimental String identifier of an api connector technology | `Kubernetes`; `CloudFoundry`; `AWS`; `Dynatrace Extension`; `Azure` |

`dt.active_gate.api_connector.pipeline_status` MUST be one of the following:

| Value | Description |
| --- | --- |
| `failed` | Pipeline execution failed |
| `skipped` | Pipeline execution skipped |
| `succeeded` | Pipeline execution succeeded |

## Dynatrace OneAgent Metadata

Metadata of the OneAgent module that reported a signal. These attributes are what one would also see in [OneAgent Health](/docs/ingest-from/dynatrace-oneagent/oneagent-health "Discover deployed OneAgent modules at scale and detect anomalies before they turn into problems.").

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.agent.module.health` | string | resource experimental Health status of given OneAgent module | `CRITICAL` |
| `dt.agent.module.id` | uid | resource stable OneAgent module ID. | `031f613871fab0b4`; `fc3cd1bb276f0bed` |
| `dt.agent.module.injection_mode` | string | resource experimental Injection Mode of given OneAgent module | `INJECTION_MODE_AUTO_INJECTED` |
| `dt.agent.module.issues` | array | resource experimental List of issues detected for given OneAgent module | `['QUOTA_OS_EXCEEDED', 'VERSION_TOO_OLD', 'VERSION_NEWER_THAN_BACKEND', 'INSTALLER_VERSION_BAD', 'VERSION_BAD', 'OSI_ID_CLASH', 'HEARTBEAT_OVERDUE', 'AGENT_OUTDATED']` |
| `dt.agent.module.parent_id` | uid | resource stable OneAgent parent module ID, in case this is a so-called sub-agent | `ea89eef5db8b85a9` |
| `dt.agent.module.type` | string | resource stable OneAgent module type | `apache` |
| `dt.agent.module.version` | string | resource stable OneAgent full module version | `1.269.17.20221117-132428` |
| `dt.agent.module.version_short` | string | resource experimental OneAgent short module version, to be expected only on record types where `dt.agent.module.version`'s cardinality would be a problem | `1.269` |
| `dt.agent.monitoring_mode` | string | resource experimental Monitoring Mode in which given OneAgent module operates | `DISCOVERY` |

`dt.agent.module.health` MUST be one of the following:

| Value | Description |
| --- | --- |
| `CRITICAL` | The OneAgent module has critical issues that need immediate attention to ensure proper functionality. |
| `HEALTHY` | The OneAgent module is functioning properly without any detected issues. |
| `INFO` | The OneAgent module has informational messages that may require attention. |
| `WARNING` | The OneAgent module has warnings that indicate potential issues that should be investigated. |

`dt.agent.module.injection_mode` MUST be one of the following:

| Value | Description |
| --- | --- |
| `INJECTION_MODE_AUTO_INJECTED` | The OneAgent module was automatically injected into the application/process. |
| `INJECTION_MODE_MANUALLY_INJECTED` | The OneAgent module was manually injected or installed, requiring explicit user configuration or deployment. |
| `INJECTION_MODE_UNKNOWN` | The injection mode is not known or not determined yet. This is the default/fallback value. |

`dt.agent.module.type` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `apache` | apache |
| `dotnet` | dotnet |
| `dumpproc` | dumpproc |
| `extensions` | extensions |
| `go` | go |
| `iis` | iis |
| `java` | java |
| `log_analytics` | log\_analytics |
| `net` | net |
| `nettracer` | nettracer |
| `nginx` | nginx |
| `nodejs` | nodejs |
| `opentracingnative` | opentracingnative |
| `os` | os |
| `php` | php |
| `plugin` | plugin |
| `process` | process |
| `python` | python |
| `remote_plugin` | remote\_plugin |
| `ruby` | ruby |
| `sdk` | sdk |
| `support` | support |
| `updater` | updater |
| `varnish` | varnish |
| `wsmb` | wsmb |
| `z` | z\_ |

`dt.agent.monitoring_mode` MUST be one of the following:

| Value | Description |
| --- | --- |
| `DISCOVERY` | Discovery monitoring mode provides basic metrics enabling you to discover your hosts and processes and learn the potential to extend your monitoring. |
| `FULL_STACK` | Full stack monitoring mode includes application performance, user experience data, code-level visbility and PurePath insights, as well as everything that is included in Infrastructure monitoring mode. |
| `INFRASTRUCTURE` | Infrastructure monitoring mode includes topology discovery, detailed health and performance monitoring of your host, and enables Network monitoring, Log monitoring and Extensions. |

## Dynatrace AutomationEngine fields

Fields defined in this namespace are used by Dynatrace to describe various aspects of events emitted by the AutomationEngine.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.automation_engine.action.app` | string | experimental The app ID of the app containing the executed action. | `dynatrace.automations` |
| `dt.automation_engine.action.function` | string | experimental Name of the function implementing the action. | `task_1` |
| `dt.automation_engine.action_execution.id` | string | experimental The unique identifier of a action execution as UUID. | `23e7b55a-884f-4497-8ad6-8d49d52b4348` |
| `dt.automation_engine.action_execution.loop.index` | long | experimental Loop index of the action execution. |  |
| `dt.automation_engine.action_execution.retry.count` | long | experimental Retry count of the action execution. |  |
| `dt.automation_engine.is_draft` | boolean | experimental Indicates whether the triggered workflow execution is based on a workflow draft. | `true`; `false` |
| `dt.automation_engine.root_workflow.id` | string | experimental The unique identifier of the root workflow. | `e6388e3a-9db2-4226-9327-2ba86eaf12f7` |
| `dt.automation_engine.root_workflow_execution.id` | string | experimental The unique identifier of the execution of the root workflow. | `a641fb59-4627-44cd-abaf-b68d86455a5b` |
| `dt.automation_engine.state` | string | experimental The state of an execution. Values depend on type of execution (workflow-, task-, or action execution). | `IDLE`; `RUNNING`; `WAITING`; `SUCCESS`; `ERROR`; `CANCELLED` |
| `dt.automation_engine.state.is_final` | boolean | experimental Indicates if `dt.automation_engine.state` is a final and immutable state or if further processing will happen. | `true`; `false` |
| `dt.automation_engine.state_info` | string | experimental Additional info about current state of execution. Typically holds error details. | `ERROR` |
| `dt.automation_engine.task.name` | string | experimental The identifier of a task within a workflow. | `task_1` |
| `dt.automation_engine.task_execution.id` | string | experimental The unique identifier of a task execution as UUID. | `6580d4af-6b1f-4e54-92fa-f47e94507acd` |
| `dt.automation_engine.throttle.limit` | long | experimental The workflow execution per hour limit that has been reached. | `1000` |
| `dt.automation_engine.workflow.id` | string | experimental The unique identifier of a workflow as UUID. | `26c0334e-a3e1-4585-8cd8-2d72742fe141` |
| `dt.automation_engine.workflow.last_execution_state_flip` | boolean | experimental Indicates if the workflow execution state has changed since the last execution, ignoring draft executions. Always false for draft executions. | `true`; `false` |
| `dt.automation_engine.workflow.title` | string | experimental The title of the workflow. | `My Workflow` |
| `dt.automation_engine.workflow.type` | string | experimental Workflow type, either SIMPLE or STANDARD, where SIMPLE comes with restrictions. | `SIMPLE`; `STANDARD` |
| `dt.automation_engine.workflow_execution.actor` | string | experimental The unique identifier of the actor as defined in the workflow. | `e622afae-ccc7-4fb5-acc5-13b32e827bbe` |
| `dt.automation_engine.workflow_execution.id` | string | experimental The unique identifier of a workflow execution as UUID. | `737a248b-d1cb-49a4-bf08-7d4c37dbfb1e` |
| `dt.automation_engine.workflow_execution.trigger.event.id` | string | experimental Unique identifier string (`event.id`) of the event that triggered the workflow execution. Only set for event-triggered executions. | `5547782627070661074_1647601320000` |
| `dt.automation_engine.workflow_execution.trigger.type` | string | experimental The identifier that describes the trigger of the workflow. | `Schedule`; `Event`; `Workflow`; `Manual` |
| `dt.automation_engine.workflow_execution.trigger.user.id` | string | experimental The unique identifier of the user who triggered the workflow execution manually/via API. | `dad18fa7-3c11-40a1-b760-1d8281bb5dcc` |
| `dt.automation_engine.workflow_execution.trigger.workflow_execution.id` | string | experimental The unique identifier of the workflow that triggered the workflow execution. | `737a248b-d1cb-49a4-bf08-7d4c37dbfb1e` |

## Dynatrace Data Acquisition

Attributes defined in this namespace are used by Dynatrace to describe different aspects of the ingested data.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.da.aws.data_firehose.arn` | string | experimental ARN of AWS Data Firehose signal is originating from. | `arn:aws:firehose:us-east-1:111110000111:deliverystream/tenantId-http-endpoint-direct-firehose-stream` |
| `dt.da.aws.log_group` | string | experimental Name of the source Amazon CloudWatch Log group | `/aws/lambda/a-SomeFumction-1AWHD6W1QC5DH` |
| `dt.da.aws.log_stream` | string | experimental Name of the source Amazon CloudWatch Log stream | `2025/02/18/[$LATEST]12312312313123123123123123123123` |
| `dt.da.aws.s3.bucket.name` | string | experimental Name of S3 bucket name signal is originating from | `aws-cloudtrail-logs` |
| `dt.da.aws.s3.key.name` | string | experimental Name of S3 bucket name signal is originating from | `AWSLogs/111110000111/CloudTrail/us-east-1/2025/02/18/111110000111_CloudTrail_us-east-1_20250218T0000Z.json.gz` |
| `dt.da.azure.event_hub.location` | string | experimental The location of the Event Hub that the signal is originating from | `polandcentral` |
| `dt.da.azure.event_hub.name` | string | experimental The name of the Event Hub that the signal is originating from | `logs-ingest-eventHub/logs-ingest` |
| `dt.da.source` | string | experimental Dynatrace source of signal ingestion | `aws-log-ingest` |

`dt.da.source` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `aws-log-ingest` | aws-log-ingest |
| `aws-metric-poller` | aws-metric-poller |
| `aws-metrics-ingest` | aws-metrics-ingest |

## Davis metadata

Some attributes are used in the context of the Davis engine.

### Fields

These fields can be set by Davis routines.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.davis.anomaly_detection.alert` | long | stable Boolean time series of 0 and 1 showing whether a single timespan was alerted due to continuous violations. |  |
| `dt.davis.anomaly_detection.anomaly` | long | stable Boolean timeseries of 0 and 1 showing whether a single timespan is outside the normal value range and therefore considered as abnormal. |  |
| `dt.davis.anomaly_detection.lower` | long | stable The lower value range limit where any value below this point is considered abnormal. |  |
| `dt.davis.anomaly_detection.upper` | long | stable The upper value range limit where any value above this point is considered abnormal. |  |
| `dt.davis.forecast.lower` | long | stable The lower bound of the prediction interval of a given metric forecast. |  |
| `dt.davis.forecast.point` | long | stable The point value of a metric forecast. |  |
| `dt.davis.forecast.upper` | long | stable The upper bound of the prediction interval of a given metric forecast. |  |

## Endpoint Detection

Fields that can be expected on a Dynatrace span where endpoint detection was applied.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.endpoint_detection.rule_id` | uid | experimental The ID of the endpoint detection rule that was applied to that span. | `4d76194c11a9426197a9062548f9e66e` |

## Enrichment

The dt.enrichment namespace contains fields related to Dynatrace Apps and App-Functions that are used for security intelligence enrichment execution.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.enrichment.duration` | duration | experimental The duration of the enrichment execution in nanoseconds. | `4000000000` |
| `dt.enrichment.integration.connection.id` | string | experimental The identifier of the connection settings object used to execute the enrichment. The connection settings object ID refers to the connection in the settings section of the integration app. | `vu9U3hXa3q0AAAABACNhcHA6ZHluYXRyYWNlLmFidXNlaXBkYjpjb25uZWN0aW9ucwAGdGVuYW50AAZ0ZW5hbnQAJDA0NzY2OTJhLTIzMDItMzdhOS05MTk5LTc1ZWI3M2MzNjYwMr7vVN4V2t6t` |
| `dt.enrichment.integration.id` | string | experimental The unique application identifier of the integration app that provided the enrichment functionality. Dynatrace apps are prefixed with 'dynatrace.', custom apps are prefixed with 'my.'. | `dynatrace.abuseipdb`; `dynatrace.virustotal` |
| `dt.enrichment.integration.method.id` | string | experimental The integration method ID of the integration app used to execute the enrichment. | `check-ip`; `enrich-observable` |
| `dt.enrichment.result.is_cached` | boolean | experimental Indicates whether the enrichment execution result was retrieved from the cache. | `true`; `false` |

## Dynatrace Entity IDs

The Dynatrace OneAgent associates monitoring data with a so called Monitored Entity ID (ME ID). On OneAgent monitored environments,
whenever ME IDs are accessible within the monitored system they should be used to enrich monitoring data to facilitate correlations with
data primarily addressed through ME IDs coming from other channels.

The structure for keys that signify entity IDs is `dt.entity.{type of entity}`.
The value associated with such a key must be valid Dynatrace entity identifier
(see [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")).

To allow linking Entity IDs across various different monitoring artifacts (logs, metrics, etc.), all string representations of Entity IDs are required to follow a canonical form, which for all current entities is defined as `PREFIX-0123456789ABCDEF`.

Consumers should treat the token as an opaque value and must not infer any semantics on the ID itself.
Producers need to match the Entity ID that is being returned by Dynatrace Entity API verbatim.

Producers of string representation must treat the string as if it was parsed case-sensitively, even though some parts of the product may be more lenient.
The structure of the entity ID is currently as follows: `<ID-NAMESPACE>-<16-digit-hex-string>`. The `<ID-NAMESPACE>` is type specific but cannot be used to determine the actual entity type reliably, especially in cases of `CUSTOM_DEVICE`. The `<16-digit-hex-string>` needs to be zero-padded (prefix) to a length of 16 digits and must use upper case letters `A-F`.

Current entity IDs in cannonical form can be represented structurally with the following regular expression: `[A-Z][A-Z_]*-[0-9A-F]{16}`.

Additional characters or changes in the format may happen in the future but will not invalidate existing IDs or ID generation rules.

When adding a name to an entity ID via the Grail function [entityName](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entityName "A list of DQL general functions."), by default, the name of the respective entity will be represented as `dt.entity.{type of entity}.name`. Similarly, further entity attributes can be added via the Grail function [entityAttr](/docs/platform/grail/dynatrace-query-language/functions/general-functions#entityAttr "A list of DQL general functions."), resulting in additional field(s) following the naming convention `dt.entity.{type of entity}.{name of attribute}`.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.entity.application` | string | resource stable The ME ID of a web application. Tags: `entity-id` | `APPLICATION-DC92E74A7A844E6E` |
| `dt.entity.aws_availability_zone` | string | resource stable An entity ID of an entity of type AWS\_AVAILABILITY\_ZONE Tags: `entity-id` | `AWS_AVAILABILITY_ZONE-6000A4E2BD2AB971` |
| `dt.entity.azure_region` | string | resource stable An entity ID of an entity of type AZURE\_REGION Tags: `entity-id` | `AZURE_REGION-0DD5C79E4034F0AA` |
| `dt.entity.azure_vm` | string | resource stable An entity ID of an entity of type AZURE\_VM Tags: `entity-id` | `AZURE_VM-326478B733D6CFB0` |
| `dt.entity.cloud_application` | string | resource stable An entity ID of an entity of type CLOUD\_APPLICATION. Tags: `entity-id` | `CLOUD_APPLICATION-3AB5BBF3E09A7942` |
| `dt.entity.cloud_application_instance` | string | resource stable An entity ID of an entity of type CLOUD\_APPLICATION\_INSTANCE. Tags: `entity-id` | `CLOUD_APPLICATION_INSTANCE-E0D8F94D9065F24F` |
| `dt.entity.cloud_application_namespace` | string | resource stable An entity ID of an entity of type CLOUD\_APPLICATION\_NAMESPACE. A CLOUD\_APPLICATION\_NAMESPACE is a Kubernetes namespace. Tags: `entity-id` | `CLOUD_APPLICATION_NAMESPACE-C61324AA70F57BCB` |
| `dt.entity.container_group` | string | resource stable An entity ID of an entity of type CONTAINER\_GROUP. Tags: `entity-id` | `CONTAINER_GROUP-7C2B1C24FFB288CB` |
| `dt.entity.container_group_instance` | string | resource stable An entity ID of an entity of type CONTAINER\_GROUP\_INSTANCE. Tags: `entity-id` | `CONTAINER_GROUP_INSTANCE-F4A1347110826781` |
| `dt.entity.custom_application` | string | resource stable The ME ID of a custom application. Tags: `entity-id` | `CUSTOM_APPLICATION-343A92501A51F286` |
| `dt.entity.custom_device` | string | resource stable An entity ID of an entity of type CUSTOM\_DEVICE. Tags: `entity-id` | `CUSTOM_DEVICE-E0D8F94D9065F24F` |
| `dt.entity.device_application` | string | resource experimental The ME ID of a device application. | `DEVICE_APPLICATION-EA8A8751A60D5BCE8` |
| `dt.entity.disk` | string | resource stable An entity ID of an entity of type DISK Tags: `entity-id` | `DISK-5472CBC1ED0981D6` |
| `dt.entity.ec2_instance` | string | resource stable An entity ID of an entity of type EC2\_INSTANCE Tags: `entity-id` | `EC2_INSTANCE-0004DD30F142D18C` |
| `dt.entity.external_synthetic_test` | string | resource stable An entity ID of an entity of type EXTERNAL\_SYNTHETIC\_TEST. Tags: `entity-id` | `EXTERNAL_SYNTHETIC_TEST-A140F3B85BCCBD1A` |
| `dt.entity.external_synthetic_test_step` | string | resource stable An entity ID of an entity of type EXTERNAL\_SYNTHETIC\_TEST\_STEP. Tags: `entity-id` | `EXTERNAL_SYNTHETIC_TEST_STEP-A140F3B85BCCBD1A` |
| `dt.entity.gcp_zone` | string | resource stable An entity ID of an entity of type GCP\_ZONE Tags: `entity-id` | `GCP_ZONE-3699CB75E19C8505` |
| `dt.entity.host` | string | resource stable An entity ID of an entity of type HOST. Tags: `entity-id` | `HOST-E0D8F94D9065F24F` |
| `dt.entity.host_group` | string | resource stable An entity ID of an entity of type HOST\_GROUP. Tags: `entity-id` | `HOST_GROUP-E7FBBCF7B1467174` |
| `dt.entity.http_check` | string | resource stable An entity ID of an entity of type HTTP\_CHECK. Tags: `entity-id` | `HTTP_CHECK-A140F3B85BCCBD1A` |
| `dt.entity.http_check_step` | string | resource stable An entity ID of an entity of type HTTP\_CHECK\_STEP. Tags: `entity-id` | `HTTP_CHECK_STEP-A140F3B85BCCBD1A` |
| `dt.entity.kubernetes_cluster` | string | resource stable An entity ID of an entity of type KUBERNETES\_CLUSTER. Tags: `entity-id` | `KUBERNETES_CLUSTER-E0D8F94D9065F24F` |
| `dt.entity.kubernetes_node` | string | resource stable An entity ID of an entity of type KUBERNETES\_NODE. Tags: `entity-id` | `KUBERNETES_NODE-874C66B68CE15070` |
| `dt.entity.kubernetes_service` | string | resource stable An entity ID of an entity of type KUBERNETES\_SERVICE. Tags: `entity-id` | `KUBERNETES_SERVICE-FE6E75BB9DF02347` |
| `dt.entity.mobile_application` | string | resource stable The ME ID of a mobile application. Tags: `entity-id` | `MOBILE_APPLICATION-E8A8751A60D5BCE8` |
| `dt.entity.multiprotocol_monitor` | string | resource stable An entity ID of an entity of type MULTIPROTOCOL\_MONITOR. Tags: `entity-id` | `MULTIPROTOCOL_MONITOR-A140F3B85BCCBD1A` |
| `dt.entity.network_interface` | string | resource stable An entity ID of an entity of type NETWORK\_INTERFACE Tags: `entity-id` | `NETWORK_INTERFACE-FC7B4A5937FC125C` |
| `dt.entity.process_group` | string | resource stable An entity ID of an entity of type PROCESS\_GROUP. Tags: `entity-id` | `PROCESS_GROUP-E0D8F94D9065F24F` |
| `dt.entity.process_group_instance` | string | resource stable An entity ID of an entity of type PROCESS\_GROUP\_INSTANCE. Tags: `entity-id` | `PROCESS_GROUP_INSTANCE-E0D8F94D9065F24F` |
| `dt.entity.service` | string | resource stable An entity ID of an entity of type SERVICE. Tags: `entity-id` | `SERVICE-57EC3CFC1FE72449` |
| `dt.entity.service_method` | string | resource stable An entity ID of an entity of type SERVICE\_METHOD. Tags: `entity-id` | `SERVICE_METHOD-659B35CA9AAC96C1` |
| `dt.entity.service_method_group` | string | resource stable An entity ID of an entity of type SERVICE\_METHOD\_GROUP. Tags: `entity-id` | `SERVICE_METHOD_GROUP-02000E1DB1CDAF9F` |
| `dt.entity.software_component` | string | resource stable An entity ID of an entity of type SOFTWARE\_COMPONENT. Tags: `entity-id` | `SOFTWARE_COMPONENT-4700CB75E19C8506` |
| `dt.entity.synthetic_location` | string | resource stable An entity ID of an entity of type SYNTHETIC\_LOCATION. Tags: `entity-id` | `SYNTHETIC_LOCATION-D140F3B85BCCBD1A` |
| `dt.entity.synthetic_test` | string | resource stable An entity ID of an entity of type SYNTHETIC\_TEST. Tags: `entity-id` | `SYNTHETIC_TEST-A140F3B85BCCBD1A` |
| `dt.entity.synthetic_test_step` | string | resource stable An entity ID of an entity of type SYNTHETIC\_TEST\_STEP. Tags: `entity-id` | `SYNTHETIC_TEST_STEP-A140F3B85BCCBD1A` |

## Dynatrace Extensions

Additional extension information sent via self-monitoring.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.extension.config.id` | string | resource experimental Extension's monitoring configuration identifier. | `vu9U3hXa3q0AAAABAAtleHQ6ZXh0LTA0MAAIYWdfZ3JvdXAAA0FHMQAkMjY2YTIyM2YtZDgxYi0zNTNjLThlYzctYzk2YzliZjg4OGQ3vu9U3hXa3q0` |
| `dt.extension.controller.pod.uid` | string | resource experimental Extension controller pod UID. [1](#fn-6-1-def) | `87654321-4321-4321-4321-cba987654321` |
| `dt.extension.ds` | string | resource experimental Name of the data source. | `SNMPTrap` |
| `dt.extension.endpoint.hints` | string[] | resource experimental Hints to provide for the cluster in order to find proper endpoint in task registry. | `['nat-test.lab.dynatrace.org', '1521', 'orc']` |
| `dt.extension.executor.pod.uid` | string | resource experimental Extension executor pod UID. [2](#fn-6-2-def) | `12345678-1234-1234-1234-123456789abc` |
| `dt.extension.name` | string | resource experimental Name of the extension. | `com.snmptrap.generic` |
| `dt.extension.python_version` | string | resource experimental Version of the Python runtime version used by extension. | `3.14` |
| `dt.extension.status` | string | resource experimental The status of the component reporting a self-monitoring event. | `AUTHENTICATION_ERROR` |
| `dt.extension.version` | string | resource experimental Version of the extension. | `0.0.1` |

1

This attribute is only set when the extension is running in a Kubernetes environment.

2

This attribute is only set when the extension is running in a Kubernetes environment.

`dt.extension.status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `AUTHENTICATION_ERROR` | Unable to connect to EEC |
| `DEVICE_CONNECTION_ERROR` | Failed to establish connection with the device |
| `EEC_CONNECTION_ERROR` | Unable to connect to EEC |
| `GENERIC_ERROR` | Generic status used to communicate job failed |
| `INVALID_ARGS_ERROR` | Invalid arguments |
| `INVALID_CONFIG_ERROR` | Config provided by EEC is invalid |
| `OK` | Extension works fine |
| `UNKNOWN_ERROR` | Uninitialized/unknown error |

### Process Grouping Fields

Attributes used for Process Group enrichment in extensions.

## Dynatrace ingest fields

Attributes defined in this namespace are used by Dynatrace to describe different aspects of the ingested data.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.ingest.debug_messages` | string[] | experimental An array of strings that represent debug messages that provide a detailed debugging information. That could include even variable parts, like which attribute was modified, or which processing rules were applied. | `['MyATTribute mapped to myAttribute']` |
| `dt.ingest.format` | string | experimental The format of the data ingested in Dynatrace via the various ingest channels. E.g., Generic log ingest, OTLP logs ingest | `dtapi/json`; `otlp/protobuf` |
| `dt.ingest.origin` | string | experimental Origin of the data ingested in Dynatrace. | `splunk`; `cribl` |
| `dt.ingest.size` | long | stable The size of the ingested data point in bytes. | `2005` |
| `dt.ingest.warnings` | string[] | experimental An array of strings representing markers of unexpected situations that might affect the correctness or completeness of incoming data points. It might be, for instance, limits applied or a processing rule failing. It should not be a detailed log of what happened, just the high-level class of the issue that occurred. | `['attr_count_trimmed', 'content_trimmed']` |

`dt.ingest.format` MUST be one of the following:

| Value | Description |
| --- | --- |
| `dtapi/json` | JSON data ingested via the Dynatrace APIs or via EEC (Extension Execution Controller) |
| `dtapi/plaintext` | (deprecated: use "plaintext") Plain text data ingested via the Dynatrace API |
| `journald` | Journald data ingested via OneAgent |
| `otlp/json` | OpenTelemetry Protocol (OTLP) JSON data ingested via the Dynatrace APIs |
| `otlp/protobuf` | OpenTelemetry Protocol (OTLP) Protobuf data ingested via the Dynatrace APIs or via EEC (Extension Execution Controller) |
| `plaintext` | Plain text data ingested via the Dynatrace APIs, EEC (Extension Execution Controller) or OneAgent |
| `syslog` | Syslog data ingested via OneAgent or via EEC (Extension Execution Controller) |
| `unknown` | The data format was not recognized (only for metrics dimension) |
| `windowseventlog` | Windows event log data ingested via OneAgent |

`dt.ingest.warnings` MUST contain only values from the following list:

| Value | Description |
| --- | --- |
| `content_trimmed` | The content was trimmed, right after receiving it by Cluster/ActiveGate, because it exceeded the event content max byte size limit. |
| `content_trimmed_pipe` | The content was trimmed in post-processing (after applying processing rules) because it exceeded the event content max byte size limit |
| `attr_count_trimmed` | The number of attributes was trimmed, right after receiving it by Cluster/ActiveGate, because it exceeded the max number of attributes limit. |
| `attr_count_trimmed_pipe` | The number of attributes was trimmed in post-processing (after applying processing rules) because it exceeded the max number of attributes limit. |
| `attr_key_case_mismatch` | The attribute key is detected that matches the custom attribute key or the semantic attribute key, but there is the attribute key case mismatch. |
| `attr_key_trimmed` | The attribute key was trimmed, right after receiving it by Cluster/ActiveGate, because it exceeded the max key length limit. |
| `attr_val_count_trimmed` | At least one multi-value attribute had values number trimmed, right after receiving it by Cluster/ActiveGate, because it exceeded the max number of attributes limit. |
| `attr_val_count_trimmed_pipe` | After applying processing rules, at least one multi-value attribute had its values number trimmed (after using processing rules) because it exceeded the maximum number of attributes limit. |
| `attr_val_size_trimmed` | At least one attribute had its value size trimmed, right after receiving it by Cluster/ActiveGate, because it exceeded the max value size in bytes limit. |
| `attr_val_size_trimmed_pipe` | At least one attribute had its value size trimmed (after applying processing rules) because it exceeded the max value size in bytes limit. |
| `timestamp_corrected` | Timestamp was too far in the future and was corrected to current time. |
| `common_attr_corrected` | STATUS, LOG\_LEVEL or EVENT\_TYPE attribute was corrected. |
| `processing_batch_timeout` | Batch timeout occurred during processing pipeline. |
| `processing_transformer_timeout` | Execution timeout in one of processing transformers occurred during processing pipeline. |
| `processing_transformer_error` | Execution error in one of processing transformers occurred during processing pipeline. |
| `processing_transformer_throttled` | Execution throttled in one of processing transformers during processing pipeline. |
| `processing_output_record_conversion_error` | Output conversion error occurred for some record during processing pipeline. |
| `processing_prepare_input_error` | Prepare input error occurred in one of enabled processing pipeline rules. |

## Dynatrace

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.cost.costcenter` | string | resource stable Can be used to assign usage to a Cost Center. | `Team A` |
| `dt.cost.product` | string | resource stable Can be used to assign usage to a Product or Application ID. | `Product A` |
| `dt.host_group.id` | string | resource stable See [Organize your environment using host groups](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."). Note that host groups are identified by their name, not by the entity ID of the host group entity. For details on the entity ID, see `dt.entity.host_group`. Tags: `permission` `primary-field` | `myHostGroup` |
| `dt.metrics.source` | string | resource experimental The source from which metrics are ingested. [1](#fn-7-1-def) | `telegraf`; `com.dynatrace.extension.sql-oracle` |
| `dt.network_zone.id` | string | resource experimental The ID of the network zone. See [Dynatrace Documentation](/docs/dynatrace-api/environment-api/network-zones/get-network-zone "View the configuration of a network zone via the Dynatrace API.") | `vpc-123` |
| `dt.openpipeline.forwarding.config_id` | string | resource experimental ID of the forwarding configuration in OpenPipeline. | `v00zu89AAABADJidWlsdGluOmh5cGVyc2NhbGVyLWF1dGhlbnRpY2F0aW9uLmNvpb25zLmF3cwAGdGVuYW50AGZ7ZW5hbnQAJDNlOTM1YmE3LTkzODUtMzczZS1hMWJiLW9uioQwNDFmNzIyMb7vVN4V2t6t` |
| `dt.openpipeline.forwarding.datatype` | string | resource experimental Forwarded datatype | `Logs` |
| `dt.pg_detection.cluster.id` | string | resource experimental `DT_CLUSTER_ID` environment variable; also see [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") |  |
| `dt.pg_detection.custom_entry` | string | resource experimental also see [Define metadata via environment variables](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment.") |  |
| `dt.pg_detection.declarative.id` | string | resource experimental |  |
| `dt.pg_detection.environment.id` | string | resource experimental `DT_ENVIRONMENT_ID` environment variable |  |
| `dt.pg_detection.node.id` | string | resource experimental `DT_NODE_ID` environment variable; also see [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") |  |
| `dt.process_group.detected_name` | string | resource stable The name of the process group as it was detect by the agent. | `Apache Web Server httpd`; `Redis unguard-redis-* redis`; `Linux System` |
| `dt.process_group.id` | string | resource experimental The identifier shared by all entities belonging to a given process group. | `PROCESS_GROUP-1234` |
| `dt.security_context` | string | resource stable The security context is used in access permissions to limit the visibility. Learn more about the [Dynatrace permission model](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.") Tags: `permission` |  |
| `dt.smartscape_source.id` | smartscapeId | resource experimental The ID of the entity considered the source of the signal. The string represents an entity ID of an entity that is stored in the Smartscape storage. [2](#fn-7-2-def) Tags: `smartscape-id` | `K8S_CLUSTER-E0D8F94D9065F24F`; `AWS_LAMBDA_FUNCTION-E0D8F94D9065F24F` |
| `dt.smartscape_source.type` | string | resource stable The entity type of the entity whose identifier is held in dt.smartscape\_source.id. | `K8S_CLUSTER`; `AWS_LAMBDA_FUNCTION` |
| `dt.source_entity` | string | resource stable The ID of the entity considered the source of the signal. The string represents an entity ID of an entity that is stored in the classic entity storage. [3](#fn-7-3-def) Tags: `entity-id` | `HOST-E0D8F94D9065F24F`; `PROCESS_GROUP_INSTANCE-E0D8F94D9065F24F` |
| `dt.source_entity.type` | string | resource stable The entity type of the entity whose identifier is held in dt.source\_entity. The value must be a valid entity type and consistent with `dt.source_entity`. Note, however, that the type identifiers are expected to be lowercased in alignment with suffixes of dt.entity.\* keys. | `host`; `process_group_instance`; `cloud:azure:resource_group` |

1

This is the framework used for capturing, processing and forwarding metrics, *not* the emitting monitored entity. Exemplary custom value: name of an extension sending metrics.

2

The value of this field will be based on one of `dt.smartscape.<type>` fields value. That means that both fields `dt.smartscape_source.id` and `dt.smartscape.<type>` will be set to the same ID.

3

The value of this field will be based on one of the `dt.entity.<type>` fields value. This means that both `dt.source_entity` and `dt.entity.<type>` fields will be set to the same ID.

`dt.metrics.source` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `dynatrace_codemodule` | dynatrace\_codemodule |
| `dynatrace_ingest` | dynatrace\_ingest |
| `dynatrace_osagent` | OsAgent |
| `micrometer` | Micrometer |
| `oneagent_metric_api` | OneAgentMetricAPI |
| `opentelemetry` | OpenTelemetry |
| `statsd` | StatsD |
| `telegraf` | Telegraf |

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.has_container_application_monitoring` | boolean | experimental Indicates that the underlying container of the data point should be considered in Container Application Monitoring license. Set to `true` for the opt-in of Container Application Monitoring. Setting to `false` is not supported by the backend and has no effect. | `true`; `false` |
| `dt.maintenance_window_ids` | array | experimental UUIDs of maintenance windows. | `c715d677-eb1b-3e1b-8dbc-db06cad5b8eb` |
| `dt.query` | string | experimental A query in the DQL format, see [Dynatrace Query Langauge](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). | `timeseries avg(dt.host.cpu.idle)`; `fetch logs` |
| `dt.raw_data` | string | experimental The complete content of the record as it was originally accepted by Dynatrace, stored as a string in JSON format. This field captures the unaltered data for reference, debugging, or auditing purposes | `{"content": "example record content"}` |

## Dynatrace OpenPipeline fields

Fields defined in this namespace are used by Dynatrace to describe various aspects of the data ingested through OpenPipeline, providing detailed insights into the ingestion process.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.openpipeline.pipelines` | string[] | resource experimental Collects the identifiers of all pipelines through which a record has passed during the ingestion process in OpenPipeline, providing a complete trace of its journey. | `['logs:default']`; `['logs:pipeline_haproxy_2656', 'bizevents:default']` |
| `dt.openpipeline.source` | string | resource experimental Identifies the source (such as API endpoints or OneAgent) used for ingesting the record into OpenPipeline. | `/platform/ingest/v1/events`; `oneagent` |
| `dt.openpipeline.source_type` | string | resource experimental Identifies the source type used to ingest data in Dynatrace, for example, from OTLP and OneAgent. | `otlp`; `oneagent` |

`dt.openpipeline.source_type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `api` | Logs ingested via one of the ActiveGate APIs |
| `aws_firehose` | Logs ingested via Amazon Data Firehose |
| `extension` | Logs ingested via the EEC running on host |
| `oneagent` | Logs ingested via OneAgent |
| `otlp` | Logs ingested via the OpenTelemetry Protocol (OTLP) |
| `unknown` | The source type was not recognized (only for metrics dimension) |

## OS service

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.osservice.alerting` | boolean | stable Boolean attribute deciding whether the service status triggers alerts or not. |  |
| `dt.osservice.status` | string | stable Current running state. | `activating` |

`dt.osservice.status` MUST be one of the following:

| Value | Description |
| --- | --- |
| `activating` | Service is activating. |
| `active` | Service is active. |
| `continue_pending` | Service continues pending. |
| `deactivating` | Service is deactivating. |
| `failed` | Service failed to start. |
| `inactive` | Service is inactive. |
| `pause_pending` | Service paused pending. |
| `paused` | Service is currently paused. |
| `reloading` | Service is reloading. |
| `running` | Service is currently running. |
| `start_pending` | Service started pending. |
| `stop_pending` | Service stopped pending. |
| `stopped` | Service is currently stopped. |

#### Resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.osservice.display_name` | string | resource stable On Linux based systems this value ought to be the same as in the name attribute. On Windows it will be a prettier version of the name attribute. | `My OS Service` |
| `dt.osservice.manufacturer` | string | resource stable Manufacturer of the service. On Linux based systems, the value will always be `-`, meaning empty. | `-`; `SSH Corp.` |
| `dt.osservice.name` | string | resource stable Unique OS service name. | `myosservice` |
| `dt.osservice.path` | string | resource stable The full path to the process executable. On Linux based systems, this can be set to the target of `proc/[pid]/exe`. On Windows, it can be set to the result of `GetProcessImageFileNameW`. | `/usr/bin/cmd/otelcol` |
| `dt.osservice.startup_type` | string | resource stable Current startup type. | `auto` |

`dt.osservice.startup_type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `auto` | Windows specific. Automatic: The service starts at system logon. |
| `auto_delay` | Windows specific. Automatic (Delayed Start): The service starts a short while after the system has finished starting up. |
| `auto_delay_trigger` | Windows specific. Automatic (Delayed Start, Trigger Start) |
| `auto_trigger` | Windows specific. Automatic (Trigger Start): This service will start automatically at boot. |
| `disabled` | Linux specific. Service is configured to not start when the system boots, but can be started manually, or as a dependency of another service. |
| `enabled` | Linux specific. Service is marked for starting up on boot. |
| `enabled-runtime` | Linux specific. Service is marked for starting up on boot. |
| `manual` | Windows specific. Manual: The service starts only when explicitly summoned. |
| `manual_trigger` | Windows specific. Manual (Trigger Start): This service will not start automatically at boot. |
| `static` | Linux specific. Service will run only if another unit depends on it. |

## Dynatrace RUM

The `dt.rum` namespace contains Dynatrace RUM specific fields.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.rum.application.entity` | string | experimental An entity ID of an entity of type APPLICATION or MOBILE\_APPLICATION. Tags: `entity-id` | `APPLICATION-DC92E74A7A844E6E`; `MOBILE_APPLICATION-E8A8751A60D5BCE8` |
| `dt.rum.application.id` | string | stable The Dynatrace RUM application ID. For mobile applications, a UUID is used. For web applications, an 8-byte HEX string is used. | `ea7c4b59f27d43eb`; `89b1a1e7-fe89-4151-81e9-410fa0235f0d` |
| `dt.rum.browser.session_id` | string | experimental The browser session ID, taken from the dtCookie value. Not applicable for OneAgent for Mobile. | `4D3133F359A76AB05AAF39691696858A` |
| `dt.rum.is_linking_candidate` | boolean | experimental If set to 'true', it indicates that Dynatrace RUM captured a user event that can be linked to this trace. | `true` |
| `dt.rum.session.id` | string | stable A unique ID that represents the user session. | `HOPCPWKILUKHFHWRRQGBHHPAFLUJUOSH-0`; `23626166142035610_1-0` |
| `rum_link` | record | experimental A RUM link provides backend to frontend linking information from traces to Dynatrace RUM. Unlike span links which reference other spans, the RUM link connects a span to a user event and/or user session. |  |

#### Resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.rum.agent.type` | string | resource experimental The Dynatrace RUM agent type. | `android` |
| `dt.rum.agent.version` | string | resource experimental The version of the Dynatrace RUM agent. It is provided in the format major.minor.patch.build. The build number is optional. | `8.263.1`; `9.293.2.1`; `1.313.0.20250402-172634` |
| `dt.rum.event.source.type` | string | resource experimental The Dynatrace RUM source technology that produced this event. Only used by cross-platform implementations, otherwise the field is omitted. | `flutter` |
| `dt.rum.instance.id` | string | resource stable The RUM application instance ID. (This was formerly called the "Visitor id", "internal user ID", and "rxVisitor cookie value".) | `3735928559`; `1742973444821E7E6Q3E3SG28ATQPAGTT6T8HU92VFRFQ` |
| `dt.rum.schema_version` | string | resource stable The Dynatrace RUM enrichment version. | `0.1` |
| `dt.rum.user_type` | string | resource experimental The RUM user type. | `real_user` |

`dt.rum.agent.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `android` | OneAgent for Android |
| `ios` | OneAgent for iOS |
| `javascript` | RUM JavaScript |

`dt.rum.event.source.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `flutter` | Flutter |
| `react_native` | React Native auto-instrumentation |

`dt.rum.user_type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `real_user` | The user event was produced by a real user. |
| `robot` | The user event was produced by a bot user. |
| `synthetic` | The user event was produced by a synthetic test. |

#### Invalid fields

The `dt.rum.invalid` namespace is used for fields that are removed because of user event ingest validation.
For example, if the calculated `web_vitals.largest_contentful_paint` value would be less than 0, the value is copied over to `dt.rum.invalid.web_vitals.largest_contentful_paint` and `web_vitals.largest_contentful_paint` is removed.

## Settings

Fields for referencing Settings 2.0 objects, schemas and scopes.

### Considerations on which fields to use

Although the `dt.settings.object_id` is enough to identify a specific settings value within a dynatrace environment, adding explicit information about the schema, scope and/or scope type can be useful nonetheless. If your use-case will only ever involve a single schema, scope type and/or scope, documenting this is good enough - if multiple schemas, scope types and/or scopes can be involved, filling the corresponding fields is strongly recommended.

`dt.settings.references` can be used if multiple settings objects need to be referenced. In that case, each entry in the array can hold a reference to a single settings object.

### Top level fields

The top level fields contain generally relevant information for all monitoring data.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.settings.object_id` | string | experimental The object ID of a settings value. This corresponds to the 'objectId' field/parameter in the Settings API. | `vu9U3hXa3q0AAAABACFidWlsdGluOnJ1bS51c2VyLWV4cGVyaWVuY2Utc2NvcmUABnRlbmFudAAGdGVuYW50ACRhMzZmYmYwMy00NDY1LTNlNTYtOTZiOS1kOWMzOGQ3MzU1NmO-71TeFdrerQ` |
| `dt.settings.object_summary` | string | experimental The human-readable summary or name of a single value of a multi-value settings schema. This corresponds to the 'summary' field in the Settings API. | `Journey Service all errors`; `Really, this can be anything`; `My alerting rule` |
| `dt.settings.references` | record[] | experimental A collection of references to settings objects. Each entry in the array holds a reference to a single settings object. | `[{'dt.settings.object_id': 'vu9U3hXa3q0AAAABACFidWlsdGluOnJ1bS51c2VyLWV4cGVyaWVuY2Utc2NvcmUABnRlbmFudAAGdGVuYW50ACRhMzZmYmYwMy00NDY1LTNlNTYtOTZiOS1kOWMzOGQ3MzU1NmO-71TeFdrerQ', 'dt.settings.relationship': 'matched_rule'}, {'dt.settings.object_id': 'vu9U3hXa3q0AAAABAB9idWlsdGluOmRhdmlzLmFub21hbHktZGV0ZWN0b3JzAAZ0ZW5hbnQABnRlbmFudAAkMzM2NTc3MTgtYWNjYi0zOGY1LTlmOGUtMTg5NTBiYmNjNmRhvu9U3hXa3q0', 'dt.settings.relationship': 'triggered_alert'}]` |
| `dt.settings.relationship` | string | experimental The type of relationship to the referenced settings object. You can use arbitrary values (in `snake_case`) here that describe the relationship for your use-case. | `matched_rule`; `triggered_alert` |
| `dt.settings.schema_id` | string | experimental The schema ID of a settings schema, as used in the Settings APIs. | `builtin:problem.notifications`; `app:dynatrace.jenkins:connection` |
| `dt.settings.schema_version` | string | experimental The version of the schema referenced by dt.settings.schema\_id, as declared by the schema itself. Typically a semantic version number. | `1.0.0`; `1.2.3` |
| `dt.settings.scope_id` | string | experimental The ID of the scope that a settings object is persisted on. This corresponds to the 'scope' field/parameter in the Settings API. | `environment`; `HOST-EFAB6D2FE7274823` |
| `dt.settings.scope_name` | string | experimental The human-readable name of the scope that a settings object is persisted on. | `deb-10-k3s-oi-01.lab.dynatrace.org` |
| `dt.settings.scope_type` | string | experimental The type of the scope that a settings object is persisted on. | `environment`; `host_group`; `host` |

## Smartscape IDs

This namespace contains all field names that contain entitiy IDs that are stored in Smartscape on Grail. To ensure we can distinguish between classic entity IDs and Smartscape IDs, we use the `dt.smartscape.*` namespace to enrich entity IDs in signal data.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.smartscape.__type__` | smartscapeId | resource stable A Smartscape ID that can be used to query entities from the Smartscape storage. `__type__` is a placeholder for any Smartscape type. Tags: `smartscape-id` | `K8S_CLUSTER-E0D8F94D9065F24F` |
| `dt.smartscape.aws_account` | string | resource stable Smartscape ID referencing an AWS Account entity. Tags: `smartscape-id` | `AWS_ACCOUNT-5566FFEE77889900` |
| `dt.smartscape.aws_availability_zone` | string | resource stable Smartscape ID referencing an AWS Availability Zone. Tags: `smartscape-id` | `AWS_AVAILABILITY_ZONE-6677001122334455` |
| `dt.smartscape.aws_ec2_eip` | string | resource stable Smartscape ID referencing an AWS Elastic IP. Tags: `smartscape-id` | `AWS_EC2_EIP-7788112233445566` |
| `dt.smartscape.aws_ec2_instance` | string | resource stable Smartscape ID referencing an AWS EC2 Instance. Tags: `smartscape-id` | `AWS_EC2_INSTANCE-8899223344556677` |
| `dt.smartscape.aws_ec2_networkinterface` | string | resource stable Smartscape ID referencing an EC2 Network Interface. Tags: `smartscape-id` | `AWS_EC2_NETWORKINTERFACE-99AA334455667788` |
| `dt.smartscape.aws_ec2_securitygroup` | string | resource stable Smartscape ID referencing an EC2 Security Group. Tags: `smartscape-id` | `AWS_EC2_SECURITYGROUP-AABB334455667788` |
| `dt.smartscape.aws_lambda_alias` | string | resource stable Smartscape ID referencing an AWS Lambda Alias. Tags: `smartscape-id` | `AWS_LAMBDA_ALIAS-BBCC334455667799` |
| `dt.smartscape.aws_lambda_code_signing_config` | string | resource stable Smartscape ID referencing a Lambda Code Signing Config. Tags: `smartscape-id` | `AWS_LAMBDA_CODE_SIGNING_CONFIG-CCDDEE1122334455` |
| `dt.smartscape.aws_lambda_function` | string | resource stable Smartscape ID referencing an AWS Lambda Function. Tags: `smartscape-id` | `AWS_LAMBDA_FUNCTION-DDEEFF2233445566` |
| `dt.smartscape.aws_rds_db_cluster` | string | resource stable Smartscape ID referencing an AWS RDS DB Cluster. Tags: `smartscape-id` | `AWS_RDS_DB_CLUSTER-EEFF334455667788` |
| `dt.smartscape.aws_rds_db_cluster_snapshot` | string | resource stable Smartscape ID referencing an RDS DB Cluster Snapshot. Tags: `smartscape-id` | `AWS_RDS_DB_CLUSTER_SNAPSHOT-FF00112233445566` |
| `dt.smartscape.aws_rds_db_instance` | string | resource stable Smartscape ID referencing an RDS DB Instance. Tags: `smartscape-id` | `AWS_RDS_DB_INSTANCE-0011FF2233445566` |
| `dt.smartscape.aws_rds_db_security_group` | string | resource stable Smartscape ID referencing an RDS Security Group. Tags: `smartscape-id` | `AWS_RDS_DB_SECURITY_GROUP-1122FF3344556677` |
| `dt.smartscape.aws_rds_db_snapshot` | string | resource stable Smartscape ID referencing an RDS DB Snapshot. Tags: `smartscape-id` | `AWS_RDS_DB_SNAPSHOT-2233FF4455667788` |
| `dt.smartscape.aws_rds_db_subnet_group` | string | resource stable Smartscape ID referencing an RDS Subnet Group. Tags: `smartscape-id` | `AWS_RDS_DB_SUBNET_GROUP-3344FF5566778899` |
| `dt.smartscape.aws_region` | string | resource stable Smartscape ID referencing an AWS Region entity. Tags: `smartscape-id` | `AWS_REGION-4455FF66778899AA` |
| `dt.smartscape.azure_availability_zone` | string | resource stable Smartscape ID referencing an Azure Availability Zone. Tags: `smartscape-id` | `AZURE_AVAILABILITY_ZONE-5566AA77889900BB` |
| `dt.smartscape.azure_location` | string | resource stable Smartscape ID referencing an Azure location/region. Tags: `smartscape-id` | `AZURE_LOCATION-6677BB889900AACC` |
| `dt.smartscape.azure_microsoft_compute_virtualmachines` | string | resource stable Smartscape ID referencing an Azure Virtual Machine resource. Tags: `smartscape-id` | `AZURE_MICROSOFT_COMPUTE_VIRTUALMACHINES-7788CC9900AABBCC` |
| `dt.smartscape.azure_microsoft_web_sites_functionapp` | string | resource stable Smartscape ID referencing an Azure Function App. Tags: `smartscape-id` | `AZURE_MICROSOFT_WEB_SITES_FUNCTIONAPP-8899DD00BBCCDDEE` |
| `dt.smartscape.azure_subscription` | string | resource stable Smartscape ID referencing an Azure Subscription. Tags: `smartscape-id` | `AZURE_SUBSCRIPTION-99AABB00CCDDEEFF` |
| `dt.smartscape.bizflow` | string | resource stable Smartscape ID referencing a Business Analytics / BizFlow entity. Tags: `smartscape-id` | `BIZFLOW-AABBCCDDEEFF0011` |
| `dt.smartscape.container` | string | resource stable Smartscape ID referencing a Container entity. Tags: `smartscape-id` | `CONTAINER-0F1E2D3C4B5A6978` |
| `dt.smartscape.frontend` | string | resource experimental The frontend Smartscape ID. Tags: `smartscape-id` | `FRONTEND-E0D8F94D9065F24F` |
| `dt.smartscape.host` | string | resource stable Smartscape ID referencing a Host entity. Tags: `smartscape-id` | `HOST-A1B2C3D4E5F67890` |
| `dt.smartscape.k8s_cluster` | string | resource stable A Smartscape ID that can be used to query Kubernetes cluster entities from the Smartscape storage. Tags: `smartscape-id` | `K8S_CLUSTER-0123456789ABCDEF` |
| `dt.smartscape.k8s_configmap` | string | resource stable Smartscape ID referencing a Kubernetes ConfigMap. Tags: `smartscape-id` | `K8S_CONFIGMAP-AABBCCDDEEFF0011` |
| `dt.smartscape.k8s_cronjob` | string | resource stable Smartscape ID referencing a Kubernetes CronJob. Tags: `smartscape-id` | `K8S_CRONJOB-2233445566778899` |
| `dt.smartscape.k8s_customresourcedefinition` | string | resource stable Smartscape ID referencing a Kubernetes CustomResourceDefinition. Tags: `smartscape-id` | `K8S_CUSTOMRESOURCEDEF-33445566778899AA` |
| `dt.smartscape.k8s_daemonset` | string | resource stable Smartscape ID referencing a Kubernetes DaemonSet. Tags: `smartscape-id` | `K8S_DAEMONSET-BBCCDDEEFF001122` |
| `dt.smartscape.k8s_deployment` | string | resource stable Smartscape ID referencing a Kubernetes Deployment. Tags: `smartscape-id` | `K8S_DEPLOYMENT-445566778899AABB` |
| `dt.smartscape.k8s_deploymentconfig` | string | resource stable Smartscape ID referencing an OpenShift DeploymentConfig. Tags: `smartscape-id` | `K8S_DEPLOYMENTCONFIG-5566778899AABBCC` |
| `dt.smartscape.k8s_dynakube` | string | resource stable Smartscape ID referencing a Dynatrace DynaKube Kubernetes resource. Tags: `smartscape-id` | `K8S_DYNAKUBE-66778899AABBCCDD` |
| `dt.smartscape.k8s_edgeconnect` | string | resource stable Smartscape ID referencing an EdgeConnect Kubernetes resource. Tags: `smartscape-id` | `K8S_EDGECONNECT-778899AABBCCDDEE` |
| `dt.smartscape.k8s_ingress` | string | resource stable Smartscape ID referencing a Kubernetes Ingress resource. Tags: `smartscape-id` | `K8S_INGRESS-8899AABBCCDDEEFF` |
| `dt.smartscape.k8s_job` | string | resource stable Smartscape ID referencing a Kubernetes Job. Tags: `smartscape-id` | `K8S_JOB-99AABBCCDDEEFF00` |
| `dt.smartscape.k8s_namespace` | string | resource stable Smartscape ID referencing a Kubernetes Namespace. Tags: `smartscape-id` | `K8S_NAMESPACE-AABBCCDDEEFF0011` |
| `dt.smartscape.k8s_networkpolicy` | string | resource stable Smartscape ID referencing a Kubernetes NetworkPolicy. Tags: `smartscape-id` | `K8S_NETWORKPOLICY-BBCCDDEEFF112233` |
| `dt.smartscape.k8s_node` | string | resource stable Smartscape ID referencing a Kubernetes Node. Tags: `smartscape-id` | `K8S_NODE-CCDDEEFF11223344` |
| `dt.smartscape.k8s_persistentvolume` | string | resource stable Smartscape ID referencing a Kubernetes PersistentVolume. Tags: `smartscape-id` | `K8S_PERSISTENTVOLUME-DDEEFF1122334455` |
| `dt.smartscape.k8s_persistentvolumeclaim` | string | resource stable Smartscape ID referencing a PersistentVolumeClaim. Tags: `smartscape-id` | `K8S_PERSISTENTVOLUMECLAIM-EEFF112233445566` |
| `dt.smartscape.k8s_pod` | string | resource stable Smartscape ID referencing a Kubernetes Pod. Tags: `smartscape-id` | `K8S_POD-FF11223344556677` |
| `dt.smartscape.k8s_replicaset` | string | resource stable Smartscape ID referencing a Kubernetes ReplicaSet. Tags: `smartscape-id` | `K8S_REPLICASET-0011AABBCCDD2233` |
| `dt.smartscape.k8s_replicationcontroller` | string | resource stable Smartscape ID referencing a Kubernetes ReplicationController. Tags: `smartscape-id` | `K8S_REPLICATIONCONTROLLER-1122BBCCDDEEFF33` |
| `dt.smartscape.k8s_secret` | string | resource stable Smartscape ID referencing a Kubernetes Secret. Tags: `smartscape-id` | `K8S_SECRET-2233CCDDEEFF4455` |
| `dt.smartscape.k8s_service` | string | resource stable Smartscape ID referencing a Kubernetes Service. Tags: `smartscape-id` | `K8S_SERVICE-3344DDEEFF556677` |
| `dt.smartscape.k8s_statefulset` | string | resource stable Smartscape ID referencing a Kubernetes StatefulSet. Tags: `smartscape-id` | `K8S_STATEFULSET-4455EEFF66778899` |
| `dt.smartscape.process` | string | resource stable Smartscape ID referencing a Process entity. Tags: `smartscape-id` | `PROCESS-1234567890ABCDEF` |
| `dt.smartscape.service` | string | resource stable Smartscape ID referencing a Service entity. Tags: `smartscape-id` | `SERVICE-0011223344556677` |

## Support

Additional information about the attributes of a data point.

### Support fields for user event

## Dynatrace Synthetic

The dt.synthetic namespace contains Dynatrace synthetic specific fields.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.synthetic.batch.id` | long | experimental The identifier of the batch (defined for on-demand executions only). |  |
| `dt.synthetic.excluded_from_step` | boolean | experimental Information whether the event is not included in step/monitor level aggregation (in metrics and counters). |  |
| `dt.synthetic.location.missing_capabilities` | array | experimental Names of missing Synthetic location capabilities. | `BROWSER`; `ICMP` |
| `dt.synthetic.monitor.id` | string | experimental The identifier of the monitor. | `HTTP_CHECK-6349B98E1CD87352` |
| `dt.synthetic.monitored_entity_ids` | array | experimental IDs of monitored entities. | `APPLICATION-EA7C4B59F27D43EB` |
| `dt.synthetic.request.targets` | array | experimental Request target addresses with DNS record type or TCP port number. | `127.0.0.1:22` |
| `dt.synthetic.step.id` | string | experimental The identifier of the monitor step. | `HTTP_CHECK_STEP-5349B98E1CD87352` |
| `dt.synthetic.violated_entity_ids` | array | experimental IDs of synthetic monitor or steps. | `HTTP_CHECK-9349B98E1CD87352`; `HTTP_CHECK_STEP-6349B98E1CD87352` |

## Dynatrace Synthetic

The dt.synthetic\_engine namespace contains Dynatrace synthetic engine specific fields.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.synthetic_engine.processing.end_timestamp` | timestamp | experimental The end timestamp of the step/monitor execution as reported by executor. | `1629891693487` |
| `dt.synthetic_engine.processing.start_timestamp` | timestamp | experimental The start timestamp of the step/monitor execution as reported by executor. | `1529891693487` |

## Dynatrace system fields

The namespace `dt.system` is reserved for Grail. These fields cannot be ingested but instead will be set by Grail directly. Every record that is fetched from Grail provides these fields, but by default they are hidden. You can display them by using the `fieldsAdd` command.

Example query:

```
// display the bucket for each log record



fetch logs



| fieldsAdd dt.system.bucket
```

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.system.bucket` | string | stable The Grail bucket that the record is stored in. | `default_logs`; `default_spans`; `default_bizevents` |
| `dt.system.environment` | string | stable The Dynatrace environment that the record belongs to. | `wkf10640` |
| `dt.system.monitoring_source` | string | stable Identifies the license under which the source is running. | `fullstack_host`; `infrastructure` |
| `dt.system.sampling_ratio` | long | stable The selected sampling ratio. | `1` |
| `dt.system.segment_id` | string | stable The segment that the record belongs to. | `5d97c09e-7337-443e-bab5-2f0474804687` |
| `dt.system.storage_interval` | string | stable Identifies the timeframe represented by individual data structures stored under a metric key. | `1 min` |
| `dt.system.table` | string | stable The table that the record belongs to. | `logs`; `bizevents` |

`dt.system.monitoring_source` MUST be one of the following:

| Value | Description |
| --- | --- |
| `discovery` | The source is running under the discovery license. |
| `fullstack_container` | The source is running under the full-stack container license. |
| `fullstack_host` | The source is running under the full-stack host license. |
| `infrastructure` | The source is running under the infrastructure license. |
| `mainframe` | The source is running under the mainframe license. |

`dt.system.storage_interval` MUST be one of the following:

| Value | Description |
| --- | --- |
| `1 min` | The timeframe represented by individual measurements of a metrics record in storage. |

## Dynatrace specific tracing fields

Fields defined in this namespace are used by Dynatrace to describe different aspects of the context propagation between spans.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.tracing.custom_link.id` | uid | experimental The custom link ID to identify spans calling each other. The ID is derived from the custom link bytes. | `736bd2684696c4a8` |
| `dt.tracing.custom_link.original_bytes` | binary | experimental The original binary data of the custom link. | `ycXlxUBAQEDee9lm8pBcA8nF5cVAQEBA3nvZZvKQXAPee9lm8s4SAQ==` |
| `dt.tracing.custom_link.transformed_bytes` | binary | experimental The transformed binary data of the custom link. Only available if a mapping was applied. | `ycXlxUBAQEDee9lm8pBcA8nF5cVAQEBA3nvZZvKQXAPee9lm8s4SAQ==` |
| `dt.tracing.custom_link.type` | string | experimental The type of the custom link defines if a mapping of the `dt.tracing.custom_link.original_bytes` to the `dt.tracing.custom_link.transformed_bytes` was applied. | `generic` |
| `dt.tracing.foreign_link.bytes` | binary | experimental An incoming foreign link (cross-environment or cross-product). | `00000004000000010000000200000003000000040000002300000001` |
| `dt.tracing.foreign_link.text` | string | experimental An incoming foreign link (cross-environment or cross-product). | `FW4;129;12;-2023406815;4539717;0;17;66;c511;2h02;3h12345678;4h676767`; `FW1;129;4711;59959450;-1859959450;3;17;0` |
| `dt.tracing.link.direction` | string | experimental The direction of the span link to define the correct order between spans. | `outgoing` |
| `dt.tracing.link.id` | uid | experimental Unique identifier for a Dynatrace link. |  |
| `dt.tracing.link.is_sync` | boolean | experimental `true` indicates that the caller waits on the response. Only available on span links with `dt.tracing.link.direction` set to `outgoing`. |  |
| `dt.tracing.response.headers` | record | experimental A collection of key-value pairs containing received response headers related to tracing from an outgoing call. There may be multiple values for each header. Used for cross-environment linking. | `{'traceresponse': ['00-7b9e3e4068167838398f50017bfad358-d4ffc7e33530967a-01'], 'x-dt-tracestate': ['9651e1a8-19506b7c@dt']}` |

`dt.tracing.custom_link.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `generic` | The `dt.tracing.custom_link.original_bytes` have no special meaning. |
| `ibm_mq` | The `dt.tracing.custom_link.original_bytes` are an IBM MQ custom link. |
| `ibm_mq_ignore_qname` | The `dt.tracing.custom_link.original_bytes` are an IBM MQ custom link, but the qname part should be ignored in mapping. |

`dt.tracing.link.direction` MUST be one of the following:

| Value | Description |
| --- | --- |
| `incoming` | Indicates that the link represents an incoming call (the child in a parent-child relationship). |
| `outgoing` | Indicates that the link represents an outgoing call (the parent in a parent-child relationship). |

## Elasticsearch

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `elasticsearch.cluster.name` | string | resource experimental |  |
| `elasticsearch.node.name` | string | resource experimental |  |

## Endpoint

Endpoints define the public interface of services.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `endpoint.name` | string | stable The endpoint name is derived from endpoint detection rules and uniquely identifies one endpoint of a particular service. Endpoint names are usually technology-specific and should be defined by attributes with low cardinality, like `http.route` or `rpc.method`. Endpoints are exclusively detected on request root spans. | `GET /`; `PUT /users/:userID?`; `GET /productpage`; `Reviews.GetReviews` |

## Equinox

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `equinox.config.path` | string | resource experimental |  |

## Error

The error namespace contains general information on errors.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `error.code` | long | experimental The code of the error. Set for iOS (NSError and Swift Error) and custom errors for C-based languages. | `-1`; `3072` |
| `error.csp_violation_count` | long | experimental The number of CSP rule violations. | `1` |
| `error.dropped_exception_count` | long | experimental The number of exceptions that are observed, but which are not captured due to error capture limits. | `1` |
| `error.exception_count` | long | experimental The total number of exceptions that are observed, including exceptions that are not captured. | `1` |
| `error.has_custom_name` | boolean | experimental If set to `true`, the `error.name` was reported via the Dynatrace API. | `true` |
| `error.http_4xx_count` | long | experimental The number of HTTP request errors with an `http.response.status_code` of 400-499. | `1` |
| `error.http_5xx_count` | long | experimental The number of HTTP request errors with an `http.response.status_code` of 500-599. | `1` |
| `error.http_other_count` | long | experimental The number of HTTP request errors with an `http.response.status_code` of 0-99 or 600+ (undefined errors). | `1` |
| `error.id` | uid | experimental A unique identifier for error grouping. The `error.id` is a 16-byte ID and hex-encoded if shown as a string. | `357bf70f3c617cb34584b31bd4616af8` |
| `error.is_fatal` | boolean | experimental If set to `true`, the error resulted in a fatal exit (for example, an unhandled exception). | `true` |
| `error.name` | string | experimental A human-readable version of `error.id`. | `500: foo.bar/path/file`; `path/file:1:5` |
| `error.reason` | string | experimental The error reason. RUM JavaScript reports a pre-defined set of values. OneAgent for iOS reports `nserror.domain`. | `no network` |
| `error.source` | string | experimental The error source. | `fetch`; `console` |
| `error.type` | string | experimental The main error type. This information is determined by Dynatrace RUM error grouping. | `request` |

`error.reason` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `abort` | The request was aborted by the user. |
| `csp` | The request failed due to a Content Security Policy (CSP) violation. |
| `no_network` | The request failed because of no connectivity. |
| `timeout` | The request timed out. |

`error.source` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `console` | console |
| `document_request` | document\_request |
| `exception` | exception |
| `fetch` | fetch |
| `promise_rejection` | promise\_rejection |
| `xhr` | xhr |

`error.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `anr` | Application Not Responding (ANR) |
| `crash` | Crash |
| `csp` | Content Security Policy (CSP) violation |
| `exception` | Exception |
| `reported` | Custom reported error |
| `request` | Failed request |

## ESB

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `esb.application.name` | string | resource experimental The name of the application that holds the workflows of the business logic. | `myBusinessApp`; `YourServiceApp`; `any_work` |
| `esb.library.name` | string | resource experimental The name of the library that hosts commonly used workflows to be reused in applications. | `myWebServicesLib`; `YourMessagingLibrary`; `any_tools` |
| `esb.vendor` | string | resource experimental The name of the vendor of the ESB technology of the current workflow. | `ibm`; `tibco` |
| `esb.workflow.name` | string | resource experimental The name of the workflow (the message flow for the IBM ESB). | `myMessageFlow`; `YourBusinessWorkflow`; `any_flow` |

## Event

The event namespace contains common identification, categorization and context on events in Dynatrace.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `event.category` | string | stable Standard categorization based on the significance of an event (similar to the severity level in the previous Dynatrace). | `Availability` |
| `event.description` | string | stable Human-readable description of an event. | `The current response time (11 s) exceeds the auto-detected baseline (767 ms) by 1,336 %` |
| `event.end` | string | stable The event end timestamp in UTC (given in Grail preferred Linux timestamp nano precision format). | `16481073970000` |
| `event.group_label` | string | experimental Group label of an event. | `Availability` |
| `event.id` | string | stable Unique identifier string of an event; is stable across multiple refreshes and updates. | `5547782627070661074_1647601320000` |
| `event.kind` | string | stable Gives high-level information about what kind of information the event contains without being specific about the contents of the event. It helps to determine the record type of a raw event. Tags: `permission` | `INFRASTRUCTURE_EVENT`; `DAVIS_EVENT`; `BIZ_EVENT`; `RUM_EVENT`; `AUDIT_EVENT`; `BILLING_USAGE_EVENT` |
| `event.name` | string | stable The human readable display name of an event type. | `Process crashed`; `CPU Saturation` |
| `event.original_content` | string | experimental The original raw data of the event as received from the source. | `{"severity_id": 3,"state_id": 1,"time": "2024-06-26T07:15:06.139000Z","state": "New","type_uid": 200101}` |
| `event.outcome` | string | stable Denotes whether the event represents a success or a failure from the perspective of the entity that produced the event (for example an HTTP response code). | `200`; `success`; `failure` |
| `event.parent_id` | string | experimental Unique identifier string of a parent event to link parent and child events. | `5547782627070661074_1647601319999` |
| `event.provider` | string | stable Source of the event, for example, the name of the component or system that generated the event. Tags: `permission` | `OneAgent`; `K8S`; `Davis`; `VMWare`; `GCP`; `AWS`; `LIMA_USAGE_STREAM` |
| `event.reason` | string | stable Describes why a certain event.outcome was set. Typically, this is some form of error description in the case of a failure. | `user is missing permission "logs.read"` |
| `event.start` | string | stable The event start timestamp in UTC (given in Grail preferred Linux timestamp nano precision format). | `16481073970000` |
| `event.status` | string | stable Status of an event as being either Active or Closed. | `Active` |
| `event.status_transition` | string | experimental An enum that shows the transition of the above event state. | `Recovered` |
| `event.type` | string | stable The unique type identifier of a given event. Tags: `permission` | `ESXI_HOST_MEMORY_SATURATION`; `PROCESS_RESTART`; `CPU_SATURATION`; `MEMORY_SATURATION`; `Automation Workflow`; `AppEngine Functions - Small` |
| `event.version` | string | stable Describes the version of the event. | `1.0.0` |

### Values

Values are either in title-case or screaming snake case.

`event.category` SHOULD be one of the following:

| Value | Description |
| --- | --- |
| `Availability` | availability |
| `Error` | error |
| `Slowdown` | slowdown |
| `Resource contention` | resource\_contention |
| `Warning` | warning |
| `Info` | info |
| `Vulnerability management` | vulnerability\_management |

`event.status` SHOULD be one of the following:

| Value | Description |
| --- | --- |
| `Active` | active |
| `Closed` | closed |

`event.status_transition` SHOULD be one of the following:

| Value | Description |
| --- | --- |
| `Created` | created |
| `Updated` | updated |
| `Refreshed` | refreshed |
| `Resolved` | resolved |
| `Recovered` | recovered |
| `Closed` | closed |
| `Timed out` | timed out |
| `Reopened` | reopened |

## Exception

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `exception.caused_by_id` | uid | stable The `exception.id` of the exception the current exception was caused by. |  |
| `exception.column_number` | long | experimental The column number where the exception happened. | `12304` |
| `exception.escaped` | boolean | stable `true` indicates that the exception was recorded at a point where it is known that the exception escaped the scope of the span. |  |
| `exception.file.domain` | string | experimental The URI domain component. This is extracted from `exception.file.full`. | `www.foo.bar` |
| `exception.file.full` | string | experimental The full file location when the exception happened. This is either an absolute URL or a filename. | `https://www.foo.bar/path/main.js`; `main.js` |
| `exception.file.path` | string | experimental The URI path component. This is extracted from `exception.file.full`. | `/path/main.js` |
| `exception.id` | uid | stable The identifier of an exception. It should be unique within a list of exceptions of a span. The identifier is used to reference the exception. |  |
| `exception.is_caused_by_root` | boolean | stable Is set to `true` if the exception is the first exception caused by the chain. |  |
| `exception.line_number` | long | experimental The line number where the exception happened. | `1401` |
| `exception.line_offsets` | string | experimental The line offset mapping for source lines shifted by instrumentation. | `{"generationTime":"2025-12-08 13:20:55","instrumentorVersion":"8.329","mappings":[{"ContentView.swift":{"1":3,"18":8,"25":13,"26":18,"27":23}},{"InstrDemoApp.swift":{"1":3,"13":4}}],"project":"Testproject.xcproject"}` |
| `exception.message` | string | stable A message that describes the exception. | `Division by zero` |
| `exception.stack_trace` | string | experimental The stack trace of the exception. The format depends on the technology and source. While OneAgent formats stack traces to unify them across technologies, stack traces from an OpenTelemetry source are in the format they were sent to Dynatrace. | `@https://www.foo.bar/path/main.js:59:26 e@https://www.foo.bar/path/lib/1.1/lib.js:2:30315` |
| `exception.type` | string | stable The type of the exception, for example, its fully-qualified class name. | `java.net.ConnectException`; `OSError` |

## Function as a Service (FaaS)

Fields that can be expected from serverless functions or Function as a Service (FaaS) on various cloud platforms.

### Fields

#### Resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `faas.max_memory` | long | resource experimental The amount of memory available to the serverless function in Bytes. |  |
| `faas.name` | string | resource experimental The name of the single function that this runtime instance executes. [1](#fn-8-1-def) | `my-function`; `myazurefunctionapp/some-function-name`; `test_function` |
| `faas.version` | string | resource experimental The immutable version of the function being executed. [2](#fn-8-2-def) | `14`; `254` |

1

This is the name of the function as configured/deployed on the FaaS platform and is usually different from the name of the callback
function (which may be stored in the `code.namespace`/`code.function` span attributes).

2

Value of the field depends on a cloud provider. This field is not set for Azure.

#### Span attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `faas.coldstart` | boolean | experimental A boolean that is true if the serverless function is executed for the first time (aka cold-start). |  |
| `faas.document.collection` | string | experimental The table/collection name on which the operation above was executed. [1](#fn-9-1-def) | `my-coll-name` |
| `faas.document.name` | string | experimental The identifier for the specific item that changed after executing the operation above. [2](#fn-9-2-def) | `my-file.jpg`; `63eeb6e7d418cd98afb1c1d7` |
| `faas.document.operation` | string | experimental Relevant only for "datasource" trigger. The operation type which triggered the function invocation. | `delete` |
| `faas.document.time` | string | experimental The UTC ISO-8601 timestamp of the operation above. [3](#fn-9-3-def) | `2020-03-08T00:30:12.456Z` |
| `faas.event.__key__` | string | stable Faas event attribute, the `__key__` attribute in a Faas event represents the precise attribute name as received in the event. For example, it might be "faas.event.StackId" for the "StackId" attribute in an AWS CloudFormation event or "faas.event.IdentityPoolId" for the "IdentityPoolId" attribute in an AWS Cognito event. The value of this attribute is identical to the value received in the event. | `arn:aws:cloudformation:us-west-2:123456789012:stack/MyStack/1a2b3c4d-5678-90ab-cdef-EXAMPLE11111`; `eu-west-1:12345678-1234-1234-1234-123456789012` |
| `faas.event_name` | string | experimental The API action that triggered the faas event. [4](#fn-9-4-def) | `ObjectCreated:Put (aws:s3)`; `INSERT (aws:dynamodb)` |
| `faas.event_source` | string | experimental The cloud service that originated the event. | `aws:cloudwatch`; `aws:cloudformation` |
| `faas.invoked_name` | string | experimental The name of the invoked function. | `my-function` |
| `faas.invoked_provider` | string | experimental The cloud provider of the invoked function. Will be equal to the invoked function's `cloud.provider` resource attribute. | `alibaba_cloud` |
| `faas.invoked_region` | string | experimental The cloud region of the invoked function. [5](#fn-9-5-def) | `eu-central-1` |
| `faas.trigger` | string | experimental Type of the trigger which caused this function invocation. | `datasource` |

1

Relevant only for `faas.trigger=datasource` trigger

2

Relevant only for `faas.trigger=datasource` trigger

3

Relevant only for `faas.trigger=datasource` trigger

4

The value of this attribute is specific to the service that generated the event.

5

Will be equal to the invoked function's `cloud.region` resource attribute.

`faas.document.operation` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `delete` | delete |
| `edit` | edit |
| `insert` | insert |

`faas.invoked_provider` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `alibaba_cloud` | Alibaba Cloud |
| `aws` | Amazon Web Services |
| `azure` | Microsoft Azure |
| `gcp` | Google Cloud Platform |
| `tencent_cloud` | Tencent Cloud |

`faas.trigger` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `datasource` | A response to some data source operation such as a database or filesystem read/write. |
| `http` | To provide an answer to an inbound HTTP request |
| `other` | If none of the others apply |
| `pubsub` | A function is set to be executed when messages are sent to a messaging system. |
| `timer` | A function is scheduled to be executed regularly. |

## Failure Detection

Fields that can be expected for a failure detection on a Dynatrace span.
For more details and how failure detection is embedded in a span, see Dynatrace Span model.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.failure_detection.general_parameters_id` | uid | experimental The `id` of the failure detection general parameters (failure detection v1) that were applied to that span (uid128). | `4d76194c11a9426197a9062548f9e66f` |
| `dt.failure_detection.global_parameters_id` | uid | experimental The `id` of the global failure detection parameters (failure detection v1) that were applied to that span (uid128).  This is always used in conjunction with the `dt.failure_detection.global_rule_id`. | `4d76194c11a9426197a9062548f9e66c` |
| `dt.failure_detection.global_rule_id` | uid | experimental The `id` of the global failure detection rule (failure detection v1) that was applied to that span (uid128).  This is always used in conjunction with the `dt.failure_detection.global_parameters_id`. | `4d76194c11a9426197a9062548f9e66b` |
| `dt.failure_detection.http_parameters_id` | uid | experimental The `id` of the failure detection HTTP parameters (failure detection v1) that were applied to that span (uid128). | `4d76194c11a9426197a9062548f9e66a` |
| `dt.failure_detection.results` | record[] | experimental A collection of individual failure detection reasons and verdicts for each applied matching rule. If no entries exist, no rules matched, and the attribute does not exist. |  |
| `dt.failure_detection.ruleset_id` | uid | experimental The `id` of the failure detection rule set (failure detection v2) that was applied to that span (uid128). | `4d76194c11a9426197a9062548f9e66e` |
| `dt.failure_detection.verdict` | string | experimental The final failure detection verdict based on the results in `dt.failure_detection.results`. | `failure` |

`dt.failure_detection.verdict` MUST be one of the following:

| Value | Description |
| --- | --- |
| `failure` | There is at least one result with verdict `failure` and no result with verdict `success`. |
| `success` | There is at least one result with verdict `success` or no result at all. |

## Feature Flag

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `feature_flag.context.id` | string | experimental The unique identifier for the flag evaluation context. For example, the targeting key. | `5157782b-2203-4c80-a857-dbbd5e7761db` |
| `feature_flag.key` | string | experimental The unique identifier of the feature flag. | `logo-color` |
| `feature_flag.provider.name` | string | experimental The name of the service provider that performs the flag evaluation. | `Flag Manager` |
| `feature_flag.result.reason` | string | experimental The reason code, which shows how a feature flag value was determined. | `static`; `targeting_match`; `error`; `default` |
| `feature_flag.result.variant` | string | experimental A semantic identifier for an evaluated flag value. [1](#fn-10-1-def) | `red`; `true`; `on` |
| `feature_flag.set.id` | string | experimental The identifier of the [flag setï»¿](https://openfeature.dev/specification/glossary/#flag-set) to that the feature flag belongs. | `proj-1`; `ab98sgs`; `service1/dev` |
| `feature_flag.version` | string | experimental The version of the ruleset used during the evaluation. This can be any stable value that uniquely identifies the ruleset. | `1`; `01ABCDEF` |

1

A semantic identifier, commonly referred to as a variant, provides a means
for referring to a value without including the value itself. This can
provide additional context for understanding the meaning behind a value.
For example, the variant `red` maybe be used for the value `#c05543`.

`feature_flag.result.reason` MUST be one of the following:

| Value | Description |
| --- | --- |
| `cached` | The resolved value was retrieved from cache. |
| `default` | The resolved value fell back to a pre-configured value (no dynamic evaluation occurred or dynamic evaluation yielded no result). |
| `disabled` | The resolved value was the result of the flag being disabled in the management system. |
| `error` | The resolved value was the result of an error. |
| `split` | The resolved value was the result of pseudorandom assignment. |
| `stale` | The resolved value is non-authoritative or possibly out of date. |
| `static` | The resolved value is static (no dynamic evaluation). |
| `targeting_match` | The resolved value was the result of a dynamic evaluation, such as a rule or specific user-targeting. |
| `unknown` | The reason for the resolved value could not be determined. |

## Frontend

The frontend namespace contains information on the monitored frontend.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `frontend.name` | string | stable The frontend name determined at ingest. Tags: `permission` | `my_frontend` |

## Google Cloud Platform

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `gcp.app_engine.instance` | string | resource experimental |  |
| `gcp.app_engine.service` | string | resource experimental |  |
| `gcp.cloud_run.service` | string | resource experimental |  |
| `gcp.instance.id` | string | resource experimental The unique, numeric identifier of the Google Cloud resource instance (e.g., GCE VM or Cloud SQL), which remains immutable throughout the resource's lifecycle. | `6639848141313102286` |
| `gcp.instance.name` | string | resource deprecated The name to display for the instance in the Cloud Console. | `single-vm-test` |
| `gcp.location` | string | resource stable Region or zone where GCP resource instance is running. | `europe-west3-c` |
| `gcp.organization.id` | string | resource experimental Unique, immutable identifier assigned to an organization resource. | `123456789012` |
| `gcp.organization.name` | string | resource experimental Name assigned to the GCP organization. | `dynatrace.com` |
| `gcp.project.id` | string | resource stable Identifier of the GCP project associated with this resource. Tags: `permission` `primary-field` | `dynatrace-gcp-extension` |
| `gcp.region` | string | resource stable A region is a specific geographical location where you can host your resources. Tags: `primary-field` | `europe-west3` |
| `gcp.resource.name` | string | resource stable The globally unique resource name in Google Cloud Platform convention. | `//cloudfunctions.googleapis.com/projects/gcp-example-project/locations/us-central1/functions/examplefunction` |
| `gcp.resource.type` | string | resource stable The name of a monitored resource type available in Google Cloud Monitoring and Logging. | `cloudsql_database` |
| `gcp.user_labels.__label__` | string | resource experimental Contains the value for the user labels with the label key named `__label__` defined in the label enrichment configuration. | `dt_owner_mail` |
| `gcp.zone` | string | resource stable A zone is a subset of a region. Each region has three or more zones. | `europe-west3-c` |

## Generative AI

### Fields

#### Span attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `gen_ai.agent.name` | string | experimental Human-readable name of the GenAI agent provided by the application. | `Math Tutor`; `Fiction Writer` |
| `gen_ai.embeddings.dimension.count` | long | experimental The number of dimensions the resulting output embeddings should have. | `512`; `1024` |
| `gen_ai.guardrail.id` | string | experimental Identifier of the guardrail that has been activated for the request. | `sensitive_data_guardrail` |
| `gen_ai.guardrail.input.latency` | long | experimental Processing time of prompt by guardrail in ms. | `123` |
| `gen_ai.guardrail.input.sensitive_information.patterns` | string[] | experimental Name of the patterns for sensitive information in prompt that triggered the Guardrail. | `['customer_identifier']` |
| `gen_ai.guardrail.input.sensitive_information.piis` | string[] | experimental Personal Identifiable Information categories in prompt that triggered the Guardrail. | `['ADDRESS', 'LICENSE_PLATE', 'DRIVER_ID']` |
| `gen_ai.guardrail.input.topic.names` | string[] | experimental Topics in prompt that triggered the Guardrail. | `['investment_advice', 'legal_advice', 'politics']` |
| `gen_ai.guardrail.input.words.lists` | string[] | experimental Word lists that triggered the guardrail for prompt. | `['custom-word-list']` |
| `gen_ai.guardrail.input.words.matches` | string[] | experimental Words in prompt that triggered the Guardrail. | `[]` |
| `gen_ai.guardrail.output.latency` | long | experimental Processing time of response by guardrail in ms. | `123` |
| `gen_ai.guardrail.output.sensitive_information.patterns` | string[] | experimental Name of the patterns for sensitive information in response that triggered the Guardrail. | `['customer_identifier']` |
| `gen_ai.guardrail.output.sensitive_information.piis` | string[] | experimental Personal Identifiable Information categories in response that triggered the Guardrail. | `['ADDRESS', 'LICENSE_PLATE', 'DRIVER_ID']` |
| `gen_ai.guardrail.output.topic.names` | string[] | experimental Topics in response that triggered the Guardrail. | `['investment_advice', 'legal_advice', 'politics']` |
| `gen_ai.guardrail.output.words.lists` | string[] | experimental Word lists that triggered the guardrail for response. | `['custom-word-list']` |
| `gen_ai.guardrail.output.words.matches` | string[] | experimental Words in response that triggered the Guardrail. | `[]` |
| `gen_ai.guardrail.version` | string | experimental Version of the guardrail that has been activated. | `DRAFT`; `5`; `12345678` |
| `gen_ai.operation.kind` | string | experimental AI framework operation being performed. | `workflow`; `task`; `agent`; `agent`; `tool`; `retrieval` |
| `gen_ai.operation.name` | string | experimental Name of operation being performed. | `chat`; `generate_content`; `text_completion` |
| `gen_ai.prompt_caching` | string | experimental Indicates how prompt cache has been used when handling the request. | `read`; `write` |
| `gen_ai.provider.name` | string | experimental Name of GenAI product being used. | `aws_bedrock`; `openai` |
| `gen_ai.request.encoding_formats` | string[] | experimental The encoding formats requested in an embeddings operation, if specified. | `['base64']`; `['float', 'binary']` |
| `gen_ai.request.frequency_penalty` | double | experimental Frequency penalty setting for GenAI request. | `0.4` |
| `gen_ai.request.max_tokens` | long | experimental Maximum number of tokens that the model can generate for a request. | `50` |
| `gen_ai.request.model` | string | experimental Model chosen to handle the request. | `amazon.nova-micro-v1:0`; `anthropic.claude-3-7-sonnet-20250219-v1:0` |
| `gen_ai.request.presence_penalty` | double | experimental Presence penalty setting for GenAI request. | `0.4` |
| `gen_ai.request.stop_sequences` | string[] | experimental List of sequences that will stop the model from generating further tokens. | `['forest', 'lived']` |
| `gen_ai.request.temperature` | double | experimental Temperature setting for GenAI request. | `0.8` |
| `gen_ai.request.top_k` | long | experimental Temperature setting for GenAI request. | `300` |
| `gen_ai.request.top_p` | double | experimental Temperature setting for GenAI request. | `0.6` |
| `gen_ai.response.finish_reasons` | string[] | experimental List of reasons why the model stopped generating tokens, corresponding to each generation received. | `['stop_sequence']`; `['stop_sequence', 'max_tokens']` |
| `gen_ai.response.id` | string | experimental Unique identifier of an LLM response. | `resp_0e7d0475962f0d2800691dd8cbf8108190b45198f77fa12d6e` |
| `gen_ai.response.model` | string | experimental Model that handled the request. | `amazon.nova-micro-v1:0`; `anthropic.claude-3-7-sonnet-20250219-v1:0` |
| `gen_ai.response.system_fingerprint` | string | experimental Identifier of system used to generate LLM response. | `fp_03e44fcc34` |
| `gen_ai.usage.input_tokens` | long | experimental Number of tokens sent to the model in the request. | `42` |
| `gen_ai.usage.output_tokens` | long | experimental Number of tokens generated by the model while handling the request. | `42` |
| `gen_ai.usage.prompt_caching.read_tokens` | long | experimental Number of tokens that has been read from cache. | `42` |
| `gen_ai.usage.prompt_caching.write_tokens` | long | experimental Number of tokens used to generate cache checkpoint. | `42` |

`gen_ai.operation.kind` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `agent` | Operation invoking an autonomous component that can make decisions or perform actions. |
| `retrieval` | Operation collecting documents for a RAG pipeline. |
| `task` | A specific operation or step within a workflow. |
| `tool` | Operation invoking a utility or function used within the application. |
| `workflow` | A high-level process or chain of operations. |

`gen_ai.operation.name` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `chat` | Operation of engaging in a conversational exchange with LLM. |
| `embeddings` | Operation of creating embeddings from user input. |
| `text_completion` | Operation of completing text based on user input by LLM. |

`gen_ai.prompt_caching` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `read` | Cache hit. Reading from cache. |
| `write` | Cache miss. Creating cache checkpoint. |

`gen_ai.provider.name` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `aws_bedrock` | Amazon Bedrock |
| `openai` | OpenAI |

## Geolocation

The geo namespace contains geo location information. This section only holds all currently agreed upon fields in the Dynatrace Semantic Dictionary. Aligned closely to the ECS, with some adaptions around field groupings

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `geo.city.name` | string | resource stable English name of the city. | `Montreal` |
| `geo.continent.name` | string | resource stable English name of the continent. | `North America` |
| `geo.country.iso_code` | string | resource experimental The two-letter country code. The format complies with ISO 3166-1 alpha-2. | `CA`; `GB` |
| `geo.country.name` | string | resource stable English name of the country. | `Canada` |
| `geo.location.latitude` | double | resource experimental The approximate latitude. The format complies with WGS 84. Tags: `sensitive-user-events` | `45.505918` |
| `geo.location.longitude` | double | resource experimental The approximate longitude. The format complies with WGS 84. Tags: `sensitive-user-events` | `-73.61483` |
| `geo.region.name` | string | resource stable English name of the region. | `Quebec` |

## Glassfish

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `glassfish.domain.name` | string | resource experimental The name of the domain this instance belongs to. |  |
| `glassfish.instance.name` | string | resource experimental The instance's name. |  |

## Go

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `go.linkage` | string | resource experimental |  |

## Host

Fields describing a host.

### Host naming

Dynatrace aims to use the best fitting name for the field `host.name`. See below, how Dynatrace determines the host name in an ordered by precedence fashion:

#### 1. Customized host name

Dynatrace supports customizing the `host.name` property. A custom set host name takes precedence over the auto detection mechanisms described further down.

* Place a configuration file containing the desired name in a specific directory as described in this [Documentation](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments#config-file "Learn how to change a monitored host name.")
* Alternatively, the `oneagentctl` tool can be used to set a custom host name. See [Documentation](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments#oneagentctl "Learn how to change a monitored host name.") for details.

#### 2. Kubernetes node name

If no customized name is set locally, the OneAgent attempts to determine if we're deployed by Dynatrace Operator in Kubernetes or OpenShift and sets `host.name` to the name of the Node.

#### 3. Cloud vendor metadata

If the Kubernetes isn't present, the OneAgent attempts to determine the `host.name` value by accessing cloud metadata where applicable.

* AWS EC2:

  + If access to EC2 tags was granted (see [AWS Documentationï»¿](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#allow-access-to-tags-in-IMDS)) and a tag with a key `name` (case insensitive) is found, the tag's value is used as the `host.name`.
* Azure VM:

  + The VM's `name` (case insensitive) instance metadata property is used. See [Microsoft Azure documentationï»¿](https://learn.microsoft.com/en-us/azure/virtual-machines/instance-metadata-service#instance-metadata)
* Google Compute Engine:

  + The VM's `hostname` instance metadata property is used. See [Google Cloud documentationï»¿](https://cloud.google.com/compute/docs/metadata/predefined-metadata-keys#instance-metadata).

#### 4a. Linux & AIX

* The result of the system call to the standard C library's `gethostname()` if it can be interpreted as a fully qualified domain name (FQDN) and doesn't contain "localhost".
* Otherwise, a system call to `getaddrinfo()` for port 80 is issued, again sanity checking whether the returned name is an FQDN and doesn't contain "localhost".
* If a correct hostname still hasn't been identified, but the system call to `gethostname()` was successful, and the returned string is not empty and doesn't contain "localhost", then it's used.
* Defaults to the string `EmptyHostName` if neither property can be resolved.

#### 4b. Windows

* On Windows, the system call `GetComputerNameExA` is used to determine a host's name. In particular, the resulting name is composed of `<hostname>.<domainname>` with the following details

  + `hostname` = ComputerNameDnsHostname retrieved by GetComputerNameEx
  + `domainname` = ComputerNameDnsDomain retrieved by GetComputerNameEx
* The result of the system call `GetComputerNameExA` is used when it can be interpreted as a fully qualified domain name (FQDN).
* Otherwise, the result of the system call `GetComputerNameExA` is used when it's not empty.
* Defaults to the string `EmptyHostName` if neither property can be resolved.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `host.fqdn` | string[] | resource experimental A list of FQDNs of this host. | `['ec2-43-213-176-3.compute-1.amazonaws.com', 'localhost.example.com']` |
| `host.ip` | ipAddress[] | resource experimental A list of IP adresses (IPv4 or IPv6) of this host. | `[194.232.104.141, 2a01:468:1000:9::140]` |
| `host.logical.cpu.cores` | long | resource experimental Logical CPU cores on the monitored host. | `8` |
| `host.logical.cpus` | long | resource experimental Logical CPUs on the monitored host. Applies to AIX LPARs. | `8` |
| `host.mac` | array | resource experimental A list of MAC adresses associated with this host. | `4C:03:4F:5B:E8:89`; `00:15:5D:2F:1C:2A` |
| `host.name` | string | resource experimental The host name as determined on the data source (for instance, OneAgent, extensions or OpenTelemetry). Important: This is not the name of the host entity, which can be modified based on naming rules. Tags: `permission` | `ip-10-178-54-32.ec2.internal` |
| `host.physical.memory` | long | resource experimental Physical memory of the monitored host, expressed in bytes. The value might be different than the total available memory, if features such as Active Memory Expansion are used. | `8141684736` |
| `host.simultaneous.multithreading` | long | resource experimental Number of threads for AIX Simultaneous Multithreading feature. | `4` |
| `host.virtual.cpus` | long | resource experimental Number of virtual CPUs for AIX LPAR. | `2` |

## HTTP

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `http.request.body.size` | long | stable The size of the request payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Lengthï»¿](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size. | `3495` |
| `http.request.header.__key__` | string | stable HTTP request headers, `__key__` being the lowercase HTTP header name, for example, "http.request.header.accept-encoding". The value is a string. If multiple headers have the same name or multiple header values, the values will be comma-separated into a single string. Tags: `sensitive-spans` | `https://www.foo.bar/`; `gzip, deflate, br`; `1.2.3.4, 1.2.3.5` |
| `http.request.id` | string | experimental String that uniquely identifies a request. | `SOX4xwn4XV6Q4rgb7XiVGOHms_BGlTAC4KyHmureZmBNrjGdRLiNIQ==`; `k6WGMNkEzR5BEM_SaF47gjtX9zBDO2m349OY2an0QPEaUum1ZOLrow==` |
| `http.request.method` | string | stable HTTP request method. | `GET`; `POST`; `HEAD` |
| `http.request.parameter.__key__` | string | stable HTTP request parameters, `__key__` for example, "http.request.parameter.username". The value is a string. If there are multiple parameters with the same name or multiple parameter values, the values will be a single, comma-separated string. | `admin`; `premium` |
| `http.request.size` | long | experimental The total size of the request in bytes. This value should be the total number of bytes sent over the wire, including the request line (HTTP/1.1), framing (HTTP/2 and HTTP/3), headers, and request body if any. | `114`; `702` |
| `http.response.body.size` | long | stable The size of the response payload body in bytes. This is the number of bytes transferred excluding headers and is often, but not always, present as the [Content-Lengthï»¿](https://www.rfc-editor.org/rfc/rfc9110.html#field.content-length) header. For requests using transport encoding, this should be the compressed size. | `3495` |
| `http.response.header.__key__` | string | stable HTTP response headers, `__key__` being the lowercase HTTP header name, for example, "http.response.header.content-type". The value is a string. If multiple headers have the same name or multiple header values, the values will be comma-separated into a single string. | `909`; `text/html; charset=utf-8`; `abc, def` |
| `http.response.range_end_value` | long | experimental When the response contains the HTTP Content-Range header, this field contains the range end value. | `499`; `1999` |
| `http.response.range_start_value` | long | experimental When the response contains the HTTP Content-Range header, this field contains the range start value. | `0`; `1000` |
| `http.response.reason_phrase` | string | experimental The HTTP reason phrase (HTTP1 only). | `Not found` |
| `http.response.size` | long | experimental The total size of the response in bytes. This value should be the total number of bytes sent over the wire, including the status line (HTTP/1.1), framing (HTTP/2 and HTTP/3), headers, and response body and trailers if any. | `251`; `608` |
| `http.response.status_code` | long | stable [HTTP response status codeï»¿](https://tools.ietf.org/html/rfc7231#section-6). | `200` |
| `http.response.time_to_first_byte` | double | experimental Time between the browser requesting a page and when it receives the first byte of information from the server. | `0.022`; `0.071` |
| `http.route` | string | stable The matched route (path template in the format used by the respective server framework). | `/users/:userID?`; `Home/Index/{id?}` |

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `http.server_name` | string | resource experimental The server name as configured by the webserver if available. If no such name exists, this is the local hostname and bound port. In Kubernetes, the base pod name is used. | `MyServer`; `localhost:8000` |

## Hybris

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `hybris.bin.dir` | string | resource experimental | `/opt/hybris-60/hybris/bin` |
| `hybris.config.dir` | string | resource experimental | `/opt/hybris-60/hybris/config` |
| `hybris.data.dir` | string | resource experimental | `/opt/hybris-60/hybris/data` |

### Reference

## IBM

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `ibm.ace.integration_node.name` | string | resource experimental The name of the integration node (broker) that manages one or more integration servers. | `myIntegrationNode`; `YourBroker`; `the_management_instance` |
| `ibm.ace.integration_server.name` | string | resource experimental The name of the broker-managed or standalone integration server (formerly known as execution group or dataflow engine). | `myIntegrationServer`; `YourExecutionGroup`; `dataflow_engine` |
| `ibm.cics.aor` | string | resource experimental |  |
| `ibm.cics.program` | string | resource experimental The name of the CICS program. | `EDUCHAN` |
| `ibm.cics.region` | string | resource experimental |  |
| `ibm.cics.tor` | string | resource experimental |  |
| `ibm.ctg.name` | string | resource experimental |  |
| `ibm.ims.connect` | string | resource experimental |  |
| `ibm.ims.control` | string | resource experimental |  |
| `ibm.ims.mpr` | string | resource experimental |  |
| `ibm.ims.soap_gw.name` | string | resource experimental |  |

## Iis

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `iis.app_pool.name` | string | resource experimental |  |
| `iis.role.name` | string | resource experimental |  |

## Java

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `java.jar.file` | string | resource experimental |  |
| `java.jar.path` | string | resource experimental |  |
| `java.main.class` | string | resource experimental |  |
| `java.main.module` | string | resource experimental |  |

## JBoss

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `jboss.home` | string | resource experimental The instance's home directory. |  |
| `jboss.mode` | string | resource experimental The instance's operating mode. | `org.jboss.as.standalone`; `org.jboss.as.server` |
| `jboss.server.name` | string | resource experimental The instance's server name. |  |

## JDBC

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `jdbc.connection.pool.name` | string | stable The name of the JDBC connection pool. | `jdbc/db2` |

## Journald

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `journald.unit` | string | experimental A unit is a systemd object that performs or controls a particular task or action; concerns unix-based systems | `cron.service`; `oneagent.service`; `kubepods.slice` |

## Kubernetes

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `k8s.cluster.name` | string | resource stable The user-defined name of the cluster in Dynatrace. Doesn't need to be unique or immutable. Tags: `permission` `primary-field` | `unguard-dev`; `acme-prod10` |
| `k8s.cluster.uid` | string | resource stable A pseudo-ID for the cluster, by default set to the UID of the kube-system namespace. | `1c7a24c7-ff51-46e0-bcc9-c52637ceec57` |
| `k8s.configmap.name` | string | resource experimental Name of the ConfigMap. | `my-configmap` |
| `k8s.container.name` | string | resource stable The name of the container from the pod specification; must be unique within a pod. Container runtime usually uses different globally unique name (`container.name`). | `redis` |
| `k8s.container.type` | string | resource experimental The type of the Kubernetes container. | `app`; `init`; `sidecar`; `ephemeral` |
| `k8s.cronjob.name` | string | resource experimental Name of the CronJob. | `my-cronjob` |
| `k8s.customresourcedefinition.name` | string | resource experimental Name of the CustomResourceDefinition. | `dynakubes.dynatrace.com` |
| `k8s.daemonset.name` | string | resource experimental Name of the DaemonSet. | `my-daemonset` |
| `k8s.deployment.name` | string | resource experimental Name of the Deployment. | `my-deployment` |
| `k8s.deploymentconfig.name` | string | resource experimental Name of the DeploymentConfig. | `my-deploymentconfig` |
| `k8s.dynakube.name` | string | resource experimental Name of the DynaKube. | `my-dynakube` |
| `k8s.edgeconnect.name` | string | resource experimental Name of the EdgeConnect. | `my-edgeconnect` |
| `k8s.ingress.name` | string | resource experimental Name of the Ingress. | `my-ingress` |
| `k8s.job.name` | string | resource experimental Name of the Job. | `my-job` |
| `k8s.namespace.name` | string | resource stable The name of the namespace that the pod is running in. Tags: `permission` `primary-field` | `default`; `kube-system` |
| `k8s.namespace.uid` | string | resource experimental The UID of the namespace. | `bfb1ba44-3bcb-467d-a2dc-188fd74d1db5` |
| `k8s.networkpolicy.name` | string | resource experimental Name of the NetworkPolicy. | `my-networkpolicy` |
| `k8s.node.name` | string | resource stable Name of the node. | `cluster-pool-1-c3c7423d-azth` |
| `k8s.persistentvolume.name` | string | resource experimental Name of the PersistentVolume. | `my-persistentvolume` |
| `k8s.persistentvolumeclaim.name` | string | resource experimental Name of the PersistentVolumeClaim. | `my-persistentvolumeclaim` |
| `k8s.pod.name` | string | resource stable The name of the pod. | `checkoutservice-7895755b94-mzs5m` |
| `k8s.pod.uid` | string | resource stable The UID of the pod. | `275ecb36-5aa8-4c2a-9c47-d8bb681b9aff` |
| `k8s.replicaset.name` | string | resource experimental Name of the ReplicaSet. | `my-replicaset` |
| `k8s.replicationcontroller.name` | string | resource experimental Name of the ReplicationController. | `my-replicationcontroller` |
| `k8s.secret.name` | string | resource experimental Name of the Secret. | `my-secret` |
| `k8s.service.name` | string | resource stable The name of the Kubernetes service. | `my-service` |
| `k8s.statefulset.name` | string | resource experimental Name of the StatefulSet. | `my-statefulset` |
| `k8s.workload.kind` | string | resource stable The type of the workload. The value is the Kubernetes object kind of the workload in lowercase. | `deployment`; `statefulset`; `cronjob`; `job`; `daemonset`; `replicaset` |
| `k8s.workload.name` | string | resource stable The name of the workload. | `checkoutservice` |
| `k8s.workload.uid` | string | resource experimental The UID of the workload. | `786a41e4-e673-44bb-bb30-18888f797a2b` |

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `k8s.namespace.annotation.__attribute_name__` | string | resource experimental Kubernetes namespace annotation that should be enriched on ingest signals and service metrics. The \_\_attribute\_name\_\_ is a placeholder that can freely be chosen. | `k8s.namespace.annotation.team=a_team` |
| `k8s.namespace.label.__attribute_name__` | string | resource experimental Kubernetes namespace label that should be enriched on ingest signals and service metrics. The \_\_attribute\_name\_\_ is a placeholder that can freely be chosen. | `k8s.namespace.label.env=dev` |
| `k8s.pod.annotation.__attribute_name__` | string | resource experimental Kubernetes pod annotation that should be enriched on ingest signals and service metrics. The \_\_attribute\_name\_\_ is a placeholder that can freely be chosen. | `k8s.pod.annotation.team=a_team` |
| `k8s.pod.label.__attribute_name__` | string | resource experimental Kubernetes pod label that should be enriched on ingest signals and service metrics. The \_\_attribute\_name\_\_ is a placeholder that can freely be chosen. | `k8s.pod.label.env=dev` |
| `k8s.workload.annotation.__attribute_name__` | string | resource experimental Kubernetes workload annotation that should be enriched on ingest signals and service metrics. The \_\_attribute\_name\_\_ is a placeholder that can freely be chosen. | `k8s.workload.annotation.team=a_team` |
| `k8s.workload.label.__attribute_name__` | string | resource experimental Kubernetes workload label that should be enriched on ingest signals and service metrics. The \_\_attribute\_name\_\_ is a placeholder that can freely be chosen. | `k8s.workload.label.env=dev` |

## Apache Kafka

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `messaging.kafka.broker_id` | string | experimental The ID of the Kafka broker. | `0`; `1`; `2` |
| `messaging.kafka.component` | string | experimental The component of the Kafka Connect worker. | `GroupCoordinator 1` |
| `messaging.kafka.connect.connector_name` | string | experimental The name of the Kafka Connect connector. | `my-s3-connector`; `jdbc-source-connector` |
| `messaging.kafka.connect.task_id` | string | experimental The ID of the Kafka Connect task. | `0`; `1`; `2` |
| `messaging.kafka.connect.worker_id` | string | experimental The ID of the Kafka Connect worker. | `10.0.0.1:8083`; `worker-1` |

## Standard fields used for log events

Fields relevant for log events

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `log.file.name` | string | experimental The basename of the file. | `messages`; `agent.log` |
| `log.file.path` | string | experimental The full path to the file. | `/var/log/messages`; `/var/log/dynatrace/agent.log` |
| `log.iostream` | string | stable The I/O stream to which the log was emitted. | `stdout`; `stderr` |
| `log.logger` | string | experimental The name of the logger inside an application. This name is usually the name of the class that initialized the logger, but it can be a custom name. | `main.logger`; `kafka.server.KafkaServer` |
| `log.raw_level` | string | experimental The original severity level of the log entry as recorded by the source, before standardization into the log.level format. [1](#fn-11-1-def) | `silly`; `verbose` |
| `log.source` | string | stable Human-readable attribute that identifies a log stream. [2](#fn-11-2-def) Tags: `permission` | `/var/log/messages`; `Windows Event Log`; `Docker Container Output`; `stdout` |
| `log.source.file_status` | string | experimental The field represents the current monitoring state of a log source. | `OK`; `NOT_EXIST`; `BINARY` |
| `log.source.ingest_status` | string | experimental The field represents the log content ingestion status. | `Ingested`; `Not ingested`; `Partially ingested` |
| `log.source.origin` | string | stable The log source origin indicates where the log derives from. | `CUSTOM`; `IIS_LOG_DETECTOR` |
| `log.source.type` | string | experimental Stores the human-readable name of the detector or mechanism that identified this log source | `Custom`; `OpenFilesDetector`; `SystemLogsDetector` |
| `loglevel` | string | stable The log event severity level. | `ERROR`; `INFO`; `TRACE` |

1

The log.raw\_level can vary in type depending on the log entry. It may be represented as a string in some cases or as an integer (for example, 30, 40, 50) in others.

2

Can contain, for example, a file path, standard output, or an URI etc., depending on the log stream type. The value should be stable for one logical source (for example, not affected by log file rotation digits).

`log.iostream` MUST be one of the following:

| Value | Description |
| --- | --- |
| `stderr` | std\_err |
| `stdout` | std\_out |

`log.source.origin` MUST be one of the following:

| Value | Description |
| --- | --- |
| `CONTAINER_LOG_DETECTOR` | Container log detector. |
| `CUSTOM_LOG` | Custom log source configuration. |
| `EVENT_CHANNEL_DETECTOR` | Event channel detector. |
| `IIS_LOG_DETECTOR` | IIS log detector. |
| `JOURNALD_LOG_DETECTOR` | Journald log detector. |
| `OPEN_LOG_DETECTOR` | Open log file detector. |
| `SYSTEM_LOG_DETECTOR` | System log detector. |

`loglevel` MUST be one of the following:

| Value | Description |
| --- | --- |
| `ALERT` | alert |
| `CRITICAL` | critical |
| `DEBUG` | debug |
| `EMERGENCY` | emergency |
| `ERROR` | error |
| `FATAL` | fatal |
| `INFO` | info |
| `NONE` | none |
| `NOTICE` | notice |
| `SEVERE` | severe |
| `TRACE` | trace |
| `WARN` | warn |

## Messaging

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `messaging.batch.failed_count` | long | experimental The number of messages in the batch for which publishing failed. | `1`; `3`; `15` |
| `messaging.batch.failure_codes` | string[] | experimental The vendor-provided error codes explaining why an operation on the message broker failed. To limit attribute size, not all error codes might be included. | `['MalformedDetail', 'InvalidArgument']` |
| `messaging.batch.message_count` | long | stable The number of messages sent, received, or processed in the scope of the batching operation. | `1`; `2`; `3` |
| `messaging.client.id` | string | stable A unique identifier for the client that consumes or produces a message. | `aclient`; `myhost@68d46b89c9-c29qc` |
| `messaging.consumer.group.name` | string | stable The name of the consumer group with which a consumer is associated. | `my-group`; `indexer` |
| `messaging.destination.kind` | string | deprecated The kind of message destination | `queue`; `topic` |
| `messaging.destination.manager_name` | string | stable The destination's manager name [1](#fn-12-1-def) | `MyBroker` |
| `messaging.destination.name` | string | stable The message destination name [2](#fn-12-2-def) | `MyQueue`; `MyTopic` |
| `messaging.destination.partition.id` | string | stable String representation of the partition ID the message is sent to or received from. | `1` |
| `messaging.destination.temporary` | boolean | stable A boolean that is true if the message destination is temporary and might not exist anymore after messages are processed. |  |
| `messaging.is_failed` | boolean | experimental Indicates that the messaging operation is considered failed according to the failure detection rules. Only present if the `messaging.operation.type` is `process`. |  |
| `messaging.message.body.size` | long | stable The (uncompressed) size of the message payload in bytes. | `2738` |
| `messaging.message.conversation_id` | string | stable The conversation ID identifying the conversation to which the message belongs, represented as a string. Sometimes called "Correlation ID". | `MyConversationId` |
| `messaging.message.header.__key__` | record | stable The message headers, `__key__` being the message header/attribute name, for example, "messaging.message.header.ExtendedPayloadSize". The data type of the value depends on the attribute. | `1024, "my-eu-bucket-3", ["a", "b"]` |
| `messaging.message.id` | string | stable A value used by the messaging system as an identifier for the message, represented as a string. | `452a7c7c7c7048c2f887f61572b18fc2` |
| `messaging.operation.type` | string | stable A string identifying the kind of messaging operation. | `peek` |
| `messaging.source.kind` | string | deprecated The kind of message source | `queue`; `topic` |
| `messaging.source.manager_name` | string | **deprecated Replaced by `messaging.destination.manager_name`.** The source's manager name [3](#fn-12-3-def) | `MyBroker` |
| `messaging.source.name` | string | **deprecated Replaced by `messaging.destination.name`.** The message source name [4](#fn-12-4-def) | `MyQueue`; `MyTopic` |
| `messaging.source.temporary` | boolean | **deprecated Replaced by `messaging.destination.temporary`.** A boolean that is true if the message source is temporary and might not exist anymore after messages are processed. |  |
| `messaging.system` | string | stable An identifier for the messaging system. See below for a list of well-known identifiers. | `kafka`; `rabbitmq` |

1

Manager name uniquely identifies the broker.

2

Destination name uniquely identifies a specific queue, topic or other entity within the broker.

3

Manager name uniquely identifies the broker.

4

Source name uniquely identifies a specific queue, topic, or other entity within the broker.

`messaging.destination.kind` MUST be one of the following:

| Value | Description |
| --- | --- |
| `queue` | A message sent to or received from a queue |
| `topic` | A message sent to or received from a topic |

`messaging.operation.type` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `peek` | A message is received from a destination by a message consumer/server, but left there (`span.kind` is "consumer"). |
| `process` | A message previously received from a destination is processed by a message consumer (`span.kind` is "consumer"). |
| `publish` | A message is sent to a destination by a message producer (`span.kind` is "producer"). |
| `receive` | A message is received from a destination by a message consumer (`span.kind` is "consumer"). |

`messaging.source.kind` MUST be one of the following:

| Value | Description |
| --- | --- |
| `queue` | A message received from a queue |
| `topic` | A message received from a topic |

`messaging.system` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `activemq` | ActiveMQ |
| `artemis` | ActiveMQ Artemis |
| `aws_eventbridge` | Amazon EventBridge |
| `aws_sns` | Amazon Simple Notification Service (SNS) |
| `aws_sqs` | Amazon Simple Queue Service (SQS) |
| `azure_eventgrid` | Azure Event Grid |
| `azure_eventhubs` | Azure Event Hubs |
| `azure_servicebus` | Azure Service Bus |
| `gcp_pubsub` | Google Cloud Pub/Sub |
| `hornetq` | HornetQ |
| `jms` | Java Message Service |
| `kafka` | Apache Kafka |
| `mqseries` | IBM MQ |
| `msmq` | MSMQ |
| `rabbitmq` | RabbitMQ |
| `rocketmq` | Apache RocketMQ |
| `sag_webmethods_is` | Software AG, webMethods Integration Server |
| `tibco_ems` | Tibco EMS |
| `weblogic` | Oracle WebLogic |
| `websphere` | IBM WebSphere Application Server |

### Akka Messaging

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `messaging.akka.actor.kind` | string | experimental Name of the top-level actor. See [The Akka actor hierarchyï»¿](https://doc.akka.io/docs/akka/2.5/guide/tutorial_1.html#the-akka-actor-hierarchy) | `system`; `user` |
| `messaging.akka.actor.path` | string | experimental Path to actor inside actor system. | `/system/log1-Logging$DefaultLogger`; `/remote/akka.tcp/RequesterSystem@localhost:52133/user/requestActor/$a` |
| `messaging.akka.actor.system` | string | experimental Name of the actor system. | `RequesterSystem`; `ResponseSystem` |
| `messaging.akka.actor.type` | string | experimental Fully qualified type name of actor. | `com.acme.RespondingActor` |
| `messaging.akka.message.type` | string | experimental Fully qualified type name of the message. | `java.lang.String`; `akka.event.Logging$Info2`; `com.acme.twosuds.ResponseActor$RequestMessage` |

### Kafka Messaging

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `messaging.kafka.message.key` | string | experimental The `key` property of the message. | `mykey` |
| `messaging.kafka.message.tombstone` | boolean | experimental A boolean that is true if the message is a tombstone. [1](#fn-13-1-def) | `true` |
| `messaging.kafka.offset` | long | experimental The offset of the message. | `42` |

1

If the message is a tombstone, the value is `true`. When missing, the value is assumed to be `false`.

## Metric

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `metric.key` | string | stable The identifier of a metric, grouping numeric measurements that share the same measurement semantics (i.e. were measured "the same way".) Tags: `permission` | `dt.host.cpu.usage` |
| `metric.type` | string | stable Identifies the type of metric and therefore the timeseries rollup functions it supports. | `summary_stats` |

`metric.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `histogram` | Identifies a metrics record supporting minimum, maximum, average, sum, count, and percentile timeseries rollup functions. |
| `summary_stats` | Identifies a metrics record supporting minimum, maximum, average, sum, and count timeseries rollup functions. |

## Module Insights

In webserver technologies a multitude of modules might be contributing to handling a single web request. Module insights provides timings for these, where available.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `module_insights.modules` | record | experimental Modules executed as part of this web request, represented as map from module name to duration in nanoseconds spent. | `{'HttpRedirectionModule': 10299, 'BasicAuthenticationModule': 4665}` |

## Network

These attributes may be used for any network related operation.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `network.carrier.name` | string | experimental The mobile carrier name. | `Magenta`; `AT&T` |
| `network.connection.subtype` | string | experimental Further details that specify `network.connection.type`, such as the cellular or WI-FI technology. | `lte`; `802.11x` |
| `network.connection.type` | string | experimental The internet connection type. | `cell`; `wifi` |
| `network.local.address` | ipAddress | experimental Local address of the network connection. | `10.102.0.45` |
| `network.peer.ip` | ipAddress | experimental The immediate peer IP address of the network connection. This is the IP address of the other side of the socket connection. | `140.78.100.116`; `172.16.11.1`; `2a01:468:1000:9::140` |
| `network.peer.port` | long | experimental The immediate peer port number of the network connection. This is the port number of the other side of the socket connection. | `49158`; `65531`; `443` |
| `network.protocol.name` | string | stable [OSI Application Layerï»¿](https://osi-model.com/application-layer/) or non-OSI equivalent. | `amqp`; `http`; `mqtt` |
| `network.protocol.number` | long | experimental The IANA protocol number of the traffic. For more information, see [Assigned Internet Protocol Numbersï»¿](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). | `3`; `10` |
| `network.protocol.version` | string | experimental Version of the application layer protocol used. | `1.1`; `3.1.1` |
| `network.proxy_chain` | record[] | experimental Information about proxies or load balancers between a client and a server, parsed out from `Forwarded` or `X-Forwarded-For (XFF)` HTTP headers. Each element in the list is a record with `ip` (type ipAddress) and `port` (type long) attributes that denote the intermediary. Port is optional; if it's not available, no `port` attribute is present in the record. | `[{'ip': '172.16.1.80', 'port': 3128}, {'ip': '18.66.233.23'}, {'ip': '2001:db8::aa:bb'}]` |
| `network.transport` | string | stable [OSI Transport Layerï»¿](https://osi-model.com/transport-layer/) or [Inter-process Communication methodï»¿](https://en.wikipedia.org/wiki/Inter-process_communication) | `tcp`; `udp` |
| `network.type` | string | stable [OSI Network Layerï»¿](https://osi-model.com/network-layer/) or non-OSI equivalent. | `ipv4`; `ipv6` |

`network.connection.type` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `cell` | cell |
| `unavailable` | unavailable |
| `unknown` | unknown |
| `wifi` | wifi |
| `wired` | wired |

`network.transport` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `inproc` | In-process communication. [1](#fn-14-1-def) |
| `other` | Something else (non-IP-based). |
| `pipe` | Named or anonymous pipe. |
| `tcp` | TCP |
| `udp` | UDP |
| `unix` | Unix domain socket. |

1

Signals that there is only in-process communication not using a "real" network protocol in cases where network attributes would typically be expected. Usually, all other network attributes can be left out.

`network.type` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `ipv4` | IPv4 |
| `ipv6` | IPv6 |

## Network device

Fields that are used in extensions to describe network devices.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `device` | string | resource **deprecated Used in Extension Framework 2.0** Address (IP address with port) used by a monitored device to communicate with an extension. | `10.102.0.45:161` |
| `device.address` | ipAddress | resource **deprecated Used in Extension Framework 2.0** IP address used by a monitored device to communicate with an extension. | `10.102.0.45` |
| `device.name` | string | resource **deprecated Used in Extension Framework 2.0** Name of a device monitored by an extension. | `AT1i-WLC-TestingLab.dynatrace.org` |
| `device.port` | string | resource **deprecated Used in Extension Framework 2.0** Port used by a monitored device to communicate with an extension. | `161` |

## Standard fields used for network flows

Fields relevant for network flows

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `network_flow.bytes.rx` | long | experimental Number of bytes (octets) received during given interval, direction: to Process (PGI). |  |
| `network_flow.bytes.tx` | long | experimental Number of bytes (octets) transmitted during given interval, direction: from Process (PGI). |  |
| `network_flow.destination.address` | ipAddress | experimental Destination IP address. By convention, destination means TCP server (acceptor of the connection). | `192.33.1.2`; `2001:0db8:85a3:0000:0000:8a2e:0370:7334` |
| `network_flow.destination.port` | long | experimental Flow destination port. By convention, destination port means TCP server (acceptor of the connection). | `22`; `8080` |
| `network_flow.network.transport` | string | experimental Protocol | `TCP`; `other`; `UDP` |
| `network_flow.network.type` | string | experimental IP protocol version. | `IPV4` |
| `network_flow.packets.retransmitted.base.rx` | long | experimental Number of packets received, used as the base for retransmission rate, direction: to Process (PGI). |  |
| `network_flow.packets.retransmitted.base.tx` | long | experimental Number of packets sent, used as the base for retransmission rate, direction: from Process (PGI). |  |
| `network_flow.packets.retransmitted.rx` | long | experimental Number of retransmitted packets during given interval, direction: to Process (PGI). |  |
| `network_flow.packets.retransmitted.tx` | long | experimental Number of retransmitted packets during given interval, direction: from Process (PGI). |  |
| `network_flow.packets.rx` | long | experimental Number of packets received during given interval, direction: to Process (PGI). |  |
| `network_flow.packets.tx` | long | experimental Number of packets transmitted during given interval, direction: from Process (PGI). |  |
| `network_flow.process_is_server` | boolean | experimental Indicates whether the entity (Process) is acting as a server in the network flow. | `true`; `false` |
| `network_flow.source.address` | ipAddress | experimental Source IP address. By convention, source means TCP client (initiator of the connection). | `192.33.1.2`; `2001:0db8:85a3:0000:0000:8a2e:0370:7334` |
| `network_flow.tcp.rtt` | long | experimental Mean RTT value [ms]. |  |
| `network_flow.tcp.rtt.ack` | long | experimental Mean RTT ack value [ms]. |  |
| `network_flow.tcp.sessions.new` | long | experimental Number of new TCP sessions in the flow. |  |
| `network_flow.tcp.sessions.reset` | long | experimental Number of reset (rejected) TCP sessions in the flow. |  |
| `network_flow.tcp.sessions.timeout` | long | experimental Number of timed out TCP sessions in flow. |  |

`network_flow.network.type` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `IPV4` | ipv4 |
| `IPV6` | ipv6 |

## Nodejs

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `nodejs.app.base.dir` | string | resource experimental |  |
| `nodejs.app.name` | string | resource experimental |  |
| `nodejs.script.name` | string | resource experimental |  |

## Elasticsearch

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `opensearch.document_id` | string | experimental ID of the document stored in OpenSearch. | `2kuZ25sBo9KPhzL41rsg` |
| `opensearch.id` | string | experimental X-Opaque-Id http header if one was used. | `152220` |
| `opensearch.index` | string | experimental The name of the OpenSearch index. | `opensearch-index`; `index-2024.01.01` |
| `opensearch.node_id` | string | experimental The ID of the node. | `80f333333b31623f94213a9a43cef6b1` |
| `opensearch.routing` | string | experimental Custom routing value. | `user42` |
| `opensearch.shard_id` | string | experimental The ID of the OpenSearch shard. | `VzblS9m1Q9CBaTHoEbKLnT` |
| `opensearch.stats` | string | experimental Search group defined in the query. | `autocomplete`; `dashboard_query` |
| `opensearch.took` | string | experimental Execution time of the request. | `56ms` |
| `opensearch.took_millis` | string | experimental Execution time of the request. | `56` |
| `opensearch.total_hits` | string | experimental Total number of hits returned by the search. | `0 hits`; `4 hits` |
| `opensearch.total_shards` | string | experimental Total number of shards. | `1`; `9` |

## OpenStack

Fields that can come from applications running on OpenStack.

### Fields

#### Resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `openstack.availability_zone` | string | resource experimental A specific availability zone in the given OpenStack region. | `us-east-1a` |
| `openstack.instance_uuid` | string | resource experimental UUID of specific OpenStack instance. | `6790cb48-f8e9-4773-bcea-001469de0599` |

## Origin

The origin of a request associated with this event.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `origin.address` | string | experimental Source IP address of the request associated with this event. Must be set if origin.type is 'REST', must not be set otherwise. | `10.11.12.13` |
| `origin.session` | string | experimental The ID of the browser session (if present) associated with the event. | `node0hfznc` |
| `origin.type` | string | experimental Origin type of the request associated with this event. | `REST`; `LOCAL` |
| `origin.x_forwarded_for` | string | experimental The verbatim value of the X-Forwarded-For HTTP request header (if present) of the request associated with the event. | `1.2.3.4` |

`origin.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `LOCAL` | The event provider issued the request locally. |
| `RECOVERY` | The event provider issued the request locally as part of disaster recovery. |
| `REST` | The event provider received an external REST API call. |

## OS

The os namespace contains information on the operating system running an application.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `os.architecture` | string | resource experimental Architecture of the CPU, discovered from the operating system. | `X86` |
| `os.name` | string | resource stable The OS name in a short, human-readable format. | `iOS` |
| `os.type` | string | resource experimental Type of discovered operating system. | `LINUX`; `WINDOWS` |
| `os.version` | string | resource stable The complete OS version, including patch, build, and other information. | `15.3.1`; `Ubuntu 16.04.7 LTS (Xenial Xerus) (kernel 4.15.0-206-generic)`; `Windows Server 2022 Datacenter 21H2 2009, ver. 10.0.20348` |

## OpenTelemetry scope

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `otel.scope.name` | string | experimental The name of the instrumentation scope - (`InstrumentationScope.Name` in OTLP). | `io.opentelemetry.contrib.mongodb` |
| `otel.scope.version` | string | experimental The version of the instrumentation scope - (`InstrumentationScope.Version` in OTLP). | `1.0.0` |

## Php

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `php.cli.script.path` | string | resource experimental |  |
| `php.cli.working.dir` | string | resource experimental |  |
| `php.drupal.application.name` | string | resource experimental |  |
| `php.fpm.pool.name` | string | resource experimental |  |
| `php.symfony.application.name` | string | resource experimental |  |
| `php.wordpress.blog.name` | string | resource experimental also see [https://developer.wordpress.org/reference/functions/get\\_bloginfo/ï»¿](https://developer.wordpress.org/reference/functions/get%5C_bloginfo/) |  |

## PostgreSQL

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `postgresql.session.id` | string | experimental A unique ID to identify a PostgreSQL database session. | `00112233-4455-6677-8899-aabbccddeeff` |

## Primary Grail Tags

Primary Grail tags are a small set of important, customer-selected tagsâsuch as Kubernetes labels, AWS/Azure tags, or key organizational attributesâthat Dynatrace automatically attaches to all raw telemetry data at ingest, using the `primary_tags.*` prefix. This enrichment enables fast, consistent filtering, grouping, and permission management across all data, without complex joins or proprietary tagging rules. Primary Grail tags are centrally configured and ensure that cloud-native and business-relevant metadata is always available for queries, dashboards, and access control.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `primary_tags.__key__` | string | resource experimental Primary Grail tags are used to tag a resource in a meaningful way. `__key__` is populated with the tag name, for example, `primary_tags.ownership`. In case of single-value tags, the value is a string. In case of multi-value tags, the value is an array of strings. | `team-alpha`; `team-bravo` |

## Process

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `process.bitness` | string | resource experimental The architecture of the monitored entity in terms of how many bits compose a basic value. | `64` |
| `process.containerized` | boolean | resource experimental True if given process is running inside container. |  |
| `process.executable.name` | string | resource experimental The name of the process executable. On Linux based systems, can be set to the `Name` in `proc/[pid]/status`. On Windows, can be set to the base name of `GetProcessImageFileNameW`. | `otelcol` |
| `process.executable.path` | string | resource experimental The full path to the process executable. On Linux-based systems, can be set to the target of `proc/[pid]/exe`. On Windows, can be set to the result of `GetProcessImageFileNameW`. | `/usr/bin/cmd/otelcol` |
| `process.listen_ports` | array | resource experimental An array of open listen ports. | `50000`; `50001`; `50002`; `50003` |
| `process.metadata` | record | resource experimental It contains a diagnostic collection of input parameters that were used or could have been used in assigning processes to the process entity. | `NODE_JS_APP_BASE_DIRECTORY:C:/home/site/wwwroot` |
| `process.pid` | long | resource experimental Process Identifier (PID) as observed by the monitored process. | `1234` |

## RabbitMQ

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `rabbitmq.function.arity` | long | experimental The number of arguments the `rabbitmq.function.name` takes. | `2`; `5` |
| `rabbitmq.function.name` | string | experimental The name of the RabbitMQ function within the `rabbitmq.module.name` that generated the log entry. | `start_it`; `main` |
| `rabbitmq.module.name` | string | experimental The name of the RabbitMQ module that generated the log entry. | `rabbit`; `my_module` |
| `rabbitmq.pid` | string | experimental ID of the Erlang process. | `0.58.0`; `1.20.4` |

## Redis

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `redis.role` | string | experimental The role of the Redis process (for example, 'M' for Master or 'X' for sentinel). | `C` |

`redis.role` MUST be one of the following:

| Value | Description |
| --- | --- |
| `C` | Child process for persistence (RDB/AOF). |
| `M` | Master Redis process. |
| `R` | Replica Redis process. |
| `X` | Sentinel monitoring process. |

## Request

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `request.is_failed` | boolean | experimental Indicates that the request is considered failed according to the failure detection rules. Only present on the request root span. |  |
| `request.is_root_span` | boolean | experimental Marks the root of a request. It's the first span and starts the request within a service. |  |

## Request Attributes

Request scoped attributes (e.g. method parameters, return values, class names, â¦) captured by the OneAgent based on a request attribute definition.
The actual name of the attribute is the prefix "request\_attribute" plus the "request attribute name" defined in the request attributes configuration.
Request attributes are built based on captured attributes and other attributes like HTTP header values or "normal" span attributes, on which the aggregations (first/last value, distinct values, ...), type conversion and normalizations defined in the request attribute configuration are performed.
They are evaluated for an entire request (possibly consisting of multiple spans) and are stored only on the request root node.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `request_attribute.__attribute_name__` | array | stable Contains the request scoped reconciled values of the attribute named `__attribute_name__` defined by the request attribute configuration. The data type of the value depends on the request attribute definition. Tags: `sensitive-spans` | `42`; `Platinum`; `['Product A', 'Product B']`; `['Special Offer', '1702']` |

## Remote Procedure Calls

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `rpc.method` | string | experimental The name of the (logical) method being called [1](#fn-15-1-def) | `exampleMethod` |
| `rpc.namespace` | string | experimental The namespace of the method being called. In SOAP, it would be the XML namespace. | `tempuri.org` |
| `rpc.service` | string | experimental The full (logical) name of the service being called, including its package name, if applicable. [2](#fn-15-2-def) | `myservice.EchoService` |
| `rpc.system` | string | experimental A string identifying the remoting system or framework. See below for a list of well-known identifiers. | `apache_cxf`; `dotnet_wcf`; `grpc`; `jax_ws` |

1

This is the logical name of the method from the RPC interface perspective, which can be different from the name of any implementing method/function. The `code.function` attribute may be used to store the latter (e.g., method executing the call on the server side, RPC client stub method on the client side).

2

This is the logical name of the service from the RPC interface perspective, which can be different from the name of any implementing class. The `code.namespace` attribute may be used to store the latter (despite the attribute name, it may include a class name, e.g., class with method executing actually executing the call on the server side, RPC client stub class on the client side).

`rpc.system` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `apache_axis` | Apache Axis |
| `apache_cxf` | Apache CXF |
| `apache_wink` | Apache Wink |
| `aws_api` | AWS API |
| `dotnet_remoting` | .NET Remoting |
| `dotnet_wcf` | .NET WCF |
| `grpc` | gRPC |
| `java_rmi` | Java RMI |
| `jax_ws` | JAX-WS |
| `jboss` | JBoss |
| `jersey` | Jersey |
| `openedge` | Progress OpenEdge |
| `resteasy` | JBoss RESTEasy |
| `restlet` | Restlet |
| `spring_ws` | Spring Web Services |
| `tibco_ws` | Tibco Web Services |
| `weblogic_ws` | WebLogic Web Services |
| `webmethods` | Webmethods |

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `rpc.grpc.status_code` | long | experimental The [numeric status codeï»¿](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md) of the gRPC request. |  |

## Server

The server namespace contains information on the responder of a network connection.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `server.address` | string | stable Logical server hostname, matches server FQDN if available, and IP or socket address if FQDN is not known. | `example.com` |
| `server.port` | long | stable Logical server port number. | `65123`; `80` |
| `server.resolved_ips` | ipAddress[] | stable A list of IP addresses that are the result of DNS resolution of `server.address`. | `[194.232.104.141, 2a01:468:1000:9::140]` |

## Service

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `service.name` | string | resource stable The logical name of the service. | `shoppingcart` |

## Servlet

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `servlet.context.name` | string | resource experimental also see [https://docs.oracle.com/javaee/6/api/javax/servlet/ServletContext.html#getServletContextNameï»¿](https://docs.oracle.com/javaee/6/api/javax/servlet/ServletContext.html#getServletContextName) |  |
| `servlet.context.path` | string | resource experimental also see [https://docs.oracle.com/javaee/6/api/javax/servlet/ServletContext.html#getContextPathï»¿](https://docs.oracle.com/javaee/6/api/javax/servlet/ServletContext.html#getContextPath) |  |

## SNMP

Fields that are used in SNMP extensions.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `trap_oid` | string | resource **deprecated Used in Extension Framework 2.0** The trap OID of a given event. | `SNMPv2-MIB::coldStart` |
| `version` | string | resource **deprecated Used in Extension Framework 2.0** The SNMP version. | `SNMPv3` |

## Softwareag

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `softwareag.install.root` | string | resource experimental |  |
| `softwareag.product.prop.name` | string | resource experimental |  |

## Span

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `span.alternate_parent_id` | uid | experimental The alternative `span.id` of this span's parent span. If a trace is monitored by more tracing systems (for example, OneAgent and OpenTelemetry), there might be two parent spans. If the two parent spans differ, `span.parent_id` holds the ID of the parent span originating from same tenant of the span while `span.alternate_parent_id` holds the other parent span ID. The `span.alternate_parent_id` is an 8-byte ID and hex-encoded if shown as a string. | `f76281848bd8288c` |
| `span.events` | record[] | stable A collection of events. An event is an optional time-stamped annotation of the span and consists of a name and key-value pairs. |  |
| `span.exit_by_exception_id` | uid | stable The `exception.id` of the exception the its `span.events` with the current span exited. The referenced exception has set the attribute `exception.escaped` to true. |  |
| `span.id` | uid | stable A unique identifier for a span within a trace. The `span.id` is an 8-byte ID and hex-encoded if shown as a string. | `f76281848bd8288c` |
| `span.is_exit_by_exception` | boolean | stable Set to `true` if an exception exited the span. If set to `false`, the span has exception events, but none exited the span. |  |
| `span.is_subroutine` | boolean | experimental If set to `true`, it indicates that this span is a subroutine of its parent span. The spans represent functions running on the same thread on the same call stack. |  |
| `span.kind` | string | stable Distinguishes between spans generated in a particular context. | `server` |
| `span.links` | record[] | stable A collection of links. A link is a reference from this span to a whole trace or a span in the same or different trace. |  |
| `span.name` | string | stable The span name identifies the work represented by the span, for example, the route in an HTTP controller, an RPC method name, a function name, or the name of a subtask or stage within a larger computation. | `prepareOrderItemsAndShippingQuoteFromCart`; `org.example.CheckoutService/PlaceOrder`; `orders process`; `GET /products/{product_id}`; `HTTP POST` |
| `span.parent_id` | uid | stable The `span.id` of this span's parent span. The `span.parent_id` is an 8-byte ID and hex-encoded if shown as a string. | `f76281848bd8288c` |
| `span.status_code` | string | stable Defines the status of a span, predominantly used to indicate a processing error. This field is absent if the reported span status is `unset`. | `error` |
| `span.status_message` | string | experimental An optional text that can provide a descriptive error message in case the `span.status_code` is `error`. | `Connection closed before message completed`; `Error sending request for url` |
| `span.timing.cpu` | duration | stable The overall CPU time spent executing the span, including the CPU times of child spans that are running on the same thread on the same call stack. |  |
| `span.timing.cpu_self` | duration | stable The CPU time spent exclusively on executing this span, not including the CPU times of any children. |  |

`span.kind` MUST be one of the following:

| Value | Description |
| --- | --- |
| `client` | Indicates that the span describes a request to some remote service. |
| `consumer` | Indicates that a span describes a child of an asynchronous `producer` request. |
| `internal` | Default Value. Indicates that the span represents an internal operation. |
| `link` | Indicates that the span describes a Dynatrace link node. |
| `producer` | Indicates that the span describes the initiator of an asynchronous request. |
| `server` | Indicates that the span covers server-side handling of a synchronous RPC or other remote request. |

`span.status_code` MUST be one of the following:

| Value | Description |
| --- | --- |
| `error` | An error happened while processing the span. |
| `ok` | The span was explicitly validated as having completed successfully, despite maybe even containing information about an error. |

## Span Event

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `span_event.name` | string | stable Some span events have a defined semantics based on the name of the span event. | `exception` |

`span_event.name` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `bizevent` | Indicates that the span event represents a business event |
| `exception` | Indicates that the span event represents an exception |
| `feature_flag` | Indicates that the span event represents a feature flag |

### Reference

[Language Independent Interface Types For OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-proto/blob/main/opentelemetry/proto/trace/v1/trace.proto)

## Spring

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `spring.application.group` | string | resource experimental Also see [Common Application Propertiesï»¿](https://docs.spring.io/spring-boot/appendix/application-properties/index.html#application-properties.core.spring.application.group) |  |
| `spring.application.name` | string | resource experimental Also see [Common Application Propertiesï»¿](https://docs.spring.io/spring-boot/appendix/application-properties/index.html#application-properties.core.spring.application.name) |  |
| `spring.profile.name` | string | resource experimental The active profile (last value of spring.profiles.active) |  |
| `spring.startup.class` | string | resource experimental |  |

## Disk extension

### Fields

Disk

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `storage.disk.encrypted` | boolean | resource stable Is encrypted disk. |  |
| `storage.disk.fstype` | string | resource stable Type of file system on the disk. | `ext4`; `btrfs` |
| `storage.disk.kname` | string | resource stable Kernel name of the disk device. It's also the disk ID in relation to other devices. | `sda` |
| `storage.disk.model` | string | resource stable Disk model. | `baracuda` |
| `storage.disk.mountpoint` | string | resource stable Primary mount point. | `/mnt/disk1` |
| `storage.disk.other-mountpoints` | string[] | resource stable List of other mount points of the disk | `['/home/user1/mydisk', '/opt/volume1']` |
| `storage.disk.path` | string | resource stable Path to the disk. | `/dev/sda` |
| `storage.disk.read-only` | boolean | resource stable Is read-only disk. |  |
| `storage.disk.removable` | boolean | resource stable Is removable disk. |  |
| `storage.disk.serial` | string | resource stable Disk serial number. | `1234-56789` |
| `storage.disk.type` | string | resource stable Disk device type. | `disk`; `hardware raid` |
| `storage.disk.vendor` | string | resource stable Vendor of the disk. | `seagate` |

Partition

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `storage.partition.encrypted` | boolean | resource stable Is encrypted partition. |  |
| `storage.partition.fstype` | string | resource stable Type of file system on the partition. | `ext4`; `btrfs` |
| `storage.partition.kname` | string | resource stable Kernel name of the partition device. It's also the partition ID in relation to other devices. | `sda1` |
| `storage.partition.mountpoint` | string | resource stable Primary mount point. | `/mnt/diskA` |
| `storage.partition.other-mountpoints` | string[] | resource stable List of other mount points of the partition. | `['/home/user1/mydiskA', '/opt/volumeA']` |
| `storage.partition.path` | string | resource stable Path to the partition. | `/dev/sda1` |
| `storage.partition.read-only` | boolean | resource stable Is read-only partition. |  |
| `storage.partition.removable` | boolean | resource stable Is removable partition (true when disk is removable). |  |
| `storage.partition.type` | string | resource stable Partition device type. | `partition` |

Volume

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `storage.volume.display-name` | string | resource stable Name of the volume device. | `vg0-lv1`; `vg1-lv2`; `my-volume` |
| `storage.volume.fstype` | string | resource stable Type of file system on the volume. | `ext4`; `btrfs` |
| `storage.volume.kname` | string | resource stable Kernel name of the volume device. It's also the volume ID in relation to other devices. | `dm-1`; `dm-2`; `dm-5` |
| `storage.volume.mountpoint` | string | resource stable Primary mount point. | `/mnt/diskA` |
| `storage.volume.other-mountpoints` | string[] | resource stable List of other mount points of the software RAID. | `['/home/user1/mydiskA', '/opt/volumeA']` |
| `storage.volume.path` | string | resource stable Path to the volume device. | `/dev/mapper/vg0-lv1` |
| `storage.volume.read-only` | boolean | resource stable Is read-only volume. |  |
| `storage.volume.removable` | boolean | resource stable Is removable volume. |  |
| `storage.volume.type` | string | resource stable Volume device type. | `lvm` |

Software RAID

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `storage.software-raid.encrypted` | boolean | resource stable Is encrypted software RAID. |  |
| `storage.software-raid.fstype` | string | resource stable Type of file system on the software RAID, | `ext4`; `btrfs` |
| `storage.software-raid.kname` | string | resource stable Kernel name of the software RAID device. It's also the software RAID ID in relation to other devices. | `md0`; `md1`; `md3` |
| `storage.software-raid.mountpoint` | string | resource stable Primary mount point. | `/mnt/diskA` |
| `storage.software-raid.other-mountpoints` | string[] | resource stable List of other mount points of the software RAID. | `['/home/user1/mydiskA', '/opt/volumeA']` |
| `storage.software-raid.parent` | string | resource stable ID of parent software RAID in which this software RAID is nested. | `md0` |
| `storage.software-raid.path` | string | resource stable Path to the software RAID device. | `/dev/md0` |
| `storage.software-raid.read-only` | boolean | resource stable Is read-only software RAID. |  |
| `storage.software-raid.removable` | boolean | resource stable Is removable software RAID. |  |
| `storage.software-raid.type` | string | resource stable Software RAID device type. | `raid0, raid10` |

## Subtrace

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `subtrace.id` | uid | experimental Present on every span of a subtrace. All spans within one subtrace share the same identifier. The ID is a hex-encoded numerical value and not globally unique, but guaranteed to be unique within one particular trace. | `95efd70fcdb5b7b3`; `96835e1d65490b48` |
| `subtrace.is_root_span` | boolean | experimental Marks the root of a subtrace. This is typically the first span of a request within a service. Endpoints detection rules are evaluated on subtrace root spans. |  |

## Supportability

Additional information about the attributes of a data point.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `supportability.alr_sampling_ratio` | long | experimental The denominator of the sampling ratio of the Dynatrace cluster, the attribute is only set if Adaptive Load Redution (ALR) is active on the Dynatrace cluster. A numerator is not specified, as it's always 1. If, for example, the Dynatrace cluster samples with a probability of 1/8 (12,5%), the value of `supportability.alr_sampling_ratio` would be 8 and the numerator is 1. | `8` |
| `supportability.atm_sampling_ratio` | long | experimental The denominator of the sampling ratio of an Adaptive Traffic Management (ATM) aware sampler. The attribute is always present if an ATM-aware sampler is active (this applies, for example, to Dynatrace OneAgent). A numerator is not specified, as it is always 1. If, for example, Dynatrace OneAgent samples with a probability of 1/16 (6,25%), the value of `supportability.atm_sampling_ratio` would be 16 and the numerator is 1. | `16` |
| `supportability.custom_service.rule_id` | uid | experimental The ID of a custom service configuration rule. This field is only present if a custom service was configured as an automatic instrumentation rule in Dynatrace. | `4d76194c11a9426197a9062548f9e66e` |
| `supportability.dropped_attributes_count` | long | experimental The number of attributes that were discarded on the source. Attributes can be discarded because their keys are too long or because there are too many attributes. | `1` |
| `supportability.dropped_events_count` | long | experimental The number of span events that were discarded on the source. | `1` |
| `supportability.dropped_http_request_headers_count` | long | experimental Number of `http.request.header.__key__` that were discarded. | `1` |
| `supportability.dropped_http_request_parameters_count` | long | experimental Number of `http.request.parameter.__key__` that were discarded. | `1` |
| `supportability.dropped_links_count` | long | experimental The number of span links that were discarded on the source. | `1` |
| `supportability.external.dt.entity.service` | string | deprecated The ID of the external service detected from this client span. The span comes from the service identified by `dt.entity.service`. This attribute indicates the external service that has been derived from it, as the remote side is not fully monitored by Dynatrace. It's only available for Service Detection v1 (SDv1) detected services that have the `isExternalService` entity attribute set to `true`. Note that this refers to classic service entities only, not Smartscape services (which do not have external services), so the attribute is removed when all services are based exclusively on Smartscape. | `SERVICE-0FA460E5CB2491A3` |
| `supportability.flaws` | string[] | experimental A string array of one or multiple error codes indicating issues in the assembly of a trace in Dynatrace. Typically, issues come from erroneous (3rd party) instrumentations (e.g. not sending a required field), data loss due to network connectivity (e.g. missing parent span) or conditions implied by the nature of the trace (e.g. trace exceeding the depth limit). The attribute is only present in case an assembly issue was detected (the list will not be empty). For more information and details about specific error codes, please reach out to Dynatrace support. | `['C4', 'S3', 'A2']` |
| `supportability.is_non_key_requests_endpoint_bucket` | boolean | experimental Indicates that the span stems from a request that was not marked as a key request. | `true` |
| `supportability.latency_before_openpipeline` | duration | experimental The difference between the Dynatrace cluster node time and the `end_time` before the span is forwarded to OpenPipeline. Only available on subtrace root spans sent from the OneAgent. | `500000000000` |
| `supportability.non_persisted_attribute_keys` | string[] | experimental A string array of attribute keys that were not stored as they were not allow-listed or were removed during the pipeline steps. | `['"my_span_attribute", "db.name"']` |
| `supportability.original_start_time` | timestamp | experimental The original start time of the span. Only available if the value of the `start_time` attribute was truncated. Truncating the start time is technically required for long running spans that have a start time older than three days in the past. | `1649822520123123123` |
| `supportability.serverid.addressee` | long | experimental The id of the Dynatrace cluster node this span was addressed to. This is only available if it differs from the value of `supportability.serverid.processing`. | `5` |
| `supportability.serverid.processing` | long | experimental The id of the Dynatrace cluster node that received and processed this span. | `5` |

### OT span rule configuration

Span sensor rules used during ingestion of OpenTelemetry/OpenTracing spans by instrumentation of the OpenTelemetry/OpenTracing Apis are applied at span start time.
Therefore these rules can only operate on span attributes given at span start time.

The value at span start time of attributes captured by this instrumentation is preserved to allow proper rule configuration.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `supportability.span_start.__key__` | record | experimental Span attributes set at span start time in case it changed later. The value at span start is relevant for span rule evaluation done by OpenTelemetry/OpenTracing instrumentation. `__key__` is a placeholder for the actual attribute name. The data type of the value depends on the attribute. | `5, "initial", ["a", "b"]` |
| `supportability.span_start.attribute_names` | array | experimental List of attribute names set at span start invocation time. |  |
| `supportability.span_start.span.name` | string | experimental The span name at span start time in case it changed later. The value at span start is relevant for span rule evaluation done by OpenTelemetry/OpenTracing instrumentation. | `GET` |

## Telemetry

The `telemetry.sdk.*` fields are used to describe the telemetry SDK in OpenTelemetry or ODIN ingest. It can be considered the closest equivalent of ODIN/OTel data to `dt.agent.module.*`.

The `telemetry.exporter.*` fields are used to define the exporter that exports telemetry data and is expected to be different for each exporter in case when multiple exporters co-exist.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `telemetry.exporter.name` | string | resource experimental The exporter name. | `odin` |
| `telemetry.exporter.package_version` | string | resource experimental The version as exposed to the package manager (for example, npm). | `1.285.1` |
| `telemetry.exporter.version` | string | resource experimental The full agent/exporter version. | `1.285.1.20240101-256988` |
| `telemetry.sdk.language` | string | resource stable The programming language/tech of the telemetry SDK. | `nodejs`; `python`; `java` |
| `telemetry.sdk.name` | string | resource stable The name of the telemetry SDK. | `odin`; `opentelemetry` |
| `telemetry.sdk.version` | string | resource stable The version string of the telemetry SDK. | `1.20.0` |

## Thread

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `thread.id` | long | stable Current "managed" thread id (as opposed to OS thread id). | `42` |
| `thread.name` | string | stable Current thread name. | `main` |
| `thread.pool.name` | string | stable The name of the thread pool. | `WorkerThreadPool` |

## TIBCO Business Works

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `tibco.businessworks.app.node.name` | string | resource experimental |  |
| `tibco.businessworks.app.space.name` | string | resource experimental |  |
| `tibco.businessworks.domain.name` | string | resource experimental |  |
| `tibco.businessworks.home` | string | resource experimental |  |
| `tibco.businessworks.property.file.name` | string | resource experimental |  |
| `tibco.businessworks.property.file.path` | string | resource experimental |  |
| `tibco.businessworks_ce.app.name` | string | resource experimental |  |
| `tibco.businessworks_ce.version` | string | resource experimental |  |

## Time correction

The time\_correction namespace contains information on time corrections applied to the timestamps of an event, for example, `start_time`, `timestamp` or `event.end`.
Time corrections may be necessary if events are reported with timestamps that are completely off compared to cluster time. For example, Dynatrace RUM reported data can be off depending on client time.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `time_correction.is_applied` | boolean | experimental If set to `true`, time correction has been applied to the event's timestamps. | `false` |
| `time_correction.offset` | long | experimental The offset (in nanoseconds) that is applied to all timestamp fields. The value may be negative. | `127927969312` |

## Timeframe

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `end` | timestamp | stable The end of the timeframe, exclusive. | `12/13/2023, 12:57 PM` |
| `start` | timestamp | stable The start of the timeframe, inclusive. | `12/13/2023, 10:57 AM` |

## Tls

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `tls.cipher` | string | experimental String indicating the [cipherï»¿](https://datatracker.ietf.org/doc/html/rfc5246#appendix-A.5) used during the current connection. | `TLS_RSA_WITH_3DES_EDE_CBC_SHA`; `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256` |
| `tls.protocol.name` | string | experimental Normalized lowercase protocol name parsed from the original string of the negotiated [SSL/TLS protocol versionï»¿](https://docs.openssl.org/1.1.1/man3/SSL_get_version/#RETURN-VALUES). | `ssl`; `tls` |
| `tls.protocol.version` | string | experimental The numeric part of the version parsed from the original string of the negotiated [SSL/TLS protocol versionï»¿](https://docs.openssl.org/1.1.1/man3/SSL_get_version/#RETURN-VALUES). | `1.2`; `3` |

## Trace

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `trace.alternate_id` | uid | experimental The preserved trace ID when OneAgent and other tracing systems monitor the same process and the trace ID from the other tracing system was replaced by the OneAgent trace ID. The `trace.alternate_id` is a 16-byte ID and hex-encoded if shown as a string. | `357bf70f3c617cb34584b31bd4616af8` |
| `trace.capture.reasons` | string[] | experimental Explains why this trace was captured, multiple reasons can apply simultaneously. Note: The sampling approach ('atm' or 'fixed') is always placed at the first position in the array. These two values are mutually exclusive, though 'fixed' may appear with other capture triggers. Values: 'atm' (Dynatrace's intelligent sampling automatically adjusted trace capture based on traffic volume and system load), 'fixed' (trace captured due to configured percentage rules - either global settings or specific endpoint rules), 'custom' (trace captured because of custom correlation headers propagated between services or systems), 'mainframe' (trace originated from or includes IBM mainframe/z/OS components), 'serverless' (trace captured from serverless functions like AWS Lambda, Azure Functions, or similar platforms), 'rum' (trace initiated by user interactions in web browsers or mobile apps monitored by Dynatrace RUM agents). | `['atm']`; `['fixed']`; `['fixed', 'custom']`; `['fixed', 'rum']` |
| `trace.id` | uid | stable A unique identifier for a trace. The `trace.id` is a 16-byte ID and hex-encoded if shown as a string. | `357bf70f3c617cb34584b31bd4616af8` |
| `trace.is_sampled` | boolean | experimental Flag indicating whether the trace was recorded. If set to `true`, the trace is recorded. If set to `false`, the trace is ignored. | `true`; `false` |
| `trace.state` | string | experimental The trace state in the w3c-trace-context format. | `f4fe05b2-bd92206c@dt=fw4;3;abf102d9;c4592;0;0;0;2ee;5607;2h01;3habf102d9;4h0c4592;5h01;6h5f9a543f1184a52b1b744e383038911c;7h6564df6f55bd6eae,apmvendor=boo,foo=bar` |

## URL

The url namespace contains semantic conventions for URL and its components.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `url.domain` | string | experimental The URI domain component. | `www.foo.bar`; `google.com`; `wikipedia.org` |
| `url.fragment` | string | stable The URI fragment component. | `SemConv` |
| `url.full` | string | stable Absolute URL describing a network resource according to RFC3986. Tags: `sensitive-spans` | `https://www.foo.bar/docs/search?q=OpenTelemetry#SemConv` |
| `url.path` | string | stable The URI path component. | `/docs/search` |
| `url.path.pattern` | string | experimental The URL path pattern used to match a set of URLs with variable path segments. | `/docs/{id}`; `/users/{userId}/posts/{postId}`; `/api/v1/resources/*` |
| `url.port` | long | experimental The URI port component. | `443`; `80` |
| `url.provider` | string | experimental The provider type for the host name of `url.full`. This information is determined by Dynatrace RUM resource detection. | `third_party` |
| `url.query` | string | stable The URI query component. Tags: `sensitive-spans` | `q=OpenTelemetry` |
| `url.scheme` | string | stable The URI scheme component identifying the used protocol. | `https`; `ftp`; `telnet` |
| `url.truncated_path` | string | experimental Truncated URI path component for endpoint detection of certain technologies that do not provide a `http.route`. The truncation logic depends on the technology and is a best effort to provide a stable value. Example Adobe Experience Manager (AEM): First two parts of `url.path`. Truncated value of `/content/wknd/us/en/` is `/content/wknd`. | `/docs` |

`url.provider` MUST be one of the following:

| Value | Description |
| --- | --- |
| `cdn` | CDN (content delivery network). |
| `first_party` | First-party provider. |
| `third_party` | Third-party provider. |

## User

Representation of a physical or logical user.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `user.email` | string | stable Email of the user. | `user@mail.com` |
| `user.id` | string | stable Unique UUID of a human user. If the system itself has to be represented, the constant 'system' is used. | `35ba9499-f87c-4047-962c-14dc32e255e5`; `system` |
| `user.name` | string | experimental Full name of the user. If the system itself has to be represented, the constant 'System' is used. | `Wolfgang Amadeus Mozart`; `System` |
| `user.organization` | string | experimental Organization the user belongs to. | `DYNATRACE`; `CUSTOMER`; `PARTNER` |

`user.organization` MUST be one of the following:

| Value | Description |
| --- | --- |
| `CUSTOMER` | Customer organization |
| `DYNATRACE` | Dynatrace organization |
| `PARTNER` | Dynatrace partner organization |

`user.organization` MUST be one of the following:

| Value | Description |
| --- | --- |
| `DYNATRACE` | Dynatrace organization |
| `CUSTOMER` | Customer organization |
| `PARTNER` | Dynatrace partner organization |

## VCS Repository

The `vcs` namespace contains information about Version Control Systems.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `vcs.change.id` | string | experimental The identifier of the change, for example, pull request ID or merge request ID. It is typically unique per repository and generated by the version control system itself. | `1234` |
| `vcs.change.state` | string | experimental The state of the change, for example, the state of a pull request or merge request. | `wip`; `open`; `reopened`; `closed`; `merged` |
| `vcs.change.title` | string | experimental The human-readable title of the change, for example, pull request title or merge request title. | `CA-1234: Fix some stuff`; `[chore] update dependency` |
| `vcs.change.url.full` | string | experimental The full URL to the change, for example, the full URL to the pull request or merge request. | `https://github.com/dynatrace-oss/terraform-provider-dynatrace/pull/20` |
| `vcs.line_change.type` | string | experimental The type of line change being measured on a branch or change. | `added`; `removed` |
| `vcs.ref.base.name` | string | experimental The name of the reference in the repository. This can be a branch name or a tag name. [1](#fn-16-1-def) | `my-branch-name` |
| `vcs.ref.base.revision` | string | experimental The revision in the repository. For Git this is a synonym for a commit hash, whereas in SVN it is a revision number. [2](#fn-16-2-def) | `d4322ab6cba38d21ad83c9de304a6a214ecf2cdc`; `main`; `1337` |
| `vcs.ref.base.type` | string | experimental The reference type in the repository. [3](#fn-16-3-def) | `branch`; `tag` |
| `vcs.ref.head.name` | string | experimental The name of the reference in the repository. This can be a branch name or a tag name. [4](#fn-16-4-def) | `my-branch-name` |
| `vcs.ref.head.revision` | string | experimental The revision in the repository. For Git, this is a synonym for a commit hash, whereas in SVN, it is a revision number. [5](#fn-16-5-def) | `d4322ab6cba38d21ad83c9de304a6a214ecf2cdc`; `main`; `1337` |
| `vcs.ref.head.type` | string | experimental The reference type in the repository. [6](#fn-16-6-def) | `branch`; `tag` |
| `vcs.ref.type` | string | experimental The reference type in the repository. | `branch`; `tag` |
| `vcs.repository.name` | string | experimental The human-readable name of the repository. It should not include any additional identifiers like GitLab group or GitHub organization. [7](#fn-16-7-def) | `dynatrace-configuration-as-code` |
| `vcs.repository.url.full` | string | experimental The repository's full URL. [8](#fn-16-8-def) | `https://github.com/dynatrace-oss/terraform-provider-dynatrace` |
| `vcs.revision_delta.direction` | string | experimental The type of revision comparison. | `ahead`; `behind` |

1

The base name refers to the starting point of a change. For example, if a feature branch was created from `main`,
`main` is the base reference of type `branch`.

2

The base revision refers to the starting revision of a change. For example, if a branch was created from a certain
commit, this commit is the base revision.

3

The base type refers to the reference type of the starting point of a change. For example,
if a feature branch was created from the `main` branch, `branch` is the base reference's type.

4

The head name refers to the current reference's name. For example,
if `main` is currently checked out, the head name is `main`.

5

The head revision refers to the currently referenced revision.

6

The head type refers to the currently referenced type in the repository. For example,
if the `main` branch is currently checked out, the head reference is of type `branch`.

7

Be aware that the repository name might clash with forked repositories.

8

For Git VCS, this should not include the `.git` URL suffix.

`vcs.change.state` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `closed` | The change was closed without being merged into the target code base. |
| `merged` | The change has successfully been merged into the target code base. |
| `open` | The change is open and ready for review or currently under review. It has not been merged yet, and changes are still possible. |
| `reopened` | The change was re-opened after being `closed` and is ready for review again. |
| `wip` | The change is still a work in progress and not yet ready for review. |

`vcs.line_change.type` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `added` | How many lines were added. |
| `removed` | How many lines were removed. |

`vcs.ref.base.type` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `branch` | The base reference type is a branch. |
| `tag` | The base reference type is a tag. |

`vcs.ref.head.type` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `branch` | The head reference type is a branch. |
| `tag` | The head reference type is a tag. |

`vcs.ref.type` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `branch` | The reference type is a branch. |
| `tag` | The reference type is a tag. |

`vcs.revision_delta.direction` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `ahead` | How many revisions the change is ahead of the target ref. |
| `behind` | How many revisions the change is behind of the target ref. |

## VMware

Fields that can come from applications running on VMware.

### Fields

#### Resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `vmware.datacenter.name` | string | resource experimental The name of the data center in which the hypervisor is running. | `srvwasapp1Cell01` |
| `vmware.disk.name` | string | resource experimental ESXi host disk. | `srvwasapp1Cell01` |
| `vmware.hypervisor.name` | string | resource experimental ESXi host. | `my-hypervisor.lab.dynatrace.org` |
| `vmware.nic.name` | string | resource experimental ESXi host network interface. | `vmnic0`; `vmnic1`; `vmnic2` |
| `vmware.vcenter.name` | string | resource experimental Name of the VMware vCenter server managing the multi-hypervisor environment. | `my-vcenter.lab.dynatrace.org` |
| `vmware.vm.name` | string | resource experimental The name of the virtual machine. | `easytravel-demo` |

## Vulnerability

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `vulnerability.code_location.name` | string | stable Name of the code location where the code-level vulnerability was detected. | `org.dynatrace.profileservice.BioController.markdownToHtml(String):80` |
| `vulnerability.cvss.base_score` | double | stable Vulnerability's CVSS base score provided by NVD. | `8.1` |
| `vulnerability.cvss.version` | string | stable Vulnerability's CVSS score version. | `3.1`; `4.0` |
| `vulnerability.davis_assessment.assessment_mode` | string | stable Availability of the information based on which the vulnerability assessment has been done. | `FULL`; `NOT_AVAILABLE`; `REDUCED` |
| `vulnerability.davis_assessment.assessment_mode_reasons` | string[] | experimental Reasons for the assessment mode. | `['LIMITED_BY_CONFIGURATION', 'LIMITED_AGENT_SUPPORT']` |
| `vulnerability.davis_assessment.data_assets_status` | string | stable Vulnerability's reachability of related data assets by affected entities. | `NOT_AVAILABLE`; `NOT_DETECTED`; `REACHABLE` |
| `vulnerability.davis_assessment.exploit_status` | string | stable Vulnerability's public exploits status. | `AVAILABLE`; `NOT_AVAILABLE` |
| `vulnerability.davis_assessment.exposure_status` | string | stable Vulnerability's internet exposure status. | `NOT_AVAILABLE`; `NOT_DETECTED`; `PUBLIC_NETWORK`; `ADJACENT_NETWORK` |
| `vulnerability.davis_assessment.level` | string | stable Vulnerability's risk level based on Davis Security Score. | `LOW`; `MEDIUM`; `HIGH`; `CRITICAL`; `NONE` |
| `vulnerability.davis_assessment.score` | double | stable Vulnerability's Davis Security Score (1-10) calculated by Dynatrace. | `8.1` |
| `vulnerability.davis_assessment.vulnerable_function_status` | string | stable Usage status of the vulnerable functions causing the vulnerability. | `IN_USE`; `NOT_AVAILABLE`; `NOT_IN_USE` |
| `vulnerability.description` | string | stable Description of the vulnerability. | `More detailed description about improper input validation vulnerability.` |
| `vulnerability.display_id` | string | stable Dynatrace user-readable identifier for the vulnerability. | `S-1234` |
| `vulnerability.exploit.status` | string | experimental Whether there is a known exploit for the vulnerability. | `AVAILABLE`; `NOT_AVAILABLE` |
| `vulnerability.external_id` | string | stable External provider's unique identifier for the vulnerability. | `SNYK-JAVA-ORGAPACHEHTTPCOMPONENTS-30646` |
| `vulnerability.external_url` | string | stable External provider's URL to the details page of the vulnerability. | `https://example.com` |
| `vulnerability.first_seen` | timestamp | stable Timestamp of when the vulnerability was first detected. | `2023-03-22T13:19:36.945Z` |
| `vulnerability.id` | string | stable Dynatrace unique identifier for the vulnerability. | `2039861408676243188` |
| `vulnerability.is_fix_available` | boolean | experimental Indicates if a vulnerability fix is available. |  |
| `vulnerability.mute.change_date` | timestamp | stable Timestamp of the vulnerability's last muted or unmuted action. | `2023-03-22T13:19:36.945Z` |
| `vulnerability.mute.comment` | string | experimental Comment when muting or unmuting the vulnerability. | `Muted because it's a false positive.` |
| `vulnerability.mute.reason` | string | stable Reason for muting or unmuting the vulnerability. | `FALSE_POSITIVE`; `IGNORE`; `AFFECTED`; `CONFIGURATION_NOT_AFFECTED`; `OTHER` |
| `vulnerability.mute.status` | string | stable Vulnerability's mute status. | `MUTED`; `NOT_MUTED` |
| `vulnerability.mute.user` | string | stable User who last changed the vulnerability's mute status. | `user@example.com` |
| `vulnerability.parent.davis_assessment.assessment_mode` | string | stable Availability of the information based on which the vulnerability assessment has been done. | `FULL`; `NOT_AVAILABLE`; `REDUCED` |
| `vulnerability.parent.davis_assessment.data_assets_status` | string | stable Vulnerability's reachability of related data assets by affected entities. | `NOT_AVAILABLE`; `NOT_DETECTED`; `REACHABLE` |
| `vulnerability.parent.davis_assessment.exposure_status` | string | stable Vulnerability's internet exposure status. | `NOT_AVAILABLE`; `NOT_DETECTED`; `PUBLIC_NETWORK`; `ADJACENT_NETWORK` |
| `vulnerability.parent.davis_assessment.level` | string | stable Vulnerability's Davis Security Score level. | `LOW`; `MEDIUM`; `HIGH`; `CRITICAL`; `NONE` |
| `vulnerability.parent.davis_assessment.score` | double | stable Vulnerability's Davis Security Score (1-10) calculated by Dynatrace. | `8.1` |
| `vulnerability.parent.davis_assessment.vulnerable_function_status` | string | stable Usage status of vulnerable functions causing the vulnerability. Status is `IN_USE` when there's at least one vulnerable function in use by an application. | `IN_USE`; `NOT_AVAILABLE`; `NOT_IN_USE` |
| `vulnerability.parent.first_seen` | string | stable Timestamp of when the vulnerability was first detected. | `2023-03-22T13:19:36.945Z` |
| `vulnerability.parent.mute.change_date` | timestamp | stable Timestamp of the last mute or unmute action of the vulnerability. | `2023-03-22T13:19:36.945Z` |
| `vulnerability.parent.mute.reason` | string | stable Reason for muting or unmuting the vulnerability. | `FALSE_POSITIVE`; `IGNORE`; `AFFECTED`; `CONFIGURATION_NOT_AFFECTED`; `OTHER` |
| `vulnerability.parent.mute.status` | string | stable Vulnerability's mute status. | `MUTED`; `NOT_MUTED` |
| `vulnerability.parent.mute.user` | string | stable User who last changed the vulnerability's mute status. | `user@example.com` |
| `vulnerability.parent.resolution.change_date` | string | stable Timestamp of the vulnerability's last resolution status change. | `2023-03-22T13:19:37.466Z` |
| `vulnerability.parent.resolution.status` | string | stable Current status of the vulnerability. | `OPEN`; `RESOLVED` |
| `vulnerability.parent.risk.level` | string | stable Vulnerability's risk score level defined by the provider. For Dynatrace, the Davis Security Score level. | `LOW`; `MEDIUM`; `HIGH`; `CRITICAL`; `NONE` |
| `vulnerability.parent.risk.score` | double | stable Vulnerability's risk score defined by the provider. For Dynatrace, Davis Security Score. | `8.1` |
| `vulnerability.previous.cvss.base_score` | double | stable Vulnerability's previous CVSS base score (in case the CVSS base score has changed). | `8.1` |
| `vulnerability.previous.davis_assessment.data_assets_status` | string | stable Vulnerability's previous reachability of related data assets by affected entities (in case the reachability has changed). | `NOT_AVAILABLE`; `NOT_DETECTED`; `REACHABLE` |
| `vulnerability.previous.davis_assessment.exploit_status` | string | stable Vulnerability's previous public exploit status (in case the public exploit status has changed). | `AVAILABLE`; `NOT_AVAILABLE` |
| `vulnerability.previous.davis_assessment.exposure_status` | string | stable Vulnerability's previous internet exposure status (in case the internet exposure status has changed). | `NOT_AVAILABLE`; `NOT_DETECTED`; `PUBLIC_NETWORK`; `ADJACENT_NETWORK` |
| `vulnerability.previous.davis_assessment.level` | string | stable Vulnerability's previous risk level (in case the risk level has changed). | `LOW`; `MEDIUM`; `HIGH`; `CRITICAL`; `NONE` |
| `vulnerability.previous.davis_assessment.score` | double | stable Vulnerability's previous Davis Security Score (in case Davis Security Score has changed). | `8.1` |
| `vulnerability.previous.davis_assessment.vulnerable_function_status` | string | stable Vulnerability's previous vulnerable function status (in case the vulnerable function status has changed). | `IN_USE`; `NOT_AVAILABLE`; `NOT_IN_USE` |
| `vulnerability.previous.external_id` | string | experimental Vulnerabilityâs unique identifier from the previous external provider. | `SNYK-JAVA-ORGAPACHEHTTPCOMPONENTS-30646` |
| `vulnerability.previous.mute.change_date` | string | stable Timestamp of the vulnerability's previous mute status (in case the mute status has changed). | `2023-03-22T13:19:36.945Z` |
| `vulnerability.previous.mute.comment` | string | experimental Comment of the vulnerability's previous mute status. | `Muted because it's a false positive.` |
| `vulnerability.previous.mute.reason` | string | stable Reason for last muting or unmuting the vulnerability (in case the reason for muting or unmuting the vulnerability has changed). | `Muted: False positive` |
| `vulnerability.previous.mute.status` | string | stable Vulnerability's previous mute status (in case the mute status has changed). | `MUTED`; `NOT_MUTED` |
| `vulnerability.previous.mute.user` | string | stable User who last changed the vulnerability's mute status (in case the mute status was last changed by a different user). | `user@example.com` |
| `vulnerability.previous.resolution.status` | string | stable Vulnerability's previous resolution status (in case the resolution status has changed). | `OPEN`; `RESOLVED` |
| `vulnerability.previous.risk.level` | string | stable Vulnerability's previous risk score level (in case the risk score level has changed). | `LOW`; `MEDIUM`; `HIGH`; `CRITICAL` |
| `vulnerability.previous.risk.score` | double | stable Vulnerability's previous risk score (in case the risk score has changed). | `8.1` |
| `vulnerability.references.cve` | string[] | stable List of the vulnerability's CVE IDs. | `['CVE-2021-41079']` |
| `vulnerability.references.cwe` | string[] | stable List of the vulnerability's CWE IDs. | `['CWE-20']` |
| `vulnerability.references.owasp` | string[] | stable List of vulnerability's OWASP IDs. | `['2021:A3']` |
| `vulnerability.remediation.description` | string | experimental Description of the vulnerability's remediation advice. | `Upgrade component to version 1.2.3 or higher` |
| `vulnerability.remediation.status` | string | experimental Indicates whether a fix for the vulnerability is available. | `AVAILABLE`; `NOT_AVAILABLE` |
| `vulnerability.resolution.change_date` | timestamp | stable Timestamp of the vulnerability's last resolution status change. | `2023-03-22T13:19:37.466Z` |
| `vulnerability.resolution.status` | string | stable Vulnerability's resolution status. | `OPEN`; `RESOLVED` |
| `vulnerability.risk.level` | string | stable Vulnerability's risk score level defined by the provider. For Dynatrace, the Davis Security Score level. | `LOW`; `MEDIUM`; `HIGH`; `CRITICAL`; `NONE` |
| `vulnerability.risk.scale` | string | stable Scale by which the vulnerability's risk score and risk score level defined by the provider are measured. | `Davis Security Score` |
| `vulnerability.risk.score` | double | stable Vulnerability's risk score defined by the provider. For Dynatrace, Davis Security Score. | `8.1` |
| `vulnerability.stack` | string | experimental Level of the vulnerable component in the technological stack. | `CODE`; `CODE_LIBRARY`; `SOFTWARE`; `CONTAINER_ORCHESTRATION` |
| `vulnerability.technology` | string | stable Technology of the vulnerable component. | `JAVA`; `DOTNET`; `GO`; `PHP`; `NODE_JS` |
| `vulnerability.title` | string | stable Title of the vulnerability. | `Improper Input Validation` |
| `vulnerability.type` | string | stable Classification of the vulnerability based on commonly accepted enums, such as CWE. | `Improper Input Validation` |
| `vulnerability.url` | string | stable Dynatrace URL to the details page of the vulnerability. | | `https://example.com` |

`vulnerability.davis_assessment.assessment_mode` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `FULL` | full |
| `NOT_AVAILABLE` | not\_available |
| `REDUCED` | reduced |

`vulnerability.davis_assessment.data_assets_status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `NOT_AVAILABLE` | not\_available |
| `NOT_DETECTED` | not\_detected |
| `REACHABLE` | reachable |

`vulnerability.davis_assessment.exploit_status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `AVAILABLE` | available |
| `NOT_AVAILABLE` | not\_available |

`vulnerability.davis_assessment.exposure_status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `ADJACENT_NETWORK` | adjacent\_network |
| `NOT_AVAILABLE` | not\_available |
| `NOT_DETECTED` | not\_detected |
| `PUBLIC_NETWORK` | public\_network |

`vulnerability.davis_assessment.level` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `CRITICAL` | critical |
| `HIGH` | high |
| `LOW` | low |
| `MEDIUM` | medium |
| `NONE` | none |

`vulnerability.davis_assessment.vulnerable_function_status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `IN_USE` | in\_use |
| `NOT_AVAILABLE` | not\_available |
| `NOT_IN_USE` | not\_in\_use |

`vulnerability.mute.reason` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `AFFECTED` | affected |
| `CONFIGURATION_NOT_AFFECTED` | configuration\_not\_affected |
| `FALSE_POSITIVE` | false\_positive |
| `IGNORE` | ignore |
| `OTHER` | other |

`vulnerability.mute.status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `MUTED` | muted |
| `NOT_MUTED` | not\_muted |

`vulnerability.parent.davis_assessment.assessment_mode` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `FULL` | full |
| `NOT_AVAILABLE` | not\_available |
| `REDUCED` | reduced |

`vulnerability.parent.davis_assessment.data_assets_status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `NOT_AVAILABLE` | not\_available |
| `NOT_DETECTED` | not\_detected |
| `REACHABLE` | reachable |

`vulnerability.parent.davis_assessment.exposure_status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `ADJACENT_NETWORK` | adjacent\_network |
| `NOT_AVAILABLE` | not\_available |
| `NOT_DETECTED` | not\_detected |
| `PUBLIC_NETWORK` | public\_network |

`vulnerability.parent.davis_assessment.level` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `CRITICAL` | critical |
| `HIGH` | high |
| `LOW` | low |
| `MEDIUM` | medium |
| `NONE` | none |

`vulnerability.parent.davis_assessment.vulnerable_function_status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `IN_USE` | in\_use |
| `NOT_AVAILABLE` | not\_available |
| `NOT_IN_USE` | not\_in\_use |

`vulnerability.parent.mute.reason` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `AFFECTED` | affected |
| `CONFIGURATION_NOT_AFFECTED` | configuration\_not\_affected |
| `FALSE_POSITIVE` | false\_positive |
| `IGNORE` | ignore |
| `OTHER` | other |

`vulnerability.parent.mute.status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `MUTED` | muted |
| `NOT_MUTED` | not\_muted |

`vulnerability.parent.resolution.status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `OPEN` | open |
| `RESOLVED` | resolved |

`vulnerability.parent.risk.level` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `CRITICAL` | critical |
| `HIGH` | high |
| `LOW` | low |
| `MEDIUM` | medium |
| `NONE` | none |

`vulnerability.previous.davis_assessment.data_assets_status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `NOT_AVAILABLE` | not\_available |
| `NOT_DETECTED` | not\_detected |
| `REACHABLE` | reachable |

`vulnerability.previous.davis_assessment.exploit_status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `AVAILABLE` | available |
| `NOT_AVAILABLE` | not\_available |

`vulnerability.previous.davis_assessment.exposure_status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `ADJACENT_NETWORK` | adjacent\_network |
| `NOT_AVAILABLE` | not\_available |
| `NOT_DETECTED` | not\_detected |
| `PUBLIC_NETWORK` | public\_network |

`vulnerability.previous.davis_assessment.level` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `CRITICAL` | critical |
| `HIGH` | high |
| `LOW` | low |
| `MEDIUM` | medium |
| `NONE` | none |

`vulnerability.previous.davis_assessment.vulnerable_function_status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `IN_USE` | in\_use |
| `NOT_AVAILABLE` | not\_available |
| `NOT_IN_USE` | not\_in\_use |

`vulnerability.previous.mute.status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `MUTED` | muted |
| `NOT_MUTED` | not\_muted |

`vulnerability.previous.resolution.status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `OPEN` | open |
| `RESOLVED` | resolved |

`vulnerability.previous.risk.level` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `CRITICAL` | critical |
| `HIGH` | high |
| `LOW` | low |
| `MEDIUM` | medium |
| `NONE` | none |

`vulnerability.resolution.status` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `OPEN` | open |
| `RESOLVED` | resolved |

`vulnerability.risk.level` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `CRITICAL` | critical |
| `HIGH` | high |
| `LOW` | low |
| `MEDIUM` | medium |
| `NONE` | none |

`vulnerability.stack` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `CODE` | code |
| `CODE_LIBRARY` | code\_library |
| `CONTAINER_ORCHESTRATION` | container\_orchestration |
| `SOFTWARE` | software |

`vulnerability.technology` has the following list of well-known values. If one of them applies, then the respective value MUST be used, otherwise a custom value MAY be used.

| Value | Description |
| --- | --- |
| `DOTNET` | dotnet |
| `GO` | go |
| `JAVA` | java |
| `NODE_JS` | node\_js |
| `PHP` | php |

## WebLogic

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `weblogic.cluster.name` | string | resource experimental The name of the cluster this instance belongs to. | `OrderManagement2` |
| `weblogic.domain.name` | string | resource experimental The name of the domain this instance belongs to. | `CustomerManagementFulfillmentSvc` |
| `weblogic.home` | string | resource experimental The instance's home directory. | `/apps/infra/wls/bin/10.3.6_64/wlserver_10.3/server` |
| `weblogic.server.name` | string | resource experimental The instance's server name. | `OrderManagement2Srv1` |

## Websocket

The WebSocket namespace contains information on WebSocket attributes for user events. When this namespace is used, the request fields (URL and network namespace) must also be used, and `url.full` and `network.protocol.name` must be set.

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `websocket.connection.status_code` | long | experimental The WebSocket connection [status codeï»¿](https://datatracker.ietf.org/doc/html/rfc6455#section-7.4). | `1001` |

## WebSphere

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `websphere.cell.name` | string | resource experimental The name of the cell this instance belongs to. | `srvwasapp1Cell01` |
| `websphere.cluster.name` | string | resource experimental The name of the cluster this instance belongs to. | `CluApp1` |
| `websphere.node.name` | string | resource experimental Name of the node to which this instance belongs. | `nodeSrvApp2` |
| `websphere.server.name` | string | resource experimental The instance's server name. | `SrvApp2` |

## WebSphere Liberty

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `websphere_liberty.server.name` | string | resource experimental The instance's server name. | `defaultServer` |

## Winlog

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `winlog.eventid` | long | experimental Event ID is a unique identifier assigned to each event logged by the system. Each event ID corresponds to a specific type of event, such as an error, warning, or informational message. (4624 -> successful logon, 1000 -> application error) | `4624`; `1000` |
| `winlog.keywords` | string | experimental Keywords are used to categorize and group events. This categorization allows to quickly identify and focus on specific types of events that are relevant to your troubleshooting or monitoring needs. | `Classic`; `Started` |
| `winlog.level` | string | experimental Level of an event indicates its severity or importance | `Critical`; `Error`; `Warrning` |
| `winlog.opcode` | string | experimental Opcode is a value that identifies a specific activity or a point within an activity that the application was performing when it raised the event. This helps in understanding the context of the event more precisely. | `Info`; `Download` |
| `winlog.provider` | string | experimental Provider is a component or service that generates events. Providers are responsible for writing specific types of events to the event logs, such as application errors, security events, or system warnings. | `Avecto Service`; `Security-SPP` |
| `winlog.task` | long | experimental Task refers to the specific operation or activity that an event is associated with. Each event is categorized under a task, which helps in identifying what the system or application was doing when the event was logged. This can be particularly useful for troubleshooting and understanding the context of the event. (5 -> HTTP Configuration Property Trace Task, 12804 -> Other Object Access Events) | `5`; `12804` |
| `winlog.username` | string | experimental Username refers to the account name associated with specific events, such as logon or logoff activities. This is particularly useful for tracking user activity and identifying who was logged into the system at a given time. | `SYSTEM`; `N/A` |

## z/OS

### Fields zos resource attributes

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cics.transaction.system_id` | string | resource experimental The system ID of the CICS region that this transaction executed on. | `C259`; `CICS` |
| `zos.address_space_id` | long | resource experimental The address space identifier (ASID) of the z/OS address space. | `1`; `296` |
| `zos.cpu_model_number` | string | resource experimental The model number of the CPU assigned to this LPAR. | `8562`; `3931` |
| `zos.cpu_serial_number` | string | resource experimental The serial number of the CPU assigned to this LPAR. | `054BB88562`; `15D77D2084` |
| `zos.job_id` | string | resource experimental The job ID of the z/OS address space. | `JOB12345` |
| `zos.job_name` | string | resource experimental The jobname of the z/OS address space. | `CICSAOR0`; `CTGATM00`; `IMSCR15` |
| `zos.job_step_id` | string | resource experimental The step ID within the job within the z/OS address space. | `00000001`; `00000002` |
| `zos.lpar_name` | string | resource experimental The name of the LPAR that the z/OS address space executes within. | `S0W1`; `ABCD` |
| `zos.sys_id` | string | resource experimental The system ID of the CICS/IMS address space. | `C259`; `CICS`; `IMSF` |
| `zos.system_name` | string | resource experimental The name of the z/OS system instance. | `S0W1`; `ABCD` |
| `zos.total_general_purpose_processors` | long | resource experimental The number of general purpose processors (GCPs) assigned for this LPAR. | `1`; `190` |
| `zos.total_physical_memory` | long | resource experimental The total amount of memory, in terabytes, assigned for this LPAR. | `1`; `16` |
| `zos.total_ziip_processors` | long | resource experimental The number of zIIPs assigned for this LPAR. | `0`; `8` |
| `zos.transaction.job_name` | string | resource experimental The jobname of the z/OS address space that the transaction executed in. | `CICSAOR0`; `CTGATM00`; `IMSCR15` |
| `zos.transaction.lpar_name` | string | resource experimental The name of the LPAR that the transaction executed on. | `S0W1`; `ABCD` |
| `zos.virtualization` | string | resource experimental Type of virtualization on the mainframe. | `LPAR` |

### Fields zos transactions general

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `zos.transaction.call_type` | string | experimental The type of transaction call that was invoked. | `CTG` |
| `zos.transaction.id` | string | experimental The ID of this transaction. | `CEMT`; `DTAX`; `IVTNO` |
| `zos.transaction.program_type` | string | experimental The type of transaction that was executed. | `DLI_DB`; `DLI_DC`; `MQ`; `DB2` |

`zos.transaction.call_type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `CTG` | A CTG request triggered this transaction. |
| `DPL` | A CICS DPL request triggered this transaction. |
| `HTTP` | An HTTP or HTTPS request triggered this transaction. |
| `IMS_CONNECT` | An IMS Connect request triggered this transaction. |
| `IMS_CONNECT_API` | An IMS Connect API request triggered this transaction. |
| `IMS_TRANS_EXEC` | The application program being scheduled and running to handle this transaction. |
| `ITRA` | An IMS TM Resource Adapter request triggered this transaction. |
| `MQ` | An MQ operation triggered this transaction. |
| `MSC` | An IMS MSC request triggered this transaction. |
| `PGM_SWITCH` | An IMS Program Switch request triggered this transaction. |
| `SDK` | An SDK call triggered this transaction. |
| `SHARED_QUEUE` | An IMS Shared Queue request triggered this transaction. |
| `SOAP` | A SOAP request triggered this transaction. |
| `START` | An EXEC CICS START triggered this transaction. |
| `TTX` | A green screen terminal transaction code triggered this transaction. |
| `TX` | A CICS or IMS transaction code triggered this transaction. |
| `ZOS_CONNECT` | A z/OS Connect request triggered this transaction. |

`zos.transaction.program_type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `DB2` | The transaction performs DB2 database actions. |
| `DLI_DB` | The transaction performs DLI database actions. |
| `DLI_DC` | The transaction performs DLI data communications actions. |
| `MQ` | The transaction performs MQ Queue actions. |

### Fields cics transactions

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cics.transaction.class_name` | string | experimental The name of the transaction class of this transaction. | `null`; `DFHTCL00` |
| `cics.transaction.client.ip` | ipAddress | experimental IP address of the client (IPv4 or IPv6) that made the request that triggered the transaction. | `194.232.104.141`; `2a01:468:1000:9::140` |
| `cics.transaction.client.port` | long | experimental Port number of the client that made the request that triggered the transaction. | `65123`; `80` |
| `cics.transaction.path.name` | string | experimental The path name, only applicable for web requests. | `/dtrouter` |
| `cics.transaction.task_id` | long | experimental The CICS task ID of this transaction. | `1234` |
| `cics.transaction.transaction_group_id` | string | experimental The transaction group ID assigned at transaction attach time. | `160dd5c5e3c44bc8e5c5c1c3f4f4f9df9fa2d8b049cb800000000000` |
| `cics.transaction.unit_of_work_id` | long | experimental The unit of work ID for this transaction, which is normally represented as a hex value. | `15977055984148641282`; `15977055491352760323` |
| `cics.transaction.user_id` | string | experimental The user ID of the user who triggered this transaction. | `USER1`; `anon` |
| `cics.transaction.wlm.reporting_service_class_name` | string | experimental The name of the z/OS Workload Manager (WLM) reporting service class of this transaction. | `null`; `BAT_ATM`; `RC_CICS` |
| `cics.transaction.wlm.service_class_name` | string | experimental The name of the z/OS Workload Manager (WLM) service class of this transaction. | `null`; `SYSSTC`; `VEL15I5` |

### Fields cics files

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `cics.file.defining_region_name` | string | experimental The system ID of the CICS region that is defined on the request. | `C259`; `CICS` |
| `cics.file.is_local` | boolean | experimental A boolean that is true if the file is defined within the CICS region that it executed in. | `true` |
| `cics.file_name` | string | experimental The logical name of the file, as defined in CEDA. | `EXMPCAT`; `CICSFILE` |

### Fields ims transactions

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `ims.message.transaction.message.segment_count` | long | experimental The number of segments in the message. | `1`; `5` |
| `ims.message.transaction.message.size` | long | experimental The size of the message. | `10`; `421` |
| `ims.message.transaction.terminal_name` | string | experimental The terminal name that this IMS transaction executed on. | `HWSAM5ZD`; `10505` |
| `ims.message.transaction.unit_of_work_id` | long | experimental The unit of work ID for this transaction, which is normally represented as a hex value. | `5981228500318430862871015129591113287966852300630664295044916520394057871645605888`; `5981112713529734741010744557477214433959078921583025076794253743298954785382793216` |
| `ims.message.transaction.user_id` | string | experimental The user ID of the user who triggered this transaction. | `USER1`; `anon` |

### Fields ims execution transactions

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `ims.execution.transaction.commit_count` | long | experimental The commit count for this transaction. | `4`; `5` |
| `ims.execution.transaction.current_priority` | long | experimental The current priority of this transaction. | `1`; `5` |
| `ims.execution.transaction.execution_class` | long | experimental The execution class of this transaction. | `45`; `66` |
| `ims.execution.transaction.psb_name` | string | experimental The PSB name that this IMS transaction executed on. | `HWSAM5ZD`; `10505` |
| `ims.execution.transaction.schedule_count` | long | experimental The schedule count for this transaction. | `346613`; `421` |
| `ims.execution.transaction.unit_of_work_id` | long | experimental The unit of work ID for this transaction, which is normally represented as a hex value. | `5981228500318430862871015129591113287966852300630664295044916520394057871645605888`; `5981112713529734741010744557477214433959078921583025076794253743298954785382793216` |

### Fields ims connect transactions

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `ims.connect.transaction.client.ip` | ipAddress | experimental IP address of the client (IPv4 or IPv6) that made the request that triggered the transaction. | `194.232.104.141`; `2a01:468:1000:9::140` |
| `ims.connect.transaction.server.port` | long | experimental Port number on the IMS Connect server that received the request for this transaction | `65123`; `80` |
| `ims.connect.transaction.user_id` | string | experimental The user ID of the user who triggered this transaction. | `USER1`; `anon` |

### Fields ims tm resource adapter (ITRA) transactions

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `ims.tm.resource.adapter.semantic_detection_version` | string | experimental The detection version for this transaction. | `1` |
| `ims.tm.resource.adapter.transaction.client.ip` | ipAddress | experimental IP address of the client (IPv4 or IPv6) that made the request that triggered the transaction. | `194.232.104.141`; `2a01:468:1000:9::140` |
| `ims.tm.resource.adapter.transaction.client.port` | long | experimental Port number of the client that made the request that triggered the transaction. | `65123`; `80` |
| `ims.tm.resource.adapter.transaction.commit_mode` | long | experimental The commit mode of the transaction. | `0` |
| `ims.tm.resource.adapter.transaction.datastore_name` | string | experimental The datastore name used by this transaction. | `IMS1500` |
| `ims.tm.resource.adapter.transaction.interaction_verb` | long | experimental The interaction verb that triggered the transaction. | `0` |
| `ims.tm.resource.adapter.transaction.lpar_name` | string | experimental The name of the LPAR that the transaction executed on. | `S0W1`; `ABCD` |
| `ims.tm.resource.adapter.transaction.sync_level` | long | experimental Indicates the synchronization level of the transaction. This only applies when the interaction verb is set to "SYNC\_SEND\_RECEIVE", "SYNC\_SEND", or "SYNC\_RECEIVE\_CALLOUT". This attribute applies to both conversational and non-conversational applications. It is used in conjuction with the ims.transaction.request.transaction.commit\_mode attribute. | `0` |

`ims.tm.resource.adapter.transaction.commit_mode` MUST be one of the following:

| Value | Description |
| --- | --- |
| `0` | The commit happens before sending the response. |
| `1` | The commit is deferred until the response has been sent and acknowledged. |

`ims.tm.resource.adapter.transaction.interaction_verb` MUST be one of the following:

| Value | Description |
| --- | --- |
| `0` | SYNC\_SEND |
| `1` | SYNC\_SEND\_RECEIVE |
| `3` | SYNC\_END\_CONVERSATION |
| `4` | SYNC\_RECEIVE\_ASYNCOUTPUT |
| `5` | SYNC\_RECEIVE\_ASYNCOUTPUT\_SINGLE\_NOWAIT |
| `6` | SYNC\_RECEIVE\_ASYNCOUTPUT\_SINGLE\_WAIT |
| `7` | SYNC\_RECEIVE\_CALLOUT |

`ims.tm.resource.adapter.transaction.sync_level` MUST be one of the following:

| Value | Description |
| --- | --- |
| `0` | There will be no synchronization. |
| `1` | Synchronization will be confirmed. |

## z/OS Connect

### Fields

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `zosconnect.api.description` | string | experimental The z/OS Connect API description. | `The API for the CICS catalog manager sample application.` |
| `zosconnect.api.name` | string | experimental The z/OS Connect API name. | `catalog` |
| `zosconnect.api.version` | string | experimental The z/OS Connect API version. | `1.0.0` |
| `zosconnect.request.body.size` | long | experimental The size of the request payload in bytes. | `234` |
| `zosconnect.request.id` | long | experimental The z/OS Connect request ID. | `2215` |
| `zosconnect.request.type` | string | experimental The type of the REST request. [1](#fn-17-1-def) | `ADMIN` |
| `zosconnect.response.body.size` | long | experimental The size of the response payload in bytes. | `125` |
| `zosconnect.service.description` | string | experimental The z/OS Connect service description. | `EDUCHAN service using the CICS Service Provider` |
| `zosconnect.service.name` | string | experimental The z/OS Connect service name. | `placeOrder` |
| `zosconnect.service.provider.name` | string | experimental The service provider name. | `CICS-1.0` |
| `zosconnect.service.version` | string | experimental The z/OS Connect service version. | `2.0` |
| `zosconnect.sor.identifier` | string | experimental The system of record identifier. The format differs depending on the SOR type. [2](#fn-17-2-def) | `localhost:8080` |
| `zosconnect.sor.reference` | string | experimental The system of record reference. | `cicsConn` |
| `zosconnect.sor.resource` | string | experimental Identifier for the resource invoked on the system of record. The format differs depending on the SOR type. [3](#fn-17-3-def) | `01,DFH0XCMN` |
| `zosconnect.sor.type` | string | experimental The system of record type. | `CICS` |

1

See [https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-datarequesttypeï»¿](https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-datarequesttype)

2

See [https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-data#SOR\_IDENTIFIERï»¿](https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-data#SOR_IDENTIFIER)

3

See [https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-data#SOR\_RESOURCEï»¿](https://www.ibm.com/docs/en/zos-connect/zosconnect/3.0?topic=spi-data#SOR_RESOURCE)

`zosconnect.request.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `ADMIN` | admin |
| `API` | api |
| `SERVICE` | service |
| `UNKNOWN` | unknown |

`zosconnect.sor.type` MUST be one of the following:

| Value | Description |
| --- | --- |
| `CICS` | cics |
| `IMS` | ims |
| `MQ` | mq |
| `REST` | rest |
| `WOLA` | wola |