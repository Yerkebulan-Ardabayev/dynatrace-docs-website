---
title: Settings API - Built-in process monitoring rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-built-in-process-monitoring-rule
---

# Settings API - Built-in process monitoring rules schema table

# Settings API - Built-in process monitoring rules schema table

* Опубликовано 5 дек. 2023 г.

### Built-in process monitoring rules (`builtin:process.built-in-process-monitoring-rule)`

Включение или отключение встроенных правил мониторинга.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process.built-in-process-monitoring-rule` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST_GROUP` - Host Group  `environment` |

Получить схему через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process.built-in-process-monitoring-rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process.built-in-process-monitoring-rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process.built-in-process-monitoring-rule` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия **Read settings** (`settings.read`). О том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Не отслеживать процессы, если существует PHP-скрипт `-1` | boolean | Rule id: 1 | Required |
| Не отслеживать процессы, если имя EXE равно 'php-cgi' `-2` | boolean | Rule id: 2 | Required |
| Отслеживать процессы, если существует путь приложения ASP.NET Core `-3` | boolean | Rule id: 3 | Required |
| Отслеживать процессы, если имя EXE равно 'w3wp.exe' `-4` | boolean | Rule id: 4 | Required |
| Не отслеживать процессы, если имя EXE равно 'filebeat' `-49` | boolean | Rule id: 49 | Required |
| Не отслеживать процессы, если имя EXE равно 'metricbeat' `-50` | boolean | Rule id: 50 | Required |
| Не отслеживать процессы, если имя EXE равно 'packetbeat' `-51` | boolean | Rule id: 51 | Required |
| Не отслеживать процессы, если имя EXE равно 'auditbeat' `-52` | boolean | Rule id: 52 | Required |
| Не отслеживать процессы, если имя EXE равно 'heartbeat' `-53` | boolean | Rule id: 53 | Required |
| Не отслеживать процессы, если имя EXE равно 'functionbeat' `-54` | boolean | Rule id: 54 | Required |
| Не отслеживать процессы, если имя EXE равно 'yq' `-72` | boolean | Rule id: 72 | Required |
| Не отслеживать процессы, если связывание Go Binary равно 'static' `-47` | boolean | Rule id: 47 | Required |
| Отслеживать процессы, если имя EXE равно 'caddy' `-5` | boolean | Rule id: 5 | Required |
| Отслеживать процессы, если имя EXE равно 'influxd' `-6` | boolean | Rule id: 6 | Required |
| Отслеживать процессы, если имя EXE равно 'adapter' `-7` | boolean | Rule id: 7 | Required |
| Отслеживать процессы, если имя EXE равно 'auctioneer' `-8` | boolean | Rule id: 8 | Required |
| Отслеживать процессы, если имя EXE равно 'bbs' `-9` | boolean | Rule id: 9 | Required |
| Отслеживать процессы, если имя EXE равно 'cc-uploader' `-10` | boolean | Rule id: 10 | Required |
| Отслеживать процессы, если имя EXE равно 'doppler' `-11` | boolean | Rule id: 11 | Required |
| Отслеживать процессы, если имя EXE равно 'gorouter' `-12` | boolean | Rule id: 12 | Required |
| Отслеживать процессы, если имя EXE равно 'locket' `-13` | boolean | Rule id: 13 | Required |
| Отслеживать процессы, если имя EXE равно 'metron' `-14` | boolean | Rule id: 14 | Required |
| Отслеживать процессы, если имя EXE равно 'rep' `-16` | boolean | Rule id: 16 | Required |
| Отслеживать процессы, если имя EXE равно 'route-emitter' `-17` | boolean | Rule id: 17 | Required |
| Отслеживать процессы, если имя EXE равно 'route-registrar' `-18` | boolean | Rule id: 18 | Required |
| Отслеживать процессы, если имя EXE равно 'routing-api' `-19` | boolean | Rule id: 19 | Required |
| Отслеживать процессы, если имя EXE равно 'scheduler' `-20` | boolean | Rule id: 20 | Required |
| Отслеживать процессы, если имя EXE равно 'silk-daemon' `-21` | boolean | Rule id: 21 | Required |
| Отслеживать процессы, если имя EXE равно 'switchboard' `-22` | boolean | Rule id: 22 | Required |
| Отслеживать процессы, если имя EXE равно 'syslog\_drain\_binder' `-23` | boolean | Rule id: 23 | Required |
| Отслеживать процессы, если имя EXE равно 'tps-watcher' `-24` | boolean | Rule id: 24 | Required |
| Отслеживать процессы, если имя EXE равно 'trafficcontroller' `-25` | boolean | Rule id: 25 | Required |
| Не отслеживать процессы, если базовая директория приложения Node.js заканчивается на '/node\_modules/prebuild-install' `-26` | boolean | Rule id: 26 | Required |
| Не отслеживать процессы, если базовая директория приложения Node.js заканчивается на '/node\_modules/npm' `-27` | boolean | Rule id: 27 | Required |
| Не отслеживать процессы, если базовая директория приложения Node.js заканчивается на '/node\_modules/grunt' `-28` | boolean | Rule id: 28 | Required |
| Не отслеживать процессы, если базовая директория приложения Node.js заканчивается на '/node\_modules/typescript' `-29` | boolean | Rule id: 29 | Required |
| Не отслеживать процессы, если приложение Node.js равно 'yarn' `-45` | boolean | Rule id: 45 | Required |
| Не отслеживать процессы, если приложение Node.js равно 'corepack' `-68` | boolean | Rule id: 68 | Required |
| Не отслеживать процессы, если базовая директория приложения Node.js заканчивается на '/node\_modules/node-pre-gyp' `-32` | boolean | Rule id: 32 | Required |
| Не отслеживать процессы, если базовая директория приложения Node.js заканчивается на '/node\_modules/node-gyp' `-33` | boolean | Rule id: 33 | Required |
| Не отслеживать процессы, если базовая директория приложения Node.js заканчивается на '/node\_modules/gulp-cli' `-34` | boolean | Rule id: 34 | Required |
| Не отслеживать процессы, если скрипт Node.js равно 'bin/pm2' `-35` | boolean | Rule id: 35 | Required |
| Не отслеживать процессы, если приложение Cloud Foundry начинается с 'apps-manager-js' `-36` | boolean | Rule id: 36 | Required |
| Не отслеживать процессы, если имя EXE равно 'grootfs' `-55` | boolean | Rule id: 55 | Required |
| Не отслеживать процессы, если имя EXE равно 'tardis' `-56` | boolean | Rule id: 56 | Required |
| Не отслеживать процессы, если путь EXE начинается с '/tmp/buildpacks/' `-43` | boolean | Rule id: 43 | Required |
| Отслеживать процессы, если существует приложение Cloud Foundry `-37` | boolean | Rule id: 37 | Required |
| Не отслеживать процессы, если имя контейнера Kubernetes равно 'POD' `-38` | boolean | Rule id: 38 | Required |
| Не отслеживать процессы, если урезанный образ Docker содержит 'pause-amd64' `-39` | boolean | Rule id: 39 | Required |
| Не отслеживать процессы, если имя EXE равно 'oc' `-44` | boolean | Rule id: 44 | Required |
| Не отслеживать процессы, если имя EXE равно 'calico-node' `-58` | boolean | Rule id: 58 | Required |
| Не отслеживать процессы, если путь EXE равно '/usr/bin/piper' `-67` | boolean | Rule id: 67 | Required |
| Не отслеживать процессы, если имя контейнера Kubernetes равно 'cassandra-operator' `-69` | boolean | Rule id: 69 | Required |
| Не отслеживать процессы, если имя EXE содержит 'UiPath' `-70` | boolean | Rule id: 70 | Required |
| Не отслеживать процессы, если имя EXE равно 'openhandlecollector.exe' `-71` | boolean | Rule id: 71 | Required |
| Отслеживать процессы, если существует пространство имён Kubernetes `-40` | boolean | Rule id: 40 | Required |
| Отслеживать процессы, если существует имя контейнера `-41` | boolean | Rule id: 41 | Required |
| Не отслеживать процессы, если путь EXE равно '/opt/cni/bin/host-local' `-46` | boolean | Rule id: 46 | Required |
| Не отслеживать процессы, если имя EXE начинается с 'mqsi' `-48` | boolean | Rule id: 48 | Required |
| Не отслеживать процессы, если файл Java JAR начинается с 'org.eclipse.equinox.launcher' `-57` | boolean | Rule id: 57 | Required |
| Не отслеживать процессы, если имя EXE равно 'casclient.exe' `-59` | boolean | Rule id: 59 | Required |
| Не отслеживать процессы, если имя файла JAR равно 'dynatrace\_ibm\_mq\_connector.jar' `-60` | boolean | Rule id: 60 | Required |
| Не отслеживать процессы, если имя EXE содержит 'Agent.Worker' `-61` | boolean | Rule id: 61 | Required |
| Не отслеживать процессы, если DLL приложения ASP.NET Core содержит 'Agent.Worker' `-62` | boolean | Rule id: 62 | Required |
| Не отслеживать процессы, если имя EXE содержит 'Agent.Listener' `-63` | boolean | Rule id: 63 | Required |
| Не отслеживать процессы, если DLL приложения ASP.NET Core содержит 'Agent.Listener' `-64` | boolean | Rule id: 64 | Required |
| Не отслеживать процессы, если имя EXE равно 'FlexNetJobExecutorService' `-65` | boolean | Rule id: 65 | Required |
| Не отслеживать процессы, если имя EXE равно 'FlexNetMaintenanceRemotingService' `-66` | boolean | Rule id: 66 | Required |
| Не отслеживать процессы, если скрипт Python равно 'pip' `-73` | boolean | Rule id: 73 | Required |
| Не отслеживать процессы, если скрипт Python равно 'hatch' `-74` | boolean | Rule id: 74 | Required |
| Не отслеживать процессы, если скрипт Python равно 'wheel' `-75` | boolean | Rule id: 75 | Required |
| Не отслеживать процессы, если скрипт Python равно 'yum' `-76` | boolean | Rule id: 76 | Required |
| Не отслеживать процессы, если скрипт Python равно 'jupyter' `-77` | boolean | Rule id: 77 | Required |
| Не отслеживать процессы, если скрипт Python равно 'conda' `-78` | boolean | Rule id: 78 | Required |
| Не отслеживать процессы, если скрипт Python равно 'ansible' `-79` | boolean | Rule id: 79 | Required |
| Не отслеживать процессы, если скрипт Python равно 'openstack' `-80` | boolean | Rule id: 80 | Required |
| Не отслеживать процессы, если скрипт Python равно 'aws' `-81` | boolean | Rule id: 81 | Required |
| Не отслеживать процессы, если скрипт Python равно 'az' `-82` | boolean | Rule id: 82 | Required |
| Не отслеживать процессы, если скрипт Python равно 'gcloud' `-83` | boolean | Rule id: 83 | Required |
| Не отслеживать процессы, если аргументы командной строки содержат 'forever/bin/monitor' `-84` | boolean | Rule id: 84 | Required |
| Не отслеживать процесс, если главный класс Java содержит 'ActiveGateCommandLineTool' `-85` | boolean | Rule id: 85 | Required |
| Не отслеживать процессы, если скрипт Python содержит 'supervisord' `-86` | boolean | Rule id: 86 | Required |