---
title: Подготовка EdgeConnect для среды Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect-provision
scraped: 2026-03-05T21:40:06.355493
---

# Provision EdgeConnect for Dynatrace environment

# Подготовка EdgeConnect для среды Dynatrace

* Latest Dynatrace
* Чтение: 1 мин
* Опубликовано 20 декабря 2023 г.

EdgeConnect обеспечивает безопасное взаимодействие между приложениями, рабочими процессами и внутренними системами в среде Kubernetes. В этом руководстве приведены подробные инструкции по подготовке EdgeConnect для среды Dynatrace.

## 1. Создание OAuth-клиента

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Identity & access management** > **OAuth clients**.
2. Создайте OAuth-клиент со следующими областями действия (scopes).

   * `app-engine:edge-connects:connect`
   * `app-engine:edge-connects:write`
   * `app-engine:edge-connects:read`
   * `app-engine:edge-connects:delete`
   * `oauth2:clients:manage`
3. Сохраните идентификатор, секрет и URN вашей учётной записи Dynatrace.

## 2. Создание секрета с OAuth-учётными данными

1. Создайте секрет с OAuth-учётными данными.

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

## 3. Настройка EdgeConnect

1. Настройте файл пользовательского ресурса EdgeConnect со свойствами `provisioner: true` и `hostPatterns`. Для свойства `resource` используйте URN учётной записи Dynatrace, полученный ранее.

   ```
   apiVersion: dynatrace.com/v1alpha2



   kind: EdgeConnect



   metadata:



   name: sample-edge-connect-name



   namespace: dynatrace



   spec:



   apiServer: "<environment-id>.apps.dynatrace.com"



   hostPatterns:



   - '*.mycompany.org'



   oauth:



   provisioner: true



   clientSecret: edgeconnect-oauth



   endpoint: https://sso.dynatrace.com/sso/oauth2/token



   resource: urn:dtaccount:<your-account-uuid>
   ```
2. Примените пользовательский ресурс EdgeConnect.

   ```
   kubectl apply -f edgeconnect.yaml
   ```

Смена OAuth-учётных данных не отражается в развёртывании EdgeConnect немедленно. Это может привести к проблемам с аутентификацией до тех пор, пока Dynatrace Operator не выполнит согласование (reconcile) развёртывания EdgeConnect.

## Связанные темы

* [Configure and deploy EdgeConnect](../../../../edgeconnect.md "Use EdgeConnect to control how your apps and workflows interact with your internal systems.")
