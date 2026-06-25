---
title: Configure build label propagation
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/metadata-automation/build-label-propagation
scraped: 2026-05-12T12:07:50.118077
---

# Configure build label propagation

# Configure build label propagation

* 2-min read
* Published Jul 28, 2023

Build label propagation enables you to provide build and version metadata information to the injected OneAgent about the newly deployed pods. This information is then visible on the **Properties and tags** section of your entities pages.

## How it works

You can [reference the value of a metadata field in an environment variableï»¿](https://dt-url.net/cy035by).

```
env:



- name: MY_POD_NAMESPACE



valueFrom:



fieldRef:



fieldPath: metadata.namespace
```

Then OneAgent injects into the newly deployed pods and collects the metadata provided via environment variables.

## Enable build label propagation

To enable build label propagation, you need to set `feature.dynatrace.com/label-version-detection` to `true` in DynaKube. Note that since enabling build label propagation requires webhook injection, it only works with `applicationMonitoring` and `cloudNativeFullStack` deployments.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/label-version-detection: "true"



...



spec:



oneAgent:



cloudNativeFullStack: {}
```

## Default behavior

* The `DT_RELEASE_VERSION` environment variable gets the value from `metadata.labels['app.kubernetes.io/version']`.
* The `DT_RELEASE_PRODUCT` environment variable gets the value from `metadata.labels['app.kubernetes.io/part-of']`.

For example, if your application has the following pod:

```
apiVersion: v1



kind: Pod



metadata:



...



labels:



app.kubernetes.io/version: "1.0.0"



app.kubernetes.io/part-of: "store"



spec:



...
```

the value of the labels is added to the environment variables of the injected containers:

```
apiVersion: v1



kind: Pod



metadata:



...



labels:



app.kubernetes.io/version: "1.0.0"



app.kubernetes.io/part-of: "Store"



spec:



...



containers:



- name: app



...



env:



- name: "DT_RELEASE_VERSION"



valueFrom:



fieldRef:



fieldPath: metadata.labels['app.kubernetes.io/version']



- name: "DT_RELEASE_PRODUCT"



valueFrom:



fieldRef:



fieldPath: metadata.labels['app.kubernetes.io/part-of']
```

If the `DT_RELEASE_VERSION` or `DT_RELEASE_PRODUCT` environment variables are already set on the container before the OneAgent injection, they will not be overwritten.

## Configuration options

You can annotate your namespace to provide further mappings or overrule the defaults for pods within that namespace.

* Each annotation key is mapped to a specific environment variable.
* Each annotation value is the reference path in `fieldPath`.
* The available information for `fieldPath` is the same as for [`fieldRef`ï»¿](https://dt-url.net/0m235nn).

Example to overwrite the default values for `version` and `product`, and enable `stage` and `build-version`:

```
annotations:



mapping.release.dynatrace.com/version: "metadata.annotations['my-version']"



mapping.release.dynatrace.com/product: "metadata.labels['app.kubernetes.io/name']"



mapping.release.dynatrace.com/stage: "metadata.namespace"



mapping.release.dynatrace.com/build-version: "metadata.labels['release.dynatrace.com/stage']"
```

Each of these annotations configures a different environment variable:

|  |  |
| --- | --- |
| `mapping.release.dynatrace.com/version` | Holds the `fieldPath` used for `DT_RELEASE_VERSION`.  If this annotation is missing, mapping falls back to the [default behavior](#default-behavior). |
| `mapping.release.dynatrace.com/product` | Holds the `fieldPath` used for `DT_RELEASE_PRODUCT`.  If this annotation is missing, mapping falls back to the [default behavior](#default-behavior). |
| `mapping.release.dynatrace.com/stage` | Holds the `fieldPath` used for `DT_RELEASE_STAGE`. |
| `mapping.release.dynatrace.com/build-version` | Holds the `fieldPath` used for `DT_RELEASE_BUILD_VERSION`. |

The values aren't validated by Dynatrace Operator or the webhook, so make sure they are valid.