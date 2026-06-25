---
title: Установка OneAgent на Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows
scraped: 2026-05-12T11:07:30.878502
---

# Установка OneAgent на Windows

# Установка OneAgent на Windows

* Практическое руководство
* Чтение: 7 мин
* Обновлено 05 марта 2026 г.

На этой странице описано, как загрузить и установить Dynatrace OneAgent на Windows.

Для начала откройте [Cluster Management Console и выберите окружение](/managed/managed-cluster/operation/manage-your-monitoring-environments "Узнайте, как создавать, настраивать, открывать, удалять, отключать окружения мониторинга и переключаться между ними."), которое нужно мониторить, затем перейдите к шагам установки ниже.

Dynatrace предоставляет коллекцию Ansible, которую можно использовать для оркестрации развёртывания OneAgent в вашем окружении.
Дополнительные сведения см. в [Установка OneAgent с помощью Ansible](/managed/ingest-from/dynatrace-oneagent/deployment-orchestration/ansible "Узнайте, как развернуть OneAgent с помощью предоставляемого Dynatrace плейбука Ansible.").

## Требования и предварительные условия

* Вам нужны [права администратора](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows") на серверах, где будет установлен OneAgent, а также для изменения настроек брандмауэра (необходимо только если ваша внутренняя политика маршрутизации может препятствовать доступу программного обеспечения Dynatrace в Интернет).
* Вам нужны разрешения и учётные данные для перезапуска всех ваших сервисов приложений.
* Также ознакомьтесь с [требованиями к дисковому пространству](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Узнайте о структуре каталогов OneAgent и требованиях к дисковому пространству для установки OneAgent на Windows.").
* Хост, на котором устанавливается OneAgent, должен иметь не менее 200 МБ оперативной памяти.
* Установка OneAgent не поддерживается на сетевых точках монтирования хранилищ, управляемых такими стандартами, как NFS или iSCSI.
* Все хосты, которые должны мониториться, должны иметь возможность отправлять данные в кластер Dynatrace. В зависимости от вашего развёртывания Dynatrace, а также от схемы сети и настроек безопасности можно либо предоставить прямой доступ к кластеру Dynatrace, либо [настроить ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите базовые концепции, связанные с ActiveGate.").
* Для OneAgent версии 1.253 и более ранних рекомендуется [удалить любой существующий драйвер `WinPcap`](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#uninstall-winpcap-driver-to-allow-npcap-installation "Узнайте, как скачать и установить Dynatrace OneAgent на Windows."), чтобы разрешить установку `Npcap`: делайте это на всех версиях Windows, кроме `Windows Server 2019 build 1809 without hotfix KB5066187`.
  Для OneAgent версии 1.255+ `Npcap` устанавливается по умолчанию и может вызвать нарушение работы сети на `Windows Server 2016`, `Windows Server 2019 build 1809` и `Windows Server 2019 build 1809 without hotfix KB5066187`. Чтобы это предотвратить, обновите ваши хосты с помощью исправления [KB5066187](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5066187) или используйте [другие документированные варианты](/managed/observe/infrastructure-observability/networks-classic/troubleshoot-network-monitoring#potential-network-disruption-during-oneagent-installation-on-windows "Узнайте больше об устранении неполадок мониторинга сети.").

### Разрешите подключения через брандмауэр

Убедитесь, что настройки вашего брандмауэра разрешают связь с Dynatrace.  
В зависимости от политики вашего брандмауэра вам может потребоваться явно разрешить определённые исходящие подключения. **Удалённые адреса Dynatrace, которые нужно добавить в список разрешённых, указаны на странице установки OneAgent.**

## Удаление драйвера WinPcap для установки Npcap

Если у вас установлен драйвер `WinPcap`, рекомендуется удалить его перед установкой OneAgent и позволить установщику OneAgent установить подходящий драйвер захвата пакетов, входящий в комплект установщика OneAgent: `Npcap` является рекомендуемым драйвером захвата пакетов для OneAgent.

`Npcap` является преемником `WinPcap` и лучше всего подходит для анализа сети Dynatrace. Драйвер `Npcap`, поставляемый с установщиком OneAgent, упакован таким образом, что файлы его DLL-библиотек интегрированы с программным обеспечением Dynatrace, что позволяет выполнять обновления без вмешательства пользователя.

Дополнительные сведения см.:

* [Безопасность OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows")
* [Настройка установки OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Узнайте, как использовать установщик OneAgent для Windows.")

При обновлении с `WinPcap` на `Npcap` возможны нарушения работы сети; их можно смягчить, обновив версию Windows Server и/или отключив `Microsoft Network Monitor Driver`. Подробнее см. [Возможные нарушения работы сети при установке OneAgent на Windows](/managed/observe/infrastructure-observability/networks-classic/troubleshoot-network-monitoring#disruptionnetwork "Узнайте больше об устранении неполадок мониторинга сети.")

## Переустановка или восстановление установки

Установщик OneAgent для Windows не поддерживает операции `modify` и `repair`. Переустановить OneAgent с помощью той же версии установщика, которая использовалась для установки текущего OneAgent, невозможно. Чтобы переустановить OneAgent, сначала удалите его или установите более новую версию.

## Установка

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **Windows**.
3. Вставьте [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей.") в поле **Installer download token** или выберите **Generate token**, чтобы сгенерировать токен сейчас и автоматически вставить его в **Installer download token**. Этот токен необходим для загрузки установщика OneAgent из вашего окружения. Токен автоматически добавляется к командам загрузки и установки, которые вы будете использовать далее.
4. Скачайте установщик. Есть два варианта:

   * Выберите **Download OneAgent installer**, чтобы скачать установщик Windows (EXE-файл) для установки на одном сервере.
   * Загрузка через командную строку Windows. Скопируйте и выполните команду `powershell`. Она генерируется автоматически при вводе PaaS-токена.

     Эта команда работает только с PowerShell 3.0 и TLS 1.2 (или новее).

   Получение MSI-пакета

   Если вы хотите использовать групповые политики для автоматического распространения OneAgent на ваши хосты Windows, вам понадобится MSI-пакет вместе с пакетным файлом. Чтобы получить MSI-пакет:

   1. Скачайте установщик OneAgent, предоставляемый в виде EXE-файла.
   2. Запустите его с параметром `--unpack-msi`. Это извлечёт MSI-пакет и пакетный файл установки. При необходимости можно указать существующий путь. Если путь пропущен, файлы сохраняются в рабочий каталог. Например:

   ```
   C:\Downloads\Dynatrace-OneAgent-Windows.exe --unpack-msi "C:\installers"
   ```

   При использовании параметра `--unpack-msi` другие [параметры установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows.") не допускаются. Добавьте параметр `--quiet`, чтобы выполнить извлечение MSI-пакета в тихом режиме. Используйте параметр `--help`, чтобы отобразить всплывающее окно со списком доступных параметров.

   Скопируйте и вставьте MSI-пакет и пакетный файл при настройке групповой политики для установки Dynatrace. Установка по умолчанию должна работать в большинстве случаев, но если её требуется настроить, можно изменить [параметры установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows."). Затем необходимо создать точку распространения, назначить пакет (MSI-пакет OneAgent с параметрами), указать команду для установки MSI-пакета в режиме [тихой установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#silent-installation "Узнайте, как использовать установщик OneAgent для Windows.") и опубликовать вашу политику.
5. Необязательно **Set customized options**  
   На этом этапе интерфейс Dynatrace позволяет настроить установку OneAgent: ряд настроек можно задать интерактивно на экране. На основе введённых данных будет сгенерирована и отображена команда установки для использования на следующем шаге установки (см. ниже).  
   Вы можете:

   * Задать [сетевую зону](/managed/manage/network-zones#deploy-network-zones "Узнайте, как работают сетевые зоны в Dynatrace.") для этого хоста.
   * Организовать ваши хосты в [группы хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов."), если ваше окружение сегментировано (например, на разработку и продакшен).
   * Переопределить автоматически определённое [имя хоста](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Узнайте, как изменить имя мониторируемого хоста."). Это полезно в крупных и динамичных окружениях, где заданные имена хостов могут быть неинтуитивными или часто меняться.
   * Применить [теги](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашем окружении Dynatrace.") к хосту, чтобы осмысленно организовать ваши мониторируемые окружения.
   * Изменить режим OneAgent на Infrastructure Monitoring или Discovery вместо Full-Stack Monitoring. Дополнительные сведения см. в [Режимы мониторинга OneAgent](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.").
   * Отключить [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить Log Monitoring, какие сведения он может предоставить, и многое другое.").

   **Если требуются дополнительные настройки, можно указать [дополнительные параметры в командной строке](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows.").**
6. Если вы не указали никаких пользовательских параметров, запустите исполняемый файл и следуйте отображаемым инструкциям.
   Если вы указали пользовательские параметры выше, используйте сгенерированную команду и запустите её из каталога загрузки. Команда будет содержать все параметры установки, отражающие указанные вами пользовательские настройки.
7. Перезапустите все процессы, которые требуется мониторить. Вам будет показан список процессов, которые нужно перезапустить. Обратите внимание, что перезапустить процессы можно в любое время, даже во время следующего планового периода обслуживания в вашей организации. Однако пока не перезапущены все процессы, вы будете видеть лишь ограниченный набор метрик, например потребление CPU или памяти.

Что происходит во время установки?

OneAgent представляет собой набор специализированных служб, настроенных специально для вашего окружения мониторинга. Роль этих служб состоит в мониторинге различных аспектов ваших хостов, включая аппаратное обеспечение, операционную систему и процессы приложений.

В процессе установки установщик:

* Устанавливает исполняемый код и библиотеки, используемые OneAgent.
* Создаёт записи в реестре Windows, которые запускают OneAgent как службу `SYSTEM`. Кроме того, устанавливаются устройство `oneagentmon` и (опционально) `Npcap` или `WinPcap` для улучшения интеграции с операционной системой и упрощения сбора сетевой статистики.
* Проверяет глобальные настройки прокси системы.
* Проверяет подключение к Dynatrace Server или ActiveGate (если вы установили ActiveGate и скачали установщик OneAgent после того, как ActiveGate был подключён к Dynatrace).
* OneAgent версии 1.193 и более ранних Создаёт собственного пользователя (`dtuser`) для запуска расширений OneAgent. Этот пользователь входит в группу **Performance Monitoring Users** и может входить в систему только как служба. Пароль генерируется случайным образом во время установки и хранится в зашифрованном виде. Изменить пароль невозможно. В целях безопасности пользователю `dtuser` запрещено:

  + Доступ к компьютеру из сети.
  + Вход в систему как пакетное задание.
  + Локальный вход в систему.
  + Вход в систему через Remote Desktop Services.  
    Пользователь `dtuser` необходим для правильной работы Dynatrace, поэтому удалять его нельзя. Если по какой-либо причине `dtuser` был удалён, следующее обновление создаст его заново.
* OneAgent версии 1.195+ Для новых установок OneAgent 1.195+ для запуска расширений OneAgent используется учётная запись `LocalSystem account` по умолчанию.
  Сводку изменений, внесённых в вашу систему при установке OneAgent, см. в [Безопасность OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows").

## Вы на месте!

Отлично, настройка завершена! Теперь можно осмотреться в своём новом окружении мониторинга.

Доступ к окружению мониторинга можно получить через [Cluster Management Console](/managed/managed-cluster/operation/manage-your-monitoring-environments "Узнайте, как создавать, настраивать, открывать, удалять, отключать окружения мониторинга и переключаться между ними.").

![Вы на месте](https://dt-cdn.net/images/arrive-1533-e7eb3573a6.png)

Вы на месте

И последнее: чтобы мониторить ваши процессы, их нужно перезапустить. Перезапустить процессы можно в любое время, даже во время следующего планового периода обслуживания в вашей организации.