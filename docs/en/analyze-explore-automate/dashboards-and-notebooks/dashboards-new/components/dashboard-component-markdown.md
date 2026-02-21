---
title: Add Markdown to dashboard
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-markdown
scraped: 2026-02-21T21:08:18.966226
---

# Add Markdown to dashboard

# Add Markdown to dashboard

* Latest Dynatrace
* How-to guide
* 10-min read
* Published Jul 08, 2022

A Markdown tile can be anything from a minor note about something on the dashboard to a whole page of formatted information with links and pictures.

## Add a Markdown tile

To add a markdown tile to a dashboard

1. In the upper-right of the dashboard, open the  **Add** menu and select  **Add markdown**.

   Keyboard shortcut: **Shift**+**M**

   ![Dashboards: Add tile button (Plus)](https://dt-cdn.net/images/updated-dashboards-add-tile-button-481-c21ba8f200.png)

   An **Options** side panel opens on the right.
2. In the **Options** side panel, enter your text.

   * Use Markdown to format your text and add links and images.
   * The tile is updated as you edit.
   * While you're editing text, press Ctrl+Space to see options.
3. Close the **Options** side panel when you're done.

## Syntax

Use Markdown to format your annotations.

While you're typing in the edit box, your Markdown is rendered in the tile.

Press Ctrl+Space on an empty line to pop up a selectable list of available Markdown elements.

![How to edit a Markdown tile](https://dt-cdn.net/images/markdown-editing-1105-1fc4ba5612.png)

### Italics

Wrap text in single asterisks (`*like this*`) to get italics *like this*.

### Bold

Wrap text in double asterisks (`**like this**`) to get bold text **like this**.

### Strikethrough

Wrap text in double tildes (~~like this~~) to get strikethrough (crossed out) text ~~like this~~.

### Blockquote

Start a line with `>` to get blockquotes, where everything before you press Enter is quoted.

### Code

* Wrap text in backticks (`like this`) to get bold text `like this`.
* Wrap text in triple backticks (```like this```) to show a code block (multiple lines of `code text`).

### Headings

To add a heading, start the line with the `#` character like this: `# This is your heading text`.

### Horizontal line

To visually separate sections of your annotation, add a horizontal line with three dashes (`---`):

### Lists

Each line of an unordered (bulleted) list starts with an asterisk (`*`):

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

If you use `1.` for each line number, the lines are renumbered automatically when you display the dashboard.

### Tables

To add a table, define the headers, the column formatting row, and then the rows of data you want to display

```
| Header 1 | Header2



--- | ---



content2 | content2
```

| Header 1 | Header2 |
| --- | --- |
| content2 | content2 |

### Special characters

You can use any printable characters, including emojis such as ð and ð and â¤ï¸.

### Links

You can link to other places in your dashboard and elsewhere.

A link in Markdown is a label and link of the form `[label](address)`, where:

* The `label` is freeform text to display on the link in your Markdown tile or section
* The `address` specifies what to open when someone selects the link, such as a website or a Dynatrace app

Link to

Syntax and examples

Website

```
[My label](https://www.example.com/)
```

Notebooks app

```
[My label](/ui/apps/dynatrace.notebooks/notebooks)
```

Specific notebook

**Syntax**:

```
[label](/ui/apps/dynatrace.notebooks/notebook/<notebookid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc)
```

To get the address

1. Display the target notebook.
2. Copy everything on the browser address line starting from `/ui/`.
3. Paste it into your Markdown as the address of a link.

Specific notebook section

**Syntax**:

```
[label](/ui/apps/dynatrace.notebooks/notebook/<notebookid>#<sectionid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.notebooks/notebook/274edae4-dfe8-41fb-aced-5020fb1270bc#cb69caf1-52ed-4e73-8a3e-120e8cd7e8f8)
```

To get the address

1. Display the target notebook.
2. Select the target section of the notebook.
3. Copy everything on the browser address line starting from `/ui/`.
4. Paste it into your Markdown as the address of a link.

Dashboards app

```
[My label](/ui/apps/dynatrace.dashboards/)
```

Specific dashboard

**Syntax**:

```
[label](/ui/apps/dynatrace.dashboards/<dashboardid>)
```

**Example**:

```
[My label](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2)
```

To get the address

1. Display the target dashboard.
2. Copy everything on the browser address line starting from `/ui/`.
3. Paste it into your Markdown as the address of a link.

Specific dashboard tile

**Syntax**:

```
[label](/ui/apps/dynatrace.dashboards/dashboard/<dashboardid>#tileIds=n)
```

**Example**:

```
[My label](/ui/apps/dynatrace.dashboards/dashboard/9f24c36e-ca5f-401c-8e00-5e4b05c46bd2#from=now%28%29-2h&to=now%28%29&tileIds=6)
```

To include a specific tile ID in the link

1. Display the target dashboard.
2. Select the target tile in the target dashboard.
3. Copy everything on the browser address line starting from `/ui/`.
4. Paste it into your Markdown as the address of a link.

### Images

To link to a picture, use this format:

`![alternate text](https://www.example.com/file-name.jpg)`

```
Here are some of the people who started [Dynatrace](https://www.dynatrace.com).



![Dynatrace founders](https://dt-cdn.net/images/original-dynatrace-team-1500-7334dbe9a8.jpg)
```

### Variables

To reference a [variable](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.") in an annotation, use the variable name prefixed by a `$` character. For example:

```
The status is $Status.
```

If the dashboard has a variable named `Status` and the current value of `Status` is `Good`, the above example would appear in your tile as "The status is Good." and it would be updated when the value of `Status` changes.

For details on variables, see [Add a variable to a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.").