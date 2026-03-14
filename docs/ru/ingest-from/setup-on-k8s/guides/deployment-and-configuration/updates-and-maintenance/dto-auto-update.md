---
title: Автообновление для Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update
scraped: 2026-03-03T21:27:10.158831
---

# Auto-update for Dynatrace Operator

# Auto-update for Dynatrace Operator

* Latest Dynatrace
* 2-min read
* Published Mar 25, 2024

Dynatrace Operator управляет компонентами, которые он развёртывает, и автоматически обновляет их. Для достижения аналогичного эффекта для самого Dynatrace Operator рекомендуется использовать GitOps и инструменты с открытым исходным кодом.

## Рекомендуемая конфигурация

* Храните конфигурацию Dynatrace Operator в репозитории Git.
* Используйте [ArgoCDï»¿](https://dt-url.net/hi037z9) для развёртывания конфигурации из репозитория Git в среду Kubernetes.
* Внедрите [Renovateï»¿](https://dt-url.net/vn237h6) для автоматического обновления репозитория Git актуальными конфигурациями Dynatrace Operator.

## Автоматизированный рабочий процесс обновления

Описанный ниже рабочий процесс является прямым результатом рекомендуемой конфигурации и обеспечивает автоматическое поддержание актуальности Dynatrace Operator в вашей среде Kubernetes.

1. ArgoCD развёртывает конфигурацию из репозитория Git в среду Kubernetes.
2. Renovate обнаруживает новый выпуск Dynatrace Operator и обновляет версию в репозитории Git.
3. ArgoCD замечает изменение в репозитории Git и соответствующим образом обновляет Dynatrace Operator в среде Kubernetes.

### Развёртывание с помощью ArgoCD

[Argoï»¿](https://dt-url.net/wt4379d) предлагает набор инструментов с открытым исходным кодом для развёртывания и управления приложениями Kubernetes. ArgoCD — инструмент непрерывной доставки — используется для поддержания синхронизации конфигурации Dynatrace Operator с кластером Kubernetes.

После настройки ArgoCD в вашем кластере создайте `ApplicationSet` YAML, который указывает исходный Helm-чарт для Dynatrace Operator, версию для развёртывания и целевую среду.

Пример ApplicationSet для ArgoCD

```
# For exact syntax refer to the official ArgoCD documentation



apiVersion: argoproj.io/v1alpha1



kind: ApplicationSet



metadata:



name: dynatrace-operator



spec:



generators:



...



template:



...



spec:



...



source:



repoURL: https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable



chart: dynatrace-operator



targetRevision: <version>
```

### Автоматизация обновлений с помощью Renovate

Renovate автоматизирует обновление зависимостей в репозиториях Git. Интеграция Renovate в ваш рабочий процесс гарантирует, что версия Dynatrace Operator, указанная в вашем `ApplicationSet`, всегда актуальна. Используйте [руководство по Renovateï»¿](https://dt-url.net/67637gq) для получения инструкций по обновлению конфигураций ArgoCD.

## Связанные темы

* [Управление развёртываниями Dynatrace с помощью GitOps](../using-gitops.md "How to deploy Dynatrace Operator and DynaKube using GitOps.")
