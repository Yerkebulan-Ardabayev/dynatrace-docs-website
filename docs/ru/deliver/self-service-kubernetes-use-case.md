---
title: Прогнозирование и автомасштабирование рабочих нагрузок Kubernetes
source: https://www.dynatrace.com/docs/deliver/self-service-kubernetes-use-case
scraped: 2026-03-06T21:35:42.123501
---

Испытываете трудности с поддержанием динамических сред Kubernetes? Ручное масштабирование не только трудоёмко и реактивно, но и подвержено ошибкам.

Вы можете использовать возможности Dynatrace Automation и Dynatrace Intelligence для прогнозирования узких мест в ресурсах и автоматического создания запросов на слияние (pull request) для масштабирования приложений. Этот проактивный подход минимизирует простои, помогает оптимизировать использование ресурсов и обеспечивает наилучшую производительность ваших приложений.

Это достигается путём сочетания предсказательного ИИ для прогнозирования ограничений ресурсов с генеративным ИИ для предложений по изменению манифестов Kubernetes в Git (GitHub и GitLab) путём создания pull request для корректировки масштабирования.

Следующая анимация демонстрирует сквозной рабочий процесс. Как инженер, вы можете включить для развёртывания рекомендации по предиктивному масштабированию через аннотации. Workflows будут прогнозировать потребление ресурсов для включённых развёртываний и создавать pull request для помощи инженеру в выполнении необходимых корректировок. Использование комбинации Dynatrace Intelligence и Workflows — это настоящее ИИ-ассистируемое предиктивное масштабирование, которое хорошо интегрируется в рабочий процесс Git.

![Включение развёртывания для рекомендаций предиктивного масштабирования через аннотации.](https://dt-cdn.net/images/k8sscaling-obslab-overview-animated-7ef05a83f5.gif)

## Чему вы научитесь

Цель данного руководства — научить вас аннотировать развёртывания и создавать два взаимосвязанных workflow, которые будут выявлять рабочие нагрузки Kubernetes, требующие масштабирования. Также будут создаваться pull request с предлагаемыми новыми лимитами в режиме самообслуживания для инженерных команд.

В этом руководстве вы узнаете, как

* Аннотировать развёртывания Kubernetes
* Создать два Dynatrace workflow: один для прогнозирования, другой для открытия pull request

В качестве альтернативы следуйте нашей [Лаборатории наблюдаемости: Предиктивное автомасштабирование рабочих нагрузок Kubernetes](https://dt-url.net/obslab-predictive-kubernetes-scaling). В этой лаборатории используется конфигурация GitHub Codespaces, позволяющая полностью автоматизировать данный сценарий.

## Прежде чем начать

### Предварительные требования

* Установлено [ИИ в Workflows — Предиктивное обслуживание облачных дисков](../dynatrace-intelligence/use-cases/davis-for-workflows.md "Автоматизация предиктивного обслуживания облачных ресурсов с помощью Dynatrace Intelligence в AutomationEngine.").
* [Настроен Kubernetes Connector](../analyze-explore-automate/workflows/actions/kubernetes-automation/kubernetes-workflows-setup.md "Узнайте, как настроить Kubernetes Connector").
* Доступ к вашей учётной записи GitHub, репозиторию GitHub и персональному токену доступа GitHub (PAT).
* Доступ к вашей среде Kubernetes, которая мониторируется с помощью Dynatrace.
* Развёртывание Kubernetes, которое можно аннотировать для включения pull request предиктивного масштабирования.
* Токен API платформы Dynatrace для выполнения Dynatrace Intelligence.
* [Настроен GitHub Connector](../analyze-explore-automate/workflows/actions/github/github-workflows-setup.md "Узнайте, как настроить GitHub Connector.")

### Аннотирование развёртываний Kubernetes

Workflow, предоставляющие предложения по предиктивному масштабированию, будут работать только с развёртываниями Kubernetes, аннотированными метаданными, специфичными для данного сценария использования. Вам необходимо добавить следующие аннотации в ваше развёртывание.

Полный пример см. в примерах развёртывания [горизонтального масштабирования](https://dt-url.net/d723u3m) и [вертикального масштабирования](https://dt-url.net/vf43uri) из [руководства на GitHub Observability Lab](https://dt-url.net/ms63uam).

## Шаги

Вам предстоит создать два workflow.

* Первый workflow использует Dynatrace Intelligence для прогнозирования того, каким рабочим нагрузкам Kubernetes требуется масштабирование, исходя из прогнозируемого использования памяти и CPU.
* Второй workflow использует генеративный ИИ Dynatrace Intelligence для создания pull request с использованием прогнозируемых значений, предложенных генеративным ИИ Dynatrace Intelligence, для обновления файлов манифестов.

Хотя мы используем возможности Dynatrace Intelligence для прогнозирования и обновления манифестов, именно вы, как пользователь, принимаете решение о принятии предложенных изменений в рамках pull request.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Прогнозирование использования ресурсов Kubernetes**](#predict-resource-usage)[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Фиксация workflow прогноза Dynatrace Intelligence**](#commit-prediction)

### Шаг 1: Workflow прогнозирования использования ресурсов Kubernetes

1. На странице обзора **Workflows** выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Workflow**.
2. Выберите заголовок по умолчанию **Untitled Workflow** и скопируйте и вставьте название workflow **Predict Resource Usage**.
3. В разделе **Select trigger** выберите тип триггера **On demand**.

   В реальном сценарии рекомендуем использовать **Time interval trigger**.

   ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — триггер workflow прогнозирования использования ресурсов Kubernetes](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-d4923ede-d1d8-4219-9342-5aaaaac89fe4-6-3736-cc5a1c4868.png)

   В первой задаче workflow вы определяете рабочие нагрузки Kubernetes, которыми будет управлять ваш workflow автоматизации для масштабирования. Теоретически можно включить все рабочие нагрузки, но это может привести к длительному времени выполнения workflow. Вместо этого сосредоточьтесь на рабочих нагрузках Kubernetes, где аннотация `predictive-kubernetes-scaling.observability-labs.dynatrace.com/enabled` установлена в `true`. Эта аннотация является хорошей практикой, позволяя разработчикам явно подписаться на рекомендации предиктивного масштабирования.
4. Добавьте задачу `find_workloads_to_scale`.

   1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле триггера. Эта задача корректирует **ограничения CPU** и **памяти** на основе спецификации `HorizontalPodAutoscaler`.
   2. В разделе **Choose action** выберите тип действия **Execute DQL query**. На панели сведений о задаче справа отображаются входные данные задачи.
   3. На вкладке **Input** скопируйте следующий DQL-запрос и вставьте его в поле **DQL query**.

      Показать код

      ```
      fetch dt.entity.cloud_application, from:now() - 5m, to:now()


      | filter kubernetesAnnotations[`predictive-kubernetes-scaling.observability-labs.dynatrace.com/enabled`] == "true"


      | fields clusterId = clustered_by[`dt.entity.kubernetes_cluster`], namespace = namespaceName, name = entity.name, type = arrayFirst(cloudApplicationDeploymentTypes), annotations = kubernetesAnnotations


      | join [ fetch dt.entity.kubernetes_cluster ],


      on: { left[clusterId] == right[id] },


      fields: { clusterName = entity.name }
      ```

      Показать скриншот настроек задачи

      ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача поиска рабочих нагрузок](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-d4923ede-d1d8-4219-9342-5aaaaac89fe4-task-find-workloads-to-scale-3720-0b07d668fa.png)

   После определения целевых рабочих нагрузок вы будете использовать Dynatrace Intelligence для прогнозирования их потребления CPU и памяти. Это поможет определить, вероятно ли превышение ими заданных ограничений ресурсов Kubernetes.
5. Добавьте задачу `predict_resource_usage`.

   1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле задачи. Эта задача проходит по всем рабочим нагрузкам, найденным задачей `predict_resource_usage`, и использует Dynatrace Intelligence для прогнозирования объёма каждого ресурса, необходимого поду.
   2. В разделе **Choose action** выберите тип действия **Analyze data**.
   3. На вкладке **Input** установите **Analyzers** в значение **Generic forecast analysis**.

      1. Установите **Start time** в **now-1h**. В реальном сценарии рекомендуем скорректировать временной интервал под вашу среду.
      2. Установите **End time** в **now**.
      3. Оставьте **Resolve data** без изменений.
   4. Скопируйте следующий DQL-запрос и вставьте его в поле **Time series data**.

      Показать код

      ```
      timeseries {


      memoryUsage = avg(dt.kubernetes.container.memory_working_set),


      memoryLimits = max(dt.kubernetes.container.limits_memory),


      cpuUsage = avg(dt.kubernetes.container.cpu_usage),


      cpuLimits = max(dt.kubernetes.container.limits_cpu)


      },


      by:{k8s.cluster.name, k8s.namespace.name, k8s.workload.kind, k8s.workload.name}


      | filter k8s.cluster.name == "{{ _.workload.clusterName }}" and k8s.namespace.name == "{{ _.workload.namespace }}" and k8s.workload.name == "{{ _.workload.name }}"


      | fields


      cluster = k8s.cluster.name,


      clusterId = "{{ _.workload.clusterId }}",


      namespace = k8s.namespace.name,


      kind = k8s.workload.kind,


      name = k8s.workload.name,


      annotations = "{{ _.workload.annotations }}",


      memoryLimit = arrayLast(memoryLimits),


      cpuLimit = arrayLast(cpuLimits),


      timeframe,


      interval,


      memoryUsage,


      cpuUsage
      ```
   5. На вкладке **Options** для **Loop task** установите **Item variable name** в значение **workload**.
   6. В поле **List** скопируйте следующее:

      ```
      {{ result("find_workloads_to_scale")["records"] }}
      ```

   Показать скриншот настроек задачи

   ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — workflow прогнозирования использования ресурсов](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-d4923ede-d1d8-4219-9342-5aaaaac89fe4-task-predict-resource-usage-6-3662-c1475e4179.png)

   Теперь, когда у вас есть прогнозируемые использование CPU и памяти, ограничения и время, вы можете анализировать и вычислять рекомендуемые изменения для рабочих нагрузок. Это выполняется в отдельной задаче, которая перебирает все прогнозы и учитывает, помечены ли рабочие нагрузки для горизонтального или вертикального масштабирования.
6. Добавьте задачу `parse_predictions`.

   1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле задачи. Эта задача получает список всех результатов прогнозирования в качестве входных данных и затем преобразует/анализирует эти результаты в список для следующих задач workflow.
   2. В разделе **Choose action** выберите тип действия **Run JavaScript**.
   3. На вкладке **Input** скопируйте следующий код и вставьте его в поле **Source code**:

      Показать код

      ```
      import {execution} from '@dynatrace-sdk/automation-utils';


      export default async function () {


      const ex = await execution();


      const predictions = await ex.result('predict\_resource\_usage');


      let workloads = \[];


      predictions.forEach(prediction => {


      prediction.result.output


      .filter(output => output.analysisStatus == 'OK' && output.forecastQualityAssessment == 'VALID')


      .forEach(output => {


      const query = JSON.parse(output.analyzedTimeSeriesQuery.expression);


      const result = output.timeSeriesDataWithPredictions.records\[0];


      let resource = query.timeSeriesData.records\[0].cpuUsage ? 'cpu' : 'memory';


      const highestPrediction = getHighestPrediction(result.timeframe, result.interval, resource, result\['dt.davis.forecast:upper'])


      workloads = addOrUpdateWorkload(workloads, result, highestPrediction);


      })


      });


      return workloads;


      }


      const getHighestPrediction = (timeframe, interval, resource, values) => {


      const highestValue = Math.max(...values);


      const index = values.indexOf(highestValue);


      const startTime = new Date(timeframe.start).getTime();


      const intervalInMs = interval / 1000000;


      return {


      resource,


      value: highestValue,


      date: new Date(startTime + (index \* intervalInMs)),


      predictedUntil: new Date(timeframe.end)


      }


      }


      const addOrUpdateWorkload = (workloads, result, prediction) => {


      const existingWorkload = workloads.find(p =>


      p.cluster === result.cluster


      && p.namespace === result.namespace


      && p.kind === result.kind


      && p.name === result.name


      );


      if (existingWorkload) {


      existingWorkload.predictions.push(prediction);


      return workloads;


      }


      const annotations = JSON.parse(result.annotations.replaceAll(`'`, `"`));


      const hpa = annotations\['predictive-kubernetes-scaling.observability-labs.dynatrace.com/managed-by-hpa'];


      workloads.push({


      cluster: result.cluster,


      clusterId: result.clusterId,


      namespace: result.namespace,


      kind: result.kind,


      name: result.name,


      repository: annotations\['predictive-kubernetes-scaling.observability-labs.dynatrace.com/managed-by-repo'],


      uuid: annotations\['predictive-kubernetes-scaling.observability-labs.dynatrace.com/uuid'],


      predictions: \[prediction],


      scalingConfig: {


      horizontalScaling: {


      enabled: hpa ? true : false,


      hpa: {


      name: hpa


      }


      },


      limits: {


      memory: result.memoryLimit,


      cpu: result.cpuLimit,


      },


      targetUtilization: getTargetUtilization(annotations),


      scaleDown: annotations\['predictive-kubernetes-scaling.observability-labs.dynatrace.com/scale-down'] ?? 'true' === 'true',


      }


      })


      return workloads;


      }


      const getTargetUtilization = (annotations) => {


      const defaultRange = annotations\['predictive-kubernetes-scaling.observability-labs.dynatrace.com/target-utilization'] ?? '80-90';


      const targetUtilization = {};


      const cpuRange = annotations\['predictive-kubernetes-scaling.observability-labs.dynatrace.com/target-cpu-utilization'] ?? defaultRange;


      targetUtilization.cpu = getTargetUtilizationFromRange(cpuRange);


      const memoryRange = annotations\['predictive-kubernetes-scaling.observability-labs.dynatrace.com/target-memory-utilization'] ?? defaultRange;


      targetUtilization.memory = getTargetUtilizationFromRange(memoryRange);


      return targetUtilization;


      }


      const getTargetUtilizationFromRange = (range) => {


      const \[min, max] = range.split('-').map(s => parseInt(s) / 100);


      const point = (min + max) / 2;


      return {min, max, point};


      }
      ```

      Показать скриншот настроек задачи

      ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача анализа прогнозов](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-d4923ede-d1d8-4219-9342-5aaaaac89fe4-task-parse-predictions-3674-cdc4d95e7e.png)
7. После запуска workflow прогнозирования использования ресурсов Kubernetes у вас будет список рабочих нагрузок с прогнозами в формате, подходящем в качестве входных данных для следующего workflow. Далее необходимо проверить, превышает ли наибольшее прогнозируемое значение использования ресурса (или остаётся ниже него при включённом понижающем масштабировании) настроенный диапазон CPU или **памяти**. Если да, сгенерировать событие Davis, содержащее запрос, который можно использовать для корректировки манифеста.

   Этот workflow имеет две ветки: вертикальное и горизонтальное масштабирование. В этих ветках оценивается необходимость масштабирования. При необходимости для обеих ветвей создаётся событие Davis.

   Сначала создадим ветку вертикального масштабирования. Она содержит задачу `add_vertical_scaling_suggestions`, где сравниваются ограничения рабочей нагрузки с прогнозируемыми значениями. Затем создаём ветку горизонтального масштабирования. Она содержит три задачи: `get_hpa_manifests`, `adjust_limits` и `add_horizontal_scaling_suggestions`, поскольку необходимо получить свойство `maxReplicas` манифеста `HorizontalPodAutoscaler` и умножить ограничение пода на максимальное количество реплик для получения абсолютного верхнего предела.

   Давайте сначала создадим ветку вертикального масштабирования workflow.

   1. Для создания ветки вертикального масштабирования добавьте задачу `add_vertical_scaling_suggestions`. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле триггера. Эта задача добавляет предложения по масштабированию для каждой рабочей нагрузки, требующей вертикального масштабирования, и анализирует заданные прогнозы Dynatrace Intelligence, возвращая все рабочие нагрузки Kubernetes с их прогнозами.
   2. В разделе **Choose action** выберите тип действия **Run JavaScript**.
   3. На вкладке **Input** скопируйте следующий код и вставьте его в поле **Source code**:

      Показать код

      ```
      import {actionExecution} from "@dynatrace-sdk/automation-utils";


      import {convert, units} from "@dynatrace-sdk/units";


      export default async function ({action\_execution\_id}) {


      const actionEx = await actionExecution(action\_execution\_id);


      const workload = actionEx.loopItem.workload;


      const targetUtilization = calculateTargetUtilization(workload.scalingConfig);


      const prompts = \[];


      const descriptions = \[`Dynatrace Intelligence has detected that the ${workload.kind} \`${workload.name}\` can be scaled based on predictive AI analysis. Therefore, this PR applies the following actions:\n\`];


      workload.predictions.forEach(prediction => {


      let resourceName;


      let newLimit;


      let range;


      let type;


      let exceedsLimit;


      if (prediction.resource === 'cpu') {


      resourceName = 'CPU';


      newLimit = `${Math.ceil(prediction.value / workload.scalingConfig.targetUtilization.cpu.point)}m`;


      range = `${workload.scalingConfig.targetUtilization.cpu.min * 100}-${workload.scalingConfig.targetUtilization.cpu.max * 100}%`;


      if (prediction.value > targetUtilization.cpu.max) {


      type = 'up';


      } else if (workload.scalingConfig.scaleDown && prediction.value < targetUtilization.cpu.min) {


      type = 'down';


      }


      exceedsLimit = type === 'up' && prediction.value > workload.scalingConfig.limits.cpu;


      } else if (prediction.resource === "memory") {


      resourceName = 'Memory';


      newLimit = `${Math.ceil(convert(


      Math.ceil(prediction.value / workload.scalingConfig.targetUtilization.memory.point),


      units.data.byte,


      units.data.mebibyte


      ))}Mi`;


      range = `${workload.scalingConfig.targetUtilization.memory.min * 100}-${workload.scalingConfig.targetUtilization.memory.max * 100}%`;


      if (prediction.value > targetUtilization.memory.max) {


      type = 'up';


      } else if (workload.scalingConfig.scaleDown && prediction.value < targetUtilization.memory.min) {


      type = 'down';


      }


      exceedsLimit = type === 'up' && prediction.value > workload.scalingConfig.limits.memory;


      }


      const prompt = `Scale the ${resourceName} request & limit of the ${workload.kind} named "${workload.name}" in this manifest to \`${newLimit}\`.\`;


      let description = type === 'up'


      ? `- â¬ï¸ **${resourceName}**: Scale up to \`${newLimit}\` (predicted to exceed its target range of ${range} at \`${prediction.date.toString()}\`)`


      : `- â¬ï¸ **${resourceName}**: Scale down to \`${newLimit}\` (predicted to stay below its target range of ${range} until \`${prediction.predictedUntil.toString()}\`)`


      if (exceedsLimit) {


      description = `- â ï¸ **${resourceName}**: Scale up to \`${newLimit}\` (predicted to exceed its ${resourceName} limit at \`${prediction.date.toString()}\`)`


      }


      descriptions.push(description);


      prompts.push({type, prompt, predictions: [prediction]});


      });


      if (prompts.length > 0) {


      descriptions.push(`\n_This Pull Request was automatically created by Dynatrace Assist._`)


      workload.scalingSuggestions = {


      description: descriptions.join('\n'),


      prompts


      };


      }


      return workload;


      }


      const calculateTargetUtilization = (scalingConfig) => {


      return {


      cpu: {


      max: scalingConfig.limits.cpu \* scalingConfig.targetUtilization.cpu.max,


      min: scalingConfig.limits.cpu \* scalingConfig.targetUtilization.cpu.min,


      point: scalingConfig.limits.cpu \* scalingConfig.targetUtilization.cpu.point


      },


      memory: {


      max: scalingConfig.limits.memory \* scalingConfig.targetUtilization.memory.max,


      min: scalingConfig.limits.memory \* scalingConfig.targetUtilization.memory.min,


      point: scalingConfig.limits.memory \* scalingConfig.targetUtilization.memory.point


      }


      };


      }
      ```
   4. На вкладке **Options** для **Loop task** установите **Item variable name** в значение **workload**.
   5. В поле **List** скопируйте и вставьте следующее:

      ```
      [{% for workload in result("parse_predictions") %}


      {% if workload.scalingConfig.horizontalScaling.enabled == false %}


      {{ workload }},


      {% endif %}


      {% endfor %}]
      ```

      Задача перебирает все рабочие нагрузки Kubernetes и проверяет, будет ли превышено ограничение. Если да, добавляет свойство `scalingSuggestion` к рабочей нагрузке, включающее запрос и описание предстоящих действий.

   Показать скриншот настроек задачи

   ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача добавления предложений вертикального масштабирования](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-d4923ede-d1d8-4219-9342-5aaaaac89fe4-task-add-vertical-scaling-suggestions-3648-0d5400892a.png)
8. Создадим ветку горизонтального масштабирования нашего workflow. Она состоит из трёх задач: `get_hpa_manifests`, `adjust_limits` и `add_horizontal_scaling_suggestions`.

   1. Для добавления задачи `get_hpa_manifests` выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле задачи. Эта задача корректирует **ограничения CPU** и **памяти** на основе спецификации `HorizontalPodAutoscaler`.
   2. В разделе **Choose action** выберите тип действия Kubernetes **Get resource**.
   3. На вкладке **Input**

      1. Выберите ранее созданное **Connection**.
      2. Установите **Namespace** в `{{ _.workload.namespace }}`.
      3. Установите **Resource Type** в `horizontalpodautoscalers.autoscaling`.
      4. Установите **Name** в `{{ _.workload.name }}`.
   4. На вкладке **Options**

      1. Включите **Loop task**. Перебирает все рабочие нагрузки, где включено горизонтальное масштабирование.
      2. Установите **Item variable name** в `workload`.
      3. В поле **List** скопируйте и вставьте следующее:

         ```
         [{% for workload in result("parse_predictions") %}


         {% if workload.scalingConfig.horizontalScaling.enabled %}


         {{ workload }},


         {% endif %}


         {% endfor %}]
         ```

         Показать скриншот настроек задачи

         ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — получение манифестов HPA](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-d4923ede-d1d8-4219-9342-5aaaaac89fe4-task-get-hpa-manifests-3665-0cf99a219a.png)
9. Добавьте задачу `adjust_limits`.

   1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле задачи. Эта задача корректирует **ограничения CPU** и **памяти** на основе спецификации `HorizontalPodAutoscaler`.
   2. В разделе **Choose action** выберите тип действия **Run JavaScript**.
   3. На вкладке **Input** скопируйте следующий код и вставьте его в поле **Source code**:

      Показать код

      ```
      import {execution, actionExecution} from "@dynatrace-sdk/automation-utils";


      export default async function ({execution\_id, action\_execution\_id}) {


      const actionEx = await actionExecution(action\_execution\_id);


      const workload = actionEx.loopItem.workload;


      // Получение соответствующего манифеста HPA


      const ex = await execution(execution\_id);


      const allHpaManifests = await ex.result('get\_hpa\_manifests');


      const hpaManifest = allHpaManifests.find(manifest =>


      manifest.metadata.name === workload.scalingConfig.horizontalScaling.hpa.name


      && manifest.metadata.namespace === workload.namespace


      && manifest.spec.scaleTargetRef.name === workload.name


      );


      // Корректировка ограничений


      const maxReplicas = hpaManifest.spec.maxReplicas;


      workload.scalingConfig.horizontalScaling.hpa = {


      ...workload.scalingConfig.horizontalScaling.hpa,


      maxReplicas,


      uuid: hpaManifest.metadata.annotations\['predictive-kubernetes-scaling.observability-labs.dynatrace.com/uuid'],


      limits: {


      cpu: maxReplicas \* workload.scalingConfig.limits.cpu,


      memory: maxReplicas \* workload.scalingConfig.limits.memory


      }


      };


      return workload;


      }
      ```
   4. На вкладке **Options** для **Loop task** установите **Item variable name** в значение **workload**.
   5. В поле **List** скопируйте и вставьте следующее:

      ```
      [{% for workload in result("parse_predictions") %}


      {% if workload.scalingConfig.horizontalScaling.enabled %}


      {{ workload }},


      {% endif %}


      {% endfor %}]
      ```

      Объединяет все рабочие нагрузки, где включено горизонтальное масштабирование, с манифестами HPA (HorizontalPodAutoscaler) из предыдущего шага, а затем корректирует ограничения путём умножения на `maxReplicas` HPA.

      Показать скриншот настроек задачи

      ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача корректировки ограничений](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-d4923ede-d1d8-4219-9342-5aaaaac89fe4-task-adjust-limits-3652-8953c9893d.png)
10. Добавьте задачу `add_horizontal_scaling_suggestions`.

    1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле триггера. Эта задача добавляет предложения по масштабированию для каждой рабочей нагрузки, требующей горизонтального масштабирования.
    2. В разделе **Choose action** выберите тип действия **Run JavaScript**.
    3. На вкладке **Input** скопируйте следующий код и вставьте его в поле **Source code**:

       Показать код

       ```
       import {actionExecution} from "@dynatrace-sdk/automation-utils";


       import {convert, units} from "@dynatrace-sdk/units";


       export default async function ({action_execution_id}) {


       const actionEx = await actionExecution(action_execution_id);


       const workload = actionEx.loopItem.workload;


       const targetUtilization = calculateTargetUtilization(workload.scalingConfig);


       let newMaxReplicas = 0;


       const predictionsToApply = [];


       const descriptions = [];


       let exceedsLimits = false;


       workload.predictions.forEach(prediction => {


       let replicas = 0;


       if (prediction.resource === 'cpu' && prediction.value > targetUtilization.cpu.max) {


       predictionsToApply.push(prediction);


       // Вычисление нового максимального количества реплик


       const newLimit = Math.ceil(prediction.value / workload.scalingConfig.targetUtilization.cpu.point);


       replicas = Math.ceil(newLimit / workload.scalingConfig.limits.cpu);


       // Получение описания


       if (prediction.value > workload.scalingConfig.horizontalScaling.hpa.limits.cpu) {


       exceedsLimits = true;


       descriptions.push(


       `  - â ï¸ **CPU**: Predicted to exceed its CPU limit of \`${workload.scalingConfig.horizontalScaling.hpa.limits.cpu}m\` ` +


       `(\`${workload.scalingConfig.limits.cpu}m * ${workload.scalingConfig.horizontalScaling.hpa.maxReplicas}\`) at \`${prediction.date.toString()}\`)`


       )


       } else {


       const range = `${workload.scalingConfig.targetUtilization.cpu.min * 100}-${workload.scalingConfig.targetUtilization.cpu.max * 100}%`;


       descriptions.push(`  - â¬ï¸ **CPU**: Predicted to exceed its target range of ${range} at \`${prediction.date.toString()}\`)`)


       }


       } else if (prediction.resource === 'memory' && prediction.value > targetUtilization.memory.max) {


       predictionsToApply.push(prediction);


       // Вычисление нового максимального количества реплик


       const newLimit = Math.ceil(prediction.value / workload.scalingConfig.targetUtilization.memory.point);


       replicas = Math.ceil(newLimit / workload.scalingConfig.limits.memory);


       // Получение описания


       if (prediction.value > workload.scalingConfig.horizontalScaling.hpa.limits.memory) {


       exceedsLimits = true;


       const limit = `${convert(


       workload.scalingConfig.limits.memory,


       units.data.byte,


       units.data.mebibyte


       )}`;


       descriptions.push(


       `  - â ï¸ **Memory**: Predicted to exceed its Memory limit of \`${limit * workload.scalingConfig.horizontalScaling.hpa.maxReplicas}Mi\` ` +


       `(\`${limit}Mi * ${workload.scalingConfig.horizontalScaling.hpa.maxReplicas}\`) at \`${prediction.date.toString()}\`)`


       )


       } else {


       const range = `${workload.scalingConfig.targetUtilization.memory.min * 100}-${workload.scalingConfig.targetUtilization.memory.max * 100}%`;


       descriptions.push(`  - â¬ï¸ **Memory**: Predicted to exceed its target range of ${range} at \`${prediction.date.toString()}\`)`)


       }


       }


       if (replicas > newMaxReplicas) {


       newMaxReplicas = replicas;


       }


       });


       if (newMaxReplicas > 0) {


       const fullDescription = [


       `Dynatrace Intelligence has detected that the deployment anomaly-simulation can be scaled based on predictive AI analysis. Therefore, this PR applies the following actions:\n`,


       `- ${exceedsLimits ? 'â ï¸' : 'â¬ï¸'} **HorizontalPodAutoscaler**: Scale the maximum number of replicas to \`${newMaxReplicas}\`:`,


       ...descriptions,


       `\n\_This Pull Request was automatically created by Dynatrace Assist.\_`    ];


       workload.scalingSuggestions = {


       description: fullDescription.join('\n'),


       prompts: [{


       type: 'up',


       prompt: `Scale the maxReplicas of the HorizontalPodAutoscaler named "${workload.scalingConfig.horizontalScaling.hpa.name}" in this manifest to ${newMaxReplicas}.`,


       predictions: predictionsToApply


       }]


       };


       }


       return workload;


       }


       const calculateTargetUtilization = (scalingConfig) => {


       const limits = scalingConfig.horizontalScaling.hpa.limits;


       return {


       cpu: {


       max: limits.cpu * scalingConfig.targetUtilization.cpu.max,


       min: limits.cpu * scalingConfig.targetUtilization.cpu.min,


       point: limits.cpu * scalingConfig.targetUtilization.cpu.point


       },


       memory: {


       max: limits.memory * scalingConfig.targetUtilization.memory.max,


       min: limits.memory * scalingConfig.targetUtilization.memory.min,


       point: limits.memory * scalingConfig.targetUtilization.memory.point


       }


       };


       }
       ```
    4. На вкладке **Options** для **Loop task** установите **Item variable name** в значение **workload**.
    5. В поле **List** скопируйте и вставьте следующее `{{ result("adjust_limits") }}`. Перебирает все рабочие нагрузки и проверяет, будут ли превышены ограничения. Если да, добавляет свойство `scalingSuggestion` к рабочей нагрузке, включающее запрос и описание предстоящих действий.

       Показать скриншот настроек задачи

       ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача добавления предложений горизонтального масштабирования](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-d4923ede-d1d8-4219-9342-5aaaaac89fe4-task-add-horizontal-scaling-suggestions-3695-e2eb82d32b.png)

       Теперь у вас есть список рабочих нагрузок с предложениями по масштабированию от вертикального и горизонтального масштабирования. Необходимо получить оба списка и создать события для рабочих нагрузок, требующих масштабирования.

       Показать notebook с горизонтальным и вертикальным масштабированием

       ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — notebook с вертикальным и горизонтальным масштабированием](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-notebooks-notebook-e76d37d8-6355-429c-95d8-e91582e2b699-8-2893-70d613b5f6.png)
11. Добавьте задачу `create_scaling_events`.

    1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле триггера. Эта задача инициирует пользовательское событие Davis для каждой рабочей нагрузки, требующей масштабирования, и позволяет другим автоматизациям реагировать на него.
    2. В разделе **Choose action** выберите тип действия **Run JavaScript**.
    3. На вкладке **Input** скопируйте следующий код и вставьте его в поле **Source code**:

       Показать код

       ```
       import {actionExecution} from "@dynatrace-sdk/automation-utils";


       import {eventsClient, EventIngestEventType} from "@dynatrace-sdk/client-classic-environment-v2";


       export default async function ({action_execution_id}) {


       const actionEx = await actionExecution(action_execution_id);


       const workload = actionEx.loopItem.workload;


       if (!workload.scalingSuggestions) {


       return;


       }


       const prompts = [];


       const types = new Set([]);


       workload.scalingSuggestions.prompts.forEach(prompt => {


       prompts.push(prompt.prompt);


       types.add(prompt.type);


       });


       const horizontalScalingConfig = workload.scalingConfig.horizontalScaling;


       let limits;


       if (horizontalScalingConfig.enabled) {


       limits = {


       cpu: horizontalScalingConfig.hpa.limits.cpu,


       memory: horizontalScalingConfig.hpa.limits.memory,


       }


       } else {


       limits = {


       cpu: workload.scalingConfig.limits.cpu,


       memory: workload.scalingConfig.limits.memory,


       }


       }


       const targetUtilization = workload.scalingConfig.targetUtilization;


       const event = {


       eventType: EventIngestEventType.CustomInfo,


       title: 'Suggesting to Scale Because of Dynatrace Intelligence Predictions',


       entitySelector: `type(CLOUD_APPLICATION),entityName.equals("${workload.name}"),namespaceName("${workload.namespace}"),` +


       `toRelationships.isClusterOfCa(type(KUBERNETES_CLUSTER),entityId("${workload.clusterId}"))`,


       properties: {


       'kubernetes.predictivescaling.type': 'DETECT_SCALING',


       // Рабочая нагрузка


       'kubernetes.predictivescaling.workload.cluster.name': workload.cluster,


       'kubernetes.predictivescaling.workload.cluster.id': workload.clusterId,


       'kubernetes.predictivescaling.workload.kind': workload.kind,


       'kubernetes.predictivescaling.workload.namespace': workload.namespace,


       'kubernetes.predictivescaling.workload.name': workload.name,


       'kubernetes.predictivescaling.workload.uuid': workload.uuid,


       'kubernetes.predictivescaling.workload.limits.cpu': limits.cpu,


       'kubernetes.predictivescaling.workload.limits.memory': limits.memory,


       // Прогноз


       'kubernetes.predictivescaling.prediction.type': [...types].join(','),


       'kubernetes.predictivescaling.prediction.prompt': prompts.join(' '),


       'kubernetes.predictivescaling.prediction.description': workload.scalingSuggestions.description,


       'kubernetes.predictivescaling.prediction.suggestions': JSON.stringify(workload.scalingSuggestions),


       // Целевое использование


       'kubernetes.predictivescaling.targetutilization.cpu.min': targetUtilization.cpu.min,


       'kubernetes.predictivescaling.targetutilization.cpu.max': targetUtilization.cpu.max,


       'kubernetes.predictivescaling.targetutilization.cpu.point': targetUtilization.cpu.point,


       'kubernetes.predictivescaling.targetutilization.memory.min': targetUtilization.memory.min,


       'kubernetes.predictivescaling.targetutilization.memory.max': targetUtilization.memory.max,


       'kubernetes.predictivescaling.targetutilization.memory.point': targetUtilization.memory.point,


       // Цель


       'kubernetes.predictivescaling.target.uuid': horizontalScalingConfig.enabled ? horizontalScalingConfig.hpa.uuid : workload.uuid,


       'kubernetes.predictivescaling.target.repository': workload.repository,


       },


       }


       await eventsClient.createEvent({body: event});


       return event;


       }
       ```
    4. На вкладке **Options** для **Loop task** установите **Item variable name** в значение **workload**.
    5. В поле **List** скопируйте и вставьте следующее

       ```
       {{ result("add_horizontal_scaling_suggestions") + result("add_vertical_scaling_suggestions") }}
       ```

       Перебирает все рабочие нагрузки и проверяет наличие предложений по масштабированию. Если они есть, создаёт событие со всей необходимой информацией.

       Показать скриншот настроек задачи

       ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача создания событий масштабирования](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-d4923ede-d1d8-4219-9342-5aaaaac89fe4-task-create-scaling-events-3647-8f46325f52.png)
12. Выберите **Save**.
13. Выберите **Run**.

    Результатом первого workflow является событие, которое запустит workflow фиксации прогноза Dynatrace Intelligence, создаваемый на следующем шаге. Разделение обнаружения масштабирования и фактического действия масштабирования является хорошей практикой.

    Если ваш workflow не определяет никаких рабочих нагрузок или прогнозов, проверьте аннотации на ваших рабочих нагрузках. Задайте меньшие целевые показатели, чтобы целевой прогноз достигался быстрее. Помните, что это пример сценария использования, и вполне нормально изменять настройки, чтобы увидеть, как ведёт себя workflow.

### Шаг 2: Workflow фиксации прогноза Dynatrace Intelligence

Этот workflow запускается каждый раз, когда первый workflow обнаруживает рабочую нагрузку Kubernetes, которую необходимо масштабировать, и генерирует событие Davis.

#### Предварительное требование

В этом workflow задача использует JavaScript для вызова API GitHub для создания pull request. Хотя некоторые действия GitHub Connector используют соединение, настроенное при выполнении [настройки GitHub Connector](../analyze-explore-automate/workflows/actions/github/github-workflows-setup.md "Узнайте, как настроить GitHub Connector."), пользовательские шаги должны использовать тот же персональный токен доступа (PAT), который запрашивается из хранилища учётных данных. Ещё один необходимый токен — это токен API платформы Dynatrace для взаимодействия с агентным и генеративным ИИ API Dynatrace Intelligence.

В качестве предварительного условия необходимо создать новые записи в хранилище учётных данных Dynatrace, хранящие PAT GitHub и токен API платформы Dynatrace. Вам понадобятся идентификаторы хранилища учётных данных; в фрагментах кода следует заменить соответствующие заглушки на ваши идентификаторы хранилища учётных данных.

Для создания второго workflow

1. На странице обзора **Workflows** выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Workflow**.
2. Выберите заголовок по умолчанию **Untitled Workflow** и скопируйте и вставьте название workflow **Commit Dynatrace Intelligence Prediction**.
3. В разделе **Select trigger**

   1. Выберите тип триггера **Event trigger**.
   2. В поле **Filter query** скопируйте и вставьте следующее

      ```
      kubernetes.predictivescaling.type == "DETECT_SCALING"
      ```
4. Добавьте задачу `find_manifest`.

   1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле задачи. Эта задача выполняет поиск манифеста рабочей нагрузки на GitHub.

      Замените `CREDENTIALS_VAULT-ID_FOR_GITLAB_PAT_TOKEN` на ваш идентификатор хранилища учётных данных, созданный в предварительном требовании этого шага.
   2. В разделе **Choose action** выберите тип действия **Run JavaScript**.
   3. На вкладке **Input** скопируйте следующий код и вставьте его в поле **Source code**:

      Показать код

      ```
      import {execution} from '@dynatrace-sdk/automation-utils';


      import {credentialVaultClient} from "@dynatrace-sdk/client-classic-environment-v2";


      export default async function () {


      const ex = await execution();


      const event = ex.params.event;


      const apiToken = await credentialVaultClient.getCredentialsDetails({


      id: "CREDENTIALS_VAULT-ID_FOR_GITLAB_PAT_TOKEN",


      }).then((credentials) => credentials.token);


      // Поиск файла


      const url = 'https://api.github.com/search/code?q=' +


      `"predictive-kubernetes-scaling.observability-labs.dynatrace.com/uuid:%20'${event['kubernetes.predictivescaling.target.uuid']}'"` +


      `+repo:${event['kubernetes.predictivescaling.target.repository']}` +


      `+language:YAML`


      const response = await fetch(url, {


      method: 'GET',


      headers: {


      'Authorization': `Bearer ${apiToken}`


      }


      }).then(response => response.json());


      const searchResult = response.items[0];


      // Получение ветки по умолчанию


      const repository = await fetch(searchResult.repository.url, {


      method: 'GET',


      headers: {


      'Authorization': `Bearer ${apiToken}`


      }


      }).then(response => response.json());


      return {


      owner: searchResult.repository.owner.login,


      repository: searchResult.repository.name,


      filePath: searchResult.path,


      defaultBranch: repository.default_branch


      }


      }
      ```

      Показать скриншот настроек задачи

      ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача поиска манифеста](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-1cf51d5c-0235-49da-8e46-66c3b7811573-task-find-manifest-3654-1f73e68fed.png)
5. Добавьте задачу `fetch_manifest`.

   1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле задачи. Эта задача получает содержимое манифеста.
   2. В разделе **Choose action** выберите тип действия GitHub **Get content**.
   3. На вкладке **Input**

      1. Установите **Connection**.
      2. Установите **Owner** в `find.manifest.owner`.
      3. Установите **Repository** в `find.manifest.repository`.
      4. Установите **File path** в `find.manifest.filePath`.
      5. Установите **Reference** в `find.manifest.defaultBranch`.
   4. На вкладке **Options** включите **Adapt timeout** и установите **Timeout this task (seconds)** в `900`.

      Показать скриншот настроек задачи

      ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача получения манифеста](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-1cf51d5c-0235-49da-8e46-66c3b7811573-task-fetch-manifest-3657-da62d61d33.png)
6. Добавьте задачу `apply_suggestions`.

   1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле задачи. Эта задача использует Dynatrace Assist для применения всех предложений к манифесту.

      Замените `CREDENTIALS_VAULT-ID_FOR_DYNATRACE_COPILOT_TOKEN` на ваш идентификатор хранилища учётных данных, созданный в предварительном требовании этого шага.
   2. В разделе **Choose action** выберите тип действия **Run JavaScript**.
   3. На вкладке **Input** скопируйте следующий код и вставьте его в поле **Source code**:

      Показать код

      ```
      import {execution} from '@dynatrace-sdk/automation-utils';


      import {credentialVaultClient} from '@dynatrace-sdk/client-classic-environment-v2';


      import {getEnvironmentUrl} from '@dynatrace-sdk/app-environment'


      export default async function () {


      const ex = await execution();


      var manifest = (await ex.result('fetch_manifest')).content;


      const event = ex.params.event;


      const apiToken = await credentialVaultClient.getCredentialsDetails({


      id: "CREDENTIALS_VAULT-ID_FOR_DYNATRACE_COPILOT_TOKEN",


      }).then((credentials) => credentials.token);


      const url = `${getEnvironmentUrl()}/platform/davis/copilot/v0.2/skills/conversations:message`;


      const response = await fetch(url, {


      method: 'POST',


      headers: {


      'Authorization': `Bearer ${apiToken}`,


      'Content-Type': 'application/json'


      },


      body: JSON.stringify({


      text: `${event['kubernetes.predictivescaling.prediction.prompt']}\n\n${manifest}`


      })


      }).then(response => response.json());


      return {


      manifest: response.text.match(/(?<=^```(yaml|yml).*\n)([^`])*(?=^```$)/gm)[0],


      time: new Date(event.timestamp).getTime(),


      description: event['kubernetes.predictivescaling.prediction.description']


      };


      }
      ```

      Показать скриншот настроек задачи

      ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача применения предложений](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-1cf51d5c-0235-49da-8e46-66c3b7811573-task-apply-suggestions-3702-3c3ae50427.png)
7. Добавьте задачу `update_manifest`.

   1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле задачи. Эта задача обновляет манифест и отправляет его в новую ветку на GitHub.
   2. В разделе **Choose action** выберите тип действия GitHub **Create or replace file**.
   3. На вкладке **Input**

      1. Установите **Connection**.
      2. Установите **Owner** в `find.manifest.owner`.
      3. Установите **Repository** в `find.manifest.repository`.
      4. Установите **Source branch** в `apply-davis-predictions-{{result("apply_suggestions").time}}`.
      5. Установите **Target branch** в `find_manifest.defaultBranch`.
      6. Установите **Pull request title** в `Apply suggestions predicted by Dynatrace Intelligence`.
      7. Установите **Pull request description** в `apply_suggestions.description`.

      Показать скриншот настроек задачи

      ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача обновления манифеста](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-1cf51d5c-0235-49da-8e46-66c3b7811573-task-update-manifest-3658-77cbd2fdc1.png)
8. Добавьте задачу `create_pull_request`.

   1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле задачи. Эта задача создаёт pull request (PR), включающий все предложенные изменения.
   2. В разделе **Choose action** выберите тип действия GitHub **Create pull request**.
   3. На вкладке **Input** установите **Connection**.

      1. Установите **Owner** в `find.manifest.owner`.
      2. Включите **Commit on a new branch**.
      3. Установите **Source branch** в `find.manifest.defaultBranch`.
      4. Установите **Branch** в `apply-davis-predictions-{{result("apply_suggestions").time}}`.
      5. Установите **File path** в `find_manifest.filePath`.
      6. Установите **File content** в `apply_suggestions.manifest`.
      7. Установите **Commit message** в `Apply suggestions predicted by Dynatrace Intelligence: {{ result("apply_suggestions").description }}`.
   4. На вкладке **Options** включите **Adapt timeout** и установите **Timeout this task (seconds)** в `900`.

      Показать скриншот настроек задачи

      ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача создания pull request](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-1cf51d5c-0235-49da-8e46-66c3b7811573-task-create-pull-request-3665-b4e5d835cc.png)
9. Добавьте задачу `create_suggestion_applied_event`.

   1. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Add task** на узле задачи. Эта задача инициирует событие типа `Custom Info` и позволяет другим компонентам реагировать на него.
   2. В разделе **Choose action** выберите тип действия **Run JavaScript**.
   3. На вкладке **Input** скопируйте следующий код и вставьте его в поле **Source code**:

      Показать код

      ```
      import {execution} from '@dynatrace-sdk/automation-utils';


      import {eventsClient, EventIngestEventType} from "@dynatrace-sdk/client-classic-environment-v2";


      export default async function () {


      const ex = await execution();


      const pullRequest = (await ex.result('create_pull_request')).pullRequest;


      const event = ex.params.event;


      const eventBody = {


      eventType: EventIngestEventType.CustomInfo,


      title: 'Applied Scaling Suggestion Because of Dynatrace Intelligence Prediction',


      entitySelector: `type(CLOUD_APPLICATION),entityName.equals("${event['kubernetes.predictivescaling.workload.name']}"),` +


      `namespaceName("${event['kubernetes.predictivescaling.workload.namespace']}"),` +


      `toRelationships.isClusterOfCa(type(KUBERNETES_CLUSTER),entityId("${event['kubernetes.predictivescaling.workload.cluster.id']}"))`,


      properties: {


      'kubernetes.predictivescaling.type': 'SUGGEST_SCALING',


      // Рабочая нагрузка


      'kubernetes.predictivescaling.workload.cluster.name': event['kubernetes.predictivescaling.workload.cluster.name'],


      'kubernetes.predictivescaling.workload.cluster.id': event['kubernetes.predictivescaling.workload.cluster.id'],


      'kubernetes.predictivescaling.workload.kind': event['kubernetes.predictivescaling.workload.kind'],


      'kubernetes.predictivescaling.workload.namespace': event['kubernetes.predictivescaling.workload.namespace'],


      'kubernetes.predictivescaling.workload.name': event['kubernetes.predictivescaling.workload.name'],


      'kubernetes.predictivescaling.workload.uuid': event['kubernetes.predictivescaling.workload.uuid'],


      'kubernetes.predictivescaling.workload.limits.cpu': event['kubernetes.predictivescaling.workload.limits.cpu'],


      'kubernetes.predictivescaling.workload.limits.memory': event['kubernetes.predictivescaling.workload.limits.memory'],


      // Прогноз


      'kubernetes.predictivescaling.prediction.type': event['kubernetes.predictivescaling.prediction.type'],


      'kubernetes.predictivescaling.prediction.prompt': event['kubernetes.predictivescaling.prediction.prompt'],


      'kubernetes.predictivescaling.prediction.description': event['kubernetes.predictivescaling.prediction.description'],


      'kubernetes.predictivescaling.prediction.suggestions': event['kubernetes.predictivescaling.prediction.suggestions'],


      // Целевое использование


      'kubernetes.predictivescaling.targetutilization.cpu.min': event['kubernetes.predictivescaling.targetutilization.cpu.min'],


      'kubernetes.predictivescaling.targetutilization.cpu.max': event['kubernetes.predictivescaling.targetutilization.cpu.max'],


      'kubernetes.predictivescaling.targetutilization.cpu.point': event['kubernetes.predictivescaling.targetutilization.cpu.point'],


      'kubernetes.predictivescaling.targetutilization.memory.min': event['kubernetes.predictivescaling.targetutilization.memory.min'],


      'kubernetes.predictivescaling.targetutilization.memory.max': event['kubernetes.predictivescaling.targetutilization.memory.max'],


      'kubernetes.predictivescaling.targetutilization.memory.point': event['kubernetes.predictivescaling.targetutilization.memory.point'],


      // Цель


      'kubernetes.predictivescaling.target.uuid': event['kubernetes.predictivescaling.target.uuid'],


      'kubernetes.predictivescaling.target.repository': event['kubernetes.predictivescaling.target.repository'],


      // Pull Request


      'kubernetes.predictivescaling.pullrequest.id': `${pullRequest.id}`,


      'kubernetes.predictivescaling.pullrequest.url': pullRequest.url,


      },


      };


      await eventsClient.createEvent({body: eventBody});


      return eventBody;


      }
      ```

      Показать скриншот настроек задачи

      ![Сценарий использования: Предиктивное автомасштабирование рабочих нагрузок Kubernetes — задача создания события применения предложения](https://dt-cdn.net/images/ypd98635-sprint-apps-dynatracelabs-com-ui-apps-dynatrace-automations-workflows-1cf51d5c-0235-49da-8e46-66c3b7811573-task-create-suggestion-applied-event-3689-89a748c667.png)

## Итог

Теперь у вас есть два Dynatrace workflow, которые обеспечивают ИИ-ассистируемое предиктивное масштабирование как код. Всё, что вам нужно сделать — аннотировать ваши развёртывания Kubernetes и ждать, когда Dynatrace откроет pull request с помощью генеративного ИИ Dynatrace Intelligence для применения прогнозируемых ограничений памяти и CPU к вашим манифестам.

## Связанные темы

* [Изучите наши примеры дашбордов на Dynatrace Playground](https://dt-url.net/playground-obslab-predictive-kubernetes-scaling)
* [Получите практический опыт и разверните наш демонстрационный проект с помощью GitHub Codespace](https://dt-url.net/obslab-predictive-kubernetes-scaling)
* [Смотрите наше видео на YouTube](https://dt-url.net/predictive-autoscaling-k8s)
