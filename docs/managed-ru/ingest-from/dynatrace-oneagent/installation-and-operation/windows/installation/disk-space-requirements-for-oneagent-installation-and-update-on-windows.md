---
title: Файлы OneAgent и требования к дисковому пространству на Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows
scraped: 2026-05-12T11:07:29.471580
---

# Файлы OneAgent и требования к дисковому пространству на Windows

# Файлы OneAgent и требования к дисковому пространству на Windows

* Чтение: 4 мин
* Обновлено 25 июня 2025 г.

Эта страница содержит информацию о структуре каталогов OneAgent и требованиях к дисковому пространству для full-stack установки и обновлений OneAgent. Обратите внимание, что точные значения могут различаться в зависимости от версии OneAgent.

## Режим Full-stack и Infrastructure Monitoring

Одни и те же требования к дисковому пространству применяются как к режиму Full-stack, так и к режиму Infrastructure monitoring.

## Каталоги OneAgent и их размеры

|  |  | Каталог по умолчанию | Можно изменить? |
| --- | --- | --- | --- |
| Размер установки (с удалёнными временными файлами установки) | ~775 МБ | `%PROGRAMFILES%\dynatrace\oneagent` | Да [1](#fn-1-1-def) |
| Постоянная конфигурация | ~10 МБ | `%PROGRAMDATA%\dynatrace\oneagent\agent\config` | Нет |
| Временные файлы, конфигурация времени выполнения | 200 МБ | `%PROGRAMDATA%\dynatrace\oneagent\agent\runtime` | Нет |
| Логи | 1 ГБ | `%PROGRAMDATA%\dynatrace\oneagent\log` | Да [2](#fn-1-2-def) |
| Отчёты о сбоях, дампы памяти | 3 ГБ | `%PROGRAMDATA%\dynatrace\oneagent\datastorage` | Да [3](#fn-1-3-def) |
| Хранение данных Log analytics | ~1 ГБ [4](#fn-1-4-def) | `%PROGRAMDATA%\dynatrace\oneagent\datastorage\loganalytics` | Да [3](#fn-1-3-def) |
| Файл хранения данных для повторной передачи логов EEC | 600 МБ + 1,5 ГБ буфер | `%PROGRAMDATA%\dynatrace\oneagent\agent\runtime\extensions\persistence` | Да [5](#fn-1-5-def) [6](#fn-1-6-def) |
| Дополнительное место, необходимое для обновлений | ~3,4 ГБ | См. [Место, необходимое для установки и обновлений](#updates) |  |
| **Всего** | **~11,5 ГБ** |  |  |

1

Используйте параметр установки [INSTALL\_PATH](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#installation-path "Узнайте, как использовать установщик OneAgent для Windows.").

2

Используйте параметр установки [LOG\_PATH](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#log-path "Узнайте, как использовать установщик OneAgent для Windows.").

3

Используйте параметр установки [DATA\_STORAGE](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Узнайте, как использовать установщик OneAgent для Windows.").

4

Размер зависит от количества принятых логов.

5

Применимо только если вы используете Dynatrace Extensions, которые [определяют метрики логов, события или добавляют свои правила обработки логов](/managed/ingest-from/extensions/advanced-configuration/extension-customize#log-metrics-events-and-processing-rules "Узнайте, как инструментировать ваши расширения, чтобы настроить обработку принимаемых данных в Dynatrace."). Может быть изменено через запрос в поддержку.

6

Механизм надёжности не работает, если требование не выполнено. Подробнее см. [Подробности хранения данных](#persistence).

Полный список файлов и каталогов, добавляемых OneAgent в вашу систему, см. в [Безопасность OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows").

## Механизм устаревания файлов OneAgent

OneAgent в режиме full-stack monitoring использует встроенный механизм устаревания для того, чтобы файлы OneAgent, включая файлы логов и данные времени выполнения, оставались в пределах разумного размера. Подробнее см. [Механизм устаревания файлов OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Узнайте, как OneAgent удаляет старые файлы для минимизации использования дискового пространства.").

## Место, необходимое для обновлений

При расчёте места, необходимого для обновлений, мы учитываем размер сжатого EXE-установщика, распакованный MSI-пакет и размер процесса установки (место, необходимое для развёртывания файлов OneAgent).

|  | Размер | Описание | Удаляется после | Кем занято | Путь |
| --- | --- | --- | --- | --- | --- |
| 1 | ~130 МБ | EXE-установщик, скачанный AutoUpdate | Перезапуск OneAgent или установка следующей версии [1](#fn-2-1-def) | AutoUpdate | `%PROGRAMDATA%\dynatrace\oneagent` |
| 2 | ~750 МБ | Распакованный MSI-установщик | Конец установки | Установка OneAgent | `%PROGRAMDATA%\dynatrace\oneagent` |
| 3 | ~750 МБ | Дополнительное хранилище для временных файлов установки | Конец установки | Установка OneAgent | `%APPDATA%` |
| 4 | ~750 МБ | Копия MSI-установщика, сохранённая Windows | Установка следующей версии | Windows installer | `%WINDIR%\Installer` |
| 5 | ~750 МБ | Установленные файлы | Установка следующей версии | Установка OneAgent | `[Installation path]` |
| Σ | ~3130 МБ |  |  |  |  |

1

Если вы скачиваете EXE-установщик вручную, процесс установки не будет его удалять.

Дополнительное место, необходимое для установки и обновлений, рассчитывается с запасом 10%:

`(размер процесса установки [2+3+4+5] + размер файлов установщика [1]) * 1.1`

Необходимое дисковое пространство для установки и обновления OneAgent на одном диске составляет ~3,4 ГБ согласно этой формуле.

Обратите внимание, что EXE-установщик сжат, что объясняет разницу в размере по сравнению с MSI-установщиком.

С точки зрения требований к дисковому пространству нет реальной разницы между ручной установкой новой версии (когда уже установлена более старая версия), автоматическим обновлением и обновлениями, запускаемыми перезапуском контейнера OneAgent. Во всех этих случаях процесс установки выполняется одинаково. Различается только метод запуска обновления.

## Подробности хранения данных

Механизм надёжности обеспечивает хранение логов Extension Execution Controller (EEC) на случай недоступности ActiveGate или OneAgent, проблем с сетью или перегрузки EEC при приёме данных. Это минимизирует пробелы в покрытии логами.

### Общая информация

* Постоянное хранение данных требует 2136 МБ свободного дискового пространства:

  + 600 МБ свободного дискового пространства для использования механизмом надёжности
  + 1,5 ГБ свободного дискового пространства для использования в качестве буфера
* Требование проверяется периодически, и если оно не выполняется, хранение данных будет отключено, а приём логов будет передаваться без механизма надёжности.
* Объём используется пропорционально нагрузке приёма логов.
* Если требование не может быть выполнено на хосте, можно изменить конфигурацию хранения логов. Подробнее см. [Конфигурация хранения данных](#persistence_config).

### Конфигурация

Файл конфигурации для Windows: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`

Файл конфигурации для Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`

| **Переменная** | **Описание** |
| --- | --- |
| `persistence.reliable_mode` | `true` - надёжный режим включён; SFM-логи генерируются, если требование к месту не выполнено `false` - надёжный режим отключён; приём логов будет передаваться без механизма надёжности |
| `persistence.total_limit_kb` | Максимальный лимит объёма для Extensions Log Persistence в килобайтах. По умолчанию: 600 МБ Может быть изменён вручную, если требование не может быть выполнено на хосте. |