---
title: Установка Cluster ActiveGate
source: https://docs.dynatrace.com/managed/managed-cluster/installation/install-cluster-activegate
scraped: 2026-05-12T11:06:45.807451
---

# Установка Cluster ActiveGate

# Установка Cluster ActiveGate

* How-to guide
* 4-min read
* Updated on May 08, 2026

Для установки Cluster ActiveGate на Linux или Windows следуйте приведённым ниже шагам.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Проверка требований**](/managed/managed-cluster/installation/install-cluster-activegate#review-requirements "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Загрузка установщика**](/managed/managed-cluster/installation/install-cluster-activegate#download-installer "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Запуск установщика**](/managed/managed-cluster/installation/install-cluster-activegate#run-installer "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Финализация**](/managed/managed-cluster/installation/install-cluster-activegate#finalize "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.")

## Шаг 1. Проверка требований

Перед установкой определите назначение ActiveGate и ознакомьтесь с соответствующими требованиями:

* **Маршрутизация трафика OneAgent** — см. [требования для маршрутизации/мониторинга](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.").
* **Запуск Synthetic-мониторов из приватного местоположения** — ActiveGate с поддержкой Synthetic поддерживает ограниченный набор операционных систем и предъявляет более высокие [требования к аппаратному обеспечению и системе](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations"), чем маршрутизирующие ActiveGate.

В большинстве случаев ActiveGate можно установить в любое время после установки OneAgent. Однако в некоторых случаях порядок установки имеет значение, поскольку установщику OneAgent необходимо знать об ActiveGate до установки OneAgent.

Если OneAgent уже установлен

В таком случае сначала установите ActiveGate, а затем загрузите установщик OneAgent. Например, если вы загрузили установщик OneAgent и использовали его для установки Dynatrace в DMZ или сетевом сегменте без доступа к интернету, а затем установили ActiveGate, вам потребуется повторно загрузить и установить OneAgent, чтобы установщик обеспечил правильную настройку взаимодействия между OneAgent и ActiveGate. Это необходимо, поскольку OneAgent должен быть автоматически настроен в процессе установки для подключения к отслеживаемой среде и отправки данных мониторинга в кластер Dynatrace через ActiveGate.

## Шаг 2. Загрузка установщика

1. Войдите в **Cluster Management Console**.
2. Перейдите в **Home**, выберите кнопку **[…]** и нажмите **Add new Cluster ActiveGate**.
3. Выберите **Windows** или **Linux** в зависимости от вашей операционной системы, затем укажите назначение:

   * **Route traffic** — маршрутизирует трафик OneAgent, публичного Synthetic, мобильный трафик, Real User Monitoring и REST API.
   * **Run synthetic monitors from a private location** — запускает исключительно Synthetic-мониторы. Установка ActiveGate с этим назначением отключает все другие функции ActiveGate, включая взаимодействие с OneAgent.

   Выбранное назначение автоматически устанавливает соответствующий параметр установщика (`--enable-synthetic` на Linux, `ENABLE_SYNTHETIC=true` на Windows).
4. Загрузите установщик или скопируйте команду установки для вашей платформы.

   Windows

   Linux

   Выберите назначение ActiveGate и нажмите **Download installer** для загрузки на целевой хост.

   Выберите назначение ActiveGate, скопируйте команду `wget` из поля **Run this command on the target host** и вставьте её в терминал. Копируйте команду непосредственно из вашего кластера — она содержит основной адрес вашего кластера.

## Шаг 3. Запуск установщика

Параметр установки (определяемый выбранным назначением ActiveGate) автоматически устанавливается для команды запуска установщика. Убедитесь, что используете команду, отображаемую в веб-интерфейсе Dynatrace, которая отражает выбранное назначение ActiveGate.

Windows

Linux

Запустите установщик на целевом хосте. Если выбрано назначение **Run synthetic monitors from a private location**, скопируйте команду установочного скрипта из шага **Run the installer via Command Prompt** и вставьте её в терминал.

Скопируйте команду установочного скрипта из шага **Run the installer script with root rights** и выполните её в терминале.

### Настройка установки

К команде установки можно добавлять дополнительные [параметры](/managed/managed-cluster/installation/customize-managed-cluster-install "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates."). Например, для отключения самомониторинг-OneAgent:

```
[root@localhost]# /bin/bash Dynatrace-ActiveGate-Linux-x86-1.0.0.sh --install-agent off
```

### FIPS-совместимый режим

Только Linux

ActiveGate версии 1.315+

Для установки Cluster ActiveGate в FIPS-совместимом режиме см. раздел [FIPS-совместимый режим](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#fips-compliant-mode "Learn about the command-line parameters that you can use with ActiveGate on Linux.") с инструкциями по предварительным требованиям и настройке.

### Параметры установки по умолчанию

Сведения о директориях по умолчанию и других настройках см. в разделе [Параметры ActiveGate по умолчанию для Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Learn about the default settings with which ActiveGate is installed on Linux").

## Шаг 4. Финализация

После подключения Cluster ActiveGate к Dynatrace установка завершается, и Dynatrace перенастраивает OneAgent для отправки данных мониторинга через Cluster ActiveGate.

* Для проверки установки выберите **Show deployment status** и перейдите на вкладку **Dynatrace ActiveGates**.
* Сведения по устранению неполадок см. в разделе [Устранение неполадок ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").