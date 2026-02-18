---
title: Set up host name determination in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-host-name-determination
scraped: 2026-02-18T05:48:17.128737
---

# Set up host name determination in the New RUM Experience

# Set up host name determination in the New RUM Experience

* Latest Dynatrace
* How-to guide
* Updated on Jan 08, 2026

The host portion of the URL is essential for two specific RUM featuresâapplying [frontend detection rules](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience.") and automatically detecting the RUM cookie domain. However, in environments with components like reverse proxies or load balancers, the original host may be rewritten before reaching an instrumented tier using a [technology with RUM support](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."). To resolve this, OneAgent provides a host name determination feature.

## Add a host name determination header

Components like reverse proxies and load balancers can be configured to forward the original host information to the backend in a request header. Common headers for this purpose include [`X-Forwarded-Host`ï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Host) and the standardized [`Forwarded`ï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Forwarded) header.
OneAgent can retrieve the original host from one of these headers or from any proprietary header that follows the same format as `X-Forwarded-Host`: `<host>` for default ports or `<host>:<port>` otherwise. A comma-separated list of such entries is also supported, with the assumption that the first entry represents the original host name.

Some components add one of these headers by default. If yours does not, you need to configure it to include such a header to use the host name determination feature.

## Configure host name determination

OneAgent uses a list of request headers to determine the host name. Headers in the list are processed in order, with those at the top taking precedence. As soon as OneAgent finds a matching header on the request, it stops evaluating the remaining headers. After confirming that your uninstrumented component adds a suitable header, you might need to add that header to the list.

To configure the headers used for host name determination

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Real User Monitoring** > **Frontend** > **Host name determination**.
2. If the header added by your component is missing from the list, select **Add HTTP header** and enter the header name.
3. You can reorder entries by selecting and holding ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") next to the header name, then dragging it up or down. Ensure the new entry appears above the `Host` header, which is included in every HTTP/1.1 request.

## Example

If the original host name requested by the browser is `www.example.com` and your uninstrumented reverse proxy forwards the request to an internal host such as `backend.com`, the original host information is lost. In this case, the proxy must add a header that preserves the original host name to allow OneAgent to determine the original host, as illustrated in the diagram below.

![Passing the original host information in the X-Forwarded-Host header](https://dt-cdn.net/images/host-name-determination-1142-4fea9931ba.png)

## Related topics

* [Set up an auto-injected frontend in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience.")