# -*- coding: utf-8 -*-
"""Builder for dtax-messages.md  (L4-IF.71 batch)."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_messages, qa_one

REL = "ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages"
FN = "dtax-messages.md"

# ---------------------------------------------------------------------------
# PROSE: EN value of Explanation / System action / User response -> RU
# (без ведущего "* **Label** - "; ключ — EN, значение — RU без отступа)
# ---------------------------------------------------------------------------
PROSE = {
    # ── ZDTP001S ──────────────────────────────────────────────────────────
    "The CICS PLT program was unable to allocate a required persistent storage area.": "Программа CICS PLT не смогла выделить необходимую область постоянной памяти.",
    "The PLT program terminates and the CICS code module is not enabled.": "Программа PLT завершается, и кодовый модуль CICS не включается.",
    "Determine why the CICS region is unable to provide storage for the DTAX transaction.": "Выясните, по какой причине регион CICS не может предоставить память для транзакции DTAX.",
    # ── ZDTP001S / ZDTP003S / ZDTP023S … (continuation – META) ───────────
    # Continuation абзацы идут через META (не буллет), см. ниже.
    # ── ZDTP002S ──────────────────────────────────────────────────────────
    "The PLT program was unable to allocate a required Message block storage area.": "Программа PLT не смогла выделить необходимую область памяти для блока сообщений.",
    "The PLT program terminates and the CICS code module is disabled.": "Программа PLT завершается, а кодовый модуль CICS отключается.",
    "Determine why the CICS region is unable to provide storage for the PLT program.": "Выясните, по какой причине регион CICS не может предоставить память для программы PLT.",
    # ── ZDTP003S ──────────────────────────────────────────────────────────
    "CICS could not load `ZDTSOAPH`.": "CICS не смог загрузить `ZDTSOAPH`.",
    # System action same as ZDTP002S (PLT terminates / disabled) – уже выше
    "Determine why the CICS region is unable to load one of the DTAX modules - ZDTSOAPH.": "Выясните, по какой причине регион CICS не может загрузить один из модулей DTAX: ZDTSOAPH.",
    # ── ZDTP004S ──────────────────────────────────────────────────────────
    "Message transfer from CICS code module to zDC has failed.": "Передача сообщения от кодового модуля CICS к zDC завершилась ошибкой.",
    "CICS code module operation continues but with missing nodes in the distributed trace.": "Кодовый модуль CICS продолжает работу, однако в распределённой трассировке отсутствуют некоторые узлы.",
    "Please contact a Dynatrace product expert via live chat within your environment.": "Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP005S ──────────────────────────────────────────────────────────
    "The `EXEC CICS START` command used to initiate the `DTAX ICE` transaction in 5 minutes interval has failed.": "Команда `EXEC CICS START`, используемая для запуска транзакции `DTAX ICE` с интервалом 5 минут, завершилась ошибкой.",
    "None": "Нет",
    "Examine the more detailed message in the appropriate CICS job log to look at the precise EIBRESP code that indicates why this EXEC CICS START command failed.": "Изучите подробное сообщение в соответствующем журнале задания CICS, чтобы получить точный код EIBRESP, указывающий причину сбоя команды EXEC CICS START.",
    # ── ZDTP006S ──────────────────────────────────────────────────────────
    "`EXEC CICS INQUIRE` for MQ Connection information has failed.": "Команда `EXEC CICS INQUIRE` для получения информации о подключении MQ завершилась ошибкой.",
    "Missing MQ Queue manager name in CICS attachment details.": "В сведениях о подключении CICS отсутствует имя диспетчера очередей MQ.",
    "With the help of `resp` and `resp2` codes, determine why INQUIRE MQCONN failed.": "С помощью кодов `resp` и `resp2` выясните причину сбоя INQUIRE MQCONN.",
    # ── ZDTP007S ──────────────────────────────────────────────────────────
    "Indicates that the Language Environment sensor could not be enabled because zDC is unavailable.": "Указывает, что датчик Language Environment не удалось включить из-за недоступности zDC.",
    "Language Environment sensor is not enabled. CICS code module doesn't monitor LE dynamic calls.": "Датчик Language Environment не включён. Кодовый модуль CICS не отслеживает динамические вызовы LE.",
    "Start the zDC for CICS code module to reconnect.": "Запустите zDC, чтобы кодовый модуль CICS мог восстановить соединение.",
    # ── ZDTP008S ──────────────────────────────────────────────────────────
    "Storage allocation for PLT work area failed.": "Выделение памяти для рабочей области PLT завершилось ошибкой.",
    # System action + User response same as ZDTP002S – уже выше
    # ── ZDTP009S ──────────────────────────────────────────────────────────
    "Persistent storage for PLT program is not found.": "Постоянная память для программы PLT не найдена.",
    # System action same as ZDTP002S – уже выше
    # ── ZDTP010S ──────────────────────────────────────────────────────────
    "RMI hook initialization failed.": "Инициализация хука RMI завершилась ошибкой.",
    "CICS code module not initialized successfully.": "Кодовый модуль CICS не был успешно инициализирован.",
    # ── ZDTP011S ──────────────────────────────────────────────────────────
    "Disabling RMI hook failed.": "Отключение хука RMI завершилось ошибкой.",
    "CICS code module not disabled successfully.": "Кодовый модуль CICS не был успешно отключён.",
    # ── ZDTP012S ──────────────────────────────────────────────────────────
    "Global work area storage for PLT program is unavailable.": "Память глобальной рабочей области для программы PLT недоступна.",
    "Hooks don't initialize successfully.": "Хуки не инициализируются успешно.",
    # ── ZDTP013S ──────────────────────────────────────────────────────────
    "SOAP hook enable/disable has failed.": "Включение/отключение хука SOAP завершилось ошибкой.",
    "Hook operation fails.": "Операция с хуком завершается ошибкой.",
    # ── ZDTP014S ──────────────────────────────────────────────────────────
    "Language Environment sensor enable/disable has failed.": "Включение/отключение датчика Language Environment завершилось ошибкой.",
    # System action: Hook operation fails. – уже выше
    # ── ZDTP015S ──────────────────────────────────────────────────────────
    "MRO hook enable/disable has failed.": "Включение/отключение хука MRO завершилось ошибкой.",
    # System action: Hook operation fails. – уже выше
    # ── ZDTP016S ──────────────────────────────────────────────────────────
    "Hook operation has failed.": "Операция с хуком завершилась ошибкой.",
    "CICS code module don't initialize successfully.": "Кодовый модуль CICS не инициализируется успешно.",
    # ── ZDTP018S ──────────────────────────────────────────────────────────
    "Storage allocation for config block has failed.": "Выделение памяти для блока конфигурации завершилось ошибкой.",
    "CICS code module doesn't initialize successfully.": "Кодовый модуль CICS не инициализируется успешно.",
    "Determine why the CICS region is unable to provide storage for the DTAX transaction.": "Выясните, по какой причине регион CICS не может предоставить память для транзакции DTAX.",
    # ── ZDTP019S ──────────────────────────────────────────────────────────
    "Storage allocation for message buffer has failed.": "Выделение памяти для буфера сообщений завершилось ошибкой.",
    # System + User response same as ZDTP018S – уже выше
    # ── ZDTP020S ──────────────────────────────────────────────────────────
    "`EXEC CICS ASSIGN` for APPLID retrieval has failed.": "Команда `EXEC CICS ASSIGN` для получения APPLID завершилась ошибкой.",
    "CICS Applid is not displayed in DTAX screen and in log messages.": "CICS Applid не отображается на экране DTAX и в сообщениях журнала.",
    "Determine the cause of the problem from `resp` and `resp2` codes.": "Выясните причину неполадки с помощью кодов `resp` и `resp2`.",
    # ── ZDTP021S ──────────────────────────────────────────────────────────
    "`EXEC CICS ASSIGN` for program start code retrieval has failed.": "Команда `EXEC CICS ASSIGN` для получения кода запуска программы завершилась ошибкой.",
    # System action: CICS code module doesn't initialize successfully. – уже выше
    # ── ZDTP022S ──────────────────────────────────────────────────────────
    "`EXEC CICS DELAY` has failed.": "Команда `EXEC CICS DELAY` завершилась ошибкой.",
    "None": "Нет",
    # ── ZDTP023S ──────────────────────────────────────────────────────────
    "`EXEC CICS INQUIRE DB2ENTRY` has failed.": "Команда `EXEC CICS INQUIRE DB2ENTRY` завершилась ошибкой.",
    "CICS code module operation continues.": "Кодовый модуль CICS продолжает работу.",
    # ── ZDTP024S ──────────────────────────────────────────────────────────
    "CICS code module didn't get a valid AgentId after initialization.": "Кодовый модуль CICS не получил допустимый AgentId после инициализации.",
    "CICS code module is disabled.": "Кодовый модуль CICS отключён.",
    "Check for error messages in zRemote log. If the zRemote service is not running, start it.": "Проверьте наличие сообщений об ошибках в журнале zRemote. Если служба zRemote не запущена, запустите её.",
    # ── ZDTP025S ──────────────────────────────────────────────────────────
    "`EXEC CICS INQUIRE SYSTEM` for CICS version retrieval has failed.": "Команда `EXEC CICS INQUIRE SYSTEM` для получения версии CICS завершилась ошибкой.",
    "By default CICS code module for CICS Version 4.2 is loaded.": "По умолчанию загружается кодовый модуль CICS для CICS версии 4.2.",
    # ── ZDTP026S ──────────────────────────────────────────────────────────
    "`EXEC CICS INQUIRE PROGRAM` has failed.": "Команда `EXEC CICS INQUIRE PROGRAM` завершилась ошибкой.",
    # System action: CICS code module operation continues. – уже выше
    # ── ZDTP027S ──────────────────────────────────────────────────────────
    "`EXEC CICS DISABLE PROGRAM` for all exits has failed.": "Команда `EXEC CICS DISABLE PROGRAM` для всех точек выхода завершилась ошибкой.",
    "CICS code module is not disabled successfully.": "Кодовый модуль CICS не был успешно отключён.",
    # ── ZDTP028S ──────────────────────────────────────────────────────────
    "`EXEC CICS DISABLE PROGRAM` for RMI exit has failed.": "Команда `EXEC CICS DISABLE PROGRAM` для точки выхода RMI завершилась ошибкой.",
    "RMI exit is not disabled successfully.": "Точка выхода RMI не была успешно отключена.",
    # ── ZDTP029S ──────────────────────────────────────────────────────────
    "`EXEC CICS ENABLE START` for `XPCREQC/XRMIIN/XRMIOUT` exit has failed.": "Команда `EXEC CICS ENABLE START` для точек выхода `XPCREQC/XRMIIN/XRMIOUT` завершилась ошибкой.",
    "Exits are not started successfully.": "Точки выхода не были успешно запущены.",
    # ── ZDTP030S ──────────────────────────────────────────────────────────
    "`EXEC CICS FREEMAIN` has failed.": "Команда `EXEC CICS FREEMAIN` завершилась ошибкой.",
    "Global Work Area for PLT program FREEMAIN fails.": "Выполнение FREEMAIN для глобальной рабочей области программы PLT завершается ошибкой.",
    # ── ZDTP031S ──────────────────────────────────────────────────────────
    "`EXEC CICS ENABLE PROGRAM` for enabling exits failed.": "Команда `EXEC CICS ENABLE PROGRAM` для включения точек выхода завершилась ошибкой.",
    "CICS code module exits are not enabled successfully.": "Точки выхода кодового модуля CICS не были успешно включены.",
    # ── ZDTP032S ──────────────────────────────────────────────────────────
    "`EXEC CICS DISABLE` stop for exits failed.": "Остановка точек выхода через `EXEC CICS DISABLE` завершилась ошибкой.",
    "CICS code module exits are not stopped successfully.": "Точки выхода кодового модуля CICS не были успешно остановлены.",
    # ── ZDTP033S ──────────────────────────────────────────────────────────
    "`EXEC CICS CANCEL REQID` has failed.": "Команда `EXEC CICS CANCEL REQID` завершилась ошибкой.",
    "`DTAX ICE` transaction is not cancelled.": "Транзакция `DTAX ICE` не отменена.",
    # ── ZDTP034S ──────────────────────────────────────────────────────────
    "`EXEC CICS INQUIRE REQID` has failed.": "Команда `EXEC CICS INQUIRE REQID` завершилась ошибкой.",
    "`DTAX ICE` transaction is not started successfully.": "Транзакция `DTAX ICE` не была успешно запущена.",
    # ── ZDTP035S ──────────────────────────────────────────────────────────
    "`EXEC CICS GETMAIN` for Global Work Area has failed.": "Команда `EXEC CICS GETMAIN` для глобальной рабочей области завершилась ошибкой.",
    "Global Work Area for PLT program is not allocated. CICS code module doesn't initialize successfully.": "Глобальная рабочая область для программы PLT не выделена. Кодовый модуль CICS не инициализируется успешно.",
    # ── ZDTP036S ──────────────────────────────────────────────────────────
    "`EXEC CICS START` has failed.": "Команда `EXEC CICS START` завершилась ошибкой.",
    "DTAX Interval control transaction is not started every 5 minutes.": "Транзакция управления интервалом DTAX не запускается каждые 5 минут.",
    # ── ZDTP037S ──────────────────────────────────────────────────────────
    "`EXEC CICS LOAD PROGRAM` for `ZDTAGTxx` module has failed.": "Команда `EXEC CICS LOAD PROGRAM` для модуля `ZDTAGTxx` завершилась ошибкой.",
    "`ZDTAGTxx` PTF and build date is not printed in the log messages.": "PTF и дата сборки `ZDTAGTxx` не выводятся в сообщениях журнала.",
    # ── ZDTP038S ──────────────────────────────────────────────────────────
    "`EXEC CICS LOAD PROGRAM` for `ZDTSOAPH` module has failed.": "Команда `EXEC CICS LOAD PROGRAM` для модуля `ZDTSOAPH` завершилась ошибкой.",
    "`ZDTSOAPH` build date and version information are not printed in the log messages.": "Дата сборки и версия `ZDTSOAPH` не выводятся в сообщениях журнала.",
    # ── ZDTP039S ──────────────────────────────────────────────────────────
    "`EXEC CICS RELEASE PROGRAM` for `ZDTAGTxx/ZDTSOAPH` module has failed.": "Команда `EXEC CICS RELEASE PROGRAM` для модуля `ZDTAGTxx/ZDTSOAPH` завершилась ошибкой.",
    # System action: CICS code module operation continues. – уже выше
    # ── ZDTP040S ──────────────────────────────────────────────────────────
    "`EXEC CICS RECEIVE DATA` has failed.": "Команда `EXEC CICS RECEIVE DATA` завершилась ошибкой.",
    "User command for `DTAX` transaction is not received and hence is not processed successfully.": "Команда пользователя для транзакции `DTAX` не получена и поэтому не обработана.",
    # ── ZDTP041S ──────────────────────────────────────────────────────────
    "Error retrieving zOS SMFid.": "Ошибка при получении SMFid для z/OS.",
    "CICS code module doesn't initialize.": "Кодовый модуль CICS не инициализируется.",
    # ── ZDTP042S ──────────────────────────────────────────────────────────
    "CICS code module initialization has failed.": "Инициализация кодового модуля CICS завершилась ошибкой.",
    # System action: CICS code module doesn't initialize. – уже выше
    # ── ZDTP043S ──────────────────────────────────────────────────────────
    "`EXEC CICS INQUIRE DB2CONN` retreives an `AUTHTYPE` that is not one of `GROUP, TERM, TX, OPID, USERID`.": "Команда `EXEC CICS INQUIRE DB2CONN` возвращает `AUTHTYPE`, не являющийся одним из значений `GROUP, TERM, TX, OPID, USERID`.",
    "Authtype not specified in DB2 attachment data in distributed trace.": "Тип авторизации не указан в данных о подключении Db2 в распределённой трассировке.",
    "Contact your Db2 administrator.": "Обратитесь к администратору Db2.",
    # ── ZDTP044S ──────────────────────────────────────────────────────────
    "Sending Db2 connection pool information from CICS code module to zDC has failed.": "Передача сведений о пуле соединений Db2 от кодового модуля CICS к zDC завершилась ошибкой.",
    "Db2 attachment details in distributed trace is empty.": "Сведения о подключении Db2 в распределённой трассировке пусты.",
    # ── ZDTP045S ──────────────────────────────────────────────────────────
    "Sending DL1 connection pool information from CICS code module to zDC has failed.": "Передача сведений о пуле соединений DL1 от кодового модуля CICS к zDC завершилась ошибкой.",
    "DLI attachment details in distributed trace is empty.": "Сведения о подключении DLI в распределённой трассировке пусты.",
    # ── ZDTP046S ──────────────────────────────────────────────────────────
    "CICS code module could not send message to zDC.": "Кодовый модуль CICS не смог отправить сообщение в zDC.",
    "No data passes from CICS to zDC.": "Данные от CICS в zDC не передаются.",
    # ── ZDTP047S ──────────────────────────────────────────────────────────
    "The RDO definition for DTAX transaction is not found.": "Определение RDO для транзакции DTAX не найдено.",
    "CICS code module not enabled and the PLT program execution terminates.": "Кодовый модуль CICS не включён, а выполнение программы PLT завершается.",
    "Define DTAX transaction for the PLT program. Refer to CICRDO member in SZDTSAMP installation library for sample definition.": "Определите транзакцию DTAX для программы PLT. Образец определения см. в элементе CICRDO библиотеки установки SZDTSAMP.",
    # ── ZDTP048S ──────────────────────────────────────────────────────────
    "CICS code module could not find the configuration data with sensor settings.": "Кодовый модуль CICS не смог найти данные конфигурации с параметрами датчиков.",
    # System action: CICS code module doesn't initialize. – уже выше
    # ── ZDTP049S ──────────────────────────────────────────────────────────
    "CICS code module could not find the config block with CICS sensor settings.": "Кодовый модуль CICS не смог найти блок конфигурации с параметрами датчиков CICS.",
    # System action: CICS code module is disabled. – уже выше
    "Check if the CICS Transaction Server sensor is placed in the CICS code module Mapping.": "Убедитесь, что датчик CICS Transaction Server размещён в сопоставлении кодового модуля CICS.",
    # ── ZDTP050S ──────────────────────────────────────────────────────────
    "Couldn't enable CICS code module.": "Не удалось включить кодовый модуль CICS.",
    # System action: CICS code module doesn't initialize successfully. – уже выше
    # ── ZDTP051S ──────────────────────────────────────────────────────────
    "Could not find the Copyright block in ZDTAGTxx module.": "Блок авторских прав в модуле ZDTAGTxx не найден.",
    "CICS code module continues. No PTF/Build date is printed in the zRemote log.": "Кодовый модуль CICS продолжает работу. Данные о PTF и дате сборки в журнал zRemote не выводятся.",
    # ── ZDTP052S ──────────────────────────────────────────────────────────
    "Configuration block with the CICS sensor information is not found.": "Блок конфигурации со сведениями о датчиках CICS не найден.",
    # System action: CICS code module is disabled. – уже выше
    "Check if the CICS transaction server sensor is placed in the CICS code module mapping.": "Убедитесь, что датчик CICS transaction server размещён в сопоставлении кодового модуля CICS.",
    # ── ZDTP053S ──────────────────────────────────────────────────────────
    "This message is an extension of `ZDTP052S`.": "Это сообщение является продолжением `ZDTP052S`.",
    # System action: CICS code module is disabled. – уже выше
    "Follow `ZDTP052S`.": "Следуйте инструкциям сообщения `ZDTP052S`.",
    # ── ZDTP054S ──────────────────────────────────────────────────────────
    "Couldn't enable Trace hook.": "Не удалось включить хук трассировки.",
    "Trace hook is not installed.": "Хук трассировки не установлен.",
    "Look in CICS log for problems. If you don't find anything, please contact a Dynatrace product expert via live chat within your Dynatrace environment.": "Проверьте журнал CICS на наличие ошибок. Если проблем не обнаружено, обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении Dynatrace.",
    # ── ZDTP055S ──────────────────────────────────────────────────────────
    "Couldn't disable trace hook.": "Не удалось отключить хук трассировки.",
    # System action: Trace hook is not installed. – уже выше
    # User response: Look in CICS log... – уже выше
    # ── ZDTP056S ──────────────────────────────────────────────────────────
    "Bad address for DSA storage": "Недопустимый адрес для памяти DSA.",
    "Dynatrace hooks are not enabled.": "Хуки Dynatrace не включены.",
    "CICS getmain failed. Check CICS logs and correct problem.": "Выполнение CICS GETMAIN завершилось ошибкой. Проверьте журналы CICS и устраните неполадку.",
    # ── ZDTP057S ──────────────────────────────────────────────────────────
    "Storage allocation for DSA area has failed.": "Выделение памяти для области DSA завершилось ошибкой.",
    # System action: Dynatrace hooks are not enabled. – уже выше
    "Check CICS log and correct the problem.": "Проверьте журнал CICS и устраните неполадку.",
    # ── ZDTP058S ──────────────────────────────────────────────────────────
    "Bad address for DSA storage free": "Недопустимый адрес при освобождении памяти DSA.",
    "No attempt to free main storage.": "Попытка освободить основную память не предпринимается.",
    "This is usually not a problem as Dynatrace code module usually just didn't get any storage for this configuration.": "Как правило, это не является проблемой: кодовый модуль Dynatrace просто не получил память для данной конфигурации.",
    # ── ZDTP059S ──────────────────────────────────────────────────────────
    "Bad address for DSA storage free from CICS chain.": "Недопустимый адрес при освобождении памяти DSA из цепочки CICS.",
    # System action: No attempt to free main storage. – уже выше
    "The storage chain is broken or corrupt.": "Цепочка памяти повреждена или нарушена.",
    # ── ZDTP060S ──────────────────────────────────────────────────────────
    "DTAX time value was not in the range from 1 to 5.": "Значение времени DTAX находилось вне диапазона от 1 до 5.",
    "The value is reset to 5.": "Значение сбрасывается на 5.",
    "If you are changing ICE values in the DTAX transaction make sure it is value from 1 to 5.": "При изменении значений ICE в транзакции DTAX убедитесь, что вводимое значение находится в диапазоне от 1 до 5.",
    # ── ZDTP061S ──────────────────────────────────────────────────────────
    "CICS code module has been updated. A CICS restart is required to run the new code.": "Кодовый модуль CICS обновлён. Для запуска нового кода требуется перезапуск CICS.",
    # System action: None – уже выше
    "Restart CICS when you can to pick up new code module versions.": "При первой возможности перезапустите CICS, чтобы загрузить новые версии кодового модуля.",
    # ── ZDTP062S ──────────────────────────────────────────────────────────
    "CICSPlex name not found for the CICS region due to an unexpected error indicated by the error code âxxâ": 'Имя CICSPlex для региона CICS не найдено вследствие непредвиденной ошибки, обозначенной кодом ошибки "xx".',
    "CICS code module continues initialization.": "Кодовый модуль CICS продолжает инициализацию.",
    # User response: None – уже выше
    # ── ZDTP063S ──────────────────────────────────────────────────────────
    "Couldn't disable Language Environment sensor.": "Не удалось отключить датчик Language Environment.",
    "Language Environment sensor is not turned off, CICS code module continues to monitor LE events.": "Датчик Language Environment не отключён, кодовый модуль CICS продолжает отслеживать события LE.",
    # ── ZDTP064S ──────────────────────────────────────────────────────────
    "Couldn't enable Language Environment sensor.": "Не удалось включить датчик Language Environment.",
    "CICS code module doesn't monitor LE events.": "Кодовый модуль CICS не отслеживает события LE.",
    # ── ZDTP065S ──────────────────────────────────────────────────────────
    "Couldn't disable the TRUE and GLUE exits after two consecutive attempts.": "Не удалось отключить точки выхода TRUE и GLUE после двух последовательных попыток.",
    "CICS code module might cause an `AKEA` abend.": "Кодовый модуль CICS может вызвать аварийное завершение `AKEA`.",
    "Examine CICS log for `DISABLE EXITALL` failure. Please contact a Dynatrace product expert via live chat within your environment.": "Изучите журнал CICS на предмет сбоя `DISABLE EXITALL`. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP066S ──────────────────────────────────────────────────────────
    "CICS code module has detected an unsupported version of CICS.": "Кодовый модуль CICS обнаружил неподдерживаемую версию CICS.",
    # System action: CICS code module is disabled. – уже выше
    "Upgrade your CICS region to a version supported by Dynatrace.": "Выполните обновление региона CICS до версии, поддерживаемой Dynatrace.",
    # ── ZDTP067S ──────────────────────────────────────────────────────────
    "Loading of the CICS code module has failed.": "Загрузка кодового модуля CICS завершилась ошибкой.",
    # System action: CICS code module is disabled. – уже выше
    "Examine the CICS job output for any other messages that may be relevant to the failure. Please contact a Dynatrace product expert via live chat within your environment.": "Изучите вывод задания CICS на наличие других сообщений, которые могут быть связаны со сбоем. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP068S ──────────────────────────────────────────────────────────
    "The `EXEC CICS RETRIEVE` command used to control the Language Environment sensor interval has failed.": "Команда `EXEC CICS RETRIEVE`, используемая для управления интервалом датчика Language Environment, завершилась ошибкой.",
    # System action: None – уже выше
    "Examine the more detailed message in the appropriate CICS job log to look at the precise EIBRESP code that indicates why this EXEC CICS RETRIEVE command failed. Please contact a Dynatrace product expert via live chat within your environment.": "Изучите подробное сообщение в соответствующем журнале задания CICS, чтобы получить точный код EIBRESP, указывающий причину сбоя команды EXEC CICS RETRIEVE. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP069S ──────────────────────────────────────────────────────────
    "The `EXEC CICS START` command used to initiate the Language Environment sensor interval has failed.": "Команда `EXEC CICS START`, используемая для запуска интервала датчика Language Environment, завершилась ошибкой.",
    # System action: None – уже выше
    "Examine the more detailed message in the appropriate CICS job log to look at the precise EIBRESP code that indicates why this EXEC CICS START command failed. Please contact a Dynatrace product expert via live chat within your environment.": "Изучите подробное сообщение в соответствующем журнале задания CICS, чтобы получить точный код EIBRESP, указывающий причину сбоя команды EXEC CICS START. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP070S ──────────────────────────────────────────────────────────
    "During CICS startup or DTAX command processing, the Agent program was not marked ThreadSafe. ThreadSafe is required for CICS performance.": "При запуске CICS или обработке команды DTAX программа агента не была отмечена как ThreadSafe. Атрибут ThreadSafe необходим для производительности CICS.",
    "Processing is terminated and the CICS region is not setup to run Dynatrace.": "Обработка завершается, и регион CICS не настроен для работы с Dynatrace.",
    "Check that the Dynatrace CICS resource definitions has been added to the CICS region. Sample resource definitions can be found in installation sample dataset member(CICRDO). Please contact a Dynatrace product expert via live chat within your environment.": "Убедитесь, что определения ресурсов Dynatrace CICS добавлены в регион CICS. Образцы определений ресурсов см. в элементе набора данных образцов установки (CICRDO). Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP072S ──────────────────────────────────────────────────────────
    "DTAX transaction could not update the sensor hook settings in the GWA.": "Транзакция DTAX не смогла обновить параметры хуков датчиков в GWA.",
    "If this happens during DTAX initialization, DTAX is disabled. If this happens during the ICE interval, the new sensor changes will not take effect.": "Если это произошло в процессе инициализации DTAX, DTAX отключается. Если это произошло в течение интервала ICE, новые изменения датчиков не вступят в силу.",
    # ── ZDTP001W ──────────────────────────────────────────────────────────
    "RDO definition for `ZDTPLT` with suffix (67/68/69/70/71/72/73) found.": "Обнаружено определение RDO для `ZDTPLT` с суффиксом (67/68/69/70/71/72/73).",
    "Execution continues.": "Выполнение продолжается.",
    "Update the RDO definitions for `ZDTPLTxx` and DTAX to refer to `ZDTPLT` without suffix. Refer to CICRDO member in `SZDTSAMP` installation library for sample RDO definitions.": "Обновите определения RDO для `ZDTPLTxx` и DTAX, указав `ZDTPLT` без суффикса. Образцы определений RDO см. в элементе CICRDO библиотеки установки `SZDTSAMP`.",
    # ── ZDTP002W ──────────────────────────────────────────────────────────
    "There was a problem in retrieving the Global Work Area storage for exit program. `EXEC CICS EXTRACT EXIT` operation failed. This is also possible when an attempt was made to look up `DTAX CONF` when the CICS code module is disabled.": "Возникла проблема при получении памяти глобальной рабочей области для программы точки выхода. Операция `EXEC CICS EXTRACT EXIT` завершилась ошибкой. Это также возможно при попытке обратиться к `DTAX CONF`, когда кодовый модуль CICS отключён.",
    # System action: None – уже выше
    "Determine the cause of the problem from `resp` and `resp2` codes. Please contact a Dynatrace product expert via live chat within your environment.": "Выясните причину неполадки с помощью кодов `resp` и `resp2`. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP004W ──────────────────────────────────────────────────────────
    "There was no zDC available for CICS code module to connect to.": "Для кодового модуля CICS нет доступного zDC для подключения.",
    # System action: CICS code module is disabled. – уже выше
    "Start zDC and check if the zDC connects successfully to zRA. Please contact a Dynatrace product expert via live chat within your environment.": "Запустите zDC и убедитесь, что zDC успешно подключается к zRA. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP005W ──────────────────────────────────────────────────────────
    "CICS code module could not retrieve CICS Sensor configuration block.": "Кодовый модуль CICS не смог получить блок конфигурации датчиков CICS.",
    "DTAX transaction attempts to retrieve CICS Sensor configuration block in the next 5 minutes interval.": "Транзакция DTAX попытается получить блок конфигурации датчиков CICS в течение следующего 5-минутного интервала.",
    "Check if the CICS code module is successfully enabled in the next 5 minutes interval. Please contact a Dynatrace product expert via live chat within your environment.": "Убедитесь, что кодовый модуль CICS успешно включился в течение следующего 5-минутного интервала. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP006W ──────────────────────────────────────────────────────────
    "`DTAX ICE` command was issued with an invalid value.": "Команда `DTAX ICE` была выполнена с недопустимым значением.",
    "DTAX transaction sets the ICE value to the default 5 minutes.": "Транзакция DTAX устанавливает значение ICE по умолчанию: 5 минут.",
    "If you want to change the default DTAX ICE value, enter a value between 1 to 5.": "Для изменения значения ICE по умолчанию введите число от 1 до 5.",
    # ── ZDTP007W ──────────────────────────────────────────────────────────
    "No CICSplex name is available for the CICS region.": "Имя CICSplex недоступно для региона CICS.",
    # System action: CICS code module continues initialization. – уже выше
    # User response: None – уже выше
    # ── ZDTP008W ──────────────────────────────────────────────────────────
    "`DTAX CONF` option couldn't display all the configuration settings in the DTAX panel, because there's not enough screen area for the display.": "Параметр `DTAX CONF` не смог отобразить все параметры конфигурации на панели DTAX из-за недостаточной площади экрана.",
    "Configuration settings are truncated in the DTAX display": "Параметры конфигурации усечены на экране DTAX.",
    # User response: None – уже выше
    # ── ZDTP009W ──────────────────────────────────────────────────────────
    "Check all CICS code module configuration parameters in Dynatrace UI.": "Проверьте все параметры конфигурации кодового модуля CICS в интерфейсе Dynatrace.",
    # System action: None – уже выше
    "To view all the CICS code module configuration settings, go to **Settings** > **Server-side service monitoring** > **Deep monitoring** > **CICS, IMS and MQ monitoring**.": "Для просмотра всех параметров конфигурации кодового модуля CICS перейдите в **Settings** > **Server-side service monitoring** > **Deep monitoring** > **CICS, IMS and MQ monitoring**.",
    # ── ZDTP010W ──────────────────────────────────────────────────────────
    # Explanation: Couldn't enable Language Environment sensor. – уже выше
    "CICS code module doesn't monitor Language Environment events.": "Кодовый модуль CICS не отслеживает события Language Environment.",
    # ── ZDTP011W ──────────────────────────────────────────────────────────
    # Explanation: Couldn't disable Language Environment sensor. – уже выше
    "CICS code module continues to monitor Language Environment events which might cause overhead.": "Кодовый модуль CICS продолжает отслеживать события Language Environment, что может создавать дополнительную нагрузку.",
    # ── ZDTP012W ──────────────────────────────────────────────────────────
    "Dynatrace does not have permission to issue EXEC CPSM comands.": "У Dynatrace нет прав для выполнения команд EXEC CPSM.",
    "CICS code module continues but the plex name is blank or invalid.": "Кодовый модуль CICS продолжает работу, однако имя plex пустое или недопустимое.",
    "Contact system security and authorize Dynatrace to access CPSM.": "Обратитесь в службу системной безопасности и предоставьте Dynatrace доступ к CPSM.",
    # ── ZDTP013W ──────────────────────────────────────────────────────────
    "Dynatrace CICS code module versions are different.": "Версии кодового модуля Dynatrace CICS различаются.",
    # System action: None – уже выше
    "Perform `CEMT SET NEWCOPY` for the version that is older. For example: If PLT is older `CEMT SET PROG(ZDTPLT) NEWCOPY` If CICS code module version is older (`zz` is the CTS version) `CEMT SET PROG(ZDTAGTzz) NEWCOPY`": "Выполните `CEMT SET NEWCOPY` для более старой версии. Например: если PLT старее, выполните `CEMT SET PROG(ZDTPLT) NEWCOPY`; если версия кодового модуля CICS старее (`zz` соответствует версии CTS), выполните `CEMT SET PROG(ZDTAGTzz) NEWCOPY`.",
    # ── ZDTP014W ──────────────────────────────────────────────────────────
    "Invalid minute value entered for the Language Environment sensor.": "Введено недопустимое значение в минутах для датчика Language Environment.",
    # System action: None – уже выше
    "Enter a valid interval, between 1-1000 minutes, to enable the Language Environment sensor.": "Введите допустимый интервал от 1 до 1000 минут для включения датчика Language Environment.",
    # ── ZDTP015W ──────────────────────────────────────────────────────────
    "The Language Environment sensor interval value entered is out of range.": "Введённое значение интервала датчика Language Environment выходит за допустимые пределы.",
    # System action: None – уже выше
    "Enter a valid interval value between 1-1000 minutes to enable the Language Environment sensor.": "Введите допустимое значение интервала от 1 до 1000 минут для включения датчика Language Environment.",
    # ── ZDTP016W ──────────────────────────────────────────────────────────
    "The PLT program is unable to connect to the collection system.": "Программа PLT не может подключиться к системе сбора данных.",
    "Execution continues. The PLT program tries to reconnect with the collection system during the next 5 minute window.": "Выполнение продолжается. Программа PLT попытается повторно подключиться к системе сбора данных в течение следующих 5 минут.",
    "Check if the zRemote code module is up and running and connected to Dynatrace. If not, start the service that is down.": "Убедитесь, что кодовый модуль zRemote запущен и подключён к Dynatrace. Если нет, запустите неработающую службу.",
    # ── ZDTP017W ──────────────────────────────────────────────────────────
    "During CICS startup or DTAX command processing, the Agent program is not registered to the zDC.": "При запуске CICS или обработке команды DTAX программа агента не зарегистрирована в zDC.",
    "Hooks and exits are not installed.": "Хуки и точки выхода не установлены.",
    "Make sure the zDC is started and connected to a zRemote. Please contact a Dynatrace product expert via live chat within your environment.": "Убедитесь, что zDC запущен и подключён к zRemote. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP001I ──────────────────────────────────────────────────────────
    "User issued a `DTAX PING` command.": "Пользователь выполнил команду `DTAX PING`.",
    "Check if the connection exists between the z/OS CICS code module and the zRemote code module.": "Проверьте наличие соединения между кодовым модулем CICS z/OS и кодовым модулем zRemote.",
    # ── ZDTP002I ──────────────────────────────────────────────────────────
    "User issued a `DTAX DISABLE` command.": "Пользователь выполнил команду `DTAX DISABLE`.",
    "Disable all the exits used by CICS code module and terminate the 5 minutes DTAX cycle.": "Отключить все точки выхода, используемые кодовым модулем CICS, и завершить 5-минутный цикл DTAX.",
    # ── ZDTP004I ──────────────────────────────────────────────────────────
    "User issued a `DTAX CONF` command.": "Пользователь выполнил команду `DTAX CONF`.",
    "Display the active CICS Sensor configuration in the DTAX panel.": "Отобразить активную конфигурацию датчиков CICS на панели DTAX.",
    # ── ZDTP005I ──────────────────────────────────────────────────────────
    "User issued a `DTAX ENABLE` command.": "Пользователь выполнил команду `DTAX ENABLE`.",
    "CICS code module registers with the collection system. On successful connection, respective EXITs and Hooks are enabled.": "Кодовый модуль CICS регистрируется в системе сбора данных. При успешном подключении включаются соответствующие точки выхода (EXITs) и хуки.",
    # ── ZDTP006I ──────────────────────────────────────────────────────────
    "This message is displayed in the zRemote log file when DTAX initializes successfully. The call type indicates the time when DTAX initalizes. Possible call types are, CPLT - DTAX initialized during CICS startup; USER - DTAX initialized due to user command `DTAX EN`. ICE - DTAX initialized during the ICE interval. This message gives ZDTPLT compilation and version information.": "Это сообщение выводится в журнал zRemote при успешной инициализации DTAX. Тип вызова указывает на момент инициализации DTAX. Возможные типы: CPLT (DTAX инициализирован при запуске CICS), USER (DTAX инициализирован по команде пользователя `DTAX EN`), ICE (DTAX инициализирован в течение интервала ICE). Сообщение содержит информацию о компиляции и версии ZDTPLT.",
    # ── ZDTP007I ──────────────────────────────────────────────────────────
    "This message is logged in the zRemote log file when DTAX initializes successfully. This message gives CICS code module module (ZDTAGT) compilation and version information.": "Это сообщение записывается в журнал zRemote при успешной инициализации DTAX. Сообщение содержит информацию о компиляции и версии кодового модуля CICS (ZDTAGT).",
    # ── ZDTP008I ──────────────────────────────────────────────────────────
    "This message is logged in the zRemote log file when DTAX initializes successfully. This message gives ZDTSOAPH compilation and version information.": "Это сообщение записывается в журнал zRemote при успешной инициализации DTAX. Сообщение содержит информацию о компиляции и версии ZDTSOAPH.",
    # ── ZDTP009I ──────────────────────────────────────────────────────────
    "The PLT program is unable to establish connection with the zRemote code module during PLT time.": "Программа PLT не может установить соединение с кодовым модулем zRemote в течение времени PLT.",
    "Reconnect attempted during the next DTAX cycle, which starts immediately after the CICS region comes up.": "Попытка повторного подключения предпринимается в течение следующего цикла DTAX, который запускается сразу после старта региона CICS.",
    # ── ZDTP010I ──────────────────────────────────────────────────────────
    "There was a problem in retrieving the screen attributes.": "Возникла проблема при получении атрибутов экрана.",
    "Screen attributes are defaulted to `Screen Width=80` and `Screen Height=24`.": "Атрибуты экрана установлены по умолчанию: `Screen Width=80` и `Screen Height=24`.",
    # ── ZDTP011I ──────────────────────────────────────────────────────────
    "The exit program `ZDTAGTxx` associated with entryname `ZDTAGENT` is disabled. `xx` represents the CTS version.": "Программа точки выхода `ZDTAGTxx`, связанная с именем точки входа `ZDTAGENT`, отключена. `xx` соответствует версии CTS.",
    # ── ZDTP012I ──────────────────────────────────────────────────────────
    "The exit program ZDTAGTxx associated with entryname ZDTAGENT is enabled. `xx` represents the CTS version.": "Программа точки выхода ZDTAGTxx, связанная с именем точки входа ZDTAGENT, включена. `xx` соответствует версии CTS.",
    # ── ZDTP013I ──────────────────────────────────────────────────────────
    "Enable the global exit point specified by `[exit name]` associated with the ZDTAGTxx exit.": "Включить глобальную точку выхода, указанную в `[exit name]`, связанную с точкой выхода ZDTAGTxx.",
    # ── ZDTP014I ──────────────────────────────────────────────────────────
    "Start the user exit `ZDTAGENT` associated with the exit program `ZDTAGTxx`.": "Запустить пользовательскую точку выхода `ZDTAGENT`, связанную с программой точки выхода `ZDTAGTxx`.",
    # ── ZDTP015I ──────────────────────────────────────────────────────────
    "Start the global exit point specified by `[exit name]` associated with the exit program `ZDTAGTxx`.": "Запустить глобальную точку выхода, указанную в `[exit name]`, связанную с программой точки выхода `ZDTAGTxx`.",
    # ── ZDTP016I ──────────────────────────────────────────────────────────
    "Stop and disable all the exit points associated with the exit `ZDTAGTxx`.": "Остановить и отключить все точки выхода, связанные с `ZDTAGTxx`.",
    # ── ZDTP017I ──────────────────────────────────────────────────────────
    "Disable the global exit point `[exit name]` associated with the exit ZDTAGTxx.": "Отключить глобальную точку выхода `[exit name]`, связанную с точкой выхода ZDTAGTxx.",
    # ── ZDTP019I ──────────────────────────────────────────────────────────
    "Indicates that CICS sensor configuration has been retrieved successfully after there was a problem in configuration block access. This message follows after ZDTP049S when the CICS transaction server sensor has been placed.": "Указывает, что конфигурация датчиков CICS успешно получена после возникшей проблемы с доступом к блоку конфигурации. Это сообщение следует за ZDTP049S, когда датчик CICS transaction server размещён.",
    "CICS code module is initialized.": "Кодовый модуль CICS инициализирован.",
    # ── ZDTP020I ──────────────────────────────────────────────────────────
    "Indicates the CICS Sensors that are placed and active.": "Указывает, какие датчики CICS размещены и активны.",
    # ── ZDTP021I ──────────────────────────────────────────────────────────
    "Indicates that the CICS Sensors have been updated and the CICS code module honored the changes during DTAX 5 minutes cycle.": "Указывает, что датчики CICS обновлены и кодовый модуль CICS применил изменения в течение 5-минутного цикла DTAX.",
    # ── ZDTP022I ──────────────────────────────────────────────────────────
    "EXEC CICS INQUIRE DB2CONN has failed.": "Команда EXEC CICS INQUIRE DB2CONN завершилась ошибкой.",
    "CICS code module operation continues. No DB2 attachment details provided in the distributed trace.": "Кодовый модуль CICS продолжает работу. Сведения о подключении DB2 в распределённой трассировке отсутствуют.",
    # ── ZDTP023I ──────────────────────────────────────────────────────────
    "`DTAX ICE` value was changed.": "Значение `DTAX ICE` изменено.",
    "None.": "Нет.",
    # ── ZDTP024I ──────────────────────────────────────────────────────────
    "Indicates that the Trace hook is being turned on in the CICS code module.": "Указывает, что хук трассировки включается в кодовом модуле CICS.",
    # ── ZDTP025I ──────────────────────────────────────────────────────────
    "Indicates that the Trace hook is being turned off in the CICS code module.": "Указывает, что хук трассировки отключается в кодовом модуле CICS.",
    # ── ZDTP026I ──────────────────────────────────────────────────────────
    "Indicates that the Language Environment sensor has been turned on for the current DTAX ICE interval. Note that the Language Environment sensor will be automatically turned off during the following DTAX ICE cycle.": "Указывает, что датчик Language Environment включён на текущий интервал DTAX ICE. Датчик Language Environment будет автоматически отключён в течение следующего цикла DTAX ICE.",
    # ── ZDTP027I ──────────────────────────────────────────────────────────
    "Indicates that the Language Environment sensor has been automatically turned off at the end of the current ICE interval.": "Указывает, что датчик Language Environment был автоматически отключён по окончании текущего интервала ICE.",
    # ── ZDTP028I ──────────────────────────────────────────────────────────
    "Displays the Start TX sensor setting in Deep Monitoring in the web UI for the CICS regions.": "Отображает параметр датчика Start TX в разделе Deep Monitoring веб-интерфейса для регионов CICS.",
    # ── ZDTP029I ──────────────────────────────────────────────────────────
    "User issued a `DTAX LEENAB` command to turn on the Language Environment sensor.": "Пользователь выполнил команду `DTAX LEENAB` для включения датчика Language Environment.",
    "Language Environment sensor is turned on temporarily. CICS code module starts monitoring LE dynamic calls.": "Датчик Language Environment временно включён. Кодовый модуль CICS начинает отслеживать динамические вызовы LE.",
    # ── ZDTP030I ──────────────────────────────────────────────────────────
    "DTAX STATUS console command was issued. This can be used for Automated Operations to see if Dynatrace Hooks/Exits are enabled. Field descriptions: \\* `V.R`: DT Version \\* `PLT-PTF`: PLT PTF \\* `AGT-PTF`: Agent PTF \\* `TRUE-STS`: TRUE Status \\* `XPC-STS`: XPCREQ/C Status \\* `RMI-STS`: RMIIN/R \\* `ZDC-NAME`: zDC Name \\* `AGT-ID`: Agent ID": "Была выполнена консольная команда DTAX STATUS. Её можно использовать в системах автоматизированных операций для проверки того, включены ли хуки и точки выхода Dynatrace. Описание полей: `V.R`: версия DT; `PLT-PTF`: PTF для PLT; `AGT-PTF`: PTF агента; `TRUE-STS`: статус TRUE; `XPC-STS`: статус XPCREQ/C; `RMI-STS`: RMIIN/R; `ZDC-NAME`: имя zDC; `AGT-ID`: идентификатор агента.",
    "None, this is informational only.": "Нет, это исключительно информационное сообщение.",
    # ── ZDTP031I ──────────────────────────────────────────────────────────
    "Indicates that the DSA at location `addr`, used by CICS code module, has been freed.": "Указывает, что область DSA по адресу `addr`, используемая кодовым модулем CICS, освобождена.",
    "DSA memory is freed.": "Память DSA освобождена.",
    # ── ZDTP032I ──────────────────────────────────────────────────────────
    "DTAX received the LOG level update from MODIFY command.": "DTAX получил обновление уровня журналирования от команды MODIFY.",
    "None. Please contact a Dynatrace product expert via live chat within your environment.": "Нет. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP033I ──────────────────────────────────────────────────────────
    "DTAX is now using ZDTQ DD for messages instead of the default MSGUSR.": "DTAX теперь использует ZDTQ DD для сообщений вместо MSGUSR по умолчанию.",
    # ── ZDTP034I ──────────────────────────────────────────────────────────
    "This message is displayed with user specified Terminal transaction code, in the zRemote log during DTAX initialization.": "Это сообщение выводится с указанным пользователем кодом терминальной транзакции в журнале zRemote в процессе инициализации DTAX.",
    "CICS code module stops monitoring MRO events if the MRO hook has been removed successfully.": "Кодовый модуль CICS прекращает отслеживание событий MRO, если хук MRO успешно удалён.",
    "If the Return code is a non-zero value, MRO hook removal has failed. Please contact a Dynatrace product expert via live chat within your environment.": "Если код возврата не равен нулю, удаление хука MRO завершилось ошибкой. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP035I ──────────────────────────────────────────────────────────
    "The Language Environment sensor has been disabled. The CICS agent will stop monitoring LE programs.": "Датчик Language Environment отключён. Агент CICS прекратит отслеживание программ LE.",
    "None. Please contact a Dynatrace product expert via live chat within your environment.": "Нет. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP036I ──────────────────────────────────────────────────────────
    "Language Environment sensor is already disabled, no action taken.": "Датчик Language Environment уже отключён, никаких действий не предпринято.",
    # ── ZDTP131I ──────────────────────────────────────────────────────────
    "CICS code module has completed installing SOAP hook for SOAP request monitoring. Return code 0 indicates successful SOAP hook installation.": "Кодовый модуль CICS завершил установку хука SOAP для мониторинга SOAP-запросов. Код возврата 0 означает успешную установку хука SOAP.",
    "CICS code module is ready to monitor SOAP events with successful SOAP hook installation.": "Кодовый модуль CICS готов к отслеживанию событий SOAP при успешной установке хука SOAP.",
    "If the Return code is a non-zero value, SOAP hook installation has failed. Please contact a Dynatrace product expert via live chat within your environment.": "Если код возврата не равен нулю, установка хука SOAP завершилась ошибкой. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP132I ──────────────────────────────────────────────────────────
    "CICS code module has completed removing SOAP hook. Return code 0 indicates successful SOAP hook removal.": "Кодовый модуль CICS завершил удаление хука SOAP. Код возврата 0 означает успешное удаление хука SOAP.",
    # System action: CICS code module stops monitoring SOAP events if the SOAP hook has been removed successfully.
    "CICS code module stops monitoring SOAP events if the SOAP hook has been removed successfully.": "Кодовый модуль CICS прекращает отслеживание событий SOAP, если хук SOAP успешно удалён.",
    "If the Return code is a non-zero value, SOAP hook removal has failed. Please contact a Dynatrace product expert via live chat within your environment.": "Если код возврата не равен нулю, удаление хука SOAP завершилось ошибкой. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP133I ──────────────────────────────────────────────────────────
    "CICS code module has completed installing MRO hook for multi region call monitoring. Return code 0 indicates successful MRO hook installation.": "Кодовый модуль CICS завершил установку хука MRO для мониторинга вызовов нескольких регионов. Код возврата 0 означает успешную установку хука MRO.",
    "CICS code module is ready to monitor MRO events with the successful MRO hook installation.": "Кодовый модуль CICS готов к отслеживанию событий MRO при успешной установке хука MRO.",
    "If the Return code is a non-zero value, MRO hook installation has failed. Please contact a Dynatrace product expert via live chat within your environment.": "Если код возврата не равен нулю, установка хука MRO завершилась ошибкой. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP134I ──────────────────────────────────────────────────────────
    "CICS code module has completed removing MRO hook. Return code 0 indicates successful MRO hook removal.": "Кодовый модуль CICS завершил удаление хука MRO. Код возврата 0 означает успешное удаление хука MRO.",
    # System action: CICS code module stops monitoring MRO events if the MRO hook has been removed successfully.
    # User response: If the Return code is a non-zero value, MRO hook removal has failed... -> уже через ZDTP034I
    # ── ZDTP135I ──────────────────────────────────────────────────────────
    "CICS code module has completed installing ERM hook for DB2 call monitoring. Return code 0 indicates successful ERM hook installation.": "Кодовый модуль CICS завершил установку хука ERM для мониторинга вызовов Db2. Код возврата 0 означает успешную установку хука ERM.",
    "CICS code module is ready to monitor DB2 calls from the CICS region with the successful ERM hook installation.": "Кодовый модуль CICS готов к отслеживанию вызовов Db2 из региона CICS при успешной установке хука ERM.",
    "If the Return code is a non-zero value, ERM hook installation has failed. Please contact a Dynatrace product expert via live chat within your environment.": "Если код возврата не равен нулю, установка хука ERM завершилась ошибкой. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP136I ──────────────────────────────────────────────────────────
    "CICS code module has completed removing ERM hook. Return code 0 indicates successful ERM hook removal.": "Кодовый модуль CICS завершил удаление хука ERM. Код возврата 0 означает успешное удаление хука ERM.",
    "CICS code module stops monitoring DB2 calls if the ERM hook has been removed successfully.": "Кодовый модуль CICS прекращает отслеживание вызовов Db2, если хук ERM успешно удалён.",
    "If the Return code is a non-zero value, ERM hook removal has failed. Please contact a Dynatrace product expert via live chat within your environment.": "Если код возврата не равен нулю, удаление хука ERM завершилось ошибкой. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP137I ──────────────────────────────────────────────────────────
    "CICS code module has completed installing PL1 hook for monitoring PL1 dynamic calls. Return code 0 indicates successful PL1 hook installation.": "Кодовый модуль CICS завершил установку хука PL1 для мониторинга динамических вызовов PL1. Код возврата 0 означает успешную установку хука PL1.",
    "CICS code module is ready to monitor PL1 dynamic calls with the successful PL1 hook installation.": "Кодовый модуль CICS готов к отслеживанию динамических вызовов PL1 при успешной установке хука PL1.",
    "If the Return code is a non-zero value, PL1 hook installation has failed. Please contact a Dynatrace product expert via live chat within your environment.": "Если код возврата не равен нулю, установка хука PL1 завершилась ошибкой. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP138I ──────────────────────────────────────────────────────────
    "CICS code module has completed removing PL1 hook. Return code 0 indicates successful PL1 hook removal.": "Кодовый модуль CICS завершил удаление хука PL1. Код возврата 0 означает успешное удаление хука PL1.",
    "CICS code module stops monitoring PL1 dynamic calls if the PL1 hook has been removed successfully.": "Кодовый модуль CICS прекращает отслеживание динамических вызовов PL1, если хук PL1 успешно удалён.",
    "If the Return code is a non-zero value, PL1 hook removal has failed. Please contact a Dynatrace product expert via live chat within your environment.": "Если код возврата не равен нулю, удаление хука PL1 завершилось ошибкой. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP139I ──────────────────────────────────────────────────────────
    "CICS code module has completed installing COBOL hooks IGZCFCC, IGZCLNK and IGZXFCAL (indicated by âCOBOL routineâ) for monitoring COBOL dynamic calls. Return code 0 indicates successful COBOL hooks installation.": 'Кодовый модуль CICS завершил установку хуков COBOL: IGZCFCC, IGZCLNK и IGZXFCAL (обозначается как "COBOL routine") для мониторинга динамических вызовов COBOL. Код возврата 0 означает успешную установку хуков COBOL.',
    "CICS code module is ready to monitor COBOL dynamic calls with the successful COBOL hooks installation.": "Кодовый модуль CICS готов к отслеживанию динамических вызовов COBOL при успешной установке хуков COBOL.",
    "If the Return code is a non-zero value, COBOL hook installation has failed. Please contact a Dynatrace product expert via live chat within your environment.": "Если код возврата не равен нулю, установка хуков COBOL завершилась ошибкой. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── ZDTP140I ──────────────────────────────────────────────────────────
    "CICS code module has completed removing COBOL hook. Return code 0 indicates successful COBOL hook removal.": "Кодовый модуль CICS завершил удаление хука COBOL. Код возврата 0 означает успешное удаление хука COBOL.",
    "CICS code module stops monitoring COBOL dynamic calls if the COBOL hook has been removed successfully.": "Кодовый модуль CICS прекращает отслеживание динамических вызовов COBOL, если хук COBOL успешно удалён.",
    "If the Return code is a non-zero value, COBOL hook removal has failed. Please contact a Dynatrace product expert via live chat within your environment.": "Если код возврата не равен нулю, удаление хука COBOL завершилось ошибкой. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ── shared ─────────────────────────────────────────────────────────────
    "Please contact a Dynatrace product expert via live chat within your Dynatrace environment.": "Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении Dynatrace.",
}

# ---------------------------------------------------------------------------
# META: всё что не буллет-лейбл и не message-ID:
#   title/# заголовки / *N-min read / *Published / continuation абзацы /
#   ## Related topics / ссылки.
# ---------------------------------------------------------------------------
META = {
    "title: z/OS module messages - DTAX messages": "title: Сообщения модулей z/OS - сообщения DTAX",
    "# z/OS module messages - DTAX messages": "# Сообщения модулей z/OS - сообщения DTAX",
    "* 43-min read": "* Чтение: 43 мин",
    "* Published Mar 22, 2019": "* Опубликовано 22 марта 2019 г.",
    # continuation абзацы (отступ 2 пробела, но движок strip'ует):
    "If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.": "Если проблема не устраняется, обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении Dynatrace.",
    "If the problem persists, please contact a Dynatrace product expert via live chat within your environment.": "Если проблема не устраняется, обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # Related topics
    "## Related topics": "## Связанные темы",
    '* [Manage the CICS module via DTAX transactions](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.")': '* [Управление модулем CICS через DTAX-транзакции](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Управление модулем CICS через DTAX-транзакции.")',
}

if __name__ == "__main__":
    build_messages(REL, FN, PROSE, META)
    qa_one(REL, FN)
