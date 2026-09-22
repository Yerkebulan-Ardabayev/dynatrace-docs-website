---
title: Configure custom TLS certificates for SQL Extension Executor pods
source: https://docs.dynatrace.com/managed/ingest-from/extensions/kubernetes/tls-certificates
---

# Configure custom TLS certificates for SQL Extension Executor pods

# Configure custom TLS certificates for SQL Extension Executor pods

* How-to guide
* 3-min read
* Published Aug 25, 2026

You can provide TLS certificates to the SQL Extension Executor pod via:

* Custom individual certificate files: The SQL Extension Executor reads them from a mounted directory.
* Custom pre-built PKCS12 truststore: Provide your own truststore with certificates already loaded.

You can also combine both approaches. When both individual certificates and a truststore are provided, the SQL Extension Executor imports the certificate files on top of the provided truststore.

If you need to import more than ten custom certificates, we recommend using a pre-built truststore instead of mounting individual certificate files. Certificate manipulation at startup can be time-consuming and a pre-built truststore avoids this overhead entirely.

## Mount custom certificates

The SQL Extension Executor reads all valid, non-expired certificates found in `/app/user/ssl-certs`. Any Kubernetes volume type that exposes files at that path works. Common options are Kubernetes Secrets and PersistentVolumes.

The SQL Extension Executor supports certificate bundles in PEM format. In such cases, each certificate within the bundle is imported separately.

```
spec:



extensions:



databases:



- id: default



replicas: 1



volumeMounts:



- mountPath: /app/user/ssl-certs



name: user-ssl-certs



volumes:



- name: user-ssl-certs



secret:



secretName: user-ssl-certs
```

## Mount a custom truststore

If you already manage a PKCS12 truststore, you can mount it directly. To create a new one, follow the same process as described for [ActiveGate-based SQL monitoring](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring#ssl "JDBC extensions in the Extensions framework.") and mount the file in the location listed below.

* Format: PKCS12
* Password: `sqlds_truststore`
* Filename: `sqlds_truststore`
* Mount path: `/app/user/truststore/`

```
spec:



extensions:



databases:



- id: default



replicas: 1



volumeMounts:



- mountPath: /app/user/truststore/



name: custom-truststore



readOnly: true



volumes:



- name: custom-truststore



secret:



secretName: custom-truststore
```

## Automatic certificate reload

When mounted certificate files or the truststore change, the SQL Extension Executor automatically restarts to apply the updated certificates. No manual action is required, and monitoring resumes automatically afterward.

The restart is typically triggered within five minutes of a detected change. Logs for the affected extension configuration show the scheduled time. Brief metric gaps may occur in the meantime.

Automatic certificate reload requires Kubernetes to update the mounted files when the source (such as a Secret) changes. Some mount configurations prevent this. For example, Kubernetes doesn't update volumes mounted using `subPath`, which means they won't trigger a reload.