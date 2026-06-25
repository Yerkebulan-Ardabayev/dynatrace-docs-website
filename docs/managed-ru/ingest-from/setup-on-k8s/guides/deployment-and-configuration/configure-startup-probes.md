---
title: Настройка startup-проверок для компонентов Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/configure-startup-probes
scraped: 2026-05-12T12:09:18.163544
---

# Настройка startup-проверок для компонентов Dynatrace Operator

# Настройка startup-проверок для компонентов Dynatrace Operator

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 12 марта 2026 г.

## Настройка startup-проверок для компонентов Dynatrace Operator

Конфигурация startup-проверки по умолчанию подходит для большинства окружений, но startup-проверки для компонентов Dynatrace Operator можно настроить так, чтобы они лучше соответствовали вашему конкретному окружению и эксплуатационным требованиям. Правильная настройка этих проверок помогает гарантировать, что компоненты полностью инициализированы и готовы к работе, прежде чем они начнут обрабатывать запросы.

Настройку startup-проверки можно легко выполнить через Helm `values.yaml` для Dynatrace Operator, Webhook или CSI driver.

* **Dynatrace Operator**

  ```
  operator:



  startupProbe:



  periodSeconds: 10



  timeoutSeconds: 5



  failureThreshold: 1
  ```
* **Webhook**

  ```
  webhook:



  startupProbe:



  periodSeconds: 10



  timeoutSeconds: 5



  failureThreshold: 1
  ```
* **CSI driver**

  ```
  csidriver:



  provisioner:



  startupProbe:



  periodSeconds: 10



  timeoutSeconds: 5



  failureThreshold: 1
  ```