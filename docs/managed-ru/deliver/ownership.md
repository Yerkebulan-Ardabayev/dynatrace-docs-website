---
title: Владение сущностями
source: https://docs.dynatrace.com/managed/deliver/ownership
scraped: 2026-05-12T11:03:55.722938
---

# Ownership

# Ownership

* Overview
* 2-min read
* Updated on Nov 07, 2023

Назначение команд-владельцев для отслеживаемых сущностей в Dynatrace способствует эффективному сотрудничеству в рамках DevSecOps и быстрому, грамотному устранению инцидентов и деградации сервисов.

Метаданные о владении, прикреплённые к сущностям, поддерживают ваши рабочие процессы BizDevSecOps, обеспечивая участие правильных людей из команд безопасности, эксплуатации, инфраструктуры, бизнеса и разработки с нужной контекстной информацией.

Знание о владельце сущности открывает возможности для дополнительной автоматизации, например:

* Уведомление соответствующих команд о производственных проблемах, требующих их внимания.
* Создание тикетов в системах управления IT-сервисами (например, Jira и ServiceNow) и их назначение нужным командам.
* Назначение уязвимостей ответственным участникам команды.
* Предоставление информации всем заинтересованным сторонам.

Вы можете [создавать информацию о владении](/managed/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") в веб-интерфейсе, через API и с помощью [Configuration as Code](/managed/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform."). Для масштабируемости и полного охвата [назначайте владение](/managed/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") как часть метаданных развёртывания. Для этих целей также можно использовать веб-интерфейс настроек и сущностей.

1. [Создайте и поддерживайте команды владельцев](/managed/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") с уникальными идентификаторами и контактной информацией для упрощения маршрутизации проблем. См. также [Рекомендации по владению сущностями](/managed/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").

   ![Ownership teams settings page](https://dt-cdn.net/images/ownership-teams-page-2212-be3abe3c7d.png)

   Страница настроек команд владельцев
2. [Назначайте команды отслеживаемым сущностям Dynatrace](/managed/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") через метаданные хоста, метки и аннотации Kubernetes, переменные окружения и теги. См. также [Рекомендации по владению сущностями](/managed/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").
3. Просматривайте информацию о владении с деталями маршрутизации на страницах сведений о сущностях Dynatrace.

   ![Owner of a Kubernetes workload](https://dt-cdn.net/images/ownership-k8s-workload-2213-2217e57297.png)

   Владелец Kubernetes workload

### Основное

* [Создание и управление командами для владения сущностями](/managed/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.")
* [Назначение команд владельцев отслеживаемым сущностям](/managed/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.")
* [Рекомендации по владению сущностями](/managed/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage")

### Дополнительно

[Определение тегов и метаданных для хостов](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.")

[Определение собственных метаданных группы процессов](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.")

[Обзор Configuration as Code](/managed/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.")

### API

[Settings API (получение схемы и создание команд)](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")

[Monitored entities — Custom tags API](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")