---
title: Launchpads
source: https://www.dynatrace.com/docs/discover-dynatrace/get-started/dynatrace-ui/launchpads
scraped: 2026-02-26T21:27:23.143813
---

# Launchpads

# Launchpads

* Latest Dynatrace
* 4-min read
* Published Sep 18, 2024

The full landscape of Dynatrace use cases can seem overwhelming, with a somewhat complex learning curve towards understanding which elements people need in their daily observability journeys through Dynatrace.

To make things easier, use the **Launcher** app to create customizable "launchpads" (customizable start pages) designed to improve user experience and efficiency. When people start Dynatrace with a launchpad, they focus on what they want to see first and have quick navigation to the Dynatrace components most important to them.

* Coordinate a project with a bigger group of people
* Manage the rollout of Dynatrace across an entire organization

## Get started with launchpads

1. In the **Launcher** app, select  **Launchpad** to add a new launchpad.
2. Select **Customize**.
3. Select a component type and start customizing it. Components you can add to your launchpad include:

   * LinksâA collection of links to Dynatrace apps and documents, as well as general links to internal or external resources
   * MarkdownâA tile of Markdown-formatted text, including links to web pages and images
   * CardsâFor each card, add a brief explanation, an optional image, and a button to take you to your destination
4. After you have built your launchpad, select **Done**.

## Home launchpads

Home launchpads act as individual start pages, providing a customized experience when using Dynatrace, for focus and quick access to things people need most.

### Set home launchpads for user groups

To set home launchpads for user groups

1. Go to **Settings**.
2. Select **General**.
3. Select **Launcher** > **Home launchpad**.
4. Select  **Add home launchpad**.
5. Select a launchpad from the list.
6. Start typing to **Select a user group**, or select **Everyone** to change the start page for all users.
7. Select **Save**.

After setting a home launchpad, it will be indicated as the  **Home** launchpad and load as the start page when entering Dynatrace. Access to **Getting started with Dynatrace**, the default home launchpad, is retained on the launchpads overview page.

![Launchpads list](https://dt-cdn.net/images/launchpads-list-2208-f213920787.png)

### Set your personal home launchpad

To set your personal home launchpad

1. Select  **Browse all**.  
   The launchpads overview page opens.
2. Select the launchpad you want to switch to.
3. Select  >  **Set as Home**
4. The next time you sign in to Dynatrace, your home launchpad will be your new start page.

![Set as home](https://dt-cdn.net/images/set-as-home-2642-cfef19cf7b.png)

Setting a home launchpad for yourself will override any home launchpad set by your admin. Access to home launchpads set by your admin will be retained under **Suggested** on the lauchpads overview page.

Home launchpad priority

1. Your personal home launchpad, set as  **Home**
2. Home launchpad set by your admin with highest rank
3. Other home launchpads set by your admin with lower ranks and other groups you're member of
4. **Getting started with Dynatrace**, the default home launchpad

In case a home launchpad fails to load (for example, due to failing permissions), the next in line will be opened.

## Common actions for launchpads

Select  in a launchpad or the overview page. From there, you can:

* **Rename** a launchpad.
* **Make a copy** to start building a new launchpad based on an existing one.
* **Delete** a launchpad.
* **Download** a launchpad so you can move it between environments. See [Download and upload a launchpad](#move).
* **Add to Dock**.

## Customize your launchpad

To customize a launchpad, open the launchpad and select **Customize**.

* Hover over a component you want to customize and select  >  **Edit**. You can also simply select a component when in **Customize** mode.
* Hover over a component and select  to select and drag the component to a new position.

![Move launchpad component](https://dt-cdn.net/images/drag-1888-0f03edd34a.png)

### Add a launchpad icon

Adding an icon will help your team know which launchpad they're on and will make it easier to pick the right one from a list of launchpads.

![Upload launchpad icon](https://dt-cdn.net/images/launchpads-icon-upload-2442-75e4e4057e.png)

To add a launchpad icon

1. Select **Customize**
2. Select **Upload icon**
3. Select the image to use as this launchpad's icon.
4. Select **Save**

File size limits

* 1 MB for JPG, PNG, and WEBP images
* 10 KB for SVG images

## Download and upload a launchpad

To move a launchpad between environments

1. Select  >  **Download** to download the launchpad.
2. Go to the destination environment, select  **Launchpads** >  **Upload**, and upload the JSON file you downloaded in the previous step.

## Share launchpads

If you own a launchpad, you can share it with other users in your Dynatrace environment.

![Share launchpad](https://dt-cdn.net/images/share-2226-f40006e092.png)

For details on sharing Dynatrace documents (including launchpads), see [Share documents](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Share Dynatrace documents (dashboards, notebooks, and launchpads) with other Dynatrace users in your company.").

## API for launchpads

The **Launcher** app uses the [document serviceï»¿](https://dt-url.net/x403ua9) API to persist launchpads as documents.

Documents are content-agnostic, but have common metadata: a unique identifier, a name, and a description.

To distinguish different types of documents, and to make them visible to the respective apps, they need the correct `type` document attribute, in this case: `launchpad`. This attribute can also be used to query the API as shown in the following example.

```
https://environment/platform/document/v1/documents?filter=type='launchpad'
```

### Access full document service documentation

To see the full API documentation for the documents service

1. Go to the [Document serviceï»¿](https://dt-url.net/x403ua9) page of the [Dynatrace Developerï»¿](https://developer.dynatrace.com/) site.
2. In the **Related links** section, select the **Swagger API** link.

   You may need to sign in to your Dynatrace environment.