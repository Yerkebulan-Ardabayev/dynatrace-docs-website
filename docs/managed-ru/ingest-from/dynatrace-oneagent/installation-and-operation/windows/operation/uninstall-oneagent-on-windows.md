---
title: Удаление Dynatrace OneAgent на Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/uninstall-oneagent-on-windows
scraped: 2026-05-12T11:07:33.689170
---

# Удаление Dynatrace OneAgent на Windows

# Удаление Dynatrace OneAgent на Windows

* Чтение: 1 мин
* Опубликовано 19 сентября 2018 г.

OneAgent имеет специальную программу удаления. Для удаления OneAgent из системы необходимо запустить её.

## Удаление OneAgent через панель управления Windows

Используйте **Control Panel** Windows для удаления OneAgent.

После того как все файлы OneAgent будут удалены из системы, потребуется перезагрузить компьютер, чтобы выгрузить библиотеки агента из памяти.

## Тихое удаление OneAgent

### Командная строка

Чтобы тихо удалить OneAgent через командную строку Windows, выполните следующие команды WMIC с правами администратора.

```
> wmic product where name='Dynatrace OneAgent' call uninstall /nointeractive
```

or

```
> wmic product where name='Dynatrace OneAgent' get IdentifyingNumber



IdentifyingNumber



{12345678-ABCD-1234-ABCD-12345678ABCD}



> msiexec /x {12345678-ABCD-1234-ABCD-12345678ABCD} /quiet /l*vx uninstall.log
```

Можно опустить `/l*vx uninstall.log`, если лог-файл вам не нужен.

### PowerShell

```
PS> $app = Get-WmiObject win32_product -filter "Name like 'Dynatrace OneAgent'"



PS> msiexec /x $app.IdentifyingNumber /quiet /l*vx uninstall.log
```

## После удаления OneAgent

После удаления лог-файлы, пользователь, от имени которого работает OneAgent, и часть конфигурации сохраняются в каталоге установки OneAgent. Их можно удалить вручную. Обратите внимание, что если конфигурационные файлы были удалены и OneAgent установлен повторно, хост будет отображаться как новый с другим внутренним идентификатором.

Для полного удаления OneAgent удалите следующее:

* Лог-файлы, расположенные по адресу `%PROGRAMDATA%\dynatrace\oneagent\log`.
* Конфигурационные файлы, расположенные по адресу `%PROGRAMDATA%\dynatrace\oneagent\agent\config`.