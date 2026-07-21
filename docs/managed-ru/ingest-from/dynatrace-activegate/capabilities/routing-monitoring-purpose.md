---
title: Маршрутизация трафика OneAgent к Dynatrace, мониторинг облачных сред и удалённых технологий с помощью extensions
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose
---

# Маршрутизация трафика OneAgent к Dynatrace, мониторинг облачных сред и удалённых технологий с помощью extensions

# Маршрутизация трафика OneAgent к Dynatrace, мониторинг облачных сред и удалённых технологий с помощью extensions

* Чтение за 6 минут
* Опубликовано 09 ноя 2018

Функциональность, предоставляемая этими типами ActiveGate, зависит от функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."), которые в данный момент установлены или настроены.

## Маршрутизация трафика OneAgent

Dynatrace ActiveGate обеспечивает присутствие Dynatrace, компонент Dynatrace, в локальной сети. Таким образом Dynatrace ActiveGate позволяет свести взаимодействие с Dynatrace к одной единственной точке, доступной локально.
Помимо удобства, это решение также оптимизирует объём трафика и снижает сложность сетевых подключений, а следовательно, снижает затраты. Оно также обеспечивает безопасность закрытых сетей.

### Функциональность маршрутизации сообщений и модули

#### Маршрутизация сообщений

(модуль: [маршрутизация OneAgent](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))
ActiveGate знает структуру среды выполнения Dynatrace и маршрутизирует сообщения от экземпляров OneAgent к нужным конечным точкам сервера.

#### Буферизация и сжатие

(модуль: [маршрутизация OneAgent](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))
ActiveGate собирает сообщения от экземпляров OneAgent и формирует из них пакеты, которые затем отправляются в сжатом виде на серверы Dynatrace. Это может значительно снизить сетевую нагрузку, в зависимости от количества экземпляров OneAgent, взаимодействующих с ActiveGate, и объёма передаваемых ими данных.

#### Аутентификация

(модуль: [маршрутизация OneAgent](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))
ActiveGate аутентифицирует запросы OneAgent (SSL-рукопожатие и аутентификация по ID среды).

#### Доступ к закрытым сетям

(модуль: [маршрутизация OneAgent](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))
Если у OneAgent нет доступа в интернет, нужно установить ActiveGate, который будет служить единой точкой доступа, вместо того чтобы открывать файервол для нескольких хостов, на которых работают OneAgent. Такой подход значительно снижает трудозатраты на управление настройками файервола и/или прокси и их обслуживание.

### Дампы памяти

Дампы памяти поступают от OneAgent и поэтому могут считаться частью функциональности маршрутизации ActiveGate.

#### Дампы памяти

(модуль: [Дампы памяти](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#mem_dump_mod "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))
Dynatrace поддерживает как автоматический, так и ручной захват и анализ [дампов памяти](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis "Узнать, как Dynatrace позволяет запускать, скачивать и анализировать дампы памяти для Java и Node.js.") на отслеживаемых хостах. Дампы памяти нужно хранить в централизованном месте для скачивания и анализа. Поскольку такие дампы часто имеют большой размер и могут содержать конфиденциальные данные, Dynatrace не позволяет загружать дампы в кластер Dynatrace в облаке. Вместо этого нужно настроить ActiveGate и сконфигурировать его в качестве хоста для дампов памяти. Интерфейс Dynatrace предоставляет URL-адреса для скачивания с ActiveGate REST API, который обслуживает дампы.

## Мониторинг облачных сред и удалённых технологий

#### Мониторинг AWS

(модуль: [AWS](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#aws-monitoring "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))
[Мониторинг сервисов AWS](/managed/observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring "Мониторинг AWS с помощью Dynatrace"), ресурсоёмкая задача. Поэтому для мониторинга более 2000 ресурсов AWS нужно установить ActiveGate и настроить мониторинг AWS.

#### Мониторинг Cloud Foundry

(модуль: [Cloud Foundry](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#cf_mod "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))
Чтобы подключить фундаменты Cloud Foundry к Dynatrace, нужно установить экземпляр ActiveGate, дополняющий метрики уровня процессов и хостов Cloud Foundry, собираемые OneAgent Dynatrace, дополнительными метаданными и метриками, получаемыми из API Cloud Foundry. Эта интеграция позволяет использовать [страницу обзора Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/cloud-foundry-metrics "Доступные метрики для мониторинга кластеров Cloud Foundry с помощью Dynatrace"), а также автоматическое обнаружение организаций Cloud Foundry в дополнение к другим свойствам процессов Cloud Foundry, таким как `space`, `space ID`, `application`, `application ID` и `instance index`.

#### Мониторинг Kubernetes/OpenShift

Только Environment ActiveGate

(модуль: [Kubernetes](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#k8s_mod "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))
Чтобы подключить кластеры Kubernetes/OpenShift к Dynatrace и воспользоваться преимуществами специальной [страницы обзора Kubernetes/OpenShift](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-cluster-utilization-kubernetes "Мониторинг работоспособности и утилизации ресурсов кластера Kubernetes/OpenShift."), нужно запустить ActiveGate в среде.

#### Мониторинг Azure

(модуль: [Azure](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#azure_mod "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))
Для интеграции данных [мониторинга Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настроить и сконфигурировать мониторинг Azure в Dynatrace.") требуется специальный ActiveGate для опроса метаданных и метрик из API Azure. Эта интеграция обеспечивает мониторинг сервисов Azure (особенно для облачных сервисов, на которых нельзя установить OneAgent), а также мониторинг через интерфейс Dynatrace.

#### Мониторинг с помощью extension ActiveGate

Только Environment ActiveGate

(модуль: [Extensions](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))  
С помощью [extensions ActiveGate](/managed/ingest-from/extend-dynatrace "Узнать, какие механизмы extension предлагает Dynatrace.") можно расширить мониторинг Dynatrace на любую удалённую технологию, предоставляющую интерфейс, там, где установка OneAgent невозможна. Например, PaaS-технологии, сетевые устройства или облачные технологии. Extensions ActiveGate (также известные как remote plugins) выполняются на ActiveGate и могут получать метрики и информацию о топологии из удалённых источников, тем самым полностью интегрируя мониторинг удалённых технологий в Smartscape и обнаружение проблем Dynatrace.

#### Database insights для Oracle

(модуль: [Database insights](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#oracle_mod "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))
[Database insights](/managed/observe/infrastructure-observability/database-services-classic/database-insights "Узнать, как расширить мониторинг базы данных на уровень инфраструктуры базы данных.") добавляют перспективу инфраструктуры к мониторингу базы данных. С помощью дополнительных данных, получаемых с уровня базы данных, можно решать проблемы производительности, коренящиеся глубоко в базе данных.

#### Мониторинг виртуализированной инфраструктуры

(модуль: [VMware](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#vmware "Узнать, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."))
ActiveGate может опрашивать [vCenter или автономные хосты ESXi](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Мониторинг VMware vSphere с помощью Dynatrace."), чтобы получать информацию обо всех важных ресурсах, которые серверы ESXi предоставляют виртуальным машинам (например, использование CPU, потребление памяти и активность, связанную с хранилищами данных на платформе VMware). Для получения этой информации Dynatrace нужен компонент, установленный в среде, который имеет доступ к API vCenter.

## Dynatrace API

Dynatrace ActiveGate предоставляет эндпоинты для доступа к [Dynatrace API](/managed/dynatrace-api "Find out what you need to use the Dynatrace API."). Перечисленные ниже типы вызовов API обрабатываются или предварительно обрабатываются на ActiveGate, прежде чем задействуется Cluster Dynatrace. Остальные вызовы API пересылаются напрямую в Cluster Dynatrace.  
ActiveGate поддерживает вызовы всех эндпоинтов версий v1 и v2 API Configuration и Environment Dynatrace.

#### Log Monitoring

(модуль: [Log Monitoring](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "Learn which ActiveGate properties you can configure based on your needs and requirements."))
С [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") как частью платформы Dynatrace появляется прямой доступ к содержимому логов всех критически важных для бизнеса процессов. Можно создавать пользовательские метрики логов для более быстрого и умного устранения неполадок. Данные логов можно понимать в контексте всего стека, включая влияние на реальных пользователей.

#### Metric ingestion

(модуль: [HTTP Metric API](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#metric_api_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
[Metric ingestion](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.") даёт простой способ отправлять любые пользовательские метрики в Dynatrace. Метрики можно дополнительно разбивать по категориям.

#### OpenTelemetry trace ingestion

(модуль: [OTLP Ingest](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#otlp_ingest_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
Можно отправлять [данные трассировки OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (traces и spans) в формате OTLP в Dynatrace через API, доступный на Dynatrace ActiveGate. Полученные spans интегрируются в распределённые трассировки PurePath®.

#### OpenTelemetry metric ingestion

(модуль: [OTLP Ingest](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#otlp_ingest_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
Можно отправлять [данные метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") в формате OTLP в Dynatrace через API, доступный на Dynatrace ActiveGate.

#### OpenTelemetry log ingestion

(модуль: [Log Monitoring](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "Learn which ActiveGate properties you can configure based on your needs and requirements."))
Можно отправлять [данные логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") в формате OTLP в Dynatrace через API, доступный на Dynatrace ActiveGate.

#### Real User Monitoring

(модуль: [Beacon forwarder](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#bf_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))
Инфраструктуру Dynatrace можно использовать как эндпоинт beacon по умолчанию [для мониторинга приложений без агента](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server."). Приложения с автоматическим внедрением отправляют beacon обратно на веб-сервер заказчика, минуя необходимость в стороннем домене. Однако при необходимости такие приложения также могут использовать инфраструктуру Dynatrace как эндпоинт для сигналов мониторинга RUM.