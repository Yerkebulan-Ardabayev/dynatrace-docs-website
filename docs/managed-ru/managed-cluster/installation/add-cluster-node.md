---
title: Добавление узла кластера Managed
source: https://docs.dynatrace.com/managed/managed-cluster/installation/add-cluster-node
scraped: 2026-05-12T11:06:39.697766
---

# Add a Managed Cluster node

# Add a Managed Cluster node

* How-to guide
* 3-min read
* Updated on May 08, 2026

Вы можете масштабировать кластер Managed, добавляя узлы через Cluster Management Console. Для запуска установщика на целевом хосте требуются права root.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Download installer**](/managed/managed-cluster/installation/add-cluster-node#download-installer "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Run installer**](/managed/managed-cluster/installation/add-cluster-node#run-installer "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Finalize**](/managed/managed-cluster/installation/add-cluster-node#finalize "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.")

* Нельзя добавлять новые узлы кластера до завершения синхронизации.
* После удаления узла кластера следует подождать 72 часа перед установкой нового узла на хост с тем же IP-адресом (например, при переустановке на тот же хост).

## Шаг 1. Загрузка установщика

1. Войдите в **Cluster Management Console**.
2. Перейдите в раздел **Deployment Status** и нажмите **Add new cluster node**.
3. Скопируйте командную строку `wget` из поля **Run this command on the target host** и вставьте её в окно терминала. Дождитесь завершения загрузки.

## Шаг 2. Запуск установщика

1. Выполните одну из следующих команд из директории, куда был загружен установочный скрипт. Требуются права root.

   Замените `<version>` на версию Dynatrace Managed.

   * Ubuntu Server

     ```
     sudo /bin/sh dynatrace-managed-<version>.sh
     ```
   * Red Hat Enterprise Linux

     ```
     su -c '/bin/sh dynatrace-managed-<version>.sh'
     ```
   * Другие дистрибутивы Linux с сессией root

     ```
     /bin/sh dynatrace-managed-<version>.sh
     ```
2. Введите `Accept`, чтобы принять [Условия использования](https://www.dynatrace.com/eula/managed/) Dynatrace Managed. Установка не продолжится до завершения этого шага. Чтобы прервать установку, нажмите `Ctrl+C`.
3. Подтвердите запрашиваемые значения (путь установки, учётная запись пользователя и другие), нажав `Enter`. Чтобы переопределить значение, введите нужный вариант и нажмите `Enter`.

## Шаг 3. Финализация

После добавления нового узла он отображается в Cluster Management Console со статусом `joining`. Полная синхронизация данных может занять несколько часов. Для отслеживания прогресса синхронизации узла выполните:

```
[root@host]# /opt/dynatrace-managed/utils/cassandra-nodetool.sh status
```

Пример ответа:

```
Datacenter: datacenter-1



=====================



Status=Up/Down



|/ State=Normal/Leaving/Joining/Moving



--  Address         Load     Tokens       Owns (effective)  Host ID                               Rack



UN  1.6.1.6  349.88 GiB       256          100.0%           aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee  rack1



UN  1.6.2.2  358.2  GiB       256          100.0%           zzzzzzzz-xxxx-cccc-vvvv-ffffffffffff  rack1



UJ  1.6.3.9  278.75 GiB       256          ?                qqqqqqqq-wwww-eeee-rrrr-rrrrrrrrrrrr  rack1
```

Где `UJ` обозначает узел в состоянии `joining` (присоединяется).

Как читать ответ?

Значение `100.0%` в столбце `Owns (effective)` отображается только для кластеров с тремя узлами и менее.

Если узлов более трёх, процент рассчитывается по формуле:

`(3/количество_узлов)*100%`

Пока узел присоединяется, в столбце `Owns (effective)` отображается знак вопроса (`?`). После масштабирования с двух до трёх узлов значение меняется на `100.0%`. Для дополнительных узлов значение рассчитывается по приведённой выше формуле.

В конфигурации с несколькими стойками формула для столбца `Owns (effective)` изменяется на `(100 / количество_узлов)%`. Первый узел в стойке показывает `100.0%`. При добавлении второго узла отображается `50.0%`, третьего — `33.3%`.

Подсказки

* Можно увидеть неравные значения в столбце `Owns (effective)`, например `75.1%` вместо `75.0%`. Это нормально, поскольку данные нельзя разделить на равные части между узлами. Как следствие, значение `Load` может незначительно отличаться между узлами.
* Cassandra не выполняет автоматическую балансировку данных на диске во всём кластере после добавления узла. Значение `Owns (effective)` уменьшается по мере добавления узлов в кластер. Это ожидаемое поведение, указывающее на снижение ответственности за данные на каждый узел.
* Соответственно, данные на диске (`Load`) не уменьшаются автоматически на всех узлах кластера. Чтобы дать Cassandra команду удалить данные с локального узла, за которые она больше не отвечает, можно выполнить команду очистки.

  Перед выполнением команды учтите следующее:

  + Эта команда может выполняться несколько часов, так как Cassandra должна переписать все данные на локальном диске. В этот период утилизация CPU и диска локально на узле, выполняющем команду, возрастёт, однако производительность других узлов не пострадает.
  + Чтобы избежать многократной перезаписи данных, выполняйте очистку только после добавления всех желаемых узлов. Например, если планируется масштабирование кластера с трёх до шести узлов, очистку следует запускать только после успешного добавления шестого узла. Команду очистки необходимо выполнить на всех пяти оставшихся узлах, так как она является операцией, локальной для узла.

  **Команда очистки:**

  ```
  /opt/dynatrace-managed/utils/cassandra-nodetool.sh
  ```

## Часто задаваемые вопросы

### Добавление узла с использованием процедуры установки кластера Managed

Да, узел можно добавить с использованием той же процедуры, что и для [установки кластера Managed](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration."). Отличие состоит в том, что установщик спрашивает, следует ли добавить узел в существующий кластер (необходимо ввести IP-адрес существующего узла кластера Managed) или создать новый кластер. В качестве альтернативы можно использовать параметр `--seed-auth`, чтобы пропустить этот запрос и автоматически добавить узел в существующий кластер.

### Использование системы управления привилегиями, отличной от sudo

Да, можно использовать `pbrun`, однако необходимо предоставить пользователю Dynatrace разрешение на запуск `/opt/dtrun/dtrun *`. Укажите пользователя, устанавливающего Dynatrace Managed, и команду, заменяющую `sudo`. Обратите внимание, что `<version>` представляет номер версии Dynatrace Managed.

```
/bin/sh dynatrace-managed-<version>.sh --system-user dynatrace:dynatrace --sudo-cmd  "/usr/bin/pbrun \$CMD"
```

В целях обслуживания добавьте следующие пути к скриптам в конфигурацию системы управления привилегиями:

* `/opt/dynatrace-managed/uninstall-dynatrace.sh`
* `/opt/dynatrace-managed/launcher/*`
* `/opt/dynatrace-managed/utils/*`

Для остановки всех процессов Dynatrace Managed на узле выполните:

```
pbrun /opt/dynatrace-managed/launcher/dynatrace.sh stop
```

Не удаляйте и не перезаписывайте `dtrun`, так как он необходим для процедур установки и обновления. Установщик вызывает `dtrun` без аргументов для проверки наличия у пользователя прав администратора, однако при нормальной эксплуатации Dynatrace вызывает `dtrun` с аргументами для фактического выполнения команд.