---
title: Migrate from cloud-native full-stack to application monitoring mode
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/cloud-native-to-app-monitoring
scraped: 2026-03-05T21:38:59.753270
---

# Миграция с cloud-native full-stack на режим мониторинга приложений

# Миграция с cloud-native full-stack на режим мониторинга приложений

* Latest Dynatrace
* 2-min read
* Published Apr 09, 2024

Dynatrace Operator версии 1.0.0 и выше

Данное руководство описывает шаги, необходимые для миграции развёртывания Dynatrace с cloud-native full-stack на [режим мониторинга приложений](/docs/ingest-from/setup-on-k8s/how-it-works#auto "In-depth description on how the deployment on Kubernetes works.").

## Преимущества

Для мониторинга только выбранных приложений в Kubernetes мониторинг приложений предлагает гибкий подход со следующими преимуществами:

* Режим мониторинга приложений, аналогично режиму cloud native full stack, предотвращает состояния гонки, которые могут возникать при одновременном запуске подов DaemonSet OneAgent и подов мониторируемых приложений.
* Используя концепции Kubernetes, такие как admission webhooks и драйвер CSI для внедрения Code Module, режим мониторинга приложений снижает требуемые привилегии для OneAgent.

### Соображения и последствия

* При переключении на мониторинг приложений ранее развёрнутые OneAgent будут деактивированы, и глубокий мониторинг приложений прекратится. Следовательно, обязательным становится перезапуск всех подов приложений, требующих глубокого мониторинга. Перезапуск этих подов обеспечивает повторное внедрение в приложения и возобновление глубокого мониторинга.
* В режиме мониторинга приложений правила мониторинга контейнеров игнорируются. Вместо этого следует использовать [селекторы меток](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods") для точного управления внедрением OneAgent.
* Мониторинг журналов требует [дополнительной настройки](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace.").

## Переход на режим мониторинга приложений

В этом разделе содержится вся необходимая информация для выполнения миграции с cloud-native full-stack на режим мониторинга приложений.

1. Перенастройте (существующий) DynaKube для режима мониторинга приложений:

   Следующее сравнение «бок о бок» показывает, как перенастроить DynaKube CR с cloud-native full-stack на мониторинг приложений:

   Cloud-native full-stack мониторинг

   Мониторинг приложений

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   cloudNativeFullStack:



   args:



   - "--set-host-group=<host-group>"



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   hostGroup: <host-group>



   applicationMonitoring: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   Дополнительную информацию о настройке DynaKube для режима мониторинга приложений см. в [руководстве по развёртыванию](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") или [параметрах DynaKube](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-applicationmonitoring "List the available parameters for setting up Dynatrace Operator on Kubernetes."). Кроме того, вы можете загрузить [пример пользовательского ресурса DynaKube](https://dt-url.net/0w036dz) для мониторинга приложений с GitHub и адаптировать пользовательский ресурс DynaKube в соответствии с вашими требованиями.
2. Примените пользовательский ресурс DynaKube:

   Выполните приведённую ниже команду для применения пользовательского ресурса DynaKube. Webhook валидации выдаст полезные сообщения об ошибках при возникновении проблем.

   ```
   kubectl apply -f dynakube.yaml
   ```

   Это действие приведёт к удалению OneAgent в режиме cloud-native full-stack и последующему прекращению глубокого мониторинга подов приложений вскоре после этого.
3. Перезапустите рабочие нагрузки приложений:

   Незамедлительно перезапустите все рабочие нагрузки приложений, чтобы инициировать внедрение OneAgent и включить глубокий мониторинг, сводя к минимуму перерывы в мониторинге.

## Изменения в ресурсах Kubernetes

Миграция затрагивает несколько ресурсов Kubernetes, изменяя их функции или вводя новые компоненты для поддержки режима мониторинга приложений. Основные изменения включают:
