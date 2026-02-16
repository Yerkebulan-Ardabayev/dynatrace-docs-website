# Dynatrace Documentation: whats-new/edgeconnect

Generated: 2026-02-16

Files combined: 5

---


## Source: edgeconnect-release-notes-1-330-2.md


---
title: EdgeConnect release notes version 1.330.2
source: https://www.dynatrace.com/docs/whats-new/edgeconnect/edgeconnect-release-notes-1-330-2
scraped: 2026-02-15T21:22:19.060661
---

# EdgeConnect release notes version 1.330.2

# EdgeConnect release notes version 1.330.2

* Latest Dynatrace
* Release notes
* Published Jan 28, 2025

Release date: Jan 27, 2025

## New features and enhancements

* EdgeConnect now supports an increased request timeout of 120 seconds.


---


## Source: edgeconnect-release-notes-1-416-14.md


---
title: EdgeConnect release notes version 1.416.14
source: https://www.dynatrace.com/docs/whats-new/edgeconnect/edgeconnect-release-notes-1-416-14
scraped: 2026-02-15T21:22:20.429616
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


---


## Source: edgeconnect-release-notes-1-473-0.md


---
title: EdgeConnect release notes version 1.473.0
source: https://www.dynatrace.com/docs/whats-new/edgeconnect/edgeconnect-release-notes-1-473-0
scraped: 2026-02-15T21:22:13.527805
---

# EdgeConnect release notes version 1.473.0

# EdgeConnect release notes version 1.473.0

* Latest Dynatrace
* Release notes
* Published Jul 15, 2025

Release date: Jun 18, 2025

## New features and enhancements

* EdgeConnect now includes a `Software Bill of Materials (SBOM)` for supply chain transparency. This helps you to identify the origin of potential security vulnerabilities within the EdgeConnect image.


---


## Source: edgeconnect-release-notes-1-473-2.md


---
title: EdgeConnect release notes version 1.473.2
source: https://www.dynatrace.com/docs/whats-new/edgeconnect/edgeconnect-release-notes-1-473-2
scraped: 2026-02-15T21:22:16.015134
---

# EdgeConnect release notes version 1.473.2

# EdgeConnect release notes version 1.473.2

* Latest Dynatrace
* Release notes
* Published Jan 15, 2026

Release date: Jan 15, 2026

## Resolved issues

* EdgeConnect now properly handles timeouts on initial authentication with the platform.


---


## Source: edgeconnect-release-notes-1-473-5.md


---
title: EdgeConnect release notes version 1.473.5
source: https://www.dynatrace.com/docs/whats-new/edgeconnect/edgeconnect-release-notes-1-473-5
scraped: 2026-02-15T21:22:14.761180
---

# EdgeConnect release notes version 1.473.5

# EdgeConnect release notes version 1.473.5

* Latest Dynatrace
* Release notes
* Published Jan 26, 2026

Release date: Jan 26, 2026

## Resolved issues

* EdgeConnect now properly sets the HTTP `Host` header when connecting to the proxy.


---
