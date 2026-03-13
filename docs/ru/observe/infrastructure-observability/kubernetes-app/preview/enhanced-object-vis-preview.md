---
title: Kubernetes Enhanced Object Visibility Preview
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/preview/enhanced-object-vis-preview
scraped: 2026-03-06T21:26:38.879293
---

# Предварительный просмотр расширенной видимости объектов Kubernetes

# Предварительный просмотр расширенной видимости объектов Kubernetes

* Latest Dynatrace
* Объяснение
* Обновлено 28 января 2026 г.

Завершённый предварительный просмотр

Предварительный просмотр расширенной видимости объектов Kubernetes представляет новый способ исследования сред Kubernetes в Dynatrace, обеспечивая более глубокую видимость, улучшенную производительность и мощные возможности диагностики. **Предварительный просмотр завершён с декабря 2025 года**.

Предварительные требования

* Среда Dynatrace SaaS на базе Grail и AppEngine

  + Существует очень небольшое исключение для нескольких конкретных тенантов, которые не смогут получить доступ к предварительному просмотру. Дополнительная информация об этом будет доступна в продукте.
* [Лицензия DPS](../../../../license.md "О Dynatrace Platform Subscription (DPS), модели лицензирования для всех возможностей Dynatrace.") с возможностью **Kubernetes Platform Monitoring** в вашей тарифной карте
* [Достаточные разрешения](../reference/permissions.md "Обзор пользовательских разрешений и разрешений на настройку.") для использования ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** в вашей среде Dynatrace
* Dynatrace версии 1.324+
* ActiveGate версии 1.323+
* Dynatrace Operator версии 1.7.0+
* Приложение Kubernetes версии 1.33.0+

Обзор

Настройка

Часто задаваемые вопросы

Включив этот предварительный просмотр, вы получите:

* Видимость дополнительных объектов Kubernetes: Ingress, NetworkPolicies, CRD, PVC, PV, ConfigMaps и других.
* Доступ к определениям YAML для отладки и проверки конфигураций в реальном времени.
* Возможность запрашивать YAML-файлы по всем кластерам и пространствам имён с помощью Dynatrace Query Language (DQL) для мгновенного выявления неправильных конфигураций, отсутствующих ссылок или нарушений политик в вашей среде Kubernetes.

В частности, этот предварительный просмотр открывает видимость в:

* Хранилище: Persistent Volumes (PV), Persistent Volume Claims (PVC)
* Сеть: Ingress, Network Policies
* Пользовательские ресурсы: CRD и выбранные CR
* Необязательная конфигурация: ConfigMaps и Secrets

  + Secrets и ConfigMaps не загружаются по умолчанию из-за потенциально конфиденциального содержимого. Для мониторинга этих объектов Kubernetes вы можете вручную предоставить необходимые разрешения. Инструкции по включению ConfigMaps и Secrets см. на вкладке [Настройка](#setup).

Этот предварительный просмотр также добавляет возможности просмотра YAML-файлов всех объектов Kubernetes, позволяя вам инспектировать конфигурации объектов непосредственно в Dynatrace. Включите **Watch**, чтобы потоково получать обновления этих конфигураций в веб-интерфейсе в течение нескольких секунд, что позволяет быстро проверять недавние изменения. Размер YAML в настоящее время ограничен 32 КБ, и мы автоматически удаляем менее важные поля (например, `/metadata/managedFields` и аннотацию `kubectl.kubernetes.io/last-applied-configuration`).

Эти дополнения доступны после подключения на дополнительной вкладке **Explorer (Preview)** в ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

![Предварительный просмотр расширенной видимости объектов в приложении Kubernetes.](https://dt-cdn.net/images/k8s-enhanced-object-visibility-preview-1920-7aa7863ffb.png)

Множество дополнительных сценариев использования становятся доступными благодаря возможности запрашивать все YAML-файлы через DQL. Блокнот с различными примерами можно найти в нашем [сообществе](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132).

Чтобы подключиться к этому предварительному просмотру, перейдите в **Settings** > **Cloud and virtualization** > ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**. Эта настройка доступна в рамках вашего тенанта или в рамках отслеживаемого кластера Kubernetes.

Мы рекомендуем начать с включения предварительного просмотра только для одного кластера Kubernetes, так как эта новая функциональность может увеличить нагрузку на ActiveGate, мониторящий этот кластер. Чтобы включить это только для одного кластера, перейдите в настройки выбранного кластера в ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** и выберите  > **Connection settings** в правом верхнем углу страницы с деталями кластера.

![Включение расширенной видимости объектов Kubernetes](https://dt-cdn.net/images/k8s-enable-public-preview-7e45dfe3d5.gif)

Если вы установили жёсткие ограничения ресурсов (лимиты ЦП и памяти) на ActiveGate, мониторящем этот кластер, это может вызвать перебои в мониторинге. Вы можете легко исправить это, увеличив настроенные лимиты или временно удалив их, чтобы подобрать подходящие новые лимиты. Хотя загрузка дополнительных данных может контролироваться для каждого кластера отдельно, дополнительная вкладка **Explorer (Preview)** в ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** становится доступной, как только любой кластер подключён к предварительному просмотру.

## Разблокировка ConfigMaps и Secrets

Чтобы получить видимость в ConfigMaps и Secrets, вам необходимо предоставить дополнительные разрешения для ActiveGate, позволяющие ему получать доступ к этим объектам. По умолчанию эта функциональность отключена, поскольку эти объекты могут содержать конфиденциальные данные. Для Secrets ActiveGate автоматически применяет маскирование данных.

Примените следующий YAML с помощью `kubectl`, чтобы включить эти объекты:

```
apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRoleBinding



metadata:



name: dynatrace-kubernetes-monitoring-sensitive



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: ClusterRole



name: dynatrace-kubernetes-monitoring-sensitive



subjects:



- kind: ServiceAccount



name: dynatrace-kubernetes-monitoring



namespace: dynatrace



---



apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRole



metadata:



name: dynatrace-kubernetes-monitoring-sensitive



labels:



rbac.dynatrace.com/aggregate-to-monitoring: "true"



rules:



- apiGroups:



- ""



resources:



- configmaps



- secrets



verbs:



- list



- watch



- get
```

## Увеличивает ли этот предварительный просмотр потребление DPS?

Предварительный просмотр основан на существующем ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** и соответствующей лицензии на основе [pod-hours](../../../../license/capabilities/container-monitoring/kubernetes-platform-monitoring.md "Узнайте, как рассчитывается потребление возможности Dynatrace Kubernetes Platform Monitoring DPS."). Потреблённые pod-hours включают информацию обо всех вновь добавленных объектах Kubernetes, что означает отсутствие увеличения потребления DPS, связанного именно с этим предварительным просмотром.

## Что происходит технически при подключении к этому предварительному просмотру?

Dynatrace начинает дополнительно загружать объекты Kubernetes в новый Smartscape. Вновь разблокированные объекты (например, Ingress, Network Policies) будут доступны только в новом Smartscape. Это обеспечивает более удобный доступ через DQL, более быстрые запросы и доступ к YAML этих объектов. Мы продолжим записывать существующие сущности в старое хранилище. В нашем [сообществе](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132) вы также найдёте блокнот, который поможет вам начать работу с объектами Kubernetes, хранящимися в новом Smartscape, с использованием DQL. В ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** новый **Explorer (Preview)** автоматически использует новый Smartscape в фоновом режиме, в то время как существующий **Explorer** продолжает работать на данных, хранящихся в старом хранилище.

## Каковы дальнейшие планы для этого предварительного просмотра?

**Explorer (Preview)** будет постепенно улучшаться в течение следующих месяцев, пока не будет включать все те же функции, что и существующий **Explorer**. С выходом GA этой новой функциональности **Explorer (Preview)** заменит существующий **Explorer** для всех, и мы также планируем включить больше пользовательских ресурсов. Мы будем рады получить [ваши отзывы](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132) о том, какие из них наиболее важны для вас.
Мы продолжим некоторое время предоставлять сущности, которые обеспечивали работу прежнего **Explorer**, через DQL (например, fetch dt.entity.cloud\_application).

## Какой вариант наблюдаемости мне нужен для этого предварительного просмотра? Нужна ли мне полная наблюдаемость (Full-Stack)?

Этот предварительный просмотр основан на **Kubernetes platform monitoring**, который включён во все [варианты наблюдаемости](../../../../ingest-from/setup-on-k8s/deployment.md "Развертывание Dynatrace Operator в Kubernetes").

## Что такое рабочие нагрузки верхнего уровня?

Рабочая нагрузка верхнего уровня — это самый верхний управляющий владелец пода.
Возможные типы рабочих нагрузок верхнего уровня: Deployment, ReplicaSet, StatefulSet, DaemonSet, Job, CronJob, ReplicationController, DeploymentConfig.
Список этих рабочих нагрузок можно найти в пункте меню `Top-level workloads`.

## Что я вижу в представлении `Definition (YAML)`?

При первом открытии этого представления вы видите сокращённую версию оригинального YAML, доступного через Kubernetes API. При активации живого режима вы получаете полный YAML, потоково передаваемый непосредственно из Kubernetes API.

Сокращённая версия YAML также доступна в формате JSON через DQL в поле `k8s.object` соответствующего узла Smartscape.
Обратите внимание, что метки и аннотации не входят в это поле, а хранятся как `tags`.

## Как исправить отсутствующие разрешения `ClusterRole`?

Вновь добавленные типы объектов Kubernetes требуют дополнительных разрешений ActiveGate. Эти разрешения (за исключением ConfigMaps и Secrets [1](#fn-1-1-def)) автоматически предоставляются при обновлении Dynatrace Operator до [версии 1.7.0](../../../../whats-new/dynatrace-operator/dto-fix-1-7-0.md "Примечания к выпуску Dynatrace Operator, версия 1.7.0"). Клиенты, использующие более старые версии Dynatrace Operator или вручную переопределившие разрешения ActiveGate, могут не иметь доступа к новым конечным точкам Kubernetes. Если разрешения отсутствуют, над таблицей появляется предупреждающее сообщение (например, `Missing "ConfigMap" ClusterRole permission for cluster(s): aks-playground-dev.`):

![Как исправить отсутствующие разрешения ClusterRole?](https://dt-cdn.net/images/image-20250909-123859-2305-e1ca79056f.png)

Чтобы исправить это, [обновите Dynatrace Operator](../../../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator.md#update "Процедуры обновления и удаления Dynatrace Operator") до версии 1.7.0+.

1

ConfigMaps и Secrets могут содержать конфиденциальную информацию. Поэтому Dynatrace Operator версии 1.7.0 не предоставляет разрешения на доступ к этим конечным точкам по умолчанию. Чтобы включить доступ к этим объектам, следуйте инструкциям в разделе [Разблокировка ConfigMaps и Secrets](#setup).

## Дополнительные ресурсы

Углубитесь в изучение ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** с помощью следующих ресурсов:

[### Канал обратной связи по предварительному просмотру расширенной видимости объектов Kubernetes

Блокнот с различными примерами можно найти в нашем сообществе.](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132)

[### Тестовая среда

Протестируйте приложение в песочнице.](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.kubernetes)[### От 0 до полной наблюдаемости в Kubernetes менее чем за 3 минуты

Краткое видеоруководство по установке Dynatrace Operator.](https://dt-cdn.net/resources/product/videos/k8s-0-to-full-observability.mp4)[### Статья в блоге: раскройте возможности DevSecOps с новым интерфейсом Kubernetes для платформенной инженерии](https://www.dynatrace.com/news/blog/kubernetes-platform-engineering/)
