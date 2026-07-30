---
title: Установка OneAgent на Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux
---

# Установка OneAgent на Linux

# Установка OneAgent на Linux

* Практическое руководство
* 5 минут чтения
* Обновлено 22 июля 2026

На этой странице описано, как скачать и установить Dynatrace OneAgent на Linux.

Для начала перейдите в [Cluster Management Console и выберите среду](/managed/managed-cluster/operation/manage-your-monitoring-environments "Создание, настройка, доступ, удаление, отключение и переключение между средами мониторинга."), которую нужно мониторить, затем выполните шаги установки ниже.

## Требования

Можно установить OneAgent на любую Linux-систему, [поддерживаемую Dynatrace](/managed/ingest-from/technology-support#linux "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки."), независимо от системы пакетов дистрибутива.

### Права доступа

* Для загрузки и установки OneAgent нужны права [Download/install OneAgent](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions").
* Права [root](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Когда Dynatrace OneAgent требует root-привилегий на Linux.") нужны только для запуска установки OneAgent. При этом система должна соответствовать [определённым требованиям](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged#system-req "Когда Dynatrace OneAgent требует root-привилегий на Linux."). В противном случае добавьте параметр `NON_ROOT_MODE=0` в команду установки, чтобы отключить непривилегированный режим OneAgent.
* Нужны права доступа и учётные данные для перезапуска всех служб приложений.

### Ресурсы

* Проверьте [требования к дисковому пространству](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Структура каталогов OneAgent и требования к дисковому пространству для установки OneAgent на Linux.").
* Для запуска установки и обновления OneAgent на хосте требуется не менее 256 МБ свободной оперативной памяти.
* Для процесса установки требуется не менее 256 МБ виртуальной памяти.
* Все хосты, подлежащие мониторингу, должны иметь возможность отправлять данные в кластер Dynatrace. В зависимости от конфигурации Dynatrace, топологии сети и настроек безопасности можно либо предоставить прямой доступ к кластеру Dynatrace, либо [настроить ActiveGate](/managed/ingest-from/dynatrace-activegate "Базовые концепции ActiveGate.").

### Ограничения

При развёртывании OneAgent на Linux-хосте с Oracle Database Server 19c и/или подключёнными NFS-дисками существуют определённые ограничения. См. [Устранение неполадок при установке OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation#oracle-database-server-19c "Устранение неполадок при установке OneAgent на AIX, Linux и Windows.").

### Разрешение подключений через брандмауэр

Убедитесь, что настройки брандмауэра разрешают обмен данными с Dynatrace.  
В зависимости от политики брандмауэра может потребоваться явно разрешить определённые исходящие подключения. **Удалённые адреса Dynatrace, которые нужно добавить в список разрешённых, указаны на странице установки OneAgent.**

## Установка

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **Linux**.
3. Вставьте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") в поле **Installer download token** или выберите **Generate token**, чтобы сгенерировать токен прямо сейчас и автоматически вставить его в поле **Installer download token**. Токен нужен для загрузки установщика OneAgent из вашего окружения. Он автоматически добавляется к командам загрузки и установки, которые понадобятся позже.
4. **Select installer type**
   OneAgent поддерживает следующие архитектуры процессоров:

   * `Linux ARM` – ARM64 (AARch64), включая [процессоры AWS Graviton﻿](https://aws.amazon.com/ec2/graviton/)
   * `PowerPC (BE)` – 64-разрядная PowerPC (ppc64be) [Подробнее](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux "Learn how to download and install Dynatrace OneAgent on PPC BE Linux.")
   * `PowerPC (LE)` – 64-разрядная PowerPC (ppc64le)
   * `s390` – 64-разрядный мейнфрейм IBM Z (s390) [Подробнее](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS.")
   * `x86-64` – 64-разрядные Intel/AMD
5. **Download the installer**  
   Вставьте предложенную команду в терминал и запустите её.
6. **Verify the signature**  
   После завершения загрузки нажмите **Copy** в блоке **Verify signature**, чтобы скопировать команду `wget` в буфер обмена, затем вставьте её в терминал и запустите. Убедитесь, что система обновлена, особенно SSL и связанные библиотеки сертификатов.
7. Опционально **Set customized options**

   * Задайте [network zone](/managed/manage/network-zones#deploy-network-zones "Find out how network zones work in Dynatrace.") для этого хоста.
   * Если окружение сегментировано (например, на development и production), рассмотрите возможность [организации хостов в группы](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.").
   * Переопределите автоматически определённое [имя хоста](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name."). Это полезно в больших и динамичных окружениях, где заданные имена хостов могут быть неочевидны или часто меняться.
   * Примените [теги](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") к хосту, чтобы упорядочить отслеживаемые окружения удобным способом.
   * Переключите режим OneAgent на Infrastructure Monitoring или Discovery вместо Full-Stack Monitoring. Подробнее см. [Режимы мониторинга OneAgent](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").
   * Отключите [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

   Командный установщик OneAgent предоставляет дополнительные параметры для [настройки установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").
8. **Run the installer**  
   Вставьте команду в терминал и запустите её. Root-доступ нужен только для запуска установки OneAgent. Повышенные привилегии снимаются сразу после развёртывания Dynatrace OneAgent.

   Для Ubuntu Server

   ```
   sudo /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh
   ```

   Для Red Hat Enterprise Linux

   ```
   su -c '/bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh'
   ```

   При запуске root-сессии

   ```
   /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh
   ```

* Если планируется загрузить Dynatrace OneAgent напрямую на сервер, учтите: устаревшие или отсутствующие библиотеки (например, CA-сертификаты или OpenSSL) не позволят установщику выполнить загрузку.
* Dynatrace использует зашифрованные соединения. OpenSSL необходим, чтобы `wget` мог обращаться к серверу. Установщик также можно скачать, выбрав **Download OneAgent installer** в подвале страницы и сохранив скрипт установщика в любом удобном месте, что полностью исключает команду `wget`.

Что происходит во время установки?

Dynatrace OneAgent, это набор специализированных сервисов, настроенных конкретно для вашего окружения мониторинга. Эти сервисы отслеживают различные аспекты работы хостов: оборудование, операционную систему и процессы приложений.

В процессе установки установщик:

* Устанавливает исполняемый код и библиотеки, используемые Dynatrace OneAgent. Бинарные файлы OneAgent размещаются в каталоге `/opt/dynatrace/oneagent`, а стартовые скрипты создаются в `/etc/init.d` (на systemd-системах стартовые скрипты создаются в `/etc/systemd/system/`). Один из компонентов Linux OneAgent, `liboneagentproc.so`, находится в системном каталоге библиотек (`/lib` или `/lib64` в зависимости от архитектуры) и подключается через `/etc/ld.so.preload`.
* Создаёт собственного пользователя (`dtuser`). Этот пользователь создаётся без пароля. Войти под ним нельзя. В целях безопасности сервисы, не требующие root-привилегий, запускаются от имени этого пользователя. При этом сама установка по-прежнему требует root-доступа.
* Проверяет глобальные настройки прокси системы.
* Проверяет подключение к Dynatrace Server или ActiveGate (если ActiveGate установлен и установщик OneAgent загружен после подключения ActiveGate к Dynatrace).
* Определяет все SELinux-aware приложения и соответствующим образом корректирует политику безопасности SELinux.
* Разрешает Dynatrace OneAgent внедрять собственные библиотеки в отслеживаемые процессы.
* Изменяет конфигурацию core pattern, чтобы OneAgent мог обнаруживать и сообщать об аварийных завершениях процессов. Исходная конфигурация core\_pattern продолжит работать после установки и будет сохранена в `/opt/dynatrace/oneagent/agent/conf/original_core_pattern`, где можно задать собственные настройки core в формате, описанном в [Linux Programmer's Manual﻿](https://man7.org/linux/man-pages/man5/core.5.html).

Сводку изменений, внесённых в систему при установке OneAgent, см. в разделе [Безопасность OneAgent на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Learn about Dynatrace OneAgent security and modifications to your Linux-based system").

## Готово!

Настройка завершена. Теперь можно осмотреться в новом окружении мониторинга.

Доступ к окружению мониторинга осуществляется через [Cluster Management Console](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments.").

![Готово](https://dt-cdn.net/images/arrive-1533-e7eb3573a6.png)

Готово

Ещё один момент: чтобы процессы начали отслеживаться, их нужно перезапустить. Это можно сделать в любое время, в том числе во время следующего планового технического обслуживания в организации.