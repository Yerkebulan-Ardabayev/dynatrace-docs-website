---
title: Миграция с cloud-native full-stack на режим мониторинга приложений
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/cloud-native-to-app-monitoring
scraped: 2026-05-12T12:09:35.604051
---

# Миграция с cloud-native full-stack на режим мониторинга приложений

# Миграция с cloud-native full-stack на режим мониторинга приложений

* Чтение: 2 мин
* Опубликовано 9 апреля 2024 г.

Dynatrace Operator версии 1.0.0+

В этом руководстве описаны шаги, необходимые для миграции вашего развёртывания Dynatrace с cloud-native full-stack на [режим мониторинга приложений](/managed/ingest-from/setup-on-k8s/how-it-works#auto "Подробное описание того, как работает развёртывание в Kubernetes.").

## Преимущества

Для мониторинга только выбранных приложений в Kubernetes мониторинг приложений предлагает гибкий подход со следующими преимуществами:

* Режим мониторинга приложений, как и режим cloud-native full-stack, предотвращает состояния гонки, которые могут возникнуть, когда поды OneAgent DaemonSet и поды отслеживаемых приложений запускаются одновременно.
* Используя концепции Kubernetes, такие как admission webhooks и CSI driver для внедрения Code Module, режим мониторинга приложений снижает количество привилегий, требуемых для OneAgent.

### Особенности и последствия

* При переключении на мониторинг приложений ранее развёрнутые OneAgent будут деактивированы, а глубокий мониторинг приложений прекратится. Следовательно, перезапуск всех подов приложений, требующих глубокого мониторинга, становится обязательным. Перезапуск этих подов обеспечивает повторное внедрение в приложения, что позволяет возобновить глубокий мониторинг.
* В режиме мониторинга приложений правила мониторинга контейнеров игнорируются. Вместо этого следует использовать [селекторы меток](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Настройка мониторинга для пространств имён и подов"), чтобы точно управлять внедрением OneAgent.
* Мониторинг логов требует [дополнительной настройки](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

## Миграция на режим мониторинга приложений

В этом разделе приведена вся информация, необходимая для выполнения миграции с cloud-native full-stack на режим мониторинга приложений.

1. Перенастройте (существующий) DynaKube для режима мониторинга приложений:

   Следующее параллельное сравнение показывает, как перенастроить DynaKube CR с cloud-native full-stack на мониторинг приложений:

   Мониторинг cloud-native full-stack

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

   Дополнительную информацию о том, как настроить DynaKube для режима мониторинга приложений, см. в [руководстве по развёртыванию](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes") или в [параметрах DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-applicationmonitoring "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). Также можно скачать [образец пользовательского ресурса DynaKube](https://dt-url.net/0w036dz) для мониторинга приложений с GitHub и адаптировать пользовательский ресурс DynaKube согласно вашим требованиям.
2. Примените пользовательский ресурс DynaKube:

   Выполните команду ниже, чтобы применить пользовательский ресурс DynaKube. Валидирующий вебхук выдаст полезные сообщения об ошибках, если возникнет проблема.

   ```
   kubectl apply -f dynakube.yaml
   ```

   Это действие приведёт к удалению OneAgent в режиме cloud-native full-stack и впоследствии к прекращению глубокого мониторинга подов приложений вскоре после этого.
3. Перезапустите рабочие нагрузки приложений:

   Незамедлительно перезапустите все рабочие нагрузки приложений, чтобы запустить внедрение OneAgent и включить глубокий мониторинг, минимизируя перерывы в мониторинге.

## Изменения в ресурсах Kubernetes

Миграция затрагивает несколько ресурсов Kubernetes, изменяя их функции или вводя новые компоненты для поддержки режима мониторинга приложений. Основные изменения включают:

| Компонент | cloud-native full-stack | Мониторинг приложений |
| --- | --- | --- |
| Dynatrace OneAgent | * Развёртывается как DaemonSet * Собирает метрики хостов на узлах | * Отсутствует |
| Dynatrace Webhook Server | * Проверяет определения DynaKube * Внедряет модули кода в поды приложений, изменяя определения подов | * Проверяет определения DynaKube * Внедряет модули кода в поды приложений, изменяя определения подов |
| [Dynatrace Operator CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works#csi-driver "Подробное описание того, как работает развёртывание в Kubernetes.") | Требуется  * Развёртывается как DaemonSet * Предоставляет дисковое хранилище для OneAgent * Управляет модулями кода, используемыми для внедрения в поды, и предоставляет их, а также оптимизирует потребление хранилища | Необязательно  * Развёртывается как DaemonSet * Управляет модулями кода, используемыми для внедрения в поды, и предоставляет их, а также оптимизирует потребление хранилища |