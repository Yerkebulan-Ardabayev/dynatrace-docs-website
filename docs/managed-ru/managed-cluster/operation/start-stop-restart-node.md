---
title: Запуск/остановка/перезапуск узла
source: https://docs.dynatrace.com/managed/managed-cluster/operation/start-stop-restart-node
scraped: 2026-05-12T11:53:15.065043
---

# Запуск/остановка/перезапуск узла

# Запуск/остановка/перезапуск узла

* Updated on May 24, 2022

Программное обеспечение Dynatrace Managed состоит из ряда взаимозависимых служб Dynatrace, которые необходимо останавливать и запускать в определённом порядке.

* Для развёртываний Dynatrace Managed с тремя (3) и более узлами используйте процедуру кластера ([Запуск/остановка/перезапуск кластера](/managed/managed-cluster/operation/start-stop-restart-cluster "Properly shut down and restart Dynatrace Managed deployments containing three or more nodes.")).
* Для развёртываний Dynatrace Managed с менее чем тремя (3) узлами можно использовать официальный скрипт `dynatrace.sh` с дополнительными параметрами для корректного запуска, остановки или перезапуска служб Dynatrace на каждом узле кластера индивидуально.

По умолчанию скрипт расположен в директории `/opt/dynatrace-managed/launcher/`. Убедитесь, что скрипт `dynatrace.sh` имеет права на выполнение.

Скрипт `dynatrace.sh` можно выполнить с параметром (`start`, `stop`, `restart`, `status`, `check`, `pid`), как описано ниже.

* **start**

  Запускает все необходимые службы Dynatrace Managed в рекомендованном порядке.

  ```
  [root@localhost]# ./dynatrace.sh start
  ```
* **stop**

  Останавливает все необходимые службы Dynatrace Managed в рекомендованном порядке.

  ```
  [root@localhost]# ./dynatrace.sh stop
  ```
* **restart**

  Перезапускает все необходимые службы Dynatrace Managed в рекомендованном порядке.

  ```
  [root@localhost]# ./dynatrace.sh restart
  ```
* **status**

  Выводит список необходимых служб Dynatrace и статус каждой из них, включая подробную информацию о каждой службе:

  ```
  [root@localhost]# ./dynatrace.sh status
  ```

  Пример вывода dynatrace.sh status

  ```
  ● dynatrace-firewall.service - Dynatrace Firewall settings



  Loaded: loaded (/etc/systemd/system/dynatrace-firewall.service; enabled; vendor preset: enabled)



  Active: active (exited) since Tue 2019-07-09 08:34:54 UTC; 1 months 3 days ago



  Main PID: 12967 (code=exited, status=0/SUCCESS)



  Tasks: 0



  Memory: 0B



  CPU: 0



  CGroup: /system.slice/dynatrace-firewall.service



  Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.



  ● dynatrace-nodekeeper.service - Dynatrace Nodekeeper



  Loaded: loaded (/etc/systemd/system/dynatrace-nodekeeper.service; enabled; vendor preset: enabled)



  Active: active (running) since Tue 2019-07-09 08:30:02 UTC; 1 months 3 days ago



  Tasks: 69 (limit: 32768)



  Memory: 389.2M



  CPU: 2h 9min 51.936s



  CGroup: /system.slice/dynatrace-nodekeeper.service



  ├─  552 /opt/managed/nodekeeper/jre/bin/java -Xms239M -Xmx239M -XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=60 -Duser.language=EN -Djava.io.tmpdir=...



  └─  966 /bin/sh /opt/managed/nodekeeper/services/watchdog.sh watch /opt/managed/nodekeeper/services/nodekeeper.sh



  └─22167 sleep 60



  Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.



  ● dynatrace-cassandra.service - Dynatrace Cassandra



  Loaded: loaded (/etc/systemd/system/dynatrace-cassandra.service; enabled; vendor preset: enabled)



  Active: active (running) since Tue 2019-07-09 08:37:52 UTC; 1 months 3 days ago



  Tasks: 199 (limit: 32768)



  Memory: 3.2G



  CPU: 17h 1min 32.540s



  CGroup: /system.slice/dynatrace-cassandra.service



  ├─13690 /opt/managed/jre/bin/java -javaagent:/opt/managed/cassandra/bin/../lib/jamm-0.3.0.jar -XX:+CMSClassUnloadingEnabled -XX:+UseThreadPriorities -XX:ThreadPr...



  └─13721 /bin/sh /opt/managed/services/watchdog.sh watch /opt/managed/services/cassandra.sh



  └─22197 sleep 60



  Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.



  ● dynatrace-elasticsearch.service - Dynatrace Elasticsearch



  Loaded: loaded (/etc/systemd/system/dynatrace-elasticsearch.service; enabled; vendor preset: enabled)



  Active: active (running) since Tue 2019-07-09 08:38:15 UTC; 1 months 3 days ago



  Tasks: 58 (limit: 32768)



  Memory: 884.6M



  CPU: 6h 59min 48.051s



  CGroup: /system.slice/dynatrace-elasticsearch.service



  ├─14802 /opt/managed/jre/bin/java -Xms558M -Xmx558M -XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -XX:+AlwaysP...



  └─14834 /bin/sh /opt/managed/services/watchdog.sh watch /opt/managed/services/elasticsearch.sh



  └─21975 sleep 60



  Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.



  ● dynatrace-server.service - Dynatrace Server



  Loaded: loaded (/etc/systemd/system/dynatrace-server.service; enabled; vendor preset: enabled)



  Active: active (running) since Tue 2019-07-09 08:39:01 UTC; 1 months 3 days ago



  Main PID: 2927 (code=exited, status=0/SUCCESS)



  Tasks: 475 (limit: 32768)



  Memory: 1.6G



  CPU: 1d 3h 10min 18.812s



  CGroup: /system.slice/dynatrace-server.service



  ├─15294 /opt/managed/server/dynatraceserver -vm=/opt/managed/jre/bin/java -vmargs -Xms2873M -Xmx2873M -XX:-OmitStackTraceInFastThrow -XX:+UseConcMarkSweepGC -XX:...



  └─15302 /opt/managed/jre/bin/java -Dcom.compuware.apm.WatchDogPort=50004 -classpath :/opt/managed/server/lib/ace-1.4.4-dt-2.0.jar:/opt/managed/server/lib/acme4j-...



  Aug 12 13:04:05 ip-10-176-32-69 sudo[20856]: pam_unix(sudo:session): session closed for user root



  Aug 12 13:04:05 ip-10-176-32-69 sudo[21125]:  dynaman : TTY=unknown ; PWD=/opt/managed/server ; USER=root ; COMMAND=/opt/dtrun/dtrun service dynatrace-cassandra status



  Aug 12 13:04:05 ip-10-176-32-69 sudo[21125]: pam_unix(sudo:session): session opened for user root by (uid=0)



  Aug 12 13:04:05 ip-10-176-32-69 sudo[21125]: pam_unix(sudo:session): session closed for user root



  Aug 12 13:04:05 ip-10-176-32-69 sudo[21389]:  dynaman : TTY=unknown ; PWD=/opt/managed/server ; USER=root ; COMMAND=/opt/dtrun/dtrun service dynatrace-security-gateway status



  Aug 12 13:04:05 ip-10-176-32-69 sudo[21389]: pam_unix(sudo:session): session opened for user root by (uid=0)



  Aug 12 13:04:05 ip-10-176-32-69 sudo[21389]: pam_unix(sudo:session): session closed for user root



  Aug 12 13:04:05 ip-10-176-32-69 sudo[21665]:  dynaman : TTY=unknown ; PWD=/opt/managed/server ; USER=root ; COMMAND=/opt/dtrun/dtrun service dynatrace-server status



  Aug 12 13:04:05 ip-10-176-32-69 sudo[21665]: pam_unix(sudo:session): session opened for user root by (uid=0)



  Aug 12 13:04:05 ip-10-176-32-69 sudo[21665]: pam_unix(sudo:session): session closed for user root



  Hint: Some lines were ellipsized, use -l to show in full.



  ● dynatrace-security-gateway.service - Dynatrace Active Gate



  Loaded: loaded (/etc/systemd/system/dynatrace-security-gateway.service; enabled; vendor preset: enabled)



  Active: active (running) since Tue 2019-07-09 08:39:37 UTC; 1 months 3 days ago



  Main PID: 16173 (dynatracegatewa)



  Tasks: 247 (limit: 32768)



  Memory: 410.7M



  CPU: 3h 44min 58.189s



  CGroup: /system.slice/dynatrace-security-gateway.service



  ├─16173 /opt/managed/security-Gateway/launcher/dynatracegateway -bg -vm=/opt/managed/jre/bin/java -vmargs -Xms638M -Xmx638M -XX:+UseConcMarkSweepGC -XX:CMSInitia...



  └─16182 /opt/managed/jre/bin/java -Dcom.compuware.apm.WatchDogPort=50005 -classpath /opt/managed/security-Gateway/lib/* -XX:ErrorFile=/var/opt/managed/log/securi...



  Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.



  ● dynatrace-nginx.service - Dynatrace NGINX



  Loaded: loaded (/etc/systemd/system/dynatrace-nginx.service; enabled; vendor preset: enabled)



  Active: active (running) since Tue 2019-07-09 08:39:46 UTC; 1 months 3 days ago



  Tasks: 14 (limit: 32768)



  Memory: 92.7M



  CPU: 40min 38.507s



  CGroup: /system.slice/dynatrace-nginx.service



  ├─17152 nginx: OneAgent companion process



  ├─17153 nginx: master process /opt/managed/nginx/sbin/nginx -c /opt/managed/nginx/conf/nginx.conf



  ├─17155 nginx: worker process



  ├─17156 nginx: worker process



  └─17164 /bin/bash /opt/managed/services/logs-watcher.sh watch-nginx /var/opt/managed/log/nginx/access.log /var/opt/managed/log/nginx/error.log



  └─19214 sleep 600



  Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.



  All services are OK
  ```
* **check**

  Проверяет статус правил iptables и процессов для Nodekeeper, Cassandra, Elasticsearch, ActiveGate, Watcher и NGINX.

  ```
  [root@localhost]# ./dynatrace.sh check
  ```

  Пример вывода dynatrace.sh status

  ```
  Checking rules in iptables ...



  Rule is present in 'filter': INPUT -p tcp -m tcp -m multiport --ports 443,5701:5711,7000:7001,7199,8018:8022,8443,9042,9200,9300,9998 -j DROP



  Rule is present in 'filter': OUTPUT -p tcp -m tcp -m multiport --ports 443,5701:5711,7000:7001,7199,8018:8022,8443,9042,9200,9300,9998 -j ACCEPT



  Rule is present in 'filter': INPUT -p tcp -m addrtype --src-type LOCAL -m tcp -m multiport --ports 443,5701:5711,7000:7001,7199,8018:8022,8443,9042,9200,9300,9998 -j ACCEPT



  Rule is present in 'filter': INPUT -s 10.10.10.10/32 -p tcp -m tcp -m multiport --ports 5701:5711,7000:7001,7199,8019,9042,9200,9300 -j ACCEPT



  Rule is present in 'filter': INPUT -p tcp -m tcp -m multiport --ports 443,8020:8022,8443,9998 -j ACCEPT



  Rule is present in 'filter': FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT



  Rule is present in 'nat': PREROUTING -p tcp -m addrtype --dst-type LOCAL -m tcp --dport 443 -j REDIRECT --to-ports 8022



  Rule is present in 'nat': OUTPUT -p tcp -m addrtype --dst-type LOCAL -m tcp --dport 443 -j REDIRECT --to-ports 8022



  All rules are active.



  Nodekeeper is running at launcher PID: 966, main PID: 552, listening on ports 8018



  Cassandra is running at launcher PID: 13721, main PID: 13690, listening on ports 9042



  Elasticsearch is running at launcher PID: 14834, main PID: 14802, listening on ports 9200,9300



  {



  "cluster_name" : "11bc1cd1e1-c222-33e3-4f44-0e0bc0dcdc0d",



  "status" : "yellow",



  "timed_out" : false,



  "number_of_nodes" : 1,



  "number_of_data_nodes" : 1,



  "active_primary_shards" : 299,



  "active_shards" : 299,



  "relocating_shards" : 0,



  "initializing_shards" : 0,



  "unassigned_shards" : 598,



  "delayed_unassigned_shards" : 0,



  "number_of_pending_tasks" : 0,



  "number_of_in_flight_fetch" : 0,



  "task_max_waiting_in_queue_millis" : 0,



  "active_shards_percent_as_number" : 33.33333333333333



  }



  Server is running at launcher PID: 15294, main PID: 15302, listening on ports 8021



  ActiveGate is running at launcher PID: 16173, main PID: 16182, listening on ports 8443



  Command to run as user dynaman: /opt/managed/services/logs-watcher.sh status



  Watcher is running, reporting in log: /var/opt/managed/log/logs-watcher-for-nginx-logs.log



  NGINX is running at launcher PID: 17153, main PID: 17155 17156, listening on ports 8022



  All processes are OK
  ```
* **pid**

  Выводит идентификатор процесса для всех необходимых служб Dynatrace, запущенных с помощью скрипта `dynatrace.sh`.

  ```
  [root@localhost]# ./dynatrace.sh pid
  ```

  Пример вывода dynatrace.sh status pid

  ```
  966 552 13721 13690 14834 14802 15294 15302 16173 16182 17153 17155 17156
  ```