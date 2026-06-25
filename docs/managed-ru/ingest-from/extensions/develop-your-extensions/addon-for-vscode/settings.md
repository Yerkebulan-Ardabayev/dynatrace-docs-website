---
title: Settings
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings
scraped: 2026-05-12T12:16:06.470993
---

# Settings

# Settings

* Справочник
* Чтение: 4 мин
* Обновлено 23 марта 2026 г.

Все настройки можно задать глобально или для каждого рабочего пространства.

Подробнее о доступе к этим настройкам см. в [официальной документации](https://code.visualstudio.com/docs/getstarted/settings) Visual Studio Code.

## Учётные данные

**Dynatrace Extensions** может либо создать все учётные данные, необходимые для разработки Extension 2.0, либо позволить использовать собственные файлы учётных данных.

### При использовании собственных учётных данных

Необходимо указать файлы с помощью следующих настроек:

| Настройка | Описание |
| --- | --- |
| `dynatraceExtensions.developerCertkeyLocation` | Путь к файлу [разработческих учётных данных](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions#cert "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework."). |
| `dynatraceExtensions.rootOrCaCertificateLocation` | Путь к корневому сертификату (CA). |

Пример использования:

```
{



"dynatraceExtensions.developerCertkeyLocation": "C:\\Temp\\certificates\\dev.pem",



"dynatraceExtensions.rootOrCaCertificateLocation": "C:\\Temp\\certificates\\ca.pem"



}
```

### При создании учётных данных

Сведения, встраиваемые в создаваемые сертификаты, можно настроить с помощью следующих параметров:

| Настройка | Значение по умолчанию | Описание |
| --- | --- | --- |
| `dynatraceExtensions.certificateCommonName` | Extension Developer | Атрибут общего имени (CN) сертификата. |
| `dynatraceExtensions.certificateOrganization` |  | Атрибут организации (O) сертификата. |
| `dynatraceExtensions.certificateOrganizationUnit` |  | Атрибут подразделения организации (OU) сертификата. |
| `dynatraceExtensions.certificateStateOrProvince` |  | Атрибут штата или провинции (ST) сертификата. |
| `dynatraceExtensions.certificateCountryCode` |  | Атрибут кода страны (C) сертификата. |

## Поведение

Дополнение стремится предоставить пользователям максимальные возможности для настройки процесса разработки расширений. Следующие настройки позволяют включать или отключать различные функции по требованию.

### Функции

| Настройка | Значение по умолчанию | Описание |
| --- | --- | --- |
| `dynatraceExtensions.metricSelectorsCodeLens` | true | [Code lens для селектора метрик](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#metric-selectors "Обзор всех функций Dynatrace Extensions для разработки приложений") |
| `dynatraceExtensions.entitySelectorsCodeLens` | true | [Code lens для селектора сущностей](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#entity-selectors "Обзор всех функций Dynatrace Extensions для разработки приложений") |
| `dynatraceExtensions.fastDevelopmentMode` | false | [Режим быстрой разработки](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#fast-development-mode "Обзор всех функций Dynatrace Extensions для разработки приложений") |
| `dynatraceExtensions.wmiCodeLens` | true | [Code lens для запросов WMI](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#windows-management-interface-wmi-queries "Обзор всех функций Dynatrace Extensions для разработки приложений") |
| `dynatraceExtensions.screenCodeLens` | true | [Code lens для экранов унифицированного анализа](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#unified-analysis-screens "Обзор всех функций Dynatrace Extensions для разработки приложений") |

### Журналирование

| Настройка | Значение по умолчанию | Описание |
| --- | --- | --- |
| `dynatraceExtensions.logging.level` | `INFO` | Минимальный уровень сообщений журнала |
| `dynatraceExtensions.logging.maxFiles` | 10 | Максимальное количество файлов журнала (по возрасту), хранимых на диске. |
| `dynatraceExtensions.logging.maxFileSize` | 10 | Максимальный размер одного файла журнала (в МБ). |

### Настройки подключения к тенанту

Дополнение всегда выполняет веб-запросы к среде Dynatrace по HTTPS. В некоторых сценариях, например в Dynatrace Managed, среда может быть доступна через выделенный эндпоинт, использующий SSL-сертификат с пользовательской подписью или самоподписанный сертификат. Хотя такие сертификаты обеспечивают шифрование, большинство фреймворков и браузеров не признают их доверенными, что приводит к сбою запросов.

Параметр `dynatraceExtensions.tenantConnectivitySettings` доступен только из файла `settings.json` и представляет собой массив эндпоинтов среды, требующих специальных настроек для подключения по HTTPS. Каждый элемент массива является объектом со следующими полями:

| Атрибут | Значение по умолчанию | Описание |
| --- | --- | --- |
| `tenantUrl` | "" | Базовый URL вашей среды Dynatrace. Дополнение использует этот URL для определения момента применения специальных настроек подключения к веб-запросам. |
| `certificatePath` | "" | Путь на диске к файлу Root/CA в формате `.pem` или `.crt`. Дополнение загрузит этот файл и добавит его в список доверенных центров сертификации для указанного `tenantUrl`. |
| `disableSSLVerification` | `false` | При включении дополнение игнорирует SSL-сертификаты для указанного `tenantUrl`. Включайте только при использовании самоподписанных сертификатов на эндпоинте Dynatrace. |

Пример:

* Добавление пользовательского сертификата в список доверенных центров сертификации:

  ```
  "dynatraceExtensions.tenantConnectivitySettings": [



  {



  "tenantUrl": "https://10.0.0.1:5555/e/my-tenant",



  "certificatePath": "C:\\Temp\\my_custom.crt"



  }



  ]
  ```
* Использование самоподписанного сертификата на эндпоинте:

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
| `dynatraceExtensions.diagnostics.metricKeys` | true | Ключи, используемые для определений метрик |
| `dynatraceExtensions.diagnostics.cardKeys` | true | Ключи карточек, на которые ссылаются или которые определены в разделе screens |
| `dynatraceExtensions.diagnostics.snmp` | true | Источник данных SNMP, в частности использование OID |

Подробнее о [пользовательской диагностике](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#diagnostics "Обзор всех функций Dynatrace Extensions для разработки приложений") Dynatrace Extensions.

## Среда Python

Параметры этого раздела позволяют настроить виртуальную среду при работе с расширениями Python.

| Настройка | Значение по умолчанию | Описание |
| --- | --- | --- |
| `dynatraceExtensions.pythonExtraPlatforms` | `[ "linux_x86_64", "win_amd64" ]` | Список платформ для сборки пакетов Python. |
| `dynatraceExtensions.pythonExtraPlatformsOnly` | false | При включении команда `Dynatrace extensions: Build` выполняет сборку только для платформ, указанных выше. |
| `dynatraceExtensions.pythonBuildVersion` | `3.10 + 3.14` | Возможные значения: `3.10 + 3.14`, `3.10` или `3.14`. Выберите `3.10` для отката к версиям EEC ранее `1.333.x`. |