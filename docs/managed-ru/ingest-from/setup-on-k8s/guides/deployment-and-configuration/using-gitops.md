---
title: Управление развёртываниями Dynatrace с помощью GitOps
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops
scraped: 2026-05-12T12:09:22.558351
---

# Управление развёртываниями Dynatrace с помощью GitOps

# Управление развёртываниями Dynatrace с помощью GitOps

* Чтение: 4 мин
* Опубликовано 25 марта 2024 г.

Поскольку сегодня многие компании внедряют GitOps для упрощённых развёртываний Kubernetes, растёт интерес к применению этих практик к компонентам Dynatrace. Это руководство посвящено развёртыванию Dynatrace Operator с помощью инструментов GitOps и эффективной настройке мониторинга с использованием пользовательского ресурса (CR) DynaKube, в соответствии с современными стратегиями развёртывания.

## Использование ArgoCD

В этом разделе рассматривается развёртывание Dynatrace Operator и применение CR DynaKube с помощью [ArgoCD](https://dt-url.net/hi037z9). Кроме того, в нём описаны варианты и советы по гибкой интеграции с ArgoCD.

Следующие три пункта описывают варианты развёртывания Dynatrace, изложенные в подразделах, и их комбинации.

1. По отдельности [разверните Dynatrace Operator](#deploy-dynatrace-operator) и [примените CR DynaKube](#apply-dynakube-custom-resource) через ArgoCD Applications
2. Примените [паттерн App of Apps](#applying-the-app-of-apps-pattern) ArgoCD
3. Используйте [несколько источников](#using-multiple-sources-for-an-argocd-application-beta-feature) для ArgoCD Application (бета-функция)

Это руководство было разработано и протестировано с ArgoCD версии 2.10.3.

### Развёртывание Dynatrace Operator

Следующее ArgoCD Application определяет развёртывание Dynatrace Operator с использованием Helm-чарта на основе OCI из Amazon ECR:

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

Для настройки развёртывания через значения Helm обратитесь к [руководству пользователя по Helm](https://argo-cd.readthedocs.io/en/stable/user-guide/helm/) ArgoCD.

CR Application можно применить следующими способами:

* Напрямую через *kubectl*
* Путём [применения паттерна App of Apps](#applying-the-app-of-apps-pattern)

#### Развёртывания в нескольких кластерах через ArgoCD ApplicationSet

Чтобы использовать CR ApplicationSet для развёртываний в нескольких кластерах, используйте приведённый выше CR Application в качестве шаблона и интегрируйте его в CR ApplicationSet в соответствии с [официальной документацией ArgoCD](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/#the-applicationset-resource).

### Применение пользовательского ресурса DynaKube

Следующее ArgoCD Application ссылается на репозиторий Git, содержащий CR DynaKube по указанному пути к файлу:

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

Замените поля источника `repoURL`, `targetRevision` и `path` осмысленными значениями, прежде чем применять CR Application одним из следующих способов:

* Напрямую через *kubectl*
* Путём [применения паттерна App of Apps](#applying-the-app-of-apps-pattern)

Подробнее о настройке CR DynaKube см. документацию по [режимам развёртывания](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator в Kubernetes").

### Применение паттерна App of Apps

[Паттерн App Of Apps](https://dt-url.net/s963lbz) ArgoCD описывает очень распространённый в сообществе ArgoCD подход, обеспечивающий автоматическую начальную настройку кластера. В сочетании с [фазами и волнами синхронизации](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/) паттерн App of Apps обеспечивает последовательный контроль над синхронизацией Application, необходимый для развёртывания Dynatrace Operator перед применением CR DynaKube [1](#fn-1-1-def).

Добавьте аннотацию `argocd.argoproj.io/sync-wave` с соответствующим значением к CR Application из приведённых выше разделов, как показано в следующем фрагменте:

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

[Создание определений пользовательских ресурсов (CRD)](https://dt-url.net/8g23lou), устанавливаемых через Helm-чарт, может занять несколько секунд, из-за чего первоначальное применение CR DynaKube может завершиться неудачей. Чтобы обойти данное состояние гонки, мы рекомендуем [настроить ArgoCD для использования App of Apps](https://dt-url.net/ci03l8w), изменив логику оценки работоспособности для Application. В качестве альтернативы можно настроить автоматические повторные попытки синхронизации.

### Использование нескольких источников для ArgoCD Application (бета-функция)

Несколько источников для Application являются бета-функцией ArgoCD и, согласно документации ArgoCD, могут изменяться обратно несовместимым образом.

[Несколько источников для Application](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/) позволяют использовать одно ArgoCD Application для развёртывания Dynatrace Operator и CR DynaKube.
Кроме того, эта функция позволяет брать файлы значений Helm из репозитория Git, отличного от самого Helm-чарта, что ранее было невозможно в ArgoCD.

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



retry: # sample retry configuration; for details, see footnote below



limit: 5



...



...
```

Перед применением замените все заполнители осмысленными значениями и настройте автоматические повторные попытки[2](#fn-2-2-def).

2

[Создание определений пользовательских ресурсов (CRD)](https://dt-url.net/id43ley), устанавливаемых через Helm-чарт, может занять несколько секунд, из-за чего первоначальное применение ресурса DynaKube может завершиться неудачей. Чтобы обеспечить успешное развёртывание, необходимо настроить повторные попытки, указав политику синхронизации.

## Автоматическое обновление Dynatrace Operator

О настройке автоматических обновлений Dynatrace Operator см. [Автоматическое обновление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "Включение автоматических обновлений Dynatrace Operator по подходу GitOps."), где описана интеграция GitOps с инструментами автоматизации зависимостей.

## Связанные темы

* [Автоматическое обновление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "Включение автоматических обновлений Dynatrace Operator по подходу GitOps.")