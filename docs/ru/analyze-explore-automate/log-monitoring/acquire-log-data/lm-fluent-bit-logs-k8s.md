---
title: Передача журналов Kubernetes с помощью Fluent Bit (Классические журналы)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/lm-fluent-bit-logs-k8s
scraped: 2026-03-05T21:35:44.907456
---

* Классический
* Учебник
* 5-минутное чтение

Мониторинг журналов Classic

Для самой новой версии Dynatrace см. Передача журналов Kubernetes с помощью Fluent Bit.

Эта страница предоставляет инструкции по развертыванию и настройке Fluent Bit в вашей среде Kubernetes для сбора журналов.

## Предварительные условия

* Настройте [ограничения контекста безопасности (SCC)](https://dt-url.net/fb02ljw) правильно, если вы используете OpenShift.
* Helm является обязательным. Используйте [версию Helm 3](https://dt-url.net/n5036j1).
* Исходящий трафик должен быть разрешен из пространства имен, в котором установлен Fluent Bit (`dynatrace-fluent-bit`), в Dynatrace.
* Для обогащения рабочей нагрузки требуется версия 1.1.0+ оператора Dynatrace.

## Настройка конфигурации Fluent Bit

Следуйте пошаговому руководству, чтобы подготовить конфигурацию для Fluent Bit.

1. Скопируйте образец файла `values.yaml` и откройте его в вашем предпочитаемом редакторе.

   Пример журналов контейнеров (values.yaml)

   ```
   openShift:


   # установите значение true для OpenShift


   enabled: false


   securityContext:


   capabilities:


   drop:


   - ALL


   readOnlyRootFilesystem: true


   # раскомментируйте строку ниже для OpenShift


   #privileged: true


   rbac:


   nodeAccess: true


   config:


   inputs: |


   [INPUT]


   Name tail


   Tag kube.*


   Path /var/log/containers/*.log


   DB /fluent-bit/tail/kube.db


   DB.Sync Normal


   multiline.parser cri


   Mem_Buf_Limit 15MB


   Skip_Long_Lines On


   filters: |


   [FILTER]


   Name kubernetes


   Match kube.*


   Merge_Log On


   Keep_Log Off


   K8S-Logging.Parser Off


   K8S-Logging.Exclude Off


   Labels Off


   Annotations On


   Use_Kubelet On


   Kubelet_Host ${NODE_IP}


   tls.verify Off


   Buffer_Size 0


   # Только включайте журналы из подов с аннотацией


   #[FILTER]


   #    Name grep


   #    Match kube.*


   #    Regex $kubernetes['annotations']['logs.dynatrace.com/ingest'] ^true$


   # Только включайте журналы из определенных пространств имен, удалите весь раздел фильтра, чтобы получить все журналы


   #[FILTER]


   #    Name grep


   #    Match kube.*


   #    Logical_Op or


   #    Regex $kubernetes['namespace_name'] ^my-namespace-a$


   #    Regex $kubernetes['namespace_name'] ^my-namespace-b$


   [FILTER]


   Name nest


   Match kube.*


   Operation lift


   Nested_under kubernetes


   Add_prefix kubernetes.


   [FILTER]


   Name nest


   Match kube.*


   Operation lift


   Nested_under kubernetes.annotations


   Add_prefix kubernetes.annotations.


   [FILTER]


   Name nest


   Match kube.*


   Operation nest


   Nest_under dt.metadata


   Wildcard kubernetes.annotations.metadata.dynatrace.com/*


   [FILTER]


   Name parser


   Match kube.*


   Key_name kubernetes.annotations.metadata.dynatrace.com


   Parser docker


   Preserve_Key false


   Reserve_Data true


   [FILTER]


   Name nest


   Match kube.*


   Operation lift


   Nested_under dt.metadata


   Remove_prefix kubernetes.annotations.metadata.dynatrace.com/


   [FILTER]


   Name modify


   Match kube.*


   # Отображайте данные в формат журнала Dynatrace


   Rename time timestamp


   Rename log content


   Rename kubernetes.host k8s.node.name


   Rename kubernetes.namespace_name k8s.namespace.name


   Rename kubernetes.pod_id k8s.pod.uid


   Rename kubernetes.pod_name k8s.pod.name


   Rename kubernetes.container_name k8s.container.name


   Add k8s.cluster.name ${K8S_CLUSTER_NAME)


   Add k8s.cluster.uid ${K8S_CLUSTER_UID)


   # устарело, но все еще используется


   Add dt.kubernetes.cluster.name ${K8S_CLUSTER_NAME)


   Add dt.kubernetes.cluster.id ${K8S_CLUSTER_UID)


   Remove_wildcard kubernetes.


   outputs: |


   # Отправьте данные в Dynatrace лог ингест API


   [OUTPUT]


   Name http


   Match kube.*


   host ${DT_INGEST_HOST)


   port 443


   tls On


   tls.verify On


   uri /api/v2/logs/ingest


   format json


   allow_duplicated_headers false


   header Authorization Api-Token ${DT_INGEST_TOKEN)


   header Content-Type application/json; charset=utf-8


   json_date_key timestamp


   json_date_format iso8601


   log_response_payload false


   daemonSetVolumes:


   - hostPath:


   path: /var/lib/fluent-bit/


   name: positions


   - hostPath:


   path: /var/log/containers


   name: containers


   - hostPath:


   path: /var/log/pods


   name: pods


   daemonSetVolumeMounts:


   - mountPath: /fluent-bit/tail


   name: positions


   - mountPath: /var/log/containers


   name: containers


   readOnly: true


   - mountPath: /var/log/pods


   name: pods


   readOnly: true


   podAnnotations:


   dynatrace.com/inject: "false"


   #  Раскомментируйте это, чтобы собирать метрики Prometheus для Fluent Bit


   #  metrics.dynatrace.com/path: "/api/v1/metrics/prometheus"


   #  metrics.dynatrace.com/port: "2020"


   #  metrics.dynatrace.com/scrape: "true"


   envWithTpl:


   - name: K8S_CLUSTER_UID


   value: '{{ (lookup "v1" "Namespace" "" "kube-system").metadata.uid }}'


   env:


   - name: K8S_CLUSTER_NAME


   value: "{ENTER_YOUR_CLUSTER_NAME}"


   - name: DT_INGEST_HOST


   value: "{your-environment-id}.live.dynatrace.com"


   - name: DT_INGEST_TOKEN


   value: "{ENTER_YOUR_INGEST_TOKEN}"


   - name: NODE_IP


   valueFrom:


   fieldRef:


   apiVersion: v1


   fieldPath: status.hostIP
   ```
2. Получите токен Dynatrace API с областью `logs.ingest` (Ingest Logs) для переменной среды `DT_INGEST_TOKEN`.
3. Обновите переменные среды `K8S_CLUSTER_NAME`, `DT_INGEST_HOST` и `DT_INGEST_TOKEN` в файле `values.yaml`. Используйте одно и то же имя кластера, которое вы настроили в Dynatrace для `K8S_CLUSTER_NAME`, и укажите ваш конечный пункт SaaS или Managed в качестве `DT_INGEST_HOST`.
4. Необязательно. Адаптируйте раздел фильтра в файле `values.yaml`, чтобы нацелиться на определенные пространства имен или поды, как описано в разделе [Фильтр Fluent Bit](https://dt-url.net/m903n8q) для получения подробной информации.
5. Необязательно. Обеспечьте удаление или маскировку любой конфиденциальной информации в журналах.
6. Сохраните файл.

## Установка и настройка Fluent Bit с помощью Helm

1. Добавьте репозиторий fluent в ваши локальные репозитории Helm

   ```
   helm repo add fluent https://fluent.github.io/helm-charts
   ```
2. Обновите репозиторий Fluent Bit

   ```
   helm repo update
   ```
3. Установите Fluent Bit с подготовленной конфигурацией

   ```
   helm install fluent-bit fluent/fluent-bit -f values.yaml --create-namespace --namespace dynatrace-fluent-bit
   ```

## Удаление Fluent Bit

Удалите Fluent Bit из вашей среды Kubernetes, используя следующую команду:

```
helm uninstall fluent-bit
```

## Просмотр ингестируемых журналов

Отслеживаемые журналы доступны на уровне кластера, пространства имен, рабочей нагрузки и подов и могут быть просмотрены на страницах подробной информации каждой сущности.

![Журналы подов](https://dt-cdn.net/images/podlogsfromfluentbitclassic-1920-32cea17fc9.png)

Альтернативно, вы можете перейти к ![Журналы и события](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Журналы и события") **Журналы и события Classic**, где фильтрация может быть выполнена в простом или расширенном режиме.

![Журналы](https://dt-cdn.net/images/view-ingested-logs-1920-4339b9537f.png)

## Ограничения

* `GKE Autopilot` не поддерживается.
* Аннотации `fluentbit.io/parser` и `fluentbit.io/exclude` отключены по умолчанию.

## Устранение неполадок

Посетите [Устранение неполадок журналов, ингестируемых через Fluent Bit](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718) в сообществе Dynatrace, а также см. Устранение неполадок мониторинга журналов (Классические журналы).

### Проверьте, что поды Fluent Bit запущены

```
kubectl get pods -n dynatrace-fluent-bit
```

```
NAME               READY   STATUS              RESTARTS    AGE


fluent-bit-5jzlr   0/1     CrashLoopBackOff    1 (7s ago)  11s


fluent-bit-8zfr4   1/1     Running             0           38s


fluent-bit-qxjzh   1/1     Running             0           39s
```

Если поды находятся в состоянии ошибки, то файл значений helm может содержать ошибки. Проверьте журналы неработающих подов для получения подробной информации.

```
kubectl logs fluent-bit-5jzlr -n dynatrace-fluent-bit
```

### Проверьте здоровье и метрики Fluent Bit

[Метрики Fluent Bit](https://dt-url.net/nh43pqz) дают вам представление о том, как журналы собираются (`fluentbit_input_*`), фильтруются (`fluentbit_filter_*`) и отправляются в Dynatrace (`fluentbit_output_*`).

1. Найдите узел, на котором запущен под, который вы отлаживаете.

   ```
   kubectl get pod pod-with-logs -o wide -n dms
   ```

   ```
   NAME            READY   STATUS    RESTARTS   AGE   IP           NODE                       NOMINATED NODE   READINESS GATES


   pod-with-logs   1/1     Running   0          31m   10.28.2.41   some-node-782e86b8-mnoz    <none>           <none>
   ```
2. Найдите под Fluent Bit, который запускается на том же узле.

   ```
   kubectl get pods -o wide -n dynatrace-fluent-bit
   ```

   ```
   NAME               READY   STATUS    RESTARTS   AGE   IP           NODE                       NOMINATED NODE   READINESS GATES


   fluent-bit-5jzlr   1/1     Running   0          30m   10.28.3.44   some-node-782e86b8-zdb1    <none>           <none>


   fluent-bit-8zfr4   1/1     Running   0          30m   10.28.4.23   some-node-782e86b8-mkjw    <none>           <none>


   fluent-bit-qxjzh   1/1     Running   0          30m   10.28.2.42   some-node-782e86b8-mnoz    <none>           <none>
   ```
3. Настройте перенаправление порта метрик пода Fluent Bit на ваш localhost.

   ```
   kubectl port-forward fluent-bit-qxjzh 2020:2020 -n dynatrace-fluent-bit
   ```
4. Проверьте конечную точку здоровья.

   ```
   curl http://127.0.0.1:2020/api/v1/health
   ```

   ```
   ok
   ```
5. Изучите метрики.

   * Метрики `fluentbit_output_proc_*` указывают на количество журналов, которые обрабатываются
   * Метрики `fluentbit_*` дают вам более подробную информацию о том, что происходит до этого

   ```
   curl http://127.0.0.1:2020/api/v2/metrics | grep fluentbit_output_proc
   ```

   ```
   2024-06-11T07:05:37.257418778Z fluentbit_output_proc_records_total{name="http.0"} = 767


   2024-06-11T07:05:37.257418778Z fluentbit_output_proc_bytes_total{name="http.0"} = 359630
   ```
6. Когда метрики `fluentbit_output_errors_total` или `fluentbit_output_retries_failed_total` указывают на проблемы, потенциальной причиной может быть то, что вы достигли [лимитов мониторинга журналов](https://dt-url.net/vj23poy).

## Связанные темы

* Передача журналов в Dynatrace с помощью Fluent Bit (Классические журналы)