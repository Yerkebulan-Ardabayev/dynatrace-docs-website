---
title: Безопасность OneAgent на Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows
scraped: 2026-05-12T11:07:34.962767
---

# Безопасность OneAgent на Windows

# Безопасность OneAgent на Windows

* Чтение: 5 мин
* Опубликовано 12 ноября 2020 г.

Для полной автоматизации мониторинга ваших операционных систем, процессов и сетевых интерфейсов Dynatrace требуется привилегированный доступ к вашей операционной системе как во время установки, так и во время эксплуатации.

OneAgent проходит обширное тестирование, чтобы гарантировать минимальное влияние на производительность вашей системы и [соответствие высочайшим стандартам безопасности](/managed/manage/data-privacy-and-security "Узнайте, как Dynatrace применяет различные меры безопасности, необходимые для защиты приватных данных.").

## Разрешения

OneAgent требует прав администратора на Windows как для установки, так и для эксплуатации.

### Установка

Установщику OneAgent требуются права администратора, чтобы:

* Создать службу OneAgent.
* Изменять определённые ключи реестра.
* Установить драйвер захвата пакетов (Npcap или WinPcap) для сбора сетевых метрик. Дополнительные сведения см. в [Драйвер захвата пакетов (pcap)](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Узнайте, как использовать установщик OneAgent для Windows.").
* Установить [устройство oneagentmon](/managed/discover-dynatrace/get-started/glossary#o "Познакомьтесь с терминологией Dynatrace.").

### Эксплуатация

OneAgent требуются права администратора, чтобы:

* Получать список всех процессов.
* Получать статистику памяти для всех процессов.
* Читать командную строку и окружение каждого процесса.
* Просматривать описания исполняемых файлов.
* Читать конфигурацию приложений для Apache и IIS
* Просматривать список библиотек, загруженных для каждого процесса.
* Читать ключи реестра Windows.
* Читать домен приложений .NET для .NET 2.0, 3.0 и 3.5.
* Запускать мониторинг сетевого трафика.
* Анализировать исполняемые файлы для Go Discovery.
* Собирать данные мониторинга, связанные с контейнерами Docker.

## Изменения операционной системы

OneAgent вносит в вашу систему следующие изменения:

### Установка

Установщик OneAgent изменяет следующие аспекты вашей системы:

* Начиная с версии 1.195, для запуска расширений OneAgent не создаётся учётная запись пользователя. Вместо этого используется привилегированная системная учётная запись `NT AUTHORITY\SYSTEM`. Дополнительные сведения см. в [Пользователь расширений OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#oneagent-extension-user "Узнайте, как использовать установщик OneAgent для Windows.").
* Создаётся служба `Dynatrace OneAgent`.
* Программа Dynatrace OneAgent регистрируется в Windows Installer.
* Устанавливается драйвер `oneagentmon` и создаётся устройство `OneAgentMon`. Это необходимо для включения автоматической инъекции в процессы.
* Создаются поддеревья реестра:

  + `HKEY_LOCAL_MACHINE\SOFTWARE\Dynatrace\OneAgent`
  + `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\oneagentmon`
  + `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Dynatrace OneAgent`
  + `HKEY_LOCAL_MACHINE\SOFTWARE\Caphyon\Advanced Installer`
* [Устранение неполадок: сбой инициализации Network Agent на Windows](https://dt-url.net/7c438ee)
* Драйвер `Npcap` устанавливается с установленным флагом `/admin_only`, который ограничивает чтение и запись пакетов Npcap только пользователями с правами администратора. Непривилегированные пользователи не могут получить доступ к функциональности Npcap на мониторируемом хосте. Обратите внимание, что WinPcap не предлагает такого ограничения. Дополнительные сведения см. в [Настройка установки OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Узнайте, как использовать установщик OneAgent для Windows.").

  Убедитесь, что следующие операции Npcap и WinPcap разрешены в настройках безопасности вашей системы:

  + **Npcap:** Запись значений реестра в `SYSTEM\CurrentControlSet\Services\npcap`
  + **Npcap:** Чтение и запись значений реестра в `SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\NpcapInst`
  + **Winpcap:** Чтение и запись значений реестра в `SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\WinPcapInst` и `SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\WinPcapInst`
  + **Npcap and Winpcap:** Загрузка `wpcap.dll` и `packet.dll`, расположенных в `C:\WINDOWS\system32\Npcap` / `C:\WINDOWS\system32\WinPcap`
  + **Npcap and Winpcap:** Чтение значений реестра о текущих сетевых интерфейсах в [`SYSTEM\CurrentControlSet\Control\Network\{Network-Service-GUID}`](https://dt-url.net/lz036sy)\*

## Добавленные файлы

### Установка

Установщик OneAgent добавляет в вашу систему следующие файлы:

* Бинарные и конфигурационные файлы OneAgent сохраняются в `%PROGRAMFILES%\dynatrace\oneagent`. Обратите внимание, что расположение можно изменить с помощью параметра [INSTALL\_PATH](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#installation-path "Узнайте, как использовать установщик OneAgent для Windows.").
* Временные файлы установщика сохраняются в `C:\AI_RecycleBin`. Папка удаляется после завершения установки.

### Эксплуатация

* Временные файлы OneAgent и конфигурация времени выполнения сохраняются в `%PROGRAMDATA%\dynatrace\oneagent\runtime`.
* Постоянная конфигурация OneAgent сохраняется в `%PROGRAMDATA%\dynatrace\oneagent\config`.
* Крупные данные времени выполнения, такие как дампы памяти, сохраняются в `%PROGRAMDATA%\dynatrace\oneagent\datastorage`. Обратите внимание, что расположение крупных данных времени выполнения можно изменить с помощью параметра [DATA\_STORAGE](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Узнайте, как использовать установщик OneAgent для Windows.").

## Системные логи, скачиваемые OneAgent

OneAgent скачивает системные логи Security, System и Application за последние 14 дней, чтобы Dynatrace мог диагностировать проблемы, которые могут быть вызваны условиями в вашем окружении. Чаще всего такие проблемы связаны с глубоким мониторингом или автоматическими обновлениями.

Отзыв доступа к системным логам

Чтобы отозвать доступ к системным логам, используйте команду `oneagentctl` с параметром `--set-system-logs-access-enabled`, установленным в `false`.  
Дополнительные сведения см. в [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.")

## Глобально доступные для записи каталоги

[Структура каталогов OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Узнайте о структуре каталогов OneAgent и требованиях к дисковому пространству для установки OneAgent на Windows.") содержит глобально доступные для записи каталоги (каталоги, в которые группа пользователей `Everyone` может записывать, изменять или выполнять). Изменение этих прав пользователями не поддерживается.

### Механизм инъекции OneAgent

Такие права на выбранном наборе каталогов необходимы для успешной инъекции OneAgent в процессы на мониторируемых хостах. Когда OneAgent внедряется в процесс, кодовый модуль, отвечающий за инъекцию, выполняется в контексте исходного процесса, в который произошла инъекция. Следовательно, пользователям, под которыми запускаются эти процессы, должно быть разрешено выполнять запись в структуру каталогов OneAgent, что и является причиной глобальных прав на запись, которые делают это возможным.

Аналогично, некоторым файлам логов требуются глобальные права на запись, чтобы приложения, работающие под разными пользователями, могли в них писать.

### Безопасность системы

Нам известно, что глобальные права на чтение и запись для каталогов OneAgent помечаются эвристиками сканеров безопасности, но мы можем заверить вас, что они полностью безопасны.

* Мы держим количество глобально доступных для записи каталогов настолько ограниченным, насколько это возможно.
* Мы используем расширенные права доступа к файлам и применяем разрешение `Creator Owner` для ограничения доступа к файлам.

## Подписывание установщика

Установщик OneAgent подписан одним или несколькими [корневыми сертификатами DigiCert](https://www.digicert.com/kb/digicert-root-certificates.htm). На регулярно обслуживаемых системах Windows проверяет, что установщик OneAgent был опубликован проверенным издателем.

Если ваша система на базе Windows находилась офлайн с марта 2021 года или дольше, Windows не сможет проверить установщик, и издатель установщика OneAgent будет отображаться как **Unknown publisher** при попытке установки или обновления. В таком случае необходимо скачать последний сертификат с [корневых сертификатов DigiCert](https://www.digicert.com/kb/digicert-root-certificates.htm) и добавить его в вашу систему. Среди всех сертификатов DigiCert сертификат `DigiCert Global Root G3` обязателен для успешной проверки установщика OneAgent.

* См. [Как просмотреть сертификаты с помощью оснастки MMC](https://docs.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in) в документации Microsoft, чтобы узнать, какие корневые сертификаты установлены в вашей системе.
* Скачайте последние корневые сертификаты с [корневых сертификатов DigiCert](https://www.digicert.com/kb/digicert-root-certificates.htm).

### Windows 2008 R2

Начиная с OneAgent версии 1.225, установщик подписывается с использованием алгоритма SHA-2. Следовательно, на хостах Windows 2008 R2 должна быть установлена поддержка подписывания кода SHA-2. Если вы используете Windows Update, обновления были предложены вам автоматически (KB4474419 и KB4490628). Однако если ваша система Windows 2008 R2 не поддерживает проверку установщиков, подписанных SHA-2, автообновление и установка OneAgent не будут работать, если `Applocker` настроен на блокировку неизвестных издателей, и/или могут отображаться предупреждения безопасности. Дополнительные сведения см. в объявлении Microsoft [Требование поддержки подписывания кода SHA-2 2019 для Windows и WSUS](https://support.microsoft.com/en-us/topic/2019-sha-2-code-signing-support-requirement-for-windows-and-wsus-64d1c82d-31ee-c273-3930-69a4cde8e64f).