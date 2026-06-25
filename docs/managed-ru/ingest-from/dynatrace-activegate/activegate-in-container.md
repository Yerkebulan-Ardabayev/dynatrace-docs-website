---
title: Образ контейнера ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-in-container
scraped: 2026-05-12T11:08:17.100809
---

# Образ контейнера ActiveGate

# Образ контейнера ActiveGate

* 2-min read
* Updated on May 09, 2025

Dynatrace поддерживает запуск ActiveGate в контейнере. В качестве примера контейнерного развёртывания на этой странице описывается развёртывание контейнерного ActiveGate с использованием StatefulSet на Kubernetes/OpenShift.

## Предварительные требования

1. [Создайте токен доступа с областью `InstallerDownload`](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях.")
2. [Создайте токен аутентификации](/managed/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Защитите ActiveGate с помощью выделенных токенов.")
3. Определите конечные точки связи ActiveGate и аутентификацию. Используйте API [GET connectivity information for ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "Просмотрите информацию о подключении ActiveGate через Dynatrace API.").
4. Получите UUID пространства имён kube-system

   Выполните приведённую ниже команду и сохраните UUID из вывода для дальнейшего использования.

   Kubernetes

   OpenShift

   ```
   kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'
   ```

   ```
   oc get namespace kube-system -o jsonpath='{.metadata.uid}'
   ```

## Системные требования

Образ Dynatrace ActiveGate поддерживается на различных версиях Kubernetes и OpenShift. Полный список смотрите в разделе [Поддержка технологий — Kubernetes](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift и известные проблемы").

Образы доступны для следующих архитектур:

* x86-64
* ARM64 (AArch64)
* s390x
* PPC64le

## Реестры контейнеров

Для обеспечения бесшовной интеграции с вашим инструментарием и адаптируемости к вашим потребностям мы предлагаем образы контейнеров различными способами:

* [Встроенный реестр Dynatrace](/managed/ingest-from/setup-on-k8s/guides/container-registries#default "Управление реестрами контейнеров с Dynatrace") — по умолчанию
* [Публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использовать публичный реестр")
* [Ваш собственный частный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Хранение образов Dynatrace в частных реестрах") — Рекомендуется

Мульти-архитектурные образы контейнеров Dynatrace, обеспечивающие совместимость с различными платформами, доступны только из [публичных реестров](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использовать публичный реестр"). Встроенный реестр Dynatrace предоставляет только образы для x86-64.

## Развёртывание

Dynatrace предоставляет подписанные образы контейнеров для обеспечения подлинности и целостности, а также SBOM со списком всех включённых программных компонентов.

> _Полные YAML-манифесты развёртывания (StatefulSet) доступны в оригинальной английской документации по ссылке выше._

Краткая последовательность развёртывания (частный или публичный реестр):

1. Создайте выделенное пространство имён `dynatrace`.
2. Создайте secret с данными аутентификации (`tenant-token` и `auth-token`).
3. Создайте файл `ag-deployment-example.yaml` на основе шаблона из английской документации, заменив плейсхолдеры:

   * `CPU_ARCHITECTURE` — архитектура CPU (`amd64`, `arm64`, `s390x`, `ppcle64`)
   * `<REPOSITORY_URL>` — URL поддерживаемого реестра
   * `<IMAGE_TAG>` — тег образа
   * `<YOUR_ENVIRONMENT_ID>` — ID вашего окружения
   * `<YOUR_COMMUNICATION_ENDPOINTS>` — значение `communicationEndpoints` из API
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` — UUID пространства имён kube-system

4. Необязательно: включите AppArmor-профиль `runtime/default`.
5. Необязательно: настройте лимиты ресурсов согласно рекомендациям:

   | Количество подов | CPU | Память |
   | --- | --- | --- |
   | До 100 подов | 500 millicore | 512 MiB |
   | До 1000 подов | 1000 millicore | 1 GiB |
   | До 5000 подов | 1500 millicore | 2 GiB |
   | Более 5000 подов | более 1500 millicore | более 2 GiB |

6. Разверните ActiveGate: `kubectl apply -f ./ag-deployment-example.yaml`
7. Проверьте подключение: **Deployment Status** > **ActiveGates**.

### Дополнительная конфигурация для архитектуры PPC64le

Для завершения настройки контейнерного ActiveGate на архитектуре PPC64le необходимо:

1. Увеличить количество ядер CPU: для соответствия производительности архитектуры x86-64 количество ядер CPU следует увеличить в четыре раза.
2. Уменьшить количество потоков ActiveGate:

   * Создайте пользовательские свойства согласно описанию в разделе [Расширенная конфигурация](/managed/ingest-from/dynatrace-activegate/activegate-in-container/configuration#advanced-configuration "Узнайте, как настроить контейнерный ActiveGate.")
   * Добавьте следующие строки в `custom.properties`:

     ```
     [com.compuware.apm.webserver]



     threadpool-max-size=30



     async-worker-pool-coresize=60
     ```

## Специализированные развёртывания

* Для мониторинга Kubernetes/OpenShift выберите один из вариантов:

  + Используйте [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator на Kubernetes")
  + Разверните [ActiveGate напрямую как StatefulSet](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Установка и настройка ActiveGate в Kubernetes как StatefulSet.")

## FIPS-совместимые образы

ActiveGate версии 1.315+

Доступен выделенный FIPS-совместимый образ ActiveGate. Информацию о требованиях, ограничениях, местах получения образа и способах проверки развёртывания смотрите в разделе [FIPS-совместимость ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-fips-compliance "Узнайте о FIPS-совместимости ActiveGate.").