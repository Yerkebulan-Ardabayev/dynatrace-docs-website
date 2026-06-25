---
title: Settings API - Built-in process monitoring rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-built-in-process-monitoring-rule
scraped: 2026-05-12T11:49:14.678424
---

# Settings API - Built-in process monitoring rules schema table

# Settings API - Built-in process monitoring rules schema table

* Published Dec 05, 2023

### Built-in process monitoring rules (`builtin:process.built-in-process-monitoring-rule)`

Enable or disable built-in monitoring rules.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process.built-in-process-monitoring-rule` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process.built-in-process-monitoring-rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process.built-in-process-monitoring-rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process.built-in-process-monitoring-rule` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Do not monitor processes if PHP script exists `-1` | boolean | Rule id: 1 | Required |
| Do not monitor processes if EXE name equals 'php-cgi' `-2` | boolean | Rule id: 2 | Required |
| Do monitor processes if ASP.NET Core application path exists `-3` | boolean | Rule id: 3 | Required |
| Do monitor processes if EXE name equals 'w3wp.exe' `-4` | boolean | Rule id: 4 | Required |
| Do not monitor processes if EXE name equals 'filebeat' `-49` | boolean | Rule id: 49 | Required |
| Do not monitor processes if EXE name equals 'metricbeat' `-50` | boolean | Rule id: 50 | Required |
| Do not monitor processes if EXE name equals 'packetbeat' `-51` | boolean | Rule id: 51 | Required |
| Do not monitor processes if EXE name equals 'auditbeat' `-52` | boolean | Rule id: 52 | Required |
| Do not monitor processes if EXE name equals 'heartbeat' `-53` | boolean | Rule id: 53 | Required |
| Do not monitor processes if EXE name equals 'functionbeat' `-54` | boolean | Rule id: 54 | Required |
| Do not monitor processes if EXE name equals 'yq' `-72` | boolean | Rule id: 72 | Required |
| Do not monitor processes if Go Binary Linkage equals 'static' `-47` | boolean | Rule id: 47 | Required |
| Do monitor processes if EXE name equals 'caddy' `-5` | boolean | Rule id: 5 | Required |
| Do monitor processes if EXE name equals 'influxd' `-6` | boolean | Rule id: 6 | Required |
| Do monitor processes if EXE name equals 'adapter' `-7` | boolean | Rule id: 7 | Required |
| Do monitor processes if EXE name equals 'auctioneer' `-8` | boolean | Rule id: 8 | Required |
| Do monitor processes if EXE name equals 'bbs' `-9` | boolean | Rule id: 9 | Required |
| Do monitor processes if EXE name equals 'cc-uploader' `-10` | boolean | Rule id: 10 | Required |
| Do monitor processes if EXE name equals 'doppler' `-11` | boolean | Rule id: 11 | Required |
| Do monitor processes if EXE name equals 'gorouter' `-12` | boolean | Rule id: 12 | Required |
| Do monitor processes if EXE name equals 'locket' `-13` | boolean | Rule id: 13 | Required |
| Do monitor processes if EXE name equals 'metron' `-14` | boolean | Rule id: 14 | Required |
| Do monitor processes if EXE name equals 'rep' `-16` | boolean | Rule id: 16 | Required |
| Do monitor processes if EXE name equals 'route-emitter' `-17` | boolean | Rule id: 17 | Required |
| Do monitor processes if EXE name equals 'route-registrar' `-18` | boolean | Rule id: 18 | Required |
| Do monitor processes if EXE name equals 'routing-api' `-19` | boolean | Rule id: 19 | Required |
| Do monitor processes if EXE name equals 'scheduler' `-20` | boolean | Rule id: 20 | Required |
| Do monitor processes if EXE name equals 'silk-daemon' `-21` | boolean | Rule id: 21 | Required |
| Do monitor processes if EXE name equals 'switchboard' `-22` | boolean | Rule id: 22 | Required |
| Do monitor processes if EXE name equals 'syslog\_drain\_binder' `-23` | boolean | Rule id: 23 | Required |
| Do monitor processes if EXE name equals 'tps-watcher' `-24` | boolean | Rule id: 24 | Required |
| Do monitor processes if EXE name equals 'trafficcontroller' `-25` | boolean | Rule id: 25 | Required |
| Do not monitor processes if Node.js application base directory ends with '/node\_modules/prebuild-install' `-26` | boolean | Rule id: 26 | Required |
| Do not monitor processes if Node.js application base directory ends with '/node\_modules/npm' `-27` | boolean | Rule id: 27 | Required |
| Do not monitor processes if Node.js application base directory ends with '/node\_modules/grunt' `-28` | boolean | Rule id: 28 | Required |
| Do not monitor processes if Node.js application base directory ends with '/node\_modules/typescript' `-29` | boolean | Rule id: 29 | Required |
| Do not monitor processes if Node.js application equals 'yarn' `-45` | boolean | Rule id: 45 | Required |
| Do not monitor processes if Node.js application equals 'corepack' `-68` | boolean | Rule id: 68 | Required |
| Do not monitor processes if Node.js application base directory ends with '/node\_modules/node-pre-gyp' `-32` | boolean | Rule id: 32 | Required |
| Do not monitor processes if Node.js application base directory ends with '/node\_modules/node-gyp' `-33` | boolean | Rule id: 33 | Required |
| Do not monitor processes if Node.js application base directory ends with '/node\_modules/gulp-cli' `-34` | boolean | Rule id: 34 | Required |
| Do not monitor processes if Node.js script equals 'bin/pm2' `-35` | boolean | Rule id: 35 | Required |
| Do not monitor processes if Cloud Foundry application begins with 'apps-manager-js' `-36` | boolean | Rule id: 36 | Required |
| Do not monitor processes if EXE name equals 'grootfs' `-55` | boolean | Rule id: 55 | Required |
| Do not monitor processes if EXE name equals 'tardis' `-56` | boolean | Rule id: 56 | Required |
| Do not monitor processes if EXE path begins with '/tmp/buildpacks/' `-43` | boolean | Rule id: 43 | Required |
| Do monitor processes if Cloud Foundry application exists `-37` | boolean | Rule id: 37 | Required |
| Do not monitor processes if Kubernetes container name equals 'POD' `-38` | boolean | Rule id: 38 | Required |
| Do not monitor processes if Docker stripped image contains 'pause-amd64' `-39` | boolean | Rule id: 39 | Required |
| Do not monitor processes if EXE name equals 'oc' `-44` | boolean | Rule id: 44 | Required |
| Do not monitor processes if EXE name equals 'calico-node' `-58` | boolean | Rule id: 58 | Required |
| Do not monitor processes if EXE path equals '/usr/bin/piper' `-67` | boolean | Rule id: 67 | Required |
| Do not monitor processes if Kubernetes container name equals 'cassandra-operator' `-69` | boolean | Rule id: 69 | Required |
| Do not monitor processes if EXE name contains 'UiPath' `-70` | boolean | Rule id: 70 | Required |
| Do not monitor processes if EXE name equals 'openhandlecollector.exe' `-71` | boolean | Rule id: 71 | Required |
| Do monitor processes if Kubernetes namespace exists `-40` | boolean | Rule id: 40 | Required |
| Do monitor processes if container name exists `-41` | boolean | Rule id: 41 | Required |
| Do not monitor processes if EXE path equals '/opt/cni/bin/host-local' `-46` | boolean | Rule id: 46 | Required |
| Do not monitor processes if EXE name begins with 'mqsi' `-48` | boolean | Rule id: 48 | Required |
| Do not monitor processes if Java JAR file begins with 'org.eclipse.equinox.launcher' `-57` | boolean | Rule id: 57 | Required |
| Do not monitor processes if EXE name equals 'casclient.exe' `-59` | boolean | Rule id: 59 | Required |
| Do not monitor processes if JAR file name equals 'dynatrace\_ibm\_mq\_connector.jar' `-60` | boolean | Rule id: 60 | Required |
| Do not monitor processes if EXE name contains 'Agent.Worker' `-61` | boolean | Rule id: 61 | Required |
| Do not monitor processes if ASP.NET Core application DLL contains 'Agent.Worker' `-62` | boolean | Rule id: 62 | Required |
| Do not monitor processes if EXE name contains 'Agent.Listener' `-63` | boolean | Rule id: 63 | Required |
| Do not monitor processes if ASP.NET Core application DLL contains 'Agent.Listener' `-64` | boolean | Rule id: 64 | Required |
| Do not monitor processes if EXE name equals 'FlexNetJobExecutorService' `-65` | boolean | Rule id: 65 | Required |
| Do not monitor processes if EXE name equals 'FlexNetMaintenanceRemotingService' `-66` | boolean | Rule id: 66 | Required |
| Do not monitor processes if EXE name equals 'pip' `-73` | boolean | Rule id: 73 | Required |
| Do not monitor processes if EXE name equals 'hatch' `-74` | boolean | Rule id: 74 | Required |
| Do not monitor processes if EXE name equals 'wheel' `-75` | boolean | Rule id: 75 | Required |
| Do not monitor processes if EXE name equals 'yum' `-76` | boolean | Rule id: 76 | Required |
| Do not monitor processes if EXE name equals 'jupyter' `-77` | boolean | Rule id: 77 | Required |
| Do not monitor processes if EXE name equals 'conda' `-78` | boolean | Rule id: 78 | Required |
| Do not monitor processes if EXE name equals 'ansible' `-79` | boolean | Rule id: 79 | Required |
| Do not monitor processes if EXE name equals 'openstack' `-80` | boolean | Rule id: 80 | Required |
| Do not monitor processes if EXE name equals 'aws' `-81` | boolean | Rule id: 81 | Required |
| Do not monitor processes if EXE name equals 'az' `-82` | boolean | Rule id: 82 | Required |
| Do not monitor processes if EXE name equals 'gcloud' `-83` | boolean | Rule id: 83 | Required |
| Do not monitor processes if command line arguments contain 'forever/bin/monitor' `-84` | boolean | Rule id: 84 | Required |