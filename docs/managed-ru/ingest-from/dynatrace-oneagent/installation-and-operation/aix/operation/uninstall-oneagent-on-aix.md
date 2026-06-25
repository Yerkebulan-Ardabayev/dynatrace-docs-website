---
title: Удаление OneAgent на AIX
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/uninstall-oneagent-on-aix
scraped: 2026-05-12T11:10:52.470209
---

# Удаление OneAgent на AIX

# Удаление OneAgent на AIX

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 19 сентября 2018 г.

OneAgent имеет специальную программу удаления. Для удаления OneAgent из системы необходимо запустить её. Перейдите в каталог `/opt/dynatrace/oneagent/agent` и с правами root выполните скрипт `uninstall.sh`.

## После удаления

После удаления лог-файлы и часть конфигурации сохраняются в каталоге установки OneAgent. Их можно удалить вручную. Обратите внимание, что если конфигурационные файлы были удалены и OneAgent установлен повторно, хост будет отображаться как новый с другим внутренним идентификатором.

Для полного удаления OneAgent удалите следующее:

* Лог-файлы, расположенные по адресу:

  + OneAgent версии 1.203+ `/var/log/dynatrace/oneagent`
  + OneAgent версии 1.201 и ниже `/opt/dynatrace/oneagent/log`
* Конфигурационные файлы, расположенные по адресу `/var/lib/dynatrace/oneagent/agent/config`.
* Очистите переменные окружения `LDR_PRELOAD` и `LDR_PRELOAD64`.