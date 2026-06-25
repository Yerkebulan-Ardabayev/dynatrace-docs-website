---
title: Назначения и функциональность ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/capabilities
scraped: 2026-05-12T11:08:06.373449
---

# Назначения и функциональность ActiveGate

# Назначения и функциональность ActiveGate

* 4-min read
* Updated on Apr 02, 2026

ActiveGate может использоваться для трёх различных сценариев, которые мы называем **назначениями**:

* [Маршрутизация трафика OneAgent в Dynatrace, мониторинг облачных окружений или мониторинг удалённых технологий с помощью расширений](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.")
* [Запуск синтетических мониторов из частного расположения](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGate для синтетического мониторинга внутренних и внешних ресурсов из частных синтетических расположений")
* [Установка модуля zRemote для мониторинга z/OS](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Узнайте об установке модуля zRemote для мониторинга z/OS.")

Каждое назначение поставляется с различным подмножеством функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."). Не следует смешивать модули между назначениями — такая переконфигурация не поддерживается.

## Функциональность, доступная для ActiveGate с назначением маршрутизации и мониторинга

> _Reference-таблица ниже на английском._

| Functionality | Module name | x86-64 host-based Linux/Windows | s390 host-based Linux | arm64 host-based Linux | Containerized |
| --- | --- | --- | --- | --- | --- |
| [Message Routing](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#msg_routing) | OneAgent routing | Applicable | Applicable | Applicable | Applicable |
| [Buffering and compression](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#buff_compr) | OneAgent routing | Applicable | Applicable | Applicable | Applicable |
| [Authentication](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#auth) | OneAgent routing | Applicable | Applicable | Applicable | Applicable |
| [Accessing sealed networks](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#sealed_net) | OneAgent routing | Applicable | Applicable | Applicable | Applicable |
| [Memory dumps](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#mem_dump) | Memory dumps | Applicable | Applicable | Applicable | Not applicable |
| [AWS monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#aws_mon) | AWS | Applicable | Applicable | Applicable | Not applicable |
| [Cloud Foundry monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#cf_mon) | Cloud Foundry | Applicable | Applicable | Applicable | Applicable |
| [Kubernetes/OpenShift monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#k8s_mon) | Kubernetes | Applicable | Applicable | Applicable | Applicable |
| [Azure monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#azure_mon) | Azure | Applicable | Applicable | Applicable | Applicable |
| [Extension monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#extn) | Extensions | Applicable | Not applicable | Not applicable | Not applicable |
| [Oracle database insights](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#oracle_ins) | Database insights | Applicable | Applicable | Applicable | Applicable |
| [VMware monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#vmware) | VMware | Applicable | Applicable | Applicable | Applicable |
| [Dynatrace API](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#api) | REST API | Applicable | Applicable | Applicable | Applicable |
| [Log Monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#log_mon) | Log Monitoring | Applicable | Applicable | Applicable | Applicable |
| [Metric ingestion](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#metric_ing) | HTTP Metric API | Applicable | Applicable | Applicable | Applicable |
| [OpenTelemetry metric ingestion](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#otlp_ingest) | OTLP Ingest | Applicable | Applicable | Applicable | Applicable |
| [OpenTelemetry trace ingestion](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#otlp_ingest) | OTLP Ingest | Applicable | Applicable | Applicable | Applicable |
| [Real User Monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#rum_mon) | Beacon forwarder | Applicable | Applicable | Applicable | Applicable |

## Функциональность для ActiveGate, запускающих синтетические мониторы из частного расположения

| Functionality | Module name | x86-64 host-based | s390 host-based | arm64 host-based | Containerized |
| --- | --- | --- | --- | --- | --- |
| [Execute private HTTP monitors](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose#execute-mon) | Synthetic | Applicable | Not applicable | Not applicable | Applicable |
| [Execute private browser monitors](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose#execute-mon) | Synthetic | Applicable | Not applicable | Not applicable | Applicable |

## Функциональность для ActiveGate с модулем zRemote

| Functionality | Module name | x86-64 host-based | s390 host-based | arm64 host-based | Containerized |
| --- | --- | --- | --- | --- | --- |
| [zRemote module for z/OS monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose#zos_mon) | zRemote | Applicable | Applicable | Not applicable | Not applicable |