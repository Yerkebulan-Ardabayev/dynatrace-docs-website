---
title: Настройка подсистемы zDC
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc/customize-zdc
scraped: 2026-05-12T12:30:54.783659
---

# Настройка подсистемы zDC

# Настройка подсистемы zDC

* Чтение: 8 мин
* Опубликовано 22 июля 2016 г.

Узнайте, как настроить подсистему zDC в соответствии с вашими задачами.

## Команды z/OS MODIFY

Формат [команды z/OS MODIFY](https://www.ibm.com/docs/en/zos/2.5.0?topic=reference-modify-command) определён следующим образом:

```
MODIFY <jobName or stcProcName>,DT1 <command>
```

Подсистема zDC поддерживает следующие команды z/OS MODIFY.

| Команда | Описание |
| --- | --- |
| DISPLAY | Отображает статистику процессора подзадач Dynatrace. |
| DTM%V | Принудительно отображает (ZDC952) загрузку очереди сообщений zLocal. |
| LOG=? | Запрашивает уровень логирования zDC. |
| LOG=3 | Задаёт уровень логирования zDC. Допустимые значения: от `0` до `8`. Значение по умолчанию: `3`. Значение `4` подавляет информационные сообщения. Значения ниже `3` следует использовать только при диагностической отладке. |
| START | Запускает zLocal. |
| STDO | Добавляет ранее незарегистрированные строки из `stdo.log` zLocal в `SYSPRINT`. |
| STOP | Останавливает zLocal. |
| ZLALOGLEVEL=INFO | Задаёт уровень логирования zLocal. Допустимые значения: `FINEST`, `FINER`, `FINE`, `CONFIG`, `INFO`, `WARNING`, `SEVERE`, `DEBUG` и `NONE`. Значение по умолчанию не задано. |

Команда `DISPLAY` пропускает большинство строк с нулевыми счётчиками, если уровень логирования не ниже значения по умолчанию, равного 3. Для вывода полного набора счётчиков нужно повысить уровень логирования до 1.

```
MODIFY MEPx,DT1 LOG=1



MODIFY MEPx,DT1 DISPLAY
```

Пример вывода zDC от команды `DISPLAY` при `LOG=1`.

```
14:13:33.854126 ZDC027I MODIFY COMMAND RECEIVED



14:13:33.857174 ZDC028I DT1 DISPLAY



14:13:33-977432 ZDC994I ShoS Counters



35:Msgs sent from MAgent to zDC using unnamed pipe



1:QUEUE_MAX_EVENTS(EQH)High watermark elements used



128:EQH queue elements defined



128:EQH elements currently free



0:Internal Performance:XmPosts avoided



0:Internal Performance:XmPost Skip DupSrbs



1,758:zDC Elapsed time (approx sec)



0: Bytes read from DTM Msgs



49:SMO Msgs written



34:Internal:Redundant Post bypassed



15:Internal:Attempt Rd=Wr cursor for vStorage Perf.



15:z/OS Unix has no ready Msgs, waiting for work



48:z/OS Unix Msgs read



3,808: Bytes read from SMO Msgs



2,267:TBC Total Transactional Buffers



2,267:TBC number in Free queue



25:TBC Msgs written



25:TBC Msgs read



10:TBC TBCs written



10:TBC TBCs read



10:TBC Post bypass



41:TBC No Ready Q



1,905:TBC Bytes written



1,905:TBC Bytes read



2:TBC Age<=PingDelay*.5



2:TBC Age<=PingDelay*.75



2:TBC Age<=PingDelay*1



2:TBC Age<=PingDelay*1.25



2:TBC Age>=PingDelay*1.25



10,485,760:DTMSG_SMOSIZE Bytes allocated



9,248:DTMSG_SMOSIZE Bytes used



14:13:36-712702 ZDC995W  DispTcb:     009D1438                0.900sec



14:13:36-712792 ZDC995W  DispTcb:     009BBAD0                0.577sec



14:13:36-712832 ZDC995W  DispTcb:     009BBCF0                0.013sec



14:13:36-712882 ZDC995W  DispTcb:     009BBE88                0.012sec



14:13:36-714022 ZDC995W  DispTcb:     009BE170                0.924sec



14:13:36-714062 ZDC995W  DispTcb:     009BE390                0.590sec



14:13:36-714112 ZDC995W  DispTcb:     009BE528                0.251sec
```

Строки, заканчивающиеся восклицательным знаком (`!`), должны иметь нулевые значения счётчиков.

## Несколько стеков TCP/IP на LPAR

LPAR с несколькими стеками TCP/IP требует дополнительного шага настройки в процедуре PROC запускаемой задачи `ZDCMEPC` из `SZDTSAMP`.

Программа `BPXTCAFF` связывает определённый стек TCP/IP с текущим адресным пространством.

Значение `PARM`: имя задания, запускающего нужный стек TCP/IP.

```
//MEPC     PROC



...



//STEP0 EXEC PGM=BPXTCAFF,PARM='TCPIP_stack_name'



//*



//ZDCMAIN EXEC PGM=ZDCMAIN,REGION=0M,PARM='LANGUAGE=EN'



//STEPLIB   DD DISP=SHR,DSN=hlq.SZDTAUTH



//* Notes:



//* SYSPRINT is required in all cases.



//* SYSPRINT must be allocated to spool, not disk, on JES2 systems.



//* SYSPRIN3 is required on JES3 systems only.



//SYSPRINT  DD SYSOUT=*



//SYSPRIN3  DD SYSOUT=*



//SYSIN     DD DISP=SHR,DSN=hlq.SZDTSAMP(ZDCSYSIN)
```

## Несколько пар zDC/zRemote на LPAR

Пара zDC/zRemote соединяет модули на LPAR с одним окружением Dynatrace. В ряде случаев может потребоваться настроить несколько пар zDC/zRemote на LPAR:

* если нужно поддерживать различные группы приложений в разных окружениях Dynatrace;
* если нужно оптимизировать производительность мониторинга при высоких объёмах транзакций.

### Установка дополнительной пары zDC/zRemote

1. Установите дополнительный [модуль zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#installation "Подготовьте и установите zRemote для мониторинга z/OS.").
2. На своём LPAR скопируйте текущий элемент JCL SYSIN `ZDCSYSIN` под другим именем (например, `ZDCSYSI2`).
3. Отредактируйте новый элемент JCL SYSIN, изменив следующие [параметры SYSIN](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Настройка подсистемы сбора данных z/OS (zDC).").

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN2)



   DTAGTCMD(zremote=<ipaddress>[:port]



   name=zlocal_<lpar>)



   SUBSYSTEM_ID(<subsystem>)



   DEFAULT(NO)
   ```

   * Укажите в `zremote=<ipaddress>[:port]` IP-адрес и порт нового модуля zRemote.
   * Измените `name=<zlocal_<lpar>>` на новое имя zLocal.
   * Измените `<subsystem>` на новое имя.
   * Измените `DEFAULT(YES)` на `DEFAULT(NO)`. Первый zDC назначается основным. Только один zDC на LPAR может задавать `DEFAULT(YES)`. Дополнительные zDC не инициализируются, если не задано `DEFAULT(NO)`.
4. Создайте копию текущей процедуры PROC запускаемой задачи и измените элемент JCL SYSIN так, чтобы он ссылался на новый элемент SYSIN.
5. Запустите новый zDC и проверьте, установлено ли соединение с новым zRemote.

### Подключение модулей к новому zDC

Модуль CICS

Модуль IMS

Модуль z/OS Java

Создайте переопределение параметра `INITPARM` при инициализации системы CICS для направления запросов в новую подсистему zDC.

См. раздел [Подключение модуля CICS к подсистеме zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics#connect-cics-zdc "Установка модуля Dynatrace CICS.").

Измените параметр `ZDC=` в параметрах служебной программы инжекции, чтобы направить запросы в новую подсистему zDC.

См. служебную программу инжекции раздела [Управляющий регион IMS](#install-ims-control-region).

Измените параметр `ZdcName` в файле `dtconfig.json` для направления запросов в новую подсистему zDC.

См. процедуру [Загрузка](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Настройка мониторинга Java на z/OS с помощью модуля Java.") модуля z/OS Java.

## Обработка отказоустойчивости для zDC/zRemote

Это не балансировка нагрузки.

Подсистема zDC может автоматически переключиться на следующий активный модуль zRemote, если с основным zRemote возникает проблема.

zLocal версии 1.1.0+ и модуль zRemote версии 1.261+. После переключения при отказе и подключения резервного zRemote zDC каждые 5 минут проверяет доступность основного zRemote. Если основной zRemote недоступен, соединение с резервным zRemote сохраняется и цикл начинается заново. Если основной zRemote доступен, резервный zRemote отключается и немедленно предпринимается попытка повторного подключения к основному zRemote.

zLocal версий ниже 1.1.0

После переключения при отказе zDC остаётся подключённым к следующему zRemote до разрыва этого соединения. Если в этот момент исходный zRemote снова окажется онлайн, zDC попытается к нему подключиться. При перезапуске zDC исходный zRemote является первым кандидатом для подключения.

Чтобы применить это поведение и в более новых версиях zLocal, задайте `zlaDisablePrimaryReconnect=true` в параметре SYSIN `DTAGTCMD`.

Список адресов zRemote, используемых при обработке отказоустойчивости, хранится в элементе JCL SYSIN `ZDCSYSIN`. Отредактируйте его, изменив следующие [параметры SYSIN](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Настройка подсистемы сбора данных z/OS (zDC).").

```
//SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN2)



DTAGTCMD(zremote=<ipaddress>[:port];<ipaddress>[:port];<ipaddress>[:port]



nobootstrap=true)
```

* Задайте `zremote=<ipaddress>[:port]` со списком адресов zRemote.
* Задайте `nobootstrap=true`, чтобы отключить автоматическое обновление zLocal: оно не поддерживается при обработке отказоустойчивости.

  Сообщение об ошибке zLocal при попытке обновления в ходе обработки отказоустойчивости

  ```
  severe  [native] Connection error (connect()/apr_sockaddr_info_get(), EDC9501I The name does not resolve for the supplied parameters.) while trying to bootstrap the zLocal.
  ```

### Обновление zLocal в ходе обработки отказоустойчивости

Порядок обновления zLocal в ходе обработки отказоустойчивости:

1. Отредактируйте элемент JCL SYSIN `ZDCSYSIN`, изменив следующие [параметры SYSIN](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Настройка подсистемы сбора данных z/OS (zDC).").

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN2)



   DTAGTCMD(zremote=<ipaddress>[:port]



   nobootstrap=false)
   ```

   * Укажите в `zremote=<ipaddress>[:port]` адрес основного модуля zRemote.
   * Задайте `nobootstrap=false`, чтобы включить автоматическое обновление zLocal.
2. Запустите zDC. Загрузчик `dtzagent` скачает последний бинарный файл zLocal `libdtzagent.so` в каталог `/u/dt/agent/downloads/native/a.b.c.d/zos-s390-64`.
3. Скопируйте бинарный файл zLocal `libdtzagent.so` в каталог `/u/dt/agent/lib64`. Теперь zDC готов к обработке отказоустойчивости с последним бинарным файлом zLocal.
4. Отредактируйте элемент JCL SYSIN `ZDCSYSIN`, изменив следующие [параметры SYSIN](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Настройка подсистемы сбора данных z/OS (zDC).").

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN2)



   DTAGTCMD(zremote=<ipaddress>[:port];<ipaddress>[:port];<ipaddress>[:port]



   nobootstrap=true)
   ```

   * Задайте `zremote=<ipaddress>[:port]` со списком адресов zRemote.
   * Задайте `nobootstrap=true`, чтобы отключить автоматическое обновление zLocal.
5. Перезапустите zDC.

## Завершение работы zDC

zDC, как правило, освобождает системные ресурсы (в особенности общую память) при штатном завершении по команде остановки или при аварийном завершении по команде отмены или аварийном завершении программы (ABEND). Подпрограммы восстановления (ESTAEX) всегда активны: они перехватывают аварийные завершения и освобождают все системные ресурсы.

Тем не менее возможна ситуация, когда zDC нельзя отменить из-за аномалии или сбоя z/OS, препятствующего выполнению команды отмены. Если необходимо завершить работу zDC, выполняйте приведённые ниже команды в указанном порядке до завершения zDC. Переходите к шагу 2 только при неуспехе шага 1, к шагу 3 только при неуспехе шага 2, и так далее.

Чтобы избежать ручной очистки системных ресурсов с помощью описанной ниже процедуры `ZDCDELET`, делайте небольшую паузу между командами, чтобы успели создаться дампы и освободиться системные ресурсы.

1. Выполните команду `STOP jobname`.
2. Выполните команду `MODIFY jobname,SHUTDOWN IMMED`.
3. Выполните команду `CANCEL jobname`.
4. Выполните команду `FORCE jobname`.

Попытайтесь перезапустить zDC. При успешном перезапуске задание можно продолжать выполнять. При неуспешном перезапуске, если zDC сообщает о невозможности продолжения работы, запустите аварийную программу очистки zDC с именем `ZDCDELET`.

`ZDCDELET`: отдельная задача, которая пытается завершить указанную задачу zDC и освободить все системные ресурсы, удерживаемые процессом zDC. JCL для выполнения `ZDCDELET` представлен ниже.

```
//*



//* PLACE YOUR JOB STATEMENT HERE



//*



//DELETE EXEC PGM=ZDCDELET,PARM=xxxx



//STEPLIB DD DISP=SHR,DSN=<hlq>.R1nnnxx.SZDTAUTH
```

В операторе `EXEC` параметр `PARM=` должен содержать 4-символьное имя подсистемы процесса zDC, который требуется завершить.

* Могут возникать пользовательские ABEND `100` и `101`; описывающие их сообщения записываются в лог задания.
* Пользовательский ABEND `100` означает, что значение `PARM=` имеет длину не ровно 4 байта.
* Пользовательский ABEND `101` означает, что имя подсистемы, указанное в операнде `PARM=`, не найдено в системе.
* В лог задания могут записываться сообщения от `ZDC400` до `ZDC403`.

Полный список сообщений zDC см. в разделах [Пользовательские ABEND zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#user-abends "Настройка подсистемы сбора данных z/OS (zDC).") и [Сообщения модулей z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages "Сообщения, формируемые модулями Dynatrace z/OS.").