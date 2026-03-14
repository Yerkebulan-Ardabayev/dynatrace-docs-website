---
title: Сетевой трафик
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/network
scraped: 2026-02-23T21:31:13.154982
---

# Сетевой трафик

# Сетевой трафик

* Latest Dynatrace
* Чтение: 3 мин
* Обновлено 2 января 2026 г.

Для корректной работы компонентов Dynatrace Operator в кластере Kubernetes они должны иметь возможность обмениваться данными как с кластером Dynatrace, так и с кластером Kubernetes.

Компоненты Dynatrace Operator доступны через определённые порты и обращаются к различным ресурсам внутри и за пределами кластера Kubernetes. Подробнее о ресурсах, к которым происходит обращение внутри кластера Kubernetes, см. на справочной странице [Разрешения RBAC оператора](../../../../ingest-from/setup-on-k8s/reference/security.md "На этой странице представлен обзор компонентов Dynatrace, их конфигураций по умолчанию и требуемых разрешений").

## Входящий трафик

Источник

Назначение

Порт

Примечание

kubelet

Dynatrace Operator `/healthz`

`TCP 10080`

Проверка жизнеспособности [1](#fn-1-1-def)

Сборщик метрик Prometheus (необязательно)

Dynatrace Operator `/metrics`

`TCP 8080`

Адрес метрик [2](#fn-1-2-def)

kubelet

Dynatrace Webhook `/healthz`

`TCP 10080`

Проверка жизнеспособности/готовности [1](#fn-1-1-def)

kube-apiserver

Dynatrace Webhook `/inject`, `/label-ns`, `/validate*`

`TCP 8443`

Динамический контроллер допуска

Сборщик метрик Prometheus (необязательно)

Dynatrace Webhook `/metrics`

`TCP 8080`

Адрес метрик [2](#fn-1-2-def)

kubelet

Контейнер `server` CSI-драйвера Dynatrace Operator `/healthz`

`TCP 9808`

Проверка жизнеспособности [1](#fn-1-1-def)

kubelet

Контейнер `provisioner` CSI-драйвера Dynatrace Operator `/healthz`

`TCP 10090`

Проверка жизнеспособности [1](#fn-1-1-def)

Сборщик метрик Prometheus (необязательно)

Контейнер `server` CSI-драйвера Dynatrace Operator `/metrics`

`TCP 8080`

Адрес метрик [2](#fn-1-2-def)

Сборщик метрик Prometheus (необязательно)

Контейнер `provisioner` CSI-драйвера Dynatrace Operator `/metrics`

`TCP 8090`

Адрес метрик [2](#fn-1-2-def)

kubelet

ActiveGate `/rest/health`

`TCP 9999`

Проверка готовности [1](#fn-1-1-def)

kubelet

Extension Execution Controller `/readyz`

`TCP 14599`

Проверка готовности [1](#fn-1-1-def)

Поды приложений

ActiveGate `/*`

`TCP 9999`

Порт `HTTPS` по умолчанию

Поды приложений

ActiveGate `/*`

`TCP 9998`

Порт `HTTP` по умолчанию, приём данных, доступ к API

Поды приложений

Dynatrace Collector

[Порты приёма телеметрии](../../../../ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest.md#port-list "Включение конечных точек приёма телеметрии Dynatrace в Kubernetes для локального приёма данных в кластере.")

[Приём данных телеметрии](../../../../ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest.md "Включение конечных точек приёма телеметрии Dynatrace в Kubernetes для локального приёма данных в кластере.")

kubelet

Контейнер SQL Extension Executor `/health/live`

`TCP 8080`

Проверка жизнеспособности [1](#fn-1-1-def)

kubelet

Контейнер SQL Extension Executor `/health/ready`

`TCP 8080`

Проверка готовности [1](#fn-1-1-def)

1

[Проверки жизнеспособности](https://dt-url.net/dh03q2c) используются Kubernetes для проверки правильной работы контейнера. Если запрос не удаётся, контейнер будет перезапущен. [Проверки готовности](https://dt-url.net/ml23qbl) используются Kubernetes для проверки готовности пода к приёму трафика.

2

[Конечные точки метрик](https://dt-url.net/t543q6q) предоставляют дополнительные метрики в формате Prometheus.

Входящий трафик не принимается для EdgeConnect и OneAgent.

## Исходящий трафик

Компоненты Dynatrace Operator должны иметь доступ как к кластеру Kubernetes, так и к ресурсам за пределами кластера для корректной работы. Все ресурсы в пространстве имён Dynatrace Operator, пространство имён по умолчанию — `dynatrace`, должны иметь возможность разрешать DNS-запросы.

В зависимости от вашей конфигурации порт по умолчанию может отличаться от `TCP 443`.

Источник

Назначение

Порт

Примечание

* Dynatrace Operator
* Dynatrace Webhook
* CSI-драйвер Dynatrace Operator
* ActiveGate
* Extension Execution Controller

kube-dns

`TCP 53`, `UDP 53` [1](#fn-2-1-def)

Разрешение имён хостов для обнаружения сервисов

Dynatrace Operator

Сервер Dynatrace

`TCP 443` [1](#fn-2-1-def)

Конфигурация на стороне сервера [2](#fn-2-2-def)

Dynatrace Operator

kube-apiserver

`TCP 443` [1](#fn-2-1-def)

Управление жизненным циклом компонентов

Dynatrace Webhook

kube-apiserver

`TCP 443` [1](#fn-2-1-def)

Запросы мутации/валидации/конверсии

CSI-драйвер Dynatrace Operator

Сервер Dynatrace

`TCP 443` [1](#fn-2-1-def)

Расположение бинарных файлов модуля кода по умолчанию [2](#fn-2-2-def)

CSI-драйвер Dynatrace Operator

kube-apiserver

`TCP 443` [1](#fn-2-1-def)

Обработка томов CSI

CSI-драйвер Dynatrace Operator

частный реестр

`TCP 443` [1](#fn-2-1-def)

Необязательно. Связь с частным реестром для доступа к модулям кода [3](#fn-2-3-def)

ActiveGate

Конечные точки связи [4](#fn-2-4-def)

`TCP 443`, `TCP 9999` [1](#fn-2-1-def)

Информация о наблюдаемости [2](#fn-2-2-def)

ActiveGate

kube-apiserver

`TCP 443` [1](#fn-2-1-def)

Сбор ресурсов

ActiveGate

Поды приложений

Порт Prometheus Exporter [1](#fn-2-1-def)

Сбор метрик

OneAgent

Конечные точки связи [4](#fn-2-4-def)

`TCP 443`, `TCP 9999` [1](#fn-2-1-def)

Информация о наблюдаемости [2](#fn-2-2-def)

EdgeConnect

Сервер Dynatrace

`TCP 443` [1](#fn-2-1-def)

Конфигурация на стороне сервера [2](#fn-2-2-def)

EdgeConnect

kube-apiserver

`TCP 443` [1](#fn-2-1-def)

Необязательно. Взаимодействия рабочих процессов [5](#fn-2-5-def)

Extension Execution Controller

ActiveGate

`TCP 443` [1](#fn-2-1-def)

Конфигурация расширений и данные телеметрии [2](#fn-2-2-def)

1

В зависимости от вашей конфигурации порт может отличаться от значения по умолчанию.

2

Связь с хостами должна быть разрешена в соответствии с конфигурацией в [DynaKube](../../../../ingest-from/setup-on-k8s/reference/dynakube-parameters.md "Перечень доступных параметров для настройки Dynatrace Operator в Kubernetes.") (`apiUrl`) или [EdgeConnect](../../../../ingest-from/setup-on-k8s/reference/edgeconnect-parameters.md "Перечень параметров конфигурации EdgeConnect.") (`apiServer`) пользовательских ресурсов. Различные конечные точки связи могут использоваться в качестве резервных для обеспечения корректного подключения.

3

Требуется только при использовании поля `codeModulesImage`.

4

[Поддерживаемые схемы подключения для ActiveGate](../../../../ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates.md "Узнайте о приоритетах подключения между типами ActiveGate, а также о приоритетах между ActiveGate и OneAgent.")

5

Требуется только при включённой автоматизации Kubernetes.
