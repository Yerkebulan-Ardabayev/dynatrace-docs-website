---
title: Установка плитки Dynatrace Service Broker для Cloud Foundry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/install-the-service-broker-for-cloud-foundry-dashboard-tile
scraped: 2026-05-12T11:09:24.551149
---

# Установка плитки Dynatrace Service Broker для Cloud Foundry

# Установка плитки Dynatrace Service Broker для Cloud Foundry

* 3-min read
* Published Aug 03, 2018

Данная статья описывает установку и настройку плитки Dynatrace Service Broker для VMware Tanzu Platform (ранее Pivotal Platform), а также настройку мониторинга приложений через сервис Dynatrace SaaS/Managed путём создания экземпляра сервиса и его привязки к приложению.

## Установка плитки Dynatrace Service Broker

Установите плитку Dynatrace Service Broker через **Ops Manager Installation Dashboard**, выполнив следующие шаги:

1. Загрузите файл продукта с [Broadcom Support](https://dt-url.net/nb03qvh).
2. Загрузите файл продукта через **Ops Manager Installation Dashboard**.
3. Нажмите **Add next** рядом с загруженной плиткой Dynatrace Service Broker в разделе **Ops Manager Available Products view**, чтобы добавить её в область подготовки.
4. Выберите добавленную плитку Dynatrace Service Broker для открытия параметров конфигурации.
5. Нажмите **Save**.

## Настройка плитки Dynatrace Service Broker

Одновременно можно поддерживать несколько окружений Dynatrace SaaS/Managed.

Для настройки плитки Dynatrace Service Broker выполните следующие шаги:

1. В **Tanzu Ops Manager** выберите плитку Dynatrace Service Broker для открытия параметров конфигурации.

   ![Pivotal 1](https://dt-cdn.net/images/configure-broker-1-1139-b706fcc7e1.png)

   Pivotal 1

2. Нажмите **Assign AZs and Networks** для настройки сети и зон доступности.

   ![Pivotal 2](https://dt-cdn.net/images/pivotal2-918-717f876ef5.png)

   Pivotal 2

3. Перейдите в **SaaS/Managed Plans** и нажмите кнопку **Add** в правом верхнем углу для добавления сервисного плана.

   ![Pivotal 3](https://dt-cdn.net/images/configure-broker-2-1400-bab7e386a3.png)

   Pivotal 3

   Выполните следующие шаги для создания и настройки каждого сервисного плана:

   * Введите `Plan Name`.
   * Введите **Environment ID** и **Paas token**.
   * Введите **apiURL**.
   * Нажмите **Save**.

   Настройте `apiurl` в соответствии с вашим окружением:

   Для Dynatrace SaaS с подключением к интернету

   Замените `ENVIRONMENTID` в `https://ENVIRONMENTID.live.dynatrace.com/api` на ваш ID окружения.

   Для Dynatrace SaaS без доступа к интернету

   Используйте `https://YourActiveGateIP:Port/api` или `FQDN:9999/e/<ENVIRONMENTID>/api` для загрузки OneAgent и маршрутизации трафика через ActiveGate.

   Для Dynatrace Managed

   Используйте `https://YourActiveGateIP:Port/api`, `https://FQDN/e/<ENVIRONMENTID>/api` или IP-адрес ActiveGate для прямого подключения.
   В зависимости от настроек может потребоваться указать порт.

4. Нажмите **Apply Changes**.

## Настройка мониторинга приложений

Для настройки мониторинга приложений с помощью сервиса Dynatrace SaaS/Managed привяжите сервис к приложению в [Apps Manager](https://dt-url.net/3j23qbc) или используйте [cf CLI](https://dt-url.net/b543qgc). Выполните команду ниже для передачи параметров.

1. Создайте экземпляр сервиса на основе настроенных планов.

   ```
   cf create-service SERVICE PLAN SERVICE_INSTANCE
   ```

   * **SERVICE** должен быть `dynatrace`.
   * **PLAN** зависит от планов, настроенных в **Ops Manager**; в примере выше это `planname`.
   * **SERVICE\_INSTANCE** — имя сервиса `cf`, который будет создан и привязан к приложению.

2. Привяжите сервис к приложению, например с помощью [cf CLI](https://dt-url.net/9b63qbn).

   ```
   cf bind-service APP_NAME SERVICE_INSTANCE
   ```

   * **APP\_NAME** — имя вашего приложения.
   * **SERVICE\_INSTANCE** — имя экземпляра сервиса, созданного командой выше.

После привязки сервиса к приложению [начните использовать Dynatrace SaaS/Managed](https://dt-url.net/6q03pwu).

## Связанные темы

* [Мониторинг Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Мониторинг Cloud Foundry с помощью Dynatrace.")