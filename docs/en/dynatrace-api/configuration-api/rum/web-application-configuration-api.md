---
title: Web application configuration API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api
scraped: 2026-02-16T09:31:24.870224
---

# Web application configuration API

# Web application configuration API

* Reference
* Published Jan 24, 2019

The **Web application configuration** API enables you to manage configuration of [web applications](/docs/discover-dynatrace/get-started/glossary#app "Get acquainted with Dynatrace terminology.").

This API only supports web applications. For mobile and custom applications, see [Mobile and custom app API](/docs/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.").

[### List all

Get an overview of all web applications.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-all "List all web applications via the Dynatrace API.")[### View a web application

Get parameters of a web application by its ID.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/get-web-application "View parameters of a web application via the Dynatrace API.")

[### Create a web application

Create a new web application with the exact parameters you need.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/post-web-application "Create a web application via the Dynatrace API.")[### Edit a web application

Update an existing web application or create a new application with the specified ID.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/put-web-application "Update a web application via the Dynatrace API.")[### Delete a web application

Delete a web application you don't need anymore.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/web-application/del-web-application "Delete a web application via the Dynatrace API.")

Default application is pre-configured in your Dynatrace environment. By default all traffic goes to this application. After you configure your own [applications](/docs/discover-dynatrace/get-started/glossary#app "Get acquainted with Dynatrace terminology."), all the traffic, which doesn't fit to any of your applications, goes to the default one.

[### View configuration

Get the parameters of the default web application.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/get-configuration "View configuration of the default web application via the Dynatrace API.")[### Update configuration

Update the parameters of the default web application.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/default-application/put-configuration "Update configuration of the default web application via the Dynatrace API.")

### Check data privacy

View the data privacy parameters for

* [All applications](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-all-web-apps "View data privacy configuration of all applications via the Dynatrace API.")
* [A specific application](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-web-app "View data privacy configuration of an application via the Dynatrace API.")
* [The default application](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-default-app "View data privacy configuration of the default application via the Dynatrace API.")

### Update data privacy

View the data privacy parameters for

* [A specific application](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-web-app "Edit data privacy configuration of an application via the Dynatrace API.")
* [The default application](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-default-app "Edit data privacy configuration of the default application via the Dynatrace API.")

[### View key user actions

Get the list of key user actions in an application.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/get-configuration "View key user actions of a web application via the Dynatrace API.")[### Edit key user actions list

Mark a user action as the key action in an application.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/post-configuration "Add a key user action to a web application via the Dynatrace API.")[### Delete a key user action

Remove a user action from the list of key actions in an application.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/key-user-actions/del-configuration "Remove a key user action from a web application via the Dynatrace API.")

[### View error rules

Get an overview of error rules configuration.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/get-configuration "Read error rules of an application via the Dynatrace API.")[### Update error rules

Update configuration of configuration.](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api/error-rules/put-configuration "Update error rules of an application via the Dynatrace API.")