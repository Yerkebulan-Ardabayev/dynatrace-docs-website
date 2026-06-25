---
title: Обзор метрик Cloud Foundry
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/cloud-foundry-metrics
scraped: 2026-05-12T11:37:33.432161
---

# Cloud Foundry metrics overview

# Обзор метрик Cloud Foundry

* Reference
* 2-min read
* Published Apr 27, 2020

Страница обзора Cloud Foundry дополняет метрики Cloud Foundry, собираемые Dynatrace OneAgent на уровне процессов и хостов, дополнительными метаданными и метриками, получаемыми через Cloud Foundry API.

![Cloud Foundry overview page](https://dt-cdn.net/images/cf-screen-165-166-1920-78d87ab14f.png)

Страница обзора Cloud Foundry

## Виртуальные машины под управлением BOSH

Dynatrace автоматически обнаруживает метаданные виртуальных машин Cloud Foundry. Эти метаданные отображаются на странице обзора хоста для виртуальной машины, управляемой BOSH:

![Bosh-managed VMs](https://dt-cdn.net/images/download-1689-14a9ebfb79.png)

Виртуальные машины под управлением BOSH

Автоматически обнаруженные метаданные, специфичные для Cloud Foundry, можно использовать для управления крупными средами Cloud Foundry несколькими способами. Например, правила автоматической расстановки тегов позволяют группировать все сущности, принадлежащие одному BOSH-развёртыванию. Метаданные, такие как `Technology type: Diego cell` или `Technology type: BOSH`, а также `Cloud platform type: Cloud Foundry foundation`, также доступны для фильтрации списка хостов.

## Gorouters

Плитка **Gorouters** предоставляет:

* Поток трафика на основе суммарных запросов, собранных по всем Gorouters
* Обнаружение повторяющихся сбоев приложений в результате ответов `HTTP 5xx` или `HTTP 502`
* HTTP-метрики Gorouter

HTTP-метрики Gorouter также доступны на страницах экземпляров группы процессов Gorouter.

## Auctioneers

Плитка **Auctioneers** предоставляет:

* Распределение приложений и задач Auctioneer по Diego cells
* Неудачные размещения экземпляров приложений и неудачные размещения задач

## Diego cells

Плитка **Diego cells** предоставляет стандартные метрики производительности: использование памяти, CPU и дискового пространства.

## Организации, пространства, приложения

Страница обзора Cloud Foundry также включает концепции Cloud Foundry — **организации** и **пространства** для размещения приложений.
Для организации организаций, пространств и приложений Cloud Foundry рекомендуется использовать [Management zones](https://www.dynatrace.com/news/blog/organize-your-cloud-foundry-foundations-with-management-zones-beta/).
Сведения об автоматическом обнаружении этих и других тегов см. в статье [метаданные группы процессов для приложений Cloud Foundry](https://www.dynatrace.com/news/blog/define-process-group-metadata-for-cloud-foundry-applications/).

## Свойства

На странице обзора Cloud Foundry есть разворачиваемый раздел **Properties and tags** (см. выше), где отображается версия Cloud Foundry API и версия Cloud Foundry Build (соответствующая версии основы Cloud Foundry). Эти свойства получаются из конечной точки Cloud Foundry API.

## Ограничения

Если вы отслеживаете несколько основ Cloud Foundry с одинаковым BOSH deployment ID (например, `cf`), управляемых разными BOSH directors, Dynatrace объединит их в одну Cloud Foundry foundation в вашем окружении Dynatrace. Чтобы разделить их и в Dynatrace, необходимо задать разные BOSH deployment ID в YAML-файлах развёртывания.

## Связанные темы

* [Настройка Dynatrace на Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")