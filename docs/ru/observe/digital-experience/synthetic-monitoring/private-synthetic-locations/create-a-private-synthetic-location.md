---
title: Создание частной Synthetic-локации
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location
scraped: 2026-03-06T21:24:42.801902
---

# Создание частной Synthetic-локации

# Создание частной Synthetic-локации

* Classic
* Практическое руководство
* Чтение: 24 мин
* Обновлено 11 февраля 2026 г.

Вы можете запускать синтетические мониторы Dynatrace из частной Synthetic-локации — локации в вашей частной сетевой инфраструктуре, где устанавливается один или несколько экземпляров Synthetic-совместимого ActiveGate.

С мониторами, запускаемыми из частной локации, вы можете перенести возможности тестирования, доступные в публичных локациях, прямо в вашу среду. С частными локациями вы можете:

* Измерять производительность и доступность внутренних веб-страниц.
* Измерять сложные внутренние приложения с помощью браузерных clickpath-сценариев.
* Измерять внешние ресурсы с помощью синтетических мониторов, запускаемых из внутренних локаций.
* Отслеживать API — как внутренние, так и внешние.

Частные Synthetic-локации поддерживают все [типы синтетических мониторов Dynatrace](../general-information/types-of-synthetic-monitors.md "Узнайте о типах синтетических мониторов Dynatrace.").

## Системные и аппаратные требования для частных локаций

Убедитесь, что целевой хост, который вы планируете использовать для запуска синтетических мониторов, соответствует [системным и аппаратным требованиям для частных Synthetic-локаций](system-and-hardware-requirements-for-private-synthetic.md "Поддерживаемые операционные системы, версии Chromium и аппаратные требования для запуска синтетических мониторов из частных локаций"). Обратите внимание, что Synthetic-совместимые ActiveGate предъявляют более высокие требования к оборудованию и системе, чем обычный Environment или Cluster ActiveGate.

Информация об окончании поддержки

* Для Red Hat/Oracle Linux/Rocky Linux 8 нет новых версий Chromium после версии 133.
  По важным соображениям безопасности и стабильности было принято решение прекратить поддержку установки **Synthetic-совместимого** ActiveGate на Red Hat/Oracle Linux/Rocky Linux 8 после версии ActiveGate 1.325.
  ActiveGate версии 1.325 — **последний Synthetic-совместимый** ActiveGate с поддержкой Red Hat/Oracle Linux/Rocky Linux 8.
  Кроме того, начиная с Dynatrace версии 1.326, планируется ввести механизмы, предотвращающие обновление Synthetic-совместимых ActiveGate на Red Hat/Oracle Linux/Rocky Linux 8 после версии 1.325.
* Разработка Chromium для Amazon Linux 2 остановилась на версии 126.
  По важным соображениям безопасности и стабильности было принято решение прекратить поддержку установки Synthetic-совместимого ActiveGate на Amazon Linux 2 после версии ActiveGate 1.307.
  ActiveGate версии 1.307 — последний Synthetic-совместимый ActiveGate с поддержкой Amazon Linux 2.
  Кроме того, начиная с Dynatrace версии 1.308, введены механизмы, предотвращающие обновление Synthetic-совместимых ActiveGate на Amazon Linux 2 после версии 1.307.
* Разработка Chromium для Red Hat/CentOS 7 остановилась на версии 126.
  По важным соображениям безопасности и стабильности было принято решение прекратить поддержку установки Synthetic-совместимого ActiveGate на Red Hat/CentOS 7 после версии ActiveGate 1.305.
  ActiveGate версии 1.305 — последний Synthetic-совместимый ActiveGate с поддержкой Red Hat/CentOS 7.
  Кроме того, начиная с Dynatrace версии 1.306, введены механизмы, предотвращающие обновление Synthetic-совместимых ActiveGate на Red Hat/CentOS 7 после версии 1.305.

  + Поскольку Red Hat Enterprise Linux 7 достиг [окончания поддержки обслуживания](https://dt-url.net/af03uea) 30 июня 2024 года, все его пакеты были заархивированы. Это означает, что найти необходимые зависимости для обновления может быть невозможно. Подробнее см. [статус Red Hat Enterprise Linux 7](https://dt-url.net/e623zr1).
* До версии 1.329 Synthetic-совместимые ActiveGate на Ubuntu 20 и Ubuntu 22 используют Chromium snap. При настройке [временного каталога по умолчанию для частных Synthetic-файлов](../../../../ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files.md#default-activegate-directories--linux "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.") — `/var/tmp/dynatrace/synthetic`, путь должен начинаться с `/var/tmp`, например `TEMP=/var/tmp/syn`. Dynatrace требует доступ на запись к `/var/tmp` для установки пакетов Chromium snap.
  Начиная с версии 1.331 эти ограничения больше не действуют. Последняя версия ActiveGate на Ubuntu 20 и Ubuntu 22 использует Chrome for Testing, как и Ubuntu 24.

### Подготовка

* Нельзя выполнять синтетические мониторы с помощью Environment ActiveGate, настроенного для [поддержки нескольких сред](../../../../ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support.md "Прочитайте пошаговую инструкцию по настройке одного Environment ActiveGate для поддержки нескольких сред.").
* Вы можете создать частную локацию, используя чистую установку Synthetic-совместимого Environment ActiveGate версии 1.169+ или Cluster ActiveGate с Dynatrace Managed версии 1.176+. Если вы хотите использовать существующий хост ActiveGate, сначала [удалите ActiveGate](../../../../ingest-from/dynatrace-activegate/operation/uninstall-activegate.md "Узнайте, как удалить ActiveGate из систем на Windows или Linux.").
* Synthetic-совместимый ActiveGate используется исключительно для запуска синтетических мониторов. Чистая установка ActiveGate для синтетического мониторинга отключает все остальные функции ActiveGate, включая взаимодействие с OneAgent.
* Убедитесь, что ActiveGate может подключаться к другим [компонентам Dynatrace](../../../../ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates.md "Узнайте о приоритетах подключения между типами ActiveGate, а также между ActiveGate и OneAgent."), а также к ресурсу, который вы хотите тестировать. См. [Настройка прокси для частного синтетического мониторинга](setting-up-proxy-for-private-synthetic.md "Узнайте, как настроить свойства ActiveGate для использования прокси при частном синтетическом мониторинге.").
* Для сетевой конфигурации поддерживаются только IPv4 и DNS UDP.
* Synthetic-совместимому ActiveGate необходим доступ к сервису Amazon S3 для загрузки и доступа к снимкам экрана браузерных мониторов из частных локаций. Убедитесь, что конфигурация брандмауэра разрешает соединения с `*.s3-accelerate.amazonaws.com` по порту `443`. Также можно [настроить прокси](setting-up-proxy-for-private-synthetic.md "Узнайте, как настроить свойства ActiveGate для использования прокси при частном синтетическом мониторинге.") для подключения к сервису Amazon S3. (Снимки экрана хранятся в разных папках для каждой среды мониторинга, но S3-бакет одинаков — `ruxit-synth-screencap`. Данные шифруются с помощью [ключей, управляемых Amazon S3](https://dt-url.net/4a02xvx).)
* Как ручное, так и автоматическое обновление браузера требует доступа к `https://synthetic-packages.s3.amazonaws.com`. В целях безопасности публичный доступ к S3-бакету включён только для определённых файлов; попытка доступа к другим файлам приведёт к ошибке 403.

## Установка Synthetic-совместимого ActiveGate

Установка ActiveGate в последней версии Dynatrace

Приведённые ниже инструкции описывают установку ActiveGate в предыдущей версии Dynatrace. Чтобы узнать, как установить ActiveGate в последней версии Dynatrace, см. [Частные Synthetic-локации на Grail](../../synthetic-on-grail/synthetic-app/private-locations.md#create-a-private-location "Узнайте, как управлять частными локациями в приложении Synthetic.").

Synthetic-совместимый ActiveGate используется исключительно для запуска синтетических мониторов. Чистая установка ActiveGate для синтетического мониторинга отключает все остальные функции ActiveGate, включая взаимодействие с OneAgent. Убедитесь, что хост, на котором устанавливается ActiveGate, имеет доступ к интернету.

Ручная установка

Если эта установка через веб-интерфейс завершится ошибкой, или если вы предпочитаете самостоятельно подготовить хост для Synthetic-движка, вы можете [вручную установить браузер и другие зависимости через S3](#manual). Также можно [установить браузер из пользовательского локального репозитория](#custom-repo).

1. Для Environment ActiveGate: в Dynatrace Hub выберите **ActiveGate** > **Настройка**.

   Для Cluster ActiveGate: перейдите в консоль управления кластером Dynatrace и выберите **Ещё** ![Ещё](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "Ещё") > **Добавить новый Cluster ActiveGate**.
2. Выберите операционную систему для просмотра инструкций.
3. Создайте [**PaaS-токен**](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md "Ознакомьтесь с концепцией токена доступа и его областями.") или введите существующий. Этот токен имеет область `InstallerDownload` **Загрузка установщиков OneAgent и ActiveGate**, что позволяет загрузить установщик ActiveGate. После ввода токен автоматически добавляется к командам загрузки и установки, которые затем отображаются в интерфейсе.

   Существующие токены перечислены на странице **Токены доступа**. Обратите внимание, что PaaS-токен отображается только один раз при создании, после чего хранится в зашифрованном виде и не может быть раскрыт. Рекомендуем хранить PaaS-токен после создания в менеджере паролей, чтобы можно было повторно использовать его по мере необходимости.
4. Только для Linux. В поле **Выберите тип установщика** оставьте выбор по умолчанию: `x86/64`.
5. В поле **Для чего предназначен этот ActiveGate** выберите **Запуск синтетических мониторов из частной локации**.
6. Необязательно. Назначьте ActiveGate в частную Synthetic-локацию — выберите локацию из выпадающего списка. Также можно [назначить ActiveGate в локацию](#add) после установки.
7. Необязательно. Можно отключить поддержку браузерных мониторов. В таком случае Synthetic ActiveGate будет рассматриваться как [без браузера](#browserless).

   ![Отключение поддержки браузерных мониторов](https://dt-cdn.net/images/browserless-deploy-415-1d20a6159c.png)
8. Необязательно. **Задайте настройки** для назначения ActiveGate в [**Зону сети**](../../../../manage/network-zones.md "Узнайте, как работают сетевые зоны в Dynatrace.") и [**Группу ActiveGate**](../../../../ingest-from/dynatrace-activegate/activegate-group.md "Ознакомьтесь с базовыми концепциями групп ActiveGate.").
9. Загрузите установщик на целевой хост.
10. Только для Linux. Рекомендуется **Проверить подпись** — выполните отображаемую команду на целевом хосте для загрузки файла сертификата и проверки установщика.
11. Только для Linux. Выберите дистрибутив Linux.
12. Запустите установщик и другие команды — убедитесь, что используете именно те команды, которые отображаются в интерфейсе.

    Только для Linux. Установщик автоматически загружает браузер и зависимости, необходимые для Synthetic-движка. На Red Hat, Oracle Linux и Rocky Linux также необходимо включить репозитории, из которых установщик загружает зависимости. В качестве предварительного условия для включения проприетарных репозиториев на Red Hat необходимо зарегистрировать экземпляр Red Hat. Веб-интерфейс предоставляет все необходимые команды, как показано в примере ниже.

    ![Команды для установки ActiveGate на Red Hat 9](https://dt-cdn.net/images/synth-ag-commands-red-hat-9-2025-11-17-723-eef29810b5.png)
13. Проверьте установку ActiveGate (**Показать статус развёртывания**).

## Добавление частной локации

Добавление частной локации в последней версии Dynatrace

Приведённые ниже инструкции описывают добавление частной локации в предыдущей версии Dynatrace. Чтобы узнать, как добавить частную локацию в последней версии Dynatrace, см. [Частные Synthetic-локации на Grail](../../synthetic-on-grail/synthetic-app/private-locations.md#create-a-private-location "Узнайте, как управлять частными локациями в приложении Synthetic.").

1. Найдите и выберите **Настройки**. Затем выберите **Мониторинг веб и мобильных приложений** > **Частные Synthetic-локации**.
2. Выберите **Создать локацию**.
3. Дайте вашей локации пользовательское **Имя**, например `Офис в Бостоне, 3-й этаж`.
4. Нанесите её на существующее географическое расположение или добавьте пользовательское географическое расположение, определив **Страну**, **Регион**, **Город** и **Географические координаты**.
5. Добавьте Synthetic-совместимый ActiveGate в локацию. Обратите внимание, что ActiveGate можно назначить только в одну локацию.

   Также можно временно оставить локацию без назначения и назначить её в процессе [установки ActiveGate](#install).
6. Выберите **Добавить**.
7. Выберите **Сохранить**.

## Создание синтетического монитора

Теперь, когда вы создаёте свой HTTP- или браузерный монитор, выберите только что созданную локацию из списка всех доступных локаций. Подробнее см. [Создание HTTP-монитора](../http-monitors-classic/create-an-http-monitor-classic.md "Узнайте, как настроить HTTP-монитор для проверки производительности и доступности вашего сайта."), [Создание браузерного монитора с одним URL](../browser-monitors/create-a-single-url-browser-monitor.md "Узнайте, как настроить браузерный монитор с одним URL для проверки доступности вашего сайта.") или [Запись браузерного clickpath-сценария](../browser-monitors/record-a-browser-clickpath.md "Узнайте, как записать браузерный clickpath-сценарий для мониторинга доступности и производительности приложения.").

## Только для Linux. Ручная установка браузера и зависимостей из S3

Этот раздел не актуален для локаций без браузера.

Amazon Linux 2023, Ubuntu и Oracle Linux 9

Amazon Linux 2023, Ubuntu и Oracle Linux 9 используют Chrome for Testing вместо Chromium. Для ручной установки Chrome for Testing в этих операционных системах см. [Amazon Linux 2023, Ubuntu и Oracle Linux 9 (Chrome for Testing)](#chrome-for-testing).

Если [установка через веб-интерфейс](#install) завершается ошибкой или вы предпочитаете самостоятельно подготовить хост для Synthetic-движка, установите браузер и другие зависимости, используя описанную ниже процедуру. Убедитесь, что вы можете подключиться к `https://synthetic-packages.s3.amazonaws.com` для доступа к браузеру и зависимостям. В целях безопасности публичный доступ к S3-бакету включён только для определённых файлов; попытка доступа к другим файлам приведёт к ошибке 403.

Также см. [Установка браузера из пользовательского репозитория](#custom-repo) ниже.

См. [как вручную обновить браузер](manage-private-synthetic-locations.md#browser-manual "Анализируйте и управляйте использованием ёмкости в ваших частных Synthetic-локациях.") в [Управление частными Synthetic-локациями](manage-private-synthetic-locations.md "Анализируйте и управляйте использованием ёмкости в ваших частных Synthetic-локациях."). Настоятельно рекомендуется поддерживать актуальность версий Linux-совместимых Synthetic-совместимых ActiveGate и браузеров — Dynatrace поддерживает версии браузеров не более чем на две версии позади [последней поддерживаемой Dynatrace версии](system-and-hardware-requirements-for-private-synthetic.md#browser-linux "Поддерживаемые операционные системы, версии Chromium и аппаратные требования для запуска синтетических мониторов из частных локаций") для конкретного выпуска ActiveGate.

### Ubuntu Server 20.04 и 22.04

Этот раздел актуален только для версий 1.329 и более ранних.

1. Установите зависимости Synthetic-движка:

   Зависимости Synthetic-движка:

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

   * Загрузите архив snap-пакета (Ubuntu Server 20.04 и 22.04). Это безопасный проверенный архив, размещённый Dynatrace.

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
   * Извлеките установочные пакеты. Перейдите в директорию, куда вы сохранили архив, и выполните следующую команду:

     ```
     mkdir /tmp/chromium ; tar xzf chromium.tgz -C /tmp/chromium
     ```

     Это создаёт директорию `/tmp/chromium` и извлекает пакеты в неё.
   * Установите извлечённые пакеты.

     ```
     sudo chown -R root:root /tmp/snap-private-tmp
     ```

     ```
     sudo snap ack /tmp/chromium/chromium.assert
     ```

     ```
     sudo snap install --devmode /tmp/chromium/chromium.snap
     ```

     Замените `dtuserag` именами пользователя и группы службы ActiveGate, если они отличаются от значений по умолчанию.

     ```
     sudo chown -R dtuserag:dtuserag /tmp/snap-private-tmp
     ```

     Это устанавливает все пакеты, извлечённые в директорию `/tmp/chromium/`. После успешной установки Chromium директорию `/tmp/chromium/` и загруженный архив `chromium.tgz` можно удалить.
3. После выполнения всех зависимостей запустите установщик ActiveGate с правами root с параметром `--enable-synthetic`, установленным в значение `manual`. Например:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписей, хранящихся вместе с архивами пакетов.

### Red Hat Enterprise Linux, Oracle Linux 8 и Rocky Linux

* Разработка Chromium для Red Hat/CentOS 7 и Amazon Linux 2 остановилась на версии 126.

  + Поскольку Red Hat Enterprise Linux 7 достиг [окончания поддержки обслуживания](https://dt-url.net/af03uea) 30 июня 2024 года, все его пакеты были заархивированы. Это означает, что найти необходимые зависимости для обновления может быть невозможно. Подробнее см. [статус Red Hat Enterprise Linux 7](https://dt-url.net/e623zr1).
* Установка Chromium при необходимости использования прокси для доступа к интернету.

  + Если вам нужно загрузить и установить Chromium, а ваша система требует прокси для доступа к интернету, следует настроить `curl` на использование правильного прокси. Укажите данные вашего прокси и порта, выполнив команды, как в этом примере:

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

   ActiveGate версии 1.305 — последний Synthetic-совместимый ActiveGate с поддержкой Red Hat 7.

   * Зарегистрируйте экземпляр Red Hat.

     ```
     sudo subscription-manager register --auto-attach
     ```
   * Включите репозитории `Extras` и `Optional` Red Hat, а также `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo subscription-manager repos --enable rhel-7-server-extras-rpms



     sudo subscription-manager repos --enable rhel-7-server-optional-rpms



     sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
     ```
   * Установите зависимости Synthetic-движка.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая операционная система

   ActiveGate версии 1.325 — последний Synthetic-совместимый ActiveGate с поддержкой Red Hat 8.

   * Зарегистрируйте экземпляр Red Hat.

     ```
     sudo subscription-manager register --auto-attach
     ```
   * Включите репозитории `Extras` и `Optional` Red Hat, а также `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo subscription-manager repos --enable rhel-8-for-x86_64-baseos-rpms



     sudo subscription-manager repos --enable rhel-8-for-x86_64-appstream-rpms



     sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
     ```
   * Установите зависимости Synthetic-движка.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   * Зарегистрируйте экземпляр Red Hat.

     ```
     sudo subscription-manager register --auto-attach
     ```
   * Включите репозитории `Extras` и `Optional` Red Hat, а также `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo subscription-manager repos --enable rhel-9-for-x86_64-baseos-rpms



     sudo subscription-manager repos --enable rhel-9-for-x86_64-appstream-rpms



     sudo rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
     ```
   * Установите зависимости Synthetic-движка.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая операционная система

   ActiveGate версии 1.305 — последний Synthetic-совместимый ActiveGate с поддержкой CentOS.

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo yum install epel-release
     ```
   * Установите зависимости Synthetic-движка.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая операционная система

   ActiveGate версии 1.325 — последний Synthetic-совместимый ActiveGate с поддержкой Oracle Linux 8.

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo yum install -y oracle-epel-release-el8
     ```
   * Установите зависимости Synthetic-движка.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая операционная система

   ActiveGate версии 1.307 — последний Synthetic-совместимый ActiveGate с поддержкой Amazon Linux 2.

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo amazon-linux-extras install epel
     ```
   * Установите зависимости Synthetic-движка.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая операционная система

   ActiveGate версии 1.325 — последний Synthetic-совместимый ActiveGate с поддержкой Rocky Linux 8.

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo yum install epel-release
     ```
   * Установите зависимости Synthetic-движка.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo yum install epel-release
     ```
   * Установите зависимости Synthetic-движка.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```
2. Загрузите и установите Chromium.

   * Загрузите архив rpm-пакета. Это безопасный проверенный архив, размещённый Dynatrace.

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
   * Извлеките установочные пакеты. Перейдите в директорию, куда вы сохранили архив, и выполните следующую команду:

     ```
     mkdir /tmp/chromium ; tar xzf chromium.tgz -C /tmp/chromium
     ```

     Это создаёт директорию `/tmp/chromium` и извлекает пакеты в неё.
   * Установите извлечённые пакеты.

     ```
     sudo yum install -y /tmp/chromium/*.rpm
     ```

     Это устанавливает все пакеты, извлечённые в директорию `/tmp/chromium/`. После успешной установки Chromium директорию `/tmp/chromium/` и загруженный архив `chromium.tgz` можно удалить.
3. Отключите автоматическое обновление пакетов Chromium:

   ```
   sudo yum -y install yum-plugin-versionlock



   sudo yum versionlock chromium



   sudo yum versionlock chromium-common
   ```
4. Необязательно. Установите нелатинские шрифты TrueType:

   ```
   sudo yum install dejavu-fonts-common.noarch dejavu-sans-fonts.noarch
   ```
5. После выполнения всех зависимостей запустите установщик ActiveGate с правами root с параметром `--enable-synthetic`, установленным в значение `manual`. Например:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписей, хранящихся вместе с архивами пакетов.

### Amazon Linux 2023, Ubuntu и Oracle Linux 9 (Chrome for Testing)

См. [как вручную обновить Chrome for Testing](manage-private-synthetic-locations.md#browser-manual "Анализируйте и управляйте использованием ёмкости в ваших частных Synthetic-локациях.") в [Управление частными Synthetic-локациями](manage-private-synthetic-locations.md "Анализируйте и управляйте использованием ёмкости в ваших частных Synthetic-локациях."). Настоятельно рекомендуется поддерживать актуальность версий Linux-совместимых Synthetic-совместимых ActiveGate и Chrome for Testing — Dynatrace поддерживает версии Chrome for Testing не более чем на две версии позади [последней поддерживаемой Dynatrace версии](system-and-hardware-requirements-for-private-synthetic.md#browser-linux "Поддерживаемые операционные системы, версии Chromium и аппаратные требования для запуска синтетических мониторов из частных локаций") для конкретного выпуска ActiveGate.

В отличие от Chromium на других дистрибутивах, обновления Chrome for Testing не используют менеджеры пакетов. Двоичные файлы Chrome управляются вручную, а зависимости — системным менеджером пакетов.

Chrome for Testing на Ubuntu Server 20.04 и 22.04 поддерживается начиная с версии 1.331

1. Настройте репозитории и установите зависимости.

   Ubuntu

   Amazon Linux 2023

   Oracle Linux 9

   * Установите зависимости Synthetic-движка:

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
   * Установите зависимости Synthetic-движка:

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
   * Установите зависимости Synthetic-движка:

     ```
     sudo yum install -y xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools unzip
     ```
   * Установите зависимости Chrome for Testing:

     ```
     sudo yum install -y alsa-lib at-spi2-atk atk cairo cups-libs libXcomposite libXdamage libXrandr libxkbcommon mesa-libgbm nspr nss pango
     ```
2. Загрузите и настройте Chrome for Testing.

   * Создайте директорию Chrome for Testing:

     ```
     sudo mkdir -p /usr/lib/chrome_for_testing
     ```
   * Загрузите архив пакета Chrome for Testing во временное расположение. Это безопасный проверенный архив, размещённый Dynatrace.

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
   * Извлеките установочный пакет и удалите временные файлы:

     ```
     sudo unzip /tmp/chrome.zip -d /usr/lib/chrome_for_testing



     rm /tmp/chrome.zip
     ```

     Это создаёт директорию `chrome-linux64` внутри `/usr/lib/chrome_for_testing` и извлекает двоичный файл Chrome и вспомогательные файлы в неё.
   * Проверьте Chrome for Testing, проверив версию:

     ```
     /usr/lib/chrome_for_testing/chrome-linux64/chrome --version
     ```

     Вывод команды должен показать загруженную версию Chrome.
3. После выполнения всех зависимостей запустите установщик ActiveGate с правами root. Установщик автоматически обнаружит и проверит Chrome for Testing. Например:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

* Пользовательская директория Chrome for Testing: если вы хотите использовать директорию, отличную от `/usr/lib/chrome_for_testing` по умолчанию, укажите её, установив свойство `synthetic_chrome_for_testing_path` в файле `custom.properties` после установки. Новая директория будет использоваться после обновления модуля Synthetic.
* Файлы Chrome for Testing сохраняются при удалении ActiveGate. При удалении ActiveGate директория Chrome for Testing и её содержимое остаются в системе и могут быть повторно использованы при переустановке.
* Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписей, хранящихся вместе с архивами пакетов.

## Только для Linux. Установка браузера из пользовательского репозитория

ActiveGate версии 1.243+ В дополнение к [установке ActiveGate через веб-интерфейс](#install) и [ручной установке браузера и зависимостей](#manual), вы также можете **установить ActiveGate, указав пользовательский локальный репозиторий для компонентов браузера**. Поскольку этот репозиторий является HTTP-сервером, который вы настраиваете в своей сети, преимущество этого метода в том, что он может использоваться в средах с доступом только к интранету или ограниченным доступом к сети.

Этот метод установки браузера в целом состоит из:

* Загрузки необходимых архивов пакетов deb, snap или rpm, размещённых Dynatrace, и соответствующих файлов подписей.
* Установки и запуска локально размещённого веб-сервера, где находятся загруженные компоненты браузера.
* Загрузки и запуска установщика ActiveGate на целевом хосте с переменной окружения, указывающей на расположение пользовательского репозитория на HTTP-сервере.

* Пользовательский репозиторий браузера может использоваться только для компонентов браузера, но не для их зависимостей. Установка браузера из пользовательского репозитория будет работать только при условии, что все зависимости были разрешены до установки.
* Пользовательские репозитории можно использовать только для **установки и автообновления браузера** — подробнее см. [Автообновление браузера из пользовательского репозитория в разделе «Управление частными Synthetic-локациями»](manage-private-synthetic-locations.md#autoupdate-custom-repo "Анализируйте и управляйте использованием ёмкости в ваших частных Synthetic-локациях.").

1. Загрузите компоненты браузера — архив пакета и файл подписи — из безопасного проверенного архива, размещённого Dynatrace. Ссылки на последние поддерживаемые и предоставляемые версии браузера см. в [Требованиях для частных Synthetic-локаций](system-and-hardware-requirements-for-private-synthetic.md "Поддерживаемые операционные системы, версии Chromium и аппаратные требования для запуска синтетических мониторов из частных локаций").

   Рекомендуется поддерживать актуальность версий Linux-совместимых Synthetic-совместимых ActiveGate и браузеров; выбирайте последнюю предоставляемую версию браузера для ActiveGate.

   Например, для ActiveGate версии 1.331 на Ubuntu 24 необходимы следующие файлы:

   * Архив пакета — `https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip`
   * Файл подписи — `https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip.sig`

   Соответствующие команды загрузки:

   ```
   curl -o chrome-for-testing-linux64-143.0.7499.192.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip
   ```

   ```
   curl -o chrome-for-testing-linux64-143.0.7499.192.zip.sig https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip.sig
   ```
2. Установите веб-сервер по своему выбору и создайте директорию, например `chromium-repo`, для передачи компонентов браузера на хост ActiveGate. Скопируйте загруженные компоненты браузера в эту директорию.
3. Загрузите установщик ActiveGate из Dynatrace Hub.
4. Разрешите все зависимости и включите репозитории, как показано в разделе [Ручная установка браузера и зависимостей из S3](#manual) выше. Пользовательский репозиторий можно использовать только для пакетов браузера, но не для их зависимостей.
5. Установите ActiveGate с включённым модулем Synthetic (`--enable-synthetic`) и переменной окружения `DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO`, указывающей на расположение пользовательского репозитория (в данном примере `https://172.18.0.100/chromium-repo`).

   ```
   sudo DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO=http://172.18.0.100:8000/chromium-repo  /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic
   ```

   Вместо IP-адреса можно использовать имя хоста HTTP-сервера, при условии, что хост ActiveGate может разрешить это имя хоста.

После установки браузера из пользовательского репозитория его можно только автоматически обновлять. Подробнее см. [Автообновление браузера из пользовательского репозитория в разделе «Управление частными Synthetic-локациями»](manage-private-synthetic-locations.md#autoupdate-custom-repo "Анализируйте и управляйте использованием ёмкости в ваших частных Synthetic-локациях.") для получения сведений и альтернативных вариантов обновления.

## Пользовательская версия браузера

Вы можете установить пользовательскую версию браузера, то есть переопределить версию, которую ищет установщик ActiveGate. Это применимо к ручной установке ActiveGate, как описано в разделах [Установка браузера через S3](#manual) или через [пользовательский репозиторий](#custom-repo).

В этой команде для ручной установки ActiveGate через S3 переменная окружения указывает на явный номер версии браузера `143.0.7499.192`, который является частью архива пакета Chrome for Testing.

```
sudo /bin/bash -c "export DYNATRACE_SYNTHETIC_EXPLICIT_CHROMIUM_VERSION=143.0.7499.192; /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic"
```

Эта команда выполняет поиск версии браузера `143.0.7499.192` в пользовательском репозитории `https://172.18.0.100/chromium-repo`.

```
sudo DYNATRACE_SYNTHETIC_EXPLICIT_CHROMIUM_VERSION=143.0.7499.192 DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO=http://172.18.0.100:8000/chromium-repo  /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic
```

## Synthetic-совместимый ActiveGate без браузера

В целом рекомендуется развёртывать Synthetic-совместимый ActiveGate для поддержки выполнения всех типов синтетических мониторов (HTTP, браузер, NAM).

Если вам не нужно запускать браузерные мониторы, рассмотрите возможность развёртывания узла в режиме без браузера. В этом режиме узел развёртывается без браузера, что снижает требования к оборудованию. Однако браузерные мониторы не могут работать на узле без браузера.

Рассматривайте узлы без браузера как альтернативу узлам с поддержкой браузерных мониторов, когда вы сосредоточены исключительно на:

* Сетевых и инфраструктурных задачах (с использованием мониторов NAM)
* Мониторинге API (с использованием HTTP-мониторов)

## Настройка клиента Kerberos

Если вы хотите запускать браузерные мониторы с аутентификацией Kerberos, частная локация должна быть настроена так, чтобы иметь возможность получать билет от Kerberos Key Distribution Center.

Windows

Linux

1. Каждая машина Windows, использующая Kerberos, должна быть правильно настроена с Active Directory.
2. Если аутентификация Kerberos на Windows не работает, используйте следующую команду для регистрации машины.

```
ksetup /addkdc DOMAIN.TO.ADD address.of.kerberos.server
```

`DOMAIN.TO.ADD` — ваше доменное имя, а `address.of.kerberos.server` — Kerberos Key Distribution Center (Active Directory Controller, если вы используете решение Microsoft). Обратите внимание, что в используемых учётных данных имя домена должно быть в верхнем регистре (например, user@EXAMPLE.COM).

Synthetic использует аутентификацию Kerberos путём выполнения команды `kinit`. Подробнее см. [Документация MIT Kerberos — kinit](https://dt-url.net/pr43wj6).

Частная локация Linux должна быть правильно настроена для получения билета от Kerberos Key Distribution Center. Убедитесь, что в локации выполнены следующие условия:

* Установлены пакеты для клиента Kerberos (рабочая станция).
* Правильно настроен файл `/etc/krb5.conf` (или файл конфигурации, указанный переменной окружения `KRB5_CONFIG`).

Конфигурация зависит от дистрибутива Linux. Дополнительную информацию можно найти в официальной документации.

* Ubuntu:

  + `sudo apt install krb5-user`
  + Дополнительная информация: [Документация Ubuntu Server — Как настроить базовую аутентификацию рабочей станции](https://dt-url.net/3g03w9p)
* Red Hat/Rocky:

  + `yum install krb5-workstation krb5-libs`
  + Дополнительная информация: [Документация Red Hat — Настройка клиента Kerberos](https://dt-url.net/1u23wq7)

## Соответствие Synthetic требованиям FIPS

ActiveGate версии 1.315+

### Установка

Для установки Synthetic-совместимого ActiveGate в режиме соответствия FIPS необходимо добавить флаг `--fips-mode`, также см. [настройку установки ActiveGate для соответствия FIPS](../../../../ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate.md#fips-compliant-mode "Узнайте о параметрах командной строки, которые можно использовать с ActiveGate на Linux.").

```
/bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic --fips-mode
```

Обратите внимание, что режим соответствия FIPS нельзя изменить после установки. Для изменения режима необходимо удалить ActiveGate и переустановить его с нужными настройками.
Кроме того, если вы намерены выполнять браузерные мониторы, потребуется дополнительная настройка, описанная в разделах [Настройка прокси для режима FIPS](setting-up-proxy-for-private-synthetic.md#fips-proxy "Узнайте, как настроить свойства ActiveGate для использования прокси при частном синтетическом мониторинге.") и [Настройка прокси для режима FIPS с корпоративным прокси](setting-up-proxy-for-private-synthetic.md#fips-corporate-proxy "Узнайте, как настроить свойства ActiveGate для использования прокси при частном синтетическом мониторинге.").

### Требования и ограничения

* Требуется операционная система с включённым режимом соответствия FIPS, также см. [Соответствие ActiveGate требованиям FIPS](../../../../ingest-from/dynatrace-activegate/activegate-fips-compliance.md "Узнайте о соответствии ActiveGate требованиям FIPS").
* В настоящее время поддерживаются следующие операционные системы:

  + Ubuntu Pro 22.04
  + Red Hat Enterprise Linux 9
* Частные Synthetic-локации на Kubernetes в настоящее время не поддерживаются.

### Обеспечение соответствия

Для обеспечения соответствия трафика браузерных мониторов требованиям FIPS он должен маршрутизироваться через локальный перехватывающий прокси, который шифрует трафик с помощью криптографической библиотеки, сертифицированной FIPS. Подробнее см. [Настройка прокси для режима FIPS](setting-up-proxy-for-private-synthetic.md#fips-proxy "Узнайте, как настроить свойства ActiveGate для использования прокси при частном синтетическом мониторинге.").

Для HTTP-мониторов используется [Amazon Corretto Crypto Provider](https://github.com/corretto/amazon-corretto-crypto-provider/) — криптографическая библиотека, сертифицированная FIPS, которая использует AWS-LC-FIPS 2.x в качестве криптографического модуля. См. [Сертификат №4816](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4816).

Synthetic-совместимый ActiveGate в режиме соответствия FIPS поддерживает тот же набор шифровальных наборов, что и [обычный ActiveGate](../../../../ingest-from/dynatrace-activegate/activegate-fips-compliance.md#supported-cipher-suites "Узнайте о соответствии ActiveGate требованиям FIPS").

## Часто задаваемые вопросы

Как проверить подлинность загруженных пакетов Chrome(-ium)?

Chromium

Chrome for Testing

Каждый архив пакета `tgz` хранится в S3-бакете вместе с файлом подписи `*.tgz.sig`. Для проверки подлинности пакетов на вашем диске:

1. Загрузите файл подписи. Имя файла идентично архиву пакета, но с расширением `sig`. Например, для Chromium 140 команда будет:

   ```
   curl --output chromium.tgz.sig https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-140.0.7339.185-1.el9.tgz.sig
   ```
2. Проверьте пакет:

   ```
   wget https://ca.dynatrace.com/dt-root.cert.pem ; openssl cms



   -verify



   -in chromium.tgz.sig



   -inform PEM



   -content chromium.tgz



   -binary



   -CAfile dt-root.cert.pem > /dev/null
   ```
3. Проверьте временную метку подписи.

   Также можно получить точную временную метку подписи. Загрузите файл `*.tgz.sig.tsr` из того же расположения, что и установочные пакеты и подпись, и выполните следующую команду:

   ```
   openssl ts -reply -in chromium.tgz.sig.tsr -text
   ```

Каждый архив пакета `zip` хранится в S3-бакете вместе с файлом подписи `*.zip.sig`. Для проверки подлинности пакетов на вашем диске:

1. Загрузите файл подписи. Имя файла идентично архиву пакета, но с расширением `sig`. Например, для Chrome for Testing 141.0.7390.122 команда будет:

   ```
   curl --output chrome.zip.sig https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-141.0.7390.122.zip.sig
   ```
2. Проверьте пакет:

   ```
   wget https://ca.dynatrace.com/dt-root.cert.pem ; openssl cms



   -verify



   -in chrome.zip.sig



   -inform PEM



   -content chrome.zip



   -binary



   -CAfile dt-root.cert.pem > /dev/null
   ```
3. Проверьте временную метку подписи.

   Также можно получить точную временную метку подписи. Загрузите файл `*.zip.sig.tsr` из того же расположения, что и установочные пакеты и подпись, и выполните следующую команду:

   ```
   openssl ts -reply -in chrome.zip.sig.tsr -text
   ```

Можно ли использовать прокси с Synthetic-совместимым ActiveGate?

Начиная с ActiveGate версии 1.175+, ActiveGate, выполняющий синтетические мониторы, может подключаться через прокси как к кластеру Dynatrace, так и к тестируемому ресурсу. Подробнее см. [Настройка прокси для частного синтетического мониторинга](setting-up-proxy-for-private-synthetic.md "Узнайте, как настроить свойства ActiveGate для использования прокси при частном синтетическом мониторинге.").

Можно ли обновить более ранний ActiveGate до версии 1.169+ и настроить его для использования с частными синтетическими мониторами?

Нет, для работы мониторов из частных локаций требуется чистая установка специально для синтетического мониторинга.

Можно ли включить Synthetic на существующей установке ActiveGate?

Частные Synthetic-локации требуют чистой установки ActiveGate специально для синтетического мониторинга.

Ручного редактирования файла `custom.properties` недостаточно для включения в ActiveGate возможности выполнения синтетических мониторов.

## Устранение неполадок

[Не отображаются снимки экрана в результатах браузерного монитора](https://dt-url.net/mfw2xmb)

Посетите [форум по устранению неполадок в сообществе Dynatrace](https://dt-url.net/dy122xtf) для получения дополнительной информации по устранению неполадок.

## Связанные темы
