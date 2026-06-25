---
title: Обновление кластера
source: https://docs.dynatrace.com/managed/managed-cluster/operation/update-cluster
scraped: 2026-05-12T11:07:54.718319
---

# Обновление кластера

# Обновление кластера

* How-to guide
* 5-min read
* Updated on Mar 02, 2026

Версии Dynatrace Managed выпускаются последовательно, однако при развёртывании можно пропустить некоторые версии для более быстрого обновления до новой. Для установленных версий Managed, допускающих более быстрое обновление, рекомендуется дождаться выхода целевой версии, если завершить процесс обновления в течение одного месяца невозможно. Логика версий представлена в следующей таблице.

| Установленная версия | Можно обновить до версии [1](#fn-1-1-def) |
| --- | --- |
| 1.306 | 1.308 |
| 1.304 | 1.306 (только до выхода 1.308); 1.308 |
| 1.302 | 1.304 |
| 1.300 | 1.302 (только до выхода 1.304); 1.304 |

1

Пропуск версии Managed возможен только в том случае, если номер установленной версии делится на 4.

Если установлена версия Managed 1.300 и необходимо обновиться до 1.304, можно пропустить версию 1.302 сразу после выхода 1.304. Если версия 1.304 ещё не вышла, сначала нужно обновиться до 1.302, а затем до 1.304. Однако после выхода версии 1.304 версия 1.302 будет недоступна для загрузки.

Можно ли всегда обновлять версии Managed последовательно, не пропуская ни одной?

Да, начиная с Dynatrace Managed версии 1.324 при использовании функции автоматического обновления у вас есть полный контроль над тем, до каких версий обновляться. Для последовательной установки каждой версии:

1. Войдите в **Cluster Management Console**.
2. Перейдите в **Settings** > **Automatic update**.
3. Включите **Run Dynatrace cluster updates sequentially without skipping a version**.

Как проверить установленную версию Managed?

Для проверки установленной версии Dynatrace Managed:

1. Войдите в **Cluster Management Console** или в одну из сред мониторинга.
2. Откройте **User menu** в правом верхнем углу.

   Номер версии Dynatrace Managed отображается в нижней части меню.

Альтернативно можно:

1. Войти в **Cluster Management Console** и выбрать **Deployment status**.
2. На вкладке **Cluster nodes** выбрать узел для просмотра его обзора.

   Номер версии Dynatrace Managed отображается как значение **Version**.

## Перед началом

Перед началом обновления кластера убедитесь, что выполняются следующие условия.

* На разделе, где установлен Dynatrace Managed, доступно не менее 5 ГБ свободного места на диске. Подробности см. в разделе [Требования к аппаратному обеспечению](/managed/managed-cluster/installation/managed-hardware-requirements#storage "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").
* Между обновлениями кластера выдерживается интервал 24 часа, чтобы все постобработочные шаги были завершены до начала следующего обновления.
* Если кластер содержит менее 3 узлов, Dynatrace Managed будет недоступен в процессе обновления.

## Обновление кластера

Существуют три подхода к обновлению кластера Managed. Выберите подход, наиболее подходящий для ваших задач.

[**Автоматическое обновление (рекомендуется)**](/managed/managed-cluster/operation/update-cluster#automatic-update "Learn how to update a Managed cluster and how to schedule an automatic update.")[**Полуавтоматическое обновление**](/managed/managed-cluster/operation/update-cluster#semi-automatic-update "Learn how to update a Managed cluster and how to schedule an automatic update.")[**Ручное обновление**](/managed/managed-cluster/operation/update-cluster#manual-update "Learn how to update a Managed cluster and how to schedule an automatic update.")

### Автоматическое обновление (рекомендуется)

По умолчанию пакеты установки загружаются автоматически из [Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") сразу после их доступности для вашего кластера.

После загрузки пакета установки требуется 24-часовой период ожидания перед запуском автоматического обновления. Это означает, что автоматическое обновление будет выполнено в течение первого запланированного окна обслуживания, наступающего через 24 часа после завершения загрузки. Например, если пакет установки загружен сегодня, а окно обслуживания запланировано на 1:00 завтра, обновление будет выполнено на следующей неделе, а не завтра, так как 24-часовой период ожидания не завершится к 1:00.

Задайте подходящее окно обслуживания для запуска автоматического обновления.

1. Войдите в **Cluster Management Console**.
2. Перейдите в **Settings** > **Automatic update**.
3. Убедитесь, что **Install Dynatrace cluster updates automatically during the selected maintenance window** включено.
4. Задайте время начала окна обслуживания. Обновление будет запущено в указанное время.

#### Запуск обновления вручную

Обновление можно запустить вручную в любое время за пределами заданного окна обслуживания через:

* **Automatic update** в **Cluster Management Console**.
* **Cluster API v1 — Updates — Trigger Upgrade**.

Если **Install Dynatrace cluster updates automatically during the selected maintenance window** отключено, обновление всегда нужно запускать вручную.

### Полуавтоматическое обновление

Если автоматическая загрузка пакетов установки отключена или отсутствует подключение к Mission Control, вы будете получать уведомления по электронной почте при появлении нового пакета установки. В этих письмах содержатся ссылки для загрузки пакетов установки. После загрузки пакетов установки их необходимо вручную загрузить в кластер.

Если необходим строгий контроль над загрузкой пакетов установки, можно отказаться от автоматической загрузки пакетов. В этом случае необходимо обновить лицензию. Обратитесь в службу поддержки Dynatrace за помощью.

Пример письма с уведомлением об обновлении

![Managed notification email](https://dt-cdn.net/images/managed-update-email-578-d1337b6a3a.png)

Managed notification email

Для ручной загрузки пакета установки в кластер:

1. Войдите в **Cluster Management Console**.
2. Перейдите в **Settings** > **Automatic update**.
3. Выберите **Upload installation package** для загрузки скачанного пакета в кластер.
4. После загрузки пакет установки автоматически распределяется по всем узлам кластера.

   * Если включено [автоматическое обновление](/managed/managed-cluster/operation/update-cluster#automatic-update "Learn how to update a Managed cluster and how to schedule an automatic update."), обновление запустится автоматически в заданное окно обслуживания.
   * Альтернативно можно [запустить обновление вручную](/managed/managed-cluster/operation/update-cluster#trigger-update-manually "Learn how to update a Managed cluster and how to schedule an automatic update.").

#### Ручное копирование пакетов установки

Пакет установки можно скопировать вручную в следующие директории на каждом узле кластера.

* Для обновлений кластера:

  ```
  /opt/dynatrace-managed/installer/upgrade
  ```
* Для OneAgent, RUM JavaScript, ActiveGate и Synthetic:

  ```
  /var/opt/dynatrace-managed/agents
  ```

### Ручное обновление

После ручной загрузки пакетов установки на каждый узел кластера необходимо запустить скрипт обновления на каждом узле. Поскольку обновляемый узел не работает, крайне важно обновлять по одному узлу за раз.

* Запустите скрипт обновления **на каждом узле** последовательно, **по одному узлу за раз**.
* Дождитесь завершения обновления узла, прежде чем начинать обновление следующего.

Для ручного обновления узла кластера следуйте приведённым ниже шагам и замените `<version>` на версию Dynatrace Managed.

1. Перейдите к скрипту обновления в:

   ```
   /opt/dynatrace-managed/installer/upgrade
   ```
2. Предоставьте скрипту обновления права на выполнение с помощью команды Linux `chmod`.

   ```
   [root@localhost]# chmod +x dynatrace-managed-<version>.sh
   ```
3. Выполните скрипт обновления от имени пользователя `root`.

   ```
   [root@localhost]# ./dynatrace-managed-<version>.sh --upgrade
   ```
4. После успешного завершения обновления перейдите к следующему узлу и повторите процедуру.

   Пример успешного обновления узла кластера

   ```
   [root@localhost]# ./dynatrace-managed-<version>.sh --upgrade



   Starting Dynatrace <version> installer ...                              OK



   Testing connection to Dynatrace Mission Control ...                     OK



   Verifying system compatibility ...                                      OK



   Verifying disk space ...                                                OK



   Verifying Dynatrace directories ...                                     OK



   Verifying system privileges ...                                         OK



   Verifying system connectivity ...                                       OK



   Stopping Dynatrace ...                                                  OK



   Preparing system user for Dynatrace ...                                 OK



   Initializing upgrade ...                                                OK



   Checking user permissions ...                                           OK



   Checking file ownership ...                                             OK



   Downloading Dynatrace OneAgent. This may take a few minutes ...         OK



   Upgrading. This may take a few minutes ...                              OK



   Preparing connectivity settings ...                                     OK



   Setting up cluster configuration. This may take a few minutes ...       OK



   Starting Dynatrace. This may take up to half an hour ...                OK



   Upgrade completed successfully after 8 minutes 50 seconds.



   Dynatrace binaries are located in directory /opt/dynatrace-managed



   Dynatrace data is located in directory /var/opt/dynatrace-managed



   Dynatrace metrics repository is located in directory /var/opt/dynatrace-managed/cassandra



   Dynatrace Elasticsearch store is located in directory /var/opt/dynatrace-managed/elasticsearch



   Dynatrace server store is located in directory /var/opt/dynatrace-managed/server



   Dynatrace session replay store is located in directory /var/opt/dynatrace-managed/server/replayData



   You can now log into your Dynatrace Server at https://10.10.10.10



   [root@localhost]#
   ```