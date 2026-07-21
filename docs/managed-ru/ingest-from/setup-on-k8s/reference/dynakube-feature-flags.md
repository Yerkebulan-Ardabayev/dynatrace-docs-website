---
title: Флаги функций DynaKube для Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags
---

# Флаги функций DynaKube для Dynatrace Operator

# Флаги функций DynaKube для Dynatrace Operator

* Чтение: 7 мин
* Обновлено 15 июня 2026 г.

На этой странице приведён список флагов функций, которые можно использовать для настройки Dynatrace Operator на Kubernetes. Флаги функций служат для включения или отключения отдельных возможностей.

## Установка флага функции

Чтобы установить флаг функции.

1. Открыть файл YAML для custom resource DynaKube (например, `dynakube.yaml`).
2. В секции metadata найти или добавить поле `annotations`.
3. В `annotations` добавить нужный флаг функции в формате `flag: value`.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/<flag>: <value>
   ```
4. Сохранить изменения и применить обновлённый файл YAML, выполнив `kubectl apply -f <file-name>.yaml`.

## Флаги функций

| Флаг функции | Значение по умолчанию | Тип данных | Описание | Минимальная версия Dynatrace Operator |
| --- | --- | --- | --- | --- |
| `feature.dynatrace.com/label-version-detection` | `"false"` | boolean | Включает или отключает распространение build label, предоставляя внедрённому OneAgent информацию о метаданных сборки и версии для вновь развёрнутых Pod. | 0.10.0 |
| `feature.dynatrace.com/automatic-injection` | `"true"` | boolean | Отключает или включает автоматическое внедрение для namespace, за которыми наблюдает данный DynaKube. Dynatrace Operator можно настроить на мониторинг namespace без внедрения в какие-либо Pod, что позволяет самостоятельно выбирать, какие Pod мониторить. Pod, в которые нужно внедрение, должны быть аннотированы `oneagent.dynatrace.com/inject: "true"`, `metadata-enrichment.dynatrace.com/inject: "true"` или `otlp-exporter-configuration.dynatrace.com/inject: "true"` (в зависимости от того, какие функции будут использоваться). | 0.8.0 |
| `feature.dynatrace.com/no-proxy` | `""` | string | Список URL, исключаемых из конфигурации прокси. Применяется ко всем основным компонентам Dynatrace Operator, а также к следующим компонентам, которыми управляет Dynatrace Operator: OneAgent, OneAgent Log Module, ActiveGate, OpenTelemetry Collector. Используется список hostname, разделённых запятыми (например, `host1,host2`). Hostname также можно указывать в нотации CIDR (например, `1.2.3.0/24`). ActiveGate версий старше 1.335 требует нотацию с подстановочным знаком (например, `1.2.3.*`). При необходимости можно использовать обе нотации одновременно (например, `1.2.3.0/24,1.2.3.*`). | 0.11.0 |
| `feature.dynatrace.com/injection-failure-policy` | `"silent"` | string | Политика отказа определяет, что должно происходить, если внедрение OneAgent не удаётся для конкретного Pod в кластере Kubernetes. По умолчанию политика отказа установлена в silent. Политику отказа можно переопределить для всех Pod, внедряемых в соответствии с DynaKube.  * `silent`, если внедрение OneAgent не удалось для конкретного Pod, Pod продолжит работать без мониторинга. * `fail`, если внедрение OneAgent не удалось для конкретного Pod, Pod не запустится, а сбой внедрения будет считаться ошибкой. | 0.11.0 |
| `feature.dynatrace.com/init-container-seccomp-profile` | `"true"` | boolean | Включает или отключает добавление профиля seccomp по умолчанию в init-container Dynatrace. Профиль seccomp (secure computing mode) определяет системные вызовы, которые может выполнять процесс в initContainer. По умолчанию добавляется профиль seccomp `Runtime/default`. См. [Включение профиля seccomp для init-контейнеров Dynatrace](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp#init-container "Обзор настройки профиля seccomp для компонентов Dynatrace."). | 0.11.2 |
| `feature.dynatrace.com/activegate-updates` | `"true"` | boolean | Настраивает автоматические обновления для Pod ActiveGate. | 0.3.0 |
| `feature.dynatrace.com/activegate-apparmor` | `"false"` | boolean | Устанавливает аннотацию AppArmor для Pod ActiveGate в значение `Runtime/Default`. | 0.7.0 |
| `feature.dynatrace.com/automatic-kubernetes-api-monitoring` | `"true"` | boolean | Подключает контейнеризированный ActiveGate к локальному endpoint API Kubernetes. | 0.6.0 |
| `feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name` | `<your-dynakube>` | string | Задаёт имя, под которым кластер Kubernetes определяется в Dynatrace. | 0.7.0 |
| `feature.dynatrace.com/oneagent-initial-connect-retry-ms` | `-1` | int | Настраивает тайм-аут в миллисекундах для попытки OneAgent подключиться к серверу Dynatrace при режимах `cloudNativeFullStack` и `applicationMonitoring`. Если первоначальная попытка подключения не удалась, OneAgent подождёт указанный тайм-аут перед повторной попыткой подключения. | 0.7.0 |
| `feature.dynatrace.com/max-csi-mount-attempts` | `10` | int | Задаёт максимальное количество попыток CSI-драйвера Dynatrace Operator для монтирования тома. При достижении этого предела Pod запустится с фиктивным томом, что приведёт к потере данных глубокого мониторинга. | 0.9.0 |
| `feature.dynatrace.com/oneagent-privileged` | `"false"` | boolean | Настраивает запуск контейнера OneAgent (и Log Agent, если он настроен) в привилегированном режиме. | 1.0.0 |
| `feature.dynatrace.com/max-csi-mount-timeout` | `10m` (10 минут) | string | Задаёт максимальный тайм-аут для монтирования тома CSI-драйвером Dynatrace. При превышении этого тайм-аута под запустится с фиктивным томом и без мониторинга. | 1.5.0 |
| `feature.dynatrace.com/automatic-tls-certificate` | `"true"` | boolean | Настраивает Dynatrace Operator на управление TLS-сертификатом для ActiveGate внутри кластера и его распространение среди компонентов, взаимодействующих с ним. Требует версию ActiveGate 1.307 и выше. | 1.5.0 |
| `feature.dynatrace.com/node-image-pull` | `"false"` | boolean | Управляет тем, использует ли CSI-драйвер [node image pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Справочник о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, image pull через CSI-драйвер и загрузку ZIP.") для своего установочного Job. Начиная с Dynatrace Operator 1.10.0, этот флаг влияет только на поведение Job CSI-драйвера; webhook теперь самостоятельно выбирает init-контейнер на основе того, доступен ли образ CodeModules (через `spec.oneAgent.<mode>.codeModulesImage` либо настроенный через [публичный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Настройка Dynatrace Operator на использование образов из публичного реестра для себя и управляемых им компонентов. Это можно сделать вручную или через автоматическое разрешение из окружения Dynatrace.")). На кластере без CSI-драйвера этот флаг не имеет эффекта и вызывает предупреждение admission. | 1.5.0 |
| `feature.dynatrace.com/use-public-registry` | `"false"` | boolean | Включает автоматическое разрешение образов из публичного реестра для OneAgent, ActiveGate и CodeModules. Когда включено, Dynatrace Operator получает актуальные URI образов из endpoint публичного реестра окружения Dynatrace и применяет их автоматически. Поля `image` настраивать вручную не нужно. Чтобы запрашивать образы с конкретного хоста реестра, задать `spec.publicRegistryOverride` в DynaKube. При использовании platform token эта функция всегда активна; Dynatrace Operator игнорирует этот флаг и записывает предупреждение в лог. См. [Автоматическое разрешение образов публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Настройка Dynatrace Operator на использование образов из публичного реестра для себя и управляемых им компонентов. Это можно сделать вручную или через автоматическое разрешение из окружения Dynatrace."). | 1.10.0 |
| `oneagent.dynatrace.com/technologies` | `""` | string | Известная проблема Из-за известной проблемы, пожалуйста, воздержитесь от использования этого флага функции. Подробности см. в [примечаниях к выпуску Dynatrace Operator версии 1.5.1](/managed/whats-new/dynatrace-operator/dto-fix-1-5-1#known-issues "Примечания к выпуску Dynatrace Operator, версия 1.5.1").  Можно применить к поду приложения или к DynaKube для настройки того, какие технологии модулей кода Dynatrace предоставляются. Подробнее см. [node image pull через эфемерный том](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#storage-optimization "Справочник о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, image pull через CSI-драйвер и загрузку ZIP."). | 1.5.0 |
| `feature.dynatrace.com/enable-attributes-dt.kubernetes` | `"true"` | boolean | Добавляет устаревшие общие атрибуты `dt.kubernetes.cluster.id`, `dt.kubernetes.workload.kind` и `dt.kubernetes.workload.name` ко всем Pod, в которые внедрён OneAgent Dynatrace, при значении `"true"`.  Примечание Для обеспечения плавного перехода устаревшие атрибуты по умолчанию включены, что даёт время на обновление дашбордов и других запросов. После перехода на новые атрибуты `k8s.cluster.uid`, `k8s.workload.kind` и `k8s.workload.name` этот флаг функции можно установить в `"false"`, чтобы прекратить добавление ставших избыточными устаревших атрибутов. | 1.10.0 |

## Устаревшие флаги функций

Список флагов функций, которые были помечены как устаревшие в последних версиях Dynatrace Operator.

Если версия **Последняя версия Dynatrace Operator** для флага уже прошла, флаг официально удалён и его больше нельзя использовать.

| Флаг функции | Значение по умолчанию | Тип данных | Описание | Минимальная версия Dynatrace Operator | Последняя версия Dynatrace Operator |
| --- | --- | --- | --- | --- | --- |
| `feature.dynatrace.com/oneagent-readonly-host-fs` | `"true"` | boolean | Управляет режимом «только для чтения» для OneAgent в конфигурациях `cloudNativeFullStack` или `hostMonitoring` с CSI driver. | 1.2.2 | 1.3.2 |
| `feature.dynatrace.com/activegate-readonly-fs` | `"true"` | boolean | Изменяет securityContext для Pod ActiveGate, чтобы принудительно применить файловую систему только для чтения. | 0.6.0 | 0.15.0 |
| `feature.dynatrace.com/dynatrace-api-request-threshold` | `"15"` | string | Минимальное время в минутах между запросами от Dynatrace Operator, которое ранее было жёстко закодировано как 15 минут для снижения нагрузки на сеть. Указанный интервал отсчитывается независимо для каждого из этих типов запросов. | 0.11.0 | 1.1.1 |
| `feature.dynatrace.com/oneagent-seccomp-profile` | `""` | string | Включает или отключает добавление профиля seccomp по умолчанию к Dynatrace OneAgent. Профиль seccomp (secure computing mode) определяет системные вызовы, которые может выполнять процесс в initContainer. По умолчанию профиль seccomp не задан. Если включено, используется пользовательский профиль seccomp, который нужно добавить в Cluster. | 0.11.0 | 1.1.1 |
| `feature.dynatrace.com/metadata-enrichment` | `"true"` | boolean | Настраивает функцию metadata-enrichment в Dynatrace Operator. Эта функция обогащает метрики, собранные Dynatrace OneAgent, дополнительным контекстом, например хостом или экземпляром группы процессов, с которого были собраны метрики. | 0.8.0 | 1.1.1 |
| `feature.dynatrace.com/activegate-ignore-proxy` | `"false"` | boolean | Предотвращает распространение настройки прокси из DynaKube на Pod ActiveGate. | 0.6.0 | 1.3.0 |
| `feature.dynatrace.com/oneagent-ignore-proxy` | `"false"` | boolean | Предотвращает распространение настройки прокси из DynaKube на OneAgent. | 0.6.0 | 1.3.0 |
| `feature.dynatrace.com/injection-readonly-volume` | `"false"` | boolean | Настраивает тома CSI как доступные только для чтения при внедрении через webhook. | 0.12.0 | 1.6.0 |
| `feature.dynatrace.com/oneagent-max-unavailable` | `1` | int | Задаёт максимальное количество недоступных Pod OneAgent во время обновления, эквивалент `UpdateStrategy.RollingUpdate.MaxUnavailable` в `DaemonSet`. | 0.6.0 | 1.10.0 |
| `feature.dynatrace.com/k8s-app-enabled` | `"false"` | boolean | Ранее использовался для запуска создания схемы настроек `builtin:app-transition.kubernetes`. Схема больше не доступна в более новых средах Dynatrace, где [эксперience приложения Kubernetes](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") включается автоматически. | 0.15.0 |  |