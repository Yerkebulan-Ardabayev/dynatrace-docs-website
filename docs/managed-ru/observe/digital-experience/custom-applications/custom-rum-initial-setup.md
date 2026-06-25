---
title: Начальная настройка RUM для пользовательских приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/custom-applications/custom-rum-initial-setup
scraped: 2026-05-12T11:34:08.163357
---

# Начальная настройка RUM для пользовательских приложений

# Начальная настройка RUM для пользовательских приложений

* How-to guide
* 1-min read
* Updated on Apr 25, 2024

Данные мониторинга, отправляемые через Dynatrace OpenKit, инкапсулируются в сущность, представляющую ваше приложение и называемую **custom application** (пользовательское приложение). Таким образом, для мониторинга приложения необходимо определить и инструментировать пользовательское приложение, следуя приведённым ниже инструкциям.

Чтобы создать пользовательское приложение в Dynatrace и инструментировать его:

1. В Dynatrace перейдите в **Custom Applications**.
2. Нажмите **Create custom application**.
3. Введите имя для вашего пользовательского приложения и выберите иконку для его визуального представления в веб-интерфейсе Dynatrace.
4. Нажмите **Monitor custom application**. Откроется страница настроек вашего пользовательского приложения.
5. В настройках приложения выберите **Instrumentation wizard**, затем выберите технологию для загрузки последней [библиотеки OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-libraries-on-github "Ознакомьтесь с библиотеками Dynatrace OpenKit на GitHub.").
6. Используйте загруженную библиотеку, а также **Beacon URL** и **Application ID**, указанные в мастере инструментирования, для инструментирования вашего приложения.
7. Необязательно: в мастере инструментирования нажмите **View incoming beacons** для отображения входящих beacon-запросов по мере их поступления с задержкой в несколько секунд. Эта функция также предоставляет информацию о возможных проблемах.

Ниже приведён базовый пример использования Dynatrace OpenKit для отправки данных мониторинга в Dynatrace. Подробнее см. [Методы API Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods "Узнайте, как использовать Dynatrace OpenKit с точки зрения разработчика.").

Java

.NET

C++

C

JavaScript

```
// Obtain an OpenKit instance



String applicationID = "application-id";                // Your application's ID



long deviceID = 42;                                     // Replace with a unique value per device/installation



String endpointURL = "https://tenantid.beaconurl.com/mbeacon";  // Dynatrace endpoint URL



OpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.withApplicationVersion("1.0.0.0")



.withOperatingSystem("Windows 10")



.withManufacturer("MyCompany")



.withModelID("MyModelID")



.build();



// Wait up to 10 seconds for OpenKit to complete initialization



long timeoutInMilliseconds = 10 * 1000;



boolean success = openKit.waitForInitCompletion(timeoutInMilliseconds);



// Create session



String clientIP = "8.8.8.8";



Session session = openKit.createSession(clientIP);



// Identify user



session.identifyUser("jane.doe@example.com");



// Create root and child actions



String rootActionName = "rootActionName";



RootAction rootAction = session.enterAction(rootActionName);



String childActionName = "childAction";



Action childAction = rootAction.enterAction(childActionName);



// Leave action



childAction.leaveAction();



rootAction.leaveAction();



// Finish session



session.end();



// Terminate OpenKit instance



openKit.shutdown();
```

```
// Obtain an OpenKit instance



string applicationID = "application-id";                        // Your application's ID



long deviceID = 42L;                                            // Replace with a unique value per device/installation



string endpointURL = "https://tenantid.beaconurl.com/mbeacon";  // Dynatrace endpoint URL



IOpenKit openKit = new DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.WithApplicationVersion("1.0.0.0")



.WithOperatingSystem("Windows 10")



.WithManufacturer("MyCompany")



.WithModelID("MyModelID")



.Build();



// Wait up to 10 seconds for OpenKit to complete initialization



int timeoutInMilliseconds = 10 * 1000;



bool success = openKit.WaitForInitCompletion(timeoutInMilliseconds);



// Create session



string clientIP = "8.8.8.8";



ISession session = openKit.CreateSession(clientIP);



// Identify user



session.IdentifyUser("jane.doe@example.com");



// Create root and child actions



string rootActionName = "rootActionName";



IRootAction rootAction = session.EnterAction(rootActionName);



string childActionName = "childAction";



IAction childAction = rootAction.EnterAction(childActionName);



// Leave action



childAction.LeaveAction();



rootAction.LeaveAction();



// Finish session



session.End();



// Terminate OpenKit instance



openKit.ShutDown();
```

```
// Obtain an OpenKit instance



const char* applicationID = "application-id";                        // Your application's ID



int64_t deviceID = 42;                                               // Replace with a unique value per device/installation



const char* endpointURL = "https://tenantid.beaconurl.com/mbeacon";  // Dynatrace endpoint URL



std::shared_pointer<openkit::IOpenKit> openKit =



openkit::DynatraceOpenKitBuilder(endpointURL, applicationID, deviceID)



.withApplicationVersion("1.0.0.0")



.withOperatingSystem("Windows 10")



.withManufacturer("MyCompany")



.withModelID("MyModelID")



.build();



// Wait up to 10 seconds for OpenKit to complete initialization



int64_t timeoutInMilliseconds = 10 * 1000;



bool success = openKit->waitForInitCompletion(timeoutInMilliseconds);



// Create session



const char* clientIP = "8.8.8.8";



std::shared_ptr<openkit::ISession> session = openKit->createSession(clientIP);



// Identify user



session->identifyUser("jane.doe@example.com");



// Create root and child actions



const char* rootActionName = "rootActionName";



std::shared_ptr<IRootAction> rootAction = session->enterAction(rootActionName);



const char* childActionName = "childAction";



std::shared_ptr<IRootAction> childAction = rootAction->enterAction(childActionName);



// Leave action



childAction->leaveAction();



rootAction->leaveAction();



// Finish session



session->end();



// Terminate OpenKit instance



openKit->shutdown();
```

```
// Obtain an OpenKit instance



const char* applicationID = "application-id";                        // Your application's ID



int64_t deviceID = 42;                                               // Replace with a unique value per device/installation



const char* endpointURL = "https://tenantid.beaconurl.com/mbeacon";  // Dynatrace endpoint URL



struct OpenKitConfigurationHandle* configurationHandle = createOpenKitConfiguration(endpointURL, applicationID, deviceID);



useApplicationVersionForConfiguration(configurationHandle, "1.0.0.0");



useOperatingSystemForConfiguration(configurationHandle, "Windows 10");



useManufacturerForConfiguration(configurationHandle, "MyCompany");



useModelIDForConfiguration(configurationHandle, "MyModelID");



struct OpenKitHandle* openKit = createDynatraceOpenKit(configurationHandle);



// Wait up to 10 seconds for OpenKit to complete initialization



int64_t timeoutInMilliseconds = 10 * 1000;



bool success = waitForInitCompletionWithTimeout(openKit, timeoutInMilliseconds);



// Create session



const char* clientIP = "8.8.8.8";



struct SessionHandle* session = createSession(openKit, clientIP);



// Identify user



identifyUser(session, "jane.doe@example.com");



// Create root and child actions



const char* rootActionName = "rootActionName";



struct RootActionHandle* rootAction = enterRootAction(session, rootActionName);



const char* childActionName = "childAction";



struct ActionHandle* childAction = enterAction(rootAction, childActionName);



// Leave action



leaveAction(childAction);



leaveRootAction(rootAction);



// Finish session



endSession(session);



// Terminate OpenKit instance



shutdownOpenKit(openKit);
```

```
// Obtain an OpenKit instance



const endpointURL: string = 'https://tenantid.beaconurl.com/mbeacon'; // Dynatrace endpoint URL



const applicationID: string = 'application-id'; // Your application's ID



const deviceID: number = 42; // Replace with a unique value per device/installation



const openkit = new OpenKitBuilder(endpointURL, applicationID, deviceID)



.withApplicationVersion('1.0.0.0')



.withOperatingSystem("Windows 10")



.withManufacturer("MyCompany")



.withModelID("MyModelID")



.build();



const timeoutInMilliseconds = 10 * 1000;



openKit.waitForInit((success) => {



if (success) {



// Create session



const clientIP = '8.8.8.8';



const session: Session = openkit.createSession(clientIP);



// Identify user



session.identifyUser('jane.doe@example.com');



// Create root and child actions



string rootActionName = 'rootActionName';



const rootAction = session.enterAction(rootActionName);



string childActionName = 'childAction';



const childAction = rootAction.enterAction(childActionName);



// Leave action



childAction.leaveAction();



rootAction.leaveAction();



// Finish session



session.end();



// Terminate OpenKit instance



openkit.shutdown();



}



}, timeoutInMilliseconds);
```

ID вашего приложения и URL конечной точки можно найти в мастере инструментирования (в настройках приложения выберите **Instrumentation wizard**).

Для пользовательских приложений идентификация пользователей осуществляется через передачу `deviceID`, который должен быть уникальным для каждого пользователя или устройства. В веб-интерфейсе Dynatrace `deviceID` отображается как **Internal user ID**.

После создания пользовательского приложения в Dynatrace и инструментирования вашего приложения с помощью OpenKit ознакомьтесь со страницами ниже для настройки и устранения проблем инструментирования.

* [Библиотеки Dynatrace OpenKit на GitHub](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-libraries-on-github "Ознакомьтесь с библиотеками Dynatrace OpenKit на GitHub.")
* [Методы API Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods "Узнайте, как использовать Dynatrace OpenKit с точки зрения разработчика.")
* [Логирование Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-logging "Узнайте, как работает логирование с OpenKit.")
* [Устранение проблем инструментирования Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/troubleshoot-dynatrace-openkit-instrumentation "Узнайте, как решать проблемы, возникающие при инструментировании Dynatrace OpenKit.")

После того как ваше пользовательское приложение начнёт отправлять данные мониторинга в Dynatrace, вы можете анализировать их так же, как данные любого другого приложения. Например, [изучать сессии пользователей](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Узнайте о сегментации и атрибутах фильтрации сессий пользователей."), [проверять метрики пользовательского опыта](/managed/observe/digital-experience/custom-applications/analyze-and-use/check-usage-metrics-custom "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта."), [анализировать веб-запросы](/managed/observe/digital-experience/custom-applications/analyze-and-use/analyze-web-requests-custom "Используйте Dynatrace для мониторинга веб-запросов в пользовательских приложениях."), [просматривать отчёты о сбоях](/managed/observe/digital-experience/custom-applications/analyze-and-use/crash-reports-custom "Проверьте последние отчёты о сбоях в ваших пользовательских приложениях.") и многое другое.

На изображении ниже показана страница обзора тестового пользовательского приложения.

![Страница обзора пользовательского приложения](https://dt-cdn.net/images/custom-app-overview-page-1632-8f4bd766b2.png)

Страница обзора пользовательского приложения