---
title: Все облачные сервисы Azure
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics
scraped: 2026-03-06T21:17:44.007967
---

# Все облачные сервисы Azure

# Все облачные сервисы Azure

* Последняя версия Dynatrace
* Обзор
* 19 минут чтения
* Обновлено 12 февраля 2024 г.

Dynatrace может получать метрики Azure Monitor для нескольких предварительно выбранных сервисов.

* Вы можете просматривать графики для каждого экземпляра сервиса с набором измерений, а также создавать пользовательские графики, которые можно закрепить на дашбордах.
* Вы можете снизить затраты на Azure Monitor и риск превышения лимитов, выбрав, какие дополнительные сервисы мониторить.
* Для неклассических (ранее называвшихся «невстроенными») сервисов можно выбрать, какие метрики отслеживать.

## Облачные сервисы Azure, мониторируемые по умолчанию

В результате [интеграции мониторинга Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройте и сконфигурируйте мониторинг Azure в Dynatrace.") некоторые сервисы мониторируются «из коробки».

[Служба управления API Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-service) [Шлюзы приложений Azure (классические)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-app-gateways-builtin) [Служба приложений Azure (классическая)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-azure-app-service-builtin) [Cosmos DB Azure (классическая)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-builtin) [Концентраторы событий Azure (классические)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-hub-builtin) [IoT Hub Azure (классический)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub-builtin) [Балансировщики нагрузки Azure (классические)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-load-balancers-builtin) [Кэш Redis Azure (классический)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-redis-cache-builtin) [Служебная шина Azure (классическая)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-service-bus-builtin) [SQL Server Azure (классический)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-servers-builtin) [Виртуальные машины Azure (классические)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-builtin) [Учётная запись хранения Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account)

Информацию о различиях между классическими и другими сервисами см. в разделе [Миграция с классических сервисов Azure (ранее «встроенных») на облачные сервисы](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-migration-guide "Мигрируйте классические сервисы Azure на новые версии.").

## Другие облачные сервисы Azure

Помимо сервисов, мониторируемых по умолчанию, вы можете также мониторить другие сервисы Azure, влияющие на производительность ваших приложений, размещённых на Azure.

[Azure AI — Универсальный](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-all-in-one) [Azure AI — Anomaly Detector](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-anomaly-detector) [Azure AI — Bing Autosuggest](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-autosuggest) [Azure AI — Bing Custom Search](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-custom-search) [Azure AI — Bing Entity Search](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-entity-search) [Azure AI — Bing Search](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-search) [Azure AI — Bing Spell Check](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-bing-spell-check) [Azure AI — Computer Vision](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-computer-vision) [Azure AI — Content Moderator](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-content-moderator) [Azure AI — Custom Vision Prediction](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-custom-vision-prediction) [Azure AI — Custom Vision Training](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-custom-vision-training) [Azure AI — Face](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-face) [Azure AI — Immersive Reader](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-immersive-reader) [Azure AI — Ink Recognizer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cognitive-services-ink-recognizer) [Azure AI — Language Understanding (LUIS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-language-understanding) [Azure AI — Language Understanding (LUIS) Authoring](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-language-understanding-authoring) [Azure AI — OpenAI](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-openai) [Azure AI — Personalizer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-personalizer) [Azure AI — QnA Maker](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-qna-maker) [Azure AI — Speech](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-speech) [Azure AI — Text Analytics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-text-analytics) [Azure AI — Translator](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-translator) [Службы управления API Azure (классические, устаревшие)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-api-management-services-builtin) [Конфигурация приложений Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-app-configuration) [Служба приложений Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-app-service) [![Azure App Env v2](https://dt-cdn.net/images/azure-app-service-environment-v2-5888da78cc.svg "Azure App Env v2")Среда службы приложений Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/monitor-azure-app-service-environment) [Шлюз приложений Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-gateway) [Application Insights Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-application-insights) [Учётная запись автоматизации Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-automation-account) [Базовый балансировщик нагрузки Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-basic-load-balancer) [Azure Batch](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-batch) [Azure Blockchain](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-blockchain-service) [Кэш Azure для Redis](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cache-for-redis) [Контейнерное приложение Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-app) [Среда контейнерных приложений Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-apps-environment) [Экземпляры контейнеров Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-instances) [Реестр контейнеров Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-container-registry) [Учётная запись Azure Cosmos DB (GlobalDocumentDB)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-globaldocumentdb) [Учётная запись Azure Cosmos DB (MongoDB)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-cosmos-db-account-mongodb) [Azure Data Explorer](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-explorer-cluster) [Azure Data Factory](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-factory) [Azure Data Lake Analytics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-lake-analytics) [Azure Data Lake Storage](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-lake-storage-gen1) [Azure Data Share](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-data-share) [База данных Azure для MariaDB](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mariadb) [База данных Azure для MySQL (гибкие серверы)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql-flexible-servers) [База данных Azure для MySQL](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-mysql) [База данных Azure для PostgreSQL](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-db-postgresql) [Служба подготовки устройств Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-device-provisioning-service) [Зона DNS Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-dns-zone) [Event Grid Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-grid) [Концентраторы событий Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-hubs) [Канал ExpressRoute Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-expressroute-circuit) [Брандмауэр Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-firewall) [Azure Front Door (классический)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door) [Профили Azure Front Door Standard/Premium и CDN](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door-cdn-profiles) [Шлюзовой балансировщик нагрузки Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-gateway-load-balancer) [Azure HDInsight](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-hdinsight) [Среда службы интеграции Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-integration-service-environment) [Центральные приложения IoT Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-central-applications) [Azure IoT Hub](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-iot-hub) [Azure Key Vault](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-key-vault) [Служба Azure Kubernetes (AKS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks/monitor-azure-kubernetes-service) [Приложения логики Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-logic-apps) [Компьютер Azure — Azure Arc](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-arc) [Машинное обучение Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-machine-learning) [Учётная запись Azure Maps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-maps-account) [Службы мультимедиа Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-media-service) [Приложение сетки Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-mesh-application) [Файлы Azure NetApp](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-netapp-files) [Сетевой интерфейс Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-network-interface) [Наблюдатель за сетью Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-network-watcher) [Концентратор уведомлений Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-notification-hub) [Azure Power BI](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-power-bi) [Частная зона DNS Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-private-dns-zone) [Общедоступный IP-адрес Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-public-ip-addresses) [Хранилище служб восстановления Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-recovery-services-vault) [Azure Relay](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-relay) [Служба поиска Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-search) [Azure Service Fabric](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-service-fabric) [Azure SignalR](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-signalr) [Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps) [База данных SQL Azure (DTU)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-dtu) [База данных SQL Azure Hyperscale](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-hyperscale) [База данных SQL Azure (vCore)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-database-vcore) [Хранилище данных SQL Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-data-warehouse) [Эластичный пул SQL Azure (DTU)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-dtu) [Эластичный пул SQL Azure (vCore)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-elastic-pool-vcore) [Управляемый экземпляр SQL Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-managed-instance) [SQL Server Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-sql-server) [Стандартный балансировщик нагрузки Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-standard-load-balancer) [Учётная запись хранения Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account) [Учётные записи хранения Azure (классические)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-builtin) [Классическая учётная запись хранения Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-account-classic) [Синхронизация хранилища Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-storage-sync) [Azure Stream Analytics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-stream-analytics) [Azure Synapse Analytics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-synapse-analytics) [Аналитика временных рядов Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-time-series-insights) [Диспетчер трафика Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-traffic-manager) [Классические виртуальные машины Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic) [Шлюз виртуальной сети Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-virtual-network-gateways) [Политика брандмауэра веб-приложений Azure (WAF) на Azure CDN](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-web-application-firewall-policies)

## Облачные сервисы и соответствующие типы сущностей Dynatrace

Не для всех облачных сервисов создаются сущности Dynatrace и не для всех из них можно импортировать теги из облака. Разверните таблицу ниже, чтобы просмотреть облачные сервисы с соответствующими типами сущностей Dynatrace и проверить, импортируются ли для них теги от поставщика облака.

### Список сервисов Azure с сущностями и тегами

| Сервис | Тип облака | Мониторинг и фильтрация тегов | Тип сущности Dynatrace |
| --- | --- | --- | --- |
| Службы управления API Azure (встроенные, устаревшие) | Microsoft.ApiManagement/service | Применимо | AZURE\_API\_MANAGEMENT\_SERVICE |
| Служба управления API Azure | Microsoft.ApiManagement/service | Применимо | cloud:azure:apimanagement:service, CUSTOM\_DEVICE |
| Контейнерное приложение Azure | Microsoft.App/containerApps | Применимо | cloud:azure:app:containerapps, CUSTOM\_DEVICE |
| Среда контейнерных приложений Azure | Microsoft.App/managedEnvironments | Применимо | cloud:azure:app:managedenvironments, CUSTOM\_DEVICE |
| Конфигурация приложений Azure | Microsoft.AppConfiguration/configurationStores | Применимо | cloud:azure:appconfiguration:configurationstores, CUSTOM\_DEVICE |
| Azure Spring Apps | Microsoft.AppPlatform/Spring | Применимо | cloud:azure:appplatform:spring, CUSTOM\_DEVICE |
| Учётная запись автоматизации Azure | Microsoft.Automation/automationAccounts | Применимо | cloud:azure:automation:automationaccounts, CUSTOM\_DEVICE |
| Учётная запись Azure Batch | Microsoft.Batch/batchAccounts | Применимо | cloud:azure:batch:account, CUSTOM\_DEVICE |
| Служба блокчейн Azure | Microsoft.Blockchain/blockchainMembers | Применимо | cloud:azure:blockchain:blockchainmembers, CUSTOM\_DEVICE |
| Кэш Azure для Redis | Microsoft.Cache/redis | Применимо | cloud:azure:cache:redis, CUSTOM\_DEVICE |
| Azure Redis (встроенный) | Microsoft.Cache/redis | Применимо | AZURE\_REDIS\_CACHE |
| Политика Azure CDN WAF | Microsoft.Cdn/cdnwebapplicationfirewallpolicies | Применимо | cloud:azure:cdn:cdnwebapplicationfirewallpolicies, CUSTOM\_DEVICE |
| Классическая виртуальная машина Azure | Microsoft.ClassicCompute/virtualMachines | Применимо | cloud:azure:classic\_virtual\_machine, CUSTOM\_DEVICE |
| Классическая учётная запись хранения Azure | Microsoft.ClassicStorage/storageAccounts | Применимо | cloud:azure:classic\_storage\_account, CUSTOM\_DEVICE |
| Классические службы BLOB-объектов хранилища Azure | Microsoft.ClassicStorage/storageAccounts | Применимо | cloud:azure:classic\_storage\_account:blob, CUSTOM\_DEVICE |
| Классические файловые службы хранилища Azure | Microsoft.ClassicStorage/storageAccounts | Применимо | cloud:azure:classic\_storage\_account:file, CUSTOM\_DEVICE |
| Классические службы очередей хранилища Azure | Microsoft.ClassicStorage/storageAccounts | Применимо | cloud:azure:classic\_storage\_account:queue, CUSTOM\_DEVICE |
| Классические службы таблиц хранилища Azure | Microsoft.ClassicStorage/storageAccounts | Применимо | cloud:azure:classic\_storage\_account:table, CUSTOM\_DEVICE |
| Azure Anomaly Detector | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:anomalydetector, CUSTOM\_DEVICE |
| Azure Bing Autosuggest | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:bingautosuggest, CUSTOM\_DEVICE |
| Azure Bing Custom Search | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:bingcustomsearch, CUSTOM\_DEVICE |
| Azure Bing Entity Search | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:bingentitysearch, CUSTOM\_DEVICE |
| Azure Bing Search | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:bingsearch, CUSTOM\_DEVICE |
| Azure Bing Spell Check | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:bingspellcheck, CUSTOM\_DEVICE |
| Azure AI (универсальный) | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:allinone, CUSTOM\_DEVICE |
| Azure Computer Vision | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:computervision, CUSTOM\_DEVICE |
| Azure AI Content Moderator | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:contentmoderator, CUSTOM\_DEVICE |
| Azure Custom Vision Prediction | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:customvisionprediction, CUSTOM\_DEVICE |
| Azure Custom Vision Training | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:customvisiontraining, CUSTOM\_DEVICE |
| Azure Face | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:face, CUSTOM\_DEVICE |
| Azure Immersive Reader | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:immersivereader, CUSTOM\_DEVICE |
| Azure Ink Recognizer | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:inkrecognizer, CUSTOM\_DEVICE |
| Azure Language Understanding (LUIS) | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:luis, CUSTOM\_DEVICE |
| Azure Language Understanding Authoring (LUIS) | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:luisauthoring, CUSTOM\_DEVICE |
| Azure Machine Azure Arc | Microsoft.Hybridcompute/machines | Применимо | cloud:azure:hybridcompute:machines, CUSTOM\_DEVICE |
| Azure OpenAI | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:openai, CUSTOM\_DEVICE |
| Azure Personalizer | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:personalizer, CUSTOM\_DEVICE |
| Azure QnA Maker | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:qnamaker, CUSTOM\_DEVICE |
| Хранилище служб восстановления Azure | Microsoft.RecoveryServices/Vaults | Применимо | cloud:azure:recoveryservices:vaults, CUSTOM\_DEVICE |
| Azure Speech | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:speech, CUSTOM\_DEVICE |
| Azure Text Analytics | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:textanalytics, CUSTOM\_DEVICE |
| Azure Translator | Microsoft.CognitiveServices/accounts | Применимо | cloud:azure:cognitiveservices:translator, CUSTOM\_DEVICE |
| Виртуальные машины Azure (встроенные) | Microsoft.Compute/virtualMachines | Применимо | AZURE\_VM |
| Виртуальные машины Azure (встроенные) | Microsoft.Compute/virtualMachineScaleSets | Применимо | AZURE\_VM\_SCALE\_SET |
| Экземпляр контейнера Azure | Microsoft.ContainerInstance/containerGroups | Применимо | cloud:azure:containerinstance:containergroup, CUSTOM\_DEVICE |
| Реестр контейнеров Azure | Microsoft.ContainerRegistry/registries | Применимо | cloud:azure:containerregistry:registries, CUSTOM\_DEVICE |
| Служба Azure Kubernetes (AKS) | Microsoft.ContainerService/managedClusters | Применимо | cloud:azure:containerservice:managedcluster, CUSTOM\_DEVICE |
| Azure Data Factory v1 | Microsoft.DataFactory/dataFactories | Применимо | cloud:azure:datafactory:v1, CUSTOM\_DEVICE |
| Azure Data Factory v2 | Microsoft.DataFactory/factories | Применимо | cloud:azure:datafactory:v2, CUSTOM\_DEVICE |
| Azure Data Lake Analytics | Microsoft.DataLakeAnalytics/accounts | Применимо | cloud:azure:datalakeanalytics:accounts, CUSTOM\_DEVICE |
| Azure Data Lake Storage Gen1 | Microsoft.DataLakeStore/accounts | Применимо | cloud:azure:datalakestore:accounts, CUSTOM\_DEVICE |
| Azure Data Share | Microsoft.DataShare/accounts | Применимо | cloud:azure:datashare:accounts, CUSTOM\_DEVICE |
| Azure DB для MariaDB | Microsoft.DBforMariaDB/servers | Применимо | cloud:azure:mariadb:server, CUSTOM\_DEVICE |
| Azure DB для MySQL (гибкие серверы) | Microsoft.DBforMySQL/flexibleServers | Применимо | cloud:azure:mysql:flexibleservers, CUSTOM\_DEVICE |
| Azure DB для MySQL | Microsoft.DBforMySQL/servers | Применимо | cloud:azure:mysql:server, CUSTOM\_DEVICE |
| Azure DB для PostgreSQL (гибкий сервер) | Microsoft.DBforPostgreSQL/flexibleServers | Применимо | cloud:azure:postgresql:flexibleservers, CUSTOM\_DEVICE |
| Azure DB для PostgreSQL Server | Microsoft.DBforPostgreSQL/servers | Применимо | cloud:azure:postgresql:server, CUSTOM\_DEVICE |
| Azure DB для PostgreSQL Hyperscale | Microsoft.DBforPostgreSQL/serversv2 | Применимо | cloud:azure:postgresql:serverv2, CUSTOM\_DEVICE |
| Azure IoT Hubs (встроенные) | Microsoft.Devices/IotHubs | Применимо | AZURE\_IOT\_HUB |
| Azure IoT Hub | Microsoft.Devices/IotHubs | Применимо | cloud:azure:devices:iothubs, CUSTOM\_DEVICE |
| Служба подготовки устройств Azure | Microsoft.Devices/provisioningServices | Применимо | cloud:azure:devices:provisioningservices, CUSTOM\_DEVICE |
| Учётная запись Azure Cosmos DB (GlobalDocumentDB) | Microsoft.DocumentDB/databaseAccounts | Применимо | cloud:azure:documentdb:databaseaccounts:global, CUSTOM\_DEVICE |
| Учётная запись Azure Cosmos DB (MongoDB) | Microsoft.DocumentDB/databaseAccounts | Применимо | cloud:azure:documentdb:databaseaccounts:mongo, CUSTOM\_DEVICE |
| Azure Cosmos DB (встроенная) | Microsoft.DocumentDB/databaseAccounts | Применимо | AZURE\_COSMOS\_DB |
| Домен Event Grid Azure | Microsoft.EventGrid/domains | Применимо | cloud:azure:eventgrid:domains, CUSTOM\_DEVICE |
| Системная тема Event Grid Azure | Microsoft.EventGrid/systemTopics | Применимо | cloud:azure:eventgrid:systemtopics, CUSTOM\_DEVICE |
| Тема Event Grid Azure | Microsoft.EventGrid/topics | Применимо | cloud:azure:eventgrid:topics, CUSTOM\_DEVICE |
| Кластер концентраторов событий Azure | Microsoft.EventHub/clusters | Применимо | cloud:azure:eventhub:clusters, CUSTOM\_DEVICE |
| Концентраторы событий Azure (встроенные) | Microsoft.EventHub/namespaces | Применимо | AZURE\_EVENT\_HUB\_NAMESPACE |
| Концентраторы событий Azure (встроенные) | Microsoft.EventHub/namespaces/eventhubs | Не применимо | AZURE\_EVENT\_HUB |
| Кластер Azure HDInsight | Microsoft.HDInsight/clusters | Применимо | cloud:azure:hdinsight:cluster, CUSTOM\_DEVICE |
| Azure Machine Azure Arc | Microsoft.hybridcompute/machines | Применимо | cloud:azure:hybridcompute:machines, CUSTOM\_DEVICE |
| Azure Application Insights | Microsoft.Insights/components | Применимо | cloud:azure:insights:components, CUSTOM\_DEVICE |
| Центральное приложение Azure IoT | Microsoft.IoTCentral/IoTApps | Применимо | cloud:azure:iotcentral:iotapps, CUSTOM\_DEVICE |
| Azure Key Vault | Microsoft.KeyVault/vaults | Применимо | cloud:azure:keyvault:vaults, CUSTOM\_DEVICE |
| Кластер Azure Data Explorer | Microsoft.Kusto/Clusters | Применимо | cloud:azure:kusto:clusters, CUSTOM\_DEVICE |
| Среда службы интеграции Azure | Microsoft.Logic/integrationServiceEnvironments | Применимо | cloud:azure:logic:integrationserviceenvironments, CUSTOM\_DEVICE |
| Приложения логики Azure | Microsoft.Logic/workflows | Применимо | cloud:azure:logic:workflows, CUSTOM\_DEVICE |
| Рабочая область машинного обучения Azure | Microsoft.MachineLearningServices/workspaces | Применимо | cloud:azure:machinelearningservices:workspaces, CUSTOM\_DEVICE |
| Учётная запись Azure Maps | Microsoft.Maps/accounts | Применимо | cloud:azure:maps:accounts, CUSTOM\_DEVICE |
| Служба мультимедиа Azure | Microsoft.Media/mediaservices | Применимо | cloud:azure:media:mediaservices, CUSTOM\_DEVICE |
| Конечная точка потоковой передачи Azure | Microsoft.Media/mediaservices/streamingEndpoints | Применимо | cloud:azure:media:mediaservices:streamingendpoints, CUSTOM\_DEVICE |
| Пул ёмкости Azure NetApp | Microsoft.NetApp/netAppAccounts/capacityPools | Применимо | cloud:azure:netapp:netappaccounts:capacitypools, CUSTOM\_DEVICE |
| Том Azure NetApp | Microsoft.NetApp/netAppAccounts/capacityPools/volumes | Применимо | cloud:azure:netapp:netappaccounts:capacitypools:volumes, CUSTOM\_DEVICE |
| Шлюз приложений Azure | Microsoft.Network/applicationGateways | Применимо | cloud:azure:network:applicationgateways, CUSTOM\_DEVICE |
| Шлюз приложений Azure (встроенный) | Microsoft.Network/applicationGateways | Применимо | AZURE\_APPLICATION\_GATEWAY |
| Брандмауэр Azure | Microsoft.Network/azurefirewalls | Применимо | cloud:azure:network:azurefirewalls, CUSTOM\_DEVICE |
| Зона DNS Azure | Microsoft.Network/dnszones | Применимо | cloud:azure:network:dnszones, CUSTOM\_DEVICE |
| Канал ExpressRoute Azure | Microsoft.Network/expressRouteCircuits | Применимо | cloud:azure:network:expressroutecircuits, CUSTOM\_DEVICE |
| Azure Front Door | Microsoft.Network/frontdoors | Применимо | cloud:azure:frontdoor, CUSTOM\_DEVICE |
| Профили Azure Front Door и CDN | Microsoft.Cdn/Profiles | Применимо | cloud:azure:cdn:profiles, CUSTOM\_DEVICE |
| Базовый балансировщик нагрузки Azure | Microsoft.Network/loadBalancers | Применимо | cloud:azure:network:loadbalancers:basic, CUSTOM\_DEVICE |
| Шлюзовой балансировщик нагрузки Azure | Microsoft.Network/loadBalancers | Применимо | cloud:azure:network:loadbalancers:gateway, CUSTOM\_DEVICE |
| Стандартный балансировщик нагрузки Azure | Microsoft.Network/loadBalancers | Применимо | cloud:azure:network:loadbalancers:standard, CUSTOM\_DEVICE |
| Балансировщик нагрузки Azure (встроенный) | Microsoft.Network/loadBalancers | Применимо | AZURE\_LOAD\_BALANCER |
| Сетевой интерфейс Azure | Microsoft.Network/networkInterfaces | Применимо | cloud:azure:network:networkinterfaces, CUSTOM\_DEVICE |
| Мониторы подключений Azure | Microsoft.Network/networkWatchers/connectionMonitors | Применимо | cloud:azure:network:networkwatchers:connectionmonitors, CUSTOM\_DEVICE |
| Предварительный просмотр мониторов подключений Azure | Microsoft.Network/networkWatchers/connectionMonitors | Применимо | cloud:azure:network:networkwatchers:connectionmonitors:preview, CUSTOM\_DEVICE |
| Частная зона DNS Azure | Microsoft.Network/privateDnsZones | Применимо | cloud:azure:network:privatednszones, CUSTOM\_DEVICE |
| Общедоступный IP-адрес Azure | Microsoft.Network/publicIPAddresses | Применимо | cloud:azure:network:publicipaddresses, CUSTOM\_DEVICE |
| Профиль диспетчера трафика Azure | Microsoft.Network/trafficManagerProfiles | Применимо | cloud:azure:traffic\_manager\_profile, CUSTOM\_DEVICE |
| Шлюз виртуальной сети Azure | Microsoft.Network/virtualNetworkGateways | Применимо | cloud:azure:virtual\_network\_gateway, CUSTOM\_DEVICE |
| Концентратор уведомлений Azure | Microsoft.NotificationHubs/namespaces/notificationHubs | Применимо | cloud:azure:notificationhubs:namespaces:notificationhubs, CUSTOM\_DEVICE |
| Azure Power BI Embedded | Microsoft.PowerBIDedicated/capacities | Применимо | cloud:azure:powerbidedicated:capacities, CUSTOM\_DEVICE |
| Хранилище служб восстановления Azure | Microsoft.RecoveryServices/Vaults | Применимо | cloud:azure:recoveryservices:vaults, CUSTOM\_DEVICE |
| Azure Relay | Microsoft.Relay/namespaces | Применимо | cloud:azure:relay:namespaces, CUSTOM\_DEVICE |
| Служба поиска Azure | Microsoft.Search/searchServices | Применимо | cloud:azure:search:searchservices, CUSTOM\_DEVICE |
| Служебная шина Azure (встроенная) | Microsoft.ServiceBus/namespaces | Применимо | AZURE\_SERVICE\_BUS\_NAMESPACE |
| Служебная шина Azure (встроенная) | Microsoft.ServiceBus/namespaces/topics | Не применимо | AZURE\_SERVICE\_BUS\_TOPIC |
| Служебная шина Azure (встроенная) | Microsoft.ServiceBus/namespaces/queues | Не применимо | AZURE\_SERVICE\_BUS\_QUEUE |
| Приложение сетки Azure | Microsoft.ServiceFabricMesh/applications | Применимо | cloud:azure:servicefabricmesh:applications, CUSTOM\_DEVICE |
| Azure SignalR | Microsoft.SignalRService/SignalR | Применимо | cloud:azure:signalrservice:signalr, CUSTOM\_DEVICE |
| SQL Azure (встроенный) | Microsoft.Sql/servers | Применимо | AZURE\_SQL\_SERVER |
| SQL Azure (встроенный) | Microsoft.Sql/servers/databases | Применимо | AZURE\_SQL\_DATABASE |
| SQL Azure (встроенный) | Microsoft.Sql/servers/elasticPools | Применимо | AZURE\_SQL\_ELASTIC\_POOL |
| Управляемый экземпляр SQL Azure | Microsoft.Sql/managedInstances | Применимо | cloud:azure:sql:managed, CUSTOM\_DEVICE |
| SQL Server Azure | Microsoft.Sql/servers | Применимо | cloud:azure:sql:servers, CUSTOM\_DEVICE |
| Хранилище данных SQL Azure (устаревшее) | Microsoft.Sql/servers/databases | Применимо | cloud:azure:sql:servers:databases:datawarehouse, CUSTOM\_DEVICE |
| База данных SQL Azure (DTU) | Microsoft.Sql/servers/databases | Применимо | cloud:azure:sql:servers:databases:dtu, CUSTOM\_DEVICE |
| База данных SQL Azure Hyperscale | Microsoft.Sql/servers/databases | Применимо | cloud:azure:sql:servers:databases:hyperscale, CUSTOM\_DEVICE |
| База данных SQL Azure (vCore) | Microsoft.Sql/servers/databases | Применимо | cloud:azure:sql:servers:databases:vcore, CUSTOM\_DEVICE |
| Эластичный пул SQL Azure (DTU) | Microsoft.Sql/servers/elasticpools | Применимо | cloud:azure:sql:servers:elasticpools:dtu, CUSTOM\_DEVICE |
| Эластичный пул SQL Azure (vCore) | Microsoft.Sql/servers/elasticpools | Применимо | cloud:azure:sql:servers:elasticpools:vcore, CUSTOM\_DEVICE |
| Служба синхронизации хранилища Azure | Microsoft.StorageSync/storageSyncServices | Применимо | cloud:azure:storagesync:storagesyncservices, CUSTOM\_DEVICE |
| Учётная запись хранения Azure | Microsoft.Storage/storageAccounts | Применимо | cloud:azure:storage:storageaccounts, CUSTOM\_DEVICE |
| Служба BLOB-объектов хранилища Azure | Microsoft.Storage/storageAccounts | Применимо | cloud:azure:storage:storageaccounts:blob, CUSTOM\_DEVICE |
| Файловая служба хранилища Azure | Microsoft.Storage/storageAccounts | Применимо | cloud:azure:storage:storageaccounts:file, CUSTOM\_DEVICE |
| Служба очередей хранилища Azure | Microsoft.Storage/storageAccounts | Применимо | cloud:azure:storage:storageaccounts:queue, CUSTOM\_DEVICE |
| Служба таблиц хранилища Azure | Microsoft.Storage/storageAccounts | Применимо | cloud:azure:storage:storageaccounts:table, CUSTOM\_DEVICE |
| Учётные записи хранения Azure (встроенные) | Microsoft.Storage/storageAccounts | Применимо | AZURE\_STORAGE\_ACCOUNT |
| Задание Azure Stream Analytics | Microsoft.StreamAnalytics/streamingjobs | Применимо | cloud:azure:streamanalytics:streamingjobs, CUSTOM\_DEVICE |
| Рабочая область Azure Synapse | Microsoft.Synapse/workspaces | Применимо | cloud:azure:synapse:workspaces, CUSTOM\_DEVICE |
| Пул Apache Spark Azure | Microsoft.Synapse/workspaces/bigDataPools | Применимо | cloud:azure:synapse:workspaces:bigdatapools, CUSTOM\_DEVICE |
| Пул SQL Azure | Microsoft.Synapse/workspaces/sqlPools | Применимо | cloud:azure:synapse:workspaces:sqlpools, CUSTOM\_DEVICE |
| Среда Azure Time Series Insights | Microsoft.TimeSeriesInsights/environments | Применимо | cloud:azure:timeseriesinsights:environments, CUSTOM\_DEVICE |
| Источник событий Azure Time Series Insights | Microsoft.TimeSeriesInsights/environments/eventsources | Применимо | cloud:azure:timeseriesinsights:eventsources, CUSTOM\_DEVICE |
| Среда службы приложений Azure v2 | Microsoft.Web/hostingEnvironments | Применимо | cloud:azure:web:hostingenvironments:v2, CUSTOM\_DEVICE |
| План службы приложений Azure | Microsoft.Web/serverfarms | Применимо | cloud:azure:web:serverfarms, CUSTOM\_DEVICE |
| Службы приложений Azure (встроенные) | Microsoft.Web/sites | Применимо | AZURE\_WEB\_APP |
| Службы приложений Azure (встроенные) | Microsoft.Web/sites | Применимо | AZURE\_FUNCTION\_APP |
| Слот развёртывания веб-приложения Azure | Microsoft.Web/sites/slots | Применимо | cloud:azure:web:appslots, CUSTOM\_DEVICE |
| Слот развёртывания функционального приложения Azure | Microsoft.Web/sites/slots | Применимо | cloud:azure:web:functionslots, CUSTOM\_DEVICE |

## Configuration API

Для получения списка всех поддерживаемых Azure сервисов на вашем кластере для текущей версии используйте [API поддерживаемых сервисов Azure](/docs/dynatrace-api/configuration-api/azure-supported-services "Получите список поддерживаемых сервисов Azure через Dynatrace API.").

## Потребление ресурсов мониторинга

Все облачные сервисы потребляют DDU. Объём потребления DDU на экземпляр сервиса зависит от количества отслеживаемых метрик и их измерений.

* Каждое измерение метрики приводит к приёму 1 точки данных
* 1 точка данных потребляет 0,001 DDU

## Связанные темы

* [Мониторинг сервисов Azure с метриками Azure Monitor](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройте и сконфигурируйте мониторинг Azure в Dynatrace.")
