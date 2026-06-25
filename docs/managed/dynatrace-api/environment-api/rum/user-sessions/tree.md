---
title: User sessions API - GET Tree
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/user-sessions/tree
scraped: 2026-05-12T12:00:06.854572
---

# User sessions API - GET Tree

# User sessions API - GET Tree

* Reference
* Updated on May 02, 2022

Executes a USQL query and returns results as a tree structure of the requested columnsâa flat list containing the requested columns.

To get a proper tree structure, you need to specify grouping in the query. The fields used in the `GROUP BY` clause form the "branches" of the tree, each holding "leaves"âselected fields that have not been used for grouping.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/userSessionQueryLanguage/tree` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/userSessionQueryLanguage/tree` |

## Authentication

To execute this request, you need an access token with `DTAQLAccess` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| query | string | The user session query to be executed. See [USQL documentation pageï»¿](https://dt-url.net/dtusql) for syntax details.  You can find the available columns of the **usersession** table in the `UserSession` object.  Here is an example of the query: `SELECT country, city, COUNT(*) FROM usersession GROUP BY country, city`. | query | Required |
| startTimestamp | integer | The start timestamp of the query, in UTC milliseconds.  If not set or set as `0`, 2 hours behind the current time is used.  If the exact times are important, set the timeframe in the query itself (**query** parameter). | query | Optional |
| endTimestamp | integer | The end timestamp of the query, in UTC milliseconds.  If not set or set as `0`, the current timestamp is used.  If the exact times are important, set the timeframe in the query itself (**query** parameter). | query | Optional |
| offsetUTC | integer | Optional offset of local time to UTC time in minutes. Offset will be applied to Date fields encountered in the query.  Can be positive or negative. E.g. if the local time is UTC+02:00, the timeOffset is 120. If it is UTC-05:00, timeOffset is -300. | query | Optional |
| addDeepLinkFields | boolean | Add (`true`) to enable deep linking of additional fields in the query.  If not set, then `false` is used | query | Optional |
| explain | boolean | Add (`true`) or don't add (`false`) some additional information about the result to the response.  It helps to understand the query and how the result was calculated.  If not set, then `false` is used | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **199** | [UserSession](#openapi-definition-UserSession) | The data structure of the user session. This response code is never returned. |
| **200** | [UsqlResultAsTree](#openapi-definition-UsqlResultAsTree) | Success. The response contains the result of the query. |
| **400** | - | Failed. The query is missing. |
| **404** | - | Failed. The query is invalid. See the response body for more information. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `UsqlResultAsTree` object

The user session query result as a tree.

| Element | Type | Description |
| --- | --- | --- |
| additionalColumnNames | string[] | A list of columns in the additionalValues table.  Only present if the endpoint was called with `deepLinkFields=true` parameter. |
| additionalValues | array[] | A list of data rows.  Each array element represents a row in the table of additionally linked fields.  The size of each data row and the order of the elements correspond to the **additionalColumnNames** content.  Only present if the endpoint was called with `deepLinkFields=true` parameter. |
| branchNames | string[] | A list of branches of the tree.  Typically, these are fields from the `SELECT` clause, that have been used in the `GROUP BY` clause. |
| explanations | string[] | Additional information about the query and the result, that helps to understand the query and how the result was calculated.  Only appears when the **explain** parameter is set to `true`.  Example: The number of results was limited to the default of 50. Use the `LIMIT` clause to increase or decrease this limit. |
| extrapolationLevel | integer | The extrapolation level of the result.  To improve performance, some results may be calculated from a subset of actual data. The extrapolation level indicates the share of actual data in the result.  The number is the denominator of a fraction and indicates the amount of actual data. The value `1` means that the result contains only the actual data. The value `4` means that result is calculated using 1/4 of the actual data.  If you need the analysis to be based on the actual data, reduce the timeframe of your query. For example, in case of extrapolation level of `4`, try to use 1/4 of the original timeframe. |
| leafNames | string[] | A list of leaves on each tree branch.  Typically, these are fields from the `SELECT` clause, that have not been used in the `GROUP BY` clause. |
| values | string | The user session query result as a tree. |

#### The `AnyValue` object

A schema representing an arbitrary value type.

### Response body JSON models

```
{



"branchNames": [



"country",



"city"



],



"extrapolationLevel": 1,



"leafNames": [



"avg(duration)",



"max(duration)"



],



"values": {



"Austria": {



"Klagenfurt": [



"65996.75",



"129940"



],



"Linz": [



"57360.86",



"222912"



]



},



"Poland": {



"Gdansk": [



"22482.2",



"351263"



]



}



}



}
```

## Example

In this example, the request executes the `SELECT country, city, avg(duration), max(duration) FROM usersession GROUP BY country, city` query.

The API token is passed in the **Authorization** header.

The result is truncated to 4 entries.

Since the timeframe is not specified, the query uses the default timeframe of **2 hours** back from the current time.

In the resulting structure, all the values are grouped initially by the **country**, with each object of the **values** array representing a country. These objects each hold arrays of **average** and **maximal** durations of user sessions for each **city**.

The **extrapolationLevel** of 4 indicates that the values are extrapolated from 1/4th of the actual data.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/userSessionQueryLanguage/api/v1/userSessionQueryLanguage/tree?query=select%20country,%20city,%20avg%28duration%29,%20max%28duration%29%20from%20usersession%20group%20by%20country,%20city' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/userSessionQueryLanguage/api/v1/userSessionQueryLanguage/tree?query=select%20country,%20city,%20avg%28duration%29,%20max%28duration%29%20from%20usersession%20group%20by%20country,%20city
```

#### Response body

```
{



"extrapolationLevel": 4,



"branchNames": [



"country",



"city"



],



"leafNames": [



"avg(duration)",



"max(duration)"



],



"values": {



"Austria": {



"Vienna": [



64423.908602150535,



557649



]



},



"United States": {



"Detroit": [



58984.49809402796,



504369



],



"Boston": [



53865.68464730291,



434636



]



},



"Poland": {



"GdaÅsk": [



31177.50773993808,



445353



]



}



}



}
```

#### Response code

200

## Related topics

* [Custom queries, segmentation, and aggregation of session data](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.")