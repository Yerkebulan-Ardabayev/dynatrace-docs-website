---
title: Seccomp profiles
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp
---

# Seccomp profiles

# Seccomp profiles

* Explanation
* 5-min read
* Published Mar 24, 2026

## What is seccomp?

Seccomp (secure computing mode) is a Linux kernel security feature that restricts the system calls a process is allowed to make. By applying a seccomp profile to a container, you limit which kernel-level operations it can perform, reducing the attack surface of your workloads. Kubernetes supports configuring seccomp profiles at both the pod and container level through the `securityContext` field, making it a key mechanism for meeting security standards such as the Kubernetes [Pod Security Standards﻿](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

There are three seccomp profile types in Kubernetes:

* **RuntimeDefault**—The container runtime's built-in default profile. It permits a curated set of common system calls while blocking potentially dangerous ones.
* **Localhost**—A custom profile loaded from a JSON file on the node's filesystem.
* **Unconfined**—No seccomp filtering is applied; all system calls are allowed.

All Dynatrace Operator infrastructure components (operator, webhook, and CSI driver) and operator-deployed components (ActiveGate, EdgeConnect) use the `RuntimeDefault` seccomp profile. The exception is OneAgent, which is unconfined (no seccomp profile set). The `RuntimeDefault` profile is suitable for most workloads and satisfies the **restricted** Pod Security Standard.

Using seccomp on OpenShift

If Dynatrace Operator injects a seccomp profile into an application pod in OpenShift, [SecurityContextConstraints (SCCs)﻿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/managing-pod-security-policies) that prevent seccomp profile usage — such as `anyuid`, `restricted`, or `nonroot` — will no longer apply. The system will instead fall back to another SCC (for example `restricted-v2`), which may render pods unschedulable or cause workload degradation.

## OneAgent seccomp profile

The OneAgent runs without a seccomp profile (unconfined) by default. This default was chosen to ensure compatibility with the widest range of platforms and container runtimes, as the OneAgent requires access to a broader set of system calls for deep host-level monitoring.

### Configure a custom seccomp profile for OneAgent

Dynatrace Operator version 1.2.0+

If your security policies require a seccomp profile on the OneAgent, you can configure one using the `secCompProfile` field under the appropriate OneAgent mode in your DynaKube custom resource.

**Limitation:** The OneAgent seccomp profile is always applied with the type `Localhost`. This means you must provide a custom seccomp profile JSON file on each node—you cannot set the type to `RuntimeDefault` or `Unconfined` through this field.

Cloud-native full stack

Classic full stack

Host monitoring

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullStack:



secCompProfile: "my-seccomp-profile.json"
```

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



oneAgent:



classicFullStack:



secCompProfile: "my-seccomp-profile.json"
```

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



oneAgent:



hostMonitoring:



secCompProfile: "my-seccomp-profile.json"
```

The `Localhost` type requires that the seccomp profile JSON file is present on the node's local filesystem, under the kubelet's configured seccomp profile root directory (by default `/var/lib/kubelet/seccomp/`). For the examples above, the profile file would need to be located at `/var/lib/kubelet/seccomp/my-seccomp-profile.json` on every node where the OneAgent is scheduled.

To learn how to create and manage `Localhost` seccomp profiles, refer to the Kubernetes documentation:

* [Restrict a Container's Syscalls with seccomp﻿](https://kubernetes.io/docs/tutorials/security/seccomp/)
* [Set the seccomp profile for a Container﻿](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-seccomp-profile-for-a-container)

## Configure seccomp for the Dynatrace init container

Dynatrace Operator version 0.11.2+

The seccomp profile for the Dynatrace init container (used for code module injection) is controlled by the `feature.dynatrace.com/init-container-seccomp-profile` feature flag.

Starting with Dynatrace Operator version 1.9.0, the default value of this feature flag changed from `"false"` to `"true"`. This means the init container now has the `RuntimeDefault` seccomp profile applied by default, helping meet the requirements of the **restricted** Pod Security Standard for your monitored Kubernetes workloads.

If you are running Dynatrace Operator version 0.11.2 through 1.8.x, you must explicitly enable this feature flag to apply the `RuntimeDefault` profile:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/init-container-seccomp-profile: "true"
```

To disable the seccomp profile on the init container (on any version), set the feature flag to `"false"`:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/init-container-seccomp-profile: "false"
```

When set to `"false"`, the init container will not have a seccomp profile set, and the default behavior of your container runtime will be used instead.