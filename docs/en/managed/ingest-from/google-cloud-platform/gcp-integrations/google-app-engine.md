---
title: Monitor Google App Engine
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine
scraped: 2026-02-27T21:16:46.043707
---

# Monitor Google App Engine

# Monitor Google App Engine

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jun 23, 2020

The Google App Engine standard environment type supports applications that run on Java, .NET, Node.js, Golang, and more. For custom Docker images, Google App Engine provides flexible environment support.

## Prerequisites

* Create a [PaaS Token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Review the list of [supported applications and versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Integrate OneAgent into the application image

To integrate OneAgent into a container deployment with a Dockerfile in Google App Engine flexible environment and activate instrumentation of your application, add the commands below to your current Dockerfile, making sure to enter your own values for the `DT_API_URL`, `DT_API_TOKEN`, and `DT_ONEAGENT_OPTIONS` arguments.

* `<environmentID>` should be replaced with your Dynatrace environment ID. If youâre using Dynatrace Managed, you need to provide your Dynatrace Server URL (`https://<YourDynatraceServerURL>/e/<environmentID>/api`).
* `<token>`should be replaced with the PaaS token mentioned in the prerequisites.
* Technology support is enabled via `include` parameters. Valid options for `flavor=default` are `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php` and `go`. Including specific technology-support options, rather than support for all technology options, results in a smaller OneAgent package. For Alpine Linux based environments, Dynatrace OneAgent supports the flavor `musl`. Valid options for `flavor=musl` are `all`, `go`, `java`, `apache`, `nginx`, and `nodejs`.

```
ARG DT_API_URL="https://<environmentID>.live.dynatrace.com/api"



ARG DT_API_TOKEN="<token>"



ARG DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"



ENV DT_HOME="/opt/dynatrace/oneagent"



RUN mkdir -p "$DT_HOME" && \



wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



rm "$DT_HOME/oneagent.zip"



ENTRYPOINT [ "/opt/dynatrace/oneagent/dynatrace-agent64.sh" ]



CMD [ "executable", "param1", "param2" ] # the command of your application, for example, Java
```

The `wget` and `unzip` commands above might fail if they aren't provided by the base image.

## Deploy the application image

After integrating the OneAgent into the application Docker file, deploy the application. In order to do this, switch to the directory of the application that contains the `Dockerfile` and the `app.yaml` file, and run the following command in the `gcloud` CLI.

```
gcloud app deploy
```

Google App Engine will take care of building the Docker image based on the Docker file provided, and thereby of downloading and installing the OneAgent code-modules into the application image.

## Update OneAgent

Every time you want to update your version of Dynatrace OneAgent, you must redeploy your application. Google App Engine thus rebuilds the application image with the latest OneAgent components. Any newly started containers from this application image is then monitored with the latest version of OneAgent.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")