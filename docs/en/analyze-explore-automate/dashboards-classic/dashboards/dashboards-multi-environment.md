---
title: Create remote/multi-environment Dynatrace dashboards
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment
scraped: 2026-02-21T21:12:13.150473
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

To create a tile that pulls data from the remote environment

1. Display the dashboard that will display the tile.
2. Select **Edit**.
3. Select or add a tile on which you want to display data from the remote environment.  
   The **Environment** section of the tile settings pane displays the name of the environment from which that tile pulls monitoring data.

   * **Default (local)** configures the tile to pull its data from the local Dynatrace environment.
   * All other listed environments are remote environments for which a connection has been established.
4. Select the remote environment that you want the selected tile to query.  
   If you named the remote environment `Boston` when you added the remote environment in the previous procedure, `Boston` should be on this list.

   ![Example: select remote environment for tile](https://dt-cdn.net/images/select-tile-environment-example-317-72348cc81f.png)
5. Select **Done** to display the finished dashboard.
6. Hover over the tile filter icon to see the environment selection.

   ![Example: display tile filters to see remote environment selection](https://dt-cdn.net/images/tile-remote-environment-tooltip-example-495-96be8d3ec4.png)

## Examples

### Same tiles, different environments

In this example, we create a dashboard that shows the host health and network status for the local environment and a remote environment side by side. We assume that you have already added the remote environment to your local environment.

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**, select **Create dashboard**, give it a name, and select **Create**.
2. Drag two **Header** tiles to the dashboard (or drag one and then clone it).
3. Edit one header to say **Local** and the other to say **Remote**.
4. Drag two **Host health** tiles to the dashboard (or drag one and then clone it).  
   Position one under the **Local** header and the other under the **Remote** header.
5. Drag two **Network status** tiles to the dashboard (or drag one and then clone it).  
   Position one under the **Local** header and the other under the **Remote** header.

   At this point, all of the tiles query the local environment, so you have two identical **Host health** tiles and two identical **Network status** tiles.

   ![Same tiles, same environments](https://dt-cdn.net/images/same-tiles-same-environments-595-51063546a9.png)
6. Under the **Remote** header, edit the **Host health** and **Network status** tiles so that both of them query the remote environment (`Boston` in this example).

   ![Example: select remote environment for tile](https://dt-cdn.net/images/select-tile-environment-example-317-72348cc81f.png)
7. Select **Done** to display the dashboard.

   * The tiles under **Local** still display local host and network information.
   * The tiles under **Remote** now query the remote environment:

     + The remote tiles display the host health and network status for the remote environment, not the default local environment.
     + The remote tiles each display a filter icon. Hover over the icon to see the environment name.

   ![Same tiles, different environments](https://dt-cdn.net/images/same-tiles-different-environments-595-d747473897.png)

You can of course add other tile types and point to additional remote environments.

## Troubleshooting

[`Verification failed, please check your settings: Constraints violated.` message displayed when adding a remote environmentï»¿](https://dt-url.net/t903mr6)

## Related topics

* [Dashboards Classic API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")
* [Remote environments API](/docs/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.")
* [What is a monitoring environment?](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")