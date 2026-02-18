---
title: Create remote/multi-environment Dynatrace dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment
scraped: 2026-02-18T21:26:30.118956
---

# Create remote/multi-environment Dynatrace dashboards

# Create remote/multi-environment Dynatrace dashboards

* How-to guide
* 8-min read
* Updated on Jun 04, 2024

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

A Dynatrace dashboard can include monitoring artifacts (such as metrics, logs, events, user sessions, and server-side traces) from multiple Dynatrace environments and can even support remote management zones (for tiles that support custom management zones).

## Overview

### Advantages

Dynatrace dashboards serve as a single pane of glass for monitoring artifacts such as metrics, logs, events, and user sessions. With multi-environment dashboards, your dashboards can combine these monitoring artifacts from separate Dynatrace environments.

After you configure the remote connection in your local Dynatrace environment, [you can quickly point dashboard tiles to the remote environment](#tile).

![Example: select remote environment for tile](https://dt-cdn.net/images/select-tile-environment-example-317-72348cc81f.png)

For tiles that allow a custom management zone (look for the **Custom management zone** setting in the configuration panel for the tile), you can specify another management zone.

Because the remote-environment capabilities of dashboard tiles allow you to build a common overview of problems and other data, dashboards can essentially serve as a hub for deeper analysis. A single click on any given dashboard tile displaying remote information takes you straight into a dedicated view of the remote environment where you can continue your analysis.

### Limitations

* A remote environment tile is backward compatible for up to five versions.

  + A remote environment tile running in a Dynatrace version *x* environment will work correctly with Dynatrace version *x*-5 or later deployed in the remote environment.

    When there's a difference of more than five versions between the local and remote versions, the tile may still work but that configuration is not supported.
  + A remote environment tile displays data based on the features included in the remote environment's cluster version.

    For example, if a remote environment tile depends on a feature that was added in Dynatrace version *x*, and that version is deployed locally, but the remote environment is still running Dynatrace version *x*-1, the feature won't be displayed in the local dashboard because the remote environment doesn't support it.

    If a remote environment tile depends on a feature that is not supported in the remote environment, the tile displays an error message explaining the discrepancy between the local and remote environments.
  + To maintain maximum compatibility between local and remote environments, keep your Dynatrace environments on the same version.
* Remote-environment connections donât pass user context and permissions over environment boundaries.

  For this reason, the best practice is to use management zones to segment/limit dashboard tiles when viewing remote information.

  Because of the above consideration, remote-environment dashboards can be configured only by environment administrators. Regular users can still view and interact with remote-environment dashboards without limitation.
* The world map dashboard tile isnât suited for (and therefore doesnât support) remote-environment scenarios.

## Configuration

To create a dashboard tile that queries data from a remote environment:

* In the remote Dynatrace environment, [create an access token](#token) that permits you to query data from that environment
* In the local Dynatrace environment, [add the remote environment](#link) to the table of remote environments
* In the local Dynatrace environment, [create one or more tiles that display remote data](#tile) queried from the remote environment

API equivalents

The procedures that follow use the Dynatrace web UI. To carry out the equivalent tasks via API, see:

* [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.")âto create a token in the remote environment
* [Remote environments API](/docs/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.")âto create a link to the remote environment from the local environment
* [Dashboards Classic API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")âto configure a dashboard with tiles that query the remote environment

### Create an access token

With this procedure, you get an access token from the remote environment that you need in the other steps.

To create an access token for the remote Dynatrace environment

1. Sign in to the remote environment.

   * This is the environment from which you pull data.
   * If you can't sign in to the remote environment, someone with access to the remote environment can do this procedure for you.
2. Go to **Access Tokens**.
3. Select **Generate new token**.
4. Enter a token name.
5. Find the **Fetch data from a remote environment** scope (`RestRequestForwarding`) and select its checkbox.
6. Select **Generate token**.  
   This generates a token that gives your local environment permission to pull data from this remote environment.
7. Select **Copy** and then paste the token to a secure location.  
   It's a long string that you need to copy and paste back into Dynatrace later.

### Add the remote environment

To add the remote Dynatrace environment to your list of available remote environments

1. Sign in to your local Dynatrace environment.
2. Go to **Settings**.
3. Select **Integration** > **Remote environments**.
4. Select **Connect environment**.
5. Define the remote environment from which your local environment pulls data, and then select **Save changes**.

   * **Name** is the name under which this environment will be listed in your local Dynatrace environment when you configure a tile to query this remote environment. This is freeform text. It doesn't affect the remote environment.
   * **Remote environment URI**

     + For Dynatrace SaaS, it needs to be in the following format:

       `https://<ENVIRONMENTID>.live.dynatrace.com/`

       Replace `<ENVIRONMENTID>` with your actual environment ID.
     + For Dynatrace Managed, any URI is allowed.
     + To connect a Dynatrace (SaaS deployment) environment to a Dynatrace Managed deployment via a URI that is outside the `dynatrace-managed.com` domain, contact a Dynatrace product expert via live chat within your Dynatrace environment.
   * **Network scope**

     + `External`: The remote environment is located in another network. Globally configured proxy settings are used if present. This is the default scope.
     + `Internal`: The remote environment is located in the same network. Globally configured proxy settings are not used.
     + `Cluster`: The remote environment is located in the same cluster. The request is made to `localhost`.

     Dynatrace SaaS can only use the `External` network scope.
   * **Token** is the token you generated in the previous procedure. It needs to include the **Fetch data from a remote environment** scope (`RestRequestForwarding`).
   * **Test connection** checks the connection from your local environment to the remote environment.

     Be sure to get a `connection successfully established` message before continuing.

Now that you have established a link to the remote environment, you can create dashboard tiles that query that environment.

### Create a tile that displays remote data

Чтобы создать плитку, которая получает данные из удаленной среды

1. Отобразите панель мониторинга, на которой будет отображаться плитка.
2. Выберите **Редактировать**.
3. Выберите или добавьте плитку, на которой вы хотите отобразить данные из удаленной среды.  
   Раздел **Environment** панели настроек плитки отображает имя среды, из которой эта плитка получает данные мониторинга.

   * **По умолчанию (локально)** настраивает плитку на получение данных из локальной среды Dynatrace.
   * Все другие перечисленные среды являются удаленными средами, для которых установлено соединение.
4. Выберите удаленную среду, которую вы хотите, чтобы выбранная плитка запрашивала.  
   Если вы назвали удаленную среду `Бостон` при добавлении удаленной среды в предыдущей процедуре, `Бостон` должен быть в этом списке.

   ![Пример: выбор удаленной среды для плитки](https://dt-cdn.net/images/select-tile-environment-example-317-72348cc81f.png)
5. Выберите **Готово**, чтобы отобразить завершенную панель мониторинга.
6. Наведите указатель мыши на иконку фильтра плитки, чтобы увидеть выбор среды.

   ![Пример: отображение фильтров плитки, чтобы увидеть выбор удаленной среды](https://dt-cdn.net/images/tile-remote-environment-tooltip-example-495-96be8d3ec4.png)

## Примеры

### Одни и те же плитки, разные среды

В этом примере мы создаем панель мониторинга, которая отображает состояние здоровья хоста и сетевой статус для локальной среды и удаленной среды рядом. Мы предполагаем, что вы уже добавили удаленную среду в свою локальную среду.

1. Перейдите к ![Классические панели мониторинга](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Классические панели мониторинга") **Классические панели мониторинга**, выберите **Создать панель мониторинга**, дайте ей имя и выберите **Создать**.
2. Перетащите две плитки **Заголовок** на панель мониторинга (или перетащите одну и затем клонируйте ее).
3. Отредактируйте один заголовок, чтобы он говорил **Локально**, и другой, чтобы он говорил **Удаленно**.
4. Перетащите две плитки **Состояние здоровья хоста** на панель мониторинга (или перетащите одну и затем клонируйте ее).  
   Поместите одну под заголовком **Локально** и другую под заголовком **Удаленно**.
5. Перетащите две плитки **Сетевой статус** на панель мониторинга (или перетащите одну и затем клонируйте ее).  
   Поместите одну под заголовком **Локально** и другую под заголовком **Удаленно**.

   На этом этапе все плитки запрашивают локальную среду, поэтому у вас есть две одинаковые плитки **Состояние здоровья хоста** и две одинаковые плитки **Сетевой статус**.

   ![Одинаковые плитки, одна и та же среда](https://dt-cdn.net/images/same-tiles-same-environments-595-51063546a9.png)
6. Под заголовком **Удаленно** отредактируйте плитки **Состояние здоровья хоста** и **Сетевой статус**, чтобы обе они запрашивали удаленную среду (`Бостон` в этом примере).

   ![Пример: выбор удаленной среды для плитки](https://dt-cdn.net/images/select-tile-environment-example-317-72348cc81f.png)
7. Выберите **Готово**, чтобы отобразить панель мониторинга.

   * Плитки под **Локально** по-прежнему отображают локальную информацию о хосте и сети.
   * Плитки под **Удаленно** теперь запрашивают удаленную среду:

     + Удаленные плитки отображают состояние здоровья хоста и сетевой статус для удаленной среды, а не для локальной среды по умолчанию.
     + Удаленные плитки каждая отображают иконку фильтра. Наведите указатель мыши на иконку, чтобы увидеть имя среды.

   ![Одинаковые плитки, разные среды](https://dt-cdn.net/images/same-tiles-different-environments-595-d747473897.png)

Вы можете, конечно, добавить другие типы плиток и указать на дополнительные удаленные среды.

## Устранение неполадок

[Сообщение `Verification failed, please check your settings: Constraints violated.` отображается при добавлении удаленной среды](https://dt-url.net/t903mr6)

## Связанные темы

* [Классические панели мониторинга API](/docs/dynatrace-api/configuration-api/dashboards-api "Узнайте, как управлять конфигурацией панели мониторинга через классическую конфигурацию Dynatrace API. ")
* [Удаленные среды API](/docs/dynatrace-api/configuration-api/remote-environments "Управляйте конфигурациями удаленных сред Dynatrace через конфигурацию Dynatrace API. ")
* [Что такое среда мониторинга?](/docs/discover-dynatrace/get-started/monitoring-environment "Поймите и узнайте, как работать с средами мониторинга. ")