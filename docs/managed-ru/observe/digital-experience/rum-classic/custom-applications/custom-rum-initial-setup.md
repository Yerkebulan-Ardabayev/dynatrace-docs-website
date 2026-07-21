---
title: Начальная настройка для пользовательских приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/custom-applications/custom-rum-initial-setup
---

# Начальная настройка для пользовательских приложений в RUM Classic

# Начальная настройка для пользовательских приложений в RUM Classic

* Практическое руководство
* Чтение: 1 минута
* Обновлено 25 апр. 2024 г.

Данные мониторинга, отправляемые через Dynatrace OpenKit, инкапсулируются в сущность, представляющую приложение, и называются **custom application**. Поэтому для мониторинга приложения нужно определить и инструментировать custom application, следуя приведённым ниже инструкциям.

Как создать custom application в Dynatrace и инструментировать его

1. В Dynatrace перейти в **Custom Applications**.
2. Выбрать **Create custom application**.
3. Ввести имя custom application и выбрать значок для визуального представления приложения в веб-интерфейсе Dynatrace.
4. Выбрать **Monitor custom application**. Откроется страница настроек custom application.
5. В настройках приложения выбрать **Instrumentation wizard**, затем выбрать свою технологию, чтобы скачать последнюю версию [OpenKit library](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-libraries-on-github "Check out the Dynatrace OpenKit libraries on GitHub.").
6. Использовать скачанную библиотеку, а также **Beacon URL** и **Application ID**, указанные в instrumentation wizard, для инструментирования приложения.
7. Необязательно: в instrumentation wizard выбрать **View incoming beacons**, чтобы видеть входящие beacon по мере поступления с задержкой всего в пару секунд. В этом представлении также отображается информация о возможных проблемах.

Ниже приведён базовый пример использования Dynatrace OpenKit для отправки данных мониторинга в Dynatrace. Подробнее см. [Dynatrace OpenKit API methods](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods "Read how Dynatrace OpenKit can be used from the developer's point of view.").

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

Application ID и endpoint URL можно найти в instrumentation wizard (в настройках приложения выбрать **Instrumentation wizard**).

Для custom application идентификация пользователя выполняется путём передачи `deviceID`, который должен быть уникальным для каждого пользователя или устройства. Затем `deviceID` отмечается как **Internal user ID** в веб-интерфейсе Dynatrace.

После создания custom application в Dynatrace и инструментирования приложения с помощью OpenKit ознакомьтесь со страницами ниже, чтобы настроить инструментирование и устранить возможные неполадки.

* [Dynatrace OpenKit libraries on GitHub](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-libraries-on-github "Check out the Dynatrace OpenKit libraries on GitHub.")
* [Методы API Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-api-methods "Read how Dynatrace OpenKit can be used from the developer's point of view.")
* [Логирование Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/dynatrace-openkit-logging "Learn how logging works with OpenKit.")
* [Устранение неполадок инструментирования Dynatrace OpenKit](/managed/ingest-from/extend-dynatrace/openkit/troubleshoot-dynatrace-openkit-instrumentation "Learn how to solve problems that you may encounter when instrumenting Dynatrace OpenKit.")

После того как пользовательское приложение начнёт отправлять данные мониторинга в Dynatrace, эти данные можно анализировать так же, как и для любого другого приложения. Например, можно [изучить пользовательские сессии](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Learn about user session segmentation and filtering attributes."), [проверить метрики пользовательского опыта](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/check-usage-metrics-custom "Learn how to use Dynatrace to check the user experience metrics of your custom application."), [проанализировать веб-запросы](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/analyze-web-requests-custom "Leverage Dynatrace to monitor web requests for your custom applications."), [просмотреть отчёты о сбоях](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/crash-reports-custom "Check the latest crash reports for your custom applications.") и многое другое.

На изображении ниже показана страница обзора нашего тестового пользовательского приложения.

![Custom application overview page](https://dt-cdn.net/images/custom-app-overview-page-1632-8f4bd766b2.png)

Страница обзора пользовательского приложения