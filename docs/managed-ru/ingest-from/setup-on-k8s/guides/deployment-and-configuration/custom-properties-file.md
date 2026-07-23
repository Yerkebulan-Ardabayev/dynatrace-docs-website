---
title: Настройка ActiveGate для Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/custom-properties-file
---

# Настройка ActiveGate для Kubernetes

# Настройка ActiveGate для Kubernetes

* 1 мин чтения
* Обновлено 27 янв. 2026

В рамках начала работы с мониторингом платформы Kubernetes или запуска ActiveGate в Kubernetes в целом можно добавить файл пользовательских свойств для настройки ActiveGate. Этот файл позволяет указать [настройки конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#activegate-configuration-files "Узнайте, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."). Файл можно добавить, передав его как значение или сославшись на него из секрета.

## Добавление файла пользовательских свойств как значения

Чтобы добавить файл пользовательских свойств как значение, см. пример ниже.

```
customProperties:



value: |



[kubernetes_monitoring]



...
```

## Ссылка на файл пользовательских свойств из секрета

1. Создайте секрет со следующим содержимым.

   Секрет должен находиться в том же пространстве имён, что и Dynatrace Operator (например, `dynatrace`).

   Содержимое секрета должно быть закодировано в `base64`.

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: <customproperties-secret>



   namespace: dynatrace



   data:



   customProperties: <base64 encoded properties>
   ```
2. Добавьте секрет в пользовательские свойства.

   ```
   customProperties:



   valueFrom: <customproperties-secret>
   ```