---
title: OneAgent security
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/oneagent-security
scraped: 2026-05-12T12:25:36.112555
---

# OneAgent security

# OneAgent security

* 1-min read
* Published Apr 25, 2023

## Trusted root certificates for OneAgent

OneAgent is shipped with trusted Dynatrace SSL certificates, which are used to verify that OneAgent connects successfully to Dynatrace Server or ActiveGate.

If your environment uses a proxy with a custom certificate (thereby requiring an update to the remote server's SSL certificate) or you have an Environment ActiveGate with its own custom certificate, you need to add additional certificates to OneAgent.

### ActiveGate with custom certificate

1. Identify the SSL certificate that your ActiveGate uses.
2. Obtain the CA certificate (along with any intermediate certificates if they are in place).
3. Save the CA certificates as `custom.pem`.
4. Place the `custom.pem` file in the appropriate directory based on your operating system:

   **Linux**: `/var/lib/dynatrace/oneagent/agent/customkeys`

   **Windows**: `%PROGRAMDATA%\dynatrace\oneagent\agent\customkeys`

Make sure the `custom.pem` file contains the ActiveGate's certificate along with any intermediate certificates as required.

### Proxy with custom certificate

1. Identify the SSL certificate that your proxy uses.
2. Obtain the CA certificate (along with any intermediate certificates if they are in place).
3. Save the CA certificates as `custom-proxy.pem`.
4. Place the `custom-proxy.pem` file in the appropriate directory based on your operating system:

   **Linux**: `/var/lib/dynatrace/oneagent/agent/customkeys`

   **Windows**: `%PROGRAMDATA%\dynatrace\oneagent\agent\customkeys`

Make sure the `custom-proxy.pem` file contains the proxy's certificate along with any intermediate certificates as required.

### ActiveGate and proxy with custom certificate

If your setup involves both an HTTPS proxy with a custom certificate and an Environment ActiveGate with its own custom certificate, you need to provide a `custom.pem` file and a `custom-proxy.pem` file.