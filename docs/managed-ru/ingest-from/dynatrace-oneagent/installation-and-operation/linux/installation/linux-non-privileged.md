---
title: Непривилегированный режим OneAgent на Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged
scraped: 2026-05-12T11:05:37.916125
---

# Непривилегированный режим OneAgent на Linux

# Непривилегированный режим OneAgent на Linux

* Чтение: 7 мин
* Опубликовано 19 июля 2017 г.

По умолчанию OneAgent устанавливается в непривилегированном режиме, в котором привилегии суперпользователя используются один раз для запуска процесса установки.

Затем OneAgent работает от имени непривилегированного пользователя, сохраняя полный набор функций.

## Системные требования

Чтобы установить OneAgent в непривилегированном режиме, ваша система должна соответствовать следующим требованиям:

* Файловая система должна поддерживать [расширенные атрибуты](https://man7.org/linux/man-pages/man7/xattr.7.html).
* В системе должен быть установлен `libcap2`. Например, в установке Red Hat Enterprise Linux 5 по умолчанию `libcap2` отсутствует.
* Файловая система не должна быть смонтирована как `noexec` или `nosuid`.
* Должны быть включены Linux Filesystem Capabilities. Например, в SUSE Linux Enterprise Server 11 Linux Filesystem Capabilities по умолчанию отключены. Подробнее см. [Непривилегированный режим и Linux Filesystem Capabilities](#cap) ниже.

Сведения о действиях мониторинга, выполняемых OneAgent, которые требуют привилегированного доступа, см. в [Безопасность OneAgent на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux#permissions "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Linux").

## Привилегии во время установки

При работе в непривилегированном режиме установщику OneAgent требуются привилегии суперпользователя, чтобы:

* Устанавливать file capabilities для двоичных файлов OneAgent, расположенных в `/opt/dynatrace/oneagent/agent/lib[64]/*`.
* Вызывать сервисный скрипт `oneagent` для запуска `oneagentwatchdog`.
* На системах с systemd взаимодействовать с демоном systemd через d-bus для выполнения следующих команд:

  + `systemctl <start|stop|enable|disable> oneagent.service`
  + `systemctl daemon-reload`
* На системах с SysV выполнять `/sbin/chkconfig` для добавления сервисного скрипта `oneagent` в автозапуск или его удаления.
* Выполнять запись в `/proc/sys/kernel/core_pattern`.

Привилегии суперпользователя сбрасываются при выполнении сервисного скрипта Dynatrace OneAgent:

* На системах с systemd непривилегированный пользователь включён в определение сервиса (unit-файл). Таким образом, демон systemd запускает сервисный скрипт OneAgent в непривилегированном режиме.
* На системах с SysV привилегии сбрасываются в скрипте при запуске процесса OneAgent Watchdog.

## Linux System Capabilities

Dynatrace OneAgent Watchdog запускает и выполняет все остальные процессы от имени непривилегированного пользователя без доступа суперпользователя. Двоичные файлы OneAgent используют следующие Linux System Capabilities.

| Двоичный файл | Linux System Capabilities |
| --- | --- |
| oneagentwatchdog | `cap_sys_resource`[1](#fn-1-1-def)- для установки [лимитов системных ресурсов](https://man7.org/linux/man-pages/man3/getrlimit.3p.html) при запуске процессов OneAgent |
| oneagentos | `cap_dac_override`[2](#fn-1-2-def) - для доступа к файловой системе `cap_chown`[2](#fn-1-2-def) [3](#fn-1-3-def) - для установки владельца файлов, заменяемых в файловой системе (например, двоичного файла `runc`) `cap_fowner` [2](#fn-1-2-def) - для установки владельца файлов, заменяемых в файловой системе `cap_sys_ptrace` - для чтения данных из псевдофайловой системы `/proc` и трассировки процессов `cap_sys_resource`[3](#fn-1-3-def) - для чтения лимитов ресурсов процессов `cap_setuid`[4](#fn-1-4-def) - для временного повышения привилегий для выполнения определённых операций; подробнее см. [Автоматические обновления и эксплуатация](#autoupdate) `cap_kill` [3](#fn-1-3-def) [5](#fn-1-5-def) [6](#fn-1-6-def) `cap_setfcap` [3](#fn-1-3-def) [5](#fn-1-5-def) [6](#fn-1-6-def) `cap_fsetid` [3](#fn-1-3-def) [5](#fn-1-5-def) [6](#fn-1-6-def) |
| oneagentnettracer | `cap_bpf` (ядро >=5.8)[7](#fn-1-7-def) `cap_perfmon` (ядро >=5.8)[7](#fn-1-7-def) `cap_sys_admin` (ядро <5.8 или когда `cap_bpf` явно заблокирован)[7](#fn-1-7-def) `cap_dac_override` `cap_sys_ptrace` `cap_sys_resource` |
| oneagentnetwork | `cap_net_raw` - для открытия raw-сокетов `cap_net_admin`[8](#fn-1-8-def)- для чтения информации о сетевых интерфейсах |
| oneagentloganalytics | `cap_dac_read_search` - для доступа ко всем логам, хранящимся на хосте `cap_sys_ptrace` - для чтения данных из псевдофайловой системы `/proc` |
| oneagentplugin | `cap_set_gid`[1](#fn-1-1-def)- для добавления docker в список дополнительных групп процесса, что позволяет получать данные контейнера |
| oneagenthelper[9](#fn-1-9-def) | `cap_sys_admin` - для системного вызова `mount()` `cap_dac_override` - для проверки и изменения файловых систем запущенных контейнеров `cap_sys_ptrace` - для трассировки демона `Docker` `cap_sys_chroot` - для системного вызова `chroot()` `cap_fowner` - для изменения владельца и прав файлов внутри файловой системы контейнера `cap_fsetid` - для изменения владельца и прав файлов внутри файловой системы контейнера |
| Установщик OneAgent, выполняемый во время автообновления | `cap_dac_override` - для доступа к файловой системе `cap_chown` - для доступа к файловой системе `cap_fowner` - для доступа к файловой системе `cap_fsetid` - для доступа к файловой системе `cap_kill` - для возможности отправлять сигналы всем запущенным процессам, например остановленным осиротевшим процессам OneAgent `cap_setfcap` - для установки file capabilities Linux Filesystem на двоичных файлах агента во время установки |
| oneagentosconfig | `cap_setuid`[6](#fn-1-6-def)- для выполнения привилегированных операций во время процесса установки `cap_setgid`[6](#fn-1-6-def)- для установки групповой принадлежности файлов во время процесса установки |
| oneagenteventstracer | `cap_sys_admin` - для системного вызова `perf_event_open()` `cap_dac_override` - для доступа к `/sys/kernel/debug/tracing` |
| oneagentdmidecode | `cap_dac_override` - для доступа к файловой системе |
| oneagentmntconstat | `cap_dac_read_search` - для получения статистики занятости диска с помощью `statvfs64()` `cap_sys_chroot` - для системного вызова `setns()` `cap_sys_admin` - для системного вызова `setns()` `cap_sys_ptrace` - для доступа к `/proc/1/ns` |
| oneagentebpfdiscovery | `cap_bpf` (ядро >=5.8)[7](#fn-1-7-def) `cap_perfmon` (ядро >=5.8)[7](#fn-1-7-def) `cap_sys_admin` (ядро <5.8 или когда `cap_bpf` явно заблокирован)[7](#fn-1-7-def) `cap_dac_override` - для доступа на запись в /sys/kernel/debug/tracing `cap_sys_resource` - для снятия ограничения на использование памяти программой bpf |

1

Требуется только на этапе инициализации и безусловно сбрасывается после.

2

Не используется, если [автообновления](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#enable-or-disable-auto-update "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.") и [автоматическая инъекция](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#injection-toggle "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.") отключены.

3

Хранится только в permitted-наборе и повышается до effective-набора при необходимости.

4

Только если ambient capabilities не поддерживаются.

5

Не используется, если [автообновления](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#enable-or-disable-auto-update "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.") отключены.

6

Только если ambient capabilities поддерживаются.

7

Только для ядер 5.8 и новее, если только использование непривилегированного `cap_bpf` не [заблокировано ОС](https://ubuntu.com/blog/whats-new-in-security-for-ubuntu-21-10), в таком случае выполняется откат к `cap_sys_admin`. Для более ранних версий ядра вместо этого включается `cap_sys_admin`.

8

Только на ядрах старше 2.6.33.

9

Не запускается, если [автоматическая инъекция](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#injection-toggle "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.") отключена.

Включение Linux Filesystem Capabilities

Linux Filesystem Capabilities необходимы для установки OneAgent в непривилегированном режиме. В SUSE Linux Enterprise Server 11 Linux Filesystem Capabilities по умолчанию отключены. Эти возможности также могут быть отключены в других поддерживаемых дистрибутивах Linux или в результате пользовательской настройки. Установщик OneAgent выводит следующее сообщение, если Linux Filesystem Capabilities отключены:

```
Warning: Failed to enable non-privileged mode, kernel does not support file capabilities.
```

Также можно проверить параметры загрузки ядра, чтобы узнать, включены ли Linux Filesystem Capabilities. Выполните следующую команду для проверки параметров загрузки ядра.

```
cat /proc/cmdline
```

Если в выводе присутствует `file_caps=1`, ваша настройка в порядке.

Чтобы включить Linux Filesystem Capabilities, добавьте `file_caps=1` в параметры загрузки ядра. Например, на SUSE Linux Enterprise Server 11 используйте [YaST](https://doc.opensuse.org/documentation/leap/reference/html/book-reference/cha-grub2.html#sec-grub2-yast2-config), отредактируйте параметры загрузки ядра, добавьте `file_caps=1` и перезагрузите машину.

## Привилегии во время автоматических обновлений и эксплуатации

Набор привилегий, требуемых OneAgent, зависит от того, поддерживает ли ядро Linux ambient capabilities. Как правило, ambient capabilities поддерживаются ядром 4.3+. Однако в случае Red Hat Enterprise Linux они могут поддерживаться и в более ранних версиях ядра из-за политики Red Hat по бэкпортированию патчей. Благодаря этому ambient capabilities поддерживаются версиями ядра вплоть до 3.10.x.

Ядра с ambient capabilities (версия 4.3+)

Ядра без ambient capabilities (версии с 2.6.26 по 4.3)

Во время автоматического обновления установщик запускается от имени непривилегированного `dtuser` с правильно установленными ambient capabilities. OneAgent не требует доступа root для выполнения автоматического обновления.

В Red Hat Enterprise Linux 7 слишком низкая версия `systemd` (v219 вместо требуемой v221), и чтобы иметь возможность выполнять автоматические обновления в непривилегированном режиме, мы временно повышаем привилегии для выполнения `systemctl <start|stop|enable|disable> oneagent.service`.

В большинстве случаев OneAgent работает от имени непривилегированного `dtuser`. Когда ядро не предоставляет ambient capabilities, он автоматически повышает свои привилегии до уровня суперпользователя с помощью `setuid(0)` в следующих случаях:

* Автоматические обновления OneAgent
* Генерация Host OSI ID на хостах Azure
* Определение свойств контейнеров Docker
* Самодиагностика

Если вы не хотите предоставлять OneAgent уровень разрешений суперпользователя, его можно отключить, добавив параметр `DISABLE_ROOT_FALLBACK=1` к команде установки OneAgent. Например:

`sudo /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh NON_ROOT_MODE=1 DISABLE_ROOT_FALLBACK=1`

В таких случаях необходимо выполнять [ручные обновления на отдельных хостах](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux#manual-update "Узнайте о различных способах обновления OneAgent на Linux."). Мы не рекомендуем использовать параметр `DISABLE_ROOT_FALLBACK=1` для OneAgent на хостах Azure или в контейнерах Docker.

## Как узнать, работает ли OneAgent в непривилегированном режиме?

Установщик выводит сообщение в конце установки OneAgent. В зависимости от версии ядра и поддержки им ambient capabilities вы увидите одно из следующих сообщений:

* `Non-privileged mode is enabled`  
  Ядро поддерживает ambient capabilities, доступ root не используется для обновлений или эксплуатации.
* `Enabled non-privileged mode, but ambient capabilities are not supported by kernel`  
  Ядро соответствует минимальной поддерживаемой версии, но из-за неподдерживаемых ambient capabilities OneAgent необходимо повышать привилегии в отдельных случаях, см. выше.
* `Failed to enable non-privileged mode`  
  Ядро не соответствует требованиям к минимальной версии для включения непривилегированного режима.