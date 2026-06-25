---
title: Флаги функций DynaKube для Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags
scraped: 2026-05-12T11:53:42.020921
---

# Флаги функций DynaKube для Dynatrace Operator

# Флаги функций DynaKube для Dynatrace Operator

* Чтение: 7 мин
* Обновлено 19 марта 2026 г.

На этой странице приведён список флагов функций, которые можно использовать для настройки Dynatrace Operator в Kubernetes. Флаги функций используются для включения или отключения отдельных функций.

## Установка флага функции

Чтобы установить флаг функции.

1. Откройте YAML-файл пользовательского ресурса DynaKube (например, `dynakube.yaml`).
2. В разделе metadata найдите или добавьте поле `annotations`.
3. В разделе `annotations` добавьте флаг функции, который нужно установить, в формате `flag: value`.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/<flag>: <value>
   ```
4. Сохраните изменения и примените обновлённый YAML-файл, выполнив `kubectl apply -f <file-name>.yaml`.

## Флаги функций

| Флаг функции | Значение по умолчанию | Тип данных | Описание | Минимальная версия Dynatrace Operator |
| --- | --- | --- | --- | --- |
| `feature.dynatrace.com/label-version-detection` | `"false"` | boolean | Включает или отключает распространение меток сборки, передавая внедрённому OneAgent информацию о метаданных сборки и версии недавно развёрнутых подов. | 0.10.0 |
| `feature.dynatrace.com/automatic-injection` | `"true"` | boolean | Отключает или включает автоматическое внедрение для пространств имён, которые отслеживаются этим DynaKube. Dynatrace Operator можно настроить на мониторинг пространств имён без внедрения в какие-либо поды, поэтому можно выбрать, какие поды отслеживать. Поды, в которые требуется внедрение, должны быть помечены аннотацией `oneagent.dynatrace.com/inject: "true"`, `metadata-enrichment.dynatrace.com/inject: "true"` или `otlp-exporter-configuration.dynatrace.com/inject: "true"` (в зависимости от того, какие функции будут использоваться). | 0.8.0 |
| `feature.dynatrace.com/no-proxy` | `""` | string | Список URL-адресов, которые следует исключить из конфигурации прокси. Применяется ко всем основным компонентам Dynatrace Operator и к следующим компонентам, которыми управляет Dynatrace Operator: OneAgent, OneAgent Log Module, ActiveGate, OpenTelemetry Collector. Используйте список имён хостов через запятую (например, `host1,host2`). Имя хоста также можно указать с помощью нотации CIDR (например, `1.2.3.0/24`). ActiveGate старше 1.335 требует нотации с подстановочным знаком (например, `1.2.3.*`). При необходимости используйте обе нотации (например, `1.2.3.0/24,1.2.3.*`). | 0.11.0 |
| `feature.dynatrace.com/injection-failure-policy` | `"silent"` | string | Политика сбоя определяет, что должно произойти при сбое внедрения OneAgent для конкретного пода в кластере Kubernetes. По умолчанию политика сбоя установлена в значение silent. Политику сбоя можно переопределить для всех внедрённых подов, которые соответствуют DynaKube.  * `silent`: если внедрение OneAgent для конкретного пода завершается сбоем, под продолжит работу без мониторинга. * `fail`: если внедрение OneAgent для конкретного пода завершается сбоем, под не запустится, а сбой внедрения будет расценен как ошибка. | 0.11.0 |
| `feature.dynatrace.com/init-container-seccomp-profile` | `"false"` | boolean | Включает или отключает добавление профиля seccomp по умолчанию к init-контейнеру Dynatrace. Профиль seccomp (secure computing mode) определяет системные вызовы, которые может выполнять процесс в initContainer. По умолчанию профиль seccomp не задан. Если включено, добавляется профиль seccomp `Runtime/default`, см. [Включение профиля seccomp для init-контейнеров Dynatrace](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp#init-container "Обзор настройки профиля seccomp для компонентов Dynatrace."). | 0.11.2 |
| `feature.dynatrace.com/activegate-updates` | `"true"` | boolean | Настраивает автоматические обновления для подов ActiveGate. | 0.3.0 |
| `feature.dynatrace.com/activegate-apparmor` | `"false"` | boolean | Задаёт для аннотации AppArmor на поде ActiveGate значение `Runtime/Default`. | 0.7.0 |
| `feature.dynatrace.com/automatic-kubernetes-api-monitoring` | `"true"` | boolean | Подключает контейнеризованный ActiveGate к локальной конечной точке Kubernetes API. | 0.6.0 |
| `feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name` | `<your-dynakube>` | string | Указывает имя, по которому кластер Kubernetes идентифицируется в Dynatrace. | 0.7.0 |
| `feature.dynatrace.com/oneagent-initial-connect-retry-ms` | `-1` | int | Настраивает тайм-аут в миллисекундах, в течение которого OneAgent для `cloudNativeFullStack` и `applicationMonitoring` пытается подключиться к серверу Dynatrace. Если первая попытка подключения неудачна, OneAgent будет ожидать указанный тайм-аут перед повторной попыткой подключения. | 0.7.0 |
| `feature.dynatrace.com/max-csi-mount-attempts` | `10` | int | Задаёт максимальное число попыток для CSI driver Dynatrace Operator смонтировать том. Если этот лимит достигнут, под запустится с фиктивным томом, что приведёт к потере данных глубокого мониторинга. | 0.9.0 |
| `feature.dynatrace.com/oneagent-privileged` | `false` | boolean | Настраивает запуск контейнера OneAgent (и Log Agent, если настроен) в привилегированном режиме. | 1.0.0 |
| `feature.dynatrace.com/max-csi-mount-timeout` | `10m` (10 minutes) | string | Задаёт максимальный тайм-аут для CSI driver Dynatrace на монтирование тома. Если этот тайм-аут превышен, под запустится с фиктивным томом и без мониторинга. | 1.5.0 |
| `feature.dynatrace.com/automatic-tls-certificate` | `"true"` | boolean | Настраивает Dynatrace Operator для управления TLS-сертификатом внутрикластерного ActiveGate и его распространения на компоненты, которые взаимодействуют с ним. Требует ActiveGate версии 1.307+. | 1.5.0 |
| `feature.dynatrace.com/node-image-pull` | `"false"` | boolean | Настраивает [функцию загрузки образа на узле](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка загрузки образа на узле"). | 1.5.0 |
| `oneagent.dynatrace.com/technologies` | `""` | string | Известная проблема Из-за известной проблемы воздержитесь от использования этого флага функции. Подробнее см. [примечания к выпуску Dynatrace Operator версии 1.5.1](/managed/whats-new/dynatrace-operator/dto-fix-1-5-1#known-issues "Примечания к выпуску Dynatrace Operator, версия 1.5.1"). Можно применить к поду приложения или к DynaKube, чтобы настроить, какие технологии модуля кода Dynatrace предоставляются. Дополнительные сведения см. в нашем [руководстве по функции загрузки образа на узле](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#configure-dynakube "Настройка загрузки образа на узле"). | 1.5.0 |

## Устаревшие флаги функций

Список флагов функций, поддержка которых была прекращена в последних версиях Dynatrace Operator.

Если **Last Dynatrace Operator version** для флага функции пройдена, флаг был официально удалён и больше не должен использоваться.

| Флаг функции | Значение по умолчанию | Тип данных | Описание | Минимальная версия Dynatrace Operator | Последняя версия Dynatrace Operator |
| --- | --- | --- | --- | --- | --- |
| `feature.dynatrace.com/oneagent-readonly-host-fs` | `"true"` | boolean | Управляет режимом только для чтения для OneAgent в конфигурациях `cloudNativeFullStack` или `hostMonitoring` с CSI driver. | 1.2.2 | 1.3.2 |
| `feature.dynatrace.com/activegate-readonly-fs` | `"true"` | boolean | Изменяет securityContext на поде ActiveGate, чтобы принудительно применить файловую систему только для чтения. | 0.6.0 | 0.15.0 |
| `feature.dynatrace.com/dynatrace-api-request-threshold` | `"15"` | string | Минимальное время в минутах между запросами от Dynatrace Operator, которое ранее было жёстко задано равным 15 минутам для снижения нагрузки на сеть. Указанный интервал отсчитывается независимо для каждого из этих типов запросов. | 0.11.0 | 1.1.1 |
| `feature.dynatrace.com/oneagent-seccomp-profile` | `""` | string | Включает или отключает добавление профиля seccomp по умолчанию к Dynatrace OneAgent. Профиль seccomp (secure computing mode) определяет системные вызовы, которые может выполнять процесс в initContainer. По умолчанию профиль seccomp не задан.  Если включено, используется пользовательский профиль seccomp, который необходимо добавить в Cluster. | 0.11.0 | 1.1.1 |
| `feature.dynatrace.com/metadata-enrichment` | `"true"` | boolean | Настраивает функцию обогащения метаданными в Dynatrace Operator. Эта функция обогащает метрики, собираемые Dynatrace OneAgent, дополнительным контекстом, таким как хост или экземпляр группы процессов, из которого были собраны метрики. | 0.8.0 | 1.1.1 |
| `feature.dynatrace.com/activegate-ignore-proxy` | `"false"` | boolean | Предотвращает распространение настройки прокси из DynaKube на под ActiveGate. | 0.6.0 | 1.3.0 |
| `feature.dynatrace.com/oneagent-ignore-proxy` | `"false"` | boolean | Предотвращает распространение настройки прокси из DynaKube на OneAgent. | 0.6.0 | 1.3.0 |
| `feature.dynatrace.com/injection-readonly-volume` | `"false"` | boolean | Настраивает тома CSI как тома только для чтения при внедрении через вебхук. | 0.12.0 | 1.6.0 |
| `feature.dynatrace.com/oneagent-max-unavailable` | `1` | int | Задаёт максимальное число недоступных подов OneAgent во время обновления, эквивалентно `UpdateStrategy.RollingUpdate.MaxUnavailable` в `DaemonSet`. | 0.6.0 | 1.10.0 |