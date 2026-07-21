---
title: Развёртывание с учётом стоек
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rack-awareness
---

# Развёртывание с учётом стоек

# Развёртывание с учётом стоек

* Пояснение
* Чтение: 3 мин
* Обновлено 07 июля 2026 г.

Dynatrace Managed развёртывание с учётом стоек позволяет группировать узлы Managed Cluster в три домена отказа (стойки). Такое развёртывание устойчиво к отказу всех узлов одной стойки. Можно сделать один Managed Cluster с учётом стоек либо применить эту схему к каждому дата-центру в развёртывании Premium High Availability (PHA).

## Как работает развёртывание с учётом стоек

Развёртывание с учётом стоек гарантирует, что ни одна реплика не хранится избыточно внутри одной стойки: реплики распределяются по всем стойкам. Если одна стойка выходит из строя, две другие полные реплики остаются доступны, что обеспечивает согласованность и доступность данных. Например, в развёртывании ниже Managed Cluster способен выдержать отказ до трёх узлов в стойке без потери данных.

![Крупный Managed Cluster с учётом стоек без потери данных](https://cdn.bfldr.com/B686QPH3/as/ngjgbptj3nb5jm7g7pqxf23/Premium_high_availability_rack_aware_Managed_deployment_with_no_data_loss-Light_Mode?auto=webp&format=png&position=1)

Крупный Managed Cluster с учётом стоек без потери данных

В стандартном развёртывании Dynatrace Managed с высокой доступностью нужно как минимум три узла Managed Cluster, чтобы предотвратить потерю данных. Аналогично, в развёртываниях с учётом стоек нужно иметь три стойки (домена отказа), чтобы предотвратить потерю данных. Если стойка выходит из строя, две оставшиеся стойки сохраняют данные. Поскольку в стойке находится как минимум три узла, в развёртываниях с учётом стоек можно допустить отказ целой стойки и при этом сохранить целостность данных.

Та же концепция применима к PHA Managed развёртываниям. Использование Managed Cluster с учётом стоек в разных дата-центрах повышает устойчивость к потере данных.

![Premium High Availability Managed развёртывание без потери данных](https://cdn.bfldr.com/B686QPH3/as/kq99pm9bftxrgfbtp3s4rg6p/Premium_high_availability_Managed_deployment_with_no_data_loss-Light_Mode?auto=webp&format=png&position=1)

Premium High Availability Managed развёртывание без потери данных

![Premium High Availability Managed развёртывание с учётом стоек без потери данных](https://cdn.bfldr.com/B686QPH3/as/ngjgbptj3nb5jm7g7pqxf23/Premium_high_availability_rack_aware_Managed_deployment_with_no_data_loss-Light_Mode?auto=webp&format=png&position=1)

Premium High Availability Managed развёртывание с учётом стоек без потери данных

Для максимальной высокой доступности и избыточности используй PHA развёртывание с учётом стоек.

## Предварительные условия

Схему с учётом стоек стоит применять только при следующих условиях:

* Итоговое число стоек равно трём, что соответствует коэффициенту репликации хранилища данных Dynatrace.
* Стойки отражают фактическое физическое расположение узлов при развёртывании.
* Стойки находятся в одной сети с низкой задержкой. Обычно это означает одну локальную сеть. Если стойки расположены в разных площадках, соединённых через глобальную сеть, задержка сети между площадками должна оставаться ниже 10 мс.

В противном случае возможна потеря данных и проблемы с доступностью Managed Cluster.

## Настройка развёртывания с учётом стоек

Чтобы создать развёртывание с учётом стоек уже на этапе первоначального развёртывания Managed, используй параметры установки для указания дата-центра и стойки для каждого узла. См. [Установка Managed Cluster](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") и [Настройка установки Dynatrace Managed](/managed/managed-cluster/installation/customize-managed-cluster-install#install-managed-cluster "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates."). Например:

```
dynatrace-managed.sh --rack-name az-1 --rack-dc datacenter1
```

Чтобы преобразовать существующий Managed Cluster в схему с учётом стоек, выбери метод в зависимости от размера хранилища метрик:

* Используй метод [преобразования в схему с учётом стоек через репликацию](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.") для небольших Managed Cluster, где один узел может содержать полную реплику. Этот метод не вызывает простоя Managed Cluster.
* Используй метод [преобразования в схему с учётом стоек через восстановление](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Dynatrace Managed Cluster to rack-aware topology using the backup and restore method, including preparation and installer parameters.") когда хранилище метрик (база данных Cassandra) на узел превышает 1 ТБ. Метод расширения кластера тоже работает, но требуемая начальная загрузка (bootstrapping) Cassandra занимает неоправданно много времени.

## Похожие темы

* [Преобразование в схему с учётом стоек через репликацию](/managed/managed-cluster/high-availability/rack-aware-replication "Learn how to convert a Dynatrace Managed Cluster to a rack-aware deployment using the replication method, including preparation and node migration steps.")
* [Преобразование в схему с учётом стоек через восстановление](/managed/managed-cluster/high-availability/rack-aware-restore "Learn how to convert a Dynatrace Managed Cluster to rack-aware topology using the backup and restore method, including preparation and installer parameters.")