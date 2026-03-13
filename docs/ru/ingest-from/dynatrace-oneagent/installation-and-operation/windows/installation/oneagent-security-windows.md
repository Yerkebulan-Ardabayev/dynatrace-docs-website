---
title: OneAgent security on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows
scraped: 2026-03-06T21:19:25.957588
---

# Безопасность OneAgent в Windows

# Безопасность OneAgent в Windows

* Latest Dynatrace
* Чтение: 5 мин
* Опубликовано 12 ноября 2020

Для полной автоматизации мониторинга ваших операционных систем, процессов и сетевых интерфейсов Dynatrace требуется привилегированный доступ к вашей операционной системе как при установке, так и при работе.

OneAgent тщательно тестируется, чтобы обеспечить минимальное влияние на производительность вашей системы и [соответствие самым высоким стандартам безопасности](/docs/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").

## Разрешения

OneAgent требует прав администратора в Windows как для установки, так и для работы.

### Установка

Установщику OneAgent требуются права администратора для:

* Создания службы OneAgent.
* Изменения определённых ключей реестра.
* Установки драйвера захвата пакетов (Npcap или WinPcap) для сбора сетевых метрик. Подробнее см. [Драйвер захвата пакетов (pcap)](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Learn how to use the OneAgent installer for Windows.").
* Установки [устройства oneagentmon](/docs/discover-dynatrace/get-started/glossary#o "Get acquainted with Dynatrace terminology.").

### Работа

OneAgent требует прав администратора для:

* Перечисления всех процессов.
* Получения статистики памяти для всех процессов.
* Чтения командной строки и среды каждого процесса.
* Просмотра описаний исполняемых файлов.
* Чтения конфигурации приложений для Apache и IIS.
* Просмотра списка библиотек, загруженных для каждого процесса.
* Чтения ключей реестра Windows.
* Чтения домена приложения .NET для .NET 2.0, 3.0 и 3.5.
* Начала мониторинга сетевого трафика.
* Анализа исполняемых файлов для обнаружения Go.
* Сбора данных мониторинга, связанных с контейнерами Docker.

## Изменения операционной системы

OneAgent вносит следующие изменения в вашу систему:

### Установка

Установщик OneAgent изменяет следующие аспекты вашей системы:

* Начиная с версии 1.195, учётная запись пользователя для запуска расширений OneAgent не создаётся. Вместо этого используется привилегированная системная учётная запись `NT AUTHORITY\SYSTEM`. Подробнее см. [Пользователь расширения OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#oneagent-extension-user "Learn how to use the OneAgent installer for Windows.").
* Создаётся служба `Dynatrace OneAgent`.
* Программа Dynatrace OneAgent регистрируется в Windows Installer.
* Устанавливается драйвер `oneagentmon` и создаётся устройство `OneAgentMon`. Это необходимо для включения автоматического внедрения в процессы.
* Создаются поддеревья реестра:

  + `HKEY_LOCAL_MACHINE\SOFTWARE\Dynatrace\OneAgent`
  + `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\oneagentmon`
  + `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Dynatrace OneAgent`
  + `HKEY_LOCAL_MACHINE\SOFTWARE\Caphyon\Advanced Installer`
* [Устранение неполадок: сбой инициализации Network Agent в Windows](https://dt-url.net/7c438ee)
* Драйвер `Npcap` устанавливается с флагом `/admin_only`, который ограничивает чтение и запись пакетов Npcap только пользователями с правами администратора. Непривилегированные пользователи не могут использовать функциональность Npcap на отслеживаемом хосте. Обратите внимание, что WinPcap не предлагает такого ограничения. Подробнее см. [Настройка установки OneAgent в Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Learn how to use the OneAgent installer for Windows.").

  Убедитесь, что следующие операции Npcap и WinPcap разрешены в настройках безопасности вашей системы:

  + **Npcap:** Запись значений реестра в `SYSTEM\CurrentControlSet\Services\npcap`
  + **Npcap:** Чтение и запись значений реестра в `SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\NpcapInst`
  + **Winpcap:** Чтение и запись значений реестра в `SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\WinPcapInst` и `SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\WinPcapInst`
  + **Npcap и Winpcap:** Загрузка `wpcap.dll` и `packet.dll`, расположенных в `C:\WINDOWS\system32\Npcap` / `C:\WINDOWS\system32\WinPcap`
  + **Npcap и Winpcap:** Чтение значений реестра для текущих сетевых интерфейсов в [`SYSTEM\CurrentControlSet\Control\Network\{Network-Service-GUID}`](https://dt-url.net/lz036sy)\*

## Добавленные файлы

### Установка

Установщик OneAgent добавляет следующие файлы в вашу систему:

* Бинарные файлы и файлы конфигурации OneAgent сохраняются в `%PROGRAMFILES%\dynatrace\oneagent`. Обратите внимание, что вы можете изменить расположение с помощью параметра [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#installation-path "Learn how to use the OneAgent installer for Windows.").
* Временные файлы установщика сохраняются в `C:\AI_RecycleBin`. Папка удаляется после завершения установки.

### Работа

* Временные файлы и конфигурация среды выполнения OneAgent сохраняются в `%PROGRAMDATA%\dynatrace\oneagent\runtime`.
* Постоянная конфигурация OneAgent сохраняется в `%PROGRAMDATA%\dynatrace\oneagent\config`.
* Большие данные среды выполнения, такие как дампы памяти, сохраняются в `%PROGRAMDATA%\dynatrace\oneagent\datastorage`. Обратите внимание, что вы можете изменить расположение больших данных среды выполнения с помощью параметра [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Learn how to use the OneAgent installer for Windows.").

## Системные журналы, загружаемые OneAgent

OneAgent загружает системные журналы Security, System и Application за последние 14 дней, чтобы Dynatrace мог диагностировать проблемы, которые могут быть вызваны условиями в вашей среде. Чаще всего такие проблемы связаны с глубоким мониторингом или автоматическими обновлениями.

Отзыв доступа к системным журналам

Чтобы отозвать доступ к системным журналам, используйте команду `oneagentctl` с параметром `--set-system-logs-access-enabled`, установленным в `false`.
Подробнее см. [Конфигурация OneAgent через интерфейс командной строки](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

## Глобально доступные для записи каталоги

[Структура каталогов OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.") содержит глобально доступные для записи каталоги (каталоги, в которых группа пользователей `Everyone` может записывать, изменять или выполнять). Изменение этих разрешений пользователями не поддерживается.

### Механизм внедрения OneAgent

Такие разрешения на выбранном наборе каталогов необходимы для успешного внедрения OneAgent в процессы на отслеживаемых хостах. Когда OneAgent внедряется в процесс, кодовый модуль, ответственный за внедрение, выполняется в контексте исходного внедрённого процесса. Следовательно, пользователи, под которыми запускаются эти процессы, должны иметь разрешение на запись в структуру каталогов OneAgent, что и является причиной глобальных разрешений на запись.

Аналогично, определённые файлы журналов требуют глобальных разрешений на запись, чтобы приложения, работающие под различными пользователями, могли записывать в них данные.

### Безопасность системы

Мы осведомлены о том, что глобальные разрешения на чтение и запись в каталогах OneAgent отмечаются эвристиками сканирования безопасности, но мы можем заверить вас, что они полностью безопасны.

* Мы ограничиваем количество глобально доступных для записи каталогов до минимума.
* Мы используем расширенные разрешения файлов и разрешение `Creator Owner` для ограничения доступа к файлам.

## Подпись установщика

Установщик OneAgent подписан одним или несколькими [корневыми сертификатами DigiCert](https://www.digicert.com/kb/digicert-root-certificates.htm). Для регулярно обслуживаемых систем Windows проверяет, что установщик OneAgent опубликован проверенным издателем.

Если ваша система на базе Windows была отключена от сети с марта 2021 года или дольше, Windows не сможет проверить установщик, и издатель установщика OneAgent будет отображаться как **Unknown publisher** (Неизвестный издатель) при попытке установки или обновления. В таком случае вам необходимо загрузить последний сертификат с [корневых сертификатов DigiCert](https://www.digicert.com/kb/digicert-root-certificates.htm) и добавить его в вашу систему. Среди всех сертификатов DigiCert сертификат `DigiCert Global Root G3` является обязательным для успешной проверки установщика OneAgent.

* См. [How to: View certificates with the MMC snap-in](https://docs.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in) в документации Microsoft, чтобы узнать, какие корневые сертификаты установлены в вашей системе.
* Загрузите последние корневые сертификаты с [корневых сертификатов DigiCert](https://www.digicert.com/kb/digicert-root-certificates.htm).

### Windows 2008 R2

Начиная с OneAgent версии 1.225, установщик подписывается с использованием алгоритма SHA-2. Следовательно, хосты Windows 2008 R2 должны иметь установленную поддержку подписи кода SHA-2. Если вы используете Windows Update, обновления были предложены вам автоматически (KB4474419 и KB4490628). Однако, если ваша система Windows 2008 R2 не поддерживает проверку установщиков, подписанных SHA-2, автоматическое обновление и установка OneAgent не будут работать, если `Applocker` настроен на блокировку неизвестных издателей, и/или могут отображаться предупреждения безопасности. Подробнее см. объявление Microsoft [2019 SHA-2 Code Signing Support requirement for Windows and WSUS](https://support.microsoft.com/en-us/topic/2019-sha-2-code-signing-support-requirement-for-windows-and-wsus-64d1c82d-31ee-c273-3930-69a4cde8e64f).