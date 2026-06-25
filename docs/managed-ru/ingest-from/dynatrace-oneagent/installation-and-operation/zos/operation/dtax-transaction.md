---
title: Управление модулем CICS через DTAX-транзакции
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction
scraped: 2026-05-12T12:04:54.968352
---

# Управление модулем CICS через DTAX-транзакции

# Управление модулем CICS через DTAX-транзакции

* Чтение: 4 мин
* Опубликовано 22 июля 2016 г.

Эти функции в первую очередь предназначены для диагностики и устранения неполадок. Ни одна из них не требуется для штатной работы, но можно автоматизировать включение модуля CICS, отправляя транзакции `DTAX ENABLE` и `DTAX DISABLE` через систему автоматизации операций, такую как CAFC, или через команды modify z/OS. Команды modify CICS для DTAX возвращают сообщения в очередь CSMT TD и в системный лог z/OS. Доступна команда modify `DTAX STATUS`, чтобы посмотреть, включены ли Dynatrace CICS HOOKS/EXITS. Эта команда выводит сообщение `ZDTP030I` на консоль z/OS. Полное описание вывода см. в разделе [Сообщения модулей z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages "Сообщения, создаваемые модулями Dynatrace z/OS.").

DTAX-транзакция запускается автоматически каждые 5 минут. В этот момент она инициализирует подключение модуля CICS к только что запущенному или перезапущенному zDC. Поскольку данные собираются только пока zDC активен, он должен быть запущен до инициализации региона CICS или IMS. Кроме того, данные могут теряться до 5 минут после перезапуска zDC или после того, как zDC впервые стартует уже после инициализации региона CICS. Опционально процесс переподключения можно завершить сразу, вручную запустив DTAX-транзакцию и выполнив функцию `DISABLE`, а затем функцию `ENABLE` после повторной инициализации zDC. Используйте только функцию `ENABLE`, если регион CICS не был подключён к zDC и поэтому показывает статус `DISABLED`.

DTAX-транзакция также предоставляет интерфейс для доступа к базовой функциональности модуля CICS. Войдите в CICS и запустите DTAX-транзакцию без параметров, чтобы получить краткое описание её функций и текущий статус модуля.

![Главное меню DTAX](https://dt-cdn.net/images/dtax-panel-dt-3199-cf520f3ba8.png)

Главное меню DTAX

## Изменение уровня логирования

Уровень логирования модуля CICS установлен в **Info** и, в отличие от других модулей, его нельзя изменить из Dynatrace. Однако его можно изменить через DTAX-транзакцию. Установите курсор в правый верхний угол и введите один из следующих уровней логирования: **Severe**, **Warning**, **Info**(по умолчанию) или **Fine**.

## Отправка ping-сообщения

С помощью функции ping-сообщения можно проверить связь между модулем CICS и модулем zRemote.

Выполните DTAX-транзакцию с параметром `PING`.

```
DTAX Ping
```

Убедитесь, что `PING` прошёл по пути CICS → zDC → zRemote и вернулся.

Ping-сообщение генерирует следующий вывод DTAX:

![DTAXPing](https://dt-cdn.net/images/dtaxping-1042-cb46eb515d.png)

DTAXPing

В случае успеха также генерируется запись в логе zRemote, например:

```
info    [native] ASID[53], smfID[S0W1], sysid[C449], jobName[H71AC449] Ping data=asid=53, CFDE33C15E800000
```

## Включение или отключение сбора данных Dynatrace

Эти функции включают или отключают все exits, используемые модулем CICS. Команда `ENABLE` также запускает 5-минутный цикл перезапуска DTAX, если он не был активен. Аналогично команда `DISABLE` завершает любой активный 5-минутный цикл перезапуска DTAX.

### Включение модуля CICS

`DTAX Enable` должен сгенерировать следующий вывод DTAX:

![DTAXEna](https://dt-cdn.net/images/dtaxena-1040-c3d45ff65b.png)

DTAXEna

Enable также должен зарегистрировать это адресное пространство CICS в Dynatrace. Ниже приведены примеры сообщений в логе zRemote после успешного `DTAX Enable`:

```
info    [native] Registering a pgi for the job: HVEAC727[C727], snaId[NETD    .HVEAC727], asid=51, CICS, protocol version=7.3.0, host=xx.xx.xxx.xx, groupId=16db6009dd8ec573, pgir.groupInstanceID=9b720782ca4a076, hostID=ed11bc0b5ee8f53a, nodeID=9b720782ca4a076, groupName=HVEAC727, hostGroup=, processGroupType=28



info    [native] Registered SubAgent[C727,51,6df4c9acf8f61ef5] with zDC[Z727,148], Software Release=54 rc=true
```

### Отключение модуля CICS

`DTAX Disable` должен сгенерировать следующий вывод DTAX:

![DTAXDis](https://dt-cdn.net/images/dtaxdis-1048-2f658f2d3e.png)

DTAXDis

Disable также должен отменить регистрацию этого адресного пространства в Dynatrace. Сообщение из логов zRemote:

```
info    [native] UnregisterSubAgentRunner: starting to unregister 1 subagents
```

### Включение сенсора Language Environment в DTAX

Dynatrace предоставляет сенсор для среды выполнения Language Environment, который формирует события для запросов динамической линковки из программ COBOL и инструкций FETCH из программ PL/I. Сенсор Language Environment трассирует только вызовы программ, скомпонованных в отдельный загрузочный модуль, и не трассирует вызовы программ внутри одного загрузочного модуля. Команда `DTAX LEENAB` включает сенсор Language Environment для захвата этих событий. По умолчанию сенсор Language Environment включён на 5 минут, затем отключается.

Чтобы включить сенсор Language Environment на произвольный интервал, используйте команду `LEENAB=<time>`, где `<time>` задаётся в диапазоне от `1` до `1000` минут.

![DTAXLEE](https://dt-cdn.net/images/leenab-953-df6ab6d3f3.png)

DTAXLEE

Включение сенсора Language Environment может увеличить накладные расходы CPU внутри региона CICS.

### Отключение сенсора Language Environment в DTAX

`DTAX LEDIS` отключает сенсор Dynatrace Language Environment внутри CICS.

## Сообщения DTAX

Описание всех сообщений DTAX см. в разделе [Сообщения модулей z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages "Сообщения, создаваемые модулями Dynatrace z/OS.").