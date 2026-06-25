---
title: OneAgent SDK for iOS
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios
scraped: 2026-05-12T11:22:03.391840
---

# OneAgent SDK for iOS

# OneAgent SDK for iOS

* How-to guide
* 23-min read
* Updated on Mar 24, 2026

Используйте OneAgent SDK for iOS для передачи дополнительных сведений о пользовательских сессиях в вашем мобильном приложении. OneAgent SDK for iOS позволяет создавать пользовательские действия, измерять веб-запросы, сообщать об ошибках и помечать конкретных пользователей. В разделах ниже описано, как включить эти возможности.

Для iOS OneAgent SDK доступен автоматически после добавления Dynatrace CocoaPod в ваш проект. OneAgent SDK for iOS можно использовать в Swift и Objective-C.

## Запуск OneAgent

OneAgent for iOS можно запустить только один раз. Многократный запуск в рамках одного приложения не поддерживается.

Чтобы отключить [автоматический запуск OneAgent](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#automatic-startup "Изучите список функций, доступных после инструментирования приложения с помощью OneAgent."), установите [конфигурационный ключ `DTXAutoStart`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в значение `false` в файле [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") вашего приложения:

```
<key>DTXAutoStart</key>



<false/>
```

После этого можно запустить OneAgent вручную: с помощью конфигурации из `Info.plist` или передав словарь конфигурации.

Рекомендуется запускать OneAgent как можно раньше, например в `applicationWillFinishLaunching`.

### Запуск OneAgent с конфигурацией из `Info.plist`

Если вы хотите запустить OneAgent с конфигурацией из файла `Info.plist`, используйте вызов API `startupWithInfoPlistSettings`.

OneAgent for iOS запускается только при вызове из главного потока.

Swift

Objective-C

```
Dynatrace.startupWithInfoPlistSettings()
```

```
[Dynatrace startupWithInfoPlistSettings];
```

### Запуск OneAgent с передаваемым словарём конфигурации

Если вы хотите запустить OneAgent с передаваемым словарём конфигурации, используйте вызов API `startupWithConfig`. [Конфигурационные ключи](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") для словаря те же, что и для файла `Info.plist`. Их также можно найти в заголовочном файле `Dynatrace.h`, поставляемом с OneAgent.

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

[Конфигурационные ключи](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#general "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") `DTXApplicationID` и `DTXBeaconURL` обязательны всегда.

Могут потребоваться и другие параметры. Проверьте в [мастере инструментирования](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios#instrumentation-wizard "Настройка мониторинга пользовательского опыта для iOS-приложений в Dynatrace.") Dynatrace, какие параметры и значения нужно передать.

## Создание пользовательских действий

Вы можете определять и передавать пользовательские действия. После запуска [добавьте к ним дополнительную информацию](#custom-action-additional-info), а затем закройте их.

Если нужно изменить автоматически сгенерированное пользовательское действие, см. раздел [Изменение и отмена автоматически сгенерированных действий](#modify-auto-actions).

Если для вашего приложения включён [пользовательский режим согласия (opt-in)](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для соответствия требованиям регулирования в вашем регионе."), он может влиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, которые не передаются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте настройки конфиденциальности Dynatrace для соответствия требованиям регулирования в вашем регионе.").

### Запуск и закрытие пользовательских действий

В приведённом ниже примере кода показано, как запустить и закрыть пользовательское действие. Обратите внимание: если пользовательское действие не закрыто, OneAgent удаляет все связанные с ним данные мониторинга. Время измеряется автоматически.

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

Максимальная длина имени для пользовательского или автоматически сгенерированного мобильного действия составляет 250 символов.

Максимальная длительность мобильного пользовательского действия составляет 9 минут.

Если пользовательское действие выполняется дольше 9 минут и не закрыто, оно удаляется и не передаётся в Dynatrace.

С пользовательским действием можно выполнять следующие операции мониторинга:

* [Создать дочернее действие](#create-child-action)
* [Сообщить о событии](#report-event)
* [Сообщить о значении](#report-value)
* [Сообщить об ошибке](#report-error)
* [Прикрепить веб-запрос](#measure-web-requests)
* [Отменить действие](#cancel-action)

### Создание дочерних действий

[Дочерние действия](/managed/observe/digital-experience/rum-concepts/user-actions#child-actions "Узнайте, что такое пользовательские действия и как они помогают понять поведение пользователей.") аналогичны родительским. При закрытии родительского действия OneAgent автоматически закрывает все его дочерние действия.

В приведённом ниже примере кода показано, как запустить действие в качестве дочернего для другого действия.

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

Максимальная длина имени для пользовательского или автоматически сгенерированного мобильного действия составляет 250 символов.

Количество дочерних действий, прикреплённых к родительскому, не ограничено. Однако допускается не более девяти уровней вложенности: одно родительское действие и девять уровней дочерних (дочернее действие A добавляется к родительскому, дочернее B к A, дочернее C к B и т.д.). Также см. раздел [Структура пользовательских сессий](/managed/observe/digital-experience/rum-concepts/user-session#session-structure-dep-on-app-type "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается, как рассчитывается её длительность и многое другое.").

Дочерние действия не отображаются на [странице сведений о пользовательской сессии](/managed/observe/digital-experience/session-segmentation/new-user-sessions#session-details-page "Узнайте об атрибутах сегментации и фильтрации пользовательских сессий."), но их можно просматривать на [странице анализа водопада](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Узнайте, как анализировать данные мониторинга пользовательских действий с помощью анализа водопада.") для родительского действия. Несмотря на то что полная вложенность не сохраняется в представлении анализа водопада и все дочерние действия отображаются как дочерние первого уровня, иерархию можно понять из временных меток.

### Пример пользовательского действия

В следующем примере кода показан образец ручного инструментирования.

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

OneAgent for iOS версии 8.229+

Можно отменить [пользовательское действие](#create-custom-user-action) или [автоматически сгенерированное пользовательское действие](#modify-auto-actions). Отмена действия удаляет все связанные с ним данные: все переданные значения и все дочерние действия отменяются.

Нельзя отменить закрытое действие, поэтому вызов `cancel`/`cancelAction` после `leave`/`leaveAction` для одного и того же действия невозможен. То же справедливо в обратную сторону: нельзя вызвать `leave`/`leaveAction` после `cancel`/`cancelAction` для одного и того же действия.

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

С помощью `reportEvent` можно сообщить о конкретном событии. Событие должно принадлежать существующему [пользовательскому действию](#create-custom-user-action) или [автоматически сгенерированному пользовательскому действию](#modify-auto-actions). Переданные события отображаются в анализе водопада пользовательских действий.

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

Если для вашего приложения включён [пользовательский режим согласия (opt-in)](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для соответствия требованиям регулирования в вашем регионе."), он может влиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, которые не передаются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте настройки конфиденциальности Dynatrace для соответствия требованиям регулирования в вашем регионе.").

## Передача ошибки

С помощью `reportError` можно сообщить о конкретном событии как об [ошибке](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Узнайте о пользовательских событиях и ошибках, а также их типах, фиксируемых Dynatrace.").

Ошибку можно сообщить двумя способами:

* В рамках действия (либо [пользовательского](#create-custom-user-action), либо [автоматически сгенерированного](#modify-auto-actions))
* Как автономную ошибку: она создаётся как глобальное событие, не привязанное к конкретному действию

Переданные ошибки (как автономные, так и привязанные к действию) отображаются на странице сведений о пользовательской сессии и на многомерной странице **User action analysis**. Ошибки, привязанные к пользовательскому действию, также отображаются в анализе водопада.

Ошибку можно сообщить с кодом ошибки, исключением или `NSError`.

Swift

Objective-C

Автономная ошибка (не привязана к конкретному пользовательскому действию)

```
DTXAction.reportError(withName: "My custom error", error: NSError(domain: "Global issue", code: 007, userInfo: nil))
```

Ошибка, привязанная к конкретному пользовательскому действию

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

Если для вашего приложения включён [пользовательский режим согласия (opt-in)](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для соответствия требованиям регулирования в вашем регионе."), он может влиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, которые не передаются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте настройки конфиденциальности Dynatrace для соответствия требованиям регулирования в вашем регионе.").

## Передача значения

Метод `reportValue` позволяет передавать пары ключ-значение метаданных, которые затем можно просматривать в веб-интерфейсе Dynatrace и преобразовывать в [свойства пользовательских действий и сессий](/managed/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "Свойства пользовательских действий и сессий (пары ключ-значение метаданных) обеспечивают расширенную видимость и более глубокий анализ опыта конечных пользователей."). Передаваемые значения должны быть частью пользовательского действия.

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

Чтобы просмотреть переданные значения в веб-интерфейсе Dynatrace, перейдите к сведениям о пользовательском действии, которое должно содержать эти метаданные, и прокрутите вниз до раздела **Reported values**.

![Страница сведений о пользовательском действии с переданными через SDK значениями](https://dt-cdn.net/images/user-action-details-with-reported-values-2048-b44e8bca3e.png)

Страница сведений о пользовательском действии с переданными через SDK значениями

Чтобы добавить свойства действий и сессий на основе переданных значений и использовать их для создания запросов, сегментации и агрегирования, см. раздел [Определение свойств пользовательских действий и сессий для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Отправляйте метаданные в Dynatrace и определяйте свойства действий и сессий для отслеживаемых мобильных приложений.").

## Измерение веб-запросов

Для отслеживания веб-запросов OneAgent добавляет HTTP-заголовок `x-dynatrace` с уникальным значением к каждому запросу. Это необходимо для сопоставления данных мониторинга на стороне сервера с соответствующим мобильным веб-запросом. Помимо этого, измеряются временные значения на стороне мобильного устройства.

OneAgent for iOS автоматически измеряет время веб-запросов, выполняемых с помощью `NSURLRequest`, `NSURLConnection`, `NSURLSession`, `NSURLProtocol`, `NSString`, `WKWebView` или `NSData`. Однако в следующих случаях потребуется ручное инструментирование:

* Когда [автоматическое инструментирование веб-запросов отключено](#disable-auto-request-instrumentation)
* Когда запросы сторонних фреймворков не инструментированы
* Когда нужно [сообщить о не-HTTP(S)-запросах](#measure-non-http-requests)

### Выбор типа инструментирования

Для HTTP(S)-запросов нельзя совмещать автоматическое и ручное инструментирование веб-запросов. Однако можно использовать автоматическое инструментирование для HTTP(S)-запросов и ручное для [не-HTTP(S)-запросов](#measure-non-http-requests), таких как WebSocket или gRPC.

В таблице ниже указано, какой тип инструментирования запросов следует использовать в зависимости от типов запросов в вашем приложении, а также показано, нужно ли [отключать автоматическое инструментирование запросов](#disable-auto-request-instrumentation).

| Тип запроса | Тип инструментирования | `DTXInstrumentWebRequestTiming` |
| --- | --- | --- |
| Только HTTP(S) | Вариант А: Авто | `true` |
|  | Вариант Б: Ручное | `false` |
| Только не-HTTP(S) | Ручное | `false` (опционально) |
| HTTP(S) + не-HTTP(S) | Вариант А: Авто для HTTP(S) и ручное для не-HTTP(S) | `true` |
|  | Вариант Б: Ручное | `false` |

### Родительское действие веб-запросов

OneAgent for iOS придерживается заданного порядка для определения родителя события веб-запроса, что влияет на отображение запросов в анализе водопада.

#### Автоматическое инструментирование веб-запросов

* Если на том же потоке, что и веб-запрос, есть активное [пользовательское действие](#create-custom-user-action), оно становится родительским.
* Если активного пользовательского действия нет, но есть активное [автоматически сгенерированное действие](#modify-auto-actions) (например, `Touch on...`), оно становится родительским. Это также распространяется на автоматически сгенерированное действие `Loading ...`.
* Если OneAgent не находит активного действия, событие веб-запроса является корневым событием без родительского действия.

#### Ручное инструментирование веб-запросов

* Если родительское действие не указано (`Dynatrace.getRequestTagValue(for: url)`), порядок поиска родительского действия такой же, как при автоматическом измерении времени веб-запросов.
* Если родительское действие указано (`childAction?.getTagFor(url)`), оно становится родительским.

В данный момент автономные события веб-запросов корневого уровня нельзя просматривать в разделе [**Session Segmentation**](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Узнайте об атрибутах сегментации и фильтрации пользовательских сессий.").

### Пример: упрощённое ручное инструментирование веб-запросов

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

### Мониторинг не-HTTP(S)-запросов

OneAgent for iOS не поддерживает авто-инструментирование не-HTTP(S)-запросов. Если нужно сообщать о запросах, например WebSocket (начинающихся с `ws://` или `wss://`), воспользуйтесь приведёнными ниже примерами кода.

Если у вас только не-HTTP(S)-запросы, можно [отключить автоматическое инструментирование запросов](#disable-auto-request-instrumentation), но это не обязательно.

Если у вас есть как HTTP(S)-, так и не-HTTP(S)-запросы, и HTTP(S)-запросы инструментированы автоматически, не отключайте автоматическое инструментирование.

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

Возможность указывать количество отправленных и полученных байт (размеры запроса и ответа) при ручном сообщении о веб-запросе доступна начиная с OneAgent for iOS версии 8.285+. Эта дополнительная информация отображается в веб-интерфейсе Dynatrace на следующих страницах:

* На странице сведений о веб-запросах (доступна через раздел [**Top providers**](/managed/observe/digital-experience/mobile-applications/analyze-and-use/analyze-web-requests-mobile#top-providers "Используйте Dynatrace для мониторинга веб-запросов мобильных приложений.")): отображается только размер запроса (отправленные байты)
* На странице **User action analysis** для веб-запросов, привязанных к пользовательским действиям: отображаются как отправленные, так и полученные байты (размеры запроса и ответа)

### Отключение автоматического инструментирования запросов

Чтобы отключить автоматическое инструментирование веб-запросов, установите [конфигурационный ключ `DTXInstrumentWebRequestTiming`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#web-requests "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в значение `false`.

## Тегирование конкретных пользователей

Каждого пользователя мобильного приложения можно пометить уникальным именем. Это позволяет искать и фильтровать конкретные пользовательские сессии, а также анализировать поведение отдельных пользователей с течением времени. Подробнее см. в разделе [Тегирование пользователей](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Узнайте о пользовательских событиях и ошибках и их типах.").

Ниже описано, как вручную пометить отдельного пользователя через Dynatrace API.

Swift

Objective-C

```
Dynatrace.identifyUser("userId")
```

```
[Dynatrace identifyUser:@"userId"];
```

OneAgent for iOS версии 235+ Сессии, разделённые из-за простоя или превышения длительности, повторно помечаются автоматически.

Когда OneAgent завершает помеченную сессию из-за достижения лимита длительности или простоя пользователя, следующая сессия автоматически помечается заново. Повторно предоставлять идентификационную информацию не нужно.

Однако OneAgent не помечает последующую сессию повторно в следующих случаях:

* При явном завершении помеченной пользовательской сессии через [`endVisit`](#end-session)
* При закрытии или принудительной остановке приложения пользователем или мобильной операционной системой
* При завершении текущей пользовательской сессии OneAgent и создании новой сессии после изменения настроек конфиденциальности

О том, когда OneAgent завершает мобильную пользовательскую сессию, см. раздел [Пользовательские сессии — Завершение сессии](/managed/observe/digital-experience/rum-concepts/user-session#user-session-end--mobile-apps "Узнайте, как определяется пользовательская сессия, когда она начинается и заканчивается и как рассчитывается её длительность.").

Если для вашего приложения включён [пользовательский режим согласия (opt-in)](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для соответствия требованиям регулирования в вашем регионе."), он может влиять на тегирование пользователей и передачу пользовательских событий, действий, значений и ошибок. Конкретные типы данных, которые не передаются в Dynatrace, зависят от уровня сбора данных, установленного конкретным пользователем. Подробнее см. в разделе [Уровни сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте настройки конфиденциальности Dynatrace для соответствия требованиям регулирования в вашем регионе.").

## Завершение сессии

Можно принудительно завершить сессию через Dynatrace API. При этом закрываются все открытые действия и начинается новая сессия.

Swift

Objective-C

```
Dynatrace.endVisit()
```

```
[Dynatrace endVisit];
```

## Настройка конфиденциальности данных (режим согласия)

В режиме согласия каждый пользователь вашего приложения может установить предпочтения конфиденциальности данных и решить, хочет ли он делиться своей информацией. Когда режим согласия включён, необходимо запрашивать у каждого пользователя разрешение на сбор данных и сохранять его предпочтения. Подробнее см. в разделе [Пользовательский режим согласия](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для соответствия требованиям регулирования в вашем регионе.").

### Включение пользовательского режима согласия

Чтобы активировать пользовательский режим согласия, добавьте [конфигурационный ключ `DTXUserOptIn`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в файл [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") вашего приложения:

```
<key>DTXUserOptIn</key>



<true/>
```

### Изменение предпочтений конфиденциальности пользователя

Следующие примеры кода показывают, как изменить предпочтения конфиденциальности данных на основе решения конкретного пользователя.

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

Возможные значения [уровня сбора данных](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#data-collection-levels "Используйте настройки конфиденциальности Dynatrace для соответствия требованиям регулирования в вашем регионе."):

| Swift | Objective-C |
| --- | --- |
| `.off` | `DTX_DataCollectionOff` |
| `.performance` | `DTX_DataCollectionPerformance` |
| `.userBehavior` | `DTX_DataCollectionUserBehavior` |

OneAgent сохраняет предпочтения конфиденциальности данных и автоматически применяет их при перезапуске приложения. При каждом изменении пользователем уровня сбора данных OneAgent создаёт новую сессию с новыми настройками. Убедитесь, что вы не оборачиваете этот метод API в пользовательское действие, иначе OneAgent не сможет прикрепить пользовательское действие к правильной сессии.

### Получение предпочтений конфиденциальности пользователя

Те же свойства можно использовать для получения предпочтений конфиденциальности конкретного пользователя.

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

Для формирования имён пользовательских действий OneAgent извлекает заголовок элемента управления из `UIButton`, оценивая следующий порядок API и полей и останавливаясь, как только получает допустимый текст:

1. `titleLabel.attributedText`
2. `attributedTitleForState:UIControlStateNormal`
3. `accessibilityLabel`

Если ни один из них не возвращает подходящий текст, OneAgent использует значение по умолчанию `Button` в качестве заголовка элемента управления.

Для ячеек поведение аналогично: эвристика определяет наиболее заметный заголовок в ячейке, и OneAgent использует этот текст в имени пользовательского действия.

## Использование пользовательских заголовков элементов управления

Можно переопределить захваченные заголовки для `UIControl`, `UITableViewCell` и `UICollectionViewCell`. Это позволяет изменять заголовки или скрывать их по соображениям конфиденциальности.

Если передать пустую строку, OneAgent использует тип элемента управления в имени пользовательского действия, например `Touch on Button`. Передача `nil` сбрасывает заголовок к значению по умолчанию.

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

Если нужно убрать заголовки элементов управления во всех пользовательских действиях сразу, см. раздел [Маскировка пользовательских действий](#mask-user-actions).

## Изменение автоматически сгенерированных действий

OneAgent for iOS создаёт пользовательские действия на основе взаимодействий пользователей с приложением. Эти действия отличаются от [пользовательских действий](#create-custom-user-action) и иногда называются *автоматически сгенерированными действиями* или просто *пользовательскими действиями*.

С помощью OneAgent SDK for iOS можно изменять или отменять эти автоматически сгенерированные действия.

Если нужно избежать захвата персональных данных для всех пользовательских действий сразу, см. раздел [Маскировка пользовательских действий](#mask-user-actions).

### Изменение конкретного пользовательского действия

OneAgent for iOS версии 8.215+

С помощью `Dynatrace.modifyUserAction` можно изменить текущее пользовательское действие: изменить имя, сообщать о событиях, значениях и ошибках, а также отменить пользовательское действие.

Допустимые операции над возвращаемым объектом пользовательского действия:

* `getName`
* `setName`
* `reportEvent`
* `reportValue`
* `reportError`
* OneAgent for iOS версии 8.241+ `cancelAction` / `cancel`

Пользовательское действие можно изменить только пока оно ещё открыто. Если пользовательское действие завершается по тайм-ауту до его изменения, изменение не применяется. Вызов `leave` для этого объекта также не имеет эффекта.

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

Максимальная длина имени для пользовательского или автоматически сгенерированного мобильного действия составляет 250 символов.

### Изменение любого пользовательского действия

OneAgent for iOS версии 8.241+

Автоматически сгенерированные пользовательские действия можно изменять через [`Dynatrace.modifyUserAction`](#modify-specific-auto-action). Однако это применяется только к конкретному пользовательскому действию, и, как правило, нужно знать, открыто ли оно в данный момент.

Для преодоления этих ограничений введена возможность получать обратный вызов для каждого вновь созданного пользовательского действия. При таком подходе вы получаете уведомление о каждом новом автоматически сгенерированном пользовательском действии и можете обновить его имя, а также сообщить о событиях, значениях и ошибках. Пользовательское действие также можно отменить.

Можно зарегистрировать обратный вызов, который будет вызываться для каждого автоматически сгенерированного пользовательского действия. Задать обратный вызов можно в любом месте приложения в любое время.

Каждый последующий вызов метода API перезаписывает ранее зарегистрированный обратный вызов.

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

Максимальная длина имени для пользовательского или автоматически сгенерированного мобильного действия составляет 250 символов.

## Маскировка пользовательских действий

OneAgent for iOS версии 8.249+

По умолчанию имена пользовательских действий [формируются из заголовков элементов UI](#user-action-naming), например заголовков кнопок или ячеек таблицы. В редких случаях в имена пользовательских действий могут непреднамеренно попасть адреса электронной почты, имена пользователей или другие персональные данные. Это происходит, когда такая информация входит в параметры, используемые для заголовков элементов управления, что приводит к именам типа `Touch on Account 123456`.

Если такие персональные данные присутствуют в именах пользовательских действий вашего приложения, включите маскировку пользовательских действий. OneAgent заменит все имена действий вида `Touch on <заголовок элемента>` на тип элемента управления, которого коснулся пользователь, например:

* `Touch on Account 123456` → `Touch on Button`
* `Touch on Transfer all amount` → `Touch on Switch`
* `Touch on Country` → `Touch on TableCell`

Чтобы включить маскировку пользовательских действий, установите [конфигурационный ключ `DTXUIActionNamePrivacy`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#user-actions "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.") в значение `true` в файле [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") вашего приложения.

```
<key>DTXUIActionNamePrivacy</key>



<true/>
```

Маскировка пользовательских действий не изменяет [пользовательские заголовки элементов управления](#custom-control-names).

Если нужно изменить имена только для определённых элементов управления или действий, используйте одну из следующих настроек:

* [Используйте пользовательские заголовки элементов управления](#custom-control-names), чтобы переопределить заголовки UI-элементов, захваченные по умолчанию
* [Изменяйте автоматически сгенерированные действия](#modify-auto-actions) для изменения имён пользовательских действий
* Настройте правила именования (настройки мобильного приложения > **Naming rules**) для настройки правил именования или извлечения пользовательских действий