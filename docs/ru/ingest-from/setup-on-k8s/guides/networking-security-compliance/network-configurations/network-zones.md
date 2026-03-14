---
title: Использование сетевых зон в Kubernetes
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones
scraped: 2026-03-03T21:30:28.434429
---

# Использование сетевых зон в Kubernetes


* Latest Dynatrace
* Время чтения: 5 мин
* Опубликовано 25 марта 2024 г.

На этой странице описано, как эффективно использовать сетевые зоны в средах Kubernetes, с акцентом на их настройку через DynaKube.

Для обеспечения беспроблемного процесса настройки мы настоятельно рекомендуем тщательно изучить это руководство перед любыми действиями по настройке. Это позволит сетевым администраторам получить чёткое понимание предварительных требований и необходимых шагов, обеспечивая успешное развёртывание.

Мы предполагаем базовое понимание сетевых зон. Для получения справочной информации обратитесь к следующим ссылкам:

* [Введение в сетевые зоны](../../../../../manage/network-zones.md "Find out how network zones work in Dynatrace.") и [базовая информация](../../../../../manage/network-zones/network-zones-basic-info.md#activate "Learn how to get started with network zones.")
* Подключение [OneAgent](../../../../../manage/network-zones/oneagent-connectivity.md "Find out how network zones prioritize ActiveGates for OneAgent connectivity.") и [ActiveGate](../../../../../manage/network-zones/activegate-connectivity.md "Find out how network zones prioritize ActiveGates for Environment ActiveGate connectivity.")

## Сетевые зоны в средах Kubernetes

Сетевые зоны играют ключевую роль в управлении и направлении потоков трафика между компонентами Dynatrace, обеспечивая эффективную коммуникацию в сети как в средах Kubernetes, так и в традиционных конфигурациях. Используя сетевые зоны, сетевые администраторы могут оптимизировать потоки трафика и адаптироваться к средам со строгими сетевыми ограничениями, например с ограниченными возможностями исходящего трафика.

Сетевые зоны для компонентов Dynatrace, развёрнутых в Kubernetes, легко настраиваются через пользовательский ресурс DynaKube, что обеспечивает гибкое и эффективное управление сетью.

## Настройка сетевых зон

В этом разделе конфигурации разделены на два сценария в зависимости от их характеристик:

* [Кластер Kubernetes без ограничений исходящего трафика](#kubernetes-cluster-with-non-restricted-egress)
* [Кластер Kubernetes с ограниченным исходящим трафиком](#kubernetes-cluster-with-restricted-egress)

### Кластер Kubernetes без ограничений исходящего трафика

В кластерах Kubernetes без ограничений исходящего трафика основные цели сетевых зон:

* Эффективное направление трафика для предотвращения ненужной глобальной маршрутизации
* Фильтрация недоступных эндпоинтов

Поэтому использование сетевых зон широко рекомендуется для оптимального управления трафиком компонентов Dynatrace.

1. Настройте сетевую зону, задав поле `networkZone`, и убедитесь, что ActiveGate развёрнут в рамках конфигурации DynaKube. Указанная сетевая зона будет автоматически применена к развёрнутым ActiveGate и OneAgent с помощью Dynatrace Operator.

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
2. Примените CR DynaKube к API Kubernetes.

   ```
   kubectl apply -f dynakube.yaml
   ```

   После применения Dynatrace Operator развернёт компоненты Dynatrace в соответствии с конфигурацией DynaKube. В рамках развёртывания ActiveGate и OneAgent получают доступные эндпоинты в соответствии с указанной сетевой зоной (с резервным режимом *Any ActiveGate*) и могут начать взаимодействие независимо от статуса развёртывания друг друга.

   В этом сценарии не требуется вручную создавать сетевую зону перед применением пользовательского ресурса DynaKube, поскольку исходящий сетевой трафик не ограничен. Создание сетевой зоны происходит неявно, когда ActiveGate регистрирует себя в кластере Dynatrace, с настроенным [резервным режимом](../../../../../manage/network-zones/network-zones-basic-info.md#fallback-mode "Learn how to get started with network zones.") *Any ActiveGate*.

### Кластер Kubernetes с ограниченным исходящим трафиком

В кластерах Kubernetes с ограниченным исходящим трафиком обычно только компоненты из белого списка могут взаимодействовать с внешними сетями. Для Dynatrace ActiveGate разработан для этого сценария и служит ключевым шлюзовым компонентом, способным централизовать все исходящие коммуникации в направлении кластера Dynatrace.

Поскольку все компоненты Dynatrace должны взаимодействовать исключительно через ActiveGate из белого списка, необходимо, чтобы сетевая зона была настроена для поддержки этого требования. Следовательно, сетевая зона должна обеспечивать предоставление для связи только ActiveGate в рамках указанной сетевой зоны, без использования каких-либо резервных вариантов. Для этого сетевую зону необходимо создать заранее с резервным режимом *None*, чтобы предотвратить блокировку компонентов мониторинга Dynatrace.

Dynatrace Operator версии 0.14.0+ откладывает развёртывание OneAgent и внедрение до тех пор, пока хотя бы один ActiveGate не станет доступным. Как только ActiveGate становится доступным, OneAgent развёртывается и выполняется внедрение OneAgent. Поды приложений, в которые не было выполнено внедрение из-за отсрочки, необходимо перезапустить вручную.

Кроме того, может потребоваться [настроить прокси](../network-configurations.md#configure-proxy "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations.") для обеспечения контролируемого сетевого доступа в кластерах Kubernetes с ограниченным исходящим трафиком.

1. Выполните следующую команду для создания сетевой зоны в резервном режиме *None* с помощью [Dynatrace API](../../../../../dynatrace-api/environment-api/network-zones/put-network-zone.md "Update a network zone via the Dynatrace API.").

   ```
   curl -X PUT https://<environment-fqdn>/api/v2/networkZones/<network-zone-name> \


   -H "Authorization: Api-Token <api-token>" \


   -H "Content-Type: application/json" \


   -d "{ \"fallbackMode\": \"NONE\" }"
   ```

   API-токен должен иметь разрешение `networkZones.write`.
2. Настройте сетевую зону, задав поле `networkZone`, и убедитесь, что ActiveGate развёрнут в рамках конфигурации DynaKube.

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
3. Примените CR DynaKube к API Kubernetes.

   ```
   kubectl apply -f dynakube.yaml
   ```

   После развёртывания Dynatrace Operator выполняет следующие шаги.

   1. Развёртывание ActiveGate.

   2. Опрос кластера Dynatrace на наличие доступных ActiveGate через определённые интервалы до тех пор, пока ActiveGate не станет доступным.
   3. Развёртывание OneAgent с доступными эндпоинтами связи.
   4. Внедрение OneAgent в поды приложений.

   Поды приложений, в которые не было выполнено внедрение из-за отсрочки, необходимо перезапустить вручную.

   Устранение неполадок внедрения OneAgent в поды приложений

   Если поды приложений запускаются до того, как ActiveGate станет доступным, Dynatrace Operator пропускает внедрение OneAgent. Таким образом, запуск приложений не будет задержан, но приложения не будут мониториться в глубоком режиме.

   Следующие причины могут привести к пропуску внедрения OneAgent:

   * ActiveGate всё ещё запускаются и ни один из них ещё не зарегистрирован в кластере Dynatrace.
   * ActiveGate аварийно завершают работу из-за неправильной настройки.

   Dynatrace Operator добавляет следующие аннотации к каждому поду в случае пропуска внедрения OneAgent:

   ```
   oneagent.dynatrace.com/injected: "false"


   oneagent.dynatrace.com/reason: "EmptyConnectionInfo"
   ```

   В качестве альтернативы можно проанализировать журналы Dynatrace Operator на предмет пропущенных внедрений OneAgent.

## Связанные темы

* [Начало работы с сетевыми зонами](../../../../../manage/network-zones/network-zones-basic-info.md "Learn how to get started with network zones.")
* [Сетевые зоны](../../../../../manage/network-zones.md "Find out how network zones work in Dynatrace.")
