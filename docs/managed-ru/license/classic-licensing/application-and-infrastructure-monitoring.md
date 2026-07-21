---
title: Мониторинг приложений и инфраструктуры (Host Units)
source: https://docs.dynatrace.com/managed/license/classic-licensing/application-and-infrastructure-monitoring
---

# Мониторинг приложений и инфраструктуры (Host Units)

# Мониторинг приложений и инфраструктуры (Host Units)

* 12 мин на чтение
* Обновлено 18 марта 2026 г.

Мониторинг приложений и инфраструктуры Dynatrace обеспечивается установкой единого [Dynatrace OneAgent](/managed/platform/oneagent "Ознакомиться с возможностями мониторинга OneAgent.") на каждом отслеживаемом хосте в среде. OneAgent лицензируется из расчёта на хост (виртуальный или физический сервер).

Однако не все хосты одинаковы по размеру. Более крупные хосты потребляют больше host units, чем хосты меньшего размера. Объём RAM на отслеживаемом сервере используется как мерило для определения размера хоста (то есть сколько host units он составляет). Преимущество такого подхода в его простоте: можно иметь 10 JVM или 1000 JVM, такие факторы не влияют на объём мониторинга, потребляемый средой.

OneAgent может работать в двух разных режимах. По умолчанию OneAgent работает в режиме Full-Stack Monitoring. В качестве альтернативы можно использовать [режим Infrastructure monitoring](/managed/platform/oneagent/monitoring-modes/monitoring-modes#infrastructure-only "Узнать больше о доступных режимах мониторинга при использовании OneAgent."), чтобы отслеживать хосты, для которых не требуется полная видимость стека. Режим Infrastructure потребляет меньше host units, чем режим Full-Stack.

## Host units

В таблице весовых коэффициентов host unit ниже показано, сколько host units потребляется в зависимости от объёма RAM отслеживаемого сервера. Общее потребление host unit рассчитывается как сумма всех host units по всем режимам и отслеживаемым системам. Подробности см. в разделе [Управление лицензиями Dynatrace Managed](/managed/manage/account-management/subscription-and-license/subscription-and-license-managed "Управление лицензиями Dynatrace Managed").

| Макс. RAM | Host units (Full-Stack[1](#fn-1-1-def)) | Host units (Infrastructure[2](#fn-1-2-def)) |
| --- | --- | --- |
| 1,6 ГиБ | 0,10 | 0,03 |
| 4 ГиБ | 0,25 | 0,075 |
| 8 ГиБ | 0,50 | 0,15 |
| 16 ГиБ | 1,0 | 0,3 |
| 32 ГиБ | 2,0 | 0,6 |
| 48 ГиБ | 3,0 | 0,9 |
| 64 ГиБ | 4,0 | 1,0 |
| 80 ГиБ | 5,0 | 1,0 |
| 96 ГиБ | 6,0 | 1,0 |
| 112 ГиБ | 7,0 | 1,0 |
| nx16 ГиБ | n | 1,0 |

1

Когда объём RAM на хосте попадает между значениями, перечисленными в таблице выше, число округляется в большую сторону. Например, хост с 12 ГиБ RAM потребляет 1 host unit, потому что 12 ГиБ находится между 8 ГиБ и 16 ГиБ.

2

Для [режима Infrastructure Monitoring](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнать больше о доступных режимах мониторинга при использовании OneAgent.") действует тот же принцип округления. Если для лицензии Cloud Infrastructure включено ограничение host unit, количество host units, потребляемых хостом, ограничивается значением 1,0. Если у вас есть действующее соглашение, в котором не отражено ограничение `1,0` на host unit на хост, обратитесь к [представителю отдела продаж Dynatrace](https://www.dynatrace.com/contact/).

### Host unit hours

Host unit hour, это показатель потребления host unit за период времени. 1 host unit hour соответствует потреблению 1 host unit в течение 1 часа. Хост с 16 ГиБ RAM (то есть 1 host unit), работающий полные сутки, потребляет 24 host unit hours.

Пример расчёта host unit hours

Например, допустим, доступно 1000 host unit hours и нужно отслеживать хост с 64 ГиБ RAM (что соответствует 4 host units). Если оставить хост работающим полные сутки, он потребит 96 host unit hours.  
`4 (host units) × 24 (часа в сутках) = 96 (host unit hours)`

1000 host unit hours будут израсходованы чуть более чем за 10 дней.  
`4 (host units) × 24 (часа) × 10 (дней) = 960 host unit hours`

Истинная параллельность (true concurrency) в расчётах host unit hours

Каждую минуту Dynatrace рассчитывает потребление host unit на основе истинной параллельности. Это означает, что два хоста, работающие в течение одного и того же часа, потребят два host units, если оба хоста работают одновременно. Host unit hours считаются в календарных часах (например, с 10:00 до 11:00), а не в часах использования (например, с 10:23 до 11:23).

Если хост работает менее 5 минут, это не засчитывается в квоту host unit hour. Хост, работающий 5 минут или дольше, округляется до `1 host unit hour`.

Когда мониторинг хоста по какой-либо причине останавливается, потреблённые этим хостом host units освобождаются и становятся доступны другому хосту примерно через пять минут.

#### Пример 1

Есть хост с 16 ГиБ RAM (что равно 1 host unit), работающий с 10:00 до 10:30. В 10:30 запускается другой хост того же размера. Dynatrace считает это одним host unit, потому что хосты не работают одновременно.

#### Пример 2

Первый хост запускается в 10:00, а другой хост запускается в 10:30. Затем оба хоста работают вместе в течение 30 минут и останавливаются одновременно. Dynatrace считает это 2 host units, потому что оба хоста работают одновременно.

#### Пример 3

Один хост размером 16 ГиБ RAM запускается и останавливается три раза в течение часа:

`12:10 - запуск сервера`  
`12:20 - остановка сервера`

`12:30 - запуск сервера`  
`12:40 - остановка сервера`

`12:50 - запуск`  
`13:00 - остановка`

Такой сценарий соответствует `1 host unit hour`, потому что учитывается истинная параллельность.

#### Пример 4

Есть хост с 16 ГиБ RAM (что равно 1 host unit), работающий с 10:23 до 11:23. Поскольку хост работает в течение 2 календарных часов (с 10:00 до 11:00 и с 11:00 до 12:00), это соответствует `2 host unit hours`.

Host unit hours в бесплатной пробной версии

Host unit hours используются для бесплатных пробных версий Dynatrace. При регистрации на бесплатную пробную версию Dynatrace предоставляется определённое количество host unit hours для оценки Dynatrace.

Применение host unit hours к всплескам спроса и отдельным проектам

Если заранее известно, что базовая квота host units будет превышена из-за праздничного спроса или краткосрочного проекта (например, в Чёрную пятницу или во время разового тестового мероприятия), можно использовать host unit hours вместо host units для управления переменными всплесками трафика. Например, если есть пул из 9000 host unit hours и 100 host units, в Чёрную пятницу потребуется больше хостов для масштабирования под возросший трафик на сайте. В таком случае есть возможность использовать все 9000 host unit hours за один день. Это позволит подключить дополнительные 375 host units (475 всего максимум) к Dynatrace на один день.  
`9000 (host unit hours) / 24 (часа) + 100 (базовая квота host units) = 475 (макс. host units)`

Превышения (overages) и несколько сред

Если в аккаунте несколько сред мониторинга, например одна для разработки, а другая для продакшена, превышения рассчитываются на уровне аккаунта, а не на уровне среды. Превышения возникают только тогда, когда квота аккаунта превышена.

Например, лицензировано 100 host units, и есть две среды: одна для продакшена и одна для тестирования. 80 host units назначены среде продакшена, а 20 host units, среде тестирования. Лицензия предусматривает превышения (это видно в обзоре аккаунта под кругом host units).
Если продакшен использует 70 host units, а тестирование использует 30 host units, общая квота аккаунта в 100 host units не превышена, поэтому превышения не возникают. Превышения возникают, только если обе среды в сумме используют более 100 host units.

### Превышения host unit Опционально

Если для мониторинга хостов выделено определённое количество host units и предусмотрено право превышать это число (то есть для аккаунта разрешены превышения), превышения будут рассчитываться в host unit hours. Например, если предусмотрен мониторинг до 10 host units (максимум 160 ГиБ RAM в сумме) и аккаунт допускает превышения, при подключении ещё одного хоста, соответствующего 2 host units, общее количество составит 12 host units, и, следовательно, квота будет превышена на 2 host units. Если продолжать отслеживать хосты с использованием 12 host units в течение полной недели, накопится превышение в 336 host unit hours.  
`2 (host units) × 24 (часа в сутках) × 7 (дней) = 336 (host unit hours превышения)`  
Чтобы добавить или убрать превышения в аккаунте, [обратитесь в отдел продаж Dynatrace](https://www.dynatrace.com/contact/).

## Мониторинг только приложений

Dynatrace обеспечивает мониторинг только приложений для контейнерных платформ.
Это полезно с платформами (такими как Kubernetes или Amazon Elastic Container Service (ECS)), когда нужно:

* Разворачивать, мониторить и лицензировать на уровне контейнера.
* При отсутствии доступа к базовой виртуальной машине.

Примеры сценариев включают, но не ограничиваются следующим:

* [Amazon ECS﻿](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html)

  + [AWS ECS daemon](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs/deploy-oneagent-on-ecs "Мониторинг кластеров ECS в виде демона (daemon service) с типом запуска EC2.")
  + [AWS Elastic Beanstalk](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk "Установка OneAgent на AWS Elastic Beanstalk.")
  + [AWS Elastic Kubernetes Service](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-eks "Установка OneAgent на Elastic Kubernetes Service.")
* [AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Установка OneAgent на AWS Fargate.")
* [Azure App Service](/managed/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Мониторинг Azure с помощью Dynatrace") включая [Azure Functions на App-Service (Dedicated) Plan](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Информация об установке, настройке, обновлении и удалении OneAgent для мониторинга Azure Functions с использованием расширения сайта Azure.")
* [Azure Container instances﻿](https://docs.microsoft.com/en-us/azure/container-instances/)

  + [Azure Kubernetes Service](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-aks "Информация о развёртывании, эксплуатации и обслуживании OneAgent на Azure Kubernetes Service.")
* [Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.")

* [Red Hat OpenShift Container Platform﻿](https://www.redhat.com/en/technologies/cloud-computing/openshift/container-platform)

Для мониторинга только приложений Dynatrace использует [универсальную инъекцию](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#universal-injection "Информация о том, какие возможности поддерживаются OneAgent на разных операционных системах и платформах.") для встраивания модулей кода OneAgent в приложения единым образом на разных платформах.

Расчёт host unit для мониторинга только приложений основан на обнаруженном лимите памяти, например лимите памяти контейнера.
Эта память определяется на уровне экземпляра ОС или контейнера.
Если лимиты памяти не обнаружены, при расчёте host unit может использоваться память базового хоста, что может отражать более высокое количество host unit.
Интеграции OneAgent Dynatrace для serverless-сервисов вычислений потребляют [host unit](#classic-host-units), и расчёты используют [весовые коэффициенты host unit для Full-Stack](#classic-host-units).

Следующие сценарии имеют собственные расчёты host unit и часов host unit, как описано в таблице ниже.

| Сценарий | Описание |
| --- | --- |
| Azure App Services (работающие на плане App Service (dedicated) для Windows) | Потребление основано на количестве и объёме памяти экземпляров плана. Не имеет значения, сколько приложений работает на этих экземплярах. |
| Azure App Service (работающий на Linux OS или в контейнерах Linux) | Потребление основано на объёме памяти экземпляра плана, умноженном на количество работающих контейнеров. Это связано с тем, что лимиты ресурсов контейнера установить нельзя. |
| Oracle Solaris Zones | Solaris Zones учитываются как хосты. |
| Мониторируемые контейнеры, не определённые как контейнеры | Такие контейнеры учитываются как хосты. |
| Serverless-функции | Serverless-функции потребляют [DDU для serverless-функций](/managed/license/classic-licensing/davis-data-units/serverless-monitoring "Информация о том, как рассчитывается потребление при мониторинге serverless."). |

## Мониторинг мейнфреймов на IBM z/OS

Мониторинг [модулей кода CICS, IMS и z/OS Java](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Установка, настройка и управление модулями Dynatrace на z/OS."), работающих на IBM z/OS, потребляется на основе миллионов сервисных единиц (MSU). Поэтому мониторинг мейнфреймов не влияет на потребление host unit или часов host unit.

MSU, это единица измерения IBM для объёма вычислительной нагрузки, которую мейнфрейм IBM Z может выполнить за час. Количество потреблённых MSU при [sub-capacity лицензировании﻿](https://www.ibm.com/it-infrastructure/z/pricing-licensing) рассчитывается на основе пиковых скользящих 4-часовых средних значений MSU за последний месяц по данным IBM system management facility для каждого мониторируемого логического раздела (LPAR) или подсистемы.

Пиковые скользящие 4-часовые средние значения MSU для каждого мониторируемого LPAR можно получить из Dynatrace или раздела N5 отчёта [sub-capacity reporting tool﻿](https://www.ibm.com/docs/en/zos/2.5.0?topic=tool-about-sub-capacity-reporting) (SCRT). Пиковые скользящие 4-часовые средние значения MSU для каждой подсистемы можно получить из раздела P5 отчёта SCRT.

## Premium High Availability

Модель развёртывания [Premium High Availability](/managed/managed-cluster/high-availability/multi-data-centers "Информация о том, как Dynatrace Managed Premium High Availability обеспечивает отказоустойчивость, устойчивость данных и маршрутизацию данных между дата-центрами.") лицензируется отдельно, только на основе лимита конкурентных host unit. Premium High Availability не влияет на потребление конкурентных host unit или часов host unit.

## Как потребление Synthetic NAM Monitoring влияет на биллинг

Мониторы network availability monitoring (NAM) не имеют отдельной строки в прайс-листе Dynatrace. Вместо этого биллинг рассчитывается на основе [количества точек данных метрик](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."), генерируемых при каждом выполнении NAM-теста. Для получения дополнительной информации обратитесь к своему менеджеру по работе с клиентами Dynatrace.

Расчёт точек данных метрик

К точкам данных метрик применяются следующие детали:

* Точки данных метрик, связанные с выполнением монитора и шага, не подлежат биллингу.
* На биллинг влияет только потребление метрик, произведённых на уровне запроса.
* Каждое выполнение запроса в рамках ping-тестов генерирует 6 точек данных метрик.

  + Количество пакетов, использованных в ping-тесте, не влияет на количество произведённых метрик или на биллинг.
  + Количество пакетов не влияет на цену.
* Каждое выполнение запроса в рамках TCP/DNS-тестов генерирует 3 точки данных метрик.
* Цена остаётся неизменной независимо от того, создаётся ли несколько тестов с одним запросом каждый или один тест с множеством запросов для одного и того же набора хостов или устройств.

## Похожие темы

* [Цены Dynatrace﻿](https://www.dynatrace.com/pricing/)
* [Расширение Dynatrace (Davis data units)](/managed/license/classic-licensing/davis-data-units "Информация о том, как рассчитывается потребление мониторинга Dynatrace на основе Davis data units (DDU).")
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Информация о расширении наблюдаемости метрик в Dynatrace.")
* [DDU для Log Monitoring Classic](/managed/license/classic-licensing/davis-data-units/log-monitoring-consumption "Информация о том, как рассчитывается объём потребления DDU для Dynatrace Log Monitoring Classic.")