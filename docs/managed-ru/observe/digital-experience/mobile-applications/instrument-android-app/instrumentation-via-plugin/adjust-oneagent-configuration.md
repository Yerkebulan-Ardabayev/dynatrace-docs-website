---
title: Настройка конфигурации OneAgent через Dynatrace Android Gradle plugin
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration
scraped: 2026-05-12T11:33:17.022098
---

# Настройка конфигурации OneAgent через Dynatrace Android Gradle plugin

# Настройка конфигурации OneAgent через Dynatrace Android Gradle plugin

* How-to guide
* 3-min read
* Updated on Mar 05, 2026

Следующие параметры конфигурации можно использовать для изменения конфигурации OneAgent по умолчанию. Они особенно полезны при совместном использовании с функцией автоматического запуска OneAgent.

Их также можно применять для настройки конфигурации OneAgent при ручном запуске. В этом случае следует учитывать, что настройки могут быть переопределены через `ConfigurationBuilder`.

## Изменение настроек конфиденциальности данных (режим opt-in)

В режиме opt-in для пользователя каждый пользователь вашего приложения может устанавливать собственные настройки конфиденциальности и решать, хочет ли он делиться своими данными. При включённом режиме opt-in необходимо запрашивать у каждого пользователя разрешение на сбор данных, а затем сохранять его предпочтения. Подробнее см. в разделе [Режим opt-in для пользователя](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности Dynatrace для обеспечения соответствия мобильных приложений нормативным требованиям вашего региона.").

Чтобы активировать режим opt-in для пользователя (при использовании [автоматического запуска OneAgent](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#auto-startup "Узнайте, как настроить Dynatrace Android Gradle plugin для регулировки процесса авто-инструментирования.")), включите свойство [`userOptIn`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:userOptIn).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



userOptIn true



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



userOptIn(true)



}



}



}
```

Используйте OneAgent SDK для [изменения настроек конфиденциальности пользователя](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#data-privacy "Узнайте, как расширить мониторинг пользовательского опыта на Android с помощью OneAgent SDK.").

## Настройка гибридных приложений

В гибридных приложениях нативное мобильное приложение отслеживается OneAgent, а браузерная часть — [Dynatrace RUM JavaScript](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Узнайте, как настроить Real User Monitoring с помощью JavaScript API."). Поэтому мониторинг гибридных приложений требует дополнительной настройки. Подробнее см. в разделе [Инструментирование гибридных приложений](/managed/observe/digital-experience/mobile-applications/instrument-hybrid-app "Узнайте, как инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.").

Все свойства, связанные с мониторингом гибридных приложений, являются частью [HybridWebView DSL](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html), поэтому настраивайте их через [блок `hybridWebView`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:hybridWebView(org.gradle.api.Action)).

### Включение мониторинга гибридных приложений

Активировать функцию мониторинга гибридных приложений можно с помощью свойства [`enabled`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html#com.dynatrace.tools.android.dsl.HybridOptions:enabled).

### Указание доменов, хостов и IP-адресов

Для гибридных приложений, использующих RUM JavaScript внутри `WebView`, OneAgent должен устанавливать cookies для каждого инструментированного домена или сервера, с которым взаимодействует приложение. При включённой функции мониторинга гибридных приложений OneAgent генерирует эти cookies для каждого указанного домена и сохраняет их в `CookieManager`. Dynatrace использует эти cookies для идентификации мобильных и веб-сессий в приложении и объединения их в одну «гибридную» сессию.

Для указания доменов, хостов и IP-адресов используйте свойство [`domains`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html#com.dynatrace.tools.android.dsl.HybridOptions:domains) или [`httpsDomains`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html#com.dynatrace.tools.android.dsl.HybridOptions:httpsDomains). Домены и субдомены должны начинаться с точки (`.`).

#### Свойство `domains`

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



hybridWebView {



enabled true



domains '.<domain1>', '.<domain2>'



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



hybridWebView {



enabled(true)



domains(".<domain1>", ".<domain2>")



}



}



}



}
```

#### Свойство `httpsDomains`

При использовании свойства `httpsDomains` атрибут `Secure` добавляется ко всем cookies, устанавливаемым Dynatrace. Это гарантирует отправку браузером этих cookies только через защищённые соединения.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



hybridWebView {



enabled true



httpsDomains 'https://.<domain1>', 'https://.<domain2>'



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



hybridWebView {



enabled(true)



httpsDomains("https://.<domain1>", "https://.<domain2>")



}



}



}



}
```

### Отключение cookies для файловых доменов

Dynatrace Android Gradle plugin версии 8.271+

Для установки cookies для файловых доменов (начинающихся с `file://`) Dynatrace использует [`setAcceptFileSchemeCookies`](https://developer.android.com/reference/android/webkit/CookieManager#setAcceptFileSchemeCookies(boolean)). Однако этот API больше не рекомендуется из-за проблем безопасности; в ближайшие месяцы планируется прекратить добавление cookies для доменов файловой схемы.

Если вы хотите защитить приложение прямо сейчас, установите `fileDomainCookies` в значение `false`, и Dynatrace не будет добавлять cookies для файловых доменов.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



hybridWebView {



enabled true



fileDomainCookies false



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



hybridWebView {



enabled(true)



fileDomainCookies(false)



}



}



}



}
```

## Включение балансировки нагрузки

OneAgent позволяет включить клиентскую балансировку нагрузки, которая помогает избежать неравномерной нагрузки на сервер при одновременном установлении соединения несколькими OneAgent с ActiveGate.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



agentBehavior {



startupLoadBalancing true



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



agentBehavior {



startupLoadBalancing(true)



}



}



}



}
```

## Включение нового RUM Experience при первом запуске приложения

OneAgent позволяет включить новый RUM Experience при первом запуске приложения, до получения конфигурации кластера. Этот параметр не оказывает никакого эффекта после первого запуска приложения. После получения конфигурации кластера она постоянно переопределяет этот флаг. По умолчанию данная функция отключена.

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



agentBehavior {



startupWithGrailEnabled true



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



agentBehavior {



startupWithGrailEnabled(true)



}



}



}



}
```