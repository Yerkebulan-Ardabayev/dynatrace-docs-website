---
title: Сетевой трафик
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/network
scraped: 2026-05-12T11:53:40.710402
---

# Сетевой трафик

# Сетевой трафик

* Чтение: 3 мин
* Обновлено 02 января 2026 г.

Чтобы компоненты Dynatrace Operator работали правильно в кластере Kubernetes, они должны иметь возможность взаимодействовать как с кластером Dynatrace, так и с кластером Kubernetes.

Компоненты Dynatrace Operator доступны через определённые порты и обращаются к различным ресурсам внутри и снаружи кластера Kubernetes. Подробнее о том, к каким ресурсам выполняется обращение внутри кластера Kubernetes, см. справочную страницу [Разрешения RBAC для Operator](/managed/ingest-from/setup-on-k8s/reference/security "На этой странице приведён обзор компонентов Dynatrace, их конфигураций по умолчанию и требуемых ими разрешений").

## Входящий трафик

| Источник | Назначение | Порт | Примечание |
| --- | --- | --- | --- |
| kubelet | Dynatrace Operator `/healthz` | `TCP 10080` | Liveness probe [1](#fn-1-1-def) |
| Prometheus metrics scraper Необязательно | Dynatrace Operator `/metrics` | `TCP 8080` | Адрес метрик [2](#fn-1-2-def) |
| kubelet | Dynatrace Webhook `/healthz` | `TCP 10080` | Liveness/Readiness probe [1](#fn-1-1-def) |
| kube-apiserver | Dynatrace Webhook `/inject`, `/label-ns`, `/validate*` | `TCP 8443` | Dynamic Admission Controller |
| Prometheus metrics scraper Необязательно | Dynatrace Webhook `/metrics` | `TCP 8080` | Адрес метрик [2](#fn-1-2-def) |
| kubelet | Dynatrace Operator CSI driver `server` container `/healthz` | `TCP 9808` | Liveness probe [1](#fn-1-1-def) |
| kubelet | Dynatrace Operator CSI driver `provisioner` container `/healthz` | `TCP 10090` | Liveness probe [1](#fn-1-1-def) |
| Prometheus metrics scraper Необязательно | Dynatrace Operator CSI driver `server` container `/metrics` | `TCP 8080` | Адрес метрик [2](#fn-1-2-def) |
| Prometheus metrics scraper Необязательно | Dynatrace Operator CSI driver `provisioner` container `/metrics` | `TCP 8090` | Адрес метрик [2](#fn-1-2-def) |
| kubelet | ActiveGate `/rest/health` | `TCP 9999` | Readiness probe [1](#fn-1-1-def) |
| kubelet | Extension Execution Controller `/readyz` | `TCP 14599` | Readiness probe [1](#fn-1-1-def) |
| Application pods | ActiveGate `/*` | `TCP 9999` | Порт `HTTPS` по умолчанию |
| Application pods | ActiveGate `/*` | `TCP 9998` | Порт `HTTP` по умолчанию, приём данных, доступ к API |
| Application pods | Dynatrace Collector | [Порты приёма телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest#port-list "Включите конечные точки приёма телеметрии Dynatrace в Kubernetes для локального приёма данных в кластере.") | [Приём данных телеметрии](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включите конечные точки приёма телеметрии Dynatrace в Kubernetes для локального приёма данных в кластере.") |
| kubelet | SQL Extension Executor container `/health/live` | `TCP 8080` | Liveness probe [1](#fn-1-1-def) |
| kubelet | SQL Extension Executor container `/health/ready` | `TCP 8080` | Readiness probe [1](#fn-1-1-def) |

1

[Проверки Liveness](https://dt-url.net/dh03q2c) используются Kubernetes для проверки того, что контейнер работает правильно. Если запрос не выполняется, контейнер будет перезапущен. [Проверки Readiness](https://dt-url.net/ml23qbl) используются Kubernetes для проверки того, что под готов принимать трафик.

2

[Конечные точки метрик](https://dt-url.net/t543q6q) выдают дополнительные метрики в формате Prometheus.

Входящий трафик для EdgeConnect и OneAgent не принимается.

## Исходящий трафик

Компоненты Dynatrace Operator должны обращаться как к кластеру Kubernetes, так и к ресурсам за пределами кластера, чтобы работать правильно. Все ресурсы в пространстве имён Dynatrace Operator, где пространством имён по умолчанию является `dynatrace`, должны иметь возможность разрешать DNS-запросы.

В зависимости от вашей конфигурации порт по умолчанию может отличаться от `TCP 443`.

| Источник | Назначение | Порт | Примечание |
| --- | --- | --- | --- |
| * Dynatrace Operator * Dynatrace Webhook * Dynatrace Operator CSI driver * ActiveGate * Extension Execution Controller | kube-dns | `TCP 53`, `UDP 53` [1](#fn-2-1-def) | Разрешение имён хостов для обнаружения сервисов |
| Dynatrace Operator | Dynatrace server | `TCP 443` [1](#fn-2-1-def) | Настройка на стороне сервера [2](#fn-2-2-def) |
| Dynatrace Operator | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | Управление жизненным циклом компонентов |
| Dynatrace Webhook | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | Запросы Mutating/Validating/Conversion |
| Dynatrace Operator CSI driver | Dynatrace server | `TCP 443` [1](#fn-2-1-def) | Расположение по умолчанию для двоичных файлов модуля кода [2](#fn-2-2-def) |
| Dynatrace Operator CSI driver | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | Обработка томов CSI |
| Dynatrace Operator CSI driver | private registry | `TCP 443` [1](#fn-2-1-def) | Необязательно Взаимодействие с приватным реестром для доступа к модулям кода [3](#fn-2-3-def) |
| ActiveGate | Communication endpoints [4](#fn-2-4-def) | `TCP 443`, `TCP 9999` [1](#fn-2-1-def) | Информация наблюдаемости [2](#fn-2-2-def) |
| ActiveGate | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | Сбор ресурсов |
| ActiveGate | Application Pods | Prometheus Exporter port [1](#fn-2-1-def) | Сбор метрик |
| OneAgent | Communication endpoints [4](#fn-2-4-def) | `TCP 443`, `TCP 9999` [1](#fn-2-1-def) | Информация наблюдаемости [2](#fn-2-2-def) |
| EdgeConnect | Dynatrace server | `TCP 443` [1](#fn-2-1-def) | Настройка на стороне сервера [2](#fn-2-2-def) |
| EdgeConnect | kube-apiserver | `TCP 443` [1](#fn-2-1-def) | Необязательно Взаимодействия с Workflow [5](#fn-2-5-def) |
| Extension Execution Controller | ActiveGate | `TCP 443` [1](#fn-2-1-def) | Настройка расширений и данные телеметрии [2](#fn-2-2-def) |

1

В зависимости от вашей конфигурации порт может отличаться от значения по умолчанию.

2

Взаимодействие с хостами должно быть разрешено в соответствии с настройкой в пользовательских ресурсах [DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") (`apiUrl`) или [EdgeConnect](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.") (`apiServer`). Для обеспечения корректного подключения в качестве резервных могут использоваться разные конечные точки взаимодействия.

3

Требуется только при использовании поля `codeModulesImage`.

4

[Поддерживаемые схемы подключения для ActiveGate](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate, а также о приоритетах между ActiveGate и OneAgent.")

5

Требуется только при включённой Kubernetes Automation.