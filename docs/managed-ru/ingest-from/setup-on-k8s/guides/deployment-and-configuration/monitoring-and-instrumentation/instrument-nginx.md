---
title: Инструментирование ingress-nginx
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx
scraped: 2026-05-12T12:00:23.608602
---

# Инструментирование ingress-nginx

# Инструментирование ingress-nginx

* Чтение: 1 мин
* Обновлено 18 марта 2026 г.

Приведённые ниже инструкции актуальны только для [официальной реализации ingress-контроллера Kubernetes от Google](https://dt-url.net/xr03xh3).

* Производные от официального проекта, такие как [ingress-контроллер Bitnami](https://dt-url.net/ns03xjt), не поддерживаются. Однако их можно инструментировать вручную с помощью [инструментирования во время выполнения](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Узнайте, как принудительно инструментировать пропатченные/нестандартные двоичные файлы NGINX во время выполнения.") для NGINX.
* ingress-nginx-controller от Chainguard является форком официального ingress-nginx-controller Kubernetes (используйте те же инструкции ниже). Используйте вариант образа `-debug` (например, `ingress-nginx-controller:latest-debug`), который включает отладочные символы nginx, необходимые для инструментирования во время выполнения.
* [Реализацию ingress-контроллера от F5 NGINX](https://dt-url.net/ph43xrd) можно инструментировать автоматически; никаких действий вручную не требуется.

Процесс NGINX в образе контейнера официального ingress-nginx контроллера Kubernetes невозможно инструментировать автоматически. Чтобы инструментировать ingress-nginx в Kubernetes вручную, следуйте приведённым ниже инструкциям.

## Предварительные требования

Архитектура ARM64 не поддерживается.

* OneAgent версии 1.227+
* Имя пода должно содержать подстроку `ingress-nginx-`, чтобы обеспечить корректное инструментирование двоичного файла NGINX. Рекомендуем сохранять имя пода по умолчанию `ingress-nginx-controller`.

## Инструментирование ingress-nginx в Kubernetes

Чтобы инструментировать ingress-nginx в Kubernetes, необходимо вручную загрузить модуль NGINX через ConfigMap.

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

   Для развёртываний `cloudNativeFullStack` и `applicationMonitoring` путь становится следующим:

   ```
   data:



   main-snippet: load_module /opt/dynatrace/oneagent-paas/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;
   ```

## Проверка вашей конфигурации

Если ваш под не запущен и не работает, убедитесь, что он не превысил ни один из следующих лимитов:

* Свою квоту ресурсов (особенно по памяти).
* Начальные тайм-ауты проверок liveness/readiness. Возможно, вам потребуется увеличить `initialDelaySeconds` для этих проверок.