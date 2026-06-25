---
title: Удаление ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/operation/uninstall-activegate
scraped: 2026-05-12T11:52:13.361934
---

# Удаление ActiveGate

# Удаление ActiveGate

* 1-min read
* Published Jul 17, 2018

ActiveGate имеет выделенную программу удаления. Её необходимо запустить для удаления ActiveGate из системы.

* На Windows:
  Перейдите в **Панель управления** > **Программы и компоненты** и удалите Dynatrace ActiveGate.
* На Linux:
  Перейдите в директорию `/opt/dynatrace/gateway` и с правами root запустите скрипт `uninstall.sh`.

## После удаления

После удаления файлы журналов и часть конфигурации сохраняются в [директориях журналов и конфигурации](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.") ActiveGate соответственно. Эти файлы необходимо удалить вручную.