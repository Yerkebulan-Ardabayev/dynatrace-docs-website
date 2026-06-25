---
title: Логирование Dynatrace OpenKit
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-logging
scraped: 2026-05-12T11:37:59.140301
---

# Логирование Dynatrace OpenKit

# Логирование Dynatrace OpenKit

* 3-min read
* Updated on Mar 16, 2023

OpenKit поддерживает встроенный логгер (console logger) и возможность реализации пользовательского логгера.

## Уровни логирования

| Уровень | Приоритет | Описание |
| --- | --- | --- |
| Debug | 1 (наименьший) | Отладочная информация |
| Info | 2 | Информационные сообщения |
| Warning | 3 | Предупреждения |
| Error | 4 (наибольший) | Ошибки |

По умолчанию выводятся сообщения уровня Warning и выше.

## Console Logger

Встроенный console logger выводит сообщения в стандартный вывод (stdout).

### Java

```java
OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .withLogLevel(LogLevel.DEBUG)
    .build();
```

### .NET

```csharp
IOpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .WithLogLevel(LogLevel.DEBUG)
    .Build();
```

### C/C++

```c
struct OpenKitHandle* openKit = DynatraceOpenKitBuilderCreate(endpointURL, applicationID, deviceID);
OpenKitBuilderSetLogLevel(openKit, LOG_LEVEL_DEBUG);
```

### JavaScript

```javascript
const openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .withLogLevel(LogLevel.DEBUG)
    .build();
```

## Реализация пользовательского логгера

Для интеграции с существующей системой логирования реализуйте пользовательский логгер.

### Java

```java
public class CustomLogger implements Logger {
    @Override
    public void debug(String message) { /* реализация */ }
    @Override
    public void info(String message) { /* реализация */ }
    @Override
    public void warning(String message) { /* реализация */ }
    @Override
    public void error(String message) { /* реализация */ }
    @Override
    public boolean isDebugEnabled() { return true; }
    @Override
    public boolean isInfoEnabled() { return true; }
    @Override
    public boolean isWarnEnabled() { return true; }
    @Override
    public boolean isErrorEnabled() { return true; }
}

OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .withLogger(new CustomLogger())
    .build();
```

## Связанные темы

* [Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit "Обзор OpenKit.")
* [Методы API OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods "Полный справочник по методам API.")