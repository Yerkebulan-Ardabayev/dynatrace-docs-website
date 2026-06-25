---
title: Инструментирование мобильных приложений с помощью пакета Dynatrace Xamarin NuGet
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget
scraped: 2026-05-12T11:23:39.531111
---

# Инструментирование мобильных приложений с помощью пакета Dynatrace Xamarin NuGet

# Инструментирование мобильных приложений с помощью пакета Dynatrace Xamarin NuGet

* How-to guide
* 12-min read
* Updated on Apr 16, 2024

Пакет Dynatrace Xamarin NuGet помогает автоматически инструментировать Xamarin-приложение с помощью OneAgent для Android и iOS, а также предоставляет API для [ручного инструментирования](#usage-mobile-agent). Пакет совместим с проектами `Xamarin.iOS`, `Xamarin.Android` и `Xamarin.Forms`.

Устаревание и прекращение поддержки пакета Dynatrace Xamarin NuGet

1 мая 2024 года [Microsoft прекратила поддержку всех Xamarin SDK](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin#microsoft-support). По этой причине пакет Dynatrace Xamarin NuGet признан устаревшим в мае 2024 года. В дальнейшем будут выходить только исправления ошибок и устранение важных проблем безопасности.

Кроме того, в соответствии с [Политикой поддержки Dynatrace](https://www.dynatrace.com/company/trust-center/support-policy/), поддержка пакета Dynatrace Xamarin NuGet будет прекращена в мае 2025 года.

Рекомендуется [перевести проекты Xamarin на .NET](https://learn.microsoft.com/en-gb/dotnet/maui/migration) и использовать [пакет Dynatrace .NET MAUI NuGet](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui "Выполняйте мониторинг .NET MAUI-приложений с помощью Dynatrace OneAgent.") вместо устаревшего пакета Xamarin NuGet.

## Поддерживаемые функции

#### Автоинструментирование

* Пользовательские действия
* События жизненного цикла
* Веб-запросы
* Сбои

#### Ручное инструментирование

* Пользовательские действия
* Веб-запросы
* Значения
* События
* Ошибки
* Сбои
* Тегирование пользователей

## Требования

* **Для Android:**

  + Android версии 5.0+ (уровень API 21+)
  + Xamarin.Android SDK версии 10.1.x+
* **Для iOS:** iOS версии 12+
* **Для Xamarin.Forms:** .NET Standard версии 2.0+

## Настройка пакета

Выполните следующие шаги для настройки пакета Dynatrace Xamarin NuGet в Xamarin-приложении.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Установите пакет Dynatrace Xamarin NuGet**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#install-package "Выполняйте мониторинг Xamarin-приложений с помощью Dynatrace OneAgent.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создайте приложение и получите файл конфигурации**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#installation-dynatrace "Выполняйте мониторинг Xamarin-приложений с помощью Dynatrace OneAgent.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Добавьте файл конфигурации в проект**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#configure-app "Выполняйте мониторинг Xamarin-приложений с помощью Dynatrace OneAgent.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Добавьте метод запуска OneAgent**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#start-method "Выполняйте мониторинг Xamarin-приложений с помощью Dynatrace OneAgent.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

Только для Xamarin.Forms

**Настройте DependencyService для Xamarin.Forms**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#usage-forms "Выполняйте мониторинг Xamarin-приложений с помощью Dynatrace OneAgent.")[![Step 6 optional](https://dt-cdn.net/images/dotted-step-6-fbd29ea893.svg "Шаг 6 необязательный")

**Включите автоматическое инструментирование веб-запросов**](/managed/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#http-client "Выполняйте мониторинг Xamarin-приложений с помощью Dynatrace OneAgent.")

### Шаг 1 Установка пакета NuGet

Добавьте пакет Dynatrace Xamarin NuGet во все необходимые проекты.

1. В Visual Studio щёлкните правой кнопкой мыши основной проект приложения и выберите **Manage NuGet packages**.
2. Найдите [**Dynatrace.OneAgent.Xamarin** на nuget.org](https://www.nuget.org/packages/Dynatrace.OneAgent.Xamarin) и выберите **Add Package**.
3. Установите флажки для всех проектов, в которые требуется добавить пакет NuGet.
4. Нажмите **OK**.

### Шаг 2 Создание приложения и получение файла конфигурации

Создайте новое мобильное приложение в Dynatrace и загрузите файл конфигурации.

1. В Dynatrace перейдите в раздел **Mobile**.
2. Выберите **Create mobile app**.
3. Введите имя приложения и нажмите **Create mobile app**. Откроется страница параметров приложения.
4. В параметрах приложения выберите **Instrumentation wizard** > **Xamarin**.
5. В шаге 2 выберите **Download dynatrace.config.json** для получения файла конфигурации.

### Шаг 3 Добавление файла конфигурации в проект

Добавьте [файл `dynatrace.config.json`](#config-file), загруженный на предыдущем шаге, в проект.

Android

iOS

Добавьте файл `dynatrace.config.json` в каталог `Assets` Android-проекта.

Добавьте файл `dynatrace.config.json` в каталог `Resources` iOS-проекта.

Перед каждой сборкой пакет автоматически создаёт новый файл `Dynatrace.plist` на основе параметров, указанных в файле конфигурации.

### Шаг 4 Добавление метода запуска OneAgent

Метод запуска необходим для старта OneAgent.

Android

iOS

```
using Dynatrace.Xamarin;



Agent.Instance.Start();
```

```
using Dynatrace.Xamarin;



Agent.Instance.Start();
```

### Шаг 5 Настройка `DependencyService` для Xamarin.Forms

Только для Xamarin.Forms

Эта инструкция предназначена для Xamarin.Forms версий 4.7.0+, в которых используется `RegisterSingleton`. Для более ранних версий Xamarin.Forms см. [инструкцию ниже](#xamarin-forms-4-6).

Зарегистрируйте интерфейс при запуске в нативной части Xamarin.Forms-приложения и вставьте следующий код сразу после `Forms.Init()`.

Пример для Android-приложения Forms:

```
using Dynatrace.Xamarin;



Xamarin.Essentials.Platform.Init(this, savedInstanceState);



global::Xamarin.Forms.Forms.Init(this, savedInstanceState);



Xamarin.Forms.DependencyService.RegisterSingleton<IDynatrace>(Agent.Instance);



LoadApplication(new App());
```

Следующий код в Xamarin.Forms-приложении обеспечивает доступ к OneAgent:

```
using Dynatrace.Xamarin;



IDynatrace dynatrace = DependencyService.Get<IDynatrace>();
```

При автоинструментировании необходимо также применить пакет Dynatrace Xamarin NuGet к нативным частям приложения.

Xamarin.Forms 4.6.0 и более ранние версии

Если использование `DependencyService.RegisterSingleton` невозможно из-за версии Xamarin.Forms 4.6.0 или более ранней, существует обходное решение. Следующий фрагмент кода показывает, как это работает для Xamarin.Forms и Android, но его можно применить и к iOS.

Файл `App.xaml.cs` в части Xamarin.Forms:

```
public partial class App : Application



{



static readonly Dictionary<Type, Func<object, object>> factories = new Dictionary<Type, Func<object, object>>();



public App()



{



InitializeComponent();



DependencyResolver.ResolveUsing((type, args) => factories.ContainsKey(type) ? factories[type].Invoke(args) : null);



IDynatrace Dynatrace = DependencyService.Resolve<IDynatrace>();



Dynatrace.Start(null);



}



public static void Register(Type type, Func<object, object> factory)



{



factories[type] = factory;



}



...



}
```

Часть Android, где необходимо вызвать `RegisterSingleton`, должна выглядеть следующим образом:

```
public class MainActivity : global::Xamarin.Forms.Platform.Android.FormsAppCompatActivity



{



protected override void OnCreate(Bundle savedInstanceState)



{



...



Xamarin.Essentials.Platform.Init(this, savedInstanceState);



global::Xamarin.Forms.Forms.Init(this, savedInstanceState);



App.Register(typeof(IDynatrace), (o) => Agent.Instance);



LoadApplication(new App());



}



...



}
```

### Шаг 6 необязательный Включение автоматического инструментирования веб-запросов Необязательный шаг

Дополнительно можно использовать следующий метод для включения автоинструментирования веб-запросов. `HttpMessageHandler`, используемый `HttpClient`, берёт на себя ручное инструментирование веб-запросов.

```
using Dynatrace.Xamarin;



var httpHandler = Agent.Instance.GetHttpMessageHandler();



var httpClient = new HttpClient(httpHandler);
```

Кроме того, можно использовать собственный HTTP-обработчик:

```
using Dynatrace.Xamarin;



var defaultHttpHandler = new HttpClientHandler();



var httpHandler = Agent.Instance.GetHttpMessageHandler(defaultHttpHandler);



var httpClient = new HttpClient(httpHandler);
```

## Ручное инструментирование

В разделах ниже описано, как запустить OneAgent вручную, создавать пользовательские действия, инструментировать веб-запросы и сообщать о значениях, событиях и сбоях.

### Запуск OneAgent

Можно использовать ручной запуск с построителем конфигурации (Android) или словарём конфигурации (iOS).

1. Измените [файл `dynatrace.config.json`](#config-file), чтобы отключить автозапуск OneAgent.

   Android

   iOS

   ```
   {



   "android": {



   "autoStart": {



   "enabled": false



   }



   }



   }
   ```

   ```
   {



   "ios": {



   "DTXAutoStart": false



   }



   }
   ```

   Не добавляйте дополнительные свойства в файл конфигурации. В противном случае сборка завершится ошибкой.
2. Запустите OneAgent вручную и передайте необходимые свойства.

   Android

   iOS

   ```
   using Dynatrace.Xamarin;



   Agent.Instance.Start(new ConfigurationBuilder("<insertBeaconURL>","<insertApplicationID>") .BuildConfiguration());
   ```

   ```
   using Dynatrace.Xamarin;



   var configDict = new Dictionary<string, object>();



   configDict.Add("DTXApplicationID", "<insertApplicationID>");



   configDict.Add("DTXBeaconURL", "<insertBeaconURL");



   Agent.Instance.Start(configDict);
   ```

### Создание пользовательских действий

Можно создавать пользовательские действия и обогащать их дополнительной информацией: значениями, событиями и ошибками.

Вызовите `EnterAction` для начала пользовательского действия и `LeaveAction` для его завершения. Время измеряется автоматически.

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



//Perform the action and whatever else is needed.



myAction.LeaveAction();
```

Для мобильного пользовательского действия максимальная длина имени составляет 250 символов.

Сведения об именовании пользовательских действий см. по ссылкам: [Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#user-action-naming "Настройте плагин Dynatrace Android Gradle для изменения возможностей мониторинга OneAgent.") и [iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios#user-action-naming "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.").

Если для приложения включён [режим согласия пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе."), это может повлиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не передаваемых в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе.").

### Создание дочерних действий

Помимо создания самостоятельных пользовательских действий, можно также создавать [дочерние действия](/managed/observe/digital-experience/rum-concepts/user-actions#child-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с приложением.").

Дочерние действия аналогичны родительским пользовательским действиям. При закрытии родительского действия все его дочерние действия закрываются автоматически.

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



var mySubAction = myAction.EnterAction("Tap on Confirm again");



//Perform the action and whatever else is needed.



mySubAction.LeaveAction();



myAction.LeaveAction();
```

Для мобильного пользовательского действия максимальная длина имени составляет 250 символов.

Количество дочерних действий, прикреплённых к пользовательскому действию, не ограничено. Однако следует учитывать, что доступен только один уровень дочерних действий: нельзя создать дочернее действие для другого дочернего действия (у дочерних действий не может быть собственных дочерних действий). Также см. раздел [Структура пользовательской сессии для отдельного пользователя](/managed/observe/digital-experience/rum-concepts/user-session#session-structure-dep-on-app-type "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её продолжительность и многое другое.").

Дочерние действия не отображаются на [странице сведений о пользовательской сессии](/managed/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Узнайте о сегментации и фильтрации пользовательских сессий."), но их можно просмотреть на [странице водопадного анализа](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Узнайте, как анализировать все данные мониторинга пользовательских действий с помощью водопадного анализа.") для соответствующего пользовательского действия.

### Отмена пользовательских действий

Если требуется отменить уже созданное, но ещё не закрытое пользовательское действие, вызовите `Cancel`. Отмена действия удаляет все связанные с ним данные: все переданные значения, события и ошибки отбрасываются; все дочерние действия отменяются.

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



// Action is canceled



myAction.Cancel();
```

Невозможно отменить уже закрытое действие, поэтому вызов `Cancel` после `LeaveAction` недопустим для одного действия. То же правило применяется к закрытию отменённого действия: нельзя вызвать `LeaveAction` после `Cancel` для одного действия.

### Инструментирование веб-запросов

Используйте следующий фрагмент кода для инструментирования веб-запросов:

```
using Dynatrace.Xamarin;



// Create an action



var webAction = Agent.Instance.EnterAction(actionName: "WebRequest Action");



// Generate a new unique tag associated with the web request action



string requestTag = webAction.GetRequestTag(url);



string requestTagHeader = webAction.GetRequestTagHeader();



// Place the Dynatrace HTTP header on your web request



httpClient.DefaultRequestHeaders.Add(requestTagHeader, requestTag);



// Generate a WebRequestTiming object based on the unique tag



WebRequestTiming timing = (WebRequestTiming)Agent.Instance.GetWebRequestTiming(requestTag, url);



// Start web request timing before the HTTP request is sent



timing.StartWebRequestTiming();



try



{



var response = await httpClient.GetAsync(url);



// Stop web request timing when the HTTP response is received and the response body is obtained



timing.StopWebRequestTiming(url, (int)response.StatusCode, response.ReasonPhrase);



}



catch (HttpRequestException exception)



{



// Stop web request timing when a connection exception occurs



timing.StopWebRequestTiming(url, -1, exception.ToString());



}



finally



{



// Leave an action



webAction.LeaveAction();



}
```

### Передача значения

Метод `reportValue` позволяет передавать пары «ключ-значение» с метаданными, которые впоследствии можно просматривать в веб-интерфейсе Dynatrace и преобразовывать в [свойства пользовательских действий и сессий](/managed/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "Свойства пользовательских действий и сессий — пары «ключ-значение» с метаданными — обеспечивают расширенную видимость и более глубокий анализ опыта конечных пользователей."). Передаваемые значения должны быть частью пользовательского действия.

Можно передавать значения следующих типов данных:

* `int`
* `double`
* `string`

```
ReportValue(valueName: string, value: int);



ReportValue(valueName: string, value: double);



ReportValue(valueName: string, value: string);
```

Например, для передачи значения типа `string` в рамках действия `Tap on Confirm` используйте следующий код:

```
using Dynatrace.Xamarin;



var myAction = Agent.Instance.EnterAction("Tap on Confirm");



myAction.ReportValue("Customer type", "Gold");



myAction.LeaveAction();
```

Для просмотра переданных значений в веб-интерфейсе Dynatrace перейдите к сведениям о пользовательском действии, которое должно содержать эти метаданные, и прокрутите вниз до раздела **Reported values**.

![User action details page with SDK-reported values](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

Страница сведений о пользовательском действии с переданными значениями SDK

Чтобы добавить свойства действий и сессий на основе переданных значений и затем использовать их для создания мощных запросов, сегментации и агрегации, см. раздел [Определение свойств пользовательских действий и сессий для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Передавайте метаданные в Dynatrace и определяйте свойства действий и сессий для отслеживаемых мобильных приложений.").

Если для приложения включён [режим согласия пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе."), это может повлиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не передаваемых в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе.").

### Передача события

Для любого открытого действия можно передать событие. Используйте следующий вызов API:

```
ReportEvent(eventName: string);
```

Если для приложения включён [режим согласия пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе."), это может повлиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не передаваемых в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе.").

### Передача ошибки

Для передачи [ошибки](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Узнайте о событиях пользователей и ошибках, а также о типах событий, фиксируемых Dynatrace.") используйте метод `ReportError`.

```
ReportError(errorName: string, errorCode: number);
```

Если для приложения включён [режим согласия пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе."), это может повлиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не передаваемых в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе.").

### Передача трассировки стека ошибки

Для передачи трассировки стека ошибки используйте следующий вызов API:

```
using Dynatrace.Xamarin;



Agent.Instance.ReportErrorStacktrace("Error_Class", "Error_Value", "Error_Reason", "Error_Stacktrace");
```

### Передача сведений о сбое

Для передачи сведений о [сбое](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Узнайте о событиях пользователей и ошибках, а также о типах событий, фиксируемых Dynatrace.") используйте следующий вызов API.

```
using Dynatrace.Xamarin;



Agent.Instance.ReportCrash("CrashWithoutException", "Crash_Reason", "Crash_Stacktrace");
```

Также можно использовать объект исключения:

```
using Dynatrace.Xamarin;



Agent.Instance.ReportCrashWithException("CrashWithExceptionObj", exception);
```

Время отправки сведений о сбое в Dynatrace зависит от операционной системы мобильного приложения.

* **Android**

  Как правило, сведения о сбое отправляются сразу после сбоя, поэтому пользователю не требуется перезапускать приложение. Однако в некоторых случаях приложение необходимо открыть повторно в течение 10 минут, чтобы отчёт о сбое был отправлен. Обратите внимание, что Dynatrace не отправляет отчёты о сбоях, которые старше 10 минут (такие отчёты уже не могут быть скоррелированы в кластере Dynatrace).
* **iOS**

  Сведения о сбое отправляются только при повторном открытии мобильного приложения пользователем (то есть при следующем запуске). Однако если пользователь не откроет приложение в течение 10 минут, отчёт о сбое будет удалён. Это связано с тем, что Dynatrace не отправляет отчёты о сбоях, которые старше 10 минут (такие отчёты уже не могут быть скоррелированы в кластере Dynatrace).

Передача сведений о сбое принудительно завершает пользовательскую сессию. Все последующие действия включаются в новую пользовательскую сессию.

Только для Android При использовании автоматической отчётности о сбоях Visual Studio может перехватить исключение раньше OneAgent. Если Dynatrace не сообщает о сбоях в вашу среду, убедитесь, что [параметр отладки в Visual Studio не используется](#debugger-turn-off). В противном случае отладчик перехватывает сбой и ничего не передаётся в среду Dynatrace.

### Тегирование конкретных пользователей

Каждого пользователя приложения можно пометить уникальным именем. Это позволяет выполнять поиск и фильтрацию конкретных пользовательских сессий, а также анализировать поведение отдельных пользователей со временем. Подробнее см. в разделе [Тегирование пользователей](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Узнайте о событиях пользователей и ошибках, а также о типах событий, фиксируемых Dynatrace.").

Для пометки текущей сессии конкретным именем выполните следующий вызов API:

```
using Dynatrace.Xamarin;



Agent.Instance.IdentifyUser("John Smith");
```

OneAgent для Android версии 237+ OneAgent для iOS версии 235+ Сессии, разделённые из-за простоя или таймаута продолжительности, автоматически повторно тегируются.

Когда OneAgent завершает тегированную сессию из-за достижения установленного лимита или простоя пользователя, последующая сессия тегируется автоматически. Повторно предоставлять идентификационные данные пользователя не требуется.

Однако следует учитывать, что OneAgent не выполняет повторное тегирование в следующих случаях:

* Когда тегированная пользовательская сессия явно завершается через [`endVisit`](#end-session)
* Когда пользователь или мобильная операционная система закрывает или принудительно останавливает приложение
* Когда OneAgent завершает текущую пользовательскую сессию и создаёт новую после изменения параметров конфиденциальности

Узнайте, когда OneAgent завершает мобильную пользовательскую сессию, в разделе [Пользовательские сессии > Завершение сессии](/managed/observe/digital-experience/rum-concepts/user-session#user-session-end--mobile-apps "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её продолжительность и многое другое.").

Если для приложения включён [режим согласия пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе."), это может повлиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не передаваемых в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе.").

### Завершение сессии

Сессию можно принудительно завершить через вызов API. При этом все открытые действия закрываются и начинается новая сессия.

```
using Dynatrace.Xamarin;



Agent.Instance.EndVisit();
```

### Настройка конфиденциальности данных (режим согласия)

В режиме согласия пользователя каждый пользователь приложения может установить свои предпочтения в отношении конфиденциальности данных и решить, хочет ли он передавать свою информацию. При включённом режиме согласия необходимо запрашивать у каждого пользователя разрешение на сбор его данных и сохранять его предпочтения. Подробнее см. в разделе [Режим согласия пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе.").

#### Включение режима согласия пользователя

Для активации режима согласия пользователя установите свойство `userOptIn` (Android) или [ключ конфигурации `DTXUserOptIn`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "С помощью ключей конфигурации можно выполнить тонкую настройку автоинструментирования iOS-приложений.") (iOS) в значение `true` в [файле `dynatrace.config.json`](#config-file).

#### Получение предпочтений конфиденциальности пользователя

Можно получить предпочтения конфиденциальности конкретного пользователя.

Для получения текущей конфигурации `UserPrivacyOptions` используйте следующий вызов API:

```
using Dynatrace.Xamarin;



// Get the UserPrivacyOptions object



UserPrivacyOptions currentOptions = Agent.Instance.GetUserPrivacyOptions();



// Get the individual settings for DataCollectionLevel and crash reporting



bool crashOptedIn = Agent.Instance.GetUserPrivacyOptions().CrashReportingOptedIn;



DataCollectionLevel dataCollectionLevel = Agent.Instance.GetUserPrivacyOptions().DataCollectionLevel;
```

#### Изменение предпочтений конфиденциальности пользователя

Можно скорректировать предпочтения конфиденциальности на основе решения конкретного пользователя.

Для задания новых параметров объекта `UserPrivacyOptions` используйте следующий код:

```
using Dynatrace.Xamarin;



// Creating a new UserPrivacyOptions object requires setting the two parameters of DataCollectionLevel and crash reporting



UserPrivacyOptions options = new UserPrivacyOptions(DataCollectionLevel.Performance, false);



// Update the options with the setter



// Set a data collection level (user allowed you to capture performance and personal data)



options.DataCollectionLevel = DataCollectionLevel.UserBehavior;



// Allow crash reporting (user allowed you to collect information on crashes)



options.CrashReportingOptedIn = true;



// Get the values of the configuration with the getter



options.DataCollectionLevel;



options.CrashReportingOptedIn;



// Get the UserPrivacyOptions object



UserPrivacyOptions currentOptions = Agent.Instance.GetUserPrivacyOptions();
```

Для применения новой конфигурации `UserPrivacyOptions` используйте следующий код:

```
using Dynatrace.Xamarin;



UserPrivacyOptions options = new UserPrivacyOptions(DataCollectionLevel.UserBehavior, true);



Agent.Instance.ApplyUserPrivacyOptions(options);
```

Возможные значения [уровня сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте параметры конфиденциальности Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям законодательства о защите данных в вашем регионе."):

* `Off`
* `Performance`
* `UserBehavior`

### Передача GPS-местоположения

Можно передавать широту и долготу.

```
SetGPSLocation(latitude: double, longitude: double);
```

## Файл конфигурации

Файл конфигурации `dynatrace.config.json` содержит идентификатор приложения, URL маяка и ряд других параметров.

* Можно [загрузить этот файл из Dynatrace](#installation-dynatrace) или создать вручную.
* Если не добавить файл конфигурации, содержащий хотя бы URL маяка и идентификатор приложения, сборка завершится ошибкой. В качестве альтернативы используйте [ручной запуск](#start-agent) с построителем конфигурации (Android) или словарём конфигурации (iOS).
* При использовании конкретной конфигурации сборки — например, `Debug`, `Release` или пользовательской — пакет ищет в каталоге `Assets` (Android) или `Resources` (iOS) файл конфигурации с именем `dynatrace<Configuration>.config.json`. Например, при использовании конфигурации сборки `Debug` пакет ищет файл `dynatraceDebug.config.json`.
* Для указания пользовательского пути к конфигурации задайте его через свойство `DynatraceConfigurationFile`.

  Создайте файл `Directory.Build.props` в каталоге проекта Android/iOS (или общем):

  ```
  <Project>



  <PropertyGroup>



  <DynatraceConfigurationFile>CUSTOM_PATH/dynatrace.config.json</DynatraceConfigurationFile>



  </PropertyGroup>



  </Project>
  ```

В итоге конфигурация применяется в следующем порядке:

1. Пользовательский путь через свойство `DynatraceConfigurationFile`
2. Файл, специфичный для конфигурации, например `dynatrace<Configuration>.config.json`
3. Имя по умолчанию `dynatrace.config.json`

Ниже приведена структура файла `dynatrace.config.json` для Android и iOS.

Android

iOS

```
{



"android": {



"autoStart": {



"applicationId": "<insertApplicationID>",



"beaconUrl": "<insertBeaconURL>"



},



"userOptIn": true,



"agentBehavior": {



"startupLoadBalancing": true



}



}



}
```

```
{



"ios": {



"DTXApplicationId": "<insertApplicationID>",



"DTXBeaconUrl": "<insertBeaconURL>",



"DTXUserOptIn": true,



"DTXStartupLoadBalancing": true



}



}
```

Никогда не используйте точечную нотацию в файле конфигурации. Всегда используйте полный стиль скобок.

## Включение журналов отладки OneAgent

Если инструментирование выполнено и приложение запускается, но данные не появляются в среде Dynatrace, необходимо провести более глубокую диагностику. Для начала лучше всего собрать журналы, прежде чем открывать обращение в службу поддержки.

Android

iOS

Обновите [файл `dynatrace.config.json`](#config-file) для включения журналов отладки OneAgent.

```
{



"android": {



"autoStart": {



"applicationId": "<insertApplicationID>",



"beaconUrl": "<insertBeaconURL>"



},



"userOptIn": true,



"debug": {



"agentLogging": true



}



}



}
```

Добавьте следующий фрагмент конфигурации в [файл `dynatrace.config.json`](#config-file):

```
{



"ios": {



"DTXApplicationId": "<insertApplicationID>",



"DTXBeaconUrl": "<insertBeaconURL>",



"DTXUserOptIn": true,



"DTXLogLevel": "ALL"



}



}
```

## Включение журналов отладки сборки для Android

Только для Android

При сбое инструментирования Android, скорее всего, потребуется открыть обращение в службу поддержки и предоставить журналы отладки сборки. Для этого необходимо задать свойство `DynatraceInstrumentationLogging` и изменить уровень детализации журнала сборки на `Diagnostic`.

1. Задайте свойство `DynatraceInstrumentationLogging`. Выберите один из следующих способов:

   * Создайте файл `Directory.Build.props` в каталоге Android-проекта:

   ```
   <Project>



   <PropertyGroup>



   <DynatraceInstrumentationLogging>true</DynatraceInstrumentationLogging>



   </PropertyGroup>



   </Project>
   ```

   * Добавьте свойство `DynatraceInstrumentationLogging` в файл `.csproj` проекта. Вставьте его в подходящую `PropertyGroup` в зависимости от выполняемой конфигурации.
2. Измените детализацию вывода сборки на `Diagnostic`. Подробнее см. в документации Microsoft о том, как [изменить объём информации в журнале сборки](https://docs.microsoft.com/en-us/visualstudio/ide/how-to-view-save-and-configure-build-log-files?view=vs-2019#to-change-the-amount-of-information-included-in-the-build-log).
3. Пересоберите проект.
4. Прикрепите журналы сборки к обращению в службу поддержки для дальнейшего анализа.

## Устранение неполадок

Если проблему не удаётся решить, обратитесь к разделу [Mobile applications: Issues with Dynatrace Xamarin NuGet package](https://dt-url.net/xn638zc) в сообществе Dynatrace.

## Связанные темы

* [Инструментирование Android-приложений](/managed/observe/digital-experience/mobile-applications/instrument-android-app "Узнайте, как инструментировать мониторинг мобильных приложений на Android, как настраивать инструментирование и многое другое.")
* [Инструментирование iOS-приложений](/managed/observe/digital-experience/mobile-applications/instrument-ios-app "Инструментируйте мониторинг мобильных приложений для iOS, настраивайте автоинструментирование и собирайте дополнительные данные через ручное инструментирование.")