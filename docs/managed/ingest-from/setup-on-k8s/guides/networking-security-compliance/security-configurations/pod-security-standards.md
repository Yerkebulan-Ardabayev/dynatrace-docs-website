---
title: Apply Pod Security Standards
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/pod-security-standards
---

# Apply Pod Security Standards

# Apply Pod Security Standards

* 3-min read
* Updated on Jan 16, 2024

Kubernetes version 1.25+

You can set namespace-based isolation levels for pods using [Pod Security Standards﻿](https://dt-url.net/mp0345l), enforced by the built-in [Pod Security admission controller﻿](https://dt-url.net/19238ro). These standards specify a list of controls, such as capabilities, seccomp profiles, and volume types.

While the Pod Security admission controller is a built-in feature of Kubernetes, it is not necessarily enabled by default in all Kubernetes distributions. Moreover, for environments where enhanced or different security policies are required, third-party alternatives such as Open Policy Agent (OPA) can be utilized. For more information on using third-party tools to enforce pod security standards, see [enforcing pod security standards with third-party alternatives﻿](https://dt-url.net/ix038h9).

## Pod security standards

Pod Security Standards define three policies:

* [Privileged﻿](https://dt-url.net/mv038z4): An unrestricted policy.
* [Baseline﻿](https://dt-url.net/4p238n8): Minimally restrictive policy.
* [Restricted﻿](https://dt-url.net/ut4387d): Heavily restricted policy.

Pod Security Standards are a built-in feature of Kubernetes, and they cannot be extended or customized.

## Configure pod security for the namespace

Pod security standards are applied at the namespace level when pods are created. If the default enforced profile set by the built-in admission controller is anything other than `privileged` (for example, `baseline` or `restricted`), at the [built-in admission controller level﻿](https://dt-url.net/yo4383i), the `privileged` profile needs to be configured for your namespace. Only the `privileged` policy is supported by Dynatrace Operator, as the CSI driver and OneAgent pods require more permissions than the `baseline` or `restricted` policies allow.

Run the following command to set the `dynatrace` namespace to `privileged`:

```
kubectl label namespace dynatrace pod-security.kubernetes.io/enforce=privileged pod-security.kubernetes.io/audit=privileged pod-security.kubernetes.io/warn=privileged
```

### Audit and warning modes

The [audit and warning modes﻿](https://dt-url.net/6l037ti) are applied to the deployment, DaemonSet, or other workload resources to catch violations even if a pod hasn't been created.

## Troubleshooting

To understand why OneAgent pods might fail to be created under a restricted policy, use the following command.

```
kubectl -n dynatrace describe daemonset.apps/<dynakube>-oneagent
```

The following event output shows a pod security standard violation preventing pod creation. This type of output is what you should watch out for when diagnosing deployment issues.

```
> Events:



>



> Type | Reason | Age| From| Message



> ---- |--------|---- |----|-------



> Warning|FailedCreate|15s|daemonset-controller|Error creating: pods "dynakube-oneagent-kp6sf" is forbidden: violates PodSecurity "restricted:latest": forbidden AppArmor profile (container.apparmor.security.beta.kubernetes.io/dynatrace-oneagent="unconfined"), host namespaces (hostNetwork=true, hostPID=true), allowPrivilegeEscalation != false (container "dynatrace-oneagent" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (container "dynatrace-oneagent" must not include "CHOWN", "DAC_OVERRIDE", "DAC_READ_SEARCH", "FOWNER", "FSETID", "KILL", "NET_ADMIN", "NET_RAW", "SETFCAP", "SETGID", "SETUID", "SYS_ADMIN", "SYS_CHROOT", "SYS_PTRACE", "SYS_RESOURCE" in securityContext.capabilities.add), restricted volume types (volume "host-root" uses restricted volume type "hostPath"), seccompProfile (pod or container "dynatrace-oneagent" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
```

Similarly, to check why CSI driver pods might fail under the same conditions, use the following command.

```
kubectl -n dynatrace describe daemonset.apps/dynatrace-oneagent-csi-driver
```

```
> Events:



>



> Type| Reason | Age| From| Message



> ---- |--------|---- |----| -------



> Warning|FailedCreate|25m|daemonset-controller|Error creating: pods "dynatrace-oneagent-csi-driver-nh7p9" is forbidden: violates PodSecurity "restricted:latest": privileged (containers "server", "provisioner" must not set securityContext.privileged=true), allowPrivilegeEscalation != false (containers "server", "provisioner", "registrar" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (containers "csi-init", "server", "provisioner", "registrar", "liveness-probe" must set securityContext.capabilities.drop=["ALL"]), restricted volume types (volumes "registration-dir", "plugin-dir", "data-dir", "mountpoint-dir" use restricted volume type "hostPath"), runAsNonRoot != true (containers "csi-init", "server", "provisioner", "registrar", "liveness-probe" must not set securityContext.runAsNonRoot=false), runAsUser=0 (containers "csi-init", "server", "provisioner", "registrar", "liveness-probe" must not set runAsUser=0)
```