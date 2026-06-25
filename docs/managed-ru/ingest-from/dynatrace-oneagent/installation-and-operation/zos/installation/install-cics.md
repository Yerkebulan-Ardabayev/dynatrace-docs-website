---
title: Установка модуля CICS
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics
scraped: 2026-05-12T11:24:24.044665
---

# Установка модуля CICS

# Установка модуля CICS

* Чтение: 14 мин
* Обновлено 28 января 2026 г.

С модулем CICS вы получаете наблюдаемость транзакций и программ CICS, включая вызовы DB2, DLI и VSAM.

| Наблюдаемость для | Включает |
| --- | --- |
| Транзакции CICS | Транзакции, инициируемые через: * IBM MQ Bridge и Trigger Monitor * CICS Transaction Gateway, HTTP/S, SOAP over HTTP/S, JSON через non-Java JSON pipeline * терминал 3270 |
| Программы CICS | * Программы, вызываемые через CICS LINK * Детали транзакций для запросов DPL LINK и START TRANSACTION в распределённой трассировке |
| Обращения к базам данных | Обращения к базам данных с их SQL-выражениями из CICS в Db2 и IMS DB через метод доступа DL/I |
| Доступ к файлам | [Мониторинг доступа к файлам в приложениях CICS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-cics-file-access "Мониторинг доступа к файлам в приложениях CICS с использованием модуля CICS.") через методы доступа VSAM и BDAM. |

Полная сквозная трассировка транзакций CICS с Dynatrace

Анализируйте производительность транзакций end-to-end с помощью [Service flow](/managed/observe/application-observability/services-classic/service-backtrace "Отслеживайте последовательность вызовов сервисов вплоть до клика в браузере, который инициировал эту цепочку.").

![CICS: поток сервиса](https://dt-cdn.net/images/cics-trace-2357-0a7717e199.png)

CICS: поток сервиса

Используйте [PurePath distributed traces](/managed/observe/application-observability/distributed-traces "Получите наблюдаемость в высоко распределённых облачно-нативных архитектурах для эффективной трассировки и анализа транзакций в реальном времени.") для детализации до уровня кода и оптимизации программ.

![CICS: уровень кода](https://dt-cdn.net/images/cics-code-level-1984-d6aeff52fb.png)

CICS: уровень кода

Анализируйте исключения в контексте транзакций вплоть до уровня базы данных Db2.

![CICS: распределённая трассировка с исключением](https://dt-cdn.net/images/cics-distributed-trace-1986-97b2240549.png)

CICS: распределённая трассировка с исключением

Обнаружение аномалий CICS и изоляция зон сбоев с Dynatrace

Davis® AI автоматически определяет первопричину проблем и оценивает их влияние на пользователей, что позволяет расставлять приоритеты в стратегиях устранения и сокращать среднее время восстановления.

![CICS: автоматическая изоляция зоны сбоя](https://dt-cdn.net/images/cics-problem-1985-100d80f55c.png)

CICS: автоматическая изоляция зоны сбоя

Анализируйте сбои с подробностями исключений в контексте транзакций.

![CICS: анализ сбоев](https://dt-cdn.net/images/cics-exceptions-1985-478b6f8ba6.png)

CICS: анализ сбоев

## Установка

Модуль CICS включает PLT-программу, которая инициализируется при запуске CICS. Эта программа использует хуки для инструментирования CICS-регионов, владеющих терминалами и приложениями, создавая интересующие события. Данные мониторинга передаются в подсистему zDC через общие буферы.

Модуль CICS нужно установить в каждом регионе CICS, который требуется мониторить. Если Dynatrace уже установлен в CICS и нужно обновить модуль CICS без перезапуска региона, см. раздел [Обновление без перезапуска региона](#cics-update).

Необходимо добавить [модуль z/OS Java](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#middleware "Настройка мониторинга Java на z/OS с помощью модуля Java.") к каждому CICS Transaction Gateway, который требуется мониторить.

### Поддержка CTS 6.2

Начиная с OneAgent версии 1.299 обеспечивается поддержка CTS 6.2. Это значительное изменение, соответствующее последним улучшениям безопасности подсистемы CICS.

Поддержка CTS 6.2 требует, чтобы загрузочный модуль `DFHBPZDT`, поставляемый в `SZDTAUTH`, был доступен при запуске региона CICS.
Рекомендуемая процедура установки:

Добавьте строку, аналогичную приведённому ниже примеру, в элемент parmlib PROGxx. Обратите внимание, что `SZDTAUTH` должен иметь APF-авторизацию.

```
LPA ADD MODNAME(DFHBPZDT) DSNAME(<hlq>.SZDTAUTH)
```

Чтобы немедленно добавить модуль в LPA, введите консольную команду, аналогичную приведённому ниже примеру.

```
SETPROG LPA,ADD,MODNAME=DFHBPZDT,DSNAME=<hlq>.SZDTAUTH
```

Также возможно добавить `DFHBPZDT` в `STEPLIB` регионов CICS 6.2, в которых установлен агент Dynatrace.
Тем не менее добавлять весь `SZDTAUTH` в CICS STEPLIB не рекомендуется.

Для проверки установки CTS 6.2 выводит следующее сообщение:

```
DFHKE0010  HVPAC449 Vendor table DFHBPZDT for product ID ZDT has been loaded
```

### Определение библиотеки CICS

Загрузочную библиотеку можно динамически добавить как определение библиотеки CICS в CSD. Определение CEDA находится в элементе `CICRDO` набора данных `SZDTSAMP`. Пример приведён в следующем разделе.

Если использовать определение библиотеки CICS не нужно, добавьте следующий PDS (или его содержимое) в конкатенацию DFHRPL:

```
// DD DISP=SHR,DSN=<hlq>.SZDTLOAD
```

Независимо от выбранного варианта необходимо скорректировать DSN, заменив `<hlq>` высококвалифицированным квалификатором, заданным при выполнении процедуры [Загрузка наборов данных продукта z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets "Загрузите и установите наборы данных продукта Dynatrace для z/OS.").

### Программы и транзакция CICS Dynatrace

Определения ресурсов CICS для модуля CICS Dynatrace находятся в элементе `CICRDO` набора данных `SZDTSAMP`, предназначенном для использования с пакетной служебной программой `RDO` `DFHCSDUP`.

Рекомендуется использовать приведённые имена транзакций и групп, однако их можно изменить в соответствии с политиками вашей инсталляции. Согласуйте имя группы и имя списка групп с администратором CICS. Замените `XYZLIST` именем вашего списка групп (`GRPLIST`).

Рекомендуется использовать идентификатор транзакции по умолчанию `DTAX` для `ZDTPLT`, однако при наличии конфликтующих определений транзакций можно указать пользовательский идентификатор вместо `DTAX`.

### Таблица списка программ запуска CICS

Добавьте программу запуска CICS (`ZDTPLT`) после записи `DFHDELIM` в исходном коде PLTPI и соберите таблицу.

Этот шаг необязателен для тестовых инсталляций, так как для активации модуля после инициализации CICS можно воспользоваться [DTAX-транзакцией](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Управление модулем CICS через DTAX-транзакции."). Рекомендуется размещать запись `ZDTPLT` непосредственно перед спецификацией `TYPE=FINAL`.

Для формирования таблицы PLTPI можно использовать JCL-процедуру `DFHAUPLE` из `CICSHLQ.SDFHINST(DFHAUPLE)`.

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

Пользователи Compuware Xpediter Global Storage Protection

PLT-программа запуска (`ZDTPLT`) инициализирует рабочую область выхода модуля CICS, которую CICS получает от его имени. Такие продукты, как Compuware Xpediter/CICS, могут быть настроены на применение строгого контроля доступа к памяти и вызывать аварийное завершение `ZDTPLT`, препятствуя запуску модуля CICS, если он не исключён из этих ограничений. При использовании функции глобальной защиты памяти Xpediter/CICS добавьте запись `monitor exceptions` в DD XDDBPINP JCL региона CICS для исключения `ZDTPLT*`. Например:

```
DBPA 17.02 TRAN=*,PROGRAM=ZDTPLT*,CSECT=*
```

### Таблица списка программ завершения CICS

Добавьте программу завершения CICS (`ZDTPLTSD`) перед записью `DFHDELIM` в исходном коде PLTSD и соберите таблицу.

Рекомендуется размещать запись `ZDTPLTSD` непосредственно после спецификации `TYPE=INITIAL`.

Для формирования таблицы PLTSD можно использовать JCL-процедуру `DFHAUPLE` из `CICSHLQ.SDFHINST(DFHAUPLE)`.

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

PLT-программа запуска (`ZDTPLT`) автоматически подключается к подсистеме zDC по умолчанию при инициализации региона CICS.

При работе нескольких подсистем zDC подключение выполняется к той, для которой задан параметр `DEFAULT(YES)`, если только параметр переопределения `INITPARM` в параметрах CICS SYSIN не указывает на подключение к zDC с конкретным именем:

```
INITPARM=(ZDTPLT='MEPC,<option>'),
```

`<option>` задаёт уровень журналирования для модуля CICS; см. раздел [Журналирование](#logging).

Для проверки связи между модулем CICS и подсистемой zDC [отправьте ping-сообщение](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction#ping "Управление модулем CICS через DTAX-транзакции.").

## Настройка

### Группировка регионов по имени CICSPlex

Регионы CICS, принадлежащие одному CICSPlex, можно объединить в одну группу процессов. Для этого:

1. Перейдите в **Settings** > **Mainframe** > **Transaction monitoring**.
2. Включите **Group CICS regions that belong to the same CICSPlex**.
3. Добавьте `MASPLTWAIT(YES)` в параметр LMAS. Это указывает региону CICS ожидать доступности CICSPlex перед продолжением работы. Если CICSPlex недоступен, модуль не сможет его учесть.
4. Необязательно. Интервал ожидания `MASINITTIME(10)` по умолчанию составляет 10 минут. Его можно настроить в диапазоне от 5 до 59 минут.

Если группировка по имени CICSPlex была включена **после** запуска региона CICS, необходимо выполнить [DTAX-транзакцию](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Управление модулем CICS через DTAX-транзакции.") `DTAX DISABLE` и `DTAX ENABLE`.

### Поддержка веб-сервисов CICS

Модуль CICS позволяет трассировать веб-сервисы CICS, вызываемые через SOAP-запрос или JSON-запрос (non-Java JSON pipeline). Для трассировки JSON-запросов требуется OneAgent версии 1.257 или новее.

Для трассировки программ провайдера веб-сервисов CICS, вызываемых программами-обработчиками из CICS SOAP pipelines или CICS non-Java JSON pipelines, обновите файл конфигурации провайдера (`.xml`), добавив `ZDTSOAPH`, как показано ниже.

Dynatrace поддерживает только конвейеры со стандартным обработчиком терминала. При использовании нестандартного обработчика его инструментирование возможно через CICS and IMS SDK. В качестве отправной точки можно воспользоваться следующими примерами кода:

* [ADKJSONA](https://assets.dynatrace.com/global/doc/appmon/integrations-and-extensions/development-kits/agent-development-kit-adk/cics-and-ims-adk/adkjsona.txt): пример на ассемблере CICS стартовых путей для JSON-запросов в пользовательском apphandler.
* [ADKJSONC](https://assets.dynatrace.com/global/doc/appmon/integrations-and-extensions/development-kits/agent-development-kit-adk/cics-and-ims-adk/adkjsonc.txt): пример на CICS COBOL стартовых путей для JSON-запросов в пользовательском apphandler.

#### CICS SOAP pipeline

`DFHPITP`: программа-обработчик приложений, используемая в конфигурации CICS SOAP pipeline для вызова программ провайдера сервиса. Помимо `DFHPITP` в конвейере, кодовый модуль CICS также поддерживает пользовательские программы обработчика терминала.

Обновите файл конфигурации конвейера, добавив `ZDTSOAPH` в секцию `<headerprogram>` под элементом обработчика SOAP. Все SOAP-конвейеры содержат элемент обработчика SOAP `<cics_soap_1.1_handler>` или `<cics_soap_1.2_handler>`, в который добавляется `ZDTSOAPH`. Ниже приведён пример CICS SOAP provider pipeline с добавленным `ZDTSOAPH`.

Для трассировки исходящих SOAP-запросов, возникающих в рамках CICS-транзакций, отслеживаемых модулем CICS, добавьте секцию `<headerprogram>` в определения конвейера запрашивающей стороны для тех SOAP-сервисов, которые нужно трассировать. Исходящие SOAP-запросы, возникающие в рамках не отслеживаемых CICS-транзакций, игнорируются. При этом трассировка не ограничена запросами от SOAP-программ, выступающих провайдерами сервиса CICS SOAP.

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

#### CICS non-Java JSON pipeline (OneAgent версии 1.257 и новее)

`DFHPIJT`: программа-обработчик терминала, используемая в CICS non-Java JSON pipeline для вызова программ провайдера сервиса. Для трассировки провайдера веб-сервиса CICS, вызываемого через non-Java JSON pipeline, обновите файл конфигурации конвейера, добавив `ZDTSOAPH` в секцию `<handler>` под XML-тегами `<default_http_transport_handler_list>`. Ниже приведён пример CICS non-Java JSON provider pipeline с добавленным `ZDTSOAPH`.

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

### Маршрутизация сообщений DTAX через TDQueue

Необязательно. Для маршрутизации сообщений DTAX в TDQueue Dynatrace (Transient Data Queue) используйте определение ресурса `ZDTQ`, приведённое выше в элементе `CICRDO`.

Сообщения DTAX записываются в TDQueue ZDTQ только при открытой очереди. При использовании предоставленного определения ресурса очередь остаётся закрытой из-за атрибута `OPENTIME(DEFERRED)`. Открыть её вручную можно командой `CEMT INQUIRE|SET TDQUEUE`, либо настроить открытие при инициализации, изменив определение TDQUEUE для ZDTQ на атрибут `OPENTIME(INITIAL)`.

## Журналирование

Уровень журналирования модуля CICS можно задавать с помощью [DTAX-транзакции](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Управление модулем CICS через DTAX-транзакции.") или необязательного параметра `INITPARM` при запуске региона CICS.

```
INITPARM=(ZDTPLT='MEPC,<Option>'),
```

`<Option>` задаёт уровень журналирования для модуля CICS. Допустимые значения:

1. `FINE` | `F`: детальное журналирование. Рекомендуется включать только при проблемах с запуском модуля CICS.
2. `INFO` | `I`: информационное журналирование. Значение по умолчанию.
3. `WARNING` | `W`: журналирование предупреждений.
4. `SEVERE` | `S`: журналирование сообщений об ошибках.

```
Example:



INITPARM=(ZDTPLT='MEPC,SEVERE'),
```

Существует два набора логов CICS:

* Один набор сообщений формируется при выполнении [DTAX-транзакцией](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Управление модулем CICS через DTAX-транзакции.") команд `DISABLE` и `ENABLE`. Эти сообщения записываются в CICS CSMT Transient Data Queue (обычно в MSGUSR). Просматривайте их в спуле задания CICS. DTAX также записывает набор сообщений в оператор CEEOUT SYSOUT при возникновении ошибок соединения между zDC и DTAX-транзакцией. Просматривайте эти сообщения в спуле задания CICS. Пока DTAX-транзакция может подключаться к zDC, она журналирует свои сообщения в zRemote.
* Мониторинговая транзакционная активность модуля CICS направляет свои сообщения журнала в zDC, а затем в zRemote. Лог отражает наличие повреждённых распределённых трассировок, таймаутов и других ошибок. В этих логах также могут присутствовать статистические сведения.

Доступ к логам CICS можно получить через [логи zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#logging "Подготовка и установка модуля zRemote для мониторинга z/OS.").

## Обновление без перезапуска региона

Для обновления модуля CICS до новой версии без перезапуска региона:

1. [Загрузите наборы данных продукта z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#download-pax "Загрузите и установите наборы данных продукта Dynatrace для z/OS.") и [распакуйте их](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#extract-datasets "Загрузите и установите наборы данных продукта Dynatrace для z/OS.").
2. С помощью [DTAX-транзакции](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Управление модулем CICS через DTAX-транзакции.") отключите модуль CICS в регионе CICS командой `DISABLE`.
3. Скопируйте модули CICS из набора данных `SZDTLOAD` в набор данных Dynatrace `DFHRPL`, определённый для вашего региона CICS.
4. Используйте команду CICS `CEMT I PROG(ZDT*)` для отображения модулей CICS. Выполните команду `SET PROG(ZDT*) NEWCOPY`, чтобы указать CICS на использование новой версии каждой программы.
5. С помощью DTAX-транзакции включите модуль CICS командой `ENABLE`. Убедитесь, что на панели DTAX отображается новая версия модуля CICS.

## Вопросы и ответы

Как проверить правильность установки модуля CICS и его ресурсов?

Имя группы может отличаться, как и двухсимвольный суффикс, обозначающий релиз CICS модуля (например, CTS52 использует 69).

В регионе CICS найдите приведённые ниже сообщения для подтверждения определения ресурсов модуля CICS:

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

Как проверить, вызывается ли PLT-программа модуля CICS?

Модуль CICS записывает сообщения инициализации в лог zRemote.

Лог zRemote доступен из Dynatrace так же, как и все остальные файлы логов модулей. Найдите записи лога, аналогичные следующим:

```
2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] Registering a pgi for the job: HVBAC021, host=10.30.220.41, groupId= f39f4801966aa7c7, pgir.groupInstanceID= fad6dee63cfd1522, hostID= 95c0bb0371704b8c, nodeID= fad6dee63cfd1522, groupName=HVBAC021, hostGroup=, processGroupType= 28



2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] Registered SubAgent[C021,51,32aa8d038887d1c9] with zDC[Z021,52], rc=true



2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021], subagentid[32aa8d038887d1c9] snaId[NETD    .HVBAC021], CICS release 54 was successfully registered with zdc[52] using protocol version=7.2.0, allocator=pooled.



2019-05-09 20:19:13.789 UTC [d37f9842] info    [native] ASID[52], smfID[S0W1], sysid[Z021], jobName[AFVBZ021] - ZDC955I  - Dynatrace connection being processed ZDC-Job/ID:AFVBZ021/Z021.



2019-05-09 20:19:13.790 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021] - ZDTP008I - ZDTP008I ZDTAGT71.



2019-05-09 20:19:13.790 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021] - ZDTP020I - ZDTP020I Active Sensors: MQ DB2 DB2R SOAP CTG DB2Fetch DLI DLIR HTTP .
```

Что делать, если регион CICS не может подключиться к zDC?

Проверьте лог задания затронутых регионов CICS на наличие следующего сообщения (`yyyy` здесь означает идентификатор подсистемы zDC, к которой подключается регион; значение может быть пустым, если регион подключается к подсистеме по умолчанию с параметром DEFAULT(YES)). Рекомендуется просто выполнить поиск по коду сообщения об ошибке.

```
ZDTP004W zDC yyyy unavailable
```

Убедитесь, что zDC с данным идентификатором подсистемы запущен. Если это так, попробуйте выполнить команду `ENABLE` [DTAX-транзакции](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Управление модулем CICS через DTAX-транзакции.") для повторного включения соединений.

Как обнаружить несовместимость версий?

Версия модуля CICS должна быть меньше или равна версии модуля zRemote. Не подключайте более новые модули CICS к более старым модулям zRemote. Ниже приведён пример сообщения в логе zRemote при несовместимости версий модуля CICS и модуля zRemote.

```
severe  [native] CICS14CR1[asid = 108] is trying to initialize with an invalid protocol version number : x.xxx.xx
```