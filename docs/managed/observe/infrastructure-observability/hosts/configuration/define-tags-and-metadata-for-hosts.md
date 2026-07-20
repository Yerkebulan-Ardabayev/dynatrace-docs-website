---
title: Define tags and metadata for hosts
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts
---

# Define tags and metadata for hosts

# Define tags and metadata for hosts

* How-to guide
* 4-min read
* Published Mar 08, 2018

Within dynamic or large environments, manual host tagging can be impractical. For dynamic deployments that include frequently changing host instances and names (for example, AWS or MS Azure), you should automate adding tags and metadata to your hosts.

### Tags

To automate the addition of tags to your hosts using OneAgent versions 1.189+, use OneAgent command-line parameters. For earlier versions, use the host tag configuration file.

### OneAgent command-line parameters for tags

OneAgent version 1.189+

To add or change host tags, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
* **Windows**  
  `.\oneagentctl.exe --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
  You can add or change more than one tag in the same command. You can also define tags with the same key but different values.

For more information on `oneagentctl`, see [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

### Edit the host tag configuration file

OneAgent version 1.187 and earlier

UTF-8 encoded

Any `hostautotag.conf` or `hostcustomproperties.conf` files created should be encoded in UTF-8.

During OneAgent installation, the installer creates a simple `hostautotag.conf` configuration file on the monitored host. On Windows, the file is located in `%PROGRAMDATA%\dynatrace\oneagent\agent\config`, and on Linux in `/var/lib/dynatrace/oneagent/agent/config`.

The file should contain a list of strings or key/value pairs that will be reported to the server with every file change. New lines or spaces are used to separate tag values. For example:

```
TestHost Gdansk role=fallback
```

### Result

After you configure them, the tags are displayed at the top of the **Properties and tags** section of the host overview page.

Tags created using `oneagentctl` behave similarly to [automated, rule-based tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") and [environment variable-based tags](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.").

They are prefixed with the `[Environment]` string and can't be removed manually from a host. They can only be removed through a `oneagentctl` command. To remove a tag, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --remove-host-tag=TestHost`
* **Windows**  
  `.\oneagentctl.exe --remove-host-tag=TestHost`

For more information, see [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Other options for automated tagging

You can also set up automated tagging of the hosts in your environment using:

* [Automated rules](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.")
* [Environment variables](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.")
* [Smartscape and topology API](/managed/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API.")

## Host metadata

To automate the addition of metadata to your hosts using OneAgent versions 1.189+, use command-line parameters. For earlier versions, use the host metadata configuration file.

### OneAgent command-line parameters for host metadata

OneAgent version 1.189+

To add or change host properties, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --set-host-property=AppName=easyTravel --set-host-property=Environment=Dev`
* **Windows**  
  `.\oneagentctl.exe --set-host-property=AppName=easyTravel --set-host-property=Environment=Dev`
  You can add or change more than one property in the same command.

When custom host metadata is used to enrich metrics and other telemetry, the keys and values might be adjusted to meet normalization requirements: keys are converted to lowercase, unsupported characters are replaced with an underscore (`_`), and keys or values that exceed the maximum length are truncated. As a result, an enriched value can differ from what you set here.

To set a security context for your host, use the following command:

* **Linux** and **AIX**  
  `./oneagentctl --set-host-tag=dt.security_context=easytrade_sec`
* **Windows**  
  `.\oneagentctl.exe --set-host-tag=dt.security_context=easytrade_sec`

To **remove host properties**, run the following command:

* **Linux** and **AIX**  
  `./oneagentctl --remove-host-property=AppName --remove-host-property=Environment=Dev`
* **Windows**  
  `.\oneagentctl.exe --remove-host-property=AppName --remove-host-property=Environment=Dev`

For more information, see [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Edit the host metadata configuration file

OneAgent version 1.187 and earlier

The process of configuring properties is similar to the one for tags, but here they're configured through the `hostcustomproperties.conf` file, which you need to create and add to your OneAgent configuration directories.

* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config`
* All Unix-like systems: `/var/lib/dynatrace/oneagent/agent/config`

### Result

After you configure them, custom properties are displayed in the **Environment custom meta data** section of **Properties and tags** on the host overview page. You can then set up [automatic tagging rules](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") to enable tagging of these properties.

## Related topics

* [Ownership](/managed/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.")