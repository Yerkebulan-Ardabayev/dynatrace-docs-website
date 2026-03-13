---
title: How to enable deep monitoring for applications confined by AppArmor
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/how-to-enable-deep-monitoring-for-applications-confined-by-apparmor
scraped: 2026-03-06T21:18:55.494155
---

# Как включить глубокий мониторинг для приложений, ограниченных AppArmor

# Как включить глубокий мониторинг для приложений, ограниченных AppArmor

* Latest Dynatrace
* 2-min read
* Published Aug 08, 2017

AppArmor — это система обязательного контроля доступа, ограничивающая приложения набором ресурсов. Для каждого ограниченного приложения существует профиль, определяющий, какие операции приложению разрешено выполнять, а также пути в файловой системе, к которым оно имеет доступ. Чтобы включить глубокий мониторинг приложений, ограниченных AppArmor, в профили этих приложений необходимо включить пользовательский набор правил для OneAgent.

Определение набора правил, а также пошаговое руководство по добавлению набора правил в существующий профиль представлены в приведённом ниже примере. В этом примере мы включаем глубокий мониторинг веб-сервера Apache Tomcat, скрипт начальной загрузки которого расположен по пути `/usr/sbin/tomcat-sysd`.

Предполагается, что структура каталогов для AppArmor выглядит следующим образом:

```
/etc/apparmor.d/



|--- usr.sbin.tomcat-sysd
```

Где `usr.sbin.tomcat-sysd` — это файл, определяющий профиль AppArmor для Tomcat.

1. Создайте новый каталог и новый набор правил для OneAgent в этом каталоге с именем `agentinjection`.

   ```
   /etc/apparmor.d/



   |--- usr.sbin.tomcat-sysd



   |--- dynatrace-oneagent



   |--- agentinjection
   ```
2. Содержимое файла `/etc/apparmor.d/dynatrace-oneagent/agentinjection` должно быть следующим:

   ```
   #include <abstractions/base>



   #include <abstractions/nameservice>



   # Process Agent injection



   /etc/ld.so.preload r,



   # Host identifier calculation



   /sys/class/net/ r,



   /sys/devices/virtual/net/** r,



   /sys/devices/*/*{,/*}/net/** r,



   # OneAgent directories



   /opt/dynatrace/oneagent/agent/** mr,



   /var/lib/dynatrace/oneagent/** r,



   /var/lib/dynatrace/oneagent/agent/runtime/** w,



   /var/lib/dynatrace/oneagent/agent/config/{discovery_entry_point,ruxit_shm_v*} w,



   /var/lib/dynatrace/enrichment/** r,



   # This path must be adjusted if LOG_PATH installation parameter was used



   /var/log/dynatrace/oneagent/** rkw,



   # This path must be adjusted if DATA_STORAGE installation parameter was used



   /var/lib/dynatrace/oneagent/datastorage/** rkw,



   # Needed for Process Agent to determine whether specialized agent should be loaded and to calculate PGI ID



   /proc/[0-9]*/{cgroup,cmdline,environ,maps,mem,mountinfo,stat,statm,task/*/maps,task/*/mem} r,



   # Miscellaneous



   /dev/random rw,



   /etc/os-release r,



   /proc/sys/fs/file-nr r,



   /proc/sys/kernel/hostname r,



   /proc/{uptime,vmstat} r,



   /sys/devices/system/cpu/ r,



   /sys/fs/cgroup{,/,/**} r,



   /tmp/** rw,



   /var/tmp/ r,



   /var/tmp/** rw,



   /{,var/}run/utmp rk,



   /proc/cgroups r,
   ```

   Если вы использовали параметр установки [DATA\_STORAGE](../installation/customize-oneagent-installation-on-linux.md "Узнайте, как использовать установщик Linux с параметрами командной строки.") для задания пользовательского каталога хранения больших данных времени выполнения, отредактируйте следующую строку и добавьте ваш пользовательский каталог:

   ```
   # This path must be adjusted if DATA_STORAGE installation parameter was used



   /var/lib/dynatrace/oneagent/datastorage/** rkw,
   ```
3. Включите набор правил в профиль Tomcat (`/etc/apparmor.d/usr.sbin.tomcat-sysd`).

   ```
   /usr/sbin/tomcat-sysd {



   #include <dynatrace-oneagent/agentinjection>



   ... (rest of the rules that were already present in the profile)



   }
   ```
4. Убедитесь, что определённый профиль работает корректно:

   1. Перезагрузите службу AppArmor.
   2. Перезапустите Tomcat.
   3. Убедитесь в веб-интерфейсе, что глубокий мониторинг для процесса Tomcat работает.
   4. Проверьте журналы аудита, чтобы убедиться в отсутствии отказов AppArmor.

Обратите внимание, что, несмотря на то что набор правил, представленный в этом примере, прошёл обширное тестирование, он может потребовать расширения или изменения из-за различий в среде, а также того, что пользовательский путь установки для OneAgent не поддерживается.

### Предупреждения об отказах доступа в журналах аудита

Если вы обнаружите отказы, связанные с OneAgent для других процессов в системе, добавьте следующий подмножество правил в профили этих процессов.

```
# Process injection



/etc/ld.so.preload r,



/etc/oneagentproc/ld.so.preload r,



/var/log/dynatrace/oneagent/process/* rkw,
```

Хотя этот шаг является необязательным, поскольку неудачные попытки внедрения OneAgent в другие процессы не влияют на функциональность ваших приложений, он может потребоваться, если вы используете IDS или другую автоматизированную систему, которая сообщает о предупреждениях об отказах доступа, найденных в журналах аудита.
