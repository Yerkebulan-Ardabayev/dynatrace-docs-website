---
title: "Dynatrace MCP server"
source: https://docs.dynatrace.com/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp
updated: 2026-02-09
---

# Dynatrace MCP server

# Dynatrace MCP server

* Latest Dynatrace
* Overview
* 5-min read
* Updated on Jan 28, 2026

This page provides an overview of the Dynatrace Model Context Protocol (MCP) server and how you can use it to maximize your efficiency and quickly complete a variety of tasks, such as generating, executing or explaining a DQL query, with the help of an MCP client (external agent).

Currently, the MCP server supports the following use cases:

* Generating a DQL query with generative AI
* Explaining a DQL query with generative AI
* Using generative AI to quickly answer product-related questions
* Running a generated DQL query
* Investigating problems and vulnerabilities
* Analyzing Kubernetes events
* Forecasting timeseries data

## What is MCP?

The Dynatrace MCP server is a server that hosts tools that can be used to fulfill specific use cases. An external agent, such as GitHub CoPilot VS Code integration or Claude desktop, can then make use of the MCP server and its tools to execute a series of calls when fulfilling a user request.

To learn more about MCP servers, see [What is the Model Context Protocol (MCP)?ï»¿](https://modelcontextprotocol.io/docs/getting-started/intro).

## Server and server tools

Dynatrace provides a `dynatrace-mcp` server that hosts a collection of tools designed for external connections. It currently hosts the following tools:

Tool name

Description

State

Grail Query Agent

* Allows you to generate a DQL query based on a natural language prompt. This tool doesn't execute the query.
* Both the user and the token require the `davis-copilot:nl2dql:execute` permission.

Preview

DQL Explanation Agent

* Provides natural language explanation of a DQL query.
* Both the user and the token require the `davis-copilot:dql2nl:execute` permission.

Preview

Help Agent

* Allows you to ask about general Dynatrace information (for example, "How to create workflows?" or "What is a custom alert?").
* Both the user and the token require the `davis-copilot:conversations:execute` permission.

Preview

Data Analysis Agent

* Executes any valid DQL query and returns the raw result that can be used by the agent.
* Limits Grail responses to 1000 records.
* Both the user and the token require the `storage:buckets:read` permission.
* You can include additional permissions to allow DQL access to other data. For more information, see [Grail permissions table](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table "Find out how to assign permissions to buckets and tables in Grail.").

Data Analysis Agent tool respects permission scopes and won't access any data outside of the permissions you provided.

Public

Root Cause Agent

* Returns an overview list of all problems on the tenant.
* Can return only active or closed problems based on your request.
* Both the user and the token require `storage:buckets:read` and `storage:events:read` permissions.

Public

.css-b62m3t-container{position:relative;box-sizing:border-box;}

.css-7pg0cj-a11yText{z-index:9999;border:0;clip:rect(1px, 1px, 1px, 1px);height:1px;width:1px;position:absolute;overflow:hidden;padding:0;white-space:nowrap;}

.css-1hac4vs-dummyInput{background:0;border:0;caret-color:transparent;font-size:inherit;grid-area:1/1/2/3;outline:0;padding:0;width:1px;color:transparent;left:-100px;opacity:0;position:relative;-webkit-transform:scale(.01);-moz-transform:scale(.01);-ms-transform:scale(.01);transform:scale(.01);}.css-14oxtc6{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;display:grid;-webkit-flex:1;-ms-flex:1;flex:1;-webkit-box-flex-wrap:wrap;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-overflow-scrolling:touch;position:relative;overflow:hidden;box-sizing:border-box;}

.css-w54w9q-singleValue{grid-area:1/1/2/3;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;box-sizing:border-box;}

5

rows per page

Page

.css-b62m3t-container{position:relative;box-sizing:border-box;}

.css-7pg0cj-a11yText{z-index:9999;border:0;clip:rect(1px, 1px, 1px, 1px);height:1px;width:1px;position:absolute;overflow:hidden;padding:0;white-space:nowrap;}

.css-1hac4vs-dummyInput{background:0;border:0;caret-color:transparent;font-size:inherit;grid-area:1/1/2/3;outline:0;padding:0;width:1px;color:transparent;left:-100px;opacity:0;position:relative;-webkit-transform:scale(.01);-moz-transform:scale(.01);-ms-transform:scale(.01);transform:scale(.01);}.css-14oxtc6{-webkit-align-items:center;-webkit-box-align:center;-ms-flex-align:center;align-items:center;display:grid;-webkit-flex:1;-ms-flex:1;flex:1;-webkit-box-flex-wrap:wrap;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;-webkit-overflow-scrolling:touch;position:relative;overflow:hidden;box-sizing:border-box;}

.css-w54w9q-singleValue{grid-area:1/1/2/3;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;box-sizing:border-box;}

1

of 1

## Connect to the MCP server

You can connect to an MCP server via a URL by using the following address:

```
https://{tenant-name}.apps.dynatrace.com/platform-reserved/mcp-gateway/v0.1/servers/dynatrace-mcp/mcp
```

* You need to provide a bearer token in the authorization header for the request to work. You can obtain the token from a Platform Token or from an OAuth client. Dynatrace doesn't support using OAuth client directly when connecting to the MCP server, so you must generate a token from the client. To learn more about generating and authorizing a bearer token, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").
* The token you created will only work within the scope of your user permissions. To use the Dynatrace MCP server, you need to have all of the necessary permissions. For more information, see [Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens#my-platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.") or [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients."), depending on the type of the token you use.

In addition to the tool permissions mentioned in [Server and server tools](#server), both the user and the token must have the following permissions to access and invoke server tools:

* `mcp-gateway:servers:invoke`
* `mcp-gateway:servers:read`

You can setup connections by using VS Code and its chat integration, or by using any other tool of your choice.

## Related topics

* [Dynatrace Intelligence generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.")
* [Dynatrace Assist](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot "Ask questions using natural language and get quick answers from Dynatrace Assist, your generative AI assistant.")
