---
title: Удаление OneAgent на AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/uninstall-oneagent-on-aix
scraped: 2026-03-06T21:18:32.537603
---

# Удаление OneAgent на AIX


* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 19, 2018

OneAgent поставляется с отдельной программой удаления. Для удаления OneAgent из системы необходимо запустить её. Перейдите в каталог `/opt/dynatrace/oneagent/agent` и запустите скрипт `uninstall.sh` с правами суперпользователя (root).

## После удаления

После удаления лог-файлы и часть конфигурации сохраняются в каталоге установки OneAgent. Их можно удалить вручную. Однако обратите внимание: если файлы конфигурации были удалены и OneAgent переустановлен, хост отобразится как новый с другим внутренним идентификатором.

Для полного удаления OneAgent необходимо удалить следующее:

* Лог-файлы, расположенные по адресу:

  + OneAgent версии 1.203 и новее: `/var/log/dynatrace/oneagent`
  + OneAgent версии 1.201 и более ранних: `/opt/dynatrace/oneagent/log`
* Файлы конфигурации, расположенные по адресу `/var/lib/dynatrace/oneagent/agent/config`.
* Очистите переменные окружения `LDR_PRELOAD` и `LDR_PRELOAD64`.
