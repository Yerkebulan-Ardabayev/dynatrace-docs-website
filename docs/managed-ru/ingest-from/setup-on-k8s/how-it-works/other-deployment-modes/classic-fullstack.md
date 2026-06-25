---
title: Classic Full-Stack monitoring
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack
scraped: 2026-05-12T11:23:23.613216
---

# Classic Full-Stack monitoring

# Classic Full-Stack monitoring

* Чтение: 2 мин
* Опубликовано 31 октября 2024 г.

Classic Full-Stack monitoring объединяет мониторинг хостов и приложений для окружений Kubernetes. Инструментированные Pod сохраняют связь с хостами, что позволяет собирать метрики хостов.

Дополнительную информацию см. в разделе [`.spec.oneAgent.classicFullStack`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") DynaKube.

## Возможности

* Инструментированные Pod сохраняют таксономическую связь с хостами и метриками хостов. OneAgent дополняет code modules обнаружением OOM, мониторингом дисков и хранилища, мониторингом сети и другими возможностями.
* Этот комплексный подход включает мониторинг кластеров Kubernetes, распределённое трассирование, изоляцию доменов отказа и глубокие инсайты на уровне кода с использованием единой конфигурации развёртывания во всех ваших кластерах.

## Ограничения

Существует зависимость запуска между контейнером, в котором развёрнут OneAgent, и контейнером приложения, который нужно инструментировать (например, контейнерами с включённым deep process monitoring). Контейнер OneAgent должен быть запущен, а процесс `oneagenthelper` должен работать до запуска контейнера приложения, чтобы обеспечить корректное инструментирование.

## Развёрнутые ресурсы

### Компоненты Dynatrace Operator

Следующие компоненты развёртываются через Helm/Manifests в рамках базовой установки. Подробнее см. в соответствующих разделах:

* [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Компоненты Dynatrace Operator") управляет автоматическим развёртыванием, настройкой и жизненным циклом компонентов Dynatrace в вашем окружении Kubernetes.
* [Dynatrace Operator webhook](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Компоненты Dynatrace Operator") проверяет определения DynaKube, конвертирует определения с устаревшими версиями API и внедряет конфигурации в Pod.

### Компоненты под управлением оператора

Следующие компоненты развёртываются путём применения DynaKube с full-stack observability:

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Изучите ключевые концепции OneAgent и узнайте, как устанавливать и эксплуатировать OneAgent на различных платформах.") собирает метрики хостов с узлов Kubernetes.
* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.") маршрутизирует данные observability в кластер Dynatrace и отслеживает Kubernetes API.

![classic-full-stack](https://dt-cdn.net/images/screenshot-2024-01-31-at-2-37-54-pm-2354-6d55b949e0.png)

classic-full-stack

Инъекция classic full-stack требует *доступа на запись* от Pod OneAgent к файловой системе узла Kubernetes для обнаружения и инъекции во вновь развёрнутые контейнеры.