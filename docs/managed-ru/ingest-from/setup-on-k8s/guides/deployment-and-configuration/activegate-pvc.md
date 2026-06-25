---
title: Настройка постоянного хранилища для ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc
scraped: 2026-05-12T11:36:21.361977
---

# Настройка постоянного хранилища для ActiveGate

# Настройка постоянного хранилища для ActiveGate

* Чтение: 1 мин
* Обновлено 4 февраля 2026 г.

Модуль ActiveGate [`log_analytics_collector`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "Узнайте, какие свойства ActiveGate можно настроить в соответствии с вашими потребностями и требованиями.") использует дисковые буферы для временного хранения данных. Чтобы избежать потери данных при перезапусках ActiveGate, рекомендуется подключить [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes) (PVC) к ActiveGate.

## Добавление PersistentVolumeClaim

В следующем фрагменте показано, как подключить PersistentVolumeClaim к ActiveGate в DynaKube.

v1beta5

v1beta4

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



activeGate:



volumeClaimTemplate:



accessModes:



- ReadWriteOnce



resources:



requests:



storage: 1Gi
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



activeGate:



persistentVolumeClaim:



accessModes:



- ReadWriteOnce



resources:



requests:



storage: 1Gi
```

В средах Kubernetes без StorageClass по умолчанию необходимо задать поле `storageClassName`. Без него под ActiveGate может не запланироваться с ошибкой: `pod has unbound immediate PersistentVolumeClaims`. Это требование также относится к развёртываниям EEC (Extensions Execution Controller).

Убедитесь, что значение `storageClassName` соответствует корректному StorageClass в вашем кластере:

```
persistentVolumeClaim:



storageClassName: fast-ssd
```

## Изменение льготного периода завершения работы ActiveGate

Когда ActiveGate выполняет корректное завершение работы (например, в сценарии уменьшения масштаба), ему необходимо сбросить буферы, чтобы избежать потери данных. В крупных средах это может занять больше времени, чем льготный период Kubernetes по умолчанию, который составляет 30 с. Чтобы этого избежать, может быть полезно задать большее значение `terminationGracePeriodSeconds` для подов ActiveGate. Изменить его можно так, как показано в следующем фрагменте.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



activeGate:



terminationGracePeriodSeconds: 120s
```