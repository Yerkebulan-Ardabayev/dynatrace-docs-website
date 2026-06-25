---
title: Доступность хоста
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring/host-availability
scraped: 2026-05-12T12:07:18.763522
---

# Host availability

# Доступность хоста

* How-to guide
* 5-min read
* Updated on Nov 26, 2024

Доступность хоста можно отслеживать на странице обзора выбранного хоста. Плитка **Host availability** отображает процент выбранного временного диапазона, в течение которого хост был онлайн и реагировал на запросы.

## Проверка состояния доступности хоста

Чтобы проверить состояние доступности хоста:

1. Перейдите в **Hosts**, чтобы просмотреть список всех машин (физических и виртуальных) в вашей среде с установленным OneAgent.
2. Выберите хост для перехода на страницу его обзора, где можно просмотреть сведения о хосте, включая все доступные метрики.
3. На панели уведомлений **Availability** показывает процент времени, в течение которого хост был онлайн и реагировал на запросы. Dynatrace обнаруживает и отображает завершения работы ОС (включая перезагрузки) и периоды недоступности хоста (например, при его неожиданном отключении).

   При потере соединения с хостом OneAgent кэширует все собранные данные в буфере объёмом 55 минут. После восстановления соединения данные для хоста собираются из содержимого буфера и обновляются.

   В данном примере панель уведомлений отображает уровень доступности 99,74% для выбранного хоста за выбранный временной диапазон.

   ![Host availability on the notifications bar](https://dt-cdn.net/images/notifications-bar-availability-854-e927dcebcb.png)

   Host availability on the notifications bar
4. Выберите **Availability** на панели уведомлений, чтобы открыть панель **Host availability** с графиком доступности хоста во времени.

   В данном примере легенда показывает три различных состояния доступности хоста, возникших за выбранный временной диапазон.

   ![Host page detail - online availability](https://dt-cdn.net/images/image-3-757-d2642a2b5d.png)

   Host page detail - online availability

## Состояния доступности хоста

| Состояние доступности | Описание |
| --- | --- |
| **up** | Хост работает; OneAgent активен и отправляет данные. При потере соединения с хостом OneAgent отправит все закэшированные метрики после его восстановления. |
| **no\_data** | Хост работает и OneAgent активен, но данные не отправляются. Это состояние также устанавливается, когда сбор данных мониторинга занимает слишком много времени (например, при зависании OneAgent). |
| **no\_data\_agent\_inactive** | Хост работает, OneAgent неактивен, данные не отправляются, поскольку OneAgent отключён вручную в настройках конфигурации. |
| **shutdown\_host** | Хост был остановлен в результате ожидаемого завершения работы или перезагрузки ОС. |
| **unmonitored\_agent\_stopped** | Хост не отслеживается, поскольку OneAgent неактивен. Подробнее см. в разделе [Проверка настроек мониторинга OneAgent для хоста](#check-monitoring-settings). |
| **unmonitored\_agent\_upgrade** | Хост не отслеживается, поскольку выполняется обновление OneAgent. |
| **unmonitored\_agent\_uninstalled** | Хост не отслеживается, поскольку OneAgent был удалён. |
| **reboot\_graceful** | Хост перезагружен после плановой остановки ОС. |
| **reboot\_ungraceful** | Хост перезагружен после внезапной остановки ОС. Это может быть вызвано такими событиями, как отключение питания или системный сбой. |

### Проверка настроек мониторинга OneAgent для хоста

Чтобы проверить или изменить настройки мониторинга для конкретного хоста:

1. Перейдите в **Settings** > **Monitoring** > **Monitoring overview**.
2. Выберите вкладку **Hosts**.
3. Найдите хост и проверьте столбец **Summary**, чтобы убедиться, что он отслеживается.
4. Нажмите кнопку редактирования ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") и проверьте настройки на вкладке **Monitoring**.

## События доступности хоста

При изменении состояния доступности (например, при остановке хоста) OneAgent отправляет события доступности. Чтобы просмотреть все события для конкретного хоста, перейдите в **Hosts**, выберите нужный хост, а затем перейдите на плитку **Events**.

Типы событий:

* Reboot graceful (плановая перезагрузка)
* Reboot ungraceful (внеплановая перезагрузка)
* Graceful shutdown (плановая остановка)

  + K8s node termination (подэлемент Graceful shutdown, специфичный для сред Kubernetes)

### Reboot graceful/ungraceful

После перезапуска системы OneAgent проверяет системные файлы журналов или события, чтобы определить, была ли остановка хоста плановой или внезапной.

* Graceful reboot означает, что хост был перезагружен после ожидаемого завершения работы ОС.

  ![Host availability event - graceful reboot](https://dt-cdn.net/images/host-availability-graceful-reboot-1027-9c5a256356.png)

  Host availability event - graceful reboot
* Ungraceful reboot означает, что хост был перезагружен после неожиданного завершения работы ОС, вызванного такими событиями, как отключение питания или системный сбой.

  ![Host availability event - ungraceful reboot](https://dt-cdn.net/images/host-availability-ungraceful-reboot-1007-a3958d05f4.png)

  Host availability event - ungraceful reboot

События reboot graceful и reboot ungraceful поддерживаются в операционных системах Linux, AIX и Windows.

### Graceful shutdown

Когда хост готовится к остановке, OneAgent отправляет соответствующее событие остановки хоста.

![Host availability event - graceful shutdown](https://dt-cdn.net/images/host-availability-graceful-shutdown-compact-1450-1488a61897.png)

Host availability event - graceful shutdown

Событие graceful shutdown поддерживается в операционных системах Linux, AIX и Windows.

### K8s node termination

K8s node termination поддерживается в операционной системе Linux. Это событие генерируется на хостах, на которых обнаружен движок Kubernetes. OneAgent создаёт блокировку inhibitor для получения дополнительного времени при остановке.

Убедитесь, что у OneAgent достаточно прав для регистрации блокировки inhibitor.

Если в вашем дистрибутиве Linux возникают проблемы с соединением или сетевой менеджер завершает работу быстрее, чем успевает отправить событие, событие остановки может не быть отправлено своевременно.

![Host availability event - Kubernetes node shutdown](https://dt-cdn.net/images/host-availability-k8s-node-shutdown-969-3fd821c153.png)

Host availability event - Kubernetes node shutdown

## Окна обслуживания

Окна обслуживания — это периоды времени, в которые запланировано выполнение работ по обслуживанию в отслеживаемых средах. Эти окна можно использовать для приостановки оповещений, сбора файлов журналов, профилирования системы и других операций. Подробнее см. в разделе [Maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Understand when to use a maintenance window. Read about the supported maintenance window types.").

Окна обслуживания отображаются в виде серых полос в верхней части плиток **Host availability** и **Host performance** на странице обзора хоста.

![Availability tile maintenance window](https://dt-cdn.net/images/image-938-c6ad83866e.png)

Availability tile maintenance window

![Host performance maintenance window](https://dt-cdn.net/images/image-1923-d376018fd7.png)

Host performance maintenance window