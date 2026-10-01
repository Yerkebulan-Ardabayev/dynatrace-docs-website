---
title: Configure init-container user and group identity
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/init-container-security-context
---

# Configure init-container user and group identity

# Configure init-container user and group identity

* 2-min read
* Updated on Sep 09, 2026

Dynatrace Operator version 1.11.0+

When Dynatrace Operator injects an init-container into your pods, it configures the security context based on your pod or container settings. You can use annotations to explicitly configure the `runAsUser` and `runAsGroup` values for the Dynatrace Operator injected init-container.

Apply these annotations at the pod level:

* `init-container.dynatrace.com/securityContext.runAsUser`: Configures the `runAsUser` value for the init-container. Must be a positive integer. If not provided or invalid, the default behavior applies.
* `init-container.dynatrace.com/securityContext.runAsGroup`: Configures the `runAsGroup` value for the init-container. Must be a positive integer. If not provided or invalid, the default behavior applies.

## Default behavior

When these annotations are not provided, the init-container applies the following logic:

* If `runAsUser` or `runAsGroup` is configured on the first user container or at the pod level, the init-container copies those settings
* If nothing is configured on the user container or pod level AND you are running on OpenShift, the init-container inherits the values set by the restricted-v2 Security Context Constraint (SCC)
* Otherwise, the init-container defaults to `runAsUser: 1001` and `runAsGroup: 1001`

## Example

```
apiVersion: v1



kind: Pod



metadata:



name: my-app



annotations:



init-container.dynatrace.com/securityContext.runAsUser: "1000"



init-container.dynatrace.com/securityContext.runAsGroup: "1000"



spec:



containers:



- name: app



image: my-app:latest
```