---
title: Dynatrace web UI requirements
source: https://docs.dynatrace.com/managed/discover-dynatrace/get-started/dynatrace-ui/dynatrace-web-ui-requirements
scraped: 2026-05-12T12:05:49.920004
---

# Dynatrace web UI requirements

# Dynatrace web UI requirements

* Reference
* 2-min read
* Published Dec 19, 2025

Learn about the browser requirements to use Dynatrace.

## Supported browsers for Dynatrace UI

You can access the Dynatrace web UI using the following browsers.

| Browser | Versions |
| --- | --- |
| Microsoft Edge | Latest version (desktop and mobile) |
| Mozilla Firefox | Latest version (desktop) |
| Google Chrome | Latest version (desktop and mobile) |
| Safari | Latest version (OS X and iOS) |

### HTTPS requirements

As of June 30, 2019, you must enable the TLS 1.2 protocol in your browser to access the Dynatrace web UI. All modern browsers use TLS 1.2 by default.

After June 30, 2019, you won't be able to access the Dynatrace web UI using TLS 1.0 or TLS 1.1.

## Supported browsers for Session Replay

You can use any browser supported for Dynatrace web UI to play back the user sessions recorded with [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.").

## Supported browsers for Synthetic Monitoring

The supported browser for the Dynatrace Synthetic Recorder is Google Chrome (latest version, backwards compatible).

The browser used for executing browser monitors from public locations is listed on the Frequency and locations page when you create or edit a browser monitor.

See [Browser monitors in private locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") for browser versions you should install on a Synthetic-enabled ActiveGate running private browser monitors.