---
title: Настройка EdgeConnect
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect
scraped: 2026-03-06T21:35:56.082307
---

# Настройка EdgeConnect

# Настройка EdgeConnect

* Latest Dynatrace
* 2-min read
* Published Oct 11, 2023

EdgeConnect обеспечивает безопасное взаимодействие между приложениями, рабочими процессами и внутренними системами в среде Kubernetes. Это руководство содержит информацию о том, как развернуть и настроить EdgeConnect с использованием Dynatrace.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create EdgeConnect**](#create-edgeconnect)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create OAuth credentials secret**](#create-secret)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure EdgeConnect**](#configure-edgeconnect)[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Verify that EdgeConnect is up**](#check-edgeconnect)

## Шаг 1. Создание EdgeConnect

Чтобы создать EdgeConnect, следуйте инструкциям в разделе [Create a new EdgeConnect configuration](../../../../edgeconnect.md#createconfiguration "Use EdgeConnect to control how your apps and workflows interact with your internal systems.").

## Шаг 2. Создание секрета учётных данных OAuth

1. Создайте секрет для хранения учётных данных OAuth. Значения идентификатора клиента OAuth и секрета необходимо получить из конфигурации EdgeConnect, созданной на шаге [Create EdgeConnect](#create-edgeconnect).

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: edgeconnect-oauth



   namespace: dynatrace



   data:



   oauth-client-id: <base64 encoded client id>



   oauth-client-secret: <base64 encoded client secret>
   ```
2. Примените секрет.

   ```
   kubectl apply -f edgeconnect-oauth-secret.yaml
   ```

## Шаг 3. Настройка EdgeConnect

1. Перед применением конфигурации убедитесь, что у вас есть все необходимые сведения. Поля конфигурации см. в разделе [EdgeConnect parameters for Dynatrace Operator](../../../reference/edgeconnect-parameters.md "List of configuration parameters for EdgeConnect.").
2. Создайте файл пользовательского ресурса EdgeConnect. Убедитесь, что значение `metadata.name` совпадает с именем, использованным при создании конфигурации EdgeConnect на шаге 1.

   ```
   apiVersion: dynatrace.com/v1alpha2



   kind: EdgeConnect



   metadata:



   name: sample-edge-connect-name



   namespace: dynatrace



   spec:



   apiServer: "<environment-id>.apps.dynatrace.com"



   replicas: 1



   oauth:



   clientSecret: edgeconnect-oauth



   endpoint: https://sso.dynatrace.com/sso/oauth2/token



   resource: urn:dtenvironment:<tenant>
   ```
3. Примените пользовательский ресурс EdgeConnect.

   ```
   kubectl apply -f edgeconnect.yaml
   ```

## Шаг 4. Проверка работоспособности EdgeConnect

После настройки EdgeConnect используйте приведённую ниже команду для проверки его статуса.

```
kubectl get edgeconnects -n dynatrace
```

Убедитесь, что статус отображает `Running`.

```
NAME          APISERVER                             STATUS    AGE



sample-edge-connect-name   <environment-id>.apps.dynatrace.com   Running   16m
```

## Связанные темы

* [Configure and deploy EdgeConnect](../../../../edgeconnect.md "Use EdgeConnect to control how your apps and workflows interact with your internal systems.")
