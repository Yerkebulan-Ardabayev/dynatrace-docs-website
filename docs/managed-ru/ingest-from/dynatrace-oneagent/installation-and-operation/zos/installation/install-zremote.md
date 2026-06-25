---
title: Установка модуля zRemote
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote
scraped: 2026-05-12T11:08:19.414306
---

# Установка модуля zRemote

# Установка модуля zRemote

* Чтение: 8 мин
* Обновлено 22 января 2026 г.

Модуль zRemote обрабатывает данные мониторинга, получаемые от zLocal, и направляет эти данные, сжатые и зашифрованные, через свой локальный ActiveGate в Dynatrace. Таким образом, модуль zRemote снимает значительную часть работы по обработке, возникающей при инструментировании подсистем и приложений, с кодовых модулей CICS, IMS и z/OS Java, перенося её на открытую систему.

Модуль zRemote можно [настроить](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote "Настройка модуля zRemote под ваши задачи."), чтобы включить необязательные функции, такие как **Host groups** и **Db2 SQL statement fetch**.

## Требования к аппаратному обеспечению

Требования к аппаратному обеспечению машины, на которой работает модуль zRemote, зависят от ожидаемого числа транзакций CICS и IMS под мониторингом в секунду. Требования для машин с архитектурами x86-64 и s390 приведены ниже.

* Для сред разработки CICS и IMS: малая или средняя машина.
* Для производственных сред CICS и IMS: большая или сверхбольшая машина.
* Для сред z/OS Java: малая или средняя машина.

| Требования к аппаратному обеспечению | Small (DEV) | Medium (DEV) | Large (PROD) | X-Large (PROD) |
| --- | --- | --- | --- | --- |
| **Ожидаемое число транзакций CICS/IMS под мониторингом в секунду** | **4 000** | **7 500** | **15 000** | **30 000** |
| Необходимые ядра CPU на архитектуре x86-64 (Xeon E5-2600 series) | 2 | 4 | 8 | 16 |
| Необходимые [процессоры IFL](https://www.ibm.com/products/integrated-facility-for-linux) на архитектуре s390 | 1 | 1 | 1 | 2 |
| Необходимая память | 4 ГБ | 6 ГБ | 8 ГБ | 16 ГБ |
| Необходимое дисковое пространство | 20 ГБ | 20 ГБ | 20 ГБ | 20 ГБ |

* Указанные требования к аппаратному обеспечению справедливы для случая, когда модуль zRemote и его ActiveGate используются только для мониторинга мейнфрейма.
* К одному zRemote можно подключить несколько [подсистем zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Настройка подсистемы сбора данных z/OS (zDC)."), пока число транзакций под мониторингом соответствует требованиям к аппаратному обеспечению.

## Системные требования

Мы рекомендуем устанавливать модуль zRemote на мейнфрейме IBM Z или LinuxONE, на поддерживаемой операционной системе Linux для s390. Действуют следующие системные требования:

* Подсистема zDC и модуль zRemote, к которому она подключается, должны находиться в одном дата-центре, чтобы избежать проблем с производительностью и безопасностью.

  + При задержке соединения 3 секунды zRemote запишет предупреждение в свои логи.
  + При задержке соединения 10 секунд zRemote разорвёт соединение.
* zRemote поддерживает только [установку ActiveGate на хост](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate."), настроенную для одного окружения.
* Мониторинг хоста, на котором работает zRemote, с помощью OneAgent поддерживается только в [режиме Full-Stack Monitoring](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.").

### Поддерживаемые операционные системы

Модуль zRemote можно установить на любой из перечисленных ниже операционных систем Linux и Windows.

| Дистрибутив | Версии | Архитектуры CPU |
| --- | --- | --- |
| Oracle Linux | 8.10 | x86-64 |
| Red Hat Enterprise Linux | 8.10, 9.4 | s390, x86-64 |
| Rocky Linux | 8.10 | x86-64 |
| SUSE Enterprise Linux | 15.6 | s390, x86-64 |
| Ubuntu | 16.04, 18.04, 20.04, 22.04, 24.04 | x86-64 |
| Ubuntu | 20.04, 22.04, 24.04 | s390 |
| Windows | 11 | x86-64 |
| Windows Server | 2016, 2019, 2022, 2025 | x86-64 |

## Обзор установщика

В обзоре перечислены ключевые компоненты приложения zRemote, конфигурации zRemote и их каталоги установки по умолчанию. Непостоянные каталоги заменяются при обновлении и удалении.

### Приложение zRemote и каталоги установки

Linux

Windows

Базовый путь: `/opt/dynatrace/zremote`

Базовый путь: `C:/Program Files/dynatrace/zremote`

Все перечисленные ниже каталоги не сохраняются при обновлении или удалении zRemote. Внесённые здесь изменения будут перезаписаны или удалены.

| Каталог | Компонент | Описание |
| --- | --- | --- |
| `agent/lib64` | noneagentz | Бинарный файл zRemote |
| `agent/lib64` | oneagentzwatchdog | Бинарный файл, обеспечивающий работу службы zRemote и контролирующий лимиты ресурсов |
| `agent/lib64` | oneagentdumpproc | Бинарный файл, поддерживающий создание дампов при падении основного приложения |
| `agent/lib64/zos-s390-64/<version>` | dtzagent | Бинарный файл, развёртываемый в UNIX-части мейнфрейма для поддержки коммуникаций OneAgent. Подробнее см. в разделе [Установка подсистемы zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Настройка подсистемы сбора данных z/OS (zDC).") |
| `agent/lib64/zos-s390-64/<version>` | libdtzagent.so | Бинарный файл, развёртываемый в UNIX-части мейнфрейма для поддержки коммуникаций агента. Подробнее см. в разделе [Установка подсистемы zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Настройка подсистемы сбора данных z/OS (zDC).") |
| `agent/conf` | ruxitagent.conf | Файл конфигурации zRemote по умолчанию |
| `agent/conf` | oneagentzwatchdog.ini | Файл конфигурации watchdog по умолчанию |
| `agent/conf` | .pem | Сертификаты приложения |
| `agent` | installer.version | Версия установщика бинарного файла zRemote, обычно совпадает с версией zRemote |
| `agent` | zremote | Только Linux Сервисный скрипт для запуска приложения zRemote |
|  | uninstallation.sh | Только Linux Сервисный скрипт для удаления приложения zRemote.  Удаляет всё, кроме постоянной пользовательской конфигурации и файлов логов. |

### Конфигурация zRemote и каталоги установки

Linux

Windows

Базовый путь: `/var/lib/dynatrace/zremote`

Базовый путь: `C:/Program Files/dynatrace/zremote`

Все перечисленные ниже каталоги не сохраняются при обновлении или удалении zRemote. Внесённые здесь изменения будут перезаписаны или удалены.

| Каталог | Компонент | Описание |
| --- | --- | --- |
| `agent` | runtime | Содержит детали подключения, заданные вашим окружением Dynatrace. |
| `config` | instance.properties | Содержит ID текущего зарегистрированного экземпляра. |
| `config` | version.properties | Содержит полный номер версии модуля zRemote. |
|  | state | Содержит адрес последнего успешного подключения к серверу для индикации корректно установленного соединения. |

Перечисленные ниже каталоги сохраняются при обновлении или удалении. Здесь можно вносить изменения. Подробнее см. [Настройка модуля zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote "Настройка модуля zRemote под ваши задачи.").

| Каталог | Компонент | Описание |
| --- | --- | --- |
| `agent/conf` | zremoteagentuserconfig.conf | Файл конфигурации для настройки модуля zRemote |
| `agent/conf` | watchdoguserconfig.conf | Файл конфигурации для настройки watchdog |

## Установка

Модуль zRemote скачивается и устанавливается автоматически во время процедуры установки ActiveGate на [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-install-an-environment-activegate "Прочитайте пошаговую процедуру установки Environment ActiveGate на Linux.") или [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-install-an-environment-activegate "Прочитайте пошаговую процедуру установки Environment ActiveGate на Windows.").

1. Перейдите в **Deploy Dynatrace**, затем выберите **Install ActiveGate**.
2. На странице **Install Environment ActiveGate** выберите **Linux** или **Windows**.
3. Только Linux Выберите тип установщика **s390** (рекомендуется) или **x86/64**.
4. Выберите назначение **Install the zRemote module for z/OS monitoring**, скачайте установщик и запустите процедуру установки.
5. Необязательно Настройте выбор порта прослушивания.

   По умолчанию модуль zRemote прослушивает порт 8898 для соединений от zLocal, работающего в составе zDC. Чтобы прослушивать другой порт, задайте параметру `zdclistenerport` ваш порт в файле `zremoteagentuserconfig.conf`. Убедитесь, что этот порт не заблокирован брандмауэром.

Подробнее о настройках установки по умолчанию см. в настройках установки ActiveGate по умолчанию для [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Узнайте о настройках по умолчанию, с которыми ActiveGate устанавливается на Linux") или [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings "Узнайте о настройках по умолчанию, с которыми ActiveGate устанавливается на Windows.").

Подробнее о настройке установки см. в разделе настройки установки ActiveGate для [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Узнайте о параметрах командной строки, которые можно использовать с ActiveGate на Linux.") или [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate "Узнайте о параметрах, которые можно использовать с ActiveGate на Windows.").

## Журналирование

Логи zRemote создаются на машине, где установлен модуль zRemote, в каталогах по умолчанию для [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Узнайте о настройках по умолчанию, с которыми ActiveGate устанавливается на Linux") и [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings "Узнайте о настройках по умолчанию, с которыми ActiveGate устанавливается на Windows."). Логи zRemote можно просмотреть либо напрямую на машине, где работает zRemote, либо запросив их у Dynatrace по процедуре [Диагностика OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Узнайте, как запускать диагностику OneAgent.").

Реальный лог zRemote должен содержать следующие сообщения:

* Сообщения логов, отправляемые от всех кодовых модулей CICS/IMS и zDC.
* Сообщения логов, отправляемые от zLocal.

## Обновление и обслуживание

Чтобы оставаться в актуальной версии, модуль zRemote можно обновлять до новой версии автоматически через [процедуру автообновления ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/update-activegate "Узнайте, как определить установленную версию ActiveGate и как скачать и установить последнюю версию.").

Чтобы обновить модуль zRemote вручную

Linux

Windows

1. Если установка была настроена, сделайте резервную копию файла `zremoteagentuserconfig.conf` модуля zRemote и файла `custom.properties` ActiveGate. Установщик не должен перезаписывать эти файлы, но для безопасности рекомендуем сделать резервные копии.
2. Удалите модуль zRemote.

   ```
   /opt/dynatrace/gateway/uninstall.sh
   ```
3. Установите модуль zRemote.

   ```
   ./bin/bash Dynatrace-ActiveGate-Linux-<arch>-<version>.sh --enable-zremote
   ```

1. Если установка была настроена, сделайте резервную копию файла `zremoteagentuserconfig.conf` модуля zRemote и файла `custom.properties` ActiveGate. Установщик не должен перезаписывать эти файлы, но для безопасности рекомендуем сделать резервные копии.
2. Удалите модуль zRemote через панель управления Windows.
3. [Установите модуль zRemote](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-install-an-environment-activegate "Прочитайте пошаговую процедуру установки Environment ActiveGate на Windows."), запустив установщик.

### Операции

Чтобы остановить, запустить или перезапустить модуль zRemote, можно использовать следующие команды.

Linux

Windows

Для выполнения этих команд необходимы права root.

Чтобы запросить текущий статус модуля zRemote:

```
service zremote status
```

Чтобы остановить, запустить или перезапустить модуль zRemote:

```
service zremote stop|start|restart|forcestop
```

Разница между `stop` и `forcestop` в том, что команда `stop` указывает процессу выполнить контролируемую процедуру завершения работы, а `forcestop` принудительно завершает процесс.

Для выполнения этих команд необходимы права администратора.

В Windows модуль zRemote можно обслуживать через вкладку **Services** диспетчера задач Windows. Можно также использовать следующую команду:

```
sc stop|start|restart "Dynatrace zRemote"
```

Команда `sc` асинхронна, поэтому, чтобы определить, когда служба полностью остановится, нужно запрашивать статус службы:

```
sc query "Dynatrace zRemote"
```