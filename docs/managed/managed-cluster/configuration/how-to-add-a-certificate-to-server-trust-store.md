---
title: Add an SSL certificate to Dynatrace Managed cluster TrustStore
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/how-to-add-a-certificate-to-server-trust-store
scraped: 2026-05-12T11:53:05.491075
---

# Add an SSL certificate to Dynatrace Managed cluster TrustStore

# Add an SSL certificate to Dynatrace Managed cluster TrustStore

* Published Jan 08, 2018

There may be times when you need to manually add an SSL certificate to the Dynatrace Managed cluster TrustStores, for example if your cluster refuses to accept the SSL certificate when sending emails or WebHook notifications. This typically happens when a self-signed certificate is used.

## How to know when your cluster isn't accepting certificates

If a cluster is having trouble sending notifications, look for any [files in the log directory](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.") of your cluster node installation that have the name pattern `Server.*.*.log`.

If any files with this naming pattern exist in the log folder, search through those log files for the following entry:

```
sun.security.validator.ValidatorException: PKIX path building failed:



sun.security.provider.certpath.SunCertPathBuilderException
```

Log entries such as the example above indicate that the certificate provided by the notification receiver wasn't accepted by the cluster node. The reason for this is usually that the certificate isn't trusted.

## Add a custom certificate to the cluster node TrustStore

Use the PEM certificate (`.crt`, `.pem`, `.cer`) and execute the reconfiguration script on every node in the cluster using the `--update-cert` and `--network-proxy-cert-file` parameters. Use the `nohup` command to prevent interruption of script execution (such as session disconnect) during important operations.

`nohup <PRODUCT_PATH>/installer/reconfigure.sh --update-cert --network-proxy-cert-file <cert_file>.cer &`

Proxy parameter

The `--network-proxy-cert-file` parameter is designed to provide a proxy certificate for Managed but, it can also be used to provide the certificate for any secure connection to Managed cluster.