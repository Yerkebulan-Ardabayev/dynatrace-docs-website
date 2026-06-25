---
title: Настройка взаимодействия с OneAgent SDK for Android
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/adjust-oneagent-communication
scraped: 2026-05-12T11:33:19.081187
---

# Настройка взаимодействия с OneAgent SDK for Android

# Настройка взаимодействия с OneAgent SDK for Android

* How-to guide
* 5-min read
* Updated on Mar 05, 2026

После завершения инструментирования проверьте следующие аспекты взаимодействия с OneAgent.

## Конфигурация сетевой безопасности

Если в вашем Android-приложении [настроена сетевая безопасность](https://developer.android.com/training/articles/security-config), убедитесь, что HTTP-трафик к конечной точке `beaconUrl` не заблокирован конфигурацией сетевой безопасности.

## Фаервол

Убедитесь, что GET- и POST-запросы к конечной точке `beaconUrl` не блокируются фаерволом.

## Подключение сертификатов

Для HTTPS-коммуникации OneAgent проверяет сертификат сервера и имя хоста. Если проверка не пройдена, взаимодействие OneAgent не будет установлено.

Если у вашего Cluster ActiveGate нет сертификата, выданного доверенным промежуточным или корневым центром сертификации (CA), предоставьте сертификат сервера для SSL-коммуникации в [файле конфигурации сетевой безопасности](https://developer.android.com/training/articles/security-config.html) (для Android API уровня 24 и выше).

Чтобы использовать функцию Network Security Configuration, добавьте раздел `domain-config` в файл `network_security_config.xml`.

```
<domain-config>



<domain includeSubdomains="true">your.domain.com</domain>



<trust-anchors>



<certificates src="@raw/your_server_certificate" />



</trust-anchors>



</domain-config>
```

Подключение сертификатов для приложений с Android API уровня 23 и ниже

Deprecated

Если вам нужно предоставить сертификат сервера для приложений с Android API уровня 23 и ниже, включите сертификат в объект `KeyStore` и передайте его в OneAgent путём [выполнения ручного запуска через API `DynatraceConfigurationBuilder`](/managed/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android#start-oneagent "Узнайте, как расширить мониторинг пользовательского опыта на Android с помощью OneAgent SDK."). Объект `KeyStore` должен содержать цепочку сертификатов Cluster ActiveGate, к которому вы хотите подключиться.

Этот вариант устарел начиная с версии OneAgent SDK for Android 8.257. Начиная с этой версии, используйте конфигурацию `KeyStore` только для более старых версий Android.

Если вы используете одновременно функцию Network Security Configuration и конфигурацию `KeyStore`, последняя имеет приоритет.

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

Временное отключение проверки сертификатов

Deprecated

Вы также можете отключить проверку сертификатов. Однако используйте этот вариант осторожно и не в промышленном коде. Отключение проверки сертификатов может нарушить аутентичность соединения. Кроме того, обратите внимание, что проверку имени хоста отключить нельзя.

Этот вариант устарел начиная с версии OneAgent SDK for Android 8.257.

#### Через Dynatrace Android Gradle plugin

Отключить проверку сертификатов можно через свойство [`certificateValidation`](https://docs.dynatrace.com/javadoc/oneagent/android/gradle-plugin/dsl/com.dynatrace.tools.android.dsl.DebugOptions.html#com.dynatrace.tools.android.dsl.DebugOptions:certificateValidation).

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

Также можно отключить проверку сертификатов с помощью метода [`ConfigurationBuilder.withCertificateValidation(boolean)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/conf/ConfigurationBuilder.html#withCertificateValidation(boolean)).

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

## Прикрепление сертификатов

Чтобы использовать прикрепление сертификатов (certificate pinning), следуйте инструкциям Android: [Network security configuration > Pin certificates](https://developer.android.com/training/articles/security-config#CertificatePinning).

## Пользовательские HTTP-заголовки

Если HTTP-запросы OneAgent не соответствуют требованиям безопасности вашей серверной инфраструктуры, вы можете изменить HTTP-заголовки OneAgent с помощью метода `Dynatrace.setBeaconHeaders(Map<String, String>)`. Эта функция позволяет добавить заголовок `Authorization` к HTTP-запросам и немедленно повторно подключиться к Cluster ActiveGate при истечении срока действия токена.

Чтобы удалить старые заголовки, вызовите `Dynatrace.setBeaconHeaders(null)`.

#### Базовая авторизация

Если информация об авторизации доступна при запуске приложения, вызовите метод `Dynatrace.setBeaconHeaders` перед вызовом метода запуска `Dynatrace.startup`. В таком случае все HTTP-запросы OneAgent будут содержать корректные заголовки.

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

Если информация об авторизации недоступна при запуске приложения, вызовите метод [`Dynatrace.setBeaconHeaders`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/Dynatrace.html#setBeaconHeaders-java.util.Map-), когда эта информация станет доступна. Метод запуска `Dynatrace.startup` по-прежнему следует вызывать в методе `Application.onCreate` для корректной регистрации времени запуска. OneAgent автоматически деактивируется, когда сервер возвращает неверный код состояния. Метод `Dynatrace.setBeaconHeaders` активирует OneAgent и немедленно восстановит соединение с Cluster ActiveGate.

#### Авторизация с помощью токена

Если вы используете процедуру авторизации, при которой требуется регулярное обновление токена, следует добавить `CommunicationProblemListener`. Слушатель должен быть добавлен через `DynatraceConfigurationBuilder` в методе `Dynatrace.startup`.

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

При использовании [`CommunicationProblemListener`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/comm/CommunicationProblemListener.html) поведение коммуникации OneAgent несколько отличается от стандартного. Если Cluster ActiveGate отвечает неверным кодом состояния, например `403 Forbidden`, OneAgent не будет повторно подключаться к серверу. Вместо этого OneAgent будет ожидать, пока вы не укажете правильные заголовки с помощью метода `Dynatrace.setBeaconHeaders`. В этом случае OneAgent асинхронно уведомит `CommunicationProblemListener` в фоновом потоке через метод интерфейса [`onFailure(int, String, String)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/comm/CommunicationProblemListener.html#onFailure-int-java.lang.String-java.lang.String-). Ниже приведён пример реализации интерфейса `CommunicationProblemListener`:

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

Метод интерфейса [`onError(Throwable)`](https://docs.dynatrace.com/javadoc/oneagent/android/agent/com/dynatrace/android/agent/comm/CommunicationProblemListener.html#onError-java.lang.Throwable-) вызывается асинхронно при возникновении проблемы со связью, например тайм-аута соединения или ошибки SSL-рукопожатия. В этом случае OneAgent ожидает определённое время и затем повторно подключается к Cluster ActiveGate. Как правило, реагировать на этот метод обратного вызова не нужно.

## Мониторинг в автономном режиме

В целях повышения эффективности Dynatrace не принимает данные мониторинга старше 10 минут. Если приложение не подключено к интернету в течение более длительного времени, OneAgent отбрасывает устаревшие данные мониторинга и прекращает мониторинг приложения до тех пор, пока устройство не установит новое сетевое соединение.