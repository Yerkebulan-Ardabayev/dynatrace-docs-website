---
title: Устранение неполадок при установке OneAgent
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation
---

# Устранение неполадок при установке OneAgent

# Устранение неполадок при установке OneAgent

* Устранение неполадок
* 13 мин. чтения
* Обновлено 22 июля 2026 г.

Здесь описано, как устранять неполадки при установке OneAgent на AIX, Linux и Windows.

## Общие рекомендации по устранению неполадок

Почему OneAgent не начинает мониторить процесс Apache после перезапуска?

После установки OneAgent веб-сервер Apache нужно *полностью* перезапустить, чтобы включить мониторинг. Чтобы сделать это правильно, важно понимать разницу между «частичным» и «полным» перезапуском. При частичном перезапуске основной процесс Apache перечитывает конфигурационные файлы, заново открывает файлы журналов и перезапускает рабочие процессы. OneAgent требует полного перезапуска веб-сервера Apache, при котором все рабочие процессы и, что особенно важно, основной процесс Apache полностью останавливаются и запускаются заново.

Подробнее о доступных типах перезапуска см. [Stopping and Restarting Apache HTTP Server﻿](https://httpd.apache.org/docs/2.4/stopping.html).

## Как выполнить полный перезапуск

**Linux и AIX**

Возможно, вы привыкли перезапускать Apache командой `apachectl restart`. Однако эта команда даёт лишь частичный перезапуск Apache.

Чтобы выполнить полный перезапуск Apache и включить глубокий мониторинг с Dynatrace OneAgent, нужно сначала выполнить полное завершение работы командой `apachectl stop`. Только после этого шага можно запустить сервер командой `apachectl start`.

На Ubuntu-системах допустимо использовать `service apache2 restart`. Обратите внимание: какие бы команды ни применялись, скорее всего потребуются права суперпользователя (sudo).

**Windows**

На Windows можно воспользоваться встроенным Windows Service Management или Apache Service Monitor (`httpd.exe`) для перезапуска служб Apache. Перезапуск службы Apache через Windows Service Management гарантирует полный перезапуск. При использовании `httpd.exe` вы, возможно, привыкли перезапускать Apache командой `httpd.exe -k restart -n "Apache2.4"`. Однако эта команда даёт лишь частичный перезапуск Apache.

Чтобы выполнить полный перезапуск Apache и включить глубокий мониторинг с OneAgent, нужно сначала выполнить полное завершение работы командой `httpd.exe -k stop -n "Apache2.4"`. Только после этого шага можно запустить сервер командой `httpd.exe -k start -n "Apache2.4"`.

Что делать, если OneAgent блокирует нужный порт?

Устарело

Начиная с версии OneAgent 1.301, OneAgent не использует TCP-порты для собственного межпроцессного взаимодействия. Если OneAgent занимает порты ваших приложений, обновите OneAgent до версии 1.301+.

OneAgent состоит из нескольких процессов, которые взаимодействуют с watchdog через TCP-порт. При запуске watchdog OneAgent пытается открыть первый доступный порт в диапазоне от 50000 до 50100. В ряде случаев этот порт может потребоваться вашим приложениям, запускаемым после OneAgent. В таких случаях можно изменить диапазон портов, который использует watchdog OneAgent, через интерфейс командной строки OneAgent.

Изменить прослушиваемый watchdog порт можно с помощью `set-watchdog-portrange` через [oneagentctl command-line tool](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent."):

Например, чтобы изменить диапазон портов на `50005:50105`, перейдите в [директорию oneagentctl](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") и выполните следующую команду:

* На **Linux** или **AIX**:  
  `./oneagentctl --set-watchdog-portrange 50005:50105`
* На **Windows**:  
  `.\oneagentctl.exe --set-watchdog-portrange 50005:50105`  
  Перезапустите службу OneAgent, чтобы применить изменения.

Информацию о портах, используемых Dynatrace, см. в разделе [Какие сетевые порты использует сервер Dynatrace?](/managed/managed-cluster/installation/cluster-node-ports "Review the network ports required by Dynatrace Managed and configure your firewall for inbound and outbound communication.")

Проверка сертификата сервера завершилась ошибкой

OneAgent поставляется с доверенными SSL-сертификатами Dynatrace, которые используются для проверки успешного подключения OneAgent к серверу Dynatrace или ActiveGate.

Если в вашей среде используется прокси (что требует обновления SSL-сертификата удалённого сервера) или у вас есть Environment ActiveGate с собственным пользовательским сертификатом, в процессе первоначальной проверки подключения может появиться сообщение `Server certificate check failed`.

Для решения этой проблемы см. раздел [Безопасность OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-security#trusted-root-certificates "Manage OneAgent security").

Процессы не обнаруживаются?

Возможна одна из следующих причин:

* Процесс не поддерживается нашей технологией мониторинга. Всегда можно проверить, [какие типы процессов поддерживает Dynatrace](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Процесс не работает на вашем сервере. Убедитесь, что серверы запущены и процессы функционируют.
* Наблюдается задержка в обмене данными между Dynatrace и OneAgent. В этом случае подождите несколько секунд и повторите попытку.
* OneAgent работает некорректно. Перейдите в **Settings** > **Monitoring** > **Monitoring overview** и убедитесь, что мониторинг включён для хоста, на котором работает ваше программное обеспечение.

Если проблему решить не удаётся, свяжитесь с экспертом по продукту Dynatrace через чат в вашей среде Dynatrace. Также рассмотрите возможность установки OneAgent на другой машине.

Проблемы с OneAgent возникли после значительного обновления ОС хоста.

Мы не поддерживаем серьёзные изменения операционной системы на хосте, где установлен OneAgent.

Изменения ОС, способные повлиять на OneAgent, включают обновления и модификации, такие как:

* Патч ядра системы
* Крупное обновление ОС
* Любое другое изменение конфигурации системы, приводящее к значительному обновлению или модификации ОС

Серьёзные изменения ОС могут привести к таким проблемам, как:

* Проблемы с мониторингом OneAgent
* Перезапуск или удаление службы OneAgent
* Удаление OneAgent

Чтобы выполнить серьёзные изменения ОС на хосте с OneAgent:

1. Удалите OneAgent
2. Примените изменения ОС
3. Переустановите OneAgent  
   При переустановке может потребоваться указать установщику данные подключения. При этом часть конфигурации OneAgent сохранится после удаления, например идентификатор хоста.

Эта информация относится ко всем операционным системам, на которых поддерживается полная установка OneAgent.

Инициализация SDK и обработка ошибок

Если заглушка SDK сталкивается с проблемами при загрузке или инициализации модуля OneAgent (в частности, если [`onesdk_initialize`﻿](https://dt-url.net/mp038qp) или [`onesdk_initalize_2`﻿](https://dt-url.net/dz238k4) возвращает код ошибки), включите логирование для заглушки SDK, чтобы диагностировать проблему.

Для включения логирования используйте один из следующих способов:

* Задайте переменную окружения `DT_LOGLEVELSDK={level}` (наиболее простой вариант).
* Вызовите функцию `onesdk_stub_set_logging_level(ONESDK_LOGGING_LEVEL_{LEVEL})`.
* Если ваша программа передаёт аргументы командной строки в SDK ([`onesdk_stub_process_cmdline_args`﻿](https://dt-url.net/t50394g)), используйте аргумент командной строки `--dt_loglevelsdk={level}`.

Какой бы способ ни был выбран, обязательно примените его до вызова `onesdk_initialize` или `onesdk_initalize_2`.

По умолчанию после включения логирования вывод лога заглушки направляется в `stderr`. Если нужен альтернативный способ обработки сообщений лога заглушки, см. документацию функции [`onesdk_stub_set_logging_callback`﻿](https://dt-url.net/hn03995).

При сбое инициализации наиболее часто встречается код ошибки `ONESDK_ERROR_LOAD_AGENT` (числовой код `2952658951`, `-1342308345` или `0xaffe0007`, сообщение об ошибке `"Could not load agent."`).

Две основные причины этой проблемы:

* **Причина**: OneAgent не установлен на хосте, где выполняется программа.

  **Решение**: Установите OneAgent и перезапустите программу.
* **Причина**: Программа запущена с отладчиком, поэтому OneAgent не выполнит инъекцию.

  **Решение**: Запустите программу без отладчика. Отладчик можно подключить позже, после того как программа будет запущена.

Устранение неполадок SDK после инициализации

После успешной инициализации SDK могут возникать проблемы, например отсутствие путей в интерфейсе или неожиданные коды ошибок, такие как `ONESDK_INVALID_HANDLE`. В таких случаях:

* Проверьте сообщения из коллбэков логирования OneAgent. См. документацию для [`onesdk_agent_set_warning_callback`﻿](https://dt-url.net/2r43812) и [`onesdk_agent_set_verbose_callback`﻿](https://dt-url.net/8w6389l).
* Изучите лог-файлы OneAgent.

  Точное расположение лог-файлов см. на следующих страницах:

  + [Безопасность OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system")
  + [Безопасность OneAgent на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Learn about Dynatrace OneAgent security and modifications to your Linux-based system")

  Уровень логирования OneAgent можно повысить, задав переменную окружения `DT_LOGLEVELFILE={level}` или передав аргумент командной строки `--dt_loglevelfile={level}` в SDK.

  Как вариант, можно использовать `DT_LOGLEVELCON={level}` или `--dt_loglevelcon={level}`, если нужно получать вывод лога OneAgent через `stderr`.
* В определённых сценариях [`onesdk_agent_get_current_state`﻿](https://dt-url.net/l9838z9) может дать дополнительную информацию.

Почему Log Monitoring отключается после обновления OneAgent?

После обновления OneAgent Log Monitoring (`app-log-content-access`) может неожиданно отключиться на хосте.

Это может произойти, когда шаг миграции конфигурации перезаписывает существующий файл конфигурации (\_loganalyticsconf.ctl.json) значениями из устаревшего файла конфигурации (ruxitagentloganalytics.conf). Это редкий случай, затрагивающий только хосты с определённой историей конфигурации, где оба файла сосуществуют.

Чтобы повторно включить Log Monitoring, выполните следующую команду на затронутом хосте:

* **Linux**: `./oneagentctl --set-app-log-content-access=true`
* **Windows**: `.\oneagentctl.exe --set-app-log-content-access=true`

## Устранение неполадок для конкретных ОС

### Linux

Установка завершается ошибкой из-за нехватки памяти

OneAgent может завершить установку с ошибкой, если Linux-хост не соответствует минимальным требованиям к памяти.

* На хосте должно быть не менее 256 МБ свободной памяти для установки и обновления OneAgent.
* Процессу установки требуется не менее 256 МБ виртуальной памяти.

Чтобы устранить проблему, освободите память или увеличьте объём виртуальной памяти на хосте, затем повторите установку. Полный список требований см. в [Install OneAgent on Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux#requirements "Learn how to download and install Dynatrace OneAgent on Linux.").

OneAgent, установленный в развёртываниях Chef Habitat, не инжектируется в процессы

Даже если установить OneAgent на машины, где работают сервисы, развёрнутые через Chef Habitat, инжектироваться в процессы он не сможет: в таких развёртываниях Chef Habitat использует собственный supervisor-специфичный glibc, а не системный glibc, на который опирается OneAgent.

#### Workaround

В качестве обходного решения нужно создать файл `ld.so.preload` для каждой версии glibc, установленной Chef, содержимое которого указывает на Process Module OneAgent на supervisor-хосте Chef Habitat. Выполните следующую команду от имени root:

```
[ -d /hab/pkgs/core/glibc ] && for v in $(find /hab/pkgs/core/glibc -type d -name etc); do sudo echo "/opt/dynatrace/oneagent/agent/bin/current/linux-x86-64/liboneagentproc.so" > $v/ld.so.preload && echo "Installed workaround in '$v'"; done
```

Команду нужно выполнять заново каждый раз, когда Chef Habitat обновляет версию glibc. Также её можно запускать по расписанию через cron job. В таком случае убедитесь, что она выполняется до запуска сервиса, который требуется мониторить. В противном случае потребуется перезапустить сервис, чтобы инжекция OneAgent заработала.

Operation not permitted

Если в консоли Linux или журналах установки появляется ошибка `Operation not permitted`, убедитесь, что установку OneAgent не блокирует антивирусное программное обеспечение, установленное на хосте.

Проблемы с коммуникацией OneAgent при включённом SELinux

OneAgent поддерживает SELinux только при загруженной targeted-политике; политика multi-level security не поддерживается. При попытке установить OneAgent на систему, где SELinux работает с политикой в режиме multi-level security, появится следующее сообщение об ошибке: `Installation with SELinux loaded in multi-level security mode is not supported. Dynatrace OneAgent may not work correctly.`

Если система работает с SELinux в enforcing mode и инжектированные OneAgent не могут установить соединение, тогда как OS-модуль OneAgent работает нормально, попробуйте выполнить следующие действия. Приведённый пример основан на процессе `httpd`, однако аналогичная ситуация возможна и для NGINX и других процессов.

1. Проверьте `/var/log/audit/audit.log` или `journalctl` на наличие отказов, например:

   ```
   # grep type=AVC /var/log/audit/audit.log



   # journalctl --utc -a -t "audit"
   ```
2. Если обнаружен отказ для нужного процесса, например:

   ```
   type=AVC msg=audit(1535366769.867:209537): avc:  denied  { name_connect } for  pid=8348 comm="httpd" dest=9999 scontext=unconfined_u:system_r:httpd_t:s0 tcontext=system_u:object_r:jboss_management_port_t:s0 tclass=tcp_socket`
   ```

   сначала проверьте, разрешает ли SElinux данное соединение следующей командой:

   ```
   # sesearch -AC -s httpd_t -t jboss_management_port_t
   ```

   Интерпретацию вывода команды см. в [Using SELinux booleans﻿](https://wiki.gentoo.org/wiki/SELinux/Tutorials/Using_SELinux_booleans).
3. Если соединение не разрешено, выполните следующую команду:

   ```
   # setsebool -P httpd_can_network_connect on
   ```

   Команда постоянно (с сохранением после перезагрузки хоста) включит SELinux boolean `httpd_can_network_connect`, что позволит OneAgent инжектироваться в процесс `httpd` и устанавливать соединение с ActiveGate.
4. Перезапустите процесс и убедитесь, что соединение работает.

OneAgent на NFS-дисках

Зафиксированы случаи нестабильной работы OneAgent на Linux при развёртывании на некачественных NFS-дисках. Чтобы автоматическая инжекция и автоматические обновления работали корректно, убедитесь, что развёртывание OneAgent соответствует следующим рекомендациям.

#### Custom installation path

Настройте установку OneAgent так, чтобы он не располагался в NFS-директориях (по умолчанию OneAgent устанавливается в `/opt/dynatrace`). Используйте параметр `INSTALL_PATH` установщика OneAgent. Подробнее см. в [Customize OneAgent installation on Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#installation-path "Learn how to use the Linux installer with command line parameters.").

#### Runtime path

Убедитесь, что путь времени выполнения `/var/lib/dynatrace/oneagent` не находится в NFS-директориях.

#### Filesystem availability

Доступность файловой системы критически важна не только для мониторинга OneAgent, но и для запуска любых процессов на хосте. Даже при кастомной установке OneAgent создаёт символические ссылки на `/opt/dynatrace` для своих модулей глубокого мониторинга и автоматической инжекции. Убедитесь, что `/opt/dynatrace` доступен как можно раньше при запуске системы. OneAgent стартует сравнительно рано, поэтому `/opt/dynatrace` должен быть доступен максимально рано в процессе загрузки.

#### Stopping processes for OneAgent update

Если при наличии NFS наблюдаются проблемы с обновлением OneAgent, перед запуском обновления OneAgent останавливайте все процессы, у которых могут быть активированы модули глубокого мониторинга кода OneAgent.

#### FUSE not supported

Файловые системы, использующие FUSE, не поддерживаются.

Ведётся работа по устранению проблем, связанных с развёртыванием на NFS, поэтому данные рекомендации будут обновляться со временем.

Несовместимость с Splunk

Компонент `splunkd` Splunk версии 8.2+ аварийно завершает работу при включённой автоматической инжекции OneAgent.

#### Problem

Согласно [Splunk issue SPL-207550﻿](https://docs.splunk.com/Documentation/Splunk/8.2.1/ReleaseNotes/Knownissues) (внешняя ссылка), Splunk не запускается после установки на Linux при наличии Dynatrace OneAgent, выдавая ошибку `ERROR: pid XXXX terminated with signal 4 (core dumped)`, поскольку возникает конфликт между watchdog Splunk и библиотеками Dynatrace OneAgent.

#### Workaround

В `server.conf`, секция `[watchdog]`, задайте следующее:  
`usePreloadedPstacks = false`

Совместимость с антивирусным программным обеспечением

Блокировка mutex в ядре Linux может приводить к тому, что CrowdStrike Falcon блокирует OneAgent при чтении данных процессов из `/proc`, содержащего по одному подкаталогу на каждый запущенный на системе процесс.

* Когда OneAgent обращается к `/proc/<pid>`, CrowdStrike Falcon блокирует mutex в ядре при создании каталога идентификатора процесса. OneAgent перейдёт в непрерываемое состояние, и освободить процессы можно будет только перезагрузкой сервера или ожиданием ответа от I/O.
* Установка OneAgent может быть затронута в любой момент из-за отсутствия единственного правила, вызывающего проблему.

Oracle Database Server 19c не отвечает

#### Problem

Автоматическая инструментация OneAgent невозможна при установленном Oracle Database Server 19c из-за несовместимости с Process Module OneAgent.

#### Details

Process Module OneAgent требует базовой функциональности системной библиотеки `libc` для выполнения автоматической инструментации. Когда другой продукт переопределяет эту функциональность (в данном случае функцию `__errno_location`), Process Module не может отличить символ, предоставляемый `libc`, от символа, предоставляемого продуктом. Вызов символа продукта приводит к аварийному завершению, поскольку в этот момент он ещё не инициализирован.

#### Scope

Linux-хосты с установленным Oracle Database Server 19c

#### Solution

Достаточно любого из перечисленных вариантов:

* Использовать Oracle Database Server 21c или новее
* Отключить инжекцию Process Agent через `oneagentctl --set-auto-injection-enabled false`
* Выполнить следующий фрагмент, заменив `[PATH-TO-DATABASE-EXECUTABLE]` путём к исполняемому файлу Oracle Database 19c

  ```
  unshare -m -- sh -c 'mount --bind /dev/null /etc/ld.so.preload && [PATH-TO-DATABASE-EXECUTABLE]'
  ```
* Задать переменную окружения `LD_AUDIT` так, чтобы она применялась к Oracle Database при запуске. Подробнее, включая конкретные шаги, см. в [Preventing loading of the process module on Linux﻿](https://community.dynatrace.com/t5/Troubleshooting/Preventing-loading-of-the-process-module-on-Linux/ta-p/213303).
* Отключить инжекцию Process Agent через схему `builtin:host.monitoring.advanced` / UI. ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Warning Это отключит все code module на данном хосте, включая вручную включённые code module.

Если на хосте есть процессы, требующие инжекции Code Module, их можно включить вручную через переменную окружения LD\_PRELOAD=/lib{64}/liboneagentproc.so.
За дополнительной помощью обратитесь к специалистам поддержки Dynatrace в чате.

### Windows

Совместимость с антивирусным программным обеспечением

Для бесперебойной работы OneAgent и устранения лишней нагрузки рекомендуется исключить все файлы в каталоге установки OneAgent из антивирусного сканирования.

Также рекомендуется настроить антивирусное программное обеспечение так, чтобы процесс OneAgent считался доверенным и безопасным. О том, как это сделать, смотрите в документации вашего антивирусного решения.

При использовании McAfee может возникать повышенная нагрузка на CPU. Чтобы устранить эту проблему, нужно переключить McAfee в **Exploit Prevention Compatibility Mode**.

1. Отключите Self-Protection и Exploit Prevention в консоли ENS.
2. Установите следующие значения реестра как DWORD:

   * `HKEY_LOCAL_MACHINE\SOFTWARE\McAfee\Endpoint\Ips\BO\dwBOCompatibilityMode=1`
   * `HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\McAfee\EndPoint\Ips\BO\dwBOCompatibilityMode=1`
3. Повторно включите Self-Protection и Exploit Prevention в консоли ENS.

Процессы не обнаруживаются?

Возможна одна из следующих причин

* Процесс не поддерживается нашей технологией мониторинга. Можно проверить, [какие типы процессов поддерживает Dynatrace](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Процесс не работает на вашем сервере. Убедитесь, что серверы запущены и процессы функционируют.
* Есть задержка в обмене данными между Dynatrace и вашим OneAgent. В таком случае нужно подождать несколько секунд и повторить попытку.
* OneAgent работает некорректно. Перейдите в **Settings** > **Monitoring** > **Monitoring overview** и убедитесь, что мониторинг включён для хоста, на котором выполняется ваше программное обеспечение.

Если устранить проблему по-прежнему не удаётся, обратитесь к эксперту по продукту Dynatrace через живой чат в вашей среде Dynatrace. Также можно попробовать установить OneAgent на другой машине.

Как выполнить восстановление установки OneAgent?

Установщик OneAgent для Windows не поддерживает операции изменения и восстановления. Переустановить OneAgent с помощью той же версии установщика, что и установленный OneAgent, нельзя.

Чтобы переустановить OneAgent на Windows, нужно либо удалить его и установить заново, либо установить более новую версию поверх существующей.

Сбой обновления OneAgent из-за отсутствия пакета MSI в Windows Installer Cache

Установщик OneAgent для Windows использует Windows Installer Cache, который по умолчанию расположен в `C:\Windows\Installer`. В нём хранятся важные файлы, необходимые для удаления и обновления продукта. Если в журнале установки (расположение по умолчанию: `C:\ProgramData\dynatrace\oneagent\log\installer\installation_msiexec_*.log`) есть записи, похожие на следующие:

```
MSI (s) (C0:E4) [09:27:14:308]: Warning: Local cached package 'C:\Windows\Installer\312c0.msi' is missing.



...



Error 1714. The older version of Dynatrace OneAgent cannot be removed.  Contact your technical support group.  System Error 1612.



MSI (s) (C0:54) [09:27:56:489]: Product: Dynatrace OneAgent -- Error 1714. The older version of Dynatrace OneAgent cannot be removed.  Contact your technical support group.  System Error 1612.
```

Для устранения проблемы выполните следующие шаги:

1. Загрузите и распакуйте пакет MSI из установщика текущей установленной версии, следуя инструкциям [Get MSI Package](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#msi "Learn how to download and install Dynatrace OneAgent on Windows.").
2. Скопируйте пакет MSI в `C:\Windows\Installer` и переименуйте его в соответствии с именем, указанным в журнале (в данном примере, `312c0.msi`).

Дополнительные сведения смотрите в статье [Missing Windows Installer cache requires a computer rebuild﻿](https://dt-url.net/gs03u5l).

Папка AI\_RecycleBin заполняет дисковое пространство

Это известная проблема [Advanced Installer﻿](https://dt-url.net/e303ta4). В качестве обходного решения установщик OneAgent очищает `AI_RecycleBin` в конце установки. Однако эта очистка может не сработать, если установка завершилась с ошибкой на раннем этапе, например при [отсутствии пакета MSI в Windows Installer Cache](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation#missing-msi "Learn how to troubleshoot OneAgent installation on AIX, Linux, and Windows."). Подробнее смотрите в обсуждении на [форумах Advanced Installer﻿](https://dt-url.net/w503uks).

### AIX

Сбой установки из-за недостаточного объёма памяти

Установка OneAgent может завершиться с ошибкой, если AIX-хост не соответствует минимальным требованиям к памяти.

* Для установки и обновления OneAgent на хосте требуется не менее 256 МБ свободной памяти.
* Процесс установки требует не менее 256 МБ виртуальной памяти.

Чтобы устранить проблему, нужно освободить память или увеличить выделение виртуальной памяти на хосте, а затем повторить установку. Полный список требований смотрите в статье [Install OneAgent on AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix#requirements "Learn how to download and install Dynatrace OneAgent on AIX.").

Инжекция не работает из-за ручной конфигурации предыдущей версии

Если OneAgent для AIX использовался до версии 1.137, конфигурация могла выполняться через `JAVA_OPTS` с помощью скрипта `dynatrace-java-env.sh`. Перед использованием единых скриптов мониторинга `dynatrace-agentXX.sh` это необходимо убрать.

* Убедитесь, что `dynatrace-java-env.sh` нигде не вызывается в вашем shell при использовании скрипта `dynatrace-agentXX.sh`.
  `dynatrace-java-env.sh` является устаревшим и должен использоваться только как запасной вариант.
* Найдите и удалите следующий параметр из командной строки запуска Java или скриптов запуска (конкретный каталог может отличаться):

  `-agentpath:/opt/dynatrace/oneagent/agent/lib64/liboneagentloader.so`

LDR\_PRELOAD64: parameter not set

При использовании `dynatrace-agentXX.sh` в shell-скрипте может возникнуть следующая ошибка.

```
Info: using DT_HOME: /opt/dynatrace/oneagent



.profile[33] LDR_PRELOAD64: parameter not set
```

Это происходит при использовании `set -u` для обработки неустановленных переменных и параметров как ошибок. Скрипт `dynatrace-agentXX.sh` экспортирует переменные, которые могут ещё не существовать в вашем скрипте, но необходимы для корректной работы. Чтобы обойти это, нужно вызвать `set +u` перед скриптом `dynatrace-agentXX.sh`.

```
# avoid error



set +u



export DT_HOME=/opt/dynatrace/oneagent



. $DT_HOME/dynatrace-agent64.sh
```