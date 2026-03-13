---
title: Ownership Classic
source: https://www.dynatrace.com/docs/deliver/ownership
scraped: 2026-03-06T21:28:42.755901
---

# Владение (Classic)

# Владение (Classic)

* Classic
* Overview
* 2-min read
* Updated on Nov 07, 2023

Назначение владельцев команд отслеживаемым объектам в Dynatrace способствует эффективному сотрудничеству в рамках DevSecOps и быстрому, грамотному устранению инцидентов и деградации сервисов.

Метаданные о владении, привязанные к объектам, питают ваши рабочие процессы BizDevSecOps, обеспечивая привлечение нужных людей из команд безопасности, эксплуатации, инфраструктуры, бизнеса и разработки с нужной контекстной информацией.

Знание о владельце объекта позволяет реализовать дополнительную автоматизацию, например:

* Уведомление соответствующих команд о производственных проблемах, требующих их внимания.
* Создание заявок в системах управления ИТ-услугами (например, в Jira и ServiceNow) и назначение их нужным командам.
* Назначение уязвимостей ответственным членам команды.
* Предоставление информации всем соответствующим заинтересованным сторонам.

Вы можете [создавать информацию о владении](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") в веб-интерфейсе, через API и с помощью [Configuration as Code](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform."). Вы также можете импортировать команды владельцев из сторонних служб каталогов ([Microsoft Entra ID](/docs/analyze-explore-automate/workflows/actions/microsoft-entra-id "Set up Microsoft Entra ID Connector to automate importing teams from Microsoft Entra ID via Workflows.")) через [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflows — react to events, schedule tasks, and connect services."). Для масштабируемости и полного охвата [назначайте владение](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") в составе метаданных развёртывания. Для этих целей также можно использовать настройки и веб-интерфейсы объектов.

1. [Создавайте и поддерживайте команды владельцев](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") с уникальными идентификаторами и соответствующей контактной информацией для упрощения маршрутизации проблем. См. также [Рекомендации по владению объектами](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").

   ![Ownership teams settings page](https://dt-cdn.net/images/ownership-teams-page-2212-be3abe3c7d.png)
2. [Назначайте команды отслеживаемым объектам Dynatrace](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") через метаданные хоста, метки и аннотации Kubernetes, переменные среды и теги. См. также [Рекомендации по владению объектами](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").
3. Просматривайте информацию о владении с маршрутизационными данными на страницах деталей объектов Dynatrace.

   ![Owner of a Kubernetes workload](https://dt-cdn.net/images/ownership-k8s-workload-2213-2217e57297.png)

### Основы

* [Создание и управление командами для владения объектами](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.")
* [Назначение команд владельцев отслеживаемым объектам](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.")
* [Рекомендации по владению объектами](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage")

### Дополнительно

[Определение тегов и метаданных для хостов](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.")

[Определение собственных метаданных группы процессов](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.")

[Обзор Configuration as Code](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.")

[Коннектор Microsoft Entra ID](/docs/analyze-explore-automate/workflows/actions/microsoft-entra-id "Set up Microsoft Entra ID Connector to automate importing teams from Microsoft Entra ID via Workflows.")

### API

[Settings API (получение схемы и создание команд)](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")

[Monitored entities — Custom tags API](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")
