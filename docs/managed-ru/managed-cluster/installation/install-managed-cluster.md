---
title: Установка Managed Cluster
source: https://docs.dynatrace.com/managed/managed-cluster/installation/install-managed-cluster
scraped: 2026-05-12T11:06:43.410216
---

# Установка Managed Cluster

# Установка Managed Cluster

* How-to guide
* 7-min read
* Updated on May 08, 2026

Чтобы развернуть Managed Cluster и установить первый узел, выполните следующие шаги.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Проверка требований**](/managed/managed-cluster/installation/install-managed-cluster#review-prerequisites "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Загрузка установщика**](/managed/managed-cluster/installation/install-managed-cluster#download-installer "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Проверка установщика**](/managed/managed-cluster/installation/install-managed-cluster#verify-installer "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Получение SBOM-файла**](/managed/managed-cluster/installation/install-managed-cluster#retrieve-sbom "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Запуск установщика**](/managed/managed-cluster/installation/install-managed-cluster#run-installer "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Финализация**](/managed/managed-cluster/installation/install-managed-cluster#finalize "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")

## Шаг 1. Проверка требований

Убедитесь, что ваша система соответствует указанным [требованиям к аппаратному обеспечению](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.") и [системным требованиям](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.").

Не устанавливайте хранилища данных Dynatrace Managed на сетевые или удалённые диски. Это может привести к проблемам с производительностью и стабильностью.

## Шаг 2. Загрузка установщика

1. Войдите на Linux-машину и перейдите в директорию, куда необходимо установить Dynatrace Managed.
2. Скопируйте команду `wget` для установщика из полученного письма с активацией.
3. Вставьте команду `wget` для установщика в окно терминала. Дождитесь завершения загрузки.

## Шаг 3. Проверка установщика

Файл установщика Dynatrace Managed снабжён цифровой подписью. Совместно с OpenSSL и [корневым сертификатом Dynatrace](https://ca.dynatrace.com/dt-root.cert.pem) файл подписи подтверждает подлинность установщика. Файл подписи имеет то же имя, что и установщик, с расширением `.sig`.

1. Скопируйте команду `wget` для файла подписи установщика из полученного письма с активацией.
2. Вставьте команду `wget` для файла подписи установщика в окно терминала. Дождитесь завершения загрузки.
3. Проверьте подпись файла установщика с помощью следующей команды:

   ```
   openssl cms -inform PEM -binary -verify -CAfile dt-root.cert.pem -in dynatrace-managed-<version>.sh.sig -content dynatrace-managed-<version>.sh > /dev/null
   ```

   Замените `<version>` на версию Dynatrace Managed.
4. При успешной проверке ответом будет `Verification successful`. При неудачной — `Verification failure` с подробностями.

## Шаг 4 (необязательно). Получение Software Bill of Materials

Dynatrace предоставляет [Software Bill of Materials (SBOM)](https://www.dynatrace.com/company/trust-center/customers/reports), содержащий подробную инвентаризацию программных компонентов и зависимостей. SBOM в формате CycloneDX можно извлечь из архива установщика.

1. Для извлечения архива установщика Dynatrace Managed необходимы права root. Используйте `su` или `sudo` для выполнения команды извлечения. Введите одну из следующих команд в директории, куда загружен установочный скрипт.

   Замените `<version>` на версию Dynatrace Managed.

   * Ubuntu Server

     ```
     sudo /bin/sh dynatrace-managed-<version>.sh --extract ARCH
     ```
   * Red Hat Enterprise Linux

     ```
     su -c '/bin/sh dynatrace-managed-<version>.sh --extract ARCH'
     ```
   * Другие дистрибутивы Linux с root-сессией

     ```
     /bin/sh dynatrace-managed-<version>.sh --extract ARCH
     ```
2. В результате извлечения создаётся архивный файл с именем `dynatrace-managed-<version>.tar.gz`. Распакуйте архив следующей командой.

   ```
   tar -xzvf dynatrace-managed-<version>.tar.gz
   ```
3. Команда `tar` создаёт папку с именем `dynatrace-managed-<version>`. Список файлов в папке можно получить следующей командой.

   ```
   ls -l dynatrace-managed-<version>
   ```
4. Папка содержит SBOM в формате CycloneDX с именем файла `dynatrace-managed-sbom.cdx.json`.

## Шаг 5. Запуск установщика

1. Для установки Managed Cluster необходимы права root. Используйте `su` или `sudo` для запуска установочного скрипта. Введите одну из следующих команд в директории, куда загружен установочный скрипт.

   Замените `<version>` на версию Dynatrace Managed.

   * Ubuntu Server

     ```
     sudo /bin/sh dynatrace-managed-<version>.sh
     ```
   * Red Hat Enterprise Linux

     ```
     su -c '/bin/sh dynatrace-managed-<version>.sh'
     ```
   * Другие дистрибутивы Linux с root-сессией

     ```
     /bin/sh dynatrace-managed-<version>.sh
     ```

   Для просмотра списка всех доступных [параметров установки](/managed/managed-cluster/installation/customize-managed-cluster-install "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.") запустите установщик с параметром `--help`.
2. Введите `Accept`, чтобы принять [Условия использования](https://www.dynatrace.com/eula/managed/) Dynatrace Managed. Установка не продолжится до завершения этого шага. Для выхода нажмите `Ctrl+C`.
3. Установщик Managed работает в интерактивном режиме. Он выводит запросы на ввод значений, таких как путь установки и учётная запись пользователя. Для принятия значений по умолчанию нажмите `Enter`. Для переопределения значений введите свои в терминале и нажмите `Enter`.

   Подготовьте лицензионный ключ Dynatrace Managed. Без него завершить установку невозможно.

   #### Настройки по умолчанию

   * Путь установки (бинарные файлы): `/opt/dynatrace-managed`
   * Файлы данных Dynatrace Server: `/var/opt/dynatrace-managed`
   * Системный пользователь, запускающий процессы Dynatrace: `dynatrace`
   * Системная группа, запускающая процессы Dynatrace: `dynatrace`

   #### Обход интерактивного режима

   Для установки с настройками по умолчанию без диалогов запустите установщик с параметром `--install-silent`. Обязательно укажите лицензионный ключ Dynatrace Managed в качестве значения параметра `--license`.

   #### Что происходит в процессе установки

   Managed Cluster — это набор специализированных компонентов, совместно обеспечивающих работу среды мониторинга и обработку данных мониторинга процессов.

   Установщик разворачивает следующие компоненты в директории установки (по умолчанию `/opt/dynatrace-managed`):

   * Предварительно настроенная Java Runtime Environment (настройки операционной системы не затрагиваются). В списке `alternatives` не отображается.
   * Hypercube storage на основе Cassandra
   * Поисковый движок на основе Elasticsearch
   * Dynatrace Server
   * Встроенный ActiveGate

   Установщик также оптимизирует настройки операционной системы:

   * Подкачка отключается (с помощью `swapoff`).  
     Обратите внимание: включение подкачки может привести к нежелательному поведению и не поддерживается.
   * Правила `iptables` `"PREROUTING"` расширены для включения переадресации трафика к Dynatrace Server (через HTTPS на порту 8021). Для просмотра точных правил введите `iptables -L -vt nat` в терминале.
   * Кеш опережающего чтения `readahead` установлен на 512.
   * Лимиты для пользователей изменены глобально (неограниченное заблокированное в памяти адресное пространство, неограниченное адресное пространство, увеличенный лимит числа процессов и открытых файлов). Подробнее в `/etc/security/limits.conf`.
   * Изменено значение `max_map_count`.

   В процессе установки Dynatrace Managed могут быть изменены следующие системные файлы и директории:

   * `/etc/hosts`
   * `/etc/sysctl.conf`
   * `/etc/pam.d/su`
   * `/etc/rc.local`
   * `/etc/security/limits.conf`
   * `/etc/security/limits.d/90-nproc.conf`
   * `/etc/sudoers`
   * `/etc/sudoers.d/`
   * `/etc/init.d/`
   * `/etc/init.d/rc*.d/`
   * `/etc/systemd/system/`

   #### Журналы установки

   Журнал установки Dynatrace Managed находится в директории `/opt/dynatrace-managed/installer/`. Для идентификации нужного файла ориентируйтесь на дату установки в его имени. Например, журнал успешной установки 30 сентября будет называться `20160930-173309-success-install-of-managed-installer.log`.

## Шаг 6. Финализация

1. Скопируйте адрес среды, отображаемый в конце процесса установки. Вставьте его в браузер для завершения установки. Откроется следующая страница.

   ![После установки сервера](https://dt-cdn.net/images/after-server-installation-425-705dc79015.png)

   После установки сервера
2. Задайте имя первой среды мониторинга и создайте учётную запись администратора. Затем выберите **Next**. После входа в систему вы будете перенаправлены в Cluster Management Console. Будет сгенерирован домен по умолчанию, который следует использовать вместо IP-адреса для безопасного HTTPS-подключения.
3. Перейдите в **Environments**, чтобы просмотреть только что созданную среду. Выберите среду, затем **Go to environment**, чтобы открыть веб-интерфейс среды мониторинга. Позже можно [создать дополнительные среды мониторинга](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments.").

## Часто задаваемые вопросы

### Использование системы управления привилегиями вместо sudo

Да, можно использовать `pbrun`, однако необходимо предоставить пользователю Dynatrace разрешение на выполнение `/opt/dtrun/dtrun *`. Укажите пользователя, устанавливающего Dynatrace Managed, и команду, заменяющую `sudo`. Обратите внимание: `<version>` обозначает номер версии Dynatrace Managed.

```
/bin/sh dynatrace-managed-<version>.sh --system-user dynatrace:dynatrace --sudo-cmd  "/usr/bin/pbrun \$CMD"
```

В целях технического обслуживания добавьте следующие пути к скриптам в конфигурацию системы управления привилегиями:

* `/opt/dynatrace-managed/uninstall-dynatrace.sh`
* `/opt/dynatrace-managed/launcher/*`
* `/opt/dynatrace-managed/utils/*`

Для остановки всех процессов Dynatrace Managed на узле выполните следующую команду:

```
pbrun /opt/dynatrace-managed/launcher/dynatrace.sh stop
```

Не удаляйте и не перезаписывайте `dtrun`, так как он необходим для процедур установки и обновления. Установщик вызывает `dtrun` без аргументов для проверки наличия у пользователя прав администратора, а при штатной работе Dynatrace вызывает `dtrun` с аргументами для выполнения команд.