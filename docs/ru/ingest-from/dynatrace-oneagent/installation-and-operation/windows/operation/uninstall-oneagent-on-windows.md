---
title: Удаление Dynatrace OneAgent на Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/uninstall-oneagent-on-windows
scraped: 2026-03-06T21:19:27.656584
---

# Удаление Dynatrace OneAgent в Windows

# Удаление Dynatrace OneAgent в Windows

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

У OneAgent есть специальная программа удаления. Вам потребуется запустить её, чтобы удалить OneAgent из системы.

## Удаление OneAgent с помощью панели управления Windows

Используйте **Панель управления** Windows для удаления OneAgent.

После того как все файлы OneAgent будут удалены из системы, вам потребуется перезагрузить машину, чтобы удалить библиотеки агента из памяти.

## Тихое удаление OneAgent

### Командная строка

Чтобы выполнить тихое удаление OneAgent с помощью командной строки Windows, запустите следующие команды WMIC от имени администратора.

```
> wmic product where name='Dynatrace OneAgent' call uninstall /nointeractive
```

или

```
> wmic product where name='Dynatrace OneAgent' get IdentifyingNumber



IdentifyingNumber



{12345678-ABCD-1234-ABCD-12345678ABCD}



> msiexec /x {12345678-ABCD-1234-ABCD-12345678ABCD} /quiet /l*vx uninstall.log
```

Вы можете опустить `/l*vx uninstall.log`, если файл журнала вам не нужен.

### PowerShell

```
PS> $app = Get-WmiObject win32_product -filter "Name like 'Dynatrace OneAgent'"



PS> msiexec /x $app.IdentifyingNumber /quiet /l*vx uninstall.log
```

## После удаления OneAgent

После удаления в каталоге установки OneAgent сохраняются файлы журналов, пользователь, от имени которого запускался OneAgent, и часть конфигурации. Их можно удалить вручную. Однако обратите внимание, что если файлы конфигурации были удалены и OneAgent переустановлен, хост отобразится как новый с другим внутренним идентификатором.

Для полного удаления OneAgent удалите следующее:

* Файлы журналов по адресу `%PROGRAMDATA%\dynatrace\oneagent\log`.
* Файлы конфигурации по адресу `%PROGRAMDATA%\dynatrace\oneagent\agent\config`.
