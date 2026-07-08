---
title: Problems API v1
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems
---

# Problems API v1

# Problems API v1

* Reference
* Updated on Jun 13, 2022
* Deprecated

This API is deprecated. Use the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.") instead.

The **Problems** API delivers details about [problems](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.") that Dynatrace detects within your environment. A single problem typically contains summary information, impact analysis, and a list of any events that are correlated with the problem.

[### List problem count

Find out how many open problems are there.](/managed/dynatrace-api/environment-api/problems/problems/get-status "View the status of a problem via Problems v1 API.")[### Fetch the problem feed

Gain high-level details of open problems.](/managed/dynatrace-api/environment-api/problems/problems/get-feed "Fetch the list of problems via Problems v1 API.")[### Get the problem details

When you find a problem you want to investigate, fetch details about it.](/managed/dynatrace-api/environment-api/problems/problems/get-details "View details of a problem via Problems v1 API.")[### Close problem

When a problem is not a concern anymore, close it and add a closing comment in single request.](/managed/dynatrace-api/environment-api/problems/problems/post-close "Close a problem and add a closing comment via Problems v1 API.")

[### List comments

View all comments to a problem.](/managed/dynatrace-api/environment-api/problems/comments/get-all "View all comments to a problem via Problems v1 API.")[### Post comment

Post a comment to a specified problem](/managed/dynatrace-api/environment-api/problems/comments/post-comment "Post a comment to a problem via Problems v1 API.")

[### Edit comment

Edit a comment to a specified problem.](/managed/dynatrace-api/environment-api/problems/comments/put-comment "Edit a comment to a problem via Problems v1 API.")[### Delete comment

Delete a comment from a specified problem](/managed/dynatrace-api/environment-api/problems/comments/del-comment "Delete a comment to a problem via Problems v1 API.")

## Related topics

* [Davis® AI](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.")