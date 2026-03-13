---
title: Monitor Kubernetes/OpenShift services
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-services-kubernetes
scraped: 2026-03-06T21:21:46.421691
---

# Мониторинг сервисов Kubernetes/OpenShift

# Мониторинг сервисов Kubernetes/OpenShift

* Classic
* 3 мин. чтения
* Опубликовано 28 сен. 2022 г.

Dynatrace версии 1.251+

Унифицированное представление анализа для сервисов Kubernetes позволяет изучать определения портов и IP-адреса для сервисов Kubernetes, а также предоставляет ценные сведения о наборе подов, обслуживаемых конкретным сервисом Kubernetes, включая события и журналы.

![k8s-services](https://dt-cdn.net/images/screenshot-2022-09-28-at-10-20-34-1409-0007e0fe8d.png)

Сервисы Kubernetes из Infrastructure Monitoring и сервисы из Applications & Microservices — это два принципиально разных понятия.

* [Сервис Kubernetes](https://dt-url.net/x3034x8) (тип сущности: `KUBERNETES_SERVICE`) — это концепция, специфичная для Kubernetes. Обычно он предоставляет доступ к набору подов на сетевом уровне. Поды могут обслуживаться несколькими сервисами Kubernetes.
* [Сервис](../../../application-observability/services.md "Узнайте, как отслеживать и анализировать ваши сервисы, определять и использовать атрибуты запросов и многое другое.") (тип сущности: `SERVICE`) автоматически обнаруживается Dynatrace на основе свойств развёртывания и конфигурации вашего приложения. В зависимости от технологий и конфигурации Dynatrace может обнаруживать несколько сервисов на под или сервисы, охватывающие несколько подов.

## Предварительные требования

* ActiveGate версии 1.251+ с включённым мониторингом Kubernetes API
* В Dynatrace перейдите на страницу настроек кластера Kubernetes и убедитесь, что включён параметр **Monitor Kubernetes namespaces, services, workloads, and pods**.

Если вы не используете Dynatrace Operator, вам также необходимо включить разрешения `list services` и `get services` для вашей [сервисной учётной записи](https://dt-url.net/ov034vn), используемой для подключения к Kubernetes API.

## Доступ к сервисам Kubernetes

В Dynatrace доступ к сервисам Kubernetes можно получить через:

* Страницу обзора кластера/пространства имён Kubernetes (см. столбец **Kubernetes services**)
* Страницу сведений о пространстве имён/рабочей нагрузке/поде Kubernetes (см. карточку **Kubernetes services**)

На страницах обзора сервиса/рабочей нагрузки/пода Kubernetes можно фильтровать по:

* Сервис Kubernetes
* Имя сервиса Kubernetes
* Тип сервиса Kubernetes (`ClusterIP`, `NodePort`, `LoadBalancer` и `ExternalName`)

## Типы сервисов Kubernetes

* **Cluster IP:** Стабильный IP-адрес внутри кластера, который можно использовать внутри кластера.
* **Node port:** Расширение типа cluster IP. Клиенты могут отправлять запросы на IP-адрес узла по одному или нескольким портам узла. Эти запросы маршрутизируются на cluster IP сервиса Kubernetes.

  Dynatrace предоставляет cluster IP, а также определения портов и протоколов рядом со списком обслуживаемых подов на экране сведений о сервисе Kubernetes.
* **Load balancer:** Клиенты могут отправлять запросы на IP-адрес сетевого балансировщика нагрузки. Сервисы node port и cluster IP, на которые будет маршрутизировать внешний балансировщик нагрузки, создаются автоматически.

  Помимо cluster IP, Dynatrace предоставляет внешний IP-адрес, а также определения портов и протоколов рядом со списком обслуживаемых подов на странице сведений о сервисе Kubernetes.
* **External name:** Внутренние клиенты используют DNS-имя сервиса как псевдоним для внешнего DNS-имени.

  Dynatrace предоставляет внешнее имя как свойство на странице сведений о сервисе Kubernetes.
* **Headless service:** Можно использовать, когда стабильный IP-адрес не нужен, но требуется группировка подов.

  Dynatrace предоставляет определения портов и протоколов, а также список обслуживаемых подов для headless-сервисов с селекторами.

## Настройка зон управления

Чтобы настроить зоны управления для сервисов Kubernetes, необходимо создать правило для отслеживаемой сущности типа «сервис Kubernetes». Пример: `Kubernetes service` на **Hosts**, где `Kubernetes cluster name` равно `GKE CP KLU`.

![kubernetes-service-management-zones](https://dt-cdn.net/images/2022-12-09-08-26-56-1042-192ab170ec.png)

Правило для сервисов Kubernetes автоматически включается при выборе пункта **Create management zone** в контекстном меню кластера Kubernetes.

Существующие зоны управления необходимо обновлять вручную для охвата сервисов Kubernetes.

## Связанные темы

* [Настройка Dynatrace на Kubernetes](../../../../ingest-from/setup-on-k8s.md "Способы развёртывания и настройки Dynatrace на Kubernetes")
