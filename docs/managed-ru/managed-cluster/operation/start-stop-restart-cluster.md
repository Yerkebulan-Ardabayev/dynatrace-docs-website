---
title: Запуск/остановка/перезапуск кластера
source: https://docs.dynatrace.com/managed/managed-cluster/operation/start-stop-restart-cluster
scraped: 2026-05-12T11:53:24.883782
---

# Запуск/остановка/перезапуск кластера

# Запуск/остановка/перезапуск кластера

* Updated on Dec 03, 2025

Программное обеспечение Dynatrace Managed состоит из ряда взаимозависимых служб Dynatrace, которые необходимо останавливать и запускать в определённом порядке. Используйте эту процедуру для развёртываний Dynatrace Managed, содержащих три и более узлов.

* Для развёртываний Dynatrace Managed с менее чем тремя (3) узлами можно использовать официальный скрипт `dynatrace.sh` с дополнительными параметрами для корректного запуска, остановки или перезапуска служб Dynatrace на каждом узле кластера индивидуально ([Запуск/остановка/перезапуск узла](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.")).
* Для развёртываний Dynatrace Managed с тремя (3) и более узлами используйте следующие процедуры кластера:

## Остановка кластера

1. Выполните следующую команду на каждом существующем узле:

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/server.sh stop
   ```
2. Выполните следующую команду для проверки статуса:

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/server.sh status
   ```

   Когда все серверные процессы полностью остановлены и проверка статуса показывает, что они не выполняются, выполните следующую команду на каждом существующем узле по одному:

   ```
   sudo nohup ../launcher/dynatrace.sh stop
   ```

## Запуск кластера

1. Выполните `/opt/dynatrace-managed/launcher/firewall.sh start` на каждом узле.
2. Выполните следующую команду на каждом существующем узле максимально одновременно:

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/elasticsearch.sh start
   ```

   Выполните следующую команду для проверки статуса:

   ```
   curl -X GET "localhost:9200/_cluster/health?wait_for_status=yellow&timeout=50s&pretty"
   ```

   Проверка статуса

   Убедитесь, что `active_shards_percent_as_number` составляет 100%, а `number_of_nodes` равно количеству узлов в кластере.
3. Выполните следующую команду на каждом существующем узле максимально одновременно:

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/cassandra.sh start
   ```

   Выполните следующую команду для проверки статуса:

   ```
   sudo nohup ./opt/dynatrace-managed/utils/cassandra-nodetool.sh status
   ```

   Проверка статуса

   Убедитесь, что все узлы отображают `UN`, прежде чем переходить к следующему шагу.
4. Выполните следующую команду на каждом существующем узле максимально одновременно. Полный запуск узла может занять до ~10 минут.

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/server.sh start
   ```
5. После полного запуска всех серверных процессов запустите остальные процессы. Выполните следующую команду на каждом существующем узле:

   ```
   sudo nohup ./opt/dynatrace-managed/launcher/dynatrace.sh start
   ```