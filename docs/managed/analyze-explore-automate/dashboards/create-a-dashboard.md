---
title: Create a dashboard
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards/create-a-dashboard
---

# Create a dashboard

# Create a dashboard

* How-to guide
* 8-min read
* Updated on Oct 05, 2026

To build a dashboard, follow the steps below.

To edit an existing dashboard, go to **Dashboards**, select the name of the dashboard, select **Edit** in the upper-right corner, and continue with [adding tiles](/managed/analyze-explore-automate/dashboards/create-a-dashboard#add-tiles "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF."); if you don't see an **Edit** option, you don't have permission to edit that dashboard. To delete a whole dashboard, see [Organize dashboards](/managed/analyze-explore-automate/dashboards/organize-dashboards "Filter the Dashboards table, mark favorites, add tags, hide dashboards you don't need, and find little-used dashboards to clean up by popularity.").

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create the dashboard**](/managed/analyze-explore-automate/dashboards/create-a-dashboard#create "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add tiles**](/managed/analyze-explore-automate/dashboards/create-a-dashboard#add-tiles "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure tiles**](/managed/analyze-explore-automate/dashboards/create-a-dashboard#configure-tiles "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Set dashboard defaults**](/managed/analyze-explore-automate/dashboards/create-a-dashboard#settings "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.")[![Step 5 optional](https://dt-cdn.net/images/dotted-step-5-52040ae237.svg "Step 5 optional")

**Edit the dashboard JSON**](/managed/analyze-explore-automate/dashboards/create-a-dashboard#edit-offline "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.")[![Step 6 optional](https://dt-cdn.net/images/dotted-step-6-fbd29ea893.svg "Step 6 optional")

**Print to PDF**](/managed/analyze-explore-automate/dashboards/create-a-dashboard#print-pdf "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.")

## Step 1 Create the dashboard

Start with an empty dashboard, clone an existing one, or import a dashboard definition from a JSON file.

### Create an empty dashboard

1. Go to **Dashboards**.
2. Select **Create Dashboard**.
3. Enter a name for your dashboard and select **Create**.

The new dashboard opens in edit mode.

### Clone an existing dashboard

You can't customize or [share](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.") dashboards for which you have only viewing permission, but you can clone them and then modify and share the clones. You also can't edit preset dashboards directly. Clone one to start from a more elaborate example. The clone gets `-cloned` appended to the dashboard name.

1. Go to **Dashboards**.
2. Clone the dashboard in one of these ways:

   * In the table of dashboards, select **More** (:more:) > **Clone** for the dashboard you want to copy.
   * Open the dashboard, select **More** (:more:) in the upper-right of the dashboard, and select **Clone**.

The copy opens in edit mode, and the original dashboard stays unchanged.

### Import a dashboard from a JSON file

Importing adds a new dashboard. To overwrite an existing dashboard instead, [edit its JSON offline](/managed/analyze-explore-automate/dashboards/create-a-dashboard#edit-offline "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.").

1. Optional: To start from an existing dashboard definition, export it. Go to **Dashboards** and, in the table of dashboards, select **More** (:more:) > **Export** for the dashboard you want to export. The dashboard definition is exported as a JSON file to your computer.
2. Optional: Edit the dashboard JSON in your preferred development environment. For JSON syntax details, see the [Dashboards API](/managed/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.") documentation.
3. Go to **Dashboards** and select **Import dashboard**.
4. Select the JSON file for the dashboard you want to import.

The imported dashboard opens in edit mode.

## Step 2 Add tiles

With the dashboard in edit mode, use the **Tiles** tab to change its content. For the full list of tile types, see [Available tiles](/managed/analyze-explore-automate/dashboards/available-tiles "Look up every tile you can add to a dashboard, with what each tile displays, where it drills down to, and the settings it offers."). You can also [pin tiles to the dashboard](/managed/analyze-explore-automate/dashboards/pin-tiles-to-a-dashboard "Pin a filtered Dynatrace page or a Data Explorer chart to a dashboard as a tile, then update, copy, or clone that tile to other dashboards.") from other Dynatrace pages.

1. Drag a tile from the **Tiles** pane to your dashboard.

   To see a description of a tile, drag it to your dashboard and then refer to the description on the tile configuration panel.
2. Optional: Add a header tile to put a bold label over other tiles.

   1. Drag a **Header** tile into position. For example, create a header above three related tiles.
   2. Select the edit control on the header tile and edit the header text.
   3. Size the header tile, and then select the check mark on the header tile.

   The header tile remains independent. You can move and resize it to label more than one tile with a single header.
3. Optional: Add a Markdown tile to describe what the dashboard does and how to use it. Each Markdown tile holds up to 1,000 characters.
4. Optional: Add an image tile that shows an uploaded image.

   1. Drag an **Image** tile into position.
   2. On the **Image** panel, select the **Upload an image** tab.
   3. Select **Upload image**, then browse for and select the image file you want to display in the tile.
   4. Size and position the tile as needed.

   Supported image file types are JPG/JPEG, GIF, PNG, WEBP, TIFF, BMP, and SVG. Unlike other tile types, an image tile isn't refreshed automatically. Refresh the dashboard manually to update its image tiles.
5. Optional: Add an image tile that points to an image URL.

   Before you can add an image by URL, you need to add the URL to the allowlist.

   1. Go to **Settings** and select **Dashboards** > **Allowed URL pattern rules**.
   2. Select **Add item**.
   3. Set **Rule**, which specifies how to process this allowlist entry.

      * **Starts with**: allow any image whose URL starts with the contents of **Pattern**.
      * **Exact**: allow the specific image whose URL matches the contents of **Pattern** exactly.
   4. Set **Pattern**.

      * To specify a URL start, enter enough of the URL to make sure any matching image URLs are suitable for your dashboards. For example, enter `https://example.com/images/` to allow `https://example.com/images/image-x.jpg` and `https://example.com/images/my-picture.svg`.
      * To specify an exact URL, enter the entire URL of the image. For example, enter `https://example.com/images/my-image-file-name.jpg` to allow only that image.
   5. Select **Save changes** to add the rule to the allowlist.
   6. On the dashboard in edit mode, drag an **Image** tile into position.
   7. On the **Image** panel, select the **Add image URL** tab.
   8. Enter the URL of the image file you want to display in the tile. The URL needs to match one of the rules on the allowlist.
   9. Size and position the tile as needed.

## Step 3 Configure tiles

With the dashboard in edit mode, select a tile to configure it. Changes to the tile configuration are reflected in the tile in real time.

1. Edit a tile's configuration. Hover over the tile, select the tile menu in the upper-right corner, and select **Edit tile**. Change the configuration as needed, and select **Done**.
2. Change the tile title. Select the tile, edit the title under **Title**, and select **Done**.
3. Override the dashboard timeframe for one tile. Select the tile, turn on **Custom timeframe**, select the timeframe you want to be the default for this tile, and select **Done**.

   A filter is displayed in the upper-right of the tile. Hover over it to see the setting.
4. Override the dashboard management zone for one tile. Select the tile, turn on **Custom management zone**, select the management zone you want to be the default for this tile, and select **Done**.

   A filter is displayed in the upper-right of the tile. Hover over it to see the setting.
5. Override the dashboard environment for one tile. Select the tile, select the environment for this tile under **Environment**, and select **Done**. For details on remote environments, see [Create multi-environment dashboards](/managed/analyze-explore-automate/dashboards/create-multi-environment-dashboards "Connect a remote Dynatrace environment with an access token and point dashboard tiles to it, so one dashboard shows data from several environments.").

   A filter is displayed in the upper-right of the tile. Hover over it to see the setting.
6. Clone tiles within the dashboard. Select the tile, and then select **Clone**. To clone several tiles, drag a selection rectangle around them, and then select **Clone x tiles**. Edit the cloned tiles as needed.
7. Move tiles. Select and drag the tile to a new location. To move several tiles, drag a selection rectangle around them, and then drag the selected tiles together to a new location.
8. Resize tiles. Select the tile, and then drag its lower-right corner until the tile has the size you want. Tiles snap to the dashboard grid.
9. Delete tiles. Select the unwanted tile, select **Delete**, and confirm. To delete several tiles, drag a selection rectangle around them, select **Delete x tiles**, and confirm.

## Step 4 Set dashboard defaults

On the **Edit dashboard** pane, select the **Settings** tab. For the full list of settings, see [Dashboard settings](/managed/analyze-explore-automate/dashboards/dashboard-settings "Look up every dashboard setting, from global sharing, preset, and image URL rules to the timeframe, report, and access options of a single dashboard.").

1. Set the default timeframe and default management zone for the dashboard. For how they interact with tile settings, see [How dashboards scope and refresh data](/managed/analyze-explore-automate/dashboards/how-dashboards-scope-and-refresh-data "Learn how timeframe, management zone, and dynamic filter settings decide which data dashboard tiles show, and how often each tile refreshes.").
2. Set the title size to small, medium, or large for all tiles on the dashboard.
3. Use the **Consistent entity colors** switch to show the same entity in the same color on every tile where it appears. The switch applies only to tiles created with Data Explorer.

   For example, with **Consistent entity colors** turned off, host A can have one color on one chart and another color on a second chart.

   ![Consistent entity colors turned off](https://dt-cdn.net/images/colors-consistent-off-384-7892d9ab41.png)

   Consistent entity colors turned off

   With it turned on, host A has the same color on both charts, and so does host B.

   ![Consistent entity colors turned on](https://dt-cdn.net/images/colors-consistent-on-383-585ee79076.png)

   Consistent entity colors turned on
4. Select **Done**.

   The dashboard is displayed as it appears to you and to people you [share](/managed/analyze-explore-automate/dashboards/share-a-dashboard "Share a dashboard with specific users, groups, anyone with the link, or anonymous viewers, and subscribe people to weekly or monthly email reports.") it with. People without edit permission don't see the **Edit** button.

## Step 5 optional Edit the dashboard JSON

To manage dashboard JSON at scale, use the [Dashboards API](/managed/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API."). For JSON syntax details, see the same documentation.

### Edit offline

Uploading the edited file overwrites the dashboard whose definition you downloaded. To add the definition as a new dashboard, [import it](/managed/analyze-explore-automate/dashboards/create-a-dashboard#import-dashboard "Create an empty, cloned, or imported dashboard, then add and configure tiles, set dashboard defaults, edit the dashboard JSON, and print it to PDF.") instead.

1. Display the dashboard and select **Edit**.
2. Switch to the **Settings** tab, select **Configure more**, and select **Dashboard JSON**.
3. On the **Dashboard JSON** page, select **Download**. A JSON file with the dashboard's name is downloaded to your local machine.
4. Edit the JSON in your preferred development environment.
5. On the **Dashboard JSON** page, select **Upload**, and browse for and upload the edited JSON file. The uploaded JSON is displayed on the **Dashboard JSON** page.
6. Select **Save changes** to replace the old JSON with your edited JSON.
7. Display the dashboard to verify your changes.

### Edit in place

1. Display the dashboard and select **Edit**.
2. Switch to the **Settings** tab, select **Configure more**, and select **Dashboard JSON**. The dashboard JSON is displayed in an edit window.
3. Edit the JSON directly in the edit window, or copy and paste between it and another editor.

   * The **You have unsaved changes** message in the lower left of the page reminds you of work in progress. Save before you navigate away from the page.
   * Syntax is checked each time you save, so you can work incrementally and use **Save changes** to verify that the JSON still parses.
4. When you're finished, display the dashboard to verify your changes.

## Step 6 optional Print to PDF

Printing a dashboard to a PDF file is supported in Chromium-based browsers (Chrome, Edge, and Opera) and Safari. Printing from Firefox isn't supported.

1. Go to **Dashboards** and select the name of the dashboard you want to print.
2. Select  > **Print PDF** in the upper-right corner of the dashboard.
3. Adjust the settings as needed.

   * **Destination**: select **Save as PDF**.
   * **Options**: select **Background graphics**.
   * **Pages**: if an empty page is generated, set **Pages** to `Custom`, and then enter `1` as the page range.
4. Select **Save**, and then select a name and destination for the PDF file.

The dashboard is saved as a PDF file in the destination you selected.

## Related topics

* [Dashboards API](/managed/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")