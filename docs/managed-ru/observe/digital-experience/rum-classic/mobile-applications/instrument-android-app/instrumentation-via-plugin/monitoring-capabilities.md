---
title: Настройка возможностей мониторинга Android Gradle plugin Dynatrace в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities
---

# Настройка возможностей мониторинга Android Gradle plugin Dynatrace в RUM Classic

# Настройка возможностей мониторинга Android Gradle plugin Dynatrace в RUM Classic

* Практическое руководство
* 25 мин на чтение
* Обновлено 27 апр. 2026 г.

Следующие параметры конфигурации позволяют настроить возможности мониторинга OneAgent и точно подстроить процесс автоматической инструментации для этих функций.

## Мониторинг пользовательских действий

OneAgent создаёт пользовательские действия на основе компонентов интерфейса, которые их вызывают, и автоматически объединяет данные о пользовательских действиях с другими данными мониторинга, например с информацией о веб-запросах и сбоях. OneAgent продлевает время жизни пользовательских действий, чтобы корректно агрегировать их с другими событиями, которые выполняются в фоновом потоке или сразу после пользовательского действия.

### Настройка мониторинга пользовательских действий

Мониторинг пользовательских действий настраивается с помощью следующих свойств:

* [`timeout`](#timeout-and-max-duration-properties)
* [`maxDuration`](#timeout-and-max-duration-properties)
* [`emptyActions`](#empty-actions-property)
* [`enabled`](#disable-user-action-monitoring)
* [`sensors`](#action-monitoring-sensors)
* [`namePrivacy`](#mask-user-actions)
* [`composeEnabled`](#compose-enable)

Все свойства, связанные с мониторингом пользовательских действий, входят в [UserAction DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html), поэтому настраивать их нужно через [блок `userActions`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:userActions(org.gradle.api.Action)).

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

С помощью свойства [`timeout`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:timeout) можно настроить время, в течение которого OneAgent может добавлять другие события к только что созданному пользовательскому действию. При обнаружении нового пользовательского взаимодействия OneAgent прекращает добавлять события к пользовательскому действию предыдущего взаимодействия, независимо от настроенного значения `timeout`. Вместо этого OneAgent добавляет события только к пользовательскому действию текущего взаимодействия.

По истечении периода `timeout` OneAgent проверяет, есть ли открытые события, и ждёт их завершения. С помощью свойства [`maxDuration`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:maxDuration) можно настроить максимальную длительность таких пользовательских действий. Если открытое событие, например веб-запрос, всё ещё не завершилось по истечении этого периода, OneAgent удаляет эти события из пользовательского действия и закрывает пользовательское действие с соответствующим значением времени окончания.

Значение для обоих свойств указывается в миллисекундах. Значение свойства `maxDuration` должно быть равно или больше значения свойства `timeout`.

| Свойство | Значение по умолчанию | Возможные значения |
| --- | --- | --- |
| `timeout` | `500` | `100` – `5000` |
| `maxDuration` | `60000` | `100` – `540000` |

Для свойств `timeout` и `maxDuration` можно настроить только по одному значению каждое, и эти значения должны подходить для всех пользовательских действий на всех устройствах.

#### Свойство `emptyActions`

OneAgent также передаёт пользовательские действия, которые не содержат дочерних событий. Чтобы отбрасывать такие пользовательские действия, используй свойство [`emptyActions`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:emptyActions).

### Отключение мониторинга пользовательских действий

Мониторинг пользовательских действий можно полностью отключить с помощью свойства [`enabled`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:enabled). В этом случае все остальные свойства игнорируются, поэтому во избежание путаницы стоит указывать только свойство `enabled`.

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

### Датчики мониторинга пользовательских действий

Плагин автоматически инструментирует следующие классы и методы:

| Библиотека/фреймворк | Инструментируемые классы/методы | Датчик |
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
| Jetpack Compose | `Slider`  `RangeSlider` | `composeSlider` |
| Jetpack Compose | `HorizontalPager`  `VerticalPager` | `composePager` |
| Jetpack Compose | Отвечает за предоставление [семантической информации для пользовательских действий](#compose-user-action-naming).  Этот датчик не обнаруживает никакого пользовательского ввода. | `composeSemantics` |

Отдельные датчики можно отключить через свойства [UserAction Sensor DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionSensors.html) и настроить их внутри [блока `sensors`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:sensors(org.gradle.api.Action)).

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

Для формирования имён пользовательских действий OneAgent получает заголовок элемента управления из разных атрибутов в зависимости от используемого слушателя или метода. Подробности смотри в таблице ниже.

| Слушатель, метод или компонент | Оцениваемый атрибут/свойство |
| --- | --- |
| `android.view.View$OnClickListener`  `android.widget.AdapterView$OnItemClickListener`  `android.widget.AdapterView$OnItemSelectedListener` | Атрибуты оцениваются в следующем порядке:  1. Атрибут [`android:contentDescription`﻿](https://developer.android.com/reference/android/view/View.html#attr_android:contentDescription) 2. Атрибут [`android:text`﻿](https://developer.android.com/reference/android/widget/TextView#attr_android:text) для компонентов на основе `TextView` 3. Имя класса |
| `android.app.Activity.onOptionsItemSelected`  `android.view.MenuItem$OnMenuItemClickListener` | [`getTitle`﻿](https://developer.android.com/reference/android/view/MenuItem#getTitle()) для пунктов меню |
| `androidx.viewpager.widget.ViewPager$OnPageChangeListener`  `androidx.swiperefreshlayout.widget.SwipeRefreshLayout$OnRefreshListener`  `android.support.v4.view.ViewPager$OnPageChangeListener`  `android.support.v4.widget.SwipeRefreshLayout$OnRefreshListener` | В качестве имени действия используется тип действия, так как компонент интерфейса недоступен |
| [Компоненты интерфейса Jetpack Compose](#compose-instrumentation) | Свойства оцениваются в следующем порядке:  1. [`SemanticsPropertyReceiver.dtActionName`](#compose-custom-user-action-name) 2. [`SemanticsPropertyReceiver.contentDescription`﻿](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/SemanticsPropertyReceiver#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).contentDescription()) 3. [`SemanticsPropertyReceiver.text`﻿](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/SemanticsPropertyReceiver#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).text()) 4. Имя класса |

### Маскирование пользовательских действий

Android Gradle plugin версии 8.249+

По умолчанию имена действий пользователя [формируются на основе заголовков элементов интерфейса](#user-action-naming), например, заголовков кнопок или пунктов меню. В редких случаях адреса электронной почты, имена пользователей и другая личная информация могут непреднамеренно попасть в имена действий пользователя. Это происходит, когда такая информация содержится в параметрах, используемых для заголовков элементов управления, в результате чего получаются такие имена действий, как `Touch on Account 123456`.

Если такая личная информация появляется в именах действий пользователя приложения, включи маскирование действий пользователя. OneAgent заменит все имена действий вида `Touch on <control title>` на имя класса элемента управления, которого коснулся пользователь, например:

* `Touch on Account 123456` > `Touch on Button`
* `Touch on Transfer all amount` > `Touch on Switch`
* `Touch on Account settings` > `Touch on ActionMenuItem`

Маскирование действий пользователя включается через свойство [`namePrivacy`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:namePrivacy) [UserAction DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html).

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

Если включить свойство `namePrivacy`, оно также будет маскировать действия пользователя для UI-компонентов [Jetpack Compose](#compose-instrumentation), и часть [метаданных компонентов](#compose-captured-metadata-by-component) не будет захватываться.

Если нужно изменить имена только для определённых действий пользователя, используй один из следующих вариантов:

* [Изменить автоматически создаваемые действия](#modify-auto-actions), чтобы поменять имена действий пользователя
* Задать правила именования (настройки мобильного приложения > **Naming rules**) для настройки правил именования действий пользователя или правил извлечения

### Изменение действий пользователя

OneAgent для Android создаёт действия пользователя на основе взаимодействий пользователей приложения. Эти действия отличаются от [пользовательских действий](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#create-custom-actions "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.") и иногда называются *автоматически создаваемыми действиями*. Также мы называем их *действиями пользователя*.

Действия пользователя можно изменять и даже отменять.

Если нужно избежать захвата личной информации сразу для всех действий пользователя, см. [Маскирование действий пользователя](#mask-user-actions).

Для UI-компонентов Jetpack Compose есть дополнительная возможность [задать пользовательское имя действия](#compose-custom-user-action-name).

#### Изменение конкретного действия пользователя

С помощью [`Dynatrace.modifyUserAction`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#modifyUserAction(com.dynatrace.android.agent.UserActionModifier)) можно изменить текущее действие пользователя. Можно поменять имя действия пользователя и передавать события, значения и ошибки. Также можно отменить действие пользователя.

Метод `Dynatrace.modifyUserAction` принимает в качестве параметра реализацию [`UserActionModifier`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/UserActionModifier.html), которая предоставляет текущий изменяемый объект [`ModifiableUserAction`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/ModifiableUserAction.html).

Для этого объекта действия пользователя допустимы следующие операции:

* `getActionName`
* `setActionName`
* `reportEvent`
* `reportValue`
* `reportError`
* OneAgent для Android версии 8.241+ `cancel`

Действие пользователя можно изменить, только пока оно ещё открыто. Если действие пользователя завершается по тайм-ауту до изменения, изменение не имеет эффекта. Рекомендуется вызывать `Dynatrace.modifyUserAction` внутри инструментированного [метода-слушателя](#user-action-monitoring-sensors) и не вызывать этот метод из другого потока.

В следующем примере на основе приложения-калькулятора показано, как изменить имя действия пользователя, создаваемого при нажатии кнопки, и как передать значение в это действие.

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

Для пользовательского мобильного действия или автоматически создаваемого мобильного действия пользователя максимальная длина имени составляет 250 символов.

#### Изменение любого действия пользователя

OneAgent для Android версии 8.241+

Изменять действия пользователя можно через [`Dynatrace.modifyUserAction`](#modify-specific-auto-action). Однако это возможно только для конкретного действия пользователя, и обычно нужно знать, открыто ли ещё это действие пользователя.

Чтобы преодолеть эти ограничения, была добавлена функция, позволяющая получать обратный вызов для каждого вновь созданного действия пользователя. С таким подходом уведомление приходит о каждом новом автоматически создаваемом действии пользователя, что даёт возможность обновить имя действия пользователя, а также передать события, значения и ошибки. Также можно отменить действие пользователя.

Можно зарегистрировать обратный вызов, который будет вызываться для каждого действия пользователя. [`UserActionModifier`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/UserActionModifier.html) задаётся один раз при запуске OneAgent через метод [`DynatraceConfigurationBuilder#withAutoUserActionModifier`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withAutoUserActionModifier(com.dynatrace.android.agent.UserActionModifier)). После этого он вызывается каждый раз, когда OneAgent создаёт действие пользователя. Он не вызывается для [пользовательских действий](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#create-custom-actions "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").

Зарегистрировать обратный вызов можно только при запуске OneAgent, поэтому нужно [запустить OneAgent вручную](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#start-oneagent "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").

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

Для пользовательского мобильного действия или автоматически создаваемого мобильного действия пользователя максимальная длина имени составляет 250 символов.

### Библиотека data binding для Android

Android Gradle plugin Dynatrace может инструментировать логику событий и слушатели, определённые с помощью функции [data binding﻿](https://developer.android.com/topic/libraries/data-binding). Если приложение содержит код, аналогичный [официальному примеру listener binding﻿](https://developer.android.com/topic/libraries/data-binding/expressions#listener_bindings), плагин может обнаружить нужный байт-код и инструментировать его.

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

### Определение обработчика события через атрибут XML

В [следующем примере из документации Android﻿](https://developer.android.com/guide/topics/ui/controls/button#HandlingEvents) показано, как определить обработчик события через атрибуты XML.

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

Плагин Dynatrace Android Gradle не может определить связь между кнопкой в файле разметки XML и методом `sendMessage` в activity. Однако, если приложение использует библиотеку Appcompat и активности унаследованы от `androidx.appcompat.app.AppCompatActivity`, плагин автоматически инструментирует логику делегирования библиотеки Appcompat. Если библиотека Appcompat не используется, эти методы обработчиков событий нужно инструментировать вручную, поскольку плагин не может определить связь между байт-кодом и файлом разметки XML.

## Мониторинг действий пользователя для Jetpack Compose

Dynatrace Android Gradle plugin версии 8.263+

Dynatrace поддерживает автоматическое инструментирование компонентов UI [Jetpack Compose﻿](https://developer.android.com/jetpack/compose). OneAgent создаёт действия пользователя на основе компонентов UI, которые их вызывают, и автоматически объединяет данные о действиях пользователя с другими данными мониторинга, например информацией о веб-запросах и сбоях.

Автоматическое инструментирование Jetpack Compose включено по умолчанию начиная с Dynatrace Android Gradle plugin версии 8.271.

Подробнее см. [Technology support | Mobile app Real User Monitoring](/managed/ingest-from/technology-support#mobile-rum "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

### Поддерживаемые компоненты UI

Поддерживается автоматическое инструментирование стандартных и пользовательских компонентов со стандартными действиями пользователя из UI-фреймворка Jetpack Compose. В таблице ниже перечислены эти компоненты и действия пользователя, а также ряд компонентов UI, основанных на этих инструментированных действиях пользователя.

| Компоненты и действия пользователя | Примеры компонентов |
| --- | --- |
| [Modifier.clickable﻿](https://dt-url.net/compose-modifier-clickable) | [Button﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.ButtonElevation,androidx.compose.ui.graphics.Shape,androidx.compose.foundation.BorderStroke,androidx.compose.material.ButtonColors,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1))  [IconButton﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#IconButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0))  [RadioButton﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#RadioButton(kotlin.Boolean,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.RadioButtonColors))  [Chip﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Chip(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.foundation.BorderStroke,androidx.compose.material.ChipColors,kotlin.Function0,kotlin.Function1)) |
| [Modifier.combinedClickable﻿](https://dt-url.net/compose-modifier-combinedClickable) |  |
| [Modifier.toggleable﻿](https://dt-url.net/compose-modifier-toggleable) | [Checkbox﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Checkbox(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.CheckboxColors))  [TriStateCheckbox﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TriStateCheckbox(androidx.compose.ui.state.ToggleableState,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.CheckboxColors))  [Switch﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Switch(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.SwitchColors))  [IconToggleButton﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#IconToggleButton(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) |
| [Modifier.swipeable﻿](https://dt-url.net/compose-modifier-swipeable)[3](#fn-1-3-def) | [SwipeToDismiss﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#SwipeToDismiss(androidx.compose.material.DismissState,androidx.compose.ui.Modifier,kotlin.collections.Set,kotlin.Function1,kotlin.Function1,kotlin.Function1))  [BottomDrawer﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#BottomDrawer(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.material.BottomDrawerState,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function0)) |
| [Modifier.pullRefresh﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/pullrefresh/package-summary#(androidx.compose.ui.Modifier).pullRefresh(androidx.compose.material.pullrefresh.PullRefreshState,kotlin.Boolean))[1](#fn-1-1-def), [2](#fn-1-2-def), [3](#fn-1-3-def) |  |
| [Slider﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Slider(kotlin.Float,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.ranges.ClosedFloatingPointRange,kotlin.Int,kotlin.Function0,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.SliderColors))[1](#fn-1-1-def)  [RangeSlider﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#RangeSlider(kotlin.ranges.ClosedFloatingPointRange,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.ranges.ClosedFloatingPointRange,kotlin.Int,kotlin.Function0,androidx.compose.material.SliderColors))[1](#fn-1-1-def) |  |
| [HorizontalPager﻿](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#HorizontalPager(androidx.compose.foundation.pager.PagerState,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.pager.PageSize,kotlin.Int,androidx.compose.ui.unit.Dp,androidx.compose.ui.Alignment.Vertical,androidx.compose.foundation.gestures.snapping.SnapFlingBehavior,kotlin.Boolean,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.input.nestedscroll.NestedScrollConnection,kotlin.Function2))[1](#fn-1-1-def), [3](#fn-1-3-def)  [VerticalPager﻿](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#VerticalPager(androidx.compose.foundation.pager.PagerState,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.pager.PageSize,kotlin.Int,androidx.compose.ui.unit.Dp,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.snapping.SnapFlingBehavior,kotlin.Boolean,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.input.nestedscroll.NestedScrollConnection,kotlin.Function2))[1](#fn-1-1-def), [3](#fn-1-3-def) |  |

1

Dynatrace Android Gradle plugin версии 8.267+

2

[Вторая версия `Modifier.pullRefresh`﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/pullrefresh/package-summary#(androidx.compose.ui.Modifier).pullRefresh(kotlin.Function1,kotlin.coroutines.SuspendFunction1,kotlin.Boolean)) не поддерживается.

3

Поддерживаемые версии Jetpack Compose: 1.3–1.5.

### Отключение мониторинга действий пользователя

Мониторинг действий пользователя для Jetpack Compose можно отключить с помощью свойства [`composeEnabled`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:composeEnabled) [UserAction DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html). Обратите внимание, что при отключённом автоматическом инструментировании Jetpack Compose все остальные свойства сенсора Jetpack Compose игнорируются, поэтому во избежание путаницы стоит указывать только свойство `composeEnabled`.

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

### Сенсоры мониторинга действий пользователя

Следующие сенсоры поддерживаются для автоматической инструментации Jetpack Compose. Подробности см. в [обзорной таблице со всеми сенсорами](#action-monitoring-sensors).

* `composeClickable`
* `composeSwipeable`
* `composeSemantics`

* `composePullRefresh`[1](#fn-2-1-def)
* `composeSlider`[1](#fn-2-1-def)
* `composePager`[1](#fn-2-1-def)

1

Dynatrace Android Gradle plugin версии 8.267+

Можно [отключить отдельные сенсоры](#deactivate-action-monitoring-sensors) через UserAction Sensor DSL.

Не рекомендуется отключать сенсор `composeSemantics`, поскольку он отвечает за формирование корректных имён пользовательских действий.

Если этот сенсор отключён, OneAgent использует имя класса инструментированного компонента в имени пользовательского действия. Например, `Touch on Finish your order` может измениться на что-то вроде `Touch on Button with function OrderViewKt$Toolbar$finish$1$2`.

### Формирование имени пользовательского действия

Чтобы сформировать имена пользовательских действий для компонентов Jetpack Compose UI, OneAgent считывает [семантическую информацию﻿](https://developer.android.com/jetpack/compose/semantics) и оценивает данные из [объединённого семантического дерева﻿](https://developer.android.com/jetpack/compose/semantics#merged-vs-unmerged) инструментированного компонента.

Для формирования корректных имён пользовательских действий оцениваются [четыре свойства](#compose-properties-for-user-action-names). Если присутствует несколько свойств, для имени пользовательского действия используется свойство с наивысшим приоритетом.

Если доступно несколько свойств одного типа, для имени пользовательского действия используется значение первого свойства. Пустые значения свойств игнорируются.

Упрощённый пример с двумя свойствами одного типа

В приведённом ниже фрагменте кода кнопка содержит два свойства `Text`, значения обоих свойств доступны в объединённом семантическом дереве. OneAgent возьмёт первое из них и сформирует имя пользовательского действия `Touch on Title`.

```
Button(onClick = { ... }) {



Text("Title")



Text("Body")



}
```

Более сложный пример с двумя свойствами одного типа

В приведённом ниже фрагменте кода компонент содержит два свойства `contentDescription`, значения обоих свойств доступны в объединённом семантическом дереве. OneAgent возьмёт первое из них и сформирует имя пользовательского действия `Touch on Finish your order` (а не `Touch on Finish`).

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

Чтобы задать собственное имя пользовательского действия для компонента Jetpack Compose UI, используй свойство `SemanticsPropertyReceiver.dtActionName`.

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

Для приведённого выше фрагмента кода OneAgent сформирует имя пользовательского действия `Touch on Finish your order`.

Свойство `SemanticsPropertyReceiver.dtActionName` является частью [объединённого семантического дерева﻿](https://developer.android.com/jetpack/compose/semantics#merged-vs-unmerged), но игнорируется службами специальных возможностей.

Для мобильного пользовательского (custom) действия или автоматически сформированного пользовательского действия максимальная длина имени составляет 250 символов.

Если нужно замаскировать персональные данные, отображающиеся в именах пользовательских действий приложения, включи [маскирование пользовательских действий](#mask-user-actions).

### Собираемые метаданные компонентов

При мониторинге мобильного приложения OneAgent для Android также собирает дополнительные метаданные для инструментированных компонентов Jetpack Compose. Эти метаданные хранятся в виде пар ключ-значение и [доступны в веб-интерфейсе Dynatrace](#compose-view-captured-metadata). Они дают дополнительный контекст по инструментированным компонентам, например, их расположение в коде, начальное и целевое состояния, типы пользовательских действий и прочее.

![Пример собранных метаданных для компонента Jetpack Compose в веб-интерфейсе Dynatrace](https://dt-cdn.net/images/jetpack-compose-captured-metadata-2023-0330-1771-60c62469c5.png)

Пример собранных метаданных для компонента Jetpack Compose в веб-интерфейсе Dynatrace

#### Собираемые параметры и значения по компонентам

В зависимости от того, как пользователь взаимодействовал с компонентом Jetpack Compose UI, передаются следующие пары ключ-значение.

Modifier.clickable

| Параметр | Описание | Передаваемое значение |
| --- | --- | --- |
| `function` | Имя функции для параметра `onClick` |  |
| [`role`﻿](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/Role) | Тип элемента пользовательского интерфейса | `null`, если `role` не задан |
| `type` | Тип пользовательского действия | `click` |

Modifier.combinedClickable

| Параметр | Описание | Передаваемое значение |
| --- | --- | --- |
| `function` | Имя функции для параметра `onClick`, `onLongClick` или `onDoubleClick` |  |
| [`role`﻿](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/Role) | Тип элемента пользовательского интерфейса | `null`, если `role` не задан |
| `type` | Тип пользовательского действия | `click` `double click` `long click` |

Modifier.toggleable

| Параметр | Описание | Передаваемое значение |
| --- | --- | --- |
| `function` | Имя функции для параметра `onValueChange` |  |
| [`role`﻿](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/Role) | Тип элемента пользовательского интерфейса | `null`, если `role` не задан |
| `fromState` | Начальное состояние UI-компонента. Например, если чекбокс был выбран и пользователь его снял, в качестве `fromState` передаётся `On`. |  |
| `type` | Тип пользовательского действия | `toggle` |

Modifier.swipeable

| Параметр | Описание | Передаваемое значение |
| --- | --- | --- |
| `state class` | Класс, являющийся держателем состояния для UI-компонента, например, [SwipeableState﻿](https://developer.android.com/reference/kotlin/androidx/compose/material/SwipeableState) |  |
| `fromState`[1](#fn-3-1-def) | Начальное состояние UI-компонента. Например, если пользователь смахнул от `A` к `B`, в качестве `fromState` передаётся `A`. |  |
| `toState`[1](#fn-3-1-def) | Целевое состояние UI-компонента. Например, если пользователь смахнул от `A` к `B`, в качестве `toState` передаётся `B`. |  |
| `type` | Тип пользовательского действия | `swipe` |

1

Не передаётся, если включено [маскирование пользовательских действий](#mask-user-actions).

Modifier.pullRefresh

| Параметр | Описание | Передаваемое значение |
| --- | --- | --- |
| `function` | Имя класса для параметра `onRefresh` (метод `rememberPullRefreshState`) |  |
| `type` | Тип пользовательского действия | `pull refresh` |

Slider и RangeSlider

| Параметр | Описание | Передаваемое значение |
| --- | --- | --- |
| `function` | Имя функции для параметра `onValueChange` |  |
| `toState` для `Slider` | Выбранное значение слайдера, например, `150` |  |
| `toState` для `RangeSlider` | Выбранный диапазон слайдера, например, `25..150` |  |
| `type` | Тип пользовательского действия | `slide` |

HorizontalPager и VerticalPager

| Параметр | Описание | Передаваемое значение |
| --- | --- | --- |
| `orientation` | Тип pager | `Horizontal` или `Vertical` |
| `fromState` | Начальный индекс страницы. Например, если пользователь пролистал фотогалерею от фото `1` к фото `2`, в качестве `fromState` передаётся `1`. |  |
| `toState` | Целевой индекс страницы. Например, если пользователь пролистал фотогалерею от фото `1` к фото `2`, в качестве `toState` передаётся `2`. |  |
| `type` | Тип пользовательского действия | `pager` |

#### Просмотр метаданных компонента в Dynatrace

Метаданные, собранные для компонентов Jetpack Compose UI, доступны на страницах waterfall-анализа пользовательских действий приложения.

Чтобы просмотреть собранные метаданные для компонента Jetpack Compose

1. В Dynatrace перейди в **Session Segmentation**.
2. Найди и выбери сессию, содержащую нужное пользовательское действие.
3. В разделе **Events and actions** разверни пользовательское действие, затем выбери **Perform waterfall analysis**.
4. Прокрути вниз до раздела **Reported values**, чтобы увидеть метаданные, собранные для компонента Jetpack Compose UI.

## Мониторинг веб-запросов

Плагин Dynatrace Android Gradle plugin может автоматически инструментировать и помечать веб-запросы. Для отслеживания веб-запросов OneAgent добавляет к веб-запросу HTTP-заголовок `x-dynatrace` с уникальным значением. Это необходимо для сопоставления данных мониторинга на стороне сервера с соответствующим мобильным веб-запросом.

Для HTTP(S)-запросов нельзя совмещать автоматическую и ручную инструментацию веб-запросов. Однако можно использовать автоматическую инструментацию для HTTP(S)-запросов и [ручную инструментацию для не-HTTP(S)-запросов](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#monitor-non-http-requests "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK."), таких как WebSocket или gRPC запросы.

### Настройка мониторинга веб-запросов

Все свойства мониторинга веб-запросов входят в [WebRequest DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestOptions.html), поэтому настраивать эти свойства нужно через [блок `webRequests`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:webRequests(org.gradle.api.Action)).

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

Если веб-запрос запускается вскоре после отслеживаемого пользовательского взаимодействия, OneAgent добавляет веб-запрос как дочернее событие к отслеживаемому пользовательскому действию. OneAgent автоматически усекает запрос из захваченного URL и сообщает только доменное имя и путь веб-запросов.

### Отключение мониторинга веб-запросов

Мониторинг веб-запросов можно полностью деактивировать с помощью свойства [`enabled`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestOptions.html#com.dynatrace.tools.android.dsl.WebRequestOptions:enabled). В этом случае все остальные свойства игнорируются, поэтому во избежание путаницы стоит указывать только свойство `enabled`.

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

### Фильтрация веб-запросов по URL

Свойство `urlFilters` внутри блока `webRequests` используется для того, чтобы предотвратить автоматическую инструментацию запросов, URL которых совпадает с одним или несколькими шаблонами регулярных выражений. Любой запрос, совпадающий хотя бы с одним шаблоном, исключается из автоматической инструментации и не отслеживается.

Значение по умолчанию, это пустой список, то есть по умолчанию ни один URL не отфильтровывается.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



webRequests {



urlFilters "example.com", "^http://", "\.test\."



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



urlFilters("example.com", "^http://", "\.test\.")



}



}



}



}
```

Каждый шаблон, это регулярное выражение, сопоставляемое со всем URL целиком.

### Сенсоры мониторинга веб-запросов

Поддерживаются следующие HTTP-фреймворки:

* [HttpURLConnection﻿](https://developer.android.com/reference/java/net/HttpURLConnection.html)
* [OkHttp﻿](https://github.com/square/okhttp): только версии 3, 4 и 5
* Apache HTTP Client: только внутренняя для Android версия HTTP Client[1](#fn-4-1-def)

1

Android объявил устаревшей библиотеку Apache HTTP client (см. [изменения в Android 6.0﻿](https://developer.android.com/about/versions/marshmallow/android-6.0-changes#behavior-apache-http-client) и [изменения в Android 9.0﻿](https://developer.android.com/about/versions/pie/android-9.0-changes-28#apache-p)), поэтому стоит использовать другой HTTP-фреймворк. [Apache HTTP Client версии 5﻿](https://hc.apache.org/httpcomponents-client-5.0.x/index.html) не поддерживается. Старые версии Apache HTTP Client поддерживаются, так как они предоставляют тот же интерфейс.

Если библиотека веб-запросов, которую использует приложение, основана на одном из этих поддерживаемых фреймворков, внутренние классы библиотеки инструментируются автоматически. Например, Retrofit версии 2 основан на OkHttp, поэтому все веб-запросы Retrofit инструментируются автоматически.

Конкретные сенсоры можно деактивировать через свойства [WebRequest Sensor DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestSensors.html) и настроить это внутри [блока `sensors`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestOptions.html#com.dynatrace.tools.android.dsl.WebRequestOptions:sensors(org.gradle.api.Action)).

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

Для отслеживания событий жизненного цикла используется официальный интерфейс Android [`ActivityLifecycleCallbacks`﻿](https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks). Для activity Dynatrace сообщает время каждого пройденного состояния жизненного цикла вплоть до момента, когда activity становится видимой; если доступны, временные метки колбэков жизненного цикла отображаются в анализе водопада пользовательского действия и помечаются как **Lifecycle event**.

### Отслеживаемые события жизненного цикла

При мониторинге жизненного цикла OneAgent собирает данные по следующим событиям жизненного цикла.

* **Событие запуска приложения** (`AppStart`): измеряет время, необходимое для запуска приложения и отображения первой activity.

  Событие запуска приложения не фиксируется, если [автоматический запуск OneAgent отключён](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#disable-auto-startup "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.") или если приложение запускается в фоновом режиме и не открывает activity незамедлительно.

* **Отображение activity**: измеряет время, необходимое для отображения activity.
* **Повторное отображение activity**: измеряет время, необходимое для повторного отображения ранее созданной activity. Возможны два варианта:

  + Вариант 1: activity находится в состоянии *Stopped* и не видна на экране, а затем снова переходит в состояния *Started* и *Resumed*.
  + Вариант 2: activity находится в состоянии *Paused* и не полностью видна на экране, а частично закрыта, а затем снова переходит в состояние *Resumed*.

Временной интервал, используемый для измерения длительности события жизненного цикла, зависит от типа события жизненного цикла и уровня Android API. При использовании Android API уровня 29+ длительность событий жизненного цикла можно измерить точнее благодаря колбэкам до и после жизненного цикла.

| Событие жизненного цикла | Android API 29+ | Android API 28 и ниже | Отслеживаемые колбэки жизненного цикла |
| --- | --- | --- | --- |
| **Событие запуска приложения** | `Application.onCreate()` – `onActivityPostResumed` первой activity | `Application.onCreate()` – `onActivityResumed` первой activity | Колбэки не отслеживаются |
| **Отображение activity** | `onActivityPreCreated` – `onActivityPostResumed` | `onActivityCreated` – `onActivityResumed` | ``` onCreate``onStart``onResume ``` |
| **Повторное отображение activity**, вариант 1 | `onActivityPreStarted` – `onActivityPostResumed` | `onActivityStarted` – `onActivityResumed` | ``` onStart``onResume ``` |
| **Повторное отображение activity**, вариант 2 | `onActivityPreResumed` – `onActivityPostResumed` | Измерить длительность невозможно | `onResume` |

### Настройка мониторинга жизненного цикла

События жизненного цикла либо входят в состав существующих пользовательских действий, либо создают новое пользовательское действие и присоединяют к нему действие отображения или повторного отображения жизненного цикла.
Все свойства, относящиеся к мониторингу жизненного цикла, входят в [Lifecycle DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleOptions.html), поэтому настраивать их нужно через [блок `lifecycle`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:lifecycle(org.gradle.api.Action)).

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

Мониторинг жизненного цикла можно деактивировать с помощью свойства [`enabled`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleOptions.html#com.dynatrace.tools.android.dsl.LifecycleOptions:enabled). В этом случае все остальные свойства игнорируются, поэтому стоит указывать только свойство `enabled`.

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

Конкретные сенсоры можно деактивировать через свойства [Lifecycle Sensor DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleSensors.html) и настроить это внутри [блока `sensors`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleOptions.html#com.dynatrace.tools.android.dsl.LifecycleOptions:sensors(org.gradle.api.Action)).

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

OneAgent фиксирует все [необработанные исключения﻿](https://dt-url.net/UncaughtExceptionHandler). Отчёт о [сбое](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") содержит время возникновения и полную трассировку стека исключения.

Как правило, данные о сбое отправляются сразу после его возникновения, поэтому пользователю не нужно перезапускать приложение. Однако в некоторых случаях приложение нужно снова открыть в течение 10 минут, чтобы отчёт о сбое был отправлен. Обрати внимание: Dynatrace не отправляет отчёты о сбоях старше 10 минут (такие отчёты уже нельзя сопоставить на кластере Dynatrace).

Отчёты о сбоях можно отключить с помощью свойства [`crashReporting`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:crashReporting).

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

Плагин Dynatrace Android Gradle версии 8.231+

Когда мобильное приложение медленно реагирует, текстовая метка выглядит как кнопка или переключатель скрыт под другим переключателем, пользователи могут раздражённо нажимать на экран или на затронутый элемент интерфейса несколько раз подряд. OneAgent распознаёт такое поведение как [rage tap](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.").

OneAgent может отслеживать только события касания экрана, обрабатываемые компонентом `Activity`. OneAgent не может отслеживать компоненты интерфейса Android с собственной логикой обработки касаний экрана, например `Dialog` и `DreamService`.

Обнаружение rage tap можно отключить с помощью свойства [`detectRageTaps`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.BehavioralEventsOptions.html#com.dynatrace.tools.android.dsl.BehavioralEventsOptions:detectRageTaps) из [BehavioralEvents DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.BehavioralEventsOptions.html).

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

## Отслеживание местоположения

При включении этой функции OneAgent добавляет зафиксированные позиции конечных пользователей к данным мониторинга. Для защиты конфиденциальности конечного пользователя OneAgent фиксирует координаты GPS с точностью до двух знаков после запятой (точность ~1 км).

Функцию отслеживания местоположения можно включить с помощью свойства [`locationMonitoring`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:locationMonitoring).

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

OneAgent фиксирует только те данные о местоположении, которые уже обрабатываются в приложении. OneAgent не запрашивает дополнительные данные о местоположении у SDK Android. Если приложение не обрабатывает данные о местоположении, эта функция не включается. Когда отслеживание местоположения отключено или данные о местоположении недоступны, Dynatrace определяет местоположение пользователя по IP-адресу.

Плагин поддерживает следующий слушатель местоположения:

* `android.location.LocationListener`