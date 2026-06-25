---
title: Установка Environment ActiveGate на Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/windows/windows-install-an-environment-activegate
scraped: 2026-05-12T11:36:28.466208
---

# Установка Environment ActiveGate на Windows

# Установка Environment ActiveGate на Windows

* 3-min read
* Published Jul 17, 2018

Следуйте этим шагам для установки Environment ActiveGate на Windows.

## Перед началом

Определите назначение ActiveGate и проверьте соответствующие требования к оборудованию и системе. Требования к оборудованию и системе ActiveGate различаются в зависимости от **назначения**, для которого он устанавливается:

* Назначение: [Маршрутизация трафика OneAgent к Dynatrace, мониторинг облачных окружений или мониторинг удалённых технологий с помощью расширений](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.").
  Требования к оборудованию и системе для [ActiveGate маршрутизации/мониторинга](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Узнайте о требованиях к оборудованию и ОС перед установкой ActiveGate на Windows для маршрутизации и мониторинга.").
* Назначение: [Запуск синтетических мониторов из частного расположения](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGate для синтетического мониторинга внутренних и внешних ресурсов из частных расположений Synthetic.").
  Synthetic-enabled ActiveGate поддерживает подмножество операционных систем и предъявляет более высокие [требования к оборудованию и системе](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые ОС, версии Chromium и требования к оборудованию для запуска синтетических мониторов из частных расположений"), чем ActiveGate для маршрутизации и мониторинга.
* Назначение: [Установка модуля zRemote для мониторинга z/OS](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Узнайте об установке модуля zRemote для мониторинга z/OS.").
  ActiveGate с модулем zRemote предъявляет более высокие [требования к оборудованию и системе](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Подготовка и установка zRemote для мониторинга z/OS."), чем ActiveGate для маршрутизации и мониторинга.

В большинстве случаев ActiveGate можно установить в любое время после установки OneAgent. Однако в некоторых случаях порядок установки имеет значение, так как установщику OneAgent нужна информация об установке ActiveGate до того, как OneAgent будет установлен.

Если OneAgent уже установлен

В таких случаях сначала установите ActiveGate, затем загрузите установщик OneAgent.
Например, если вы загрузили установщик OneAgent и использовали его для установки Dynatrace в DMZ или сетевом сегменте без доступа в интернет, а затем установили ActiveGate, вам потребуется снова загрузить и установить OneAgent, чтобы установщик предоставил правильную конфигурацию между OneAgent и ActiveGate. Это связано с тем, что OneAgent должен быть автоматически настроен во время установки для подключения к мониторируемому окружению и отправки данных мониторинга на кластер Dynatrace через ActiveGate.

### Разрешение подключений через брандмауэр

Убедитесь, что настройки брандмауэра разрешают связь с Dynatrace.
В зависимости от политики брандмауэра может потребоваться явно разрешить определённые исходящие соединения. **Удалённые адреса Dynatrace для добавления в список разрешённых указаны в нижней части страницы установки ActiveGate.**
По умолчанию ActiveGate принимает входящие соединения на `порту 9999` и подключается к Dynatrace (исходящие соединения) через `порт 443`. Подробнее об использовании портов см. [Какие сетевые порты использует ActiveGate?](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates#port-usage "Узнайте о приоритетах подключения между типами ActiveGate и между ActiveGate и OneAgent.").

![AG на Windows](https://dt-cdn.net/images/screenshot-2023-08-10-at-11-10-53-am-1517-967b5764b3.png)

AG на Windows

## Начало установки

Войдите в Dynatrace. Перейдите в **Deploy Dynatrace**, затем выберите **Install ActiveGate**.

На странице **Install Environment ActiveGate** выберите **Windows**.

## Загрузка установщика

Способ загрузки установщика зависит от ваших настроек и потребностей. Можно загрузить установщик непосредственно на сервер, где планируется установка ActiveGate, или загрузить на другую машину, а затем перенести на сервер.

1. Выберите [назначение ActiveGate](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate.").

   * Для запуска синтетических мониторов из частного расположения см. [Создание частного расположения Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.").
   * Для маршрутизации z/OS-трафика к Dynatrace см. [Установка модуля zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS.").
2. Укажите [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях видимости."). Этот токен необходим для загрузки установщика ActiveGate из вашего окружения. Если у вас нет PaaS-токена, его можно создать прямо в UI. Токен автоматически добавляется к командам загрузки и установки.
3. Загрузите установщик. Доступны два варианта:

   * Нажмите **Download installer** для загрузки установщика Windows (EXE-файл).
   * Загрузка через командную строку Windows. Скопируйте и выполните команду `powershell`. Она генерируется автоматически при указании PaaS-токена.

     Эта команда работает только с PowerShell 3.0 и TLS 1.2 (или выше).

## Запуск установщика

Параметр установки (определяемый выбранным назначением ActiveGate) автоматически задаётся в команде запуска установщика. Убедитесь, что используете команду, отображённую в веб-интерфейсе Dynatrace, которая отражает назначение ActiveGate.

Для установки Environment ActiveGate необходимы права администратора. **Запустите исполняемый файл с правами администратора** и следуйте отображаемым инструкциям.

### Настройка установки

К команде установки можно добавить дополнительные [параметры](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate "Узнайте о параметрах для ActiveGate на Windows.") для настройки установки. Например, для установки исполняемых файлов и библиотек Environment ActiveGate в другую директорию используйте параметр `INSTALL=<path>` (ActiveGate версии 1.232+):

```
C:\ Dynatrace-ActiveGate-Windows-x86-1.0.0.exe INSTALL=D:\hosted_app\dynatrace
```

### Пользовательский сертификат для ActiveGate

Рекомендуется использовать пользовательские сертификаты для ActiveGate в целях повышения безопасности.

См. [Пользовательский SSL-сертификат](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate#custom-ssl-certificate "Узнайте о параметрах для ActiveGate на Windows.").

### Параметры установки по умолчанию

Параметры по умолчанию, включая директории по умолчанию, см. [Параметры установки ActiveGate по умолчанию для Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings "Узнайте о параметрах по умолчанию, с которыми устанавливается ActiveGate на Windows.").

## Установка завершена

После подключения ActiveGate к Dynatrace установка завершена, и OneAgent перенастраивается для отправки данных мониторинга через ActiveGate.

* Для проверки статуса установки выберите **Show deployment status** и перейдите на вкладку **Dynatrace ActiveGates**.
* Для получения помощи в устранении неполадок см. [Устранение неполадок ActiveGate](/managed/ingest-from/dynatrace-activegate "Понять основные концепции ActiveGate.").