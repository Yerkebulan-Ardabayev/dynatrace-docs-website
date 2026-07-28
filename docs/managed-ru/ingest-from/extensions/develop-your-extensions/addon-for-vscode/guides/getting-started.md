---
title: Начало работы
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/guides/getting-started
---

# Начало работы

# Начало работы

* Практическое руководство
* Чтение: 5 минут
* Обновлено 07 июл. 2026 г.

Это руководство описывает установку ![Dynatrace Extensions](https://dt-cdn.net/images/dynatrace-extensions-icon-1580-5032ebda6e.png "Dynatrace Extensions") **Dynatrace Extensions** в Visual Studio Code, подключение к среде Dynatrace и публикацию первого расширения с помощью встроенных рабочих процессов VS Code.

## Перед началом

### Установка

Найти ![Dynatrace Extensions](https://dt-cdn.net/images/dynatrace-extensions-icon-1580-5032ebda6e.png "Dynatrace Extensions") **Dynatrace Extensions** можно в [marketplace﻿](https://marketplace.visualstudio.com/items?itemName=DynatracePlatformExtensions.dynatrace-extensions) Visual Studio Code. Установить можно оттуда или через поиск расширений VS Code.

### Access token

Add-on для VS Code автоматизирует многие операции по разработке расширений с помощью Dynatrace API.

Чтобы использовать все возможности, нужно создать [API Access Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции access token и его областях применения.") со следующими разрешениями:

* `WriteConfig`
* `ReadConfig`
* `credentialVault.read`
* `credentialVault.write`
* `extensions.read`
* `extensions.write`
* `extensionEnvironment.write`
* `extensionEnvironment.read`
* `extensionConfigurations.read`
* `extensionConfigurations.write`
* `metrics.read`
* `entities.read`
* `settings.read`
* `settings.write`

В UI Dynatrace есть специальный шаблон **Extension Development**, который применяет именно эти разрешения токена.

### Connectivity settings

Требуется только если среда Dynatrace доступна по выделенному URL с пользовательским или самоподписанным SSL-сертификатом.

Чтобы настроить параметры подключения для среды Dynatrace:

1. Откройте представление **Extensions** в Visual Studio Code, найдите **Dynatrace Extensions**, выберите значок  и затем выберите **Settings**.

   Подробнее: [Settings in Visual Studio Code﻿](https://code.visualstudio.com/docs/getstarted/settings).
2. Введите `DynatraceExtensions tenant` в строку поиска, чтобы найти **Tenant Connectivity Settings**, и выберите **Edit in settings.json**.
3. Зарегистрируйте выделенный URL среды в открытом файле и укажите путь к CA-файлу либо отключите проверку SSL.

   Например:

   ```
   {



   "dynatraceExtensions.tenantConnectivitySettings": [



   {



   "tenantUrl": "https://my.custom.dynatrace/e/abcd-123",



   "certificatePath": "/tmp/certificates/ca.crt"



   }



   ]



   }
   ```

   Подробнее: [Tenant connectivity settings](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#tenant-connectivity-settings "Подробности настроек для конфигурации Dynatrace Extensions").

## Подключение к Dynatrace

Чтобы подключить среду Dynatrace:

1. Перейдите в **Dynatrace Extensions** в представлении **Extensions** в Visual Studio Code и выберите **Add environment**.
2. Укажите базовый URL для доступа к Dynatrace. Он должен соответствовать шаблону:

   `https://<Domain>/e/<Id>`

   Замените `<Id>` идентификатором среды, а `<Domain>` доменом управляемой среды.
3. Укажите заранее подготовленный токен и при необходимости задайте метку.
4. Установите эту среду как текущую.

VS Code отобразит среду в списке и будет использовать её для всех операций API. Подробнее об использовании представления **Environments**: [Environments](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/specialized-views#environments "Подробности о специализированных представлениях панели действий для Dynatrace Extensions").

## Инициализация рабочего пространства

Пора создать первый проект. Если нужно открыть другую папку рабочего пространства, выберите **Open folder**. В противном случае нажмите кнопку **Initialize workspace**.

Подробнее об использовании представления Workspaces: [Extension workspaces](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/specialized-views#extension-20-workspaces "Подробности о специализированных представлениях панели действий для Dynatrace Extensions").

### 1. Schema validation

Процесс начинается с выбора целевой версии схемы. Выберите любую из списка. Это позволяет проверять манифест расширения в процессе написания и выявлять проблемы заблаговременно.

### 2. Developer certificates

Developer certificates используются для подписи и упаковки расширения. Выберите **Generate new ones**, чтобы создать новый набор сертификатов, которые будут храниться в хранилище VS Code.

Точный путь к хранилищу учётных данных можно найти в [settings](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings "Подробности настроек для конфигурации Dynatrace Extensions") расширения.

Процесс предлагает дополнительные шаги для удобства:

* Использовать ли эти сертификаты по умолчанию для всех рабочих пространств:

  + При согласии глобальные настройки Dynatrace Extensions будут обновлены с учётом этого выбора.
  + В рамках этого руководства выберите **Yes**.
* Загружать ли новый CA-сертификат в Credentials Vault Dynatrace.

  + Нужно указать имя и при необходимости описание.
  + В рамках этого руководства выберите **Yes** и укажите дополнительные сведения.
* Загружать ли новый CA-сертификат в локально установленные OneAgents и ActiveGates.

  + Этот шаг появляется только при обнаружении локальной установки OneAgent или ActiveGate.
  + Для этого шага необходимо запустить VS Code с правами администратора.
  + В рамках этого руководства выберите **No**.

Подробнее об использовании существующих developer certificates: [Credentials](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#credentials "Подробности настроек для конфигурации Dynatrace Extensions").

### 3. Project template

Последний шаг процесса, выбор типа проекта. Это позволяет расширению создать нужные файлы.

Поскольку это первое расширение, на этом шаге выберите **Extension 2.0 ⭐**.

Это опция по умолчанию для новых проектов, она создаёт следующую стартовую структуру:

* `extension` - папка для всех ресурсов расширения.
* `extension/extension.yaml` - манифест расширения.

Подробнее о других типах проектов: [Project templates](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/commands#project-templates "Обзор всех команд, доступных в Dynatrace Extensions").

Кроме того, все шаблоны создают следующие папки и файлы:

* `.vscode` - папка для хранения специфичных для рабочего пространства настроек VS Code.
* `dist` - папка для хранения всех пакетов расширений.
* `config` - папка для хранения файлов конфигурации мониторинга.
* `.gitignore` - файл с полезными правилами игнорирования ненужных элементов в git-репозитории.

## Внесение изменений в расширение

Сначала откройте манифест расширения и внесите изменения. Задайте имя расширению и укажите себя как автора.

Например, обновите файл `extension/extension.yaml` следующим содержимым:

```
name: custom:my.first.extension



version: "0.0.1"



minDynatraceVersion: "1.265.0"



author:



name: <Your-Name>
```

Замените `<Your-Name>` именем автора.

## Публикация расширения

Для загрузки расширения в Dynatrace выполните следующие шаги.

1. Нажмите клавишу F1 и выберите команду **Dynatrace extensions: Build**. Процесс соберёт расширение и создаст пакет в папке `dist`.
2. При появлении запроса о загрузке расширения в Dynatrace выберите **Yes**.
3. При появлении запроса об активации этой версии расширения выберите **Yes**.

Поздравляем. Первое расширение создано, собрано, загружено и активировано. Просмотреть его в Dynatrace можно, перейдя в Extensions .