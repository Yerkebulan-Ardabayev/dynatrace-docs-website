---
title: Установка модуля CICS
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics
scraped: 2026-03-05T21:29:30.899274
---

# Установка модуля CICS


* Последняя версия Dynatrace
* 14 минут чтения
* Обновлено 28 января 2026 г.

С помощью модуля CICS можно получить возможность наблюдаемости транзакций и программ CICS, включая вызовы DB2, DLI и VSAM.

Трассируйте транзакции CICS от начала до конца с Dynatrace

Анализируйте производительность транзакций от начала до конца с помощью [потока сервисов](../../../../../observe/application-observability/services-classic/service-backtrace.md "Отслеживайте последовательность вызовов сервисов вплоть до клика в браузере, который инициировал цепочку вызовов.").

![Поток сервисов CICS](https://dt-cdn.net/images/cics-trace-2357-0a7717e199.png)

Используйте [распределённые трассировки PurePath](../../../../../observe/application-observability/distributed-traces.md "Получите наблюдаемость в высокодистрибутивных, облачно-нативных архитектурах для эффективной трассировки и анализа транзакций в реальном времени."), чтобы детализировать информацию до уровня кода и оптимизировать свои программы.

![Уровень кода CICS](https://dt-cdn.net/images/cics-code-level-1984-d6aeff52fb.png)

Понимайте исключения в контексте ваших транзакций вплоть до уровня базы данных Db2.

![Распределённая трассировка CICS с исключением](https://dt-cdn.net/images/cics-distributed-trace-1986-97b2240549.png)

Обнаруживайте аномалии CICS и изолируйте домены сбоев с Dynatrace

Интеллект Dynatrace автоматически определяет первопричину проблем и оценивает их влияние на пользователей, чтобы вы могли расставлять приоритеты в стратегиях по устранению и сокращать среднее время восстановления.

![Автоматическая изоляция домена сбоев CICS](https://dt-cdn.net/images/cics-problem-1985-100d80f55c.png)

Анализируйте сбои с подробными сведениями об исключениях в контексте транзакций.

![Анализ сбоев CICS](https://dt-cdn.net/images/cics-exceptions-1985-478b6f8ba6.png)

## Установка

Модуль CICS включает программу PLT, которая инициализируется при запуске CICS. Эта программа использует хуки для инструментирования регионов CICS с терминальными и прикладными владельцами, создавая интересующие события. Она пересылает данные мониторинга в подсистему zDC через общие буферы.

Необходимо установить модуль CICS в каждый регион CICS, который вы хотите отслеживать. Если Dynatrace уже установлен на CICS и вы хотите обновить модуль CICS без перезапуска региона CICS, см. раздел [Обновление модуля CICS без перезапуска региона](#cics-update).

Необходимо добавить [модуль Java z/OS](install-zos-java.md#middleware "Настройте мониторинг Java на z/OS с помощью модуля Java.") к каждому CICS Transaction Gateway, который вы хотите отслеживать.

### Поддержка CTS 6.2

Начиная с версии OneAgent 1.299, предоставляется поддержка CTS 6.2 — это значительное изменение, следующее за последними улучшениями безопасности для подсистемы CICS.

Поддержка CTS 6.2 требует, чтобы загрузочный модуль `DFHBPZDT`, поставляемый в `SZDTAUTH`, был доступен при запуске региона CICS.
Рекомендуемая процедура установки:

Добавьте строку, аналогичную приведённому ниже примеру, в член parmlib PROGxx. Обратите внимание, что `SZDTAUTH` должен иметь APF-авторизацию.

```
LPA ADD MODNAME(DFHBPZDT) DSNAME(<hlq>.SZDTAUTH)
```

Чтобы немедленно добавить модуль в LPA, введите консольную команду, аналогичную приведённому ниже примеру.

```
SETPROG LPA,ADD,MODNAME=DFHBPZDT,DSNAME=<hlq>.SZDTAUTH
```

Кроме того, можно добавить `DFHBPZDT` в `STEPLIB` регионов CICS 6.2, где установлен агент Dynatrace.
Однако мы не рекомендуем добавлять весь `SZDTAUTH` в STEPLIB CICS.

Для проверки установки CTS 6.2 выводит следующее сообщение:

```
DFHKE0010  HVPAC449 Vendor table DFHBPZDT for product ID ZDT has been loaded
```

### Определение библиотеки CICS

Можно динамически добавить загрузочную библиотеку в качестве определения библиотеки CICS в CSD. Определение CEDA находится в члене `CICRDO` набора данных `SZDTSAMP`. Его можно найти в примере в следующем разделе.

Если вы не хотите использовать определение библиотеки CICS, необходимо добавить следующий PDS (или его содержимое) в конкатенацию DFHRPL:

```
// DD DISP=SHR,DSN=<hlq>.SZDTLOAD
```

Независимо от того, какой вариант вы выберете, необходимо настроить DSN, заменив `<hlq>` квалификатором высокого уровня, заданным при [скачивании наборов данных продукта z/OS](zosmf-installer/download-zos-datasets.md "Скачайте и установите наборы данных продукта Dynatrace для z/OS.").

### Программы и транзакции Dynatrace CICS

Определения ресурсов CICS для модуля Dynatrace CICS находятся в члене `CICRDO` набора данных `SZDTSAMP`, который предназначен для использования с пакетной утилитой `RDO` `DFHCSDUP`.

Мы рекомендуем использовать эти имена транзакций и групп, но вы можете изменить их в соответствии с правилами вашей установки. Согласуйте имя группы и имя списка групп с вашим администратором CICS. Замените `XYZLIST` именем вашего списка групп (`GRPLIST`).

Хотя мы рекомендуем использовать идентификатор транзакции по умолчанию `DTAX` для `ZDTPLT`, вы также можете использовать пользовательский идентификатор транзакции вместо `DTAX` в ваших определениях, если возникают конфликты с определениями транзакций.

### Таблица программного списка запуска CICS

Добавьте программу запуска CICS (`ZDTPLT`) после записи `DFHDELIM` в исходный код PLTPI и скомпилируйте таблицу.

Этот шаг является необязательным для тестовых установок, поскольку вместо него можно использовать [транзакцию DTAX](../operation/dtax-transaction.md "Управляйте модулем CICS с помощью транзакций DTAX.") для активации модуля после инициализации CICS. Мы рекомендуем помещать запись `ZDTPLT` непосредственно перед спецификацией `TYPE=FINAL`.

Процедуру JCL `DFHAUPLE` в `CICSHLQ.SDFHINST(DFHAUPLE)` можно использовать для построения таблицы PLTPI.

Пример таблицы PLTPI, содержащей программу запуска CICS

```
*


* PLT USED TO SUPPORT DYNATRACE CODE MODULE INITIALIZATION


*


DFHPLT TYPE=INITIAL,SUFFIX=SI


DFHPLT TYPE=ENTRY,PROGRAM=DFHDELIM


* Other PLT startup programs here...


DFHPLT TYPE=ENTRY,PROGRAM=ZDTPLT


DFHPLT TYPE=FINAL


END
```

Пользователи глобальной защиты хранилища Compuware Xpediter

Программа запуска PLT (`ZDTPLT`) инициализирует рабочую область выхода модуля CICS, которую CICS получает от его имени. Такие продукты, как Compuware Xpediter/CICS, могут быть настроены на применение строгих средств управления доступом к хранилищу и могут прерывать `ZDTPLT`, препятствуя запуску модуля CICS, если только он не исключён из этих средств управления. Если вы используете функцию глобальной защиты хранилища Xpediter/CICS, добавьте запись `monitor exceptions` в DD XDDBPINP в JCL региона CICS для исключения `ZDTPLT*`. Например:

```
DBPA 17.02 TRAN=*,PROGRAM=ZDTPLT*,CSECT=*
```

### Таблица программного списка завершения CICS

Добавьте программу завершения CICS (`ZDTPLTSD`) перед записью `DFHDELIM` в исходный код PLTSD и скомпилируйте таблицу.

Мы рекомендуем помещать запись `ZDTPLTSD` непосредственно после спецификации `TYPE=INITIAL`.

Процедуру JCL `DFHAUPLE` в `CICSHLQ.SDFHINST(DFHAUPLE)` можно использовать для построения таблицы PLTSD.

Пример таблицы PLTSD, содержащей программу завершения CICS

```
*


* PLT USED TO SUPPORT DYNATRACE CODE MODULE SHUTDOWN


*


DFHPLT TYPE=INITIAL,SUFFIX=SD


DFHPLT TYPE=ENTRY,PROGRAM=ZDTPLTSD


* Other PLT shutdown programs here...


DFHPLT TYPE=ENTRY,PROGRAM=DFHDELIM


DFHPLT TYPE=FINAL


END
```

### Подключение модуля CICS к подсистеме zDC

Программа запуска PLT (`ZDTPLT`) автоматически подключается к подсистеме zDC по умолчанию при инициализации региона CICS.

Если запущено несколько подсистем zDC, она подключается к той, которая указывает `DEFAULT(YES)`, если только параметр переопределения `INITPARM` в параметрах CICS SYSIN не указывает, что она должна подключиться к zDC с определённым именем:

```
INITPARM=(ZDTPLT='MEPC,<option>'),
```

`<option>` задаёт уровень журнала для модуля CICS; см. раздел [Ведение журнала](#logging).

Для проверки подключения между модулем CICS и подсистемой zDC [отправьте эхо-запрос](../operation/dtax-transaction.md#ping "Управляйте модулем CICS с помощью транзакций DTAX.").

## Настройка

### Группировка имён CICSPlex

Вы можете объединить регионы CICS, принадлежащие одному CICSPlex, в одну группу процессов. Для этого:

1. Перейдите в **Настройки** > **Mainframe** > **Мониторинг транзакций**.
2. Включите параметр **Группировать регионы CICS, принадлежащие одному CICSPlex**.
3. Добавьте `MASPLTWAIT(YES)` в параметр LMAS. Это указывает региону CICS ждать доступности CICSPlex перед продолжением. Если CICSPlex недоступен, модуль не сможет его учесть.
4. Необязательно Интервал ожидания `MASINITTIME(10)` по умолчанию составляет 10 минут. Его можно настроить в диапазоне от 5 до 59 минут.

Если вы включили группировку имён CICSPlex **после** запуска региона CICS, необходимо выполнить [транзакцию DTAX](../operation/dtax-transaction.md "Управляйте модулем CICS с помощью транзакций DTAX.") `DTAX DISABLE` и `DTAX ENABLE`.

### Поддержка веб-сервисов CICS

Модуль CICS может трассировать веб-сервисы CICS, вызываемые через запрос SOAP или запрос JSON (конвейер JSON без Java). Для трассировки запросов JSON требуется OneAgent версии 1.257 или более поздней.

Чтобы трассировать программы поставщиков веб-сервисов CICS, вызываемые программами-обработчиками из конвейеров CICS SOAP или конвейеров CICS JSON без Java, обновите файл конфигурации конвейера поставщика (`.xml`), добавив `ZDTSOAPH`, как показано ниже.

Dynatrace поддерживает только конвейеры, использующие стандартный обработчик терминала. Если вы используете нестандартный обработчик терминала, его можно инструментировать с помощью CICS и IMS SDK. В качестве отправной точки можно использовать следующие примеры кода:

* [ADKJSONA](https://assets.dynatrace.com/global/doc/appmon/integrations-and-extensions/development-kits/agent-development-kit-adk/cics-and-ims-adk/adkjsona.txt) — пример CICS Assembler для начальных путей запросов JSON в написанном пользователем обработчике приложений.
* [ADKJSONC](https://assets.dynatrace.com/global/doc/appmon/integrations-and-extensions/development-kits/agent-development-kit-adk/cics-and-ims-adk/adkjsonc.txt) — пример CICS COBOL для начальных путей запросов JSON в написанном пользователем обработчике приложений.

#### Конвейер CICS SOAP

`DFHPITP` — программа обработчика приложений, используемая в конфигурации конвейера CICS SOAP, которая вызывает программы поставщиков сервисов. В дополнение к `DFHPITP` в конвейере кодовый модуль CICS также поддерживает написанные пользователем терминальные программы.

Обновите файл конфигурации конвейера, включив `ZDTSOAPH` в строфу `<headerprogram>` под элементом обработчика SOAP. Обратите внимание, что все конвейеры SOAP имеют элемент обработчика SOAP `<cics_soap_1.1_handler>` или `<cics_soap_1.2_handler>`, куда добавляется `ZDTSOAPH`. Ниже приведён пример конвейера поставщика CICS SOAP, обновлённого с `ZDTSOAPH`.

Для трассировки исходящих запросов SOAP, возникающих в транзакциях CICS, трассируемых модулем CICS, добавьте строфу `<headerprogram>` в определения конвейера запрашивающей стороны для тех сервисов SOAP, которые должны трассироваться. Исходящие запросы SOAP, возникающие в транзакциях CICS, которые не трассируются, игнорируются. Однако трассировка не ограничена запросами от программ SOAP, выступающих в роли поставщиков сервисов CICS SOAP.

```
<?xml version="1.0" encoding="EBCDIC-CP-US"?>


<provider_pipeline


xmlns="http://www.ibm.com/software/htp/cics/pipeline"


xmlns:xsi="http://www.w3.org/2001/XMLSchemainstance"


xsi:schemaLocation="http://www.ibm.com/software/htp/


cics/pipeline/provider.xsd ">


<service>


<terminal_handler>


<cics_soap_1.1_handler>


<headerprogram>


<program_name>ZDTSOAPH</program_name>


<namespace>*</namespace>


<localname>*</localname>


<mandatory>true</mandatory>


</headerprogram>


</cics_soap_1.1_handler>


</terminal_handler>


</service>


<apphandler>DFHPITP</apphandler>


</provider_pipeline>
```

#### OneAgent версии 1.257+ — конвейер CICS JSON без Java

`DFHPIJT` — программа обработчика терминала, используемая в конвейере CICS JSON без Java, которая вызывает программы поставщиков сервисов. Для трассировки поставщика веб-сервисов CICS, вызываемого через конвейер JSON без Java, обновите файл конфигурации конвейера, включив `ZDTSOAPH` в строфу `<handler>` под XML-тегами `<default_http_transport_handler_list>`. Ниже приведён пример конвейера поставщика CICS JSON без Java, обновлённого с `ZDTSOAPH`.

```
<?xml version="1.0" encoding="EBCDIC-CP-US"?>


<provider_pipeline xmlns="http://www.ibm.com/software/htp/cics/pipeline">


<transport>


<default_http_transport_handler_list>


<handler>


<program>ZDTSOAPH</program><handler_parameter_list/>


</handler>


</default_http_transport_handler_list>


</transport>


<service>


<terminal_handler>


<handler>


<program>DFHPIJT</program><handler_parameter_list/>


</handler>


</terminal_handler>


</service>


</provider_pipeline>
```

### Маршрутизация сообщений DTAX с использованием TDQueue

Необязательно Для маршрутизации сообщений DTAX в TDQueue Dynatrace (Transient Data Queue) используйте определение ресурса `ZDTQ`, указанное выше в члене `CICRDO`.

Сообщения DTAX будут записываться в TDQueue ZDTQ только в том случае, если очередь открыта. При использовании предоставленного определения ресурса очередь остаётся закрытой из-за атрибута `OPENTIME(DEFERRED)`. Можно открыть её вручную с помощью команды `CEMT INQUIRE|SET TDQUEUE` или настроить открытие очереди в момент инициализации, изменив определение TDQUEUE для ZDTQ на использование атрибута `OPENTIME(INITIAL)`.

## Ведение журнала

Управлять уровнем журнала модуля CICS можно с помощью [транзакции DTAX](../operation/dtax-transaction.md "Управляйте модулем CICS с помощью транзакций DTAX.") или указав необязательный параметр `INITPARM` при запуске региона CICS.

```
INITPARM=(ZDTPLT='MEPC,<Option>'),
```

`<Option>` задаёт уровень ведения журнала для модуля CICS. Допустимые значения:

1. `FINE` | `F` — подробное ведение журнала. Рекомендуем включать только при возникновении проблем с запуском модуля CICS.
2. `INFO` | `I` — информационное ведение журнала. Это значение по умолчанию.
3. `WARNING` | `W` — ведение журнала предупреждений.
4. `SEVERE` | `S` — ведение журнала критических сообщений.

```
Example:


INITPARM=(ZDTPLT='MEPC,SEVERE'),
```

Существует два набора журналов CICS:

* Один набор сообщений появляется, когда [транзакция DTAX](../operation/dtax-transaction.md "Управляйте модулем CICS с помощью транзакций DTAX.") выполняет команды `DISABLE` и `ENABLE`. Эти сообщения записываются в Transient Data Queue CICS CSMT (обычно записывается в MSGUSR). Просматривайте эти сообщения в журнале задания CICS. DTAX также записывает набор сообщений в инструкцию SYSOUT CEEOUT при возникновении ошибок в соединении между zDC и транзакцией DTAX. Просматривайте эти сообщения в журнале задания CICS. Пока транзакция DTAX может подключиться к zDC, она записывает свои сообщения в zRemote.
* Мониторинговая транзакция модуля CICS маршрутизирует свои сообщения журнала в zDC, а затем в zRemote. В журнале показывается, происходили ли повреждённые распределённые трассировки, тайм-ауты или другие ошибки. В этих журналах также может отображаться некоторая статистическая информация.

Доступ к журналам CICS можно получить через [журналы zRemote](install-zremote.md#logging "Подготовьте и установите zRemote для мониторинга z/OS.").

## Обновление без перезапуска региона

Для обновления модуля CICS до более новой версии без перезапуска региона:

1. [Скачайте наборы данных продукта z/OS](zosmf-installer/download-zos-datasets.md#download-pax "Скачайте и установите наборы данных продукта Dynatrace для z/OS.") и [извлеките их](zosmf-installer/download-zos-datasets.md#extract-datasets "Скачайте и установите наборы данных продукта Dynatrace для z/OS.").
2. Используйте [транзакцию DTAX](../operation/dtax-transaction.md "Управляйте модулем CICS с помощью транзакций DTAX.") для отключения модуля CICS в регионе CICS командой `DISABLE`.
3. Скопируйте модули CICS из набора данных `SZDTLOAD` в набор данных Dynatrace `DFHRPL`, определённый для вашего региона CICS.
4. Используйте команду CICS `CEMT I PROG(ZDT*)` для отображения модулей CICS. Используйте команду `SET PROG(ZDT*) NEWCOPY`, чтобы сообщить CICS о том, что будет использоваться новая версия каждой программы.
5. Используйте транзакцию DTAX для включения модуля CICS командой `ENABLE`. Убедитесь, что на панели DTAX отображается новая версия модуля CICS.

## Часто задаваемые вопросы

Как проверить, правильно ли установлены модуль CICS и ресурсы?

Имя группы может отличаться, как и двухсимвольный суффикс, представляющий версию CICS модуля (например, для CTS52 используется 69).

Из региона CICS найдите следующие сообщения для проверки определения ресурсов модуля CICS:

```
CICSAPPL Install for group XXXX has completed successfully.


CICSAPPL OWNER CSSY Resource definition for ZDTAGT72 has been added.


CICSAPPL OWNER CSSY Resource definition for ZDTDC2 has been added.


CICSAPPL OWNER CSSY Resource definition for ZDTDC2A has been added.


CICSAPPL OWNER CSSY Resource definition for ZDTPLT has been added.


CICSAPPL OWNER CSSY Resource definition for ZDTPLTSD has been added.


CICSAPPL OWNER CSSY Resource definition for ZDTSOAPH has been added.


CICSAPPL OWNER CSSY TRANSACTION definition entry for DTAX has been added.
```

Как проверить, вызывается ли программа PLT модуля CICS?

Модуль CICS записывает сообщения инициализации в журнал zRemote.

Доступ к журналу zRemote можно получить из Dynatrace так же, как и к другим файлам журналов модулей. Ищите записи журнала, аналогичные следующим:

```
2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] Registering a pgi for the job: HVBAC021, host=10.30.220.41, groupId= f39f4801966aa7c7, pgir.groupInstanceID= fad6dee63cfd1522, hostID= 95c0bb0371704b8c, nodeID= fad6dee63cfd1522, groupName=HVBAC021, hostGroup=, processGroupType= 28


2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] Registered SubAgent[C021,51,32aa8d038887d1c9] with zDC[Z021,52], rc=true


2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021], subagentid[32aa8d038887d1c9] snaId[NETD    .HVBAC021], CICS release 54 was successfully registered with zdc[52] using protocol version=7.2.0, allocator=pooled.


2019-05-09 20:19:13.789 UTC [d37f9842] info    [native] ASID[52], smfID[S0W1], sysid[Z021], jobName[AFVBZ021] - ZDC955I  - Dynatrace connection being processed ZDC-Job/ID:AFVBZ021/Z021.


2019-05-09 20:19:13.790 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021] - ZDTP008I - ZDTP008I ZDTAGT71.


2019-05-09 20:19:13.790 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021] - ZDTP020I - ZDTP020I Active Sensors: MQ DB2 DB2R SOAP CTG DB2Fetch DLI DLIR HTTP .
```

Что делать, если регион CICS не может подключиться к zDC?

Проверьте журнал задания затронутых регионов CICS на наличие следующего сообщения, где `yyyy` — идентификатор подсистемы zDC, к которой пытается подключиться регион CICS. Он может быть пустым, если регион CICS пытается подключиться к подсистеме по умолчанию, настроенной с параметром DEFAULT(YES). Рекомендуем просто выполнить поиск по коду сообщения об ошибке.

```
ZDTP004W zDC yyyy unavailable
```

Убедитесь, что zDC с этим идентификатором подсистемы запущен. Если это так, попробуйте выполнить команду `ENABLE` [транзакции DTAX](../operation/dtax-transaction.md "Управляйте модулем CICS с помощью транзакций DTAX.") для восстановления соединений.

Как обнаружить несовместимость версий?

Убедитесь, что версия модуля CICS меньше или равна версии модуля zRemote. Не подключайте более новые модули CICS к более старым модулям zRemote. Ниже приведён пример сообщения в журнале zRemote, когда версия модуля CICS несовместима с версией zRemote.

```
severe  [native] CICS14CR1[asid = 108] is trying to initialize with an invalid protocol version number : x.xxx.xx
```
