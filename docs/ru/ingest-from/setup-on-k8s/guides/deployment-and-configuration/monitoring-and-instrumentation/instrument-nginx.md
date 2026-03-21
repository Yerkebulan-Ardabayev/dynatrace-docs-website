---
title: Инструментирование ingress-nginx
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx
scraped: 2026-03-06T21:22:46.951929
---

# Instrument ingress-nginx

* Latest Dynatrace

Приведённые ниже инструкции применимы только к [официальной реализации контроллера Kubernetes ingress от Google](https://dt-url.net/xr03xh3).

* Производные от официального проекта, например [контроллер ingress от Bitnami](https://dt-url.net/ns03xjt), не поддерживаются. Однако их можно инструментировать вручную с помощью [Manual runtime instrumentation](../../../../technology-support/application-software/nginx/manual-runtime-instrumentation.md "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.") для NGINX.
* [Реализация контроллера ingress от F5 NGINX](https://dt-url.net/ph43xrd) может быть инструментирована автоматически; никаких ручных действий не требуется.

Процесс NGINX официального образа контейнера контроллера Kubernetes ingress-nginx не может быть инструментирован автоматически. Для ручного инструментирования ingress-nginx в Kubernetes следуйте приведённым ниже инструкциям.

## Предварительные требования

Архитектура ARM64 не поддерживается.

* OneAgent версии 1.227+
* Имя пода должно содержать подстроку `ingress-nginx-` для правильного инструментирования двоичного файла NGINX. Рекомендуется сохранять имя пода по умолчанию `ingress-nginx-controller`.

## Инструментирование Kubernetes ingress-nginx

Для инструментирования ingress-nginx в Kubernetes необходимо вручную загрузить модуль NGINX через ConfigMap.

Убедитесь, что OneAgent запущен и способен инструментировать контейнеры ingress-nginx при применении изменений к ConfigMap ingress-nginx. Если эти условия не выполнены, NGINX не запустится.

1. Отредактируйте ConfigMap.

   ```
   kubectl edit configmap ingress-nginx-controller
   ```
2. Добавьте следующее значение к ключу `main-snippet` (под `data`).

   Пример:

   ```
   data:


   main-snippet: load_module /opt/dynatrace/oneagent/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;
   ```

   Для развёртываний `cloudNativeFullStack` и `applicationMonitoring` путь принимает следующий вид:

   ```
   data:


   main-snippet: load_module /opt/dynatrace/oneagent-paas/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;
   ```

## Проверка конфигурации

Если ваш под не запускается, убедитесь, что не превышено ни одно из следующих ограничений:

* Квота ресурсов (особенно по памяти).
* Начальные тайм-ауты проб живости/готовности (liveness/readiness). Возможно, потребуется увеличить значение `initialDelaySeconds` для этих проб.
