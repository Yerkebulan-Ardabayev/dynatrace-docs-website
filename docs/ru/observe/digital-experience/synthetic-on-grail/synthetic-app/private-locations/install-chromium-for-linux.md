---
title: Установка и обновление Chromium для Linux
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux
scraped: 2026-03-06T21:31:26.009069
---

Если [управляемая установка через веб-интерфейс](active-gate-for-private-locations-install.md#ui-guided-browser-installation "Узнайте, как установить ActiveGate с поддержкой Synthetic.") завершается неудачей или вы предпочитаете самостоятельно подготовить хост для движка Synthetic, вы можете установить Chromium и другие зависимости [вручную](#manual) или из [пользовательского репозитория](#custom-repo).

## Установка браузера и зависимостей вручную из S3

Этот раздел не актуален для локаций без браузера.

Amazon Linux 2023, Ubuntu и Oracle Linux 9

Amazon Linux 2023, Ubuntu и Oracle Linux 9 используют Chrome for Testing вместо Chromium. Для ручной установки Chrome for Testing на этих операционных системах см. раздел [Amazon Linux 2023, Ubuntu и Oracle Linux 9 (Chrome for Testing)](#chrome-for-testing).

Убедитесь, что вы можете подключиться к `https://synthetic-packages.s3.amazonaws.com` для доступа к пакетам браузера. По соображениям безопасности публичный доступ к S3-корзине включён только для определённых файлов; попытка получить доступ к чему-либо другому приведёт к ошибке 403.

Также см. раздел [Установка браузера из пользовательского репозитория](#custom-repo) ниже.

Подробнее об [обновлении браузера вручную](../../../synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations.md#browser-manual "Анализ и управление использованием ресурсов в частных локациях Synthetic.") читайте в разделе [Управление частными локациями Synthetic](../../../synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations.md "Анализ и управление использованием ресурсов в частных локациях Synthetic."). Мы настоятельно рекомендуем поддерживать актуальность версий ActiveGate с поддержкой Synthetic на базе Linux и браузера — Dynatrace поддерживает версии браузера, которые отстают не более чем на две версии от [последней поддерживаемой Dynatrace версии](../../../synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic.md#browser-linux "Поддерживаемые операционные системы, версии Chromium и аппаратные требования для запуска синтетических мониторов из частных локаций") для конкретного выпуска ActiveGate.

### Ubuntu Server 20.04 и 22.04

Этот раздел актуален только для выпусков 1.329 и более ранних.

1. Установите зависимости движка Synthetic:

   Зависимости движка Synthetic:

   ```
   sudo apt-get update && sudo apt-get -y install xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable libnss3-tools auditd
   ```

   Зависимости Chromium:

   ```
   sudo apt-get -y install fonts-dejavu-core
   ```

   ```
   sudo snap install gnome-3-38-2004 gtk-common-themes
   ```
2. Загрузите и установите Chromium.

   * Загрузите архив snap-пакета (Ubuntu Server 20.04 и 22.04). Это безопасный и проверенный архив, размещённый Dynatrace.

     ActiveGate версии 1.329

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-142.0.7444.175-3313.tgz
     ```

     ActiveGate версии 1.327

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-141.0.7390.122-3285.tgz
     ```

     ActiveGate версии 1.325

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-140.0.7339.185-3251.tgz
     ```

     ActiveGate версии 1.323

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-139.0.7258.138-3235.tgz
     ```

     ActiveGate версии 1.321

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-138.0.7204.157-3203.tgz
     ```

     ActiveGate версии 1.319

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-138.0.7204.100-3199.tgz
     ```

     ActiveGate версии 1.317

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-137.0.7151.103-3169.tgz
     ```

     ActiveGate версии 1.315

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-136.0.7103.59-3121.tgz
     ```

     ActiveGate версии 1.313

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-135.0.7049.95-3110.tgz
     ```

     ActiveGate версии 1.311

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-134.0.6998.35-3060.tgz
     ```

     ActiveGate версии 1.309

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-132.0.6834.159-3036.tgz
     ```

     ActiveGate версии 1.307

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-131.0.6778.85-3002.tgz
     ```

     Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписей, хранящихся вместе с архивами пакетов.
   * Распакуйте установочные пакеты. Перейдите в каталог, в который вы сохранили архив, и выполните следующую команду:

     ```
     mkdir /tmp/chromium ; tar xzf chromium.tgz -C /tmp/chromium
     ```

     Это создаст каталог `/tmp/chromium` и распакует в него пакеты.
   * Установите распакованные пакеты.

     ```
     sudo chown -R root:root /tmp/snap-private-tmp
     ```

     ```
     sudo snap ack /tmp/chromium/chromium.assert
     ```

     ```
     sudo snap install --devmode /tmp/chromium/chromium.snap
     ```

     Замените `dtuserag` на имена пользователя и группы сервиса ActiveGate, если они отличаются от значений по умолчанию.

     ```
     sudo chown -R dtuserag:dtuserag /tmp/snap-private-tmp
     ```

     Это устанавливает все пакеты, распакованные в каталог `/tmp/chromium/`. После успешной установки Chromium можно удалить каталог `/tmp/chromium/` и загруженный архив `chromium.tgz`.
3. После выполнения всех зависимостей запустите установщик ActiveGate с правами root с параметром `--enable-synthetic`, установленным в `manual`. Например:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

Вы можете [проверить подлинность пакетов](../private-locations.md#verify "Узнайте, как управлять частными локациями в приложении Synthetic.") с помощью файлов подписей, хранящихся вместе с архивами пакетов.

### Red Hat Enterprise Linux, Oracle Linux 8 и Rocky Linux

* Разработка Chromium для Red Hat/CentOS 7 и Amazon Linux 2 остановилась на версии 126.

  + Поскольку Red Hat Enterprise Linux 7 достиг [окончания поддержки Maintenance](https://dt-url.net/af03uea) 30 июня 2024 г., все его пакеты были заархивированы. Это означает, что поиск необходимых зависимостей для обновления может оказаться невозможным. Подробнее см. в разделе [Статус Red Hat Enterprise Linux 7](https://dt-url.net/e623zr1)
* Установка Chromium при необходимости использования прокси для доступа в интернет.

  + Если вам нужно загрузить и установить Chromium, а ваша система требует прокси для доступа в интернет, следует настроить `curl` для использования нужного прокси. Укажите данные прокси и порта, выполнив команды, как в этом примере:

    ```
    vi /root/.curlrc


    proxy=http://proxy.example.com:8080
    ```

1. Настройте репозитории и установите зависимости.

   Red Hat 7

   Red Hat 8

   Red Hat 9

   CentOS

   Oracle Linux 8

   Amazon Linux 2

   Rocky Linux 8

   Rocky Linux 9

   Устаревшая операционная система

   ActiveGate версии 1.305 является последним ActiveGate с поддержкой Synthetic для Red Hat 7.

   * Зарегистрируйте экземпляр Red Hat.

     ```
     sudo subscription-manager register --auto-attach
     ```
   * Включите репозитории Red Hat `Extras` и `Optional`, а также `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo subscription-manager repos --enable rhel-7-server-extras-rpms


     sudo subscription-manager repos --enable rhel-7-server-optional-rpms


     sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
     ```
   * Установите зависимости движка Synthetic.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая операционная система

   ActiveGate версии 1.325 является последним ActiveGate с поддержкой Synthetic для Red Hat 8.

   * Зарегистрируйте экземпляр Red Hat.

     ```
     sudo subscription-manager register --auto-attach
     ```
   * Включите репозитории Red Hat `Extras` и `Optional`, а также `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo subscription-manager repos --enable rhel-8-for-x86_64-baseos-rpms


     sudo subscription-manager repos --enable rhel-8-for-x86_64-appstream-rpms


     sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
     ```
   * Установите зависимости движка Synthetic.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   * Зарегистрируйте экземпляр Red Hat.

     ```
     sudo subscription-manager register --auto-attach
     ```
   * Включите репозитории Red Hat `Extras` и `Optional`, а также `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo subscription-manager repos --enable rhel-9-for-x86_64-baseos-rpms


     sudo subscription-manager repos --enable rhel-9-for-x86_64-appstream-rpms


     sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
     ```
   * Установите зависимости движка Synthetic.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая операционная система

   ActiveGate версии 1.305 является последним ActiveGate с поддержкой Synthetic для CentOS.

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo yum install epel-release
     ```
   * Установите зависимости движка Synthetic.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая операционная система

   ActiveGate версии 1.325 является последним ActiveGate с поддержкой Synthetic для Oracle Linux 8.

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo yum install -y oracle-epel-release-el8
     ```
   * Установите зависимости движка Synthetic.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая операционная система

   ActiveGate версии 1.307 является последним ActiveGate с поддержкой Synthetic для Amazon Linux 2.

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo amazon-linux-extras install epel
     ```
   * Установите зависимости движка Synthetic.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая операционная система

   ActiveGate версии 1.325 является последним ActiveGate с поддержкой Synthetic для Rocky Linux 8.

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo yum install epel-release
     ```
   * Установите зависимости движка Synthetic.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo yum install epel-release
     ```
   * Установите зависимости движка Synthetic.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```
2. Загрузите и установите Chromium.

   * Загрузите архив rpm-пакета. Это безопасный и проверенный архив, размещённый Dynatrace.

     ActiveGate версии 1.331

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-143.0.7499.192-1.el9.tgz
     ```

     ActiveGate версии 1.329

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-142.0.7444.175-2.el9.tgz
     ```

     ActiveGate версии 1.327

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-141.0.7390.122-1.el9.tgz
     ```

     ActiveGate версии 1.325

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-140.0.7339.185-1.el9.tgz
     ```

     ActiveGate версии 1.323

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-139.0.7258.138-1.el9.tgz
     ```

     ActiveGate версии 1.321

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-138.0.7204.157-1.el9.tgz
     ```

     ActiveGate версии 1.319

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-138.0.7204.100-1.el9.tgz
     ```

     ActiveGate версии 1.317

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-137.0.7151.103-1.el9.tgz
     ```

     ActiveGate версии 1.315

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-136.0.7103.59-1.el9.tgz
     ```

     ActiveGate версии 1.313

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-135.0.7049.95-1.el9.tgz
     ```

     ActiveGate версии 1.311

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-134.0.6998.35-1.el9.tgz
     ```

     ActiveGate версии 1.309

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-132.0.6834.159-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-132.0.6834.159-1.el9.tgz
     ```

     ActiveGate версии 1.307

     ##### Amazon Linux 2

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-126.0.6478.114-1.el7.tgz
     ```

     ##### Red Hat Enterprise Linux/Oracle/Rocky Linux 8

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-131.0.6778.204-1.el8.tgz
     ```

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-131.0.6778.204-1.el9.tgz
     ```

     Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписей, хранящихся вместе с архивами пакетов.
   * Распакуйте установочные пакеты. Перейдите в каталог, в который вы сохранили архив, и выполните следующую команду:

     ```
     mkdir /tmp/chromium ; tar xzf chromium.tgz -C /tmp/chromium
     ```

     Это создаст каталог `/tmp/chromium` и распакует в него пакеты.
   * Установите распакованные пакеты.

     ```
     sudo yum install -y /tmp/chromium/*.rpm
     ```

     Это устанавливает все пакеты, распакованные в каталог `/tmp/chromium/`. После успешной установки Chromium можно удалить каталог `/tmp/chromium/` и загруженный архив `chromium.tgz`.
3. Отключите автоматическое обновление пакетов Chromium:

   ```
   sudo yum -y install yum-plugin-versionlock


   sudo yum versionlock chromium


   sudo yum versionlock chromium-common
   ```
4. Необязательно Установите шрифты TrueType для нелатинских символов:

   ```
   sudo yum install dejavu-fonts-common.noarch dejavu-sans-fonts.noarch
   ```
5. После выполнения всех зависимостей запустите установщик ActiveGate с правами root с параметром `--enable-synthetic`, установленным в `manual`. Например:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

Вы можете [проверить подлинность пакетов](../private-locations.md#verify "Узнайте, как управлять частными локациями в приложении Synthetic.") с помощью файлов подписей, хранящихся вместе с архивами пакетов.

### Amazon Linux 2023, Ubuntu и Oracle Linux 9 (Chrome for Testing)

В отличие от Chromium на других дистрибутивах, обновления Chrome for Testing не используют менеджеры пакетов. Вы управляете двоичными файлами Chrome вручную, тогда как зависимостями управляет системный менеджер пакетов.

Chrome for Testing на Ubuntu Server 20.04 и 22.04 поддерживается начиная с версии 1.331

1. Настройте репозитории и установите зависимости.

   Ubuntu

   Amazon Linux 2023

   Oracle Linux 9

   * Установите зависимости движка Synthetic:

     ```
     sudo apt-get update && sudo apt-get -y install xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable libnss3-tools auditd unzip
     ```
   * Установите зависимости Chrome for Testing:

     ```
     sudo apt-get -y install libasound2t64 libatk-bridge2.0-0t64 libatk1.0-0t64 libcairo2 libcups2t64 libgbm1 libnspr4 libnss3 libpango-1.0-0 libxcomposite1 libxdamage1 libxfixes3 libxkbcommon0 libxrandr2
     ```

   * Включите `EPEL` (Extra Packages for Enterprise Linux):

     ```
     sudo yum install -y epel-release
     ```
   * Установите зависимости движка Synthetic:

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools unzip
     ```
   * Установите зависимости Chrome for Testing:

     ```
     sudo yum install -y alsa-lib at-spi2-atk atk cairo cups-libs dbus-libs libXcomposite libXdamage libXrandr libxkbcommon mesa-libgbm nspr nss pango
     ```

   * Включите `EPEL` (Extra Packages for Enterprise Linux):

     ```
     sudo yum install -y oracle-epel-release-el9
     ```
   * Установите зависимости движка Synthetic:

     ```
     sudo yum install -y xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools unzip
     ```
   * Установите зависимости Chrome for Testing:

     ```
     sudo yum install -y alsa-lib at-spi2-atk atk cairo cups-libs libXcomposite libXdamage libXrandr libxkbcommon mesa-libgbm nspr nss pango
     ```
2. Загрузите и настройте Chrome for Testing.

   * Создайте каталог Chrome for Testing:

     ```
     sudo mkdir -p /usr/lib/chrome_for_testing
     ```
   * Загрузите архив пакета Chrome for Testing во временное расположение. Это безопасный и проверенный архив, размещённый Dynatrace.

     ActiveGate версии 1.331

     ```
     curl --output /tmp/chrome.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip
     ```

     ActiveGate версии 1.329

     ```
     curl --output /tmp/chrome.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-142.0.7444.175.zip
     ```

     ActiveGate версии 1.327

     ```
     curl --output /tmp/chrome.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-141.0.7390.122.zip
     ```

     Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписей, хранящихся вместе с архивами пакетов.
   * Распакуйте установочный пакет и очистите:

     ```
     sudo unzip /tmp/chrome.zip -d /usr/lib/chrome_for_testing


     rm /tmp/chrome.zip
     ```

     Это создаёт каталог `chrome-linux64` внутри `/usr/lib/chrome_for_testing` и распаковывает в него двоичный файл Chrome и вспомогательные файлы.
   * Проверьте Chrome for Testing, проверив версию:

     ```
     /usr/lib/chrome_for_testing/chrome-linux64/chrome --version
     ```

     В выводе команды должна отображаться загруженная вами версия Chrome.
3. После выполнения всех зависимостей запустите установщик ActiveGate с правами root. Установщик автоматически обнаружит и проверит Chrome for Testing. Например:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

* Пользовательский каталог Chrome for Testing: если вы хотите использовать другой каталог вместо `/usr/lib/chrome_for_testing` по умолчанию, укажите его, задав свойство `synthetic_chrome_for_testing_path` в файле `custom.properties` после установки. Новый каталог будет использоваться после обновления модуля Synthetic.
* Файлы Chrome for Testing сохраняются при удалении ActiveGate. При удалении ActiveGate каталог Chrome for Testing и его содержимое останутся в системе и могут быть повторно использованы при переустановке.
* Вы можете [проверить подлинность пакетов](../private-locations.md#verify "Узнайте, как управлять частными локациями в приложении Synthetic.") с помощью файлов подписей, хранящихся вместе с архивами пакетов.

## Обновление браузера вручную из S3

Если у вас автономная среда или вы установили ActiveGate вручную для управления зависимостями или из-за ограниченного доступа к Amazon S3, вам необходимо обновлять браузер и зависимости вручную.

Вам необходимо обновлять браузер вручную для каждого ActiveGate, и процесс незначительно различается в зависимости от операционной системы. Обратите внимание, что ручное обновление браузера применяется только к ActiveGate на базе Linux; на ActiveGate на базе Windows браузер обновляется автоматически во время обновлений движка Synthetic.

Предварительные требования:

* Убедитесь, что [**Enable Chrome(-ium) auto-update**](../private-locations.md#browser-autoupdate "Узнайте, как управлять частными локациями в приложении Synthetic.") отключено для вашей частной локации. Если вы отключили автообновление для локации, вам нужно обновлять браузер вручную на каждом ActiveGate, назначенном этой локации.
* Убедитесь, что вы можете подключиться к `https://synthetic-packages.s3.amazonaws.com` для доступа к пакетам браузера.

* Движок Synthetic будет использовать новую версию браузера после завершения обновления — обратите внимание, что статус обновляется раз в час, поэтому обновление версии браузера, отображаемой для вашего ActiveGate в **Deployment Status**, может занять до часа.
* Мы настоятельно рекомендуем поддерживать актуальность версий ActiveGate с поддержкой Synthetic на базе Linux и браузера — Dynatrace поддерживает версии браузера, которые отстают не более чем на две версии от [последней поддерживаемой Dynatrace версии](requirements-for-private-synthetic.md#browser-linux "Проверьте системные и аппаратные требования для частных локаций Synthetic.") для конкретного выпуска ActiveGate.
* Мы настоятельно рекомендуем обновлять все ActiveGate в локации до одной и той же версии.
* Также см. раздел [Автообновление браузера из пользовательского репозитория](install-chromium-for-linux.md#autoupdate-custom-repo "Узнайте, как установить Chromium для Linux вручную и из пользовательских репозиториев.").

Начиная с ActiveGate 1.331, на Ubuntu Server 20.04 и 22.04 используется Chrome for Testing. Snap-дистрибутив Chromium больше не поддерживается.
Если вы используете автоматизацию для обновления браузера, переведите её на использование Chrome for Testing. Подробности см. в [руководстве сообщества](https://dt-url.net/il0363p).

Ubuntu (snap)

Red Hat Enterprise Linux и CentOS

Amazon Linux 2023, Ubuntu и Oracle Linux 9 (Chrome for Testing)

Этот раздел актуален только для выпусков 1.329 и более ранних для Ubuntu Server 20.04 и 22.04.

1. Если версии вашего ActiveGate и Chromium устарели или не обновлялись несколько выпусков, просмотрите зависимости движка Synthetic и Chromium и при необходимости переустановите их. См. [инструкции по ручной установке для Ubuntu Server](install-chromium-for-linux.md#ubuntu "Узнайте, как установить Chromium для Linux вручную и из пользовательских репозиториев.").
2. Загрузите архив snap-пакета (Ubuntu Server 20.04 и 22.04). Это безопасный и проверенный архив, размещённый Dynatrace по адресу `https://synthetic-packages.s3.amazonaws.com`. Обязательно используйте конкретную команду, указанную для вашей версии ActiveGate и Ubuntu Server, в [инструкциях по ручной установке для Ubuntu Server](install-chromium-for-linux.md#ubuntu "Узнайте, как установить Chromium для Linux вручную и из пользовательских репозиториев.").
3. Распакуйте и установите загруженные пакеты. Обязательно используйте правильную команду установки для вашей версии Ubuntu Server (см. [инструкции по ручной установке для Ubuntu Server](install-chromium-for-linux.md#ubuntu "Узнайте, как установить Chromium для Linux вручную и из пользовательских репозиториев.")).
4. Проверьте обновление Chromium, выполнив следующую команду из каталога установки по умолчанию. В выводе команды должна отображаться установленная вами версия Chromium.

   ```
   /opt/dynatrace/synthetic/browser --version
   ```

Ручное обновление Chromium выполняется одинаково на Red Hat Enterprise Linux и CentOS; единственное отличие — загружаемые пакеты для Red Hat/CentOS версии 7 и версии 8.

Если вы установили Chromium вручную, при обновлении не нужно регистрировать экземпляр Red Hat в менеджере подписок или включать репозитории Red Hat или пакеты EPEL.

1. Если версии вашего ActiveGate и Chromium давно не обновлялись, возможно, потребуется повторно установить зависимости движка Synthetic. См. [инструкции по ручной установке для Red Hat Enterprise Linux и CentOS](#redhat).
2. Загрузите архив rpm-пакета. Это безопасный и проверенный архив, размещённый Dynatrace по адресу `https://synthetic-packages.s3.amazonaws.com`. Обязательно используйте конкретную команду, указанную для вашей версии ActiveGate и ОС, в [инструкциях по ручной установке для Red Hat Enterprise Linux и CentOS](#redhat).
3. Распакуйте и установите загруженные пакеты. См. [инструкции по ручной установке для Red Hat Enterprise Linux и CentOS](#redhat).
4. При необходимости отключите автоматическое обновление пакетов Chromium. Обратите внимание, что для Red Hat Enterprise Linux и CentOS блокировка пакетов, выполненная однажды, сохраняется при всех последующих обновлениях.

   ```
   sudo yum -y install yum-plugin-versionlock


   sudo yum versionlock chromium


   sudo yum versionlock chromium-common
   ```
5. Проверьте обновление Chromium, выполнив следующую команду из каталога установки по умолчанию. В выводе команды должна отображаться установленная вами версия Chromium.

   ```
   /opt/dynatrace/synthetic/browser --version
   ```

Управление Chrome for Testing отличается от управления Chromium. Для обновления вручную загрузите новую версию и распакуйте её в каталог Chrome for Testing.

В отличие от Chromium на других дистрибутивах, обновления Chrome for Testing не используют менеджеры пакетов. Вы управляете двоичными файлами Chrome вручную, тогда как зависимостями управляет системный менеджер пакетов.

Ubuntu Server 20.04 и 22.04

При переходе с Chromium snap сначала обновите ActiveGate, затем установите Chrome for Testing и при необходимости удалите файлы Chromium snap.

1. Если версии вашего ActiveGate и Chrome for Testing давно не обновлялись, возможно, потребуется проверить и повторно установить зависимости движка Synthetic и Chrome for Testing. См. [инструкции по ручной установке для Chrome for Testing](#chrome-for-testing).
2. Загрузите архив пакета Chrome for Testing во временное расположение. Это безопасный и проверенный архив, размещённый Dynatrace по адресу `https://synthetic-packages.s3.amazonaws.com`. Обязательно используйте конкретную команду, указанную для вашей версии ActiveGate, в [инструкциях по ручной установке для Chrome for Testing](#chrome-for-testing), но измените выходной путь на `/tmp/chrome.zip`.
3. Удалите старый каталог Chrome for Testing, распакуйте новую версию и очистите:

   ```
   sudo rm -rf /usr/lib/chrome_for_testing/chrome-linux64


   sudo unzip /tmp/chrome.zip -d /usr/lib/chrome_for_testing


   rm /tmp/chrome.zip
   ```

   Если вы настроили пользовательский каталог Chrome for Testing через свойство `synthetic_chrome_for_testing_path` в `custom.properties`, замените `/usr/lib/chrome_for_testing` на ваш пользовательский путь в приведённых выше командах.
4. Проверьте обновление Chrome for Testing, выполнив следующую команду. В выводе команды должна отображаться установленная вами версия Chrome.

   ```
   /usr/lib/chrome_for_testing/chrome-linux64/chrome --version
   ```

   Движок Synthetic немедленно начнёт использовать новую версию Chrome for Testing. Обратите внимание, что статус обновляется раз в час, поэтому обновление версии Chrome, отображаемой для вашего ActiveGate в **Deployment Status**, может занять до часа.

## Установка браузера из пользовательского репозитория

ActiveGate версии 1.243+ В дополнение к [управляемой установке ActiveGate через веб-интерфейс](active-gate-for-private-locations-install.md "Узнайте, как установить ActiveGate с поддержкой Synthetic.") и [ручной установке браузера и зависимостей](#manual) вы также можете **установить ActiveGate, указав на пользовательский локальный репозиторий для компонентов браузера**. Поскольку этот репозиторий является HTTP-сервером, который вы размещаете в своей сети, преимущество этого метода состоит в том, что он может использоваться в средах с доступом только к интранету или ограниченным сетевым доступом.

Этот метод установки браузера в целом состоит из:

* Загрузки необходимых архивов пакетов deb, snap или rpm, размещённых Dynatrace, и соответствующих файлов подписи.
* Установки и запуска локально размещённого веб-сервера, на котором находятся загруженные компоненты браузера.
* Загрузки и запуска установщика ActiveGate на целевом хосте с переменной среды, указывающей на расположение пользовательского репозитория на HTTP-сервере.

* Пользовательский репозиторий браузера может использоваться только для компонентов браузера, но не для их зависимостей. Установка браузера из пользовательского репозитория будет работать только в том случае, если все зависимости были разрешены до установки.
* Пользовательские репозитории можно использовать только для **установки и автообновления браузера** — подробнее см. в разделе [Автообновление браузера из пользовательского репозитория](install-chromium-for-linux.md#autoupdate-custom-repo "Узнайте, как установить Chromium для Linux вручную и из пользовательских репозиториев.").

1. Загрузите компоненты браузера — архив пакета и файл подписи — из безопасного и проверенного архива, размещённого Dynatrace. Ссылки на последние поддерживаемые и предоставляемые версии браузера см. в разделе [Требования для частных локаций Synthetic](requirements-for-private-synthetic.md "Проверьте системные и аппаратные требования для частных локаций Synthetic.").

   Мы рекомендуем поддерживать актуальность версий ActiveGate с поддержкой Synthetic на базе Linux и браузера; выбирайте последнюю предоставляемую версию браузера для ActiveGate.

   Например, для ActiveGate версии 1.331 на Ubuntu 24 требуются следующие файлы:

   * Архив пакета — `https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip`
   * Файл подписи — `https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip.sig`

   Соответствующие команды загрузки:

   ```
   curl -o chrome-for-testing-linux64-143.0.7499.192.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip
   ```

   ```
   curl -o chrome-for-testing-linux64-143.0.7499.192.zip.sig https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip.sig
   ```
2. Установите веб-сервер по вашему выбору и создайте каталог, например `chromium-repo`, для предоставления компонентов Chromium хосту ActiveGate. Скопируйте загруженные компоненты браузера в этот каталог.
3. Загрузите установщик ActiveGate из Dynatrace Hub.
4. Разрешите все зависимости и включите репозитории по мере необходимости, как показано в разделе [Установка браузера и зависимостей вручную из S3](#manual) выше. Пользовательский репозиторий можно использовать только для пакетов браузера, но не для их зависимостей.
5. Установите ActiveGate с включённым модулем Synthetic (`--enable-synthetic`) и переменной среды `DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO`, указывающей на расположение пользовательского репозитория (`https://172.18.0.100/chromium-repo` в данном примере).

   ```
   sudo DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO=http://172.18.0.100:8000/chromium-repo  /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic
   ```

   Вы можете использовать имя хоста HTTP-сервера вместо IP-адреса при условии, что хост ActiveGate может разрешить это имя хоста.

После установки браузера таким образом из пользовательского репозитория его можно только автообновлять. Подробнее и об альтернативах обновления см. в разделе [Автообновление браузера из пользовательского репозитория в разделе «Управление частными локациями Synthetic»](../../../synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations.md#autoupdate-custom-repo "Анализ и управление использованием ресурсов в частных локациях Synthetic.").

## Автообновление браузера из пользовательского репозитория

Если вы включили [пользовательский локальный репозиторий для установки браузера](#custom-repo), браузер можно только автообновлять. Следуйте этой процедуре для автообновления браузера через тот же пользовательский репозиторий.

1. После установки ActiveGate укажите пользовательский репозиторий ActiveGate в [разделе `[synthetic]` файла `custom.properties`](../../../../../ingest-from/dynatrace-activegate/configuration/configure-activegate.md#synth_mod "Узнайте, какие свойства ActiveGate можно настроить в соответствии с вашими потребностями и требованиями.") в каталоге `/var/lib/dynatrace/gateway/config`. Это обеспечивает автоматическое обновление браузера из пользовательского репозитория при ручных или автоматических обновлениях движка Synthetic.

   ```
   [synthetic]


   chromium_repo = https://172.18.0.100/chromium-repo
   ```
2. Включите [**Enable Chrome(-ium) auto-update**](../private-locations.md#browser-autoupdate "Узнайте, как управлять частными локациями в приложении Synthetic.") для вашей частной локации.

   Обратите внимание, что параметр автообновления браузера в пользовательском интерфейсе применяется ко всем ActiveGate, назначенным вашей частной локации.
3. Убедитесь, что компоненты браузера, необходимые для обновления, доступны в расположении пользовательского репозитория. После этого браузер будет автоматически обновляться из пользовательского репозитория при обновлениях ActiveGate и движка Synthetic.

Параметр автообновления браузера

Если вы не укажете пользовательский репозиторий в `custom.properties`, браузер будет загружаться и обновляться из S3 при ручном или автоматическом обновлении ActiveGate и движка Synthetic.

## Пользовательская версия браузера

Вы можете установить пользовательскую версию браузера, то есть переопределить версию браузера, которую ищет установщик ActiveGate. Это применимо для ручной установки ActiveGate, как описано в разделе [Установка браузера через S3](#manual) или через [пользовательский репозиторий](#custom-repo).

В этой команде для ручной установки ActiveGate через S3 переменная среды указывает на явный номер версии браузера `143.0.7499.192`, который является частью архива пакета Chrome for Testing.

```
sudo /bin/bash -c "export DYNATRACE_SYNTHETIC_EXPLICIT_CHROMIUM_VERSION=143.0.7499.192; /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic"
```

Эта команда выполняет поиск версии браузера `143.0.7499.192` в пользовательском репозитории `https://172.18.0.100/chromium-repo`.

```
sudo DYNATRACE_SYNTHETIC_EXPLICIT_CHROMIUM_VERSION=143.0.7499.192 DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO=http://172.18.0.100:8000/chromium-repo  /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic
```
