---
title: Параметры конфигурации и properties ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate
scraped: 2026-05-12T11:52:23.117753
---

# Параметры конфигурации и properties ActiveGate

# Параметры конфигурации и properties ActiveGate

* 17-min read
* Updated on Feb 24, 2026

## Перед началом

Изучите базовые концепции конфигурации ActiveGate, связанные с property-файлами.

Host-based ActiveGate (то есть ActiveGate с модулем OTLP Ingest, развёрнутый стандартным способом через установщик) и контейнеризованные ActiveGate используют одни и те же конфигурационные properties, хранящиеся в тех же файлах. Однако фактические значения properties могут отличаться, и properties задаются или изменяются разными механизмами: host-based ActiveGate настраивается напрямую на хосте, где он работает, а контейнеризованный ActiveGate настраивается механизмом конфигурации вашей облачной платформы.

* [Как развернуть и настроить контейнеризованный ActiveGate в Kubernetes](/managed/ingest-from/dynatrace-activegate/activegate-in-container "Развёртывание контейнеризованного ActiveGate.")

## Базовые правила работы с конфигурацией ActiveGate

### Конфигурационные файлы ActiveGate

Многие настройки ActiveGate (например, параметры подключения и прокси, шифры, настройки memory dump) хранятся в property-файлах `config.properties` и `custom.properties`, расположенных в **[конфигурационной директории ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Где хранятся файлы ActiveGate на Windows и Linux.")**.
Properties в property-файлах применимы как к Environment ActiveGates, так и к Cluster ActiveGates.

Файлы `config.properties` и `custom.properties` разделены на **секции**. Имя секции указывается в квадратных скобках, например:

```
[collector]



MSGrouter = true



restInterface = true



DumpSupported = false
```

### config.properties

Конфигурационный файл `config.properties` содержит дефолтные настройки установки ActiveGate и не предназначен для редактирования.

Этот файл перезаписывается при каждом обновлении ActiveGate.

### custom.properties

Настройки, хранящиеся в `custom.properties`, переопределяют соответствующие настройки в `config.properties`, и файл переносится в новую версию ActiveGate при обновлении.

Конфигурационные файлы разделены на `[секции]` в квадратных скобках.  
Чтобы задать пользовательские настройки в `custom.properties`, укажите имена секций и впишите соответствующие properties внутри них.

В качестве справочника при добавлении пользовательских настроек в `custom.properties` можно использовать файл `config.txt`. Файл `config.txt`, также расположенный в конфигурационной директории ActiveGate, не используется ActiveGate, но содержит справочный список всех возможных конфигурационных properties.
Альтернативно можно сначала найти нужную секцию в `config.properties`, а затем скопировать заголовок секции и имена нужных properties в `custom.properties`.  
После этого записи в секции можно изменять по необходимости.

### launcheruserconfig.conf

ActiveGate launcher — это watchdog-процесс, который запускает Java virtual machine для ActiveGate.
Конфигурация launcher хранится в файле `launcheruserconfig.conf`, в **[конфигурационной директории ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Где хранятся файлы ActiveGate на Windows и Linux.")**. Он содержит properties launcher'а и параметры, передаваемые в JVM.

Для Remote Plugin Module (RPM) файл `launcheruserconfig.conf` должен находиться по пути `/var/lib/dynatrace/remotepluginmodule/agent/conf/`.

Файл `launcheruserconfig.conf` сохраняется при обновлениях ActiveGate.

### Перезапуск ActiveGate

После изменения конфигурации ActiveGate необходимо [перезапустить главный сервис ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Запуск, остановка и перезапуск ActiveGate на Windows или Linux."), чтобы изменения вступили в силу.

## Настройка ActiveGate через `agctl`

ActiveGate версии 1.333+

Начиная с версии ActiveGate 1.333, для управления конфигурацией ActiveGate можно использовать CLI `agctl`. Инструмент `agctl` упрощает управление конфигурацией, предоставляя:

* **Специализированные команды** для типовых задач: настройка proxy endpoints, управление SSL-сертификатами, настройка trust stores, назначение ActiveGate в группы.
* **Универсальную команду property**, позволяющую настраивать любое свойство в файле `custom.properties` через команду [agctl property](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#property "Использование agctl для настройки и управления ActiveGate из командной строки") для свойств без выделенной команды.

Подробности по всем командам, параметрам и примерам смотрите в [agctl command-line interface](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface "Использование agctl для настройки и управления ActiveGate из командной строки").

## Лимиты памяти ActiveGate

Лимиты использования памяти для ActiveGate задаются в конфигурационном файле launcher `launcheruserconfig.conf` через следующие properties:

* `-java.xmx.relative_part` — процент от доступной RAM
* `-java.xmx.absolute_part` — абсолютное значение размера памяти в МБ

Конфигурация может включать любое сочетание этих properties, итоговый лимит памяти равен сумме absolute part и relative part (вычисленного от доступной RAM).

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

Launcher ActiveGate отслеживает процесс ActiveGate через локальный heartbeat-порт. Этот порт выбирается launcher'ом из заранее определённого диапазона, заданного в конфигурации launcher'а. Launcher находит свободный порт в указанном диапазоне и передаёт его номер процессу ActiveGate.

По умолчанию launcher использует порты выше 50000 для heartbeat-мониторинга. В отдельных развёртываниях могут потребоваться другие порты. Чтобы задать диапазон портов для launcher ActiveGate, добавьте или измените свойство `-healthcheck.heartbeat.portrange` в конфигурационном файле launcher `launcheruserconfig.conf`, как в примере ниже.

```
-healthcheck.heartbeat.portrange=60100:60200
```

## Пользовательские параметры для Java-процесса ActiveGate

Чтобы передать пользовательские параметры Java-процессу ActiveGate, укажите их в конфигурационном файле launcher `launcheruserconfig.conf`:

* Все строки после `-arguments_section.jvm` передаются как аргументы JVM. Таким образом, через `-D` опции можно задать параметры для ActiveGate.

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

Разные функциональные возможности ActiveGate называются **[модулями](/managed/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Возможности и применение ActiveGate.")**. При установке ActiveGate под конкретную [задачу](/managed/ingest-from/dynatrace-activegate/capabilities "Возможности и применение ActiveGate.") устанавливается или включается соответствующий набор модулей.

Модуль активен, если соответствующее property указано со значением `true` в секции конфигурации, выделенной под этот модуль. Однако не все модули можно включить через `custom.properties` простым изменением значения свойства: если ActiveGate был установлен как private Synthetic location или для мониторинга mainframe, и требуется сменить назначение, ActiveGate нужно переустановить.  
Активные модули перечислены на странице [Deployment status](/managed/ingest-from/dynatrace-activegate/operation/update-activegate "Как узнать установленную версию ActiveGate и скачать/установить актуальную версию.").

У каждого модуля своя секция в конфигурации.

Помимо секций под конкретные функции, у каждого модуля ActiveGate своя секция в конфигурационных файлах. Настройки в этой секции применяются именно к этому модулю. Это касается, например, proxy-настроек. При этом не все настройки можно дублировать в секцию модуля: каждая секция модуля принимает ограниченный набор опций. **НЕ копируйте настройки между секциями без явного указания делать это.**

### Управление модулями через `agctl`

ActiveGate версии 1.333+

С помощью [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Использование agctl для настройки и управления ActiveGate из командной строки") можно включать и отключать модули ActiveGate.

После включения или отключения модулей через `agctl` необходимо [перезапустить ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Запуск, остановка и перезапуск ActiveGate на Windows или Linux."), чтобы изменения вступили в силу.

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
**Секция: [aws\_monitoring]**

| Property | Описание |
| --- | --- |
| `aws_monitoring_enabled` | Включает модуль [AWS monitoring](/managed/ingest-from/amazon-web-services "Настройка мониторинга Amazon Web Services."). Возможные значения: `true` или `false`. |
| `aws_default_region` | Задаёт регион по умолчанию для модуля [AWS monitoring](/managed/ingest-from/amazon-web-services "Настройка мониторинга Amazon Web Services."). Возможные значения: коды регионов AWS. Например: `us-east-1` |
| `aws_client_regions` | Задаёт регионы для модуля [AWS monitoring](/managed/ingest-from/amazon-web-services "Настройка мониторинга Amazon Web Services."). Возможные значения: список кодов регионов AWS через `;`. Например: `us-east-1;eu-central-1` |

## Модуль: Azure

Мониторинг Microsoft Azure  
**Секция: [azure\_monitoring]**

| Property | Описание |
| --- | --- |
| `azure_monitoring_enabled` | Включает модуль [Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройка мониторинга Azure в Dynatrace."). Возможные значения: `true` или `false`. |

## Модуль: Cloud Foundry

Мониторинг Cloud Foundry  
**Секция: [cloudfoundry\_monitoring]**

| Property | Описание |
| --- | --- |
| `cloudfoundry_monitoring_enabled` | Включает модуль [Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Включение мониторинга для Cloud Foundry foundations."). Возможные значения: `true` или `false`. |

Эта секция может содержать proxy-настройки для коммуникации с Cloud Foundry. Если в секции указано `proxy-off = true`, прокси для Cloud Foundry не используется. Если указано свойство `proxy-host`, то именно этот прокси будет использоваться для Cloud Foundry monitoring вместо прокси из `[http.client.external]`.

ActiveGate версии 1.247 и ранее: если у вас в `custom.properties` есть секция `[cloudfoundry_monitoring]`, необходимо также добавить секцию `[http.client.external]`, в которой указать остальные параметры коммуникации для Cloud Foundry.

[Настроить прокси только для Cloud Foundry monitoring](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#set-up-proxy-only-for-cloud-foundry-monitoring "Настройка properties ActiveGate для прокси.")

## Модуль: Kubernetes

Kubernetes Platform Monitoring  
**Секция: [kubernetes\_monitoring]**

| Property | Описание |
| --- | --- |
| `kubernetes_monitoring_enabled` | Включает модуль [Kubernetes Platform Monitoring](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Установка и настройка ActiveGate в Kubernetes как StatefulSet."). Возможные значения: `true` или `false`. |

Эта секция может содержать proxy-настройки для коммуникации с Kubernetes, а также прочие параметры тонкой настройки коммуникации для Kubernetes Platform Monitoring.  
Если в секции указано `proxy-off = true`, прокси для Kubernetes не используется. Если указано свойство `proxy-host`, то именно этот прокси будет использоваться для Kubernetes Platform Monitoring вместо прокси из `[http.client.external]`.

ActiveGate версии 1.247 и ранее: если у вас в `custom.properties` есть секция `[kubernetes_monitoring]`, необходимо также добавить секцию `[http.client.external]`, в которой указать остальные параметры коммуникации для Kubernetes.

[Настроить прокси только для Kubernetes Platform Monitoring](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#set-up-proxy-only-for-kubernetes-monitoring "Настройка properties ActiveGate для прокси.")

## Модуль: Log Monitoring

**Секция: [log\_analytics\_collector]**

| Property | Описание |
| --- | --- |
| `log_analytics_collector_enabled` | Включает модуль [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Включение Log Monitoring, возможности и инсайты Log Monitoring."). Возможные значения: `true` или `false`. |

**Секция: [generic\_ingest]**

Специально для Log Monitoring, при настройке Log ingestion API можно изменить properties очереди логов. Можно задать временную папку, в которой будут храниться логи в очереди (по умолчанию используется системная временная папка), и изменить максимальный размер очереди в этой папке (по умолчанию 300 МБ).

| Property | Значение по умолчанию | Описание |
| --- | --- | --- |
| `disk_queue_path` | Текущая системная временная папка | Путь к временной папке, в которой будут храниться логи в очереди. |
| `disk_queue_max_size_mb` | 300 MB | Максимальный размер очереди логов во временной папке. |

## Модуль: VMware

Мониторинг VMware  
**Секция: [vmware\_monitoring]**

| Property | Описание |
| --- | --- |
| `vmware_monitoring_enabled` | Включает модуль [VMware monitoring](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Мониторинг VMware vSphere через Dynatrace."). Возможные значения: `true` или `false`. |

## Модуль: Database insights

Oracle database insights  
**Секция: [dbAgent]**

| Property | Описание |
| --- | --- |
| `dbAgent_enabled` | Включает модуль [Oracle database insights](/managed/observe/infrastructure-observability/databases/database-services-classic/database-insights "Расширение мониторинга БД на уровень инфраструктуры."). Возможные значения: `true` или `false`. |

## Модуль: Extensions

**Секция: [extension\_controller]**

| Property | Описание |
| --- | --- |
| `extension_controller_enabled` | Включает фреймворк Extensions. Возможные значения: `true` или `false`. |

## Модуль: zRemote

Установка модуля zRemote для мониторинга z/OS  
**Секция: [zremote]**

| Property | Описание |
| --- | --- |
| `zremote_enabled` | Включает [zRemote module](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS."). Возможные значения: `true` или `false`. |

## Модуль: Synthetic

Synthetic-мониторы из private Synthetic locations  
**Секция: [synthetic]**

Proxy-настройки для Synthetic Monitoring. Если в секции указано `proxy-off = true`, прокси для Synthetic Monitoring не используется. Если указано свойство `proxy-host`, то именно этот прокси будет использоваться для Synthetic Monitoring вместо прокси из `[http.client.external]` (или из `[http.client]`, если `[http.client.external]` не определена).

Если у вас в `custom.properties` есть секция `[synthetic]`, можно добавить секцию `[http.client.external]`, в которой указать остальные параметры коммуникации для Synthetic Monitoring. Альтернативно можно указать остальные параметры коммуникации в секции `[http.client]`.

ActiveGate версии 1.247 и ранее: однако если вы всё же создаёте секцию `[http.client.external]`, в ней нужно указать ВСЕ параметры коммуникации. Иначе параметры коммуникации для отслеживаемых сред (Cloud Foundry, Kubernetes, Synthetic Monitoring) сбросятся к значениям по умолчанию.

Подробнее о proxy-related properties для Synthetic-enabled ActiveGate смотрите [Set up a proxy for private synthetic monitoring](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Настройка properties ActiveGate для прокси private synthetic monitoring.").

Учтите: изменение свойства `synthetic_enabled` работает только если ActiveGate установлен для [запуска Synthetic-мониторов из private location](/managed/ingest-from/dynatrace-activegate#synthetic "Базовые концепции ActiveGate."). Если ActiveGate был установлен для [маршрутизации трафика, мониторинга облачных сред или удалённых технологий через extensions](/managed/ingest-from/dynatrace-activegate#route "Базовые концепции ActiveGate.") или [мониторинга mainframe](/managed/ingest-from/dynatrace-activegate#mainframe "Базовые концепции ActiveGate."), для использования в Synthetic Monitoring ActiveGate нужно переустановить. Подробнее: [Create a private Synthetic location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Создание private location для synthetic monitoring.").

Если в значении присутствует запятая (`,`), её нужно экранировать обратной косой чертой (`\`).

Пример: `proxy-password = foo\,bar`

| Property | Значение по умолчанию | Описание |
| --- | --- | --- |
| `synthetic_enabled` | `false` в режиме развёртывания **Default**  `true` в режиме развёртывания **Synthetic monitoring** | Разрешает ActiveGate выполнять мониторы из private Synthetic locations. |
| `synthetic_autoinstall` | `true` для автоматического обновления Synthetic engine | Автоматически выставляется в `true` при установке для Synthetic-enabled ActiveGate. |
| `proxy-server` | unset | Адрес proxy-сервера. |
| `proxy-port` | unset | Порт proxy (числовой). |
| `proxy-user` | unset | Имя пользователя proxy (опционально). |
| `proxy-password` | unset | Пароль proxy (опционально).  Пароль из свойства `proxy-password` обфусцируется после перезапуска ActiveGate, обфусцированный пароль хранится в свойстве `proxy-password-encr`. **Примечание**: символ запятой, если он часть значения, нужно экранировать одной обратной косой чертой. Например, `proxy-password = foo\,bar`. |
| `proxy-off` | unset | Отключает proxy-коммуникацию между ActiveGate и тестируемым ресурсом. |
| `proxy-non-proxy-hosts` | unset | Не использовать proxy при коммуникации с этими хостами. |
| `chromium_repo` | unset  Задаёт пользовательский репозиторий браузерного пакета на HTTP-сервере. Пример: `https://172.18.0.100/chromium-repo` Работает, только если оба `synthetic_autoinstall` и `synthetic_autoupgrade_chromium` равны `true`. | Включает автообновление браузера из [пользовательского репозитория](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Создание private location для synthetic monitoring."). |

Не рекомендуется менять значение свойства `synthetic_autoupgrade_chromium` в `custom.properties`, так как изменения могут быть перезаписаны.

`synthetic_autoupgrade_chromium` для автообновления браузера можно определить на уровне location (для locations с Environment ActiveGates) — либо [через web UI](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser "Анализ и управление потреблением мощности private Synthetic locations."), либо через вызов API [PUT a location](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/put-a-location "Обновление private synthetic location через Synthetic v2 API.") Synthetic locations API v2. Для Cluster ActiveGates это свойство настраивается через вызов [PUT a location (Dynatrace Managed)](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/put-a-location "Обновление private Synthetic location через Synthetic API v2 в Dynatrace Managed.") Cluster API v2. Это свойство не определяется для ActiveGates, не назначенных в location. Для ActiveGates, назначенных в location, значение по умолчанию `true`.

## Модуль: Beacon forwarder

Использование ActiveGate для Real User Monitoring  
**Секция: [beacon\_forwarder]**

| Property | Описание |
| --- | --- |
| `beacon_forwarder_enabled` | Включает [Beacon forwarder module](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Изменение beacon endpoint URL по умолчанию и отправка RUM beacons в инфраструктуру Dynatrace или другой инструментированный web-сервер."). Возможные значения: `true` или `false`. |

## Модуль: HTTP Metric API

Metric ingestion — простой способ отправлять произвольные пользовательские метрики в Dynatrace.  
**Секция: [metrics\_ingest]**

| Property | Описание |
| --- | --- |
| `metrics_ingest_enabled` | Включает модуль HTTP Metric API, обеспечивающий [приём метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Расширение наблюдаемости метрик в Dynatrace."). Возможные значения: `true` или `false`. |

## Модуль: Memory dumps

Триггер и скачивание memory dumps  
**Секция: [collector]**

| Property | Описание |
| --- | --- |
| `DumpSupported` | Включает [модуль memory dumps](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Включение хранения memory dumps на ActiveGate."). Возможные значения: `true` или `false`. |

Когда у вашего приложения утечки памяти или высокая частота создания объектов, memory dumps крайне важны для анализа проблем. В production-средах это часто непросто: бывает невозможно зайти на сервер, и других способов снять memory dump нет. Dynatrace позволяет и снимать memory dumps, и безопасно скачивать их в нужный инструмент анализа.  
Смотрите [Configure ActiveGate for memory dump storage](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Включение хранения memory dumps на ActiveGate.").

## Модуль: OneAgent routing

ActiveGate знает о runtime-структуре вашего Dynatrace-окружения и маршрутизирует сообщения от OneAgent на правильные server endpoints. Он отвечает за маршрутизацию, буферизацию, сжатие, аутентификацию и доступ через изолированные сети.  
**Секция: [collector]**

| Property | Описание |
| --- | --- |
| `MSGrouter` | Включает модуль OneAgent routing, маршрутизирующий трафик OneAgent и другой трафик ActiveGate через Dynatrace. Возможные значения: `true` или `false`. |

## Модуль: OTLP Ingest

**Секция: [otlp\_ingest]**
Этот модуль создаёт endpoints на ActiveGate, принимающие OpenTelemetry trace-данные (traces и spans), метрики и логи в формате OTLP. Подробнее: [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api "OTLP API endpoints для экспорта данных OpenTelemetry в Dynatrace.").

| Property | Описание |
| --- | --- |
| `otlp_ingest_enabled` | Включает модуль OTLP ingest, обеспечивающий приём OpenTelemetry [traces](/managed/ingest-from/opentelemetry "Интеграция и приём данных OpenTelemetry (traces, metrics, logs) в Dynatrace.") и [metrics](/managed/ingest-from/opentelemetry "Интеграция и приём данных OpenTelemetry (traces, metrics, logs) в Dynatrace."). Возможные значения: `true` или `false`. |

## Модуль: REST API

**Секция: [collector]**   
ActiveGate можно использовать для доступа к [Dynatrace API](/managed/dynatrace-api "Что нужно для работы с Dynatrace API."). ActiveGate поддерживает вызовы всех configuration и environment endpoints Dynatrace API в версиях v1 и v2. Для доступа к Dynatrace API через ActiveGate используйте URL в формате: `https://{your-ActiveGate-domain}/e/{your-environment-id}/api/...`

| Property | Описание |
| --- | --- |
| `restInterface` | Включает модуль REST API, обеспечивающий доступ к Dynatrace API через REST. Возможные значения: `true` или `false`. |

## Модуль: debugging

**Секция: [debugging]**   
Через ActiveGate можно получить доступ к code-level данным, нужным для быстрого устранения неполадок и отладки в любой среде — от разработки до production.

| Property | Описание |
| --- | --- |
| `debugging_enabled` | Включает модуль Dynatrace Live Debugger. Возможные значения: `true` или `false`. |

## Network zone

**Секция: [connectivity]**

| Property | Значение по умолчанию | Описание |
| --- | --- | --- |
| `networkZone` | unset | Определяет [network zone](/managed/manage/network-zones "Как работают network zones в Dynatrace."), к которой принадлежит ActiveGate. ActiveGate может принадлежать только одной network zone. Имя network zone — это строка из букв, цифр, дефисов (`-`), подчёркиваний (`_`) и точек (`.`). Точки используются как разделители, поэтому точка не может быть первым символом имени network zone. Длина строки ограничена 256 символами. После добавления или изменения параметра нужен перезапуск ActiveGate. После перезапуска network zone автоматически создаётся в Dynatrace. |
| `bindToNetworkInterface` | unset | По умолчанию ActiveGate слушает на всех доступных интерфейсах. Если ActiveGate должен слушать только на одном интерфейсе, задайте в этом свойстве IP-адрес этого интерфейса. |

### Управление network zone через `agctl`

ActiveGate версии 1.333+

С помощью [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#network-zone "Использование agctl для настройки и управления ActiveGate из командной строки") можно настроить network zone для ActiveGate:

```
agctl network-zone set production-zone
```

После настройки network zone через `agctl` необходимо перезапустить ActiveGate, чтобы изменения вступили в силу. Смотрите [Start/stop/restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Запуск, остановка и перезапуск ActiveGate на Windows или Linux.").

Альтернативно, чтобы централизованно изменить назначение network zone из Dynatrace Cluster, можно использовать [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-activegates "Конфигурация OneAgent и ActiveGate на хостах через Deployment status или массово через Dynatrace API.") (выбрать действие **modify network zone**).

## Group

**Секция: [collector]**

| Property | Значение по умолчанию | Описание |
| --- | --- | --- |
| `group` | unset | [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Базовые концепции ActiveGate groups.") |

### Управление ActiveGate group через `agctl`

ActiveGate версии 1.333+

С помощью [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#group "Использование agctl для настройки и управления ActiveGate из командной строки") можно назначить ActiveGate в группу:

```
agctl group set my.group
```

После настройки ActiveGate group через `agctl` необходимо перезапустить ActiveGate, чтобы изменения вступили в силу. Смотрите [Start/stop/restart ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Запуск, остановка и перезапуск ActiveGate на Windows или Linux.").

Альтернативно, чтобы централизованно изменить назначение ActiveGate group из Dynatrace Cluster, можно использовать [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-activegates "Конфигурация OneAgent и ActiveGate на хостах через Deployment status или массово через Dynatrace API.") (выбрать действие **modify ActiveGate group**).

## File cache ActiveGate

File cache ActiveGate снижает трафик между ActiveGate и Dynatrace Cluster, позволяя OneAgent скачивать автоматические обновления с ActiveGate, а не с Cluster.

File cache активируется автоматически при установке или обновлении ActiveGate. Однако активация происходит только при выполнении **минимального требования к свободному месту в 512 МБ**. Если минимум не выполнен, кеширование автоматически отключается.

File cache можно тонко настроить или отключить в конфигурации ActiveGate, в файле `custom.properties`:

**Секция: [generic\_filecache]**

| Property | Значение по умолчанию | Описание |
| --- | --- | --- |
| `generic_filecache_enabled` | `true` | Включает или отключает file cache ActiveGate. Возможные значения: `true` или `false`. |
| `generic_filecache_path` | `<ActiveGate temporary directory>/generic_filecache` | Путь к директории file cache ActiveGate. Директория будет создана, если её ещё нет (при наличии соответствующих прав). |
| `generic_filecache_size` | `2147483648` (2 ГБ) | Размер file cache ActiveGate в байтах.  File cache ActiveGate не использует больше места, чем задано в конфигурации. Если доступного места меньше указанного значения, ActiveGate будет использовать доступное. |
| `generic_filecache_max_age` | `1209600000` (14 дней) | Максимальный возраст файлов в file cache ActiveGate в миллисекундах. Возраст считается со времени последнего использования (не со времени загрузки/создания).  Если файл не используется дольше установленного максимального возраста, он автоматически удаляется. Файлы также удаляются из кеша до достижения максимального возраста, если для новых файлов недостаточно места. В первую очередь удаляются LRU-файлы (least recently used). |

Если значение содержит запятую, её нужно экранировать одной обратной косой чертой. Например, `proxy-password = foo\,bar`.

## Секция: [com.compuware.apm.webserver]

| Property | Значение по умолчанию | Описание |
| --- | --- | --- |
| `port-ssl` | `9999` | Порт, на котором ActiveGate слушает трафик от OneAgent — используется для HTTPS-подключения. Настраивается через команду [agctl ssl-port](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#ssl-port "Использование agctl для настройки и управления ActiveGate из командной строки"). Если требуется изменить значение порта, смотрите [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.") и [Extension Execution Controller custom configuration](/managed/ingest-from/extensions/advanced-configuration/eec-custom-configuration "Настройка Extension Execution Controller (EEC)."). |
| `port` | unset | Порт, на котором ActiveGate слушает трафик от OneAgent — используется для HTTP-подключения. По умолчанию отключён. На Linux рекомендуется значение > 1024, чтобы не требовались root-привилегии. |
| `ssl-protocols` | `TLSv1.2`, `TLSv1.3` | Поддерживаемые SSL-протоколы. Одно значение или список через запятую. Учтите: указание конкретной версии не подразумевает автоматическую поддержку всех предыдущих/младших версий, каждую версию нужно указывать явно. Допустимые значения: `TLSv1.2` и `TLSv1.3` |
| `excluded-ciphers` | unset | Список исключённых шифров. Шифры задаются подстрокой, совпадающей хотя бы с частью имени шифра, например: `excluded-ciphers = TLS_RSA_WITH,SHA$,TLS_ECDH` |
| `certificate-file` | unset | Путь к `PKCS#12`-файлу с сертификатами, используемыми web-сервером ActiveGate. Смотрите также [Configuration of custom SSL certificate on ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Настройка SSL-сертификата на ActiveGate."). |
| `certificate-password` | unset | Пароль для файла сертификата. |
| `certificate-alias` | unset | Дружественное имя сертификата в `PKCS#12`-файле. |

#### Работа по HTTPS и HTTP

По умолчанию ActiveGate работает безопасно — обслуживает входящие запросы по HTTPS. Это задаётся свойством `port-ssl`, которое можно изменить в `custom.properties`. Если же требуется, чтобы ActiveGate работал по HTTP, укажите свойство `port` в `custom.properties`.

Учтите: безопасный режим — это режим по умолчанию и рекомендованный. Тем не менее HTTP может быть выбран по соображениям производительности. Например, если перед Cluster ActiveGate стоит балансировщик, терминирующий внешние SSL-подключения (смотрите [третий сценарий развёртывания](/managed/managed-cluster/basics/managed-deployments#scenario-3-integration-with-existing-it-landscape "Эволюция развёртываний Dynatrace Managed от базового внутреннего до глобально распределённой high-availability архитектуры.")).

## Секция: [http.client]

Настройки коммуникации, используемые для мониторинга AWS/VMware/Azure и для коммуникации с Dynatrace Cluster (если не переопределены в `[http.client.internal]`).
В частности, эта секция содержит конфигурационные properties для proxy и таймаутов подключения.

[Задать общие proxy-настройки для коммуникации с Dynatrace Cluster и для мониторинга AWS/VMware/Azure](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#proxy-for-cluster-aws-vmware-azure "Настройка properties ActiveGate для прокси.").

## Секция: [http.client.internal]

Настройки, специфичные для коммуникации только с Dynatrace Cluster.  
В частности, секция может содержать конфигурационные properties для proxy и таймаутов подключения.

Если в секции указано `proxy-off = true`, прокси для коммуникации с Dynatrace Cluster не используется. Если указано свойство `proxy-host`, именно этот прокси будет использоваться для коммуникации с Dynatrace Cluster.

Если секция отсутствует, коммуникация с Dynatrace Cluster определяется настройками из секции `[http.client]`.

ActiveGate версии 1.247 и ранее: если секция `[http.client.internal]` существует, но в ней не указан какой-то параметр коммуникации, то для коммуникации с Dynatrace Cluster значение этого параметра **считается равным значению по умолчанию** (оно **не** наследуется из `[http.client]`).

[Настроить прокси только для коммуникации с Dynatrace Cluster](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#set-up-proxy-only-for-dynatrace-cluster-communication "Настройка properties ActiveGate для прокси.")

## Секция: [http.client.external]

Настройки коммуникации для конкретных модулей: Cloud Foundry, Kubernetes, а также Synthetic Monitoring.  
В частности, секция может содержать конфигурационные properties для proxy и таймаутов подключения.

Если в секции указано `proxy-off = true`, прокси для модулей не используется. Если указано свойство `proxy-host`, именно этот прокси будет использоваться для модулей.

ActiveGate версии 1.247 и ранее

Настройки коммуникации, указанные в `[http.client]`, **не всегда** используются как значения по умолчанию для модулей. Если какой-то параметр **не** указан в `[http.client.external]`, то для Cloud Foundry, Kubernetes или Synthetic Monitoring этот параметр сбросится к заводскому значению по умолчанию, а не к значению из `[http.client]`.

Аналогично, если вся секция `[http.client.external]` отсутствует, все параметры коммуникации для Kubernetes и Cloud Foundry сбросятся к заводским значениям по умолчанию; однако для Synthetic Monitoring будут использоваться значения из секции `[http.client]`.

[Задать общие proxy-настройки для Cloud Foundry, Kubernetes и Synthetic Monitoring](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#specify-common-proxy-settings-for-cloud-foundry-kubernetes-and-synthetic-monitoring "Настройка properties ActiveGate для прокси.")

## Секция: [connectivity]

| Property | Значение по умолчанию | Описание |
| --- | --- | --- |
| `reverseDnsLookupEnabled` | `true` | ActiveGate версии 1.255+: включает или отключает резолвинг FQDN через reverse DNS lookup. Если включено и стандартный резолвинг FQDN не дал результата, делается попытка резолвинга через reverse DNS lookup. ActiveGates, ранее показанные по IP, теперь могут показываться по hostname. Возможные значения: `true` или `false`. |

## Trusted root certificate

**Секция: [collector]**

| Property | Значение по умолчанию | Описание |
| --- | --- | --- |
| `trustedstore` | unset | Ваш trusted keystore (опционально). Свойство `trustedstore` должно содержать путь к файлу с trusted-сертификатами. Путь указывается относительно SSL-директории ActiveGate. Смотрите также [Trusted root certificates for ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Настройка кастомных trusted root certificates на ActiveGate для безопасных SSL/TLS-соединений."). |
| `trustedstore-exclusive` | unset | Если `true`, ActiveGate больше не объединяет встроенный trust store (поставляемый с JRE) с вашим кастомным trust store, указанным в `trustedstore`. Для коммуникации будет использоваться только ваш кастомный trust store. |
| `trustedstore-password` | `changeit` | Пароль вашего trusted keystore (опционально), шифруется при старте ActiveGate. Обфусцированный пароль затем хранится в `trustedstore-password-encr`. |
| `trustedstore-type` | `pkcs12` | Java-формат key/certificate databases по умолчанию (опционально). |