---
title: Управление средами мониторинга
source: https://docs.dynatrace.com/managed/managed-cluster/operation/manage-your-monitoring-environments
scraped: 2026-05-12T11:22:12.862572
---

# Управление средами мониторинга

# Управление средами мониторинга

* Published Aug 10, 2017

Вы можете легко создавать среды мониторинга и управлять ими с помощью Cluster Management Console.

![Managed deployment](https://dt-cdn.net/images/managed-deployment-1329-1278e41da4.png)

Managed deployment

## Создание среды

1. Перейдите в **Environments**.
2. Нажмите кнопку **+ Add another environment**.
3. В текстовом поле **Environment name** введите имя среды.
4. (Необязательно) Можно отключить Synthetic-мониторы, переведя переключатель **Enable synthetic monitors** в положение **off**.
5. Нажмите **Save**.

## Настройка среды

После создания среды и нажатия **Save** вы будете перенаправлены на страницу конфигурации среды. Однако страницу конфигурации среды можно открыть в любое время. Перейдите в **Environments** и выберите среду, которую необходимо настроить.

На странице конфигурации можно задать общие, а также ежемесячные и годовые квоты для вашей среды.

### Общие квоты среды

* **Host units** — размер хоста в лицензионных целях (определяется объёмом RAM хоста). Для полноценного мониторинга (Full-Stack Monitoring) хост с 16 ГБ RAM (или любой его частью) составляет 1 хост-юнит. Для мониторинга облачной инфраструктуры хост с 16 ГБ RAM (или любой его частью) составляет 0,3 хост-юнита.  
  Подробности см. в разделе [Расчёт потребления мониторинга](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").
* **Custom metrics** — количество уникальных метрик временных рядов в скользящем окне 24 часа.  
  Подробности см. в разделе [DDU для метрик](/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

### Ежемесячные и годовые квоты

* **User sessions** — количество пользовательских сеансов (то есть «RUM-сеансов») для мониторинга в месяц/год.  
  Подробности см. в разделе [DEM units — Real User Monitoring](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units#rum "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.").
* **Synthetic monitors** — количество Synthetic-мониторов для выполнения в месяц/год.  
  Подробности см. в разделе [Расчёт потребления мониторинга](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units#synthetic "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.").
* **Avg. daily log volume** — объём трафика Log Monitoring в месяц/год.  
  Подробности см. в разделе [Расчёт потребления мониторинга](/managed/license/monitoring-consumption-classic/log-monitoring-consumption-legacy#managed-log-storage "Understand how Log Monitoring consumption is calculated for Dynatrace versions 1.207 and earlier.").

Также можно настроить параметры хранилища, включая:

* **Transaction storage** — объём дискового пространства для транзакций (например, вызовов сервисов, стеков вызовов и SQL-запросов).
* **Symbol files from mobile apps** — объём хранилища для файлов символов из мобильных приложений.
* **Service request level retention** — время хранения дискового пространства для запросов к сервисам.
* **Service code level retention** — время хранения дискового пространства для видимости на уровне кода.
* **Real user monitoring retention** — время хранения дискового пространства для пользовательских сеансов.
* **Synthetic monitoring retention** — время хранения дискового пространства для Synthetic-мониторов.
* **Session Replay retention** — время хранения дискового пространства для данных Session Replay.
* **Log Monitoring storage** — объём дискового пространства для Log Monitoring.
* **Log Monitoring storage retention** — время хранения указанного дискового пространства для Log Monitoring.

После исчерпания любого из этих лимитов соответствующий мониторинг станет недоступен, и потребуется приобрести дополнительный мониторинг. Для приобретения Dynatrace [обратитесь в отдел продаж Dynatrace](https://dt-url.net/c901yj9). Ваш менеджер по продажам предоставит дополнительную информацию.

### Назначение разрешений среды группам пользователей

Используйте эти элементы управления для назначения разрешений среды определённым группам пользователей.  
Подробности см. в разделе [Управление группами пользователей и разрешениями](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

## Переименование среды

1. Перейдите в **Environments**.
2. Выберите среду, которую необходимо переименовать.
3. Нажмите на значок карандаша рядом с именем среды.
4. Введите новое имя и нажмите кнопку с галочкой.

## Отключение/удаление среды

1. Перейдите в **Environments**.
2. Выберите среду, которую необходимо отключить или удалить.
3. Нажмите кнопку **Browse** (**…**) в правом верхнем углу.
4. Выберите **Disable environment** или **Permanently delete environment**.

## Доступ к среде

Для доступа к среде со страницы администрирования Dynatrace Managed:

1. Перейдите в **Environments**.
2. Выберите среду, к которой необходимо получить доступ.
3. Нажмите кнопку **Go to environment** в правом верхнем углу.  
   На вашей панели управления будут отображены данные мониторинга выбранной среды.

   ![Dashboard](https://dt-cdn.net/images/dashboard-2235-901caf1901.png)

   Dashboard

Альтернативный способ доступа к среде со страницы администрирования Dynatrace Managed:

1. Откройте меню пользователя, нажав на значок пользователя в правом верхнем углу.
2. Откройте раскрывающийся список **Cluster Management**.
3. Выберите среду, к которой необходимо получить доступ.

Для возврата в Cluster Management Console в любое время:

1. В представлении панели управления откройте меню пользователя, нажав на значок пользователя в правом верхнем углу.
2. Нажмите на имя среды, чтобы открыть раскрывающийся список.
3. Выберите **Cluster Management**.

## Переключение между средами

Находясь в представлении панели управления конкретной среды:

1. Откройте меню пользователя, нажав на значок пользователя в правом верхнем углу.
2. Нажмите на имя среды, чтобы открыть раскрывающийся список.
3. Выберите другую среду, к которой необходимо получить доступ.