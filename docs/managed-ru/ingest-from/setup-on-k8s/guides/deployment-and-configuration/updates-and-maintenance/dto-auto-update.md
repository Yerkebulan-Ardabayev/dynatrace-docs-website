---
title: Автообновление Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update
scraped: 2026-05-12T12:09:26.245154
---

# Автообновление Dynatrace Operator

# Автообновление Dynatrace Operator

* Чтение: 2 мин
* Опубликовано 25 марта 2024 г.

Dynatrace Operator управляет развёртываемыми им компонентами и автоматически их обновляет. Чтобы добиться аналогичного эффекта для самого Dynatrace Operator, рекомендуется использовать GitOps и инструменты с открытым исходным кодом.

## Рекомендуемая настройка

* Храните конфигурацию Dynatrace Operator в репозитории Git.
* Используйте [ArgoCD](https://dt-url.net/hi037z9), чтобы развернуть конфигурацию из репозитория Git в окружение Kubernetes.
* Внедрите [Renovate](https://dt-url.net/vn237h6), чтобы автоматически обновлять репозиторий Git последними конфигурациями Dynatrace Operator.

## Автоматизированный процесс обновления

Описанный ниже процесс является прямым результатом рекомендуемой настройки и обеспечивает автоматическое поддержание Dynatrace Operator в актуальном состоянии в вашем окружении Kubernetes.

1. ArgoCD развёртывает конфигурацию из репозитория Git в окружение Kubernetes.
2. Renovate обнаруживает новый выпуск Dynatrace Operator и обновляет версию в репозитории Git.
3. ArgoCD замечает изменение в репозитории Git и соответственно обновляет Dynatrace Operator в окружении Kubernetes.

### Развёртывание с помощью ArgoCD

[Argo](https://dt-url.net/wt4379d) предлагает набор инструментов с открытым исходным кодом для развёртывания приложений Kubernetes и управления ими. ArgoCD, инструмент непрерывной поставки, используется для синхронизации конфигурации Dynatrace Operator с кластером Kubernetes.

После настройки ArgoCD в кластере создайте YAML `ApplicationSet`, в котором указаны исходный Helm chart для Dynatrace Operator, версия, которую требуется развернуть, и целевое окружение для развёртывания.

Пример ArgoCD ApplicationSet

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

Renovate автоматизирует обновление зависимостей в репозиториях Git. Интеграция Renovate в ваш процесс гарантирует, что версия Dynatrace Operator, указанная в вашем `ApplicationSet`, всегда актуальна. Используйте [руководство по Renovate](https://dt-url.net/67637gq) для инструкций по обновлению конфигураций ArgoCD.

## Связанные темы

* [Управление развёртываниями Dynatrace с помощью GitOps](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops "Как развернуть Dynatrace Operator и DynaKube с помощью GitOps.")