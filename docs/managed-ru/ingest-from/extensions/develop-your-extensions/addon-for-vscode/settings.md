---
title: Настройки
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings
---

# Настройки

# Настройки

* Справочник
* 4 мин чтения
* Обновлено 23 марта 2026

Все настройки можно задать глобально или для каждого workspace.

Подробнее о доступе к этим настройкам можно узнать в [официальной документации﻿](https://code.visualstudio.com/docs/getstarted/settings) Visual Studio Code.

## Учётные данные

![Dynatrace Extensions](https://dt-cdn.net/images/dynatrace-extensions-icon-1580-5032ebda6e.png "Dynatrace Extensions") **Dynatrace Extensions** может либо сгенерировать все учётные данные, необходимые для разработки Extension 2.0, либо позволить использовать собственные файлы учётных данных.

### При использовании собственных учётных данных

Нужно указать свои файлы с помощью следующих настроек:

| Настройка | Описание |
| --- | --- |
| `dynatraceExtensions.developerCertkeyLocation` | Путь к файлу [учётных данных разработчика](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions#cert "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework."). |
| `dynatraceExtensions.rootOrCaCertificateLocation` | Путь к корневому сертификату (CA). |

Пример использования:

```
{



"dynatraceExtensions.developerCertkeyLocation": "C:\\Temp\\certificates\\dev.pem",



"dynatraceExtensions.rootOrCaCertificateLocation": "C:\\Temp\\certificates\\ca.pem"



}
```

### При генерации учётных данных

Детали, встраиваемые в генерируемые сертификаты, можно настроить с помощью следующих параметров:

| Настройка | Значение по умолчанию | Описание |
| --- | --- | --- |
| `dynatraceExtensions.certificateCommonName` | Extension Developer | Атрибут common name (CN) сертификата. |
| `dynatraceExtensions.certificateOrganization` |  | Атрибут organization (O) сертификата. |
| `dynatraceExtensions.certificateOrganizationUnit` |  | Атрибут organization unit (OU) сертификата. |
| `dynatraceExtensions.certificateStateOrProvince` |  | Атрибут state or province (ST) сертификата. |
| `dynatraceExtensions.certificateCountryCode` |  | Атрибут country code (C) сертификата. |

## Поведение

Add-on стремится предоставить пользователям максимально гибкую настройку процесса разработки расширений. Следующие параметры позволяют включать и отключать различные функции по требованию.

### Функции

| Настройка | Значение по умолчанию | Описание |
| --- | --- | --- |
| `dynatraceExtensions.metricSelectorsCodeLens` | true | [Metric selector code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#metric-selectors "Overview of all Dynatrace Extensions features to help you develop apps") |
| `dynatraceExtensions.entitySelectorsCodeLens` | true | [Entity selector code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#entity-selectors "Overview of all Dynatrace Extensions features to help you develop apps") |
| `dynatraceExtensions.fastDevelopmentMode` | false | [Fast development mode](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#fast-development-mode "Overview of all Dynatrace Extensions features to help you develop apps") |
| `dynatraceExtensions.wmiCodeLens` | true | [WMI queries code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#windows-management-interface-wmi-queries "Overview of all Dynatrace Extensions features to help you develop apps") |
| `dynatraceExtensions.screenCodeLens` | true | [Unified analysis screen code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#unified-analysis-screens "Overview of all Dynatrace Extensions features to help you develop apps") |

### Логирование

| Настройка | Значение по умолчанию | Описание |
| --- | --- | --- |
| `dynatraceExtensions.logging.level` | `INFO` | Минимальный уровень сообщений лога |
| `dynatraceExtensions.logging.maxFiles` | 10 | Максимальное количество файлов лога (по давности), хранящихся на диске. |
| `dynatraceExtensions.logging.maxFileSize` | 10 | Максимальный размер одного файла лога (в МБ). |

### Настройки подключения к тенанту

Add-on всегда выполняет веб-запросы к среде Dynatrace по HTTPS. В некоторых сценариях, например в Dynatrace Managed, среда может быть доступна через выделенный endpoint, использующий SSL-сертификат с нестандартной или самоподписанной подписью. Хотя такие сертификаты пригодны для шифрования, большинство фреймворков и браузеров не признают их доверенными, из-за чего запросы завершаются ошибкой.

Настройка `dynatraceExtensions.tenantConnectivitySettings` доступна только в файле `settings.json` и представляет собой массив endpoint'ов среды, для которых требуются специальные параметры HTTPS-подключения. Каждый элемент массива является объектом со следующими полями:

| Атрибут | Значение по умолчанию | Описание |
| --- | --- | --- |
| `tenantUrl` | "" | Базовый URL среды Dynatrace. Add-on использует этот URL для определения момента применения специальных параметров подключения к веб-запросам. |
| `certificatePath` | "" | Путь на диске к файлу Root/CA в формате `.pem` или `.crt`. Add-on загружает этот файл и добавляет его в список доверенных CA для указанного `tenantUrl`. |
| `disableSSLVerification` | `false` | При включении add-on игнорирует SSL-сертификаты для указанного `tenantUrl`. Включать только при использовании самоподписанных сертификатов на endpoint'е Dynatrace. |

Пример:

* Добавление пользовательского сертификата в список доверенных CA:

  ```
  "dynatraceExtensions.tenantConnectivitySettings": [



  {



  "tenantUrl": "https://10.0.0.1:5555/e/my-tenant",



  "certificatePath": "C:\\Temp\\my_custom.crt"



  }



  ]
  ```
* Использование самоподписанного сертификата на endpoint'е:

  ```
  "dynatraceExtensions.tenantConnectivitySettings": [



  {



  "tenantUrl": "https://my.custom.endpoint/e/my-other-tenant",



  "disableSSLVerification": true



  }



  ]
  ```

## Диагностика

| Настройка | Значение по умолчанию | Описание |
| --- | --- | --- |
| `dynatraceExtensions.diagnostics.all` | true | Вся диагностика |
| `dynatraceExtensions.diagnostics.extensionName` | true | Имя расширения |
| `dynatraceExtensions.diagnostics.metricKeys` | true | Ключи, используемые в определениях метрик |
| `dynatraceExtensions.diagnostics.cardKeys` | true | Ключи карточек, на которые ссылаются или которые определены в разделе screens |
| `dynatraceExtensions.diagnostics.snmp` | true | Источник данных SNMP, в особенности использование OID |

Подробнее о [пользовательской диагностике](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#diagnostics "Overview of all Dynatrace Extensions features to help you develop apps") Dynatrace Extensions.

## Среда Python

Настройки в этом разделе позволяют настроить параметры виртуальной среды при работе с расширениями на Python.

| Настройка | Значение по умолчанию | Описание |
| --- | --- | --- |
| `dynatraceExtensions.pythonExtraPlatforms` | `[ "linux_x86_64", "win_amd64" ]` | Список платформ для сборки пакетов Python. |
| `dynatraceExtensions.pythonExtraPlatformsOnly` | false | При включении команда `Dynatrace extensions: Build` выполняет сборку только для платформ, указанных выше. |
| `dynatraceExtensions.pythonBuildVersion` | `3.10 + 3.14` | Допустимые значения: `3.10 + 3.14`, `3.10` или `3.14`. Выбрать `3.10` для отката к версиям EEC ранее `1.333.x`. |