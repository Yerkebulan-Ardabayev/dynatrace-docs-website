---
title: Как включить синтетические мониторы?
source: https://docs.dynatrace.com/managed/offline-doc/how-do-i-enable-synthetic-monitors
scraped: 2026-05-12T11:25:04.925366
---

# Как включить синтетические мониторы?

# Как включить синтетические мониторы?

* Published Jul 19, 2017

Этот раздел применим только к установкам Dynatrace Managed.

Для включения синтетических мониторов ваше развёртывание Dynatrace Managed должно иметь возможность получать данные синтетического мониторинга из облака Dynatrace. Для этого необходимо:

1. Установить [Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.") и
2. [Настроить публичную конечную точку коммуникации](/managed/managed-cluster/basics/managed-deployments "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture.").

После того как Dynatrace подтвердит доступность вашего Cluster ActiveGate из облака Dynatrace, вы сможете планировать синтетические мониторы для всех сред.

Безагентный мониторинг реальных пользователей и мониторинг мобильных приложений используют ту же конечную точку для передачи данных мониторинга в Dynatrace.