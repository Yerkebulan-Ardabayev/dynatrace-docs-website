---
title: Manage Dynatrace deployments using GitOps
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops
scraped: 2026-03-06T21:18:22.287307
---

# Управление развертываниями Dynatrace с помощью GitOps

# Управление развертываниями Dynatrace с помощью GitOps

* Последняя версия Dynatrace
* Чтение: 4 мин
* Опубликовано 25 марта 2024

Многие компании сегодня внедряют GitOps для упрощения развертываний в Kubernetes, и интерес к применению этих практик к компонентам Dynatrace постоянно растет. Это руководство посвящено развертыванию Dynatrace Operator с помощью инструментов GitOps и эффективной настройке мониторинга с использованием пользовательского ресурса (CR) DynaKube в соответствии с современными стратегиями развертывания.

## Использование ArgoCD

В этом разделе рассматривается развертывание Dynatrace Operator и применение CR DynaKube с помощью [ArgoCD](https://dt-url.net/hi037z9). Кроме того, описаны параметры и советы по гибкой интеграции с ArgoCD.

Следующие три пункта описывают варианты развертывания Dynatrace, изложенные в подразделах, и их комбинации.

1. Индивидуальное [развертывание Dynatrace Operator](#deploy-dynatrace-operator) и [применение CR DynaKube](#apply-dynakube-custom-resource) через ArgoCD Applications
2. Применение [паттерна App of Apps](#applying-the-app-of-apps-pattern) в ArgoCD
3. Использование [нескольких источников](#using-multiple-sources-for-an-argocd-application-beta-feature) для ArgoCD Application (бета-функция)

Это руководство было разработано и протестировано с ArgoCD версии 2.10.3.

### Развертывание Dynatrace Operator

Следующий ArgoCD Application определяет развертывание Dynatrace Operator с использованием OCI-based Helm chart из Amazon ECR:

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



name: dynatrace-operator



namespace: argocd



spec:



project: default



destination:



server: https://kubernetes.default.svc



namespace: dynatrace



source:



repoURL: public.ecr.aws/dynatrace



chart: dynatrace-operator



targetRevision: 1.0.0



helm: {}
```

Для настройки развертывания через значения Helm обратитесь к [руководству пользователя Helm](https://argo-cd.readthedocs.io/en/stable/user-guide/helm/) в ArgoCD.

CR Application можно применить следующими способами:

* Напрямую через *kubectl*
* С помощью [паттерна App of Apps](#applying-the-app-of-apps-pattern)

#### Мультикластерные развертывания через ArgoCD ApplicationSet

Для использования CR ApplicationSet при мультикластерных развертываниях используйте приведенный выше CR Application в качестве шаблона и интегрируйте его в CR ApplicationSet согласно [официальной документации ArgoCD](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/#the-applicationset-resource).

### Применение пользовательского ресурса DynaKube

Следующий ArgoCD Application ссылается на Git-репозиторий, содержащий CR DynaKube по указанному пути к файлу:

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



name: dynakube



namespace: argocd



spec:



project: default



destination:



server: https://kubernetes.default.svc



namespace: dynatrace



source:



repoURL: <git-reopository-url>



targetRevision: <revision>



path: <path-to-dynakube-dir>
```

Замените поля источника `repoURL`, `targetRevision` и `path` на соответствующие значения перед применением CR Application одним из следующих способов:

* Напрямую через *kubectl*
* С помощью [паттерна App of Apps](#applying-the-app-of-apps-pattern)

Подробности о настройке CR DynaKube см. в документации по [режимам развертывания](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

### Применение паттерна App of Apps

[Паттерн App Of Apps](https://dt-url.net/s963lbz) в ArgoCD описывает очень распространенный подход в сообществе ArgoCD, обеспечивающий автоматическую начальную настройку кластера. В сочетании с [фазами и волнами синхронизации](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/) паттерн App of Apps обеспечивает последовательный контроль над синхронизацией Application, необходимый для развертывания Dynatrace Operator перед применением CR DynaKube [1](#fn-1-1-def).

Добавьте аннотацию `argocd.argoproj.io/sync-wave` с соответствующим значением к CR Application из приведенных выше разделов, как показано в следующем фрагменте:

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



annotations:



argocd.argoproj.io/sync-wave: "0"



name: dynatrace-operator



namespace: argocd



spec:



...



---



apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



annotations:



argocd.argoproj.io/sync-wave: "10"



name: dynakube



namespace: argocd



spec:



...
```

Оба CR Application предназначены для применения через паттерн App of Apps (который требует родительского CR Application).

1

[Создание пользовательских определений ресурсов (CRD)](https://dt-url.net/8g23lou), установленных через Helm chart, может занять несколько секунд, что может привести к сбою первоначального применения CR DynaKube. Чтобы обойти это состояние гонки, мы рекомендуем [настроить ArgoCD для использования паттерна App of Apps](https://dt-url.net/ci03l8w), изменив логику оценки состояния для Applications. В качестве альтернативы можно настроить автоматические повторные попытки синхронизации.

### Использование нескольких источников для ArgoCD Application (бета-функция)

Использование нескольких источников для Application является бета-функцией ArgoCD и может быть изменено с нарушением обратной совместимости, согласно документации ArgoCD.

[Несколько источников для Application](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/) позволяет использовать один ArgoCD Application для развертывания Dynatrace Operator и CR DynaKube.
Кроме того, эта функция позволяет использовать файлы значений Helm из Git-репозитория, отличного от самого Helm chart, что ранее не было возможно в ArgoCD.

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



name: dynatrace



namespace: argocd



spec:



project: default



destination:



server: https://kubernetes.default.svc



namespace: dynatrace



sources:



- repoURL: public.ecr.aws/dynatrace



chart: dynatrace-operator



targetRevision: 1.0.0



helm:



valueFiles:



- $values/<path-to-dynatrace-operator-values-file>



- repoURL: <git-repository-url>



targetRevision: HEAD



ref: values



- repoURL: <git-repository-url>



targetRevision: HEAD



path: <path-to-dynakube-dir>



syncPolicy:



retry: # пример конфигурации повторных попыток; подробности см. в примечании ниже



limit: 5



...



...
```

Перед применением замените все заполнители на соответствующие значения и настройте автоматические повторные попытки[2](#fn-2-2-def).

2

[Создание пользовательских определений ресурсов (CRD)](https://dt-url.net/id43ley), установленных через Helm chart, может занять несколько секунд, что может привести к сбою первоначального применения ресурса DynaKube. Для обеспечения успешного развертывания необходимо настроить повторные попытки, указав политику синхронизации.

## Автоматическое обновление Dynatrace Operator

Для настройки автоматических обновлений Dynatrace Operator см. [Автоматическое обновление Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "Enable automatic updates of Dynatrace Operator following a GitOps approach."), где описана интеграция GitOps с инструментами автоматизации зависимостей.

## Связанные темы

* [Автоматическое обновление Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "Enable automatic updates of Dynatrace Operator following a GitOps approach.")
