---
title: Настройка SELinux
source: https://docs.dynatrace.com/managed/managed-cluster/installation/selinux
scraped: 2026-05-12T11:53:36.960187
---

# Настройка SELinux

# Настройка SELinux

* How-to guide
* 3-min read
* Updated on May 08, 2026

SELinux (Security-Enhanced Linux) — это модуль безопасности ядра Linux, который использует обязательный контроль доступа (MAC) для ограничения процессов и пользователей в соответствии с политиками, определёнными системным администратором. Он доступен для большинства дистрибутивов Linux и включён по умолчанию в новых версиях Red Hat Enterprise Linux.

Dynatrace Managed автоматически определяет режим SELinux в процессе установки и применяет правильные контексты файлов, чтобы его службы могли работать в режиме `enforcing`. Для этого требуется утилита `semanage`. Установка завершится ошибкой, если пакет отсутствует.

* **Новые установки** — дополнительные действия не требуются.
* **Существующие установки** — после включения SELinux запустите скрипт `reconfigure.sh`:

  ```
  /opt/dynatrace-managed/installer/reconfigure.sh
  ```
* **Старые версии** — переключите режим SELinux на `permissive`.

## Включение SELinux

Перед включением SELinux убедитесь, что в вашей системе установлены следующие пакеты:

* `policycoreutils`
* `selinux-utils`
* `selinux-basics`

Приведённые ниже шаги описаны на примере Ubuntu.

1. Установите следующие пакеты с помощью команды `apt`:

   ```
   sudo apt install policycoreutils selinux-utils selinux-basics
   ```
2. Активируйте SELinux:

   ```
   sudo selinux-activate
   ```

   Должно появиться следующее сообщение:

   ```
   SE Linux is activated. You may need to reboot now.
   ```
3. Установите режим принудительного применения SELinux:

   ```
   sudo selinux-config-enforcing
   ```
4. Остановите службы Dynatrace Managed:

   ```
   ./dynatrace.sh stop
   ```

   Подробности см. в разделе [Запуск/остановка/перезапуск узла](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.").
5. Перезагрузите систему.  
   После перезагрузки запускается перемаркировка SELinux. По завершении система перезагрузится ещё раз автоматически.
6. Проверьте статус SELinux:

   ```
   # sestatus



   SELinux status:                 enabled



   SELinuxfs mount:                /sys/fs/selinux



   SELinux root directory:         /etc/selinux



   Loaded policy name:             default



   Current mode:                   enforcing



   Mode from config file:          error (Success)



   Policy MLS status:              enabled



   Policy deny_unknown status:     allowed



   Memory protection checking:     requested (insecure)



   Max kernel policy version:      31
   ```
7. Перенастройте Dynatrace Managed с включённым SELinux:

   ```
   /opt/dynatrace-managed/installer/reconfigure.sh
   ```

## Отключение SELinux

Для отключения SELinux выполните следующие шаги:

1. Откройте `/etc/selinux/config` и установите для `SELINUX` значение `disabled`:

   ```
   SELINUX=disabled
   ```
2. Остановите службы Dynatrace Managed:

   ```
   ./dynatrace.sh stop
   ```

   Подробности см. в разделе [Запуск/остановка/перезапуск узла](/managed/managed-cluster/operation/start-stop-restart-node "Properly shut down and restart Dynatrace Managed nodes using command line parameters.").
3. Перезагрузите систему.
4. Перенастройте Dynatrace Managed после отключения SELinux:

   ```
   /opt/dynatrace-managed/installer/reconfigure.sh
   ```

## Изменения операционной системы

Если SELinux находится в режиме `enforcing` и для установки или хранилища используются пользовательские пути, установщик Managed обновляет контекст файлов всех директорий Dynatrace Managed до `usr_t`. Для пользовательского пути `/custom-dir/dynatrace-managed` выполняются следующие команды:

```
semanage fcontext -a -t usr_t "/custom-dir/dynatrace-managed"
```

```
semanage fcontext -a -t usr_t "/custom-dir/dynatrace-managed/.*"
```

```
restorecon -R /custom-dir/dynatrace-managed
```