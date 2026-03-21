---
title: Анализ сбоев
source: https://www.dynatrace.com/docs/observe/application-observability/profiling-and-optimization/crash-analysis
scraped: 2026-03-06T21:20:13.204821
---

Процессы аварийно завершаются по множеству причин, и зачастую сложно понять коренные причины таких сбоев. Когда мониторируемый процесс аварийно завершается, вы увидите запись о сбое процесса в разделе **Events** на каждой затронутой странице процесса и хоста. Пример процесса ниже имеет проблемы с доступностью (показаны красным на временной шкале). При выборе затронутого временного диапазона на шкале раздел **Events** показывает количество сбоев процесса, произошедших за этот период (1 сбой в данном примере).

![Детали события](https://dt-cdn.net/images/event-details-3321-d2e1237b17.png)

Выберите **Process crash details** для просмотра детального списка сбоев, произошедших за выбранный период. Здесь вы найдёте все подробности о причинах каждого сбоя процесса.

![Сбой процесса](https://dt-cdn.net/images/process-crash-1418-427d215ec4.png)

Предоставляемые данные о сбое включают сигнал, который завершил процесс (например, `Segmentation fault` или `Abort`), фрейм стека выполнения, вызвавший сбой, и многое другое. Тип сбоя -- например, нативный дамп ядра, дамп ядра Java или аварийное завершение программы из-за исключения -- определяет, какие детали сбоя доступны.

Эта функциональность работает для всех процессов на каждом мониторируемом хосте.

## Анализ дополнительных артефактов сбоя

Детали сбоя часто включают кнопку **Download**, предоставляющую доступ к дополнительным артефактам сбоя, таким как файлы `hs_err_pid` для сбоев Java, текстовые файлы с анализом дампов ядра Linux и Windows, или файлы, содержащие исключения .NET, Java или Node.js, которые потенциально стали причиной сбоев. Например, приведённый выше отчёт о сбое **Segmentation fault** привёл к дампу ядра. OneAgent автоматически проанализировал дамп ядра и затем создал следующий отчёт в виде лог-артефакта:

```
dumpproc version 1.108.0.20161025-115919, installer version 1.108.0.20161025-121046


2016-11-09 18:00:44: Application 'CreditCardAutho', inner pid '15891', outer pid '0', signal: 'Segmentation fault' (11)


process group ID: 0x441b2cb89962033d


process group instance ID: 0xfe58bab23100f42c


process group Name: easytravel-*-x*


threadCount: 1


thread: 0 - stack range: 0x7ffeda572000-0x7ffeda594000, size: 136 kB


0x00007ffeda592be0 0x00007f4de477604d libpthread-2.15.so!<imagebase>+0xf04d


0x00007ffeda592bf0 0x00000000004038d8 CreditCardAuthorizationS64!main+0x1b8


0x00007ffeda592c60 0x00007f4de41c676d libc-2.15.so!__libc_start_main+0xed


0x00007ffeda592d20 0x000000000040329a CreditCardAuthorizationS64!<imagebase>+0x329a


mapped files:


0000000000400000-000000000041e000 0 /home/labuser/easytravel-2.0.0-x64/CreditCardAuthorizationS64 (MD5: da5992daf5ba3b76c633c853c7da5e87)


000000000051d000-000000000051e000 1d /home/labuser/easytravel-2.0.0-x64/CreditCardAuthorizationS64 (MD5: da5992daf5ba3b76c633c853c7da5e87)


00007f4de41a5000-00007f4de4359000 0 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)


00007f4de4359000-00007f4de4558000 1b4 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)


00007f4de4558000-00007f4de455c000 1b3 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)


00007f4de455c000-00007f4de455e000 1b7 /lib/x86_64-linux-gnu/libc-2.15.so (GNU Build-Id: aa64a66ac46bff200848c0a0694011bd0140ab4e)


00007f4de4563000-00007f4de4565000 0 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)


00007f4de4565000-00007f4de4765000 2 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)


00007f4de4765000-00007f4de4766000 2 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)


00007f4de4766000-00007f4de4767000 3 /lib/x86_64-linux-gnu/libdl-2.15.so (GNU Build-Id: d181af551dbbc43e9d55913d532635fde18e7c4e)


00007f4de4767000-00007f4de477f000 0 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)


00007f4de477f000-00007f4de497e000 18 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)


00007f4de497e000-00007f4de497f000 17 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)


00007f4de497f000-00007f4de4980000 18 /lib/x86_64-linux-gnu/libpthread-2.15.so (GNU Build-Id: c340af9dee97c17c730f7d03693286c5194a46b8)


00007f4de4984000-00007f4de4a02000 0 /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)


00007f4de4a02000-00007f4de4c01000 7e /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)


00007f4de4c01000-00007f4de4c03000 7d /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)


00007f4de4c03000-00007f4de4c05000 7f /lib/x86_64-linux-gnu/liboneagentproc.so (1.108.0.20161025-115919)


00007f4de4cc0000-00007f4de4ce2000 0 /lib/x86_64-linux-gnu/ld-2.15.so (GNU Build-Id: e25ad1a11ccf57e734116b8ec9c69f643dca9f18)


00007f4de4ee2000-00007f4de4ee3000 22 /lib/x86_64-linux-gnu/ld-2.15.so (GNU Build-Id: e25ad1a11ccf57e734116b8ec9c69f643dca9f18)


00007f4de4ee3000-00007f4de4ee5000 23 /lib/x86_64-linux-gnu/ld-2.15.so (GNU Build-Id: e25ad1a11ccf57e734116b8ec9c69f643dca9f18)
```

## Защита конфиденциальных данных пользователей

Отчёты о сбоях могут содержать конфиденциальную персональную информацию, которая не должна быть доступна всем пользователям. По этой причине ваш администратор Dynatrace должен включить [разрешение **View logs** в настройках безопасности учётной записи](../../../manage/identity-access-management/permission-management/role-based-permissions.md#environment "Разрешения на основе ролей") и разрешение [**View sensitive request data**](../../../manage/identity-access-management/permission-management/role-based-permissions.md#environment "Разрешения на основе ролей") в вашем профиле пользователя, прежде чем вы сможете просматривать персональные данные. Этот параметр отключён по умолчанию для всех пользователей без прав администратора и должен быть явно включён для получения доступа к содержимому логов.

## Обработка сбоев в Windows

Для того чтобы общий сбой процесса Windows (дамп ядра) был виден для Dynatrace, сбой должен быть обнаружен службой Windows Error Reporting. По этой причине служба Windows Error Reporting должна быть включена.

![Сбои процессов 6](https://dt-cdn.net/images/process-crashes6-1142-db9303969a.png)

При возникновении сбоя в Windows появляется диалоговое окно с вопросом, хотите ли вы отладить или закрыть аварийно завершившееся приложение. Это нежелательно для автономных систем. Вы можете отключить это диалоговое окно, добавив значение в реестр, как показано ниже:

`[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting] "DontShowUI"=dword:00000001`

![Сбои процессов 8](https://dt-cdn.net/images/process-crashes8-880-1d0cfb52b5.png)

Узнать о других полезных настройках, связанных с Windows Error Reporting, можно в [документации Microsoft](https://msdn.microsoft.com/en-us/library/windows/desktop/bb513638(v=vs.85).aspx).

## Обработка дампов ядра в Linux

В Linux способ обработки дампа ядра ядром устанавливается в `/proc/sys/kernel/core_pattern`. Начиная с ядра 2.6.19 (1), существует два метода обработки сбоев приложений. Дамп ядра может быть записан в файл, указанный в записи `/proc/sys/kernel/core_pattern`, или передан приложению -- запись должна начинаться с символа вертикальной черты (`|`).

Поскольку Suse Linux использует первый метод, запись выглядит примерно так:
`/proc/sys/kernel/core_pattern:core`. Это означает, что файл с именем `core` записывается в текущий рабочий каталог аварийно завершившегося процесса.

Ubuntu и Red Hat обычно полагаются на собственные инструменты для отчётов о дампах сбоев, поэтому строки выглядят следующим образом:
`|/usr/share/apport/apport %p %s %c %P`
или
`|/usr/libexec/abrt-hook-ccpp %s %c %p %u %g %t e`

В последнем примере, когда программа аварийно завершается, вывод `coredump` передаётся в `stdin` приложения, указанного в первом параметре. Кроме того, ядро заполняет значения всех параметров в формате `%[a-zA-Z]`. Служба отчётов `apport` перезаписывает файл `/proc/sys/kernel/core_pattern`. Если `apport` включён (в `/etc/default/apport`), то настройка `/proc/sys/kernel/core_pattern` устанавливается при запуске службы отчётов о сбоях `apport` при загрузке системы.
[Подробнее...](https://askubuntu.com/questions/420410/how-to-permanently-edit-the-core-pattern-file)

### Изменения в операционной системе

Установщик OneAgent вносит следующие изменения в вашу систему для обработки дампов ядра.

#### Отключение ABRT и Apport

Службы [ABRT](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-abrt) (Red Hat) и [Apport](https://launchpad.net/ubuntu/+source/apport) (Debian) останавливаются и отключаются.

Обе службы повторно включаются при [удалении OneAgent](../../../ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux.md "Узнайте, как удалить OneAgent из вашей системы на базе Linux.").

Подробнее см. [Безопасность OneAgent на Linux](../../../ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux.md#operating-system-changes "Узнайте о безопасности Dynatrace OneAgent и изменениях в вашей системе на базе Linux").

#### Обработка core pattern

Установщик OneAgent перезаписывает core pattern собственной командой, но сохраняет исходный шаблон.

* Содержимое исходного файла `/proc/sys/kernel/core_pattern` копируется в:

  + OneAgent версии 1.301 и ранее: `/opt/dynatrace/oneagent/agent/conf/original_core_pattern`
  + OneAgent версии 1.302+: `/var/lib/dynatrace/oneagent/agent/backup/original_core_pattern`

  При удалении OneAgent исходный core pattern из этого файла восстанавливается в `/proc/sys/kernel/core_pattern`.
* Содержимое исходного параметра `kernel.core_pattern` в `/etc/sysctl.conf` копируется в:

  + OneAgent версии 1.301 и ранее: `/opt/dynatrace/oneagent/agent/conf/original.sysctl.corepattern`
  + OneAgent версии 1.302+: `/var/lib/dynatrace/oneagent/agent/backup/original.sysctl.corepattern`

  При удалении OneAgent исходный core pattern из этого файла восстанавливается в `kernel.core_pattern` в `/etc/sysctl.conf`. Если `kernel.core_pattern` отсутствовал в `/etc/sysctl.conf` до установки OneAgent, файл резервной копии не создаётся.

В зависимости от исходной записи в `core_pattern`, Dynatrace записывает различные шаблоны в `core_pattern`. Возможные конфигурации и ожидаемые записи после установки перечислены ниже:

| Исходная запись core\_pattern | core\_pattern после установки ruxitdumpproc | Комментарий |
| --- | --- | --- |
| core | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s | Простой дамп ядра без параметров. |
| core\_%s\_%e | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s -kp %s,%e | Простой дамп ядра с параметрами в имени файла. Параметр `-kp` добавляется вместе со всеми параметрами ядра, необходимыми Dynatrace для подстановки в исходное имя файла. |
| /usr/share/apport/apport | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s | Дамп ядра через следующее приложение без параметров. Аргумент `-a` не добавляется к выходной записи `core_pattern`, если параметров нет. |
| /usr/share/apport/apport %p %s %c %P | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s -a %p %s %c %P | Дамп ядра через следующее приложение с параметрами. Аргумент `-a` добавляется вместе со всеми параметрами после пути к бинарному файлу `apport`. |

### Обработка дампов ядра с помощью OneAgent dumpproc

При возникновении сбоя:

1. Вызывается `rdp` для записи дампа ядра в каталоги OneAgent. Этот дамп используется функциональностью отчётов о сбоях.
2. OneAgent считывает `original_core_pattern` и создаёт дамп ядра на основе его настроек. Таким образом, если исходная конфигурация указывала определённое местоположение для записи файла дампа ядра, это сохраняется и после установки OneAgent.
3. Дамп ядра анализируется для определения, мог ли Dynatrace быть коренной причиной сбоя.

   * Если OneAgent определяет, что Dynatrace мог быть виноват:

     + Генерируется оповещение поддержки. Оно передаётся команде DevOps.
     + Дамп ядра архивируется и сохраняется вместе со всеми задействованными библиотеками. Это необходимо для дальнейшего офлайн-анализа.
   * Если OneAgent определяет, что Dynatrace не виноват:

     + Пользователю сообщается о сбое через веб-интерфейс Dynatrace.
     + Если сбой повлиял на приложение клиента, открывается проблема и генерируется соответствующее событие для задействованных процессов, как описано выше.

## Очистка

Каталоги логов и оповещений поддержки очищаются автоматически.

* Для оповещений поддержки мы обрабатываем `core dump`, затем архивируем его и сохраняем для отправки в кластер.
* Для сбоев (неинструментированные процессы или инструментированные, где мы определили, что Dynatrace не виноват) мы обрабатываем и затем удаляем копию `core dump`.

## Связанные темы

* [Просмотр отчётов о сбоях для мобильных приложений](../../digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile.md "Просмотр последних отчётов о сбоях для ваших мобильных приложений.")
* [Просмотр отчётов о сбоях для пользовательских приложений](../../digital-experience/custom-applications/analyze-and-use/crash-reports-custom.md "Просмотр последних отчётов о сбоях для ваших пользовательских приложений.")
* [Новое: Анализ сессий пользователей](../../digital-experience/session-segmentation/new-user-sessions.md "Узнайте о сегментации сессий пользователей и атрибутах фильтрации.")
