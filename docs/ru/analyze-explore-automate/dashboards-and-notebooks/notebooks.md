---
title: Notebooks
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks
scraped: 2026-02-26T21:15:40.598510
---

# Notebooks

# Notebooks

* Latest Dynatrace
* App
* 11-min read
* Updated on Jan 28, 2026

Prerequisites

### Permissions

The following table describes the required permissions.

app-engine:apps:run

Allows the user to run functions

app-engine:functions:run

Allows the user to run functions

document:documents:read

Allows the user to access notebooks

document:documents:write

Allows the user to create and update notebooks

document:documents:delete

Allows the user to delete notebooks

document:trash.documents:read

Allows the user to access deleted notebooks

document:trash.documents:delete

Allows the user to permanently delete notebooks

document:trash.documents:restore

Allows the user to restore deleted notebooks

document:environment-shares:read

Allows the user to access shared notebooks

document:direct-shares:read

Allows the user to access shared notebooks

Get started

Concepts

Use cases

With ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, you can create powerful, data-driven documents for custom analytics.

![Create powerful, data-driven documents.](https://dt-cdn.net/hub/01_General_xWZn5HR.png)![Explore, analyze, and directly interact with all your data.](https://dt-cdn.net/hub/02_Explore_and__interact_paewzqz.png)![Transform data into insights and uncover the story behind the numbers.](https://dt-cdn.net/hub/Tell_the_story.png)![Create and share stunning reports with persisted data.](https://dt-cdn.net/hub/04_Reporting_pV4hDMB.png)![Include Davis AI powered anomaly detection and forecasting.](https://dt-cdn.net/hub/05_AI_e1KD03b.png)

1 of 5Create powerful, data-driven documents.

## Notebook sections

A notebook can consist of multiple sections:

* [Explore](#explore): explore data such as your logs, metrics, and business events with our point-and-click interface.
* [Query](#query): displays data queried via Grail.
* [Code](#code): display data returned by code executed via Dynatrace functions.
* [Markdown](#markdown): static content edited in markdown.

### Explore sections

You can use the Explore options to explore your logs, metrics, business events, and more with our point-and-click interface. With zero knowledge of DQL or coding, you can create and start using notebook sections in minutes.

For more information, we have a whole [Explore data](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") page that shows you how to create Explore sections.

### Query section

The query sections allow you to easily query data from Grail and [visualize](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") the result in different ways.

![Query section](https://dt-cdn.net/images/notebooks-query-section-select-685-01cd3782b4.png)

The query section consists of a query input where you can write a DQL query. In the query input, use **Ctrl**+**Space** to trigger autocompletion at any time.

You can control the timeframe for the query via the timeframe dropdown list. If the timeframe is defined in the query itself, the dropdown list is disabled.

### Code section

The code section enables you to fetch data for your notebook using Dynatrace functions.

![Code section](https://dt-cdn.net/images/notebooks-code-section-select-694-e39f69d7ee.png)

### Markdown section

A markdown section can be anything from a minor note about something on the notebook to a whole page of formatted information with links and pictures.

Easy to edit:

![Markdown section: edit](https://dt-cdn.net/images/notebooks-markdown-section-edit-841-8301eddf20.png)

Attractive to look at:

![Markdown section: display](https://dt-cdn.net/images/notebooks-markdown-section-display-836-030ea62933.png)

To insert queries from your notebook with autocomplete, use **Ctrl**+**Space**.

#### Add links

You can link to other places in your notebook and elsewhere.

A link in Markdown is a label and link of the form `[label](address)`, where:

* The `label` is freeform text to display on the link in your Markdown tile or section
* The `address` specifies what to open when someone selects the link, such as a website or a Dynatrace app

## Use cases

Notebooks enables you to:

* Query, analyze, and visualize all your security, observability, and business data such as logs, metrics, and events powered byâ¯ Grailï»¿.
* Predict future trends with embedded Davis forecast capabilities.
* Create and collaborate on interactive, data-driven, and persistent documents.
* Fetch and incorporate external data by runningâ¯ Dynatrace Functionsï»¿.
* Interact with data; start drill-downs by sorting, filtering, and aggregation, or even trigger workflows.
* Annotate and add context with markdown.

These procedures describe the basics of using ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and get you started on the way to customizing and creating your own dashboards.

## Learning tips

A fast way to learn about notebooks is to open a ready-made notebook, make a copy, and start experimenting. You can undo and redo as needed.

### Open a ready-made notebook

To open a ready-made notebook

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the **Notebooks** panel, select  **Ready-made notebooks**.

   ![Select "Ready-made notebooks" ](https://dt-cdn.net/images/ready-made-notebooks-list1-476-aa735fed50.png)

   Alternatively, you can select  **All notebooks** and then change the tab at the top of the table from **All** to  **Ready-made**.

   ![Notebooks: Select "Ready-made" tab](https://dt-cdn.net/images/notebooks-select-ready-made-tab-466-f52a4b69b3.png)
3. Select a notebook to open it.

### Make a copy

To make a copy of the current notebook

1. At the top of the notebook, open the  menu next to the notebook name.
2. Select  **Duplicate** from the menu.

Alternatively, go to the **Last opened by you** section of the sidebar, hover over the notebook you want to copy, and select  >  **Duplicate**.

### Undo and redo

You can quickly undo or redo a notebook edit.

* The  (**Undo**) and  (**Redo**) controls are displayed in the upper-left of your notebook after you make a change.
* If you prefer, you can use keyboard shortcuts.

  |  | **Undo** | **Redo** |
  | --- | --- | --- |
  | Windows | **Ctrl+Z** | **Ctrl+Shift+Z** |
  | Mac | **Cmd+Z** | **Cmd+Shift+Z** |

The number of undos could be limited depending on your notebook's size.

## Use notebooks

### Use shortcuts

keyboard shortcuts help you work faster in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

To list keyboard shortcuts, in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, open the  menu and select  **Keyboard shortcuts** or use keyboard shortcut **Shift**+**?**

| Action | Keyboard shortcut |
| --- | --- |
| **General** |  |
| Close section | **Esc** |
| Add section | **Ctrl**/**Cmd**+**Shift**+**Enter** |
| Move section down | **Ctrl**/**Cmd**+**Alt**+ |
| Move section up | **Ctrl**/**Cmd**+**Alt**+ |
| Delete selected sections | **Del** |
| Duplicate selected sections | **Ctrl**/**Cmd**+**Shift**+**D** |
| Select all | **Ctrl**/**Cmd**+**A** |
| Undo | **Ctrl**/**Cmd**+**Z** |
| Redo | **Ctrl**/**Cmd**+**Shift**+**Z** |
| Open withâ¦ | **O** |
|  |  |
| **Data sections** |  |
| Add section | **Shift**+**D** |
| Run query | **Ctrl**/**Cmd**+**Enter** |
|  |  |
| **Code sections** |  |
| Add section | **Shift**+**C** |
| Execute code | **Ctrl**/**Cmd**+**Enter** |
|  |  |
| **Markdown sections** |  |
| Add section | **Shift**+**M** |
| Toggle between view and edit mode | **Ctrl**/**Cmd**+**Enter** |

### List notebooks



#### List all

To list all notebooks

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the **Notebooks** panel, select **Owned by anyone**.

#### List my notebooks

To list all notebooks you own

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the **Notebooks** panel, select **All**.
3. At the top of the **Notebooks** table, select **Owned by me**.

#### List notebooks shared with me

To list all notebooks that are shared with you

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the **Notebooks** panel, select **All**.
3. At the top of the **Notebooks** table, select **Shared with me**.

#### List ready-made notebooks

What's special about ready-made documents

* Created and automatically distributed by Dynatrace as examples and templates.
* Read-only: you can edit them for use during your session, and you can save a copy with your changes, but you can't save your changes to the original document.
* This icon  in a table of documents indicates that it's a ready-made document.

To list all ready-made notebooks

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the **Notebooks** panel, select  **Ready-made notebooks**.

   ![Select "Ready-made notebooks" ](https://dt-cdn.net/images/ready-made-notebooks-list1-476-aa735fed50.png)

   Alternatively, you can select  **All notebooks** and then change the tab at the top of the table from **All** to  **Ready-made**.

   ![Notebooks: Select "Ready-made" tab](https://dt-cdn.net/images/notebooks-select-ready-made-tab-466-f52a4b69b3.png)

For more about ready-made documents, see [Ready-made documents](/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents "Use ready-made documents right out of the box.").

### Find a notebook

The easiest way to search for a notebook is through the [global search](/docs/discover-dynatrace/get-started/dynatrace-ui#search "Navigate the latest Dynatrace").

The search can be triggered from any context using the **Ctrl**/**Cmd**+**K** keyboard shortcut. Notebooks with matching titles will show up in the results.

Alternatively, select  **All notebooks** in the sidebar. Enter a search term to list only matching notebooks.

### Create a notebook

To create a new notebook

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. In the app header, select  **Notebook**.

Now you need to create one or more sections within your notebook. For details, see [Create a section](#section-create).

### Duplicate a notebook

To make a copy of the current notebook

1. At the top of the notebook, open the  menu next to the notebook name.
2. Select  **Duplicate** from the menu.

Alternatively, go to the **Last opened by you** section of the sidebar, hover over the notebook you want to copy, and select  >  **Duplicate**.

### Pin notebook to Dock

To add a notebook to the Dock for easy access

1. Display the notebook.
2. Open the  menu next to the notebook name (in the upper-left corner of the notebook).
3. Select  **Add to dock**.

   If you change the name of the notebook, it's automatically updated on the Dock.

To remove a notebook from the Dock

1. Hover over the notebook name in the Dock.
2. Select  **Unpin from dock**.

### Delete a notebook

To delete a notebook

1. At the top of the notebook, open the  menu next to the notebook name.
2. Select  **Delete** from the menu.

Alternatively, you can also trigger the same action in the **Last opened by you** section of the sidebar. Select  >  **Delete**.

To delete multiple notebooks, select  **All notebooks** and use the  buttons in the table.

## Create a section

Every notebook needs one or more sections.

### Create a Prompt section

To create a notebook section using [Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.") to translate your natural language questions into DQL queries

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open or create a notebook you can edit.
2. Open the  **Add** menu and select  **Prompt**. A new Generative AI notebook section is created with an empty prompt box.
3. In the prompt box, type a prompt. Try `average cpu usage percentage by host` or see the examples displayed in the web UI for inspiration.
4. Optional If your prompt doesn't specify the timeframe, you can still specify it in your section header. The default is **Last 2 hours**.
5. Select **Run**. Generative AI creates and runs the query for you.

   Optional If you want to see the generated query before running it, open the  menu next to the **Run** button and select **Generate DQL only**.
6. Review the results.

   * You can review the query by expanding **DQL**  on the right.
   * Optional You can't edit the query directly in Dynatrace Intelligence generative AI, but you have two options for reusing it:

     + Copy the query and paste it elsewhere manually.
     + Open the  menu in the section header and select **Create DQL section** to create a DQL section from this query.
   * You can edit your original prompt, regenerate the query, and run it to update the results.  
     If you select **Rerun sections**, the Notebooks app will first check if any prompts have been edited.

     + If a prompt has been edited, the DQL will first be regenerated and then run.
     + If no prompts have been edited, the existing generated DQL will simply be run.
7. Optional Select the  **Options** in the section header to change the visualization (refer to the [visualization-specific documentation](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") for more information).

   Automatically select visualization

   To have Dynatrace automatically select a visualization for your query, turn on **Auto select** in the upper-right corner of your visualization settings pane.

   * If you manually select a different visualization, the **Auto select** switch will turn off.
   * To have Dynatrace once again automatically select a visualization, turn **Auto select** back on.

### Create an Explore section

The Explore sections offer the easiest way to get started.

* To learn more about Explore sections first, see [Explore data](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.").
* To dive right in, just display a notebook, open the  **Add** menu, and select an Explore option such as **Logs**, **Metrics**, **Events**, **Problems**, or **Business Events**.

### Create a Grail query section

The fastest and easiest way to explore your data is with an [Explore](#section-create-explore-data) section. In a few seconds, you can find and analyze your logs, metrics, or business events. No DQL required!

Deprecated: `dt.entity.*` fields

If you see the following message:

`The dt.entity.* fields are deprecated. Please use dt.smartscape.* fields instead.`

we recommend that you use an equivalent `dt.smartscape.*` field instead.

The deprecated `dt.entity.*` fields will eventually be removed.

To add data to a notebook

1. Open the  **Add** menu and select  **DQL**.

   Keyboard shortcut: **Shift**+**D**

   An empty section is added to the notebook and an **Options** side panel opens on the right.
2. In the section edit box, use the [Dynatrace Query Language (DQL)ï»¿](https://dt-url.net/bv03yk8) to define your query.
3. Select  **Run** to execute the DQL query.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Enter**

   ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** automatically visualizes the result.
4. Select **Add title** to add the title header to this notebook section.
5. Select a [visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") to display your results in your preferred format. Adjust visualization settings as needed.

   Automatically select visualization

   To have Dynatrace automatically select a visualization for your query, turn on **Auto select** in the upper-right corner of your visualization settings pane.

   * If you manually select a different visualization, the **Auto select** switch will turn off.
   * To have Dynatrace once again automatically select a visualization, turn **Auto select** back on.

### Create a code section



To add code fetching data for your notebook using Dynatrace functions

1. Open the  **Add** menu and select  **Code**.

   Keyboard shortcut: **Shift**+**C**

   ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** creates a code section with sample JavaScript code in the edit box.
2. Select  **Run** to execute the code.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Enter**

   ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** runs the sample code and displays the result: "Hello, world!"
3. Edit the section as needed.

   * To change the code, edit it directly in the edit box above the result. For details, see [App functionsï»¿](https://dt-url.net/functions-help).
   * To configure the visualization, select  **Options**. For details, see [Edit visualizations for Notebooks and Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.").

To try an example code section

1. In your notebook, open the  **Add** menu, scroll down the menu to the **Library** section, and select any of the  code section examples.

   This adds the selected example code section to your notebook.
2. Read the comments in the code example for essential details.

### Create a Markdown section

To add a Markdown-formatted annotation to a notebook

1. Open the  **Add** menu and select  **Markdown**.

   Keyboard shortcut: **Shift**+**M**
2. Enter your text. Use Markdown to format your text and add links and images.

   * While you're typing in the edit box, your Markdown is rendered in the section.
   * Press Ctrl+Space on an empty line to pop up a selectable list of available Markdown elements.

   You can use the toolbar to insert common elements like a heading, bold text, or a link:

   ![Example: Notebooks: edit Markdown section](https://dt-cdn.net/images/notebooks-markdown-edit-969-a08f9afae1.png)

* **Italics**: wrap text in single asterisks (`*like this*`) to get italics *like this*.
* **Bold**: wrap text in double asterisks (`**like this**`) to get bold text **like this**.
* **Strikethrough**: wrap text in double tildes (~~like this~~) to get strikethrough (crossed out) text ~~like this~~.
* **Blockquote**: start a line with `>` to get blockquotes, where everything before you press Enter is quoted.
* **Code**:

  + Wrap text in backticks (`like this`) to get code text `like this`.
  + Wrap text in triple backticks (```like this```) to show a code block (multiple lines of `code text`).
* **Headings**: start a line with one or more `#` characters to create headings.
* **Horizontal line**: to visually separate sections of your annotation, add a horizontal line with three dashes (`---`).
* **Lists**: each line of an unordered (bulleted) list starts with an asterisk (`*`):

  ```
  * Line 1



  * Line 2
  ```

  Alternatively, you can use a dash (`-`):

  ```
  - Line 1



  - Line 2
  ```

  An ordered (numbered) list starts with a number and a period (`1.`) followed by a space and then your text:

  ```
  1. The first line of my procedure.



  2. The second line of my procedure.



  3. The third line of my procedure.
  ```

  If you use `1.` for each line number, the lines are renumbered automatically when you display the notebook.
* **Tables**: to add a table, define the headers, the column formatting row, and then the rows of data you want to display

  ```
  | Header 1 | Header2



  --- | ---



  content2 | content2
  ```

  | Header 1 | Header2 |
  | --- | --- |
  | content2 | content2 |
* **Special characters**: you can use any printable characters, including emojis such as ð and ð and â¤ï¸.
* **Links**: You can link to other places in your notebook and elsewhere.

  A link in Markdown is a label and link of the form `[label](address)`, where:

  + The `label` is freeform text to display on the link in your Markdown tile or section
  + The `address` specifies what to open when someone selects the link, such as a website or a Dynatrace app
* **Images**: to link to a picture, use this format:

  `![alternate text](https://www.example.com/file-name.jpg)`

  ```
  Here are some of the people who started [Dynatrace](https://www.dynatrace.com).



  ![Dynatrace founders](https://dt-cdn.net/images/original-dynatrace-team-1500-7334dbe9a8.jpg)
  ```

### Start with a snippet

Several data and code snippets are available out of the box. Use our predefined DQL or code snippets to quickly start your data analytics journey.

To get started based on a snippet

1. In a notebook, select  **Add**.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Shift**+**Enter**
2. Scroll down to the **Start with a snippet** section and choose one of the snippets. For example, select the  **Fetch logs** snippet, which is displayed in a preview panel.
3. When you select a snippet, a notebook section is created for the snippet.
4. Edit the query or code (depending on the snippet type you selected) and the visualization settings as needed.
5. Select  **Run** to see results.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Enter**

The list of available snippets is long and growing. Create a new notebook and try them out.

When you find something interesting:

* Inspect it to see how it works
* See if you can tweak and adapt it to your own purposes

## Edit a section

### Undo and redo

You can quickly undo or redo a notebook edit.

* The  (**Undo**) and  (**Redo**) controls are displayed in the upper-left of your notebook after you make a change.
* If you prefer, you can use keyboard shortcuts.

  |  | **Undo** | **Redo** |
  | --- | --- | --- |
  | Windows | **Ctrl+Z** | **Ctrl+Shift+Z** |
  | Mac | **Cmd+Z** | **Cmd+Shift+Z** |

The number of undos could be limited depending on your notebook's size.

### Section edit controls

To see the edit commands for a section, select the section. If you have edit permission, the edit commands are displayed.

* is where you click to drag the selected section to a different position.
* **Run** starts your query. Keyboard shortcut: **Ctrl**/**Cmd**+**Enter**
* sets the segment.
* displays timeframe options.
* and  decrement and increment the timeframe.
* and  hide and show the input.
* opens the options panel, where you can select and adjust the [visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.").
* opens a menu of further options:

  + **Copy section** copies the selected section to the clipboard.
  + **Duplicate section** creates a copy of the selected section.
  + **Create DQL section** creates a DQL section from the selected [Explore](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.") section.
  + **Move section up** and  **Move section down** move the section up or down one row.  
    Alternative: use  to drag the section into a new position.
  + **Clear result** clears the result. Select  **Run** (or Ctrl+Enter) again to get new results.
  + **Delete section** removes the section from the notebook.
  + **Explain query** displays an AI-generated summary of the query.
  + **Dynatrace Query Language** opens DQL documentation.
  + **Copy query link** copies a link to the clipboard. If you open the link in a browser, the query will be opened in a new or existing notebook.
  + **Download result** downloads (exports) the result of the current notebook section.
  + ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Add to dashboard** opens the selected section in a dashboard.
  + **Open with** opens the section in another document. For details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/drilldowns-and-navigation "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

You can select multiple sections and then apply the same command to all of them at once. For details, see [Manage multiple sections](#edit-manage-multiple-sections).

### Section edit panels

The available edit options will vary depending on the type of section you're editing.

* Prompt section: type a plain-text prompt in the edit box and select  **Run** (or Ctrl+Enter) to get an answer.

  ![Editing the generative AI prompt section in the Notebooks app.](https://dt-cdn.net/images/notebooks-dynatrace-intelligence-prompt-edit-2262-06425469c6.png)
* Explore data section: These sections are a great shortcut to results. To learn more about Explore sections, see [Explore data](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data "Explore your data with our point-and-click interface.").
* DQL section

  ![Example: Notebooks: edit DQL section](https://dt-cdn.net/images/notebooks-dql-edit-1156-a4d71cda36.png)
* Code section

  ![Example: Notebooks: edit Code section](https://dt-cdn.net/images/notebooks-code-edit-1151-83a2b34c65.png)
* Markdown section

  ![Example: Notebooks: edit Markdown section](https://dt-cdn.net/images/notebooks-markdown-edit-969-a08f9afae1.png)

### Select section segments



To filter data for a section, you can specify [segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.") for a section.

1. In the action bar for that section, select  and, in **Filter by segments**, select a segment.
2. If the segment requires an additional value selection, select it now.
3. To add another segment, select  **Segment**. Repeat this step for each segment you want to add for the selected notebook section.
4. Select **Apply** to apply the selection.

   * The segment selector  for that section now displays the name of the selected segment or, if you select more than one segment, the number of selected segments.
   * To change your segment selection, select  again, make your changes, and select **Apply**.
   * To manage segments in general (list, create, view, edit, delete), select  and then select the **Manage segments** link.

### Set section options

To open the **Options** panel (where you can select and customize a [visualization](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") for your section)

1. Select the section.
2. Select **Options**.

## Manage sections

### Undo and redo

You can quickly undo or redo a notebook edit.

* The  (**Undo**) and  (**Redo**) controls are displayed in the upper-left of your notebook after you make a change.
* If you prefer, you can use keyboard shortcuts.

  |  | **Undo** | **Redo** |
  | --- | --- | --- |
  | Windows | **Ctrl+Z** | **Ctrl+Shift+Z** |
  | Mac | **Cmd+Z** | **Cmd+Shift+Z** |

The number of undos could be limited depending on your notebook's size.

### Move a section

To move a section up or down within your notebook

1. Select the section.
2. Select and drag  the section to a new location within the notebook.

Alternate method:

1. Select the section.
2. Select  > **Move section up** or **Move section down**.

   Keyboard shortcut: **Ctrl**/**Cmd**+**Alt**+ or **Ctrl**/**Cmd**+**Alt**+

### Copy and paste sections

You can copy and paste sections to the same notebook or another notebook.

An easy way to start a new notebook is to copy reusable sections from existing notebooks to a new notebook and then edit the copied sections in the new notebook.

To copy and paste one or more sections

1. Click one section to select it.
2. You can select multiple sections and then copy all of them at once.

   * **Shift**+**Click**âselects one or more consecutive sections
   * **Ctrl/Cmd**+**Click**âselects one or more nonconsecutive sections
   * **Ctrl/Cmd**+**A**âselects all sections

   Each selected section is highlighted
3. Press **Ctrl/Cmd**+**C** to copy the selected sections to your clipboard.

   Menu alternative: on the section command bar, select  **Copy section**.
4. Press **Ctrl/Cmd**+**V** to paste the copied sections.

   * Pasting the copied sections to the current notebook is the equivalent of the  >  **Duplicate section** menu command.
   * To paste the copied sections to a different notebook, switch to the other notebook (or select  **Notebook** to create an empty notebook), and then paste (**Ctrl/Cmd**+**V**) the copied sections there.
5. To move the copied sections to new positions, select and drag  them as needed.

   You can select and drag one or more section at a time.

   * **Shift**+**Click**âselects one or more consecutive sections
   * **Ctrl/Cmd**+**Click**âselects one or more nonconsecutive sections
   * The  control is displayed on the section you selected last

### Delete a section

To remove a section from your notebook

1. Select the section.
2. Select  >  **Delete section**.

   Keyboard shortcut: **Del**

### Copy a link to a section

To copy a link to a section

1. Select the section.
2. Select  > **Copy [section type] link**.

### Download results of a section

To download (export) the result of the current dashboard tile or notebook section to a local file

1. Select the tile or section.
2. On the command bar, open the  menu and select  **Download result** > [format].

   The format options available depend on the visualization.

   * **CSV**: The result is downloaded to a local comma-separated values (\*.csv) file. This option includes table formatting such as visible columns and unit formatting.
   * **CSV (raw)**: The result is downloaded to a local comma-separated values (\*.csv) file. This option includes the complete unformatted data.
   * **JSON**: The result is downloaded to a local JSON (\*.json) file.

   Some visualizations offer no option to download the result.

#### Possible issue with importing CSV into Excel

When you export results to a CSV fileâwhether **CSV** or **CSV (raw)**âwith line breaks in any result column/field, and then open the file with Microsoft Excel or try to convert the file into a table using Excel option **Data** > **Text to Columns**, you may encounter an issue in which the line breaks are incorrectly rendered in Excel. This is caused by an Excel limitation.

To avoid this issue, use Excel option **Data** > **From Text/CSV**.

### Edit read-only notebook

When you open a document (dashboard or notebook) for which you don't have write permission, you can still edit the document during your session. After you're finished, you have two options:

* Save your changes to a new document
* Discard your changes

Example:

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, list the ready-made notebooks, and select the **Getting started** notebook.

   It says  **Ready-made** in the upper-left corner, next to the document name.
2. Select the Line chart section and then select  **Options**.
3. Change the visualization from Line to Area.

   Now you are offered two buttons: **Save as new** and **Discard changes**.
4. Use the updated notebook as needed. You have full edit access for this session.
5. When you're finished, select what to do with your changes:

   * **Save as new**âsaves your changes in a new copy of the edited notebook.
   * **Discard changes**âdiscards your changes and returns you to the unedited read-only notebook.

### Manage multiple sections

You can select multiple sections and then apply the same command to all of them at once.

* **Shift**+**Click**âselects one or more consecutive sections
* **Ctrl/Cmd**+**Click**âselects one or more nonconsecutive sections
* **Ctrl/Cmd**+**A**âselects all sections

  The **x sections** menu in the upper-right corner of the notebook offers commands that apply to all sections:

  + **Select all** selects all sections in the notebook.
  + **Run all** runs all sections in the notebook.

When you select multiple sections, the available commands include:

* is where you click to drag the selected sections to a different position.
* **Run x** runs all selected sections.
* set segments for all selected sections.
* sets the timeframe for all selected sections.
* and  hide and show the input for all selected sections.
* opens a menu of further options:

  + **Duplicate sections** creates a copy of the selected sections.
  + **Clear results** clears the results of the selected sections. Select  **Run** again to get new results.
  + **Delete sections** removes the selected sections from the notebook.
  + ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Add to dashboard** opens the selected sections in a dashboard.
  + **Open with** opens the selected sections in another document. For details, see [Drilldowns and navigation](/docs/analyze-explore-automate/dashboards-and-notebooks/drilldowns-and-navigation "Drill down from Dashboards and Notebooks using links based on intents or URLs.").

## Run a section

### Run code

To run a code section

1. Select the section.
2. Select **Run**.

After you run a code section, you can clear the code results

1. Select the section.
2. Select  > **Clear result**.

### Show/hide code

To display the code in a code section

1. Select the section.
2. Select **Show code**.

   The code is displayed in a panel above the section.

To hide the code panel again, select **Hide code**.

### Run query

To run a query section

1. Select the section.
2. Select **Run**.

After you run a query section, you can clear the query results

1. Select the section.
2. Select  > **Clear result**.

### Show/hide query

To display the query in a query section

1. Select the section.
2. Select **Show query**.

   The query is displayed in a panel above the section.

To hide the query panel again, select **Hide query**.

## Share with others

### Share a notebook

If you own a dashboard or notebook, you can share it.

There are three ways to share a document with other Dynatrace users in your company:

* **Access for all (view-only)**: Give view-only access to everyone in your Dynatrace environment.
* **Share access**: Create and maintain a list of users and user groups with access the document.
* **Share links**: Create links (URLs) pointing to your document and distribute the links through the channels of your choice (email, for example).

These methods are not mutually exclusive. For example, you can maintain a focused list of users for ongoing access to the document (maybe everyone in a certain group edits the document regularly) and you can create and distribute view-only links for a wider audience as needed.

In any case, you control whether people can edit the document or only view it.

For details on sharing documents, see [Share documents](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Share Dynatrace documents (dashboards, notebooks, and launchpads) with other Dynatrace users in your company.").

You can also export a notebook as a JSON file and send the JSON to others, and then they can import the JSON.

### Export a notebook



To export a notebook

1. At the top of the notebook, open the  menu next to the notebook name.
2. Select  **Download** from the menu.

Alternatively, you can also trigger the same action in the **Last opened by you** section of the sidebar. Select  >  **Export as JSON**.

### Import a notebook

To import a notebook from a JSON file

1. Select  **All notebooks** in the document sidebar.
2. In the upper-left corner of the page, select  **Upload**.
   A file browser window opens.
3. Find and open the notebook JSON definition file.

The definition is imported as a new notebook and listed on the **Notebooks** page with **Last modified** set to the import date and time.

### Change notebook owner

When you create a document (dashboard or notebook), you are the owner. To give ownership of the document to another Dynatrace user

1. Open the  document menu and select  **Change owner**.
2. Find and select a new owner, and then select **Change owner**.

   When you change the document owner, you immediately lose access to the document.

   * Be sure you are ready to transfer ownership before you select this command.
   * You can regain access to the document only if the new owner gives you permission.
3. After the transfer is complete, the new owner will receive email about the document ownership transfer.

### Print or export to PDF

To print a notebook or export it to PDF

1. Open your notebook.
2. Optional Prepare your notebook sections for printing.

   For example:

   * Select **Run** to get the latest result before printing
   * Select **Hide input** to hide a section query and display only the result
   * Set [visualization options](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks."), such as hiding sensitive or irrelevant table columns that you don't want to print and distribute
3. From the notebook menu, select **Print view**.

   ![Open notebook menu from current notebook](https://dt-cdn.net/images/notebook-menu-from-notebook-411-119580207f.png)

   A printable view of the notebook is displayed on a **Print preview** page with print settings displayed at the top.
4. Select the page size (`A4` or `US Letter`) and orientation (`Portrait` or `Landscape`), and then select **Print**.

   The notebook is displayed in a print options window. Each notebook section prints to a new page.
5. Make additional print settings as needed, and then select **Save** or **Print** (depending on the print destination) to finish.

#### Known print limitations

* When printing in `Landscape` mode, a table may overlap the next section.
* When Dynatrace is in dark mode, printing a notebook uses dark mode color schemes. To avoid this, you can temporarily switch Dynatrace to light mode: from the Dynatrace user menu (in the lower-left corner of Dynatrace), select **Appearance** > **Light**.

## Analyze data

### Analyze data with AI



To analyze data using Dynatrace Intelligence Data Analyzers

1. Explore a timeseries.

   Example

   In your document (dashboard or notebook)

   1. Select  to add a new section or tile, and then select **Metrics** to explore metrics.

      ![Example: select Add > Metrics](https://dt-cdn.net/images/example-select-explore-metrics-637-025cadac69.png)
   2. In **Select metric**, select **Infrastructure** > **CPU** > **CPU usage %**.

      ![Example: select metric "CPU usage %"](https://dt-cdn.net/images/example-select-metric-cpu-usage-percent-771-a672aa20e2.png)
   3. Set **Split by** to `host.name`.

      ![Example: set "Split by" to host.name](https://dt-cdn.net/images/example-select-host-name-743-5bd89ea6a3.png)
   4. Set **Limit** to the maximum number of series to analyze. Dynatrace Intelligence Data Analyzer currently supports analysis up to 1000 series.

   You should get something like this:

   ![Example: complete query](https://dt-cdn.net/images/example-complete-query-737-dfa24f730d.png)
2. Run the query.
3. In the options panel on the right, scroll down and expand  **Davis AI**.

   Show me

   ![An example of selecting the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-select-analyze-and-alert-settings-746-7155ef9415.png)

   ![The initial panel for the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-details-746-8d503491c8.png)
4. On the **Davis AI** panel, set **Analyzers** to the analyzer you want to use, and then configure the analyzer.

   * For an overview of anomaly detection, see [Anomaly detection](/docs/dynatrace-intelligence/anomaly-detection "How Dynatrace detects anomalies in your environment.")
   * For details on anomaly detection settings, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.")

   * For details on forecast analyzer settings, [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.")

   Anomaly Detection: Auto adaptive threshold anomaly detection

   * **Number of signal fluctuations**âhow many times the signal fluctuation is added to the baseline to produce the actual threshold for alerting.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above, below, or outside (above or below) the normal range.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Anomaly Detection: Seasonal baseline anomaly detection

   * **Tolerance**âthe higher the tolerance, the broader the confidence band, leading to fewer triggered events.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above, below, or outside (above or below) the normal range.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Anomaly Detection: Static threshold anomaly detection

   * **Threshold**âa hard limit that a metric should not violate.
   * **Unit**âthe unit of the value.
   * **Alert condition**âyour selection depends on whether you want to know when the metric is above or below the threshold value.
   * **Suggest threshold**âDavis AI can help you to find the right threshold based on historical data.

   For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").

   Prediction: Forecast

   * **Data points to predict**âthe total steps the time series is forecasted. More steps generally results in less reliable forecasts and longer analyzer runtimes.
   * **Forecast offset**âan offset for the start of the forecast. For example, if the offset is set to `2`, the last two data points are ignored and a forecast for these points is returned as well.

   For details, see [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.").

   Advanced settings (for anomaly detection)

   You can use the default values or turn on **Show advanced properties** to fine-tune these settings.

   * **Alert on missing data**âalert if no data is detected within the sliding window.
   * **Violating samples**ânumber of samples in the sliding window that must violate to trigger an event.
   * **Sliding window**ânumber of samples that form the sliding window.
   * **Dealerting samples**ânumber of samples in the sliding window that must go back to normal to close the event.
5. By default, the analyzer is not enabled. To enable it, turn on the switch at the top of the edit panel (switch from **AI data analysis is not active** to **AI data analysis is active**).
6. To view the results, select the **Davis AI analysis** visualization and expand the **Davis AI analysis chart** section to review or change the visualization-specific settings:

   Show me

   ![Example of selecting "AI analysis" visualization and displaying visualization-specific settings in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-visualizations-757-4cf3f48b3c.png)

   The **Davis AI analysis** visualization has two sections: chart and visualization. You can use the **Visible sections** setting to display either or both of them.

   * **All**âshow a chart and a table. The chart reflects your table selections.
   * **Table**âshow only a table. You can sort columns that display a sort icon  in the header. Select the column header to toggle the sort order up  or down .
   * **Chart**âshow only a chart. Use the table to select entries you want to show on the chart.

#### Example: anomalous CPU usage percent

To detect when CPU usage percent exceeds 70 percent, in your document (dashboard or notebook)

1. Select  to add a new section or tile, and then select **Metrics** to explore metrics.

   Show me

   ![Example: select Add > Metrics](https://dt-cdn.net/images/example-select-explore-metrics-637-025cadac69.png)
2. In **Select metric**, select **Infrastructure** > **CPU** > **CPU usage %**.

   Show me

   ![Example: select metric "CPU usage %"](https://dt-cdn.net/images/example-select-metric-cpu-usage-percent-771-a672aa20e2.png)
3. Set **Split by** to `host.name`.

   Show me

   ![Example: set "Split by" to host.name](https://dt-cdn.net/images/example-select-host-name-743-5bd89ea6a3.png)
4. Set **Limit** to the maximum number of series to analyze. Davis analyzer currently supports analysis up to 1000 series.

   Show me

   ![Example: complete query](https://dt-cdn.net/images/example-complete-query-737-dfa24f730d.png)
5. Select **Run**.
6. In the edit panel, expand  **Davis AI**.

   Show me

   ![An example of selecting the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-select-analyze-and-alert-settings-746-7155ef9415.png)

   ![The initial panel for the Analyze and alert settings in the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-details-746-8d503491c8.png)
7. In the **Analyzers** list, select **Static threshold anomaly detection**.

   Show me

   ![Selecting the "Static threshold anomaly detection" analyzer in the Analyze and alert settings of the Dashboards app.](https://dt-cdn.net/images/dashboards-analyze-and-alert-select-static-threshold-anomaly-detection-752-45026264f0.png)
8. Set **Threshold** to `70` (enter a value) and **Alert condition** to **Alert if metric is above** (default).

   Show me

   ![Configuring settings for the "Static threshold anomaly detection" analyzer in the Dashboards app.](https://dt-cdn.net/images/dashboards-static-threshold-anomaly-detection-settings-748-4d20c8220e.png)
9. Activate the analyzer: at the top of the edit panel, switch from **AI data analysis is not active** to **AI data analysis is active**.
10. To view the results, select the **Davis AI analysis** visualization. Expand the **Davis AI analysis chart** section to see visualization-specifc settings.

    Show me

    ![Example of selecting "AI analysis" visualization and displaying visualization-specific settings in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-visualizations-757-4cf3f48b3c.png)
11. In the **Davis AI analysis chart** section, set **Visible sections** to **All**.
12. Review the results.

    In this example, we selected the hosts that exceeded the threshold.

    * The chart shows a line for the selected metric (`CPU usage %`) for each selected host.
    * A red bar across the top of the visualization indicates where the threshold for that metric was exceeded.
    * The table under the chart has those hosts selected.

    ![Example analyzer results with "AI analysis" visualization in the Notebooks app.](https://dt-cdn.net/images/notebooks-ai-analysis-chart-1920-5ac0e1f854.png)

### Start forecast analysis



From your notebook, you can trigger a series forecast analysis powered by Dynatrace Intelligence.

In this example, we issue the following query:

`timeseries avg(dt.host.cpu.usage), by:{ dt.entity.host }`

and then run a forecast for a time series selected in the results.

1. In a notebook, select  >  **DQL**.
2. Enter a query such as `timeseries avg(dt.host.cpu.usage), by:{ dt.entity.host }` to chart time series.
3. Select **Run query**.
4. Hover over the required time series in the sidebar and select  > **Filter and forecast**.

   ![Filter and forecast: select](https://dt-cdn.net/images/filter-and-forecase-select2-1183-5f9b6cae74.png)
5. The query is automatically updated to filter by the selected time series and the chart is extended to show the projection for the selected series.

   ![Filter and forecast: results](https://dt-cdn.net/images/filter-and-forecase-results-1117-910a185d8a.png)

For details, see [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.").

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Create powerful, data-driven documents for custom analytics and collaboration.](https://www.dynatrace.com/hub/detail/notebooks/?internal_source=doc&internal_medium=link&internal_campaign=cross)