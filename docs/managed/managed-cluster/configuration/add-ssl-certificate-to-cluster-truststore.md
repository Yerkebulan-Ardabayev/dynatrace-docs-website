---
title: Add certificate to truststore
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/add-ssl-certificate-to-cluster-truststore
---

# Add certificate to truststore

# Add certificate to truststore

* How-to guide
* 1-min read
* Updated on Jun 18, 2026

Add an SSL certificate to the Managed Cluster truststore if the Managed Cluster can't verify SSL connections. Adding a certificate is typically required when sending email or webhook notifications with a self-signed certificate.

## Check for certificate rejection

If a Managed Cluster has trouble sending notifications, look for any [files in the log directory](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.") of your Managed Cluster node installation that have the name pattern `Server.*.*.log`.

If any files with this naming pattern exist in the log folder, search through those log files for the following entry:

```
sun.security.validator.ValidatorException: PKIX path building failed:



sun.security.provider.certpath.SunCertPathBuilderException
```

Certificate rejection typically occurs when the certificate provided by the notification receiver isn't accepted by the Managed Cluster node. The reason for this is usually that the certificate isn't trusted.

## Add certificate to truststore

Use the PEM certificate (`.crt`, `.pem`, `.cer`) and run the reconfiguration script on every node in the Managed Cluster using the `--update-cert` and `--network-proxy-cert-file` parameters. Use the `nohup` command to prevent interruption of script execution (such as session disconnect) during important operations.

```
nohup <PRODUCT_PATH>/installer/reconfigure.sh --update-cert --network-proxy-cert-file <cert_file>.cer &
```

Replace `<PRODUCT_PATH>` with the Dynatrace Managed installation path (default: `/opt/dynatrace-managed`) and `<cert_file>` with the name of your certificate file.

Proxy parameter

The `--network-proxy-cert-file` parameter supplies a proxy certificate for Dynatrace Managed, but you can also use it to supply the certificate for any secure connection to the Managed Cluster.