---
title: Средства управления безопасностью данных
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/data-security/data-security-controls
scraped: 2026-05-12T11:08:29.544606
---

# Средства управления безопасностью данных

# Средства управления безопасностью данных

* Чтение 10 мин
* Updated on May 04, 2026

## Хранение данных

Ваши данные мониторинга остаются в вашем собственном локальном центре обработки данных.

Также см. раздел [Сроки хранения данных](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Проверьте сроки хранения для различных типов данных.").

## Компоненты Dynatrace

[Dynatrace OneAgent](/managed/platform/oneagent "Узнайте о возможностях мониторинга OneAgent.") собирает все данные мониторинга в вашем мониторируемом окружении. Опционально все данные, собранные OneAgent, могут маршрутизироваться через [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate."), который выступает в роли прокси между Dynatrace OneAgent и кластером Dynatrace. При отсутствии ActiveGate данные, собранные OneAgent, отправляются непосредственно в кластер Dynatrace.

Кластеры Dynatrace Managed периодически обмениваются информацией — такой как лицензионные и потребительские данные — с [Dynatrace Mission Control](/managed/managed-cluster/basics/mission-control-data-exchange "Ознакомьтесь с данными, которыми кластер Managed обменивается с Mission Control, и доступными параметрами отказа для каждой категории данных.").

![Компоненты Dynatrace Managed](https://dt-cdn.net/images/dynatrace-data-security-managed-components-2-2690-71d9d32760.png)

Компоненты Dynatrace Managed

## Разграничение данных между окружениями клиентов

Dynatrace Managed выделяет один кластер на один аккаунт клиента.

## Шифрование данных в состоянии покоя

Настройку шифрования жёсткого диска и управление ключами шифрования вы выполняете самостоятельно.

## Шифрование данных в транзите

Все данные, передаваемые между OneAgent, ActiveGate и кластером Dynatrace, шифруются в транзите. Данные сериализуются и десериализуются с использованием Google Protocol Buffers.

Вы можете настраивать версии TLS и наборы шифров, а также использовать собственные [SSL-сертификаты](/managed/managed-cluster/installation/ssl-certificate-managed-cluster "Настройте собственный SSL-сертификат для кластера Managed вместо использования встроенной автоматизации сертификатов Dynatrace.").

![Шифрование данных в транзите](https://dt-cdn.net/images/dynatrace-data-security-managed-data-in-transit-2676-fee13f7c58.png)

Шифрование данных в транзите

## Аутентификация пользователей

Управление пользователями осуществляется через [настройку групп пользователей](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions "Узнайте о поддерживаемых разрешениях и политиках, о том, как назначать их группам и управлять пользователями и группами."), [SAML](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-saml "Узнайте, как подключить Dynatrace Server к серверу SAML для импорта групп пользователей или аккаунтов."), [OpenID](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-openid "Узнайте, как использовать OpenID в качестве SSO IdP для управления пользователями и группами.") и [LDAP](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-ldap "Узнайте, как подключить Dynatrace Server к серверу LDAP для импорта групп пользователей или аккаунтов.").

![Аутентификация пользователей](https://dt-cdn.net/images/dynatrace-data-security-managed-user-authentication-2525-25b24aca80.png)

Аутентификация пользователей

## Проверка целостности компонентов Dynatrace

Компоненты Dynatrace подписываются с использованием сертификатов подписи кода в рамках конвейера непрерывной доставки и интеграции (CI/CD).

Сертификаты подписи кода хранятся на аппаратных токенах с сертификатами подписи кода Extended Validation (EV) для Windows. Проверка подписи выполняется автоматически перед обновлением или установкой. При первоначальной установке компонента проверка подписи должна выполняться вручную.

![Проверка целостности компонентов Dynatrace](https://cdn.bfldr.com/B686QPH3/as/sjrcqtck3j773vsf95tsmfrk/Data_security_controls-_Integrity_verification_-_Light_Mode?auto=webp&format=png&position=1)

Проверка целостности компонентов Dynatrace

## Непрерывность бизнеса и высокая доступность

Высокая доступность может быть достигнута путём настройки нескольких узлов кластера. Команда Dynatrace Mission Control отслеживает качество сервиса и использование оборудования кластерами Dynatrace Managed. Используется настройка высокой доступности с несколькими узлами, и отправляются оповещения при необходимости дополнительного оборудования для мониторинга окружения. Дополнительные сведения см. в документе [Managed SLA](https://www.dynatrace.com/company/trust-center/sla/managed/) (для загрузки).

## Резервные копии данных и аварийное восстановление

Dynatrace Managed предлагает встроенный [механизм резервного копирования](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Изучите шаги и команды, необходимые для восстановления кластера Dynatrace Managed."), который необходимо настроить.

## Мониторинг инфраструктуры

Кластеры Dynatrace Managed регулярно отправляют проверки работоспособности в Dynatrace Mission Control. Опционально кластеры Managed могут мониторироваться кластером самомониторинга Dynatrace.

![Мониторинг инфраструктуры](https://dt-cdn.net/images/dynatrace-data-security-managed-infrastructure-monitoring-2539-ba851e65a0.png)

Мониторинг инфраструктуры

## Выпуск обновлений и исправлений

Используя полностью автоматизированный конвейер CI/CD, Dynatrace способен выпускать обновления и исправления в течение нескольких часов. Архитектура Dynatrace обеспечивает обновление кластеров без простоя.

Обновления доставляются через Dynatrace Mission Control. Новые функции выпускаются каждые 4 недели. Обновления кластера, OneAgent и ActiveGate можно выполнять автоматически или вручную.

![Выпуск обновлений и исправлений](https://dt-cdn.net/images/dynatrace-data-security-managed-updates-3029-959588547a.png)

Выпуск обновлений и исправлений

## Доступ к данным для поддержки Dynatrace

Вы полностью контролируете [удалённый доступ](/managed/managed-cluster/configuration/cluster-remote-access "Узнайте, как предоставить разрешение на удалённый доступ.") к своему кластеру в случае необходимости поддержки. Вы можете отключить удалённый доступ или настроить его таким образом, чтобы он требовал одобрения перед предоставлением. Поддержка Dynatrace имеет доступ только к программному обеспечению Dynatrace Managed (на уровне приложения), но не к базовой инфраструктуре или системному уровню.

Удалённый доступ устанавливается Dynatrace Mission Control, который доступен только из корпоративной сети Dynatrace. Удалённый доступ Dynatrace Mission Control требует многофакторной аутентификации. Каждый случай доступа и все внесённые изменения регистрируются в журнале аудита и полностью доступны вам.

![Доступ к данным для поддержки Dynatrace](https://dt-cdn.net/images/dynatrace-data-security-managed-support-access-2979-a5672b06a1.png)

Доступ к данным для поддержки Dynatrace

## Предотвращение утечки секретов Dynatrace

Dynatrace может обнаруживать и предотвращать утечку секретов Dynatrace в репозитории исходного кода на GitHub. Такие секреты могут включать токены платформы или API, случайно помещённые в репозиторий исходного кода. При обнаружении утечки секрета мы свяжемся с вами и окажем помощь в устранении последствий.

Подробнее о сообщении о проблемах безопасности см. в разделе [Сообщение об уязвимости безопасности](/managed/manage/data-privacy-and-security/data-security/report-a-security-related-concern "Узнайте, как сообщать об уязвимостях и к кому обращаться при проблемах безопасности.").

![Предотвращение утечки секретов](https://cdn.bfldr.com/B686QPH3/as/g36rffwrskqsrjkb47ghr2w/Data_security_controls_-_Secret_leak_prevention_-_Light_Mode?auto=webp&format=png&position=1)

Предотвращение утечки секретов

## Соответствие требованиям, сертификаты и аудиты

Dynatrace проходит ежегодные независимые аудиты третьих сторон и проводит тесты на проникновение и оценки red team с независимыми компаниями в области безопасности.

Наличие нескольких глобальных и локальных сертификатов и аккредитаций подтверждает соответствие наиболее признанным международным стандартам управления безопасностью.

Dynatrace также использует преимущества защищённых центров обработки данных Amazon, Azure и Google, сертифицированных для ISO 27001, PCI-DSS Level 1 и SOC 1/SSAE-16.

Полный список сертификатов см. в [Trust Center](https://www.dynatrace.com/company/trust-center/).