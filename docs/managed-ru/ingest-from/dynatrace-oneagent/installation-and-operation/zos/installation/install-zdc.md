---
title: Установка подсистемы zDC
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc
scraped: 2026-05-12T11:24:11.231792
---

# Установка подсистемы zDC

# Установка подсистемы zDC

* Чтение: 18 мин
* Обновлено 3 февраля 2026 г.

Подсистема z/OS Data Collection (zDC) взаимодействует с кодовыми модулями CICS, IMS и z/OS Java через объект общей памяти (SMO) на LPAR. Подсистема zDC поддерживает этот SMO, а модули записывают в него данные мониторинга.

Модуль zLocal (`libdtzagent.so`), размещённый в среде z/OS [Unix System Services](https://www.ibm.com/docs/en/zos/2.5.0?topic=zos-unix-system-services) (USS), работает в составе zDC. Он управляет TCP/IP-сокетным соединением с модулем zRemote, считывает данные мониторинга из SMO и передаёт их в zRemote.

Начальный загрузчик (`dtzagent`), размещённый в среде z/OS USS, работает в составе zDC. Он управляет процессом обновления zLocal.

При инициализации zDC (при запуске системы или вручную) он запускает начальный загрузчик, а тот запускает zLocal. При завершении работы zDC zLocal и начальный загрузчик останавливаются.

## Безопасность системы

zDC (zLocal) использует TCP/IP-сокетные соединения, поэтому может потребоваться обновить правила доступа вашей системы безопасности, если они настроены на запрет TCP/IP-доступа по умолчанию.

zDC не ограничивает перечень идентификаторов пользователей, которые могут вводить команды оператора.

Разрешения, назначаемые файлам, создаваемым zLocal и начальным загрузчиком, можно регулировать с помощью параметра `DT_UMASK`. По умолчанию используется `umask(022)`.

## Установка

zDC работает как авторизованный процесс z/OS (обычно как системная задача). Это означает, что программы должны находиться в авторизованной библиотеке. Предполагается, что zDC запускается автоматически как запускаемая задача при IPL системы, что обеспечивает его непрерывную доступность для сбора данных мониторинга из модулей.

zDC может также работать как пакетное задание. Класс обслуживания zDC должен быть достаточно высоким, чтобы он всегда был доступен для keep-alive-сообщений от zRemote. Приоритет zDC должен быть выше, чем у отслеживаемых регионов CICS и IMS.

Подсистема zDC должна быть установлена на каждом LPAR, который нужно отслеживать.

1. [Загрузите наборы данных продукта z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets "Скачайте и установите наборы данных продукта Dynatrace для z/OS."). Запишите квалификатор высокого уровня, использованный в процедуре загрузки.
2. Создайте RACF-идентификатор пользователя для процесса zDC. Этот идентификатор должен иметь сегмент z/OS USS. Рекомендуемое имя домашнего каталога: `/u/dt`.

   Если задан домашний каталог, отличный от `/u/dt`, измените в шаге 8 путь к начальному загрузчику, который по умолчанию равен `/u/dt/agent/lib64/dtzagent`. Имена путей ниже домашнего каталога изменить нельзя.

   Домашний каталог или заменяющий его квалификатор высокого уровня должны быть доступны для записи процессом zDC.

   * zDC записывает бинарный файл zLocal по пути `/u/dt/agent/downloads/native/a.b.c.d/zos-s390-64/libdtzagent.so` (версия zLocal, например 1.0.1.0).
   * zDC записывает логи zDC и zLocal по пути `/u/dt/log/dtxxx.log`.

   При сбое записи процессы zDC используют каталог `/tmp/dynaTrace`.

   Если zDC запускается как запускаемая задача, данный идентификатор должен быть способен представлять запускаемую задачу zDC и иметь доступ к указанному USS-пути.
3. Замените квалификатор высокого уровня набора данных, обозначенный как <hlq>, в элементе `COPYAGNT` набора `SZDTSAMP` на значение, использованное в процедуре [Загрузки наборов данных продукта z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets "Скачайте и установите наборы данных продукта Dynatrace для z/OS.").
4. Запустите задание `COPYAGNT`, чтобы создать необходимые подкаталоги z/OS USS в домашнем каталоге запускаемой задачи zDC.
5. Скопируйте бинарный файл `dtzagent` из `SZDTSAMP` и установите для него атрибут исполняемого файла.

   При использовании домашнего каталога по умолчанию `/u/dt` результирующий путь: `/u/dt/agent/lib64/dtzagent`.

   Если используется домашний каталог, отличный от `/u/dt`, путь в этом задании необходимо изменить соответствующим образом. Имена файлов и каталогов чувствительны к регистру. Имена путей ниже домашнего каталога изменить нельзя.

   Задание `COPYAGNT` рекомендуется запускать под идентификатором пользователя, созданным для процесса zDC, чтобы этот идентификатор владел бинарным файлом `dtzagent`. Если это неудобно, можно использовать команды `chown` и `chgrp` для сброса владельца и группы бинарного файла `dtzagent` после выполнения `COPYAGNT`.
6. Авторизуйте `<hlq>.SZDTAUTH`, подставив вместо `<hlq>` квалификатор высокого уровня из процедуры [Загрузки наборов данных продукта z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets "Скачайте и установите наборы данных продукта Dynatrace для z/OS.").

   Например, создайте элемент `SYS1.PARMLIB(PROGDT)` со следующим содержимым:

   ```
   APF FORMAT(DYNAMIC)



   APF ADD DSNAME(<hlq>.SZDTAUTH) VOLUME(XXXXXX)
   ```

   Затем введите команду консоли:

   ```
   SET PROG=DT
   ```
7. Скопируйте образец PROC запускаемой задачи zDC `ZDCMEPC` из `SZDTSAMP` в системную библиотеку PROCLIB, используемую для запускаемых задач.

   Имя PROC по умолчанию: `MEPC`. Настройте его в соответствии с местными стандартами. Если выбрано другое имя подсистемы, измените параметр `SUBSYSTEM_ID()` в [параметрах SYSIN](#sysin-parameters) соответственно.

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)



   SUBSYSTEM_ID(MEPC)
   ```

   PROC и два элемента JCL SYSIN `ZDCSYSIN` и `ZDCMEPCA`, которые он использует, содержат имена наборов данных, в которых необходимо заменить `<hlq>.` на соответствующие квалификаторы высокого уровня.
8. Обновите параметр `DTAGTCMD()` в [параметрах SYSIN](#sysin-parameters) в соответствии с вашими определениями.

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)



   DTAGTCMD(/u/dt/agent/lib64/dtzagent



   nobootstrap=false



   zremote=<ipaddress>[:port])
   ```

   * `/u/dt/agent/lib64/dtzagent` задаёт путь к начальному загрузчику. Имя домашнего каталога по умолчанию: `/u/dt`. Если в шаге 2 задан другой домашний каталог, измените значение соответственно.
   * `nobootstrap=false` разрешает начальному загрузчику автоматически обновлять zLocal при появлении новой версии. По умолчанию zLocal получает автоматические обновления. Установите `true`, чтобы отключить автоматические обновления и [обновлять zLocal вручную](#update-zlocal).
   * `zremote=<ipaddress>[:port]` задаёт IP-адрес и порт [установленного модуля zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовьте и установите zRemote для мониторинга z/OS."). IP-адрес обязателен, порт необязателен и по умолчанию равен 8898.
9. Проверьте, что соответствующий выход активен согласно версии OneAgent.

   | Версия OneAgent | Выход(ы) | Дополнительные примечания |
   | --- | --- | --- |
   | OneAgent версии 1.300+ | U86 | * Обязательно Необходимо, чтобы работала z/OS 2.3 или более поздняя версия. * Обязательно Выход U86 необходим для передачи данных о загрузке LPAR для метрик DPS и биллинга. + OneAgent версии 1.300 до OneAgent версии 1.314: Dynatrace может приостановить трассировку при отсутствии метрик DPS.   + OneAgent версии 1.315+: трассировка будет автоматически приостановлена, если метрика `host.zos.msu_hours` не получена в течение 12 последовательных часов.  При этом в лог zRemote записывается следующее сообщение:  `Tracing has been disabled. The LPAR[LPAR] has not sent valid billing metrics.`  Трассировка будет автоматически возобновлена после получения допустимых метрик `host.zos.msu_hours`. |
   | OneAgent версии 1.300 и ранее | U83 |  |

   Чтобы проверить активность выхода SMF U86, выполните следующую команду:

   ```
   D SMF,O
   ```

   В выводе команды найдите строки `SUBSYS(STC,EXITS(IEFU83))` и `SYS(EXITS(IEFU83))` или `SUBSYS(STC,EXITS(IEFU86))` и `SYS(EXITS(IEFU86))`.

   * Если эти строки найдены, выход SMF U83 и/или U86 активен. Перейдите к следующему шагу.
   * Если строки не найдены, добавьте их в элемент parmlib SMFPRMxx.

     + U83:

       ```
       SUBSYS(STC,EXITS(IEFU83)
       ```
     + U86:

       ```
       SUBSYS(STC,EXITS(IEFU86)
       ```

     Затем активируйте его.

     + U83:

       ```
       D PROG,EXIT,EN=SYS.IEFU83,DIAG
       ```
     + U86:

       ```
       D PROG,EXIT,EN=SYS.IEFU86,DIAG
       ```
10. Необязательно Добавьте команду в процедуру запуска системы для автоматического старта подсистемы zDC при IPL.
11. Используйте PROC `ZDCIVP` из `SZDTSAMP` для проверки установки zDC и подключения к zRemote.

    Успешный тест подключения к zRemote возвращает `Connection timeout`, так как zRemote не поддерживает протокол FTP. При наличии проблемы с подключением к zRemote она обозначается сообщением `EDC8128I Connection refused`. Это означает, что zRemote не прослушивает ожидаемый порт.

    Шаг ZDCXVER, ожидаемые сообщения JOBLOG:

    ```
    JOBnnnnn  IEA630I  OPERATOR ZDCXVER  NOW ACTIVE,   SYSTEM=ZZZZ    , LU=



    JOBnnnnn  D SMF,O



    JOBnnnnn  IEA631I  OPERATOR ZDCXVER  NOW INACTIVE, SYSTEM=ZZZZ    , LU=



    JOBnnnnn  IEA630I  OPERATOR ZDCXVER  NOW ACTIVE,   SYSTEM=ZZZZ    , LU=



    JOBnnnnn  D PROG,EXIT,EXITNAME=SYS.IEFU86,DIAG



    JOBnnnnn  IEA631I  OPERATOR ZDCXVER  NOW INACTIVE, SYSTEM=ZZZZ    , LU=



    JOBnnnnn  IEA630I  OPERATOR ZDCXVER  NOW ACTIVE,   SYSTEM=ZZZZ    , LU=



    JOBnnnnn  D PROG,EXIT,EXITNAME=SYSSTC.IEFU86,DIAG
    ```

    Шаг ZDCXVER, спул //SYSTSPRT; специальные символы используются для форматирования TSO 3270

    ```
    <3270> <Current Date/Time>



    <3270> Beginning of IEFU86 exit analysis......



    <3270> This routine inspects SMFPRMxx for active exits



    <3270> Also displays active ZDC information and release



    <3270> The status display should be all 'OK' for SM70(ZOSMETRICS) and DB2 performance metrics



    <3270> SYS.IEFU86 exit is active in SMFPRMxx



    <3270> STCSYS.IEFU86 exit is active in SMFPRMxx



    <3270> OK    ZDC Version is 1.vvv.0 ZDCSUBS(ZDTSMEPC)



    <3270> OK    SYS.EXIT(IEFU86) is active and is loaded at address: <hex>



    Note: Repeated for other zDCs
    ```

    Шаг SHOWIP, спул //SYSTSPRT, пример вывода

    ```
    Interface            Domain Port IP_ADDRESS



    OSA1I                AF_INET 0   172.23.243.82



    OSA2I                AF_INET 0   172.23.243.142



    IQDF0                AF_INET 0   10.250.250.82



    Interface Index  Interface



    65538            LOOPBACK



    65545            OSA1I



    65659            OSA2I



    65661            IQDF0



    Note: In this case, zDC PARM TCPIP_INTF() could specify OSA1I or OSA2I to set the LPARs IP address. This is usually used when a common VIPA address is used for the Sysplex. Without this parameter, the Dynatrace Hosts page may show multiple LPARs with the same IP address.
    ```

## Проверка установки

После завершения установки проверьте её корректность.

### Проверка корректного запуска zDC

Убедитесь, что zDC запустился в правильной версии, успешно инициализировался и запустил zLocal. Найдите следующие сообщения в `zDC SYSPRINT DD`.

```
ZDC000I INITIALIZATION STARTED FOR zDC  VER 1.195.00



ZDC052I zDC IS RUNNING ON Z/OS RELEASE 02.02.00



ZDC053I LPAR NAME IBMSYS1    CVTSNAME S0W1



.



.



.



.



ZDC955L Dynatrace connection being processed ZDC-Job/ID:AFVBZ021/Z021



ZDC958L Dynatrace INIT completed, ZDC AgentId received ZDC-Job/ID:AFVBZ021/Z021



ZDC993I Opn1RFD:0008  /u/labuser/adcdk/ci/7.2build/log/dt_Z021_Z021_33620108.0.log



ZDC955I Dynatrace connection being processed ZDC-Job/ID:AFVBZ021/Z021
```

Если в журнале заданий zDC появляется следующее сообщение (имя вашей подсистемы может отличаться от `MEPC`), [перезапустите zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc/customize-zdc#terminate-zdc "Настройка подсистемы zDC.") с другим значением `SUBSYSTEM_ID` в [параметрах SYSIN](#sysin-parameters).

```
11:55:30.419083 ZDC006E SUBSYSTEM MEPC ALREADY EXISTS AND IS ACTIVE
```

### Проверка корректного запуска zLocal и его подключения к zRemote

zLocal записывает сообщения журнала в zDC SYSPRINT DD, а также в `/u/dt/log` в среде z/OS USS. Лог zLocal содержит сведения о запуске zLocal, версионировании и подключении к zRemote.

Чтобы убедиться, что все каналы zLocal подключены к zRemote, найдите следующие сообщения в SYSPRINT:

```
info    [native] dynaTrace z Remote Agent data channel connected successfully, performing handshake.



info    [native] dynaTrace z Remote Agent client handshake performed.



info    [native] dynaTrace z Remote Agent data channel handshake successful, version[rr.rr.rr.bbbb].



info    [native] dynaTrace z Remote Agent control channel connected successfully, performing handshake



info    [native] dynaTrace z Remote Agent handshakes are complete, all channels are fully operational.
```

Используйте приведённую ниже [команду z/OS MODIFY](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc/customize-zdc#Thezos-modify-cmd "Настройка подсистемы zDC."), чтобы указать zDC отобразить статус zLocal и найти пути к файлам журналов zLocal и zRemote.

```
MODIFY <zdc-jobname>,DT1 STDO
```

После обнаружения файла журнала zLocal к нему можно получить доступ стандартными методами. Используйте OMVS, ssh/telnet или просмотрите его в веб-интерфейсе Dynatrace как обычный файл журнала OneAgent.

Также найдите следующие сообщения в соответствующем файле журнала zRemote (значения в скобках должны отражать реальные данные).

```
info    [native] dynaTrace z Local Agent handshakes are complete, all channels are fully operational, version[rr.rr.rr.bbbb].



info    [native] Data client socket listener thread started



info    [native] ASID[48], smfID[S0W1], sysid[Z208], jobName[AF71Z208], subagentid[da57ff16] smfID.JobID[S0W1    .JOB92014], zDC release 65 was successfully initialized with protocol version=6.5.0



info    [native] zDC[Z208] SMO is initialized with size=10M.



info    [native] Registering the zdc[48]
```

### Проверка уровня обслуживания загрузочного модуля zLocal

Просмотрите установочную библиотеку `<hlq>.R1nnnxx.SZDTAUTH` (квалификатор высокого уровня набора данных продукта), чтобы найти загрузочный модуль `ZDCDTAGT` для zLocal.

В приведённом ниже примере заголовка видно значение `1.nnn.00`, которое означает, что это версия загрузочного модуля без применённого обслуживания. При применении обслуживания поле содержит номер подверсии, например `1.nnn.01`. Даты меняются со временем.

```
ZDCDTAGT 00000000 YYYYMMDD HH.MM VER 1.nnn.00 COPYRIGHT (C)...
```

Загрузочный модуль `ZDCDTAGT` может выдавать диагностические сообщения в следующем формате:

```
ZDC99<n><i>
```

Здесь `n` обозначает уровень журналирования, а `i` обозначает степень серьёзности.

### Сообщение о недостаточных правах доступа при запуске zDC

Если в журнале заданий zDC появляются следующие сообщения (или аналогичные):

```
H408I USER(xxxxxxxx) GROUP(xxxx) NAME(STARTED TASK )



BPX.FILEATTR.PROGCTL CL(FACILITY)



INSUFFICIENT ACCESS AUTHORITY



ACCESS INTENT(READ ) ACCESS ALLOWED(NONE )
```

И в файле журнала zLocal появляются связанные сообщения:

```
JJJJ-MM-DD HH:MM:SS  3f8bbe02¨ info  native¨ Server requests us to use Agent



dTMajor.dTMinorVersion.0.dTBuild with a hash of 0317af199c1ab1a03dda2cee90c2ea61



JJJJ-MM-DD HH:MM:SS  3f8bbe02¨ info  native¨ Requesting Agent library from Server



JJJJ-MM-DD HH:MM:SS  3f8bbe02¨ info  native¨ Error setting Agent library program



controlled: EDC5139I Operation not permitted.



JJJJ-MM-DD HH:MM:SS  3f8bbe02¨ info  native¨ Loading Agent



/dt/dynatrace-<dTMajor.dTMinorVersion.0>/agent/downloads/<dTMajor.dTMinorVersion.0.dTBuild>



/native/zos-s390-64/libdtzagent.so
```

Их можно безопасно проигнорировать.

После первоначальной загрузки zLocal операционная система пытается установить флаг для загруженной библиотеки, который необходим в определённых обстоятельствах. Флаг не устанавливается при повторном запуске, так как библиотека больше не загружается, если она уже существует.

## Набор данных SYSIN

Все значения, настраивающие выполнение zDC, хранятся в наборе данных, на который указывает `DDNAME SYSIN`. Образец PROC запускаемой задачи `ZDCMEPC` ссылается на элемент JCL SYSIN `ZDCSYSIN` набора `SZDTSAMP`, как показано ниже:

```
//SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)
```

Набор данных должен содержать записи по 80 символов, блокированные кратно 80 байтам.

При внесении любых изменений в набор данных SYSIN для их вступления в силу необходимо перезапустить процесс zDC.

### Параметры SYSIN

Позиции с 1 по 71 каждого оператора могут содержать значения параметров. Позиции с 72 по 80 игнорируются и могут содержать порядковый номер.

Каждый параметр использует формат `KEYWORD(value)`. Каждое ключевое слово и требования к связанным с ним значениям задокументированы в элементе JCL SYSIN `ZDCSYSIN` набора `SZDTSAMP`.

Если значение параметра занимает несколько строк, укажите значение до позиции 71 и продолжите его на следующем операторе, начиная с позиции 1.

Как добавить комментарий к оператору?

Чтобы использовать комментарий, поместите звёздочку в позицию 1 оператора. Весь оператор считается частью комментария.

Комментарий может быть заключён между косой чертой со звёздочкой и звёздочкой с косой чертой.

```
/* This is a comment. */
```

Комментарии такого типа могут занимать несколько строк.

| Параметр(значение по умолчанию) | Описание |
| --- | --- |
| DTAGTCMD(/u/dt/agent/lib64/dtzagent) | Задаёт путь к начальному загрузчику `dtzagent`.  Дополнительные параметры:  * `nobootstrap=false` разрешает начальному загрузчику автоматически обновлять zLocal при появлении новой версии. Установите `true`, чтобы отключить автоматические обновления. * `zremote=<ipaddress>[:port]` задаёт IP-адрес и порт [установленного модуля zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовьте и установите zRemote для мониторинга z/OS."). IP-адрес обязателен, порт необязателен и по умолчанию равен 8898. * `name=zlocal_<lpar>` задаёт имя zLocal для файлов журналов. Имя должно отражать, что это zLocal, и может включать SMF ID обслуживаемого LPAR. * `loglevel=<value>` задаёт уровень журналирования zLocal. Допустимые значения: `FINEST`, `FINER`, `FINE`, `CONFIG`, `INFO`, `WARNING`, `SEVERE`, `DEBUG`, `NONE`). Значение по умолчанию отсутствует. |
| SUBSYSTEM\_ID(MEPC) | Определяет имя подсистемы zDC. Должно содержать четыре непробельных символа:  * Первый символ: прописная буква (A:Z). * Последние три символа: прописные буквы или цифры (#,$,@,A:Z,0-9). |
| DEFAULT(YES) | Определяет подсистему zDC как основную. Данные мониторинга собирает основная подсистема zDC, в которой задано `DEFAULT(YES)`. При запуске нескольких подсистем zDC на одном LPAR необходимо указать `DEFAULT(NO)` для каждой дополнительной подсистемы, иначе они не инициализируются. |
| DISPLAY\_NAME() | Определяет отображаемое имя данной подсистемы zDC для её идентификации в определённых сообщениях журнала. |
| DTLOGLEVEL(3) | Задаёт уровень журналирования zDC. Допустимые значения: от `0` до `8`. Установите значение `4`, чтобы подавить информационные сообщения. Значения ниже `3` следует использовать только для диагностической отладки. |
| DTMSG\_SMOSIZE(1) | Задаёт максимальный объём памяти (МБ) для сообщений, которые могут находиться в очереди в объекте общей памяти zDC в ожидании записи в модули z/OS. Значение по умолчанию 1 МБ достаточно в большинстве случаев при включённой буферизации транзакций. При отключённой буферизации транзакций (не рекомендуется) при очень большом объёме трассируемых транзакций установите размер SMO 10 МБ. |
| DTCHDIR(/u/dt) | Изменяет текущий каталог z/OS USS, в котором начальный загрузчик `dtzagent` создаёт временные файлы для `stdin`, `stdout` и `stderr`. По умолчанию используется домашний каталог связанного идентификатора пользователя. |
| DTMSG\_TRANBUFSIZE(n,m) | Переопределяет количество и размер буферов транзакций по умолчанию. Буферы транзакций повышают производительность для модулей CICS и IMS, помещая сообщения о событиях, связанных с каждой распределённой трассировкой, в выделенные буферы. Вместо отправки отдельных сообщений о событиях по мере их возникновения они группируются в один или несколько буферов и отправляются совместно. Кроме того, буфер связанных сообщений обрабатывается zRemote более эффективно.  Параметр `n` задаёт количество буферов в тысячах. Например, 2 = 2 000 буферов. Нулевое значение отключает буферы транзакций. Параметр `m` должен быть равен `2` или `4`, задавая размер буфера 2 КБ или 4 КБ. Мы рекомендуем размер буфера 4 КБ, если потребление памяти не является критически важным. Минимальное ненулевое значение: `1,2`. Максимальное: `126,4` или `248,2`, что соответствует общему размеру 512 МБ. Верхняя граница требуемого числа буферов: один на каждый регион сообщений IMS и MAXTASK, умноженное на количество регионов CICS; однако фактические потребности, как правило, значительно меньше. |

## Журналирование

Уровень журналирования zDC задаётся параметром `DTLOGLEVEL()` в [параметрах SYSIN](#sysin-parameters). Изменить уровень журналирования динамически можно с помощью [команды z/OS MODIFY](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc/customize-zdc#Thezos-modify-cmd "Настройка подсистемы zDC.").

```
//SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)



DTLOGLEVEL(3)



MODIFY <jobName>,DT1 LOG=1
```

Просматривайте вывод сообщений журнала в спуле заданий zDC. Спул заданий помогает определить ошибки, которые могут возникнуть при запуске zDC или при подключении к zRemote. После успешного подключения zDC к zRemote сообщения об ошибках от подсистемы zDC и модулей CICS и IMS направляются в zRemote.

Уровень журналирования zLocal задаётся параметром `DTAGTCMD(loglevel=INFO)` в [параметрах SYSIN](#sysin-parameters). Изменить уровень журналирования динамически можно с помощью [команды z/OS MODIFY](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc/customize-zdc#Thezos-modify-cmd "Настройка подсистемы zDC."). Параметр `DTAGTCMD(name=zlocal_<lpar>)` задаёт имя zLocal для файлов журналов. Имя должно отражать, что это zLocal, и может включать SMF ID обслуживаемого LPAR.

```
//SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)



DTAGTCMD(loglevel=INFO name=zlocal_<lpar>)



MODIFY <jobname>,DT1 ZLALOGLEVEL=FINE
```

Для zLocal создаются два набора журналов. Оба набора создаются в файловой системе OMVS. Один набор является временным и действителен только для текущего выполнения zDC; расположение этих журналов по умолчанию соответствует домашнему каталогу идентификатора пользователя zDC. Переопределить расположение можно с помощью параметра `DTCHDIR()` в [параметрах SYSIN](#sysin-parameters).

zLocal также создаёт стандартный набор журналов: один для начального загрузчика и один для самого zLocal. Эти журналы находятся в стандартных расположениях журналов Dynatrace в файловой системе OMVS.

## Обновление и обслуживание

1. [Загрузите наборы данных продукта z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#download-pax "Скачайте и установите наборы данных продукта Dynatrace для z/OS.") и [распакуйте их](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#extract-datasets "Скачайте и установите наборы данных продукта Dynatrace для z/OS.").
2. Обновите задание zDC так, чтобы оно указывало на новый `<hlq>.SZDTAUTH`. Если вы [задали псевдоним](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#alias "Скачайте и установите наборы данных продукта Dynatrace для z/OS."), переопределите его. Например:

   ```
   DELETE 'DT.DYNTRC.SZDTAUTH' NOSCRATCH



   DEFINE ALIAS(NAME('DT.DYNTRC.SZDTAUTH') RELATE('DT.R12710.SZDTAUTH'))
   ```

Обновление подсистемы zDC с версии 1.211 или более ранней

При обновлении подсистемы zDC с версии 1.211 или более ранней требуется специальная обработка, чтобы избежать аварийного завершения (abend) в отслеживаемых регионах CICS.

1. Остановите zDC.
2. Подождите **15 минут**, пока модуль CICS сбросит и очистит управляющие блоки.
3. Обновите zDC до более новой версии.
4. Запустите zDC.

### zLocal

По умолчанию zLocal получает автоматические обновления, если в [параметрах SYSIN](#sysin-parameters) задано `DTAGTCMD(nobootstrap=false)`. При каждом запуске zDC начальный загрузчик запрашивает у модуля zRemote наличие доступных обновлений. Последняя версия zLocal устанавливается в составе установки zRemote. При наличии обновления zLocal автоматически загружается из zRemote и обновляется.

Примеры сообщений журнала в выводе заданий zDC при автоматических обновлениях

```
info    (native) The bootstrap channel connected successfully, requesting version: a.b.c.d



info    (native) Interprocess lock acquired for /u/dt/agent/downloads/native/a.b.c.d/zos-s390-64/libdtzagent.so



info    (native) Fetching agent binary succeeded for /u/dt/agent/downloads/native/a.b.c.d/zos-s390-64/libdtzagent.so
```

### Обновление zLocal вручную

* Не используйте процедуру обновления вручную для zLocal при первом подключении к вашему окружению Dynatrace, так как zDC не запустится успешно.
* Модуль zRemote должен быть запущен при первом старте zDC, чтобы избежать [аварийного завершения пользователя](#user-abends) `U103`.

Если получение автоматических обновлений для zLocal не требуется, задайте `DTAGTCMD(nobootstrap=true)` в [параметрах SYSIN](#sysin-parameters). При ручном обновлении бинарный файл zLocal `libdtzagent.so` должен находиться на LPAR в каталоге `/u/dt/agent/lib64`.

Для этого выполните следующее

1. Запустите начальный загрузчик `dtzagent` хотя бы один раз на производственном или непроизводственном LPAR.
2. Скопируйте бинарный файл zLocal на целевой LPAR. В наборе данных `SZDTSAMP` элемент `OCOPYAGT` является заданием, которое копирует бинарный файл zLocal `libdtzagent.so` в каталог `/u/dt/agent/lib64`.
3. Выполните инструкции по запуску zDC и его подключению к вашему окружению Dynatrace.
4. При успешном подключении zDC к Dynatrace файл `libdtzagent.so` копируется в каталог `/u/dt/agent/downloads/native/a.b.c.d/zos-s390-64/libdtzagent.so` (версия zLocal, например 1.0.1.0).

Примеры сообщений журнала в выводе заданий zDC при обновлении вручную

```
info    (native) Configured to not download module - loading local module



info    (native) Start loading local agent binary



info    (native) Successfully loaded agent binary /u/dt/agent/lib64/libdtzagent.so
```

## Аварийные завершения пользователя zDC

zDC может завершиться аварийным завершением пользователя (user abend) из-за внутренних ошибок и сбоев инициализации. Все аварийные завершения, кроме `U103` и `U106`, создают дамп-файл. Ниже приведён список возможных аварийных завершений.

| Аварийное завершение | Описание |
| --- | --- |
| U100 | Внутренняя ошибка вследствие сбоя инициализации zDC. |
| U101 | Инициализация zDC завершилась сбоем, отобразить сообщение об ошибке невозможно. |
| U102 | Хранилище ECSA недоступно для zDC. |
| U103 | Проблема возникла во время операции RETRY из подпрограммы восстановления. |
| U104 | Задача очереди завершилась аварийно. Это аварийное завершение сопровождается сообщением `ZDC066E` в SYSLOG. |
| U105 | Задача очереди завершилась аварийно, когда завершение работы НЕ выполнялось. |
| U106 | Фатальная ошибка в подпрограмме TCPSP. |
| U110 | Это аварийное завершение может возникать по различным причинам внутренних ошибок. Оно сопровождается одним из следующих сообщений об ошибках zDC в SYSLOG:  * `ZDC988E` * `ZDC987E` * `ZDC985E` * `ZDC984E` * `ZDC983E` * `ZDC982E` * `ZDC981E` * `ZDC988E` * `ZDC982E` * `ZDC981E` * `ZDC979E` * `ZDC978E` |
| U111 | Внутренняя ошибка в одном из модулей zDC. Аварийное завершение сопровождается одним из следующих сообщений об ошибках в SYSLOG:  * `AgtSt:DqrIErr-Get Token/Name for FML failed` * `AgtSt:DqrILod LOAD failed` * `AgtSt:Waiting for Que Data Space failed-Abort` |
| U205 | zDC не может открыть SYSPRINT или SYSPRIN3 DD для отображения сообщений журнала. |
| U222 | Внутренняя ошибка в одном из модулей zDC. Аварийное завершение сопровождается одним из следующих сообщений в SYSLOG:  * `066E IEAVRLS Error limit!` * `066E Freed dead TBC Error-Abend222` |

## Устранение неполадок

* [Устранение неполадок подсистемы zDC](https://dt-url.net/al03k4i)