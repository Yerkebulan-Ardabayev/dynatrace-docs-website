---
title: Начало работы
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/getting-started
scraped: 2026-05-12T12:15:22.440198
---

# Начало работы

# Начало работы

* Практическое руководство
* Чтение: 5 мин
* Опубликовано 16 июня 2025 г.

Начните работу с Dynatrace Extensions, следуя этому руководству: настройте редактор Visual Studio Code и соберите и загрузите первое расширение в Dynatrace за 5 минут.

## Подготовка

### Установка

**Dynatrace Extensions** доступно в [магазине](https://marketplace.visualstudio.com/items?itemName=DynatracePlatformExtensions.dynatrace-extensions) Visual Studio Code. Установить его можно оттуда или через поиск расширений VS Code.

### Токен доступа

Дополнение VS Code автоматизирует многие операции разработки Extension 2.0, используя Dynatrace API.

Чтобы использовать все возможности дополнения, создайте [токен доступа к API](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Узнайте о концепции токена доступа и его областях.") со следующими областями доступа:

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

Интерфейс Dynatrace предоставляет специальный шаблон **Extension Development**, который применяет именно эти области доступа токена.

### Настройки подключения

Этот шаг необходим только в том случае, если окружение Dynatrace доступно через выделенный URL, использующий пользовательский или самоподписанный SSL-сертификат.

В этом случае необходимо настроить параметры перед продолжением работы с руководством. Откройте **File > Preferences > Settings**, разверните раздел **Extensions** и найдите секцию **Dynatrace Extensions**. Прокрутите вниз до **Tenant Connectivity Settings** и выберите **Edit in settings.json**.

Зарегистрируйте URL выделенного окружения в открытом файле и укажите путь к CA-файлу или отключите проверку SSL. Например:

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

Ознакомьтесь со всеми [настройками подключения тенанта](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#tenant-connectivity-settings "Подробности настроек для конфигурации Dynatrace Extensions").

## Подключение к Dynatrace

Начните с подключения к окружению Dynatrace. Для этого выполните следующие действия:

* Откройте представление Dynatrace Extensions в интерфейсе VS Code и выберите кнопку **Add environment**, как показано.

  Укажите базовый URL для доступа к Dynatrace. Он должен соответствовать одному из следующих шаблонов:

  + `https://<Id>.live.dynatrace.com` для SaaS-окружений.
  + `https://<Domain>/e/<Id>` для Managed-окружений.
  + `https://<Id>.apps.dynatrace.com` для последней версии платформы Dynatrace.

  **Примечание**: замените `<Id>` идентификатором окружения, а `<Domain>` соответствует домену управляемого окружения.
* Укажите **API Access Token**, подготовленный ранее, и при необходимости добавьте метку.
* Задайте это окружение как текущее.

Дополнение отображает окружение в списке и использует текущее окружение для всех операций API. Дополнительные сведения об использовании представления Environment см. в разделе [Environments](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/specialized-views#environments "Подробности о специализированных представлениях панели действий для Dynatrace Extensions").

## Инициализация рабочего пространства

Пришло время создать первый проект. Если нужно открыть другую папку рабочего пространства, выберите **Open folder**. В противном случае нажмите кнопку **Initialize workspace** для начала.

Сведения об использовании представления Workspaces см. в разделе [Extension 2.0 workspaces](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/specialized-views#extension-20-workspaces "Подробности о специализированных представлениях панели действий для Dynatrace Extensions").

### 1. Проверка схемы

Рабочий процесс начинается с выбора целевой версии схемы из списка. Это позволяет проверять манифест расширения в процессе написания и выявлять проблемы на раннем этапе.

### 2. Разработческие сертификаты

Extensions использует разработческие сертификаты для подписи и упаковки расширений. Выберите **Generate new ones**, чтобы создать новый набор сертификатов, хранящихся в хранилище VS Code.

Сведения о точном пути хранения учётных данных см. в [настройках](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings "Подробности настроек для конфигурации Dynatrace Extensions") расширения.

Рабочий процесс предлагает несколько дополнительных удобных шагов:

* Использовать ли эти сертификаты по умолчанию для всех рабочих пространств:

  + Это обновит глобальные настройки Dynatrace Extensions в соответствии с выбором.
  + В рамках данного руководства выберите **Yes**.
* Загружать ли новый корневой сертификат в хранилище учётных данных Dynatrace.

  + Укажите имя и при необходимости описание.
  + В рамках данного руководства выберите **Yes** и укажите дополнительные сведения.
* Загружать ли новый корневой сертификат в локально установленные OneAgent и ActiveGate.

  + Этот шаг появляется только при обнаружении локальной установки OneAgent или ActiveGate.
  + Этот шаг требует запуска VS Code с правами администратора.
  + В рамках данного руководства выберите **No**.

Сведения об использовании имеющихся разработческих сертификатов см. в разделе [Credentials](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#credentials "Подробности настроек для конфигурации Dynatrace Extensions").

### 3. Шаблон проекта

Последний шаг рабочего процесса: выбор типа проекта. Это позволяет расширению создать нужные файлы.

Поскольку это первое расширение, на этом шаге выберите **Extension 2.0 ⭐**.

Этот вариант является выбором по умолчанию для новых проектов и создаёт следующую начальную структуру:

* `extension`: папка, в которой размещаются все ресурсы расширения.
* `extension/extension.yaml`: файл манифеста расширения.

Дополнительные сведения о других типах проектов см. в разделе [Project templates](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/commands#project-templates "Обзор всех команд, доступных в Dynatrace Extensions").

Кроме того, все шаблоны создают следующие папки и файлы:

* `.vscode`: папка для хранения настроек VS Code, специфичных для рабочего пространства.
* `dist`: папка для хранения всех пакетов расширений.
* `config`: папка для хранения файлов конфигурации мониторинга.
* `.gitignore`: файл с правилами игнорирования ненужных элементов в репозитории git.

## Внесение изменений в расширение

Откройте манифест расширения и внесите изменения: задайте имя расширению и добавьте себя в качестве автора.

Например, обновите файл `extension/extension.yaml` следующими данными:

```
name: custom:my.first.extension



version: "0.0.1"



minDynatraceVersion: "1.265.0"



author:



name: <Your-Name>
```

Замените `<Your-Name>` именем автора.

## Публикация расширения

Наконец, выполните следующие шаги для загрузки расширения в Dynatrace.

1. Нажмите клавишу F1 и выберите команду **Dynatrace extensions: Build**. Рабочий процесс соберёт расширение и создаст пакет в папке `dist`.
2. При запросе о загрузке расширения в Dynatrace выберите **Yes**.
3. При запросе об активации этой версии расширения выберите **Yes**.

Расширение создано, собрано, загружено и активировано. Просмотреть его можно в интерфейсе Dynatrace, перейдя в раздел Extensions.