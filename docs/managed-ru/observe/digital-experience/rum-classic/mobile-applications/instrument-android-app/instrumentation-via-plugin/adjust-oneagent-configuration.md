---
title: Настройка конфигурации OneAgent через плагин Dynatrace Android Gradle в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/adjust-oneagent-configuration
---

# Настройка конфигурации OneAgent через плагин Dynatrace Android Gradle в RUM Classic

# Настройка конфигурации OneAgent через плагин Dynatrace Android Gradle в RUM Classic

* Практическое руководство
* 3 мин чтения
* Обновлено 05 марта 2026 г.

Следующие параметры конфигурации можно использовать для изменения конфигурации OneAgent по умолчанию. Они особенно полезны при использовании вместе с функцией автоматического запуска OneAgent.

Их также можно использовать для настройки конфигурации OneAgent при использовании подхода с ручным запуском. В этом случае нужно быть внимательным, поскольку эти настройки могут быть переопределены с помощью `ConfigurationBuilder`.

## Изменение настроек конфиденциальности данных (режим opt-in)

В режиме opt-in каждый пользователь приложения может настроить свои предпочтения конфиденциальности данных и решить, хочет ли он делиться своей информацией. Когда режим opt-in включён, нужно запрашивать у каждого пользователя разрешение на сбор его данных, а затем сохранять его предпочтения конфиденциальности. Подробнее см. [Режим opt-in для пользователей](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Используйте настройки конфиденциальности, предоставляемые Dynatrace, чтобы обеспечить соответствие мобильных приложений требованиям регионального законодательства о защите данных.").

Чтобы активировать режим opt-in для пользователей (при использовании [автоматического запуска OneAgent](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/configure-plugin-for-instrumentation#auto-startup "Узнайте, как настроить плагин Dynatrace Android Gradle для настройки процесса автоинструментирования.")), включите свойство [`userOptIn`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:userOptIn).

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

Используйте OneAgent SDK для [изменения предпочтений конфиденциальности данных пользователя](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#data-privacy "Узнайте, как расширить мониторинг пользовательского опыта на мобильных устройствах в Android с помощью OneAgent SDK.").

## Настройка гибридных приложений

Для гибридных приложений нативное мобильное приложение отслеживается через OneAgent, а браузерная часть наблюдается с помощью [Dynatrace RUM JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Узнайте, как настроить Real User Monitoring Classic с помощью API JavaScript."). По этой причине мониторинг гибридных приложений требует дополнительной настройки. Дополнительную информацию см. в разделе [Инструментирование гибридных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-hybrid-app "Узнайте, как можно инструментировать различные типы гибридных и кроссплатформенных мобильных приложений.").

Все свойства, связанные с мониторингом гибридных приложений, являются частью [HybridWebView DSL﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html), поэтому настраивайте их через блок [`hybridWebView`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.VariantConfiguration.html#com.dynatrace.tools.android.dsl.VariantConfiguration:hybridWebView(org.gradle.api.Action)).

### Включение мониторинга гибридных приложений

Функцию мониторинга гибридных приложений можно активировать с помощью свойства [`enabled`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html#com.dynatrace.tools.android.dsl.HybridOptions:enabled).

### Указание доменов, имён хостов и IP-адресов

Для гибридных приложений, использующих RUM JavaScript внутри `WebView`, OneAgent должен устанавливать cookie для каждого инструментированного домена или сервера, с которым взаимодействует приложение. Когда функция мониторинга гибридных приложений включена, OneAgent генерирует эти cookie для каждого указанного домена и сохраняет их в `CookieManager`. Dynatrace использует эти cookie для идентификации мобильных и веб-сессий в приложении и объединения этих сессий в одну «гибридную» сессию.

Чтобы указать домены, имена хостов и IP-адреса, используйте свойство [`domains`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html#com.dynatrace.tools.android.dsl.HybridOptions:domains) или [`httpsDomains`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.HybridOptions.html#com.dynatrace.tools.android.dsl.HybridOptions:httpsDomains). Домены и поддомены должны начинаться с точки (`.`).

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

Если использовать свойство `httpsDomains`, атрибут cookie `Secure` добавляется ко всем cookie, устанавливаемым Dynatrace. Это гарантирует, что браузер отправляет эти cookie только по защищённым соединениям.

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

### Отключение cookie для файловых доменов

Плагин Dynatrace Android Gradle версии 8.271+

Для установки cookie для файловых доменов (начинающихся с `file://`) Dynatrace использует [`setAcceptFileSchemeCookies`﻿](https://developer.android.com/reference/android/webkit/CookieManager#setAcceptFileSchemeCookies(boolean)). Однако этот API больше не рекомендуется из-за проблем с безопасностью, планируется прекратить добавление cookie для доменов файловой схемы через пару месяцев.

Если нужно защитить приложение прямо сейчас, установите `fileDomainCookies` в `false`, и Dynatrace не будет добавлять cookie для доменов файловой схемы.

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

OneAgent позволяет включить балансировку нагрузки на стороне клиента, что помогает избежать неравномерной нагрузки на сервер, когда несколько OneAgent одновременно устанавливают соединение с ActiveGate.

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

## Включение RUM при первом запуске приложения

OneAgent позволяет включить RUM при первом запуске приложения, ещё до получения конфигурации кластера. Эта настройка не действует после первого запуска приложения. После получения конфигурации кластера этот флаг переопределяется навсегда. По умолчанию эта функция отключена.

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