# -*- coding: utf-8 -*-
"""Builder for zdc-system-messages.md  (L4-IF.71 batch)."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_messages, qa_one

REL = "ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages"
FN = "zdc-system-messages.md"

PROSE = {
    # ZDC000I
    "This informational message indicates that the initialization of the zDC has started or ended. The subsystem ID and the version of the product are displayed.": "Это информационное сообщение указывает, что инициализация zDC началась или завершилась. Отображается идентификатор подсистемы и версия продукта.",
    "Processing continues.": "Обработка продолжается.",
    "None": "Нет",
    # ZDC001E
    "At zDC system startup the was an attempt to load all the processing modules into storage. This load was unsuccessful for the module named (`@@`) in this message.": "При запуске системы zDC была предпринята попытка загрузить все модули обработки в память. Загрузка модуля, указанного в этом сообщении (`@@`), завершилась неудачей.",
    "zDC terminates.": "zDC завершает работу.",
    "Ensure that the `//STEPLIB` or `//JOBLIB DD` statements in the JCL executing zDC point to the correct data sets and that these data sets contain the correct release of the zDC.": "Убедитесь, что операторы `//STEPLIB` или `//JOBLIB DD` в JCL, запускающем zDC, указывают на правильные наборы данных, и что эти наборы данных содержат нужный выпуск zDC.",
    # ZDC002E
    "This message follows `ZDC001` and gives the module name as well as the contents of `R15` and `R1` at the completion of the LPAD operation.": "Это сообщение следует за `ZDC001` и содержит имя модуля, а также содержимое регистров `R15` и `R1` по завершении операции LPAD.",
    "Save the information in this message if you need to contact your systems programmer or a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.": "Сохраните информацию из этого сообщения, если потребуется обратиться к системному программисту или специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC003E
    "This message indicates that the attempt to load the module named in the message into extended common storage has failed because there is not enough available storage to hold the module.": "Это сообщение указывает, что попытка загрузить модуль, указанный в сообщении, в расширенную общую память завершилась ошибкой из-за нехватки доступной памяти для размещения модуля.",
    "Increase the amount of common storage, specifically subpool 241, and start zDC again.": "Увеличьте объём общей памяти, в частности субпула 241, и снова запустите zDC.",
    # ZDC004E
    "At zDC system startup there was an attempt to load all the processing modules into storage. The `BLDL` for this load was unsuccessful for the module named in the message.": "При запуске системы zDC была предпринята попытка загрузить все модули обработки в память. Операция `BLDL` для загрузки модуля, указанного в сообщении, завершилась неудачей.",
    # ZDC005E
    "This message follows `ZDC004` and gives the module name, and the contents of `R15` and `R1` at the completion of the `BLDL` operation.": "Это сообщение следует за `ZDC004` и содержит имя модуля, а также содержимое регистров `R15` и `R1` по завершении операции `BLDL`.",
    "Save the information in this message if you have to contact your systems programmer or a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.": "Сохраните информацию из этого сообщения, если потребуется обратиться к системному программисту или специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC006E
    "This message indicates that the 4-character subsystem ID you specified in the `//SYSIN DD` parameter data set already exists in your system and it is an active zDC subsystem.": "Это сообщение указывает, что 4-символьный идентификатор подсистемы, указанный в наборе данных параметров `//SYSIN DD`, уже существует в системе и является активной подсистемой zDC.",
    "Ensure that the subsystem ID you have specified is unique in your system. Then restart zDC or stop the instance of the zDC that holds this name.": "Убедитесь, что указанный идентификатор подсистемы уникален в вашей системе. Затем перезапустите zDC или остановите экземпляр zDC с этим именем.",
    # ZDC007E
    "This message indicates that the attempt to obtain storage for the subsystem control block has failed. There is not enough storage above the line in extended CSA sub-pool 241 for these blocks.": "Это сообщение указывает, что попытка выделить память для управляющего блока подсистемы завершилась ошибкой. В расширенном субпуле CSA 241 недостаточно памяти выше граничной линии для этих блоков.",
    "Increase the amount of extended CSA subpool 241 storage and restart the zDC.": "Увеличьте объём памяти расширенного субпула CSA 241 и перезапустите zDC.",
    # ZDC008I
    "This message is displayed only at zDC startup. It names the columns shown below in multiple message numbers `ZDC009`. The module name, highest problem tracking number, the date and time the module was last assembled, the version of the module and the main storage address where it is loaded are shown.": "Это сообщение отображается только при запуске zDC. В нём указаны столбцы, отображаемые далее в нескольких сообщениях `ZDC009`: имя модуля, наибольший номер отслеживания проблем, дата и время последней сборки модуля, его версия и адрес основной памяти, по которому он загружен.",
    # ZDC009I
    "This message lists one module loaded by zDC. See the `ZDC008` message for a description of the columns.": "В этом сообщении перечислен один модуль, загруженный zDC. Описание столбцов см. в сообщении `ZDC008`.",
    # ZDC010E
    "This message is displayed on the system console by the zDC dump routines. It names the abend code.": "Это сообщение выводится на системную консоль подпрограммами дампа zDC. В нём указан код аварийного завершения.",
    "Execution terminates.": "Выполнение завершается.",
    "Prepare the dump for examination by your systems staff or for transmission to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment. re-execute the zDC.": "Подготовьте дамп для изучения системным персоналом или передачи специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении. Повторно запустите zDC.",
    # ZDC011E
    "This message is displayed on the system console by the zDC dump routines. It indicates that the attempt to obtain a system dump has failed. The return and reason code for the failure are shown in the message.": "Это сообщение выводится на системную консоль подпрограммами дампа zDC. Оно указывает, что попытка получить системный дамп завершилась ошибкой. В сообщении отображены код возврата и код причины сбоя.",
    "Examine the return and reason codes or supply this message to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment. re-execute the zDC.": "Изучите коды возврата и причины или передайте это сообщение специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении. Повторно запустите zDC.",
    # ZDC012E
    "This message is the title for all SDUMPX macros issued by zDC. This title indicates the abend code that caused the dump to be taken.": "Это сообщение является заголовком для всех макросов SDUMPX, выдаваемых zDC. Заголовок указывает код аварийного завершения, ставший причиной создания дампа.",
    "Ensure that the dump is preserved and can be given to your systems programming staff or a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment. re-execute the zDC.": "Убедитесь, что дамп сохранён и может быть передан системным программистам или специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении. Повторно запустите zDC.",
    # ZDC014E
    "This message indicates that a non-zero return code has resulted from a VSAM zDC log request. The name of the request is contained in the message.": "Это сообщение указывает, что запрос журнала VSAM zDC вернул ненулевой код возврата. В сообщении содержится имя запроса.",
    "The log task terminates but the execution of the zDC continues.": "Задача журналирования завершается, но выполнение zDC продолжается.",
    "Examine the subsequent messages, which contain detailed information about the nature of the error. Keep this information for your systems programming staff or for a Dynatrace product expert via live chat. Try to and re-attach and re-open the log (MVS command: `Modify ZdcStcName,LOG OPEN`). Please contact a Dynatrace product expert via live chat within your environment.": "Изучите последующие сообщения, содержащие подробную информацию о характере ошибки. Сохраните эту информацию для системных программистов или специалиста по продуктам Dynatrace через чат. Попробуйте повторно подключить и открыть журнал (команда MVS: `Modify ZdcStcName,LOG OPEN`). Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC015E
    "This message contains the value of the VSAM RPL feedback word following a VSAM PUT to the log data set.": "Это сообщение содержит значение слова обратной связи VSAM RPL после операции VSAM PUT в набор данных журнала.",
    "The log task terminates but execution of the zDC continues.": "Задача журналирования завершается, но выполнение zDC продолжается.",
    "Examine the subsequent messages, which contain detailed information about the nature of the error. Keep this information for your systems programming staff or for a Dynatrace product expert via live chat. Try to re-attach and re-open the log (MVS command: `Modify ZdcStcName,LOG OPEN`). Please contact a Dynatrace product expert via live chat within your environment.": "Изучите последующие сообщения, содержащие подробную информацию о характере ошибки. Сохраните эту информацию для системных программистов или специалиста по продуктам Dynatrace через чат. Попробуйте повторно подключить и открыть журнал (команда MVS: `Modify ZdcStcName,LOG OPEN`). Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC016E
    "This message contains the value of the VSAM ACB error flag following a VSAM OPEN or CLOSE of the log data set.": "Это сообщение содержит значение флага ошибки VSAM ACB после операции VSAM OPEN или CLOSE над набором данных журнала.",
    "Examine the subsequent messages, which contain detailed information about the nature of the error. Keep this information for your systems programming staff or for a Dynatrace product expert via live chat. Enter the ISPF zDC control system. Then re-attach and re-open the log. Please contact a Dynatrace product expert via live chat within your environment..": "Изучите последующие сообщения, содержащие подробную информацию о характере ошибки. Сохраните эту информацию для системных программистов или специалиста по продуктам Dynatrace через чат. Войдите в систему управления ISPF zDC. Затем повторно подключите и откройте журнал. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC017E
    "This message indicates that an abend has occurred at the displacement shown into the SRB routine named `ZDCSRBRT`.": "Это сообщение указывает, что произошло аварийное завершение по смещению, указанному в подпрограмме SRB `ZDCSRBRT`.",
    "If a dump is produced, save it for your systems staff or for transmission to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment. re-execute the zDC.": "Если дамп создан, сохраните его для системного персонала или передайте специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении. Повторно запустите zDC.",
    # ZDC018E
    "This message indicates that a `STORAGE OBTAIN` has failed to report that extended CSA storage from subpool 241 is not available.": "Это сообщение указывает, что операция `STORAGE OBTAIN` завершилась ошибкой: расширенная память CSA из субпула 241 недоступна.",
    "Report this condition to your systems programmer who may want to increase the amount of extended CSA storage in the system.": "Сообщите об этой ситуации системному программисту, которому может потребоваться увеличить объём расширенной памяти CSA в системе.",
    # ZDC019E
    "This message indicates that the initialization routines have failed. It also shows the return and reason codes describing this failure.": "Это сообщение указывает, что подпрограммы инициализации завершились ошибкой. В нём также отображены коды возврата и причины, описывающие сбой.",
    "zDC execution terminates.": "Выполнение zDC завершается.",
    "Examine the SYSPRINT data set for any other messages that may be relevant to the failure. Please contact a Dynatrace product expert via live chat within your environment.": "Изучите набор данных SYSPRINT на наличие других сообщений, которые могут быть связаны со сбоем. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC026I
    "This message confirms that the STOP command entered by an operator has been accepted by zDC and end of job processing has commenced.": "Это сообщение подтверждает, что команда STOP, введённая оператором, принята zDC и начата обработка завершения задания.",
    "Execution terminates.": "Выполнение завершается.",
    # ZDC027I
    "This message confirms that the MODIFY command entered by an operator has been received by zDC and is processing. Any errors encountered during parsing or execution of the command are indicated later.": "Это сообщение подтверждает, что команда MODIFY, введённая оператором, получена zDC и обрабатывается. Ошибки, возникшие при синтаксическом разборе или выполнении команды, будут указаны позднее.",
    "Execution continues.": "Выполнение продолжается.",
    # ZDC028I
    "This message contains a copy of the entire command entered by the operator in the console. Only the first 120 bytes of the command are displayed.": "Это сообщение содержит копию полной команды, введённой оператором на консоли. Отображаются только первые 120 байт команды.",
    # ZDC029E
    "This message indicates that the ECB for TCPSP subtask is busy and unavailable to receive the shutdown request.": "Это сообщение указывает, что ECB подзадачи TCPSP занят и недоступен для получения запроса на завершение работы.",
    "If a dump is produced, save it for your systems staff or for transmission to a Dynatrace product expert via live chat. Re-execute the zDC. Please contact a Dynatrace product expert via live chat within your environment.": "Если дамп создан, сохраните его для системного персонала или передайте специалисту по продуктам Dynatrace через чат. Повторно запустите zDC. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC033E
    "The command you just entered in the operator console was invalid and wasn't processed.": "Команда, введённая на операторской консоли, недопустима и не была обработана.",
    "The command is ignored and processing continues.": "Команда игнорируется, обработка продолжается.",
    "Re-enter a valid command if possible. If the command was valid, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.": "Если возможно, введите допустимую команду. Если команда была верной, обратитесь к специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC035I
    "This message indicates that you have selected ARM processing and this is the first time the element named in this message has been armed. This means the execution is not due to an automatic restart.": "Это сообщение указывает, что выбрана обработка ARM и элемент, указанный в сообщении, вооружён впервые. Это означает, что выполнение не является результатом автоматического перезапуска.",
    # ZDC036I
    "This message indicates that this zDC has been automatically restarted by the system. The reason code indicates whether the JCL or START command has been changed (RSNCD=108) or has not been changed (RSNCD=104).": "Это сообщение указывает, что данный zDC был автоматически перезапущен системой. Код причины указывает, был ли изменён JCL или команда START (RSNCD=108) или нет (RSNCD=104).",
    # ZDC037E
    "An attempt to issue IXCARM macro has resulted in a return code greater than 4. This indicates that the request did not complete. The actual return and reason codes are shown in this message.": "Попытка выдать макрос IXCARM привела к коду возврата больше 4. Это означает, что запрос не выполнен. Фактические коды возврата и причины отображены в этом сообщении.",
    "Processing continues but without ARM support.": "Обработка продолжается, но без поддержки ARM.",
    "See the **z/OS MVS Sysplex Services Reference** for a complete list of the possible return and reason codes. Correct any environmental errors or report this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.": "Полный список возможных кодов возврата и причин см. в **z/OS MVS Sysplex Services Reference**. Исправьте ошибки среды или сообщите о проблеме специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC038E
    "An attempt to issue `IXCARM` macro has resulted in a return code greater than 4. This indicates that the request did not complete. The actual return and reason codes are shown in this message.": "Попытка выдать макрос `IXCARM` привела к коду возврата больше 4. Это означает, что запрос не выполнен. Фактические коды возврата и причины отображены в этом сообщении.",
    "See the **z/OS MVS Sysplex Services Reference** for a complete list of the possible return and reason codes. Correct any environmental errors or report this problem to a Dynatrace product expert via live chat within your Dynatrace environment.": "Полный список возможных кодов возврата и причин см. в **z/OS MVS Sysplex Services Reference**. Исправьте ошибки среды или сообщите о проблеме специалисту по продуктам Dynatrace через чат в вашем окружении Dynatrace.",
    # ZDC039I
    "An attempt to issue IXCARM macro has resulted in a return code indicating that ARM support is not available on this system, or it may be available but stopped.": "Попытка выдать макрос IXCARM привела к коду возврата, указывающему, что поддержка ARM недоступна в данной системе или может быть доступна, но остановлена.",
    "See the **z/OS MVS Sysplex Services Reference** for a complete list of the possible return and reason codes. You might need to issue the operator command `SETXCF START,POLICY,TYPE=ARM` to activate ARM processing.": "Полный список возможных кодов возврата и причин см. в **z/OS MVS Sysplex Services Reference**. Возможно, потребуется выполнить команду оператора `SETXCF START,POLICY,TYPE=ARM` для активации обработки ARM.",
    # ZDC040I
    "This message indicates that an `IXCARM` has been issued in order for the server to go to a normal end of job.": "Это сообщение указывает, что был выдан макрос `IXCARM`, чтобы сервер перешёл к нормальному завершению задания.",
    # ZDC048I
    "This message is printed in the `SYSPRINT` data set and indicates that all modules named next via `ZDC009I` messages were loaded into ECSA.": "Это сообщение выводится в набор данных `SYSPRINT` и указывает, что все модули, перечисленные далее в сообщениях `ZDC009I`, были загружены в ECSA.",
    # ZDC049I
    "This message is printed in the `SYSPRINT` data set and indicates that all modules named next via `ZDC009I` messages were loaded into the private area of the zDC.": "Это сообщение выводится в набор данных `SYSPRINT` и указывает, что все модули, перечисленные далее в сообщениях `ZDC009I`, были загружены в частную область zDC.",
    # ZDC052I
    "This informational message indicates the name and release level on which this zDC is running.": "Это информационное сообщение указывает имя и уровень выпуска, на котором работает данный zDC.",
    # ZDC053I
    "This informational message indicates the name of the LPAR on which this zDC is running and the name of the operating system on which this zDC is running.": "Это информационное сообщение указывает имя LPAR, на котором работает данный zDC, и имя операционной системы, в которой работает данный zDC.",
    # ZDC054E
    "This message indicates that during the process of establishing a new zDC subsystem on this LPAR, a previous subsystem named in the message was already active and marked as the default subsystem.": "Это сообщение указывает, что в процессе создания новой подсистемы zDC на этом LPAR предыдущая подсистема, указанная в сообщении, уже была активна и отмечена как подсистема по умолчанию.",
    "zDC execution ends.": "Выполнение zDC завершается.",
    "Only one zDC subsystem at a time can be marked as the default. Change the parameter specification of this zDC to indicate `DEFAULT(NO)` and re-execute the zDC. You can also stop the zDC job with the named subsystem, which allows another subsystem to specify it as the default one. Note, that if the zDC instance with the subsystem named is unable to be cancelled or if it has been cancelled and its subsystem remains active, then you can specify `DEFAULT(YES,FORCE)`. The existing subsystem is marked as not the default and the new one is marked as the default.": "Только одна подсистема zDC одновременно может быть отмечена как подсистема по умолчанию. Измените спецификацию параметра данного zDC, указав `DEFAULT(NO)`, и повторно запустите zDC. Можно также остановить задание zDC с именованной подсистемой, что позволит другой подсистеме указать её в качестве подсистемы по умолчанию. Обратите внимание: если экземпляр zDC с указанной подсистемой невозможно отменить или если он отменён, но его подсистема остаётся активной, можно указать `DEFAULT(YES,FORCE)`. Существующая подсистема будет снята с роли подсистемы по умолчанию, а новая будет отмечена как таковая.",
    # ZDC055I
    "This informational message indicates the MSU capacity on which this zDC is running. If running as z/VM guest, shows guest MSU capacity.": "Это информационное сообщение указывает ёмкость MSU, на которой работает данный zDC. Если zDC работает как гостевая система z/VM, отображается гостевая ёмкость MSU.",
    # ZDC056I
    "This informational message indicates the processors vailable to LPAR and how many of them are ZIIP speciality processors.": "Это информационное сообщение указывает количество процессоров, доступных LPAR, и сколько из них являются специализированными процессорами ZIIP.",
    # ZDC057I
    "Facilities installed in the configuration. Hex dump of the area to assist issue diagnosis. See STORE FACILITY LIST EXTENDED (STFLE) instruction": "Средства, установленные в конфигурации. Шестнадцатеричный дамп области для помощи в диагностике проблем. См. инструкцию STORE FACILITY LIST EXTENDED (STFLE).",
    # ZDC059I
    "This message is written to SYSPRINT indicating that the user ID you specified in `TCPIP_USERID` is now in control of the main task of the zDC.": "Это сообщение записывается в SYSPRINT и указывает, что идентификатор пользователя, заданный в `TCPIP_USERID`, теперь управляет основной задачей zDC.",
    # ZDC060I
    "This message is written to `SYSPRINT` indicating that the action you requested in a `LOG` command has been successfully executed.": "Это сообщение записывается в `SYSPRINT` и указывает, что запрошенное командой `LOG` действие успешно выполнено.",
    # ZDC061E
    "This message is written to `SYSPRINT` indicating that the `USERID`under which zDC is running does not have the necessary security access to the log data set. This access must be `ACCESS(ALTER)` in order that the log data set can be created and/or extended and be available.": "Это сообщение записывается в `SYSPRINT` и указывает, что идентификатор пользователя, под которым работает zDC, не имеет необходимого доступа к набору данных журнала. Для создания и/или расширения набора данных журнала и его доступности требуется `ACCESS(ALTER)`.",
    "Processing continues but without the log.": "Обработка продолжается, но без журнала.",
    "Either grant the user ID under which zDC is running ACCESS(ALTER) to the log data set or supply a user ID that has this access level. Note that the log data set must be defined as a generic entity in order to pass the RACROUTE used in zDC.": "Предоставьте идентификатору пользователя, под которым работает zDC, доступ ACCESS(ALTER) к набору данных журнала или укажите идентификатор пользователя с таким уровнем доступа. Обратите внимание: набор данных журнала должен быть определён как универсальная сущность для прохождения проверки RACROUTE, используемой в zDC.",
    # ZDC062E
    "This message is written to `SYSPRINT` indicating that the log subtask has failed to initialize.": "Это сообщение записывается в `SYSPRINT` и указывает, что подзадача журналирования не смогла инициализироваться.",
    "zDC processing continues but without the log.": "Обработка zDC продолжается, но без журнала.",
    "Scan the system console and the JES job log for messages relating to this problem. Look carefully for any system access `(RACF, ACF/2, TOPSECRET)` messages relating to the log data set.": "Просмотрите системную консоль и журнал заданий JES на наличие сообщений, связанных с этой проблемой. Обратите особое внимание на сообщения системного доступа `(RACF, ACF/2, TOPSECRET)`, относящиеся к набору данных журнала.",
    # ZDC064E
    "This message is written to `SYSPRINT` indicating that the queue subtask has failed to initialize.": "Это сообщение записывается в `SYSPRINT` и указывает, что подзадача очереди не смогла инициализироваться.",
    "zDC terminates.": "zDC завершает работу.",
    "Please contact a Dynatrace product expert via live chat within your environment.": "Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC065I
    "This message is written to SYSPRINT indicating that initialization of the zDC has been successful.": "Это сообщение записывается в SYSPRINT и указывает, что инициализация zDC прошла успешно.",
    # ZDC066E
    "This message is written to `SYSPRINT` indicating that the queue subtask has failed. Return and reason codes are contained in this message.": "Это сообщение записывается в `SYSPRINT` и указывает, что подзадача очереди завершилась ошибкой. В сообщении содержатся коды возврата и причины.",
    'If `"QUEUE"=DtAgt`, in the message, review the following: \\* The zDC task tries to connect to the zRemote. One of the first things it does is bootstrap the zLocal from the server using the zRemote. If the bootstrapping fails, meaning that the zLocal can\'t be loaded, the zDC task tries three times then issues a user abend. The fallback is that if this happens, the zDC tries to load the most recently bootstrapped zLocal. If it is the first time the zDC has been started in a new work area on the OMVS filesystem, and there is no previously downloaded zLocal, then this user abend is issued. \\* Check that the zRemote code module parameter in the zDC `//SYSIN` is correct. This needs to point to the zRemote instance, which needs to be up and running, and connected to a server, so that the zLocal bootstrapping can happen. \\* Review the zDC spool output for bootstrap messages. If `"QUEUE"=QUEUE`, in the message, report this message to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.': 'Если в сообщении `"QUEUE"=DtAgt`, выполните следующие действия: задача zDC пытается подключиться к zRemote. Одним из первых действий является начальная загрузка zLocal с сервера через zRemote. Если начальная загрузка завершается ошибкой (zLocal не удаётся загрузить), задача zDC предпринимает три попытки, после чего выдаёт пользовательское аварийное завершение. Резервный вариант: если это происходит, zDC пытается загрузить последний загрузочный образ zLocal. Если zDC запускается в новой рабочей области файловой системы OMVS впервые и ранее загруженный zLocal отсутствует, выдаётся это пользовательское аварийное завершение. Убедитесь, что параметр кодового модуля zRemote в `//SYSIN` zDC указан верно: он должен ссылаться на запущенный экземпляр zRemote, подключённый к серверу, чтобы начальная загрузка zLocal была возможна. Просмотрите вывод спула zDC на наличие сообщений о начальной загрузке. Если в сообщении `"QUEUE"=QUEUE`, сообщите о проблеме специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.',
    # ZDC067E
    "This message is written to `SYSPRINT` indicating that the log subtask has failed. Return and reason codes are contained in this message.": "Это сообщение записывается в `SYSPRINT` и указывает, что подзадача журналирования завершилась ошибкой. В сообщении содержатся коды возврата и причины.",
    "Scan the system console and the JES job log for messages relating to this problem. Look carefully for any system access `(RACF, ACF/2, TOPSECRET)` messages relating to the log data set.": "Просмотрите системную консоль и журнал заданий JES на наличие сообщений, связанных с этой проблемой. Обратите особое внимание на сообщения системного доступа `(RACF, ACF/2, TOPSECRET)`, относящиеся к набору данных журнала.",
    # ZDC069W
    "This message indicates that the queue is filling. New internal events are not accepted once the queue reaches 100%. This message first displays when the queue reaches 75% and it re-displays at each 5% interval. When the queue drops below 75%, this message is no longer displayed. This message appears on the system console as well as in the SYSPRINT data set.": "Это сообщение указывает, что очередь заполняется. При достижении 100% заполнения новые внутренние события не принимаются. Сообщение впервые отображается при заполнении очереди на 75% и повторяется через каждые 5%. Когда уровень заполнения опускается ниже 75%, сообщение больше не отображается. Оно выводится как на системной консоли, так и в наборе данных SYSPRINT.",
    "Execution continues.": "Выполнение продолжается.",
    # ZDC071W
    "This message indicates that the `ZDCSDUMP` module could not create a symptom record to be included in the `SDUMP` that it was about to write.": "Это сообщение указывает, что модуль `ZDCSDUMP` не смог создать запись симптомов для включения в `SDUMP`, который он собирался записать.",
    "The dump is created but without a symptom record.": "Дамп создан, но без записи симптомов.",
    "None": "Нет",
    # ZDC072W
    "This message indicates that the process to create an WLM enclave has not been successful. The function name is shown in the message along with the return and reason codes from execution of this function. This is a warning message only because execution of the zDC continues. See below.": "Это сообщение указывает, что процесс создания анклава WLM завершился неудачно. В сообщении отображены имя функции, а также коды возврата и причины её выполнения. Это только предупреждение: выполнение zDC продолжается. Подробнее см. ниже.",
    "zDC execution continues but all processing is performed in task mode and the enclave SRB is not dispatched. Hence there is no execution on any zIIP.": "Выполнение zDC продолжается, но вся обработка выполняется в режиме задачи, а SRB анклава не диспетчеризуется. Таким образом, выполнение на каком-либо zIIP не производится.",
    "Report this message to your systems programmer who might need to contact a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.": "Сообщите об этом системному программисту, которому может потребоваться обратиться к специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC073I
    "This message indicates that the process to create an WLM enclave has been successful and zDC is a member of the enclave named in the message.": "Это сообщение указывает, что процесс создания анклава WLM успешно завершён и zDC является членом анклава, указанного в сообщении.",
    # ZDC074E
    "This message indicates that the process to delete a WLM enclave has not been successful. The function name is shown in the message along with the return and reason codes from the execution of this function.": "Это сообщение указывает, что процесс удаления анклава WLM завершился неудачно. В сообщении отображены имя функции, а также коды возврата и причины её выполнения.",
    "Report this message to your systems programmer who might need to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.": "Сообщите об этом системному программисту, которому может потребоваться обратиться к специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC076E
    "This message indicates that the enclave SRB has failed to execute correctly. If the RETCODE in this message is `1C`, then message `ZDC077` is written next with the details concerning the failure.": "Это сообщение указывает, что SRB анклава не выполнился корректно. Если код возврата RETCODE в этом сообщении равен `1C`, далее записывается сообщение `ZDC077` с подробностями сбоя.",
    # ZDC077E
    "The three codes in this message correspond to the `IEAMSCHD` `SYNCHCOMPADDR`, `SYNCHCODEADDR` and `SYNCHRSNADDR` values.": "Три кода в этом сообщении соответствуют значениям `IEAMSCHD` `SYNCHCOMPADDR`, `SYNCHCODEADDR` и `SYNCHRSNADDR`.",
    # ZDC078W
    "This message is written to `SYSPRINT` indicating that the zDC appears to be getting insufficient processor service to handle messages in a timely fashion.": "Это сообщение записывается в `SYSPRINT` и указывает, что zDC, по всей видимости, получает недостаточное процессорное обслуживание для своевременной обработки сообщений.",
    "There are 2 formats of the message followed by 4 hex words: \\* {QueRt.StaWDGp Unexpected GP dispatch delay} \\* {QueRt.StaWZSp Unexpected ZIIP dispatch delay} GP is general processor delay, while ZIIP is IBM's Systems Integrated Information Processor. The first 2 hex words are a 64bit number in STCK format with the sum of the unexpected delays. (Convert to decimal and divide by 4096 to getmicro-seconds) The 3rd and 4th word are a count of unexpected delays and a count of how may times the delay has been evaluated. The average unexpected delay is the 64bit sum divided by the unexpected delay count. For example: `ZDC078W QueRt.StaWDGp Unexpected GP dispatch` delay 00000000 F7E0822C 00000003 000019E2. xF7E0822C/x00000003=1.015sec/3=.338sec average unexpected delay base on x19E2/6,626 observations. By default, he message will display at most once every 10 minutes. An unexpected delay defaults to .25 sec. That is, a task goes into a wait for 2 seconds and gets control back after over 2.25 seconds. zDC parm: `ZDCDISPATCHDELAYWARN(25)` sets delay threshold in .01 second units e.g. 25=250 milli-sec. zDC parm: `ZDCDISPATCHDELAYRPTM(10)` sets reporting interval in minutes. Generally, use your performance tools to look for workflow delays in the 10 minute window before the warning message (for example, IBM's RMF monitor III). Also, check PARMLIB member `IEAOPTxx` parameter: `IIPHONORPRIORITY=NO`. NO can cause ZIIP eligible work to be delayed if GP processors are available.": "Сообщение имеет 2 формата, за которыми следуют 4 шестнадцатеричных слова: {QueRt.StaWDGp Unexpected GP dispatch delay} и {QueRt.StaWZSp Unexpected ZIIP dispatch delay}. GP означает задержку универсального процессора, ZIIP - Systems Integrated Information Processor компании IBM. Первые 2 шестнадцатеричных слова представляют собой 64-битное число в формате STCK с суммой неожиданных задержек (преобразуйте в десятичное и разделите на 4096 для получения микросекунд). 3-е и 4-е слова: счётчик неожиданных задержек и счётчик количества оценок задержки. Средняя неожиданная задержка: 64-битная сумма, делённая на счётчик неожиданных задержек. Пример: `ZDC078W QueRt.StaWDGp Unexpected GP dispatch` delay 00000000 F7E0822C 00000003 000019E2. xF7E0822C/x00000003=1.015 сек/3=0.338 сек средняя неожиданная задержка на основе x19E2/6 626 наблюдений. По умолчанию сообщение выводится не чаще одного раза в 10 минут. Неожиданная задержка по умолчанию составляет 0.25 сек: задача уходит в ожидание на 2 секунды и возвращает управление после более чем 2.25 секунды. Параметр zDC `ZDCDISPATCHDELAYWARN(25)` задаёт порог задержки в единицах 0.01 сек (например, 25=250 мс). Параметр zDC `ZDCDISPATCHDELAYRPTM(10)` задаёт интервал отчётности в минутах. Для поиска задержек в рабочем процессе используйте средства анализа производительности в 10-минутном окне перед предупреждением (например, RMF monitor III от IBM). Также проверьте параметр `IIPHONORPRIORITY=NO` в элементе PARMLIB `IEAOPTxx`: значение NO может приводить к задержке работ, подходящих для ZIIP, если доступны процессоры GP.",
    # ZDC079W
    "This message indicates that and internal release function didn't complete properly.": "Это сообщение указывает, что внутренняя функция освобождения не выполнилась корректно.",
    "If the issue persists, save the information in this message and contact your systems programmer or a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.": "Если проблема сохраняется, сохраните информацию из этого сообщения и обратитесь к системному программисту или специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC083E
    "This message indicates that the 4-character subsystem ID you specified in the `//SYSIN DD` parameter data set already exists on your system but is used by some other program that is not Dynatrace zDC.": "Это сообщение указывает, что 4-символьный идентификатор подсистемы, указанный в наборе данных параметров `//SYSIN DD`, уже существует в системе, но используется другой программой, не являющейся Dynatrace zDC.",
    "Ensure that the subsystem ID you have specified is unique on your system then restart zDC.": "Убедитесь, что указанный идентификатор подсистемы уникален в вашей системе, затем перезапустите zDC.",
    # ZDC100I
    "This message indicates that the `//SYSIN` parameters specified by the customer are listed next.": "Это сообщение указывает, что далее перечислены параметры `//SYSIN`, указанные клиентом.",
    # ZDC101I
    "This message indicates that the `//SYSIN` parameters specified by the customer have all been previously listed.": "Это сообщение указывает, что все параметры `//SYSIN`, указанные клиентом, были перечислены ранее.",
    # ZDC102E
    "During the parsing of the `//SYSIN DD` data, the z/OS system variable substitution routine is called for each parameter. A non-zero return code resulted from one of these calls.": "При синтаксическом разборе данных `//SYSIN DD` для каждого параметра вызывается подпрограмма подстановки системных переменных z/OS. Один из этих вызовов вернул ненулевой код возврата.",
    "Correct the parameter in error and re-execute the zDC.": "Исправьте параметр с ошибкой и повторно запустите zDC.",
    # ZDC103E
    "The attempt to open the `SYSIN` data set failed. There is no return code associated with this error but a message may be displayed in the job log that better explains the error.": "Попытка открыть набор данных `SYSIN` завершилась ошибкой. Код возврата для этой ошибки отсутствует, однако в журнале задания может быть отображено сообщение с более подробным объяснением.",
    "Ensure that the `//SYSIN DD` statement exists in the JCL used to invoke zDC and ensure that it points to a data set with DCB characteristics of `LRECL=80`.": "Убедитесь, что оператор `//SYSIN DD` существует в JCL, используемом для запуска zDC, и что он указывает на набор данных с характеристиками DCB `LRECL=80`.",
    # ZDC105E
    'Comment control characters are "/*" to begin a comment and "*/" to end a comment. These must be paired; one of each. All statements between this pair are treated as a comment. This message indicates that the pairing of these control sequences is not correct.': 'Управляющие символы комментариев: "/*" для начала и "*/" для конца комментария. Они должны быть парными. Все операторы между ними считаются комментарием. Это сообщение указывает, что сопряжение данных управляющих последовательностей некорректно.',
    "Correct the comment pairing error and re-execute the zDC.": "Исправьте ошибку сопряжения комментариев и повторно запустите zDC.",
    # ZDC106E
    "The `SYSIN` keyword shown in the message text is not one of the valid keywords.": "Ключевое слово `SYSIN`, отображённое в тексте сообщения, не является допустимым.",
    "Correct the keyword in the `SYSIN` data set and re-execute the zDC.": "Исправьте ключевое слово в наборе данных `SYSIN` и повторно запустите zDC.",
    # ZDC107E
    "The `SUBSYSTEM_ID` parameter names a unique 4-character name for this zDC instance. This name must not be duplicated on this LPAR, and must NOT be defined in the `SYS1.PARMLIB IEFSSNxx` member.": "Параметр `SUBSYSTEM_ID` задаёт уникальное 4-символьное имя для данного экземпляра zDC. Это имя не должно дублироваться на данном LPAR и не должно быть определено в элементе `SYS1.PARMLIB IEFSSNxx`.",
    "Add the SUBSYSTEM\\_ID parameter to the `//SYSIN` data set and re-execute the zDC. This 4-character name must be unique across all subsystems running on this LPAR but may be the same on different LPARs. You may name all your zDC subsystems with the same name on each LPA. But on any one LPAR this name must be unique. Do not define this name in the `IEFSSNxx SYS1.PARMLIB` member.": "Добавьте параметр SUBSYSTEM\\_ID в набор данных `//SYSIN` и повторно запустите zDC. Это 4-символьное имя должно быть уникальным среди всех подсистем, работающих на данном LPAR, но может совпадать на разных LPAR. Все подсистемы zDC на каждом LPA можно называть одним именем, однако на любом одном LPAR оно должно быть уникальным. Не определяйте это имя в элементе `IEFSSNxx SYS1.PARMLIB`.",
    # ZDC110E
    "The `NAME` parameter is required and must specify a name for this zDC that is meaningful to personnel in your enterprise who may see messages from this zDC. The value you specify in the `NAME` parameter is not used for any purpose except to uniquely identify this instance of the zDC.": "Параметр `NAME` обязателен и должен содержать имя данного zDC, понятное сотрудникам предприятия, которые могут видеть сообщения от него. Значение параметра `NAME` используется только для уникальной идентификации данного экземпляра zDC.",
    "Add the `NAME` parameter and re-execute the zDC.": "Добавьте параметр `NAME` и повторно запустите zDC.",
    # ZDC116E
    "You have specified `ARM(YES)` but have not specified the name to be used for Automatic Restart Management. This name must be from 1 to 16 bytes long. zDC registers with the z/OS automatic restart management and is then eligible for this facility. This name can consist of uppercase letters, numbers, and the following special characters: underscore (`_`), dollar sign (`$`), pound sign(`#`), or At sign (`@`). The first character cannot be numeric.": "Указан параметр `ARM(YES)`, но не задано имя для Automatic Restart Management. Это имя должно иметь длину от 1 до 16 байт. zDC регистрируется в системе автоматического перезапуска z/OS и становится участником этого механизма. Имя может состоять из букв верхнего регистра, цифр и специальных символов: подчёркивания (`_`), знака доллара (`$`), знака фунта (`#`) или символа @. Первый символ не может быть цифрой.",
    "See *z/OS V1Rn.0 MVS Setting Up a Sysplex* for a complete discussion of how an installation invokes this facility. When all of the steps outlined in this manual have been followed, then add the `ARM_NAME` parameter and re-execute the zDC. In the meantime, specify `ARM(NO)` or omit the parameter.": "Полное описание активации этого механизма см. в *z/OS V1Rn.0 MVS Setting Up a Sysplex*. После выполнения всех шагов, описанных в этом руководстве, добавьте параметр `ARM_NAME` и повторно запустите zDC. Пока что укажите `ARM(NO)` или пропустите параметр.",
    # ZDC121E
    "The SUBSYSTEM\\_ID parameter has been specified but is not valid. The value for this parameter must be 4 bytes long consisting only of uppercase letters and numbers and dollar sign (`$`), pound sign(`#`), or At sign (`@`). The first character must be a letter.": "Параметр SUBSYSTEM_ID указан, но недопустим. Его значение должно содержать ровно 4 байта, состоящих только из букв верхнего регистра, цифр, знака доллара (`$`), знака фунта (`#`) или символа @. Первый символ должен быть буквой.",
    "Correct the `SUBSYSTEM_ID` parameter and re-execute the zDC.": "Исправьте параметр `SUBSYSTEM_ID` и повторно запустите zDC.",
    # ZDC122E
    "The `DISPLAY_NAME` parameter has been specified, but is not valid. The value for this parameter must be from 1 to 40 bytes long. Any displayable characters are valid.": "Параметр `DISPLAY_NAME` указан, но недопустим. Его значение должно иметь длину от 1 до 40 байт. Допустимы любые отображаемые символы.",
    "Correct the `DISPLAY_NAME` parameter and re-execute the zDC.": "Исправьте параметр `DISPLAY_NAME` и повторно запустите zDC.",
    # ZDC123E
    "The `DEFAULT` parameter has been specified, but is not valid. Only two values are allowed: `YES` or `NO`. Only one zDC instance in a given LPAR may specify that it is the default; all others must specify NO.": "Параметр `DEFAULT` указан, но недопустим. Допускаются только два значения: `YES` или `NO`. Только один экземпляр zDC на данном LPAR может указывать, что он является подсистемой по умолчанию; все остальные должны указывать NO.",
    "Correct the `DEFAULT` parameter and re-execute the zDC.": "Исправьте параметр `DEFAULT` и повторно запустите zDC.",
    # ZDC125E
    "The EVENT\\_WAIT parameter can only specify `YES` or `NO`. If this parameter is omitted `YES` is assumed. An EVENT\\_WAIT specified as `YES` or allowed to default to `YES` indicates that when events are processed, programs are kept from continuing their execution until the event has been successfully processed by the zDC address space. In most cases this is the desirable option. If it is determined that too much time is lost while zDC is processing the event, then specify `NO` to this parameter. The liability is that events may be lost if zDC terminates abnormally.": "Параметр EVENT\\_WAIT может принимать только значения `YES` или `NO`. Если параметр опущен, принимается значение `YES`. Значение `YES` означает, что при обработке событий программы ждут успешной обработки события адресным пространством zDC перед продолжением выполнения. В большинстве случаев это предпочтительный вариант. Если обработка события в zDC занимает слишком много времени, укажите значение `NO`. При этом существует риск потери событий при аварийном завершении zDC.",
    "Correct the `EVENT_WAIT` parameter and re-execute the zDC.": "Исправьте параметр `EVENT_WAIT` и повторно запустите zDC.",
    # ZDC126E
    "The `TCPIP_USERID` parameter must specify a 1- to 8-character valid user ID. You may omit this parameter in which case the user ID under which zDC was submitted is used.": "Параметр `TCPIP_USERID` должен содержать допустимый идентификатор пользователя длиной от 1 до 8 символов. Параметр можно не указывать: тогда будет использован идентификатор пользователя, от имени которого отправлен zDC.",
    "Either correct the user ID parameter or omit it entirely. re-execute the zDC.": "Исправьте параметр идентификатора пользователя или полностью опустите его. Повторно запустите zDC.",
    # ZDC127E
    "The `LOG_INITIAL` parameter must specify either `(OPEN)` `(CLOSED)` or `()`. Any other values are invalid. If you omit this parameter or specify `()`, the default is`LOG_INITIAL(CLOSED)`. Specify all the other parameters for logging that are applicable to your SMS environment, and also specify `LOG_INITIAL(CLOSED)`. You can dynamically start logging using the specified parameters if the need arises. With the log in a `CLOSED` state no system resources are consumed.": "Параметр `LOG_INITIAL` должен содержать одно из значений: `(OPEN)`, `(CLOSED)` или `()`. Любые другие значения недопустимы. Если параметр не указан или указано `()`, по умолчанию используется `LOG_INITIAL(CLOSED)`. Укажите все остальные параметры журналирования, применимые к вашей среде SMS, а также задайте `LOG_INITIAL(CLOSED)`. При необходимости можно динамически запустить журналирование с использованием указанных параметров. В состоянии `CLOSED` системные ресурсы не расходуются.",
    "Correct the `LOG_INITIAL` parameter and re-execute the zDC.": "Исправьте параметр `LOG_INITIAL` и повторно запустите zDC.",
    # ZDC128E
    "The `LOG_DSNAME` parameter must specify a 1 to 35- character data set name for the optional logging. Be sure you haven't specified more than 35 characters because `IDCAMS` appends a `.DATA` and a `.INDEX` to this name when the cluster is defined.": "Параметр `LOG_DSNAME` должен содержать имя набора данных для необязательного журналирования длиной от 1 до 35 символов. Убедитесь, что не указано более 35 символов: `IDCAMS` добавляет `.DATA` и `.INDEX` к этому имени при определении кластера.",
    "Correct the `LOG_DSNAME` and re-execute the zDC.": "Исправьте значение `LOG_DSNAME` и повторно запустите zDC.",
    # ZDC130E
    "The `LOG_VOLSER` parameter must specify a 6-character volume serial number for the volume on which the log is to be defined. You must specify this parameter only if your SMS environment dictates it, else you may omit this parameter and take your system defaults.": "Параметр `LOG_VOLSER` должен содержать 6-символьный серийный номер тома, на котором должен быть определён журнал. Этот параметр следует указывать только в том случае, если это требуется средой SMS; в противном случае его можно опустить и использовать системные значения по умолчанию.",
    "Correct the `LOG_VOLSER` and re-execute the zDC.": "Исправьте значение `LOG_VOLSER` и повторно запустите zDC.",
    # ZDC131E
    "The `LOG_TRKS` parameter must specify a 1 to 8-digit number representing the number of tracks you want defined in the primary and secondary extents of the log data set. The maximum value for this parameter is `65535` and the minimum value is 1.": "Параметр `LOG_TRKS` должен содержать число от 1 до 8 цифр, представляющее количество дорожек в первичных и вторичных экстентах набора данных журнала. Максимальное значение: `65535`, минимальное: 1.",
    "Correct the `LOG_TRKS` and re-execute the zDC.": "Исправьте значение `LOG_TRKS` и повторно запустите zDC.",
    # ZDC132E
    "The `LOG_CYLS` parameter must specify a 1 to 8-digit number representing the number of cylinders you want defined in the primary and secondary extents of the log data set. The maximum value for this parameter is `65535` and the minimum value is 1.": "Параметр `LOG_CYLS` должен содержать число от 1 до 8 цифр, представляющее количество цилиндров в первичных и вторичных экстентах набора данных журнала. Максимальное значение: `65535`, минимальное: 1.",
    "Correct the `LOG_CYLS` and re-execute the zDC.": "Исправьте значение `LOG_CYLS` и повторно запустите zDC.",
    # ZDC133E
    "The `LOG_MGMTCLASS` parameter must specify a 1- to 8-character name for the management class SMS parameter that is defined in your installation for the log data set.": "Параметр `LOG_MGMTCLASS` должен содержать имя длиной от 1 до 8 символов для класса управления SMS, определённого в вашей установке для набора данных журнала.",
    "Correct the `LOG_MGMTCLASS` parameter and re-execute the zDC.": "Исправьте параметр `LOG_MGMTCLASS` и повторно запустите zDC.",
    # ZDC134E
    "The `LOG_DATACLASS` parameter must specify a 1- to 8-character name for the data class SMS parameter that is defined in your installation for the log data set.": "Параметр `LOG_DATACLASS` должен содержать имя длиной от 1 до 8 символов для класса данных SMS, определённого в вашей установке для набора данных журнала.",
    # ZDC135E
    "The `LOG_STORCLASS` parameter must specify a 1- to 8-character name for the storage class SMS parameter that is defined in your installation for the log data set.": "Параметр `LOG_STORCLASS` должен содержать имя длиной от 1 до 8 символов для класса хранения SMS, определённого в вашей установке для набора данных журнала.",
    "Correct the `LOG_STORCLASS` parameter and re-execute the zDC.": "Исправьте параметр `LOG_STORCLASS` и повторно запустите zDC.",
    # ZDC155E
    "The `ARM` parameter must specify either `ARM(YES)`, if you want Automatic Restart Management to restart this zDC in case of abnormal termination, or `ARM(NO)`, if you do not want the zDC restarted. Initially you should specify `ARM(NO)` until you have assured yourself that the zDC is working correctly under normal circumstances. When this is the case you can request `ARM` support.": "Параметр `ARM` должен содержать значение `ARM(YES)`, если требуется, чтобы Automatic Restart Management перезапускал данный zDC при аварийном завершении, или `ARM(NO)`, если перезапуск не нужен. Изначально следует указать `ARM(NO)` до тех пор, пока не будет подтверждено корректное функционирование zDC в обычных условиях. После этого можно запросить поддержку `ARM`.",
    "Correct the `ARM` parameter and re-execute the zDC": "Исправьте параметр `ARM` и повторно запустите zDC.",
    # ZDC156E
    "The `ARM_ELEMENT_NAME` parameter specifies a 1- to 16- character name to be used by z/OS in identifying this program to the Automatic Restart Management system. Only letters and numbers and the special characters `_`, `$`, `#` and `@` are valid. In addition, the first byte must not be numeric.": "Параметр `ARM_ELEMENT_NAME` задаёт имя длиной от 1 до 16 символов, используемое z/OS для идентификации данной программы в системе Automatic Restart Management. Допустимы только буквы, цифры и специальные символы `_`, `$`, `#` и `@`. При этом первый байт не должен быть цифрой.",
    "Correct the `ARM_ELEMENT_NAME` parameter and re-execute the zDC.": "Исправьте параметр `ARM_ELEMENT_NAME` и повторно запустите zDC.",
    # ZDC185E
    "The `PROTECT` parameter must specify `PROTECT(YES)` if pages in extended common storage are to be protected from inadvertent alteration by other programs running in the `LPAR` or `PROTECT(NO)` if this protection is not to occur. If this parameter is omitted then no protection exists. Any program running in key 0 can alter this storage.": "Параметр `PROTECT` должен содержать значение `PROTECT(YES)`, если страницы расширенной общей памяти должны быть защищены от непреднамеренного изменения другими программами, работающими в `LPAR`, или `PROTECT(NO)`, если такая защита не требуется. Если параметр опущен, защита отсутствует: любая программа, работающая в ключе 0, может изменить эту память.",
    "Correct the `PROTECT` parameter and re-execute the zDC.": "Исправьте параметр `PROTECT` и повторно запустите zDC.",
    # ZDC187E
    "The `DEFAULT` parameter is required as either `DEFAULT(YES)` or `DEFAULT(NO)`. Only one zDC subsystem in the LPAR can specify `DEFAULT(YES)`. All others must specify `DEFAULT(NO)`.": "Параметр `DEFAULT` обязателен: требуется указать либо `DEFAULT(YES)`, либо `DEFAULT(NO)`. Только одна подсистема zDC на LPAR может указывать `DEFAULT(YES)`. Все остальные должны указывать `DEFAULT(NO)`.",
    "Add the `DEFAULT` parameter and re-execute the zDC.": "Добавьте параметр `DEFAULT` и повторно запустите zDC.",
    # ZDC189E
    "The `OPERATING_SYSTEM` parameter should never be specified at a customer parameter. Its use is only for emulating releases of z/OS earlier than the current one.": "Параметр `OPERATING_SYSTEM` не должен указываться в клиентских параметрах. Он предназначен исключительно для эмуляции выпусков z/OS, предшествующих текущему.",
    "zDC ends.": "zDC завершает работу.",
    "Remove this parameter from the `SYSIN` data set.": "Удалите этот параметр из набора данных `SYSIN`.",
    # ZDC193E
    "The TCPIP\\_INTF parameter specifies the TCPIP interface name or IPV4 address. It has a maximum length of 16 characters.": "Параметр TCPIP_INTF задаёт имя интерфейса TCPIP или адрес IPv4. Максимальная длина: 16 символов.",
    "Correct the TCPIP\\_INTF parameter and resubmit zDC.": "Исправьте параметр TCPIP\\_INTF и повторно отправьте zDC.",
    # ZDC194E
    "The `zIIP_ENABLE` parameter can specify `YES` or `NO`. If `zIIP_ENABLE(YES)` is specified, then the SRB under which all XML creation and TCP/IP SOCKET(SEND) routines run is zIIP enabled. This SRB is not run on your zIIP if set to NO.": "Параметр `zIIP_ENABLE` может принимать значения `YES` или `NO`. Если указано `zIIP_ENABLE(YES)`, SRB, в котором выполняются все подпрограммы создания XML и TCP/IP SOCKET(SEND), включается с поддержкой zIIP. При значении NO этот SRB не выполняется на zIIP.",
    "Correct the `zIIP_ENABLE` parameter and resubmit zDC.": "Исправьте параметр `zIIP_ENABLE` и повторно отправьте zDC.",
    # ZDC196E
    "The `DTMSG_QSIZE` parameter specifies a Data Space size in Kilobyte. The default is 1024 (1024K). This Data Space is used to queue messages from the CICS code module of OneAgent to the zLocal. The minimum value is 8 and the maximum is 262144K (256Megabytes).": "Параметр `DTMSG_QSIZE` задаёт размер пространства данных в килобайтах. По умолчанию: 1024 (1024 КБ). Это пространство данных используется для постановки в очередь сообщений от кодового модуля CICS OneAgent к zLocal. Минимальное значение: 8, максимальное: 262 144 КБ (256 МБ).",
    "Specify a value in the range given.": "Укажите значение в допустимом диапазоне.",
    # ZDC197E
    "The `DTMSG_SMOSIZE` parameter specifies a 64-bit SMO size in MB. The default is 1 MB. This 64-bit SMO is used to queue messages from the CICS code module to the zLocal. The minimum value is 1 and the maximum is 256 MB. (256 Megabytes).": "Параметр `DTMSG_SMOSIZE` задаёт 64-битный размер SMO в МБ. По умолчанию: 1 МБ. Этот 64-битный SMO используется для постановки в очередь сообщений от кодового модуля CICS к zLocal. Минимальное значение: 1, максимальное: 256 МБ.",
    "Choose a correct value for `SMOSIZE` and then resubmit zDC.": "Выберите допустимое значение для `SMOSIZE` и повторно отправьте zDC.",
    # ZDC198E
    "The `DT_UMASK` parameter specifies user file-creation mask. The default is 0022(octal) and corresponds to rwxr-xr-x permission for new files. Error is generated if the parameter is over 3 characters, or contain non-octal characters (o:7).": "Параметр `DT_UMASK` задаёт маску создания файлов пользователем. По умолчанию: 0022 (восьмеричный), что соответствует разрешению rwxr-xr-x для новых файлов. Ошибка генерируется, если параметр превышает 3 символа или содержит невосьмеричные символы (o:7).",
    "Choose a correct value for `DT_UMASK` and then resubmit zDC.": "Выберите допустимое значение для `DT_UMASK` и повторно отправьте zDC.",
    # ZDC199E
    "The `DTMSG_TBCSIZE` parameter specifies a 64-bit Transaction buffer total size in MB and either a 2K or 4K buffer size. The default is `(1,2)`, which stands for 1MB and 2K buffer. This 64-bit SMO is used to buffer messages related to a transaction before being sent to OneAgent. The minimum value is 1 and the maximum is 256 MB (256Megabytes).": "Параметр `DTMSG_TBCSIZE` задаёт общий 64-битный размер буфера транзакций в МБ и размер буфера: 2 КБ или 4 КБ. По умолчанию: `(1,2)` (1 МБ и буфер 2 КБ). Этот 64-битный SMO используется для буферизации сообщений, связанных с транзакцией, перед отправкой в OneAgent. Минимальное значение: 1, максимальное: 256 МБ.",
    "Choose a correct value for `TBCSIZE` and then resubmit zDC.": "Выберите допустимое значение для `TBCSIZE` и повторно отправьте zDC.",
    # ZDC200I
    "The `DTMSG_QSIZE` parameter specified DataSpace size in Kilobytes It is replace by `DTMSG_SMOSIZE(Megabytes)` The parameter has been converted to Megabytes and used to set the SMO size.": "Параметр `DTMSG_QSIZE` задавал размер пространства данных в килобайтах. Он заменён параметром `DTMSG_SMOSIZE(Megabytes)`. Значение параметра преобразовано в мегабайты и использовано для задания размера SMO.",
    "zDC execution continues.": "Выполнение zDC продолжается.",
    "Use `DTMSG_SMOSIZE` in the future.": "В дальнейшем используйте `DTMSG_SMOSIZE`.",
    # ZDC201E
    "`ZDCLOGBUFFERSIZE` specifies a log buffer in kilobytes. It is a SMO memory are areas to buffer the zDC `.log` file. The zDC .log file in the same directory as the ZLocal code module `.log` files. The default is (64) - 64K. The minimum is 16K, the maximum is 10240K =10M.": "`ZDCLOGBUFFERSIZE` задаёт буфер журнала в килобайтах. Это область памяти SMO для буферизации файла `.log` zDC. Файл `.log` zDC находится в том же каталоге, что и файлы `.log` кодового модуля ZLocal. По умолчанию: (64), то есть 64 КБ. Минимум: 16 КБ, максимум: 10 240 КБ (10 МБ).",
    "Correct value for `ZDCLOGBUFFERSIZE` and resubmit.": "Исправьте значение `ZDCLOGBUFFERSIZE` и повторно отправьте.",
    # ZDC202E
    "`ZDCMAXLOGFILESIZE` specifies the log file size limit. It is used to rotate to a new log file when exceeded. The ZDClogfile pattern: `.._ZDCID_PID_.#.log`, for example: `dt_DTV1ZDC4_MEPC_33620088.1.log`. The default is (10240) =10M. The minimum is 10K; the maximum is 1048576K =1G.": "`ZDCMAXLOGFILESIZE` задаёт предельный размер файла журнала. При превышении этого значения выполняется ротация к новому файлу журнала. Шаблон имени файла ZDC: `.._ZDCID_PID_.#.log`, например: `dt_DTV1ZDC4_MEPC_33620088.1.log`. По умолчанию: (10240), то есть 10 МБ. Минимум: 10 КБ, максимум: 1 048 576 КБ (1 ГБ).",
    "Correct value for `ZDCMAXLOGFILESIZE` and resubmit.": "Исправьте значение `ZDCMAXLOGFILESIZE` и повторно отправьте.",
    # ZDC203E
    "`ZDCDISPATCHDELAYWARN` specifies an unexpected dispatch delay threshold in units of .01sec. For example, `ZDCDISPATCHDELAYWARN(100)` specifies 1sec. The default is (25) =.25sec. The minimum non-zero valuse is 10 =.1sec. The maximum is (32000) =320sec. Disable delay checking: `ZDCDISPATCHDELAYWARN(0)`": "`ZDCDISPATCHDELAYWARN` задаёт порог неожиданной задержки диспетчеризации в единицах 0.01 сек. Например, `ZDCDISPATCHDELAYWARN(100)` соответствует 1 сек. По умолчанию: (25), то есть 0.25 сек. Минимальное ненулевое значение: 10 (0.1 сек). Максимальное: (32000) (320 сек). Для отключения проверки задержки: `ZDCDISPATCHDELAYWARN(0)`.",
    "Correct value for `ZDCDISPATCHDELAYWARN` and resubmit.": "Исправьте значение `ZDCDISPATCHDELAYWARN` и повторно отправьте.",
    # ZDC204E
    "`ZDCDISPATCHDELAYRPTM` specifies a minimum report interval for unexpected dispatch delay in minutes. If no exceptions occur, no warning is reported. For example, `ZDCDISPATCHDELAYRPTM(15)` reports delays at most every 15 minutes. The default is (10) =10Minutes The minimum is (1) (not recommended, small) The maximum is (32000) (over 533Hours)": "`ZDCDISPATCHDELAYRPTM` задаёт минимальный интервал отчётности для неожиданных задержек диспетчеризации в минутах. Если исключений нет, предупреждение не выводится. Например, `ZDCDISPATCHDELAYRPTM(15)` сообщает о задержках не чаще одного раза в 15 минут. По умолчанию: (10) (10 минут). Минимум: (1) (не рекомендуется, слишком мало). Максимум: (32000) (более 533 часов).",
    "Correct value for `ZDCDISPATCHDELAYRPTM` and resubmit.": "Исправьте значение `ZDCDISPATCHDELAYRPTM` и повторно отправьте.",
    # ZDC205E
    "The `ZEDC_COMPRESS` parameter may specify a 1- or 2-digit number representing the minimum size for a data block to be eligible for zEDC hardware assisted data compression. Smaller blocks will be sent without compression. A null argument may be specified to enable hardware data compression using the 8K default minimum block size.": "Параметр `ZEDC_COMPRESS` может содержать 1- или 2-значное число, представляющее минимальный размер блока данных для аппаратного сжатия данных с помощью zEDC. Блоки меньшего размера будут отправляться без сжатия. Можно указать пустой аргумент для включения аппаратного сжатия данных с минимальным размером блока 8 КБ по умолчанию.",
    "Correct the ZEDC\\_COMPRESS parameter and re-execute the zDC.": "Исправьте параметр ZEDC\\_COMPRESS и повторно запустите zDC.",
    # ZDC206E
    "The `TCP_BUFFER` parameter specifies a 1- to 4-digit number representing the size of the buffer that is used to pass OneAgent data to TCP/IP.": "Параметр `TCP_BUFFER` содержит 1- до 4-значное число, представляющее размер буфера для передачи данных OneAgent в TCP/IP.",
    "Correct the `TCP_BUFFER` parameter and re-execute the zDC.": "Исправьте параметр `TCP_BUFFER` и повторно запустите zDC.",
    # ZDC207E
    "The minimum compression threshold must be smaller than the size of the TCP/IP buffer.": "Минимальный порог сжатия должен быть меньше размера буфера TCP/IP.",
    "Correct one of the parameters and re-execute the zDC.": "Исправьте один из параметров и повторно запустите zDC.",
    # ZDC208I
    "\\* The minimum interval is 10 seconds. \\* The maximum interval is 600 seconds. Specify a zero value to disable metrics processing.": "Минимальный интервал: 10 секунд. Максимальный интервал: 600 секунд. Укажите нулевое значение для отключения обработки метрик.",
    "Correct the parameter and re-execute the zDC.": "Исправьте параметр и повторно запустите zDC.",
    # ZDC209I
    "\\* The minimum interval is 10 seconds. \\* The maximum interval is 600 (seconds). \\* Specify a zero value to disable AutoDisplay processing.": "Минимальный интервал: 10 секунд. Максимальный интервал: 600 секунд. Укажите нулевое значение для отключения обработки AutoDisplay.",
    # ZDC210I
    "This informational message indicates that the TERMAPI macro was successfully executed to terminate TCP/IP communications.": "Это информационное сообщение указывает, что макрос TERMAPI успешно выполнен для завершения связи TCP/IP.",
    # ZDC211E
    "The `DTMSG_TRANBUFSIZE` parameter specifies a Transaction buffer total size in thousands of buffers and either a 2K or 4K buffer size. The default is `(1,2)`, which stands for 1 thousand 2K buffers. This 64-bit SMO is used to buffer messages related to a transaction before being sent to the zLocal. The minimum value is `(1,2)`, maximum is `(126,4)` or `(248,2)` (512Megabytes).": "Параметр `DTMSG_TRANBUFSIZE` задаёт общий размер буфера транзакций в тысячах буферов и размер буфера: 2 КБ или 4 КБ. По умолчанию: `(1,2)` (1 тысяча буферов по 2 КБ). Этот 64-битный SMO используется для буферизации сообщений, связанных с транзакцией, перед отправкой в zLocal. Минимальное значение: `(1,2)`, максимальное: `(126,4)` или `(248,2)` (512 МБ).",
    "Choose a correct value for `DTMSG_TRANBUFSIZE` and resubmit.": "Выберите допустимое значение для `DTMSG_TRANBUFSIZE` и повторно отправьте.",
    # ZDC212E
    "A zRemote code module parameter is required. The zRemote code module properties such as host and port are not specified in the `DTAGTCMD` parameter.": "Требуется параметр кодового модуля zRemote. Свойства кодового модуля zRemote (хост и порт) не указаны в параметре `DTAGTCMD`.",
    "zDC is terminated.": "zDC завершает работу.",
    "Add `zremote=` to `DTAGTCMD` resubmit zDC.": "Добавьте `zremote=` в `DTAGTCMD` и повторно отправьте zDC.",
    # ZDC213W
    "The TCP\\_BUFFER parameter must be in range from 8k to 256k. If less than 8k is specified, 8k is used. If more than 256k is specified, 256k is used.": "Параметр TCP_BUFFER должен находиться в диапазоне от 8 КБ до 256 КБ. Если указано менее 8 КБ, используется 8 КБ. Если указано более 256 КБ, используется 256 КБ.",
    "Correct the TCP\\_BUFFER parameter for next ZDC execution.": "Исправьте параметр TCP\\_BUFFER перед следующим запуском ZDC.",
    # ZDC215I
    "This informational message indicates that termination processing has started for this zDC.": "Это информационное сообщение указывает, что для данного zDC начата обработка завершения.",
    "Termination processing continues.": "Обработка завершения продолжается.",
    # ZDC217I
    "This informational message is followed by messages that show the number of bytes of storage allocated in each of the designated areas. These numbers may only be approximate as dynamic storage areas are not included in them.": "За этим информационным сообщением следуют сообщения, показывающие количество байт памяти, выделенных в каждой из указанных областей. Значения могут быть приблизительными, так как динамические области памяти в них не учитываются.",
    # ZDC218I
    "The number of bytes of private zDC storage that is allocated long term is shown in this message. This number may only be approximate as dynamic storage areas are not included. Storage allocated both over and under the 16M line are included in this number.": "В этом сообщении отображено количество байт частной памяти zDC, выделенной на длительный срок. Значение может быть приблизительным, так как динамические области памяти не учитываются. В это число включена память, выделенная как выше, так и ниже границы 16 МБ.",
    # ZDC219I
    "The number of bytes of subpool 241 (pageable common) storage that has been allocated for the duration of the zDC execution.": "Количество байт памяти субпула 241 (страничная общая память), выделенной на время выполнения zDC.",
    # ZDC220I
    "The number of bytes of subpool 245 (fixed common) storage that has been allocated for the duration of the zDC execution.": "Количество байт памяти субпула 245 (фиксированная общая память), выделенной на время выполнения zDC.",
    # ZDC221I
    "The number of pages in subpool 241 that have had the PGSER PROTECT macro issued against them. This message displays only if you have specified `PROTECT(YES)` in the SYSIN parameter data set.": "Количество страниц субпула 241, для которых был выдан макрос PGSER PROTECT. Это сообщение отображается только при указании `PROTECT(YES)` в наборе данных параметров SYSIN.",
    # ZDC302E
    "Validation routines invoked to ensure that each message to the zLocal is valid has detected an error in the data.": "Подпрограммы проверки, вызываемые для обеспечения корректности каждого сообщения к zLocal, обнаружили ошибку в данных.",
    "If logging is active, the event is logged. This message is written to the user's JOBLOG and the event is discarded.": "Если журналирование активно, событие записывается в журнал. Это сообщение записывается в JOBLOG пользователя, а событие отбрасывается.",
    # ZDC666W
    "This informational message warns that the zDC might be contenting with other work for access to the processors. Up to 6 Job names are shown.": "Это информационное сообщение предупреждает, что zDC может конкурировать с другими заданиями за доступ к процессорам. Отображается до 6 имён заданий.",
    "Processing continues. Check with the system performance group about adjusting the zDC priority.": "Обработка продолжается. Уточните у группы производительности системы необходимость корректировки приоритета zDC.",
    "None.": "Нет.",
    # ZDC667E
    "This error message warns that the zDC has not seen any SMF Type 70 metric records in the last hour (approximately). Check SMFPRMxx to ensure exits SYS.IEFU86 and SUBSYS.IEFU86 process TYPE 70 records.": "Это сообщение об ошибке предупреждает, что zDC не получал записей метрик SMF типа 70 в течение последнего часа (приблизительно). Проверьте SMFPRMxx, чтобы убедиться, что точки выхода SYS.IEFU86 и SUBSYS.IEFU86 обрабатывают записи TYPE 70.",
    # ZDC668W
    "This error message warns that the zDC has not seen Db2 SMF Type 100/101 records in the last hour (approximately). Check SMFPRMxx to ensure exits SYS.IEFU86 and SUBSYS.IEFU86 process TYPE 70 records.": "Это сообщение об ошибке предупреждает, что zDC не получал записей Db2 SMF типа 100/101 в течение последнего часа (приблизительно). Проверьте SMFPRMxx, чтобы убедиться, что точки выхода SYS.IEFU86 и SUBSYS.IEFU86 обрабатывают записи TYPE 70.",
    # ZDC669E
    "This error message notifies the operator that the zDC has encountered an S202 abend.": "Это сообщение об ошибке уведомляет оператора о том, что zDC столкнулся с аварийным завершением S202.",
    "zDC terminates": "zDC завершает работу",
    "Restart zDC.": "Перезапустите zDC.",
    # ZDC8XXW
    "Generally, these are internal diagnostic messages issued when the `DTLOGLEVEL` 2 or less (fine). They may be requested by Dynatrace software support to diagnose an issue.": "Как правило, это внутренние диагностические сообщения, выдаваемые при `DTLOGLEVEL` 2 или ниже (fine). Они могут запрашиваться службой поддержки программного обеспечения Dynatrace для диагностики проблем.",
    # ZDC950E
    "The parameters `DTPIPEPATH`, `DTCHDIR`, `DTAGTCMD`, or `DTLOG` are invalid. See comments in the supplied sample config member for a description of these parameters.": "Параметры `DTPIPEPATH`, `DTCHDIR`, `DTAGTCMD` или `DTLOG` недопустимы. Описание этих параметров см. в комментариях предоставленного образца элемента конфигурации.",
    # ZDC951I
    "There is a limit on how frequently the internal tables that contain CICS properties can be updated. The current limit is 30 seconds.": "Существует ограничение на частоту обновления внутренних таблиц, содержащих свойства CICS. Текущее ограничение: 30 секунд.",
    "Informational, processing continues.": "Информационное сообщение, обработка продолжается.",
    "Re-apply the update later.": "Примените обновление позднее.",
    # ZDC952W
    "This message indicates that the queue is filling and you should be aware that, if it reaches 100%, new messages won't be sent to the zLocal, possibly causing distribute trace corruption. This message first displays when the queue reaches 70% and re-displays at five percent increments. When utilization drops below 70%, this message no longer displays. Note that this message appears on the system console as well as in the `SYSPRINT` data set.": "Это сообщение указывает, что очередь заполняется. При достижении 100% новые сообщения не будут отправляться в zLocal, что может привести к повреждению распределённой трассировки. Сообщение впервые отображается при заполнении очереди на 70% и повторяется с шагом 5%. Когда уровень заполнения опускается ниже 70%, сообщение больше не отображается. Оно выводится как на системной консоли, так и в наборе данных `SYSPRINT`.",
    "Monitor these messages carefully. \\* If the **{Buffer–Type};** is `Trans Buffer Que`, consider increasing zDC parameter: `DTMSG_TRANBUFSIZE()`. \\* If the **{Buffer–Type};** is `SMO Buffer Space`, consider increasing zDC parameter: `DTMSG_SMOSIZE()`.": "Внимательно следите за этими сообщениями. Если **{Buffer–Type}** имеет значение `Trans Buffer Que`, рассмотрите увеличение параметра zDC `DTMSG_TRANBUFSIZE()`. Если **{Buffer–Type}** имеет значение `SMO Buffer Space`, рассмотрите увеличение параметра zDC `DTMSG_SMOSIZE()`.",
    # ZDC953I
    "ZIIP enablement requires remote agent option.": "Для включения ZIIP требуется параметр удалённого агента.",
    "ZIIP enablement requires both the zremote= in the DTABGCMT command line and ZIIP\\_ENABLE(YES) in the zDC SYSIN parameters.": "Для включения ZIIP требуется наличие `zremote=` в командной строке DTABGCMT и `ZIIP\\_ENABLE(YES)` в параметрах SYSIN zDC.",
    # ZDC954W
    "Dynatrace parameter `SYSLOG` is invalid. Only `CONNECTSTATUS` or `()` to disable the option are allowed.": "Параметр Dynatrace `SYSLOG` недопустим. Допускаются только `CONNECTSTATUS` или `()` для отключения параметра.",
    "Remove the parameter or code allowed values.": "Удалите параметр или укажите допустимые значения.",
    # ZDC955L
    "zLocal code module has connected though the zRemote code module to the Dynatrace server.": "Кодовый модуль zLocal подключился к серверу Dynatrace через кодовый модуль zRemote.",
    # ZDC956E
    "zLocal code module has disconnected from the Dynatrace server.": "Кодовый модуль zLocal отключился от сервера Dynatrace.",
    "If this is not planned, investigate the outage.": "Если отключение не запланировано, изучите причину сбоя.",
    # ZDC957I
    "Ignore if expected, otherwise check **Settings** > **Server-side service monitoring** > **Deep monitoring** > **Troubleshooting**.": "Игнорируйте, если ожидается. В противном случае проверьте **Settings** > **Server-side service monitoring** > **Deep monitoring** > **Troubleshooting**.",
    # ZDC958I
    "ZDC has completed sending INIT msg and received an AgentId response.": "ZDC завершил отправку сообщения INIT и получил ответ с AgentId.",
    # ZDC959I
    "ZDC could not find the V4 IP address in the SMO. Verify your zLocal is current.": "ZDC не смог найти IP-адрес V4 в SMO. Убедитесь, что zLocal обновлён до актуальной версии.",
    "Confirm zLocal version is current.": "Убедитесь, что версия zLocal актуальна.",
    # ZDC960L
    "ZDC could not find the V4 IP address using the IBM EZA tcpip macros.": "ZDC не смог найти IP-адрес V4 с помощью макросов IBM EZA tcpip.",
    "Processing continues with zero IP address.": "Обработка продолжается с нулевым IP-адресом.",
    "If this repeats, please contact Dynatrace support.": "Если проблема повторяется, обратитесь в службу поддержки Dynatrace.",
    # ZDC961L
    "Processing continues with TCPIP\\_USE\\_PRIMARY value.": "Обработка продолжается со значением TCPIP\\_USE\\_PRIMARY.",
    # ZDC974E
    "This message is written to the `SYSPRINT` and Oper. Check that the agent file exists and is executable. See `DTAGTCMD()` parameter.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Убедитесь, что файл агента существует и доступен для выполнения. См. параметр `DTAGTCMD()`.",
    "Processing terminates.": "Обработка завершается.",
    "Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.": "Проверьте журнал задания на наличие дополнительных сообщений об ошибках и по возможности устраните их. Если проблема не решена, обратитесь к специалисту по продуктам Dynatrace через чат. Обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении.",
    # ZDC975E
    "This message is written to the SYSPRINT and Oper. Check that the DTAGTCMD parameter references an accessible and executable OneAgent.": "Это сообщение записывается в SYSPRINT и на операторскую консоль. Убедитесь, что параметр DTAGTCMD ссылается на доступный и исполняемый OneAgent.",
    # ZDC976E
    "This message is written to the `SYSPRINT` and Oper. Check that the zDC has read+write access to the `DTCHDIR` directory.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Убедитесь, что zDC имеет доступ на чтение и запись к каталогу `DTCHDIR`.",
    # ZDC977E
    "This message is written to the `SYSPRINT` and Oper. Check that the user ID that is running the zDC is defined to the security product. The userid is either the normally assigned ID, or overriden by the `TCPIP_USERID` parameter.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Убедитесь, что идентификатор пользователя, от имени которого работает zDC, определён в системе безопасности. Идентификатор может быть обычным назначенным или переопределён параметром `TCPIP_USERID`.",
    "Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat within your Dynatrace environment.": "Проверьте журнал задания на наличие дополнительных сообщений об ошибках и по возможности устраните их. Если проблема не решена, обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении Dynatrace.",
    # ZDC978E
    "This message is written to the `SYSPRINT` and Oper. The MVS Name/Token is used for internal processing. The operation failed.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. MVS Name/Token используется для внутренней обработки. Операция завершилась ошибкой.",
    "Processing terminates with a dump.": "Обработка завершается с дампом.",
    # ZDC979E
    "This message is written to the `SYSPRINT` and Oper. The Data Space used to pass messages to the ZDC has not initialized.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Пространство данных, используемое для передачи сообщений в ZDC, не инициализировано.",
    "Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat within your Dynatrace environment.": "Проверьте журнал задания на наличие дополнительных сообщений об ошибках и по возможности устраните их. Если проблема не решена, обратитесь к специалисту по продуктам Dynatrace через чат в вашем окружении Dynatrace.",
    # ZDC980E
    "This message is written to the `SYSPRINT` and Oper. The OMVS kernel is not ready.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Ядро OMVS не готово.",
    "Check why the OMVS address space is not operational. Restart OMVS or delay zDC startup until OMVS is ready.": "Выясните причину неработоспособности адресного пространства OMVS. Перезапустите OMVS или отложите запуск zDC до готовности OMVS.",
    # ZDC981E
    "This message is written to the `SYSPRINT` and Oper. A critical Data Space process has failed.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Критический процесс пространства данных завершился ошибкой.",
    # ZDC983E
    "This message is written to the `SYSPRINT` and Oper. A critical timer wait function has failed.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Критическая функция ожидания таймера завершилась ошибкой.",
    # ZDC984E
    "This message is written to the `SYSPRINT` and Oper. A Unix wait to check zLocal status has failed.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Ожидание Unix для проверки состояния zLocal завершилось ошибкой.",
    # ZDC985E
    "This message is written to the `SYSPRINT` and Oper. A Unix poll for zLocal messages has failed.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Опрос Unix для получения сообщений zLocal завершился ошибкой.",
    # ZDC986E
    "This message is written to the `SYSPRINT` and Oper. A Unix unnamed pipe is needed for zLocal communication.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Для связи с zLocal требуется безымянный канал Unix.",
    # ZDC987E
    "This message is written to the `SYSPRINT` and Oper. A critial internal call function has failed.": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Критическая внутренняя функция вызова завершилась ошибкой.",
    # ZDC989E
    "This message is written to the `SYSPRINT` and Oper. It is intended for internal diagnostic for Dynatrace loglevel:finer(1).": "Это сообщение записывается в `SYSPRINT` и на операторскую консоль. Предназначено для внутренней диагностики при loglevel:finer(1) Dynatrace.",
    "Informational, processing continues.": "Информационное сообщение, обработка продолжается.",
    # ZDC990I
    "This message is written to the `SYSPRINT`. It is intended for internal diagnostic for `loglevel:finest(0)`.": "Это сообщение записывается в `SYSPRINT`. Предназначено для внутренней диагностики при `loglevel:finest(0)`.",
    # ZDC991I
    "This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:finer(1)`.": "Это сообщение записывается в `SYSPRINT`. Предназначено для внутренней диагностики Dynatrace при `loglevel:finer(1)`.",
    # ZDC992I
    "This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:fine(2)`.": "Это сообщение записывается в `SYSPRINT`. Предназначено для внутренней диагностики Dynatrace при `loglevel:fine(2)`.",
    # ZDC993I
    "This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:config(3)`.": "Это сообщение записывается в `SYSPRINT`. Предназначено для внутренней диагностики Dynatrace при `loglevel:config(3)`.",
    # ZDC994I
    "This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:info(4)`": "Это сообщение записывается в `SYSPRINT`. Предназначено для внутренней диагностики Dynatrace при `loglevel:info(4)`.",
    # ZDC995W
    "This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:warn(5)`.": "Это сообщение записывается в `SYSPRINT`. Предназначено для внутренней диагностики Dynatrace при `loglevel:warn(5)`.",
    "If a connection issue, investigate the status of the zRemote code module. Otherwise, informational, processing continues.": "Если это проблема подключения, изучите состояние кодового модуля zRemote. В противном случае: информационное сообщение, обработка продолжается.",
    # ZDC996E
    "This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:severe(6)`.": "Это сообщение записывается в `SYSPRINT`. Предназначено для внутренней диагностики Dynatrace при `loglevel:severe(6)`.",
    # ZDC997I
    "This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:debug(7)`.": "Это сообщение записывается в `SYSPRINT`. Предназначено для внутренней диагностики Dynatrace при `loglevel:debug(7)`.",
    # ZDC998I
    "This message is written to the `SYSPRINT`. It is intended for internal Dynatrace. Dynatrace product experts might ask that system parameters be changed to cause these messages.": "Это сообщение записывается в `SYSPRINT`. Предназначено для внутренних нужд Dynatrace. Специалисты по продуктам Dynatrace могут запросить изменение системных параметров для воспроизведения этих сообщений.",
    # ZDC999I
    "This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic and shouldn't appear under normal operation. Dynatrace product experts might ask that system parameters be changed to cause these messages.": "Это сообщение записывается в `SYSPRINT`. Предназначено для внутренней диагностики Dynatrace и не должно появляться в штатном режиме работы. Специалисты по продуктам Dynatrace могут запросить изменение системных параметров для воспроизведения этих сообщений.",
}

META = {
    "title: z/OS module messages - zDC system messages": "title: Сообщения модулей z/OS - системные сообщения zDC",
    "# z/OS module messages - zDC system messages": "# Сообщения модулей z/OS - системные сообщения zDC",
    "* 63-min read": "* Чтение: 63 мин",
    "* Updated on Feb 10, 2026": "* Обновлено 10 февраля 2026 г.",
    "The zDC is unable to recover and will be shut down automatically. The operator must manually restart": "zDC не может восстановиться и будет автоматически остановлен. Оператор должен вручную перезапустить",
    "the zDC.": "zDC.",
    "## Related topics": "## Связанные темы",
    '* [Install the zDC subsystem](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Set up the z/OS Data Collection subsystem (zDC).")': '* [Установка подсистемы zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Настройка подсистемы сбора данных z/OS (zDC).")',
}

if __name__ == "__main__":
    build_messages(REL, FN, PROSE, META)
    qa_one(REL, FN)
