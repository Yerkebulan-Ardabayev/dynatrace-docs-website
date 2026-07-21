---
title: Миграция оператора Dynatrace
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-dto
---

# Миграция оператора Dynatrace

# Миграция оператора Dynatrace

* Опубликовано 02 авг. 2023 г.

Если оператор Dynatrace развёрнут в кластере Kubernetes, самый простой способ перенести мониторинг Kubernetes с Managed-кластера в SaaS-окружение, это переконфигурировать развёртывание оператора Dynatrace. Для реконфигурации оператора Dynatrace на уровне окружения нужно обновить всего одну настройку.

Предварительные условия

Перед установкой Dynatrace в кластер Kubernetes нужно убедиться, что выполнены следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который нужно мониторить.
* В мониторируемом кластере достаточно прав для выполнения команд `kubectl` или `oc`. Если роль кластера `cluster-admin` не используется, нужные права описаны в разделе [права доступа для развёртывания](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "Обзор компонентов Dynatrace, их конфигураций по умолчанию и требуемых прав доступа").

### Настройка и конфигурация кластера

* Нужно разрешить исходящий трафик (egress) от подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL окружения Dynatrace.

  + Для Dynatrace Managed можно опционально использовать URL Cluster ActiveGate.
* Для OpenShift Dedicated нужна [роль cluster-admin﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm Используйте [Helm версии 3﻿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

Список поддерживаемых [версий платформ](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы") Kubernetes/OpenShift и [дистрибутивов](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Сгенерировать токен**](/managed/upgrade/up-execute-upgrade/up-migrate-dto#generate-token "Перенос конфигурации оператора Dynatrace в SaaS.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создать новый секрет**](/managed/upgrade/up-execute-upgrade/up-migrate-dto#secret "Перенос конфигурации оператора Dynatrace в SaaS.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Обновить файл пользовательского ресурса DynaKube**](/managed/upgrade/up-execute-upgrade/up-migrate-dto#update-custom-resource "Перенос конфигурации оператора Dynatrace в SaaS.")

## Шаг 1 Сгенерировать токен

Чтобы сгенерировать токен доступа в целевом SaaS-окружении,

1. Перейдите в раздел **Access Tokens**.
2. Выберите **Generate new token**.
3. Введите имя токена.  
   Dynatrace не проверяет уникальность имён токенов. Можно создать несколько токенов с одинаковым именем. Рекомендуется давать каждому созданному токену осмысленное имя: это помогает эффективно управлять токенами и при необходимости удалять их, когда они больше не нужны.
4. Выберите шаблон **Kubernetes: Dynatrace Operator**.  
   Это автоматически добавит нужные области действия (см. [токен оператора](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#operator-token "Настройка токенов и прав доступа для мониторинга кластера Kubernetes")).
5. Выберите **Generate token**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

   Токен доступен только один раз, в момент создания. Позже посмотреть его нельзя.

Генерация токена в целевом SaaS-окружении никак не повлияет на кластер Kubernetes и на Managed-кластер.

## Шаг 2 Создать новый секрет

Чтобы создать новый секрет (`saasdynakube`), хранящий новый токен в кластере Kubernetes, замените плейсхолдеры в примере кода ниже (`saasdynakube` и `<API-TOKEN>`) на свои значения, затем выполните команду.

Kubernetes

OpenShift

```
kubectl -n dynatrace create secret generic saasdynakube --from-literal="apiToken=<API-TOKEN>"
```

```
oc -n dynatrace create secret generic saasdynakube --from-literal="apiToken=<API-TOKEN>"
```

После этого в кластере Kubernetes появится новый секрет `saasdynakube`, хранящий новый токен.

## Шаг 3 Обновить файл пользовательского ресурса DynaKube

Чтобы обновить существующий [файл пользовательского ресурса DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки оператора Dynatrace на Kubernetes.") с новым секретом,

1. Перейдите в [**Account Management**﻿](https://myaccount.dynatrace.com/), чтобы найти свой SaaS [Environment ID].
2. Чтобы начать изменение файла пользовательского ресурса `dynakube`, выполните команду ниже

   Kubernetes

   OpenShift

   ```
   kubectl edit dynakube dynakube -n dynatrace
   ```

   ```
   oc edit dynakube dynakube -n dynatrace
   ```
3. Обновите значения параметров конфигурации следующим образом, заменив плейсхолдеры (`{your-saas-environment-id}` и `saasdynakube`) на свои значения

   | Параметр | Обновлённое значение |
   | --- | --- |
   | apiUrl | `https://{your-saas-environment-id}.live.dynatrace.com/api` |
   | token | `saasdynakube` |

   После этого существующий файл пользовательского ресурса DynaKube будет обновлён и станет ссылаться на новый секрет `saasdynakube` и на SaaS-окружение.
4. Перезапустите приложения.  
   После этого OneAgent'ы будут указывать на SaaS-окружение. Поскольку существующие соединения с Managed-кластером Dynatrace больше не будут активны, рекомендуется удалить любой существующий секрет, который больше не используется для этого соединения.