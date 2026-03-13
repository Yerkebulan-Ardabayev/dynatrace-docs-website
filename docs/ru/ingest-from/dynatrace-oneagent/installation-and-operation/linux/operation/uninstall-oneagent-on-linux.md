---
title: Uninstall OneAgent on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux
scraped: 2026-03-06T21:19:08.954506
---

# Удаление OneAgent на Linux

# Удаление OneAgent на Linux

* Последняя версия Dynatrace
* Время чтения: 1 мин
* Обновлено 20 октября 2025 г.

OneAgent имеет специальную программу удаления. Для удаления OneAgent из системы необходимо её запустить.

Перейдите в каталог `/opt/dynatrace/oneagent/agent` и запустите скрипт `uninstall.sh` с правами суперпользователя (root).

## После удаления

После удаления в каталоге установки OneAgent сохраняются лог-файлы, пользователь, от имени которого работал OneAgent, и часть конфигурации. Их можно удалить вручную. Однако обратите внимание: если файлы конфигурации были удалены и OneAgent был переустановлен, хост будет отображаться как новый с другим внутренним идентификатором.

Для полного удаления OneAgent необходимо удалить следующее:

* Лог-файлы, расположенные по адресу:

  + OneAgent версии 1.203 и выше: `/var/log/dynatrace/oneagent`
  + OneAgent версии 1.201 и ниже: `/opt/dynatrace/oneagent/log`
* Файлы конфигурации по адресу `/var/lib/dynatrace/oneagent/agent/config`.
* Пользователя, от имени которого работал OneAgent, — `dtuser`.
* Дополнительно: если вы используете нестандартный путь установки, установщик создаёт символическую ссылку в каталоге по умолчанию (`/opt/dynatrace/oneagent`), указывающую на нестандартный путь.
  После удаления OneAgent эту символическую ссылку необходимо удалить вручную.
  Подробнее см. в разделе [Путь установки](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#installation-path "Узнайте, как использовать установщик Linux с параметрами командной строки.").
