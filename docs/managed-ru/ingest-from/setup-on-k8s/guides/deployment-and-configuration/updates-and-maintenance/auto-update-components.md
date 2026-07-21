---
title: Настройка автообновления для управляемых компонентов Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components
---

# Настройка автообновления для управляемых компонентов Dynatrace Operator

# Настройка автообновления для управляемых компонентов Dynatrace Operator

* Практическое руководство
* Чтение 2 мин
* Обновлено 01 июля 2026

Dynatrace Operator управляет развёртыванием и обновлением следующих компонентов в Kubernetes:

* OneAgent
* ActiveGate
* CodeModules
* Extension Execution Controller (EEC)
* Standalone Log Module
* SQL Extension Executor
* EdgeConnect (настраивается через Custom Resource EdgeConnect)

Настройки по умолчанию для OneAgent и ActiveGate автоматически разворачивают обновления, как только они становятся доступны. DynaKube также автоматически обновляет все поды при обнаружении обновлений. Обновление может занять до 15 минут, так как Dynatrace Operator проверяет наличие обновлений с интервалом 15 минут. Настройка кастомного `image` отключает автоматические обновления.

Окна обновления не применяются в средах Kubernetes.

## Автоматические обновления с образами из публичного реестра

Dynatrace Operator версии 1.10.0+

Dynatrace Operator может автоматически определять актуальные URI публичных образов для управляемых компонентов из окружения Dynatrace, без ручной настройки поля `image`.

Когда эта функция активна, Dynatrace Operator периодически синхронизирует ссылки на образы для каждого компонента из окружения Dynatrace и применяет их автоматически.

### Включение автоматического определения образов

1. Удалить поля `image` и `codeModulesImage` из DynaKube, если они заданы: их значения имеют приоритет над автоматически определяемыми образами для соответствующего компонента.
2. Установить аннотацию `feature.dynatrace.com/use-public-registry` в DynaKube:

   ```
   apiVersion: dynatrace.com/v1beta6



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/use-public-registry: "true"



   spec:



   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



   ...
   ```

Включение автоматически с помощью platform token

Если DynaKube использует platform token, Dynatrace Operator автоматически включает определение образов из публичного реестра. Аннотация не требуется. Можно задать `spec.publicRegistryOverride`, чтобы использовать конкретный поддерживаемый публичный реестр.

Переопределение хоста реестра

Чтобы запрашивать образы из конкретного поддерживаемого публичного реестра, нужно задать `spec.publicRegistryOverride` одним из хостов реестра, перечисленных в разделе [Поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Настройка Dynatrace Operator для использования образов из публичного реестра для себя и для управляемых компонентов. Это можно сделать вручную или через автоматическое определение из окружения Dynatrace."), например, `public.ecr.aws` для Amazon ECR Public или `registry-1.docker.io` для Docker Hub. Dynatrace Operator передаёт хост в окружение Dynatrace при определении URI образов.

### Что меняется при включении функции

* **Образы компонентов**: Dynatrace Operator определяет ссылки на образы из окружения Dynatrace для OneAgent, ActiveGate и CodeModules. Компоненты без источника образа по умолчанию (Extension Execution Controller, Standalone Log Module, SQL Extension Executor) всегда требуют кастомный образ в соответствующем поле `spec.templates`.
* **Перезапуск подов**: все поды управляемых компонентов перезапускаются при первом включении функции.
* **Внедрение в приложения**: образ init-контейнера, внедряемый в поды приложений, меняется при следующем перезапуске пода, если не используется CSI driver или используется [node image pull через ephemeral volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Справочник о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая ephemeral volumes, image pull через CSI driver и загрузку ZIP."). В обоих случаях webhook переключается с режима загрузки ZIP на режим самораспаковки с использованием образа CodeModules.

### Проверка

После включения нужно убедиться, что Dynatrace Operator определяет образы из публичного реестра:

```
kubectl get dynakube <dynakube-name> -n dynatrace -o jsonpath='{.status.activeGate.source}'
```

Значение `public-registry` подтверждает, что образ ActiveGate был определён из публичного реестра. Аналогично можно проверить `status.oneAgent.source` и `status.codeModules.source` для OneAgent и CodeModules.

## Автоматические обновления с образом из встроенного реестра Dynatrace

### Настройка автообновления OneAgent

Нужно установить целевую версию на Dynatrace Server как относительную версию, например `Latest stable version`. Dynatrace Operator будет периодически проверять наличие обновлений и распространять их в среду Kubernetes. Обновление версии OneAgent всегда перезапускает поды OneAgent.

Минимальная конфигурация DynaKube с использованием автообновления:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



cloudNativeFullStack: {}
```

Чтобы отключить автообновление, нужно задать поле `image` в DynaKube. Чтобы автообновление осталось включённым, поле нужно опустить.

```
# Автообновление включено (по умолчанию) — image не указан



spec:



oneAgent:



cloudNativeFullStack: {}



# Автообновление отключено — закреплён конкретный образ



spec:



oneAgent:



cloudNativeFullStack:



image: public.ecr.aws/dynatrace/dynatrace-oneagent:<tag>
```

Для CodeModules, пока Dynatrace Operator загружает новые образы, приложения обновляются только при перезапуске. Стоит учитывать, что автомасштабирование также внедряет самый актуальный CodeModule.

### Настройка автообновления ActiveGate

Целевая версия ActiveGate, настроенная в Dynatrace, определяет образ, используемый Dynatrace Operator. Dynatrace Operator периодически проверяет наличие обновлений и применяет их автоматически.

Минимальная конфигурация DynaKube с использованием автообновления:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



activeGate:



capabilities:



- kubernetes-monitoring
```

Чтобы отключить автообновление, нужно задать поле `image` в DynaKube. Чтобы автообновление осталось включённым, поле нужно опустить.

```
# Автообновление включено (по умолчанию) — image не указан



spec:



activeGate:



capabilities:



- kubernetes-monitoring



# Автообновление отключено — закреплён конкретный образ



spec:



activeGate:



capabilities:



- kubernetes-monitoring



image: public.ecr.aws/dynatrace/dynatrace-activegate:<tag>
```