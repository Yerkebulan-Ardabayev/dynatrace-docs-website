---
title: Azure Native Dynatrace Service
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-native-integration
---

# Azure Native Dynatrace Service

# Azure Native Dynatrace Service

* Пояснение
* 17 минут на чтение
* Обновлено 23 июня 2026 г.

Azure Native Dynatrace Service, это Azure Native Integration, доступная в [Azure Marketplace﻿](https://dt-url.net/9n039mv). Она позволяет приобретать, настраивать и управлять Dynatrace прямо в портале Azure. После развёртывания интеграции Dynatrace отображается как **Azure Native Dynatrace Service**, и её конфигурацией можно управлять из портала Azure.

Эту интеграцию разработали и совместно поддерживают Microsoft и Dynatrace.

Возможности и ограничения

Возможности:

* **Интегрированное подключение:** после покупки интеграции через конфигурацию или Marketplace можно создать Dynatrace и управлять им как нативным сервисом Azure.

* **Единый биллинг:** при покупке Dynatrace SaaS через Azure Marketplace потребление лицензии Dynatrace становится частью обычного счёта Azure. Это значит, что Dynatrace можно администрировать как нативный сервис Azure и использовать обязательство организации по потреблению Microsoft Azure для покупок Dynatrace, которые отображаются в едином консолидированном счёте Azure.
* **Единый вход (SSO):** можно включить SSO через Azure Active Directory вместо настройки отдельной аутентификации в портале Dynatrace.
* **Приём метрик и логов Azure**: настройка автоматического мониторинга для метрик Azure Monitor, активности подписки Azure и логов ресурсов.

* **Развёртывание OneAgent:** установка и удаление Dynatrace OneAgent как расширения на Azure Virtual Machines, Azure App Services, [серверах с поддержкой Arc](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-arc-enabled-servers "Интеграция Azure с серверами ARC") и Azure Kubernetes Service.
* **Управление Dynatrace**: проверка, какие ресурсы отправляют метрики и логи Azure в Dynatrace, и внесение изменений по мере необходимости.
* **Масштабирование автоматизации**: управление ресурсами Dynatrace из Azure CLI, Terraform и Pulumi (IaC), что расширяет возможности развёртывания ресурсов.

Ограничения:

* Интеграция создаёт новое окружение и аккаунт Dynatrace, её нельзя запустить в уже существующем окружении Dynatrace SaaS.
* Интеграция работает в рамках одного окружения Entra ID.

Azure Marketplace

Доступ к Azure Native Dynatrace Service можно получить через [Azure Marketplace﻿](https://dt-url.net/9n039mv).

Чтобы получить индивидуальное частное предложение для Azure Native Dynatrace Service, нужно обратиться к своей команде по работе с аккаунтом Dynatrace или написать в отдел продаж Dynatrace ([sales@dynatrace.com](mailto:sales@dynatrace.com)).

Также можно начать бесплатный 30-дневный пробный период Azure Native Dynatrace Service, оформив подписку на план "Dynatrace for Azure Trial".

## Предварительные требования

Чтобы подготовиться к покупке Azure Native Dynatrace Service через Marketplace, нужно выполнить следующее:

* [Получить свой Azure Billing Account ID﻿](https://learn.microsoft.com/en-us/marketplace/private-offers-pre-check#locate-your-billing-account-id) и определить подписку Azure, в которой планируется развернуть Azure Native Dynatrace Service.
* [Получить отчёт о соответствии частному предложению﻿](https://learn.microsoft.com/en-us/marketplace/private-offers-eligibility-report#run-the-report) и передать его команде Dynatrace.
* Проверить настройки контроля покупок Azure Marketplace. Если в организации уже есть частный Azure Marketplace:

  + включить покупки Marketplace для подписки Azure под своим billing ID;
  + убедиться, что глобальный администратор клиента Azure назначил роль `Marketplace admin` пользователю, управляющему частным магазином Marketplace;
  + перейти в раздел **Gallery** и добавить листинг Dynatrace Marketplace в **Collection Items**.
* Убедиться, что у пользователей, ответственных за покупку частного предложения, достаточно прав, чтобы принять предложение и оформить подписку на него.

Azure Native Dynatrace Service доступна через [частное предложение﻿](https://dt-url.net/3d03xln). Чтобы Dynatrace создала для вас частное предложение, [обратитесь в Dynatrace﻿](https://dt-url.net/m003xf1). После принятия предложения Azure Native Dynatrace Service станет доступна в Azure Marketplace.

### Чек-лист на день покупки

В день покупки нужно убедиться, что всё готово к операции, выполнив следующее:

1. **Принять частное предложение**: внимательно изучить условия, указанные в частном предложении, и принять предложение через Azure Marketplace.

   Для принятия частного предложения нужны права `Billing Account Owner` или `Enterprise Administrator`.
2. **Приобрести Azure Native Dynatrace Service**: для SaaS-продуктов, приобретаемых через Azure Marketplace, принятие предложения и фактическая покупка, это два разных шага.

   Для создания ресурса Dynatrace нужен доступ уровня `Owner` или `Contributor` к подписке Azure, в которой будет выполняться развёртывание.
3. **Создать и настроить ресурс Dynatrace**: в процессе покупки нужно выполнить описанные шаги для создания ресурса Dynatrace и управления им по необходимости.

### Настройка прав доступа

#### Портал Azure

Для создания ресурса Dynatrace в подписке Azure нужны как минимум права `Contributor`. Однако рекомендуется получить права `Owner`, чтобы все интеграции Azure Native Dynatrace работали корректно, включая отправку метрик Azure Monitor в Dynatrace.

Если ресурс Dynatrace настроен с правами `Contributor`, потребуется также вручную выдать управляемому удостоверению (managed identity), связанному с ресурсом Dynatrace, права `Monitoring Reader` для всех подписок, из которых нужно отправлять метрики Azure Monitor в Dynatrace.

#### Dynatrace

Со стороны Dynatrace пользователь портала Azure, создавший первый ресурс и окружение Dynatrace, становится владельцем аккаунта Dynatrace, создаваемого при развёртывании интеграции. Права владельца аккаунта можно делегировать другим пользователям.

## Настройка интеграции

При первом развёртывании ресурса Azure Native Dynatrace в подписке Azure для вас создаётся новое окружение Dynatrace, размещённое в Azure.

* Окружение Dynatrace создаётся в том же регионе Azure, в котором создаётся ресурс Dynatrace. В этом новом интегрированном окружении Azure Native:

  + можно [установить OneAgent](#oa) для включения мониторинга различных вычислительных ресурсов Azure;
  + можно отслеживать [метрики](/managed/analyze-explore-automate/metrics-classic "Узнайте о классических метриках, которые предлагает Dynatrace.") ресурсов Azure. Также можно настроить метрики для [сервисов по умолчанию](/managed/ingest-from/microsoft-azure-services/azure-native-integration#default "Настройте и сконфигурируйте окружение Dynatrace SaaS с помощью Azure Marketplace.");
  + можно собирать [логи](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить мониторинг логов, какие данные он может предоставить, и многое другое.") ресурсов Azure.

Чтобы настроить интеграцию

1. В подписке Azure разверните своё частное предложение и выберите **Purchase**.
2. В разделе **Create a new Dynatrace environment** выберите **Create**.
3. В разделе **Basics** для **Resource group** укажите, создавать ли новую группу ресурсов или использовать существующую.

   Группа ресурсов, это контейнер, содержащий связанные ресурсы для решения Azure. Подробнее см. в [обзоре Azure Resource Group﻿](https://dt-url.net/xv43x96).
4. Введите **Resource name** для ресурса Dynatrace, а затем выберите **Region** из выпадающего меню. Ресурс Dynatrace в Azure и окружение Dynatrace будут созданы в выбранном регионе.

   Список поддерживаемых регионов Azure, в которых можно создавать ресурсы Azure Native Dynatrace, см. в разделе [Хранение данных](/managed/manage/data-privacy-and-security/data-security/data-security-controls#data-storage "Узнайте о средствах контроля безопасности данных и операционной безопасности.").
5. Убедитесь, что условия биллинга и цена частного предложения совпадают с условиями, согласованными в частном предложении.
6. В нижней части страницы укажите своё имя и название компании для создания аккаунта Dynatrace, а затем выберите **Next: Metrics and Logs**.
7. Необязательно Выберите, нужно ли **Send subscription activity logs** и/или **Send Azure resource logs**. Подробности см. в разделе [Настройка метрик и логов](#metrics-logs).

   При выборе **Send Azure resource logs for all defined services** Azure автоматически отправляет логи для всех поддерживаемых ресурсов. Чтобы собирать логи только с определённых ресурсов Azure в Dynatrace, можно использовать теги ресурсов Azure. Правила тегирования следующие:

   * ресурсы Azure с тегами `Include` отправляют логи в Dynatrace;
   * ресурсы Azure с тегами `Exclude` не отправляют логи в Dynatrace;
   * при конфликте между правилами включения и исключения приоритет имеет исключение.

   Ограничение: не более 20 записей для тегов `Include` или `Exclude`.
8. Выберите **Next: Single sign-on**.
9. Необязательно Выберите, включать ли **SSO through Microsoft Entra ID**.

   * Если эту функцию включать не нужно, выберите **Next: Tags**.
   * Если эту функцию нужно включить, выберите её, укажите отображаемый ID приложения Dynatrace, а затем выберите **Next: Tags**.
10. Необязательно [Укажите теги Azure](#tags) для нового ресурса Dynatrace, а затем выберите **Next: Review and create**.
11. Проверьте правильность отправленной информации, а затем выберите **Create**. После завершения развёртывания можно выбрать **Go to resource**, чтобы перейти к конкретному ресурсу Dynatrace.

## Привязка нескольких подписок Azure к одному окружению Dynatrace Необязательно

Убедитесь, что у аккаунта Azure есть доступ к аккаунту Dynatrace со следующими разрешениями:

* `View Account`
* `View Environment`
* `Install OneAgent`
* `Manage Monitoring Settings`

Подробнее см. [права доступа Environment](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions").

После развёртывания первого окружения Dynatrace с нативной интеграцией Azure можно:

* Привязать дополнительные подписки Azure к вновь созданному окружению Dynatrace.
* Привязать больше окружений Dynatrace к одной подписке Azure.

  При привязке нескольких подписок Azure и создании ресурса нужно иметь привилегии учётной записи Dynatrace с разрешениями `tenant-manage-settings` и `tenant-agent-install`. Подробнее о настройке этих разрешений см. [Role-based permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

Выполните шаги ниже, повторяя процедуру для каждой подписки, которую нужно привязать.

1. Перейдите в портал Azure и найдите `Azure Native Dynatrace Service` в строке поиска сверху.
2. Выберите **Azure Native Dynatrace Service**.
3. Выберите **Create**.
4. В разделе **Basics** для **Resource group** укажите, создавать новую группу ресурсов или использовать существующую.

   Группа ресурсов, это контейнер, который содержит связанные ресурсы решения Azure. Подробнее см. [Azure Resource Group overview﻿](https://dt-url.net/xv43x96).
5. Введите **Resource name**, затем выберите **Region** из выпадающего меню.

   Окружение Dynatrace для привязки и новый ресурс Dynatrace должны находиться в одном регионе.
6. Выберите **окружение Dynatrace** для привязки к подписке Azure, затем выберите **Next: Metrics and Logs**.
7. Опционально выберите, нужно ли **Send subscription activity logs** и/или **Send Azure resource logs**. Подробнее см. [Configure metrics and logs](#metrics-logs).

   Если выбрать **Send Azure resource logs for all defined services**, Azure автоматически будет отправлять логи для всех поддерживаемых ресурсов. Чтобы собирать логи только с определённых ресурсов Azure в Dynatrace, можно использовать теги ресурсов Azure. Правила тегирования следующие:

   * Ресурсы Azure с тегами `Include` отправляют логи в Dynatrace.
   * Ресурсы Azure с тегами `Exclude` не отправляют логи в Dynatrace.
   * При конфликте между правилами включения и исключения приоритет имеет исключение.

   Существует лимит в 20 записей для тегов `Include` или `Exclude`.
8. Пропустите **Next: Single sign-on**, так как SSO можно настроить только после развёртывания, затем выберите **Next: Tags**.
9. Опционально [укажите теги](#tags) для нового ресурса Dynatrace, затем выберите **Next: Review and create**.
10. Проверьте правильность отправленной информации, затем выберите **Create**. По завершении развёртывания можно выбрать **Go to resource**, чтобы перейти к конкретному ресурсу Dynatrace.

## Доступ к окружению Dynatrace

После настройки интеграции можно получить доступ к окружению Dynatrace напрямую из портала Azure.

В портале Azure перейдите к ресурсу Dynatrace и выберите **Overview**. Там появятся все детали окружения Dynatrace, включая прямые ссылки на следующие страницы веб-интерфейса:

* **Dashboards**, подробнее см. [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* **Log Viewer**, подробнее см. [Log viewer (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Learn how to use Dynatrace log viewer to analyze log data.").
* **топология Smartscape**, подробнее см. [Visualize your environment through Smartscape](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment.").

## Настройка метрик и логов

### Метрики

Метрики можно активировать [metrics](/managed/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.") после развёртывания интеграции Azure.

Сбор метрик с Virtual Machines, App Services и Azure Kubernetes Service

Чтобы начать сбор метрик с ваших Virtual Machines, App Services и Azure Kubernetes Service, нужно [установить Dynatrace OneAgent на эти ресурсы как расширение](#oa).

Сбор метрик с облачных сервисов

Все сервисы и метрики по умолчанию включены. При необходимости их можно отключить, выбрав кнопку удаления в списке сервисов. После подключения Dynatrace к окружению Azure он сразу начинает мониторинг встроенных сервисов Azure для указанного вами субъекта-службы (service principal). На странице [Azure Cloud Services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics "The list of classic metrics Dynatrace collects by default for Azure monitoring.") перечислены метрики облачных сервисов Azure, которые отслеживаются по умолчанию.

### Управление облачными сервисами

Все облачные сервисы отслеживаются по умолчанию, но их можно быстро отключить в списке или снова включить при необходимости.

Чтобы добавить сервисы в мониторинг

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Cloud and virtualization** > **Azure**.
2. На странице обзора Azure найдите подключение, которое нужно изменить, и выберите **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") в этой строке.
3. В разделе **Services** выберите **Manage services**.
4. Для каждого сервиса, который нужно добавить: выберите **Add service**, выберите сервис из списка, затем выберите **Add service**.
5. Выберите **Save changes**, чтобы сохранить конфигурацию.

Настройка собираемых метрик по сервису

После добавления сервиса Dynatrace автоматически начинает собирать набор метрик для этого сервиса.

Рекомендуемые метрики:

* Включены по умолчанию, и их нельзя отключить.
* Могут поставляться с рекомендуемыми измерениями (включены по умолчанию, отключить нельзя) и опциональными измерениями (по умолчанию отключены, можно включить).

Помимо рекомендуемых метрик, большинство сервисов предлагают возможность включения опциональных метрик, которые можно добавить и настроить вручную.

Список облачных сервисов Azure и собираемых метрик

Чтобы увидеть полный список облачных сервисов Azure и узнать о метриках, собираемых для каждого из них, см. [All Azure cloud services](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Monitor Azure services with Dynatrace and view available metrics.").

Также можно проверить список поддерживаемых сервисов Azure во встроенном в продукт Dynatrace Hub (поиск по **Azure**) или в [веб-версии Dynatrace Hub﻿](https://www.dynatrace.com/hub/?query=azure).

Чтобы добавить и настроить метрики

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Cloud and virtualization** > **Azure**.
2. На странице обзора Azure найдите подключение, которое нужно изменить, и выберите **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") в этой строке.
3. В разделе **Services** выберите **Manage services**.
4. Выберите сервис, для которого нужно добавить метрики. На странице сведений о сервисе перечислены метрики, которые уже отслеживаются для этого сервиса.
5. Выберите **Add metric**.
6. В списке **Add new metric** выберите метрику, затем выберите **Add metric**.
7. Выберите ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row"), чтобы развернуть детали метрики и настроить её.
8. Выберите **Apply**, чтобы сохранить конфигурацию.

После выбора облачных сервисов и сохранения изменений мониторинг вновь добавленных сервисов запускается автоматически.

### Логи

* Логи можно активировать либо [во время развёртывания интеграции Azure](#setup), либо [после развёртывания](#how-to-logs).
* Можно настроить два типа логов Azure для Dynatrace: [логи активности подписки](#activity) и [логи ресурсов Azure](#resource).
* Логи из домена Azure Entra ID можно отправлять следующим образом:

  + Создать настройки диагностики.
  + Указать в качестве места отправки решение партнёра.

#### Логи активности подписки

Логи активности подписки дают представление об операциях (PUT, POST, DELETE), выполненных над каждым ресурсом Azure в подписке (management plane). Для каждой подписки Azure есть один лог активности.

#### Логи ресурсов Azure

Логи ресурсов Azure дают представление об операциях, выполненных внутри ресурса Azure (data plane), например получение секрета из key vault или запрос к базе данных. Содержимое логов ресурсов зависит от службы Azure и типа ресурса.

Все службы Azure в [категориях логов Azure Monitor﻿](https://dt-url.net/fja38sr) передают логи, включая Microsoft Entra ID и [Azure Monitor Integration Service﻿](https://dt-url.net/dpc38am).

Список логов ресурсов Azure приведён в разделе [Supported categories for Azure Monitor resource logs﻿](https://dt-url.net/ea03xvn).

#### Логи активности Entra ID

Данные, собранные в логах Microsoft Entra, позволяют:

* Отслеживать многие аспекты среды Microsoft Entra.
* Определять, как пользователи используют приложения и службы.
* Обнаруживать потенциальные риски, влияющие на состояние среды.
* Устранять проблемы, мешающие пользователям выполнять работу.
* Получать представление о событиях аудита изменений в каталоге Microsoft Entra.

Entra ID предоставляет несколько типов логов, например логи аудита, логи входа и логи подготовки (provisioning). Чтобы отправлять логи Microsoft Entra ID в Dynatrace, нужно указать Dynatrace как назначение в настройках диагностики Microsoft Entra ID.

#### Как активировать логи после развёртывания

Активация логов активности подписки

Активация логов ресурсов Azure

Активация логов Azure Entra ID

1. В портале Azure перейти к ресурсу Dynatrace и выбрать **Metrics and logs**.
2. Выбрать **Send subscription activity logs**.
3. Выбрать **Save**.

1. В портале Azure перейти к ресурсу Dynatrace и выбрать **Metrics and logs**.
2. Выбрать **Send Azure resource logs for all defined sources**.

   При выборе этого параметра логи ресурсов Azure по умолчанию отправляются для всех определённых ресурсов, то есть логи собираются для всех поддерживаемых ресурсов.
3. Необязательно. Чтобы отфильтровать конкретный набор ресурсов Azure, отправляющих логи в Dynatrace, можно использовать теги ресурсов Azure. Правила тегов:

   * Ресурсы Azure с тегами `Include` отправляют логи в Dynatrace.
   * Ресурсы Azure с тегами `Exclude` не отправляют логи в Dynatrace.
   * При конфликте между правилами включения и исключения приоритет имеет исключение.
4. Выбрать **Save**.

1. Войти в Microsoft Entra admin center.

   Для входа в Microsoft Entra admin center нужна как минимум роль `Security Administrator`.
2. Перейти в **Entra ID** > **Monitoring & health** > **Diagnostic settings**. По умолчанию отображаются **General settings**, а существующие настройки диагностики видны в таблице.
3. Выбрать **Edit settings**, чтобы изменить существующую настройку, или **Add diagnostic setting**, чтобы создать новую.
4. В **Categories** выбрать, какие логи включить.
5. В **Destination Details** выбрать **Send to partner solutions**.
6. Выбрать **Subscription** и среду **Dynatrace**, куда отправлять данные.

Azure Native Dynatrace Service автоматически включает пересылку логов в подписке Azure, где включён ресурс Dynatrace. Пересылка логов включена для всех поддерживаемых служб и ресурсов. Можно определить правила фильтрации по тегам, чтобы включать или исключать определённые ресурсы Azure из отправки логов.

Azure Native Dynatrace Service использует токен доступа Dynatrace под названием `azure-native-integration`, который меняется каждые 24 часа.

## Создание тегов

* Теги можно создавать либо [во время развёртывания интеграции Azure](#setup), либо [после развёртывания](#how-to-tags).

Теги можно применять к ресурсам, группам ресурсов и подпискам Azure, чтобы логически упорядочить их в таксономию. Теги для нового ресурса Dynatrace в Azure можно задать, добавив пары «ключ-значение»:

* В поле **Name** ввести имя тега, соответствующего ресурсу Dynatrace в Azure (например, `owner`).
* В поле **Value** ввести значение тега, соответствующего ресурсу Dynatrace в Azure (например, адрес электронной почты владельца).

Если теги не заданы, все логи с отслеживаемых ресурсов в подписке Azure отправляются в Dynatrace.

### Как создать теги после развёртывания

В портале Azure перейти к новому ресурсу Dynatrace, затем выбрать **Tags**. Также можно выбрать **Monitored resources**, а затем выбрать **Edit tags** для нужных ресурсов.

## Управление отслеживаемыми ресурсами в портале Azure

После развёртывания Azure Native Dynatrace Service можно просматривать, управлять и отслеживать ресурсы Azure, а также устанавливать OneAgent на виртуальные машины Azure и службы Azure App Services.

Чтобы просмотреть список ресурсов, отправляющих логи и метрики в Dynatrace, в портале Azure нужно перейти к ресурсу Dynatrace и выбрать **Monitored resources**. Список отображаемых ресурсов можно фильтровать по **Resource name** (имя ресурса Azure), **Resource type** (тип ресурса Azure), **Resource group** (имя группы ресурсов для ресурса Azure), **Region** (расположение ресурса Azure) и **Logs to Dynatrace** (отправляет ли ресурс логи в Dynatrace).

## Развёртывание OneAgent на виртуальных машинах Azure и службах Azure App Services

* OneAgent можно развернуть после развёртывания интеграции Azure.

Чтобы отслеживать виртуальные машины Azure или службы Azure App Services, на эти ресурсы можно установить Dynatrace OneAgent в виде расширения.

Установка OneAgent на виртуальную машину

Установка OneAgent на App Service

Установка OneAgent на службы Azure Kubernetes

1. В портале Azure перейти к ресурсу Dynatrace и выбрать **Virtual Machines**.
2. Выбрать в списке виртуальную машину, на которую нужно установить расширение OneAgent.
3. Выбрать **Install extension**.
4. Необязательно. Выбрать, включать ли log analytics.
5. Необязательно. Указать [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") для OneAgent.
6. Выбрать **OK**, чтобы начать процесс установки.
7. По завершении установки в поле **OneAgent status** для выбранной виртуальной машины отображается **Installed**.

* Чтобы посмотреть подробности об установленном OneAgent, выбрать виртуальную машину и перейти в **Extensions**.
* Чтобы удалить OneAgent, выбрать виртуальную машину, затем выбрать **Uninstall extension**.

1. В портале Azure перейти к ресурсу Dynatrace и выбрать **App Services**.
2. Выбрать в списке App Service, на который нужно установить расширение OneAgent.
3. Выбрать **Install extension**.
4. Необязательно. Выбрать, включать ли log analytics.
5. Необязательно. Указать [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") для OneAgent.
6. Выбрать **OK**, чтобы начать процесс установки.
7. По завершении установки в поле **OneAgent status** для выбранной виртуальной машины отображается **Installed**.

* Чтобы посмотреть подробности об установленном OneAgent, выбрать App Service и перейти в **Extensions**.
* Чтобы удалить OneAgent, выбрать App Service, затем выбрать **Uninstall extension**.

1. В портале Azure перейти к ресурсу Dynatrace и выбрать **Azure Kubernetes Service**.
2. Выбрать в списке кластер Kubernetes, на который нужно установить OneAgent Operator.
3. Выбрать **Install extension**.
4. Выбрать **OK**, чтобы начать процесс установки на выбранном кластере Azure Kubernetes.
5. По завершении установки можно увидеть статус OneAgent для выбранных кластеров Kubernetes.

* Чтобы посмотреть подробности об установленном OneAgent, выбрать Azure Kubernetes Service и перейти в **Extensions and Applications**.
* Чтобы удалить OneAgent Operator, выбрать Azure Kubernetes Service, затем выбрать **Uninstall extension**.

Если после включения интеграции App Service не отображается в Dynatrace, нужно перезапустить план App Service.

Чтобы запускать OneAgent на Virtual Machine Scale Sets с интеграцией Dynatrace Azure, нужно использовать [расширение Dynatrace OneAgent для виртуальных машин](#vm) и создать [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

## Удаление Azure Native Dynatrace Service

Чтобы удалить Azure Native Dynatrace Service, нужно удалить ресурс Dynatrace. После удаления ресурса Dynatrace из Azure логи и метрики больше не отправляются в Dynatrace, и вся оплата Dynatrace через Azure Marketplace прекращается.

Удаление ресурса Dynatrace

1. В портале Azure перейти к ресурсу Dynatrace и выбрать **Overview**.
2. Выбрать **Delete**.
3. Ввести имя приложения, которое нужно удалить, затем выбрать **Delete**.

## Начало бесплатного пробного периода Azure Native Dynatrace Service

Azure Marketplace предлагает 30-дневную бесплатную пробную версию Azure Native Dynatrace Service. Можно зарегистрироваться, используя пробный план, опубликованный Dynatrace. До окончания бесплатного пробного периода можно перейти на частное предложение, настроенное под организацию.

Чтобы начать бесплатный пробный период

1. В портале Azure перейти в **Marketplace** и выбрать **Azure Native Dynatrace Service**.
2. В выпадающем списке **Plan** выбрать **Dynatrace for Azure Trial**, затем выбрать **Subscribe**.
3. Выполнить шаги [настройки](#setup), чтобы настроить Azure Native Dynatrace Service.
4. По окончании пробного периода:

   * Если принято решение продолжить использовать интеграцию Azure Native Dynatrace Service, приобрести Dynatrace через Azure Marketplace, выбрав **Upgrade to Paid** в **Azure resource**.
   * Если принято решение не приобретать Dynatrace, [удалить Azure Native Dynatrace Service](#uninstall).

## Как запросить новую функцию

Если есть пожелание по новой функции, использовать [Microsoft Developer Community﻿](https://dt-url.net/po239hy), чтобы предложить новые функции.

## Устранение неполадок

* [Не удаётся включить интеграцию SSO﻿](https://dt-url.net/tq237c7)
* [Нет прав для настройки SSO для связанного окружения Dynatrace﻿](https://dt-url.net/3o038vp)
* [Как получить логи из подписки Azure в другом клиенте Azure?﻿](https://dt-url.net/4rc37kk)
* [Ресурсы Azure не пересылают логи в Dynatrace﻿](https://dt-url.net/il438i2)

## Часто задаваемые вопросы о приёме логов

* [Каковы ограничения приёма логов для Azure Native Dynatrace Service?﻿](https://dt-url.net/ine37te)
* [Как логирование Azure Native Dynatrace Service влияет на расходы на Azure?﻿](https://dt-url.net/da2380g)
* [Разве не дешевле отправлять данные с помощью существующей пересылки логов Dynatrace Azure в Dynatrace SaaS в AWS, чем использовать Azure Native Dynatrace Service?﻿](https://dt-url.net/bp038gb)

## Смежные темы

* [Интеграции Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace на Azure с помощью OneAgent или OpenTelemetry.")
* [Microsoft Azure Native Dynatrace Service﻿](https://learn.microsoft.com/en-us/azure/partner-solutions/dynatrace/)