---
title: Predictive Kubernetes operations
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/use-cases/predictive-operations
scraped: 2026-03-04T21:32:29.858245
---

# Предиктивные операции Kubernetes

# Предиктивные операции Kubernetes

* Latest Dynatrace
* Руководство
* 9 мин. чтения
* Обновлено 4 февраля 2026

В современном динамичном ИТ-ландшафте эффективное управление дисковым пространством в сервисах на базе Kubernetes имеет решающее значение для поддержания оптимальной производительности и предотвращения потенциальной потери данных.

Это руководство по лучшим практикам демонстрирует, как команды могут использовать рабочие процессы Dynatrace для автоматического изменения размера дисков для проактивного управления дисковым пространством в Kubernetes-средах.

Руководство разработано для понимания как техническими, так и нетехническими специалистами, и подчёркивает ценность автоматизации управления дисковым пространством. Внедрив эту практику, команды могут значительно сократить ручное вмешательство, обеспечить бесперебойную работу своих Kubernetes-сервисов и поддерживать эффективность системы. Подход направлен на упреждающее устранение проблем с дисковым пространством до их обострения, тем самым защищая целостность данных и повышая общую производительность сервисов.

## Целевая аудитория

Этот сценарий использования предназначен для системных администраторов, инженеров DevOps и инженеров по надёжности сайтов (SRE), которые управляют сервисами и инфраструктурой на базе Kubernetes.

Вы должны иметь базовое понимание Kubernetes-сред, включая такие концепции, как узлы, поды и утилизация дисков.

Знакомство с Dynatrace, в частности с её возможностями ИИ, такими как Dynatrace Intelligence для предиктивной аналитики и автоматизированных рабочих процессов, полезно, но не обязательно. Содержание также актуально для команд, стремящихся автоматизировать и улучшить управление инфраструктурой Kubernetes, обеспечивая оптимальную производительность и утилизацию ресурсов без необходимости глубоких технических знаний Dynatrace.

Цель этого руководства — предоставить практические шаги для тех, кто отвечает за поддержание стабильности и эффективности Kubernetes-сервисов, особенно в сценариях с динамическими требованиями к ресурсам.

## Сценарий

В крупномасштабной Kubernetes-среде операционная команда отвечает за управление множеством узлов и критически важных сервисов, требующих постоянного и эффективного управления дисковым пространством. Они сталкиваются с задачей: обеспечить оптимальную утилизацию дисков для каждого сервиса без ручного вмешательства. Команде необходимо масштабируемое решение, которое может проактивно управлять дисковым пространством для предотвращения перебоев в работе сервисов и потери данных, особенно при неожиданных всплесках трафика или спроса на ресурсы.

Текущий процесс ручного мониторинга и изменения размера дисков отнимает много времени и подвержен ошибкам, что приводит либо к избыточному выделению ресурсов (расточительство), либо к недостаточному выделению (риск перебоев в работе сервиса). Команда ищет автоматизированный подход для динамической настройки дискового пространства на основе фактического использования и прогнозируемых потребностей.

Внедрив функцию автоматического изменения размера дисков в Dynatrace, команда стремится:

* Автоматически обнаруживать и устранять нехватку дискового пространства в Kubernetes-среде.
* Использовать предиктивную аналитику для расчёта необходимых изменений дискового пространства в реальном времени.
* Обеспечить согласованное применение изменений конфигурации во всех Kubernetes-кластерах.
* Сократить ручной мониторинг и вмешательство, экономя время и ресурсы.

Этот сценарий иллюстрирует типичную проблему управления сервисами на базе Kubernetes в масштабе и то, как возможности автоматизации Dynatrace могут предоставить эффективное решение. Цель — обеспечить бесперебойную работу сервисов и оптимальную производительность через интеллектуальное автоматизированное управление дисками.

Данный конкретный случай является примером того, как при внезапном всплеске трафика обеспечить немедленное выделение дополнительного дискового пространства для Kafka, чтобы удовлетворить потребности увеличенной очереди сообщений.

## Предварительные требования

Убедитесь, что все перечисленные ниже условия выполнены, прежде чем начать.

### Разрешения

* У вас есть доступ к среде Dynatrace с необходимыми разрешениями для конфигурации и мониторинга.
* У вас есть доступ к конфигурациям Kubernetes и возможность получать и изменять конфигурации сервисов Kubernetes для настройки размера дисков.

### Знания

* У вас есть базовые знания архитектуры Kubernetes, включая узлы, поды и сервисы.
* У вас есть опыт управления дисками Kubernetes: понимание утилизации дисков в Kubernetes и проблем, связанных с управлением дисковым пространством в динамических средах.
* Вы знаете, как настраивать автоматизированные рабочие процессы в Dynatrace для реагирования на оповещения о дисковом пространстве. См. [Workflows](/docs/analyze-explore-automate/workflows "Автоматизация ИТ-процессов с помощью Dynatrace Workflows — реакция на события, планирование задач и подключение сервисов.")
* Вы знаете, как настраивать мониторинг и механизмы оповещения в Dynatrace для Kubernetes-сред.
* Вы понимаете принципы GitOps, особенно для управления конфигурациями Kubernetes через подходы на основе репозиториев.

## Шаги

Чтобы поддерживать работоспособность внутренних систем, создайте автоматизированный рабочий процесс для управления дисками Kubernetes (K8s). Этот процесс настроен на обеспечение оптимальной производительности критически важных внутренних сервисов даже при неожиданных всплесках утилизации дисков. Используя непрерывный мониторинг и автоматизированные шаги по исправлению, время простоя сводится к минимуму и поддерживается согласованность операций.

### 1. Настройка непрерывного мониторинга

[Настройте Dynatrace на Kubernetes](/docs/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes") для непрерывного мониторинга всех сервисов в вашей Kubernetes-инфраструктуре. Когда мониторинг начнёт предоставлять данные, [настройте оповещение](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues "Настройка оповещений на уровне кластера, узла, пространства имён или рабочей нагрузки Kubernetes/OpenShift.") для утилизации дисков, превышающей порог в 60%, чтобы обеспечить оптимальную производительность без расточительства ресурсов. С помощью этого оповещения вы сможете смоделировать рабочий процесс для решения проблемы нехватки дискового пространства.

### 2. Настройка получения конфигурационных файлов через владение

С помощью [владения](/docs/deliver/ownership "Сопоставление владения командами с мониторируемыми объектами для улучшения совместной работы, назначения задач, реагирования на инциденты и уязвимости, а также управления уровнем сервиса."), назначенного объектам, вы можете хранить информацию о репозитории. При обнаружении аномалии система определяет затронутый сервис и получает связанный с ним конфигурационный файл. Этот шаг гарантирует, что любая адаптация соответствует конкретной конфигурации сервиса.

### 3. Настройка рабочего процесса

Используйте получение конфигурации по оповещению для запуска рабочего процесса. Рабочий процесс состоит из следующих шагов:

1. Определите хост с диском, требующим внимания.
   Используйте DQL в качестве входных данных рабочего процесса.

   ```
   fetch dt.entity.host | filter like(entity.name, "%-grail kafka") | limit 1
   ```
2. Определите диск.
   Используйте DQL в качестве входных данных рабочего процесса.

   ```
   fetch dt.entity.disk  | fieldsAdd belongs_to[dt.entity.host] | filter belongs_to[dt.entity.host] == "{{result('query_grail_kafka_hosts').records[0].id}}"
   ```
3. Используйте Dynatrace Intelligence для расчёта необходимого размера диска.

   Dynatrace Intelligence анализирует текущее использование диска в сравнении с ожидаемыми входящими данными, определяя подходящий размер диска. Этот рассчитанный ответ обеспечивает удовлетворение как текущих, так и будущих потребностей.

   Используйте действие Run Javascript рабочего процесса для извлечения прогноза с помощью Dynatrace SDK [пакет Automation utils](https://developer.dynatrace.com/reference/sdks/automation-utils/).

   Показать код

   ```
   import { execution } from '@dynatrace-sdk/automation-utils';



   export default async function () {



   const ex = await execution();



   // In this demo workflow we use a previous grail query to get a valid host ID.



   // Usually this would come from a Davis event



   const res = await ex.result("analyze_with_davis_1");



   let prediction = 0.0;



   let validPrediction = true;



   try {



   const points = res.result.output[0].timeSeriesDataWithPredictions.records[0]["dt.davis.forecast:point"];



   console.log("Got these prediction: %s", points);



   const floatPoints = points.map(p => Number(p));



   prediction = Math.max(...floatPoints);



   console.log("Max value is: %s", prediction);



   } catch (e) {



   console.error("Unable to predict: %s", e instanceof Error ? e.message : JSON.stringify(e));



   validPrediction = false;



   }



   return {



   prediction,



   validPrediction,



   };



   }
   ```
4. Определите владение.
   Знание владения позволит вам выбрать правильный репозиторий для применения новой конфигурации размера диска.

   * Используйте действие Ownership для определения владельцев объекта диска, который вы определили ранее.
   * С информацией о владении на следующем шаге вы сможете определить правильный репозиторий для применения изменения:

     Показать код

     ```
     import {



     monitoredEntitiesClient



     } from "@dynatrace-sdk/client-classic-environment-v2";



     import {



     execution



     } from '@dynatrace-sdk/automation-utils';



     async function getEntityName(entityId) {



     const data = await monitoredEntitiesClient.getEntity({



     entityId: entityId,



     });



     return data.displayName;



     }



     function isKafkaEntity(entityName) {



     return entityName.match(/([a-z0-9-]+)-grail kafka/) !== null;



     }



     async function getKafkaConfigURL(ex, entityName) {



     const owners = (await ex.result("get\_owners")).owners;



     let repoLink = undefined;



     // Go though all the owners and figure out which one as a REPOSITORY link type set.



     // We assume that is the correct one and will just use it later for building the URL



     for (const owner of owners) {



     for (const link of owner.links) {



     if (link.linkType === "REPOSITORY") {



     repoLink = link.url;



     break;



     }



     }



     if (repoLink !== undefined) {



     break;



     }



     }



     // "Gracefully" fail and tell the user that no owner had the required link type set;



     // Helps with debugging since otherwise we would build a URL undefined/... which can



     // cause more problems down the line.



     if (repoLink === undefined) {



     throw new Error('No REPOSITORY link was provided for any tagged owner!')



     }



     const baseUrl = repoLink;



     const file = "app//kafka-worker/kafka-configuration/values-scoped.yaml";



     const cluster = entityName.match(/([a-z0-9-]+)-grail kafka/)[1];



     return `${baseUrl}/${cluster}/${file}`;



     }



     export default async function() {



     const ex = await execution();



     // In this demo workflow we use a previous grail query to get a valid host ID.



     // Usually this would come from a Davis event



     const queryResults = await ex.result("query\_grail\_kafka\_hosts");



     const records = queryResults.records;



     // Only have a look at the first element because an event likely only



     // contains one element:



     const {



     id



     } = records[0];



     // Use the following DQL to query host IDs for grail kafka entities



     // >>> fetch dt.entity.host | filter like(entity.name, "%-grail kafka")



     const name = await getEntityName(id);



     // name should be used here, but only if isKafkaEntity is true!



     return {



     isKafkaHost: isKafkaEntity(name),



     url: await getKafkaConfigURL(ex, name)



     };
     ```
5. Зафиксируйте изменения и создайте запрос на слияние.

   Используйте действие Kubernetes рабочего процесса для применения новой конфигурации. После определения желаемого размера диска рабочий процесс автоматически создаёт запрос на слияние (pull request). Этот запрос адаптирует конфигурационный файл сервиса для отражения нового определённого размера диска.

   Показать код

   ```
   apiVersion: batch/v1



   kind: Job



   metadata:



   name: {{ "demo-job-resize-%s" % result('disk_from_host').records[0].id | lower }}



   labels:



   joblabel: "test"



   spec:



   ttlSecondsAfterFinished: 300



   backoffLimit: 0



   activeDeadlineSeconds: 60



   podFailurePolicy:



   rules:



   - action: FailJob



   onExitCodes:



   operator: NotIn



   values: [0]



   template:



   spec:



   restartPolicy: Never



   containers:



   - name: main



   image: docker.io/library/bash:5



   command: ["bash"]



   args:



   - -c



   - echo "Computing..."; sleep 10; echo $PATH_URL; echo $IS_KAFKA_HOST; echo $PREDICTION; echo $VALID_PREDICTION; test $VALID_PREDICTION = 'True'; exit $?



   resources:



   limits:



   memory: 10Mi



   cpu: 1m



   env:



   - name: PATH_URL



   value: "{{result('repository_url').url}}"



   - name: IS_KAFKA_HOST



   value: "{{result('repository_url').isKafkaHost}}"



   - name: PREDICTION



   value: "{{result('extract_prediction').prediction}}"



   - name: VALID_PREDICTION



   value: "{{result('extract_prediction').validPrediction}}"
   ```
6. Развёртывание.
   Изменённые конфигурации развёртываются в сервисе через ArgoCD и ArgoWorkflows. Быстрое развёртывание минимизирует перебои в работе сервиса и гарантирует немедленное вступление изменений в силу.
7. Валидация после развёртывания.
   После развёртывания конфигурации происходит фаза валидации, в ходе которой система проверяет, было ли изменение размера диска успешным и была ли устранена исходная аномалия.

Если в ходе рабочего процесса возникнет какая-либо проблема, система оповещения Dynatrace обеспечивает немедленное внимание к потенциальным осложнениям. Рабочий процесс также включает функцию Ownership, которая определяет ответственную сторону для данной проблемы, обеспечивая эффективную коммуникацию, например, с помощью действия Slack в рабочем процессе.

## Заключение

Внедрив автоматическое изменение размера дисков в Kubernetes-средах с помощью Dynatrace, команды могут эффективно управлять дисковым пространством, обеспечивая бесперебойную и эффективную работу своих сервисов. Это руководство предоставило комплексный подход к настройке непрерывного мониторинга, автоматизации обновления конфигураций и обеспечению эффективного развёртывания и валидации. Интеграция возможностей ИИ Dynatrace позволяет выполнять предиктивные корректировки, сокращая ручные усилия и повышая надёжность системы.

После выполнения этих шагов команды могут больше сосредоточиться на стратегических задачах, а не на постоянном мониторинге и ручных вмешательствах. Возможность проактивного управления ресурсами в Kubernetes-среде является важным шагом к оптимизации производительности инфраструктуры и минимизации потенциальных перебоев или потери данных.

Для полного использования этих преимуществ рекомендуем попробовать внедрить эти практики в ваших Kubernetes-средах. Экспериментируйте с настройками, отслеживайте результаты и корректируйте по мере необходимости в соответствии с вашими конкретными потребностями.

Узнайте больше о том, как Dynatrace может трансформировать ваш подход к управлению Kubernetes, привнося эффективность и предсказуемость в ваши операционные рабочие процессы.

## Связанные темы

* [ИИ в Workflows — Предиктивное обслуживание облачных дисков](/docs/dynatrace-intelligence/use-cases/davis-for-workflows "Автоматизация предиктивного обслуживания облачных ресурсов с помощью Dynatrace Intelligence в AutomationEngine.")
* [Примеры DQL для Dynatrace Intelligence](/docs/dynatrace-intelligence/use-cases/davis-dql-examples "Создание мощных дашбордов здоровья путём разделения и анализа проблем и событий, обнаруженных Dynatrace Intelligence, с помощью DQL.")
