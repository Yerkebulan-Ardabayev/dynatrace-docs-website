---
title: Как включить глубокий мониторинг для приложений, ограниченных AppArmor
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/how-to-enable-deep-monitoring-for-applications-confined-by-apparmor
scraped: 2026-05-12T11:05:35.548711
---

# Как включить глубокий мониторинг для приложений, ограниченных AppArmor

# Как включить глубокий мониторинг для приложений, ограниченных AppArmor

* Чтение: 2 мин
* Опубликовано 8 августа 2017 г.

AppArmor представляет собой систему мандатного управления доступом, которая ограничивает приложения определённым набором ресурсов. Для каждого ограниченного приложения существует профиль, который задаёт, какие операции разрешено выполнять приложению, а также пути в файловой системе, к которым приложению разрешён доступ. Чтобы включить глубокий мониторинг приложений, ограниченных AppArmor, в профили этих приложений необходимо добавить пользовательский набор правил для OneAgent.

Определение набора правил, а также пошаговое описание добавления набора правил в существующий профиль приведены в примере ниже. В этом примере мы включаем глубокий мониторинг веб-сервера Apache Tomcat, для которого загрузочный скрипт находится в `/usr/sbin/tomcat-sysd`.

Предполагается, что структура каталогов AppArmor следующая:

```
/etc/apparmor.d/



|--- usr.sbin.tomcat-sysd
```

Здесь `usr.sbin.tomcat-sysd` это файл, определяющий профиль AppArmor для Tomcat.

1. Создайте новый каталог и новый набор правил для OneAgent внутри этого каталога с именем `agentinjection`.

   ```
   /etc/apparmor.d/



   |--- usr.sbin.tomcat-sysd



   |--- dynatrace-oneagent



   |--- agentinjection
   ```
2. Содержимое `/etc/apparmor.d/dynatrace-oneagent/agentinjection` должно быть следующим:

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

   Если для определения пользовательского каталога, предназначенного для хранения больших объёмов данных времени выполнения, вы использовали параметр установки [DATA\_STORAGE](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик Linux с параметрами командной строки."), отредактируйте следующую строку и добавьте свой пользовательский каталог

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
4. Убедитесь, что заданный профиль работает корректно:

   1. Перезагрузите службу AppArmor.
   2. Перезапустите Tomcat.
   3. Убедитесь в веб-интерфейсе, что глубокий мониторинг работает для процесса Tomcat.
   4. Просмотрите журналы аудита, чтобы убедиться в отсутствии отказов AppArmor.

Обратите внимание, что хотя набор правил, приведённый в этом примере, был тщательно протестирован, его может потребоваться расширить или изменить из-за различий в окружениях. Кроме того, пользовательский путь установки OneAgent не поддерживается.

### Предупреждения об отказах в доступе в журналах аудита

Если вы столкнётесь с отказами, связанными с OneAgent, для других процессов в системе, добавьте в профили этих процессов следующее подмножество правил.

```
# Process injection



/etc/ld.so.preload r,



/etc/oneagentproc/ld.so.preload r,



/var/log/dynatrace/oneagent/process/* rkw,
```

Этот шаг необязателен, поскольку неудачные инъекции OneAgent в другие процессы не влияют на работу ваших приложений. Тем не менее он может потребоваться, если вы используете IDS или другую автоматизированную систему, которая сообщает о предупреждениях об отказах в доступе, найденных в журналах аудита.