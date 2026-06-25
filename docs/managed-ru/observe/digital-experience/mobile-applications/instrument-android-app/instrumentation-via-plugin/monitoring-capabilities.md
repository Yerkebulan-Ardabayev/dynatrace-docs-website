---
title: Настройка возможностей мониторинга Dynatrace Android Gradle plugin
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities
scraped: 2026-05-12T11:32:36.948646
---

# Настройка возможностей мониторинга Dynatrace Android Gradle plugin

# Настройка возможностей мониторинга Dynatrace Android Gradle plugin

* How-to guide
* 25-min read
* Updated on Mar 05, 2026

Следующие параметры конфигурации позволяют настраивать возможности мониторинга OneAgent и тонко настраивать процесс авто-инструментирования для этих функций.

## Мониторинг пользовательских действий

OneAgent создаёт пользовательские действия на основе компонентов UI, которые инициируют эти действия, и автоматически объединяет данные пользовательских действий с другими данными мониторинга, например с информацией о веб-запросах и сбоях. OneAgent продлевает время жизни пользовательских действий, чтобы правильно агрегировать их с другими событиями, выполняемыми в фоновом потоке или сразу после пользовательского действия.

### Настройка мониторинга пользовательских действий

Мониторинг пользовательских действий можно настроить с помощью следующих свойств:

* [`timeout`](#timeout-and-max-duration-properties)
* [`maxDuration`](#timeout-and-max-duration-properties)
* [`emptyActions`](#empty-actions-property)
* [`enabled`](#disable-user-action-monitoring)
* [`sensors`](#action-monitoring-sensors)
* [`namePrivacy`](#mask-user-actions)
* [`composeEnabled`](#compose-enable)

Все свойства, связанные с мониторингом пользовательских действий, являются частью [UserAction DSL](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html), поэтому настраивайте их через [блок `userActions`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:userActions(org.gradle.api.Action)).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



userActions {



// your user action monitoring configuration



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



userActions {



// your user action monitoring configuration



}



}



}



}
```

#### Свойства `timeout` и `maxDuration`

С помощью свойства [`timeout`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:timeout) можно настроить время, в течение которого OneAgent может добавлять другие события к вновь созданному пользовательскому действию. При обнаружении другого пользовательского взаимодействия OneAgent прекращает добавлять события к пользовательскому действию предыдущего взаимодействия независимо от настроенного значения `timeout`. Вместо этого OneAgent добавляет события только к пользовательскому действию текущего взаимодействия.

По истечении периода `timeout` OneAgent проверяет наличие открытых событий и ждёт их завершения. С помощью свойства [`maxDuration`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:maxDuration) можно настроить максимальную продолжительность таких пользовательских действий. Если открытое событие, например веб-запрос, не завершилось по истечении этого периода, OneAgent удаляет такие события из пользовательского действия и закрывает его с соответствующим значением времени окончания.

Укажите значение для обоих свойств в миллисекундах. Значение свойства `maxDuration` должно быть равно значению свойства `timeout` или превышать его.

| Свойство | Значение по умолчанию | Возможные значения |
| --- | --- | --- |
| `timeout` | `500` | `100` — `5000` |
| `maxDuration` | `60000` | `100` — `540000` |

Для свойств `timeout` и `maxDuration` можно задать только одно значение каждое, и оно должно подходить для всех пользовательских действий на всех устройствах.

#### Свойство `emptyActions`

OneAgent также сообщает о пользовательских действиях, не содержащих дочерних событий. Чтобы отклонять такие пользовательские действия, используйте свойство [`emptyActions`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:emptyActions).

### Отключение мониторинга пользовательских действий

Мониторинг пользовательских действий можно полностью деактивировать с помощью свойства [`enabled`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:enabled). В этом случае все остальные свойства игнорируются, поэтому указывайте только свойство `enabled`, чтобы избежать путаницы.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



userActions.enabled false



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



userActions.enabled(false)



}



}



}
```

### Сенсоры мониторинга пользовательских действий

Plugin автоматически инструментирует следующие классы и методы:

| Библиотека/фреймворк | Инструментированные классы/методы | Сенсор |
| --- | --- | --- |
| Android | `android.view.View$OnClickListener` | `click` |
| Android | `android.widget.AdapterView$OnItemClickListener` | `itemClick` |
| Android | `android.widget.AdapterView$OnItemSelectedListener` | `itemSelect` |
| Android | `android.app.Activity.onOptionsItemSelected` | `optionSelect` |
| Android | `android.view.MenuItem$OnMenuItemClickListener` | `menuClick` |
| AndroidX | `androidx.viewpager.widget.ViewPager$OnPageChangeListener` | `pageChange` |
| AndroidX | `androidx.swiperefreshlayout.widget.SwipeRefreshLayout$OnRefreshListener` | `refresh` |
| Android Support | `android.support.v4.view.ViewPager$OnPageChangeListener` | `pageChange` |
| Android Support | `android.support.v4.widget.SwipeRefreshLayout$OnRefreshListener` | `refresh` |
| [Jetpack Compose](#compose-instrumentation) | `Modifier.clickable` | `composeClickable` |
| Jetpack Compose | `Modifier.combinedClickable` | `composeClickable` |
| Jetpack Compose | `Modifier.toggleable` | `composeClickable` |
| Jetpack Compose | `Modifier.swipeable` | `composeSwipeable` |
| Jetpack Compose | `Modifier.pullRefresh` | `composePullRefresh` |
| Jetpack Compose | `Slider` `RangeSlider` | `composeSlider` |
| Jetpack Compose | `HorizontalPager` `VerticalPager` | `composePager` |
| Jetpack Compose | Отвечает за предоставление семантической информации для пользовательских действий. Этот сенсор не обнаруживает пользовательский ввод. | `composeSemantics` |

Можно деактивировать отдельные сенсоры через свойства [UserAction Sensor DSL](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionSensors.html) и настроить их внутри [блока `sensors`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:sensors(org.gradle.api.Action)).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



userActions {



sensors {



// fine-tune the sensors if necessary



pageChange false



refresh false



}



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



userActions {



sensors {



// fine-tune the sensors if necessary



pageChange(false)



refresh(false)



}



}



}



}



}
```

### Именование пользовательских действий

Для формирования имён пользовательских действий OneAgent захватывает заголовок элемента управления из различных атрибутов в зависимости от используемого listener'а или метода. Подробности см. в таблице ниже.

| Listener, метод или компонент | Вычисляемый атрибут/свойство |
| --- | --- |
| `android.view.View$OnClickListener` `android.widget.AdapterView$OnItemClickListener` `android.widget.AdapterView$OnItemSelectedListener` | Атрибуты вычисляются в следующем порядке: 1. Атрибут [`android:contentDescription`](https://developer.android.com/reference/android/view/View.html#attr_android:contentDescription) 2. Атрибут [`android:text`](https://developer.android.com/reference/android/widget/TextView#attr_android:text) для компонентов на основе `TextView` 3. Имя класса |
| `android.app.Activity.onOptionsItemSelected` `android.view.MenuItem$OnMenuItemClickListener` | [`getTitle`](https://developer.android.com/reference/android/view/MenuItem#getTitle()) для пунктов меню |
| `androidx.viewpager.widget.ViewPager$OnPageChangeListener` `androidx.swiperefreshlayout.widget.SwipeRefreshLayout$OnRefreshListener` `android.support.v4.view.ViewPager$OnPageChangeListener` `android.support.v4.widget.SwipeRefreshLayout$OnRefreshListener` | В качестве имени действия используется тип действия, так как компонент UI недоступен |
| [Компоненты Jetpack Compose UI](#compose-instrumentation) | Свойства вычисляются в следующем порядке: 1. `SemanticsPropertyReceiver.dtActionName` 2. [`SemanticsPropertyReceiver.contentDescription`](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/SemanticsPropertyReceiver#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).contentDescription()) 3. [`SemanticsPropertyReceiver.text`](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/SemanticsPropertyReceiver#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).text()) 4. Имя класса |

### Маскировка пользовательских действий

Dynatrace Android Gradle plugin версии 8.249+

По умолчанию имена пользовательских действий [формируются на основе заголовков элементов управления UI](#user-action-naming), например заголовков кнопок или пунктов меню. В редких случаях адреса электронной почты, имена пользователей или другая персональная информация могут непреднамеренно попасть в имена пользовательских действий. Это происходит, когда такая информация включается в параметры, используемые для заголовков элементов управления, и приводит к именам пользовательских действий типа `Touch on Account 123456`.

Если подобная персональная информация присутствует в именах пользовательских действий вашего приложения, включите маскировку пользовательских действий. OneAgent заменит все имена действий вида `Touch on <control title>` именем класса элемента управления, которого коснулся пользователь. Например:

* `Touch on Account 123456` → `Touch on Button`
* `Touch on Transfer all amount` → `Touch on Switch`
* `Touch on Account settings` → `Touch on ActionMenuItem`

Маскировку пользовательских действий можно включить с помощью свойства [`namePrivacy`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:namePrivacy) в [UserAction DSL](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



userActions {



namePrivacy true



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



userActions {



namePrivacy(true)



}



}



}



}
```

При включении свойства `namePrivacy` маскировка также применяется к пользовательским действиям для компонентов [Jetpack Compose](#compose-instrumentation) UI, и некоторые [метаданные компонентов](#compose-captured-metadata-by-component) не будут захвачены.

Если нужно изменить имена только для определённых пользовательских действий, используйте один из следующих вариантов:

* [Изменение автоматически создаваемых действий](#modify-auto-actions) для изменения имён пользовательских действий
* Задание правил именования (настройки мобильного приложения > **Naming rules**) для настройки правил именования или извлечения пользовательских действий

### Изменение пользовательских действий

OneAgent for Android создаёт пользовательские действия на основе взаимодействий пользователей вашего приложения. Эти действия отличаются от [пользовательских действий](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#create-custom-actions "Узнайте, как расширить мониторинг мобильного пользовательского опыта на Android с помощью OneAgent SDK.") и иногда называются *автоматически создаваемыми действиями*.

Вы можете изменять или даже отменять пользовательские действия.

Если нужно избежать захвата персональной информации для всех пользовательских действий сразу, см. [Маскировка пользовательских действий](#mask-user-actions).

Для компонентов Jetpack Compose UI доступна дополнительная возможность [задания пользовательского имени действия](#compose-custom-user-action-name).

#### Изменение конкретного пользовательского действия

С помощью [`Dynatrace.modifyUserAction`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#modifyUserAction(com.dynatrace.android.agent.UserActionModifier)) можно изменить текущее пользовательское действие. Можно изменить имя пользовательского действия, сообщать о событиях, значениях и ошибках, а также отменить пользовательское действие.

Метод `Dynatrace.modifyUserAction` принимает реализацию [`UserActionModifier`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/UserActionModifier.html) в качестве параметра, который предоставляет текущий изменяемый объект [`ModifiableUserAction`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/ModifiableUserAction.html).

Допустимые операции с этим объектом пользовательского действия:

* `getActionName`
* `setActionName`
* `reportEvent`
* `reportValue`
* `reportError`
* OneAgent for Android версии 8.241+ `cancel`

Изменить пользовательское действие можно только пока оно остаётся открытым. Если пользовательское действие истечёт по тайм-ауту до его изменения, изменение не вступит в силу. Рекомендуется вызывать `Dynatrace.modifyUserAction` внутри инструментированного [метода listener'а](#user-action-monitoring-sensors) и не вызывать этот метод из другого потока.

В следующем примере используется приложение-калькулятор, чтобы показать, как изменить имя пользовательского действия, созданного для нажатия кнопки, и как сообщить значение для действия.

Java

Kotlin

```
button.setOnClickListener(new View.OnClickListener() {



@Override



public void onClick(View v) {



int result = calc();



// we use Java 8 language features here. You can also use anonymous classes instead of lambdas



Dynatrace.modifyUserAction(userAction -> {



userAction.setActionName("Click on Calculate");



userAction.reportValue("Calculated result", result);



});



showResult(result);



}



});
```

```
button.setOnClickListener {



val result = calc()



Dynatrace.modifyUserAction { userAction ->



userAction.actionName = "Click on Calculate"



userAction.reportValue("Calculated result", result)



}



showResult(result)



}
```

Максимальная длина имени для мобильного пользовательского или автоматически создаваемого действия составляет 250 символов.

#### Изменение любого пользовательского действия

OneAgent for Android версии 8.241+

Вы можете изменять пользовательские действия через [`Dynatrace.modifyUserAction`](#modify-specific-auto-action). Однако это возможно только для конкретного пользовательского действия, и вам обычно нужно знать, открыто ли оно ещё.

Для преодоления этих ограничений была введена функция, позволяющая получать обратный вызов для каждого нового пользовательского действия. При таком подходе вы получаете уведомление о каждом новом автоматически создаваемом пользовательском действии и можете обновить имя действия, а также сообщить о событиях, значениях и ошибках. Пользовательское действие также можно отменить.

Можно зарегистрировать обратный вызов, который вызывается для каждого пользовательского действия. [`UserActionModifier`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/UserActionModifier.html) задаётся один раз при запуске OneAgent через метод [`DynatraceConfigurationBuilder#withAutoUserActionModifier`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withAutoUserActionModifier(com.dynatrace.android.agent.UserActionModifier)). После этого он вызывается каждый раз, когда OneAgent создаёт пользовательское действие. Для [пользовательских действий](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#create-custom-actions "Узнайте, как расширить мониторинг мобильного пользовательского опыта на Android с помощью OneAgent SDK.") он не вызывается.

Зарегистрировать обратный вызов можно только при запуске OneAgent, поэтому необходимо [запускать OneAgent вручную](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#start-oneagent "Узнайте, как расширить мониторинг мобильного пользовательского опыта на Android с помощью OneAgent SDK.").

Допустимые операции:

* `getActionName`
* `setName`
* `reportEvent`
* `reportValue`
* `reportError`
* `cancel`

Java

Kotlin

```
Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



.withAutoUserActionModifier(modifiableAction -> {



if (modifiableAction.getActionName().contains("account ID")) {



// remove personal information from the user action name



modifiableAction.setActionName("Touch on Account");



}



})



.buildConfiguration());
```

```
Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconUrl>")



.withAutoUserActionModifier { modifiableAction: ModifiableUserAction ->



if (modifiableAction.actionName.contains("account ID")) {



// remove personal information from the user action name



modifiableAction.actionName = "Touch on Account"



}



}



.buildConfiguration())
```

Максимальная длина имени для мобильного пользовательского или автоматически создаваемого действия составляет 250 символов.

### Библиотека Android data binding

Dynatrace Android Gradle plugin может инструментировать логику событий и listener'ы, определённые с помощью функции [data binding](https://developer.android.com/topic/libraries/data-binding). Если ваше приложение содержит код, аналогичный [официальному примеру listener binding](https://developer.android.com/topic/libraries/data-binding/expressions#listener_bindings), plugin может обнаружить правильный байт-код и инструментировать его.

```
<?xml version="1.0" encoding="utf-8"?>



<layout xmlns:android="http://schemas.android.com/apk/res/android">



<data>



<variable name="task" type="com.android.example.Task" />



<variable name="presenter" type="com.android.example.Presenter" />



</data>



<LinearLayout android:layout_width="match_parent" android:layout_height="match_parent">



<Button android:layout_width="wrap_content" android:layout_height="wrap_content"



android:onClick="@{() -> presenter.onSaveClick(task)}" />



</LinearLayout>



</layout>
```

### Определение обработчика событий через атрибут XML

[Следующий пример из документации Android](https://developer.android.com/guide/topics/ui/controls/button#HandlingEvents) показывает, как определить обработчик событий через атрибуты XML.

```
<?xml version="1.0" encoding="utf-8"?>



<Button xmlns:android="http://schemas.android.com/apk/res/android"



android:id="@+id/button_send"



android:layout_width="wrap_content"



android:layout_height="wrap_content"



android:text="@string/button_send"



android:onClick="sendMessage" />
```

Java

Kotlin

```
/** Called when the user touches the button */



public void sendMessage(View view) {



// Do something in response to button click



}
```

```
/** Called when the user touches the button */



fun sendMessage(view: View) {



// Do something in response to button click



}
```

Dynatrace Android Gradle plugin не может определить связь между кнопкой в файле XML макета и методом `sendMessage` в activity. Однако если ваше приложение использует библиотеку Appcompat и ваши activity унаследованы от `androidx.appcompat.app.AppCompatActivity`, plugin автоматически инструментирует логику делегирования библиотеки Appcompat. Если вы не используете библиотеку Appcompat, необходимо вручную инструментировать эти методы обработчиков событий, так как plugin не может определить связь между байт-кодом и файлом XML макета.

## Мониторинг пользовательских действий для Jetpack Compose

Dynatrace Android Gradle plugin версии 8.263+

Dynatrace поддерживает авто-инструментирование компонентов [Jetpack Compose](https://developer.android.com/jetpack/compose) UI. OneAgent создаёт пользовательские действия на основе компонентов UI, которые инициируют эти действия, и автоматически объединяет данные пользовательских действий с другими данными мониторинга, например с информацией о веб-запросах и сбоях.

Авто-инструментирование Jetpack Compose включено по умолчанию начиная с версии Dynatrace Android Gradle plugin 8.271.

Подробнее см. в разделе [Technology support | Mobile app Real User Monitoring](/managed/ingest-from/technology-support#mobile-rum "Найдите технические сведения о поддержке Dynatrace конкретных платформ и фреймворков разработки.").

### Поддерживаемые компоненты UI

Поддерживается авто-инструментирование стандартных и пользовательских компонентов с взаимодействиями пользователей по умолчанию из UI-фреймворка Jetpack Compose. В таблице ниже перечислены эти компоненты и пользовательские взаимодействия, а также ряд компонентов UI, основанных на этих инструментированных взаимодействиях.

| Компоненты и пользовательские взаимодействия | Примеры компонентов |
| --- | --- |
| [Modifier.clickable](https://dt-url.net/compose-modifier-clickable) | Button, IconButton, RadioButton, Chip |
| [Modifier.combinedClickable](https://dt-url.net/compose-modifier-combinedClickable) |  |
| [Modifier.toggleable](https://dt-url.net/compose-modifier-toggleable) | Checkbox, TriStateCheckbox, Switch, IconToggleButton |
| [Modifier.swipeable](https://dt-url.net/compose-modifier-swipeable)[3] | SwipeToDismiss, BottomDrawer |
| [Modifier.pullRefresh](https://developer.android.com/reference/kotlin/androidx/compose/material/pullrefresh/package-summary#(androidx.compose.ui.Modifier).pullRefresh(androidx.compose.material.pullrefresh.PullRefreshState,kotlin.Boolean))[1], [2], [3] |  |
| [Slider](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Slider)[1] [RangeSlider](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#RangeSlider)[1] |  |
| [HorizontalPager](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#HorizontalPager)[1], [3] [VerticalPager](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#VerticalPager)[1], [3] |  |

1

Dynatrace Android Gradle plugin версии 8.267+

2

[Вторая версия `Modifier.pullRefresh`](https://developer.android.com/reference/kotlin/androidx/compose/material/pullrefresh/package-summary#(androidx.compose.ui.Modifier).pullRefresh(kotlin.Function1,kotlin.coroutines.SuspendFunction1,kotlin.Boolean)) не поддерживается.

3

Поддерживаемые версии Jetpack Compose: 1.3-1.5.

### Отключение мониторинга пользовательских действий

Мониторинг пользовательских действий для Jetpack Compose можно отключить с помощью свойства [`composeEnabled`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:composeEnabled) в [UserAction DSL](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html). Обратите внимание, что все остальные свойства сенсоров Jetpack Compose игнорируются при отключении авто-инструментирования Jetpack Compose, поэтому указывайте только свойство `composeEnabled`, чтобы избежать путаницы.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



userActions {



composeEnabled false



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



userActions {



composeEnabled(false)



}



}



}



}
```

### Сенсоры мониторинга пользовательских действий

Для авто-инструментирования Jetpack Compose поддерживаются следующие сенсоры. Подробности см. в [обзорной таблице всех сенсоров](#action-monitoring-sensors).

* `composeClickable`
* `composeSwipeable`
* `composeSemantics`

* `composePullRefresh`[1]
* `composeSlider`[1]
* `composePager`[1]

1

Dynatrace Android Gradle plugin версии 8.267+

Можно [деактивировать отдельные сенсоры](#deactivate-action-monitoring-sensors) через UserAction Sensor DSL.

Рекомендуется не отключать сенсор `composeSemantics`, так как он отвечает за формирование правильных имён пользовательских действий.

При отключении этого сенсора OneAgent использует имя класса инструментированного компонента в имени пользовательского действия. Например, `Touch on Finish your order` может измениться на что-то вроде `Touch on Button with function OrderViewKt$Toolbar$finish$1$2`.

### Именование пользовательских действий

Для формирования имён пользовательских действий компонентов Jetpack Compose UI OneAgent захватывает [семантическую информацию](https://developer.android.com/jetpack/compose/semantics) и вычисляет информацию из [объединённого дерева семантики](https://developer.android.com/jetpack/compose/semantics#merged-vs-unmerged) инструментированного компонента.

Для формирования правильных имён пользовательских действий вычисляются четыре свойства. При наличии нескольких свойств для имени пользовательского действия используется свойство с наивысшим приоритетом.

При наличии нескольких свойств одного типа для имени пользовательского действия используется значение первого свойства. Пустые значения свойств игнорируются.

Упрощённый пример с двумя свойствами одного типа

В приведённом ниже фрагменте кода кнопка содержит два свойства `Text`; значения обоих свойств доступны в объединённом дереве семантики. OneAgent возьмёт первое из них и создаст имя пользовательского действия `Touch on Title`.

```
Button(onClick = { ... }) {



Text("Title")



Text("Body")



}
```

Более сложный пример с двумя свойствами одного типа

В приведённом ниже фрагменте кода компонент содержит два свойства `contentDescription`; значения обоих свойств доступны в объединённом дереве семантики. OneAgent возьмёт первое из них и создаст имя пользовательского действия `Touch on Finish your order` (не `Touch on Finish`).

```
var checked by rememberSaveable { mutableStateOf(false) }



val likeIcon =



if (checked) Icons.Filled.ThumbUp



else Icons.Outlined.ThumbUp



IconToggleButton(



checked = checked,



onCheckedChange = { checked = it },



modifier = Modifier



.clip(CircleShape)



.background(



if (checked) MaterialTheme.colors.primary



else Color.Transparent



)



.semantics {



contentDescription = "Finish your order"



}



) {



Icon(likeIcon, "Like", modifier = Modifier.semantics {



contentDescription = "Finish"



})



}
```

### Задание пользовательского имени действия

Если нужно задать пользовательское имя действия для компонента Jetpack Compose UI, используйте свойство `SemanticsPropertyReceiver.dtActionName`.

```
// This import is required to use our custom semantics property



import com.dynatrace.android.api.compose.dtActionName



Box(



modifier = Modifier



.clickable { ... }



.semantics {



dtActionName = "Finish your order"



}



) {



...



}
```

Для приведённого выше фрагмента кода OneAgent создаст имя пользовательского действия `Touch on Finish your order`.

Свойство `SemanticsPropertyReceiver.dtActionName` является частью [объединённого дерева семантики](https://developer.android.com/jetpack/compose/semantics#merged-vs-unmerged), но игнорируется службами специальных возможностей.

Максимальная длина имени для мобильного пользовательского или автоматически создаваемого действия составляет 250 символов.

Если нужно маскировать персональную информацию в именах пользовательских действий приложения, включите [маскировку пользовательских действий](#mask-user-actions).

### Захваченные метаданные компонентов

При мониторинге мобильного приложения OneAgent for Android также захватывает дополнительные метаданные для инструментированных компонентов Jetpack Compose. Эти метаданные хранятся в виде пар ключ-значение и [доступны в веб-интерфейсе Dynatrace](#compose-view-captured-metadata). Они предоставляют дополнительный контекст для инструментированных компонентов: их расположение в коде, начальное и целевое состояния, типы пользовательских действий и другое.

#### Захваченные параметры и значения по компоненту

Следующие пары ключ-значение сообщаются в зависимости от того, как пользователь взаимодействовал с компонентом Jetpack Compose UI.

Modifier.clickable

| Параметр | Описание | Сообщаемое значение |
| --- | --- | --- |
| `function` | Имя функции для параметра `onClick` |  |
| `role` | Тип элемента пользовательского интерфейса | `null`, если `role` не указан |
| `type` | Тип пользовательского действия | `click` |

Modifier.combinedClickable

| Параметр | Описание | Сообщаемое значение |
| --- | --- | --- |
| `function` | Имя функции для параметра `onClick`, `onLongClick` или `onDoubleClick` |  |
| `role` | Тип элемента пользовательского интерфейса | `null`, если `role` не указан |
| `type` | Тип пользовательского действия | `click` `double click` `long click` |

Modifier.toggleable

| Параметр | Описание | Сообщаемое значение |
| --- | --- | --- |
| `function` | Имя функции для параметра `onValueChange` |  |
| `role` | Тип элемента пользовательского интерфейса | `null`, если `role` не указан |
| `fromState` | Начальное состояние компонента UI. Например, если флажок был установлен и пользователь его снял, в качестве `fromState` сообщается `On`. |  |
| `type` | Тип пользовательского действия | `toggle` |

Modifier.swipeable

| Параметр | Описание | Сообщаемое значение |
| --- | --- | --- |
| `state class` | Класс, являющийся хранителем состояния для компонента UI, например SwipeableState |  |
| `fromState`[1] | Начальное состояние компонента UI. Например, если пользователь провёл свайп из состояния `A` в `B`, в качестве `fromState` сообщается `A`. |  |
| `toState`[1] | Целевое состояние компонента UI. Например, если пользователь провёл свайп из состояния `A` в `B`, в качестве `toState` сообщается `B`. |  |
| `type` | Тип пользовательского действия | `swipe` |

1

Не сообщается, если включена [маскировка пользовательских действий](#mask-user-actions).

Modifier.pullRefresh

| Параметр | Описание | Сообщаемое значение |
| --- | --- | --- |
| `function` | Имя класса для параметра `onRefresh` (метод `rememberPullRefreshState`) |  |
| `type` | Тип пользовательского действия | `pull refresh` |

Slider и RangeSlider

| Параметр | Описание | Сообщаемое значение |
| --- | --- | --- |
| `function` | Имя функции для параметра `onValueChange` |  |
| `toState` для `Slider` | Выбранное значение слайдера, например `150` |  |
| `toState` для `RangeSlider` | Выбранный диапазон слайдера, например `25..150` |  |
| `type` | Тип пользовательского действия | `slide` |

HorizontalPager и VerticalPager

| Параметр | Описание | Сообщаемое значение |
| --- | --- | --- |
| `orientation` | Тип pager'а | `Horizontal` или `Vertical` |
| `fromState` | Начальный индекс страницы. Например, если пользователь листнул фотогалерею с фото `1` на фото `2`, в качестве `fromState` сообщается `1`. |  |
| `toState` | Целевой индекс страницы. Например, если пользователь листнул фотогалерею с фото `1` на фото `2`, в качестве `toState` сообщается `2`. |  |
| `type` | Тип пользовательского действия | `pager` |

#### Просмотр метаданных компонентов в Dynatrace

Метаданные, захваченные для компонентов Jetpack Compose UI, доступны на страницах анализа waterfall пользовательских действий вашего приложения.

Чтобы просмотреть захваченные метаданные для компонента Jetpack Compose:

1. В Dynatrace перейдите в **Session Segmentation**.
2. Найдите и выберите сессию, содержащую нужное пользовательское действие.
3. В разделе **Events and actions** разверните пользовательское действие и выберите **Perform waterfall analysis**.
4. Прокрутите вниз до раздела **Reported values**, чтобы увидеть метаданные, захваченные для компонента Jetpack Compose UI.

## Мониторинг веб-запросов

Dynatrace Android Gradle plugin может автоматически инструментировать и тегировать ваши веб-запросы. Для отслеживания веб-запросов OneAgent добавляет к веб-запросу HTTP-заголовок `x-dynatrace` с уникальным значением. Это необходимо для корреляции данных мониторинга на стороне сервера с соответствующим мобильным веб-запросом.

Для HTTP(S)-запросов нельзя совмещать автоматическое и ручное инструментирование. Однако можно использовать автоматическое инструментирование для HTTP(S)-запросов и [ручное инструментирование для не-HTTP(S)-запросов](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#monitor-non-http-requests "Узнайте, как расширить мониторинг мобильного пользовательского опыта на Android с помощью OneAgent SDK."), например WebSocket или gRPC.

### Настройка мониторинга веб-запросов

Все свойства, связанные с мониторингом веб-запросов, являются частью [WebRequest DSL](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestOptions.html), поэтому настраивайте их через [блок `webRequests`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:webRequests(org.gradle.api.Action)).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



webRequests {



// your web request monitoring configuration



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



webRequests {



// your web request monitoring configuration



}



}



}



}
```

Если веб-запрос инициируется вскоре после отслеживаемого пользовательского взаимодействия, OneAgent добавляет его как дочернее событие к отслеживаемому пользовательскому действию. OneAgent автоматически усекает запрос из захваченного URL и сообщает только доменное имя и путь ваших веб-запросов.

### Отключение мониторинга веб-запросов

Мониторинг веб-запросов можно полностью деактивировать с помощью свойства [`enabled`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestOptions.html#com.dynatrace.tools.android.dsl.WebRequestOptions:enabled). В этом случае все остальные свойства игнорируются, поэтому указывайте только свойство `enabled`, чтобы избежать путаницы.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



webRequests.enabled false



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



webRequests.enabled(false)



}



}



}
```

### Сенсоры мониторинга веб-запросов

Поддерживаются следующие HTTP-фреймворки:

* [HttpURLConnection](https://developer.android.com/reference/java/net/HttpURLConnection.html)
* [OkHttp](https://github.com/square/okhttp): только версии 3, 4 и 5
* Apache HTTP Client: только внутренняя версия Android HTTP Client[1]

1

Android объявил библиотеку Apache HTTP client устаревшей (см. [изменения Android 6.0](https://developer.android.com/about/versions/marshmallow/android-6.0-changes#behavior-apache-http-client) и [изменения Android 9.0](https://developer.android.com/about/versions/pie/android-9.0-changes-28#apache-p)), поэтому рекомендуется использовать другой HTTP-фреймворк. Новая [Apache HTTP Client версии 5](https://hc.apache.org/httpcomponents-client-5.0.x/index.html) не поддерживается. Старые версии Apache HTTP Client поддерживаются, поскольку предоставляют тот же интерфейс.

Если ваша библиотека веб-запросов основана на одном из этих поддерживаемых фреймворков, внутренние классы библиотеки инструментируются автоматически. Например, Retrofit версии 2 основан на OkHttp, поэтому все веб-запросы Retrofit инструментируются автоматически.

Можно деактивировать отдельные сенсоры через свойства [WebRequest Sensor DSL](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestSensors.html) и настроить их внутри [блока `sensors`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestOptions.html#com.dynatrace.tools.android.dsl.WebRequestOptions:sensors(org.gradle.api.Action)).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



webRequests {



sensors {



// fine-tune the sensors if necessary



}



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



webRequests {



sensors {



// fine-tune the sensors if necessary



}



}



}



}



}
```

## Мониторинг жизненного цикла

Для отслеживания событий жизненного цикла используется официальный Android-интерфейс [`ActivityLifecycleCallbacks`](https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks). Для activity Dynatrace сообщает о времени каждого вошедшего состояния жизненного цикла до момента, когда activity становится видимой; если доступны, метки времени обратных вызовов жизненного цикла отображаются в waterfall-анализе пользовательских действий и помечаются как **Lifecycle event**.

### Сообщаемые события жизненного цикла

При мониторинге жизненного цикла OneAgent собирает данные о следующих событиях.

* **Событие запуска приложения** (`AppStart`): измеряет время, необходимое для запуска приложения и отображения первой activity.

  Событие запуска приложения не захватывается при [отключении автоматического запуска OneAgent](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#disable-auto-startup "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.") или при запуске приложения в фоновом режиме без немедленного открытия activity.

* **Отображение activity**: измеряет время, необходимое для отображения activity.
* **Повторное отображение activity**: измеряет время, необходимое для повторного отображения ранее созданной activity. Возможны два варианта:

  + Вариант 1: activity находится в режиме *Stopped* и невидима на экране, затем снова переходит в режим *Started* и *Resumed*.
  + Вариант 2: activity находится в режиме *Paused* и не полностью видна (частично перекрыта), затем снова переходит в режим *Resumed*.

Временной промежуток для измерения продолжительности события жизненного цикла зависит от типа события и уровня Android API. При использовании Android API уровня 29+ можно более точно измерять продолжительность событий жизненного цикла благодаря обратным вызовам до и после жизненного цикла.

| Событие жизненного цикла | Android API 29+ | Android API 28 и ранее | Сообщаемые обратные вызовы |
| --- | --- | --- | --- |
| **Событие запуска приложения** | `Application.onCreate()` — `onActivityPostResumed` первой activity | `Application.onCreate()` — `onActivityResumed` первой activity | Обратные вызовы не сообщаются |
| **Отображение activity** | `onActivityPreCreated` — `onActivityPostResumed` | `onActivityCreated` — `onActivityResumed` | `onCreate` `onStart` `onResume` |
| **Повторное отображение activity**, вариант 1 | `onActivityPreStarted` — `onActivityPostResumed` | `onActivityStarted` — `onActivityResumed` | `onStart` `onResume` |
| **Повторное отображение activity**, вариант 2 | `onActivityPreResumed` — `onActivityPostResumed` | Измерение продолжительности невозможно | `onResume` |

### Настройка мониторинга жизненного цикла

События жизненного цикла либо являются частью существующих пользовательских действий, либо создают новое пользовательское действие и прикрепляют к нему действие отображения или повторного отображения жизненного цикла. Все свойства, связанные с мониторингом жизненного цикла, являются частью [Lifecycle DSL](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleOptions.html), поэтому настраивайте их через [блок `lifecycle`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:lifecycle(org.gradle.api.Action)).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



lifecycle {



// your lifecycle monitoring configuration



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



lifecycle {



// your lifecycle monitoring configuration



}



}



}



}
```

### Отключение мониторинга жизненного цикла

Мониторинг жизненного цикла можно деактивировать с помощью свойства [`enabled`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleOptions.html#com.dynatrace.tools.android.dsl.LifecycleOptions:enabled). В этом случае все остальные свойства игнорируются, поэтому указывайте только свойство `enabled`.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



lifecycle.enabled false



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



lifecycle.enabled(false)



}



}



}
```

### Сенсоры мониторинга жизненного цикла

Можно деактивировать отдельные сенсоры через свойства [Lifecycle Sensor DSL](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleSensors.html) и настроить их внутри [блока `sensors`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleOptions.html#com.dynatrace.tools.android.dsl.LifecycleOptions:sensors(org.gradle.api.Action)).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



lifecycle {



sensors {



// fine-tune the sensors if necessary



}



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



lifecycle {



sensors {



// fine-tune the sensors if necessary



}



}



}



}



}
```

## Отчёты о сбоях

OneAgent захватывает все [неперехваченные исключения](https://dt-url.net/UncaughtExceptionHandler). Отчёт о [сбое](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Узнайте о событиях пользователей и ошибках, а также о типах событий, захватываемых Dynatrace.") содержит время возникновения и полную трассировку стека исключения.

Как правило, сведения о сбое отправляются сразу после его возникновения, поэтому пользователю не нужно перезапускать приложение. Однако в некоторых случаях приложение должно быть открыто повторно в течение 10 минут, чтобы отчёт о сбое был отправлен. Обратите внимание, что Dynatrace не отправляет отчёты о сбоях старше 10 минут (такие отчёты больше не могут быть скоррелированы в кластере Dynatrace).

Отчёты о сбоях можно деактивировать с помощью свойства [`crashReporting`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:crashReporting).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



crashReporting false



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



crashReporting(false)



}



}



}
```

## Обнаружение rage tap

Dynatrace Android Gradle plugin версии 8.231+

Когда мобильное приложение не реагирует быстро, текстовая метка выглядит как кнопка или переключатель скрыт под другим переключателем, пользователи могут неоднократно нажимать на экран или затронутый элемент управления UI в раздражении. OneAgent обнаруживает такое поведение как [rage tap](/managed/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Узнайте о событиях пользователей и ошибках, а также о типах событий, захватываемых Dynatrace.").

OneAgent может отслеживать только события сенсорного экрана, обрабатываемые компонентом `Activity`. Компоненты Android UI, имеющие собственную логику обработки событий сенсорного экрана, например `Dialog` и `DreamService`, OneAgent не может отслеживать.

Обнаружение rage tap можно деактивировать с помощью свойства [`detectRageTaps`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.BehavioralEventsOptions.html#com.dynatrace.tools.android.dsl.BehavioralEventsOptions:detectRageTaps) в [BehavioralEvents DSL](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.BehavioralEventsOptions.html).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



behavioralEvents {



detectRageTaps false



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



behavioralEvents {



detectRageTaps(false)



}



}



}



}
```

## Мониторинг местоположения

При включении OneAgent добавляет захваченные позиции конечного пользователя к данным мониторинга. Для защиты конфиденциальности конечного пользователя OneAgent захватывает GPS-координаты с точностью до двух десятичных знаков (точность около 1 км).

Функцию мониторинга местоположения можно активировать с помощью свойства [`locationMonitoring`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:locationMonitoring).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



locationMonitoring true



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



locationMonitoring(true)



}



}



}
```

OneAgent захватывает только данные о местоположении, уже обрабатываемые в вашем приложении. OneAgent не запрашивает дополнительные данные о местоположении из Android SDK. Если ваше приложение не обрабатывает данные о местоположении, эта функция не активируется. При отключении мониторинга местоположения или отсутствии сведений о местоположении Dynatrace использует IP-адреса для определения местоположения пользователя.

Plugin поддерживает следующий listener местоположения:

* `android.location.LocationListener`