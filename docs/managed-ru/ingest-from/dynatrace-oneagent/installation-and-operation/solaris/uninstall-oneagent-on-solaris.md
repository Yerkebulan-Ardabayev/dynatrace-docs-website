---
title: Удаление OneAgent на Solaris
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/uninstall-oneagent-on-solaris
scraped: 2026-05-12T11:09:48.048864
---

# Удаление OneAgent на Solaris

# Удаление OneAgent на Solaris

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 13 ноября 2025 г.

Чтобы удалить OneAgent на Solaris, отмените все изменения конфигурации, внесённые при [установке](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Узнайте, как настроить Dynatrace для мониторинга приложений различных технологий, работающих на Solaris (x86 и SPARC).") OneAgent.

* Удалите заданные переменные окружения.
  Например:

  + `DT_HOME`
  + `LD_PRELOAD`
* Восстановите любую конфигурацию приложений, которая ссылается на OneAgent.
  Например:

  + `httpd.conf LoadModule`
* Удалите все загруженные файлы.

Хотя эти параметры конфигурации являются типичными, в вашем окружении могут потребоваться дополнительные шаги в зависимости от конфигурации, заданной во время установки. Сведения, специфичные для вашей настройки, см. в [руководстве по установке](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Узнайте, как настроить Dynatrace для мониторинга приложений различных технологий, работающих на Solaris (x86 и SPARC).") и отмените шаги, которые вы применяли для своих приложений.

Повторная установка OneAgent

Если конфигурационные файлы удалены и OneAgent установлен повторно, хост будет отображаться как новый с другим внутренним идентификатором.