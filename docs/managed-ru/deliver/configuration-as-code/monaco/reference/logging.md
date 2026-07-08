---
title: Справочник логирования Dynatrace Monaco CLI
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/reference/logging
---

# Logging reference for Dynatrace Configuration as Code via Monaco

# Logging reference for Dynatrace Configuration as Code via Monaco

* Reference
* 4-min read
* Updated on May 15, 2024

## Отладочное логирование

Все команды Dynatrace Configuration as Code через Monaco (Dynatrace Monaco CLI) принимают необязательный флаг `--verbose` (или кратко `-v`).
Этот флаг включает дополнительный отладочный вывод лога, который помогает найти причину ошибки.

Независимо от флагов, CLI всегда пишет подробный файл лога в папку `.log/`, создаваемую в каталоге, из которого была запущена команда.

## Метки времени в логах

По умолчанию логи содержат метки времени в часовом поясе машины, на которой они были созданы.

Чтобы вместо этого записывать метки времени в UTC, задайте переменную окружения `MONACO_LOG_TIME=utc`.

Linux/macOS

Windows

```
MONACO_LOG_TIME=utc monaco deploy manifest.yaml
```

```
$env:MONACO_LOG_TIME=utc



monaco deploy manifest.yaml
```

## Архив поддержки для диагностики

Для расширенной диагностики используйте флаг `--support-archive`: с ним CLI формирует ZIP-архив с подробной информацией о своих операциях во время выполнения.

```
monaco --support-archive <command>
```

Сформированный ZIP-архив с именем `support-archive-<timestamp>.zip` сохраняется в текущем рабочем каталоге CLI и включает различную информацию, такую как обычные логи, данные HTTP-запросов и ответов:

* `<timestamp>.log`: все логи, созданные Dynatrace Monaco CLI
* `<timestamp>-req.log`: HTTP-запросы к Dynatrace API
* `<timestamp>-resp.log`: HTTP-ответы, полученные от Dynatrace API

Конфиденциальная информация безопасности, такая как заголовок авторизации, исключается из записываемых данных HTTP-запросов в этих файлах.

**Известное ограничение:** содержимое multipart POST-запросов не логируется.

## Структурированное JSON-логирование

Dynatrace Monaco CLI версии 2.4.0+

Чтобы логи можно было обрабатывать другими инструментами и средствами автоматизации, CLI поддерживает логирование в структурированном формате JSON вместо неструктурированного текста.

Чтобы включить структурированное JSON-логирование, используйте переменную окружения `MONACO_LOG_FORMAT=json`.

Linux/macOS

Windows

```
MONACO_LOG_FORMAT=json monaco deploy manifest.yaml
```

```
$env:MONACO_LOG_FORMAT=json



monaco deploy manifest.yaml
```

В режиме структурированного JSON-логирования базовые данные лога дополняются полями метаданных, которые сообщают подробности о координате конфигурации, окружении и, возможно, ошибке, к которым относится строка лога. Подробнее о полях метаданных см. в разделе [Поля метаданных лога](#metadata-log-fields).

### Основные поля лога

Эти поля присутствуют всегда.

| Поле | Описание |
| --- | --- |
| `level` | Уровень лога: `debug`, `info`, `warn` или `error`. |
| `ts` | Метка времени строки лога. |
| `msg` | Сообщение лога. |

### Поля метаданных лога

Поля метаданных включаются в зависимости от их доступности и отношения к строке лога; не все поля метаданных присутствуют во всех строках лога.

| Поле | Описание | Содержимое |
| --- | --- | --- |
| `coordinate` | Координата конфигурации, к которой относится этот лог. | ```  {  "reference": "[project]:[type]:[ID]",  "project": "[project]",  "type":"[type]",  "configID":"[ID]"  } ``` |
| `type` | Логируется в некоторых случаях, когда полная `coordinate` недоступна. | ```  {  "type":"[type]"  } ``` |
| `environment` | Целевое [окружение](/managed/deliver/configuration-as-code/monaco/configuration#environment-groups "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest."), к которому относится эта строка лога.  Содержит информацию о `group` и `name` окружения. | ```  {  "group": "[group]",  "name": "[name]"  } ``` |
| `error` | Подробности о нижележащей ошибке. Включается только для строк лога уровней warning и error.  Содержит информацию о типе (`type`) ошибки, а также подробности (`details`) о её содержимом.  Подробности различаются в зависимости от типа ошибки.  Содержимое ошибок см. в [коде на GitHub](https://github.com/search?q=repo%3ADynatrace%2Fdynatrace-configuration-as-code+%28language%3AGo%29+%2Ferr.*struct+%5C%7B%2F&type=code). | ```  {  "type": "[type of error]",  "details": "[content of the error]"  } ``` |

Некоторые строки лога могут содержать дополнительные нестандартные поля со специфичной для них информацией. Например, некоторые ошибки парсинга включают полное содержимое некорректного ответа API в отдельном поле.

## Отключение записи логов в файлы

По умолчанию Monaco записывает все записи лога в файлы в папке `.logs`. Создаются два файла с суффиксами `.log` и `-errors.log`: со всеми сообщениями лога и с сообщениями об ошибках соответственно. Чтобы отключить эту функциональность, задайте переменной окружения `FEAT_LOG_FILE_ENABLED` значение `0` или `false`.
