---
title: Установка OneAgent на Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux
scraped: 2026-05-12T11:05:24.768162
---

# Установка OneAgent на Linux

# Установка OneAgent на Linux

* Практическое руководство
* Чтение: 5 мин
* Обновлено 22 января 2026 г.

На этой странице описано, как загрузить и установить Dynatrace OneAgent на Linux.

Для начала откройте [Cluster Management Console и выберите окружение](/managed/managed-cluster/operation/manage-your-monitoring-environments "Узнайте, как создавать, настраивать, открывать, удалять, отключать окружения мониторинга и переключаться между ними."), которое нужно мониторить, затем перейдите к шагам установки ниже.

## Требования

OneAgent можно установить на любую систему Linux, которая [поддерживается Dynatrace](/managed/ingest-from/technology-support#linux "Найдите технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки."), независимо от системы пакетов, на которую опирается ваш дистрибутив.

### Разрешения

* Вам нужны разрешения [Download/install OneAgent](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Разрешения на основе ролей") для загрузки и установки OneAgent.
* Для запуска установки OneAgent нужны только [права root](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Узнайте, когда Dynatrace OneAgent требует привилегий root на Linux."). Для этого ваша система должна соответствовать [определённым требованиям](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged#system-req "Узнайте, когда Dynatrace OneAgent требует привилегий root на Linux."). В противном случае добавьте параметр `NON_ROOT_MODE=0` к команде установки, чтобы отключить непривилегированный режим OneAgent.
* Вам нужны разрешения и учётные данные для перезапуска всех ваших сервисов приложений.

### Ресурсы

* Ознакомьтесь с [требованиями к дисковому пространству](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Узнайте о структуре каталогов OneAgent и требованиях к дисковому пространству для установки OneAgent на Linux.").
* Вашему хосту требуется 200 МБ свободной памяти для выполнения установки и обновления OneAgent.
* Все хосты, которые должны мониториться, должны иметь возможность отправлять данные в кластер Dynatrace. В зависимости от вашего развёртывания Dynatrace, а также от схемы сети и настроек безопасности можно либо предоставить прямой доступ к кластеру Dynatrace, либо [настроить ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите базовые концепции, связанные с ActiveGate.").

### Ограничения

Существуют определённые ограничения при развёртывании OneAgent на хосте Linux с Oracle Database Server 19c и/или с примонтированными дисками NFS. См. [Устранение неполадок установки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation#oracle-database-server-19c "Узнайте, как устранять неполадки установки OneAgent на AIX, Linux и Windows.").

### Разрешите подключения через брандмауэр

Убедитесь, что настройки вашего брандмауэра разрешают связь с Dynatrace.  
В зависимости от политики вашего брандмауэра вам может потребоваться явно разрешить определённые исходящие подключения. **Удалённые адреса Dynatrace, которые нужно добавить в список разрешённых, указаны на странице установки OneAgent.**

## Установка

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **Linux**.
3. Вставьте [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей.") в поле **Installer download token** или выберите **Generate token**, чтобы сгенерировать токен сейчас и автоматически вставить его в **Installer download token**. Этот токен необходим для загрузки установщика OneAgent из вашего окружения. Токен автоматически добавляется к командам загрузки и установки, которые вы будете использовать далее.
4. **Select installer type**
   OneAgent поддерживает следующие архитектуры ЦП:

   * `Linux ARM` - ARM64 (AARch64), включая [процессоры AWS Graviton](https://aws.amazon.com/ec2/graviton/)
   * `PowerPC (BE)` - 64-битный PowerPC (ppc64be) [Подробнее](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux "Узнайте, как скачать и установить Dynatrace OneAgent на PPC BE Linux.")
   * `PowerPC (LE)` - 64-битный PowerPC (ppc64le)
   * `s390` - 64-битный мейнфрейм IBM Z (s390) [Подробнее](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Установка, настройка и управление модулями Dynatrace на z/OS.")
   * `x86-64` - 64-битный Intel/AMD
5. **Download the installer**  
   Вставьте предоставленную команду в окно терминала и выполните её.
6. **Verify the signature**  
   После завершения загрузки нажмите **Copy** в поле **Verify signature**, чтобы скопировать команду `wget` в буфер обмена, затем вставьте предоставленную команду в окно терминала и выполните её. Убедитесь, что ваша система обновлена, особенно SSL и связанные с ним библиотеки сертификатов.
7. Необязательно **Set customized options**

   * Задайте [сетевую зону](/managed/manage/network-zones#deploy-network-zones "Узнайте, как работают сетевые зоны в Dynatrace.") для этого хоста.
   * Если ваше окружение сегментировано (например, на разработку и продакшен), рассмотрите возможность [организации хостов в группы хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов.").
   * Переопределите автоматически определённое [имя хоста](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Узнайте, как изменить имя мониторируемого хоста."). Это полезно в крупных и динамичных окружениях, где заданные имена хостов могут быть неинтуитивными или часто меняться.
   * Примените [теги](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашем окружении Dynatrace.") к хосту, чтобы осмысленно организовать ваши мониторируемые окружения.
   * Измените режим OneAgent на Infrastructure Monitoring или Discovery вместо Full-Stack Monitoring. Дополнительные сведения см. в [Режимы мониторинга OneAgent](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.").
   * Отключите [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить Log Monitoring, какие сведения он может предоставить, и многое другое.").

   Установщик командной строки OneAgent предоставляет больше параметров для [настройки установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик Linux с параметрами командной строки.").
8. **Run the installer**  
   Вставьте команду в окно терминала и выполните её. Права root нужны только для запуска установки OneAgent. Повышенные привилегии сбрасываются, как только Dynatrace OneAgent развёрнут.

   Если вы используете Ubuntu Server

   ```
   sudo /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh
   ```

   Если вы используете Red Hat Enterprise Linux

   ```
   su -c '/bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh'
   ```

   Если вы запускаете сеанс root

   ```
   /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh
   ```

* Если вы планируете загружать Dynatrace OneAgent напрямую на сервер, учтите, что устаревшие или отсутствующие библиотеки (например, CA-сертификаты или OpenSSL) не позволят установщику выполнить загрузку.
* Dynatrace использует зашифрованные подключения. OpenSSL необходим, чтобы `wget` мог получить доступ к серверу. Установщик также можно скачать, выбрав **Download OneAgent installer** в нижнем колонтитуле страницы и сохранив скрипт установщика в любое удобное место, что полностью исключает необходимость в команде `wget`.

Что происходит во время установки?

Dynatrace OneAgent представляет собой набор специализированных сервисов, настроенных специально для вашего окружения мониторинга. Роль этих сервисов состоит в мониторинге различных аспектов ваших хостов, включая оборудование, операционную систему и процессы приложений.

В процессе установки установщик:

* Устанавливает исполняемый код и библиотеки, используемые Dynatrace OneAgent. Двоичные файлы OneAgent устанавливаются в каталог `/opt/dynatrace/oneagent`, а скрипты запуска создаются в `/etc/init.d` (в системах systemd скрипты запуска создаются в `/etc/systemd/system/`). Один из компонентов OneAgent для Linux, `liboneagentproc.so`, находится в системном каталоге библиотек (`/lib` или `/lib64`, в зависимости от вашей архитектуры) и включается через `/etc/ld.so.preload`.
* Создаёт собственного пользователя (`dtuser`). Этот пользователь создаётся без пароля. Войти под этим пользователем невозможно. В целях безопасности сервисы, которым не требуются права root, выполняются от имени этого пользователя. Однако для установки всё равно нужен доступ root.
* Проверяет глобальные настройки прокси в системе.
* Проверяет наличие подключения к Dynatrace Server или ActiveGate (если вы установили ActiveGate и скачали установщик OneAgent после того, как ActiveGate был подключён к Dynatrace).
* Обнаруживает все приложения, совместимые с SELinux, и соответствующим образом корректирует политику безопасности SELinux.
* Позволяет Dynatrace OneAgent внедрять собственные библиотеки в мониторируемые процессы.
* Изменяет конфигурацию core pattern, чтобы OneAgent мог обнаруживать и сообщать о сбоях процессов. Исходная конфигурация core\_pattern продолжит работать после установки и будет сохранена в `/opt/dynatrace/oneagent/agent/conf/original_core_pattern`, где можно задать собственные настройки core в формате, указанном в [Linux Programmer's Manual](https://man7.org/linux/man-pages/man5/core.5.html).

Сводку изменений, внесённых в вашу систему при установке OneAgent, см. в [Безопасность OneAgent на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Linux").

## Вы на месте!

Отлично, настройка завершена! Теперь можно осмотреться в своём новом окружении мониторинга.

Доступ к окружению мониторинга можно получить через [Cluster Management Console](/managed/managed-cluster/operation/manage-your-monitoring-environments "Узнайте, как создавать, настраивать, открывать, удалять, отключать окружения мониторинга и переключаться между ними.").

![Вы на месте](https://dt-cdn.net/images/arrive-1533-e7eb3573a6.png)

Вы на месте

И последнее: чтобы мониторить ваши процессы, их нужно перезапустить. Перезапустить процессы можно в любое время, даже во время следующего планового периода обслуживания в вашей организации.