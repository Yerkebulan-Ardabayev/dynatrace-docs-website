---
title: Свойства и параметры конфигурации ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate
---

# Свойства и параметры конфигурации ActiveGate

# Свойства и параметры конфигурации ActiveGate

* Чтение: 17 мин
* Обновлено 19 мая 2026 г.

## Перед началом работы

Разберитесь с основными концепциями конфигурации ActiveGate, связанными с файлами свойств.

Хостовые ActiveGate, то есть ActiveGate Module: OTLP Ingest, развёрнутые обычным способом с помощью установщика, и контейнеризированные ActiveGate используют одни и те же свойства конфигурации, хранящиеся в одних и тех же файлах конфигурации. Однако фактические значения этих свойств могут отличаться, а сами свойства задаются или изменяются разными механизмами: хостовые ActiveGate настраиваются непосредственно на хосте, где работает ActiveGate, тогда как контейнеризированные ActiveGate настраиваются с помощью механизма конфигурации вашей облачной платформы.

* [Как развернуть и настроить контейнеризированный ActiveGate в Kubernetes](/managed/ingest-from/dynatrace-activegate/activegate-in-container "Развёртывание контейнеризированного ActiveGate.")

## Основные правила работы с конфигурацией ActiveGate

### Файлы конфигурации ActiveGate

Многие настройки конфигурации ActiveGate (например, настройки подключения и прокси, шифры или настройки дампа памяти) хранятся в файлах свойств `config.properties` и `custom.properties`, которые находятся в **[каталоге конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate в системах Windows и Linux.")**.
Свойства, перечисленные в файлах свойств, применимы как к Environment ActiveGate, так и к Cluster ActiveGate.

Файлы `config.properties` и `custom.properties` разделены на **секции**. Название каждой секции заключено в квадратные скобки, например:

```
[collector]



MSGrouter = true



restInterface = true



DumpSupported = false
```

### config.properties

Файл конфигурации `config.properties` содержит настройки установки ActiveGate по умолчанию и не настраивается пользователем.

Этот файл конфигурации перезаписывается при каждом обновлении ActiveGate.

### custom.properties

Настройки, хранящиеся в `custom.properties`, переопределяют соответствующие настройки в `config.properties`, и этот файл копируется в новую версию ActiveGate при обновлении.

Файлы конфигурации разделены на `[секции]`, которые обозначаются квадратными скобками.  
Чтобы задать пользовательские настройки в `custom.properties`, укажите названия секций и включите в них нужные свойства.

Файл `config.txt` можно использовать как справочник при добавлении пользовательских настроек в файл `custom.properties`. Файл `config.txt`, который также находится в каталоге конфигурации ActiveGate, самим ActiveGate не используется, однако содержит справочный список возможных свойств конфигурации.
Также можно сначала найти нужную секцию в файле `config.properties`, а затем скопировать название секции вместе с именами нужных свойств в `custom.properties`.  
После этого можно изменить записи в этой секции нужным образом.

### launcheruserconfig.conf

Лаунчер ActiveGate, это сторожевой процесс (watchdog), который запускает виртуальную машину Java для ActiveGate.
Конфигурация лаунчера хранится в файле `launcheruserconfig.conf`, в **[каталоге конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate в системах Windows и Linux.")**. Он содержит свойства и параметры лаунчера, которые передаются виртуальной машине Java.

Для Remote Plugin Module (RPM) файл `launcheruserconfig.conf` должен размещаться именно в каталоге `/var/lib/dynatrace/remotepluginmodule/agent/conf/`.

Файл `launcheruserconfig.conf` сохраняется при обновлениях ActiveGate.

### Перезапуск ActiveGate

При изменении конфигурации ActiveGate необходимо [перезапустить основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запускать, останавливать и перезапускать ActiveGate в Windows или Linux."), чтобы изменения вступили в силу.

## Настройка ActiveGate с помощью `agctl`

ActiveGate версии 1.333+

Начиная с версии ActiveGate 1.333, можно использовать интерфейс командной строки `agctl` для управления конфигурацией ActiveGate. Инструмент `agctl` упрощает управление конфигурацией, предоставляя:

* **Специализированные команды** для типовых задач конфигурации, таких как настройка конечных точек прокси, управление SSL-сертификатами, настройка хранилищ доверенных сертификатов и назначение групп ActiveGate.
* **Универсальную команду для работы со свойствами**, которая позволяет настраивать любое свойство в файле `custom.properties` с помощью команды [agctl property](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#property "Узнайте, как использовать agctl для настройки ActiveGate и управления им из командной строки") для свойств, у которых нет специализированных команд.

Подробности обо всех доступных командах, параметрах и примерах см. в разделе [Интерфейс командной строки agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface "Узнайте, как использовать agctl для настройки ActiveGate и управления им из командной строки").

## Пример использования `agctl` для управления конфигурацией ActiveGate

ActiveGate версии 1.333+

В этом примере изменим путь очереди данных логов на хостовом ActiveGate.

Для хостового Environment или Cluster ActiveGate путь, используемый для очереди данных логов, можно изменить с помощью [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#property "Узнайте, как использовать agctl для настройки ActiveGate и управления им из командной строки"). В следующих шагах в качестве примера нового пути используется `/var/disk_queue`.

1. Ознакомьтесь с [предварительными требованиями к интерфейсу командной строки `agctl`](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#prerequisites "Узнайте, как использовать agctl для настройки ActiveGate и управления им из командной строки").
2. Подключитесь к хосту по SSH.
3. Остановите службу ActiveGate:

```
systemctl stop dynatracegateway
```

4. Прочитайте текущий путь:

```
agctl property get --section=generic_ingest --key=disk_queue_path
```

5. Убедитесь, что целевой каталог `/var/disk_queue` существует, доступен для записи и на нём есть как минимум `disk_queue_max_size_mb` МБ свободного дискового пространства.
6. Измените путь:

```
agctl property set --section=generic_ingest --key=disk_queue_path --value=/var/disk_queue
```

7. Опционально: удалите каталог, на который указывал старый путь.
8. Запустите службу ActiveGate:

```
systemctl start dynatracegateway
```

## Ограничения памяти ActiveGate

Ограничения использования памяти для ActiveGate можно задать в файле конфигурации лаунчера `launcheruserconfig.conf` с помощью следующих свойств:

* `-java.xmx.relative_part`, процент доступной оперативной памяти
* `-java.xmx.absolute_part`, абсолютное значение объёма памяти, в МБ

Конфигурация может включать любую комбинацию этих свойств, а итоговое ограничение памяти представляет собой сумму абсолютной части и относительной части (рассчитанной на основе доступной оперативной памяти).

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

## Диапазон портов heartbeat ActiveGate

Лаунчер ActiveGate отслеживает процесс ActiveGate через локальный порт heartbeat. Этот порт выбирается лаунчером из заранее заданного диапазона портов, указанного в конфигурации лаунчера. Лаунчер находит свободный порт в заданном диапазоне, а затем передаёт номер порта процессу ActiveGate.

По умолчанию лаунчер использует для мониторинга heartbeat порты выше 50000. В некоторых развёртываниях может потребоваться настроить для этой цели другие порты. Чтобы указать диапазон портов, который должен использовать лаунчер ActiveGate, добавьте или измените свойство `-healthcheck.heartbeat.portrange` в файле конфигурации лаунчера `launcheruserconfig.conf`, как показано в примере ниже.

```
-healthcheck.heartbeat.portrange=60100:60200
```

## Пользовательские параметры для процесса Java ActiveGate

Чтобы передать пользовательские параметры процессу Java ActiveGate, укажите их в файле конфигурации лаунчера `launcheruserconfig.conf`:

* Все строки после `-arguments_section.jvm` передаются в качестве аргументов JVM. Таким образом, указывая параметры `-D`, можно задавать аргументы для ActiveGate.

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

Разные функциональные возможности, предоставляемые ActiveGate, называются **[модулями](/managed/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Learn the capabilities and uses of ActiveGate.")**. При установке ActiveGate для конкретной [цели](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") устанавливается или включается разный набор модулей.

Модуль активен, если соответствующее свойство конфигурации указано со значением `true` в разделе конфигурации, посвящённом этому модулю. Однако стоит учитывать, что нельзя включить все модули через `custom.properties` простым изменением значения свойства: если ActiveGate установлен для работы как приватная Synthetic-локация или для мониторинга мейнфрейма, а назначение ActiveGate нужно изменить, ActiveGate придётся переустановить.  
Активные модули перечислены на странице [Deployment status](/managed/ingest-from/dynatrace-activegate/operation/update-activegate "Configure Environment ActiveGate automatic updates---update mode, target version, and update windows---and download or install manually.").

Каждый модуль имеет соответствующий раздел в конфигурации

Помимо разделов конфигурации, посвящённых конкретной функциональности ActiveGate, каждый модуль ActiveGate имеет собственный раздел в файлах конфигурации ActiveGate. Настройки, указанные в этом разделе, применяются именно к данному модулю. Это касается, например, настроек прокси. Однако не все настройки можно продублировать таким образом и указать для модуля: каждый раздел модуля принимает лишь ограниченный набор параметров. **Не копируйте настройки конфигурации между разделами, если только это не указано отдельно.**

### Управление модулями через `agctl`

Версия ActiveGate 1.333+

С помощью [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Learn how to use agctl to configure and manage ActiveGate from the command line") можно включать и отключать модули ActiveGate.

После включения или отключения модулей через `agctl` нужно [перезапустить ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux."), чтобы изменения вступили в силу.

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
| `aws_default_region` | Задаёт регион по умолчанию, используемый модулем [мониторинга AWS](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services."). Возможные значения: допустимые коды регионов AWS. Например: `us-east-1` |
| `aws_client_regions` | Задаёт регионы, используемые модулем [мониторинга AWS](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services."). Возможные значения: список допустимых кодов регионов AWS, разделённых `;`. Например: `us-east-1;eu-central-1` |

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

Этот раздел может содержать настройки прокси для взаимодействия с Cloud Foundry. Если раздел содержит `proxy-off = true`, то прокси для взаимодействия с Cloud Foundry не используется. Если он содержит свойство `proxy-host`, то именно этот прокси используется для мониторинга Cloud Foundry вместо прокси, указанного в `[http.client.external]`.

Версия ActiveGate 1.247 и более ранние Если в файле `custom.properties` присутствует раздел `[cloudfoundry_monitoring]`, также необходим раздел `[http.client.external]`, в котором нужно указать все остальные параметры взаимодействия, используемые для связи с Cloud Foundry.

[Настройка прокси только для мониторинга Cloud Foundry](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#set-up-proxy-only-for-cloud-foundry-monitoring "Learn how to configure ActiveGate properties to set up a proxy.")

## Модуль: Kubernetes

Мониторинг платформы Kubernetes  
**Раздел: [kubernetes\_monitoring]**

| Свойство | Описание |
| --- | --- |
| `kubernetes_monitoring_enabled` | Включает модуль [мониторинга платформы Kubernetes](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet."). Возможные значения: `true` или `false`. |

Этот раздел может содержать настройки прокси для взаимодействия с Kubernetes, а также другие настройки, связанные с точной настройкой параметров взаимодействия для мониторинга платформы Kubernetes.  
Если раздел содержит `proxy-off = true`, то прокси для взаимодействия с Kubernetes не используется. Если он содержит свойство `proxy-host`, то именно этот прокси используется для мониторинга платформы Kubernetes вместо прокси, указанного в `[http.client.external]`.

Версия ActiveGate 1.247 и более ранние Если в файле `custom.properties` присутствует раздел `[kubernetes_monitoring]`, также необходим раздел `[http.client.external]`, в котором нужно указать все остальные параметры взаимодействия, используемые для связи с Kubernetes.

[Настройка прокси только для мониторинга платформы Kubernetes](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#set-up-proxy-only-for-kubernetes-monitoring "Learn how to configure ActiveGate properties to set up a proxy.")

## Модуль: Log Monitoring

**Раздел: [log\_analytics\_collector]**

| Свойство | Описание |
| --- | --- |
| `log_analytics_collector_enabled` | Включает модуль [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more."). Возможные значения: `true` или `false`. |

**Раздел: [generic\_ingest]**

Именно для Log Monitoring, при настройке приёма журналов API, можно настроить свойства очереди данных журналов. Можно указать временную папку, в которой будут храниться данные журналов из очереди. По умолчанию используется временная папка, настроенная в системе (см. [Директории ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.")). Также можно изменить максимальный размер очереди, используемой в этой папке (размер по умолчанию, 300 МБ).

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `disk_queue_path` | Текущая общесистемная временная папка | Задаёт путь к временной папке, в которой будут храниться данные журналов из очереди. |
| `disk_queue_max_size_mb` | 300 МБ | Задаёт максимальный размер данных журналов из очереди, которые могут храниться во временной папке. |

## Модуль: VMware

Мониторинг VMware  
**Раздел: [vmware\_monitoring]**

| Свойство | Описание |
| --- | --- |
| `vmware_monitoring_enabled` | Включает модуль [мониторинга VMware](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace."). Возможные значения: `true` или `false`. |

## Модуль: Database insights

Database insights для Oracle  
**Раздел: [dbAgent]**

| Свойство | Описание |
| --- | --- |
| `dbAgent_enabled` | Включает модуль [Database insights для Oracle](/managed/observe/infrastructure-observability/database-services-classic/database-insights "Learn how to extend your database monitoring to the database infrastructure layer."). Возможные значения: `true` или `false`. |

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

## Модуль: Synthetic

Синтетические мониторы из приватных Synthetic-локаций
**Раздел: [synthetic]**

Настройки прокси для Synthetic Monitoring. Если этот раздел содержит `proxy-off = true`, значит для Synthetic Monitoring прокси не используется. Если он содержит свойство `proxy-host`, значит это прокси, который будет использоваться для Synthetic Monitoring, вместо прокси, указанного в `[http.client.external]` (или в `[http.client]`, если `[http.client.external]` не определён).

Если в файле `custom.properties` есть раздел `[synthetic]`, можно добавить раздел `[http.client.external]`, где нужно указать все остальные параметры соединения, используемые для Synthetic Monitoring. Либо можно указать остальные настройки соединения в разделе `[http.client]`.

ActiveGate версии 1.247 и более ранние: однако, если создаётся раздел `[http.client.external]`, в нём нужно указать все параметры соединения. Иначе параметры соединения для отслеживаемых сред (Cloud Foundry, Kubernetes или Synthetic Monitoring) вернутся к заводским значениям по умолчанию.

Подробнее о свойствах, связанных с прокси, для ActiveGate с поддержкой Synthetic, см. в разделе [Настройка прокси для приватного синтетического мониторинга](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Узнайте, как настроить свойства ActiveGate для настройки прокси для приватного синтетического мониторинга.").

Обратите внимание, что изменение свойства `synthetic_enabled` работает только в том случае, если ActiveGate был установлен для [запуска синтетических мониторов из приватной локации](/managed/ingest-from/dynatrace-activegate#synthetic "Основные понятия, связанные с ActiveGate."). Если ActiveGate был установлен для [маршрутизации трафика, мониторинга облачных сред или мониторинга удалённых технологий с помощью расширений](/managed/ingest-from/dynatrace-activegate#route "Основные понятия, связанные с ActiveGate.") или [мониторинга мейнфрейма](/managed/ingest-from/dynatrace-activegate#mainframe "Основные понятия, связанные с ActiveGate."), то для использования его в целях Synthetic Monitoring нужно переустановить ActiveGate. Подробнее см. в разделе [Создание приватной Synthetic-локации](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать приватную локацию для синтетического мониторинга.").

Если запятая (`,`) является частью значения, перед ней нужно добавить экранирующий обратный слэш (`\`).

Пример: `proxy-password = foo\,bar`

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `synthetic_enabled` | `false` в режиме развёртывания **Default**  `true` в режиме развёртывания **Synthetic monitoring** | Включает выполнение мониторов из приватных Synthetic-локаций на ActiveGate. |
| `synthetic_autoinstall` | `true` для автоматического обновления Synthetic-движка | Автоматически устанавливается в `true` при установке для ActiveGate с поддержкой Synthetic. |
| `proxy-server` | не задано | Адрес прокси-сервера |
| `proxy-port` | не задано | Порт прокси (числовое значение) |
| `proxy-user` | не задано | Имя пользователя прокси (необязательно) |
| `proxy-password` | не задано | Пароль прокси (необязательно)  Пароль, указанный в свойстве `proxy-password`, обфусцируется после перезапуска ActiveGate, а обфусцированный пароль сохраняется в свойстве `proxy-password-encr`. **Примечание**: символ запятой, если он должен являться частью значения, нужно экранировать одним обратным слэшем. Например, `proxy-password = foo\,bar`. |
| `proxy-off` | не задано | Отключает взаимодействие через прокси между ActiveGate и тестируемым ресурсом. |
| `proxy-non-proxy-hosts` | не задано | Не использовать прокси при взаимодействии с этими хостами. |
| `chromium_repo` | не задано  Указывает пользовательский репозиторий пакетов браузера на HTTP-сервере. Пример: `https://172.18.0.100/chromium-repo` Работает только если и `synthetic_autoinstall`, и `synthetic_autoupgrade_chromium` имеют значение `true`. | Включает автообновление браузера из [пользовательского репозитория](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Узнайте, как создать приватную локацию для синтетического мониторинга."). |

Рекомендуется не редактировать значение свойства `synthetic_autoupgrade_chromium` в файле `custom.properties`, поскольку внесённые изменения могут быть перезаписаны.

Свойство `synthetic_autoupgrade_chromium` для автообновления браузера можно определить на уровне локации (для локаций с Environment ActiveGate) либо [через веб-интерфейс](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser "Анализ и управление использованием мощностей в приватных Synthetic-локациях."), либо с помощью вызова [PUT a location](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/put-a-location "Обновление приватной синтетической локации через API Synthetic v2.") API Synthetic locations API v2. Для Cluster ActiveGate это свойство можно настроить через вызов [PUT a location (Dynatrace Managed)](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/put-a-location "Обновление приватной Synthetic-локации через API Synthetic v2 в Dynatrace Managed.") API Cluster API v2. Это свойство не определено для ActiveGate, которые не были назначены локации. Для Activate, назначенных локации, значение по умолчанию, `true`.

## Модуль: Beacon forwarder

Использование ActiveGate для Real User Monitoring
**Раздел: [beacon\_forwarder]**

| Свойство | Описание |
| --- | --- |
| `beacon_forwarder_enabled` | Включает [модуль Beacon forwarder](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Изменение URL конечной точки beacon по умолчанию и отправка RUM-бэконов на инфраструктуру Dynatrace или на другой инструментированный веб-сервер."). Возможные значения: `true` или `false`. |

## Модуль: HTTP Metric API

Приём метрик: простой способ отправки любых пользовательских метрик в Dynatrace
**Раздел: [metrics\_ingest]**

| Свойство | Описание |
| --- | --- |
| `metrics_ingest_enabled` | Включает модуль HTTP Metric API, который обеспечивает [приём метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace."). Возможные значения: `true` или `false`. |

## Модуль: Memory dumps

Инициирование и загрузка дампов памяти
**Раздел: [collector]**

| Свойство | Описание |
| --- | --- |
| `DumpSupported` | Включает [модуль дампов памяти](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Узнайте, как включить хранение дампов памяти на ActiveGate."). Возможные значения: `true` или `false`. |

Когда в приложении возникают утечки памяти или высокая интенсивность создания объектов, важно получить дампы памяти, чтобы проанализировать эти проблемы. В производственных средах это часто оказывается затруднительным, когда нет возможности войти в среду и нет других способов инициировать дампы памяти. Dynatrace позволяет как инициировать, так и безопасно загружать дампы памяти в выбранный инструмент анализа.
См. [Настройка ActiveGate для хранения дампов памяти](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Узнайте, как включить хранение дампов памяти на ActiveGate.").

## Модуль: маршрутизация OneAgent

ActiveGate знает о структуре среды выполнения вашей Dynatrace среды и маршрутизирует сообщения от OneAgent к нужным конечным точкам сервера. Он обрабатывает маршрутизацию сообщений, буферизацию, сжатие, аутентификацию и доступ к изолированным сетям.
**Раздел: [collector]**

| Свойство | Описание |
| --- | --- |
| `MSGrouter` | Включает модуль маршрутизации OneAgent, который маршрутизирует трафик OneAgent и другой трафик ActiveGate через Dynatrace. Возможные значения: `true` или `false`. |

## Модуль: OTLP Ingest

**Раздел: [otlp\_ingest]**
Этот модуль создаёт на ActiveGate конечные точки, которые могут принимать данные трассировки OpenTelemetry (трассировки и спаны), метрики и логи в формате OTLP. Подробнее см. в разделе [Конечные точки API OTLP Dynatrace](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках API OTLP, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

| Свойство | Описание |
| --- | --- |
| `otlp_ingest_enabled` | Включает модуль OTLP ingest, который обеспечивает приём [трассировок](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.") и [метрик](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.") OpenTelemetry. Возможные значения: `true` или `false`. |

## Модуль: REST API

**Раздел: [collector]**
ActiveGate можно использовать для доступа к [API Dynatrace](/managed/dynatrace-api "Узнайте, что нужно для использования API Dynatrace."). ActiveGate поддерживает вызовы ко всем конечным точкам конфигурации и среды API Dynatrace, как в версии v1, так и в v2. Для доступа к API Dynatrace через ActiveGate используйте URL в следующем формате: `https://{your-ActiveGate-domain}/e/{your-environment-id}/api/...`

| Свойство | Описание |
| --- | --- |
| `restInterface` | Включает модуль REST API, который обеспечивает доступ к API Dynatrace через REST. Возможные значения: `true` или `false`. |

## Модуль: отладка

**Раздел: [debugging]**
ActiveGate можно использовать для доступа к данным на уровне кода, необходимым для быстрого устранения неполадок и отладки в любой среде, от разработки до продакшена.

| Свойство | Описание |
| --- | --- |
| `debugging_enabled` | Включает модуль Dynatrace Live Debugger. Возможные значения: `true` или `false`. |

## Сетевая зона

**Раздел: [connectivity]**

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `networkZone` | не задано | Определяет [сетевую зону](/managed/manage/network-zones "Find out how network zones work in Dynatrace."), к которой относится ActiveGate. ActiveGate может относиться только к одной сетевой зоне. Имя сетевой зоны, это строка из буквенно-цифровых символов, дефисов (`-`), символов подчёркивания (`_`) и точек (`.`). Точки используются как разделители, поэтому нельзя использовать точку в качестве первого символа имени сетевой зоны. Длина строки ограничена 256 символами. После добавления или изменения этого параметра требуется перезапуск ActiveGate. После перезапуска сетевая зона автоматически создаётся в Dynatrace. |
| `bindToNetworkInterface` | не задано | По умолчанию ActiveGate прослушивает все доступные интерфейсы. Если нужно, чтобы ActiveGate прослушивал только выбранный интерфейс, нужно настроить это свойство с IP-адресом, назначенным сетевому интерфейсу. |

### Управление сетевой зоной через `agctl`

ActiveGate версии 1.333+

Для настройки сетевой зоны ActiveGate можно использовать [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#network-zone "Learn how to use agctl to configure and manage ActiveGate from the command line"):

```
agctl network-zone set production-zone
```

После настройки сетевой зоны через `agctl` нужно перезапустить ActiveGate, чтобы изменения вступили в силу. См. [Запуск/остановка/перезапуск ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

Также, чтобы изменить привязку к сетевой зоне централизованно из Cluster Dynatrace, можно использовать [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-activegates "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбрать действие **modify network zone**).

## Group

**Раздел: [collector]**

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `group` | не задано | [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.") |

### Управление группой ActiveGate через `agctl`

ActiveGate версии 1.333+

Для назначения ActiveGate группе можно использовать [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#group "Learn how to use agctl to configure and manage ActiveGate from the command line"):

```
agctl group set my.group
```

После настройки группы ActiveGate через `agctl` нужно перезапустить ActiveGate, чтобы изменения вступили в силу. См. [Запуск/остановка/перезапуск ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

Также, чтобы изменить назначение группы ActiveGate централизованно из Cluster Dynatrace, можно использовать [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-activegates "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбрать действие **modify ActiveGate group**).

## Файловый кэш ActiveGate

Файловый кэш ActiveGate снижает трафик между ActiveGate и Cluster Dynatrace, позволяя OneAgent загружать автоматические обновления с ActiveGate, а не с Cluster.

Файловый кэш активируется автоматически при установке или обновлении ActiveGate. Однако активация происходит только при соблюдении **минимального требования к объёму свободного места в 512 МБ**. Если минимальное требование к объёму не соблюдено, кэширование автоматически деактивируется.

Файловый кэш можно настроить или отключить в конфигурации ActiveGate, в файле `custom.properties`:

**Раздел: [generic\_filecache]**

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `generic_filecache_enabled` | `true` | Включает или отключает файловый кэш ActiveGate. Возможные значения: `true` или `false`. |
| `generic_filecache_path` | `<временный каталог ActiveGate>/generic_filecache` | Путь к каталогу файлового кэша ActiveGate. Каталог будет создан, если он не существует (если это позволяют права доступа к файлам). |
| `generic_filecache_size` | `2147483648` (2 ГБ) | Размер файлового кэша ActiveGate в байтах. Файловый кэш ActiveGate не будет использовать больше места, чем указано в конфигурации. Если доступного места меньше, чем указано в конфигурации, ActiveGate будет использовать доступное место. |
| `generic_filecache_max_age` | `1209600000` (14 дней) | Максимальный возраст файлов, хранящихся в файловом кэше ActiveGate, в миллисекундах. Возраст файла отсчитывается с момента последнего использования файла (а не с момента загрузки/создания). Если файл не используется в течение настроенного максимального возраста, файл будет автоматически удалён. Файлы также удаляются из кэша до достижения максимального возраста, если недостаточно места для новых файлов. В первую очередь удаляются файлы LRU (least recently used, давно не использовавшиеся). |

Если значение содержит символ запятой, его нужно экранировать одним обратным слэшем. Например, `proxy-password = foo\,bar`.

## Раздел: [com.compuware.apm.webserver]

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `port-ssl` | `9999` | Порт, на котором ActiveGate прослушивает трафик от OneAgent, используется для HTTPS-соединения. Это можно настроить с помощью команды [agctl ssl-port](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#ssl-port "Learn how to use agctl to configure and manage ActiveGate from the command line"). Если нужно изменить значение порта, см. [Разработка собственного Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") и [Пользовательская конфигурация Extension Execution Controller](/managed/ingest-from/extensions/advanced-configuration/eec-custom-configuration "Configure the Extension Execution Controller (EEC)."). |
| `port` | не задано | Порт, на котором ActiveGate прослушивает трафик от OneAgent, используется для HTTP-соединения. По умолчанию отключён. В Linux рекомендуется значение > 1024, чтобы не требовались права root. |
| `ssl-protocols` | `TLSv1.2`, `TLSv1.3` | Поддерживаемые SSL-протоколы. Может быть одним значением или списком значений через запятую. Обратите внимание, что указание конкретной версии не подразумевает автоматически поддержку всех предыдущих/более низких версий, поэтому каждую версию нужно указывать явно. Допустимые значения: `TLSv1.2` и `TLSv1.3` |
| `excluded-ciphers` | не задано | Список исключённых шифров. Шифры определяются подстрокой, соответствующей хотя бы части имени шифра, например: `excluded-ciphers = TLS_RSA_WITH,SHA$,TLS_ECDH` |
| `certificate-file` | не задано | Путь к файлу `PKCS#12`, содержащему сертификаты, используемые веб-сервером ActiveGate. См. также [Настройка пользовательского SSL-сертификата на ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate."). |
| `certificate-password` | не задано | Пароль для файла сертификата. |
| `certificate-alias` | не задано | Понятное имя сертификата в файле `PKCS#12`. |

#### Работа по HTTPS против HTTP

По умолчанию ActiveGate работает безопасным способом, обслуживая входящие запросы по HTTPS. Это задаётся свойством конфигурации `port-ssl`, которое можно настроить в файле `custom.properties`. Однако, если нужно, чтобы ActiveGate использовал HTTP, нужно указать свойство `port` в `custom.properties`.

Обратите внимание, что безопасный способ является вариантом по умолчанию и рекомендуемым. Однако вариант с HTTP можно выбрать из соображений производительности. Например, если перед Cluster ActiveGate установлен балансировщик нагрузки и если балансировщик нагрузки завершает входящие внешние SSL-соединения (см. [третий сценарий развёртывания](/managed/managed-cluster/basics/managed-deployments#scenario-3-integration-with-existing-it-landscape "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture.")).

## Раздел: [http.client]

Настройки связи, используемые для мониторинга AWS/VMware/Azure и для связи с Cluster Dynatrace (если не переопределены в `[http.client.internal]`).
В частности, этот раздел содержит свойства конфигурации, относящиеся к настройкам прокси и таймаутам соединения.

[Указать общие настройки прокси для связи с Cluster Dynatrace и мониторинга AWS/VMware/Azure](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#proxy-for-cluster-aws-vmware-azure "Learn how to configure ActiveGate properties to set up a proxy.").

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