# -*- coding: utf-8 -*-
"""Builder for customize-zdc.md (L4-IF.71 canon)."""

import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc"
FN = "customize-zdc.md"

# Mojibake note: EN source has mojibake sequences from scraping.
# U+00EF U+00BB U+00BF (BOM)  = ï»¿  (bytes ef bb bf read as latin-1)
# Occurs in two hyperlink texts: "z/OS MODIFY commandï»¿" and "LPARsâ`LPARA`..."
# Keys below use CLEAN English (the engine's _demoji() fixes mojibake before matching).

TRANS = {
    # --- frontmatter ---
    "title: Customize the zDC subsystem": "title: Настройка подсистемы zDC",
    # --- h1 (appears twice) ---
    "# Customize the zDC subsystem": "# Настройка подсистемы zDC",
    # --- metadata ---
    "* 8-min read": "* Чтение: 8 мин",
    "* Published Jul 22, 2016": "* Опубликовано 22 июля 2016 г.",
    # --- intro ---
    "Learn how to customize the zDC subsystem depending on your needs.": "Узнайте, как настроить подсистему zDC в соответствии с вашими задачами.",
    # --- ## z/OS MODIFY commands ---
    "## z/OS MODIFY commands": "## Команды z/OS MODIFY",
    # mojibake in link text "z/OS MODIFY commandï»¿" -> cleaned by _demoji -> "z/OS MODIFY command﻿"
    # Write key as CLEAN English without BOM; _demoji will strip it before norm()
    "The format of the [z/OS MODIFY command](https://www.ibm.com/docs/en/zos/2.5.0?topic=reference-modify-command) is defined as follows:": "Формат [команды z/OS MODIFY](https://www.ibm.com/docs/en/zos/2.5.0?topic=reference-modify-command) определён следующим образом:",
    "The zDC subsystem supports the following z/OS MODIFY commands.": "Подсистема zDC поддерживает следующие команды z/OS MODIFY.",
    "| Command | Description |": "| Команда | Описание |",
    "| --- | --- |": "| --- | --- |",
    "| DISPLAY | Displays Dynatrace subtask processor stats. |": "| DISPLAY | Отображает статистику процессора подзадач Dynatrace. |",
    "| DTM%V | Forces display (ZDC952) of the utilization of the zLocal message queue. |": "| DTM%V | Принудительно отображает (ZDC952) загрузку очереди сообщений zLocal. |",
    "| LOG=? | Queries the log level of the zDC. |": "| LOG=? | Запрашивает уровень логирования zDC. |",
    "| LOG=3 | Sets the log level of the zDC. Log level values range from `0` to `8`. The default value is `3`. Set the value to `4` to suppress informational messages. Values lower than `3` should be only used for diagnostic debugging. |": "| LOG=3 | Задаёт уровень логирования zDC. Допустимые значения: от `0` до `8`. Значение по умолчанию: `3`. Значение `4` подавляет информационные сообщения. Значения ниже `3` следует использовать только при диагностической отладке. |",
    "| START | Starts the zLocal. |": "| START | Запускает zLocal. |",
    "| STDO | Appends previously unreported lines from zLocal `stdo.log` to `SYSPRINT`. |": "| STDO | Добавляет ранее незарегистрированные строки из `stdo.log` zLocal в `SYSPRINT`. |",
    "| STOP | Stops the zLocal. |": "| STOP | Останавливает zLocal. |",
    "| ZLALOGLEVEL=INFO | Sets the log level of the zLocal. Log level values include `FINEST`, `FINER`, `FINE`, `CONFIG`, `INFO`, `WARNING`, `SEVERE`, `DEBUG`, and `NONE`. No default value. |": "| ZLALOGLEVEL=INFO | Задаёт уровень логирования zLocal. Допустимые значения: `FINEST`, `FINER`, `FINE`, `CONFIG`, `INFO`, `WARNING`, `SEVERE`, `DEBUG` и `NONE`. Значение по умолчанию не задано. |",
    "The `DISPLAY` command skips most rows with zero counters if the log level is at or higher than the default level of 3. To list the complete set of counters, you need to increase the log level to 1.": "Команда `DISPLAY` пропускает большинство строк с нулевыми счётчиками, если уровень логирования не ниже значения по умолчанию, равного 3. Для вывода полного набора счётчиков нужно повысить уровень логирования до 1.",
    "A zDC sample output from `DISPLAY` with `LOG=1`.": "Пример вывода zDC от команды `DISPLAY` при `LOG=1`.",
    "Rows that end with an exclamation mark (`!`) should have zero counts.": "Строки, заканчивающиеся восклицательным знаком (`!`), должны иметь нулевые значения счётчиков.",
    # --- ## Multiple TCP/IP stacks on a LPAR ---
    "## Multiple TCP/IP stacks on a LPAR": "## Несколько стеков TCP/IP на LPAR",
    "An LPAR with multiple TCP/IP stacks requires an additional configuration step in the `ZDCMEPC` started task PROC from `SZDTSAMP`.": "LPAR с несколькими стеками TCP/IP требует дополнительного шага настройки в процедуре PROC запускаемой задачи `ZDCMEPC` из `SZDTSAMP`.",
    "The `BPXTCAFF` program associates a specific TCP/IP stack with the current address space.": "Программа `BPXTCAFF` связывает определённый стек TCP/IP с текущим адресным пространством.",
    "The `PARM` value is the job name that starts the desired TCP/IP stack.": "Значение `PARM`: имя задания, запускающего нужный стек TCP/IP.",
    # --- ## Multiple zDC/zRemote pairs on an LPAR ---
    "## Multiple zDC/zRemote pairs on an LPAR": "## Несколько пар zDC/zRemote на LPAR",
    "A zDC/zRemote pair connects the modules on a LPAR to a single Dynatrace environment. For example, it may be necessary to configure multiple zDC/zRemote pairs on an LPAR": "Пара zDC/zRemote соединяет модули на LPAR с одним окружением Dynatrace. В ряде случаев может потребоваться настроить несколько пар zDC/zRemote на LPAR:",
    "* When you want to maintain different application groups in different Dynatrace environments.": "* если нужно поддерживать различные группы приложений в разных окружениях Dynatrace;",
    "* When you want to optimize your monitoring performance with high transaction volumes.": "* если нужно оптимизировать производительность мониторинга при высоких объёмах транзакций.",
    # --- ### Install an additional zDC/zRemote pair ---
    "### Install an additional zDC/zRemote pair": "### Установка дополнительной пары zDC/zRemote",
    '1. Install an additional [zRemote module](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#installation "Prepare and install the zRemote for z/OS monitoring.").': '1. Установите дополнительный [модуль zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#installation "Подготовьте и установите zRemote для мониторинга z/OS.").',
    "2. On your LPAR, copy the current JCL SYSIN member `ZDCSYSIN` to another name (for example, `ZDCSYSI2`).": "2. На своём LPAR скопируйте текущий элемент JCL SYSIN `ZDCSYSIN` под другим именем (например, `ZDCSYSI2`).",
    '3. Edit the new JCL SYSIN member by changing the following [SYSIN parameters](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Set up the z/OS Data Collection subsystem (zDC)."):': '3. Отредактируйте новый элемент JCL SYSIN, изменив следующие [параметры SYSIN](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Настройка подсистемы сбора данных z/OS (zDC).").',
    "* Point `zremote=<ipaddress>[:port]` to the IP address and port of the new zRemote module.": "* Укажите в `zremote=<ipaddress>[:port]` IP-адрес и порт нового модуля zRemote.",
    "* Change `name=<zlocal_<lpar>>` to a new zLocal name.": "* Измените `name=<zlocal_<lpar>>` на новое имя zLocal.",
    "* Change `<subsystem>` to a new name.": "* Измените `<subsystem>` на новое имя.",
    "* Change `DEFAULT(YES)` to `DEFAULT(NO)`. The first zDC is designated as the default. Only one zDC per LPAR can specify `DEFAULT(YES)`. Additional zDCs fail to initialize unless they specify `DEFAULT(NO)`.": "* Измените `DEFAULT(YES)` на `DEFAULT(NO)`. Первый zDC назначается основным. Только один zDC на LPAR может задавать `DEFAULT(YES)`. Дополнительные zDC не инициализируются, если не задано `DEFAULT(NO)`.",
    "4. Make a copy of the current started task PROC and change the JCL SYSIN member to point to the new SYSIN member.": "4. Создайте копию текущей процедуры PROC запускаемой задачи и измените элемент JCL SYSIN так, чтобы он ссылался на новый элемент SYSIN.",
    "5. Start the new zDC and check if it connects to the new zRemote.": "5. Запустите новый zDC и проверьте, установлено ли соединение с новым zRemote.",
    # --- ### Connect the modules to the new zDC ---
    "### Connect the modules to the new zDC": "### Подключение модулей к новому zDC",
    "CICS module": "Модуль CICS",
    "IMS module": "Модуль IMS",
    "z/OS Java module": "Модуль z/OS Java",
    "Create an `INITPARM` parameter override in the CICS system initialization to target the new zDC subsystem.": "Создайте переопределение параметра `INITPARM` при инициализации системы CICS для направления запросов в новую подсистему zDC.",
    'See [Connect CICS module to a zDC subsystem](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics#connect-cics-zdc "Install the Dynatrace CICS module.").': 'См. раздел [Подключение модуля CICS к подсистеме zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics#connect-cics-zdc "Установка модуля Dynatrace CICS.").',
    "Change the `ZDC=` parameter in the injection utility parameters to target the new zDC subsystem.": "Измените параметр `ZDC=` в параметрах служебной программы инжекции, чтобы направить запросы в новую подсистему zDC.",
    "See injection utility of [IMS control region](#install-ims-control-region).": "См. служебную программу инжекции раздела [Управляющий регион IMS](#install-ims-control-region).",
    "Change the `ZdcName` parameter in the `dtconfig.json` file to target the new zDC subsystem.": "Измените параметр `ZdcName` в файле `dtconfig.json` для направления запросов в новую подсистему zDC.",
    'See the [Download](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Set up Java monitoring on z/OS using the Java module.") procedure of the z/OS Java module.': 'См. процедуру [Загрузка](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Настройка мониторинга Java на z/OS с помощью модуля Java.") модуля z/OS Java.',
    # --- ## Failover processing for zDC/zRemote ---
    "## Failover processing for zDC/zRemote": "## Обработка отказоустойчивости для zDC/zRemote",
    "This is not load balancing.": "Это не балансировка нагрузки.",
    "The zDC subsystem can automatically switch to the next active zRemote module if a problem occurs with the primary zRemote.": "Подсистема zDC может автоматически переключиться на следующий активный модуль zRemote, если с основным zRemote возникает проблема.",
    "zLocal version 1.1.0+ zRemote module version 1.261+ Once failover happens, and the secondary zRemote is connected, the zDC checks every 5 minutes to see if the primary zRemote is available. If not, the secondary zRemote connection remains intact, and the cycle starts anew. If the primary zRemote is available, the secondary zRemote is disconnected, and an immediate reconnect is attempted to the primary zRemote.": "zLocal версии 1.1.0+ и модуль zRemote версии 1.261+. После переключения при отказе и подключения резервного zRemote zDC каждые 5 минут проверяет доступность основного zRemote. Если основной zRemote недоступен, соединение с резервным zRemote сохраняется и цикл начинается заново. Если основной zRemote доступен, резервный zRemote отключается и немедленно предпринимается попытка повторного подключения к основному zRemote.",
    "zLocal versions older than 1.1.0": "zLocal версий ниже 1.1.0",
    "Once failover happens, the ZDC remains connected to this next zRemote until this connection is broken. At that time, if the original zRemote is back online, a connection attempt will be made to it from the zDC. If the zDC is restarted, the original zRemote will be the initial connect attempt.": "После переключения при отказе zDC остаётся подключённым к следующему zRemote до разрыва этого соединения. Если в этот момент исходный zRemote снова окажется онлайн, zDC попытается к нему подключиться. При перезапуске zDC исходный zRemote является первым кандидатом для подключения.",
    "To use this behavior also for newer zLocal versions, set `zlaDisablePrimaryReconnect=true` in the `DTAGTCMD` SYSIN parameter.": "Чтобы применить это поведение и в более новых версиях zLocal, задайте `zlaDisablePrimaryReconnect=true` в параметре SYSIN `DTAGTCMD`.",
    'The list of zRemote addresses used for failover processing is maintained in the JCL SYSIN member `ZDCSYSIN`. Edit it by changing the following [SYSIN parameters](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Set up the z/OS Data Collection subsystem (zDC)."):': 'Список адресов zRemote, используемых при обработке отказоустойчивости, хранится в элементе JCL SYSIN `ZDCSYSIN`. Отредактируйте его, изменив следующие [параметры SYSIN](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Настройка подсистемы сбора данных z/OS (zDC).").',
    "* Set `zremote=<ipaddress>[:port]` to include a list of zRemote addresses.": "* Задайте `zremote=<ipaddress>[:port]` со списком адресов zRemote.",
    "* Set `nobootstrap=true` to disable automatic updates for the zLocal; they're not supported during failover processing.": "* Задайте `nobootstrap=true`, чтобы отключить автоматическое обновление zLocal: оно не поддерживается при обработке отказоустойчивости.",
    "* Set `nobootstrap=true` to disable automatic updates for the zLocal.": "* Задайте `nobootstrap=true`, чтобы отключить автоматическое обновление zLocal.",
    "zLocal error message when attempting to update during failover processing": "Сообщение об ошибке zLocal при попытке обновления в ходе обработки отказоустойчивости",
    # --- ### Update zLocal during failover processing ---
    "### Update zLocal during failover processing": "### Обновление zLocal в ходе обработки отказоустойчивости",
    "To update the zLocal during failover processing": "Порядок обновления zLocal в ходе обработки отказоустойчивости:",
    '1. Edit the JCL SYSIN member `ZDCSYSIN` by changing the following [SYSIN parameters](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Set up the z/OS Data Collection subsystem (zDC)."):': '1. Отредактируйте элемент JCL SYSIN `ZDCSYSIN`, изменив следующие [параметры SYSIN](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Настройка подсистемы сбора данных z/OS (zDC).").',
    "* Set `zremote=<ipaddress>[:port]` to the primary zRemote module.": "* Укажите в `zremote=<ipaddress>[:port]` адрес основного модуля zRemote.",
    "* Set `nobootstrap=false` to enable automatic updates for the zLocal.": "* Задайте `nobootstrap=false`, чтобы включить автоматическое обновление zLocal.",
    "2. Start the zDC. The bootstrapper `dtzagent` downloads the latest zLocal binary `libdtzagent.so` to the `/u/dt/agent/downloads/native/a.b.c.d/zos-s390-64` directory.": "2. Запустите zDC. Загрузчик `dtzagent` скачает последний бинарный файл zLocal `libdtzagent.so` в каталог `/u/dt/agent/downloads/native/a.b.c.d/zos-s390-64`.",
    "3. Copy the zLocal binary `libdtzagent.so` to the `/u/dt/agent/lib64` directory. Now the zDC is ready for failover processing with the latest zLocal binary.": "3. Скопируйте бинарный файл zLocal `libdtzagent.so` в каталог `/u/dt/agent/lib64`. Теперь zDC готов к обработке отказоустойчивости с последним бинарным файлом zLocal.",
    '4. Edit the JCL SYSIN member `ZDCSYSIN` by changing the following [SYSIN parameters](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Set up the z/OS Data Collection subsystem (zDC)."):': '4. Отредактируйте элемент JCL SYSIN `ZDCSYSIN`, изменив следующие [параметры SYSIN](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Настройка подсистемы сбора данных z/OS (zDC).").',
    "5. Restart the zDC.": "5. Перезапустите zDC.",
    # --- ## Terminate the zDC ---
    "## Terminate the zDC": "## Завершение работы zDC",
    "The zDC typically releases system resources (especially common storage) when it terminates due to a shutdown command or abnormal due to a cancel command or a program abend. Recovery (ESTAEX) routines are always in effect to trap abnormal terminations and to free all system resources.": "zDC, как правило, освобождает системные ресурсы (в особенности общую память) при штатном завершении по команде остановки или при аварийном завершении по команде отмены или аварийном завершении программы (ABEND). Подпрограммы восстановления (ESTAEX) всегда активны: они перехватывают аварийные завершения и освобождают все системные ресурсы.",
    "However, there may be a situation where zDC can't be canceled due to a z/OS anomaly or failure, which precludes the functioning of the cancel command. If you want to terminate the zDC, try the commands below in the specified order until the zDC terminates. Go on to step 2 only if step 1 is unsuccessful, go on to step 3 only if step 2 is unsuccessful, and so on.": "Тем не менее возможна ситуация, когда zDC нельзя отменить из-за аномалии или сбоя z/OS, препятствующего выполнению команды отмены. Если необходимо завершить работу zDC, выполняйте приведённые ниже команды в указанном порядке до завершения zDC. Переходите к шагу 2 только при неуспехе шага 1, к шагу 3 только при неуспехе шага 2, и так далее.",
    "To avoid manually cleaning up system resources using the `ZDCDELET` process below, wait a short while between commands to permit dumps to be taken and system resources to be freed.": "Чтобы избежать ручной очистки системных ресурсов с помощью описанной ниже процедуры `ZDCDELET`, делайте небольшую паузу между командами, чтобы успели создаться дампы и освободиться системные ресурсы.",
    "1. Issue the `STOP jobname` command.": "1. Выполните команду `STOP jobname`.",
    "2. Issue the `MODIFY jobname,SHUTDOWN IMMED` command.": "2. Выполните команду `MODIFY jobname,SHUTDOWN IMMED`.",
    "3. Issue the `CANCEL jobname` command.": "3. Выполните команду `CANCEL jobname`.",
    "4. Issue the `FORCE jobname` command.": "4. Выполните команду `FORCE jobname`.",
    "Attempt to restart the zDC. If the restart is successful, you can continue to run this job. If the restart is not successful and zDC indicates that it can't continue, you can execute the emergency zDC cleanup program named `ZDCDELET`.": "Попытайтесь перезапустить zDC. При успешном перезапуске задание можно продолжать выполнять. При неуспешном перезапуске, если zDC сообщает о невозможности продолжения работы, запустите аварийную программу очистки zDC с именем `ZDCDELET`.",
    "`ZDCDELET` is a stand-alone job that attempts to terminate a specified zDC job and release all system resources held by a zDC process. The JCL to execute `ZDCDELET` is shown below:": "`ZDCDELET`: отдельная задача, которая пытается завершить указанную задачу zDC и освободить все системные ресурсы, удерживаемые процессом zDC. JCL для выполнения `ZDCDELET` представлен ниже.",
    "The `PARM=` on the `EXEC` statement must specify the 4-character subsystem name of the zDC process you want to terminate.": "В операторе `EXEC` параметр `PARM=` должен содержать 4-символьное имя подсистемы процесса zDC, который требуется завершить.",
    "* User abends `100` and `101` may occur and messages describing the abends are written to the job log.": "* Могут возникать пользовательские ABEND `100` и `101`; описывающие их сообщения записываются в лог задания.",
    "* User abend `100` indicates that the `PARM=` is not exactly 4 bytes long.": "* Пользовательский ABEND `100` означает, что значение `PARM=` имеет длину не ровно 4 байта.",
    "* User abend `101` indicates that the subsystem name specified on the `PARM=` operand can't be found in the system.": "* Пользовательский ABEND `101` означает, что имя подсистемы, указанное в операнде `PARM=`, не найдено в системе.",
    "* Messages `ZDC400` through `ZDC403` may be written to the job log.": "* В лог задания могут записываться сообщения от `ZDC400` до `ZDC403`.",
    'Refer to the [zDC user abends](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#user-abends "Set up the z/OS Data Collection subsystem (zDC).") and [z/OS module messages](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages "Messages that are created by the Dynatrace z/OS modules.") for a list of all zDC messages.': 'Полный список сообщений zDC см. в разделах [Пользовательские ABEND zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#user-abends "Настройка подсистемы сбора данных z/OS (zDC).") и [Сообщения модулей z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages "Сообщения, формируемые модулями Dynatrace z/OS.").',
}

# Lines that must remain verbatim EN (parameter names, config keys, etc.)
PASS = set()

if __name__ == "__main__":
    build_one(REL, FN, TRANS, PASS)
    qa_one(REL, FN)
