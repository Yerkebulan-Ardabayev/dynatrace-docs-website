---
title: Web application configuration API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api
scraped: 2026-03-06T21:35:47.089943
---

# Web application configuration API


* Reference
* Published Jan 24, 2019

The **Web application configuration** API enables you to manage configuration of web applications.

This API only supports web applications. For mobile and custom applications, see Mobile and custom app API.

### List all

Get an overview of all web applications.### View a web application

Get parameters of a web application by its ID.

### Create a web application

Create a new web application with the exact parameters you need.### Edit a web application

Update an existing web application or create a new application with the specified ID.### Delete a web application

Delete a web application you don't need anymore.

Default application is pre-configured in your Dynatrace environment. By default all traffic goes to this application. After you configure your own applications, all the traffic, which doesn't fit to any of your applications, goes to the default one.

### View configuration

Get the parameters of the default web application.### Update configuration

Update the parameters of the default web application.

### Check data privacy

View the data privacy parameters for

* All applications
* A specific application
* The default application

### Update data privacy

View the data privacy parameters for

* A specific application
* The default application

### View key user actions

Get the list of key user actions in an application.### Edit key user actions list

Mark a user action as the key action in an application.### Delete a key user action

Remove a user action from the list of key actions in an application.

### View error rules

Get an overview of error rules configuration.### Update error rules

Update configuration of configuration.