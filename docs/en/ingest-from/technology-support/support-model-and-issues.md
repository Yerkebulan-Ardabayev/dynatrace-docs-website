---
title: Dynatrace Operator support and known issues
source: https://www.dynatrace.com/docs/ingest-from/technology-support/support-model-and-issues
scraped: 2026-02-16T21:18:33.910731
---

# Dynatrace Operator support and known issues

# Dynatrace Operator support and known issues

* Latest Dynatrace
* 5-min read
* Updated on Feb 10, 2026

Dynatrace offers support for Kubernetes shortly after a new Kubernetes or OpenShift release. Once the new Kubernetes/OpenShift release candidate versions are available, Dynatrace tests these versions, including the latest OneAgent, ActiveGate, and Dynatrace Operator versions.

The table below lists the verified and tested release versions:

| Kubernetes upstream version | OpenShift version | Minimum OneAgent version | Minimum ActiveGate version | Minimum Dynatrace Operator version | Recommended Dynatrace Operator version | End of support (Kubernetes) | End of support (OpenShift) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.35 |  | 1.329 | 1.329 | v1.1.x | v1.8.0+ | Apr 1, 2028 |  |
| 1.34 | 4.21[4](#fn-1-4-def) | 1.321 | 1.321 | v1.1.x | v1.7.0+ | Nov 1, 2027 | Oct 1, 2028 |
| 1.33 | 4.20[4](#fn-1-4-def) | 1.319 | 1.319 | v1.1.x | v1.7.0+ | Jul 1, 2027 | Mar 1, 2028 |
| 1.32 | 4.19[4](#fn-1-4-def) | 1.309 | 1.309 | v1.1.x | v1.7.0+ | Mar 1, 2027 | Mar 1, 2028 |
| 1.31 | 4.18[3](#fn-1-3-def) | 1.297 | 1.297 | v1.1.x | v1.7.0+ | Jan 1, 2027 | Aug 1, 2028 |
| 1.30 | 4.17[3](#fn-1-3-def) | 1.291 | 1.291 | v1.1.x | v1.7.0+ | Aug 1, 2026 | Jul 1, 2027 |
| 1.29 | 4.16[3](#fn-1-3-def) | 1.281 | 1.281 | v0.14.x | v1.7.0+ | Mar 1, 2026 | Sep 1, 2027 |
| 1.28 | 4.15 | 1.275 | 1.275 | v0.12.x | v1.7.0+ | Nov 1, 2025 | Nov 1, 2026 |
| 1.27 | 4.14 | 1.269 | 1.269 | v0.10.x | v1.7.0+ | Jul 1, 2025 | Nov 1, 2026 |
| 1.26 | 4.13 | 1.259 | 1.257 | v0.10.x | v1.7.0+ | Mar 1, 2025 | Feb 1, 2026 |
| 1.25 | 4.12 | 1.249 | 1.251 | v0.8.x | v1.4.2+ | Nov 1, 2024 | Feb 1, 2026 |
| 1.24 | 4.11 | 1.241 | 1.243 | v0.7.x | v1.3.2+ | Aug 1, 2024 | Mar 1, 2025 |
| 1.23 | 4.10 | 1.233 | 1.233 | v0.4.x | v1.0.1[2](#fn-1-2-def) | Apr 1, 2024 | Mar 1, 2025 |
| 1.22 | 4.9 | 1.227 | 1.223 | v0.3.x | v1.0.1[2](#fn-1-2-def) | Jan 1, 2024 | May 1, 2024 |
| 1.21 | 4.8 | 1.217 | 1.215 | v0.3.x | v0.12.1[1](#fn-1-1-def) | Nov 1, 2023 | May 1, 2024 |
| 1.20 | 4.7 | 1.207 | 1.211 | v0.3.x | v0.6.0 | Aug 1, 2023 | Aug 1, 2023 |
| 1.19 | 4.6 | 1.199 | 1.205 | v0.3.x | v0.6.0 | Aug 1, 2023 | Aug 1, 2023 |
|  | 3.11 |  |  | v0.2.2 | v0.2.2 | Aug 1, 2023 | Aug 1, 2023 |

1

A new Go version used in Dynatrace Operator is incompatible with the CRI-O version of OpenShift 4.8 and Kubernetes 1.21. See the required manual workaround in [Dynatrace Operator release notes version 0.13.0](/docs/whats-new/dynatrace-operator/dto-fix-0-13-0 "Release notes for Dynatrace Operator, version 0.13.0").

2

Dynatrace Operator version 1.0.1 is recommended for Kubernetes 1.22 and 1.23. Upgrading to version 1.1.0+ is suggested for OpenShift 4.8 and above.

3

[Classic Full-Stack monitoring](/docs/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack "In-depth description of Classic Full-Stack monitoring using Dynatrace Operator.") is supported only on worker nodes that run Red Hat Enterprise Linux. If worker nodes run Red Hat Enterprise Linux CoreOS instead, only [Full-stack observability](/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "In-depth description of full-stack observability using Dynatrace Operator.") is supported.

4

Only [Application observability](/docs/ingest-from/setup-on-k8s/how-it-works/application-monitoring "In-depth description of Application observability using the Dynatrace Operator.") and [Full-stack observability](/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "In-depth description of full-stack observability using Dynatrace Operator.") are supported. This is because worker nodes can run only Red Hat Enterprise Linux CoreOS. To learn more, see [Red Hat release notes (1.5.13.2)ï»¿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/release_notes/ocp-4-19-release-notes#ocp-4-19-rhel-worker-nodes-removed_release-notes).

Full support is provided until a Kubernetes or OpenShift version reaches end of life. After that, Dynatrace provides maintenance support for approximately one year. End-of-support dates are announced in [End-of-support announcements](/docs/whats-new/technology/end-of-support-news#dto "End of support announcements for technologies supported by Dynatrace.").

The main distinction between full support and maintenance support is that Dynatrace reduces the daily testing activities during the maintenance support period.

During the full support and maintenance support periods, each encountered bug undergoes a backport assessment. Depending on the severity and change risk, the fix is either backported and released with a patch version or fixed in the next version. For details, refer to the relevant [Dynatrace release notes](/docs/whats-new "Read the product news and the release notes and find out which Documentation topics are new.").

## Dynatrace Operator support

The Dynatrace Operator is available on the following architectures:

* x86
* ARM
* ppc64le
* s390x [1](#fn-2-1-def)

1

Only the [cloud native full stack deployment](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes"), [application monitoring](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes"), and [host monitoring](/docs/ingest-from/setup-on-k8s/deployment/other/host-monitoring "Deploy Dynatrace Operator in host monitoring mode to Kubernetes") are supported.

In cases where issues related to the Dynatrace Operator cannot be replicated by Dynatrace on x86 or ARM architectures and are identified as specific to ppc64le, you need to reach out to `dt-operator@ibm.com` for further support. Additional information can be found in the associated open-source pull request for the Dynatrace Operator on [GitHubï»¿](https://dt-url.net/ev034k3).

Dynatrace Operator is responsible for rollout and lifecycle management of various Dynatrace components in Kubernetes and OpenShift (including ActiveGate and OneAgent). Dynatrace Operator is an open-source project maintained on [GitHubï»¿](https://dt-url.net/d7034gj). It follows the `major.minor.patch` [semantic versioningï»¿](https://semver.org/) schema, with a release cadence of minor versions being released roughly every 2â3 months.

The three latest Dynatrace Operator versions are tested with the latest Kubernetes and OpenShift versions. Additionally, we perform a backport assessment for any bug or vulnerability to analyze the severity and change risk of the fix. We recommend that you use the latest patch version, as the newly implemented features increment the minor version. For details, see the [Dynatrace Operator release notes](/docs/whats-new/dynatrace-operator "Release notes for Dynatrace Operator").

All Dynatrace Operator versions that are not considered end-of-life are treated as being in maintenance mode, which includes our regular customer support processes. Versions in maintenance mode do not receive bug fixes and vulnerability backports. See end-of-support announcements on [End-of-support announcements](/docs/whats-new/technology/end-of-support-news#dto "End of support announcements for technologies supported by Dynatrace.").

## Known issues and resolutions

A list of known issues for Dynatrace Operator versions and how they affect various components. These issues are present in released versions of the Dynatrace Operator and may require a minor version upgrade to resolve them!

### Dynatrace component injection

Dynatrace Operator version 1.7.0 Dynatrace Operator version 1.7.1 Dynatrace Operator version 1.7.2

#### Issue

* Due to optimization of the injected mounts (combining them under `/var/lib/dynatrace`), Dynatrace components can no longer be injected with the OneAgent.

* Dynatrace components contain configuration in `/var/lib/dynatrace` that is hidden by mounts added by the Webhook injection.

By default, monitoring for the Dynatrace Operator namespace (and therefore Dynatrace components) is not enabled. The issue can surface if the `feature.dynatrace.com/ignored-namespaces` feature flag is used to override ignored namespaces to include the Dynatrace Operator namespace.

#### Resolution

Configure the `dynatrace.com/split-mounts` pod annotation (requires Dynatrace Operator version 1.8.0+) on affected pods.

### Classic full-stack with metadata enrichment

Dynatrace Operator version 1.7.0 Dynatrace Operator version 1.7.1 Dynatrace Operator version 1.7.2

#### Issue

* Classic full-stack and metadata enrichment are not compatible and cannot be used to inject the same application pods.

Both OneAgent and Webhook injection attempt to add a mount to the `/var/lib/dynatrace` directory in the application pod. These mounts are incompatible and cannot coexist.

#### Resolution

If using Dynatrace Operator versions below 1.7.0:

* With OneAgent version 1.333, no changes are required.
* With OneAgent version 1.331 or earlier, the `remountOperatorEnrichment` debug flag needs to be configured for the OneAgent.

Upgrade to Dynatrace Operator version 1.8.0 (when available).

### Host availability detection

Dynatrace Operator version 1.6.0 Dynatrace Operator version 1.6.1 Dynatrace Operator version 1.6.2 Dynatrace Operator version 1.7.0 Dynatrace Operator version 1.7.1

#### Issue

* In Kubernetes environments â especially those utilizing auto-scalers â there are challenges in reliably determining whether a node was intentionally removed or has failed unexpectedly. This ambiguity can lead to a high number of false-positive âHost is unavailableâ alerts, impacting monitoring accuracy and alerting quality.

#### Resolution

Upgrade to Dynatrace Operator version 1.7.2+ or 1.6.3.

### Switch to Node image pull with Code modules image

Dynatrace Operator version 1.5.0 Dynatrace Operator version 1.5.1 Dynatrace Operator version 1.6.0 Dynatrace Operator version 1.6.1 Dynatrace Operator version 1.6.2

#### Issue

When switching from using the CSI driver without `codeModulesImage` to using it with [node image pull](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull"), ensure that the CSI driverâs filesystem does not contain a code module for the specified DynaKube. If it does, the CSI driver will fail and require manual intervention to recover.

* If this issue is encountered, reverting back to not using the `codeModulesImage` will make the CSI driver operational again.
* You can use the `find` command to check for the downloaded code module for a DynaKube in the filesystem of the CSI `server` container:

  ```
  > find /data -name latest-codemodule



  /data/_dynakubes/my-dynakube-1/latest-codemodule



  /data/_dynakubes/my-dynakube-2/latest-codemodule
  ```

#### Resolution

* Upgrade to Dynatrace Operator version 1.7.0+.

Other ways to solve the problem:

* Delete the DynaKube and recreate it. This will cause monitoring gaps.

### Incompatibilities with specific component versions

Dynatrace Operator version 1.5.0+

The automatic TLS certificate feature requires ActiveGate version 1.307.35+.

* If you prefer to disable this feature, set the feature flag `feature.dynatrace.com/automatic-tls-certificate: false` in your DynaKube configuration.