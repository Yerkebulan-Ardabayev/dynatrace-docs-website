---
title: Методы API Dynatrace OpenKit
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods
scraped: 2026-05-12T11:37:59.140301
---

# Методы API Dynatrace OpenKit

# Методы API Dynatrace OpenKit

* 30-min read
* Updated on Mar 16, 2023

Полный справочник по методам API Dynatrace OpenKit для всех поддерживаемых языков программирования.

> _Reference-таблица на английском._

## Структура API

API OpenKit организован следующим образом:

1. Получение экземпляра OpenKit через `DynatraceOpenKitBuilder`.
2. Настройка SSL/TLS и логирования.
3. Инициализация OpenKit.
4. Создание сессий (Session).
5. Создание действий (Action) внутри сессий.
6. Отчёты о событиях, значениях, ошибках.
7. Трассировка веб-запросов.
8. Завершение сессий и OpenKit.

## Создание экземпляра OpenKit (DynatraceOpenKitBuilder)

### Java

```java
OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .withApplicationVersion("1.0.0")
    .withOperatingSystem("Windows 10")
    .build();
```

### .NET

```csharp
IOpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .WithApplicationVersion("1.0.0")
    .WithOperatingSystem("Windows 10")
    .Build();
```

### C/C++

```c
struct OpenKitHandle* openKit = DynatraceOpenKitBuilderCreate(endpointURL, applicationID, deviceID);
OpenKitBuilderSetApplicationVersion(openKit, "1.0.0");
OpenKitBuilderSetOperatingSystem(openKit, "Windows 10");
```

### JavaScript

```javascript
const openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .withApplicationVersion("1.0.0")
    .withOperatingSystem("Windows 10")
    .build();
```

## SSL/TLS безопасность

По умолчанию OpenKit проверяет сертификаты сервера. Для тестовых окружений можно отключить проверку:

```java
// Java — только для тестов, не для production
OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .withTrustManager(new SSLStrictTrustManager()) // строгая проверка (по умолчанию)
    .build();
```

## Подробное логирование

```java
// Java
OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .withLogLevel(LogLevel.DEBUG)
    .build();
```

## Инициализация OpenKit

```java
// Java — синхронная инициализация с тайм-аутом (в секундах)
boolean initialized = openKit.waitForInitCompletion(10);
```

## Создание сессии

```java
// Java
Session session = openKit.createSession("192.168.1.1");
```

## Тегирование пользователей

```java
// Java
session.identifyUser("user123");
```

## Завершение сессии

```java
// Java
session.end();
```

## Отчёт о сбое

```java
// Java
session.reportCrash("NullPointerException", "Unexpected null value", "at MyClass.java:42");
```

## Создание, завершение и отмена действий

```java
// Java
RootAction action = session.enterAction("Button Click");
// ... выполнение действия
action.leaveAction();

// Отмена действия (без записи длительности)
action.cancelAction();
```

## Отчёты: событие, значение, ошибка

```java
// Java
action.reportEvent("Purchase Completed");
action.reportValue("item_count", 3);
action.reportError("Payment Error", -1, "Payment gateway timeout");
```

## Трассировка веб-запросов

```java
// Java
WebRequestTracer tracer = action.traceWebRequest("https://api.example.com/data");
tracer.start();
// ... выполнение запроса
tracer.setResponseCode(200);
tracer.stop();
```

## Настройка конфиденциальности данных

OpenKit поддерживает настройку уровней сбора данных и отчётности о сбоях:

```java
// Java
OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .withDataCollectionLevel(DataCollectionLevel.USER_BEHAVIOR)
    .withCrashReportingLevel(CrashReportingLevel.OPT_IN_CRASHES)
    .build();
```

### Уровни сбора данных

| Уровень | Описание |
| --- | --- |
| `OFF` | Данные не собираются |
| `PERFORMANCE` | Только данные о производительности |
| `USER_BEHAVIOR` | Полный сбор данных о поведении |

### Уровни отчётности о сбоях

| Уровень | Описание |
| --- | --- |
| `OFF` | Сбои не отслеживаются |
| `OPT_OUT_CRASHES` | Сбои не отправляются |
| `OPT_IN_CRASHES` | Сбои отправляются |

## Завершение работы OpenKit

```java
// Java — освобождение ресурсов
openKit.shutdown();
```

## Связанные темы

* [Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit "Обзор OpenKit.")
* [Инструментирование приложения](/managed/ingest-from/extend-dynatrace/openkit/instrument-your-application-using-dynatrace-openkit "Пошаговое руководство.")
* [Логирование OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-logging "Настройка логирования.")