---
title: Lookup data in Grail
source: https://www.dynatrace.com/docs/platform/grail/lookup-data
scraped: 2026-02-20T21:16:34.103850
---

# Lookup data in Grail

# Lookup data in Grail

* Latest Dynatrace
* Explanation
* 4-min read
* Updated on Oct 07, 2025

Preview

Storing lookup data in [Grail](#grail) enables you to enrich your observability data with your custom data. You can upload your lookup data and join it with your existing data in Grail, such as `logs`, `events`, `spans`, or `metrics`.

![A diagram demonstrating how lookup data in Grail works. ](https://dt-cdn.net/images/diagram-spc-file-storage-in-grail-web-res-docs-1920-a87d521cbd.png)

Dynatrace stores lookup data as tabular files in the Resource Store, which is part of Grail. You can upload and manage your lookup data through the [Resource Store API](#lookup-files-rest-api). Once stored in Grail, you can use your lookup files to enrich your data within [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") queries.

You can define lookup tables in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting."), which currently provides the only user interface for creating and managing lookup tables without using the API. For instructions, see [Create and use lookup tables](/docs/secure/investigations/enhance-results#lookup "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").

## Lookup files

Static data, such as lookup tables, can be permanently stored in Grail as files. We reference files via a file path such as `/lookups/http_status_codes`. The following conventions apply to file paths, effectively organizing the files stored in Grail in a folder-like structure:

* Must contain only alphanumeric characters (`a-zA-Z0-9`), `-`, `_`, `.`, or `/`.
* Must start with `/`.
* Must end with `a-zA-Z0-9`.
* Must contain at least two `/` characters.
* Between any two consecutive `/` characters, there must be at least one alphanumeric character (`a-zA-Z0-9`).

The file path must start with `/lookups` when storing lookup data in Grail.

### Organize your files

The naming conventions allow you to organize your files like a regular file system. Using prefixes that mimic folders, such as in the file path `/lookups/my_team/allow_list`, makes it convenient to find and manage your lookup files stored in Grail.

## Permissions

To read lookup data stored in Grail, the policy bound to your user group must contain the following permission:

* `storage:files:read`

To upload lookup data to Grail via REST API or to delete it, the policy bound to your user group must contain the following permissions:

* `storage:files:write`
* `storage:files:delete`

All permissions can be restricted to specific paths or prefixes, giving users access to only a limited set of files. To learn more about setting up the required permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

When creating an OAuth token or platform token to make API calls from an API client, ensure these permissions are also configured for the token. The user linked to that OAuth token or platform token must have these permissions assigned.

Preview opt-in

Customers with [Dynatrace Platform Subscription (DPS)](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") can join the preview for lookup data in Grail. During the preview phase, the `storage:files` permissions are not included in the default Grail policies. You can opt into the preview program by manually adding permissions to access lookup files to your custom policies.

You can configure permissions with [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health."). To grant full access to all lookup data in `/lookups/`, you can create a policy (**Identity & access management** > **Policy management** >  **Create policy**) with the following statements:

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/";



ALLOW storage:files:write WHERE storage:file-path startsWith "/lookups/";



ALLOW storage:files:delete WHERE storage:file-path startsWith "/lookups/";
```

As another example, to give read-only access to all lookup data in `/lookups/`, you can use the following statement:

```
ALLOW storage:files:read WHERE storage:file-path startsWith "/lookups/";
```

## Limits

The following limits apply for storing lookup data in Grail:

| Limit | Value |
| --- | --- |
| Maximum number of files per environment | `100` (during preview) |
| Maximum file size | `100 MBÂ` |
| Maximum number of fields | `128` |

Upon completion of the preview and lifting the maximum number of files that can be stored per environment, the usage of lookup data in Grail can generate Events powered by Grail consumption.

## Manage lookup files

### Manage lookup files via REST API

You can manage your lookup files in Grail via the Resource Store API. Dynatrace offers API calls to:

* Upload your lookup data to Grail
* Delete your lookup data from Grail
* Test parsing the lookup data you want to upload with DPL

To update a file's content, you need to reupload the whole file and overwrite the existing file.

The Resource Store API uses the [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") to parse uploaded data and convert it into a tabular storage format. This provides complete flexibility regarding the uploaded data, supporting various text-based formats, including `CSV`, `JSONL`, or `XML`.

### Access API documentation

To access the Swagger API documentation for the Resource Store API and to start making API requests using Swagger:

1. Search for and select **Dynatrace API**.
2. In the **Select a definition** field, select **Grail - Resource Store**.
3. Optional Authenticate with your API token if you want to use Swagger to execute your requests. For details, see [Authentication](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context."). Select the **Try it out** button to interact with the API directly from the documentation.
4. Perform one of the following actions.

To do this

Go to **Lookup Data** and select this

Test parsing your to-be-uploaded lookup data without storing the result in Grail.

**POST/platform/storage/resource-store/v1/files/tabular/lookup:test-pattern**

Upload your lookup data and store it as a new tabular file in Grail or replace an existing one.

**POST/platform/storage/resource-store/v1/files/tabular/lookup:upload**

Delete the file from the Resource Store.

**POST/platform/storage/resource-store/v1/files:delete**

### Parse lookup data

The API provides the `/platform/storage/resource-store/v1/files/tabular/lookup:test-pattern` endpoint, which previews the uploaded results without persisting them as a file in Grail. The endpoint helps you define the DPL pattern that fits the format of your data.

The endpoint accepts input as `multipart/form-data` with a `content` part for the uploaded data and a `request` part for additional parameters. The only required parameter in the request part is the `parsePattern` parameter, which provides the DPL pattern to parse the uploaded text-based data. For more details, see the Swagger API documentation.

You can define any DPL pattern that matches your data. Every pattern match produces a record. The following example shows uploaded CSV data in the following format:

```
Code,Category,Message



100,informational,Continue



101,informational,Switching Protocols



...
```

The DPL pattern `INT:code ',' LD:category ',' LD:message` matches the content and produces a record with fields `code`, `category`, and `message` for every line except for the header line. You can use the `skippedRecords` parameter to exclude header lines where the pattern matches also the header lines.

With the same data in JSONL format you can use the `JSON:json` DPL pattern:

```
{"code": 100, "category": "informational", "message": "Continue"}



{"code": 101, "category": "informational", "message": "Switching Protocols"}



...
```

Suppose the specified DPL pattern results in a single record-type field. In that case, nested fields are extracted to the root level by default. This behavior is configurable via the `autoFlatten` parameter.

Suppose you also provide a `lookupField` parameter in the API request. In that case, the specified field will be used to deduplicate the result if identical values appear in multiple records.

The following example shows a curl command for interacting with the Resource Store API using a platform token to test a DPL pattern:

```
curl -X 'POST' \



'https://<environment>.apps.dynatrace.com/platform/storage/resource-store/v1/files/tabular/lookup:test-pattern' \



-H 'accept: */*' \



-H 'Content-Type: multipart/form-data' \



-H 'Authorization: Bearer <platformtoken>' \



-F 'request={



"parsePattern":"JSON:json",



"lookupField":"code"



}' \



-F 'content=@http_status_codes.jsonl'
```

The response includes the number of records that matched the pattern and a preview of up to 100 records.

### Store lookup data

The API provides the `/platform/storage/resource-store/v1/files/tabular/lookup:upload` endpoint, which allows you to upload and store your lookup data as a tabular file in Grail.

The endpoint accepts input as `multipart/form-data` with a `content` part for the uploaded data and a `request` part for additional parameters. In the content part, you can submit your data in a text-based format. For details, see [Parse lookup data](#parse-lookup-data). The required parameters in the request part are:

* `parsePattern` for providing the DPL pattern to parse the uploaded data
* `lookupField` for defining the extracted field with the identifier of the record
* `filePath` as the fully qualified file path of the tabular file to store the lookup data in Grail

Use the `displayName` and `description` parameters to include additional meta information. For more details, see the Swagger API documentation.

If you want to update the contents of a file, you need to reupload it. If the `filePath` already exists, use the `overwrite` parameter.

The following example shows a curl command for interacting with the Resource Store API using a platform token to store your lookup data:

```
curl -X 'POST' \



'https://<environment>.apps.dynatrace.com/platform/storage/resource-store/v1/files/tabular/lookup:upload' \



-H 'accept: */*' \



-H 'Content-Type: multipart/form-data' \



-H 'Authorization: Bearer <platformtoken>' \



-F 'request={



"parsePattern":"JSON:json",



"lookupField":"code",



"filePath":"/lookups/http_status_codes",



"displayName":"My lookup data",



"description":"Description of my lookup data"



}' \



-F 'content=@http_status_codes.jsonl'
```

### Delete lookup data

You can use the `/platform/storage/resource-store/v1/files:delete` endpoint to delete files that are no longer needed. The only required parameter is the `filePath` parameter, referencing the file to be deleted. Note that deleting a file is irreversible.

The following example shows a curl command for interacting with the Resource Store API using a platform token to delete an existing lookup file:

```
curl -X 'POST' \



'https://<environment>.apps.dynatrace.com/platform/storage/resource-store/v1/files:delete' \



-H 'accept: */*' \



-H 'Content-Type: application/json' \



-H 'Authorization: Bearer <platformtoken>' \



-d '{"filePath": "/lookups/http_status_codes"}'
```

### Manage lookup files with DQL

With DQL, you can fetch the `dt.system.files` table to get a list of all accessible files stored in Grail:

```
fetch dt.system.files
```

If you want to search for specific files, you can add the [search](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#search "DQL filter and search commands") or [filter](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filter "DQL filter and search commands") commands to the above example. The autocomplete suggestions within the DQL Code Editor will also help you find your files.

Use the [load](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#load "DQL data source commands") command if you want to inspect the contents of a file:

```
load "/lookups/http_status_codes"
```

## Enrich your data

You can use the [load](/docs/platform/grail/dynatrace-query-language/commands/data-source-commands#load "DQL data source commands") command to retrieve the tabular data from your lookup files in DQL and combine it with commands such as [lookup](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#lookup "DQL correlation and join commands") or [join](/docs/platform/grail/dynatrace-query-language/commands/correlation-and-join-commands#join "DQL correlation and join commands") to add additional context to your observability data:

```
fetch spans



| lookup [ load "/lookups/http_status_codes" ],



Â  Â  sourcefield: http.response.status_code,



Â  Â  lookupField: code
```