---
title: Rack-aware развёртывание Managed
source: https://docs.dynatrace.com/managed/managed-cluster/high-availability/rack-awareness
scraped: 2026-05-12T11:53:27.988786
---

# Rack-aware развёртывание Managed

# Rack-aware развёртывание Managed

* Updated on May 04, 2026

В стандартном развёртывании Dynatrace Managed с высокой доступностью обеспечивается защита от потери данных при отказе одного узла — как в небольших, так и в крупных развёртываниях.

Rack-aware развёртывание Dynatrace Managed позволяет сгруппировать узлы кластера в три домена отказов (rack'а). Такое развёртывание устойчиво к выходу из строя всех узлов в одном rack'е.

## Требования

Rack awareness следует использовать только при выполнении следующих условий:

* Итоговое количество rack'ов равно трём, что соответствует replication factor хранилища данных Dynatrace.
* Rack'и отражают физическое расположение узлов.

В противном случае возможна потеря данных и проблемы с доступностью кластера.

## Rack-aware развёртывание

Rack-aware развёртывание гарантирует, что реплики не хранятся избыточно внутри одного rack'а — они распределяются по всем rack'ам. При отказе одного rack'а оба полных реплика доступны на двух оставшихся rack'ах, обеспечивая согласованность и доступность данных. Например, в развёртывании ниже кластер Dynatrace Managed выдерживает до трёх отказов узлов в rack'е без потери данных.

![Крупный rack-aware кластер Managed без потери данных](https://dt-cdn.net/images/3l-ra-man-cluster-no-data-loss-4eb930ca7f.svg "Крупный rack-aware кластер Managed без потери данных")

Крупный rack-aware кластер Managed без потери данных

В стандартном развёртывании Dynatrace Managed с высокой доступностью для предотвращения потери данных необходимы как минимум три узла кластера.
Аналогично в rack-aware развёртываниях для предотвращения потери данных необходимы три rack'а (домена отказов). При отказе rack'а два оставшихся сохраняют данные. При наличии в rack'е не менее трёх узлов rack-aware развёртывание выдерживает полный отказ rack'а с сохранением целостности данных.

Тот же принцип применим к развёртываниям Premium High Availability Managed. Использование rack-aware Managed-кластеров в отдельных центрах обработки данных повышает устойчивость к потере данных.

![Схема — развёртывание Premium High Availability Managed без потери данных](https://dt-cdn.net/images/4man-ha-no-data-loss-54863cd646.svg "Схема — развёртывание Premium High Availability Managed без потери данных")

Схема — развёртывание Premium High Availability Managed без потери данных

Развёртывание Premium High Availability Managed.

![Rack-aware развёртывание Premium High Availability Managed без потери данных](https://dt-cdn.net/images/5man-ha-ra-no-data-loss-5f9393973b.svg "Rack-aware развёртывание Premium High Availability Managed без потери данных")

Rack-aware развёртывание Premium High Availability Managed без потери данных

Rack-aware развёртывание Premium High Availability Managed.

Для достижения максимальной высокой доступности и избыточности используйте rack-aware развёртывание Premium High Availability.

Чтобы создать rack-aware развёртывание при первоначальной установке Managed, используйте параметры установки для указания центра обработки данных и rack'а, к которым следует добавить узел. См. [Установка кластера](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") и [Настройка установки Dynatrace Managed](/managed/managed-cluster/installation/customize-managed-cluster-install#install-managed-cluster "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates."), например:

```
dynatrace-managed.sh --rack-name az-1 --rack-dc datacenter1
```

## Конвертация в rack-aware

Для конвертации существующего Managed-развёртывания используйте метод расширения кластера или метод восстановления кластера.

### Расширение кластера (без простоя)

Вертикальное масштабирование узлов в двух расположениях позволяет им взять на себя дополнительную нагрузку после выключения третьего расположения и его переустановки с rack-aware параметрами. См. [Конвертация в rack-aware с использованием репликации](/managed/managed-cluster/high-availability/rack-aware-conversion-using-replication "Learn how to download and convert Dynatrace Managed cluster to rack-aware using the expansion method.").

Размер хранилища метрик

Если текущий размер хранилища метрик (база данных Cassandra) на узел превышает 1 ТБ, используйте метод восстановления кластера. Метод расширения кластера технически работает, однако в этом случае процесс Cassandra bootstrapping может занять неоправданно долгое время.

### Восстановление кластера (с простоем во время восстановления)

Можно выполнить резервное копирование и восстановление с rack-aware параметрами. См. [Конвертация в rack-aware с использованием восстановления](/managed/managed-cluster/high-availability/rack-aware-conversion-using-restore "Learn how to download and convert a Dynatrace Managed cluster to rack-aware using the restore method.").

## Связанные темы

* [Конвертация в rack-aware с использованием репликации](/managed/managed-cluster/high-availability/rack-aware-conversion-using-replication "Learn how to download and convert Dynatrace Managed cluster to rack-aware using the expansion method.")
* [Конвертация в rack-aware с использованием восстановления](/managed/managed-cluster/high-availability/rack-aware-conversion-using-restore "Learn how to download and convert a Dynatrace Managed cluster to rack-aware using the restore method.")