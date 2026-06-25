---
title: Token rotation
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/token-rotation
scraped: 2026-05-12T12:14:24.881177
---

# Token rotation

# Token rotation

* Published Nov 03, 2025

Dynatrace environments provide an [API](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Rotate Dynatrace tenant tokens.") that enables tenant token rotation. When triggered, the API generates new tokens for OneAgents and ActiveGates.

After a tenant token rotation:

* Dynatrace Operator automatically detects and applies the new token.
* ActiveGate instances are automatically restarted.
* OneAgents are automatically restarted.
* Log Monitoring pods are automatically restarted.

Code modules are not restarted automatically. You must restart injected application pods.

## Operator-managed communication tokens

Dynatrace Operator creates and manages communication tokens that enable secure communication between Dynatrace components:

* ActiveGateâNode Collection Controller token
* ActiveGateâExtension Execution Controller token
* EECâDynatrace Collector token

## Manually rotating Operator-managed tokens

If you need to rotate any of the Operator-managed communication tokens, follow the instructions below.

1. Delete the existing secrets.

   ```
   kubectl delete secret <dynakube>-kspm-token -n dynatrace



   kubectl delete secret <dynakube>-extension-token -n dynatrace



   kubectl delete secret <dynakube>-activegate-auth-token-secret -n dynatrace
   ```
2. After the secret is removed, Dynatrace Operator automatically generates a new token and recreates the secret.

   You can verify the secret recreation using:

   ```
   kubectl get secrets -n dynatrace
   ```
3. Restart the components that use the token.

   ```
   kubectl rollout restart statefulset <dynakube>-activegate -n dynatrace



   kubectl rollout restart statefulset <dynakube>-extension-controller -n dynatrace



   kubectl rollout restart statefulset <dynakube>-otel-collector -n dynatrace



   kubectl rollout restart daemonset <dynakube>-node-config-collector -n dynatrace
   ```