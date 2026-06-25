---
title: Управление частными расположениями Synthetic
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations
scraped: 2026-05-12T11:32:18.628329
---

# Управление частными расположениями Synthetic

# Управление частными расположениями Synthetic

* How-to guide
* 10-min read
* Updated on Mar 09, 2026
* Early Access

[Добавьте частное расположение Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#add "Узнайте, как создать частное расположение для синтетического мониторинга.") и анализируйте использование ёмкости на странице глобальных настроек **Private synthetic locations** (найдите страницу **Private synthetic locations** через поиск).

Synthetic-enabled ActiveGate версии 1.217+

Dynatrace версии 1.218+

## Общий статус расположения

Частные расположения Synthetic в вашей среде отображаются с зелёными, жёлтыми, красными или серыми индикаторами общего статуса использования ёмкости. Вы можете видеть тип и количество синтетических мониторов, а также количество Synthetic-enabled ActiveGate, назначенных каждому расположению.

Выберите тип монитора (**HTTP** или **Browser**) для просмотра списка синтетических мониторов этого типа в данном расположении.

Вы можете выбрать несколько расположений для массового управления [обработкой сбоев](#outage-handling). Установите флажок рядом с каждым расположением, которым хотите управлять.

![Private Synthetic location settings](https://dt-cdn.net/images/pvtsyntheticlocations-1400-8d3260f571.png)

Настройки частного расположения Synthetic

Цветной индикатор статуса для каждого расположения показывает, не перегружено ли оно по использованию ёмкости, что позволяет принимать взвешенные решения о добавлении ActiveGate для запуска дополнительных мониторов. (Также проверьте [требования к системе и оборудованию для частных расположений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые ОС, версии Chromium и требования к оборудованию.").)

Для расчёта использования на каждом ActiveGate Dynatrace выделяет ресурсы CPU и RAM для запуска каждого типа монитора. Выделение ресурсов на тип монитора преобразуется в максимальное количество одновременных выполнений мониторов в любой момент времени. Фактический расчёт использования ёмкости по типу монитора (см. раздел [Детали расположения](#location-details) ниже) основан на количестве одновременно выполняемых мониторов по сравнению с максимально допустимым количеством одновременных выполнений за предшествующие 30 минут.

Например, ActiveGate может поддерживать два одновременных выполнения браузерных мониторов в данный момент. Однако в зависимости от продолжительности выполняемых мониторов это может соответствовать более чем двум мониторам, выполняемым за заданный период. Например, один 55-секундный монитор и три 10-секундных монитора могут быть выполнены в течение одной минуты без более чем двух одновременных выполнений в любой момент.

Метрики использования ёмкости по типу монитора дают точное представление о работоспособности расположения Synthetic и могут использоваться для построения графиков и создания оповещений. Обязательно разбивайте эти метрики по расположению (см. раздел [Детали расположения](#location-details) ниже).

| Значок статуса | Описание |
| --- | --- |
| Зелёный круг | Использование ёмкости каждого типа синтетических мониторов ниже 80%, что является желательным показателем. |
| Жёлтый круг | Этот значок может означать любое из следующего: использование ёмкости хотя бы одного типа синтетических мониторов превышает 80%; нет резервирования, поскольку сбой любого ActiveGate или Synthetic engine может привести к превышению максимальной ёмкости, или к расположению назначен только один ActiveGate. |
| Красный круг | Использование ёмкости хотя бы одного типа синтетических мониторов в данном расположении превышает 90%, либо выполняются не все синтетические мониторы, назначенные на это расположение. Обратите внимание, что некоторые выполнения мониторов могут быть пропущены при всплесках использования ёмкости по типу монитора, например при одновременном обновлении нескольких мониторов. Этот значок также отображается, когда все ActiveGate или все Synthetic engine в расположении не работают. Если расположение недоступно или Synthetic engine/ActiveGate находится в автономном режиме, синтетические мониторы, назначенные на это расположение, не будут выполняться. |
| Серый круг | Данные отсутствуют: например, когда версии ActiveGate ниже 1.217 и данные об использовании ёмкости не могут быть собраны. |

## Детали расположения

Выберите расположение для просмотра разбивки его общего статуса по использованию ёмкости на тип монитора. Для каждого типа монитора вы можете видеть количество мониторов и запланированных выполнений в час, а также процент использования ёмкости.

* HTTP monitors
* High-resource HTTP monitors
* Browser monitors
* Network Availability monitors

Данные об использовании по типу монитора недоступны, когда все ActiveGate или Synthetic engine в расположении не работают.

ActiveGate, назначенные на расположение, перечислены и отображаются красным цветом при отключении Synthetic engine или самого ActiveGate; в столбце **Status** отображается соответствующее сообщение. Отсюда можно добавлять или удалять ActiveGate. Обратите внимание, что кнопка **Add ActiveGate** недоступна, когда нет ActiveGate для назначения на расположение: это можно проверить в **Deployment Status**.

![Private location details in previous Dynatrace](https://dt-cdn.net/images/screenshot-2025-10-22-171901-1356-64e2b3b050.png)

Детали частного расположения в предыдущем Dynatrace

Метрики работоспособности каждого типа монитора доступны для построения графиков и создания оповещений. Например, выберите метрику **Synthetic - Browser - Engine Utilization** в [браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просмотр метрик в браузере метрик Dynatrace.") или [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты."). Настоятельно рекомендуется разбивать эти метрики по расположению для получения точного представления о работоспособности расположения.

![Synthetic monitors metrics in Data Explorer Classic](https://dt-cdn.net/images/screenshot-2025-10-22-174729-1400-717532af10.png)

Метрики синтетических мониторов в Data Explorer Classic

### Автообновление браузера

Вы можете включить **Enable Chrome(-ium) auto-update** на уровне расположения, то есть для всех ActiveGate, назначенных в частное расположение. Автообновление браузера происходит как при ручном, так и при автоматическом обновлении ActiveGate и Synthetic engine.

Поскольку для гладкого и безопасного выполнения браузерных мониторов из вашего частного расположения рекомендуется использовать [последнюю поддерживаемую версию браузера](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#browser-linux "Поддерживаемые ОС, версии Chromium и требования к оборудованию."), автообновление браузера включено по умолчанию для расположений с ActiveGate на базе Linux. Если вы не хотите автоматически обновлять браузер, например для использования конкретной версии или в офлайн-среде, отключите переключатель **до запуска обновления ActiveGate**.

Эта настройка применяется только к ActiveGate на базе Linux; на ActiveGate на базе Windows браузер всегда обновляется при обновлениях Synthetic engine. Если в вашем расположении есть только ActiveGate на базе Windows, переключатель включён, но неактивен.

Успешное автообновление браузера требует доступа к системным (OS) репозиториям для зависимостей браузера и доступа к `https://synthetic-packages.s3.amazonaws.com` для пакетов браузера. Если вы включили [пользовательский локальный репозиторий](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Узнайте, как создать частное расположение для синтетического мониторинга."), пакеты браузера (но не зависимости) должны быть доступны по адресу указанного HTTP-сервера. См. [Автообновление браузера из пользовательского репозитория](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#autoupdate-custom-repo "Анализ и управление использованием ресурсов в частных расположениях Synthetic.").

Если автообновление браузера завершается неудачей по этой или другой причине, вы увидите сообщение. Рекомендуем либо выполнить требования для автообновления (например, обеспечить доступ к репозиториям), либо отключить автообновление браузера для вашего частного расположения.

* Настоятельно рекомендуется поддерживать актуальность версий Linux-based Synthetic-enabled ActiveGate и браузера: Dynatrace поддерживает версии браузера не более чем на две версии позади [последней поддерживаемой версии](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#browser-linux "Поддерживаемые ОС, версии Chromium и требования к оборудованию.") для конкретного выпуска ActiveGate. Если вы не используете автообновление браузера, вы можете [обновить браузер вручную](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser-manual "Анализ и управление использованием ресурсов в частных расположениях Synthetic.").
* Если вы отключили автообновление браузера, вы можете [вручную обновить браузер](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser-manual "Анализ и управление использованием ресурсов в частных расположениях Synthetic.") для каждого ActiveGate. Однако автообновление браузера обязательно при использовании [пользовательских репозиториев](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Узнайте, как создать частное расположение для синтетического мониторинга."). См. [Автообновление браузера из пользовательского репозитория](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#autoupdate-custom-repo "Анализ и управление использованием ресурсов в частных расположениях Synthetic.").
* Автообновление обновляет браузер до последней версии, предоставляемой Dynatrace для выпуска ActiveGate. В некоторых случаях это может отличаться от [последней поддерживаемой Dynatrace версии браузера](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#browser-linux "Поддерживаемые ОС, версии Chromium и требования к оборудованию.") для выпуска ActiveGate.

Также ознакомьтесь с информацией об [установке браузера и других зависимостей вручную (только Linux)](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#manual "Узнайте, как создать частное расположение для синтетического мониторинга.").

### Обработка сбоев расположения

Для каждого расположения включите соответствующие переключатели для генерации проблем при недоступности расположения или любого из его ActiveGate/Synthetic engine:

* Можно генерировать проблему при полной недоступности расположения (все назначенные ActiveGate или Synthetic engine находятся в автономном режиме).
* Можно генерировать проблему при отключении любого отдельного ActiveGate или Synthetic engine, назначенного в расположение.

  Например, если в расположении два ActiveGate и оба переключателя проблем включены, при недоступности расположения вы увидите три проблемы: одну для всего расположения и по одной для каждого отключённого ActiveGate.
* Дополнительно можно настроить отображение баннерного уведомления в верхней части веб-интерфейса Dynatrace при недоступности всего расположения или любого отдельного ActiveGate/Synthetic engine.

  ![Banner notification](https://dt-cdn.net/images/pvtsyntheticlocationbannernotification-1290-d2e3105395.png)

  Баннерное уведомление

На главной странице настроек со списком всех частных расположений Synthetic вы можете выбрать несколько расположений для массового управления обработкой сбоев.

1. Установите флажок рядом с каждым расположением, которым хотите управлять.
2. Выберите **Edit** в нижнем левом углу страницы.

   ![Bulk edit locations](https://dt-cdn.net/images/pvtsyntheticlocationbulkedit-1852-dcc12815fd.png)

   Массовое редактирование расположений
3. Выберите соответствующий флажок обработки сбоев.
4. Включите/отключите переключатель под флажком. Это перезапишет соответствующую настройку для выбранных расположений.

   ![Bulk edit location outage handling](https://dt-cdn.net/images/pvtsyntheticlocationbulkedit2-1296-3e4a8e3646.png)

   Массовое редактирование обработки сбоев расположений
5. **Save changes**.

## Ручное обновление браузера из S3

Если у вас офлайн-среда или вы установили ActiveGate вручную из-за управления зависимостями или ограниченного доступа к Amazon S3, необходимо обновлять браузер и зависимости вручную.

Браузер необходимо обновлять вручную для каждого ActiveGate, и процедура немного отличается в зависимости от операционной системы. Обратите внимание, что ручное обновление браузера применяется только к ActiveGate на базе Linux; на ActiveGate на базе Windows браузер обновляется автоматически при обновлениях Synthetic engine.

Предварительные условия:

* Убедитесь, что **Enable Chrome(-ium) auto-update** отключён для вашего частного расположения в **Settings** > **Web and Mobile monitoring** > **Private Synthetic locations**. Если вы отключите автообновление для расположения, необходимо будет обновлять браузер вручную на каждом ActiveGate, назначенном в это расположение.
* Убедитесь, что вы можете подключиться к `https://synthetic-packages.s3.amazonaws.com` для доступа к пакетам браузера.

* Synthetic engine будет использовать новую версию браузера после завершения обновления: обратите внимание, что статус обновляется раз в час, поэтому может потребоваться до часа для обновления версии браузера, отображаемой для вашего ActiveGate в **Deployment Status**.
* Настоятельно рекомендуется поддерживать актуальность версий Linux-based Synthetic-enabled ActiveGate и браузера: Dynatrace поддерживает версии браузера не более чем на две версии позади [последней поддерживаемой версии](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#browser-linux "Поддерживаемые ОС, версии Chromium и требования к оборудованию.") для конкретного выпуска ActiveGate. (См. также [Обновление браузера](#browser).)
* Настоятельно рекомендуется обновлять все ActiveGate в расположении до одной и той же версии.
* См. также [Обновление браузера](#browser) и [Автообновление браузера из пользовательского репозитория](#autoupdate-custom-repo).

Начиная с ActiveGate 1.331 на Ubuntu Server 20.04 и 22.04 используется Chrome for Testing. Дистрибутив Chromium snap больше не поддерживается.
Если у вас есть автоматизация для обновления браузера, переведите её на использование Chrome for Testing. Подробности см. в [руководстве сообщества](https://dt-url.net/il0363p).

Ubuntu (snap)

Red Hat Enterprise Linux

Amazon Linux 2023, Ubuntu и Oracle Linux 9 (Chrome for Testing)

Этот раздел актуален только для выпусков 1.329 и более ранних для Ubuntu Server 20.04 и 22.04.

1. Если ваши версии ActiveGate и Chromium устарели или не обновлялись несколько выпусков, проверьте и при необходимости переустановите зависимости Synthetic Engine и Chromium. См. [инструкции по ручной установке для Ubuntu Server](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#ubuntu20_22 "Узнайте, как создать частное расположение для синтетического мониторинга.") в разделе [Создание частного расположения Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.").
2. Скачайте архив snap-пакетов (Ubuntu Server 20.04 и 22.04). Это безопасный верифицированный архив, размещённый Dynatrace по адресу `https://synthetic-packages.s3.amazonaws.com`. Используйте конкретную команду, указанную для ваших версий ActiveGate и Ubuntu Server в [инструкциях по ручной установке для Ubuntu Server](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#ubuntu20_22 "Узнайте, как создать частное расположение для синтетического мониторинга.").
3. Распакуйте и установите скачанные пакеты. Используйте правильную команду установки для вашей версии Ubuntu Server (проверьте [инструкции по ручной установке для Ubuntu Server](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#ubuntu20_22 "Узнайте, как создать частное расположение для синтетического мониторинга.")).
4. Проверьте обновление Chromium, выполнив следующую команду из каталога установки по умолчанию. Вывод команды должен соответствовать установленной версии Chromium.

   ```
   /opt/dynatrace/synthetic/browser --version
   ```

Если вы установили Chromium вручную, при обновлении не нужно регистрировать экземпляр Red Hat в менеджере подписок или включать репозитории Red Hat или пакеты EPEL.

1. Если ваши версии ActiveGate и Chromium давно не обновлялись, возможно, потребуется повторная установка зависимостей Synthetic engine. См. [инструкции по ручной установке для Red Hat Enterprise Linux, Oracle Linux и Rocky Linux](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#redhat "Узнайте, как создать частное расположение для синтетического мониторинга.") в разделе [Создание частного расположения Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.").
2. Скачайте архив rpm-пакетов. Это безопасный верифицированный архив, размещённый Dynatrace по адресу `https://synthetic-packages.s3.amazonaws.com`. Используйте конкретную команду, указанную для ваших версий ActiveGate и ОС в [инструкциях по ручной установке для Red Hat Enterprise Linux, Oracle Linux и Rocky Linux](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#redhat "Узнайте, как создать частное расположение для синтетического мониторинга.").
3. Распакуйте и установите скачанные пакеты. Следуйте [инструкциям по ручной установке для Red Hat Enterprise Linux, Oracle Linux и Rocky Linux](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#redhat "Узнайте, как создать частное расположение для синтетического мониторинга.").
4. При необходимости отключите автоматическое обновление пакетов Chromium. Обратите внимание, что для Red Hat Enterprise Linux и CentOS блокировка пакетов, однажды выполненная, сохраняется при всех будущих обновлениях.

   ```
   sudo yum -y install yum-plugin-versionlock



   sudo yum versionlock chromium



   sudo yum versionlock chromium-common
   ```
5. Проверьте обновление Chromium, выполнив следующую команду из каталога установки по умолчанию. Вывод команды должен соответствовать установленной версии Chromium.

   ```
   /opt/dynatrace/synthetic/browser --version
   ```

Управление Chrome for Testing отличается от управления Chromium. Для ручного обновления скачайте новую версию и распакуйте её в каталог Chrome for Testing.

В отличие от Chromium на других дистрибутивах, обновления Chrome for Testing не используют менеджеры пакетов. Вы управляете бинарными файлами Chrome вручную, тогда как зависимости управляются системным менеджером пакетов.

Ubuntu Server 20.04 и 22.04

При миграции с дистрибутива Chromium snap сначала обновите ActiveGate, затем установите Chrome for Testing и при необходимости удалите установку Chromium snap.

1. Если ваши версии ActiveGate и Chrome for Testing давно не обновлялись, возможно, потребуется проверить и повторно установить зависимости Synthetic engine и Chrome for Testing. См. [инструкции по ручной установке для Chrome for Testing](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#chrome-for-testing "Узнайте, как создать частное расположение для синтетического мониторинга.") в разделе [Создание частного расположения Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.").
2. Скачайте архив пакетов Chrome for Testing во временное место. Это безопасный верифицированный архив, размещённый Dynatrace по адресу `https://synthetic-packages.s3.amazonaws.com`. Используйте конкретную команду, указанную для вашей версии ActiveGate в [инструкциях по ручной установке для Chrome for Testing](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#chrome-for-testing "Узнайте, как создать частное расположение для синтетического мониторинга."), но измените путь вывода на `/tmp/chrome.zip`.
3. Удалите старый каталог Chrome for Testing, распакуйте новую версию и очистите временные файлы:

   ```
   sudo rm -rf /usr/lib/chrome_for_testing/chrome-linux64



   sudo unzip /tmp/chrome.zip -d /usr/lib/chrome_for_testing



   rm /tmp/chrome.zip
   ```

   Если вы настроили пользовательский каталог Chrome for Testing через переменную окружения `CFT_DIR` или свойство `synthetic_chrome_for_testing_path` в `custom.properties`, замените `/usr/lib/chrome_for_testing` на ваш пользовательский путь в командах выше.
4. Проверьте обновление Chrome for Testing, выполнив следующую команду. Вывод должен соответствовать установленной версии Chrome.

   ```
   /usr/lib/chrome_for_testing/chrome-linux64/chrome --version
   ```

   Synthetic engine немедленно начнёт использовать новую версию Chrome for Testing. Обратите внимание, что статус обновляется раз в час, поэтому может потребоваться до часа для обновления версии Chrome, отображаемой для вашего ActiveGate в **Deployment Status**.

## Автообновление браузера из пользовательского репозитория

Если вы включили [пользовательский локальный репозиторий для установки браузера](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Узнайте, как создать частное расположение для синтетического мониторинга."), браузер может только автоматически обновляться. Следуйте этой процедуре для автообновления браузера через тот же пользовательский репозиторий.

1. После установки ActiveGate укажите пользовательский репозиторий ActiveGate в [секции `[synthetic]` файла `custom.properties`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Узнайте, какие свойства ActiveGate можно настроить.") в каталоге `/var/lib/dynatrace/gateway/config`. Это позволяет автоматически обновлять браузер из пользовательского репозитория при ручном или автоматическом обновлении Synthetic engine.

   ```
   [synthetic]



   chromium_repo = https://172.18.0.100/chromium-repo
   ```
2. Включите **Enable Chrome(-ium) auto-update** для вашего частного расположения в глобальных настройках: перейдите в **Settings** > **Web and mobile monitoring** > **Private Synthetic locations**. Выберите ваше расположение и включите переключатель в разделе **Chrome(-ium) update**.

   Обратите внимание, что настройка автообновления браузера в интерфейсе применяется ко всем ActiveGate, назначенным в ваше частное расположение.
3. Убедитесь, что пакеты браузера, необходимые для обновления, доступны в расположении пользовательского репозитория. Браузер затем автоматически обновляется из пользовательского репозитория при обновлениях ActiveGate и Synthetic engine.

Параметр автообновления браузера

Если вы не укажете пользовательский репозиторий в `custom.properties`, браузер будет скачан и обновлён из S3 при ручном или автоматическом обновлении ActiveGate и Synthetic engine.