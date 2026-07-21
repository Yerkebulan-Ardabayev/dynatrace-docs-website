---
title: OneAgent SDK для iOS в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios
---

# OneAgent SDK для iOS в RUM Classic

# OneAgent SDK для iOS в RUM Classic

* Практическое руководство
* Чтение 23 мин
* Обновлено 24 марта 2026 г.

OneAgent SDK для iOS используется для отчёта дополнительных сведений о пользовательских сессиях в мобильном приложении. OneAgent SDK для iOS позволяет создавать пользовательские действия, измерять веб-запросы, сообщать об ошибках и помечать конкретных пользователей. В разделах ниже объясняется, как включить эти возможности.

Для iOS OneAgent SDK доступен автоматически после добавления в проект CocoaPod Dynatrace. OneAgent SDK для iOS можно использовать на Swift и Objective-C.

## Запуск OneAgent

Запуск OneAgent для iOS возможен только один раз. Несколько запусков в рамках одного приложения не поддерживаются.

Чтобы отключить [автоматический запуск OneAgent](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#automatic-startup "Explore the list of features that are available after you instrument your application with OneAgent."), установи для [ключа конфигурации `DTXAutoStart`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") значение `false` в файле [`Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") приложения:

```
<key>DTXAutoStart</key>



<false/>
```

После этого OneAgent можно запустить вручную, используя либо конфигурацию `Info.plist`, либо переданный словарь конфигурации.

Рекомендуется запускать OneAgent как можно раньше, например, в `applicationWillFinishLaunching`.

### Запуск OneAgent с конфигурацией `Info.plist`

Чтобы запустить OneAgent с конфигурацией из файла `Info.plist`, используй вызов API `startupWithInfoPlistSettings`.

OneAgent для iOS запустится только в том случае, если запуск выполнен в главном потоке.

Swift

Objective-C

```
Dynatrace.startupWithInfoPlistSettings()
```

```
[Dynatrace startupWithInfoPlistSettings];
```

### Запуск OneAgent с переданным словарём конфигурации

Чтобы запустить OneAgent с переданным словарём конфигурации, используй вызов API `startupWithConfig`. [Ключи конфигурации](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") для словаря такие же, как и для файла `Info.plist`, их также можно найти в заголовочном файле `Dynatrace.h`, поставляемом вместе с OneAgent.

Swift

Objective-C

```
let startupDictionary: [String : Any?] = [



kDTXApplicationID: "aaaa-bbbb-cccc-dddd-eeee-ffff",



kDTXBeaconURL: "https://my.beacon.url/mbeacon",



kDTXLogLevel: "WARNING"



]



Dynatrace.startup(withConfig: startupDictionary)
```

```
NSDictionary<NSString*, id> *startupDictionary = @{



kDTXApplicationID: @"aaaa-bbbb-cccc-dddd-eeee-ffff",



kDTXBeaconURL: @"https://my.beacon.url/mbeacon",



kDTXLogLevel: @"WARNING"



};



[Dynatrace startupWithConfig:startupDictionary];
```

Ключи конфигурации [`DTXApplicationID` и `DTXBeaconURL`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") требуются всегда.

Может потребоваться указать дополнительные параметры. Чтобы узнать, какие параметры и значения передавать, обратись к [мастеру инструментирования](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Set up user experience monitoring for iOS apps within Dynatrace.") в Dynatrace.

## Создание пользовательских действий

Можно определять и сообщать пользовательские действия. После их запуска [дополни их дополнительной информацией](#custom-action-additional-info), прежде чем окончательно закрыть.

Если нужно изменить автоматически сгенерированное пользовательское действие, см. [Изменение и отмена автоматически сгенерированных действий](#modify-auto-actions).

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на маркировку пользователей и отчётность по пользовательским событиям, действиям, значениям и ошибкам. Точные типы данных, которые не сообщаются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Запуск и закрытие пользовательских действий

В приведённом ниже фрагменте кода показано, как запустить и закрыть пользовательское действие. Обрати внимание, что OneAgent отбрасывает все данные мониторинга, связанные с действием, если пользовательское действие не закрыто. Время измеряется автоматически.

Swift

Objective-C

```
// start the "Tap on Search" action



let action = DTXAction.enter(withName: "Tap on Search")



// ...do some work here...



// close the "Tap on Search" action



action?.leave()
```

```
// start the "Tap on Search" action



DTXAction *action = [DTXAction enterActionWithName:@"Tap on Search"];



// ...do some work here...



// close the "Tap on Search" action



[action leaveAction];
```

Для мобильного пользовательского действия или мобильного автоматически сгенерированного пользовательского действия максимальная длина имени составляет 250 символов.

Максимальная продолжительность мобильного пользовательского действия, 9 минут.

Если пользовательское действие длится дольше 9 минут и не закрыто, такое действие отбрасывается и не передаётся в Dynatrace.

С пользовательским действием можно выполнять следующие операции мониторинга:

* [Создать дочернее действие](#create-child-action)
* [Сообщить о событии](#report-event)
* [Сообщить значение](#report-value)
* [Сообщить об ошибке](#report-error)
* [Прикрепить веб-запрос](#measure-web-requests)
* [Отменить действие](#cancel-action)

### Создание дочерних действий

[Дочерние действия](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#child-actions "Learn what user actions are and how they help you understand what users do with your application.") похожи на родительские действия. Когда родительское действие закрывается, OneAgent автоматически закрывает все дочерние действия этого родительского действия.

В приведённом ниже фрагменте кода показано, как запустить действие как дочернее по отношению к другому действию.

Swift

Objective-C

```
// start a parent custom action



let searchAction = DTXAction.enter(withName: "Tap on Search")



// ...do some work here...



// start a child action



let parseAction = DTXAction.enter(withName: "Tap on Confirm", parentAction: searchAction)



// ...do some work here...



// close a child action



parseAction?.leave()



// ...do some work here...



// close a parent custom action



searchAction?.leave()
```

```
// start a parent custom action



DTXAction *searchAction = [DTXAction enterActionWithName: @"Tap on Search"];



// ...do some work here...



// start a child action



DTXAction *parseAction = [DTXAction enterActionWithName: @"Tap on Confirm" parentAction: searchAction];



// ...do some work here...



// close a child action



[parseAction leaveAction];



// ...do some work here...



// close a parent custom action



[searchAction leaveAction];
```

Для мобильного пользовательского действия или мобильного автоматически сгенерированного пользовательского действия максимальная длина имени составляет 250 символов.

Ограничения на количество дочерних действий, прикреплённых к родительскому действию, нет. Однако обрати внимание, что доступно только девять уровней вложенности дочерних действий: можно создать одно родительское действие и девять уровней дочерних действий (когда дочернее действие A добавлено к родительскому действию, дочернее действие B добавлено к дочернему действию A, дочернее действие C добавлено к дочернему действию B и так далее). См. также [Структура пользовательской сессии для отдельного пользователя](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#session-structure-dep-on-app-type "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").

Дочерние действия не отображаются на [странице сведений о пользовательской сессии](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions#session-details-page "Learn about user session segmentation and filtering attributes."), но их можно просмотреть на [странице waterfall-анализа](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") для родительского действия, к которому прикреплены эти дочерние действия. Хотя вложенность дочерних действий не полностью сохраняется в представлении waterfall-анализа и все дочерние действия отображаются как дочерние действия уровня 1, вложенность действий всё равно можно понять по времени выполнения.

### Пример пользовательского действия

Ниже приведён пример ручной инструментации.

Swift

Objective-C

```
func countParameters(query: String?) -> Int {



var count: Int = 0



//create a parent custom action



let checkQueryAction = DTXAction.enter(withName: "Tap on Check query")



//report a value on an action



checkQueryAction?.reportValue(withName: "query", stringValue: String(describing: query))



let countParametersAction = DTXAction.enter(withName: "Count parameters", parentAction: checkQueryAction)



if let query = query {



count = query.components(separatedBy:"&").count



//report a value



countParametersAction?.reportValue(withName: "Parameters found", intValue: Int64(count))



//close a child action



countParametersAction?.leave()



} else {



//report an event



countParametersAction?.reportEvent(withName: "No parameters found")



//close a child action



countParametersAction?.leave()



//report an error



checkQueryAction?.reportError(withName: "Query was nil", errorValue: -42)



}



//close a parent custom action - automatically closes all open child actions if not closed by API



checkQueryAction?.leave()



return count



}
```

```
- (int) countParameters: (NSString *) query {



int count = 0;



//create a parent custom action



DTXAction *checkQueryAction = [DTXAction enterActionWithName:@"Tap on Check query"];



//report a value on an action



[checkQueryAction reportValueWithName:@"query" stringValue:query];



DTXAction *countParametersAction = [DTXAction enterActionWithName:@"Count parameters" parentAction:checkQueryAction];



if (query != nil) {



count = [query componentsSeparatedByString:@"&"].count;



//report a value



[countParametersAction reportValueWithName:@"Parameters found" intValue:count];



//close a child action



[countParametersAction leaveAction];



} else {



//report an event



[countParametersAction reportEventWithName:@"No parameters found"];



//close a child action



[countParametersAction leaveAction];



//report an error



[checkQueryAction reportErrorWithName:@"Query was nil" errorValue:-42];



}



//close a parent custom action - automatically closes all open child actions if not closed by API



[checkQueryAction leaveAction];



return count;



}
```

## Отмена действий

OneAgent для iOS версии 8.229+

Можно отменить [пользовательское действие](#create-custom-user-action) или [автоматически сгенерированное действие пользователя](#modify-auto-actions). Отмена действия отбрасывает все связанные с ним данные: все переданные значения отбрасываются, все дочерние действия отменяются.

Закрытое действие отменить нельзя, поэтому вызов `cancel`/`cancelAction` после `leave`/`leaveAction` для одного и того же действия невозможен. То же самое касается закрытия отменённого действия: нельзя вызвать `leave`/`leaveAction` после использования `cancel`/`cancelAction` для одного и того же действия.

Swift

Objective-C

```
// start the "Tap on Search" action



let action = DTXAction.enter(withName: "Tap on Search")



// ...do some work here...



// cancel the "Tap on Search" action



action?.cancel()
```

```
// start the "Tap on Search" action



DTXAction *action = [DTXAction enterActionWithName:@"Tap on Search"];



// ...do some work here...



// cancel the "Tap on Search" action



[action cancelAction];
```

## Передача события

С помощью `reportEvent` можно передать конкретное событие. Событие должно принадлежать существующему [пользовательскому действию](#create-custom-user-action) или [автоматически сгенерированному действию пользователя](#modify-auto-actions). Переданные события отображаются в waterfall-анализе действий пользователя.

Swift

Objective-C

```
let myAction = DTXAction.enter(withName: "My action")



myAction?.reportEvent(withName: "Something important just happened")



myAction?.leave()
```

```
// report an event



- (DTX_StatusCode) reportEventWithName:(NSString *)eventName
```

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не передаваемые в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

## Передача ошибки

С помощью `reportError` можно передать конкретное событие как [ошибку](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.").

Есть два варианта передачи ошибки.

* Передать её как часть действия (либо [пользовательского действия](#create-custom-user-action), либо [автоматически сгенерированного действия пользователя](#modify-auto-actions))
* Передать её как отдельную ошибку, которая генерируется как глобальное событие, не привязанное к конкретному действию

Переданные ошибки (как отдельные, так и «привязанные» к действию пользователя) отображаются на странице сведений о пользовательской сессии и на многомерной странице **User action analysis**. Переданные ошибки, являющиеся частью действия пользователя, также отображаются в waterfall-анализе действий пользователя.

Ошибку можно передать с кодом ошибки, исключением или `NSError`.

Swift

Objective-C

Отдельная ошибка (не привязанная к конкретному действию пользователя)

```
DTXAction.reportError(withName: "My custom error", error: NSError(domain: "Global issue", code: 007, userInfo: nil))
```

Ошибка, привязанная к конкретному действию пользователя

```
let myAction = DTXAction.enter(withName: "My action")



myAction?.reportError(withName: "My custom error", error: NSError(domain: "Action issue", code: 007, userInfo: nil))



myAction?.leave()
```

```
// report an error



DTXAction *action;



NSError* error;



[action reportErrorWithName:@"CommunicationError" errorValue:[error code]];
```

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, не передаваемые в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробности см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

## Передача значения

Метод `reportValue` позволяет передавать пары «ключ-значение» метаданных, которые впоследствии можно просмотреть в веб-интерфейсе Dynatrace и преобразовать в [свойства действия и сессии пользователя](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more."). Переданные значения должны быть частью действия пользователя.

Можно передавать значения следующих типов данных:

* `int`
* `double`
* `string`

Swift

Objective-C

```
let myAction = DTXAction.enter(withName: "My action")



myAction?.reportValue(withName: "My int value", intValue: 1234)



myAction?.reportValue(withName: "My double value", doubleValue: 12.34)



myAction?.reportValue(withName: "My string value", stringValue: "Hello World!")



myAction?.leave()
```

```
- (DTX_StatusCode) reportValueWithName:(NSString *)valueName



intValue:(NSInteger)value



- (DTX_StatusCode) reportValueWithName:(NSString *)valueName



doubleValue:(double)doubleValue



- (DTX_StatusCode) reportValueWithName:(NSString *)valueName



stringValue:(NSString *)stringValue
```

Чтобы просмотреть переданные значения в веб-интерфейсе Dynatrace, перейдите к сведениям о действии пользователя, которое должно содержать эти метаданные, и прокрутите вниз до раздела **Reported values**.

![User action details page with SDK-reported values](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

Страница сведений о действии пользователя с переданными значениями SDK

Чтобы добавить свойства действия и сессии на основе переданных значений и затем использовать эти свойства для создания мощных запросов, сегментаций и агрегаций, см. [Определение свойств действия и сессии пользователя для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored mobile applications.").

## Измерение веб-запросов

Для отслеживания веб-запросов OneAgent добавляет к каждому запросу HTTP-заголовок `x-dynatrace` с уникальным значением. Это нужно для сопоставления серверных данных мониторинга с соответствующим мобильным веб-запросом. Дополнительно измеряются значения тайминга с мобильной стороны.

OneAgent для iOS автоматически замеряет время веб-запросов, выполненных с помощью `NSURLRequest`, `NSURLConnection`, `NSURLSession`, `NSURLProtocol`, `NSString`, `WKWebView` или `NSData`. Однако в следующих случаях запросы нужно инструментировать вручную:

* когда [автоматическое инструментирование веб-запросов отключено](#disable-auto-request-instrumentation);
* когда запросы стороннего фреймворка не инструментированы;
* когда нужно [сообщать о запросах, не использующих HTTP(S)](#measure-non-http-requests).

### Какой тип инструментирования использовать

Для HTTP(S)-запросов нельзя комбинировать автоматическое и ручное инструментирование веб-запросов. Однако можно использовать автоматическое инструментирование для HTTP(S)-запросов и ручное инструментирование для [запросов, не использующих HTTP(S)](#measure-non-http-requests), таких как WebSocket или gRPC.

В таблице ниже поясняется, какой тип инструментирования запросов использовать в зависимости от того, какие типы запросов есть в приложении. Также в ней показано, нужно ли [отключать автоматическое инструментирование запросов](#disable-auto-request-instrumentation).

| Тип запроса | Тип инструментирования | `DTXInstrumentWebRequestTiming` |
| --- | --- | --- |
| Только HTTP(S) | Вариант A: автоматическое | `true` |
|  | Вариант B: ручное | `false` |
| Только не HTTP(S) | Ручное | `false` (опционально) |
| HTTP(S) + не HTTP(S) | Вариант A: автоматическое для HTTP(S) и ручное для не HTTP(S) | `true` |
|  | Вариант B: ручное | `false` |

### Родительское действие веб-запросов

Существует заданный порядок, которому следует OneAgent для iOS при определении родителя события веб-запроса, что влияет на то, как веб-запросы отображаются в анализе waterfall.

#### Автоматическое инструментирование веб-запросов

* Если в том же потоке, что и веб-запрос, запущено активное [пользовательское действие](#create-custom-user-action), то это действие становится родительским.
* Если активного пользовательского действия нет, но есть активное [автоматически сгенерированное действие](#modify-auto-actions), то родительским становится это автоматически сгенерированное действие (например, `Touch on...`). Сюда же относится автоматически сгенерированное действие `Loading ...`.
* Если OneAgent не может найти активное действие, то событие веб-запроса становится событием корневого уровня без родительского действия.

#### Ручное инструментирование веб-запросов

* Если родительское действие не указано (`Dynatrace.getRequestTagValue(for: url)`), то поведение при поиске родительского действия такое же, как при автоматическом тайминге веб-запросов.
* Если родительское действие указано (`childAction?.getTagFor(url)`), то родительским становится это действие.

В настоящее время автономные события веб-запросов корневого уровня нельзя просмотреть в разделе [**Session Segmentation**](/managed/observe/digital-experience/rum-classic/session-segmentation/user-sessions "Learn about user session segmentation and filtering attributes.").

### Пример: упрощённое ручное инструментирование веб-запроса

```
import UIKit



import WebKit



import Dynatrace



class ViewController: UIViewController {



override func viewDidLoad() {



super.viewDidLoad()



let wkWebView = WKWebView(frame: self.view.frame)



self.view.addSubview(wkWebView)



manualTaggingDemo(wkWebView: wkWebView)



}



func manualTaggingDemo(wkWebView: WKWebView) {



let parentAction = DTXAction.enter(withName: #function)



let url = URL(string: "https://www.dynatrace.com")



downloadRequest(url: url!, wkWebView: wkWebView, parentAction: parentAction)  //as this is async parent action should be left when request is done



}



func downloadRequest(url: URL, wkWebView: WKWebView, parentAction: DTXAction?) {



let childAction = DTXAction.enter(withName: #function, parentAction: parentAction)  //add child action to see method call trace



let session = URLSession.shared



let request = NSMutableURLRequest(url: url)



request.httpMethod = "GET"



request.cachePolicy = .reloadIgnoringCacheData



var webrequestTiming: DTXWebRequestTiming?



//if let dynatraceHeaderValue = Dynatrace.getRequestTagValue(for: url) {  //let agent decide which action it uses as parent (last created action)



if let dynatraceHeaderValue = childAction?.getTagFor(url) {  //provide parent action



let dynatraceHeaderKey = Dynatrace.getRequestTagHeader() //this could be cached as it always is x-dynatrace



request.setValue(dynatraceHeaderValue, forHTTPHeaderField: dynatraceHeaderKey)



webrequestTiming = DTXWebRequestTiming.getDTXWebRequestTiming(dynatraceHeaderValue, request: url)



}



let task = session.downloadTask(with: request as URLRequest) {



(location, response, error) in



defer {



parentAction?.leave()   //leave parent action when request finished - all child actions are automatically left on leaving parent



}



guard let _:URL = location, let _:URLResponse = response, error == nil else {



webrequestTiming?.stop("failed") //stop webrequest timing in error case



return



}



let urlContents = try! String(contentsOf: location!, encoding: .utf8)



guard !urlContents.isEmpty else {



webrequestTiming?.stop("empty content") //stop webrequest timing in error case



return



}



webrequestTiming?.stop((response as! HTTPURLResponse).statusCode.description) //stop webrequest when request finished



DispatchQueue.main.async {



wkWebView.loadHTMLString(urlContents, baseURL: nil)



}



}



webrequestTiming?.start()    //start webrequest timing



task.resume()



}



}
```

### Мониторинг запросов, не использующих HTTP(S)

OneAgent для iOS не поддерживает автоинструментирование не-HTTP(S) запросов. Если нужно репортить такие запросы, как WebSocket-запрос (начинается с `ws://` или `wss://`), см. следующие примеры кода.

Если есть только не-HTTP(S) запросы, можно [отключить автоматическое инструментирование запросов](#disable-auto-request-instrumentation), но это не обязательно.

Если есть и HTTP(S), и не-HTTP(S) запросы, а HTTP(S) запросы автоинструментируются, не отключай автоматическое инструментирование запросов.

Swift

Objective-C

```
import UIKit



import Dynatrace



class ViewController: UIViewController {



override func viewDidLoad() {



guard let parentAction = DTXAction.enter(withName: #function) else {



print("unable to enter action")



return



}



defer { parentAction.leave() }



webSocketMonitoringExample(parentAction: parentAction)



}



func webSocketMonitoringExample(parentAction : DTXAction) {



guard let childAction = DTXAction.enter(withName: #function, parentAction: parentAction) else {



print("unable to enter child action")



return



}



defer { childAction.leave() }



let urlSession = URLSession(configuration: .default)



guard let url = URL(string: "wss://....") else {



print("unable to create URL")



return



}



// not sending the tag, just using it for internal reference



guard let tag = childAction.getTagFor(url) else {



print("unable to create tag")



return



}



let webrequestTiming = DTXWebRequestTiming.getDTXWebRequestTiming(tag, request: url)



let webSocketTask = urlSession.webSocketTask(with: url)



webSocketTask.resume()



webrequestTiming?.start()



let messageString = "Hello World"



let bytesSent = Int64(messageString.data(using: .utf8)?.count ?? 0) // sample



let message = URLSessionWebSocketTask.Message.string(messageString)



webSocketTask.send(message) { error in



if let error = error {



print("send error: \(error.localizedDescription)")



}



}



// synchronous example



let receiveDispatch = DispatchGroup()



receiveDispatch.enter()



var bytesReceived:Int64 = 0



webSocketTask.receive { result in



let receievedString = "\(result)"



print("received data: \(receievedString)")



bytesReceived = Int64(receievedString.data(using: .utf8)?.count ?? 0) // sample



receiveDispatch.leave()



}



receiveDispatch.wait()



webSocketTask.cancel()



webrequestTiming?.stop(String(URLSessionWebSocketTask.CloseCode.normalClosure.rawValue), bytesSent: bytesSent, bytesReceived: bytesReceived)



}



}
```

```
#import "ViewController.h"



#import <Dynatrace/Dynatrace.h>



@interface ViewController ()



@end



@implementation ViewController



- (void)viewDidLoad {



[super viewDidLoad];



DTXAction* parent = [DTXAction enterActionWithName: [NSString stringWithFormat:@"%s", __FUNCTION__]];



[self webSocketMonitoringExample:parent];



[parent leaveAction];



}



- (void)webSocketMonitoringExample:(DTXAction*)parentAction {



DTXAction* childAction = [DTXAction enterActionWithName:[NSString stringWithFormat:@"%s", __FUNCTION__] parentAction:parentAction];



NSURLSession* urlSession = [NSURLSession sessionWithConfiguration:NSURLSessionConfiguration.defaultSessionConfiguration];



NSURL* url = [NSURL URLWithString:@"wss://...."]; // example echo wss server



NSString* tag = [childAction getTagForURL:url]; // not sending the tag, just using it for internal reference



DTXWebRequestTiming* webrequestTiming = [DTXWebRequestTiming getDTXWebRequestTiming:tag requestUrl:url];



NSURLSessionWebSocketTask* webSocketTask = [urlSession webSocketTaskWithURL:url];



[webSocketTask resume];



[webrequestTiming startWebRequestTiming];



NSURLSessionWebSocketMessage* message = [[NSURLSessionWebSocketMessage alloc] initWithString:@"Hello World"];



NSUInteger bytesSent = [message.string dataUsingEncoding:NSUTF8StringEncoding].length; // sample



[webSocketTask sendMessage:message completionHandler:^(NSError * _Nullable error) {



if (error) {



NSLog(@"send error: %@", error.localizedDescription);



}



}];



// synchronous example



__block NSUInteger bytesReceieved;



dispatch_group_t receiveDispatch = dispatch_group_create();



dispatch_group_enter(receiveDispatch);



[webSocketTask receiveMessageWithCompletionHandler:^(NSURLSessionWebSocketMessage * _Nullable message, NSError * _Nullable error) {



bytesReceieved = [message.string dataUsingEncoding:NSUTF8StringEncoding].length; // sample



NSLog(@"received data: %@", message.string);



dispatch_group_leave(receiveDispatch);



}];



dispatch_group_wait(receiveDispatch, DISPATCH_TIME_FOREVER);



[webSocketTask cancel];



[webrequestTiming stopWebRequestTiming:[NSString stringWithFormat:@"%ld", (long)NSURLSessionWebSocketCloseCodeNormalClosure] bytesSent:bytesSent bytesReceived:bytesReceieved];



[childAction leaveAction];



}



@end
```

Указание количества отправленных и полученных байт (также известных как размеры запроса и ответа) при ручном репортинге веб-запроса возможно только для OneAgent для iOS версии 8.285+. Эта дополнительно предоставляемая информация затем отображается в веб-интерфейсе Dynatrace на следующих страницах.

* На странице деталей веб-запросов (доступна через раздел [**Top providers**](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/analyze-web-requests-mobile#top-providers "Leverage Dynatrace to monitor web requests for your mobile applications."))—показывается только размер запроса (отправленные байты)
* На странице **User action analysis** для веб-запросов, привязанных к действиям пользователя—показываются и отправленные, и полученные байты (размеры запроса и ответа)

### Отключение автоматического инструментирования запросов

Чтобы отключить автоматическое инструментирование веб-запросов, установи для [ключа конфигурации `DTXInstrumentWebRequestTiming`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") значение `false`.

## Тегирование конкретных пользователей

Можно пометить тегом каждого пользователя мобильного приложения уникальным именем пользователя. Это позволяет искать и фильтровать сессии конкретных пользователей и анализировать поведение отдельного пользователя во времени. Подробнее см. [User tagging](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.").

Ниже описано, как вручную пометить тегом отдельного пользователя через Dynatrace API.

Swift

Objective-C

```
Dynatrace.identifyUser("userId")
```

```
[Dynatrace identifyUser:@"userId"];
```

OneAgent для iOS версии 235+ Сессии, разделённые из-за таймаута простоя или длительности, тегируются повторно автоматически.

Когда OneAgent завершает помеченную тегом сессию из-за того, что длительность сессии достигла установленного лимита, или из-за неактивности пользователя, последующая сессия тегируется автоматически. Не нужно повторно предоставлять информацию идентификации пользователя.

Однако обрати внимание, что OneAgent не тегирует повторно последующую сессию в следующих случаях:

* Когда явно завершается помеченная тегом пользовательская сессия через [`endVisit`](#end-session)
* Когда пользователь или мобильная операционная система закрывает или принудительно останавливает приложение
* Когда OneAgent завершает текущую пользовательскую сессию и создаёт новую сессию после изменения настроек приватности

См. [User sessions > Session end](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session#user-session-end--mobile-apps "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more."), чтобы узнать, когда OneAgent завершает мобильную пользовательскую сессию.

Если для приложения включён [режим согласия пользователя (opt-in)](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."), это может повлиять на тегирование пользователей и репортинг пользовательских событий, действий пользователя, значений и ошибок. Точные типы данных, не репортящиеся в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. [Data collection levels](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

## Завершение сессии

Можно принудительно завершить сессию через Dynatrace API. Это также закрывает все открытые действия и запускает новую сессию.

Swift

Objective-C

```
Dynatrace.endVisit()
```

```
[Dynatrace endVisit];
```

## Настройка приватности данных (режим opt-in)

В режиме согласия пользователя (opt-in) каждый пользователь приложения может задать свои настройки приватности данных и решить, хочет ли он делиться своей информацией. Когда режим opt-in включён, нужно запросить у каждого пользователя разрешение на сбор его данных, а затем сохранить его настройки приватности данных. Подробнее см. [User opt-in mode](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.").

### Включение режима согласия пользователя (opt-in)

Чтобы включить режим согласия пользователя (user opt-in mode), добавьте [ключ конфигурации `DTXUserOptIn`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в [файл `Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") приложения:

```
<key>DTXUserOptIn</key>



<true/>
```

### Изменение настроек конфиденциальности данных пользователя

В следующих примерах кода показано, как настроить параметры конфиденциальности данных в зависимости от решения конкретного пользователя.

Swift

Objective-C

```
import Dynatrace



…



let privacyConfig = Dynatrace.userPrivacyOptions()



// set a data collection level (user allowed you to capture performance and personal data)



privacyConfig.dataCollectionLevel = .userBehavior



// allow crash reporting (user allowed you to collect information on crashes)



privacyConfig.crashReportingOptedIn = true



// allow Session Replay on crashes (user allowed you to record replays of crashes via Session Replay)



privacyConfig.crashReplayOptedIn = true



// callback after privacy changed



Dynatrace.applyUserPrivacyOptions(privacyConfig) { (successful) in



}
```

```
#import <Dynatrace/Dynatrace.h>



…



id<DTXUserPrivacyOptions> privacyConfig = [Dynatrace userPrivacyOptions];



// set a data collection level (user allowed you to capture performance and personal data)



privacyConfig.dataCollectionLevel = DTX_DataCollectionUserBehavior;



// allow crash reporting (user allowed you to collect information on crashes)



privacyConfig.crashReportingOptedIn = YES;



// allow Session Replay on crashes (user allowed you to record replays of crashes via Session Replay)



privacyConfig.crashReplayOptedIn = YES;



// callback after privacy changed



[Dynatrace applyUserPrivacyOptions:privacyConfig completion:^(BOOL successful) {



}];
```

Возможные значения для [уровня сбора данных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") следующие:

| Swift | Objective-C |
| --- | --- |
| `.off` | `DTX_DataCollectionOff` |
| `.performance` | `DTX_DataCollectionPerformance` |
| `.userBehavior` | `DTX_DataCollectionUserBehavior` |

OneAgent сохраняет настройки конфиденциальности данных и автоматически применяет их при перезапуске приложения. Каждый раз, когда пользователь меняет уровень сбора данных, OneAgent создаёт новую сессию с новыми настройками. Не оборачивайте этот метод API в пользовательское действие, иначе OneAgent не сможет привязать пользовательское действие к нужной сессии.

### Получение настроек конфиденциальности данных пользователя

Те же свойства можно использовать для получения настроек конфиденциальности данных конкретного пользователя.

Swift

Objective-C

```
import Dynatrace



…



let privacyOptions = Dynatrace.userPrivacyOptions()



let dataCollectionLevel = privacyConfig.dataCollectionLevel



let crashReporting = privacyConfig.crashReportingOptedIn



let crashReplay = privacyConfig.crashReplayOptedIn
```

```
#import <Dynatrace/Dynatrace.h>



…



id<DTXUserPrivacyOptions> privacyConfig = [Dynatrace userPrivacyOptions];



DTX_DataCollectionLevel level=  privacyConfig.dataCollectionLevel;



BOOL crashReporting = privacyConfig.crashReportingOptedIn;



BOOL crashReplay = privacyConfig.crashReplayOptedIn;
```

## Именование пользовательских действий

Чтобы сформировать имена пользовательских действий, OneAgent захватывает заголовок элемента управления из `UIButton`, проверяя следующие APIы или поля в указанном порядке и останавливаясь, как только получает валидный текст:

1. `titleLabel.attributedText`
2. `attributedTitleForState:UIControlStateNormal`
3. `accessibilityLabel`

Если ни один из них не даёт пригодного для использования текста, OneAgent устанавливает заголовок элемента управления в значение по умолчанию `Button`.

Для ячеек поведение похожее: используется эвристика для определения наиболее заметной метки в ячейке, и OneAgent использует этот текст в имени пользовательского действия.

## Использование пользовательских заголовков элементов управления

Захваченные заголовки элементов управления можно переопределить для `UIControl`, `UITableViewCell` и `UICollectionViewCell`. Это позволяет менять заголовки элементов управления или скрывать их из соображений конфиденциальности.

Если передать пустую строку, OneAgent использует тип элемента управления в имени пользовательского действия, например, `Touch on Button`. Передача `nil` сбрасывает заголовок элемента управления на значение по умолчанию.

Swift

Objective-C

```
var button: UIButton



button.dtxCustomControlName("Custom button title")



var tableCell: UITableViewCell



tableCell.dtxCustomCellName("Custom table cell title")



var collectionCell: UICollectionViewCell



collectionCell.dtxCustomCellName("Custom collection cell title")
```

```
UIButton *button;



[button dtxCustomControlName:@"Custom button title"];



UIButton *tableCell;



[tableCell dtxCustomCellName:@"Custom table cell title"];



UIButton *collectionCell;



[collectionCell dtxCustomCellName:@"Custom collection cell title"];
```

Если нужно убрать заголовки элементов управления во всех пользовательских действиях сразу, см. [Маскирование пользовательских действий](#mask-user-actions).

## Изменение автоматически сгенерированных действий

OneAgent для iOS создаёт пользовательские действия на основе взаимодействий пользователей приложения. Эти действия отличаются от [пользовательских действий](#create-custom-user-action) и иногда называются *автоматически сгенерированными действиями*. Мы также называем их *пользовательскими действиями*.

С помощью SDK OneAgent для iOS можно изменять или даже отменять эти автоматически сгенерированные действия.

Если нужно избежать захвата персональной информации сразу для всех пользовательских действий, см. [Маскирование пользовательских действий](#mask-user-actions).

### Изменение конкретного пользовательского действия

OneAgent для iOS версии 8.215+

С помощью `Dynatrace.modifyUserAction` можно изменить текущее пользовательское действие. Можно изменить имя пользовательского действия и сообщить о событиях, значениях и ошибках. Также можно отменить пользовательское действие.

Разрешённые операции над возвращённым объектом пользовательского действия следующие:

* `getName`
* `setName`
* `reportEvent`
* `reportValue`
* `reportError`
* OneAgent для iOS версии 8.241+ `cancelAction` / `cancel`

Пользовательское действие можно изменить только пока оно ещё открыто. Если пользовательское действие истекает по таймауту до того, как его изменили, изменение не имеет эффекта. Вызов `leave` для этого объекта также не имеет эффекта.

Swift

Objective-C

```
@IBAction func buttonTouchUp(_ sender: Any) {



//for example, handle button touch, get values that should be put into user action name



//fetch current autogenerated action and modify it



Dynatrace.modifyUserAction( { (action) -> () in



let oldName = action?.getName()



action?.setName("This is a renamed auto user action (was '\(oldName)')")



action?.reportValue(withName: "The Answer to the Ultimate Question of Life, the Universe, and Everything", intValue: 42)



action?.reportValue(withName: "G-force", doubleValue: 9.81)



action?.reportValue(withName: "Palindrome", stringValue: "Was it a car or a cat I saw?")



action?.reportError(withName: "Some error", errorValue: -1)



//other reportError also possible, skipping in this example



})



}
```

```
- (IBAction)buttontouchUp:(UIButton *)sender {



//for example, handle button touch, get values that should be put into user action name



//fetch current autogenerated action and modify it



[Dynatrace modifyUserAction:^(DTXAction * _Nullable modifiableAction) {



NSString* oldName = [modifiableAction getName];



[modifiableAction setName:[NSString stringWithFormat: @"This is a renamed auto user action (was '%@')", oldName]];



[modifiableAction reportValueWithName: @"The Answer to the Ultimate Question of Life, the Universe, and Everything" intValue: 42];



[modifiableAction reportValueWithName: @"G-force" doubleValue: 9.81];



[modifiableAction reportValueWithName: @"Palindrome" stringValue: @"Was it a car or a cat I saw?"];



[modifiableAction reportErrorWithName: @"Some error" errorValue: -1];



//other reportError also possible, skipping in this example



}];



}
```

Для мобильного пользовательского действия или мобильного автоматически сгенерированного пользовательского действия максимальная длина имени составляет 250 символов.

### Изменение любого пользовательского действия

OneAgent для iOS версии 8.241+

Автоматически сгенерированные пользовательские действия можно изменять через [`Dynatrace.modifyUserAction`](#modify-specific-auto-action). Однако это доступно только для конкретного пользовательского действия, и обычно нужно знать, открыто ли это пользовательское действие ещё или нет.

Чтобы преодолеть эти ограничения, добавлена функция, позволяющая получать callback для каждого вновь созданного пользовательского действия. При таком подходе приходит уведомление о каждом новом автоматически сгенерированном пользовательском действии, что даёт возможность обновить имя пользовательского действия, а также сообщить события, значения и ошибки. Также можно отменить пользовательское действие.

Можно зарегистрировать callback, который вызывается для каждого автоматически сгенерированного пользовательского действия. Callback можно установить в любом месте приложения в любой момент времени.

Любой ранее зарегистрированный callback перезаписывается последующим вызовом метода API.

Допустимые операции:

* `getName`
* `setName`
* `reportEvent`
* `reportValue`
* `reportError`
* `cancelAction` / `cancel`

Swift

Objective-C

```
Dynatrace.setAutoUserActionCreationCallback { modifiableAction in



guard let modifiableAction = modifiableAction else {



return



}



if modifiableAction.getName().starts(with: "Loading") {



modifiableAction.cancel()



} else {



modifiableAction.setName("Modified Action: " + modifiableAction.getName())



}



}
```

```
[Dynatrace setAutoUserActionCreationCallback:^(DTXAction * _Nullable modifiableAction) {



if (!modifiableAction) {



return;



}



if ([[modifiableAction getName] hasPrefix:@"Loading"]) {



[modifiableAction cancelAction];



} else {



[modifiableAction setName:[NSString stringWithFormat:@"Modified Action: %@", [modifiableAction getName]]];



}



}];
```

Для мобильного пользовательского действия custom action или мобильного автоматически сгенерированного пользовательского действия максимальная длина имени составляет 250 символов.

## Маскирование пользовательских действий

OneAgent для iOS версии 8.249+

По умолчанию имена пользовательских действий [формируются на основе заголовков элементов UI](#user-action-naming), например заголовков кнопок или ячеек таблицы. В редких случаях в имена пользовательских действий могут непреднамеренно попасть адреса электронной почты, имена пользователей или другая личная информация. Это происходит, когда такая информация включена в параметры, используемые для заголовков элементов управления, в результате чего получаются имена пользовательских действий вида `Touch on Account 123456`.

Если такая личная информация появляется в именах пользовательских действий приложения, нужно включить маскирование пользовательских действий. OneAgent заменит все имена действий вида `Touch on <control title>` на тип элемента управления, которого коснулся пользователь, например:

* `Touch on Account 123456` > `Touch on Button`
* `Touch on Transfer all amount` > `Touch on Switch`
* `Touch on Country` > `Touch on TableCell`

Чтобы включить маскирование пользовательских действий, нужно установить [ключ конфигурации `DTXUIActionNamePrivacy`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") в значение `true` в файле [`Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") приложения.

```
<key>DTXUIActionNamePrivacy</key>



<true/>
```

Маскирование пользовательских действий не изменяет [пользовательские заголовки элементов управления](#custom-control-names).

Если нужно изменить имена только для определённых элементов управления или определённых пользовательских действий, можно использовать одну из следующих настроек:

* [Использовать пользовательские заголовки элементов управления](#custom-control-names), чтобы переопределить заголовки элементов UI, захватываемые по умолчанию
* [Изменить автоматически сгенерированные действия](#modify-auto-actions), чтобы изменить имена пользовательских действий
* Настроить правила именования (настройки мобильного приложения > **Naming rules**) для настройки правил именования пользовательских действий или правил извлечения