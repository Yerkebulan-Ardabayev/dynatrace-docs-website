---
title: Удаление кластера
source: https://docs.dynatrace.com/managed/managed-cluster/operation/remove-a-cluster
scraped: 2026-05-12T11:53:12.061318
---

# Удаление кластера

# Удаление кластера

* Published Feb 01, 2018

Для удаления кластера необходимо удалить все его узлы. Иными словами, нужно [удалить Dynatrace Server с каждого узла](/managed/managed-cluster/operation/remove-a-cluster-node "Learn how to remove a new cluster node using either the command prompt or the Cluster Management Console."). Для одновременного освобождения лицензии используйте параметр `--unregister` как минимум один раз при удалении узлов кластера.

При использовании параметра `--unregister` лицензия освобождается, однако кластер по-прежнему остаётся настроенным и потенциально может быть связан с новой лицензией.