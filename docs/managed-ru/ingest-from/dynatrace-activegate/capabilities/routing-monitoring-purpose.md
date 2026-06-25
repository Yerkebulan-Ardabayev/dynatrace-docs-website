---
title: Маршрутизация трафика OneAgent, мониторинг облачных окружений и удалённых технологий с помощью расширений
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose
scraped: 2026-05-12T11:36:18.837695
---

# Маршрутизация трафика OneAgent, мониторинг облачных окружений и удалённых технологий с помощью расширений

# Маршрутизация трафика OneAgent, мониторинг облачных окружений и удалённых технологий с помощью расширений

* 6-min read
* Published Nov 09, 2018

Функциональность данного типа ActiveGate зависит от установленных или настроенных функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей.").

## Маршрутизация трафика OneAgent

Dynatrace ActiveGate создаёт присутствие Dynatrace в вашей локальной сети. Таким образом, ActiveGate позволяет сосредоточить взаимодействие с Dynatrace в одной точке, доступной локально.

Помимо удобства, это решение оптимизирует объём трафика, снижает сложность сетевых соединений и, соответственно, уменьшает затраты. Кроме того, оно обеспечивает безопасность изолированных сетей.

### Маршрутизация сообщений: функциональность и модули

#### Маршрутизация сообщений

(модуль: [OneAgent routing](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
ActiveGate знает о структуре времени выполнения вашего окружения Dynatrace и маршрутизирует сообщения от экземпляров OneAgent к правильным конечным точкам сервера.

#### Буферизация и сжатие

(модуль: [OneAgent routing](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
ActiveGate собирает сообщения от экземпляров OneAgent и формирует блоки, которые затем отправляются в сжатом виде на серверы Dynatrace. Это позволяет существенно сократить сетевые накладные расходы в зависимости от количества экземпляров OneAgent, взаимодействующих с ActiveGate, и объёма передаваемых данных.

#### Аутентификация

(модуль: [OneAgent routing](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
ActiveGate аутентифицирует запросы OneAgent (SSL-рукопожатие и аутентификация по ID окружения).

#### Доступ к изолированным сетям

(модуль: [OneAgent routing](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#routing_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
Если OneAgent не имеют доступа к интернету, рекомендуется установить ActiveGate в качестве единой точки доступа вместо того, чтобы открывать брандмауэр для нескольких хостов с OneAgent. Такой подход существенно снижает трудозатраты на управление и поддержку конфигурации брандмауэра и/или прокси.

### Дампы памяти

Дампы памяти поступают от OneAgent и могут считаться частью функциональности маршрутизации ActiveGate.

#### Дампы памяти

(модуль: [Memory dumps](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#mem_dump_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
Dynatrace поддерживает автоматический и ручной захват и анализ [дампов памяти](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis "Узнайте, как Dynatrace позволяет инициировать, загружать и анализировать дампы памяти для Java и Node.js.") на мониторируемых хостах. Дампы памяти необходимо хранить в централизованном месте для загрузки и анализа. Поскольку такие дампы часто бывают большими и могут содержать конфиденциальные данные, Dynatrace не позволяет загружать их в кластер Dynatrace в облаке. Вместо этого следует настроить ActiveGate в качестве хоста для дампов памяти. Пользовательский интерфейс Dynatrace предоставляет URL для загрузки через REST API ActiveGate.

## Мониторинг облачных окружений и удалённых технологий

#### Мониторинг AWS

(модуль: [AWS](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#aws-monitoring "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
[Мониторинг сервисов AWS](/managed/observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring "Мониторинг AWS с Dynatrace") является ресурсоёмкой задачей. Поэтому для мониторинга более 2000 ресурсов AWS необходимо установить ActiveGate и настроить мониторинг AWS.

#### Мониторинг Cloud Foundry

(модуль: [Cloud Foundry](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#cf_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
Для подключения ваших фаундейшенов Cloud Foundry к Dynatrace требуется установить экземпляр ActiveGate, дополняющий метрики процессов и хостов Cloud Foundry, собираемые Dynatrace OneAgent, дополнительными метаданными и метриками из Cloud Foundry API. Эта интеграция позволяет использовать [обзорную страницу Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/cloud-foundry-metrics "Доступные метрики для мониторинга кластеров Cloud Foundry с Dynatrace"), а также автоматическое обнаружение организаций Cloud Foundry.

#### Мониторинг Kubernetes/OpenShift

Только Environment ActiveGate

(модуль: [Kubernetes](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#k8s_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
Для подключения кластеров Kubernetes/OpenShift к Dynatrace и использования специальной [обзорной страницы Kubernetes/OpenShift](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-cluster-utilization-kubernetes "Мониторинг работоспособности и использования ресурсов кластера Kubernetes/OpenShift.") необходимо запустить ActiveGate в вашем окружении.

#### Мониторинг Azure

(модуль: [Azure](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#azure_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
Для интеграции данных [мониторинга Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройте и сконфигурируйте мониторинг Azure в Dynatrace.") требуется выделенный ActiveGate для опроса метаданных и метрик из API Azure. Эта интеграция обеспечивает мониторинг сервисов Azure (особенно для облачных сервисов, где установка OneAgent невозможна) через пользовательский интерфейс Dynatrace.

#### Мониторинг с помощью расширения ActiveGate

Только Environment ActiveGate

(модуль: [Extensions](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
С помощью [расширений ActiveGate](/managed/ingest-from/extend-dynatrace "Узнайте, какие механизмы расширения предлагает Dynatrace.") вы можете расширить мониторинг Dynatrace на любую удалённую технологию, предоставляющую интерфейс, где установка OneAgent невозможна. Например, PaaS-технологии, сетевые устройства или облачные технологии. Расширения ActiveGate (также называемые remote plugins) выполняются на ActiveGate и могут получать метрики и топологическую информацию из удалённых источников, полностью интегрируя мониторинг удалённых технологий в Dynatrace Smartscape и обнаружение проблем.

#### Аналитика баз данных Oracle

(модуль: [Database insights](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#oracle_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
[Database insights](/managed/observe/infrastructure-observability/databases/database-services-classic/database-insights "Узнайте, как расширить мониторинг баз данных до уровня инфраструктуры.") добавляет инфраструктурную перспективу в мониторинг баз данных. Дополнительные данные, получаемые из слоя базы данных, позволяют решать проблемы производительности, уходящие корнями глубоко в базу данных.

#### Мониторинг виртуализированной инфраструктуры

(модуль: [VMware](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#vmware "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
ActiveGate может опрашивать [vCenter или автономные хосты ESXi](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Мониторинг VMware vSphere с Dynatrace.") для получения информации обо всех важных ресурсах, выделяемых ESXi-серверами виртуальным машинам (например, использование CPU, потребление памяти, активность хранилищ данных). Для получения этой информации в вашем окружении должен быть установлен компонент с доступом к vCenter API.

## Dynatrace API

Dynatrace ActiveGate предоставляет конечные точки для доступа к [Dynatrace API](/managed/dynatrace-api "Узнайте, что нужно для использования Dynatrace API."). Перечисленные ниже типы вызовов API обрабатываются или предварительно обрабатываются на ActiveGate до передачи в кластер Dynatrace. Прочие вызовы API перенаправляются напрямую в кластер.
ActiveGate поддерживает вызовы ко всем конечным точкам версий v1 и v2 API конфигурации и окружения Dynatrace.

#### Мониторинг логов

(модуль: [Log Monitoring](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
С [мониторингом логов](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить мониторинг логов, какие аналитические данные он предоставляет и многое другое.") как частью платформы Dynatrace вы получаете прямой доступ к содержимому логов всех ключевых процессов. Вы можете создавать пользовательские метрики логов для более быстрого и умного устранения неполадок.

#### Приём метрик

(модуль: [HTTP Metric API](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#metric_api_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
[Приём метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.") предоставляет простой способ отправки любых пользовательских метрик в Dynatrace. Вы можете дополнительно разбивать метрики по категориям.

#### Приём трейсов OpenTelemetry

(модуль: [OTLP Ingest](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#otlp_ingest_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
Вы можете отправлять [данные трейсов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API для экспорта данных OpenTelemetry в Dynatrace.") (трейсы и спаны) в формате OTLP в Dynatrace через API, доступный на Dynatrace ActiveGate. Принятые спаны интегрируются в PurePath® распределённые трейсы.

#### Приём метрик OpenTelemetry

(модуль: [OTLP Ingest](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#otlp_ingest_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
Вы можете отправлять [метрические данные OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API для экспорта данных OpenTelemetry в Dynatrace.") в формате OTLP в Dynatrace через API на Dynatrace ActiveGate.

#### Приём логов OpenTelemetry

(модуль: [Log Monitoring](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
Вы можете отправлять [данные логов OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API для экспорта данных OpenTelemetry в Dynatrace.") в формате OTLP в Dynatrace через API на Dynatrace ActiveGate.

#### Real User Monitoring

(модуль: [Beacon forwarder](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#bf_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))
Инфраструктура Dynatrace может использоваться в качестве [конечной точки для без-агентного мониторинга приложений](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Измените URL конечной точки beacon по умолчанию и отправляйте RUM-маяки в инфраструктуру Dynatrace или другой инструментированный веб-сервер."). Автоматически инструментируемые приложения отправляют маяк обратно на веб-сервер клиента, минуя необходимость в сторонних доменах.