---
title: "User sessions API"
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/user-sessions
updated: 2026-02-09
---

# User sessions API

# User sessions API

* Reference
* Updated on May 02, 2022

The **User Sessions** API enables you to obtain data about user sessions. The API uses [User Sessions Query Language (USQL)](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") to query the required data. Both calls return the same data, differing only in how it's represented.

[### GET table

The GET table request executes a USQL query and returns results as a table structure of the requested columns.](/managed/dynatrace-api/environment-api/rum/user-sessions/table "View user sessions data in a table form via the Dynatrace API.")[### GET tree

The GET tree request executes a USQL query and returns results as a tree structure of the requested columnsâa flat list containing the requested columns.](/managed/dynatrace-api/environment-api/rum/user-sessions/tree "View user sessions data in a tree form via the Dynatrace API.")[### User session structure

Learn the structure of a user session that contains all possible fields.](/managed/dynatrace-api/environment-api/rum/user-sessions/user-session-structure "Learn the structure of a user session in the Dynatrace User Session Query language API.")

## Related topics

* [Custom queries, segmentation, and aggregation of session data](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.")
