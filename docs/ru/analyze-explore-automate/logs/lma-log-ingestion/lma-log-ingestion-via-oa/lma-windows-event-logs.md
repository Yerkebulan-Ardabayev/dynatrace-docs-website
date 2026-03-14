---
title: Windows журналы событий
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-windows-event-logs
scraped: 2026-03-04T21:36:40.493360
---

# Журналы событий Windows


* Latest Dynatrace
* Tutorial
* Updated on Aug 15, 2025

Журналы событий Windows -- это подробная запись уведомлений, хранимых операционной системой Windows. Эти журналы используются для устранения неполадок и мониторинга работоспособности и безопасности системы. Dynatrace OneAgent использует нативный Windows API для сбора всех записей журналов. Существуют три основных журнала:

* Application Logs: содержат события, зарегистрированные приложениями или программами.
* System Logs: содержат события, зарегистрированные системными компонентами Windows.
* Security Logs: содержат события, связанные с безопасностью, такие как попытки входа в систему и доступ к ресурсам.

Журналы событий Windows автоматически обнаруживаются и могут быть приняты с помощью Dynatrace OneAgent. Вы можете предоставить пользовательские журналы событий с помощью конфигурации [пользовательского источника журналов](lma-custom-log-source.md#configure-log-source-mainclscuipage "Настройка пользовательских источников журналов для ручного добавления источников данных журналов, которые не были обнаружены автоматически.").

## Настройка приёма журналов событий Windows

Существует несколько способов настройки ваших журналов событий Windows. Для включения и настройки их приёма выполните следующие шаги.

### Установка времени ожидания запроса

Перед началом фактической настройки установите значение для **Windows Event Log query timeout**:

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Log monitoring** > **Advanced log settings**.
2. В поле **Windows Event Log query timeout** введите значение в секундах для определения максимального времени ожидания запроса на извлечение журналов событий Windows.

### Включение приёма журналов событий Windows

Следующая конфигурация позволяет принимать журналы событий Windows и подготавливать их для анализа. Выполните следующие шаги:

1. Перейдите в **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Включите правило **[Built-in] Windows system, application, and security logs**.

Если опция **[Built-in] Ingest all logs** включена, журналы событий Windows автоматически включаются, и дополнительная настройка для их приёма не требуется.

### Создание правила приёма на основе атрибутов журналов событий Windows

Следующие шаги необходимы в случае, если вы хотите настроить правила приёма журналов для сбора только определённых журналов событий Windows на основе их атрибутов, а не приёма всех доступных журналов.

1. Перейдите в **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Выберите **Add rule** и укажите имя конфигурации в поле **Rule name**.
3. Убедитесь, что кнопка **Include in storage** включена, чтобы журналы, соответствующие этой конфигурации, сохранялись в Dynatrace.
4. Выберите **Add condition**.
5. В раскрывающемся списке **Matcher attribute** выберите один или несколько [атрибутов](#attributes) журналов Windows.
6. Введите условие сопоставления в поле **Value** в соответствии с выбранным атрибутом и выберите **Add matcher**.
7. Выберите **Save changes**.

### Создание правила приёма на основе имени журнала событий Windows

Следующие шаги необходимы в случае, если вы хотите настроить правила приёма журналов для сбора только определённых журналов событий Windows на основе их имён, а не приёма всех доступных журналов.

1. Перейдите в **Settings** > **Log Monitoring** > **Log ingest rules**.
2. Выберите **Add rule** и укажите имя конфигурации в поле **Rule name**.
3. Убедитесь, что кнопка **Include in storage** включена, чтобы журналы, соответствующие этой конфигурации, сохранялись в Dynatrace.
4. Выберите **Add condition**.
5. В раскрывающемся списке **Matcher [attribute](#attributes)** выберите **Log source**.
6. Введите одно или несколько условий сопоставления журналов Windows в поле **Value** (**Windows Application Log**, **Windows Security Log** или **Windows System Log**) и выберите **Add matcher**.
7. Выберите **Save changes**.

## Добавление пользовательского источника журналов событий Windows

Пользовательские источники журналов событий Windows полезны, когда вам необходимо принимать журналы из пользовательских журналов приложений или журналов, созданных сторонним программным обеспечением. Например, если ваша организация имеет пользовательское приложение, вы можете использовать эту функцию для сбора и анализа его собственных выделенных журналов событий в Dynatrace.

Для приёма пользовательских журналов событий Windows вы можете определить пользовательский источник журналов. Выполните следующие шаги для настройки и добавления пользовательского источника журналов событий Windows в соответствии с вашими требованиями.

1. Перейдите в **Settings** > **Log Monitoring** > **Custom log sources**.
2. Выберите **Add custom log source** и укажите имя конфигурации в поле **Rule name**.
3. Необязательно: привяжите правило к **Process group**, выбрав имя группы процессов из раскрывающегося меню.
4. Выберите опцию **Windows Event** log для пути пользовательского источника журналов.
5. Выберите **Add custom log source path** и введите полное имя источника журналов событий.
6. Выберите **Save changes**.
7. При необходимости добавьте соответствующее правило приёма.

## Атрибуты, выделяемые в журналах событий Windows

Для журналов событий Windows мониторинг журналов обнаруживает следующие поля и отправляет их в качестве пользовательских атрибутов:

## Поддержка структурированных данных

Эта функция позволяет собирать структурированные данные из журналов событий Windows в ветвях **User Data** или **Event Data** (в зависимости от доступности), а также их подветвях. Собранные данные передаются вместе с содержимым записи в виде атрибутов.

Для включения этой функции перейдите в **Settings** > **Log Monitoring** > **Log module feature flags** и включите флаг функции **Support for structured data in Windows Event Logs**.

Имена атрибутов назначаются на основе доступной информации, такой как имена тегов, значение поля **Name**, или, если имена тегов повторяются и поле **Name** отсутствует, к имени тега добавляется порядковый номер.

* Подветви без значений и теги с меткой Binary пропускаются.
* К имени атрибута всегда добавляется префикс `winlog.data`.
* Нумерация последовательных полей (при необходимости, с одинаковым именем атрибута) также включает поля с пустыми значениями.

Ниже приведены примеры ветвей и атрибутов:

Данные в разделе EventData

Необработанные данные журнала событий:

```
- <EventData>


<Data Name="CallerProcessId">16548</Data>


<Data Name="CallerProcessImageName">vctip</Data>


<Data Name="Type">client</Data>


</EventData>
```

Разобранные атрибуты:

```
AttributeKey: winlog.data.CallerProcessId, AttributeValue: 16548


AttributeKey: winlog.data.CallerProcessImageName, AttributeValue: vctip


AttributeKey: winlog.data.Type, AttributeValue: client
```

Данные в разделе UserData

Необработанные данные журнала событий:

```
- <UserData>


-   <CbsPackageChangeState xmlns="http://manifests.microsoft.com/win/2004/08/windows/setup_provider">


<PackageIdentifier>KB5058405</PackageIdentifier>


<IntendedPackageState>5112</IntendedPackageState>


<IntendedPackageStateTextized></IntendedPackageStateTextized>


</CbsPackageChangeState>


</UserData>
```

Разобранные атрибуты:

```
AttributeKey: winlog.data.CbsPackageChangeState.<xmlattr>.xmlns, AttributeValue: http://manifests.microsoft.com/win/2004/08/windows/setup_provider


AttributeKey: winlog.data.CbsPackageChangeState.PackageIdentifier, AttributeValue: KB5058405


AttributeKey: winlog.data.CbsPackageChangeState.IntendedPackageState, AttributeValue: 5112
```

Бинарные данные и пустые поля данных

Необработанные данные журнала событий:

```
- <EventData>


<Data>WinRT Intellisense PPI - en-us</Data>


<Data>10.1.19041.685</Data>


<Data>(NULL)</Data>


<Data />


<Binary>7B31354532394146462D434231392D413230422D394138312D4230373635413633313135467D3030303063306133616532343933363166643732376335306533653966623534363139633030303030393034</Binary>


<Data>Test</Data>


</EventData>
```

Разобранные атрибуты:

```
AttributeKey: winlog.data.Data1, AttributeValue: WinRT Intellisense PPI - en-us


AttributeKey: winlog.data.Data2, AttributeValue: 10.1.19041.685


AttributeKey: winlog.data.Data3, AttributeValue: (NULL)


AttributeKey: winlog.data.Data5, AttributeValue: Test
```
