---
title: Настройка расширенных разрешений в Dynatrace Managed
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/managed-elevated-permissions
scraped: 2026-05-12T11:52:56.055954
---

# Настройка расширенных разрешений в Dynatrace Managed

# Настройка расширенных разрешений в Dynatrace Managed

* Published Apr 07, 2022

По умолчанию кластер Dynatrace Managed использует `sudo` для повышения привилегий при выполнении отдельных операций обслуживания. При запуске установки для настройки пользователей, разрешений и сервисов никаких дополнительных действий не требуется. Однако если `sudo` недоступен в вашей операционной системе или требуется использовать альтернативную команду для повышения привилегий, их необходимо указать во время установки.

* В интерактивном режиме, при запросе о расширенных разрешениях, передайте префикс команды с программой, например `pbrun`, `sesudo` или `suexec`
* В тихом режиме этот параметр можно задать через [настраиваемую установку](/managed/managed-cluster/installation/customize-managed-cluster-install#other "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.")

Во всех примерах команд на этой странице предполагается следующее:

* `dynatrace` (по умолчанию) — пользователь, запускающий все OS-сервисы Dynatrace
* Dynatrace Managed установлен в `/opt/dynatrace-managed/`
* Каталог данных — `/var/opt/dynatrace-managed/`

Если ваша конфигурация отличается, скорректируйте действия соответствующим образом.

## Когда требуются расширенные разрешения

OS-пользователю, запускающему сервисы Dynatrace Managed, необходимы расширенные разрешения для выполнения следующих задач:

* Запуск скрипта установки или перенастройки
* Добавление или удаление узла кластера
* Запуск, остановка, перезапуск или проверка статуса сервисов

Полный список команд, требующих расширенных разрешений, см. в файле `/opt/dtrun/dtrun.conf`. Каталог `/opt/dtrun` и все файлы внутри принадлежат пользователю root из соображений безопасности.

## Перенастройка команды dtrun sudo

Для упрощения управления OS-разрешениями Dynatrace Managed использует единый скрипт для запуска всех команд, требующих расширенных привилегий. Скрипт **dtrun** является обёрткой для sudo или любой другой команды, которую вы предоставите при установке. Расположение `dtrun` — `/opt/dtrun/dtrun`, а все команды, которые `dtrun` может выполнять, перечислены в `/opt/dtrun/dtrun.conf`. Выполняться могут только скрипты и команды, включённые в `/opt/dtrun/dtrun.conf`.

Если кластеру необходимо выполнить команду от имени пользователя root (например, для добавления правил iptables, перезапуска компонента или запуска модуля обновления), он использует SUDO\_COMMAND, заданный при установке, для попытки получить расширенные привилегии.
Проблемы также можно найти в файле журнала `/var/opt/dynatrace-managed/log/dtrun.log`.

Если необходимо перенастроить существующую установку для использования альтернативы `sudo`, можно запустить скрипт перенастройки. Например, для замены команды sudo на `pbrun` используйте этот скрипт для повторного запуска установщика:

```
sudo /opt/dynatrace-managed/installer/reconfigure.sh --sudo-cmd "/usr/bin/pbrun \$CMD"
```

## Устранение неполадок

Неправильно настроенные разрешения могут привести к различным проблемам, например с сервисами Dynatrace Managed или сетью.
При наличии проблем с разрешениями в журналах установки появятся следующие записи:

```
sudo: pam_open_session: System error



sudo: policy plugin failed session initialization
```

Кроме того, проблемы могут проявляться в следующих журналах:

* `/var/opt/dynatrace-managed/log/dtrun.log` (журналы dtrun)
* `/var/opt/dynatrace-managed/log/launch-logging.log` (журналы скрипта запуска сервисов)

При устранении неполадок с sudo или расширенными разрешениями рекомендуется выполнить всю конфигурацию сразу и сравнить результаты.
От имени пользователя root все приведённые ниже команды должны выдавать вывод:

```
cat /etc/sudoers | grep -i include



cat /etc/sudoers.d/dynatrace



su - dynatrace -s /bin/bash -c 'sudo /opt/dtrun/dtrun iptables -L -n'



cat /etc/sudoers | grep dynatrace



cat /etc/passwd | grep dynatrace



cat /etc/shadow | grep dynatrace



chage -l dynatrace
```

Команда `chage` сообщает, не истекает ли срок действия пароля (это тоже может вызвать проблемы с доступом sudo).

При добавлении узла в кластер от имени пользователя root может возникнуть следующая ошибка аутентификации:

```
Installation failed, with status: installer unpacked, system verified, connected to Mission Control, connected to Dynatrace cluster, added to Dynatrace cluster, agent downloaded after 2 minutes 44 seconds.



Exit code: 5



Errors:



Installation failed, with error Dtrun doesn't work properly, check if command "/opt/dtrun/dtrun" is permitted to run with elevated privileges. The dtrun validation failed with error: sudo: PAM account management error: Authentication service cannot retrieve authentication info
```

В данном случае причиной может быть то, что пользователь `dynatrace` не может получить расширенные привилегии для команды `/opt/dtrun/dtrun`. Во время установки Managed эти привилегии автоматически добавляются в конфигурацию sudo (если она присутствует и активна в системе) следующим образом:

1. Установщик ищет следующую строку в файле `/etc/sudoers`:

   ```
   #includedir /etc/sudoers.d
   ```

   Если она отсутствует, она добавляется в конец файла.
2. Установщик создаёт файл конфигурации sudo `/etc/sudoers.d/dynatrace` со следующим содержимым:

   ```
   Defaults:dynatrace !requiretty



   Defaults:dynatrace !env_reset



   dynatrace ALL=(root:root) NOPASSWD:/opt/dtrun/dtrun
   ```

   Эти настройки предоставляют пользователю `dynatrace` возможность запускать команду `/opt/dtrun/dtrun` с правами root без запроса пароля.

В версии `sudo-1.8.23-1.el7` и выше стек PAM account оценивается, и применяются все ограничения учётных записей через PAM. Это затрагивает контроль доступа на основе хоста, а также истечение срока действия паролей.

Добавьте sudo в список разрешённых сервисов в правилах контроля доступа и убедитесь, что у пользователей нет просроченных паролей, даже в случаях, когда для входа используются SSH-ключи.

При выполнении дополнительных проверок безопасности для контроля допустимых действий `dtrun` можно легко убедиться, что `sudo` работает корректно, выполнив следующую команду от имени пользователя root:

```
su - dynatrace -s /bin/bash -c 'sudo /opt/dtrun/dtrun service dynatrace-server status'
```

Следующая команда является примером проверки повышения привилегий с использованием альтернативы `sudo` — `pbrun`:

```
su - dynatrace -s /bin/bash -c 'pbrun /opt/dtrun/dtrun service dynatrace-server status'
```