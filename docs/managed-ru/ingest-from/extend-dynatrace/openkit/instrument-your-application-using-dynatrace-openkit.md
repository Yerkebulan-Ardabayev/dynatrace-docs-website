---
title: Инструментирование приложения с помощью Dynatrace OpenKit
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/openkit/instrument-your-application-using-dynatrace-openkit
scraped: 2026-05-12T11:37:59.140301
---

# Инструментирование приложения с помощью Dynatrace OpenKit

# Инструментирование приложения с помощью Dynatrace OpenKit

* 8-min read
* Updated on Mar 16, 2023

Пошаговое руководство по созданию и инструментированию пользовательского приложения с помощью Dynatrace OpenKit.

## Создание нового приложения

Создайте новое пользовательское приложение в Dynatrace:

1. Перейдите в **Web & Mobile > Mobile apps** (или **Custom apps**).
2. Выберите **Create custom application**.
3. Укажите имя приложения.
4. Скопируйте Application ID для использования в OpenKit.

## Полные примеры кода

### Java

```java
// Инициализация
String endpointURL = "https://<your-environment>/api/v1/rum";
String applicationID = "APPLICATION-XXXXXXXXXXXX";
long deviceID = 42L;

OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .withApplicationVersion("1.0.0")
    .withOperatingSystem("Android 12")
    .withManufacturer("Samsung")
    .withModelID("Galaxy S21")
    .build();

openKit.waitForInitCompletion(10);

// Создание сессии
Session session = openKit.createSession("192.168.1.1");
session.identifyUser("user@example.com");

// Создание действия
RootAction action = session.enterAction("Purchase Flow");
action.reportEvent("Cart Opened");
action.reportValue("cart_items", 3);

// Трассировка запроса
WebRequestTracer tracer = action.traceWebRequest("https://api.shop.example.com/cart");
tracer.start();
// ... выполнение запроса
tracer.setResponseCode(200);
tracer.stop();

action.leaveAction();
session.end();
openKit.shutdown();
```

### .NET

```csharp
string endpointURL = "https://<your-environment>/api/v1/rum";
string applicationID = "APPLICATION-XXXXXXXXXXXX";
long deviceID = 42L;

IOpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)
    .WithApplicationVersion("1.0.0")
    .WithOperatingSystem("iOS 16")
    .Build();

openKit.WaitForInitCompletion(TimeSpan.FromSeconds(10));

ISession session = openKit.CreateSession("192.168.1.1");
IRootAction action = session.EnterAction("Main Screen View");
action.ReportEvent("Screen Loaded");
action.LeaveAction();
session.End();
openKit.Shutdown();
```

### C/C++

```c
struct OpenKitHandle* openKit = DynatraceOpenKitBuilderCreate(endpointURL, applicationID, deviceID);
OpenKitBuilderSetApplicationVersion(openKit, "1.0.0");
OpenKitBuilderSetOperatingSystem(openKit, "Linux");
struct OpenKitHandle* built = OpenKitBuilderBuild(openKit);

OpenKitWaitForInitCompletion(built, 10000);

struct SessionHandle* session = OpenKitCreateSession(built, "192.168.1.1");
struct RootActionHandle* action = SessionEnterAction(session, "Login");
RootActionReportEvent(action, "Login Attempted");
RootActionLeaveAction(action);
SessionEnd(session);
OpenKitShutdown(built);
```

## Дополнительные ресурсы

### Настройка

* [Методы API OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods "Полный справочник по методам API.")
* [Логирование OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-logging "Настройка логирования.")
* [Библиотеки OpenKit на GitHub](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-libraries-on-github "Репозитории OpenKit.")

### Анализ и использование данных

* [Мобильные приложения](/managed/observe/digital-experience/mobile-applications "Мониторинг мобильных приложений в Dynatrace.")
* [Session Replay](/managed/observe/digital-experience/session-replay "Воспроизведение сессий пользователей.")

## Связанные темы

* [Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit "Обзор OpenKit.")
* [Устранение неполадок](/managed/ingest-from/extend-dynatrace/openkit/troubleshoot-dynatrace-openkit-instrumentation "Устранение неполадок при инструментировании с OpenKit.")