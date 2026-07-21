---
title: OneAgent для расширенной настройки iOS в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/configuration-settings
---

# OneAgent для расширенной настройки iOS в RUM Classic

# OneAgent для расширенной настройки iOS в RUM Classic

* Практическое руководство
* Чтение 3 минуты
* Обновлено 15 декабря 2025 г.

Процесс автоматической инструментации инструментирует приложения iOS для мониторинга с помощью OneAgent. Процесс инструментации, это автоматизированный способ добавления OneAgent в приложение без ручного изменения его исходного кода. Автоматически инструментированное приложение эквивалентно приложению, инструментированному вручную для базового сбора данных. Такой уровень инструментации обеспечивает видимость реального пользовательского опыта, который предоставляет приложение. Он также включает обнаружение сбоев и мониторинг производительности, связанный со временем запуска приложения и временем ответа на веб-запросы.

## Только RUM

### Пользовательская URL-сессия

Для RUM свойство `Dynatrace.setURLSession` API можно использовать для настройки пользовательского `URLSession`, что позволяет более гибко настраивать сетевое взаимодействие.

Это можно использовать, например, для настройки закрепления сертификатов (certificate pinning) или добавления пользовательских заголовков, аналогично конфигурациям, описанным в примерах RUM Classic ниже.

## Только RUM Classic

### Настройка закрепления PKH с помощью Dynatrace

Для аутентификации можно использовать функцию **Public Key Hash Pinning** (PKH).

Закрепление публичного ключа, это рискованная операция, которая приведёт к проблемам, если настроена неправильно. При ошибке приложение может закрепить набор ключей, который проходит проверку подлинности сегодня, но перестанет работать в неизвестный момент в будущем. В таком случае приложение больше не сможет подключиться к серверу и, скорее всего, перестанет работать до тех пор, пока не будет обновлено новым набором ключей.

1. Перейдите в дистрибутивный пакет OneAgent, откройте папку **Certificate Pinning** и запустите скрипт `getPKHashFromCertificate.py`, чтобы сгенерировать хеши из сертификатов.

   ```
   python getPKHashFromCertificate.py <path to your cert>.<der|pem> --type <DER | PEM>
   ```

   Результат должен выглядеть следующим образом:

   ```
   CERTIFICATE INFO



   ----------------



   subject= *****



   issuer= *****



   SHA1 Fingerprint= ******



   ---------------------- DTXDomainPins item ----------------------



   DTXPKHash: SomePublicKeyHash=



   DTXPKHashAlgoritm: DTXAlgorithmRsa2048
   ```
2. В [файле `Info.plist`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Info.plist file stores your app identification and configuration keys. Use it to fine-tune the instrumentation configuration.") используйте вывод скрипта как массив под [конфигурационным ключом `DTXPublicKeyPins`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.").

   ```
   <key>DTXPublicKeyPins</key>



   <array>



   <dict>



   <key>DTXPKHash</key>



   <string>SomePublicKeyHash=</string>



   <key>DTXPKHashAlgoritm</key>



   <string>DTXAlgorithmRsa2048</string>



   </dict>



   <dict>...script output 2...</dict>



   <dict>...script output 3...</dict>



   </array>
   ```

Если дистрибутивного пакета OneAgent нет, его можно скачать в настройках мобильного приложения.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. Выберите **More** (**…**) > **Edit** в правом верхнем углу плитки с названием приложения.
4. В настройках приложения выберите **Instrumentation wizard**.
5. Выберите **iOS**, затем переключитесь на вкладку **Developer**.
6. Выберите **Download OneAgent**.

### Использование пользовательских HTTP-заголовков

Если HTTP-запросы OneAgent не соответствуют требованиям безопасности серверной инфраструктуры, можно изменить HTTP-заголовки OneAgent с помощью `Dynatrace.setBeaconHeaders([String : String]?)`. Эта функция позволяет добавить заголовок `Authorization` к HTTP-запросам и немедленно переподключиться к кластеру ActiveGate после истечения срока действия токена. Чтобы удалить старые заголовки, вызовите `Dynatrace.setBeaconHeaders(nil)`.

```
Dynatrace.setBeaconHeaders(["Cookie" : "n1=v1; n2=v2", "MyHeader" : "MyHeader", "Authorization" : "API-Token aa11bb22cc33dd44ee55"]) //set headers onto beacon



let headers: Dictionary<String, String>? = Dynatrace.beaconHeaders()    //request the headers that have been set



//listen for communication problems (for example, if beacon header contains a token that can expire required to pass a firewall)



NotificationCenter.default.addObserver(forName: NSNotification.Name(rawValue: Dynatrace.getCommunicationProblemNotificationName()), object: nil, queue: nil) { _ in



//for example, update beacon header with new token



}
```