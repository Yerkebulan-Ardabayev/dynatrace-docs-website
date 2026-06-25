---
title: Создание частного расположения Synthetic
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location
scraped: 2026-05-12T11:24:04.973796
---

# Создание частного расположения Synthetic

# Создание частного расположения Synthetic

* How-to guide
* 24-min read
* Updated on Apr 28, 2026

Вы можете запускать синтетические мониторы Dynatrace из частного расположения Synthetic — расположения в вашей приватной сетевой инфраструктуре, где установлен один или несколько экземпляров Synthetic-enabled ActiveGate.

С мониторами, выполняемыми из частного расположения, вы можете перенести возможности тестирования, доступные в публичных расположениях, прямо в свою среду. Частные расположения позволяют:

* Измерять производительность и доступность внутренних веб-страниц.
* Тестировать сложные внутренние приложения с помощью браузерных clickpath-ов.
* Измерять внешние ресурсы с помощью синтетических мониторов, запускаемых из внутренних расположений.
* Мониторить API — как внутренние, так и внешние.

Частные расположения Synthetic поддерживают все [типы синтетических мониторов Dynatrace](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Узнайте о типах синтетических мониторов Dynatrace.").

## Требования к системе и оборудованию для частных расположений

Убедитесь, что целевой хост, который вы планируете использовать для запуска синтетических мониторов, соответствует [требованиям к системе и оборудованию для частных расположений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые операционные системы, версии Chromium и требования к оборудованию для запуска синтетических мониторов из частных расположений"). Учтите, что Synthetic-enabled ActiveGate предъявляет более высокие требования к оборудованию и системе, чем обычный Environment или Cluster ActiveGate.

Информация о прекращении поддержки

* Новых версий Chromium для Red Hat/Oracle Linux/Rocky Linux 8 после версии 133 не выходит.
  По соображениям безопасности и стабильности принято решение прекратить поддержку установки **Synthetic-enabled** ActiveGate на Red Hat/Oracle Linux/Rocky Linux 8 после версии ActiveGate 1.325.
  Версия ActiveGate 1.325 является **последней поддерживаемой Synthetic-enabled** версией ActiveGate для Red Hat/Oracle Linux/Rocky Linux 8.
  Начиная с Dynatrace версии 1.326 будут введены механизмы, препятствующие обновлению Synthetic-enabled ActiveGate на Red Hat/Oracle Linux/Rocky Linux 8 выше версии 1.325.
* До версии 1.329 Synthetic-enabled ActiveGate на Ubuntu 20 и Ubuntu 22 использует Chromium snap. При настройке [временного каталога для файлов частного Synthetic](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files#default-activegate-directories--linux "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.")`/var/tmp/dynatrace/synthetic`, путь должен начинаться с `/var/tmp`, например `TEMP=/var/tmp/syn`. Dynatrace требует доступ на запись в `/var/tmp` для установки snap-пакетов Chromium.
  Начиная с версии 1.331 эти ограничения больше не действуют. Последняя версия ActiveGate на Ubuntu 20 и Ubuntu 22 использует Chrome for Testing, как и Ubuntu 24.

### Перед началом работы

* Синтетические мониторы нельзя выполнять с помощью Environment ActiveGate, настроенного для [поддержки нескольких сред](/managed/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support "Читайте пошаговую процедуру настройки одного Environment ActiveGate для поддержки нескольких сред.").
* Создать частное расположение можно с использованием чистой установки Synthetic-enabled Environment ActiveGate версии 1.169+ или Cluster ActiveGate с Dynatrace Managed версии 1.176+. Если вы хотите использовать существующий хост ActiveGate, сначала [удалите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/uninstall-activegate "Узнайте, как удалить ActiveGate с систем Windows или Linux.").
* Synthetic-enabled ActiveGate используется исключительно для запуска синтетических мониторов. Чистая установка ActiveGate для целей синтетического мониторинга отключает все остальные функции ActiveGate, включая связь с OneAgent-ами.
* Убедитесь, что ActiveGate может подключаться к другим [компонентам Dynatrace](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate и OneAgent-ами."), а также к ресурсу, который вы хотите тестировать. См. [Настройка прокси для частного синтетического мониторинга](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Узнайте, как настроить свойства ActiveGate для работы через прокси.").
* Поддерживаются только IPv4 и DNS UDP для сетевой конфигурации.
* Synthetic-enabled ActiveGate требует доступ к сервису Amazon S3 для загрузки и доступа к скриншотам браузерных мониторов из частных расположений. Убедитесь, что конфигурация вашего межсетевого экрана разрешает подключения к `*.s3-accelerate.amazonaws.com` на порту `443`. Вы также можете [настроить прокси](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Узнайте, как настроить свойства ActiveGate для работы через прокси.") для подключения к сервису Amazon S3. (Скриншоты хранятся в отдельной папке для каждой среды мониторинга, но корзина S3 одна (`ruxit-synth-screencap`). Данные зашифрованы с помощью [ключей, управляемых Amazon S3](https://dt-url.net/4a02xvx).)
* Как ручное, так и автоматическое обновление браузера требуют доступа к `https://synthetic-packages.s3.amazonaws.com`. По соображениям безопасности публичный доступ к корзине S3 открыт только для конкретных файлов; попытка обратиться к другим файлам вернёт ошибку 403.

## Установка Synthetic-enabled ActiveGate

Synthetic-enabled ActiveGate используется исключительно для запуска синтетических мониторов. Чистая установка ActiveGate для целей синтетического мониторинга отключает все остальные функции ActiveGate, включая связь с OneAgent-ами. Убедитесь, что хост, на который устанавливается ActiveGate, имеет доступ в интернет.

Ручная установка

Если эта установка через веб-интерфейс завершается с ошибкой или вы предпочитаете самостоятельно подготовить хост для Synthetic engine, вы можете [вручную установить браузер и зависимости через S3](#manual). Вы также можете [установить браузер из пользовательского локального репозитория](#custom-repo).

1. Для Environment ActiveGate: в Dynatrace Hub выберите **ActiveGate** > **Set up**.

   Для Cluster ActiveGate: перейдите в Dynatrace Cluster Management Console и выберите **More** ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Add new Cluster ActiveGate**.
2. Выберите операционную систему для отображения инструкций.
3. Создайте [**PaaS Token**](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Узнайте о концепции токена доступа и его областях.") или введите существующий токен. Этот токен имеет область `InstallerDownload` (**Download OneAgent and ActiveGate installers**), которая позволяет скачивать установщик ActiveGate. После ввода токен автоматически добавляется к командам скачивания и установки, которые отображаются в интерфейсе.

   Существующие токены перечислены на странице **Access tokens**. Учтите, что PaaS-токен отображается только один раз при создании, после чего хранится в зашифрованном виде и не может быть раскрыт. Рекомендуем сохранять PaaS-токен после создания в менеджере паролей для последующего использования.
4. Только Linux. Для параметра **Choose installer type** оставьте выбор по умолчанию: `x86/64`.
5. Для параметра **What's the purpose of this ActiveGate** выберите **Run synthetic monitors from a private location**.
6. Опционально. Назначьте ActiveGate частному расположению Synthetic: выберите расположение из выпадающего списка. Вы также можете [назначить ActiveGate в расположение](#add) после установки.
7. Опционально. Вы можете отключить поддержку браузерных мониторов. В этом случае Synthetic ActiveGate будет работать в [безбраузерном режиме](#browserless).

   ![Disabling support for browser monitors](https://dt-cdn.net/images/browserless-deploy-415-1d20a6159c.png)

   Отключение поддержки браузерных мониторов
8. Опционально. **Set customized options** — назначьте ActiveGate в [**Network zone**](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.") и [**ActiveGate group**](/managed/ingest-from/dynatrace-activegate/activegate-group "Понимание концепции групп ActiveGate.").
9. Скачайте установщик на целевой хост.
10. Только Linux. Рекомендуется. **Verify signature** — выполните отображаемую команду на целевом хосте, чтобы скачать файл сертификата и проверить установщик.
11. Только Linux. Выберите дистрибутив Linux.
12. Запустите установщик и другие команды — используйте точно те команды, которые отображены в интерфейсе.

    Только Linux. Установщик автоматически скачивает браузер и зависимости, необходимые для Synthetic engine. На Red Hat, Oracle Linux и Rocky Linux также требуется включить репозитории, из которых устанавливаются зависимости. Предварительным условием для включения проприетарных репозиториев на Red Hat является регистрация вашего Red Hat-экземпляра. Веб-интерфейс предоставляет все необходимые для этого команды, как показано в примере ниже.

    ![Commands to install ActiveGate on Red Hat 9](https://dt-cdn.net/images/synth-ag-commands-red-hat-9-2025-11-17-723-eef29810b5.png)

    Команды для установки ActiveGate на Red Hat 9
13. Проверьте установку ActiveGate (**Show deployment status**).

## Добавление частного расположения

Используйте [Cluster API v2](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Узнайте об управлении средами, сетевыми зонами, расположениями Synthetic, узлами и токенами в Dynatrace Managed через Cluster API v2.") для создания расположения и назначения в него Cluster ActiveGate.

1. Используйте метод [GET all nodes](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all "Получение списка всех узлов Synthetic через Synthetic API v2 в Dynatrace Managed.") для получения списка всех Synthetic-enabled Cluster ActiveGate в вашей среде. В числе других параметров в ответе будут IP-адрес хоста и `entityId`. Например:

   ```
   {



   "nodes": [



   {



   "entityId": "3086117876",



   "hostname": "gdn.dyna.trace",



   "ips": [



   "238.245.160.14"



   ],



   "version": "1.175.0.20181210-173639",



   "browserMonitorsEnabled": true



   }



   ]



   }
   ```
2. Используйте эндпоинт [POST a location](/managed/dynatrace-api/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/post-a-location "Создание частного расположения Synthetic через Synthetic API v2 в Dynatrace Managed.") для создания нового расположения и назначения в него Synthetic-enabled Cluster ActiveGate. Учтите, что ActiveGate может быть назначен только в одно расположение. Используйте `entityId` из предыдущего шага в качестве одного из значений в `nodes` и задайте `type` как `CLUSTER`. Пример тела запроса для вызова `POST`:

   ```
   {



   "type": "CLUSTER",



   "name": "Dynatrace Gdansk Lab",



   "countryCode": "PL",



   "regionCode": "PL82",



   "city": "Gdansk",



   "latitude": 54.3990,



   "longitude": 18.5766,



   "nodes": [



   "3086117876"



   ]



   }
   ```

   В случае успешного вызова вы получите ответ `200` OK.

## Создание синтетического монитора

Теперь при создании HTTP- или браузерного монитора выберите только что созданное расположение из списка доступных. Дополнительную информацию см. в разделах [Создание HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Узнайте, как создать HTTP-монитор."), [Создание браузерного монитора с одним URL](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Узнайте, как создать браузерный монитор с одним URL.") или [Запись браузерного clickpath](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath.").

## Только Linux. Ручная установка браузера и зависимостей из S3

Этот раздел не актуален для безбраузерных расположений.

Amazon Linux 2023, Ubuntu и Oracle Linux 9

Amazon Linux 2023, Ubuntu и Oracle Linux 9 используют Chrome for Testing вместо Chromium. Инструкции по ручной установке Chrome for Testing для этих операционных систем см. в разделе [Amazon Linux 2023, Ubuntu и Oracle Linux 9 (Chrome for Testing)](#chrome-for-testing).

Если [установка через веб-интерфейс](#install) завершается с ошибкой или вы предпочитаете самостоятельно подготовить хост для Synthetic engine, воспользуйтесь описанной ниже процедурой. Убедитесь, что вы можете подключиться к `https://synthetic-packages.s3.amazonaws.com` для доступа к браузеру и зависимостям. По соображениям безопасности публичный доступ к корзине S3 открыт только для конкретных файлов; попытка обратиться к другим файлам вернёт ошибку 403.

Также см. [Установка браузера из пользовательского репозитория](#custom-repo) ниже.

Инструкции по [ручному обновлению браузера](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser-manual "Анализ и управление использованием ресурсов в частных расположениях Synthetic.") см. в разделе [Управление частными расположениями Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Анализ и управление использованием ресурсов в частных расположениях Synthetic."). Настоятельно рекомендуется поддерживать актуальность версий Linux-based Synthetic-enabled ActiveGate и браузера: Dynatrace поддерживает версии браузера не более чем на две версии позади [последней поддерживаемой версии](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#browser-linux "Поддерживаемые ОС, версии Chromium и требования к оборудованию.") для конкретного выпуска ActiveGate.

### Ubuntu Server 20.04 и 22.04

Этот раздел актуален только для выпусков 1.329 и более ранних.

1. Установите зависимости Synthetic engine:

   Зависимости Synthetic engine:

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
2. Скачайте и установите Chromium.

   * Скачайте архив snap-пакетов (Ubuntu Server 20.04 и 22.04). Это безопасный верифицированный архив, размещённый на серверах Dynatrace.

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

     Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписи, хранящихся вместе с архивами пакетов.
   * Распакуйте установочные пакеты. Перейдите в каталог, куда сохранили архив, и выполните следующую команду:

     ```
     mkdir /tmp/chromium ; tar xzf chromium.tgz -C /tmp/chromium
     ```

     Это создаёт каталог `/tmp/chromium` и распаковывает пакеты в него.
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

     Замените `dtuserag` на имя пользователя и группы службы ActiveGate, если они отличаются от значений по умолчанию.

     ```
     sudo chown -R dtuserag:dtuserag /tmp/snap-private-tmp
     ```

     Устанавливаются все пакеты, распакованные в каталог `/tmp/chromium/`. После успешной установки Chromium каталог `/tmp/chromium/` и скачанный архив `chromium.tgz` можно удалить.
3. После выполнения всех зависимостей запустите установщик ActiveGate с правами root с параметром `--enable-synthetic`, установленным в `manual`. Например:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписи, хранящихся вместе с архивами пакетов.

### Red Hat Enterprise Linux, Oracle Linux 8 и Rocky Linux

* Установка Chromium при необходимости использования прокси для доступа в интернет.

  + Если для скачивания и установки Chromium ваша система требует прокси для доступа в интернет, настройте `curl` на использование нужного прокси. Укажите данные прокси и порта, выполнив команды, как в этом примере:

    ```
    vi /root/.curlrc



    proxy=http://proxy.example.com:8080
    ```

1. Настройте репозитории и установите зависимости.

   Red Hat 8

   Red Hat 9

   Oracle Linux 8

   Rocky Linux 8

   Rocky Linux 9

   Устаревшая ОС

   ActiveGate версии 1.325 является последней версией с поддержкой Synthetic-enabled для Red Hat 8.

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
   * Установите зависимости Synthetic engine.

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
   * Установите зависимости Synthetic engine.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая ОС

   ActiveGate версии 1.325 является последней версией с поддержкой Synthetic-enabled для Oracle Linux 8.

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo yum install -y oracle-epel-release-el8
     ```
   * Установите зависимости Synthetic engine.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   Устаревшая ОС

   ActiveGate версии 1.325 является последней версией с поддержкой Synthetic-enabled для Rocky Linux 8.

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo yum install epel-release
     ```
   * Установите зависимости Synthetic engine.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xorg-x11-xkb-utils xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```

   * Включите `EPEL` (Extra Packages for Enterprise Linux).

     ```
     sudo yum install epel-release
     ```
   * Установите зависимости Synthetic engine.

     ```
     sudo yum install -y xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 libwayland-server mesa-libgbm curl nss-tools
     ```
2. Скачайте и установите Chromium.

   * Скачайте архив rpm-пакетов. Это безопасный верифицированный архив, размещённый на серверах Dynatrace.

     ActiveGate версии 1.337

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-146.0.7680.177-1.el9.tgz
     ```

     ActiveGate версии 1.335

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-146.0.7680.177-1.el9.tgz
     ```

     ActiveGate версии 1.333

     ##### Red Hat Enterprise Linux/Rocky Linux 9

     ```
     curl --output chromium.tgz https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-144.0.7559.132-1.el9.tgz
     ```

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

     Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписи, хранящихся вместе с архивами пакетов.
   * Распакуйте установочные пакеты. Перейдите в каталог, куда сохранили архив, и выполните следующую команду:

     ```
     mkdir /tmp/chromium ; tar xzf chromium.tgz -C /tmp/chromium
     ```

     Это создаёт каталог `/tmp/chromium` и распаковывает пакеты в него.
   * Установите распакованные пакеты.

     ```
     sudo yum install -y /tmp/chromium/*.rpm
     ```

     Устанавливаются все пакеты, распакованные в каталог `/tmp/chromium/`. После успешной установки Chromium каталог `/tmp/chromium/` и скачанный архив `chromium.tgz` можно удалить.
3. Отключите автоматическое обновление пакетов Chromium:

   ```
   sudo yum -y install yum-plugin-versionlock



   sudo yum versionlock chromium



   sudo yum versionlock chromium-common
   ```
4. Опционально. Установите не-латинские шрифты TrueType:

   ```
   sudo yum install dejavu-fonts-common.noarch dejavu-sans-fonts.noarch
   ```
5. После выполнения всех зависимостей запустите установщик ActiveGate с правами root с параметром `--enable-synthetic`, установленным в `manual`. Например:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписи, хранящихся вместе с архивами пакетов.

### Amazon Linux 2023, Ubuntu и Oracle Linux 9 (Chrome for Testing)

Инструкции по [ручному обновлению Chrome for Testing](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser-manual "Анализ и управление использованием ресурсов в частных расположениях Synthetic.") см. в разделе [Управление частными расположениями Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Анализ и управление использованием ресурсов в частных расположениях Synthetic."). Настоятельно рекомендуется поддерживать актуальность версий Linux-based Synthetic-enabled ActiveGate и Chrome for Testing: Dynatrace поддерживает версии Chrome for Testing не более чем на две версии позади [последней поддерживаемой версии](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#browser-linux "Поддерживаемые ОС, версии Chromium и требования к оборудованию.") для конкретного выпуска ActiveGate.

В отличие от Chromium на других дистрибутивах, обновления Chrome for Testing не используют менеджеры пакетов. Вы управляете бинарными файлами Chrome вручную, тогда как зависимости управляются системным менеджером пакетов.

На Ubuntu Server 20.04 и 22.04 Chrome for Testing поддерживается начиная с версии 1.331.

1. Настройте репозитории и установите зависимости.

   Ubuntu 20/22

   Ubuntu 24

   Amazon Linux 2023

   Oracle Linux 9

   * Установите зависимости Synthetic engine:

     ```
     sudo apt-get update && sudo apt-get -y install xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable libnss3-tools auditd fonts-dejavu-core
     ```
   * Установите зависимости Chrome for Testing:

     ```
     sudo apt-get -y install libasound2 libatk-bridge2.0-0 libatk1.0-0 libcairo2 libcups2 libgbm1 libnspr4 libnss3 libpango-1.0-0 libxcomposite1 libxdamage1 libxfixes3 libxkbcommon0 libxrandr2
     ```

   * Установите зависимости Synthetic engine:

     ```
     sudo apt-get update && sudo apt-get -y install xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-scalable libnss3-tools auditd fonts-dejavu-core
     ```
   * Установите зависимости Chrome for Testing:

     ```
     sudo apt-get -y install libasound2t64 libatk-bridge2.0-0t64 libatk1.0-0t64 libcairo2 libcups2t64 libgbm1 libnspr4 libnss3 libpango-1.0-0 libxcomposite1 libxdamage1 libxfixes3 libxkbcommon0 libxrandr2
     ```

   * Установите зависимости Synthetic engine:

     ```
     sudo yum install -y lsof psmisc xorg-x11-server-Xvfb xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 nss-tools xkbcomp
     ```
   * Установите зависимости Chrome for Testing:

     ```
     sudo yum install -y alsa-lib at-spi2-atk atk cairo cups-libs dbus-libs libXcomposite libXdamage libXrandr libxkbcommon mesa-libgbm nspr nss pango
     ```

   * Включите `EPEL` (Extra Packages for Enterprise Linux):

     ```
     sudo yum install -y oracle-epel-release-el9
     ```
   * Установите зависимости Synthetic engine:

     ```
     sudo yum install -y lsof psmisc xorg-x11-server-Xvfb xkbcomp xorg-x11-server-utils xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-Type1 nss-tools unzip
     ```
   * Установите зависимости Chrome for Testing:

     ```
     sudo yum install -y alsa-lib at-spi2-atk atk cairo cups-libs libXcomposite libXdamage libXrandr libxkbcommon mesa-libgbm nspr nss pango
     ```
2. Скачайте и настройте Chrome for Testing.

   * Создайте каталог для Chrome for Testing:

     ```
     sudo mkdir -p /usr/lib/chrome_for_testing
     ```
   * Скачайте архив пакета Chrome for Testing во временное место. Это безопасный верифицированный архив, размещённый на серверах Dynatrace.

     ActiveGate версии 1.337

     ```
     curl --output /tmp/chrome.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-146.0.7680.178.zip
     ```

     ActiveGate версии 1.335

     ```
     curl --output /tmp/chrome.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-146.0.7680.178.zip
     ```

     ActiveGate версии 1.333

     ```
     curl --output /tmp/chrome.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-144.0.7559.133.zip
     ```

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

     Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписи, хранящихся вместе с архивами пакетов.
   * Распакуйте установочный пакет и очистите временные файлы:

     ```
     sudo unzip /tmp/chrome.zip -d /usr/lib/chrome_for_testing



     rm /tmp/chrome.zip
     ```

     Это создаёт каталог `chrome-linux64` внутри `/usr/lib/chrome_for_testing` и распаковывает в него бинарный файл Chrome и вспомогательные файлы.
   * Проверьте Chrome for Testing, убедившись в корректности версии:

     ```
     /usr/lib/chrome_for_testing/chrome-linux64/chrome --version
     ```

     Вывод команды должен показать версию Chrome, которую вы скачали.
3. После выполнения всех зависимостей запустите установщик ActiveGate с правами root. Установщик автоматически обнаружит и проверит Chrome for Testing. Например:

   ```
   /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
   ```

* Пользовательский каталог Chrome for Testing: если вы хотите использовать каталог, отличный от `/usr/lib/chrome_for_testing` по умолчанию, укажите его с помощью переменной окружения `CFT_DIR` при установке:

  ```
  CFT_DIR=/custom/path /bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic=manual
  ```
* Вы также можете настроить путь, задав свойство `synthetic_chrome_for_testing_path` в файле `custom.properties` после установки. Новый каталог будет использован после обновления модуля Synthetic.
* Файлы Chrome for Testing сохраняются при удалении ActiveGate. Если вы удалите ActiveGate, каталог Chrome for Testing и его содержимое останутся на системе и могут быть повторно использованы при переустановке.
* Вы можете [проверить подлинность пакетов](#verify) с помощью файлов подписи, хранящихся вместе с архивами пакетов.

## Только Linux. Установка браузера из пользовательского репозитория

ActiveGate версии 1.243+ Помимо [установки через веб-интерфейс](#install) и [ручной установки браузера и зависимостей](#manual), вы также можете **установить ActiveGate, указав пользовательский локальный репозиторий для компонентов браузера**. Поскольку этот репозиторий представляет собой HTTP-сервер, развёрнутый в вашей сети, преимущество этого метода состоит в том, что он применим в средах с доступом только к интранету или с ограниченным сетевым доступом.

Этот метод установки браузера в целом состоит из следующих шагов:

* Скачать необходимые deb-, snap- или rpm-архивы пакетов, размещённые Dynatrace, и соответствующие файлы подписи.
* Установить и запустить локальный веб-сервер с компонентами браузера.
* Скачать и запустить установщик ActiveGate на целевом хосте с переменной окружения, указывающей на расположение пользовательского репозитория на HTTP-сервере.

* Пользовательский репозиторий браузера можно использовать только для компонентов браузера, но не для их зависимостей. Установка браузера из пользовательского репозитория будет работать только если все зависимости разрешены до начала установки.
* Пользовательские репозитории можно использовать только для **установки браузера и автообновления**: подробности см. в разделе [Автообновление браузера из пользовательского репозитория в разделе Управление частными расположениями Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#autoupdate-custom-repo "Анализ и управление использованием ресурсов в частных расположениях Synthetic.").

1. Скачайте компоненты браузера — архив пакетов и файл подписи — из безопасного верифицированного архива, размещённого Dynatrace. Ссылки на последние поддерживаемые версии браузера см. в разделе [Требования для частных расположений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые ОС, версии Chromium и требования к оборудованию.").

   Рекомендуется поддерживать актуальность версий Linux-based Synthetic-enabled ActiveGate и браузера; выбирайте последнюю доступную версию браузера для ActiveGate.

   Например, для ActiveGate версии 1.331 на Ubuntu 24 необходимы следующие файлы:

   * Архив пакетов: `https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip`
   * Файл подписи: `https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip.sig`

   Соответствующие команды скачивания:

   ```
   curl -o chrome-for-testing-linux64-143.0.7499.192.zip https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip
   ```

   ```
   curl -o chrome-for-testing-linux64-143.0.7499.192.zip.sig https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip.sig
   ```
2. Установите веб-сервер на ваш выбор и создайте каталог, например `chromium-repo`, для размещения компонентов браузера для хоста ActiveGate. Скопируйте скачанные компоненты браузера в этот каталог.
3. Скачайте установщик ActiveGate из Dynatrace Hub.
4. Разрешите все зависимости и включите необходимые репозитории, как описано в разделе [Ручная установка браузера и зависимостей из S3](#manual). Пользовательский репозиторий можно использовать только для пакетов браузера, но не для их зависимостей.
5. Установите ActiveGate с включённым модулем Synthetic (`--enable-synthetic`) и переменной окружения `DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO`, указывающей на расположение пользовательского репозитория (в данном примере `https://172.18.0.100/chromium-repo`).

   ```
   sudo DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO=http://172.18.0.100:8000/chromium-repo  /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic
   ```

   Вместо IP-адреса можно использовать имя хоста HTTP-сервера, если хост ActiveGate может разрешить это имя.

После установки браузера таким способом из пользовательского репозитория он может только автоматически обновляться. Подробности и альтернативы обновления см. в разделе [Автообновление браузера из пользовательского репозитория в разделе Управление частными расположениями Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#autoupdate-custom-repo "Анализ и управление использованием ресурсов в частных расположениях Synthetic.").

## Пользовательская версия браузера

Вы можете установить пользовательскую версию браузера, то есть переопределить версию, которую ищет установщик ActiveGate. Это применимо при ручной установке ActiveGate, описанной в разделах [Установка браузера через S3](#manual) или через [пользовательский репозиторий](#custom-repo).

В этой команде для ручной установки ActiveGate через S3 переменная окружения указывает на явный номер версии браузера `143.0.7499.192`, который является частью архива пакетов Chrome for Testing.

```
sudo /bin/bash -c "export DYNATRACE_SYNTHETIC_EXPLICIT_CHROMIUM_VERSION=143.0.7499.192; /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic"
```

Эта команда ищет версию браузера `143.0.7499.192` в пользовательском репозитории `https://172.18.0.100/chromium-repo`.

```
sudo DYNATRACE_SYNTHETIC_EXPLICIT_CHROMIUM_VERSION=143.0.7499.192 DYNATRACE_SYNTHETIC_CUSTOM_CHROMIUM_REPO=http://172.18.0.100:8000/chromium-repo  /bin/bash Dynatrace-ActiveGate-Linux-x86-*.sh --enable-synthetic
```

## Безбраузерный Synthetic-enabled ActiveGate

В общем случае рекомендуется развёртывать Synthetic-enabled ActiveGate с поддержкой выполнения всех типов синтетических мониторов (HTTP, браузерных, NAM).

Если выполнение браузерных мониторов не требуется, рассмотрите развёртывание узла в безбраузерном режиме. В этом режиме узел развёртывается без браузера, что снижает требования к оборудованию. Однако браузерные мониторы на безбраузерном узле работать не будут.

Рассмотрите безбраузерные узлы как альтернативу узлам с поддержкой браузерных мониторов в следующих сценариях:

* Задачи, связанные с сетью и инфраструктурой (с использованием NAM-мониторов).
* Мониторинг API (с использованием HTTP-мониторов).

## Настройка Kerberos-клиента

Если вы хотите запускать браузерные мониторы с аутентификацией Kerberos, частное расположение должно быть настроено на получение билета от Kerberos Key Distribution Center.

Windows

Linux

1. Каждая Windows-машина, использующая Kerberos, должна быть правильно настроена с Active Directory.
2. Если аутентификация с Kerberos на Windows невозможна, используйте следующую команду для регистрации машины.

```
ksetup /addkdc DOMAIN.TO.ADD address.of.kerberos.server
```

`DOMAIN.TO.ADD` — это ваше доменное имя, `address.of.kerberos.server` — адрес Kerberos Key Distribution Center (Active Directory Controller при использовании решения Microsoft). Учтите, что в учётных данных доменное имя должно быть в верхнем регистре (например, user@EXAMPLE.COM).

Synthetic использует аутентификацию Kerberos, выполняя команду `kinit`. Подробности см. в [документации MIT Kerberos — kinit](https://dt-url.net/pr43wj6).

Частное расположение на Linux должно быть правильно настроено для получения билета от Kerberos Key Distribution Center. Убедитесь, что расположение имеет следующее:

* Установленные пакеты для Kerberos-клиента (workstation).
* Правильно настроенный файл `/etc/krb5.conf` (или конфигурационный файл, указанный переменной окружения `KRB5_CONFIG`).

Конфигурация зависит от дистрибутива Linux. Дополнительную информацию можно найти в официальной документации.

* Ubuntu:

  + `sudo apt install krb5-user`
  + Подробнее: [Документация Ubuntu Server — Базовая аутентификация рабочей станции](https://dt-url.net/3g03w9p)
* Red Hat/Rocky:

  + `yum install krb5-workstation krb5-libs`
  + Подробнее: [Документация Red Hat — Настройка Kerberos-клиента](https://dt-url.net/1u23wq7)

## Соответствие FIPS для Synthetic

ActiveGate версии 1.315+

### Установка

Для установки Synthetic-enabled ActiveGate в режиме соответствия FIPS необходимо добавить флаг `--fips-mode`; см. также [настройку установки ActiveGate для соответствия FIPS](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#fips-compliant-mode "Узнайте о параметрах командной строки для ActiveGate на Linux.").

```
/bin/bash ./Dynatrace-ActiveGate-Linux.sh --enable-synthetic --fips-mode
```

Обратите внимание, что режим соответствия FIPS нельзя изменить после установки. Для смены режима необходимо удалить ActiveGate и переустановить его с нужными параметрами.
Кроме того, если вы планируете выполнять браузерные мониторы, потребуется дополнительная настройка, описанная в разделах [Настройка прокси для режима FIPS](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-proxy "Узнайте, как настроить свойства ActiveGate для работы через прокси.") и [Настройка прокси для режима FIPS с корпоративным прокси](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-corporate-proxy "Узнайте, как настроить свойства ActiveGate для работы через прокси.").

### Требования и ограничения

* Требуется операционная система с включённым режимом FIPS; см. также [Соответствие FIPS для ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-fips-compliance "Узнайте о соответствии ActiveGate стандарту FIPS.").
* В настоящее время поддерживаются следующие операционные системы:

  + Ubuntu Pro 22.04
  + Red Hat Enterprise Linux 9
* Частные расположения Synthetic на Kubernetes в настоящее время не поддерживаются.

### Обеспечение соответствия

Для обеспечения соответствия FIPS для трафика браузерного монитора его необходимо маршрутизировать через локальный перехватывающий прокси, который шифрует трафик с использованием криптографической библиотеки, сертифицированной по FIPS. Подробности см. в разделе [Настройка прокси для режима FIPS](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-proxy "Узнайте, как настроить свойства ActiveGate для работы через прокси.").

Для HTTP-мониторов используется сертифицированная по FIPS криптографическая библиотека [Amazon Corretto Crypto Provider](https://github.com/corretto/amazon-corretto-crypto-provider/), которая использует AWS-LC-FIPS 2.x в качестве криптографического модуля. См. [Сертификат №4816](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4816).

Synthetic-enabled ActiveGate в режиме соответствия FIPS поддерживает тот же набор шифровальных наборов, что и [обычный ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-fips-compliance#supported-cipher-suites "Узнайте о соответствии ActiveGate стандарту FIPS.").

## Часто задаваемые вопросы

Как проверить подлинность скачанных пакетов Chrome(-ium)?

Chromium

Chrome for Testing

Каждый архив `tgz` хранится в корзине S3 вместе с файлом подписи `*.tgz.sig`. Чтобы проверить подлинность пакетов на вашем диске:

1. Скачайте файл подписи. Имя файла совпадает с архивом пакетов, но с расширением `sig`. Например, для Chromium 140:

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
3. Проверьте временну́ю метку подписи.

   Вы также можете получить точную временну́ю метку подписи. Скачайте файл `*.tgz.sig.tsr` из того же расположения, что и установочные пакеты и подпись, и выполните следующую команду:

   ```
   openssl ts -reply -in chromium.tgz.sig.tsr -text
   ```

Каждый архив `zip` хранится в корзине S3 вместе с файлом подписи `*.zip.sig`. Чтобы проверить подлинность пакетов на вашем диске:

1. Скачайте файл подписи. Имя файла совпадает с архивом пакетов, но с расширением `sig`. Например, для Chrome for Testing 141.0.7390.122:

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
3. Проверьте временну́ю метку подписи.

   Вы также можете получить точную временну́ю метку подписи. Скачайте файл `*.zip.sig.tsr` из того же расположения, что и установочные пакеты и подпись, и выполните следующую команду:

   ```
   openssl ts -reply -in chrome.zip.sig.tsr -text
   ```

Можно ли использовать прокси с Synthetic-enabled ActiveGate?

Начиная с ActiveGate версии 1.175+ ActiveGate, выполняющий синтетические мониторы, может подключаться через прокси как к Dynatrace Cluster, так и к тестируемому ресурсу. Дополнительную информацию см. в разделе [Настройка прокси для частного синтетического мониторинга](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Узнайте, как настроить свойства ActiveGate для работы через прокси.").

Можно ли обновить более раннюю версию ActiveGate до 1.169+ и настроить его для использования с частными синтетическими мониторами?

Нет, для выполнения мониторов из частных расположений необходима чистая установка ActiveGate специально для целей синтетического мониторинга.

Можно ли включить Synthetic на существующей установке ActiveGate?

Частные расположения Synthetic требуют чистой установки ActiveGate специально для целей синтетического мониторинга.

Ручного редактирования файла `custom.properties` недостаточно для включения возможности выполнения синтетических мониторов на ActiveGate.

## Устранение неполадок

[Скриншоты в результатах браузерного монитора не отображаются](https://dt-url.net/mfw2xmb)

Дополнительную информацию по устранению неполадок см. на [форуме Troubleshooting в сообществе Dynatrace](https://dt-url.net/dy122xtf).

## Связанные разделы

* [Synthetic locations API v2 - POST a location](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/post-a-location "Создание частного расположения Synthetic через Synthetic v2 API.")