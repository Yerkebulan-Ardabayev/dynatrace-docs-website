---
title: Мониторинг Google Vertex AI
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-vertex-ai
scraped: 2026-05-12T11:51:15.199172
---

# Мониторинг Google Vertex AI

# Мониторинг Google Vertex AI

* Практическое руководство
* Чтение: 6 мин
* Опубликовано 30 сентября 2024 г.

Интеграция Dynatrace с Google Cloud использует данные, собранные через Google Operation API, для постоянного мониторинга работоспособности и производительности сервисов Google Cloud. Объединяя все релевантные данные в дашбордах, она также обеспечивает оповещения и отслеживание событий.

## Предварительные условия

[Настройка интеграции](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.")

## Добавление сервисов и наборов функций Необязательно

После интеграции Dynatrace автоматически отслеживает ряд предустановленных сервисов и наборов функций (метрик) Google Cloud. Помимо них, в мониторинг можно добавить дополнительные сервисы или наборы функций. Подробнее см. [Добавление или удаление сервисов](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Настройка мониторинга логов и метрик для сервисов GCP в новом кластере GKE Autopilot.").

Список наборов функций, доступных для этого сервиса, см. в разделе [Таблица метрик](#table).

## Просмотр метрик

После развёртывания интеграции метрики отслеживаемых сервисов можно просматривать в [Браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики с помощью браузера метрик Dynatrace."), [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и на плитках ваших дашбордов.

## Таблица метрик

Для Google Cloud Vertex AI доступны следующие наборы функций.

| Набор функций | Имя | Единица измерения | Идентификатор метрики GCP |
| --- | --- | --- | --- |
| vertexai\_deployment\_resource\_pool/default\_metrics | Accelerator duty cycle | Процент | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/accelerator/duty\_cycle |
| vertexai\_deployment\_resource\_pool/default\_metrics | Accelerator memory usage | Байт | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/accelerator/memory/bytes\_used |
| vertexai\_deployment\_resource\_pool/default\_metrics | CPU utilization | Процент | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/cpu/utilization |
| vertexai\_deployment\_resource\_pool/default\_metrics | Memory usage | Байт | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/memory/bytes\_used |
| vertexai\_deployment\_resource\_pool/default\_metrics | Network bytes received | Байт | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/network/received\_bytes\_count |
| vertexai\_deployment\_resource\_pool/default\_metrics | Network bytes sent | Байт | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/network/sent\_bytes\_count |
| vertexai\_deployment\_resource\_pool/default\_metrics | Replica count | Количество | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/replicas |
| vertexai\_deployment\_resource\_pool/default\_metrics | Replica target | Количество | aiplatform\_googleapis\_com/prediction/online/deployment\_resource\_pool/target\_replicas |
| vertexai\_endpoint/default\_metrics | Accelerator duty cycle | Процент | aiplatform\_googleapis\_com/prediction/online/accelerator/duty\_cycle |
| vertexai\_endpoint/default\_metrics | Accelerator memory usage | Байт | aiplatform\_googleapis\_com/prediction/online/accelerator/memory/bytes\_used |
| vertexai\_endpoint/default\_metrics | CPU utilization | Процент | aiplatform\_googleapis\_com/prediction/online/cpu/utilization |
| vertexai\_endpoint/default\_metrics | Number of online prediction errors | Количество | aiplatform\_googleapis\_com/prediction/online/error\_count |
| vertexai\_endpoint/default\_metrics | Memory usage | Байт | aiplatform\_googleapis\_com/prediction/online/memory/bytes\_used |
| vertexai\_endpoint/default\_metrics | Network bytes received | Байт | aiplatform\_googleapis\_com/prediction/online/network/received\_bytes\_count |
| vertexai\_endpoint/default\_metrics | Network bytes sent | Байт | aiplatform\_googleapis\_com/prediction/online/network/sent\_bytes\_count |
| vertexai\_endpoint/default\_metrics | Number of online predictions | Количество | aiplatform\_googleapis\_com/prediction/online/prediction\_count |
| vertexai\_endpoint/default\_metrics | Prediction latencies | Миллисекунда | aiplatform\_googleapis\_com/prediction/online/prediction\_latencies |
| vertexai\_endpoint/default\_metrics | Private endpoint prediction latencies | Миллисекунда | aiplatform\_googleapis\_com/prediction/online/private/prediction\_latencies |
| vertexai\_endpoint/default\_metrics | Private endpoint response count | Количество | aiplatform\_googleapis\_com/prediction/online/private/response\_count |
| vertexai\_endpoint/default\_metrics | Replica count | Количество | aiplatform\_googleapis\_com/prediction/online/replicas |
| vertexai\_endpoint/default\_metrics | Response count | Количество | aiplatform\_googleapis\_com/prediction/online/response\_count |
| vertexai\_endpoint/default\_metrics | Replica target | Количество | aiplatform\_googleapis\_com/prediction/online/target\_replicas |
| vertexai\_feature\_online\_store/feature\_store | Request count | Количество | aiplatform\_googleapis\_com/featureonlinestore/online\_serving/request\_count |
| vertexai\_feature\_online\_store/feature\_store | Response bytes count | Количество | aiplatform\_googleapis\_com/featureonlinestore/online\_serving/serving\_bytes\_count |
| vertexai\_feature\_online\_store/feature\_store | Request latency | Миллисекунда | aiplatform\_googleapis\_com/featureonlinestore/online\_serving/serving\_latencies |
| vertexai\_feature\_online\_store/feature\_store | Running sycs | Количество | aiplatform\_googleapis\_com/featureonlinestore/running\_sync |
| vertexai\_feature\_online\_store/feature\_store | Serving data ages | Секунда | aiplatform\_googleapis\_com/featureonlinestore/serving\_data\_ages |
| vertexai\_feature\_online\_store/feature\_store | Serving data by synced time | Количество | aiplatform\_googleapis\_com/featureonlinestore/serving\_data\_by\_sync\_time |
| vertexai\_feature\_online\_store/feature\_store | CPU load | Процент | aiplatform\_googleapis\_com/featureonlinestore/storage/bigtable\_cpu\_load |
| vertexai\_feature\_online\_store/feature\_store | CPU load (hottest node) | Процент | aiplatform\_googleapis\_com/featureonlinestore/storage/bigtable\_cpu\_load\_hottest\_node |
| vertexai\_feature\_online\_store/feature\_store | Node count | Количество | aiplatform\_googleapis\_com/featureonlinestore/storage/bigtable\_nodes |
| vertexai\_feature\_online\_store/feature\_store | Optimized node count | Количество | aiplatform\_googleapis\_com/featureonlinestore/storage/optimized\_nodes |
| vertexai\_feature\_online\_store/feature\_store | Bytes stored | Байт | aiplatform\_googleapis\_com/featureonlinestore/storage/stored\_bytes |
| vertexai\_feature\_store/feature\_store | CPU load | Процент | aiplatform\_googleapis\_com/featurestore/cpu\_load |
| vertexai\_feature\_store/feature\_store | CPU load (hottest node) | Процент | aiplatform\_googleapis\_com/featurestore/cpu\_load\_hottest\_node |
| vertexai\_feature\_store/feature\_store | Node count | Количество | aiplatform\_googleapis\_com/featurestore/node\_count |
| vertexai\_feature\_store/feature\_store | Entities updated on the Featurestore online storage | Байт | aiplatform\_googleapis\_com/featurestore/online\_entities\_updated |
| vertexai\_feature\_store/feature\_store | Latencies | Миллисекунда | aiplatform\_googleapis\_com/featurestore/online\_serving/latencies |
| vertexai\_feature\_store/feature\_store | Request size | Байт | aiplatform\_googleapis\_com/featurestore/online\_serving/request\_bytes\_count |
| vertexai\_feature\_store/feature\_store | Serving count | Количество | aiplatform\_googleapis\_com/featurestore/online\_serving/request\_count |
| vertexai\_feature\_store/feature\_store | Response size | Байт | aiplatform\_googleapis\_com/featurestore/online\_serving/response\_size |
| vertexai\_feature\_store/feature\_store | Billable bytes | Байт | aiplatform\_googleapis\_com/featurestore/storage/billable\_processed\_bytes |
| vertexai\_feature\_store/feature\_store | Bytes stored | Байт | aiplatform\_googleapis\_com/featurestore/storage/stored\_bytes |
| vertexai\_feature\_store/feature\_store | Offline storage write for streaming write | Количество | aiplatform\_googleapis\_com/featurestore/streaming\_write/offline\_processed\_count |
| vertexai\_feature\_store/feature\_store | Streaming write to offline storage delay time | Секунда | aiplatform\_googleapis\_com/featurestore/streaming\_write/offline\_write\_delays |
| vertexai\_location/default\_metrics | Executing PipelineJobs | Количество | aiplatform\_googleapis\_com/executing\_vertexai\_pipeline\_jobs |
| vertexai\_location/default\_metrics | Executing PipelineTasks | Количество | aiplatform\_googleapis\_com/executing\_vertexai\_pipeline\_tasks |
| vertexai\_location/default\_metrics | Generate content requests per minute per project per base model | Количество | aiplatform\_googleapis\_com/generate\_content\_requests\_per\_minute\_per\_project\_per\_base\_model |
| vertexai\_location/default\_metrics | Online prediction dedicated requests per base model version | Количество | aiplatform\_googleapis\_com/online\_prediction\_dedicated\_requests\_per\_base\_model\_version |
| vertexai\_location/default\_metrics | Online prediction dedicated tokens per minute per base model version | Количество | aiplatform\_googleapis\_com/online\_prediction\_dedicated\_tokens\_per\_base\_model\_version |
| vertexai\_location/default\_metrics | Online prediction requests per base model | Количество | aiplatform\_googleapis\_com/online\_prediction\_requests\_per\_base\_model |
| vertexai\_location/default\_metrics | Online prediction tokens per minute per base model | Количество | aiplatform\_googleapis\_com/online\_prediction\_tokens\_per\_minute\_per\_base\_model |
| vertexai\_location/default\_metrics | Generate content requests per minute per project per base model quota exceeded error | Количество | aiplatform\_googleapis\_com/quota/generate\_content\_requests\_per\_minute\_per\_project\_per\_base\_model/exceeded |
| vertexai\_location/default\_metrics | Generate content requests per minute per project per base model quota limit | Количество | aiplatform\_googleapis\_com/quota/generate\_content\_requests\_per\_minute\_per\_project\_per\_base\_model/limit |
| vertexai\_location/default\_metrics | Generate content requests per minute per project per base model quota usage | Количество | aiplatform\_googleapis\_com/quota/generate\_content\_requests\_per\_minute\_per\_project\_per\_base\_model/usage |
| vertexai\_location/default\_metrics | Online prediction dedicated requests per base model version quota exceeded error | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_requests\_per\_base\_model\_version/exceeded |
| vertexai\_location/default\_metrics | Online prediction dedicated requests per base model version quota limit | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_requests\_per\_base\_model\_version/limit |
| vertexai\_location/default\_metrics | Online prediction dedicated requests per base model version quota usage | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_requests\_per\_base\_model\_version/usage |
| vertexai\_location/default\_metrics | Online prediction dedicated tokens per minute per base model version quota exceeded error | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_tokens\_per\_base\_model\_version/exceeded |
| vertexai\_location/default\_metrics | Online prediction dedicated tokens per minute per base model version quota limit | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_tokens\_per\_base\_model\_version/limit |
| vertexai\_location/default\_metrics | Online prediction dedicated tokens per minute per base model version quota usage | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_dedicated\_tokens\_per\_base\_model\_version/usage |
| vertexai\_location/default\_metrics | Online prediction requests per base model quota exceeded | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_requests\_per\_base\_model/exceeded |
| vertexai\_location/default\_metrics | Online prediction requests per base model quota limit | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_requests\_per\_base\_model/limit |
| vertexai\_location/default\_metrics | Online prediction requests per base model quota usage | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_requests\_per\_base\_model/usage |
| vertexai\_location/default\_metrics | Online prediction tokens per minute per base model quota exceeded | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_tokens\_per\_minute\_per\_base\_model/exceeded |
| vertexai\_location/default\_metrics | Online prediction tokens per minute per base model quota limit | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_tokens\_per\_minute\_per\_base\_model/limit |
| vertexai\_location/default\_metrics | Online prediction tokens per minute per base model quota usage | Количество | aiplatform\_googleapis\_com/quota/online\_prediction\_tokens\_per\_minute\_per\_base\_model/usage |
| vertexai\_pipeline\_job/pipelines | PipelineJob duration | Секунда | aiplatform\_googleapis\_com/pipelinejob/duration |
| vertexai\_pipeline\_job/pipelines | Completed PipelineTasks | Количество | aiplatform\_googleapis\_com/pipelinejob/task\_completed\_count |
| vertexai\_index/vector\_search | Datapoint count | Количество | aiplatform\_googleapis\_com/matching\_engine/stream\_update/datapoint\_count |
| vertexai\_index/vector\_search | Stream update latencies | Миллисекунда | aiplatform\_googleapis\_com/matching\_engine/stream\_update/latencies |
| vertexai\_index/vector\_search | Request count | Количество | aiplatform\_googleapis\_com/matching\_engine/stream\_update/request\_count |
| vertexai\_index\_endpoint/vector\_search | CPU request utilization | Процент | aiplatform\_googleapis\_com/matching\_engine/cpu/request\_utilization |
| vertexai\_index\_endpoint/vector\_search | Current replicas | Количество | aiplatform\_googleapis\_com/matching\_engine/current\_replicas |
| vertexai\_index\_endpoint/vector\_search | Current shards | Количество | aiplatform\_googleapis\_com/matching\_engine/current\_shards |
| vertexai\_index\_endpoint/vector\_search | Memory usage | Байт | aiplatform\_googleapis\_com/matching\_engine/memory/used\_bytes |
| vertexai\_index\_endpoint/vector\_search | Request latency | Миллисекунда | aiplatform\_googleapis\_com/matching\_engine/query/latencies |
| vertexai\_index\_endpoint/vector\_search | Request count | Количество | aiplatform\_googleapis\_com/matching\_engine/query/request\_count |
| vertexai\_publisher\_model/default\_metrics | Character count | Количество | aiplatform\_googleapis\_com/publisher/online\_serving/character\_count |
| vertexai\_publisher\_model/default\_metrics | Characters | Количество | aiplatform\_googleapis\_com/publisher/online\_serving/characters |
| vertexai\_publisher\_model/default\_metrics | Character Throughput | Количество | aiplatform\_googleapis\_com/publisher/online\_serving/consumed\_throughput/count |
| vertexai\_publisher\_model/default\_metrics | First token latencies | Миллисекунда | aiplatform\_googleapis\_com/publisher/online\_serving/first\_token\_latencies |
| vertexai\_publisher\_model/default\_metrics | Model invocation count | Количество | aiplatform\_googleapis\_com/publisher/online\_serving/model\_invocation\_count |
| vertexai\_publisher\_model/default\_metrics | Model invocation latencies | Миллисекунда | aiplatform\_googleapis\_com/publisher/online\_serving/model\_invocation\_latencies |
| vertexai\_publisher\_model/default\_metrics | Token count | Количество | aiplatform\_googleapis\_com/publisher/online\_serving/token\_count |
| vertexai\_publisher\_model/default\_metrics | Tokens | Количество | aiplatform\_googleapis\_com/publisher/online\_serving/tokens |
| visionai\_instance/vision\_ai | Request count | Количество | visionai\_googleapis\_com/platform/connected\_service/request\_count |
| visionai\_instance/vision\_ai | Request latencies | Миллисекунда | visionai\_googleapis\_com/platform/connected\_service/request\_latencies |
| visionai\_instance/vision\_ai | Prediction count | Количество | visionai\_googleapis\_com/platform/custom\_model/predict\_count |
| visionai\_instance/vision\_ai | Prediction latencies | Миллисекунда | visionai\_googleapis\_com/platform/custom\_model/predict\_latencies |
| visionai\_instance/vision\_ai | Uptime | Миллисекунда | visionai\_googleapis\_com/platform/instance/uptime |
| visionai\_stream/vision\_ai | Received bytes | Байт | visionai\_googleapis\_com/stream/network/received\_bytes\_count |
| visionai\_stream/vision\_ai | Received packets | Количество | visionai\_googleapis\_com/stream/network/received\_packets\_count |
| visionai\_stream/vision\_ai | Sent bytes | Байт | visionai\_googleapis\_com/stream/network/sent\_bytes\_count |
| visionai\_stream/vision\_ai | Sent packets | Количество | visionai\_googleapis\_com/stream/network/sent\_packets\_count |

## Связанные темы

* [Интеграции Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Настройка и конфигурирование Dynatrace в Google Cloud.")