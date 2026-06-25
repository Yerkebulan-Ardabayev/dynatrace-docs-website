---
title: Учебное руководство WMI: пакет расширения
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01
scraped: 2026-05-12T12:15:54.373149
---

# WMI tutorial - пакет расширения

# WMI tutorial - пакет расширения

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 30 марта 2022 г.

Расширения Extensions основаны на [файле конфигурации YAML](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать файл YAML расширения с помощью платформы Extensions framework."). Его минимальный состав:

* `name`: должно начинаться с `custom:` для пользовательских расширений
* `version`
* `author`
* `minDynatraceVersion`: минимальная версия Dynatrace для применения минимальной версии схемы расширения

На этом шаге выполните следующее.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание файла YAML**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#create-file "Узнайте о расширениях WMI в платформе Extensions framework.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Сборка пакета расширения**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#build-package "Узнайте о расширениях WMI в платформе Extensions framework.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Загрузка расширения в Dynatrace Hub**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#upload-extension "Узнайте о расширениях WMI в платформе Extensions framework.")

## Шаг 1. Создание файла YAML

Используйте следующий шаблон.

```
name: custom:demo.host-observability



version: # add version



minDynatraceVersion: "1.227"



author:



name: # add your name
```

Сохраните файл `extension.yaml`, ключ разработчика и сертификаты в следующей структуре:

```
my-sample-extension/



└── src/



├── extension.yaml



dashboards/



└── dashboard.json



alerts/



└── alert.json
```

## Шаг 2. Сборка и подпись пакета расширения

В родительском каталоге `extensions` выполните следующую команду:

```
dt extension assemble



dt extension sign --key ./developer.pem
```

Эти команды собирают [пакет расширения](/managed/ingest-from/extensions/concepts#package "Подробнее о концепции Dynatrace Extensions."), содержащий только архив `extension.zip` и файл подписи `extension.zip.sig`.

```
bundle.zip



|    extension.zip



|    extension.zip.sig
```

## Шаг 3. Загрузка расширения в Dynatrace Hub

Чтобы загрузить и активировать расширение, выполните следующую команду:

```
dt extension upload bundle.zip
```

Пример успешного вывода:

```
C:\extension>dt extension upload bundle.zip



Tenant url: your-tenant-url



Api token: your-api-token



Extension upload successful!
```

Дополнительные сведения см. в разделе [Управление расширениями WMI](/managed/ingest-from/extensions/supported-extensions/data-sources/wmi "Узнайте, как расширить возможности наблюдаемости в Dynatrace с помощью декларативного приёма метрик WMI.").

## Результаты

Расширение отображается в Dynatrace со статусом Active.

![result](https://dt-cdn.net/images/wmi-tutorial-hub-1050-7d02da15fb.png)

result

**Следующий шаг**: [Источник данных WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-02 "Узнайте о расширениях WMI в платформе Extensions framework.")