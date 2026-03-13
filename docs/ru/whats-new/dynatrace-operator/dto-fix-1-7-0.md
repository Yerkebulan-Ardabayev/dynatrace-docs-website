---
title: Dynatrace Operator release notes version 1.7.0
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-0
scraped: 2026-03-03T21:28:05.786009
---

# Примечания к выпуску Dynatrace Operator версии 1.7.0

# Примечания к выпуску Dynatrace Operator версии 1.7.0

* Latest Dynatrace
* Release notes
* Обновлено 28 нояб. 2025

Дата выпуска: 8 сентября 2025 г.

Важное уведомление

Если вы используете Dynatrace Operator версии 1.7.0, мы рекомендуем обновиться до версии 1.7.1 для получения последних важных исправлений.

## Объявления

### Сокращение количества монтируемых томов и бинарные файлы OneAgent в режиме только для чтения

Количество монтируемых томов, необходимых для внедрения модулей кода в поды приложений, было сокращено. Кроме того, бинарные файлы OneAgent теперь монтируются в режиме только для чтения для повышения безопасности и стабильности. Подробнее см. обновлённую документацию по [мутации рабочих нагрузок](../../ingest-from/setup-on-k8s/reference/workload-mutation.md "Мутации подов приложений при включённых oneagent и/или metadata-enrichment.").

### Управление размером эфемерных томов через аннотации рабочих нагрузок

Теперь вы можете ограничивать размер эфемерных томов, подключаемых к внедрённым подам приложений, с помощью аннотаций рабочих нагрузок. Подробнее о настройке и рекомендациях по размеру см. наше [руководство по хранилищу](../../ingest-from/setup-on-k8s/reference/storage.md#application-pod-volumes "Полный обзор требований к хранилищу для различных режимов развёртывания Dynatrace Operator в средах Kubernetes").

### Расширены разрешения ClusterRole `dynatrace-kubernetes-monitoring`

По мере расширения покрытия объектов Kubernetes в Dynatrace, ActiveGate требуются дополнительные разрешения. Следующие объекты были добавлены в роль `dynatrace-kubernetes-monitoring` с разрешениями `get/list/watch`:

* `customresourcedefinitions`
* `ingresses`
* `networkpolicies`
* `endpointslices`
* `horizontalpodautoscalers`

## Новые функции и улучшения

* Необходимые области действия для OAuth-клиента EdgeConnect в [режиме provisioner](../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect-provision.md "Предоставление EdgeConnect для среды Dynatrace.") были сокращены.
  Области действия `settings:object:write` и `settings:object:read` теперь требуются только при использовании [автоматизации Kubernetes](../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/kubernetes-automation/edge-connect-kubernetes-automation-operator-supported-setup.md "Настройка EdgeConnect с поддержкой оператора для Kubernetes Connector.").

* Параметры `livenessProbe` серверного контейнера CSI-драйвера теперь можно настраивать в Helm. Добавлены следующие переключатели Helm:

  + `.csidriver.server.livenessProbe.failureThreshold`
  + `.csidriver.server.livenessProbe.initialDelaySeconds`
  + `.csidriver.server.livenessProbe.periodSeconds`
  + `.csidriver.server.livenessProbe.successThreshold`
  + `.csidriver.server.livenessProbe.timeoutSeconds`

* Теперь вы получите предупреждение, если включите `.spec.telemetryIngest` без указания `.spec.templates.openTelemetryCollector.imageRef`. Dynatrace Operator продолжит использовать образ `latest` из публичного реестра Dynatrace ECR для [OpenTelemetry collector](../../ingest-from/opentelemetry/collector.md "Узнайте о Dynatrace OTel Collector."). Однако использование тегов `latest` является антипаттерном, которого следует избегать. Указание образа станет обязательным в будущей версии.

* Dynatrace Operator использует API-токен с набором [областей действия](../../ingest-from/setup-on-k8s/deployment/tokens-permissions.md#operatorToken "Настройка токенов и разрешений для мониторинга вашего кластера Kubernetes") для взаимодействия с платформой Dynatrace. В этом выпуске внесены следующие изменения в требования к областям действия токена:

  + Область действия `entities.read` больше не требуется
  + `settings.read` и `settings.write` становятся необязательными

Необязательные области действия токена

Следующие функции ограничены, если области действия `settings.read` и `settings.write` отсутствуют в API-токене.

* Автоматический мониторинг Kubernetes API отключён. Вам нужно [включить его вручную](../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring.md#local "Мониторинг Kubernetes API с помощью Dynatrace") для вашего тенанта.
* Модуль логирования OneAgent изначально развёртывается без контекста MonitoredEntityID. Как только MonitoredEntityID станет известен, его конфигурация обновится, и модуль логирования OneAgent будет перезапущен. Вследствие этого логи могут изначально не содержать обогащение `topology:dt.entity.kubernetes_cluster`.

## Исправленные проблемы

* Секрет, содержащий автоматически сгенерированный TLS-сертификат для ActiveGate, теперь корректно удаляется, когда ActiveGate отключается или удаляется из конфигурации DynaKube.

* Настройка `.spec.templates.logMonitoring.resources` DynaKube теперь корректно применяет запросы ресурсов как к init-контейнеру, так и к основному контейнеру DaemonSet LogMonitoring.

* Добавлена валидация для проверки того, что протоколы не включены в поле `.spec.apiServer` конфигурации EdgeConnect.

* Обновления `.spec.oneAgent.(classicFullStack|cloudNativeFullStack|hostMonitoring).version` теперь корректно применяются, если `.spec.oneAgent.(classicFullStack|cloudNativeFullStack|hostMonitoring).autoUpdate` отключён.

* Dynatrace Operator теперь предоставляет замены для внешних зависимостей (бинарных файлов), используемых для CSI liveness probe и CSI node driver registrar. Благодаря этим заменам повышенная частота и оперативность обновлений сведут к минимуму уязвимости в Dynatrace Operator.

  + Замены используются по умолчанию. Вы можете отключить это поведение, установив переключатели Helm `csidriver.registrar.builtIn=false` и `csidriver.livenessprobe.builtIn=false`.
  + GKE Autopilot: эта конфигурация не поддерживается, поскольку DaemonSet CSI-драйвера больше не будет соответствовать `WorkloadAllowlists`.

  Старые бинарные файлы останутся частью образа оператора в будущих выпусках. До окончательного удаления бинарных файлов сканеры уязвимостей могут продолжать сообщать об уязвимостях.

* Исправлена проблема, при которой конечная точка OpenTelemetry collector некорректно переключалась с ActiveGate на кластер Dynatrace после удаления ActiveGate из DynaKube при включённом `.spec.telemetryIngest`.

* Исправлена проблема с дублирующимися именами портов контейнеров в DaemonSet CSI-драйвера, которая вызывала предупреждения Kubernetes.

* Исправлена проблема, при которой init-контейнер инъекции, добавляемый в поды приложений, имел неправильное значение `.spec.securityContext.runAsNonRoot` в средах OpenShift.

* Настройки прокси, определённые в `.spec.proxy`, теперь корректно применяются к модулю LogMonitoring. Кроме того, URL локального сервиса ActiveGate автоматически включается в конфигурацию `noProxy`.

* Сетевая зона, указанная в `.spec.networkZone`, теперь корректно распространяется на DaemonSet `logMonitoring`.
  Для существующих развёртываний, где уже настроены автономный `logMonitoring` и `.spec.networkZone`, поды `logMonitoring` будут перезапущены для использования правильной конфигурации сетевой зоны.

## Известные проблемы

Мы выявили следующие известные проблемы с Dynatrace Operator версии 1.7.0.

* В средах Kubernetes, особенно использующих автомасштабирование, существуют сложности с надёжным определением того, был ли узел намеренно удалён или неожиданно вышел из строя. Эта неоднозначность может приводить к большому количеству ложноположительных оповещений "Host is unavailable", влияющих на точность мониторинга и качество оповещений.

* Версии OneAgent ранее `1.317` несовместимы с настройкой сокращённого монтирования томов и бинарных файлов в режиме только для чтения, поскольку они не могут читать файлы конфигурации из записываемых расположений, используемых init-контейнером.

## Уведомления об удалении и устаревании

* Устаревший Dynatrace OneAgent Operator был удалён из каталога `operatorhub.io`. Используйте [Dynatrace Operator](../../ingest-from/setup-on-k8s/quickstart.md#deploy-dynatrace-operator "Развёртывание Dynatrace Operator в Kubernetes") вместо него.

* Репозиторий Helm, расположенный в `dynatrace/helm-charts`, устарел и перестанет получать обновления в будущем выпуске! Если вы всё ещё используете его,
  обновите URL на `dynatrace/dynatrace-operator` или перейдите на подход на основе OCI-реестра. Обновите URL репозитория Helm следующими командами:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* Следующие версии API CustomResourceDefinition DynaKube были удалены в Dynatrace Operator версии 1.7.0:

  + `v1beta1`
  + `v1beta2`
* Следующие версии API CustomResourceDefinition DynaKube помечены как устаревшие и будут удалены в указанных версиях Dynatrace Operator:

  + `v1beta3` будет удалена в Dynatrace Operator версии 1.8.0

* Чтобы предотвратить возможные сбои, мы настоятельно рекомендуем поддерживать версию API DynaKube в актуальном состоянии. После того как версия устареет и будет удалена, обновления могут стать значительно более сложными и срочными.

  + Дополнительная информация о процессе устаревания версий API DynaKube доступна в [руководстве по миграции](../../ingest-from/setup-on-k8s/guides/migration/dynakube.md#deprecation "Мигрируйте ваш DynaKube CR на более новые apiVersions в зависимости от используемой версии Operator.").

* Поле DynaKube `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).autoUpdate` устарело и больше не должно использоваться. Флаг будет удалён в будущей версии Dynatrace Operator. Выполните одно из следующих действий:

  + Зафиксируйте версию OneAgent на вашем тенанте для управления всеми подключёнными кластерами Kubernetes одновременно.
  + Используйте поле `.spec.oneagent.(cloudNativeFullStack|classicFullStack|hostMonitoring).version` для фиксации версии на уровне отдельного DynaKube.

* Сопутствующие бинарные файлы CSI, расположенные в `/usr/local/bin/csi-node-driver-registrar` и `/usr/local/bin/livenessprobe`, теперь устарели и будут удалены в будущей версии Dynatrace Operator.
* [Поддержка OpenShift 4.10 и 4.11](../../ingest-from/technology-support/support-model-and-issues.md "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы") завершилась в марте 2025 г. Вследствие этого Dynatrace Operator 1.7 больше не поддерживает эти версии.

* Событие "Mark for Termination" устарело и будет удалено в будущей версии Operator. Эта функциональность теперь избыточна, так как она была заменена событиями доступности хоста при завершении работы и перезагрузке, введёнными в OneAgent версии 1.301.

## Обновление с Dynatrace Operator версии 1.6

Начиная с этой версии, больше невозможно развернуть DynaKube с API-версиями `v1beta1` или `v1beta2`. Пожалуйста, обновите ваш DynaKube до последней версии API, `v1beta5`, перед обновлением установки Dynatrace Operator. Подробнее см. [Руководство по миграции версий API DynaKube](../../ingest-from/setup-on-k8s/guides/migration/dynakube.md "Мигрируйте ваш DynaKube CR на более новые apiVersions в зависимости от используемой версии Operator.").