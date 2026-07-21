---
title: Определение тегов и метаданных для хостов
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts
---

# Определение тегов и метаданных для хостов

# Определение тегов и метаданных для хостов

* Практическое руководство
* 4 минуты чтения
* Опубликовано 08 марта 2018 г.

В динамичных или крупных средах ручное тегирование хостов может оказаться непрактичным. Для динамичных развёртываний, включающих часто меняющиеся экземпляры и имена хостов (например, AWS или MS Azure), рекомендуется автоматизировать добавление тегов и метаданных к хостам.

### Теги

Чтобы автоматизировать добавление тегов к хостам с помощью OneAgent версий 1.189+, используются параметры командной строки OneAgent. Для более ранних версий используется файл конфигурации тегов хоста.

### Параметры командной строки OneAgent для тегов

OneAgent версии 1.189+

Чтобы добавить или изменить теги хоста, нужно выполнить следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
* **Windows**
  `.\oneagentctl.exe --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
  В одной команде можно добавить или изменить несколько тегов. Также можно определить теги с одинаковым ключом, но разными значениями.

Подробнее об `oneagentctl` см. в разделе [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Узнайте, как выполнить некоторые задачи настройки OneAgent без необходимости переустановки OneAgent.")

### Редактирование файла конфигурации тегов хоста

OneAgent версии 1.187 и более ранние

Кодировка UTF-8

Любые создаваемые файлы `hostautotag.conf` или `hostcustomproperties.conf` должны быть в кодировке UTF-8.

Во время установки OneAgent инсталлятор создаёт простой файл конфигурации `hostautotag.conf` на отслеживаемом хосте. В Windows файл расположен в `%PROGRAMDATA%\dynatrace\oneagent\agent\config`, а в Linux, в `/var/lib/dynatrace/oneagent/agent/config`.

Файл должен содержать список строк или пар ключ/значение, которые будут передаваться на сервер при каждом изменении файла. Для разделения значений тегов используются новые строки или пробелы. Например:

```
TestHost Gdansk role=fallback
```

### Результат

После настройки теги отображаются в верхней части раздела **Properties and tags** на странице обзора хоста.

Теги, созданные с помощью `oneagentctl`, ведут себя аналогично [автоматизированным тегам на основе правил](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Узнайте, как определять и применять теги вручную и автоматически.") и [тегам на основе переменных окружения](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Узнайте, как Dynatrace позволяет определять теги на основе переменных окружения.").

Они имеют префикс в виде строки `[Environment]` и не могут быть удалены с хоста вручную. Удалить их можно только с помощью команды `oneagentctl`. Чтобы удалить тег, нужно выполнить следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --remove-host-tag=TestHost`
* **Windows**
  `.\oneagentctl.exe --remove-host-tag=TestHost`

Подробнее см. в разделе [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Узнайте, как выполнить некоторые задачи настройки OneAgent без необходимости переустановки OneAgent.").

### Другие варианты автоматизированного тегирования

Также можно настроить автоматизированное тегирование хостов в среде с помощью:

* [Автоматизированных правил](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Узнайте, как определять и применять теги вручную и автоматически.")
* [Переменных Environment](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Узнайте, как Dynatrace позволяет определять теги на основе переменных окружения.")
* [Smartscape и топологического API](/managed/dynatrace-api/environment-api/topology-and-smartscape "Узнайте о Dynatrace Topology и Smartscape API.")

## Метаданные хоста

Чтобы автоматизировать добавление метаданных к хостам с помощью OneAgent версий 1.189+, используются параметры командной строки. Для более ранних версий используется файл конфигурации метаданных хоста.

### Параметры командной строки OneAgent для метаданных хоста

OneAgent версии 1.189+

Чтобы добавить или изменить свойства хоста, нужно выполнить следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-property=AppName=easyTravel --set-host-property=Environment=Dev`
* **Windows**
  `.\oneagentctl.exe --set-host-property=AppName=easyTravel --set-host-property=Environment=Dev`
  В одной команде можно добавить или изменить несколько свойств.

Когда пользовательские метаданные хоста используются для обогащения метрик и других данных телеметрии, ключи и значения могут корректироваться в соответствии с требованиями нормализации: ключи приводятся к нижнему регистру, неподдерживаемые символы заменяются на символ подчёркивания (`_`), а ключи или значения, превышающие максимальную длину, обрезаются. В результате обогащённое значение может отличаться от заданного здесь.

Чтобы задать контекст безопасности для хоста, нужно выполнить следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-tag=dt.security_context=easytrade_sec`
* **Windows**
  `.\oneagentctl.exe --set-host-tag=dt.security_context=easytrade_sec`

Чтобы **удалить свойства хоста**, нужно выполнить следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --remove-host-property=AppName --remove-host-property=Environment=Dev`
* **Windows**
  `.\oneagentctl.exe --remove-host-property=AppName --remove-host-property=Environment=Dev`

Подробнее см. в разделе [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-tags "Узнайте, как выполнить некоторые задачи настройки OneAgent без необходимости переустановки OneAgent.").

### Редактирование файла конфигурации метаданных хоста

OneAgent версии 1.187 и более ранние

Процесс настройки свойств похож на процесс настройки тегов, но здесь они настраиваются через файл `hostcustomproperties.conf`, который нужно создать и добавить в каталоги конфигурации OneAgent.

* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config`
* Все Unix-подобные системы: `/var/lib/dynatrace/oneagent/agent/config`

### Результат

После настройки пользовательские свойства отображаются в разделе **Environment custom meta data** блока **Properties and tags** на странице обзора хоста. После этого можно настроить [правила автоматического тегирования](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Узнайте, как определять и применять теги вручную и автоматически.") для включения тегирования этих свойств.

## Смежные темы

* [Ownership](/managed/deliver/ownership "Сопоставьте владение командой с отслеживаемыми сущностями для улучшения совместной работы, назначения задач, реагирования на инциденты и уязвимости, а также управления уровнем обслуживания.")