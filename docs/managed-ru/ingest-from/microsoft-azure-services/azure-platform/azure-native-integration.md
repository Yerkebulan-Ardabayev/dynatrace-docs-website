---
title: Azure Native Dynatrace Service
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration
scraped: 2026-05-12T11:38:18.116244
---

# Azure Native Dynatrace Service

# Azure Native Dynatrace Service

* Пояснение
* Чтение: 17 мин
* Обновлено 23 июля 2024 г.

Интеграция через Azure Marketplace позволяет организовать удобный процесс приобретения, настройки и управления Dynatrace непосредственно в портале Azure. После настройки интеграции Dynatrace отображается как нативный сервис Azure, и конфигурацией можно управлять из Azure Portal.

Возможности и ограничения

**Возможности:**

* **Простое подключение:** удобное подключение Dynatrace SaaS как интегрированного сервиса Azure через Azure Marketplace. Чтобы настроить интеграцию:

  + не требуется настройка концентраторов событий, облачных функций или конфигураций

* **Единый биллинг:** единый счёт за все ресурсы, потребляемые в Azure, включая потребление Dynatrace SaaS.
* **Единый вход (SSO):** отдельные учётные данные для портала Dynatrace не нужны. Достаточно один раз войти на портал Azure и при необходимости перейти в Dynatrace.
* **Мониторинг журналов:** обеспечивает пересылку журналов активности подписки и ресурсов в Dynatrace. Подробнее см. в разделе [Мониторинг журналов](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить мониторинг журналов, какую аналитику он предоставляет и многое другое.").

* **Развёртывание OneAgent:** единый интерфейс управления экземплярами Dynatrace OneAgent. Можно устанавливать и удалять Dynatrace OneAgent в качестве расширений на Azure Virtual Machines и Azure App Services.

**Ограничения:**

* Интеграция создаёт новую среду и аккаунт Dynatrace; запустить её в существующей среде Dynatrace невозможно.

Azure Marketplace

Azure Native Dynatrace Service доступен через [Azure Marketplace](https://dt-url.net/9n039mv).

Чтобы получить индивидуальное частное предложение для Azure Native Dynatrace Service, обратитесь в отдел продаж Dynatrace по адресу [sales@dynatrace.com](mailto:sales@dynatrace.com).

## Предварительные требования

Активация частного плана для Azure Native Dynatrace Service

Azure Native Dynatrace Service доступен через [частный план](https://dt-url.net/3d03xln). Чтобы Dynatrace создал для вас частный план, [свяжитесь с Dynatrace](https://dt-url.net/m003xf1). После принятия предложения частный план для Azure Native Dynatrace Service будет доступен в Azure Marketplace.

Регистрация поставщика ресурсов Dynatrace

Чтобы создавать ресурсы Dynatrace и управлять ими через Azure Portal, необходимо зарегистрировать поставщика ресурсов Dynatrace с именем `Dynatrace.Observability` в подписке Azure.

Как зарегистрировать поставщика ресурсов Dynatrace

На Azure Portal

Через Azure CLI

Следуйте инструкциям в разделе [Поставщики ресурсов и типы Azure](https://dt-url.net/fu03x5j).

Выполните приведённую ниже команду, заменив `<subscription-id>` на идентификатор своей подписки.

```
az provider register --namespace Dynatrace.Observability --subscription <subscription-id>
```

Настройка разрешений

#### Общие разрешения

* Требуется разрешение `Contributor` для подписки Azure.

Первый пользователь, создавший первый ресурс и среду Dynatrace в подписке, становится владельцем аккаунта Dynatrace, созданного при развёртывании интеграции. Для всех последующих ресурсов и сред Dynatrace, созданных в той же подписке другими пользователями, владелец аккаунта также будет иметь полные права.

## Настройка интеграции

При первом развёртывании Azure Native Dynatrace Service создаётся новая среда Dynatrace, размещённая на новом ресурсе Dynatrace.

* Ресурс Dynatrace создаётся в подписке Azure и группе ресурсов, выбранных при развёртывании. Настраивать, управлять и устранять неполадки ресурса Dynatrace можно из Azure Portal.
* Среда Dynatrace создаётся в том же регионе Azure, в котором создаётся ресурс Dynatrace. В этой новой среде:

  + После [установки OneAgent](#oa) можно начать мониторинг [метрик](/managed/analyze-explore-automate/metrics-classic "Узнайте о классических метриках, предлагаемых Dynatrace.") из ресурсов Azure. Также можно собирать метрики со [стандартных сервисов](/managed/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration#default "Настройте среду Dynatrace SaaS с помощью Azure Marketplace.")
  + Можно собирать [журналы](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить мониторинг журналов, какую аналитику он предоставляет и многое другое.") из ресурсов Azure
  + ActiveGate среды для этой интеграции не требуется.

Настройка интеграции

1. Откройте подписку Azure, в которой нужно создать ресурс Dynatrace.
2. Выберите **Resources**, затем выберите **Create**.
3. Найдите **Azure Native Dynatrace Service**. Должно появиться сообщение о доступности частного продукта.
4. Выберите плитку **Azure Native Dynatrace Service**.
5. В списке выбора плана выберите частный план, принятый в разделе [Активация частного плана для Azure Native Dynatrace Service](#step-1), затем нажмите **Subscribe**.
6. На странице **Create a new Dynatrace environment** нажмите **Create**.
7. В разделе **Basics** для поля **Resource group** укажите, нужно ли создать новую группу ресурсов или использовать существующую.

   Группа ресурсов (resource group): контейнер, в котором хранятся связанные ресурсы решения Azure. Подробнее см. в разделе [Обзор групп ресурсов Azure](https://dt-url.net/xv43x96).
8. Введите **Resource name** для ресурса Dynatrace, затем выберите **Region** из выпадающего меню. Ресурс Dynatrace в Azure и среда Dynatrace будут созданы в выбранном регионе.
9. Выберите **Pricing plan**, затем нажмите **Next: Metrics and Logs**.
10. Необязательно: выберите, нужно ли включить **Send subscription activity logs** и/или **Send Azure resource logs**. Подробнее см. в разделе [Настройка метрик и журналов](#metrics-logs).

    Если выбрать **Send Azure resource logs for all defined services**, журналы ресурсов Azure по умолчанию отправляются для всех определённых ресурсов, то есть журналы собираются для всех поддерживаемых ресурсов. Чтобы фильтровать конкретный набор ресурсов Azure, отправляющих журналы в Dynatrace, можно использовать теги ресурсов Azure. Правила тегов:

    * Ресурсы Azure с тегами `Include` отправляют журналы в Dynatrace.
    * Ресурсы Azure с тегами `Exclude` не отправляют журналы в Dynatrace.
    * При конфликте правил включения и исключения приоритет имеют правила исключения.

      Лимит записей для тегов `Include` и `Exclude` составляет по 20 записей.
11. Нажмите **Next: Single sign-on**.
12. Необязательно: выберите, нужно ли включить **Enable SSO through Microsoft Entra ID**.

    * Если эта функция не нужна, нажмите **Next: Tags**.
    * Если нужно включить эту функцию, выберите её, укажите отображаемый идентификатор приложения Dynatrace, затем нажмите **Next: Tags**.
13. Необязательно: [укажите теги](#tags) для нового ресурса Dynatrace, затем нажмите **Next: Review + create**.
14. Проверьте правильность введённых данных, затем нажмите **Create**. После завершения развёртывания можно нажать **Go to resource** для перехода к конкретному ресурсу Dynatrace.

## Привязка нескольких подписок Azure к одной среде Dynatrace (необязательно)

Убедитесь, что аккаунт Azure имеет доступ к аккаунту Dynatrace со следующими разрешениями:

* Просмотр аккаунта (View Account)
* Просмотр среды (View Environment)
* Установка OneAgent (Install OneAgent)
* Управление параметрами мониторинга (Manage Monitoring Settings)

Подробнее см. в разделе [Разрешения среды](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Разрешения на уровне среды.").

После развёртывания интеграции Azure можно:

* Привязать дополнительные подписки Azure к только что созданной среде Dynatrace.
* Привязать несколько сред Dynatrace к одной подписке Azure.

  При привязке нескольких подписок Azure и создании ресурса необходимы привилегии аккаунта Dynatrace `tenant-manage-settings` и разрешения `tenant-agent-install`. Подробнее о настройке этих разрешений см. в разделе [Разрешения на основе ролей](/managed/manage/identity-access-management/permission-management/role-based-permissions "Разрешения на основе ролей.").

Выполните приведённые ниже шаги, повторив процедуру для каждой подписки, которую нужно привязать.

1. Откройте Azure Portal и найдите `Azure Native Dynatrace Service` через строку поиска вверху.
2. Выберите **Azure Native Dynatrace Service**.
3. Нажмите **Create**.
4. В разделе **Basics** для поля **Resource group** укажите, нужно ли создать новую группу ресурсов или использовать существующую.

   Группа ресурсов (resource group): контейнер, в котором хранятся связанные ресурсы решения Azure. Подробнее см. в разделе [Обзор групп ресурсов Azure](https://dt-url.net/xv43x96).
5. Введите **Resource name**, затем выберите **Region** из выпадающего меню.

   Привязываемая среда Dynatrace и новый ресурс Dynatrace должны находиться в одном регионе.
6. Выберите **Dynatrace environment** для привязки к подписке Azure, затем нажмите **Next: Metrics and Logs**.
7. Необязательно: выберите, нужно ли включить **Send subscription activity logs** и/или **Send Azure resource logs**. Подробнее см. в разделе [Настройка метрик и журналов](#metrics-logs).

   Если выбрать **Send Azure resource logs for all defined services**, журналы ресурсов Azure по умолчанию отправляются для всех определённых ресурсов, то есть журналы собираются для всех поддерживаемых ресурсов. Чтобы фильтровать конкретный набор ресурсов Azure, отправляющих журналы в Dynatrace, можно использовать теги ресурсов Azure. Правила тегов:

   * Ресурсы Azure с тегами `Include` отправляют журналы в Dynatrace.
   * Ресурсы Azure с тегами `Exclude` не отправляют журналы в Dynatrace.
   * При конфликте правил включения и исключения приоритет имеют правила исключения.
8. Пропустите **Next: Single sign-on** (SSO можно настроить только после развёртывания) и нажмите **Next: Tags**.
9. Необязательно: [укажите теги](#tags) для нового ресурса Dynatrace, затем нажмите **Next: Review + create**.
10. Проверьте правильность введённых данных, затем нажмите **Create**. После завершения развёртывания можно нажать **Go to resource** для перехода к конкретному ресурсу Dynatrace.

## Доступ к среде Dynatrace

После настройки интеграции доступ к среде Dynatrace можно получить непосредственно из Azure Portal.

В Azure Portal перейдите к ресурсу Dynatrace и выберите **Overview**. Там отобразятся все сведения о среде Dynatrace, включая прямые ссылки на следующие страницы веб-интерфейса:

* **Dashboards**: подробнее см. в разделе [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать Dynatrace Dashboards Classic, управлять ими и использовать их.").
* **Log Viewer**: подробнее см. в разделе [Log viewer (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Узнайте, как использовать просмотрщик журналов Dynatrace для анализа данных журналов.").
* **Smartscape topology**: подробнее см. в разделе [Визуализация среды через Smartscape](/managed/analyze-explore-automate/smartscape-classic "Узнайте, как Smartscape визуализирует все сущности и зависимости в вашей среде.").

## Настройка метрик и журналов

### Метрики

* Можно активировать [метрики](/managed/analyze-explore-automate/metrics-classic "Узнайте о классических метриках, предлагаемых Dynatrace.") после развёртывания интеграции Azure.

Сбор метрик с Virtual Machines и App Services

Чтобы начать сбор метрик с Virtual Machines и App Services, необходимо [установить Dynatrace OneAgent на этих ресурсах в качестве расширения](#oa).

Сбор метрик с облачных сервисов

Все сервисы и метрики включены по умолчанию. При необходимости их можно отключить, нажав кнопку удаления в списке сервисов.
После подключения Dynatrace к среде Azure немедленно начинается мониторинг встроенных сервисов Azure для определённого вами service principal. В разделе [Классические метрики Azure (ранее встроенные)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/default-azure-metrics "Список классических метрик, собираемых Dynatrace по умолчанию для мониторинга Azure.") приведён список метрик облачных сервисов Azure, собираемых по умолчанию.

### Управление облачными сервисами

Все облачные сервисы мониторятся по умолчанию, но их можно быстро отключить из списка или повторно включить при необходимости.

Добавление сервисов в мониторинг

1. Откройте **Settings** > **Cloud and virtualization** > **Azure**.
2. На странице обзора Azure найдите нужное подключение и нажмите **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") в этой строке.
3. В разделе **Services** выберите **Manage services**.
4. Для каждого сервиса, который нужно добавить: выберите **Add service**, выберите сервис из списка, затем снова нажмите **Add service**.
5. Нажмите **Save changes**, чтобы сохранить конфигурацию.

Настройка собираемых метрик для каждого сервиса

После добавления сервиса Dynatrace автоматически начинает собирать набор метрик для него.

Рекомендуемые метрики:

* Включены по умолчанию и не могут быть отключены.
* Могут включать рекомендуемые измерения (включены по умолчанию, нельзя отключить) и необязательные измерения (отключены по умолчанию, можно включить).

Помимо рекомендуемых метрик, большинство сервисов позволяют включать необязательные метрики, которые можно добавлять и настраивать вручную.

Список облачных сервисов Azure и собираемых метрик

Полный список облачных сервисов Azure и сведения о собираемых метриках см. в разделе [Все облачные сервисы Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Мониторинг сервисов Azure с помощью Dynatrace и просмотр доступных метрик.").

Также можно просмотреть список поддерживаемых сервисов Azure в Dynatrace Hub внутри продукта (поиск по **Azure**) или в [веб-версии Dynatrace Hub](https://www.dynatrace.com/hub/?query=azure).

Добавление и настройка метрик

1. Откройте **Settings** > **Cloud and virtualization** > **Azure**.
2. На странице обзора Azure найдите нужное подключение и нажмите **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") в этой строке.
3. В разделе **Services** выберите **Manage services**.
4. Выберите сервис, для которого нужно добавить метрики. На странице сведений о сервисе отображается список уже отслеживаемых метрик.
5. Нажмите **Add metric**.
6. В списке **Add new metric** выберите метрику, затем нажмите **Add metric**.
7. Нажмите ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row"), чтобы раскрыть сведения о метрике и настроить её.
8. Нажмите **Apply**, чтобы сохранить конфигурацию.

После выбора облачных сервисов и сохранения изменений мониторинг вновь добавленных сервисов запускается автоматически.

### Журналы

* Можно активировать [журналы](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить мониторинг журналов, какую аналитику он предоставляет и многое другое.") [во время развёртывания интеграции Azure](#setup) или [после развёртывания](#how-to-logs).

Можно настроить два типа журналов из Azure в Dynatrace: [журналы активности подписки](#activity) и [журналы ресурсов Azure](#resource).

#### Журналы активности подписки

Журналы активности подписки содержат сведения об операциях (PUT, POST, DELETE), выполняемых с каждым ресурсом Azure в подписке (плоскость управления). Для каждой подписки Azure существует один журнал активности.

#### Журналы ресурсов Azure

Журналы ресурсов Azure содержат сведения об операциях, выполняемых внутри ресурса Azure (плоскость данных), например получение секрета из хранилища ключей или запрос к базе данных. Содержимое журналов ресурсов зависит от сервиса Azure и типа ресурса.

Все сервисы Azure из [категорий журналов Azure Monitor](https://dt-url.net/fja38sr) принимают журналы, включая Microsoft Entra ID и [Azure Monitor Integration Service](https://dt-url.net/dpc38am).

Список журналов ресурсов Azure см. в разделе [Поддерживаемые категории журналов ресурсов Azure Monitor](https://dt-url.net/ea03xvn).

#### Активация журналов после развёртывания

Активация журналов активности подписки

Активация журналов ресурсов Azure

1. На Azure Portal перейдите к ресурсу Dynatrace и выберите **Metrics and logs**.
2. Выберите **Send subscription activity logs**.
3. Нажмите **Save**.

1. На Azure Portal перейдите к ресурсу Dynatrace и выберите **Metrics and logs**.
2. Выберите **Send Azure resource logs for all defined sources**.

   При выборе этого параметра журналы ресурсов Azure по умолчанию отправляются для всех определённых ресурсов, то есть журналы собираются для всех поддерживаемых ресурсов.
3. Необязательно: чтобы фильтровать конкретный набор ресурсов Azure, отправляющих журналы в Dynatrace, можно использовать теги ресурсов Azure. Правила тегов:

   * Ресурсы Azure с тегами `Include` отправляют журналы в Dynatrace.
   * Ресурсы Azure с тегами `Exclude` не отправляют журналы в Dynatrace.
   * При конфликте правил включения и исключения приоритет имеют правила исключения.
4. Нажмите **Save**.

Azure Native Dynatrace Service автоматически включает log forwarding в подписке Azure, в которой включён ресурс Dynatrace. Log forwarding включается для всех поддерживаемых сервисов и ресурсов. Можно определить правила фильтрации по тегам для включения или исключения определённых ресурсов Azure из отправки журналов.

Azure Native Dynatrace Service использует токен доступа Dynatrace с именем `azure-native-integration`, ротация которого выполняется каждые 24 часа.

## Создание тегов

* Можно создавать [теги](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.") [во время развёртывания интеграции Azure](#setup) или [после развёртывания](#how-to-tags).

Теги можно применять к ресурсам Azure, группам ресурсов и подпискам для логической организации их в таксономию. Можно указать теги для нового ресурса Dynatrace в Azure, добавив пользовательские пары ключ/значение:

* В поле **Name** введите имя тега, соответствующего ресурсу Azure Dynatrace (например, `owner`).
* В поле **Value** введите значение тега, соответствующего ресурсу Azure Dynatrace (например, адрес электронной почты владельца).

Если теги не заданы, все журналы с отслеживаемых ресурсов подписки Azure отправляются в Dynatrace.

### Создание тегов после развёртывания

На Azure Portal перейдите к новому ресурсу Dynatrace и выберите **Tags**. Также можно выбрать **Monitored resources**, затем нажать **Edit tags** для нужных ресурсов.

## Управление отслеживаемыми ресурсами в Azure Portal

После развёртывания Azure Native Dynatrace Service можно просматривать, управлять и отслеживать ресурсы Azure, а также устанавливать OneAgent на Azure Virtual Machines и Azure App Services.

Чтобы просмотреть список ресурсов, на Azure Portal перейдите к ресурсу Dynatrace и выберите **Monitored resources**. Список можно фильтровать по: **Resource name** (имя ресурса Azure), **Resource type** (тип ресурса Azure), **Resource group** (имя группы ресурсов для ресурса Azure), **Region** (расположение ресурса Azure) и **Logs to Dynatrace** (отправляет ли ресурс журналы в Dynatrace).

## Развёртывание OneAgent на Azure Virtual Machines и Azure App Services

* OneAgent можно развернуть после развёртывания интеграции Azure.

Для мониторинга Azure Virtual Machines или Azure App Services можно установить Dynatrace OneAgent на этих ресурсах в качестве расширения.

Установка OneAgent на виртуальную машину

Установка OneAgent на App Service

1. На Azure Portal перейдите к ресурсу Dynatrace и выберите **Virtual Machines**.
2. Выберите виртуальную машину из списка, на которой нужно установить расширение OneAgent.
3. Нажмите **Install extension**.
4. Необязательно: выберите, нужно ли включить аналитику журналов.
5. Необязательно: укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов.") для OneAgent.
6. Нажмите **OK**, чтобы начать процесс установки.
7. После завершения установки в поле **OneAgent status** для выбранной виртуальной машины отобразится **Installed**.

* Чтобы просмотреть сведения об установленном OneAgent, выберите виртуальную машину и перейдите в раздел **Extensions**.
* Чтобы удалить OneAgent, выберите виртуальную машину, затем нажмите **Uninstall extension**.

1. На Azure Portal перейдите к ресурсу Dynatrace и выберите **App Services**.
2. Из списка выберите App Service, на котором нужно установить расширение OneAgent.
3. Нажмите **Install extension**.
4. Необязательно: выберите, нужно ли включить аналитику журналов.
5. Необязательно: укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов.") для OneAgent.
6. Нажмите **OK**, чтобы начать процесс установки.
7. После завершения установки в поле **OneAgent status** для выбранной виртуальной машины отобразится **Installed**.

* Чтобы просмотреть сведения об установленном OneAgent, выберите App Service и перейдите в раздел **Extensions**.
* Чтобы удалить OneAgent, выберите App Service, затем нажмите **Uninstall extension**.

Если App Service не отображается в Dynatrace после включения интеграции, перезапустите App Service Plan.

Чтобы запустить OneAgent на Virtual Machine Scale Sets с интеграцией Dynatrace Azure, используйте [расширение Dynatrace OneAgent для Virtual Machines](#vm) и создайте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях действия.").

## Удаление Azure Native Dynatrace Service

Чтобы удалить Azure Native Dynatrace Service, необходимо удалить ресурс Dynatrace. После удаления ресурса Dynatrace из Azure журналы и метрики перестают отправляться в Dynatrace, а все расчёты за Dynatrace через Azure Marketplace прекращаются.

Удаление ресурса Dynatrace

1. На Azure Portal перейдите к ресурсу Dynatrace и выберите **Overview**.
2. Нажмите **Delete**.
3. Введите имя приложения, которое нужно удалить, затем нажмите **Delete**.

## Как запросить новые функции

Чтобы предложить новую функцию, воспользуйтесь [Microsoft Developer Community](https://dt-url.net/po239hy).

## Устранение неполадок

* [Не удаётся включить интеграцию SSO](https://dt-url.net/tq237c7)
* [Нет разрешений для настройки SSO для связанной среды Dynatrace](https://dt-url.net/3o038vp)
* [Как получить журналы из подписки Azure в другом тенанте Azure?](https://dt-url.net/4rc37kk)
* [Ресурсы Azure не пересылают журналы в Dynatrace](https://dt-url.net/il438i2)

## Вопросы и ответы по приёму журналов

* [Какие ограничения существуют для приёма журналов в Azure Native Dynatrace Service?](https://dt-url.net/ine37te)
* [Как ведение журналов Azure Native Dynatrace Service влияет на стоимость Azure?](https://dt-url.net/da2380g)
* [Разве не дешевле отправлять данные с помощью существующего log forwarding Dynatrace Azure в Dynatrace SaaS в AWS, а не использовать Azure Native Dynatrace Service?](https://dt-url.net/bp038gb)

## Связанные темы

* [Интеграции с Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройте глубокий мониторинг кода Azure с помощью OneAgent или OpenTelemetry.")