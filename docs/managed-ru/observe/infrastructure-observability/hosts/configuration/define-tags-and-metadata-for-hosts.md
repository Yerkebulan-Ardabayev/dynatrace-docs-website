---
title: Определение тегов и метаданных для хостов
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts
scraped: 2026-05-12T11:11:31.664841
---

# Define tags and metadata for hosts

# Определение тегов и метаданных для хостов

* How-to guide
* 4-min read
* Published Mar 08, 2018

В динамических или крупных средах ручная расстановка тегов хостов может быть непрактичной. Для динамических развёртываний с часто меняющимися экземплярами и именами хостов (например, AWS или MS Azure) следует автоматизировать добавление тегов и метаданных к хостам.

### Теги

Для автоматизации добавления тегов к хостам с OneAgent версии 1.189+ используйте параметры командной строки OneAgent. Для более ранних версий используйте файл конфигурации тегов хоста.

### Параметры командной строки OneAgent для тегов

OneAgent version 1.189+

Чтобы добавить или изменить теги хоста, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
* **Windows**
  `.\oneagentctl.exe --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
  Можно добавить или изменить несколько тегов в одной команде. Также можно определять теги с одинаковым ключом, но разными значениями.

Подробнее о `oneagentctl` см. в разделе [Конфигурация OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Редактирование файла конфигурации тегов хоста

OneAgent version 1.187 и ниже

Кодировка UTF-8

Все создаваемые файлы `hostautotag.conf` или `hostcustomproperties.conf` должны быть закодированы в UTF-8.

При установке OneAgent инсталлятор создаёт простой конфигурационный файл `hostautotag.conf` на отслеживаемом хосте. В Windows файл расположен в `%PROGRAMDATA%\dynatrace\oneagent\agent\config`, в Linux — в `/var/lib/dynatrace/oneagent/agent/config`.

Файл должен содержать список строк или пар «ключ/значение», которые будут отправляться на сервер при каждом изменении файла. Значения тегов разделяются новыми строками или пробелами. Например:

```
TestHost Gdansk role=fallback
```

### Результат

После настройки теги отображаются в верхней части раздела **Properties and tags** на странице обзора хоста.

Теги, созданные с помощью `oneagentctl`, ведут себя аналогично [автоматизированным тегам на основе правил](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") и [тегам на основе переменных среды](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.").

Они имеют префикс `[Environment]` и не могут быть удалены с хоста вручную. Их можно удалить только с помощью команды `oneagentctl`. Чтобы удалить тег, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --remove-host-tag=TestHost`
* **Windows**
  `.\oneagentctl.exe --remove-host-tag=TestHost`

Подробнее см. в разделе [Конфигурация OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Другие варианты автоматической расстановки тегов

Также можно настроить автоматическую расстановку тегов хостов в вашей среде с помощью:

* [Автоматизированных правил](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.")
* [Переменных среды](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.")
* [API Smartscape и топологии](/managed/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API.")

## Метаданные хоста

Для автоматизации добавления метаданных к хостам с OneAgent версии 1.189+ используйте параметры командной строки. Для более ранних версий используйте файл конфигурации метаданных хоста.

### Параметры командной строки OneAgent для метаданных хоста

OneAgent version 1.189+

Чтобы добавить или изменить свойства хоста, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-property=AppName=easyTravel --set-host-property=Environment=Dev`
* **Windows**
  `.\oneagentctl.exe --set-host-property=AppName=easyTravel --set-host-property=Environment=Dev`
  Можно добавить или изменить несколько свойств в одной команде.

Для задания контекста безопасности хоста используйте следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-property=dt.security_context=easytrade_sec`
* **Windows**
  `.\oneagentctl.exe --set-host-property=dt.security_context=easytrade_sec`

Для **удаления свойств хоста** выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --remove-host-property=AppName --remove-host-property=Environment=Dev`
* **Windows**
  `.\oneagentctl.exe --remove-host-property=AppName --remove-host-property=Environment=Dev`

Подробнее см. в разделе [Конфигурация OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Редактирование файла конфигурации метаданных хоста

OneAgent version 1.187 и ниже

Процесс настройки свойств аналогичен процессу для тегов, однако здесь свойства настраиваются через файл `hostcustomproperties.conf`, который необходимо создать и добавить в каталоги конфигурации OneAgent.

* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config`
* Все Unix-подобные системы: `/var/lib/dynatrace/oneagent/agent/config`

### Результат

После настройки пользовательские свойства отображаются в разделе **Environment custom meta data** раздела **Properties and tags** на странице обзора хоста. Затем можно настроить [правила автоматической расстановки тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") для применения тегов к этим свойствам.

## Связанные темы

* [Ownership](/managed/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.")