---
title: Требования для частных расположений Synthetic
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic
scraped: 2026-05-12T11:08:10.710699
---

# Требования для частных расположений Synthetic

# Требования для частных расположений Synthetic

* Reference
* 15-min read
* Updated on Apr 28, 2026

Убедитесь, что хост, который вы планируете использовать для частного расположения, соответствует следующим требованиям.

Информация о прекращении поддержки

Новых версий Chromium для Red Hat/Oracle Linux/Rocky Linux 8 после версии 133 не выходит. По соображениям безопасности и стабильности принято решение прекратить поддержку установки **Synthetic-enabled** ActiveGate на Red Hat/Oracle Linux/Rocky Linux 8 после версии ActiveGate 1.325.

Для обеспечения непрерывности и безопасности ваших синтетических мониторов рекомендуем перенести Synthetic-enabled ActiveGate на одну из [поддерживаемых операционных систем](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#linux-supported-os "Поддерживаемые ОС, версии Chromium и требования к оборудованию."), например Red Hat/Oracle Linux/Rocky Linux 9.

Версия ActiveGate 1.325 является **последней поддерживаемой Synthetic-enabled** версией ActiveGate для Red Hat/Oracle Linux/Rocky Linux 8.

Начиная с Dynatrace версии 1.326 будут введены механизмы, препятствующие обновлению Synthetic-enabled ActiveGate на Red Hat/Oracle Linux/Rocky Linux 8 выше версии 1.325.

* Актуальные минимально поддерживаемые версии ActiveGate см. в [примечаниях к выпуску ActiveGate](/managed/whats-new/activegate "Примечания к выпуску Dynatrace ActiveGate").

## Антивирусное и антивредоносное ПО

Антивирусное и антивредоносное программное обеспечение может негативно влиять на возможности синтетического мониторинга Dynatrace.
Такое ПО может блокировать браузер или процессы Dynatrace, выполняющие синтетические мониторы, вызывать сбои установки или обновления Synthetic-enabled ActiveGate, мешать сетевому взаимодействию и влиять на надёжность измерений.

Для обеспечения стабильности и производительности рассмотрите добавление перечисленных ниже каталогов и процессов в список разрешённых или исключение их из политики проверки.
Учтите, что исключения антивируса, как правило, отключают сканирование файлов, но не поведенческий мониторинг или хуки на уровне ядра. Они остаются активными и могут влиять на взаимодействие Synthetic Engine и браузера с системными библиотеками.
В результате даже исключённые процессы могут испытывать нарушения доступа или повреждение памяти.

Прежде чем обращаться в службу поддержки Dynatrace для устранения неполадок с вашими частными расположениями Synthetic, убедитесь, что антивирусное или антивредоносное программное обеспечение исключено как возможная причина.

Ниже приведён минимальный список процессов и каталогов, необходимых для работы Dynatrace Synthetic.
Не гарантируется корректная работа сервиса только с этими исключениями.
Взаимодействуйте с вашим поставщиком, чтобы убедиться, что все ожидаемые действия Dynatrace правильно разрешены.

**Каталоги:**

* Все каталоги, в пути которых есть слово `synthetic`. Обзор используемых каталогов см. в разделе [Каталоги ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files#default-activegate-directories--windows "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.").

**Процессы:**

* chrome
* vucwrapper
* java

## Требования к операционной системе

Свежеустановленный ActiveGate может запускать ваши частные синтетические мониторы (как HTTP, так и браузерные) на следующих операционных системах.

### Windows

#### Поддерживаемые операционные системы

| Windows OS | Версии |
| --- | --- |
| Windows Server | 2016, 2019, 2022 |

#### Версии браузера на Windows

На Windows установочный пакет ActiveGate включает браузер Chromium, используемый для запуска браузерных мониторов. В таблице ниже показаны версии Chromium, поставляемые с соответствующими версиями ActiveGate.

| Версия ActiveGate | Версия включённого браузера |
| --- | --- |
| 1.337 | 146 |
| 1.335 | 146 |
| 1.333 | 144 |
| 1.331 | 143 |
| 1.329 | 142 |
| 1.327 | 141 |
| 1.325 | 140 |
| 1.323 | 139 |
| 1.321 | 138 |
| 1.319 | 138 |
| 1.317 | 137 |
| 1.315 | 136 |
| 1.313 | 135 |

#### Неподдерживаемые версии Windows только для тестовых целей

Если вы хотите только протестировать частные расположения Synthetic на непроизводственном хосте, например на собственном рабочем столе, вы можете установить Synthetic-enabled ActiveGate на неподдерживаемые версии Windows, такие как Windows 10 или Windows 11.

Начиная с ActiveGate версии 1.263+ Synthetic-enabled ActiveGate больше не работает на Windows Server 2012 даже для тестовых целей. [Google прекратила поддержку Windows 2012 Server в Chromium 110](https://dt-url.net/e2026id), который поставляется с [установочным пакетом ActiveGate версии 1.263](#browser-windows).

### Linux

#### Поддерживаемые операционные системы

| Дистрибутив Linux | Версии |
| --- | --- |
| Red Hat Enterprise Linux[1](#fn-1-1-def) | 9.4, 9.6, 9.7 |
| Ubuntu | 20.04, 22.04, 24.04 |
| Amazon Linux | 2023 |
| Oracle Linux[2](#fn-1-2-def) | 9.6, 9.7 |
| Rocky Linux[3](#fn-1-3-def) | 9.7 |

1

Synthetic-установщик можно установить на любые минорные выпуски Red Hat Enterprise Linux 9. Однако рекомендуется использовать версии, указанные в этой таблице, поскольку они имеют Extended Life-cycle Support (ELS) согласно [циклу жизни Red Hat Enterprise Linux](https://access.redhat.com/support/policy/updates/errata).

2

Synthetic-установщик можно установить на любые минорные выпуски Oracle Linux 9. Однако рекомендуется использовать последние актуальные версии согласно документации для [Oracle Linux 9](https://docs.oracle.com/en/operating-systems/oracle-linux/9/).

3

Synthetic-установщик можно установить на любые минорные выпуски Rocky Linux 9. Однако рекомендуется использовать последние актуальные версии согласно [руководству по выпускам Rocky Linux](https://wiki.rockylinux.org/rocky/version/#current-supported-releases).

#### Устаревшие операционные системы

| Дистрибутив Linux | Версии |
| --- | --- |
| Red Hat Enterprise Linux | 7.9[1](#fn-2-1-def) |
| CentOS | 7.9[1](#fn-2-1-def) |
| Amazon Linux | 2[2](#fn-2-2-def) |
| Red Hat Enterprise Linux | 8.8[3](#fn-2-3-def) |
| Red Hat Enterprise Linux | 8.10[3](#fn-2-3-def) |
| Oracle Linux | 8.10[3](#fn-2-3-def) |
| Rocky Linux | 8.10[3](#fn-2-3-def) |

1

ActiveGate версии 1.305 является последней версией с поддержкой Synthetic-enabled для Red Hat/CentOS 7.

2

ActiveGate версии 1.307 является последней версией с поддержкой Synthetic-enabled для Amazon Linux 2.

3

ActiveGate версии 1.325 является последней версией с поддержкой Synthetic-enabled для Red Hat/Oracle Linux/Rocky Linux 8.

#### Версии браузера на Linux

Настоятельно рекомендуется поддерживать актуальность версий Linux-based Synthetic-enabled ActiveGate и браузера: Dynatrace поддерживает версии браузера не более чем на две версии позади последней поддерживаемой Dynatrace версии для конкретного выпуска ActiveGate. Например, если последняя поддерживаемая версия браузера 103, Dynatrace поддерживает браузер вплоть до версии 101. Если поставляемая версия браузера значительно старше для конкретной ОС, поддерживается только поставляемая версия. Информацию об обновлении браузера см. в разделах об [автоматическом](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser "Анализ и управление использованием ресурсов в частных расположениях Synthetic.") и [ручном](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#browser-manual "Анализ и управление использованием ресурсов в частных расположениях Synthetic.") обновлении.

На Linux установщик ActiveGate скачивает зависимости браузера, необходимые для Synthetic engine. На Red Hat и Rocky Linux необходимо включить определённые репозитории, из которых устанавливаются зависимости. Dynatrace предоставляет все необходимые команды через веб-интерфейс. Подробные инструкции см. в разделе [Создание частного расположения Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.").

При [установке ActiveGate и браузера из пользовательского локального репозитория](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Узнайте, как создать частное расположение для синтетического мониторинга.") необходимо разрешить все зависимости и включить необходимые репозитории самостоятельно: пользовательский репозиторий можно использовать только для пакетов браузера, но не для их зависимостей. Поместите архив пакета браузера и файл подписи в пользовательский репозиторий для установки. Если ваш файл архива пакетов — `https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip` (Chrome for Testing 143 для Ubuntu на ActiveGate версии 1.333), файл подписи можно найти, добавив `.sig` к URL: `https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip.sig`.

Из-за изменений в доступности пакета `libdav1d.so.6` версии Chromium старее 130 нельзя установить на Red Hat/Rocky Linux 9.
Подробности см. в [руководстве по устранению неполадок](https://dt-url.net/x303x5f).

| Версия ActiveGate | Последняя поддерживаемая версия Chromium: Red Hat/Rocky Linux 9 | Последняя поддерживаемая версия Chrome for Testing: Amazon Linux 2023, Ubuntu, Oracle Linux 9 |
| --- | --- | --- |
| 1.337 | 146 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-146.0.7680.177-1.el9.tgz) | [146](https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-146.0.7680.178.zip) |
| 1.335 | 146 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-146.0.7680.177-1.el9.tgz) | [146](https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-146.0.7680.178.zip) |
| 1.333 | 144 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-144.0.7559.132-1.el9.tgz) | [144](https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-144.0.7559.133.zip) |
| 1.331[3](#fn-3-3-def) | 143 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-143.0.7499.192-1.el9.tgz) | [143](https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-143.0.7499.192.zip) |

| Версия ActiveGate | Последняя поддерживаемая версия Chromium: Red Hat/Oracle/Rocky Linux | Последняя поддерживаемая версия Chromium: Ubuntu 20 и 22 | Последняя поддерживаемая версия Chrome for Testing: Amazon Linux 2023, Ubuntu 24, Oracle Linux 9 |
| --- | --- | --- | --- |
| 1.329 | 142 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-142.0.7444.175-2.el9.tgz) | 142 [Ubuntu 20.04 и 22.04](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-142.0.7444.175-3313.tgz) | [142](https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-142.0.7444.175.zip) |
| 1.327 | 141 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-141.0.7390.122-1.el9.tgz) | 141 [Ubuntu 20.04 и 22.04](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-141.0.7390.122-3285.tgz) | [141](https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-141.0.7390.122.zip) |
| 1.325 | 133 [Red Hat/Oracle/Rocky Linux 8](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 140 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-140.0.7339.185-1.el9.tgz) | 140 [Ubuntu 20.04 и 22.04](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-140.0.7339.185-3251.tgz) | 140 |
| 1.323 | 133 [Red Hat/Oracle/Rocky Linux 8](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 139 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-139.0.7258.138-1.el9.tgz) | 139 [Ubuntu 20.04 и 22.04](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-139.0.7258.138-3235.tgz) | 139 |
| 1.321 | 133 [Red Hat/Oracle/Rocky Linux 8](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 138 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-138.0.7204.157-1.el9.tgz) | 138 [Ubuntu 20.04 и 22.04](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-138.0.7204.157-3203.tgz) | 138 |
| 1.319 | 133 [Red Hat/Oracle/Rocky Linux 8](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 138 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-138.0.7204.100-1.el9.tgz) | 138 [Ubuntu 20.04 и 22.04](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-138.0.7204.100-3199.tgz) | 138 |
| 1.317 | 133 [Red Hat/Oracle/Rocky Linux 8](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 137 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-137.0.7151.103-1.el9.tgz) | 137 [Ubuntu 20.04 и 22.04](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-137.0.7151.103-3169.tgz) | 137 |
| 1.315 | 133 [Red Hat/Oracle/Rocky Linux 8](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 136 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-136.0.7103.59-1.el9.tgz) | 136 [Ubuntu 20.04 и 22.04](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-136.0.7103.59-3121.tgz) | 136 |
| 1.313[2](#fn-3-2-def) | 133 [Red Hat/Oracle/Rocky Linux 8](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 135 [Red Hat/Rocky Linux 9](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-135.0.7049.95-1.el9.tgz) | 135 [Ubuntu 20.04 и 22.04](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-135.0.7049.95-3110.tgz) | 135 |

1

Введена поддержка Ubuntu 24.

2

Введена поддержка Oracle Linux 9.

3

Ubuntu Server 20.04 и 22.04 перешли на использование Chrome for Testing.

#### Фреймворк File Access Policy Daemon (`fapolicyd`)

При некорректной настройке File Access Policy Daemon (`fapolicyd`) может негативно влиять на возможности синтетического мониторинга Dynatrace. Аналогично антивирусному или антивредоносному ПО, `fapolicyd` может блокировать браузер или процессы Dynatrace, ответственные за выполнение синтетических мониторов.

Для обеспечения стабильности и производительности рассмотрите добавление каталогов и процессов в список разрешённых или исключение их из политики. Дополнительную информацию см. в [документации Red Hat по fapolicyd](https://dt-url.net/tn1v0z1x). Прежде чем обращаться в поддержку Dynatrace для устранения неполадок с вашими частными расположениями Synthetic, убедитесь, что `fapolicyd` исключён как источник проблем.

Фреймворк File Access Policy Daemon можно запустить в режиме отладки, в котором все отказы регистрируются, что упрощает поиск отсутствующих правил и устранение неполадок. Подробности о режиме отладки см. в [документации по устранению неполадок, связанных с fapolicyd](https://dt-url.net/e943wcc).

## Требования к оборудованию

### Общие соображения

* Synthetic-enabled ActiveGate предъявляет более высокие требования к оборудованию и системе, чем обычный Environment или Cluster ActiveGate. Настоятельно рекомендуется использовать Synthetic-enabled ActiveGate исключительно для целей синтетического мониторинга.
* При планировании выделения ресурсов необходимо учитывать любые дополнительные компоненты, работающие на хосте. Например, если расположение мониторируется с помощью [OneAgent](/managed/ingest-from/dynatrace-oneagent/oa-requirements "Требования к модулю кода OneAgent") или другого решения глубокого мониторинга, требования к оперативной памяти возрастут.
* Для изменения размера Synthetic-enabled ActiveGate необходимо удалить его и переустановить, например после увеличения ресурсов ActiveGate размера S до требований размера M. Переустановка обязательна до начала использования обновлённых ресурсов для синтетического мониторинга; в противном случае ваш ActiveGate будет по-прежнему отображаться как размер S (**Synthetic Node size**) в **Deployment Status** и будет ограничен лимитами выполнения размера S.

### Руководство по подбору размера

В зависимости от количества тестов, выполняемых в час, Synthetic-enabled ActiveGate должен соответствовать следующим требованиям к оборудованию.

Предельные значения

Расчётные предельные значения, указанные в таблице ниже, определены по результатам внутреннего тестирования. Фактические значения могут варьироваться в зависимости от сложности ваших мониторов.

Узел XS

Узел S

Узел M

Узел L

Узел XS

Хотя узлы XS могут использоваться на ActiveGate на основе Windows Server, они могут не быть оптимальным выбором из-за более высоких требований браузера к ресурсам. Для оптимальной производительности и подготовки к будущим улучшениям рекомендуется иметь не менее 8 ГБ оперативной памяти и 25 ГБ свободного места на диске.

На Linux-системах только с 4 ГБ оперативной памяти растущие требования браузера к ресурсам в сочетании с установкой сторонних инструментов на хосте могут привести к периодической нехватке памяти. Настоятельно рекомендуется перейти на 8 ГБ оперативной памяти для более стабильной и надёжной работы.

|  | Узел с поддержкой браузерных мониторов | Безбраузерный узел |
| --- | --- | --- |
| Минимальное количество ЦП | 2 vCPU | 1 vCPU |
| Минимальное свободное место на диске | 20 ГБ | 17 ГБ |
| Минимальный объём ОЗУ | 4 ГБ | 4 ГБ |
| Минимальный свободный объём ОЗУ | 3 ГБ | 2,7 ГБ |
| Минимальный IOPS диска (Windows) | 100 | 100 |
| Расчётное максимальное количество выполнений HTTP-мониторов/ч[1](#fn-4-1-def) | 300k | 300k |
| Расчётное максимальное количество выполнений высоконагруженных HTTP-мониторов[2](#fn-4-2-def)/ч | 10k | 10k |
| Расчётное максимальное количество выполнений браузерных мониторов/ч | 300 | - |
| Расчётное максимальное количество пакетов NAM ICMP-мониторов/ч[3](#fn-4-3-def) [5](#fn-4-5-def) | 500k | 500k |
| Расчётное максимальное количество запросов NAM TCP-мониторов/ч[4](#fn-4-4-def) [6](#fn-4-6-def) | 1M | 1M |
| Расчётное максимальное количество запросов NAM DNS-мониторов/ч[4](#fn-4-4-def) [7](#fn-4-7-def) | 100k | 100k |

Примечания

1

Рассчитано как 5000 выполнений мониторов (максимум для одной среды) с частотой раз в минуту (максимальная частота).

2

Это HTTP-мониторы на частных расположениях с любым из: скрипты предвыполнения или пост-выполнения, авторизация OAuth2, аутентификация Kerberos.

3

Для NAM-мониторов с типом запроса ICMP ёмкость связана с количеством ICMP echo-запросов (пакетов), отправляемых при выполнении мониторов. Поскольку это количество пакетов может существенно различаться между определёнными мониторами, использование количества выполнений мониторов в качестве ограничения ёмкости было бы неточным.

4

Для NAM-мониторов с типами запросов TCP и DNS ёмкость связана с количеством сетевых соединений (запросов), отправляемых при выполнении мониторов. Поскольку это количество запросов может существенно различаться между определёнными мониторами, использование количества выполнений мониторов в качестве ограничения ёмкости было бы неточным.

5

В ходе нагрузочных тестов, помогших установить пределы ёмкости, NAM ICMP-мониторы были назначены исключительно на расположение с следующими характеристиками. Фактическая ёмкость может отличаться для других сред (например, где мониторируемые цели отвечают медленнее, не предоставляют ответ в течение таймаута, или одновременно выполняются другие типы мониторов).
Мониторы использовали настройки по умолчанию (включая настройки таймаутов по умолчанию и один пакет на запрос) и запускались раз в минуту.
В ходе тестов использовались несколько целевых хостов, все из которых отвечали корректно со средним временем RTT около 200 мс.

6

В ходе нагрузочных тестов, помогших установить пределы ёмкости, NAM TCP-мониторы были назначены исключительно на расположение с следующими характеристиками. Фактическая ёмкость может отличаться для других сред.
Мониторы использовали настройки по умолчанию (включая настройки таймаутов) и запускались раз в минуту.
В ходе тестов использовались несколько целевых хостов и портов, все из которых отвечали корректно со средним временем установки TCP-соединения около 200 мс.

7

В ходе нагрузочных тестов, помогших установить пределы ёмкости, NAM DNS-мониторы были назначены исключительно на расположение с следующими характеристиками. Фактическая ёмкость может отличаться для других сред. Обратите внимание, что DNS-сервер, используемый при разрешении, должен уметь обрабатывать входящие запросы и не считать входящий трафик объектом ограничения или отклонения (например, из-за обнаружения как трафика бота).
Мониторы использовали настройки по умолчанию (включая настройки таймаутов и UDP в качестве транспорта) и запускались раз в минуту.
В ходе тестов использовались несколько целей разрешения, все из которых разрешались корректно со средним временем разрешения DNS около 10 мс.
Использовались публично доступные DNS-серверы: Google (8.8.8.8 и 8.8.4.4) и Cloudflare (1.1.1.1 и 1.1.1.2).

|  | Узел с поддержкой браузерных мониторов | Безбраузерный узел |
| --- | --- | --- |
| Минимальное количество ЦП | 4 vCPU | 2 vCPU |
| Минимальное свободное место на диске | 25 ГБ | 22 ГБ |
| Минимальный объём ОЗУ | 8 ГБ | 8 ГБ |
| Минимальный свободный объём ОЗУ | 5 ГБ | 4 ГБ |
| Минимальный IOPS диска (Windows) | 200 | 200 |
| Расчётное максимальное количество выполнений HTTP-мониторов/ч[1](#fn-5-1-def) | 300k | 300k |
| Расчётное максимальное количество выполнений высоконагруженных HTTP-мониторов[2](#fn-5-2-def)/ч | 20k | 20k |
| Расчётное максимальное количество выполнений браузерных мониторов/ч | 650 | - |
| Расчётное максимальное количество пакетов NAM ICMP-мониторов/ч[3](#fn-5-3-def) [5](#fn-5-5-def) | 1M | 1M |
| Расчётное максимальное количество запросов NAM TCP-мониторов/ч[4](#fn-5-4-def) [6](#fn-5-6-def) | 2M | 2M |
| Расчётное максимальное количество запросов NAM DNS-мониторов/ч[4](#fn-5-4-def) [7](#fn-5-7-def) | 200k | 200k |

Примечания

1-7 (те же формулировки, что для узла XS)

|  | Узел с поддержкой браузерных мониторов | Безбраузерный узел |
| --- | --- | --- |
| Минимальное количество ЦП | 8 vCPU | 4 vCPU |
| Минимальное свободное место на диске | 30 ГБ | 23 ГБ |
| Минимальный объём ОЗУ | 16 ГБ | 16 ГБ |
| Минимальный свободный объём ОЗУ | 8 ГБ | 6,5 ГБ |
| Минимальный IOPS диска (Windows) | 400 | 400 |
| Расчётное максимальное количество выполнений HTTP-мониторов/ч[1](#fn-6-1-def) | 300k | 300k |
| Расчётное максимальное количество выполнений высоконагруженных HTTP-мониторов[2](#fn-6-2-def)/ч | 60k | 60k |
| Расчётное максимальное количество выполнений браузерных мониторов/ч | 1200 | - |
| Расчётное максимальное количество пакетов NAM ICMP-мониторов/ч[3](#fn-6-3-def) [5](#fn-6-5-def) | 1.5M | 1.5M |
| Расчётное максимальное количество запросов NAM TCP-мониторов/ч[4](#fn-6-4-def) [6](#fn-6-6-def) | 3M | 3M |
| Расчётное максимальное количество запросов NAM DNS-мониторов/ч[4](#fn-6-4-def) [7](#fn-6-7-def) | 300k | 300k |

Примечания

1-7 (те же формулировки, что для узла XS)

|  | Узел с поддержкой браузерных мониторов | Безбраузерный узел |
| --- | --- | --- |
| Минимальное количество ЦП | 16 vCPU | 8 vCPU |
| Минимальное свободное место на диске | 40 ГБ | 25 ГБ |
| Минимальный объём ОЗУ | 32 ГБ | 32 ГБ |
| Минимальный свободный объём ОЗУ | 12 ГБ | 10 ГБ |
| Минимальный IOPS диска (Windows) | 750 | 750 |
| Расчётное максимальное количество выполнений HTTP-мониторов/ч[1](#fn-7-1-def) | 300k | 300k |
| Расчётное максимальное количество выполнений высоконагруженных HTTP-мониторов[2](#fn-7-2-def)/ч | 100k | 100k |
| Расчётное максимальное количество выполнений браузерных мониторов/ч | 2200 | - |
| Расчётное максимальное количество пакетов NAM ICMP-мониторов/ч[3](#fn-7-3-def) [5](#fn-7-5-def) | 2M | 2M |
| Расчётное максимальное количество запросов NAM TCP-мониторов/ч[4](#fn-7-4-def) [6](#fn-7-6-def) | 4M | 4M |
| Расчётное максимальное количество запросов NAM DNS-мониторов/ч[4](#fn-7-4-def) [7](#fn-7-7-def) | 400k | 400k |

Примечания

1-7 (те же формулировки, что для узла XS)

### Хранилище и права доступа к файловой системе

В таблице ниже показаны расположения установки по умолчанию (Linux и Windows) для различных каталогов ActiveGate и минимальные требования к размеру. Эта информация взята из раздела [Каталоги ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.").

| Параметр установки | Путь по умолчанию | Мин. размер | Примечания |
| --- | --- | --- | --- |
| `<INSTALL>` | `/opt/dynatrace/` или `%PROGRAMFILES%\dynatrace` | 600 МБ | Для исполняемых файлов, библиотек и связанных файлов: 300 МБ для ActiveGate, 270 МБ для файлов Private Synthetic |
| `<LOGS>` | `/var/log/dynatrace` или `%PROGRAMDATA%\dynatrace` | 1,7 ГБ | 500 МБ для логов ActiveGate, 1 ГБ для логов Private Synthetic, 200 МБ для логов автообновления |
| `<CONFIG>` | `/var/lib/dynatrace` или `%PROGRAMDATA%\dynatrace` | 1 МБ |  |
| `<TEMP>` | `/var/tmp/dynatrace` или `%PROGRAMDATA%\dynatrace` | 21 ГБ[1](#fn-8-1-def) | 1 ГБ для временных файлов ActiveGate (без кешированных установщиков OneAgent и образов контейнеров), 20 ГБ для временных файлов Private Synthetic (включая логи выполнения, кеш и скриншоты) |

1

Для ActiveGate размера XS. Для ActiveGate большего размера требуется больше места из-за логов выполнения.

#### Права доступа к `/tmp`

Synthetic-enabled ActiveGate требует доступ на запись в каталог `/tmp` во время работы. Его зависимости, включая xvfb, используют `/tmp` для хранения временных файлов и данных среды выполнения.
Отсутствие прав записи в этот каталог может привести к непредвиденным сбоям или деградации функциональности.
Убедитесь, что среда хоста предоставляет достаточные права доступа и свободное место в `/tmp` для надёжной поддержки этих операций.

## Связанные разделы

* [Каталоги ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.")