---
title: Инструментация через OneAgent SDK для Android в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android
---

# Инструментация через OneAgent SDK для Android в RUM Classic

# Инструментация через OneAgent SDK для Android в RUM Classic

* Практическое руководство
* 26 мин чтения
* Обновлено 26 марта 2026 г.

С помощью OneAgent SDK для Android можно передавать дополнительные сведения о пользовательских сессиях в мобильном приложении. OneAgent SDK для Android позволяет создавать пользовательские действия, сообщать об ошибках, помечать конкретных пользователей и многое другое. В разделах ниже описано, как включить эти возможности.

OneAgent SDK можно использовать на Java и Kotlin.

## Запуск OneAgent

OneAgent следует запускать вручную в следующих случаях:

* если [автоматический запуск OneAgent отключён](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#disable-auto-startup "Узнайте, как настроить плагин Dynatrace Android Gradle для регулирования процесса автоматической инструментации.")
* если используется [автономная ручная инструментация](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Используйте OneAgent SDK для Android, чтобы вручную инструментировать приложение Android.") вместо автоматической

Используйте метод API [`Dynatrace.startup(Application, Configuration)`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Application,com.dynatrace.android.agent.conf.Configuration)) и запускайте OneAgent вручную в методе [`Application.onCreate`﻿](https://developer.android.com/reference/android/app/Application#onCreate()).

Java

Kotlin

```
public class YourApplication extends Application {



@Override



public void onCreate() {



super.onCreate();



// provide the application context as parameter



Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



... // additional configuration



.buildConfiguration());



}



}
```

```
class YourApplication : Application() {



override fun onCreate() {



super.onCreate()



// provide the application context as parameter



Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



... // additional configuration



.buildConfiguration())



}



}
```

Если нужно запустить OneAgent на более позднем этапе, используйте метод API [`Dynatrace.startup(Activity, Configuration)`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Activity,com.dynatrace.android.agent.conf.Configuration)). Передайте активный `Activity` в качестве параметра, чтобы OneAgent мог сразу начать его отслеживать.

Java

Kotlin

```
Dynatrace.startup(yourActiveActivity, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



... // additional configuration



.buildConfiguration());
```

```
Dynatrace.startup(yourActiveActivity, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



... // additional configuration



.buildConfiguration())
```

Чтобы получить правильные ключи идентификации приложения (`applicationId` и `beaconUrl`), откройте [мастер мобильной инструментации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Узнайте, какие шаги нужно выполнить, чтобы инструментировать приложение Android для мониторинга с помощью Dynatrace.") для своего приложения.

OneAgent можно запустить только один раз на приложение. OneAgent не поддерживает несколько одновременных инициализаций в одном запущенном приложении. Параметры `appId` и `beaconUrl` не являются механизмом для отправки данных из одного приложения в две разные среды Dynatrace.

Если приложение поддерживает Direct Boot, никогда не вызывайте метод API `Dynatrace.startup` из компонента, работающего с учётом Direct Boot. Также проверьте раздел [Настройка связи с OneAgent SDK для Android в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Настройте связь с OneAgent для передачи данных о пользовательском опыте в Dynatrace."), чтобы убедиться, что OneAgent может передавать данные в Dynatrace.

### Настройка OneAgent

Используйте класс [DynatraceConfigurationBuilder﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/DynatraceConfigurationBuilder.html), чтобы настроить параметры OneAgent.

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withUserOptIn(true)



.withCrashReporting(true)



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withUserOptIn(true)



.withCrashReporting(true)



.buildConfiguration()
```

Если используется сочетание ручной и автоматической инструментации, автоматическая инструментация вставляет вызов `Dynatrace.startup` в метод `Application.onCreate`. В этом случае встроенный вызов `Dynatrace.startup` вызывается раньше вашего ручного вызова `Dynatrace.startup`, поэтому ваша ручная конфигурация игнорируется.

Используйте свойство `autoStart.enabled`, чтобы отключить функцию автоматического запуска из автоматической инструментации. После этого можно [задать ручной вызов `Dynatrace.startup`](#start-oneagent). В этом случае можно переопределить значения, предварительно настроенные автоматической инструментацией.

OneAgent не поддерживает одновременный запуск нескольких экземпляров, нацеленных на разные среды.

## Мониторинг пользовательских действий

С помощью мониторинга пользовательских действий можно определять и передавать пользовательские действия. Затем эти пользовательские действия можно обогащать с помощью следующих операций мониторинга:

* [Создание дочернего действия](#child-actions)
* [Передача события](#report-event)
* [Передача значения](#report-value)
* [Передача ошибки](#report-errors)
* [Присоединение веб-запроса к пользовательскому действию](#attach-request-to-action)

Пользовательские действия отличаются от пользовательских действий, создаваемых плагином Dynatrace Android Gradle. OneAgent не добавляет автоматически дополнительные события, такие как веб-запросы, к пользовательским действиям и не закрывает пользовательские действия. Однако при завершении работы OneAgent или необходимости начать новую сессию все открытые пользовательские действия закрываются.

Если для приложения включён [режим согласия пользователя](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности, которые предоставляет Dynatrace, чтобы обеспечить соответствие мобильных приложений региональным требованиям законодательства о защите данных."), это может повлиять на маркировку пользователей и передачу пользовательских событий, действий, значений и ошибок. Точные типы данных, не передаваемые в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте настройки конфиденциальности, которые предоставляет Dynatrace, чтобы обеспечить соответствие мобильных приложений региональным требованиям законодательства о защите данных.").

### Создание пользовательских действий

Можно создавать пользовательские действия и дополнять их дополнительной информацией. Если пользовательские действия не закрыты явно, OneAgent закрывает их и отправляет в кластер Dynatrace.

Вызовите `enterAction`, чтобы начать пользовательское действие, и `leaveAction`, чтобы закрыть его. Время измеряется автоматически.

Java

Kotlin

```
// start a custom action



DTXAction action = Dynatrace.enterAction("Tap on Search");



// ...do some work here...



// end a custom action



action.leaveAction();
```

```
// start a custom action



val action = Dynatrace.enterAction("Tap on Search")



// ...do some work here...



// end a custom action



action.leaveAction()
```

Для мобильного пользовательского действия или автоматически создаваемого мобильного пользовательского действия максимальная длина имени составляет 250 символов.

Максимальная продолжительность мобильного пользовательского действия составляет 9 минут.

Если пользовательское действие длится дольше 9 минут и не закрыто, такое действие отбрасывается и не передаётся в Dynatrace.

### Создание дочерних действий

[Дочерние действия](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#child-actions "Learn what user actions are and how they help you understand what users do with your application.") похожи на родительские действия. Когда родительское действие закрывается, OneAgent автоматически закрывает все дочерние действия этого родительского действия.

Дочерние действия создаются с помощью метода [`Dynatrace.enterAction(String, DTXAction)`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#enterAction(java.lang.String,com.dynatrace.android.agent.DTXAction)).

Java

Kotlin

```
// start a parent custom action



DTXAction parentAction = Dynatrace.enterAction("Tap on Search");



// ...do some work here...



// start a child action



DTXAction childAction = Dynatrace.enterAction("Tap on Confirm", parentAction);



// ...do some work here...



// end a child action



childAction.leaveAction();



// ...do some work here...



// end a parent custom action



parentAction.leaveAction();
```

```
// start a parent custom action



val parentAction = Dynatrace.enterAction("Tap on Search")



// ...do some work here...



// start a child action



val childAction = Dynatrace.enterAction("Tap on Confirm", parentAction)



// ...do some work here...



// end a child action



childAction.leaveAction()



// ...do some work here...



// end a parent custom action



parentAction.leaveAction()
```

Для мобильного пользовательского действия (custom action) или автоматически сгенерированного мобильного пользовательского действия максимальная длина имени составляет 250 символов.

Ограничения на количество дочерних действий, прикреплённых к родительскому действию, нет. Однако стоит учитывать, что можно создать только девять уровней вложенности дочерних действий, то есть создать одно родительское действие и девять уровней дочерних действий (когда дочернее действие A добавляется к родительскому действию, дочернее действие B добавляется к дочернему действию A, дочернее действие C добавляется к дочернему действию B, и так далее). Также см. [Структура пользовательской сессии для отдельного пользователя](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#session-structure-dep-on-app-type "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Дочерние действия не отображаются на [странице сведений о пользовательской сессии](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), но их можно посмотреть на [странице waterfall-анализа](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") для родительского действия, к которому эти дочерние действия прикреплены. Хотя вложенность дочерних действий не полностью сохраняется в представлении waterfall-анализа и все дочерние действия отображаются как дочерние действия уровня 1, по временным меткам всё же можно понять вложенность действий.

### Отмена пользовательских действий

OneAgent для Android версии 8.231+

Если нужно отменить уже созданное, но ещё не завершённое пользовательское действие, используется вызов [`DTXAction#cancel()`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#cancel()) API.

Отмена действия приводит к отбрасыванию всех связанных с ним данных: все переданные значения отбрасываются, а все дочерние действия отменяются. Также стоит учитывать, что завершённое действие отменить нельзя.

Java

Kotlin

```
// create a custom action



DTXAction action = Dynatrace.enterAction("Tap on Purchase");



try {



// ...do some work here...



performWork();



// close the custom action. All associated data is stored and sent to Dynatrace



action.leaveAction();



}



catch(Exception e) {



// cancel the custom action. All associated data is discarded.



action.cancel();



}
```

```
// create a custom action



val action = Dynatrace.enterAction("Tap on Purchase")



try {



// ...do some work here...



performWork()



// close the custom action. All associated data is stored and sent to Dynatrace



action.leaveAction()



} catch (e: Exception) {



// cancel the custom action. All associated data is discarded.



action.cancel()



}
```

### Определение состояния пользовательского действия

OneAgent для Android версии 8.231+

Иногда полезно знать, открыто ли ещё пользовательское действие и можно ли использовать его для передачи данных.

Чтобы проверить состояние пользовательского действия, используется метод [`DTXAction#isFinished()`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#isFinished()).

Пользовательское действие считается завершённым, если оно:

* Завершено через `DTXAction#leaveAction()`, или
* Отменено через `DTXAction#cancel()`, или
* Прекращено OneAgent (например, при завершении работы OneAgent)

Обратите внимание, что не следует взаимодействовать с завершённым пользовательским действием.

#### Пример кода пользовательского действия

Следующий фрагмент кода показывает пример инструментирования вымышленного метода поиска, который выполняет веб-запрос к инструментированному серверу и разбирает полученный результат. В этот фрагмент кода входят следующие действия инструментирования:

1. Создание пользовательского действия
2. Передача значения
3. Передача ошибки
4. Мониторинг веб-запроса
5. Создание дочернего действия

Java

Kotlin

```
public boolean search(String query) {



// [1a] start a parent custom action



DTXAction searchAction = Dynatrace.enterAction("Tap on Search");



// [2] report a value



searchAction.reportValue("query", query);



URL url;



try {



url = new URL("https://www.example.com/?query=" + query);



} catch (MalformedURLException e) {



// [3] report an error



searchAction.reportError("invalid url", e);



// [1b] end a parent custom action



searchAction.leaveAction();



return false;



}



// [4.1] Generate a new unique tag associated with the custom action "Tap on Search"



String uniqueRequestTag = searchAction.getRequestTag();



// [4.2] Generate a WebRequestTiming object based on the unique tag



WebRequestTiming timing = Dynatrace.getWebRequestTiming(uniqueRequestTag);



Request request = new Request.Builder()



.url(url)



// [4.3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build();



// [4.4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming();



try (Response response = client.newCall(request).execute()) {



if (!response.isSuccessful()) {



// [4.5] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, response.code(), response.message());



return false;



}



String body = response.body().string();



// [4.5] Stop web request timing when the HTTP response is received and the response body is obtained



timing.stopWebRequestTiming(url, response.code(), response.message());



// [5a] start a child action



DTXAction parseAction = Dynatrace.enterAction("Parse result", searchAction);



parseResult(body);



// [5b] end a child action



parseAction.leaveAction();



return true;



} catch (IOException e) {



// [4.5] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString());



return false;



}



finally {



// [1b] end a parent custom action



searchAction.leaveAction();



}



}
```

```
fun search(query: String): Boolean {



// [1a] start a parent custom action



val searchAction = Dynatrace.enterAction("Tap on Search")



// [2] report a value



searchAction.reportValue("query", query)



var url: URL? = null



try {



url = URL("https://www.example.com/?query=$query")



} catch (e: MalformedURLException) {



// [3] report an error



searchAction.reportError("invalid url", e)



// [1b] end a parent custom action



searchAction.leaveAction()



return false



}



// [4.1] Generate a new unique tag associated with the custom action "Tap on Search"



val uniqueRequestTag = searchAction.requestTag



// [4.2] Generate a WebRequestTiming object based on the unique tag



val timing = Dynatrace.getWebRequestTiming(uniqueRequestTag)



val request = Request.Builder()



.url(url)



// [4.3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build()



try {



// [4.4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming()



client.newCall(request).execute().use { response ->



if (!response.isSuccessful) {



// [4.5] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, response.code, response.message)



return false



}



val body = response.body!!.string()



// [4.5] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code, response.message)



// [5a] start a child action



val parseAction = Dynatrace.enterAction("Parse result", searchAction)



parseResult(body)



// [5b] end a child action



parseAction.leaveAction()



}



return true



} catch (e: IOException) {



// [4.5] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString())



return false



} finally {



// [1b] end a parent custom action



searchAction.leaveAction()



}



}
```

## Передача пользовательских значений

С помощью OneAgent SDK для Android можно передавать события, значения и ошибки. Переданные события, значения и ошибки, входящие в состав пользовательского действия, отображаются в анализе водопада пользовательского действия. Переданные ошибки (как отдельные, так и «привязанные» к пользовательскому действию) также отображаются на странице деталей пользовательской сессии и на многомерной странице **User action analysis**.

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на пометку пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, которые не передаются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Передача события

С помощью `reportEvent` можно передать конкретное событие. Переданное событие должно входить в состав пользовательского действия.

Java

Kotlin

```
action.reportEvent("event_name");
```

```
action.reportEvent("event_name")
```

### Передача значения

Метод `reportValue` позволяет передавать пары «ключ-значение» метаданных, которые впоследствии можно просмотреть в веб-интерфейсе Dynatrace и преобразовать в [свойства пользовательского действия и пользовательской сессии](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more."). Переданные значения должны входить в состав пользовательского действия.

Можно передавать значения следующих типов данных:

* [`int`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,int))
* [`long`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,long))
* [`double`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,double))
* [`string`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,java.lang.String))

Java

Kotlin

```
// report int



action.reportValue("int_value_name", 5);



// report long



action.reportValue("long_value_name", 5L);



// report double



action.reportValue("double_value_name", 5.6);



// report string



action.reportValue("string_value_name", "exampleValue");
```

```
// report int



action.reportValue("int_value_name", 5)



// report long



action.reportValue("long_value_name", 5L)



// report double



action.reportValue("double_value_name", 5.6)



// report string



action.reportValue("string_value_name", "exampleValue")
```

Чтобы просмотреть переданные значения в веб-интерфейсе Dynatrace, нужно перейти к деталям пользовательского действия, которое должно содержать эти метаданные, и прокрутить вниз до раздела **Reported values**.

![User action details page with SDK-reported values](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

Страница деталей пользовательского действия с переданными SDK значениями

Чтобы добавить свойства действия и сессии на основе переданных значений, а затем использовать эти свойства для создания сложных запросов, сегментаций и агрегаций, см. [Определение свойств пользовательского действия и пользовательской сессии для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored mobile applications.").

### Передача ошибки

Метод `reportError` отличается от метода `reportValue` тем, что он специально идентифицируется как [событие типа "ошибка"](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.").

OneAgent SDK позволяет передавать следующее:

* **Коды ошибок**. Используется метод [`reportError(String, int)`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportError(java.lang.String,int)).
* **Обработанные исключения**. Используется метод [`reportError(String, Throwable)`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportError(java.lang.String,java.lang.Throwable)).

Есть два варианта передачи ошибки. Можно передать ошибку как часть пользовательского действия или как отдельную ошибку, которая формируется как глобальное событие, не привязанное к конкретному пользовательскому действию.

#### Ошибка в составе пользовательского действия

Java

Kotlin

```
// report an error code



action.reportError("error_code_name", -1);



// report an exception



action.reportError("exception_name", exception);
```

```
// report an error code



action.reportError("error_code_name", -1)



// report an exception



action.reportError("exception_name", exception)
```

#### Отдельная ошибка

Отдельные ошибки можно передавать через класс `Dynatrace`.

Java

Kotlin

```
// report an error code



Dynatrace.reportError("error_code_name", -1);



// report an exception



Dynatrace.reportError("exception_name", exception);
```

```
// report an error code



Dynatrace.reportError("error_code_name", -1)



// report an exception



Dynatrace.reportError("exception_name", exception)
```

## Мониторинг жизненного цикла activity

Для отслеживания событий жизненного цикла используется официальный интерфейс Android [`ActivityLifecycleCallbacks`﻿](https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks). Для activity Dynatrace передаёт время наступления каждого состояния жизненного цикла вплоть до момента, когда activity становится видимой; при наличии таких данных временные метки колбэков жизненного цикла отображаются в анализе водопада пользовательского действия и помечаются как **Lifecycle event**.

### Передаваемые события жизненного цикла

При мониторинге жизненного цикла OneAgent собирает данные по следующим событиям жизненного цикла для класса [`Activity`﻿](https://developer.android.com/reference/android/app/Activity).

* **Activity display**: измеряет время, необходимое для отображения activity.
* **Activity redisplay**: измеряет время, необходимое для повторного отображения ранее созданной activity. Возможны два варианта:

  + Вариант 1: activity находится в режиме *Stopped* и не видна на экране, а затем снова переходит в *Started* и *Resumed*.
  + Вариант 2: activity находится в режиме *Paused* и не полностью видна на экране, будучи частично перекрытой, а затем снова переходит в *Resumed*.

Временной интервал, используемый для измерения продолжительности события жизненного цикла, зависит от типа события жизненного цикла и уровня Android API. При использовании Android API уровня 29+ продолжительность событий жизненного цикла можно измерять точнее благодаря колбэкам pre- и post-lifecycle.

| Событие жизненного цикла | Android API 29+ | Android API 28 и ниже | Передаваемые колбэки жизненного цикла |
| --- | --- | --- | --- |
| **Activity display** | `onActivityPreCreated` – `onActivityPostResumed` | `onActivityCreated` – `onActivityResumed` | ``` onCreate``onStart``onResume ``` |
| **Activity redisplay**, вариант 1 | `onActivityPreStarted` – `onActivityPostResumed` | `onActivityStarted` – `onActivityResumed` | ``` onStart``onResume ``` |
| **Activity redisplay**, вариант 2 | `onActivityPreResumed` – `onActivityPostResumed` | Измерить продолжительность невозможно | `onResume` |

### Отключение мониторинга жизненного цикла

Мониторинг жизненного цикла activity включён по умолчанию, но его можно отключить с помощью метода [`withActivityMonitoring`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withActivityMonitoring(boolean)).

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withActivityMonitoring(false)



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withActivityMonitoring(false)



.buildConfiguration()
```

## Мониторинг веб-запросов

[Dynatrace Android Gradle plugin](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнай, как Dynatrace Android Gradle plugin может автоматически инструментировать проект Android-приложения.") автоматически инструментирует большинство веб-запросов. Однако запросы нужно инструментировать вручную в следующих случаях:

* Если запросы стороннего фреймворка не инструментированы
* Если нужно [сообщать о запросах не по HTTP(S)](#monitor-non-http-requests)
* Если отключён [мониторинг веб-запросов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#disable-web-request-monitoring "Настрой Dynatrace Android Gradle plugin для изменения возможностей мониторинга OneAgent.")

Для запросов по HTTP(S) нельзя сочетать автоматическую и ручную инструментацию веб-запросов. Однако можно использовать автоматическую инструментацию для запросов по HTTP(S) и ручную для [запросов не по HTTP(S)](#monitor-non-http-requests).

Для отслеживания веб-запросов добавь к веб-запросу HTTP-заголовок `x-dynatrace` с уникальным значением. Это нужно, чтобы сопоставить данные мониторинга на стороне сервера с соответствующим мобильным веб-запросом. Кроме того, нужно измерить значения времени на мобильной стороне.

Чтобы отслеживать веб-запрос

1. Сгенерировать новый уникальный тег.
2. Сгенерировать объект `WebRequestTiming` на основе тега.
3. Разместить HTTP-заголовок Dynatrace в веб-запросе.
4. Запустить измерение времени веб-запроса до отправки HTTP-запроса.
5. Остановить измерение времени веб-запроса.

   * Получен HTTP-ответ, и получено тело ответа.
   * Возникло исключение соединения.

По иерархии есть два типа веб-запросов:

* [Запросы, привязанные к действию пользователя](#attach-request-to-action)
* [Отдельные запросы](#monitor-standalone-request). Для таких запросов OneAgent автоматически пытается найти подходящее действие пользователя. Если оно находится, веб-запрос привязывается к этому действию пользователя. Веб-запрос отражается как отдельный веб-запрос только если подходящее действие пользователя не найдено.

  На данный момент отдельные запросы нельзя посмотреть в [**Session Segmentation**](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Узнай о сегментации пользовательских сессий и атрибутах фильтрации.").

### Привязка веб-запроса к действию пользователя

Чтобы привязать веб-запрос к действию пользователя, сгенерируй уникальный тег методом [`DTXAction.getRequestTag()`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#getRequestTag()).

Следующий пример показывает, как привязать синхронный веб-запрос `OkHttp` к действию пользователя `"Search request"`.

Java

Kotlin

```
URL url = new URL("https://www.example.com");



// First, create a custom action



DTXAction webAction = Dynatrace.enterAction("Search request");



// [1] Generate a new unique tag associated with the user action



String uniqueRequestTag = webAction.getRequestTag();



// [2] Generate a WebRequestTiming object based on the unique tag



WebRequestTiming timing = Dynatrace.getWebRequestTiming(uniqueRequestTag);



// Define your OkHttp request. This varies greatly depending on your implementation



Request request = new Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build();



// [4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming();



try (Response response = client.newCall(request).execute()) {



if (response.isSuccessful()) {



// handle response



String body = response.body().string();



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code(), response.message());



} catch (IOException e) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString());



// user-defined exception handling



}



finally {



// Lastly, end the custom action



webAction.leaveAction();



}
```

```
val url = URL("https://www.example.com")



// First, create a custom action



val webAction = Dynatrace.enterAction("Search request")



// [1] Generate a new unique tag associated with the user action



val uniqueRequestTag = webAction.requestTag



// [2] Generate a WebRequestTiming object based on the unique tag



val timing = Dynatrace.getWebRequestTiming(uniqueRequestTag)



// Define your OkHttp request. This varies greatly depending on your implementation



val request = Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build()



try {



// [4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming()



client.newCall(request).execute().use { response ->



if (response.isSuccessful) {



// handle response



val body = response.body!!.string()



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code, response.message)



}



} catch (e: IOException) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString())



// user-defined exception handling



} finally {



// Lastly, end the custom action



webAction.leaveAction()



}
```

Attach an asynchronous OkHttp web request to a user action

Java

Kotlin

```
final URL url = new URL("https://www.example.com");



// First, create a custom action



final DTXAction webAction = Dynatrace.enterAction("Search request");



// [1] Generate a new unique tag associated with the user action



String uniqueRequestTag = webAction.getRequestTag();



// [2] Generate a WebRequestTiming object based on the unique tag



final WebRequestTiming timing = Dynatrace.getWebRequestTiming(uniqueRequestTag);



// Define your OkHttp request. This varies greatly depending on your implementation



Request request = new Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build();



// [4] Call startWebRequestTiming to begin the timing, and then handle the response body from the OkHttp call



timing.startWebRequestTiming();



client.newCall(request).enqueue(new Callback() {



@Override



public void onFailure(Call call, IOException e) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString());



// user-defined exception handling



// [8] Lastly, end the custom action



webAction.leaveAction();



}



@Override



public void onResponse(Call call, Response response) throws IOException {



try (ResponseBody responseBody = response.body()) {



if (response.isSuccessful()) {



// handle response



String body = response.body().string();



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code(), response.message());



// Lastly, end the custom action



webAction.leaveAction();



}



}



});
```

```
val url = URL("https://www.example.com")



// First, create a custom action



val webAction = Dynatrace.enterAction("Search request")



// [1] Generate a new unique tag associated with the user action



val uniqueRequestTag = webAction.requestTag



// [2] Generate a WebRequestTiming object based on the unique tag



val timing = Dynatrace.getWebRequestTiming(uniqueRequestTag)



// Define your OkHttp request. This varies greatly depending on your implementation



val request = Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build()



// [4] Call startWebRequestTiming to begin the timing, and then handle the response body from the OkHttp call



timing.startWebRequestTiming()



client.newCall(request).enqueue(object : Callback {



override fun onFailure(call: Call, e: IOException) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString())



// user-defined exception handling



// [8] Lastly, end the custom action



webAction.leaveAction()



}



@Throws(IOException::class)



override fun onResponse(call: Call, response: Response) {



response.use {



if (response.isSuccessful) {



// handle response



val body = response.body!!.string()



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code, response.message)



// Lastly, end the custom action



webAction.leaveAction()



}



}



})
```

### Мониторинг отдельного веб-запроса

Чтобы отслеживать веб-запрос как самостоятельный запрос, нужно сгенерировать уникальный тег методом [`Dynatrace.getRequestTag()`​](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#getRequestTag()).

В следующем примере показано, как отслеживать синхронный веб-запрос `OkHttp`.

Java

Kotlin

```
URL url = new URL("https://www.example.com");



// [1] Generate a new unique tag



String uniqueRequestTag = Dynatrace.getRequestTag();



// [2] Generate a WebRequestTiming object based on the unique tag



WebRequestTiming timing = Dynatrace.getWebRequestTiming(uniqueRequestTag);



// Define your OkHttp request. This varies greatly depending on your implementation



Request request = new Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build();



// [4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming();



try (Response response = client.newCall(request).execute()) {



if (response.isSuccessful()) {



// handle response



String body = response.body().string();



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code(), response.message());



} catch (IOException e) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString());



// user-defined exception handling



}
```

```
val url = URL("https://www.example.com")



// [1] Generate a new unique tag



val uniqueRequestTag = Dynatrace.getRequestTag()



// [2] Generate a WebRequestTiming object based on the unique tag



val timing = Dynatrace.getWebRequestTiming(uniqueRequestTag)



// Define your OkHttp request. This varies greatly depending on your implementation



val request = Request.Builder()



.url(url)



// Define your headers for the OkHttp request



.addHeader(yourKey1, yourValue1)



.addHeader(yourKey2, yourValue2)



// [3] Place the Dynatrace HTTP header on your web request



.addHeader(Dynatrace.getRequestTagHeader(), uniqueRequestTag)



.build()



try {



// [4] Start web request timing before the HTTP request is sent



timing.startWebRequestTiming()



client.newCall(request).execute().use { response ->



if (response.isSuccessful) {



// handle response



val body = response.body!!.string()



}



// [5.1] Stop web request timing when the HTTP response is received and the response body was obtained



timing.stopWebRequestTiming(url, response.code, response.message)



}



} catch (e: IOException) {



// [5.2] Stop web request timing when a connection exception occurs



timing.stopWebRequestTiming(url, -1, e.toString())



// user-defined exception handling



}
```

### Отслеживание запросов, отличных от HTTP(S)

OneAgent for Android версии 8.249+

Отслеживание соединений WebSocket доступно начиная с OneAgent for Android версии 8.239. Отслеживание всех запросов, отличных от HTTP(S), доступно начиная с OneAgent for Android версии 8.249.

OneAgent for Android не поддерживает автоматическое инструментирование запросов, отличных от HTTP(S). Если нужно передавать данные о запросах вроде WebSocket-запроса (начинается с `ws://` или `wss://`), см. примеры кода ниже.

* Используй метод API [`stopWebRequestTiming(URI requestUri, int respCode, String respPhrase)`​](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/WebRequestTiming.html#stopWebRequestTiming(java.net.URI,int,java.lang.String)), чтобы вручную инструментировать запросы, отличные от HTTP(S).
* Обязательно передавай исходный URI. Не получай URI из объекта `OkHttp`, поскольку он не возвращает исходный URI.
* Этот подход подходит только для соединений WebSocket, которые открыты не дольше примерно 9 минут. Более длительные соединения могут не отслеживаться.
* Если есть только запросы, отличные от HTTP(S), можно по желанию [отключить отслеживание веб-запросов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#disable-web-request-monitoring "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.").
* Если есть и запросы HTTP(S), и запросы, отличные от HTTP(S), и запросы HTTP(S) инструментируются автоматически, не отключай отслеживание веб-запросов.

Java

Kotlin

```
final URI uri = URI.create("wss://websocket.example.com");



// First, create a custom action



DTXAction webSocketAction = Dynatrace.enterAction("WebSocket");



// Generate a WebRequestTiming object based on the unique request tag



WebRequestTiming timing = Dynatrace.getWebRequestTiming(webSocketAction.getRequestTag());



// Define your OkHttp request. This varies greatly depending on your implementation



Request request = new Request.Builder()



.url(uri.toString())



.build();



// Start web request timing when you are about to open a WebSocket connection



timing.startWebRequestTiming();



WebSocket webSocket = client.newWebSocket(request, new WebSocketListener() {



@Override



public void onClosing(@NonNull WebSocket webSocket, int code, @NonNull String reason) {



// Stop web request timing when the webSocket connection closes



// Don't retrieve the URI from the OkHttp object because it always replaces wss:// with https://



timing.stopWebRequestTiming(uri, code, reason);



// end the action



webSocketAction.leaveAction();



}



@Override



public void onFailure(@NonNull WebSocket webSocket, @NonNull Throwable t, @Nullable Response response) {



// Stop web request timing when the webSocket connection fails and customize the return code and message



// Don't retrieve the URI from the OkHttp object because it always replaces wss:// with https://



timing.stopWebRequestTiming(uri, 1011, "ERROR");



// end the action



webSocketAction.leaveAction();



}



});
```

```
val uri = URI.create("wss://websocket.example.com")



// First, create a custom action



val webSocketAction = Dynatrace.enterAction("WebSocket")



// Generate a WebRequestTiming object based on the unique request tag



val webRequestTiming = Dynatrace.getWebRequestTiming(webSocketAction.requestTag)



// Define your OkHttp request. This varies greatly depending on your implementation



val request = Request.Builder()



.url(uri.toString())



.build()



// Start web request timing when you are about to open a WebSocket connection



webRequestTiming.startWebRequestTiming()



val webSocket = client.newWebSocket(request, object : WebSocketListener() {



override fun onClosing(webSocket: WebSocket, code: Int, reason: String) {



// Stop web request timing when the webSocket connection closes



// Don't retrieve the URI from the OkHttp object because it always replaces wss:// with https://



webRequestTiming.stopWebRequestTiming(uri, code, reason)



// end the action



webSocketAction.leaveAction()



}



override fun onFailure(webSocket: WebSocket, t: Throwable, response: Response?) {



// Stop web request timing when the webSocket connection fails



// Don't retrieve the URI from the OkHttp object because it always replaces wss:// with https://



webRequestTiming.stopWebRequestTiming(uri, 1011, "ERROR")



// end the action



webSocketAction.leaveAction()



}



})
```

## Отчёты о сбоях

OneAgent перехватывает все [необработанные исключения​](https://dt-url.net/UncaughtExceptionHandler). Отчёт о [сбое](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") включает время возникновения и полную трассировку стека исключения.

Как правило, данные о сбое отправляются сразу после сбоя, поэтому пользователю не нужно перезапускать приложение. Однако в некоторых случаях приложение нужно снова открыть в течение 10 минут, чтобы отчёт о сбое был отправлен. Учитывай, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (поскольку такие отчёты уже нельзя сопоставить на Dynatrace Cluster).

Отчёты о сбоях можно отключить методом [`withCrashReporting`​](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withCrashReporting(boolean)).

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCrashReporting(false)



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCrashReporting(false)



.buildConfiguration()
```

## Тегирование конкретных пользователей

Каждому пользователю мобильных приложений можно присвоить уникальное имя пользователя. Это позволяет искать и фильтровать сессии конкретного пользователя и анализировать поведение отдельного пользователя во времени. Подробнее см. в разделе [User tagging](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.").

Ниже описаны шаги для тегирования отдельного пользователя через Dynatrace API.

Java

Kotlin

```
Dynatrace.identifyUser("john.doe@example.com");
```

```
Dynatrace.identifyUser("john.doe@example.com")
```

OneAgent для Android версии 237+ Сессии, разделённые из-за таймаута простоя или продолжительности, ретегируются автоматически.

Когда OneAgent завершает тегированную сессию из-за достижения установленного лимита продолжительности сессии или из-за бездействия пользователя, последующая сессия ретегируется автоматически. Повторно предоставлять информацию идентификации пользователя не нужно.

Однако обрати внимание, что OneAgent не ретегирует последующую сессию в следующих случаях:

* когда тегированная сессия пользователя явно завершается через [`endVisit`](#end-session);
* когда пользователь или мобильная операционная система закрывает или принудительно останавливает приложение;
* когда OneAgent завершает текущую сессию пользователя и создаёт новую сессию после изменения настроек приватности.

См. раздел [User sessions > Session end](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#user-session-end--mobile-apps "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more."), чтобы узнать, когда OneAgent завершает мобильную сессию пользователя.

Если для приложения включён [user opt-in mode](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и отчётность по пользовательским событиям, действиям пользователя, значениям и ошибкам. Конкретные типы данных, не передаваемые в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности см. в разделе [Data collection levels](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

## Завершение сессии

Можно принудительно завершить сессию через Dynatrace API. Это также закрывает все открытые действия и запускает новую сессию.

Java

Kotlin

```
Dynatrace.endVisit();
```

```
Dynatrace.endVisit()
```

## Настройка приватности данных (режим opt-in)

В режиме opt-in каждый пользователь приложения может задать свои предпочтения по приватности данных и решить, хочет ли он делиться своей информацией. Когда режим opt-in включён, нужно запрашивать у каждого пользователя разрешение на сбор его данных, а затем сохранять его предпочтения по приватности данных. Подробнее см. в разделе [User opt-in mode](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Включение режима opt-in для пользователя

Чтобы активировать режим opt-in для пользователя, включи флаг `userOptIn` через DSL из Dynatrace Android Gradle plugin или используй метод `ConfigurationBuilder.withUserOptIn`.

### Изменение предпочтений пользователя по приватности данных

С помощью метода [`Dynatrace.applyUserPrivacyOptions`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#applyUserPrivacyOptions(com.dynatrace.android.agent.conf.UserPrivacyOptions)) можно скорректировать предпочтения по приватности данных на основе решения конкретного пользователя.

Java

Kotlin

```
Dynatrace.applyUserPrivacyOptions(UserPrivacyOptions.builder()



// set a data collection level (user allowed you to capture performance and personal data)



.withDataCollectionLevel(DataCollectionLevel.USER_BEHAVIOR)



// allow crash reporting (user allowed you to collect information on crashes)



.withCrashReportingOptedIn(true)



// allow Session Replay on crashes (user allowed you to record replays of crashes via Session Replay)



.withCrashReplayOptedIn(true)



.build()



);
```

```
Dynatrace.applyUserPrivacyOptions(UserPrivacyOptions.builder()



// set a data collection level (user allowed you to capture performance and personal data)



.withDataCollectionLevel(DataCollectionLevel.USER_BEHAVIOR)



// allow crash reporting (user allowed you to collect information on crashes)



.withCrashReportingOptedIn(true)



// allow Session Replay on crashes (user allowed you to record replays of crashes via Session Replay)



.withCrashReplayOptedIn(true)



.build()



)
```

Возможные значения для [уровня сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") следующие:

* `OFF`
* `PERFORMANCE`
* `USER_BEHAVIOR`

OneAgent сохраняет предпочтения по приватности данных и автоматически применяет их при перезапуске приложения. Кроме того, OneAgent создаёт новую сессию каждый раз, когда предпочтения по приватности данных изменяются.

### Получение предпочтений пользователя по приватности данных

Также можно получить предпочтения по приватности данных конкретного пользователя с помощью метода [`Dynatrace.getUserPrivacyOptions`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#getUserPrivacyOptions()). Используй этот метод только после запуска OneAgent.

## Настройка гибридных приложений

Для гибридных приложений нативное мобильное приложение отслеживается через OneAgent, а часть в браузере наблюдается через [Dynatrace RUM JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring Classic using the JavaScript API."). По этой причине мониторинг гибридных приложений требует дополнительной настройки. См. [Instrument hybrid apps in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-hybrid-app "Learn how you can instrument various types of hybrid and cross-platform mobile apps.") для получения дополнительной информации.

### Включение мониторинга гибридных приложений

Чтобы активировать функцию мониторинга гибридных приложений, используй метод [`withHybridMonitoring`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withHybridMonitoring(boolean)).

### Указание доменов, имён хостов и IP-адресов

Для гибридных приложений, использующих RUM JavaScript внутри `WebView`, OneAgent должен устанавливать cookie для каждого инструментированного домена или сервера, с которым взаимодействует приложение. Когда функция мониторинга гибридных приложений включена, OneAgent создаёт эти cookie для каждого указанного домена и сохраняет их в `CookieManager`. Dynatrace использует эти cookie для идентификации мобильных и веб-сессий в приложении и объединения этих сессий в одну «гибридную» сессию.

Чтобы указать домены, имена хостов и IP-адреса, используй метод [`withMonitoredDomains`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withMonitoredDomains(java.lang.String...)) или [`withMonitoredHttpsDomains`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withMonitoredHttpsDomains(java.lang.String...)). Домены и субдомены нужно начинать с точки (`.`).

#### Метод `withMonitoredDomains`

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.withMonitoredDomains(".<domain1>", ".<domain2>")



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.withMonitoredDomains(".<domain1>", ".<domain2>")



.buildConfiguration()
```

#### Метод `withMonitoredHttpsDomains`

OneAgent для Android версии 8.237+

Если используется метод `withMonitoredHttpsDomains`, атрибут cookie `Secure` добавляется ко всем cookie, которые устанавливает Dynatrace. Это гарантирует, что браузер отправляет эти cookie только через безопасные соединения.

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.withMonitoredHttpsDomains("https://.<domain1>", "https://.<domain2>")



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.withMonitoredHttpsDomains("https://.<domain1>", "https://.<domain2>")



.buildConfiguration()
```

### Инструментирование `WebView`

Чтобы обеспечить взаимодействие между RUM JavaScript и OneAgent для Android, нужно проинструментировать все объекты `WebView` до загрузки URL с помощью [`WebView.loadUrl(String)`﻿](https://developer.android.com/reference/android/webkit/WebView#loadUrl(java.lang.String)). Метод [`Dynatrace.instrumentWebView`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#instrumentWebView(android.webkit.WebView)) нужно проинструментировать для каждого `WebView`, содержащего RUM JavaScript. Без этого данные мониторинга, полученные из `WebView`, не будут связаны с той же мобильной сессией.

Java

Kotlin

```
WebView myWebView = (WebView) findViewById(R.id.webview);



Dynatrace.instrumentWebView(myWebView);



myWebView.loadUrl("http://www.example.com");
```

```
val myWebView: WebView = findViewById(R.id.webview)



Dynatrace.instrumentWebView(myWebView)



myWebView.loadUrl("http://www.example.com")
```

### Отключение cookies для доменов файлов

OneAgent для Android версии 8.271+

Для установки cookies для доменов файлов (начинающихся с `file://`) Dynatrace использует [`setAcceptFileSchemeCookies`﻿](https://developer.android.com/reference/android/webkit/CookieManager#setAcceptFileSchemeCookies(boolean)). Однако этот API больше не рекомендуется из-за проблем безопасности, через пару месяцев планируется прекратить добавление cookies в домены файловой схемы.

Если нужно обезопасить приложение прямо сейчас, установи `fileDomainCookies` в значение `false`, и Dynatrace не будет добавлять cookies в домены файловой схемы.

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.fileDomainCookies(false)



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withHybridMonitoring(true)



.fileDomainCookies(false)



.buildConfiguration()
```

### Сохранение cookies Dynatrace

Для гибридных приложений важно следить за тем, чтобы cookies Dynatrace не удалялись. Без этих cookies Dynatrace не может объединить данные мониторинга, полученные из RUM JavaScript и OneAgent, в единую сессию.

При удалении cookies через [`CookieManager#removeAllCookies(ValueCallback)`﻿](https://developer.android.com/reference/android/webkit/CookieManager#removeAllCookies(android.webkit.ValueCallback%3Cjava.lang.Boolean%3E)) или [`CookieManager#removeSessionCookies(ValueCallback)`﻿](https://developer.android.com/reference/android/webkit/CookieManager#removeSessionCookies(android.webkit.ValueCallback%3Cjava.lang.Boolean%3E)) нужно также вызвать метод [`restoreCookies`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#restoreCookies()), чтобы восстановить cookies Dynatrace.

Java

Kotlin

```
CookieManager.getInstance().removeAllCookies(null);



Dynatrace.restoreCookies();
```

```
CookieManager.getInstance().removeAllCookies(null)



Dynatrace.restoreCookies()
```

## Включение балансировки нагрузки

OneAgent позволяет включить балансировку нагрузки на стороне клиента, которая помогает избежать неравномерной нагрузки на сервер, когда несколько OneAgent одновременно устанавливают соединение с ActiveGate.

Java

Kotlin

```
new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withStartupLoadBalancing(true)



.buildConfiguration();
```

```
DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withStartupLoadBalancing(true)



.buildConfiguration()
```