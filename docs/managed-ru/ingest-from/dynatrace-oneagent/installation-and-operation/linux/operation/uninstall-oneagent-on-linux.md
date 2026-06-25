---
title: Удаление OneAgent на Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux
scraped: 2026-05-12T11:05:34.381494
---

# Удаление OneAgent на Linux

# Удаление OneAgent на Linux

* Чтение: 1 мин
* Обновлено 20 октября 2025 г.

У OneAgent есть отдельная программа удаления. Чтобы удалить OneAgent из системы, потребуется её запустить.

Перейдите в каталог `/opt/dynatrace/oneagent/agent` и с правами root запустите скрипт `uninstall.sh`.

## После удаления

После удаления файлы журналов, пользователь, под которым работает OneAgent, и часть конфигурации сохраняются в каталоге установки OneAgent. Их можно удалить вручную. Однако обратите внимание, что если конфигурационные файлы удалены и OneAgent установлен повторно, хост будет отображаться как новый с другим внутренним идентификатором.

Для полного удаления OneAgent удалите следующее:

* Файлы журналов, расположенные в:

  + OneAgent версии 1.203+: `/var/log/dynatrace/oneagent`
  + OneAgent версии 1.201 и более ранние: `/opt/dynatrace/oneagent/log`
* Конфигурационные файлы, расположенные в `/var/lib/dynatrace/oneagent/agent/config`.
* Пользователь, под которым работает OneAgent, `dtuser`.
* Необязательно Если вы используете пользовательский путь установки, установщик создаёт символическую ссылку в каталоге по умолчанию (`/opt/dynatrace/oneagent`) на пользовательский путь установки.
  Эту символическую ссылку необходимо удалить вручную после удаления OneAgent.
  Дополнительные сведения см. в [Путь установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#installation-path "Узнайте, как использовать установщик Linux с параметрами командной строки.").