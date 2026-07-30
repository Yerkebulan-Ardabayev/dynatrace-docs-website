---
title: Свойства конфигурации и параметры ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate
---

# Свойства конфигурации и параметры ActiveGate

# Свойства конфигурации и параметры ActiveGate

* Чтение 17 мин
* Обновлено 16 июля 2026 г.

## Перед началом работы

Ознакомьтесь с основными концепциями конфигурации ActiveGate, связанными с файлами свойств.

ActiveGates на основе хоста, то есть ActiveGates Module: OTLP Ingest, развёрнутые стандартным способом с помощью установщика, и контейнеризованные ActiveGates используют одни и те же свойства конфигурации, хранящиеся в одних и тех же файлах конфигурации. Однако фактические значения этих свойств могут различаться, а способы их задания и изменения отличаются: ActiveGates на основе хоста настраиваются непосредственно на хосте, где запущен ActiveGate, тогда как контейнеризованные ActiveGates настраиваются через механизм конфигурации вашей облачной платформы.

* [Как развернуть и настроить контейнеризованный ActiveGate в Kubernetes](/managed/ingest-from/dynatrace-activegate/activegate-in-container "Deploy a containerized ActiveGate.")

## Основные правила работы с конфигурацией ActiveGate

### Файлы конфигурации ActiveGate

Многие параметры конфигурации ActiveGate (например, настройки подключения и прокси, шифры или параметры дампа памяти) хранятся в файлах свойств `config.properties` и `custom.properties`, которые расположены в **[каталоге конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.")**.
Свойства, перечисленные в файлах свойств, применимы как к Environment ActiveGates, так и к Cluster ActiveGates.

Файлы `config.properties` и `custom.properties` разделены на **секции**. Имя каждой секции заключено в квадратные скобки, например:

```
[collector]



MSGrouter = true



restInterface = true



DumpSupported = false
```

### config.properties

Файл конфигурации `config.properties` содержит параметры установки ActiveGate по умолчанию и не предназначен для ручного редактирования.

Этот файл конфигурации перезаписывается при каждом обновлении ActiveGate.

### custom.properties

Параметры, хранящиеся в `custom.properties`, переопределяют соответствующие параметры из `config.properties`, а сам файл копируется в новую версию ActiveGate в процессе обновления.

Файлы конфигурации разделены на `[секции]`, обозначаемые квадратными скобками.  
Чтобы задать пользовательские параметры в `custom.properties`, нужно указать имена секций и добавить в них соответствующие свойства.

Файл `config.txt` можно использовать как справочник при добавлении пользовательских параметров в `custom.properties`. Файл `config.txt`, также расположенный в каталоге конфигурации ActiveGate, не используется ActiveGate, однако содержит справочный список возможных свойств конфигурации.
Как вариант, можно найти нужную секцию в файле `config.properties`, а затем скопировать заголовок секции вместе с именами нужных свойств в `custom.properties`.  
После этого можно изменить записи в секции по мере необходимости.

### launcheruserconfig.conf

Launcher ActiveGate, это процесс-сторож, запускающий виртуальную машину Java для вашего ActiveGate.
Конфигурация launcher хранится в файле `launcheruserconfig.conf`, в **[каталоге конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.")**. Файл содержит свойства launcher и параметры, передаваемые виртуальной машине Java.

Для Remote Plugin Module (RPM) файл `launcheruserconfig.conf` должен находиться в каталоге `/var/lib/dynatrace/remotepluginmodule/agent/conf/`.

Файл `launcheruserconfig.conf` сохраняется при обновлениях ActiveGate.

### Перезапуск ActiveGate

При изменении конфигурации ActiveGate нужно [перезапустить основной сервис ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux."), чтобы изменения вступили в силу.

## Настройка ActiveGate с помощью `agctl`

ActiveGate версии 1.333+

Начиная с версии 1.333, для управления конфигурацией ActiveGate можно использовать интерфейс командной строки `agctl`. Инструмент `agctl` упрощает управление конфигурацией благодаря:

* **Специализированным командам** для типовых задач конфигурирования: задание прокси-эндпоинтов, управление SSL-сертификатами, настройка хранилищ доверия и назначение групп ActiveGate.
* **Универсальной команде property**, позволяющей настраивать любое свойство в файле `custom.properties` с помощью команды [agctl property](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#property "Learn how to use agctl to configure and manage ActiveGate from the command line") для свойств, у которых нет специализированных команд.

Подробное описание всех доступных команд, параметров и примеров см. в разделе [agctl command-line interface](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface "Learn how to use agctl to configure and manage ActiveGate from the command line").

## Пример использования `agctl` для управления конфигурацией ActiveGate

ActiveGate версии 1.333+

В этом примере рассмотрено изменение пути очереди данных журналов на ActiveGate на основе хоста.

Для Environment на основе хоста или Cluster ActiveGate путь, используемый для очереди данных журналов, можно изменить с помощью [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#property "Learn how to use agctl to configure and manage ActiveGate from the command line"). В следующих шагах в качестве примера нового пути используется `/var/disk_queue`.

1. Ознакомьтесь с [предварительными требованиями для работы с интерфейсом командной строки `agctl`](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#prerequisites "Learn how to use agctl to configure and manage ActiveGate from the command line").
2. Подключитесь к хосту по SSH.
3. Остановите сервис ActiveGate:

```
systemctl stop dynatracegateway
```

4. Прочитайте текущий путь:

```
agctl property get --section=generic_ingest --key=disk_queue_path
```

5. Убедитесь, что целевой каталог `/var/disk_queue` существует, доступен для записи и имеет не менее `disk_queue_max_size_mb` МБ свободного дискового пространства.
6. Измените путь:

```
agctl property set --section=generic_ingest --key=disk_queue_path --value=/var/disk_queue
```

7. Необязательно: удалите каталог, на который указывал старый путь.
8. Запустите сервис ActiveGate:

```
systemctl start dynatracegateway
```

## Ограничения памяти ActiveGate

Ограничения использования памяти для ActiveGate задаются в файле конфигурации launcher `launcheruserconfig.conf` с помощью следующих свойств:

* `-java.xmx.relative_part`, процент доступной оперативной памяти
* `-java.xmx.absolute_part`, абсолютное значение объёма памяти в МБ

Конфигурация может включать любую комбинацию этих свойств, и итоговый лимит памяти равен сумме абсолютной части и относительной части (вычисляемой на основе доступной оперативной памяти).

**Примеры:**

```
# Xmx = 0 MB + 83% of available RAM



-java.xmx.absolute_part=0



-java.xmx.relative_part=83
```

```
# Xmx = 2000 MB + 83% of available RAM



-java.xmx.absolute_part=2000



-java.xmx.relative_part=83
```

```
# Xmx = 2000 MB + 0 MB



-java.xmx.absolute_part=2000



-java.xmx.relative_part=0
```

## Диапазон портов heartbeat для ActiveGate

Launcher ActiveGate отслеживает процесс ActiveGate через локальный порт heartbeat. Этот порт выбирается launcher из заранее заданного диапазона портов, указанного в конфигурации launcher. Launcher находит свободный порт в указанном диапазоне и затем передаёт номер порта процессу ActiveGate.

По умолчанию для мониторинга heartbeat launcher использует порты выше 50000. В некоторых развёртываниях может потребоваться настроить другие порты для этой цели. Чтобы задать диапазон портов, который должен использовать launcher ActiveGate, нужно добавить или изменить свойство `-healthcheck.heartbeat.portrange` в файле конфигурации launcher `launcheruserconfig.conf`, как показано в примере ниже.

```
-healthcheck.heartbeat.portrange=60100:60200
```

## Пользовательские параметры для Java-процесса ActiveGate

Чтобы передать пользовательские параметры Java-процессу ActiveGate, нужно указать их в файле конфигурации launcher `launcheruserconfig.conf`:

* Все строки после `-arguments_section.jvm` передаются как аргументы JVM. Таким образом, с помощью опций `-D` можно задать аргументы для ActiveGate.

Например:

```
# Xmx settings 80% of available RAM + 0 MB



-java.xmx.absolute_part=0



-java.xmx.relative_part=83



-healthcheck.heartbeat.portrange=60100:60200



-arguments_section.jvm



-Dsomecustomproperty=value
```

## Модули ActiveGate

Различные функциональные возможности ActiveGate называются **[модулями](/managed/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Learn the capabilities and uses of ActiveGate.")**. При установке ActiveGate для конкретной [цели](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") устанавливается или включается определённый набор модулей.

Модуль активен, если соответствующее свойство конфигурации указано со значением `true` в разделе конфигурации, посвящённом этому модулю. Однако включить все модули через `custom.properties`, просто изменив значение свойства, нельзя: если ActiveGate установлен в качестве приватного Synthetic-локейшна или для мониторинга мейнфрейма, а цель ActiveGate нужно изменить, необходимо переустановить ActiveGate.

Активные модули перечислены в разделе **Deployment Status** > **ActiveGates**.

Каждый модуль имеет соответствующий раздел в конфигурации

Помимо разделов конфигурации, посвящённых конкретным функциям ActiveGate, каждый модуль ActiveGate имеет собственный раздел в файлах конфигурации ActiveGate. Параметры, указанные в этом разделе, применяются именно к данному модулю. Это касается, например, настроек прокси. Однако не все параметры можно таким образом повторить и задать для модуля отдельно: каждый раздел модуля принимает лишь ограниченный набор опций. **НЕ копируйте параметры конфигурации между разделами без явного указания на это.**

### Управление модулями с помощью `agctl`

ActiveGate версии 1.333+

Для включения или отключения модулей ActiveGate можно использовать [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Learn how to use agctl to configure and manage ActiveGate from the command line").

После включения или отключения модулей через `agctl` необходимо [перезапустить ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux."), чтобы изменения вступили в силу.

#### Включение модулей

```
# Enable a single module



agctl modules enable metrics_ingest



# Enable multiple modules (comma-separated, no spaces)



agctl modules enable MSGrouter,metrics_ingest,otlp_ingest
```

#### Отключение модулей

```
# Disable a single module



agctl modules disable synthetic



# Disable multiple modules



agctl modules disable aws_monitoring,azure_monitoring
```

## Модуль: AWS

Мониторинг AWS  
**Раздел: [aws\_monitoring]**

| Свойство | Описание |
| --- | --- |
| `aws_monitoring_enabled` | Включает модуль [мониторинга AWS](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services."). Возможные значения: `true` или `false`. |
| `aws_default_region` | Задаёт регион по умолчанию для модуля [мониторинга AWS](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services."). Возможные значения: допустимые коды регионов AWS. Например: `us-east-1` |
| `aws_client_regions` | Задаёт регионы для модуля [мониторинга AWS](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services."). Возможные значения: список допустимых кодов регионов AWS, разделённых символом `;`. Например: `us-east-1;eu-central-1` |

## Модуль: Azure

Мониторинг Microsoft Azure  
**Раздел: [azure\_monitoring]**

| Свойство | Описание |
| --- | --- |
| `azure_monitoring_enabled` | Включает модуль [Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace."). Возможные значения: `true` или `false`. |

## Модуль: Cloud Foundry

Мониторинг Cloud Foundry  
**Раздел: [cloudfoundry\_monitoring]**

| Свойство | Описание |
| --- | --- |
| `cloudfoundry_monitoring_enabled` | Включает модуль [Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Enable monitoring on your Cloud Foundry foundations."). Возможные значения: `true` или `false`. |

Этот раздел может содержать настройки прокси для связи с Cloud Foundry. Если раздел содержит `proxy-off = true`, прокси для связи с Cloud Foundry не используется. Если раздел содержит свойство `proxy-host`, этот прокси используется для мониторинга Cloud Foundry вместо прокси, указанного в `[http.client.external]`.

ActiveGate версии 1.247 и ниже. Если в файле `custom.properties` есть раздел `[cloudfoundry_monitoring]`, необходимо также добавить раздел `[http.client.external]`, в котором указываются все остальные параметры связи для коммуникации с Cloud Foundry.

[Настройка прокси только для мониторинга Cloud Foundry](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#set-up-proxy-only-for-cloud-foundry-monitoring "Learn how to configure ActiveGate properties to set up a proxy.")

## Модуль: Kubernetes

Мониторинг платформы Kubernetes  
**Раздел: [kubernetes\_monitoring]**

| Свойство | Описание |
| --- | --- |
| `kubernetes_monitoring_enabled` | Включает модуль [мониторинга платформы Kubernetes](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet."). Возможные значения: `true` или `false`. |

Этот раздел может содержать настройки прокси для связи с Kubernetes, а также другие параметры тонкой настройки связи для мониторинга платформы Kubernetes.  
Если раздел содержит `proxy-off = true`, прокси для связи с Kubernetes не используется. Если раздел содержит свойство `proxy-host`, этот прокси используется для мониторинга платформы Kubernetes вместо прокси, указанного в `[http.client.external]`.

ActiveGate версии 1.247 и ниже. Если в файле `custom.properties` есть раздел `[kubernetes_monitoring]`, необходимо также добавить раздел `[http.client.external]`, в котором указываются все остальные параметры связи для коммуникации с Kubernetes.

[Настройка прокси только для мониторинга платформы Kubernetes](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#set-up-proxy-only-for-kubernetes-monitoring "Learn how to configure ActiveGate properties to set up a proxy.")

## Модуль: Log Monitoring

**Раздел: [log\_analytics\_collector]**

| Свойство | Описание |
| --- | --- |
| `log_analytics_collector_enabled` | Включает модуль [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more."). Возможные значения: `true` или `false`. |

**Раздел: [generic\_ingest]**

Специально для Log Monitoring: при настройке API для приёма логов можно задать параметры очереди данных журналов. Можно указать временную папку, в которой будут храниться данные журналов в очереди. По умолчанию используется временная папка, настроенная в системе на текущий момент (см. [директории ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.")). Также можно изменить максимальный размер очереди в этой папке (размер по умолчанию, 300 МБ).

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `disk_queue_path` | Текущая системная временная папка | Задаёт путь к временной папке, в которой будут храниться данные журналов в очереди. |
| `disk_queue_max_size_mb` | 300 МБ | Задаёт максимальный размер данных журналов в очереди, которые можно сохранить во временной папке. |

## Модуль: VMware

Мониторинг VMware  
**Раздел: [vmware\_monitoring]**

| Свойство | Описание |
| --- | --- |
| `vmware_monitoring_enabled` | Включает модуль [мониторинга VMware](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace."). Возможные значения: `true` или `false`. |

## Модуль: Database insights

Анализ базы данных Oracle  
**Раздел: [dbAgent]**

| Свойство | Описание |
| --- | --- |
| `dbAgent_enabled` | Включает модуль [анализа базы данных Oracle](/managed/observe/infrastructure-observability/database-services-classic/database-insights "Learn how to extend your database monitoring to the database infrastructure layer."). Возможные значения: `true` или `false`. |

## Модуль: Extensions

**Раздел: [extension\_controller]**

| Свойство | Описание |
| --- | --- |
| `extension_controller_enabled` | Включает фреймворк Extensions. Возможные значения: `true` или `false`. |

## Модуль: zRemote

Установка модуля zRemote для мониторинга z/OS  
**Раздел: [zremote]**

| Свойство | Описание |
| --- | --- |
| `zremote_enabled` | Включает [модуль zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring."). Возможные значения: `true` или `false`. |

## Module: Synthetic

Synthetic monitors из приватных Synthetic locations  
**Section: [synthetic]**

Настройки прокси для Synthetic Monitoring. Если этот раздел содержит `proxy-off = true`, прокси для Synthetic Monitoring не используется. Если раздел содержит свойство `proxy-host`, оно задаёт прокси для Synthetic Monitoring вместо прокси, указанного в `[http.client.external]` (или в `[http.client]`, если `[http.client.external]` не задан).

Если в файле `custom.properties` есть раздел `[synthetic]`, можно добавить раздел `[http.client.external]`, в котором указываются все остальные параметры связи для Synthetic Monitoring. Также можно задать оставшиеся параметры связи в разделе `[http.client]`.

ActiveGate версии 1.247 и ниже. Однако, если раздел `[http.client.external]` создан, в нём нужно указать все параметры связи. Иначе параметры связи для отслеживаемых сред (Cloud Foundry, Kubernetes или Synthetic Monitoring) сбросятся до заводских значений по умолчанию.

Подробнее о свойствах, связанных с прокси, для ActiveGate с поддержкой Synthetic см. в разделе [Set up a proxy for private synthetic monitoring](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.").

Изменение свойства `synthetic_enabled` работает только в том случае, если ActiveGate установлен для [запуска Synthetic monitors из приватной location](/managed/ingest-from/dynatrace-activegate#synthetic "Understand the basic concepts related to ActiveGate."). Если ActiveGate установлен для [маршрутизации трафика, мониторинга облачных сред или мониторинга удалённых технологий с расширениями](/managed/ingest-from/dynatrace-activegate#route "Understand the basic concepts related to ActiveGate.") либо для [мониторинга мейнфреймов](/managed/ingest-from/dynatrace-activegate#mainframe "Understand the basic concepts related to ActiveGate."), нужно переустановить ActiveGate для использования с Synthetic Monitoring. Подробнее см. в разделе [Create a private Synthetic location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").

Если значение содержит запятую (`,`), перед ней нужно добавить экранирующий обратный слеш (`\`).

Пример: `proxy-password = foo\,bar`

| Property | Default value | Description |
| --- | --- | --- |
| `synthetic_enabled` | `false` в режиме развёртывания **Default**  `true` в режиме развёртывания **Synthetic monitoring** | Включает запуск monitors из приватных Synthetic locations на ActiveGate. |
| `synthetic_autoinstall` | `true` для автоматического обновления Synthetic engine | Автоматически устанавливается в `true` при установке ActiveGate с поддержкой Synthetic. |
| `proxy-server` | unset | Адрес прокси-сервера |
| `proxy-port` | unset | Порт прокси (числовой) |
| `proxy-user` | unset | Имя пользователя прокси (необязательно) |
| `proxy-password` | unset | Пароль прокси (необязательно)  Пароль, указанный в свойстве `proxy-password`, обфусцируется после перезапуска ActiveGate, и обфусцированное значение сохраняется в свойстве `proxy-password-encr`. **Примечание**: если запятая должна быть частью значения, её нужно экранировать одним обратным слешем. Например, `proxy-password = foo\,bar`. |
| `proxy-off` | unset | Отключает проксирование при связи ActiveGate с тестируемым ресурсом. |
| `proxy-non-proxy-hosts` | unset | Не использовать прокси при связи с этими хостами. |
| `chromium_repo` | unset  Указывает репозиторий пользовательских пакетов браузера на HTTP-сервере. Пример: `https://172.18.0.100/chromium-repo` Работает только если оба свойства `synthetic_autoinstall` и `synthetic_autoupgrade_chromium` установлены в `true`. | Включает автообновление браузера из [пользовательского репозитория](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Learn how to create a private location for synthetic monitoring."). |

Не рекомендуется вручную изменять значение свойства `synthetic_autoupgrade_chromium` в `custom.properties`, так как внесённые изменения могут быть перезаписаны.

Свойство `synthetic_autoupgrade_chromium` для автообновления браузера можно задать на уровне location (для locations с Environment ActiveGates) либо [через веб-интерфейс](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser "Analyze and manage capacity usage at your private Synthetic locations."), либо с помощью вызова API [PUT a location](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/put-a-location "Update a private synthetic location via the Synthetic v2 API.") из Synthetic locations API v2. Для Cluster ActiveGates это свойство можно настроить через вызов API [PUT a location (Dynatrace Managed)](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/put-a-location "Update a private Synthetic location via the Synthetic API v2 in Dynatrace Managed.") из Cluster API v2. Для ActiveGates, не назначенных ни одной location, это свойство не определено. Для ActiveGates, назначенных location, значение по умолчанию равно `true`.

## Module: Beacon forwarder

Использование ActiveGate для Real User Monitoring  
**Section: [beacon\_forwarder]**

| Property | Description |
| --- | --- |
| `beacon_forwarder_enabled` | Включает [модуль Beacon forwarder](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server."). Возможные значения: `true` или `false`. |

## Module: HTTP Metric API

Metric ingestion, простой способ отправлять произвольные пользовательские метрики в Dynatrace  
**Section: [metrics\_ingest]**

| Property | Description |
| --- | --- |
| `metrics_ingest_enabled` | Включает модуль HTTP Metric API, который обеспечивает [metric ingestion](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace."). Возможные значения: `true` или `false`. |

## Module: Memory dumps

Запуск и загрузка memory dumps  
**Section: [collector]**

| Property | Description |
| --- | --- |
| `DumpSupported` | Включает [модуль memory dumps](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate."). Возможные значения: `true` или `false`. |

Когда в приложении возникают утечки памяти или высокая интенсивность создания объектов, важно получать memory dumps для анализа этих проблем. В production-средах это часто затруднено, если нет возможности войти в среду и нет других способов запустить сбор дампов. Dynatrace позволяет как запускать сбор, так и безопасно скачивать memory dumps в любой удобный инструмент анализа.  
См. [Configure ActiveGate for memory dump storage](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate.").

## Module: OneAgent routing

ActiveGate знает о структуре вашей среды Dynatrace в реальном времени и маршрутизирует сообщения от OneAgents на нужные серверные endpoints. Модуль обеспечивает маршрутизацию сообщений, буферизацию, сжатие, аутентификацию и доступ к изолированным сетям.  
**Section: [collector]**

| Property | Description |
| --- | --- |
| `MSGrouter` | Включает модуль маршрутизации OneAgent, который перенаправляет трафик OneAgent и других ActiveGate через Dynatrace. Возможные значения: `true` или `false`. |

## Module: OTLP Ingest

**Section: [otlp\_ingest]**  
Этот модуль создаёт на ActiveGate endpoints, которые принимают данные трассировки OpenTelemetry (traces и spans), метрики и логи в формате OTLP. Подробнее см. в разделе [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

| Property | Description |
| --- | --- |
| `otlp_ingest_enabled` | Включает модуль OTLP ingest, который обеспечивает приём [traces](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") и [metrics](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") OpenTelemetry. Возможные значения: `true` или `false`. |

## Module: REST API

**Section: [collector]**  
Через ActiveGate можно получить доступ к [Dynatrace API](/managed/dynatrace-api "Find out what you need to use the Dynatrace API."). ActiveGate поддерживает вызовы всех configuration и environment endpoints Dynatrace API в версиях v1 и v2. Для доступа к Dynatrace API через ActiveGate нужно использовать URL следующего формата: `https://{your-ActiveGate-domain}/e/{your-environment-id}/api/...`

| Property | Description |
| --- | --- |
| `restInterface` | Включает модуль REST API, который обеспечивает доступ к Dynatrace API по REST. Возможные значения: `true` или `false`. |

## Module: debugging

**Section: [debugging]**  
Через ActiveGate можно получить доступ к данным на уровне кода, необходимым для быстрого поиска и устранения неисправностей в любой среде, от разработки до production.

| Property | Description |
| --- | --- |
| `debugging_enabled` | Включает модуль Dynatrace Live Debugger. Возможные значения: `true` или `false`. |

## Network zone

**Section: [connectivity]**

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `networkZone` | unset | Определяет [network zone](/managed/manage/network-zones "Find out how network zones work in Dynatrace."), к которой принадлежит ActiveGate. ActiveGate может принадлежать только одной network zone. Имя network zone, это строка из буквенно-цифровых символов, дефисов (`-`), знаков подчёркивания (`_`) и точек (`.`). Точки используются как разделители, поэтому первым символом имени network zone не может быть точка. Длина строки ограничена 256 символами. После добавления или изменения этого параметра требуется перезапуск ActiveGate. После перезапуска network zone автоматически создаётся в Dynatrace. |
| `bindToNetworkInterface` | unset | По умолчанию ActiveGate прослушивает все доступные интерфейсы. Если нужно, чтобы ActiveGate прослушивал только выбранный интерфейс, следует указать в этом свойстве IP-адрес, назначенный данному сетевому интерфейсу. |

### Управление network zone с помощью `agctl`

ActiveGate версия 1.333+

Можно использовать [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#network-zone "Learn how to use agctl to configure and manage ActiveGate from the command line") для настройки network zone для ActiveGate:

```
agctl network-zone set production-zone
```

После настройки network zone с помощью `agctl` необходимо перезапустить ActiveGate, чтобы изменения вступили в силу. См. [Start/stop/restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

Кроме того, управлять network zones централизованно можно следующими способами:

* Перейти в **Deployment Status** > **Network zones**, чтобы просматривать, редактировать или создавать network zones.
* **Remote configuration management**: использовать [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-activegates "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбрать действие **modify network zone**).

## Group

**Section: [collector]**

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `group` | unset | [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.") |

### Управление группой ActiveGate с помощью `agctl`

ActiveGate версия 1.333+

Можно использовать [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#group "Learn how to use agctl to configure and manage ActiveGate from the command line") для назначения ActiveGate группе:

```
agctl group set my.group
```

После настройки группы ActiveGate с помощью `agctl` необходимо перезапустить ActiveGate, чтобы изменения вступили в силу. См. [Start/stop/restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

Для изменения назначения группы ActiveGate централизованно из кластера Dynatrace можно использовать [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-activegates "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбрать действие **modify ActiveGate group**).

## Файловый кэш ActiveGate

Файловый кэш ActiveGate снижает трафик между ActiveGate и кластером Dynatrace, позволяя OneAgent скачивать автоматические обновления с ActiveGate, а не напрямую с кластера.

Файловый кэш активируется автоматически при установке или обновлении ActiveGate. Однако активация происходит только при соблюдении **минимального требования к свободному месту, 512 МБ**. Если минимальное требование не выполнено, кэширование автоматически деактивируется.

Файловый кэш можно настроить точнее или деактивировать в конфигурации ActiveGate, в файле `custom.properties`:

**Section: [generic\_filecache]**

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `generic_filecache_enabled` | `true` | Включает или отключает файловый кэш ActiveGate. Возможные значения: `true` или `false`. |
| `generic_filecache_path` | `<ActiveGate temporary directory>/generic_filecache` | Путь к директории файлового кэша ActiveGate. Директория будет создана, если не существует (при наличии соответствующих прав доступа к файлам). |
| `generic_filecache_size` | `2147483648` (2 ГБ) | Размер файлового кэша ActiveGate в байтах. Файловый кэш ActiveGate не будет использовать больше места, чем указано в конфигурации. Если доступного места меньше, чем задано в конфигурации, ActiveGate использует доступное место. |
| `generic_filecache_max_age` | `1209600000` (14 дней) | Максимальный возраст файлов, хранящихся в файловом кэше ActiveGate, в миллисекундах. Возраст файла отсчитывается с момента последнего использования файла (не с момента загрузки или создания). Если файл не используется в течение настроенного максимального возраста, он удаляется автоматически. Файлы также удаляются из кэша до истечения максимального возраста, если места недостаточно для новых файлов. Первыми удаляются файлы, использовавшиеся реже всего (LRU, least recently used). |

Если значение содержит символ запятой, его нужно экранировать одним обратным слешем. Например, `proxy-password = foo\,bar`.

## Section: [com.compuware.apm.webserver]

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `port-ssl` | `9999` | Порт, на котором ActiveGate прослушивает трафик от OneAgent, используется для HTTPS-соединения. Настроить это можно с помощью команды [agctl ssl-port](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#ssl-port "Learn how to use agctl to configure and manage ActiveGate from the command line"). Если нужно изменить значение порта, см. [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") и [Extension Execution Controller custom configuration](/managed/ingest-from/extensions/advanced-configuration/eec-custom-configuration "Configure the Extension Execution Controller (EEC)."). |
| `port` | unset | Порт, на котором ActiveGate прослушивает трафик от OneAgent, используется для HTTP-соединения. По умолчанию отключён. В Linux рекомендуется значение > 1024, чтобы не требовались права root. |
| `ssl-protocols` | `TLSv1.2`, `TLSv1.3` | Поддерживаемые SSL-протоколы. Можно указать одно значение или список через запятую. Обратите внимание: указание конкретной версии не означает автоматическую поддержку всех предыдущих/более низких версий, поэтому каждую версию нужно указывать явно. Допустимые значения: `TLSv1.2` и `TLSv1.3`. |
| `excluded-ciphers` | unset | Список исключённых шифров. Шифры задаются подстрокой, совпадающей хотя бы с частью имени шифра, например:`excluded-ciphers = TLS_RSA_WITH,SHA$,TLS_ECDH` |
| `certificate-file` | unset | Путь к файлу `PKCS#12`, содержащему сертификаты, которые использует веб-сервер ActiveGate. См. также [Configuration of custom SSL certificate on ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate."). |
| `certificate-password` | unset | Пароль к файлу сертификата. |
| `certificate-alias` | unset | Понятное имя сертификата в файле `PKCS#12`. |

#### Работа по HTTPS и HTTP

По умолчанию ActiveGate работает в защищённом режиме, обслуживая входящие запросы по HTTPS. Это задаётся свойством конфигурации `port-ssl`, которое можно изменить в файле `custom.properties`. Однако если нужно, чтобы ActiveGate использовал HTTP, в `custom.properties` необходимо указать свойство `port`.

Защищённый режим является режимом по умолчанию и рекомендуемым. Тем не менее HTTP может быть предпочтителен по соображениям производительности. Например, если перед кластерным ActiveGate установлен балансировщик нагрузки и балансировщик завершает входящие внешние SSL-соединения (см. [третий сценарий развёртывания](/managed/managed-cluster/basics/managed-deployments#scenario-3-integration-with-existing-it-landscape "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture.")).

## Section: [http.client]

Настройки взаимодействия, используемые для мониторинга AWS/VMware/Azure и для связи с кластером Dynatrace (если не переопределены в `[http.client.internal]`).
В частности, этот раздел содержит свойства конфигурации, относящиеся к настройкам прокси и таймаутам соединения.

[Указать общие настройки прокси для взаимодействия с кластером Dynatrace и мониторинга AWS/VMware/Azure](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#proxy-for-cluster-aws-vmware-azure "Learn how to configure ActiveGate properties to set up a proxy.").

## Section: [http.client.internal]

Настройки, специфичные только для взаимодействия с Dynatrace Cluster.
В частности, этот раздел может содержать конфигурационные свойства, связанные с настройками прокси и таймаутами соединения.

Если этот раздел содержит proxy-off = true, то для взаимодействия с Dynatrace Cluster прокси не используется. Если он содержит свойство proxy-host, то это прокси, который нужно использовать для взаимодействия с Dynatrace Cluster.

Если этот раздел не существует, взаимодействие с Dynatrace Cluster определяется настройками из раздела `[http.client]`.

ActiveGate версии 1.247 и более ранние: если раздел `[http.client.internal]` существует, но в нём не указана конкретная настройка взаимодействия, то для целей взаимодействия с Dynatrace Cluster значение этой настройки **принимается равным заводскому значению по умолчанию** (оно **не** наследуется из `[http.client]`).

[Настройка прокси только для взаимодействия с Dynatrace Cluster](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#set-up-proxy-only-for-dynatrace-cluster-communication "Узнать, как настроить свойства ActiveGate для настройки прокси.")

## Section: [http.client.external]

Настройки взаимодействия для конкретных модулей: Cloud Foundry, Kubernetes, а также для Synthetic Monitoring.
В частности, этот раздел может содержать конфигурационные свойства, связанные с настройками прокси и таймаутами соединения.

Если этот раздел содержит `proxy-off = true`, то для модулей прокси не используется. Если он содержит свойство `proxy-host`, то это прокси, который нужно использовать для модулей.

ActiveGate версии 1.247 и более ранние

Настройки взаимодействия, указанные в `[http.client]`, **не всегда** используются как значения по умолчанию для модулей: если конкретная настройка взаимодействия **не** указана в `[http.client.external]`, то для Cloud Foundry, Kubernetes или Synthetic Monitoring эта настройка вернётся к своему заводскому значению по умолчанию, а не к значению, указанному в `[http.client]`.

Аналогично, если раздел `[http.client.external]` целиком отсутствует, то все настройки взаимодействия для Kubernetes и Cloud Foundry вернутся к своим заводским значениям по умолчанию, однако настройки для Synthetic Monitoring примут значения, указанные в разделе `[http.client]`.

[Указание общих настроек прокси для Cloud Foundry, Kubernetes и Synthetic Monitoring](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#specify-common-proxy-settings-for-cloud-foundry-kubernetes-and-synthetic-monitoring "Узнать, как настроить свойства ActiveGate для настройки прокси.")

## Section: [connectivity]

| Property | Default value | Description |
| --- | --- | --- |
| `reverseDnsLookupEnabled` | `true` | ActiveGate версии 1.255+: включает или отключает разрешение полного доменного имени (FQDN) с помощью обратного DNS-запроса. Когда эта функция включена и стандартное разрешение FQDN не даёт результата, выполняется попытка разрешить имя с помощью обратного DNS-запроса. ActiveGate, которые ранее отображались по IP-адресу, теперь могут отображаться по имени хоста. Допустимые значения: `true` или `false`. |

## Trusted root certificate

**Section: [collector]**

| Property | Default value | Description |
| --- | --- | --- |
| `trustedstore` | не задано | Доверенное хранилище ключей (необязательно). Свойство `trustedstore` должно содержать путь к файлу, содержащему доверенные сертификаты. Этот путь должен быть указан относительно каталога SSL ActiveGate. См. также [Доверенные корневые сертификаты для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Узнать, как настроить пользовательские доверенные корневые сертификаты на ActiveGate для установления защищённых SSL/TLS-соединений."). |
| `trustedstore-exclusive` | не задано | Если задано значение `true`, ActiveGate больше не будет объединять встроенное хранилище доверия (поставляемое с JRE) с пользовательским хранилищем доверия, заданным в `trustedstore`. Пользовательское хранилище доверия будет единственным хранилищем доверия, используемым для взаимодействия. |
| `trustedstore-password` | `changeit` | Пароль доверенного хранилища ключей (необязательно), который шифруется при запуске ActiveGate. Обфусцированный пароль затем сохраняется в `trustedstore-password-encr`. |
| `trustedstore-type` | `pkcs12` | Формат баз данных ключей и сертификатов, используемый в Java по умолчанию (необязательно). |