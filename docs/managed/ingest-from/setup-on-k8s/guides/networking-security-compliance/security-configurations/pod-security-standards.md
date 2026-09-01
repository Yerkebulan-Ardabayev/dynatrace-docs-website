---
title: Apply Pod Security Standards
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/pod-security-standards
---

# Apply Pod Security Standards

# Apply Pod Security Standards

* 3-min read
* Updated on Aug 11, 2026

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

## Configure pod security for application namespaces

The `privileged` Pod Security Standard requirement applies to any application namespace where Dynatrace injects pods via CSI volumes (that is, when the CSI driver is enabled), not only the `dynatrace` namespace. The Dynatrace Operator webhook adds a CSI inline ephemeral volume (`csi.oneagent.dynatrace.com`) to monitored pods when the CSI driver is available, and Kubernetes PSA enforces volume restrictions at the namespace boundary before pod admission.

Run the following command for each monitored application namespace:

```
kubectl label namespace <your-namespace> \



pod-security.kubernetes.io/enforce=privileged \



pod-security.kubernetes.io/audit=privileged \



pod-security.kubernetes.io/warn=privileged
```

### OpenShift: use the CSI driver volume profile label

On OpenShift clusters where `CSIInlineVolumeSecurity` admission is enabled, you can label the Dynatrace CSI driver instead of relabeling each application namespace:

```
oc label csidriver csi.oneagent.dynatrace.com \



security.openshift.io/csi-ephemeral-volume-profile=restricted --overwrite
```

Verify the label was applied:

```
oc get csidriver csi.oneagent.dynatrace.com \



-o jsonpath='{.metadata.labels.security\.openshift\.io/csi-ephemeral-volume-profile}{"\n"}'
```

### Use node image pull

If granting `privileged` at the namespace level is not an option, you can force ephemeral volume delivery for specific pods. Ephemeral volumes do not use CSI inline volumes, so the namespace PSA requirement does not apply. Set `codeModulesImage` on your DynaKube and annotate the affected pod templates: `oneagent.dynatrace.com/volume-type: "ephemeral"` For details, see [Code modules delivery modes](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.").

## Troubleshoot

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

To understand why an application pod in a monitored namespace fails to be created, check the pod or the namespace events:

```
kubectl -n <your-namespace> describe pod <pod-name>
```

The following error indicates that the namespace PSA enforcement level is too low for the CSI inline volume that Dynatrace injects. To resolve this, see [Configure pod security for application namespaces](#configure-pod-security-for-application-namespaces).

```
Error creating pod: pods "<pod-name>" is forbidden: "<pod-name>" uses an inline volume provided by CSIDriver csi.oneagent.dynatrace.com and namespace <your-namespace> has a pod security enforce level that is lower than privileged.
```