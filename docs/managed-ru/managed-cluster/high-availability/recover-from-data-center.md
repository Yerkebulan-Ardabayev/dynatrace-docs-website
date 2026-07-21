---
title: Восстановление из другого дата-центра
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/recover-from-data-center
---

# Восстановление из другого дата-центра

# Восстановление из другого дата-центра

* Практическое руководство
* 1 мин на чтение
* Обновлено 07 июля 2026 г.

Простои одного дата-центра (ДЦ) продолжительностью до 72 часов не требуют этой процедуры аварийного восстановления. Когда недоступный ДЦ снова становится доступным, Premium High Availability (PHA) автоматически восстанавливает затронутый ДЦ и возобновляет работу Managed Cluster. Подробности приведены в разделе [Отказоустойчивое переключение между дата-центрами](/managed/managed-cluster/high-availability/failover "Learn how the Premium High Availability multi-data center failover mechanism detects node outages and transfers responsibility to a healthy data center.").

Чтобы избежать несогласованности данных, пока ДЦ недоступен, нужно остановить службу сервера на всех узлах затронутого ДЦ. Запускать службы следует только после того, как сетевое подключение снова станет стабильным.

По истечении 72 часов Mission Control (MC) помечает Managed Cluster как невосстановленный после переключения. Такой Managed Cluster ненадёжен. В результате нужно восстановить или пересоздать отказавший ДЦ либо из работающего ДЦ, либо из резервной копии.

## Процедура восстановления

Чтобы восстановить работу из другого дата-центра, нужно выполнить следующие шаги:

1. Удалить недоступные узлы из Managed Cluster.
2. Обновить конфигурацию уцелевшего ДЦ.
3. Переустановить узлы в восстанавливаемом ДЦ.
4. Реплицировать Cassandra в восстанавливаемый ДЦ.
5. Реплицировать Elasticsearch в восстанавливаемый ДЦ.
6. Пересоздать сервер, запустить ActiveGate и запустить NGINX в восстанавливаемом ДЦ.
7. Включить восстановленный ДЦ.

Подробная процедура приведена в разделе [Восстановление дата-центра](/managed/managed-cluster/high-availability/rebuild-data-center "Learn how to rebuild a lost data center in a Dynatrace Managed Premium High Availability deployment and restore replication across both data centers.").