---
title: Configure monitoring capabilities of Dynatrace Android Gradle plugin
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities
scraped: 2026-05-12T11:32:36.948646
---

# Configure monitoring capabilities of Dynatrace Android Gradle plugin

# Configure monitoring capabilities of Dynatrace Android Gradle plugin

* How-to guide
* 25-min read
* Updated on Mar 05, 2026

With the following configuration options, you can customize OneAgent monitoring capabilities and fine-tune the auto-instrumentation process for these features.

## User action monitoring

OneAgent creates user actions based on the UI components that trigger these actions and automatically combines user action data with other monitoring data, such as information on web requests and crashes. OneAgent extends the lifetime of user actions to properly aggregate them with other events that are executed in a background thread or immediately after a user action.

### Configure user action monitoring

You can configure user action monitoring using the following properties:

* [`timeout`](#timeout-and-max-duration-properties)
* [`maxDuration`](#timeout-and-max-duration-properties)
* [`emptyActions`](#empty-actions-property)
* [`enabled`](#disable-user-action-monitoring)
* [`sensors`](#action-monitoring-sensors)
* [`namePrivacy`](#mask-user-actions)
* [`composeEnabled`](#compose-enable)

All properties related to user action monitoring are part of [UserAction DSLï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html), so configure them via the [`userActions` blockï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:userActions(org.gradle.api.Action)).

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

#### `timeout` and `maxDuration` properties

With the [`timeout`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:timeout) property, you can configure the time during which OneAgent can add other events to the newly created user action. When another user interaction is detected, OneAgent stops adding events to the user action of the previous interaction, regardless of the configured `timeout` value. Instead, OneAgent adds events only to the user action from the current user interaction.

When the `timeout` time period expires, OneAgent checks if there are open events and waits until these events are completed. With the [`maxDuration`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:maxDuration) property, you can configure the maximum duration of these user actions. If an open event, for example, a web request, is still not finished after this period, OneAgent removes these events from the user action and closes the user action with an appropriate end time value.

Specify the value for both properties in milliseconds. The value of the `maxDuration` property must be equal to or greater than the value of the `timeout` property.

| Property | Default value | Possible values |
| --- | --- | --- |
| `timeout` | `500` | `100` â `5000` |
| `maxDuration` | `60000` | `100` â `540000` |

You can configure only one value for the `timeout` and `maxDuration` properties each, and these values must fit all user actions on all devices.

#### `emptyActions` property

OneAgent also reports user actions that don't contain child events. To discard such user actions, use the [`emptyActions`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:emptyActions) property.

### Disable user action monitoring

You can completely deactivate user action monitoring with the [`enabled`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:enabled) property. In this case, all other properties are ignored, so only specify the `enabled` property to avoid confusion.

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

### User action monitoring sensors

The plugin automatically instruments the following classes and methods:

| Library/framework | Instrumented classes/methods | Sensor |
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
| Jetpack Compose | Responsible for providing [semantics information for user actions](#compose-user-action-naming).  This sensor doesn't detect any user input. | `composeSemantics` |

You can deactivate specific sensors via the [UserAction Sensor DSLï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionSensors.html) properties and configure it inside the [`sensors` blockï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:sensors(org.gradle.api.Action)).

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

### User action naming

To construct user action names, OneAgent captures the control title from different attributes depending on the listener or method used. See the table below for details.

| Listener, method, or component | Evaluated attribute/property |
| --- | --- |
| `android.view.View$OnClickListener`  `android.widget.AdapterView$OnItemClickListener`  `android.widget.AdapterView$OnItemSelectedListener` | Attributes are evaluated in the following order:  1. [`android:contentDescription`ï»¿](https://developer.android.com/reference/android/view/View.html#attr_android:contentDescription) attribute 2. [`android:text`ï»¿](https://developer.android.com/reference/android/widget/TextView#attr_android:text) attribute for `TextView`-based components 3. Class name |
| `android.app.Activity.onOptionsItemSelected`  `android.view.MenuItem$OnMenuItemClickListener` | [`getTitle`ï»¿](https://developer.android.com/reference/android/view/MenuItem#getTitle()) for menu items |
| `androidx.viewpager.widget.ViewPager$OnPageChangeListener`  `androidx.swiperefreshlayout.widget.SwipeRefreshLayout$OnRefreshListener`  `android.support.v4.view.ViewPager$OnPageChangeListener`  `android.support.v4.widget.SwipeRefreshLayout$OnRefreshListener` | Action type is used as an action name, as no UI component is available |
| [Jetpack Compose UI components](#compose-instrumentation) | Properties are evaluated in the following order:  1. [`SemanticsPropertyReceiver.dtActionName`](#compose-custom-user-action-name) 2. [`SemanticsPropertyReceiver.contentDescription`ï»¿](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/SemanticsPropertyReceiver#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).contentDescription()) 3. [`SemanticsPropertyReceiver.text`ï»¿](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/SemanticsPropertyReceiver#(androidx.compose.ui.semantics.SemanticsPropertyReceiver).text()) 4. Class name |

### Mask user actions

Dynatrace Android Gradle plugin version 8.249+

By default, user action names are [derived from UI control titles](#user-action-naming), for example, button or menu item titles. In rare circumstances, email addresses, usernames, or other personal information might be unintentionally included in user action names. This happens when this information is included in parameters used for control titles, resulting in user action names such as `Touch on Account 123456`.

If such personal information appears in your application's user action names, enable user action masking. OneAgent will replace all `Touch on <control title>` action names with the class name of the control that the user touched, for example:

* `Touch on Account 123456` > `Touch on Button`
* `Touch on Transfer all amount` > `Touch on Switch`
* `Touch on Account settings` > `Touch on ActionMenuItem`

You can enable user action masking with the [`namePrivacy`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:namePrivacy) property of the [UserAction DSLï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html).

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

If you enable the `namePrivacy` property, it will also mask user actions for [Jetpack Compose](#compose-instrumentation) UI components, and some [component metadata](#compose-captured-metadata-by-component) won't be captured.

If you want to change names only for certain user actions, use one of the following settings:

* [Modify autogenerated actions](#modify-auto-actions) to change user action names
* Set naming rules (mobile app settings > **Naming rules**) to configure user action naming rules or extraction rules

### Modify user actions

OneAgent for Android creates user actions based on interactions of your application's users. These actions are different from [custom actions](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#create-custom-actions "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.") and are sometimes called *autogenerated actions*. We also refer to them as *user actions*.

You can modify or even cancel user actions.

If you want to avoid capturing personal information for all user actions at once, see [Mask user actions](#mask-user-actions).

For Jetpack Compose UI components, there is an additional option available for [setting a custom user action name](#compose-custom-user-action-name).

#### Modify a specific user action

With [`Dynatrace.modifyUserAction`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#modifyUserAction(com.dynatrace.android.agent.UserActionModifier)), you can modify the current user action. You can change the user action name and report events, values, and errors. You can also cancel a user action.

The `Dynatrace.modifyUserAction` method accepts an implementation of [`UserActionModifier`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/UserActionModifier.html) as a parameter, which provides you with the current mutable [`ModifiableUserAction`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/ModifiableUserAction.html) object.

Allowed operations on this user action object are as follows:

* `getActionName`
* `setActionName`
* `reportEvent`
* `reportValue`
* `reportError`
* OneAgent for Android version 8.241+ `cancel`

You can modify a user action only while it is still open. If the user action times out before it is modified, the modification has no effect. We recommend that you invoke `Dynatrace.modifyUserAction` inside the instrumented [listener method](#user-action-monitoring-sensors) and don't call this method from a different thread.

In the following example, we're using a calculator app to show you how to change the name of the user action that is created for the button click and how to report a value to the action.

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

For a mobile custom action or a mobile autogenerated user action, the maximum name length is 250 characters.

#### Modify any user action

OneAgent for Android version 8.241+

You can modify user actions via [`Dynatrace.modifyUserAction`](#modify-specific-auto-action). However, you can do that only for a specific user action, and you usually should know whether this user action is still open or not.

To overcome these limitations, we introduced a feature that allows you to receive a callback for every newly created user action. With this approach, you are notified about every new autogenerated user action, so you get a chance to update the user action name as well as report events, values, and errors. You can also cancel a user action.

You can register a callback that is invoked for each user action. [`UserActionModifier`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/UserActionModifier.html) is set once at OneAgent startup via the [`DynatraceConfigurationBuilder#withAutoUserActionModifier`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withAutoUserActionModifier(com.dynatrace.android.agent.UserActionModifier)) method. After that, it is invoked each time OneAgent creates a user action. It is not invoked for [custom actions](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#create-custom-actions "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").

You can register a callback only when OneAgent is started, so you need to [start OneAgent manually](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#start-oneagent "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.").

Allowed operations are as follows:

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

For a mobile custom action or a mobile autogenerated user action, the maximum name length is 250 characters.

### Android data binding library

The Dynatrace Android Gradle plugin can instrument event logic and listeners that are defined via the [data bindingï»¿](https://developer.android.com/topic/libraries/data-binding) feature. If your app contains code similar to the [official listener binding exampleï»¿](https://developer.android.com/topic/libraries/data-binding/expressions#listener_bindings), the plugin can detect the correct bytecode and instrument it.

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

### Define an event handler via XML attribute

The [following example from the Android documentationï»¿](https://developer.android.com/guide/topics/ui/controls/button#HandlingEvents) shows how you can define an event handler via XML attributes.

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

The Dynatrace Android Gradle plugin cannot determine the relationship between the button in the layout XML file and the `sendMessage` method in the activity. However, when your app uses the Appcompat library and your activities are derived from `androidx.appcompat.app.AppCompatActivity`, the plugin auto-instruments the delegation logic of the Appcompat library. If you don't use the Appcompat library, you must manually instrument these event handler methods because the plugin is unable to determine the connection between the bytecode and the layout XML file.

## User action monitoring for Jetpack Compose

Dynatrace Android Gradle plugin version 8.263+

Dynatrace supports the auto-instrumentation of [Jetpack Composeï»¿](https://developer.android.com/jetpack/compose) UI components. OneAgent creates user actions based on the UI components that trigger these actions and automatically combines user action data with other monitoring data, such as information on web requests and crashes.

Jetpack Compose auto-instrumentation is enabled by default starting with Dynatrace Android Gradle plugin version 8.271.

See [Technology support | Mobile app Real User Monitoring](/managed/ingest-from/technology-support#mobile-rum "Find technical details related to Dynatrace support for specific platforms and development frameworks.") for more details.

### Supported UI components

We support auto-instrumentation of standard and custom components with default user interactions from the Jetpack Compose UI framework. The table below contains these components and user interactions as well as several UI components that are based on these instrumented user interactions.

| Components and user interactions | Example components |
| --- | --- |
| [Modifier.clickableï»¿](https://dt-url.net/compose-modifier-clickable) | [Buttonï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.ButtonElevation,androidx.compose.ui.graphics.Shape,androidx.compose.foundation.BorderStroke,androidx.compose.material.ButtonColors,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1))  [IconButtonï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#IconButton(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0))  [RadioButtonï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#RadioButton(kotlin.Boolean,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.RadioButtonColors))  [Chipï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Chip(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.ui.graphics.Shape,androidx.compose.foundation.BorderStroke,androidx.compose.material.ChipColors,kotlin.Function0,kotlin.Function1)) |
| [Modifier.combinedClickableï»¿](https://dt-url.net/compose-modifier-combinedClickable) |  |
| [Modifier.toggleableï»¿](https://dt-url.net/compose-modifier-toggleable) | [Checkboxï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Checkbox(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.CheckboxColors))  [TriStateCheckboxï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TriStateCheckbox(androidx.compose.ui.state.ToggleableState,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.CheckboxColors))  [Switchï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Switch(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.SwitchColors))  [IconToggleButtonï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#IconToggleButton(kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) |
| [Modifier.swipeableï»¿](https://dt-url.net/compose-modifier-swipeable)[3](#fn-1-3-def) | [SwipeToDismissï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#SwipeToDismiss(androidx.compose.material.DismissState,androidx.compose.ui.Modifier,kotlin.collections.Set,kotlin.Function1,kotlin.Function1,kotlin.Function1))  [BottomDrawerï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#BottomDrawer(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.material.BottomDrawerState,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function0)) |
| [Modifier.pullRefreshï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/pullrefresh/package-summary#(androidx.compose.ui.Modifier).pullRefresh(androidx.compose.material.pullrefresh.PullRefreshState,kotlin.Boolean))[1](#fn-1-1-def), [2](#fn-1-2-def), [3](#fn-1-3-def) |  |
| [Sliderï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Slider(kotlin.Float,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.ranges.ClosedFloatingPointRange,kotlin.Int,kotlin.Function0,androidx.compose.foundation.interaction.MutableInteractionSource,androidx.compose.material.SliderColors))[1](#fn-1-1-def)  [RangeSliderï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#RangeSlider(kotlin.ranges.ClosedFloatingPointRange,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.ranges.ClosedFloatingPointRange,kotlin.Int,kotlin.Function0,androidx.compose.material.SliderColors))[1](#fn-1-1-def) |  |
| [HorizontalPagerï»¿](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#HorizontalPager(androidx.compose.foundation.pager.PagerState,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.pager.PageSize,kotlin.Int,androidx.compose.ui.unit.Dp,androidx.compose.ui.Alignment.Vertical,androidx.compose.foundation.gestures.snapping.SnapFlingBehavior,kotlin.Boolean,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.input.nestedscroll.NestedScrollConnection,kotlin.Function2))[1](#fn-1-1-def), [3](#fn-1-3-def)  [VerticalPagerï»¿](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#VerticalPager(androidx.compose.foundation.pager.PagerState,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.pager.PageSize,kotlin.Int,androidx.compose.ui.unit.Dp,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.snapping.SnapFlingBehavior,kotlin.Boolean,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.input.nestedscroll.NestedScrollConnection,kotlin.Function2))[1](#fn-1-1-def), [3](#fn-1-3-def) |  |

1

Dynatrace Android Gradle plugin version 8.267+

2

[Second version of `Modifier.pullRefresh`ï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/pullrefresh/package-summary#(androidx.compose.ui.Modifier).pullRefresh(kotlin.Function1,kotlin.coroutines.SuspendFunction1,kotlin.Boolean)) is not supported.

3

Supported versions of Jetpack Compose: 1.3â1.5.

### Disable user action monitoring

You can disable user action monitoring for Jetpack Compose with the [`composeEnabled`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html#com.dynatrace.tools.android.dsl.UserActionOptions:composeEnabled) property of the [UserAction DSLï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.UserActionOptions.html). Note that all other Jetpack Compose sensor properties are ignored when Jetpack Compose auto-instrumentation is disabled, so only specify the `composeEnabled` property to avoid confusion.

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

### User action monitoring sensors

The following sensors are supported for the Jetpack Compose auto-instrumentation. For more details, check the [overview table with all sensors](#action-monitoring-sensors).

* `composeClickable`
* `composeSwipeable`
* `composeSemantics`

* `composePullRefresh`[1](#fn-2-1-def)
* `composeSlider`[1](#fn-2-1-def)
* `composePager`[1](#fn-2-1-def)

1

Dynatrace Android Gradle plugin version 8.267+

You can [deactivate specific sensors](#deactivate-action-monitoring-sensors) via the UserAction Sensor DSL.

We recommend that you do not disable the `composeSemantics` sensor, as it's responsible for generating proper user action names.

If you disable this sensor, OneAgent uses the class name of the instrumented component in the user action name. For example, `Touch on Finish your order` might change to something like `Touch on Button with function OrderViewKt$Toolbar$finish$1$2`.

### User action naming

To construct user action names for Jetpack Compose UI components, OneAgent captures [semantics informationï»¿](https://developer.android.com/jetpack/compose/semantics) and evaluates the information from the [merged semantics treeï»¿](https://developer.android.com/jetpack/compose/semantics#merged-vs-unmerged) of the instrumented component.

[Four properties](#compose-properties-for-user-action-names) are evaluated to generate proper user action names. When several properties are present, the property with the highest priority is used for a user action name.

When several properties of the same type are available, then the value of the first property is used for the user action name. Empty property values are ignored.

Simplified example with two properties of the same type

In the code snippet below, the button contains two `Text` properties; the values of both properties are available in the merged semantics tree. OneAgent will pick up the first one and generate the `Touch on Title` user action name.

```
Button(onClick = { ... }) {



Text("Title")



Text("Body")



}
```

More complex example with two properties of the same type

In the code snippet below, the component contains two `contentDescription` properties; the values of both properties are available in the merged semantics tree. OneAgent will pick up the first one and generate the `Touch on Finish your order` user action name (not `Touch on Finish`).

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

### Set custom user action name

If you want to set a custom user action name for a Jetpack Compose UI component, use the `SemanticsPropertyReceiver.dtActionName` property.

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

For the code snippet above, OneAgent will generate the `Touch on Finish your order` user action name.

The `SemanticsPropertyReceiver.dtActionName` property is part of the [merged semantics treeï»¿](https://developer.android.com/jetpack/compose/semantics#merged-vs-unmerged), but it's ignored by accessibility services.

For a mobile custom action or a mobile autogenerated user action, the maximum name length is 250 characters.

If you want to mask personal information that appears in your application's user action names, enable [user action masking](#mask-user-actions).

### Captured component metadata

When monitoring your mobile application, OneAgent for Android also captures additional metadata for the instrumented Jetpack Compose components. This metadata is stored as key-value pairs and is [available in the Dynatrace web UI](#compose-view-captured-metadata). It provides additional context for your instrumented components, for example, their location in code, initial and target states, user action types, and more.

![Example of captured metadata for a Jetpack Compose component in the Dynatrace web UI](https://dt-cdn.net/images/jetpack-compose-captured-metadata-2023-0330-1771-60c62469c5.png)

Example of captured metadata for a Jetpack Compose component in the Dynatrace web UI

#### Captured parameters and values by component

The following key-value pairs are reported depending on how the user interacted with the Jetpack Compose UI component.

Modifier.clickable

| Parameter | Description | Reported value |
| --- | --- | --- |
| `function` | Function name for the `onClick` parameter |  |
| [`role`ï»¿](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/Role) | Type of user interface element | `null` when `role` isn't provided |
| `type` | User action type | `click` |

Modifier.combinedClickable

| Parameter | Description | Reported value |
| --- | --- | --- |
| `function` | Function name for the `onClick`, `onLongClick`, or `onDoubleClick` parameter |  |
| [`role`ï»¿](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/Role) | Type of user interface element | `null` when `role` isn't provided |
| `type` | User action type | `click` `double click` `long click` |

Modifier.toggleable

| Parameter | Description | Reported value |
| --- | --- | --- |
| `function` | Function name for the `onValueChange` parameter |  |
| [`role`ï»¿](https://developer.android.com/reference/kotlin/androidx/compose/ui/semantics/Role) | Type of user interface element | `null` when `role` isn't provided |
| `fromState` | Initial state of the UI component For example, if the Ñheckbox was selected and the user cleared it, `On` is reported as `fromState`. |  |
| `type` | User action type | `toggle` |

Modifier.swipeable

| Parameter | Description | Reported value |
| --- | --- | --- |
| `state class` | Class that is a state holder for the UI component, for example, [SwipeableStateï»¿](https://developer.android.com/reference/kotlin/androidx/compose/material/SwipeableState) |  |
| `fromState`[1](#fn-3-1-def) | Initial state of the UI component For example, if the user swiped from `A` to `B`, `A` is reported as `fromState`. |  |
| `toState`[1](#fn-3-1-def) | Target state of the UI component For example, if the user swiped from `A` to `B`, `B` is reported as `toState`. |  |
| `type` | User action type | `swipe` |

1

Not reported if [user action masking](#mask-user-actions) is enabled.

Modifier.pullRefresh

| Parameter | Description | Reported value |
| --- | --- | --- |
| `function` | Class name for the `onRefresh` parameter (method `rememberPullRefreshState`) |  |
| `type` | User action type | `pull refresh` |

Slider and RangeSlider

| Parameter | Description | Reported value |
| --- | --- | --- |
| `function` | Function name for the `onValueChange` parameter |  |
| `toState` for `Slider` | Selected slider value, for example, `150` |  |
| `toState` for `RangeSlider` | Selected slider range, for example, `25..150` |  |
| `type` | User action type | `slide` |

HorizontalPager and VerticalPager

| Parameter | Description | Reported value |
| --- | --- | --- |
| `orientation` | Pager type | `Horizontal` or `Vertical` |
| `fromState` | Initial page index For example, if the user swiped through a photo gallery from photo `1` to photo `2`, `1` is reported as `fromState`. |  |
| `toState` | Target page index For example, if the user swiped through a photo gallery from photo `1` to photo `2`, `2` is reported as `toState`. |  |
| `type` | User action type | `pager` |

#### View component metadata in Dynatrace

The metadata captured for Jetpack Compose UI components is available on the waterfall analysis pages of your app's user actions.

To view captured metadata for a Jetpack Compose component

1. In Dynatrace, go to **Session Segmentation**.
2. Find and select a session that contains the required user action.
3. Under **Events and actions**, expand the user action, and then select **Perform waterfall analysis**.
4. Scroll down to the **Reported values** section to see the metadata captured for the Jetpack Compose UI component.

## Web request monitoring

The Dynatrace Android Gradle plugin can automatically instrument and tag your web requests. To track web requests, OneAgent adds the `x-dynatrace` HTTP header with a unique value to the web request. This is required to correlate the server-side monitoring data to the corresponding mobile web request.

For HTTP(S) requests, you cannot combine automatic and manual web request instrumentation. However, you can use automatic instrumentation for HTTP(S) requests and [manual instrumentation for non-HTTP(S) requests](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#monitor-non-http-requests "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.") such as WebSocket or gRPC requests.

### Configure web request monitoring

All web request monitoring related properties are part of [WebRequest DSLï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestOptions.html), so configure these properties via the [`webRequests` blockï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:webRequests(org.gradle.api.Action)).

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

If a web request is triggered shortly after a monitored user interaction, OneAgent adds the web request as a child event to the monitored user action. OneAgent automatically truncates the query from the captured URL and only reports the domain name and path of your web requests.

### Disable web request monitoring

You can completely deactivate web request monitoring with the [`enabled`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestOptions.html#com.dynatrace.tools.android.dsl.WebRequestOptions:enabled) property. In this case, all other properties are ignored, so only specify the `enabled` property to avoid confusion.

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

### Web request monitoring sensors

The following HTTP frameworks are supported:

* [HttpURLConnectionï»¿](https://developer.android.com/reference/java/net/HttpURLConnection.html)
* [OkHttpï»¿](https://github.com/square/okhttp): Only version 3, 4, and 5
* Apache HTTP Client: Only the Android-internal HTTP Client version[1](#fn-4-1-def)

1

Android has deprecated the Apache HTTP client library (see [Android 6.0 changesï»¿](https://developer.android.com/about/versions/marshmallow/android-6.0-changes#behavior-apache-http-client) and [Android 9.0 changesï»¿](https://developer.android.com/about/versions/pie/android-9.0-changes-28#apache-p)), so use a different HTTP framework. The new [Apache HTTP Client version 5ï»¿](https://hc.apache.org/httpcomponents-client-5.0.x/index.html) is not supported. Old Apache HTTP Client versions are supported because they provide the same interface.

If your web request library is based on one of these supported frameworks, the internal classes of the library are automatically instrumented. For example, Retrofit version 2 is based on OkHttp, so all Retrofit web requests are automatically instrumented.

You can deactivate specific sensors via the [WebRequest Sensor DSLï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestSensors.html) properties and configure it inside the [`sensors` blockï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.WebRequestOptions.html#com.dynatrace.tools.android.dsl.WebRequestOptions:sensors(org.gradle.api.Action)).

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

## Lifecycle monitoring

To track lifecycle events, we use the official Android [`ActivityLifecycleCallbacks`ï»¿](https://developer.android.com/reference/android/app/Application.ActivityLifecycleCallbacks) interface. For activities, Dynatrace reports the time of each entered lifecycle state until the activity is visible; if available, the timestamps of lifecycle callbacks are displayed in the user action waterfall analysis and are marked as a **Lifecycle event**.

### Reported lifecycle events

With lifecycle monitoring, OneAgent collects data on the following lifecycle events.

* **Application start event** (`AppStart`): Measures the time required to start an application and display the first activity.

  The application start event is not captured when the [automatic OneAgent startup is disabled](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#disable-auto-startup "Learn how to configure the Dynatrace Android Gradle plugin to adjust the auto-instrumentation process.") or when the application starts up in the background and does not promptly open an activity.

* **Activity display**: Measures the time required to display an activity.
* **Activity redisplay**: Measures the time required to redisplay a previously created activity. Two options are possible:

  + Option 1: An activity is in the *Stopped* mode and is not visible on the screen, and then it's *Started* and *Resumed* again.
  + Option 2: An activity is in the *Paused* mode and is not fully visible on the screen but partially obfuscated, and then it's *Resumed* again.

The timespan used for measuring the lifecycle event duration depends on the lifecycle event type and the level of Android API. When Android API level 29+ is used, we can measure the duration of lifecycle events more accurately thanks to pre- and post-lifecycle callbacks.

| Lifecycle event | Android API 29+ | Android API 28 and earlier | Reported lifecycle callbacks |
| --- | --- | --- | --- |
| **Application start event** | `Application.onCreate()` â `onActivityPostResumed` of the first activity | `Application.onCreate()` â `onActivityResumed` of the first activity | No callbacks reported |
| **Activity display** | `onActivityPreCreated` â `onActivityPostResumed` | `onActivityCreated` â `onActivityResumed` | `onCreate` `onStart` `onResume` |
| **Activity redisplay**, option 1 | `onActivityPreStarted` â `onActivityPostResumed` | `onActivityStarted` â `onActivityResumed` | `onStart` `onResume` |
| **Activity redisplay**, option 2 | `onActivityPreResumed` â `onActivityPostResumed` | Not possible to measure the duration | `onResume` |

### Configure lifecycle monitoring

Lifecycle events are either part of existing user actions, or they create a new user action and attach the display or redisplay lifecycle action to it.
All lifecycle monitoring related properties are part of [Lifecycle DSLï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleOptions.html), so configure them via the [`lifecycle` blockï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:lifecycle(org.gradle.api.Action)).

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

### Disable lifecycle monitoring

You can deactivate lifecycle monitoring with the [`enabled`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleOptions.html#com.dynatrace.tools.android.dsl.LifecycleOptions:enabled) property. In this case, all other properties are ignored, so specify only the `enabled` property.

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

### Lifecycle monitoring sensors

You can deactivate specific sensors via the [Lifecycle Sensor DSLï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleSensors.html) properties and configure it inside the [`sensors` blockï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.LifecycleOptions.html#com.dynatrace.tools.android.dsl.LifecycleOptions:sensors(org.gradle.api.Action)).

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

## Crash reporting

OneAgent captures all [uncaught exceptionsï»¿](https://dt-url.net/UncaughtExceptionHandler). The [crash](/managed/observe/digital-experience/rum-concepts/user-and-error-events#crash "Learn about user and error events and the types of user and error events captured by Dynatrace.") report includes the occurrence time and the full stack trace of the exception.

In general, the crash details are sent immediately after the crash, so the user doesnât have to relaunch the application. However, in some cases, the application should be reopened within 10 minutes so that the crash report is sent. Note that Dynatrace doesn't send crash reports that are older than 10 minutes (as such reports can no longer be correlated on the Dynatrace Cluster).

You can deactivate crash reporting with the [`crashReporting`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:crashReporting) property.

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

## Rage tap detection

Dynatrace Android Gradle plugin version 8.231+

When your mobile app doesn't respond quickly, a text label looks like a button, or a toggle is hidden under another toggle, users might repeatedly tap the screen or the affected UI control in frustration. OneAgent detects such behavior as a [rage tap](/managed/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.").

OneAgent can monitor only touch screen events that are handled by an `Activity` component. OneAgent cannot monitor Android UI components that have their own touch screen processing logic, for example, `Dialog` and `DreamService`.

You can deactivate rage tap detection using the [`detectRageTaps`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.BehavioralEventsOptions.html#com.dynatrace.tools.android.dsl.BehavioralEventsOptions:detectRageTaps) property of the [BehavioralEvents DSLï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.BehavioralEventsOptions.html).

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

## Location monitoring

When enabled, OneAgent appends the captured end user positions to the monitoring data. To protect the privacy of the end user, OneAgent captures GPS coordinates with a precision of two decimal places (~1 km accuracy).

You can activate the location monitoring feature with the [`locationMonitoring`ï»¿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:locationMonitoring) property.

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

OneAgent only captures location data that is already processed in your application. OneAgent doesn't request additional location data from the Android SDK. If your app doesn't process location data, this feature isn't enabled. When location monitoring is disabled or no location information is available, Dynatrace uses IP addresses to determine the location of the user.

The plugin supports the following location listener:

* `android.location.LocationListener`