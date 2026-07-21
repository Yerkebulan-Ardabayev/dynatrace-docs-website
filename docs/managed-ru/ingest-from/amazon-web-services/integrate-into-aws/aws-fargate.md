---
title: Мониторинг AWS Fargate
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate
---

# Мониторинг AWS Fargate

# Мониторинг AWS Fargate

* Практическое руководство
* 1 минута на чтение
* Обновлено 08 июня 2026 г.

Для мониторинга рабочих нагрузок AWS Fargate нужно развернуть Dynatrace OneAgent, как описано ниже.

## Необходимые условия

* [Создать токен API](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") в среде Dynatrace и включить следующие права:

  + **Access problem and event feed, metrics, and topology** (API v1)
  + **PaaS integration - Installer download**
* Ознакомиться со списком [поддерживаемых приложений и версий](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Интеграция во время выполнения

Эта инструкция описывает, как интегрировать модули кода Dynatrace OneAgent в задачи Fargate с помощью initContainer. initContainer копирует артефакты OneAgent в общий эфемерный том, после чего переменные окружения настраивают и активируют OneAgent.

Dynatrace предоставляет образы модулей кода OneAgent в публичных реестрах, например:

* [Теги образов Dynatrace Code Modules﻿](https://gallery.ecr.aws/dynatrace/dynatrace-codemodules).

Такой образ можно использовать для контейнерных сервисов, поддерживающих initContainer. Образ `dynatrace-codemodules` содержит артефакты OneAgent и небольшой CLI, `dynatrace-bootstrapper`, который выполняется при запуске и копирует артефакты в том, общий с контейнером приложения.

### Выбор образа

Доступны следующие форматы тегов образов:

* **Неизменяемые теги (immutable tags)**, содержат модули кода конкретного релиза, например `1.327.51.20251205-162230`
* **Плавающие теги (rolling tags)** (major.minor), например `1.327`
* **Технологически-специфичные образы**, доступны как с неизменяемыми, так и с плавающими тегами, например `1.327-java`, `1.327-dotnet`

**Плавающие теги** (например, `1.333`) автоматически получают patch-обновления при перезапуске контейнера. Новые задачи подхватывают последнюю patch-версию без изменений в определении задачи. Плавающие теги стоит использовать, когда в приоритете автоматическая доставка исправлений.

**Неизменяемые теги** (например, `1.333.17.20250601-120000`) закрепляют задачи за конкретной версией, обеспечивая детерминированные развёртывания и понятный путь отката. Неизменяемые теги стоит использовать, когда требуется строгий контроль версий или соблюдение требований комплаенса.

**Технологически-специфичные образы** (например, `1.333-java`, `1.333-dotnet`) содержат модули кода только для одной среды выполнения, за счёт чего образ получается меньше, а загрузка и запуск быстрее. Технологически-специфичных образов стоит избегать, если контейнер использует несколько сред выполнения, которые нужно инструментировать одновременно, например PHP, работающий за NGINX.

### Безопасное хранение учётных данных

Учётные данные Dynatrace нужно хранить как секреты и ссылаться на них в поле `secrets` определения задачи. Можно использовать любое решение для хранения секретов, подходящее под конкретную конфигурацию, например AWS Secrets Manager.

### Настройка определения задачи

Нужно создать файл определения задачи (например, `task-definition.json`) со следующей структурой. Контейнер `initoneagent` запускается первым, копирует артефакты OneAgent в общий эфемерный том и завершает работу. После этого запускается контейнер приложения и загружает OneAgent через `LD_PRELOAD`.

Нужно заменить `<your-application-image>`, `<your-account-id>`, `<your-region>` и `<your-secret-name>` на собственные значения.

```
{



"family": "<your-task-family>",



"requiresCompatibilities": ["FARGATE"],



"networkMode": "awsvpc",



"cpu": "256",



"memory": "512",



"taskRoleArn": "arn:aws:iam::<your-account-id>:role/<your-task-role>",



"executionRoleArn": "arn:aws:iam::<your-account-id>:role/<your-task-execution-role>",



"containerDefinitions": [



{



"name": "initoneagent",



"image": "public.ecr.aws/dynatrace/dynatrace-codemodules:1.333",



"essential": false,



"user": "0:0",



"command": [



"--source=/opt/dynatrace/oneagent",



"--target=/mnt/dynatrace/oneagent",



"--technology=<your-technology>"



],



"environment": [



{ "name": "DT_ONEAGENT_OPTIONS", "value": "flavor=default&include=all" }



],



"secrets": [



{



"name": "DT_API_URL",



"valueFrom": "arn:aws:secretsmanager:<your-region>:<your-account-id>:secret:<your-secret-name>:DT_API_URL::"



},



{



"name": "DT_PAAS_TOKEN",



"valueFrom": "arn:aws:secretsmanager:<your-region>:<your-account-id>:secret:<your-secret-name>:DT_PAAS_TOKEN::"



}



],



"mountPoints": [



{



"sourceVolume": "oneagent",



"containerPath": "/mnt",



"readOnly": false



}



],



"logConfiguration": {



"logDriver": "awslogs",



"options": {



"awslogs-group": "<your-log-group>",



"awslogs-region": "<your-region>",



"awslogs-stream-prefix": "ecs"



}



}



},



{



"name": "<your-application-container>",



"image": "<your-application-image>",



"essential": true,



"linuxParameters": {



"initProcessEnabled": true



},



"environment": [



{ "name": "LD_PRELOAD", "value": "/mnt/dynatrace/oneagent/agent/lib64/liboneagentproc.so" }



],



"secrets": [



{



"name": "DT_TENANT",



"valueFrom": "arn:aws:secretsmanager:<your-region>:<your-account-id>:secret:<your-secret-name>:DT_TENANT::"



},



{



"name": "DT_TENANTTOKEN",



"valueFrom": "arn:aws:secretsmanager:<your-region>:<your-account-id>:secret:<your-secret-name>:DT_TENANTTOKEN::"



},



{



"name": "DT_CONNECTION_POINT",



"valueFrom": "arn:aws:secretsmanager:<your-region>:<your-account-id>:secret:<your-secret-name>:DT_CONNECTION_POINT::"



}



],



"mountPoints": [



{



"sourceVolume": "oneagent",



"containerPath": "/mnt",



"readOnly": false



}



],



"dependsOn": [



{



"containerName": "initoneagent",



"condition": "COMPLETE"



}



],



"logConfiguration": {



"logDriver": "awslogs",



"options": {



"awslogs-group": "<your-log-group>",



"awslogs-region": "<your-region>",



"awslogs-stream-prefix": "ecs"



}



}



}



],



"volumes": [



{



"name": "oneagent",



"host": {}



}



]



}
```

Нужно заменить `<your-technology>` на среду выполнения приложения (допустимые значения: `python`, `java`, `dotnet`, `nodejs`, `php`, `go`, `apache`, `nginx`, `all`).

1. Зарегистрировать определение задачи:

   ```
   aws ecs register-task-definition --cli-input-json file://task-definition.json
   ```
2. Обновить сервис ECS для использования новой ревизии:

   ```
   aws ecs update-service \



   --cluster <your-cluster-name> \



   --service <your-service-name> \



   --task-definition <your-task-family>
   ```

## Альтернативные пути интеграции

* **EKS on Fargate**, можно запускать на Amazon EKS с типом запуска Fargate, используя внедрение только уровня приложения с помощью Dynatrace Operator. См. [Установка на EKS Fargate](/managed/ingest-from/setup-on-k8s/deployment/marketplaces/eks-dto#fargate "Deploy and configure Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS) environment.").
* **Внедрение на этапе сборки контейнера**, чтобы встроить OneAgent в образ контейнера на этапе сборки с помощью многоступенчатой сборки Docker, см. [Настройка OneAgent на контейнерах для мониторинга только приложения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.").

## Дополнительная настройка

После интеграции OneAgent можно настроить его поведение, добавив переменные окружения в контейнер приложения.

### Маршрутизация логов OneAgent в stdout

Чтобы направлять диагностические логи OneAgent в stdout вместе с логами приложения, нужно добавить следующие переменные окружения в контейнер приложения:

* `DT_LOGSTREAM=stdout`, направляет диагностический вывод OneAgent в стандартный вывод
* `DT_LOGLEVELCON=INFO`, задаёт уровень детализации логов

При настройке лог-драйвера `awslogs` для контейнеров (как показано в примере определения задачи) [CloudWatch Logs](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudwatch-logs "Monitor Amazon CloudWatch Logs and view available metrics.") собирает логи приложения и диагностические логи OneAgent в единый поток.

### Настройка сетевых зон

Сетевые зоны можно настроить как переменную окружения:

* `DT_NETWORK_ZONE`: равна `your.network.zone`

Дополнительную информацию см. в разделе [сетевые зоны](/managed/manage/network-zones "Find out how network zones work in Dynatrace.").

## Мониторинг потребления

Расчёт потребления при мониторинге зависит от модели лицензирования:

* Dynatrace Platform Subscription (DPS): потребление тарифицируется в ГиБ-часах, см. [Расчёт потребления Full-Stack Monitoring](/managed/license/capabilities/app-infra-observability/full-stack-monitoring#app-only-gib-hour "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.").
* Классическое лицензирование Dynatrace: потребление тарифицируется в host unit'ах, см. [Application and Infrastructure Monitoring (Host Units)](/managed/license/classic-licensing/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

## Устранение неполадок

По проблемам интеграции OneAgent см. [Проблемы интеграции OneAgent в образ приложения﻿](https://dt-url.net/yu23mli).

## Похожие темы

* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")