---
title: Мониторинг приложений и инфраструктуры (хост-единицы)
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring
scraped: 2026-05-12T11:13:47.847769
---

# Мониторинг приложений и инфраструктуры (хост-единицы)

# Мониторинг приложений и инфраструктуры (хост-единицы)

* 12-min read
* Updated on Mar 18, 2026

Мониторинг приложений и инфраструктуры Dynatrace осуществляется путём установки единого [Dynatrace OneAgent](/managed/platform/oneagent "Learn the monitoring capabilities of OneAgent.") на каждый мониторируемый хост в вашей среде. Лицензирование OneAgent выполняется на основе каждого хоста (виртуального или физического сервера).

Однако не все хосты одинаковы по размеру. Более крупные хосты потребляют больше хост-единиц, чем хосты меньшего размера. Объём ОЗУ мониторируемого сервера используется в качестве мерила для определения размера хоста (то есть количества составляющих его хост-единиц). Преимущество этого подхода — его простота. Можно иметь 10 JVM или 1 000 JVM — такие факторы не влияют на объём потребления мониторинга окружения.

OneAgent может работать в двух режимах. По умолчанию OneAgent работает в режиме Full-Stack Monitoring. Также можно использовать [режим Infrastructure Monitoring](/managed/platform/oneagent/monitoring-modes/monitoring-modes#infrastructure-only "Find out more about the available monitoring modes when using OneAgent.") для хостов, которым не требуется полная видимость стека. Режим Infrastructure потребляет меньше хост-единиц, чем Full-Stack.

## Хост-единицы

Воспользуйтесь таблицей весов хост-единиц ниже, чтобы узнать, сколько хост-единиц потребляется в зависимости от объёма ОЗУ мониторируемого сервера. Общее потребление хост-единиц рассчитывается как сумма хост-единиц всех режимов и всех мониторируемых систем. Подробнее см. в [Управление лицензией Dynatrace Managed](/managed/manage/account-management/subscription-and-license/subscription-and-license-managed "Dynatrace Managed license management").

| Макс. ОЗУ | Хост-единицы (Full-Stack) | Хост-единицы (Infrastructure) |
| --- | --- | --- |
| 1,6 GiB | 0,10 | 0,03 |
| 4 GiB | 0,25 | 0,075 |
| 8 GiB | 0,50 | 0,15 |
| 16 GiB | 1,0 | 0,3 |
| 32 GiB | 2,0 | 0,6 |
| 48 GiB | 3,0 | 0,9 |
| 64 GiB | 4,0 | 1,0 |
| 80 GiB | 5,0 | 1,0 |
| 96 GiB | 6,0 | 1,0 |
| 112 GiB | 7,0 | 1,0 |
| n×16 GiB | n | 1,0 |

Если объём ОЗУ хоста находится между значениями в таблице, число округляется вверх. Например, хост с 12 GiB ОЗУ потребляет 1 хост-единицу, так как 12 GiB находится между 8 GiB и 16 GiB.

Для [режима Infrastructure Monitoring](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") применяется тот же принцип округления. Если для вашей лицензии Cloud Infrastructure включено ограничение хост-единиц, количество хост-единиц на хост ограничено значением 1,0. Если у вас действующее соглашение, не отражающее ограничение `1,0` хост-единиц на хост, [обратитесь к представителю по продажам Dynatrace](https://www.dynatrace.com/contact/).

### Хост-единица-часы

Хост-единица-час представляет потребление одной хост-единицы за период времени. 1 хост-единица-час соответствует потреблению 1 хост-единицы в течение 1 часа. Хост с 16 GiB ОЗУ (то есть 1 хост-единица), работающий полный день, потребляет 24 хост-единицы-часа.

Пример расчёта хост-единиц-часов

Например, у вас есть 1 000 хост-единиц-часов и вы хотите мониторировать хост с 64 GiB ОЗУ (что соответствует 4 хост-единицам). При работе хоста в течение полного дня потребляется 96 хост-единиц-часов.
`4 (хост-единицы) × 24 (часа в день) = 96 (хост-единиц-часов)`

1 000 хост-единиц-часов будут израсходованы чуть более чем за 10 дней.
`4 (хост-единицы) × 24 (часа) × 10 (дней) = 960 хост-единиц-часов`

Истинная параллельность в расчётах хост-единиц-часов

Каждую минуту Dynatrace рассчитывает потребление хост-единиц на основе истинной параллельности. Это означает, что два хоста, работающих в рамках одного часа, потребят две хост-единицы, если оба работают одновременно. Хост-единицы-часы считаются в календарных часах (например, 10:00–11:00), а не в часах использования (например, 10:23–11:23).

Если хост работает менее 5 минут, это не засчитывается в квоту хост-единиц-часов. Хост, работающий 5 и более минут, округляется до `1 хост-единицы-часа`.

Когда мониторинг хоста прекращается по любой причине, потреблённые хост-единицы высвобождаются примерно через пять минут и становятся доступны для другого хоста.

#### Пример 1

У вас есть хост с 16 GiB ОЗУ (1 хост-единица), работающий с 10:00 до 10:30. В 10:30 вы запускаете другой хост того же размера. Dynatrace считает это одной хост-единицей, так как хосты не работают одновременно.

#### Пример 2

Вы запускаете первый хост в 10:00 и второй в 10:30. Затем оба хоста работают вместе 30 минут и останавливаются одновременно. Dynatrace считает это двумя хост-единицами, так как оба хоста работают одновременно.

#### Пример 3

Один хост с 16 GiB ОЗУ запускается и останавливается три раза в течение часа:

`12:10 — запуск`
`12:20 — остановка`
`12:30 — запуск`
`12:40 — остановка`
`12:50 — запуск`
`13:00 — остановка`

Данный сценарий соответствует `1 хост-единице-часу`, так как учитывается истинная параллельность.

#### Пример 4

У вас есть хост с 16 GiB ОЗУ (1 хост-единица), работающий с 10:23 до 11:23. Поскольку хост работает в течение 2 календарных часов (10:00–11:00 и 11:00–12:00), это равнозначно `2 хост-единицам-часам`.

Хост-единицы-часы для бесплатного пробного периода

Хост-единицы-часы используются в бесплатных пробных версиях Dynatrace. При регистрации в бесплатной пробной версии вы получаете определённое количество хост-единиц-часов для оценки Dynatrace.

Использование хост-единиц-часов для всплесков нагрузки и отдельных проектов

Если вы заранее знаете, что базовая квота хост-единиц будет превышена из-за праздничного спроса или краткосрочного проекта (например, в Чёрную пятницу), вы можете использовать хост-единицы-часы для управления переменными всплесками трафика. Например, если у вас пул из 9 000 хост-единиц-часов и 100 хост-единиц, в Чёрную пятницу вам понадобится больше хостов для обработки возросшего трафика. В этом случае вы можете использовать все 9 000 хост-единиц-часов за один день, подключив дополнительно до 375 хост-единиц (475 максимум).
`9 000 (хост-единиц-часов) / 24 (часа) + 100 (базовая квота) = 475 (макс. хост-единиц)`

Превышения и несколько окружений

Если у вашего аккаунта несколько окружений мониторинга (например, одно для разработки и одно для продуктива), превышения рассчитываются по аккаунту в целом, а не по каждому окружению. Только при превышении квоты аккаунта возникают переплаты.

Например, вы лицензировали 100 хост-единиц и имеете два окружения: для продуктива и для тестирования. Вы назначили 80 хост-единиц продуктивному окружению и 20 — тестовому. Ваша лицензия предусматривает превышения. Если продуктив использует 70 хост-единиц, а тестирование — 30, суммарная квота 100 хост-единиц не превышается, и переплат нет. Переплаты возникают только если оба окружения суммарно используют более 100 хост-единиц.

### Превышения хост-единиц (опционально)

Если вы договорились об аллокации хост-единиц и имеете право превышать этот лимит, превышения рассчитываются в хост-единицах-часах. Например, если у вас 10 хост-единиц (максимум 160 GiB суммарной ОЗУ) и аккаунт допускает превышения, при подключении ещё одного хоста на 2 хост-единицы итого станет 12, что превышает квоту на 2 хост-единицы. При работе в течение полной недели накопится 336 хост-единиц-часов превышения.
`2 (хост-единицы) × 24 (часа в день) × 7 (дней) = 336 (хост-единиц-часов превышения)`
Чтобы добавить или убрать превышения для своего аккаунта, [свяжитесь с отделом продаж Dynatrace](https://www.dynatrace.com/contact/).

## Мониторинг только приложений

Dynatrace обеспечивает мониторинг только приложений для контейнерных платформ.
Это полезно на таких платформах, как Kubernetes или Amazon Elastic Container Service (ECS), когда:

* необходимо развёртывать, мониторировать и лицензировать на уровне контейнера;
* нет доступа к нижележащей VM.

Примеры сценариев включают, но не ограничиваются:

* [Amazon ECS](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html)
  + [AWS ECS daemon](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs/deploy-oneagent-on-ecs "Monitor ECS clusters as a daemon service, with the EC2 launch type.")
  + [AWS Elastic Beanstalk](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk "Install OneAgent on AWS Elastic Beanstalk.")
  + [AWS Elastic Kubernetes Service](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-eks "Install OneAgent on Elastic Kubernetes Service.")
* [AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate.")
* [Azure App Service](/managed/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace")
* [Azure Kubernetes Service](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-aks "Learn how to deploy, operate, and maintain OneAgent on Azure Kubernetes Service.")
* [Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")

Для мониторинга только приложений Dynatrace использует [универсальную инъекцию](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#universal-injection "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") для единообразного внедрения кодовых модулей OneAgent в приложения на различных платформах.

Расчёт хост-единиц для мониторинга только приложений основан на обнаруженном лимите памяти (например, лимите памяти контейнера). Эта память определяется на уровне экземпляра ОС или контейнера. Если лимиты памяти не обнаружены, расчёт может использовать память нижележащего хоста, что даёт большее число хост-единиц.

| Сценарий | Описание |
| --- | --- |
| Azure App Services (на плане App Service (dedicated) для Windows) | Потребление основано на числе и памяти экземпляров плана. Количество приложений на экземплярах не имеет значения. |
| Azure App Service (на Linux или Linux-контейнерах) | Потребление основано на памяти экземпляра плана, умноженной на число запущенных контейнеров — так как лимиты ресурсов контейнера задать невозможно. |
| Oracle Solaris Zones | Solaris Zones считаются хостами. |
| Мониторируемые контейнеры, не обнаруженные как контейнеры | Считаются хостами. |
| Бессерверные функции | Потребляют [DDU для бессерверных функций](/managed/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Understand how serverless monitoring consumption is calculated."). |

## Мониторинг мейнфреймов на IBM z/OS

Мониторинг [кодовых модулей CICS, IMS и z/OS Java](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS."), работающих на IBM z/OS, потребляется на основе миллионов сервисных единиц (MSU). Поэтому мониторинг мейнфреймов не учитывается в потреблении хост-единиц или хост-единиц-часов.

MSU — единица измерения IBM, отражающая объём вычислительной нагрузки, которую IBM Z mainframe может обработать в час. Количество потреблённых MSU при [sub-capacity licensing](https://www.ibm.com/it-infrastructure/z/pricing-licensing) рассчитывается на основе пиковых значений скользящего 4-часового среднего MSU за последний месяц из данных IBM system management facility на каждый мониторируемый логический раздел (LPAR) или подсистему.

Пиковые значения 4-часового среднего MSU на LPAR можно получить из Dynatrace или из раздела N5 [отчёта sub-capacity reporting tool](https://www.ibm.com/docs/en/zos/2.5.0?topic=tool-about-sub-capacity-reporting) (SCRT). Пиковые значения по подсистемам — из раздела P5 отчёта SCRT.

## Premium High Availability

Модель развёртывания [Premium High Availability](/managed/managed-cluster/high-availability/premium-high-availability "Learn how Dynatrace Premium High Availability provides near-zero downtime and data resilience through multi-data-center deployments for Managed Clusters.") лицензируется отдельно только на основе лимита параллельных хост-единиц. Premium High Availability не учитывается в потреблении параллельных хост-единиц или хост-единиц-часов.

## Связанные темы

* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)
* [Расширение Dynatrace (единицы Davis data units)](/managed/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).")
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")
* [DDU для Log Monitoring Classic](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.")