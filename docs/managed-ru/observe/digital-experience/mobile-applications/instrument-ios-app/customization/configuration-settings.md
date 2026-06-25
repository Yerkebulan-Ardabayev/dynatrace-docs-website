---
title: Расширенная конфигурация OneAgent for iOS
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/configuration-settings
scraped: 2026-05-12T11:33:13.011735
---

# Расширенная конфигурация OneAgent for iOS

# Расширенная конфигурация OneAgent for iOS

* How-to guide
* 3-min read
* Updated on Dec 15, 2025

Процесс авто-инструментирования инструментирует iOS-приложения для мониторинга с помощью OneAgent. Инструментирование представляет собой автоматизированный способ добавления OneAgent в приложение без ручного изменения исходного кода. Авто-инструментированное приложение эквивалентно приложению, вручную инструментированному для базового сбора данных. Этот уровень инструментирования обеспечивает видимость реального пользовательского опыта, предоставляемого приложением, а также позволяет обнаруживать сбои и отслеживать производительность, связанную со временем запуска приложения и временем отклика веб-запросов.

## Только New RUM Experience

### Пользовательский URLSession

Для нового RUM Experience можно использовать API `Dynatrace.setURLSession` для установки пользовательского `URLSession`, обеспечивающего более гибкую настройку сетевого взаимодействия.

Это можно использовать, например, для настройки certificate pinning или добавления пользовательских заголовков, аналогично конфигурациям, описанным в примерах RUM Classic ниже.

## Только RUM Classic

### Настройка PKH Pinning с Dynatrace

Для аутентификации можно использовать функцию **Public Key Hash Pinning** (PKH).

Public key pinning несёт определённые риски и может вызвать проблемы при некорректной настройке. Если допустить ошибку, приложение может закрепить набор ключей, который действителен для аутентификации сейчас, но в какой-то момент в будущем перестанет работать. В таком случае приложение больше не сможет подключиться к серверу и, скорее всего, перестанет работать до обновления с новым набором ключей.

1. Перейдите в пакет дистрибутива OneAgent, откройте папку **Certificate Pinning** и запустите скрипт `getPKHashFromCertificate.py` для генерации хешей из ваших сертификатов.

   ```
   python getPKHashFromCertificate.py <path to your cert>.<der|pem> --type <DER | PEM>
   ```

   Вывод должен выглядеть следующим образом:

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
2. В файле [`Info.plist`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/info-plist-file "Файл Info.plist хранит ключи идентификации и конфигурации приложения. Используйте его для точной настройки конфигурации инструментирования.") используйте вывод скрипта в виде массива под [конфигурационным ключом `DTXPublicKeyPins`](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "С помощью конфигурационных ключей можно точно настроить авто-инструментирование iOS-приложений.").

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

Если у вас нет пакета дистрибутива OneAgent, его можно загрузить из настроек мобильного приложения.

1. Перейдите в **Mobile**.
2. Выберите мобильное приложение, которое нужно настроить.
3. В правом верхнем углу плитки с именем приложения нажмите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Instrumentation wizard**.
5. Выберите **iOS**, затем перейдите на вкладку **Developer**.
6. Нажмите **Download OneAgent**.

### Использование пользовательских HTTP-заголовков

Если HTTP-запросы OneAgent не соответствуют требованиям безопасности серверной инфраструктуры, можно изменить HTTP-заголовки OneAgent с помощью `Dynatrace.setBeaconHeaders([String : String]?)`. Эта функция позволяет добавить заголовок `Authorization` к HTTP-запросам и немедленно переподключиться к кластеру ActiveGate при истечении срока действия токена. Для удаления старых заголовков вызовите `Dynatrace.setBeaconHeaders(nil)`.

```
Dynatrace.setBeaconHeaders(["Cookie" : "n1=v1; n2=v2", "MyHeader" : "MyHeader", "Authorization" : "API-Token aa11bb22cc33dd44ee55"]) //set headers onto beacon



let headers: Dictionary<String, String>? = Dynatrace.beaconHeaders()    //request the headers that have been set



//listen for communication problems (for example, if beacon header contains a token that can expire required to pass a firewall)



NotificationCenter.default.addObserver(forName: NSNotification.Name(rawValue: Dynatrace.getCommunicationProblemNotificationName()), object: nil, queue: nil) { _ in



//for example, update beacon header with new token



}
```