---
title: Миграция Dynatrace Operator
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-dto
scraped: 2026-05-12T12:14:02.572684
---

# Миграция Dynatrace Operator

# Миграция Dynatrace Operator

* Published Aug 02, 2023

Если Dynatrace Operator развёрнут в кластере Kubernetes, наиболее простой способ миграции мониторинга Kubernetes с кластера Managed в среду SaaS — перенастройка развёртывания Dynatrace Operator. Для перенастройки Dynatrace Operator на уровне среды достаточно обновить одну конфигурацию.

Предварительные требования

Перед установкой Dynatrace на кластер Kubernetes убедитесь, что выполняются следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который необходимо отслеживать.
* У вас достаточно привилегий на отслеживаемом кластере для выполнения команд `kubectl` или `oc`.

### Настройка и конфигурация кластера

* Необходимо разрешить исходящие соединения (egress) для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL вашей среды Dynatrace.

  + Для Dynatrace Managed можно дополнительно использовать URL Cluster ActiveGate.
* Для OpenShift Dedicated требуется [роль cluster-admin](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка через Helm. Используйте [Helm версии 3](https://dt-url.net/n5036j1).

### Поддерживаемые версии

Ознакомьтесь с поддерживаемыми [версиями платформ](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") Kubernetes/OpenShift и [дистрибутивами](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Генерация токена**](/managed/upgrade/up-execute-upgrade/up-migrate-dto#generate-token "Migrate your Dynatrace Operator configuration to SaaS.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создание нового секрета**](/managed/upgrade/up-execute-upgrade/up-migrate-dto#secret "Migrate your Dynatrace Operator configuration to SaaS.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Обновление файла пользовательского ресурса DynaKube**](/managed/upgrade/up-execute-upgrade/up-migrate-dto#update-custom-resource "Migrate your Dynatrace Operator configuration to SaaS.")

## Шаг 1. Генерация токена

Для генерации токена доступа в целевой среде SaaS:

1. Перейдите в **Access Tokens**.
2. Выберите **Generate new token**.
3. Введите имя токена.  
   Dynatrace не требует уникальных имён токенов. Можно создать несколько токенов с одним именем. Обязательно указывайте понятное имя для каждого генерируемого токена — это поможет эффективно управлять токенами и при необходимости удалять устаревшие.
4. Выберите шаблон **Kubernetes: Dynatrace Operator**.  
   Это автоматически добавит необходимые области применения (см. [токен Operator](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#operator-token "Configure tokens and permissions to monitor your Kubernetes cluster")).
5. Выберите **Generate token**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

   Токен доступен только в момент создания. Просмотреть его впоследствии невозможно.

Генерация токена в целевой среде SaaS не повлияет ни на кластер Kubernetes, ни на кластер Managed.

## Шаг 2. Создание нового секрета

Для создания нового секрета (`saasdynakube`), хранящего новый токен в кластере Kubernetes, замените заполнители в приведённом примере кода (`saasdynakube` и `<API-TOKEN>`) на свои значения, затем выполните команду.

Kubernetes

OpenShift

```
kubectl -n dynatrace create secret generic saasdynakube --from-literal="apiToken=<API-TOKEN>"
```

```
oc -n dynatrace create secret generic saasdynakube --from-literal="apiToken=<API-TOKEN>"
```

После этого в кластере Kubernetes появится новый секрет `saasdynakube`, содержащий новый токен.

## Шаг 3. Обновление файла пользовательского ресурса DynaKube

Для обновления существующего [файла пользовательского ресурса DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") с новым секретом:

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/), чтобы найти [Environment ID] вашей среды SaaS.
2. Для начала изменения файла пользовательского ресурса `dynakube` выполните следующую команду:

   Kubernetes

   OpenShift

   ```
   kubectl edit dynakube dynakube -n dynatrace
   ```

   ```
   oc edit dynakube dynakube -n dynatrace
   ```
3. Обновите значения параметров конфигурации, заменив заполнители (`{your-saas-environment-id}` и `saasdynakube`) на собственные значения:

   | Параметр | Обновлённое значение |
   | --- | --- |
   | apiUrl | `https://{your-saas-environment-id}.live.dynatrace.com/api` |
   | token | `saasdynakube` |

   Существующий файл пользовательского ресурса DynaKube будет обновлён для ссылки на новый секрет `saasdynakube` и среду SaaS.
4. Перезапустите приложения.  
   OneAgent будут указывать на среду SaaS. Поскольку существующие соединения с кластером Dynatrace Managed более не будут активны, рекомендуется удалить все существующие секреты, которые больше не используются для этого соединения.