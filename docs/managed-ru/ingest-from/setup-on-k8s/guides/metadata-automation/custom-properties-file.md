---
title: Добавление файла пользовательских свойств
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file
scraped: 2026-05-12T12:03:42.303693
---

# Добавление файла пользовательских свойств

# Добавление файла пользовательских свойств

* Чтение: 1 мин
* Обновлено 27 января 2026 г.

В рамках начала работы с мониторингом платформы Kubernetes вам может понадобиться добавить файл пользовательских свойств.

Файл пользовательских свойств можно добавить, указав его как значение или сославшись на него из секрета.

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

   Содержимое секрета должно быть закодировано в `base64`, чтобы оно работало.

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