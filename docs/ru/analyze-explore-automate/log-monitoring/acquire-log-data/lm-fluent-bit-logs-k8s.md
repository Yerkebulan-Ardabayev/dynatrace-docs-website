---
title: Stream Kubernetes logs with Fluent Bit (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/lm-fluent-bit-logs-k8s
scraped: 2026-03-05T21:35:44.907456
---

# Потоковая передача логов Kubernetes с помощью Fluent Bit (Logs Classic)

# Потоковая передача логов Kubernetes с помощью Fluent Bit (Logs Classic)

* Classic
* Руководство
* Время чтения: 5 мин
* Обновлено 8 октября 2025 г.

Log Monitoring Classic

Для новейшей версии Dynatrace см. [Потоковая передача логов Kubernetes с помощью Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Интегрируйте Fluent Bit в Kubernetes для потоковой передачи логов в Dynatrace.").

На этой странице представлены инструкции по развёртыванию и настройке Fluent Bit в вашей среде Kubernetes для сбора логов.

## Предварительные требования

* Правильно настроены [ограничения контекста безопасности (SCC)](https://dt-url.net/fb02ljw), если вы используете OpenShift.
* Требуется Helm. Используйте [Helm версии 3](https://dt-url.net/n5036j1).
* Должен быть разрешён исходящий трафик из пространства имён, в котором установлен Fluent Bit (`dynatrace-fluent-bit`), в Dynatrace.
* Для обогащения информацией о рабочих нагрузках требуется Dynatrace Operator версии 1.1.0+.

## Настройка конфигурации Fluent Bit

Следуйте пошаговому руководству для подготовки конфигурации Fluent Bit.

1. Скопируйте образец файла `values.yaml` и откройте его в предпочтительном редакторе.

   Пример логов контейнеров (values.yaml)

   ```
   openShift:



   # set to true for OpenShift



   enabled: false



   securityContext:



   capabilities:



   drop:



   - ALL



   readOnlyRootFilesystem: true



   # uncomment the line below for OpenShift



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



   # Only include logs from pods with the annotation



   #[FILTER]



   #    Name grep



   #    Match kube.*



   #    Regex $kubernetes['annotations']['logs.dynatrace.com/ingest'] ^true$



   # Only include logs from specific namespaces, remove the whole filter section to get all logs



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



   # Map data to Dynatrace log format



   Rename time timestamp



   Rename log content



   Rename kubernetes.host k8s.node.name



   Rename kubernetes.namespace_name k8s.namespace.name



   Rename kubernetes.pod_id k8s.pod.uid



   Rename kubernetes.pod_name k8s.pod.name



   Rename kubernetes.container_name k8s.container.name



   Add k8s.cluster.name ${K8S_CLUSTER_NAME}



   Add k8s.cluster.uid ${K8S_CLUSTER_UID}



   # deprecated, but still in use



   Add dt.kubernetes.cluster.name ${K8S_CLUSTER_NAME}



   Add dt.kubernetes.cluster.id ${K8S_CLUSTER_UID}



   Remove_wildcard kubernetes.



   outputs: |



   # Send data to Dynatrace log ingest API



   [OUTPUT]



   Name http



   Match kube.*



   host ${DT_INGEST_HOST}



   port 443



   tls On



   tls.verify On



   uri /api/v2/logs/ingest



   format json



   allow_duplicated_headers false



   header Authorization Api-Token ${DT_INGEST_TOKEN}



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



   #  Uncomment this to collect Fluent Bit Prometheus metrics



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
2. Получите [API-токен Dynatrace](/docs/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования API Dynatrace.") с областью действия `logs.ingest` (Ingest Logs) для переменной окружения `DT_INGEST_TOKEN`.
3. Обновите переменные окружения `K8S_CLUSTER_NAME`, `DT_INGEST_HOST` и `DT_INGEST_TOKEN` в файле `values.yaml`. Используйте то же имя кластера, которое вы настроили в Dynatrace для `K8S_CLUSTER_NAME`, и укажите конечную точку SaaS или Managed в качестве `DT_INGEST_HOST`.
4. Необязательно Адаптируйте раздел фильтров в файле `values.yaml` для нацеливания на определённые пространства имён или поды, как описано в разделе [Fluent Bit Filter](https://dt-url.net/m903n8q) для подробностей.
5. Необязательно Убедитесь, что вы удалили или замаскировали любую конфиденциальную информацию в логах.
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

Удалите Fluent Bit из вашей среды Kubernetes с помощью следующей команды:

```
helm uninstall fluent-bit
```

## Просмотр принятых логов

Контролируемые логи доступны на уровнях кластера, пространства имён, рабочей нагрузки и пода и могут быть просмотрены на страницах деталей каждой сущности.

![Логи подов](https://dt-cdn.net/images/podlogsfromfluentbitclassic-1920-32cea17fc9.png)

В качестве альтернативы вы можете перейти в ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**, где фильтрация может осуществляться в простом или расширенном режиме.

![Логи](https://dt-cdn.net/images/view-ingested-logs-1920-4339b9537f.png)

## Ограничения

* `GKE Autopilot` не поддерживается.
* Аннотации `fluentbit.io/parser` и `fluentbit.io/exclude` отключены по умолчанию.

## Устранение неполадок

Посетите раздел [Устранение неполадок логов, принятых через Fluent Bit](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718) в сообществе Dynatrace, а также см. [Устранение неполадок Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Устранение проблем, связанных с настройкой и конфигурацией Log Monitoring Classic.").

### Проверка работы подов Fluent Bit

```
kubectl get pods -n dynatrace-fluent-bit
```

```
NAME               READY   STATUS              RESTARTS    AGE



fluent-bit-5jzlr   0/1     CrashLoopBackOff    1 (7s ago)  11s



fluent-bit-8zfr4   1/1     Running             0           38s



fluent-bit-qxjzh   1/1     Running             0           39s
```

Если поды находятся в состоянии ошибки, файл значений helm может содержать ошибки. Проверьте логи неработающих подов для получения подробностей.

```
kubectl logs fluent-bit-5jzlr -n dynatrace-fluent-bit
```

### Проверка состояния и метрик Fluent Bit

[Метрики Fluent Bit](https://dt-url.net/nh43pqz) предоставляют информацию о том, как логи собираются (`fluentbit_input_*`), фильтруются (`fluentbit_filter_*`) и отправляются в Dynatrace (`fluentbit_output_*`).

1. Найдите узел, на котором работает исследуемый под.

   ```
   kubectl get pod pod-with-logs -o wide -n dms
   ```

   ```
   NAME            READY   STATUS    RESTARTS   AGE   IP           NODE                       NOMINATED NODE   READINESS GATES



   pod-with-logs   1/1     Running   0          31m   10.28.2.41   some-node-782e86b8-mnoz    <none>           <none>
   ```
2. Найдите под Fluent Bit, работающий на том же узле.

   ```
   kubectl get pods -o wide -n dynatrace-fluent-bit
   ```

   ```
   NAME               READY   STATUS    RESTARTS   AGE   IP           NODE                       NOMINATED NODE   READINESS GATES



   fluent-bit-5jzlr   1/1     Running   0          30m   10.28.3.44   some-node-782e86b8-zdb1    <none>           <none>



   fluent-bit-8zfr4   1/1     Running   0          30m   10.28.4.23   some-node-782e86b8-mkjw    <none>           <none>



   fluent-bit-qxjzh   1/1     Running   0          30m   10.28.2.42   some-node-782e86b8-mnoz    <none>           <none>
   ```
3. Настройте проброс портов метрик пода Fluent Bit на ваш localhost.

   ```
   kubectl port-forward fluent-bit-qxjzh 2020:2020 -n dynatrace-fluent-bit
   ```
4. Проверьте конечную точку состояния.

   ```
   curl http://127.0.0.1:2020/api/v1/health
   ```

   ```
   ok
   ```
5. Изучите метрики.

   * Метрики `fluentbit_output_proc_*` показывают, сколько логов принимается
   * Метрики `fluentbit_*` дают больше информации о том, что происходит до этого

   ```
   curl http://127.0.0.1:2020/api/v2/metrics | grep fluentbit_output_proc
   ```

   ```
   2024-06-11T07:05:37.257418778Z fluentbit_output_proc_records_total{name="http.0"} = 767



   2024-06-11T07:05:37.257418778Z fluentbit_output_proc_bytes_total{name="http.0"} = 359630
   ```
6. Когда метрики `fluentbit_output_errors_total` или `fluentbit_output_retries_failed_total` указывают на проблемы, возможной причиной является то, что вы достигли [лимитов мониторинга логов](https://dt-url.net/vj23poy).

## Связанные темы

* [Потоковая передача логов в Dynatrace с помощью Fluent Bit (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-with-fluent-bit "Интегрируйте Fluent Bit для потоковой передачи логов в Dynatrace.")
