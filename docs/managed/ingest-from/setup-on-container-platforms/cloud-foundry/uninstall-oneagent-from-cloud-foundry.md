---
title: Uninstall OneAgent from Cloud Foundry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/uninstall-oneagent-from-cloud-foundry
---

# Uninstall OneAgent from Cloud Foundry

# Uninstall OneAgent from Cloud Foundry

* 1-min read
* Published Apr 17, 2020

Find out below how to uninstall OneAgent according to your particular deployment strategy. For a clear view of all the deployment alternatives, see [Cloud Foundry deployment strategies](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.").

## Uninstall OneAgent Operator for BOSH release

1. Update the runtime configuration.  
   Uninstalling OneAgent for BOSH add-ons requires that you update the runtime configuration with an “empty” manifest and redeploy all BOSH deployments that are executed by the add-ons.

   Example of empty runtime configuration:

   ```
   releases:



   - name: dynatrace-oneagent



   version: 1.1.0



   #specify version of latest release
   ```

   Update the runtime configuration without Dynatrace-related jobs.

   ```
   bosh -e my-env update-runtime-config PATH/runtime-config-uninstall-dynatrace.yml
   ```
2. Deploy your changes and uninstall Dynatrace.

   ```
   bosh -e my-env -d deployment deploy
   ```

## Uninstall OneAgent for application-only monitoring

OneAgent is injected when the Dynatrace service is bound to the application. By unbinding the service, the OneAgent will no longer be injected (it's then uninstalled).

1. Unbind the service.

   ```
   cf unbind-service <app-name> <service-instance-name>
   ```
2. Restage the application.

   ```
   cf restage <app-name>
   ```

Optional To delete a service if it's no longer required (applies generically to both CUPS and service broker):

```
cf delete-service <service-instance-name>
```

## Related topics

* [Cloud Foundry monitoring](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")