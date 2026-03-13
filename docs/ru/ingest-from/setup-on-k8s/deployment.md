---
title: Deployment
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment
scraped: 2026-03-06T21:18:13.543710
---

# Развертывание

# Развертывание

* Latest Dynatrace
* 6-min read
* Updated on Jan 28, 2026

Dynatrace предоставляет гибкий подход к наблюдаемости Kubernetes, позволяя выбирать необходимый уровень наблюдаемости для ваших кластеров Kubernetes. На этой странице представлен обзор и пошаговое руководство по рекомендуемым вариантам для обеспечения ваших потребностей в наблюдаемости Kubernetes.
Все варианты развертывания на этой странице используют [Dynatrace Operator](https://github.com/Dynatrace/dynatrace-operator). Подробную документацию и варианты для основных дистрибутивов Kubernetes см. в разделе [Дистрибутивы](deployment/supported-technologies.md "Overview of different configurations for all major Kubernetes distributions.").

## Варианты наблюдаемости

1

Для новых пользователей среда Dynatrace предварительно настроена для приема логов, а отключение управляется через [правила приема логов](../../analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration.md "Include and exclude specific log sources already known to OneAgent for storage and analysis.").

Обзор развертывания и разрешений

В этой таблице представлен обзор всех используемых компонентов и необходимых разрешений для ваших потребностей в наблюдаемости Kubernetes. Dynatrace Operator управляет жизненным циклом всех компонентов наблюдаемости, необходимых для мониторинга Kubernetes.

1

Подробную документацию см. в разделе [Безопасность Dynatrace Operator](reference/security.md "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require").

[### Мониторинг платформы Kubernetes

Понимание и устранение неполадок в работоспособности ваших кластеров Kubernetes.](deployment/platform-observability.md "Deploy Dynatrace Operator for Kubernetes platform monitoring.")[### Мониторинг платформы Kubernetes + Наблюдаемость приложений

Обеспечение работоспособности и производительности рабочих нагрузок и микросервисов с помощью автоматической инструментации.](deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")[### Мониторинг платформы Kubernetes + Полная наблюдаемость стека

Обеспечение работоспособности и производительности рабочих нагрузок, микросервисов и инфраструктуры во всем кластере.](deployment/full-stack-observability.md "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes")

## Используйте возможности платформы Dynatrace

Платформа Dynatrace предлагает множество приложений, аналитических и автоматизационных функций для решения ваших задач по обеспечению единой наблюдаемости и безопасности. Вы можете использовать эти возможности для всех данных наблюдаемости Kubernetes, собранных любым из вышеуказанных режимов, например:

* Исследование состояния и сигналов Kubernetes в [приложении Kubernetes](../../observe/infrastructure-observability/kubernetes-app.md "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads.")
* Визуализация данных с помощью [Dashboards](../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")
* Совместная работа и пользовательский анализ с помощью [Notebooks](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* Автоматизация с помощью [Workflows](../../analyze-explore-automate/workflows.md "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* Повышение продуктивности с [Dynatrace Intelligence](../../dynatrace-intelligence.md "Get familiar with the capabilities of Dynatrace Intelligence.") и [генеративным ИИ](../../dynatrace-intelligence/copilot.md "Learn about Dynatrace Intelligence agentic and generative AI.")
* Прогнозирование тенденций и предотвращение проблем с помощью [предиктивного ИИ-анализа Dynatrace Intelligence](../../dynatrace-intelligence/reference/ai-models/forecast-analysis.md "Learn how Dynatrace Intelligence predictive AI generates forecasts.")
* И многое другое...

## Развертывание из маркетплейсов

Dynatrace поддерживает развертывание Dynatrace Operator из следующих маркетплейсов:

* [OpenShift OperatorHub](deployment/other/ocp-operator-hub.md "Deploy Dynatrace Operator on OpenShift via OperatorHub.")
* [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-brb73nceicv7u)
* [GKE Marketplace](https://console.cloud.google.com/marketplace/product/dynatrace-marketplace-prod/dynatrace-operator)
* [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/dynatrace.azure-dynatrace-operator?tab=Overview)

## Узнать больше

[### Как это работает

Ознакомьтесь с компонентами Dynatrace, которые развертываются в вашем кластере Kubernetes.](how-it-works.md "In-depth description on how the deployment on Kubernetes works.")[### Руководства

Узнайте, как настроить Dynatrace Operator для поддержки конкретных сценариев использования.](guides.md "Detailed description of installation and configuration options for specific use-cases")[### Справочник

Справочник API и параметры конфигурации для всех компонентов Dynatrace в вашем кластере Kubernetes.](reference.md "Contains a reference page with configuration options for each Dynatrace component")[### Примечания к выпуску Dynatrace Operator

См. примечания к выпуску Dynatrace Operator.](../../whats-new/dynatrace-operator.md "Release notes for Dynatrace Operator")
