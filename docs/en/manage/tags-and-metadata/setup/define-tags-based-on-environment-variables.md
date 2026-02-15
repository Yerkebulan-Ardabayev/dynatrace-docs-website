---
title: Define tags based on environment variables
source: https://www.dynatrace.com/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables
scraped: 2026-02-15T21:19:08.432361
---

# Define tags based on environment variables

# Define tags based on environment variables

* How-to guide
* 2-min read
* Updated on Aug 07, 2023

Dynatrace provides the ability to define tags as in environment variables for processes and process groups.

## Recommendation

Defining tags in the environment itself has its uses. However it's not recommended as a general purpose solution, as it is rather cumbersome and requires a lot of preplanning. It also makes it hard to make changes later. Therefore, you will have to use it with caution.

We recommend that you define additional metadata at the deployed system. Typically, you should think about additional metadata and standard metadata and not about tags (that is, labels).

Use the environment variable [`DT_CUSTOM_PROP`](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment.") to define your metadata. This enables you to use [automated tagging rules](/docs/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically."), based on existing or custom metadata, to define your filter sets for charts, alerting, and more. These tags and rules can be changed and adapted any time and are applied almost immediately without any change to the monitored environment or applications.

## Define tags as environment variables

You can define an environment variable called `DT_TAGS` on the process or host level. The format of the variable is simple. The variable can contain simple strings or key/value pairs (for example, `DT_TAGS=MikesStuff easyTravel=Mike`). As you can see in the Windows process example below, you can define multiple tags. Spaces are used to separate tag values.

To customize the process group of IIS, you need to define an environment variable that you can use within the scope of a rule. To set up an environment variable in IIS version 10 or later, see [Environment variablesï»¿](https://www.iis.net/configreference/system.applicationhost/applicationpools/add/environmentvariables).

How to define an environment variable for IIS earlier than version 10

#### Set up an environment variable for IIS versions earlier than 10

To set up an environment variable in IIS versions earlier than 10, follow the instructions below.

1. Configure the **Advanced Settings** for Application Pool.

   ![Environment variable IIS](https://dt-cdn.net/images/env1-1578-6d669915ad.png)
2. Set the **Load User Profile** as **True**.

   ![Environment variable IIS](https://dt-cdn.net/images/env2-1563-c1584fc0f2.png)
3. Restart IIS.  
   At the command prompt with admin rights, enter `iisreset`.
4. Open the Registry and navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\hivelist`

   ![Environment variable IIS](https://dt-cdn.net/images/env4-1571-60d8f6ab63.png)
5. Launch the application to initialize the AppPool (or set the **AppPool Start Mode** to **Always Running**), refresh `hivelist` and look for the new entries.

   ![Environment variable IIS](https://dt-cdn.net/images/env5-1580-7e22193123.png)
6. Check `C:\Users` for the name of the user who runs the AppPool.

   ![Environment variable IIS](https://dt-cdn.net/images/env7-557-1acbf9ee8c.png)
7. In the registry navigate to the ID of the user under `HKEY_USERS` and add a **String Value** named `DT_CUSTOM_PROP`.

   ![Environment variable IIS](https://dt-cdn.net/images/env8-1590-c013dd318f.png)
8. Add the value you want with spaces between the key/value pairs.

   ![Environment variable IIS](https://dt-cdn.net/images/env9-949-0ec6aad7a9.png)
9. Restart IIS one more time and check Dynatrace process for environmental metadata.

   ![Environment variable IIS](https://dt-cdn.net/images/env10-1361-e92e945f44.png)

How to define an environment variable for Windows

To customize process grouping for Windows services, open **Registry Editor** on your local machine and create a key called **Environment** of type `REG_MULTI_SZ` in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<servicename>`. The variable name should start with the `DT_CUSTOM_PROP` string, for example, `DT_CUSTOM_PROP=NAME_A=valueA`. The key may contain multiple entries.

Example:

![pg-vars](https://dt-cdn.net/images/2022-02-18-9-49-57-459-fb9fe355b4.png)

Applying [tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") to hosts (instead of thoughtfully setting up environment variables as explained here) isn't recommended. The same applies to applications and processes. For details on setting up the `DT_CUSTOM_PROP` environment variable for Tomcat or WebSphere application metadata, Kubernetes annotations for Kubernetes-based deployments, or AWS tagging, see [Application metadata & tagging](/docs/manage/tags-and-metadata/basic-concepts/best-practices-and-recommendations-for-tagging#application-metadata-and-tagging "Learn when it's recommended to use tags that leverage auto-detected metadata, as well as best practices for enriching Dynatrace monitoring with additional metadata.").

![Env tagging 1](https://dt-cdn.net/images/env-tagging1-433-ef2e38dad8.png)

## Filter entities based on environment variables

In the Dynatrace UI, the example environment variable shown above results in new filters being displayed on the related process overview page (see below). Process group overview pages display the sum of all the tags of all processes in the group.

![Env tagging 2](https://dt-cdn.net/images/env-tagging2-1414-289c172a71.png)

![Env tagging 3](https://dt-cdn.net/images/env-tagging3-1272-0d740c7cb8.png)

![Env tagging 4](https://dt-cdn.net/images/env-tagging4-1113-971391db79.png)

This feature is currently only available for processes that are deep monitored via OneAgent (Java, Apache Webserver, NGINX, .NET, Node.js, PHP, Go, and IIS).