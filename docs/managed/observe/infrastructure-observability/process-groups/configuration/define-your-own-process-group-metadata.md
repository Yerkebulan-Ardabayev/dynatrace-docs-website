---
title: Define your own process group metadata
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata
---

# Define your own process group metadata

# Define your own process group metadata

* How-to guide
* 1-min read
* Updated on Aug 07, 2023

Dynatrace automatically detects and displays lots of metadata values related to the processes that run in your environment—including version numbers, port numbers, and the name of the script or JAR file that launches each process (see images below).

![Metadata 1](https://dt-cdn.net/images/metadata1-1068-2deabeeefb.png)

Metadata 1

![Metadata 2](https://dt-cdn.net/images/metadata2-1074-353ed0c77a.png)

Metadata 2

Dynatrace enables you to use these metadata values to [automate tagging](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") as well as to use [environment variables to supply tags](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables."). Dynatrace even allows you to define your own metadata based on your organization’s or environment’s unique needs.

## Define metadata via environment variables

You can define the environment variable `DT_CUSTOM_PROP` at either the process or host level. The format of the variable is simple; it's comprised of key/value pairs, for example, `DT_CUSTOM_PROP=Department=Acceptance Stage=Sprint`. Note that environment variables must be visible to the [respective process at application startup](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection#env "Ways to customize process-group detection").

Once in place, the metadata values appear on each respective Process and Process group page (see example below).

![Metadata 3](https://dt-cdn.net/images/metadata3-1075-fb5fb788ad.png)

Metadata 3

How to define an environment variable for IIS

#### Set up an environment variable for IIS versions earlier than 10

To set up an environment variable in IIS versions earlier than 10, follow the instructions below.

1. Configure the **Advanced Settings** for Application Pool.

   ![Environment variable IIS](https://dt-cdn.net/images/env1-1578-6d669915ad.png)

   Environment variable IIS
2. Set the **Load User Profile** as **True**.

   ![Environment variable IIS](https://dt-cdn.net/images/env2-1563-c1584fc0f2.png)

   Environment variable IIS
3. Restart IIS.  
   At the command prompt with admin rights, enter `iisreset`.
4. Open the Registry and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\hivelist`

   ![Environment variable IIS](https://dt-cdn.net/images/env4-1571-60d8f6ab63.png)

   Environment variable IIS
5. Launch the application to initialize the AppPool (or set the **AppPool Start Mode** to **Always Running**), refresh `hivelist` and look for the new entries.

   ![Environment variable IIS](https://dt-cdn.net/images/env5-1580-7e22193123.png)

   Environment variable IIS
6. Check `C:\Users` for the name of the user who runs the AppPool.

   ![Environment variable IIS](https://dt-cdn.net/images/env7-557-1acbf9ee8c.png)

   Environment variable IIS
7. In the registry navigate to the ID of the user under `HKEY_USERS` and add a **String Value** named `DT_CUSTOM_PROP`.

   ![Environment variable IIS](https://dt-cdn.net/images/env8-1590-c013dd318f.png)

   Environment variable IIS
8. Add the value you want with spaces between the key/value pairs.

   ![Environment variable IIS](https://dt-cdn.net/images/env9-949-0ec6aad7a9.png)

   Environment variable IIS
9. Restart IIS one more time and check Dynatrace process for environmental metadata.

   ![Environment variable IIS](https://dt-cdn.net/images/env10-1361-e92e945f44.png)

   Environment variable IIS

How to define an environment variable for Windows

To customize process grouping for Windows services, open **Registry Editor** on your local machine and create a key called **Environment** of type `REG_MULTI_SZ` in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<servicename>`. The variable name should start with the `DT_CUSTOM_PROP` string, for example, `DT_CUSTOM_PROP=NAME_A=valueA`. The key may contain multiple entries.

Example:

![pg-vars](https://dt-cdn.net/images/2022-02-18-9-49-57-459-fb9fe355b4.png)

pg-vars

## Using annotations in Kubernetes

Dynatrace supports automated tagging in Kubernetes based on [Kubernetes labels﻿](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). You can similarly use [Kubernetes annotations﻿](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)—they too will show up on your Process and Process group pages (see below).

![Environment variables 4](https://dt-cdn.net/images/environmentvariables-4-1099-4cd32148af.png)

Environment variables 4

## Related topics

* [Ownership](/managed/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.")