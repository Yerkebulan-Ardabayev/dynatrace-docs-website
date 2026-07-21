---
title: Добавление файла пользовательских свойств
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file
---

# Добавление файла пользовательских свойств

# Добавление файла пользовательских свойств

* 1 мин на чтение
* Обновлено 27 января 2026 г.

При настройке мониторинга платформы Kubernetes может понадобиться добавить файл пользовательских свойств.

Файл пользовательских свойств применяется к ActiveGate. Общие сведения о настройке ActiveGate см. в разделе [Настройка ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").

Файл пользовательских свойств можно добавить в виде значения или сослаться на него через секрет.

## Добавление файла пользовательских свойств в виде значения

Пример добавления файла пользовательских свойств в виде значения приведён ниже.

```
customProperties:



value: |



[kubernetes_monitoring]



...
```

## Ссылка на файл пользовательских свойств через секрет

1. Создать секрет со следующим содержимым.

   Секрет должен находиться в том же пространстве имён, что и Operator Dynatrace (например, `dynatrace`).

   Содержимое секрета должно быть закодировано в `base64`, иначе оно не сработает.

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: <customproperties-secret>



   namespace: dynatrace



   data:



   customProperties: <base64 encoded properties>
   ```
2. Добавить секрет в пользовательские свойства.

   ```
   customProperties:



   valueFrom: <customproperties-secret>
   ```