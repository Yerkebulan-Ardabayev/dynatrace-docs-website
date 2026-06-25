---
title: Мониторинг сервисов Kubernetes/OpenShift
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-services-kubernetes
scraped: 2026-05-12T12:07:33.553748
---

# Monitor Kubernetes/OpenShift services

# Мониторинг сервисов Kubernetes/OpenShift

* 3-min read
* Published Sep 28, 2022

Dynatrace version 1.251+

Единый аналитический вид для сервисов Kubernetes позволяет изучать определения портов и IP-адреса сервисов Kubernetes, а также предоставляет подробную информацию о наборе подов, обслуживаемых конкретным сервисом Kubernetes, включая события и журналы.

![k8s-services](https://dt-cdn.net/images/screenshot-2022-09-28-at-10-20-34-1409-0007e0fe8d.png)

k8s-services

Сервисы Kubernetes из Infrastructure Monitoring и сервисы из Applications & Microservices — это два принципиально разных понятия.

* [Сервис Kubernetes](https://dt-url.net/x3034x8) (тип сущности: `KUBERNETES_SERVICE`) — концепция, специфичная для Kubernetes. Как правило, он предоставляет доступ к набору подов на сетевом уровне. Поды могут обслуживаться несколькими сервисами Kubernetes.
* [Сервис](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.") (тип сущности: `SERVICE`) автоматически обнаруживается Dynatrace на основе свойств развёртывания и конфигурации приложения. В зависимости от технологий и конфигурации Dynatrace может обнаруживать как несколько сервисов на под, так и сервисы, охватывающие несколько подов.

## Предварительные требования

* ActiveGate version 1.251+ с включённым мониторингом Kubernetes API
* В Dynatrace перейдите на страницу настроек кластера Kubernetes и убедитесь, что параметр **Monitor Kubernetes namespaces, services, workloads, and pods** включён.

Если Dynatrace Operator не используется, необходимо также включить разрешения `list services` и `get services` для [учётной записи сервиса](https://dt-url.net/ov034vn), используемой для подключения к Kubernetes API.

## Доступ к сервисам Kubernetes

Доступ к сервисам Kubernetes в Dynatrace можно получить через:

* Страницу обзора кластера/пространства имён Kubernetes (столбец **Kubernetes services**)
* Страницу сведений о пространстве имён/нагрузке/поде Kubernetes (карточка **Kubernetes services**)

На страницах обзора сервисов/нагрузок/подов Kubernetes можно фильтровать по:

* Сервису Kubernetes
* Имени сервиса Kubernetes
* Типу сервиса Kubernetes (`ClusterIP`, `NodePort`, `LoadBalancer` и `ExternalName`)

## Типы сервисов Kubernetes

* **Cluster IP:** стабильный IP-адрес, внутренний для кластера, используемый внутри кластера.
* **Node port:** расширение типа cluster IP. Клиенты могут отправлять запросы на IP-адрес узла через один или несколько портов узла. Эти запросы направляются на cluster IP сервиса Kubernetes.

  Dynatrace предоставляет cluster IP, а также определения портов и протоколов рядом со списком обслуживаемых подов на экране сведений о сервисе Kubernetes.
* **Load balancer:** клиенты могут отправлять запросы на IP-адрес сетевого балансировщика нагрузки. Сервисы Node port и cluster IP, на которые будет перенаправлять внешний балансировщик нагрузки, создаются автоматически.

  В дополнение к cluster IP Dynatrace предоставляет внешний IP-адрес, а также определения портов и протоколов рядом со списком обслуживаемых подов на странице сведений о сервисе Kubernetes.
* **External name:** внутренние клиенты используют DNS-имя сервиса в качестве псевдонима для внешнего DNS-имени.

  Dynatrace предоставляет внешнее имя как свойство на странице сведений о сервисе Kubernetes.
* **Headless service:** можно использовать, когда стабильный IP-адрес не нужен, но требуется группировка подов.

  Dynatrace предоставляет определения портов и протоколов, а также список обслуживаемых подов для безголовых сервисов с селекторами.

## Настройка зон управления

Чтобы настроить зоны управления для сервисов Kubernetes, необходимо создать правило отслеживаемых сущностей для сервиса Kubernetes. Пример: `Kubernetes service` на **Hosts**, где `Kubernetes cluster name` равно `GKE CP KLU`.

![kubernetes-service-management-zones](https://dt-cdn.net/images/2022-12-09-08-26-56-1042-192ab170ec.png)

kubernetes-service-management-zones

Правило для сервисов Kubernetes автоматически включается при выборе **Create management zone** в контекстном меню кластера Kubernetes.

Существующие зоны управления необходимо обновить вручную, чтобы охватить сервисы Kubernetes.

## Связанные темы

* [Настройка Dynatrace на Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")