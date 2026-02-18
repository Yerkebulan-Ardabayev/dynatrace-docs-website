---
title: EdgeConnect release notes version 1.416.14
source: https://www.dynatrace.com/docs/whats-new/edgeconnect/edgeconnect-release-notes-1-416-14
scraped: 2026-02-18T21:28:42.469926
---

# EdgeConnect release notes version 1.416.14

# EdgeConnect release notes version 1.416.14

* Latest Dynatrace
* Release notes
* Published May 13, 2025

Release date: Apr 29, 2025

## New features and enhancements

* EdgeConnect now logs a warning and hints to the documentation when your configured OAuth resource does not match the format `urn:dtenvironment:<tenant>`.

* EdgeConnect now is more verbose on HTTP errors to help identify root causes of failed HTTP requests.

* After losing its connection to the Dynatrace platform, EdgeConnect will now shut down after 1 minute in case of multiple failed reconnection attempts. This shutdown behavior will help you quickly identify issues with connecting to the Dynatrace platform.

## Changes in this version

EdgeConnect no longer follows HTTP redirects automatically. Your redirected HTTP(S) requests are now properly handled in the JavaScript Runtime instead.

This change allows you to

* Control request behavior with redirection flags `follow`, `error`, and `manual` in your JavaScript code using the `fetch` API.
* Prevent redirection to unallowed HTTP endpoints per EdgeConnect configuration.
* Route each redirect to a dedicated EdgeConnect instance as configured via the **EdgeConnect Management** app.

If you use `node:http(s)` in your JavaScript code, keep in mind that redirect handling needs to be handled manually now.