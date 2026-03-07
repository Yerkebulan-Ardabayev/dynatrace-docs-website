---
title: "Кластер Dynatrace Managed"
source: https://docs.dynatrace.com/managed/managed-cluster
updated: 2026-03-07
---

# Кластер Dynatrace Managed

Управление кластером Dynatrace Managed — установка узлов, настройка высокой доступности и мониторинг состояния кластера.

## Основные разделы

- **[Управление кластером](../managed-cluster/)** — полное руководство по настройке и обслуживанию кластера
- **[Установка](../installation/)** — требования и процесс установки
- **[Настройка](../configuration/)** — конфигурация после установки
- **[Обслуживание](../operations/)** — мониторинг и поддержка кластера
- **[Обновления](../update/)** — процесс обновления Dynatrace Managed
- **[Бэкап](../backup/)** — резервное копирование данных
- **[Безопасность](../security/)** — настройки безопасности кластера

## Архитектура кластера

Кластер Dynatrace Managed состоит из:

| Компонент | Описание |
|-----------|----------|
| **Cluster Node** | Узел кластера с Server и Embedded ActiveGate |
| **Cassandra** | Распределённое хранилище данных |
| **Elasticsearch** | Поиск и аналитика |
| **NGINX** | Обратный прокси и балансировка нагрузки |

## API кластера

- [Cluster API v2](/managed/managed-cluster/api-references/cluster-api/cluster-api-v2) — API для управления кластером
- [Токены и аутентификация](/managed/dynatrace-api/basics/dynatrace-api-authentication) — аутентификация API-запросов
