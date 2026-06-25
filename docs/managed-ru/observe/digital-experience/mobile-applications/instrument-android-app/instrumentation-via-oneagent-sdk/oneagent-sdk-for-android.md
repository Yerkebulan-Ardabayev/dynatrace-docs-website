---
title: Инструментирование через OneAgent SDK for Android
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android
scraped: 2026-05-12T11:22:06.920502
---

# Инструментирование через OneAgent SDK for Android

# Инструментирование через OneAgent SDK for Android

* How-to guide
* 26-min read
* Updated on Mar 26, 2026

Используйте OneAgent SDK for Android для сообщения дополнительных сведений о пользовательских сессиях в вашем мобильном приложении. OneAgent SDK for Android позволяет создавать пользовательские действия, фиксировать ошибки, тегировать конкретных пользователей и многое другое. В разделах ниже описывается, как включить эти возможности.

OneAgent SDK можно использовать с Java и Kotlin.

## Запуск OneAgent

Запускать OneAgent вручную нужно в следующих случаях:

* Если вы [отключили автоматический запуск OneAgent](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#disable-auto-startup "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.")
* Если вы используете [автономное ручное инструментирование](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/manual-instrumentation "Используйте OneAgent SDK for Android для ручного инструментирования Android-приложения.") вместо авто-инструментирования

Используйте API-метод [`Dynatrace.startup(Application, Configuration)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Application,com.dynatrace.android.agent.conf.Configuration)) и запустите OneAgent вручную в методе [`Application.onCreate`](https://developer.android.com/reference/android/app/Application#onCreate()).

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

Если вам нужно запустить OneAgent на более позднем этапе, используйте API-метод [`Dynatrace.startup(Activity, Configuration)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#startup(android.app.Activity,com.dynatrace.android.agent.conf.Configuration)). Передайте активный объект `Activity` в качестве параметра, чтобы OneAgent мог немедленно начать его мониторинг.

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

Чтобы получить правильные ключи идентификации приложения (`applicationId` и `beaconUrl`), воспользуйтесь [мастером инструментирования мобильных приложений](/managed/observe/digital-experience/mobile-applications/instrument-android-app/get-started-with-android-monitoring#instrumentation-wizard "Узнайте, какие шаги необходимо выполнить для инструментирования Android-приложения для мониторинга с Dynatrace.") для вашего приложения.

OneAgent можно запустить только один раз на приложение. OneAgent не поддерживает несколько одновременных инициализаций в одном запущенном приложении. Параметры `appId` и `beaconUrl` не являются механизмом для отправки данных в два разных окружения Dynatrace из одного приложения.

Если ваше приложение поддерживает Direct Boot, никогда не вызывайте API-метод `Dynatrace.startup` из компонента, поддерживающего Direct Boot. Также проверьте раздел [Настройка взаимодействия с OneAgent SDK for Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication "Настройте коммуникацию с OneAgent для отправки данных о пользовательском опыте в Dynatrace."), чтобы убедиться в возможности передачи данных OneAgent в Dynatrace.

### Настройка OneAgent

Используйте класс [DynatraceConfigurationBuilder](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/DynatraceConfigurationBuilder.html) для настройки параметров OneAgent.

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

Если вы используете комбинацию ручного и авто-инструментирования, авто-инструментирование добавляет вызов `Dynatrace.startup` в метод `Application.onCreate`. В этом случае внедрённый вызов `Dynatrace.startup` выполняется до вашего ручного вызова `Dynatrace.startup`, поэтому ручная конфигурация игнорируется.

Используйте свойство `autoStart.enabled`, чтобы отключить функцию автозапуска из авто-инструментирования. После этого вы можете [определить ручной вызов `Dynatrace.startup`](#start-oneagent). В этом случае вы сможете переопределить значения, предварительно настроенные авто-инструментированием.

OneAgent не поддерживает одновременное выполнение нескольких экземпляров, нацеленных на разные окружения.

## Мониторинг пользовательских действий

С помощью мониторинга пользовательских действий вы можете определять и фиксировать пользовательские действия. Затем эти действия можно дополнять с помощью следующих операций мониторинга:

* [Создание дочернего действия](#child-actions)
* [Фиксация события](#report-event)
* [Фиксация значения](#report-value)
* [Фиксация ошибки](#report-errors)
* [Привязка веб-запроса к пользовательскому действию](#attach-request-to-action)

Пользовательские действия отличаются от действий, создаваемых Dynatrace Android Gradle plugin. OneAgent не добавляет дополнительные события (например, веб-запросы) к пользовательским действиям автоматически и не закрывает их. Однако при завершении работы OneAgent или при начале новой сессии все открытые пользовательские действия закрываются.

Если для вашего приложения включён [режим opt-in для пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений нормативным требованиям вашего региона."), это может повлиять на тегирование пользователей и фиксацию пользовательских событий, действий, значений и ошибок. Точный перечень типов данных, не передаваемых в Dynatrace, зависит от уровня сбора данных, установленного конкретным пользователем. Подробности см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений нормативным требованиям вашего региона.").

### Создание пользовательских действий

Вы можете создавать пользовательские действия и дополнять их дополнительными сведениями. Если пользовательские действия не закрыты явно, OneAgent закрывает их и отправляет в кластер Dynatrace.

Вызовите `enterAction` для запуска пользовательского действия и `leaveAction` для его завершения. Время измеряется автоматически.

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

Максимальная длина имени мобильного пользовательского действия или мобильного автоматически сгенерированного пользовательского действия составляет 250 символов.

Максимальная продолжительность мобильного пользовательского действия составляет 9 минут.

Если пользовательское действие длится более 9 минут и не было закрыто, оно отбрасывается и не отправляется в Dynatrace.

### Создание дочерних действий

[Дочерние действия](/managed/observe/digital-experience/rum-concepts/user-actions#child-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают с приложением.") аналогичны родительским действиям. При закрытии родительского действия OneAgent автоматически закрывает все его дочерние действия.

Создавайте дочерние действия с помощью метода [`Dynatrace.enterAction(String, DTXAction)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#enterAction(java.lang.String,com.dynatrace.android.agent.DTXAction)).

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

Максимальная длина имени мобильного пользовательского действия составляет 250 символов.

Количество дочерних действий, привязанных к родительскому, не ограничено. Однако обратите внимание, что допустимо только девять уровней вложенности дочерних действий: можно создать одно родительское действие и девять уровней дочерних (когда дочернее действие A добавлено к родительскому, дочернее B — к A, дочернее C — к B, и так далее). Также см. раздел [Структура пользовательской сессии для отдельного пользователя](/managed/observe/digital-experience/rum-concepts/user-session#session-structure-dep-on-app-type "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её продолжительность и многое другое.").

Дочерние действия не отображаются на [странице сведений о пользовательской сессии](/managed/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Узнайте об атрибутах сегментации и фильтрации пользовательских сессий."), однако их можно просмотреть на [странице анализа waterfall](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Узнайте, как анализировать все данные мониторинга пользовательских действий через анализ waterfall.") для родительского действия. Несмотря на то что вложенность дочерних действий в представлении waterfall не отображается полностью (все дочерние действия показываются как дочерние первого уровня), из временных меток можно определить структуру вложенности.

### Отмена пользовательских действий

OneAgent for Android версии 8.231+

Если вам нужно отменить уже созданное, но ещё не завершённое пользовательское действие, используйте API-вызов [`DTXAction#cancel()`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#cancel()).

Отмена действия удаляет все связанные с ним данные: все зафиксированные значения отбрасываются, а все дочерние действия отменяются. Обратите внимание, что нельзя отменить уже завершённое действие.

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

OneAgent for Android версии 8.231+

Иногда нужно знать, остаётся ли пользовательское действие открытым и можно ли использовать его для фиксации данных.

Чтобы проверить состояние пользовательского действия, используйте метод [`DTXAction#isFinished()`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#isFinished()).

Пользовательское действие считается завершённым, если оно:

* Закрыто через `DTXAction#leaveAction()`, или
* Отменено через `DTXAction#cancel()`, или
* Завершено OneAgent принудительно (например, при завершении работы OneAgent)

Обратите внимание, что не следует взаимодействовать с завершённым пользовательским действием.

#### Пример кода пользовательского действия

В следующем фрагменте кода показан пример инструментирования вымышленного метода search, выполняющего веб-запрос к инструментированному серверу и разбирающего полученный результат. В фрагменте реализованы следующие операции:

1. Создание пользовательского действия
2. Фиксация значения
3. Фиксация ошибки
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

## Фиксация пользовательских значений

С помощью OneAgent SDK for Android вы можете фиксировать события, значения и ошибки. Зафиксированные события, значения и ошибки, являющиеся частью пользовательского действия, отображаются в анализе waterfall для этого действия. Зафиксированные ошибки (как отдельные, так и «привязанные» к пользовательскому действию) также отображаются на странице сведений о пользовательской сессии и на странице **User action analysis**.

Если для вашего приложения включён [режим opt-in для пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений нормативным требованиям вашего региона."), это может повлиять на тегирование пользователей и фиксацию пользовательских событий, действий, значений и ошибок. Точный перечень типов данных, не передаваемых в Dynatrace, зависит от уровня сбора данных, установленного конкретным пользователем. Подробности см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений нормативным требованиям вашего региона.").

### Фиксация события

С помощью `reportEvent` вы можете зафиксировать конкретное событие. Зафиксированное событие должно быть частью пользовательского действия.

Java

Kotlin

```
action.reportEvent("event_name");
```

```
action.reportEvent("event_name")
```

### Фиксация значения

Метод `reportValue` позволяет фиксировать пары «ключ-значение» метаданных, которые впоследствии можно просматривать в веб-интерфейсе Dynatrace и преобразовывать в [свойства пользовательских действий и сессий](/managed/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "Свойства пользовательских действий и сессий — это метаданные в формате «ключ-значение», обеспечивающие расширенную видимость и более глубокий анализ опыта конечных пользователей."). Зафиксированные значения должны быть частью пользовательского действия.

Поддерживаются следующие типы данных:

* [`int`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,int))
* [`long`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,long))
* [`double`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,double))
* [`string`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportValue(java.lang.String,java.lang.String))

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

Чтобы просмотреть зафиксированные значения в веб-интерфейсе Dynatrace, перейдите к сведениям о пользовательском действии, содержащем эти метаданные, и прокрутите вниз до раздела **Reported values**.

![Страница сведений о пользовательском действии с зафиксированными SDK-значениями](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

Страница сведений о пользовательском действии с зафиксированными SDK-значениями

Чтобы добавить свойства действий и сессий на основе зафиксированных значений и использовать их для создания мощных запросов, сегментации и агрегации, см. раздел [Определение свойств пользовательских действий и сессий для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Отправляйте метаданные в Dynatrace и определяйте свойства действий и сессий для мониторинга мобильных приложений.").

### Фиксация ошибки

Метод `reportError` отличается от метода `reportValue` тем, что он специально идентифицируется как [событие типа «ошибка»](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Узнайте о пользовательских и ошибочных событиях и типах событий, фиксируемых Dynatrace.").

OneAgent SDK позволяет фиксировать следующее:

* **Коды ошибок**. Используйте метод [`reportError(String, int)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportError(java.lang.String,int)).
* **Обработанные исключения**. Используйте метод [`reportError(String, Throwable)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#reportError(java.lang.String,java.lang.Throwable)).

Предусмотрено два варианта фиксации ошибки: в рамках пользовательского действия или как отдельная ошибка — глобальное событие, не привязанное к конкретному пользовательскому действию.

#### Ошибка в рамках пользовательского действия

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

Отдельные ошибки можно фиксировать через класс `Dynatrace`.

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

## Мониторинг жизненного цикла Activity

Для отслеживания событий жизненного цикла используется официальный интерфейс Android [`ActivityLifecycleCallbacks`](https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks). Для Activities Dynatrace фиксирует время каждого перехода состояния жизненного цикла вплоть до момента отображения Activity; при наличии временные метки обратных вызовов жизненного цикла отображаются в анализе waterfall пользовательского действия и помечаются как **Lifecycle event**.

### Фиксируемые события жизненного цикла

При мониторинге жизненного цикла OneAgent собирает данные о следующих событиях жизненного цикла класса [`Activity`](https://developer.android.com/reference/android/app/Activity).

* **Activity display**: измеряет время, необходимое для отображения Activity.
* **Activity redisplay**: измеряет время, необходимое для повторного отображения ранее созданной Activity. Возможны два варианта:

  + Вариант 1: Activity находится в состоянии *Stopped* и не отображается на экране, затем переходит в состояния *Started* и *Resumed*.
  + Вариант 2: Activity находится в состоянии *Paused* и частично перекрыта другим элементом, затем переходит в состояние *Resumed*.

Временной интервал для измерения продолжительности события жизненного цикла зависит от типа события и уровня Android API. При использовании Android API уровня 29 и выше продолжительность событий жизненного цикла измеряется точнее благодаря предварительным и постобратным вызовам жизненного цикла.

| Событие жизненного цикла | Android API 29+ | Android API 28 и ниже | Фиксируемые обратные вызовы |
| --- | --- | --- | --- |
| **Activity display** | `onActivityPreCreated` — `onActivityPostResumed` | `onActivityCreated` — `onActivityResumed` | `onCreate` `onStart` `onResume` |
| **Activity redisplay**, вариант 1 | `onActivityPreStarted` — `onActivityPostResumed` | `onActivityStarted` — `onActivityResumed` | `onStart` `onResume` |
| **Activity redisplay**, вариант 2 | `onActivityPreResumed` — `onActivityPostResumed` | Измерение продолжительности невозможно | `onResume` |

### Отключение мониторинга жизненного цикла

Мониторинг жизненного цикла Activity включён по умолчанию, но его можно отключить с помощью метода [`withActivityMonitoring`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withActivityMonitoring(boolean)).

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

[Dynatrace Android Gradle plugin](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Узнайте, как Dynatrace Android Gradle plugin может автоматически инструментировать ваш Android-проект.") автоматически инструментирует большинство веб-запросов. Однако в следующих случаях требуется ручное инструментирование:

* Когда запросы сторонних фреймворков не инструментированы
* Когда нужно [фиксировать не-HTTP(S) запросы](#monitor-non-http-requests)
* Если вы отключили [мониторинг веб-запросов](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#disable-web-request-monitoring "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.")

Для HTTP(S) запросов нельзя сочетать автоматическое и ручное инструментирование. Однако вы можете использовать авто-инструментирование для HTTP(S) запросов и ручное — для [не-HTTP(S) запросов](#monitor-non-http-requests).

Для отслеживания веб-запросов добавьте HTTP-заголовок `x-dynatrace` с уникальным значением к веб-запросу. Это необходимо для сопоставления данных мониторинга на стороне сервера с соответствующим мобильным веб-запросом. Кроме того, необходимо измерять временные значения на стороне мобильного устройства.

Чтобы осуществить мониторинг веб-запроса:

1. Сгенерируйте новый уникальный тег.
2. Создайте объект `WebRequestTiming` на основе тега.
3. Добавьте HTTP-заголовок Dynatrace к вашему веб-запросу.
4. Запустите измерение времени веб-запроса до отправки HTTP-запроса.
5. Остановите измерение времени веб-запроса.

   * Получен HTTP-ответ и тело ответа.
   * Произошло исключение соединения.

Веб-запросы делятся на два вида в зависимости от иерархии:

* [Запросы, привязанные к пользовательскому действию](#attach-request-to-action)
* [Отдельные запросы](#monitor-standalone-request). Для таких запросов OneAgent автоматически пытается найти подходящее пользовательское действие. Если оно найдено, веб-запрос привязывается к нему. Веб-запрос фиксируется как отдельный только в случае, если подходящее пользовательское действие не найдено.

  В настоящее время просмотр отдельных запросов в [**Session Segmentation**](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Узнайте об атрибутах сегментации и фильтрации пользовательских сессий.") невозможен.

### Привязка веб-запроса к пользовательскому действию

Чтобы привязать веб-запрос к пользовательскому действию, сгенерируйте уникальный тег с помощью метода [`DTXAction.getRequestTag()`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/DTXAction.html#getRequestTag()).

Ниже показан пример привязки синхронного `OkHttp` веб-запроса к пользовательскому действию `"Search request"`.

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

### Мониторинг отдельного веб-запроса

Чтобы отслеживать веб-запрос как отдельный, сгенерируйте уникальный тег с помощью метода [`Dynatrace.getRequestTag()`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#getRequestTag()).

### Мониторинг не-HTTP(S) запросов

OneAgent for Android версии 8.249+

Мониторинг WebSocket-соединений доступен начиная с версии OneAgent for Android 8.239. Мониторинг всех не-HTTP(S) запросов доступен начиная с версии 8.249.

OneAgent for Android не поддерживает авто-инструментирование не-HTTP(S) запросов. Для фиксации запросов, таких как WebSocket (начинается с `ws://` или `wss://`), воспользуйтесь приведёнными ниже примерами кода.

* Используйте API-метод [`stopWebRequestTiming(URI requestUri, int respCode, String respPhrase)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/WebRequestTiming.html#stopWebRequestTiming(java.net.URI,int,java.lang.String)) для ручного инструментирования не-HTTP(S) запросов.
* Убедитесь, что передаётся исходный URI. Не получайте URI из объекта `OkHttp`, так как это не вернёт исходный URI.
* Этот подход подходит только для WebSocket-соединений продолжительностью до примерно 9 минут. Более длительные соединения могут не фиксироваться.
* Если у вас только не-HTTP(S) запросы, вы можете при необходимости [отключить мониторинг веб-запросов](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#disable-web-request-monitoring "Настройте Dynatrace Android Gradle plugin для регулировки возможностей мониторинга OneAgent.").
* Если у вас есть и HTTP(S), и не-HTTP(S) запросы, и HTTP(S) инструментированы автоматически, не отключайте мониторинг веб-запросов.

## Фиксация сбоев

OneAgent перехватывает все [необработанные исключения](https://dt-url.net/UncaughtExceptionHandler). Отчёт о [сбое](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Узнайте о пользовательских и ошибочных событиях и типах событий, фиксируемых Dynatrace.") включает время возникновения и полную трассировку стека исключения.

Как правило, сведения о сбое отправляются сразу после его возникновения, так что пользователю не нужно перезапускать приложение. Однако в некоторых случаях приложение должно быть открыто повторно в течение 10 минут, чтобы отчёт о сбое был отправлен. Обратите внимание, что Dynatrace не отправляет отчёты о сбоях, произошедших более 10 минут назад (такие отчёты не могут быть сопоставлены на кластере Dynatrace).

Вы можете отключить фиксацию сбоев с помощью метода [`withCrashReporting`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withCrashReporting(boolean)).

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

Вы можете назначить каждому пользователю мобильного приложения уникальное имя пользователя. Это позволяет искать и фильтровать конкретные пользовательские сессии и анализировать поведение отдельных пользователей с течением времени. Подробнее см. в разделе [Тегирование пользователей](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Узнайте о пользовательских и ошибочных событиях и типах событий, фиксируемых Dynatrace.").

Следующие шаги объясняют, как тегировать отдельного пользователя через Dynatrace API.

Java

Kotlin

```
Dynatrace.identifyUser("john.doe@example.com");
```

```
Dynatrace.identifyUser("john.doe@example.com")
```

OneAgent for Android версии 237+: сессии, завершённые из-за тайм-аута простоя или продолжительности, повторно тегируются автоматически.

Когда OneAgent завершает тегированную сессию из-за достижения заданного лимита продолжительности или неактивности пользователя, последующая сессия автоматически получает тег. Повторно предоставлять идентификационные данные пользователя не нужно.

Однако обратите внимание, что OneAgent не тегирует последующую сессию в следующих случаях:

* Когда вы явно завершаете тегированную пользовательскую сессию через [`endVisit`](#end-session)
* Когда пользователь или мобильная ОС закрывает или принудительно останавливает приложение
* Когда OneAgent завершает текущую пользовательскую сессию и создаёт новую после изменения настроек конфиденциальности

См. раздел [Пользовательские сессии > Завершение сессии](/managed/observe/digital-experience/rum-concepts/user-session#user-session-end--mobile-apps "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её продолжительность и многое другое."), чтобы узнать, когда OneAgent завершает мобильную пользовательскую сессию.

Если для вашего приложения включён [режим opt-in для пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений нормативным требованиям вашего региона."), это может повлиять на тегирование пользователей и фиксацию пользовательских событий, действий, значений и ошибок.

## Завершение сессии

Вы можете принудительно завершить сессию через Dynatrace API. При этом закрываются все открытые действия и начинается новая сессия.

Java

Kotlin

```
Dynatrace.endVisit();
```

```
Dynatrace.endVisit()
```

## Настройка конфиденциальности данных (режим opt-in)

В режиме opt-in для пользователя каждый пользователь вашего приложения может устанавливать собственные настройки конфиденциальности и решать, хочет ли он делиться своими данными. При включённом режиме opt-in необходимо запрашивать у каждого пользователя разрешение на сбор данных, а затем сохранять его предпочтения. Подробнее см. в разделе [Режим opt-in для пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений нормативным требованиям вашего региона.").

### Включение режима opt-in для пользователя

Чтобы активировать режим opt-in для пользователя, включите флаг `userOptIn` через DSL Dynatrace Android Gradle plugin или используйте метод `ConfigurationBuilder.withUserOptIn`.

### Изменение настроек конфиденциальности пользователя

С помощью метода [`Dynatrace.applyUserPrivacyOptions`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#applyUserPrivacyOptions(com.dynatrace.android.agent.conf.UserPrivacyOptions)) вы можете скорректировать настройки конфиденциальности на основе решения конкретного пользователя.

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

Возможные значения [уровня сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений нормативным требованиям вашего региона."):

* `OFF`
* `PERFORMANCE`
* `USER_BEHAVIOR`

OneAgent сохраняет настройки конфиденциальности и автоматически применяет их при перезапуске приложения. Кроме того, при изменении настроек конфиденциальности OneAgent генерирует новую сессию.

### Получение настроек конфиденциальности пользователя

Также вы можете получить настройки конфиденциальности конкретного пользователя с помощью метода [`Dynatrace.getUserPrivacyOptions`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#getUserPrivacyOptions()). Используйте этот метод только после запуска OneAgent.

## Настройка гибридных приложений

В гибридных приложениях нативное мобильное приложение отслеживается OneAgent, а браузерная часть — [Dynatrace RUM JavaScript](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Узнайте, как настроить Real User Monitoring с помощью JavaScript API."). Поэтому мониторинг гибридных приложений требует дополнительной настройки. Подробнее см. в разделе [Инструментирование гибридных приложений](/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app "Узнайте, как инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.").

### Включение мониторинга гибридных приложений

Чтобы активировать функцию мониторинга гибридных приложений, используйте метод [`withHybridMonitoring`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withHybridMonitoring(boolean)).

### Указание доменов, хостов и IP-адресов

Для гибридных приложений, использующих RUM JavaScript внутри `WebView`, OneAgent должен устанавливать cookies для каждого инструментированного домена или сервера, с которым взаимодействует приложение. При включённой функции мониторинга гибридных приложений OneAgent генерирует эти cookies для каждого указанного домена и сохраняет их в `CookieManager`. Dynatrace использует эти cookies для идентификации мобильных и веб-сессий в приложении и объединения их в одну «гибридную» сессию.

Для указания доменов, хостов и IP-адресов используйте метод [`withMonitoredDomains`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withMonitoredDomains(java.lang.String...)) или [`withMonitoredHttpsDomains`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withMonitoredHttpsDomains(java.lang.String...)). Домены и субдомены должны начинаться с точки (`.`).

### Инструментирование `WebView`

Чтобы обеспечить взаимодействие между RUM JavaScript и OneAgent for Android, инструментируйте все объекты `WebView` перед загрузкой URL с помощью [`WebView.loadUrl(String)`](https://developer.android.com/reference/android/webkit/WebView#loadUrl(java.lang.String)). Вызывайте метод [`Dynatrace.instrumentWebView`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#instrumentWebView(android.webkit.WebView)) для каждого `WebView`, содержащего RUM JavaScript. Без этого данные мониторинга из `WebView` не будут ассоциированы с той же мобильной сессией.

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

### Отключение cookies для файловых доменов

OneAgent for Android версии 8.271+

Для установки cookies для файловых доменов (начинающихся с `file://`) Dynatrace использует [`setAcceptFileSchemeCookies`](https://developer.android.com/reference/android/webkit/CookieManager#setAcceptFileSchemeCookies(boolean)). Однако этот API больше не рекомендуется из-за проблем безопасности; в ближайшие месяцы планируется прекратить добавление cookies для доменов файловой схемы.

Если вы хотите защитить приложение прямо сейчас, установите `fileDomainCookies` в значение `false`, и Dynatrace не будет добавлять cookies для файловых доменов.

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

В гибридных приложениях важно следить за тем, чтобы cookies Dynatrace не удалялись. Без этих cookies Dynatrace не сможет объединить данные мониторинга от RUM JavaScript и OneAgent в одну сессию.

При удалении cookies через [`CookieManager#removeAllCookies(ValueCallback)`](https://developer.android.com/reference/android/webkit/CookieManager#removeAllCookies(android.webkit.ValueCallback%3Cjava.lang.Boolean%3E)) или [`CookieManager#removeSessionCookies(ValueCallback)`](https://developer.android.com/reference/android/webkit/CookieManager#removeSessionCookies(android.webkit.ValueCallback%3Cjava.lang.Boolean%3E)) следует также вызывать метод [`restoreCookies`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#restoreCookies()) для восстановления cookies Dynatrace.

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

OneAgent позволяет включить клиентскую балансировку нагрузки, которая помогает избежать неравномерной нагрузки на сервер при одновременном установлении соединения несколькими OneAgent с ActiveGate.

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