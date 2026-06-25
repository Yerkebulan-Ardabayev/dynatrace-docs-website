---
title: Application observability with Pod runtime injection
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/pod-runtime
scraped: 2026-05-12T11:52:43.553445
---

# Application observability with Pod runtime injection

# Application observability with Pod runtime injection

* 7-min read
* Updated on Oct 17, 2025

Inject Dynatrace code modules into a container during its deployment.

This method of application instrumentation may not fully link Kubernetes workloads with monitored containers/processes. For comprehensive relationships and linking, consider using the [automatic application-only injection](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Deploy Dynatrace Operator in application monitoring mode to Kubernetes").

## Prerequisites

* Review the list of [supported applications and versions](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* [Create an access token with `PaaS Integration - InstallerDownload`](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") scope.
* Storage requirements:

  + ~325 MB for glibc
  + ~290 MB for musl
  + ~650 MB for glibc and musl combined

Pod runtime injection and cgroup v2

If Pod runtime injection is used with [cgroup v2ï»¿](https://kubernetes.io/docs/concepts/architecture/cgroups/), the `builtin:containers.*` metrics are reported to Dynatrace only if all the following conditions are respected:

* The **Kubernetes API** is accessible (see [Grant viewer role to service accounts](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments#viewer "Organize and filter your monitored applications by importing labels and annotations from your Kubernetes/OpenShift environment."))
* The pod runs a **single container**

## Deploy

To integrate OneAgent into your application at runtime, select one of the options below based on your platform.

Linux

Windows

OneAgent is made available to the application container via an `initContainer`âyour application image remains unaffected.

To integrate OneAgent into your application at runtime, extend your deployment template as follows.

```
# your application containers



containers:



- name: customer-app



image: tomcat



env:



- name: LD_PRELOAD



value: /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so



- name: DT_NETWORK_ZONE



value: <your_network_zone>



volumeMounts:



- mountPath: /opt/dynatrace/oneagent



name: oneagent



# initcontainer to download OneAgent



initContainers:



- name: install-oneagent



image: alpine:latest



command:



- /bin/sh



args:



- -c



- ARCHIVE=$(mktemp) && wget -O $ARCHIVE "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_PAAS_TOKEN&$DT_ONEAGENT_OPTIONS" && unzip -o -d /opt/dynatrace/oneagent $ARCHIVE && rm -f $ARCHIVE



env:



- name: DT_API_URL



value: https://<your-environment-id>.live.dynatrace.com/api



- name: DT_PAAS_TOKEN



value: <Access token with PaaS integration scopes (Dynatrace -> Access tokens)>



- name: DT_ONEAGENT_OPTIONS



value: flavor=<FLAVOR>&include=<TECHNOLOGY>



volumeMounts:



- mountPath: /opt/dynatrace/oneagent



name: oneagent



# Make OneAgent available as a volume



volumes:



- name: oneagent



emptyDir: {}
```

* In the `# initContainer to download OneAgent` and `# Make OneAgent available as a volume` sections, add the `initContainer`, which will download OneAgent and make it available as a volume.
* In the `DT_ONEAGENT_OPTIONS` section, set the OneAgent code module required for your compiler flavor (`FLAVOR`) and application (`TECHNOLOGY`).

  + Valid options for `flavor` are `default`, `musl`, or `multidistro`. Set `default` to download `glibc` binaries or set `musl` to download `musl` binaries. Set `multidistro` to download both the `musl` and `glibc` binaries and subsequently autodetect which binaries to use. Note that image size will be larger in this case, as it includes both flavors.
  + Valid options for `technology` are `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go`, and `sdk`.
  + For ARM, use the following value: `flavor=default&arch=arm&include=<TECHNOLOGY>`. For other architectures, see the [list of valid values](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest#parameters "Download the latest OneAgent installer via Dynatrace API.") (scroll down to the `arch` parameter).
  + If you want to specify several code modules, use the following syntax: `&include=technology1&include=technology2`.

If you include specific technology-support options rather than 'support for all technologies' options, you'll get a smaller OneAgent package.

What if my Docker image is based on Alpine Linux?

Dynatrace OneAgent supports the flavor `musl` for Alpine Linux based environments.  
Valid options for `technology` are `all`, `dotnet`, `go`, `php`, `java`, `apache`, `nginx`, and `nodejs`.

* In the `# your application containers` section, add the newly created volume to the container of your application. Also add the `LD_PRELOAD`  environment variable.
* Optional In the `# your application containers` section, configure network zones:

```
containers:



env:



- name: DT_NETWORK_ZONE



value: <your_network_zone>
```

See [network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

* Optional Configure a proxy address.

In case you run an environment with proxy, you need to set the `DT_PROXY` environment variable in the application container to pass the proxy credentials to OneAgent.

For Alpine Linux-based containers, you might need to update the `wget` shipped with the Alpine image to allow for proxy authentication for the download of OneAgent.

Extend your deployment template as follows.

This option refers to .NET applications in Windows containers.

OneAgent version 1.319 and earlier

```
# your application containers



apiVersion: apps/v1



kind: Deployment



metadata:



name: sample



labels:



app: sample



spec:



replicas: 1



template:



metadata:



name: sample



labels:



app: sample



spec:



nodeSelector:



"kubernetes.io/os": windows



containers:



- name: sample



image: mcr.microsoft.com/dotnet/framework/samples:aspnetapp



env:



#.NET Framework



- name: COR_ENABLE_PROFILING



value: "0x01"



- name: COR_PROFILER



value: "{B7038F67-52FC-4DA2-AB02-969B3C1EDA03}"



- name: COR_PROFILER_PATH_32



value: "C:\\oneagent\\agent\\lib\\oneagentloader.dll"



- name: COR_PROFILER_PATH_64



value: "C:\\oneagent\\agent\\lib64\\oneagentloader.dll"



#.NET Core



- name: CORECLR_ENABLE_PROFILING



value: "0x01"



- name: CORECLR_PROFILER



value: "{B7038F67-52FC-4DA2-AB02-969B3C1EDA03}"



- name: CORECLR_PROFILER_PATH_32



value: "C:\\oneagent\\agent\\lib\\oneagentloader.dll"



- name: CORECLR_PROFILER_PATH_64



value: "C:\\oneagent\\agent\\lib64\\oneagentloader.dll"



- name: DT_AGENTACTIVE



value: "true"



- name: DT_BLOCKLIST



value: "powershell*"



volumeMounts:



- mountPath: "C:\\OneAgent"



name: oneagent



# initcontainer to download OneAgent



initContainers:



- name: install-oneagent



image: mcr.microsoft.com/windows/servercore:ltsc2019



command:



- powershell



args:



- |



Write-Host "Trustng all certificates..."



add-type @"



using System.Net;



using System.Security.Cryptography.X509Certificates;



public class TrustAllCertsPolicy : ICertificatePolicy {



public bool CheckValidationResult(



ServicePoint srvPoint, X509Certificate certificate,



WebRequest request, int certificateProblem) {



return true;



}



}



"@



[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy



Write-Host "Downloading agent..."



Invoke-WebRequest -Uri "$Env:DT_API_URL/v1/deployment/installer/agent/windows/paas/latest?Api-Token=$Env:DT_PAAS_TOKEN&$Env:DT_ONEAGENT_OPTIONS" -OutFile "installer.zip"



Write-Host "Unpacking agent..."



Expand-Archive -Path "installer.zip" -DestinationPath "C:\OneAgent" -Force



Write-Host "Configuring agent..."



$manifest = Get-Content "C:\OneAgent\manifest.json" | ConvertFrom-Json



$config = New-Item -Path "C:\OneAgent\agent\conf" -Name "standalone.conf" -Force



Add-Content -Path $config -Value "tenant $($manifest.tenantUUID)"



Add-Content -Path $config -Value "tenanttoken $($manifest.tenantToken)"



Add-Content -Path $config -Value "server $($manifest.communicationEndpoints -Join ';')"



Add-Content -Path $config -Value "storage C:\OneAgent"



Add-Content -Path $config -Value "loglevelcon NONE"



env:



- name: DT_API_URL



value: https://<your-environment-id>.live.dynatrace.com/api



- name: DT_PAAS_TOKEN



value: <Access token with PaaS integration scopes (Dynatrace -> Access tokens)>



- name: DT_ONEAGENT_OPTIONS



value: arch=default&include=dotnet



volumeMounts:



- mountPath: "C:\\OneAgent"



name: oneagent



# Make OneAgent available as a volume



volumes:



- name: oneagent



emptyDir: {}



selector:



matchLabels:



app: sample



---



apiVersion: v1



kind: Service



metadata:



name: sample



spec:



type: LoadBalancer



ports:



- protocol: TCP



port: 80



selector:



app: sample
```

OneAgent version 1.321+

```
# your application containers



apiVersion: apps/v1



kind: Deployment



metadata:



name: sample



labels:



app: sample



spec:



replicas: 1



template:



metadata:



name: sample



labels:



app: sample



spec:



nodeSelector:



"kubernetes.io/os": windows



containers:



- name: sample



image: mcr.microsoft.com/dotnet/framework/samples:aspnetapp



env:



#.NET Framework



- name: COR_ENABLE_PROFILING



value: "0x01"



- name: COR_PROFILER



value: "{B7038F67-52FC-4DA2-AB02-969B3C1EDA03}"



- name: COR_PROFILER_PATH_32



value: "C:\\oneagent\\agent\\bin\\current\\windows-x86-32\\oneagentdotnet.dll"



- name: COR_PROFILER_PATH_64



value: "C:\\oneagent\\agent\\bin\\current\\windows-x86-64\\oneagentdotnet.dll"



#.NET Core



- name: CORECLR_ENABLE_PROFILING



value: "0x01"



- name: CORECLR_PROFILER



value: "{B7038F67-52FC-4DA2-AB02-969B3C1EDA03}"



- name: CORECLR_PROFILER_PATH_32



value: "C:\\oneagent\\agent\\bin\\current\\windows-x86-32\\oneagentdotnet.dll"



- name: CORECLR_PROFILER_PATH_64



value: "C:\\oneagent\\agent\\bin\\current\\windows-x86-64\\oneagentdotnet.dll"



- name: DT_AGENTACTIVE



value: "true"



- name: DT_BLOCKLIST



value: "powershell*"



volumeMounts:



- mountPath: "C:\\OneAgent"



name: oneagent



# initcontainer to download OneAgent



initContainers:



- name: install-oneagent



image: mcr.microsoft.com/windows/servercore:ltsc2019



command:



- powershell



args:



- |



Write-Host "Trustng all certificates..."



add-type @"



using System.Net;



using System.Security.Cryptography.X509Certificates;



public class TrustAllCertsPolicy : ICertificatePolicy {



public bool CheckValidationResult(



ServicePoint srvPoint, X509Certificate certificate,



WebRequest request, int certificateProblem) {



return true;



}



}



"@



[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy



Write-Host "Downloading agent..."



Invoke-WebRequest -Uri "$Env:DT_API_URL/v1/deployment/installer/agent/windows/paas/latest?Api-Token=$Env:DT_PAAS_TOKEN&$Env:DT_ONEAGENT_OPTIONS" -OutFile "installer.zip"



Write-Host "Unpacking agent..."



Expand-Archive -Path "installer.zip" -DestinationPath "C:\OneAgent" -Force



Write-Host "Configuring agent..."



$manifest = Get-Content "C:\OneAgent\manifest.json" | ConvertFrom-Json



$config = New-Item -Path "C:\OneAgent\agent\conf" -Name "standalone.conf" -Force



Add-Content -Path $config -Value "tenant $($manifest.tenantUUID)"



Add-Content -Path $config -Value "tenanttoken $($manifest.tenantToken)"



Add-Content -Path $config -Value "server $($manifest.communicationEndpoints -Join ';')"



Add-Content -Path $config -Value "storage C:\OneAgent"



Add-Content -Path $config -Value "loglevelcon NONE"



env:



- name: DT_API_URL



value: https://<your-environment-id>.live.dynatrace.com/api



- name: DT_PAAS_TOKEN



value: <Access token with PaaS integration scopes (Dynatrace -> Access tokens)>



- name: DT_ONEAGENT_OPTIONS



value: arch=default&include=dotnet



volumeMounts:



- mountPath: "C:\\OneAgent"



name: oneagent



# Make OneAgent available as a volume



volumes:



- name: oneagent



emptyDir: {}



selector:



matchLabels:



app: sample



---



apiVersion: v1



kind: Service



metadata:



name: sample



spec:



type: LoadBalancer



ports:



- protocol: TCP



port: 80



selector:



app: sample
```

* In the `# initContainer to download OneAgent` and `# Make OneAgent available as a volume` sections, add the `initContainer`, which will download OneAgent and make it available as a volume.
* The `# your application containers` section contains environment variables that enable monitoring of .NET Framework and .NET Core applications. They can be set at the same time. For .NET Core, the `COR_ prefix` changes to `CORECLR_`, for example `CORECLR_ENABLE_PROFILING`.

To report the correct memory limits in Kubernetes

1. You have to specify the limit in the deployment.

   ```
   spec:



   containers:



   ...



   resources:



   limits:



   memory: "32Gi"



   requests:



   memory: "4Gi"
   ```
2. You have to enable access to the Kubernetes API so that OneAgent can read that value.

## Update

Each time you want to leverage a new OneAgent version, you only need to redeploy your Pods. In runtime injections, OneAgent is downloaded and injected within an `initContainer`. By default, the latest version of OneAgent is downloaded, but you can control which OneAgent version is downloaded by specifying it in the download URL.

## Uninstall

To uninstall OneAgent from application-only monitoring

1. Remove the install-oneagent YAML from your deployment template.

   ```
   # your application containers



   containers:



   - name: customer-app



   image: tomcat



   env:



   - name: LD_PRELOAD



   value: /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so



   volumeMounts:



   - mountPath: /opt/dynatrace/oneagent



   name: oneagent



   # initContainer to download OneAgent



   initContainers:



   - name: install-oneagent



   image: alpine:3.8



   command:



   - /bin/sh



   args:



   - -c



   - ARCHIVE=$(mktemp) && wget -O $ARCHIVE "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_PAAS_TOKEN&$DT_ONEAGENT_OPTIONS" && unzip -o -d /opt/dynatrace/oneagent $ARCHIVE && rm -f $ARCHIVE



   env:



   - name: DT_API_URL



   value: https://<Your-environment-ID>.live.dynatrace.com/api



   - name: DT_PAAS_TOKEN



   value: <paastoken>



   - name: DT_ONEAGENT_OPTIONS



   value: flavor=<FLAVOR>&include=<TECHNOLOGY>



   volumeMounts:



   - mountPath: /opt/dynatrace/oneagent



   name: oneagent



   # Make OneAgent available as a volume



   volumes:



   - name: oneagent



   emptyDir: {}
   ```
2. Redeploy your application.