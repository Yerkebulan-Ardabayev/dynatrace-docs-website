---
title: Настройка повышенных прав доступа
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-elevated-permissions
---

# Настройка повышенных прав доступа

# Настройка повышенных прав доступа

* Практическое руководство
* Чтение: 4 мин.
* Обновлено 18 июня 2026 г.

Чтобы настроить, как Dynatrace Managed повышает права операционной системы для операций обслуживания, нужно выполнить следующие шаги.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Обзор повышенных прав доступа**](/managed/managed-cluster/configuration/configure-elevated-permissions#review-elevated-permissions "Learn how to configure elevated permissions in Dynatrace Managed, including using sudo, pbrun, or other alternatives, and how to troubleshoot permission issues.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка во время установки**](/managed/managed-cluster/configuration/configure-elevated-permissions#configure-during-installation "Learn how to configure elevated permissions in Dynatrace Managed, including using sudo, pbrun, or other alternatives, and how to troubleshoot permission issues.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Переконфигурация dtrun**](/managed/managed-cluster/configuration/configure-elevated-permissions#reconfigure-dtrun "Learn how to configure elevated permissions in Dynatrace Managed, including using sudo, pbrun, or other alternatives, and how to troubleshoot permission issues.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Проверка повышенных прав доступа**](/managed/managed-cluster/configuration/configure-elevated-permissions#verify-elevated-permissions "Learn how to configure elevated permissions in Dynatrace Managed, including using sudo, pbrun, or other alternatives, and how to troubleshoot permission issues.")

Примеры команд на этой странице предполагают следующую конфигурацию:

* `dynatrace` (по умолчанию), это пользователь, от имени которого запускаются все службы ОС Dynatrace
* Каталог установки Dynatrace Managed: `/opt/dynatrace-managed/`
* Каталог данных: `/var/opt/dynatrace-managed/`

Если конфигурация отличается, действия нужно скорректировать соответственно.

## Шаг 1. Обзор повышенных прав доступа

Пользователю ОС, от имени которого запускаются службы Dynatrace Managed, нужны повышенные права для выполнения следующих задач:

* Запуск скрипта установки или переконфигурации
* Добавление или удаление узла Managed Cluster
* Запуск, остановка, перезапуск или проверка статуса служб

Полный список команд, требующих повышенных прав, можно найти в файле `/opt/dtrun/dtrun.conf`. По соображениям безопасности каталог `/opt/dtrun` и все файлы внутри него принадлежат пользователю root.

## Шаг 2. Настройка во время установки

По умолчанию Dynatrace Managed использует `sudo` для повышения прав при операциях обслуживания. Если `sudo` доступен и разрешён политиками операционной системы, настраивать другую команду не нужно.

Если `sudo` недоступен или политики операционной системы требуют другую команду повышения прав, эту команду нужно указать во время установки.

* В интерактивном режиме нужно ввести префикс команды, включающий программу вроде `pbrun`, `sesudo` или `suexec`, когда установщик спросит о повышенных правах.
* В тихом режиме параметр указывается через [настраиваемую установку](/managed/managed-cluster/installation/customize-managed-cluster-install#other "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.").

## Шаг 3. Переконфигурация dtrun

Dynatrace Managed использует скрипт `dtrun` для запуска команд, требующих повышенных прав. Скрипт `dtrun` оборачивает `sudo` или альтернативную команду, указанную во время установки.

Расположение `dtrun`: `/opt/dtrun/dtrun`. Файл `/opt/dtrun/dtrun.conf` содержит список команд, которые может запускать `dtrun`. `dtrun` может запускать только скрипты и команды, включённые в `/opt/dtrun/dtrun.conf`.

Если узлу Managed Cluster нужно запустить команду от имени пользователя root, Managed Cluster использует `SUDO_COMMAND`, заданную во время установки, для получения повышенных прав. Примеры: добавление правил iptables, перезапуск компонента или запуск апгрейдера.

Если существующую установку нужно переконфигурировать для использования альтернативы `sudo`, можно запустить скрипт переконфигурации. Например, чтобы изменить команду sudo на `pbrun`, используется следующий скрипт для повторного запуска установщика:

```
sudo /opt/dynatrace-managed/installer/reconfigure.sh --sudo-cmd "/usr/bin/pbrun \$CMD"
```

## Шаг 4. Проверка повышенных прав доступа

Нужно проверить, что `dtrun` может запускать команды с повышенными правами.

Чтобы проверить повышение прав через `sudo`, нужно выполнить следующую команду от имени пользователя root:

```
su - dynatrace -s /bin/bash -c 'sudo /opt/dtrun/dtrun service dynatrace-server status'
```

Чтобы проверить повышение прав через альтернативу `sudo`, `pbrun`, нужно выполнить следующую команду от имени пользователя root:

```
su - dynatrace -s /bin/bash -c 'pbrun /opt/dtrun/dtrun service dynatrace-server status'
```

После успешной проверки Dynatrace Managed может использовать настроенную команду повышения прав для операций обслуживания.

## Часто задаваемые вопросы

Где найти журналы повышения прав доступа

Если возникла проблема с правами, журналы установки могут содержать записи вроде:

```
sudo: pam_open_session: System error



sudo: policy plugin failed session initialization
```

Проблемы с повышением прав нужно искать в следующих журналах:

* `/var/opt/dynatrace-managed/log/dtrun.log` (журналы dtrun)
* `/var/opt/dynatrace-managed/log/launch-logging.log` (журналы скрипта запуска служб)

Как проверить конфигурацию sudo

При устранении проблем с `sudo` или повышением прав нужно выполнить полную проверку конфигурации и сравнить вывод. Следующие команды должны выдавать вывод при запуске от имени пользователя root:

```
cat /etc/sudoers | grep -i include



cat /etc/sudoers.d/dynatrace



su - dynatrace -s /bin/bash -c 'sudo /opt/dtrun/dtrun iptables -L -n'



cat /etc/sudoers | grep dynatrace



cat /etc/passwd | grep dynatrace



cat /etc/shadow | grep dynatrace



chage -l dynatrace
```

Команда `chage` показывает, скоро ли истекает срок действия пароля. Истечение срока действия пароля может вызывать проблемы с доступом sudo.

Почему установка узла завершается ошибкой управления учётной записью

При добавлении узла в Managed Cluster от имени пользователя root может возникнуть следующая ошибка аутентификации:

```
Installation failed, with status: installer unpacked, system verified, connected to Mission Control, connected to Dynatrace cluster, added to Dynatrace cluster, agent downloaded after 2 minutes 44 seconds.



Exit code: 5



Errors:



Installation failed, with error Dtrun doesn't work properly, check if command "/opt/dtrun/dtrun" is permitted to run with elevated privileges. The dtrun validation failed with error: sudo: PAM account management error: Authentication service cannot retrieve authentication info
```

Причина может быть в том, что пользователь `dynatrace` не может получить повышенные права для `/opt/dtrun/dtrun`. Во время установки Managed установщик автоматически добавляет эти права в конфигурацию sudo, если sudo присутствует и активен в системе.

1. Установщик ищет следующую строку в файле `/etc/sudoers`:

   ```
   #includedir /etc/sudoers.d
   ```

   Если строки нет, установщик добавляет её в конец файла.
2. Установщик создаёт файл конфигурации sudo `/etc/sudoers.d/dynatrace` со следующим содержимым:

   ```
   Defaults:dynatrace !requiretty



   Defaults:dynatrace !env_reset



   dynatrace ALL=(root:root) NOPASSWD:/opt/dtrun/dtrun
   ```

   Эти настройки позволяют пользователю `dynatrace` запускать `/opt/dtrun/dtrun` с правами root без ввода пароля.

`sudo-1.8.23-1.el7` и более поздние версии проверяют стек учётных записей PAM и применяют ограничения учётных записей через PAM. Проверка стека учётных записей PAM влияет на контроль доступа по узлам и на истечение срока действия пароля.

Нужно добавить sudo в список разрешённых служб в правилах контроля доступа. Нужно убедиться, что у пользователей нет истёкшего пароля, даже если они входят по SSH-ключам.

Как устранить неполадки с ограничениями команд dtrun

При выполнении дополнительных проверок безопасности для контроля того, что может запускать `dtrun`, нужно проверить, что настроенная команда повышения прав по-прежнему работает.

Чтобы проверить `sudo`, нужно выполнить следующую команду от имени пользователя root:

```
su - dynatrace -s /bin/bash -c 'sudo /opt/dtrun/dtrun service dynatrace-server status'
```

Чтобы проверить альтернативу `sudo`, `pbrun`, нужно выполнить следующую команду от имени пользователя root:

```
su - dynatrace -s /bin/bash -c 'pbrun /opt/dtrun/dtrun service dynatrace-server status'
```