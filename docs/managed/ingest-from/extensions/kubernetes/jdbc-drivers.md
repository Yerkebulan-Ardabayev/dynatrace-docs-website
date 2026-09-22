---
title: Custom JDBC drivers
source: https://docs.dynatrace.com/managed/ingest-from/extensions/kubernetes/jdbc-drivers
---

# Custom JDBC drivers

# Custom JDBC drivers

* How-to guide
* 3-min read
* Published Aug 25, 2026

For custom JDBC extensions or vendor-specific drivers with restrictive licenses (for example, SAP HANA DB), you may need to provide a custom JDBC driver JAR to the SQL Extension Executor pod. You can provide custom JDBC drivers in two ways:

## Option 1: Mount a volume with custom drivers

In your DynaKube, mount a volume to `/app/user/libs`. The drivers in this directory are automatically discovered and loaded by the SQL Extension Executor pod at startup. If you update the mounted volume, a restart of the SQL Extension Executor pod is required to pick up the new drivers.

```
spec:



extensions:



databases:



- replicas: 2



id: default



volumes:



- name: custom-drivers



secret:



name: sql-drivers-secret



volumeMounts:



- name: custom-drivers



mountPath: /app/user/libs
```

## Option 2: Use a custom container image

Build a custom container image based on the [Dynatrace SQL Extension Executor image﻿](https://gallery.ecr.aws/dynatrace/dynatrace-sql-extension-executor) with custom JDBC drivers pre-installed in `/app/user/libs/`. Then specify the image for `sqlExtensionExecutor`:

```
templates:



sqlExtensionExecutor:



imageRef:



repository: your-registry/your-custom-executor-image



tag: <tag>
```