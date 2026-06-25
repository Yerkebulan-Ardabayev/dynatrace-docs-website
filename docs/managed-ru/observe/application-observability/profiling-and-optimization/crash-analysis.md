---
title: Анализ сбоев
source: https://docs.dynatrace.com/managed/observe/application-observability/profiling-and-optimization/crash-analysis
scraped: 2026-05-12T11:21:40.362862
---

# Анализ сбоев

# Анализ сбоев

* How-to guide
* 7-min read
* Published Jul 19, 2017

Процессы аварийно завершаются по множеству причин, и часто бывает сложно понять первопричины таких сбоев. Когда отслеживаемый процесс завершается с ошибкой, в разделе **Events** страницы каждого затронутого процесса и хоста появляется запись об аварийном завершении процесса. В приведённом ниже примере процесс имеет проблемы с доступностью (показаны красным на временной шкале). При выборе затронутого временного периода на шкале раздел **Events** показывает количество аварийных завершений, произошедших в этом периоде (1 сбой в данном примере).

![Сведения о событии](https://dt-cdn.net/images/event-details-3321-d2e1237b17.png)

Сведения о событии

Выберите **Process crash details** для просмотра подробного списка сбоев, произошедших за выбранный период. Здесь можно найти все сведения о причинах аварийного завершения каждого процесса.

![Аварийное завершение процесса](https://dt-cdn.net/images/process-crash-1418-427d215ec4.png)

Аварийное завершение процесса

Предоставленные сведения о сбое включают сигнал, завершивший процесс (например, `Segmentation fault` или `Abort`), кадр стека выполнения, в котором произошёл сбой, и многое другое. Тип сбоя — такой как нативный дамп ядра, дамп ядра Java или аномальное завершение программы из-за исключения — определяет, какие сведения о сбое доступны.

Эта функциональность работает для всех процессов на каждом отслеживаемом хосте.

## Анализ дополнительных артефактов сбоя

Сведения о сбоях часто включают кнопку **Download**, предоставляющую доступ к дополнительным артефактам сбоя, таким как файлы `hs_err_pid` для сбоев Java, текстовые файлы с анализом дампов ядра Linux и Windows или файлы с исключениями .NET, Java или Node.js, потенциально ответственными за сбои. Например, приведённый выше отчёт о сбое типа **Segmentation fault** привёл к созданию дампа ядра. OneAgent автоматически проанализировал дамп ядра и создал следующий отчёт в виде артефакта лога:

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

Отчёты о сбоях могут содержать конфиденциальную персональную информацию, которая не должна быть доступна всем пользователям. По этой причине администратор Dynatrace должен включить параметр безопасности учётной записи [**View logs**](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Разрешения на основе ролей") и разрешения [**View sensitive request data**](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Разрешения на основе ролей") в вашем профиле пользователя, прежде чем вы сможете просматривать персональные данные. По умолчанию этот параметр отключён для всех пользователей без прав администратора и должен быть явно включён, прежде чем вы сможете получить доступ к содержимому логов.

## Обработка сбоев в Windows

Чтобы общий сбой процесса Windows (дамп ядра) был виден для Dynatrace, он должен быть обнаружен Windows Error Reporting. По этой причине служба Windows Error Reporting должна быть включена.

![Сбои процессов 6](https://dt-cdn.net/images/process-crashes6-1142-db9303969a.png)

Сбои процессов 6

При сбое в Windows появляется диалог с предложением отладить или закрыть аварийно завершившееся приложение. Для систем без пользовательского интерфейса это нежелательно. Этот диалог можно отключить, добавив значение в реестр, как показано ниже:

`[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting] "DontShowUI"=dword:00000001`

![Сбои процессов 8](https://dt-cdn.net/images/process-crashes8-880-1d0cfb52b5.png)

Сбои процессов 8

Другие полезные настройки, связанные с Windows Error Reporting, описаны в [документации Microsoft](https://msdn.microsoft.com/en-us/library/windows/desktop/bb513638(v=vs.85).aspx).

## Обработка дампов ядра Linux

В Linux способ обработки ядром дампа ядра задаётся в `/proc/sys/kernel/core_pattern`. Начиная с ядра версии 2.6.19 (1) существует два метода обработки аварийных завершений приложений. Дамп ядра может быть записан в файл, на который указывает запись `/proc/sys/kernel/core_pattern`, или передан приложению — при этом запись должна начинаться с символа вертикальной черты (`|`).

Поскольку Suse Linux использует первый метод, запись выглядит примерно так:
`/proc/sys/kernel/core_pattern:core`. Это означает, что файл с именем `core` записывается в текущем рабочем каталоге аварийно завершившегося процесса.

Ubuntu и Red Hat, как правило, используют собственные инструменты для отчётов о дампах ядра, поэтому строки выглядят следующим образом:  
`|/usr/share/apport/apport %p %s %c %P`  
или  
`|/usr/libexec/abrt-hook-ccpp %s %c %p %u %g %t e`

В последнем примере при сбое программы вывод `coredump` передаётся на `stdin` приложения, указанного в первом параметре. Кроме того, ядро заполняет значения любых параметров, отформатированных как `%[a-zA-Z]`. Служба отчётности `apport` перезаписывает файл `/proc/sys/kernel/core_pattern`. Если `apport` включён (в `/etc/default/apport`), параметр `/proc/sys/kernel/core_pattern` устанавливается при запуске службы отчётности о сбоях `apport` при загрузке системы.
[Подробнее…](https://askubuntu.com/questions/420410/how-to-permanently-edit-the-core-pattern-file)

### Изменения операционной системы

Установщик OneAgent выполняет следующие изменения в системе для обработки дампов ядра.

#### Отключение ABRT и Apport

Службы [ABRT](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-abrt) (Red Hat) и [Apport](https://launchpad.net/ubuntu/+source/apport) (Debian) останавливаются и отключаются.

Обе службы повторно включаются при [удалении OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Узнайте, как удалить OneAgent из системы на базе Linux.").

Дополнительные сведения см. в разделе [Безопасность OneAgent в Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux#operating-system-changes "Узнайте о безопасности OneAgent и изменениях в системах на базе Linux.").

#### Обработка шаблона ядра

Установщик OneAgent перезаписывает шаблон ядра собственной командой, но сохраняет исходный шаблон.

* Содержимое исходного файла `/proc/sys/kernel/core_pattern` копируется в:

  + OneAgent версии 1.301 и ранее: `/opt/dynatrace/oneagent/agent/conf/original_core_pattern`
  + OneAgent версии 1.302+: `/var/lib/dynatrace/oneagent/agent/backup/original_core_pattern`

  При удалении OneAgent исходный шаблон ядра из этого файла восстанавливается в `/proc/sys/kernel/core_pattern`.
* Содержимое исходного параметра `kernel.core_pattern` в `/etc/sysctl.conf` копируется в:

  + OneAgent версии 1.301 и ранее: `/opt/dynatrace/oneagent/agent/conf/original.sysctl.corepattern`
  + OneAgent версии 1.302+: `/var/lib/dynatrace/oneagent/agent/backup/original.sysctl.corepattern`

  При удалении OneAgent исходный шаблон ядра из этого файла восстанавливается в `kernel.core_pattern` в `/etc/sysctl.conf`. Если `kernel.core_pattern` отсутствовал в `/etc/sysctl.conf` до установки OneAgent, резервный файл не создаётся.

В зависимости от исходной записи в `core_pattern` Dynatrace записывает разные шаблоны в `core_pattern`. Возможные конфигурации и ожидаемые записи после установки перечислены ниже:

| Исходная запись core\_pattern | core\_pattern после установки ruxitdumpproc | Комментарий |
| --- | --- | --- |
| core | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s | Простой дамп ядра без параметров. |
| core\_%s\_%e | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s -kp %s,%e | Простой дамп ядра с параметрами в имени файла. Параметр `-kp` добавляется вместе со всеми параметрами ядра, необходимыми Dynatrace для подстановки в исходное имя файла. |
| /usr/share/apport/apport | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s | Дамп ядра с передачей следующему приложению без параметров. Аргумент `-a` не добавляется в выходную запись `core_pattern` при отсутствии параметров. |
| /usr/share/apport/apport %p %s %c %P | /opt/dynatrace/oneagent/agent/rdp -p %p -e %e -s %s -a %p %s %c %P | Дамп ядра с передачей следующему приложению с параметрами. Аргумент `-a` добавляется вместе со всеми параметрами после пути к бинарному файлу `apport`. |

### Обработка дампов ядра через OneAgent dumpproc

При возникновении сбоя:

1. Вызывается `rdp` для записи дампа ядра в папки OneAgent. Этот дамп используется функцией отчётности о сбоях.
2. OneAgent считывает `original_core_pattern` и генерирует дамп ядра на основе его настроек. Таким образом, если в исходной конфигурации было указано конкретное расположение для записи файла дампа ядра, это продолжает работать и после установки OneAgent.
3. Дамп ядра анализируется на предмет того, мог ли Dynatrace быть первопричиной сбоя.

   * Если OneAgent определяет, что Dynatrace мог быть виновником:

     + Создаётся оповещение поддержки. Оно передаётся нашей команде DevOps.
     + Дамп ядра архивируется и сохраняется вместе со всеми задействованными библиотеками. Это необходимо для последующего автономного анализа.
   * Если OneAgent определяет, что Dynatrace не является виновником:

     + Сбой отображается пользователю через веб-интерфейс Dynatrace.
     + Если это оказывает влияние на приложение пользователя, открывается проблема и для задействованных процессов создаётся соответствующее событие, как описано выше.

## Очистка

Каталоги логов и оповещений поддержки очищаются автоматически.

* Для оповещений поддержки дамп ядра обрабатывается, архивируется и сохраняется для отправки в кластер.
* Для сбоев (неинструментированные процессы или инструментированные, для которых Dynatrace определён как не виновник) дамп ядра обрабатывается, а его копия удаляется.

## Связанные темы

* [Просмотр отчётов о сбоях для мобильных приложений](/managed/observe/digital-experience/mobile-applications/analyze-and-use/crash-reports-mobile "Просматривайте последние отчёты о сбоях мобильных приложений.")
* [Просмотр отчётов о сбоях для пользовательских приложений](/managed/observe/digital-experience/custom-applications/analyze-and-use/crash-reports-custom "Просматривайте последние отчёты о сбоях пользовательских приложений.")
* [Новое: Анализ пользовательских сессий](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Узнайте о сегментации и атрибутах фильтрации пользовательских сессий.")