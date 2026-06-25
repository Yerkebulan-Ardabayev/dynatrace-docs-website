---
title: Использование network zones в Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones
scraped: 2026-05-12T12:08:43.325147
---

# Использование network zones в Kubernetes

# Использование network zones в Kubernetes

* Чтение: 5 мин
* Опубликовано 25 марта 2024 г.

На этой странице описано, как эффективно использовать network zones в окружениях Kubernetes, с акцентом на их настройку через DynaKube.

Чтобы обеспечить бесперебойный процесс настройки, настоятельно рекомендуем внимательно изучить это руководство, прежде чем приступать к настройке. Это позволит сетевым администраторам получить чёткое понимание предварительных требований и необходимых шагов, обеспечивая успешное развёртывание.

Предполагается, что вы обладаете базовым пониманием network zones. Справочную информацию см. по следующим ссылкам:

* [Введение в network zones](/managed/manage/network-zones "Узнайте, как network zones работают в Dynatrace.") и [базовая информация](/managed/manage/network-zones/network-zones-basic-info#activate "Узнайте, как начать работу с network zones.")
* Подключение [OneAgent](/managed/manage/network-zones/oneagent-connectivity "Узнайте, как network zones приоритизируют ActiveGate для подключения OneAgent.") и [ActiveGate](/managed/manage/network-zones/activegate-connectivity "Узнайте, как network zones приоритизируют ActiveGate для подключения Environment ActiveGate.")

## Network zones в окружениях Kubernetes

Network zones играют важную роль в управлении и направлении потоков трафика между компонентами Dynatrace, обеспечивая эффективную связь внутри сети, будь то в окружениях Kubernetes или в традиционных развёртываниях. Используя network zones, сетевые администраторы могут оптимизировать поток трафика и поддерживать окружения со строгими сетевыми ограничениями, например с ограниченными возможностями исходящего трафика.

Network zones для компонентов Dynatrace, развёрнутых в Kubernetes, легко настраиваются через пользовательский ресурс DynaKube, что обеспечивает адаптированное и эффективное управление сетью.

## Настройка network zones

В этом разделе варианты настройки разделены на два отдельных сценария в зависимости от их характеристик:

* [Кластер Kubernetes с неограниченным исходящим трафиком](#kubernetes-cluster-with-non-restricted-egress)
* [Кластер Kubernetes с ограниченным исходящим трафиком](#kubernetes-cluster-with-restricted-egress)

### Кластер Kubernetes с неограниченным исходящим трафиком

В кластерах Kubernetes без ограничений исходящего трафика основные цели network zones следующие:

* Эффективно направлять трафик, чтобы предотвратить излишнюю глобальную маршрутизацию
* Фильтровать недоступные конечные точки

Поэтому использование network zones широко рекомендуется для оптимального управления трафиком компонентов Dynatrace.

1. Настройте network zone, задав поле `networkZone`, и убедитесь, что ActiveGate развёрнут в рамках конфигурации DynaKube. Указанная network zone будет автоматически применена к развёрнутым ActiveGate и OneAgent оператором Dynatrace Operator.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   ...



   spec:



   ...



   networkZone: my-networkzone # Configures network zone



   oneAgent:



   ...



   activeGate: # Ensures ActiveGate rollout



   capabilities:



   - routing



   - kubernetes-monitoring



   ...
   ```
2. Примените DynaKube CR к Kubernetes API.

   ```
   kubectl apply -f dynakube.yaml
   ```

   После применения Dynatrace Operator развернёт компоненты Dynatrace в соответствии с конфигурацией DynaKube. В рамках развёртывания ActiveGate и OneAgent получают доступные конечные точки в соответствии с указанной network zone (с режимом резервирования *Any ActiveGate*) и могут начинать обмен данными независимо от статуса развёртывания друг друга.

   В этом сценарии не требуется вручную создавать network zone перед применением пользовательского ресурса DynaKube, поскольку исходящий трафик не ограничен. Создание network zone происходит неявно, когда ActiveGate регистрируется в кластере Dynatrace, при этом в качестве [режима резервирования](/managed/manage/network-zones/network-zones-basic-info#fallback-mode "Узнайте, как начать работу с network zones.") настроен *Any ActiveGate*.

### Кластер Kubernetes с ограниченным исходящим трафиком

В кластерах Kubernetes с принудительным ограничением исходящего трафика, как правило, только компоненты из списка разрешённых могут взаимодействовать с внешними сетями. В Dynatrace для этого сценария предназначен ActiveGate, который выступает в роли этого ключевого шлюзового компонента, способного централизовать все исходящие соединения к Dynatrace Cluster.

Поскольку все компоненты Dynatrace должны взаимодействовать исключительно через ActiveGate из списка разрешённых, крайне важно, чтобы network zone была настроена с учётом этого требования. Поэтому network zone должна гарантировать, что для связи предоставляются только ActiveGate в пределах указанной network zone, без обращения к каким-либо вариантам резервирования. Для этого network zone необходимо создать заранее с режимом резервирования *None*, чтобы предотвратить блокировку компонентов мониторинга Dynatrace.

Dynatrace Operator версии 0.14.0+ откладывает развёртывание и внедрение OneAgent до тех пор, пока не станет доступен хотя бы один ActiveGate. Как только ActiveGate становится доступен, OneAgent развёртываются и выполняется внедрение OneAgent. Поды приложений, в которые внедрение не было выполнено из-за отсрочки, необходимо перезапустить вручную.

Кроме того, может потребоваться также [настроить proxy](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#configure-proxy "Настройка Dynatrace в окружениях с сетевыми ограничениями, связанных с сетью параметров и конфигураций proxy.") для обеспечения контролируемого сетевого доступа в кластерах Kubernetes с ограниченным исходящим трафиком.

1. Выполните следующую команду, чтобы создать network zone с режимом резервирования *None* с помощью [Dynatrace API](/managed/dynatrace-api/environment-api/network-zones/put-network-zone "Обновление network zone через Dynatrace API.").

   ```
   curl -X PUT https://<environment-fqdn>/api/v2/networkZones/<network-zone-name> \



   -H "Authorization: Api-Token <api-token>" \



   -H "Content-Type: application/json" \



   -d "{ \"fallbackMode\": \"NONE\" }"
   ```

   API-токену должно быть назначено разрешение `networkZones.write`.
2. Настройте network zone, задав поле `networkZone`, и убедитесь, что ActiveGate развёрнут в рамках конфигурации DynaKube.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   ...



   spec:



   ...



   networkZone: my-networkzone # Configures network zone



   oneAgent:



   ...



   activeGate: # Ensures ActiveGate rollout



   capabilities:



   - routing



   - kubernetes-monitoring



   ...
   ```
3. Примените DynaKube CR к Kubernetes API.

   ```
   kubectl apply -f dynakube.yaml
   ```

   После развёртывания Dynatrace Operator выполняет следующие шаги.

   1. Развёртывает ActiveGate.

   2. Опрашивает кластер Dynatrace на наличие доступных ActiveGate через определённый интервал, пока ActiveGate не станет доступен.
   3. Развёртывает OneAgent с доступными конечными точками связи.
   4. Выполняет внедрение OneAgent в поды приложений.

   Поды приложений, в которые внедрение не было выполнено из-за отсрочки, необходимо перезапустить вручную.

   Устранение неполадок внедрения OneAgent в поды приложений

   Если поды приложений запускаются до того, как ActiveGate становится доступен, Dynatrace Operator пропускает внедрение OneAgent. Таким образом запуск приложений не задерживается, но приложения не будут глубоко мониториться.

   К пропуску внедрения OneAgent могут приводить следующие причины:

   * ActiveGate всё ещё запускаются, и ни один из них пока не зарегистрирован в кластере Dynatrace.
   * ActiveGate аварийно завершают работу из-за неправильной настройки.

   В случае пропуска внедрения OneAgent Dynatrace Operator добавляет следующие аннотации к каждому поду:

   ```
   oneagent.dynatrace.com/injected: "false"



   oneagent.dynatrace.com/reason: "EmptyConnectionInfo"
   ```

   Кроме того, для выявления пропущенных внедрений OneAgent можно проанализировать логи Dynatrace Operator.

## Связанные темы

* [Начало работы с network zones](/managed/manage/network-zones/network-zones-basic-info "Узнайте, как начать работу с network zones.")
* [Network zones](/managed/manage/network-zones "Узнайте, как network zones работают в Dynatrace.")