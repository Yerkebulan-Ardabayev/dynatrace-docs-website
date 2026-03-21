---
title: Инструментирование мобильных приложений с помощью Dynatrace Xamarin NuGet пакета
source: https://www.dynatrace.com/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget
scraped: 2026-03-05T21:26:26.299483
---

Dynatrace Xamarin NuGet пакет помогает автоматически инструментировать ваше Xamarin приложение с помощью OneAgent для Android и iOS, а также предоставляет API для [ручного инструментирования](#usage-mobile-agent). Пакет совместим с проектами `Xamarin.iOS`, `Xamarin.Android` и `Xamarin.Forms`.

Прекращение поддержки Dynatrace Xamarin NuGet пакета

1 мая 2024 года [Microsoft прекратит поддержку всех Xamarin SDK](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin#microsoft-support). По этой причине мы объявляем о прекращении поддержки Dynatrace Xamarin NuGet пакета в мае 2024 года. Мы сообщим вам, в какой версии пакета мы будем только исправлять ошибки и устранять важные проблемы безопасности.

Кроме того, в соответствии с [политикой поддержки Dynatrace](https://www.dynatrace.com/company/trust-center/support-policy/), мы прекратим поддержку Dynatrace Xamarin NuGet пакета в мае 2025 года.

Мы рекомендуем вам [обновить ваши Xamarin проекты до .NET](https://learn.microsoft.com/en-gb/dotnet/maui/migration) и использовать [Dynatrace .NET MAUI NuGet пакет](maui.md "Мониторинг приложений .NET MAUI с помощью Dynatrace OneAgent.") вместо устаревшего Xamarin NuGet пакета.

## Поддерживаемые функции

#### Автоматическое инструментирование

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

  + Android версии 5.0+ (API 21+)
  + Xamarin.Android SDK версии 10.1.x+
* **Для iOS:** iOS версии 12+
* **Для Xamarin.Forms:** .NET Standard версии 2.0+

## Настройка пакета

Выполните следующие шаги для настройки Dynatrace Xamarin NuGet пакета для вашего Xamarin приложения.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Установите Dynatrace Xamarin NuGet пакет**](xamarin-nuget.md#install-package "Мониторинг Xamarin приложений с помощью Dynatrace OneAgent.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создайте приложение и получите файл конфигурации**](xamarin-nuget.md#installation-dynatrace "Мониторинг Xamarin приложений с помощью Dynatrace OneAgent.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Добавьте файл конфигурации в ваш проект**](xamarin-nuget.md#configure-app "Мониторинг Xamarin приложений с помощью Dynatrace OneAgent.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Добавьте метод запуска OneAgent**](xamarin-nuget.md#start-method "Мониторинг Xamarin приложений с помощью Dynatrace OneAgent.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

Только для Xamarin.Forms

**Настройте Xamarin.Forms DependencyService**](xamarin-nuget.md#usage-forms "Мониторинг Xamarin приложений с помощью Dynatrace OneAgent.")[![Шаг 6 (необязательно)](https://dt-cdn.net/images/dotted-step-6-fbd29ea893.svg "Шаг 6 (необязательно)")

**Включите автоматическое инструментирование веб-запросов**](xamarin-nuget.md#http-client "Мониторинг Xamarin приложений с помощью Dynatrace OneAgent.")

### Шаг 1. Установка NuGet пакета

Добавьте Dynatrace Xamarin NuGet пакет во все необходимые проекты.

1. В Visual Studio щёлкните правой кнопкой мыши на основном проекте вашего приложения и выберите **Manage NuGet packages**.
2. Найдите [**Dynatrace.OneAgent.Xamarin** на nuget.org](https://www.nuget.org/packages/Dynatrace.OneAgent.Xamarin) и выберите **Add Package**.
3. Установите флажки для всех проектов, в которые вы хотите добавить NuGet пакет.
4. Выберите **OK**.

### Шаг 2. Создание приложения и получение файла конфигурации

Создайте новое мобильное приложение в Dynatrace и скачайте файл конфигурации.

1. В Dynatrace перейдите в **Mobile**.
2. Выберите **Create mobile app**.
3. Введите имя вашего приложения и выберите **Create mobile app**. Откроется страница настроек приложения.
4. В настройках приложения выберите **Instrumentation wizard** > **Xamarin**.
5. На шаге 2 выберите **Download dynatrace.config.json**, чтобы получить файл конфигурации.

### Шаг 3. Добавление файла конфигурации в проект

Добавьте [файл `dynatrace.config.json`](#config-file), который вы скачали на предыдущем шаге, в ваш проект.

Android

iOS

Добавьте файл `dynatrace.config.json` в директорию `Assets` вашего Android-проекта.

Добавьте файл `dynatrace.config.json` в директорию `Resources` вашего iOS-проекта.

Перед каждой сборкой наш пакет автоматически создаёт новый файл `Dynatrace.plist` на основе параметров, заданных в файле конфигурации.

### Шаг 4. Добавление метода запуска OneAgent

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

### Шаг 5. Настройка Xamarin.Forms `DependencyService`

Только для Xamarin.Forms

Эта инструкция для Xamarin.Forms версий 4.7.0+, которые используют `RegisterSingleton`. Для более ранних версий Xamarin.Forms см. [инструкцию ниже](#xamarin-forms-4-6).

Зарегистрируйте интерфейс при запуске в нативной части вашего Xamarin.Forms приложения и вставьте следующий код сразу после `Forms.Init()`.

Следующий пример для Android Forms приложения:

```
using Dynatrace.Xamarin;


Xamarin.Essentials.Platform.Init(this, savedInstanceState);


global::Xamarin.Forms.Forms.Init(this, savedInstanceState);


Xamarin.Forms.DependencyService.RegisterSingleton<IDynatrace>(Agent.Instance);


LoadApplication(new App());
```

Следующий код в вашем Xamarin.Forms приложении позволяет получить доступ к OneAgent:

```
using Dynatrace.Xamarin;


IDynatrace dynatrace = DependencyService.Get<IDynatrace>();
```

При автоматическом инструментировании вам также необходимо применить Dynatrace Xamarin NuGet пакет к нативным частям вашего приложения.

Xamarin.Forms 4.6.0 и более ранние версии

Если вы не можете использовать `DependencyService.RegisterSingleton`, поскольку версия Xamarin.Forms 4.6.0 или более ранняя, существует обходное решение. Следующий фрагмент кода показывает, как это работает для Xamarin.Forms и Android, но вы легко можете применить его и для iOS.

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

Часть Android, где нужно вызвать `RegisterSingleton`, должна выглядеть так:

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

### Шаг 6 (необязательно). Включение автоматического инструментирования веб-запросов (необязательно)

Вы можете использовать следующий метод для включения автоматического инструментирования веб-запросов. `HttpMessageHandler`, используемый `HttpClient`, берёт на себя ручное инструментирование веб-запросов.

```
using Dynatrace.Xamarin;


var httpHandler = Agent.Instance.GetHttpMessageHandler();


var httpClient = new HttpClient(httpHandler);
```

Кроме того, вы можете использовать собственный HTTP-обработчик:

```
using Dynatrace.Xamarin;


var defaultHttpHandler = new HttpClientHandler();


var httpHandler = Agent.Instance.GetHttpMessageHandler(defaultHttpHandler);


var httpClient = new HttpClient(httpHandler);
```

## Ручное инструментирование

В разделах ниже описано, как запустить OneAgent вручную, создать пользовательские действия, инструментировать веб-запросы, а также отправлять значения, события и информацию о сбоях.

### Запуск OneAgent

Вы можете использовать ручной запуск с помощью конфигурационного построителя (Android) или словаря конфигурации (iOS).

1. Измените [файл `dynatrace.config.json`](#config-file), чтобы отключить автоматический запуск OneAgent.

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

   Не добавляйте дополнительные свойства в файл конфигурации. В противном случае сборка завершится с ошибкой.
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

Вы можете создавать пользовательские действия и дополнять их информацией, такой как значения, события и ошибки.

Вызовите `EnterAction`, чтобы начать пользовательское действие, и `LeaveAction`, чтобы его завершить. Время измеряется автоматически.

```
using Dynatrace.Xamarin;


var myAction = Agent.Instance.EnterAction("Tap on Confirm");


//Perform the action and whatever else is needed.


myAction.LeaveAction();
```

Максимальная длина имени мобильного пользовательского действия или автоматически сгенерированного пользовательского действия составляет 250 символов.

Информацию об именовании пользовательских действий смотрите по следующим ссылкам: [Android](../instrument-android-app/instrumentation-via-plugin/monitoring-capabilities.md#user-action-naming "Настройте плагин Dynatrace Android Gradle для управления возможностями мониторинга OneAgent.") и [iOS](../instrument-ios-app/customization/oneagent-sdk-for-ios.md#user-action-naming "Расширьте мониторинг мобильного пользовательского опыта с помощью OneAgent SDK для iOS.").

Когда для вашего приложения включён [режим согласия пользователя](../additional-configuration/configure-rum-privacy-mobile.md#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона."), это может повлиять на тегирование пользователей и отправку пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не отправляемые в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. [Уровни сбора данных](../additional-configuration/configure-rum-privacy-mobile.md#data-collection-levels "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона.").

### Создание дочерних действий

Помимо создания самостоятельных пользовательских действий, вы также можете создавать [дочерние действия](../../rum-concepts/user-actions.md#child-actions "Узнайте, что такое пользовательские действия и как они помогают понять поведение пользователей.").

Дочерние действия аналогичны родительским пользовательским действиям. При закрытии родительского действия все его дочерние действия автоматически закрываются.

```
using Dynatrace.Xamarin;


var myAction = Agent.Instance.EnterAction("Tap on Confirm");


var mySubAction = myAction.EnterAction("Tap on Confirm again");


//Perform the action and whatever else is needed.


mySubAction.LeaveAction();


myAction.LeaveAction();
```

Максимальная длина имени мобильного пользовательского действия или автоматически сгенерированного пользовательского действия составляет 250 символов.

Количество дочерних действий, прикреплённых к пользовательскому действию, не ограничено. Однако обратите внимание, что допускается только один уровень вложенности дочерних действий — вы не можете создать дочернее действие для другого дочернего действия (дочерние действия не могут иметь собственных дочерних действий). Также см. [Структура пользовательской сессии для отдельного пользователя](../../rum-concepts/user-session.md#session-structure-dep-on-app-type "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её продолжительность и многое другое.").

Дочерние действия не отображаются на [странице деталей пользовательской сессии](../../session-segmentation/new-user-sessions.md#session-details-page "Узнайте о сегментации пользовательских сессий и атрибутах фильтрации."), но вы можете просмотреть их на [странице каскадного анализа](../../web-applications/analyze-and-use/waterfall-analysis.md "Узнайте, как анализировать данные мониторинга пользовательских действий с помощью каскадного анализа.") для пользовательского действия, к которому прикреплены эти дочерние действия.

### Отмена пользовательских действий

Если вам нужно отменить уже созданное, но ещё не закрытое пользовательское действие, вызовите `Cancel`. Отмена действия удаляет все связанные с ним данные: все отправленные значения, события и ошибки отбрасываются; все дочерние действия отменяются.

```
using Dynatrace.Xamarin;


var myAction = Agent.Instance.EnterAction("Tap on Confirm");


// Action is canceled


myAction.Cancel();
```

Вы не можете отменить закрытое действие, поэтому вызов `Cancel` после `LeaveAction` невозможен для одного и того же действия. То же самое относится к закрытию отменённого действия: вы не можете вызвать `LeaveAction` после использования `Cancel` для того же действия.

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

### Отправка значения

Метод `reportValue` позволяет отправлять пары «ключ-значение» метаданных, которые вы можете затем просматривать в веб-интерфейсе Dynatrace и преобразовывать в [свойства пользовательских действий и сессий](../analyze-and-use/action-and-session-properties-mobile.md "Свойства пользовательских действий и сессий — это пары метаданных «ключ-значение», которые обеспечивают дополнительную видимость и глубокий анализ пользовательского опыта."). Отправляемые значения должны быть частью пользовательского действия.

Вы можете отправлять значения следующих типов данных:

* `int`
* `double`
* `string`

```
ReportValue(valueName: string, value: int);


ReportValue(valueName: string, value: double);


ReportValue(valueName: string, value: string);
```

Например, чтобы отправить значение типа `string` в рамках действия `Tap on Confirm`, используйте следующий код:

```
using Dynatrace.Xamarin;


var myAction = Agent.Instance.EnterAction("Tap on Confirm");


myAction.ReportValue("Customer type", "Gold");


myAction.LeaveAction();
```

Чтобы просмотреть отправленные значения в веб-интерфейсе Dynatrace, перейдите к деталям пользовательского действия, которое должно содержать эти метаданные, и прокрутите вниз до раздела **Reported values**.

![Страница деталей пользовательского действия с отправленными через SDK значениями](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

Чтобы добавить свойства действий и сессий на основе отправленных значений, а затем использовать эти свойства для создания мощных запросов, сегментаций и агрегаций, см. [Определение свойств пользовательских действий и сессий для мобильных приложений](../additional-configuration/define-mobile-action-and-session-properties.md "Отправляйте метаданные в Dynatrace и определяйте свойства действий и сессий для ваших мобильных приложений.").

Когда для вашего приложения включён [режим согласия пользователя](../additional-configuration/configure-rum-privacy-mobile.md#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона."), это может повлиять на тегирование пользователей и отправку пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не отправляемые в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. [Уровни сбора данных](../additional-configuration/configure-rum-privacy-mobile.md#data-collection-levels "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона.").

### Отправка события

Для любого открытого действия вы можете отправить событие. Используйте следующий вызов API:

```
ReportEvent(eventName: string);
```

Если вы хотите отправлять самостоятельные события с большим количеством дополнительной информации, см. [Отправка бизнес-события](#report-business-event).

Когда для вашего приложения включён [режим согласия пользователя](../additional-configuration/configure-rum-privacy-mobile.md#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона."), это может повлиять на тегирование пользователей и отправку пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не отправляемые в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. [Уровни сбора данных](../additional-configuration/configure-rum-privacy-mobile.md#data-collection-levels "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона.").

### Отправка ошибки

Чтобы отправить [ошибку](../../rum-concepts/user-and-error-events.md#error "Узнайте о пользовательских событиях и событиях ошибок, а также о типах событий, фиксируемых Dynatrace."), используйте метод `ReportError`.

```
ReportError(errorName: string, errorCode: number);
```

Когда для вашего приложения включён [режим согласия пользователя](../additional-configuration/configure-rum-privacy-mobile.md#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона."), это может повлиять на тегирование пользователей и отправку пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не отправляемые в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. [Уровни сбора данных](../additional-configuration/configure-rum-privacy-mobile.md#data-collection-levels "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона.").

### Отправка трассировки стека ошибки

Чтобы отправить трассировку стека ошибки, используйте следующий вызов API:

```
using Dynatrace.Xamarin;


Agent.Instance.ReportErrorStacktrace("Error_Class", "Error_Value", "Error_Reason", "Error_Stacktrace");
```

### Отправка информации о сбое

Чтобы отправить информацию о [сбое](../../rum-concepts/user-and-error-events.md#crash "Узнайте о пользовательских событиях и событиях ошибок, а также о типах событий, фиксируемых Dynatrace."), используйте следующий вызов API.

```
using Dynatrace.Xamarin;


Agent.Instance.ReportCrash("CrashWithoutException", "Crash_Reason", "Crash_Stacktrace");
```

Вы также можете использовать объект исключения:

```
using Dynatrace.Xamarin;


Agent.Instance.ReportCrashWithException("CrashWithExceptionObj", exception);
```

Время отправки деталей сбоя в Dynatrace зависит от операционной системы вашего мобильного приложения.

* **Android**

  Как правило, детали сбоя отправляются сразу после сбоя, поэтому пользователю не нужно перезапускать приложение. Однако в некоторых случаях приложение необходимо повторно открыть в течение 10 минут, чтобы отчёт о сбое был отправлен. Обратите внимание, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (такие отчёты уже не могут быть скоррелированы на кластере Dynatrace).
* **iOS**

  Детали сбоя отправляются только при повторном открытии мобильного приложения (то есть при следующем запуске). Однако, если пользователь не откроет приложение в течение 10 минут, отчёт о сбое удаляется. Это связано с тем, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (такие отчёты уже не могут быть скоррелированы на кластере Dynatrace).

Отправка информации о сбое принудительно завершает пользовательскую сессию. Все последующие действия включаются в новую пользовательскую сессию.

Только для Android. При использовании автоматической отправки отчётов о сбоях Visual Studio может перехватить исключение раньше OneAgent. Если вы заметили, что Dynatrace не отправляет отчёты о сбоях в вашу среду, убедитесь, что [вы не используете режим отладки в Visual Studio](#debugger-turn-off). В противном случае отладчик перехватывает сбой и ничего не отправляется в вашу среду Dynatrace.

### Отправка бизнес-события

Dynatrace SaaS версии 1.253+

С помощью `sendBizEvent` вы можете отправлять бизнес-события. Это самостоятельные события, поскольку Dynatrace отправляет их отдельно от пользовательских действий или сессий.

Бизнес-события фиксируются только для мониторимых сессий. Когда OneAgent отключён с помощью специального флага или из-за [контроля стоимости и трафика](../additional-configuration/configure-cost-and-traffic-control-mobile.md "Используйте настройку контроля стоимости и трафика в Dynatrace для снижения использования сессий мобильных приложений."), бизнес-события для таких сессий не отправляются. Обратите внимание, что это поведение может измениться в будущем, и бизнес-события смогут отправляться в Dynatrace независимо от мониторинга сессий.

Для получения дополнительной информации о бизнес-событиях см. [Бизнес-наблюдаемость](../../../business-observability.md "Основные концепции, настройка и конфигурация, а также сценарии использования Dynatrace Business Observability").

```
using Dynatrace.Xamarin;


var attributes = new Dictionary<string, JsonValue>();


attributes.Add("event.name", "Confirmed Booking");


attributes.Add("screen", "booking-confirmation");


attributes.Add("product", "Danube Anna Hotel");


attributes.Add("amount", 358.35);


attributes.Add("currency", "USD");


attributes.Add("reviewScore", 4.8);


attributes.Add("arrivalDate", "2022-11-05");


attributes.Add("departureDate", "2022-11-15");


attributes.Add("journeyDuration", 10);


attributes.Add("adultTravelers", 2);


attributes.Add("childrenTravelers", 0);


Agent.Instance.SendBizEvent("com.easytravel.funnel.booking-finished", attributes);
```

### Тегирование конкретных пользователей

Вы можете тегировать каждого пользователя вашего приложения уникальным именем. Это позволяет искать и фильтровать конкретные пользовательские сессии и анализировать поведение отдельных пользователей с течением времени. Подробнее см. [Тегирование пользователей](../../rum-concepts/user-and-error-events.md#user-tagging "Узнайте о пользовательских событиях и событиях ошибок, а также о типах событий, фиксируемых Dynatrace.").

Выполните следующий вызов API, чтобы присвоить тег текущей сессии:

```
using Dynatrace.Xamarin;


Agent.Instance.IdentifyUser("John Smith");
```

OneAgent для Android версии 237+ OneAgent для iOS версии 235+ Сессии, разделённые из-за таймаута бездействия или длительности, автоматически получают повторный тег.

Когда OneAgent завершает помеченную сессию из-за достижения максимальной продолжительности или бездействия пользователя, следующая сессия автоматически получает повторный тег. Вам не нужно повторно предоставлять информацию для идентификации пользователя.

Однако обратите внимание, что OneAgent не присваивает повторный тег следующей сессии в следующих случаях:

* Когда вы явно завершаете помеченную пользовательскую сессию через [`endVisit`](#end-session)
* Когда пользователь или мобильная операционная система закрывает или принудительно останавливает приложение
* Когда OneAgent завершает текущую пользовательскую сессию и создаёт новую после изменения настроек конфиденциальности

См. [Пользовательские сессии > Завершение сессии](../../rum-concepts/user-session.md#user-session-end--mobile-apps "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её продолжительность и многое другое."), чтобы узнать, когда OneAgent завершает мобильную пользовательскую сессию.

Когда для вашего приложения включён [режим согласия пользователя](../additional-configuration/configure-rum-privacy-mobile.md#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона."), это может повлиять на тегирование пользователей и отправку пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не отправляемые в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. [Уровни сбора данных](../additional-configuration/configure-rum-privacy-mobile.md#data-collection-levels "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона.").

### Завершение сессии

Вы можете принудительно завершить сессию через вызов API. Это также закрывает все открытые действия и начинает новую сессию.

```
using Dynatrace.Xamarin;


Agent.Instance.EndVisit();
```

### Настройка конфиденциальности данных (режим согласия)

В режиме согласия пользователя каждый пользователь вашего приложения может устанавливать свои предпочтения конфиденциальности и решать, хочет ли он делиться своей информацией. Когда режим согласия включён, вам необходимо запрашивать у каждого пользователя разрешение на сбор его данных, а затем сохранять его предпочтения конфиденциальности. Подробнее см. [Режим согласия пользователя](../additional-configuration/configure-rum-privacy-mobile.md#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона.").

#### Включение режима согласия пользователя

Чтобы активировать режим согласия пользователя, установите свойство `userOptIn` (Android) или [ключ конфигурации `DTXUserOptIn`](../instrument-ios-app/customization/ios-configuration-keys.md#privacy-and-security "С помощью ключей конфигурации вы можете точно настроить автоматическое инструментирование ваших iOS-приложений.") (iOS) в значение `true` в [файле `dynatrace.config.json`](#config-file).

#### Получение предпочтений конфиденциальности пользователя

Вы можете получить предпочтения конфиденциальности конкретного пользователя.

Чтобы получить текущую конфигурацию `UserPrivacyOptions`, используйте следующий вызов API:

```
using Dynatrace.Xamarin;


// Get the UserPrivacyOptions object


UserPrivacyOptions currentOptions = Agent.Instance.GetUserPrivacyOptions();


// Get the individual settings for DataCollectionLevel and crash reporting


bool crashOptedIn = Agent.Instance.GetUserPrivacyOptions().CrashReportingOptedIn;


DataCollectionLevel dataCollectionLevel = Agent.Instance.GetUserPrivacyOptions().DataCollectionLevel;
```

#### Изменение предпочтений конфиденциальности пользователя

Вы можете изменить предпочтения конфиденциальности на основе решения конкретного пользователя.

Чтобы задать новые параметры объекта `UserPrivacyOptions`, используйте следующий код:

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

Чтобы применить новую конфигурацию `UserPrivacyOptions`, используйте этот код:

```
using Dynatrace.Xamarin;


UserPrivacyOptions options = new UserPrivacyOptions(DataCollectionLevel.UserBehavior, true);


Agent.Instance.ApplyUserPrivacyOptions(options);
```

Возможные значения для [уровня сбора данных](../additional-configuration/configure-rum-privacy-mobile.md#data-collection-levels "Используйте настройки конфиденциальности Dynatrace, чтобы ваши мобильные приложения соответствовали требованиям защиты данных вашего региона."):

* `Off`
* `Performance`
* `UserBehavior`

### Отправка GPS-координат

Вы можете отправлять широту и долготу.

```
SetGPSLocation(latitude: double, longitude: double);
```

## Файл конфигурации

Файл конфигурации `dynatrace.config.json` содержит идентификатор вашего приложения, URL маяка и некоторые другие настройки.

* Вы можете [скачать этот файл из Dynatrace](#installation-dynatrace) или создать его вручную.
* Если вы не добавите файл конфигурации хотя бы со свойствами URL маяка и идентификатора приложения, сборка завершится с ошибкой. В качестве альтернативы используйте [ручной запуск](#start-agent) с конфигурационным построителем (Android) или словарём конфигурации (iOS).
* Когда вы используете конкретную конфигурацию сборки — например, `Debug`, `Release` или пользовательскую конфигурацию — наш пакет ищет в директории `Assets` (Android) или `Resources` (iOS) файл конфигурации с именем `dynatrace<Configuration>.config.json`. Например, при использовании конфигурации сборки `Debug` наш пакет ищет файл с именем `dynatraceDebug.config.json`.
* Если вы хотите указать пользовательский путь для конфигурации, задайте его через свойство `DynatraceConfigurationFile`.

  Создайте `Directory.Build.props` в директории проекта Android/iOS (или общей):

  ```
  <Project>


  <PropertyGroup>


  <DynatraceConfigurationFile>CUSTOM_PATH/dynatrace.config.json</DynatraceConfigurationFile>


  </PropertyGroup>


  </Project>
  ```

В итоге конфигурация используется в следующем порядке:

1. Пользовательский путь конфигурации через свойство `DynatraceConfigurationFile`
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

Никогда не используйте точечную нотацию для файла конфигурации. Всегда используйте полный стиль записи с фигурными скобками.

## Включение отладочных журналов OneAgent

Если инструментирование проходит успешно и ваше приложение запускается, но вы не видите данных в среде Dynatrace, вам, вероятно, нужно углубиться в анализ, чтобы выяснить, почему OneAgent не отправляет данные. Создание обращения в техподдержку — хорошая идея, но сначала лучше собрать журналы.

Android

iOS

Обновите ваш [файл `dynatrace.config.json`](#config-file), чтобы включить отладочные журналы OneAgent.

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

## Включение отладочных журналов сборки для Android

Только для Android

Если инструментирование Android завершается с ошибкой, вам, скорее всего, нужно создать обращение в техподдержку и предоставить отладочные журналы сборки. Для получения этих журналов вам необходимо установить свойство `DynatraceInstrumentationLogging` и изменить уровень журнала сборки на `Diagnostic`.

1. Установите свойство `DynatraceInstrumentationLogging`. Выберите один из следующих способов:

   * Создайте `Directory.Build.props` в директории проекта Android:

   ```
   <Project>


   <PropertyGroup>


   <DynatraceInstrumentationLogging>true</DynatraceInstrumentationLogging>


   </PropertyGroup>


   </Project>
   ```

   * Добавьте свойство `DynatraceInstrumentationLogging` в файл `.csproj` вашего проекта. Вставьте его в существующую `PropertyGroup` в зависимости от конфигурации, которую вы используете.
2. Измените уровень детализации вывода сборки на `Diagnostic`. Подробнее см. документацию Microsoft о том, как [изменить объём информации в журнале сборки](https://docs.microsoft.com/en-us/visualstudio/ide/how-to-view-save-and-configure-build-log-files?view=vs-2019#to-change-the-amount-of-information-included-in-the-build-log).
3. Пересоберите проект.
4. Приложите журналы сборки к обращению в техподдержку, чтобы мы могли проанализировать вашу проблему.

## Устранение неполадок

Если вы не можете решить проблему, ознакомьтесь с разделом [Мобильные приложения: проблемы с Dynatrace Xamarin NuGet пакетом](https://dt-url.net/xn638zc) в сообществе Dynatrace.

## Связанные темы

* [Инструментирование Android-приложений](../instrument-android-app.md "Узнайте, как инструментировать мониторинг мобильных приложений на Android, как настроить инструментирование и многое другое.")
* [Инструментирование iOS-приложений](../instrument-ios-app.md "Инструментируйте мониторинг мобильных приложений для iOS, настройте автоматическое инструментирование и собирайте дополнительные данные с помощью ручного инструментирования.")
