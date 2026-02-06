---
title: Kubernetes Enhanced Object Visibility Preview
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/preview/enhanced-object-vis-preview
scraped: 2026-02-06T16:19:47.983316
---

# Предварительный просмотр расширенной видимости объектов Kubernetes

# Предварительный просмотр расширенной видимости объектов Kubernetes

* Последняя версия Dynatrace
* Обзор
* Обновлено 28 января 2026 г.

Завершенный предварительный просмотр

Предварительный просмотр расширенной видимости объектов Kubernetes представляет новый способ изучения сред Kubernetes в Dynatrace, предлагая более глубокий обзор, повышенную производительность и мощные возможности устранения неполадок.**Предварительная версия завершена с декабря 2025 года**.

Предварительные условия

* Среда Dynatrace SaaS на базе Grail и AppEngine.

+ Существует очень небольшое исключение для некоторых конкретных арендаторов, которые не смогут получить доступ к предварительной версии.Более подробная информация об этом будет доступна в продукте.
* [лицензия ДПС](/docs/license "About Dynatrace Platform Subscription (DPS), модель лицензирования для всех возможностей Dynatrace.") с возможностью **Мониторинг платформы Kubernetes** в вашем прейскуранте.
* [Достаточные разрешения](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-app/reference/permissions "Overview of user and tailoring permissions.") для использования ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** в вашей среде Dynatrace.
* Dynatrace версии 1.324+
* ActiveGate версии 1.323+
* Оператор Dynatrace версии 1.7.0+
* Приложение Kubernetes версии 1.33.0+.

Обзор

Настраивать

Часто задаваемые вопросы

Включив эту предварительную версию, вы получите:

* Видимость дополнительных объектов Kubernetes: Ingress, NetworkPolicies, CRD, PVC, PV, ConfigMaps и т. д.
* Доступ к определениям YAML для отладки и проверки конфигураций в режиме реального времени.
* Возможность запрашивать YAML-файлы во всех кластерах и пространствах имен с помощью языка запросов Dynatrace (DQL) для мгновенного выявления неправильных конфигураций, отсутствующих ссылок или нарушений политик в вашей среде Kubernetes.

В частности, этот предварительный просмотр открывает видимость:

* Хранилище: постоянные тома (PV), постоянные тома (PVC).
* Сеть: вход, сетевые политики.
* Пользовательские ресурсы: CRD и избранные CR.
* Дополнительная конфигурация: ConfigMaps и секреты.

+ Секреты и ConfigMaps не обрабатываются по умолчанию из-за их потенциально конфиденциального содержимого.Чтобы отслеживать эти объекты Kubernetes, вы можете вручную предоставить необходимые разрешения.Инструкции по включению ConfigMaps и Secrets см. в документе [Вкладка «Настройка»](#setup).

Эта предварительная версия также добавляет информацию о файлах YAML всех объектов Kubernetes, позволяя вам проверять конфигурации объектов непосредственно в Dynatrace.Включите **Слежение**, чтобы в течение нескольких секунд транслировать обновления этих конфигураций в веб-интерфейс, что позволит быстро проверить последние изменения.Размер YAML в настоящее время ограничен 32 КБ, и мы автоматически удаляем менее важные поля (например, аннотации `/metadata/managedFields` и `kubectl.kubernetes.io/last-applied-configuration`).

Эти дополнения доступны после подписки на дополнительной вкладке **Explorer (предварительная версия)** в ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.

![Улучшен предварительный просмотр видимости объектов в приложении Kubernetes.](https://dt-cdn.net/images/k8s-enhanced-object-visibility-preview-1920-7aa7863ffb.png)

Открывается множество дополнительных вариантов использования, позволяя пользователям запрашивать все файлы YAML также через DQL.Блокнот с различными примерами вы можете найти в нашем [сообщество»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132).

Чтобы принять эту предварительную версию, перейдите в раздел **Настройки** > **Облако и виртуализация** > ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**. Этот параметр доступен в пределах вашего клиента или в пределах отслеживаемого кластера Kubernetes.

Мы рекомендуем начать с включения предварительной версии только для одного кластера Kubernetes, поскольку эта новая функция может увеличить нагрузку на ActiveGate, контролирующий этот кластер.Чтобы включить это только для одного кластера, перейдите в настройки выбранного кластера в ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** и выберите > **Настройки подключения** в правом верхнем углу страницы сведений о кластере.

![Включить улучшенную видимость объектов Kubernetes](https://dt-cdn.net/images/k8s-enable-public-preview-7e45dfe3d5.gif)

Если вы установили жесткие ограничения ресурсов (ограничения процессора и памяти) на ActiveGate, контролирующем этот кластер, это может привести к перебоям в вашем мониторинге.Вы можете легко исправить это, увеличив настроенные ограничения или временно удалив их, чтобы найти подходящее место для новых ограничений.Хотя прием дополнительных данных можно контролировать для каждого кластера, дополнительная вкладка **Проводник (Предварительная версия)** в ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** становится доступной, как только для любого кластера включена предварительная версия.

## Разблокировка ConfigMaps и секретов

Чтобы получить видимость ConfigMaps и Secrets, вам необходимо предоставить ActiveGate дополнительные разрешения, позволяющие ему получать доступ к этим объектам.По умолчанию эта функция отключена, поскольку эти объекты могут содержать конфиденциальные данные.Для секретов ActiveGate автоматически применяет маскирование данных.

Примените следующий YAML с `kubectl`, чтобы включить эти объекты:

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

## Увеличивает ли этот предварительный просмотр мой расход урона в секунду?

Предварительная версия основана на существующей ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** и соответствующей лицензии на основе [капсульные часы](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged."). Потребленные часы модуля включают в себя информацию обо всех вновь добавленных объектах Kubernetes, а это означает, что не будет никакого увеличения потребления DPS, характерного для этой предварительной версии.

## Что технически произойдет, если вы присоединитесь к этой предварительной версии?

Dynatrace начинает дополнительно вставлять объекты Kubernetes в новый Smartscape.Недавно разблокированные объекты (например, Ingress, Network Policies) будут доступны только в новом Smartscape.Это упрощает доступ к DQL, ускоряет запросы и обеспечивает доступ к YAML этих объектов.Мы продолжим записывать существующие сущности в старое хранилище.В нашем [сообщество»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132) вы также найдете блокнот, который поможет вам начать работу с объектами Kubernetes, хранящимися в новом Smartscape, с помощью DQL.В ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** новый **Explorer (предварительная версия)** автоматически использует новый Smartscape в фоновом режиме, в то время как уже существующий **Explorer** продолжает работать с данными, хранящимися в нашем старом хранилище.

## Куда будет идти этот предварительный просмотр?

**Проводник (предварительная версия)** будет постепенно улучшаться в течение следующих месяцев, пока не будет включать в себя все те же функции, что и существующий **Проводник**.Благодаря общедоступной версии этой новой функции **Explorer (предварительная версия)** заменит существующий **Explorer** для всех, и мы также планируем включить больше пользовательских ресурсов.Мы будем рады услышать [ваш отзыв»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132) о том, какие из них будут для вас наиболее важными.
В течение некоторого времени мы продолжим предлагать сущности, которые использовали бывший **Explorer**, через DQL (например, fetch dt.entity.cloud\_application).

## Какой вариант наблюдения мне нужен для этого предварительного просмотра?Нужна ли мне полная наблюдаемость?

Эта предварительная версия основана на **мониторинге платформы Kubernetes**, который включен во все [параметры наблюдения](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

## Что такое рабочие нагрузки верхнего уровня?

Рабочая нагрузка верхнего уровня — это самый верхний контролирующий владелец модуля.
Возможные типы рабочей нагрузки верхнего уровня: Deployment, ReplicaSet, StatefulSet, DaemonSet, Job, CronJob, ReplicationController, DeploymentConfig.
Список этих рабочих нагрузок можно найти в пункте меню `Top-level workloads`.

## Что я вижу в представлении `Definition (YAML)`?

При первом открытии этого представления вы видите уменьшенную версию исходного YAML, доступную через API Kubernetes.Когда вы активируете режим реального времени, вы получаете полный YAML-код, передаваемый напрямую из Kubernetes API.

Уменьшенная версия YAML также доступна в формате json через DQL в поле `k8s.object` соответствующего узла Smartscape.
Обратите внимание, что метки и аннотации не являются частью этого поля, а хранятся как `tags`.

## Как исправить отсутствующие разрешения `ClusterRole`?

Недавно добавленные типы объектов Kubernetes требуют дополнительных разрешений ActiveGate.Эти разрешения (за исключением ConfigMaps и Secrets [1](#fn-1-1-def)) предоставляются автоматически при обновлении Dynatrace Operation до [версия 1.7.0](/docs/whats-new/dynatrace-operator/dto-fix-1-7-0 "Release notes for Dynatrace Operator, version 1.7.0").Клиенты, использующие более старые версии Dynatrace Оператора или те, кто вручную перезаписал разрешения ActiveGate, могут не иметь доступа к новым конечным точкам Kubernetes.Если разрешения отсутствуют, над таблицей появляется предупреждающее сообщение (например, `Missing "ConfigMap" ClusterRole permission for cluster(s): aks-playground-dev.`):

![Как исправить отсутствующие разрешения ClusterRole?](https://dt-cdn.net/images/image-20250909-123859-2305-e1ca79056f.png)

Чтобы это исправить, [обновите своего оператора Dynatrace](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#update "Upgrade and uninstallation procedures for Dynatrace Operator") до версии 1.7.0+.

1

ConfigMaps и Secrets могут содержать конфиденциальную информацию.Таким образом, Dynatrace Оператор версии 1.7.0 по умолчанию не предоставляет разрешения этим конечным точкам.Чтобы разрешить доступ к этим объектам, следуйте инструкциям, приведенным в [Разблокировка ConfigMaps и секретов](#setup).

## Узнать больше

Погрузитесь глубже в ![Кубернетес (новый)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** со следующими ресурсами:

[### Канал обратной связи для предварительного просмотра улучшенной видимости объектов Kubernetes

Вы можете найти блокнот с различными примерами в нашем сообществе.](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-Kubernetes-Enhanced-Object-Visibility/td-p/285132)

[### Детская площадка

Протестируйте приложение в изолированной среде.](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.kubernetes)[### От 0 до полной наблюдаемости в Kubernetes менее чем за 3 минуты

Краткое видеоруководство по установке Dynatrace Оператор.](https://dt-cdn.net/resources/product/videos/k8s-0-to-full-observability.mp4)[### Сообщение в блоге: Раскройте возможности DevSecOps с помощью новой версии Kubernetes Experience для проектирования платформ](https://www.dynatrace.com/news/blog/kubernetes-platform-engineering/)