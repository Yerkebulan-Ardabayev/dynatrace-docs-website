---
title: Как настроить мобильные приложения для мониторинга реальных пользователей?
source: https://docs.dynatrace.com/managed/offline-doc/how-do-i-set-up-mobile-apps-for-real-user-monitoring
scraped: 2026-05-12T11:25:02.207341
---

# Как настроить мобильные приложения для мониторинга реальных пользователей?

# Как настроить мобильные приложения для мониторинга реальных пользователей?

* Published Jul 19, 2017

Этот раздел применим только к установкам Dynatrace Managed.

Установки Dynatrace Managed, как правило, работают внутри частных центров обработки данных, где все входящие соединения ограничены брандмауэром. Чтобы инструментированные мобильные приложения могли передавать данные мониторинга реальных пользователей в вашу установку Dynatrace Managed, необходимо:

1. [Установить Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.").
2. [Настроить публичную конечную точку коммуникации](/managed/managed-cluster/basics/managed-deployments "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture."). Cluster ActiveGate предоставляет защищённый IP-адрес, на который ваши мобильные приложения могут безопасно отправлять данные мониторинга. Используйте этот URL публичной конечной точки при настройке инструментирования мобильного приложения.

Cluster ActiveGate по умолчанию прослушивает порт `9999`. Если это нежелательно, порт можно изменить в [конфигурации Cluster ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements."). Также можно использовать порт по вашему выбору и перенаправить трафик на порт `9999` через настройки брандмауэра.

Существующие URL-адреса публично доступных ActiveGates можно просмотреть в вашей установке Dynatrace Managed по пути **Settings** > **Public endpoints**.

## Инструментирование мобильного приложения

В зависимости от используемой платформы следуйте инструкциям ниже, чтобы включить отправку данных сессий непосредственно в ваш кластер Dynatrace Managed из мобильного приложения.

* [Android](/managed/observe/digital-experience/mobile-applications/instrument-android-app "Learn how to instrument mobile application monitoring on Android, how to customize instrumentation and more.")
* [iOS](/managed/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Set up user experience monitoring for iOS apps within Dynatrace.")

## Устранение неполадок

Для диагностики проблем с мониторингом реальных пользователей мобильных приложений проверьте следующее:

#### Корректен ли сертификат Cluster ActiveGate?

* Подписан ли корневой центр сертификации? [OneAgent для Android](/managed/discover-dynatrace/get-started/glossary#glossary-oneagent-android "Get acquainted with Dynatrace terminology.") и [OneAgent для iOS](/managed/discover-dynatrace/get-started/glossary#glossary-oneagent-android "Get acquainted with Dynatrace terminology.") требуют специальной настройки для работы с самоподписанными сертификатами.
* Совпадает ли имя хоста в сертификате Cluster ActiveGate с его именем? Проверка имени хоста в сертификате не выполняется для IP-адресов.

#### Доступен ли Cluster ActiveGate из сети мобильного приложения?

* С помощью браузера мобильного устройства убедитесь, что `timesync` возвращает корректный ответ. Например, `https://<psg-url>:<port>/mbeacon?type=mts` должен вернуть что-то вроде `type=mts&t1=-1&t2=-1`.

#### Получаете ли вы корректный ответ конфигурации OneAgent от Cluster ActiveGate?

* С помощью браузера мобильного устройства проверьте, возвращают ли запросы конфигурации OneAgent корректный ответ. Например, `https://<psg-url>:<port>/mbeacon/<environment id>?type=m&app=<app id>`.
* Убедитесь, что идентификатор среды и идентификатор приложения совпадают с теми, что указаны в инструкциях по настройке OneAgent для мобильных приложений.
* Ответ должен начинаться с `type=m` и не должен содержать `cp=0`. Такое значение означало бы, что захват данных отключён для данного идентификатора приложения и что это неизвестное приложение. Ответ также может содержать другие значения конфигурации, например `type=m&id=1&bl=150`.