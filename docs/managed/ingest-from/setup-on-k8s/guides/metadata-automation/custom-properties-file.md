---
title: Add a custom properties file
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file
---

# Add a custom properties file

# Add a custom properties file

* 1-min read
* Updated on Jan 27, 2026

As part of getting started with Kubernetes platform monitoring, you might want to add a custom properties file.

You can add a custom properties file by providing it as a value or by referencing it from a secret.

## Add the custom properties file as a value

To add the custom properties file as a value, see the example below.

```
customProperties:



value: |



[kubernetes_monitoring]



...
```

## Reference the custom properties file from a secret

1. Create a secret with the following content.

   The secret must be in the same namespace as the Dynatrace Operator (for example,`dynatrace`).

   The content of the secret has to be `base64` encoded in order to work.

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: <customproperties-secret>



   namespace: dynatrace



   data:



   customProperties: <base64 encoded properties>
   ```
2. Add the secret to the custom properties.

   ```
   customProperties:



   valueFrom: <customproperties-secret>
   ```