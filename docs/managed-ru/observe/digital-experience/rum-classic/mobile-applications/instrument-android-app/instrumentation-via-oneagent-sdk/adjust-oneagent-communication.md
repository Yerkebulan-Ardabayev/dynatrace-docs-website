---
title: Настройка взаимодействия с OneAgent SDK для Android в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication
---

# Настройка взаимодействия с OneAgent SDK для Android в RUM Classic

# Настройка взаимодействия с OneAgent SDK для Android в RUM Classic

* Практическое руководство
* 5 минут чтения
* Обновлено 05 марта 2026 г.

После завершения инструментации проверь следующие аспекты взаимодействия с OneAgent.

## Конфигурация сетевой безопасности

Если в приложении Android [настроена сетевая безопасность﻿](https://developer.android.com/training/articles/security-config), убедись, что HTTP-трафик к конечной точке `beaconUrl` не блокируется конфигурацией сетевой безопасности.

## Брандмауэр

Убедись, что GET- и POST-запросы к конечной точке `beaconUrl` не блокируются брандмауэром.

## Добавление сертификатов

Для HTTPS-взаимодействия OneAgent проверяет серверный сертификат и имя хоста. Взаимодействие OneAgent завершается ошибкой, если шаги проверки не выполнены.

Если для Cluster ActiveGate не выпущен сертификат доверенным промежуточным или корневым центром сертификации (CA), укажи серверный сертификат для SSL-взаимодействия в [файле конфигурации сетевой безопасности﻿](https://developer.android.com/training/articles/security-config.html) (для Android API уровня 24+).

Чтобы использовать функцию конфигурации сетевой безопасности, добавь раздел `domain-config` в файл `network_security_config.xml`.

```
<domain-config>



<domain includeSubdomains="true">your.domain.com</domain>



<trust-anchors>



<certificates src="@raw/your_server_certificate" />



</trust-anchors>



</domain-config>
```

Добавление сертификатов для приложений с Android API уровня 23 и ниже

Устарело

Если нужно указать серверный сертификат для приложений с Android API уровня 23 и ниже, включи сертификат в объект `KeyStore` и передай этот объект OneAgent, [выполнив ручной запуск через `DynatraceConfigurationBuilder` API](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#start-oneagent "Узнай, как расширить мониторинг пользовательского опыта в мобильных приложениях на Android с помощью OneAgent SDK."). Объект `KeyStore` должен содержать цепочку сертификатов Cluster ActiveGate, к которому нужно подключиться.

Эта опция устарела начиная с OneAgent SDK для Android версии 8.257. Начиная с этой версии, конфигурацию `KeyStore` используй только для более старых версий Android.

Если одновременно используются функция конфигурации сетевой безопасности и конфигурация `KeyStore`, приоритет имеет `KeyStore`.

Java

Kotlin

```
KeyStore trusted = KeyStore.getInstance("BKS");



try (InputStream in = getResources().openRawResource(R.raw.mykeystore)) {



trusted.load(in, "myverysecretpassword".toCharArray());



}



Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withKeyStore(trusted)



.buildConfiguration());
```

```
val trusted = KeyStore.getInstance("BKS")



resources.openRawResource(R.raw.mykeystore).use { inputStream ->



trusted.load(inputStream, "myverysecretpassword".toCharArray())



}



Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withKeyStore(trusted)



.buildConfiguration()



)
```

Временное отключение проверки сертификата

Устарело

Проверку сертификата можно также отключить. Однако используй эту опцию с осторожностью и не в production-коде. В противном случае отключение проверки сертификата может подорвать подлинность соединения. Также учти, что проверку имени хоста отключить нельзя.

Эта опция устарела начиная с OneAgent SDK для Android версии 8.257.

#### Через плагин Dynatrace Android Gradle

Проверку сертификата можно отключить через [свойство `certificateValidation`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DebugOptions.html#com.dynatrace.tools.android.dsl.DebugOptions:certificateValidation).

Groovy

Kotlin

```
dynatrace {



configurations {



sampleConfig {



debug {



certificateValidation false



}



}



}



}
```

```
configure<com.dynatrace.tools.android.dsl.DynatraceExtension> {



configurations {



create("sampleConfig") {



debug {



certificateValidation(false)



}



}



}



}
```

#### Через OneAgent SDK

Проверку сертификата можно также отключить методом [`ConfigurationBuilder.withCertificateValidation(boolean)`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withCertificateValidation(boolean)).

Java

Kotlin

```
Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCertificateValidation(false)



.buildConfiguration());
```

```
Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCertificateValidation(false)



.buildConfiguration())
```

## Привязка сертификата (certificate pinning)

Чтобы использовать привязку сертификата, следуй инструкциям Android в разделе [Network security configuration > Pin certificates﻿](https://developer.android.com/training/articles/security-config#CertificatePinning).

## Пользовательские HTTP-заголовки

Если HTTP-запросы OneAgent не удовлетворяют требованиям безопасности серверной инфраструктуры, можно изменить HTTP-заголовки OneAgent методом `Dynatrace.setBeaconHeaders(Map<String, String>)`. Эта функция позволяет добавить заголовок `Authorization` в HTTP-запросы и сразу переподключиться к Cluster ActiveGate после истечения срока действия токена.

Чтобы удалить старые заголовки, нужно вызвать `Dynatrace.setBeaconHeaders(null)`.

#### Базовая авторизация

Если информация об авторизации уже доступна при запуске приложения, метод `Dynatrace.setBeaconHeaders` нужно вызвать перед запуском метода `Dynatrace.startup`. В этом случае каждый HTTP-запрос OneAgent будет содержать корректные заголовки.

Java

Kotlin

```
Map<String, String> headers = new HashMap<>();



headers.put("Cookie", "n1=v1; n2=v2");



headers.put("ExampleHeader", "ExampleValue");



headers.put("Authorization", basicAuthorization(username, password));



Dynatrace.setBeaconHeaders(headers);



Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.buildConfiguration());
```

```
val headers = HashMap<String, String>()



headers["Cookie"] = "n1=v1; n2=v2"



headers["ExampleHeader"] = "ExampleValue"



headers["Authorization"] = basicAuthorization(username, password)



Dynatrace.setBeaconHeaders(headers)



Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.buildConfiguration()



)
```

Если информация об авторизации недоступна при запуске приложения, метод [`Dynatrace.setBeaconHeaders`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#setBeaconHeaders-java.util.Map-) нужно вызвать, когда эта информация станет доступна. Метод запуска `Dynatrace.startup` при этом всё равно нужно вызывать в `Application.onCreate`, чтобы корректно отследить время старта. OneAgent автоматически деактивируется, если сервер отправит ответ с недопустимым кодом статуса. Метод `Dynatrace.setBeaconHeaders` активирует OneAgent и сразу переподключит его к Cluster ActiveGate.

#### Авторизация с токеном

Если используется процедура авторизации, требующая регулярного обновления токена, нужно добавить `CommunicationProblemListener`. Слушатель нужно добавить через `DynatraceConfigurationBuilder` в методе `Dynatrace.startup`.

Java

Kotlin

```
Dynatrace.startup(this, new DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCommunicationProblemListener(new YourDynatraceListener())



.buildConfiguration());
```

```
Dynatrace.startup(this, DynatraceConfigurationBuilder("<YourApplicationID>", "<ProvidedBeaconURL>")



.withCommunicationProblemListener(YourDynatraceListener())



.buildConfiguration())
```

При использовании [`CommunicationProblemListener`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/comm/CommunicationProblemListener.html) поведение коммуникации OneAgent немного отличается от обычного. Если Cluster ActiveGate отвечает недопустимым кодом статуса, например `403 Forbidden`, OneAgent не будет переподключаться к серверу. Вместо этого OneAgent будет ждать, пока не будут заданы корректные заголовки методом `Dynatrace.setBeaconHeaders`. В этом случае OneAgent асинхронно уведомит `CommunicationProblemListener` в фоновом потоке через метод интерфейса [`onFailure(int, String, String)`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/comm/CommunicationProblemListener.html#onFailure-int-java.lang.String-java.lang.String-). Следующий фрагмент кода показывает пример реализации интерфейса `CommunicationProblemListener`:

Java

Kotlin

```
public class YourDynatraceListener implements CommunicationProblemListener {



@Override



public void onFailure(int responseCode, String responseMessage, String body) {



String token = refreshToken();



Dynatrace.setBeaconHeaders(generateAuthorizationHeader(token));



}



@Override



public void onError(Throwable throwable) {



//do nothing



}



}
```

```
class YourDynatraceListener : CommunicationProblemListener {



override fun onFailure(responseCode: Int, responseMessage: String?, body: String?) {



String token = refreshToken()



Dynatrace.setBeaconHeaders(generateAuthorizationHeader(token))



}



override fun onError(throwable: Throwable?) {



//do nothing



}



}
```

Метод интерфейса [`onError(Throwable)`﻿](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/comm/CommunicationProblemListener.html#onError-java.lang.Throwable-) вызывается асинхронно при возникновении проблемы связи, например тайм-аута соединения или ошибки SSL-рукопожатия. В этом случае OneAgent ждёт определённое время, а затем переподключается к Cluster ActiveGate. Обычно на этот callback-метод реагировать не нужно.

## Офлайн-мониторинг

Из соображений эффективности `Dynatrace` не принимает данные мониторинга старше 10 минут. Если приложение не подключено к интернету в течение более длительного периода, OneAgent отбрасывает старые данные мониторинга и прекращает мониторинг приложения до тех пор, пока устройство не установит новое сетевое соединение.