---
title: Share documents
source: https://www.dynatrace.com/docs/discover-dynatrace/get-started/dynatrace-ui/share
scraped: 2026-02-15T08:55:04.245956
---

# Share documents

# Share documents

* Latest Dynatrace
* 10-min read
* Updated on Jan 12, 2026

A Dynatrace document (dashboard, notebook, or launchpad) can be shared with other users in your Dynatrace environment.

## Who can share a document

When you create a document, you are the owner. You can share it and do everything else listed in the **Owner** column of the [Permissions](#document-share-permissions-table) table.

By default, only the document owner can share a document.

However, the owner of a dashboard, notebook, or launchpad can choose to allow everyone with **Can edit** permission for a document to also share the document.

1. Display the document (dashboard, notebook, or launchpad).
2. Select **Share**.
3. Select  (**Manage access**).
4. Turn on **Allow editors to share**.

Give it away

If you no longer want to own a document at all, you can [assign ownership to someone else](#change-owner) instead of just sharing it.

## Sharing options

If you have permission to share a document, you have the following sharing options. You can combine options.

* [Access for all (view-only)](#document-share-visible-all): let everyone in your Dynatrace environment view the document.

  + Easy to do: just turn on the **Visible to anyone in your environment (Read only)** switch.
  + Easy to undo: just turn it off again.
  + Best for publishing information that should be available to everyone.
  + No write access: this is view-only sharing.
  + No access granularity: when you turn this on, everyone in your Dynatrace environment can see your document.
* [Access per user or group](#document-share-access): specify Dynatrace users and groups that can view or edit the document.

  + Better for ongoing sharing, where you want certain people or groups to always have access to the document.
  + Better granularity over who has access to the documentâyou can add, change, and revoke access per user and user group.
  + You need to maintain a list of users and user groups that have access.
* [Access via shared link](#document-share-link): create links to your document that others can use to view or edit the document.

  + Better for *ad hoc* sharing. Just generate a URL (with [View or Edit permissions](#document-share-permissions-table)) and forward it to people who should access the document.
  + If you share a document link, recipients can share it with others.
    Caution

    - Be careful when using the **Share link** method of sharing documents.

      If you a share a document link with other people in your Dynatrace environment, link recipients could forward the link to others. No one outside your Dynatrace environment could use the link to access your document, of course, but anyone in your Dynatrace environment could use it, and they would have the same permissions (**Can edit** or **Can view**) that you selected when you created the link.

      The **Share access** method gives you tighter control (with a granularity down to the person) over who can view or edit your documents.
    - Be careful when using the **Allow editors to share** option, which allows anyone with **Can edit** permission to share your document with others.
  + If you need to revoke access for one person, you need to revoke access for everyone (disable the link you distributed) and then create and distribute a new link for people who should have access.

Note that you can use a combination of sharing options for the same document.
For example:

* Maintain a list of people or groups who need regular edit or view access to the document (collaboration and joint editing).
* Occasionally send out an early access link to a wider audience (people who only need to review the document).
* Enable view access for all when you have a publishable document that you want to share with everyone in your Dynatrace environment.

For details on document permission levels, see the [Permissions](#document-share-permissions-table) section.

### Access for all (view-only)

The simplest way to share your information with everyone in your Dynatrace environment is to give [Can view](#document-share-permissions-table) access to everyone in your Dynatrace environment.

1. Display the document (dashboard, notebook, or launchpad).
2. Select **Share**.

   If you don't see a **Share** option in the document, you don't have write permission for the document, so you can't access the share settings.
3. Select  (**Manage access**).
4. Turn on **Visible to anyone in your environment (Read only)**.

   Now everyone in your Dynatrace environment has [Can view](#document-share-permissions-table) permissions for your document.

   * To revoke this access, just turn off **Visible to anyone in your environment (Read only)**.
   * If you select [Remove all access](#document-remove-all-access), that includes turning off this switch.

### Access per user or group

If you use SCIM groups

Users in SCIM groups are not listed in the web UI for sharing a document (dashboard or notebook) to specific users or groups unless you add those users to local Dynatrace groups.

To share a document by creating a list of users and user groups with **Can view** or **Can edit** access

1. Display the document (dashboard, notebook, or launchpad).
2. Select **Share**.

   If you don't see a **Share** option in the document, you don't own the document, so you can't access the share settings.
3. In the  **Share access** section of the **Share document** window, specify one or more people and groups with whom you want to share the document, and select the permission level they should have (**Can view** or **Can edit**). Repeat this part of the procedure as many times as you need:

   1. Select **Add people or groups in your company**, and then find and select one or more people and groups with whom you want to share the document. You need to type at least three characters to get valid search results.
   2. Select the permission level (**Can view** or **Can edit**) that you want to give to the selected people and groups.
   3. Select **Share document**. This adds the selected people and groups to a list of people with whom you can share the document. It includes the permission level (**Can view** or **Can edit**) that was displayed when you selected **Share document**.

      Don't give **Can edit** access to people if you don't want them to change your copy of the document.

      For a list of what people can do with **Can view** and **Can edit** permission, see the [Permissions](#document-share-permissions-table) section below.

### Access via shared link

To share a document by generating and distributing links (URLs)

1. Display the document that you want to share.
2. Select **Share**.

   If you don't see a **Share** option in the document, you don't own the document, so you can't access the share settings.
3. In the  **Share link** section of the **Share document** window, select a permission level (**Can view** or **Can edit**) and then select **Create link**. This creates a URL (with the selected permission level) and copies it to your clipboard.
4. Paste the link to a company communication channel (email, for example) and send the link to Dynatrace users in your company with whom you want to share the document. Recipients will be able to use the link to open your document with the selected permission level.

## Manage access

To manage sharing permissions for your document

1. Display the document.
2. Select **Share**.

   If you don't see a **Share** option in the document, you don't own the document, so you can't access the share settings.
3. In the **Share document** window, select  (**Manage access**) in the upper-right corner.
4. In the **Manage access** window, review and change sharing options as needed.

   People and groups

   Link for editing

   Link for viewing

   The **People and groups** tab lists

   * The owner of the document. By default, this is the person who created the document, but you can [change the owner](#change-owner).
   * Every other person or group with **Can view** or **Can edit** access to the document (other than through any links you might have shared)

   For each entry other than the owner, you can select one of the following:

   * **Can view**
   * **Can edit**
   * **Remove**

   To add people or groups to the list, see the [Access per user or group](#document-share-access) section above.

   Anyone in your company with a link for editing can follow the link to your document and then view or edit it.

   * If you haven't made a link for editing, this tab is empty. Select **Create link** if you want to share such a link with others.
   * If you have made a link for editing, this tab displays the link.

     + To get a copy of the link that you can share with others in your company, select **Copy**.
     + To delete the link, select **Delete**. If you already shared the link with anyone, the link will no longer work.

   Anyone in your company with a link for viewing can follow the link to your document and view but not edit it.

   * If you haven't made a link for viewing, this tab is empty. Select **Create link** if you want to share such a link with others.
   * If you have made a link for viewing, this tab displays the link.

     + To get a copy of the link that you can share with others in your company, select **Copy**.
     + To delete the link, select **Delete**. If you already shared the link with anyone, the link will no longer work.

## Remove all access

Sometimes you need to quickly and easily remove all shared access to a document.

To revoke all sharing for your document

1. Display the document.
2. Select **Share**.

   If you don't see a **Share** option in the document, you don't own the document, so you can't access the share settings.
3. In the **Share document** window, select  in the upper-right corner.
4. In the **Manage access** window, select **Remove all access** and then confirm your choice.

After you remove all access, only you can view or edit your document.

* No other people have individual access
* Access is not granted to anyone through membership in any groups
* Previously shared **Can view** and **Can edit** links to your document no longer work
* If **Visible to anyone in your environment (Read only)** was turned on, now it's off

## Verify all access

After you change sharing settings, it's a good idea to verify them.

**Quick check**: the icon before the **Share** button at the top of your document indicates whether the document is already shared.

* = shared
* = not shared

If you just updated your share settings, you might need to refresh your document to display the correct icon.

If your document is shared, you can check to see who has access to it.

1. Display the document.
2. Select **Share**.
3. In the **Share document** window, select  (**Manage access**) in the upper-right corner.
4. Review the settings.

   * If **Visible to anyone in your environment (Read only)** is turned on, everyone in your Dynatrace environment can view the document.
   * If **Allow editors to share** is turned on, everyone with **Can edit** permission for the document can also share the document. If you turn this setting off, only the document owner can share the document.
   * Are the settings on the three tabs correct?

     + **People and groups**
     + **Link for editing**
     + **Link for viewing**

## Change owner

A Dynatrace documentâsuch as a dashboard, notebook, launchpad, or workflowâis initially owned by the user who created it. The document owner has full permissions for that document.

When you change the document owner, you immediately lose access to the document.

* Be sure you are ready to transfer ownership before you select this command.
* You can regain access to the document only if the new owner gives you permission.

If you think you might need to access the document again, make a duplicate of the document, transfer ownership of one of the duplicate documents, and retain ownership of the other until you're sure you don't need it anymore.

### Dashboards **Dashboards**

To change ownership of the currently displayed [dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")

1. Open the  menu next to the dashboard name and select  **Change owner**.
2. Find and select a new owner, and then select  **Change owner**.

To change ownership of multiple dashboards

1. In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, select ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** in the upper-left corner to display the **Dashboards** table.
2. Filter the table for  **Owned by me** to list your dashboards.
3. For each dashboard whose ownership you want to change, open the  menu for that dashboard and select  **Change owner**.

### Notebooks **Notebooks**

To change ownership of the currently displayed [notebook](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")

1. Open the  menu next to the notebook name and select  **Change owner**.
2. Find and select a new owner, and then select  **Change owner**.

To change ownership of multiple notebooks

1. In ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, select ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Notebooks** in the upper-left corner to display the **Notebooks** table.
2. Filter the table for  **Owned by me** to list your notebooks.
3. For each notebook whose ownership you want to change, open the  menu for that notebook and select  **Change owner**.

### Launchpads

To change ownership of a [launchpad](/docs/discover-dynatrace/get-started/dynatrace-ui/launchpads "Build and manage custom start pages with launchpads.")

1. Go to **Launcher**. If a launchpad is displayed, select  **Browse all** in the upper-left corner to display a table of launchpads.
2. Filter the table for  **Owned by me** to list your launchpads.
3. For each launchpad whose ownership you want to change, open the  menu for that launchpad and select  **Change owner**.

## Permissions

When you create a document, you are the document owner and you can do anything listed in the **Owner** column of the permissions table below. All other people have **Can view** or **Can edit** permission as determined by the document owner.

* **Can view**: can do the limited set of read-only things listed in the **Can view** column.
* **Can edit**: can do almost anything the owner can do.
* **Owner**: has permission to do everything with the document, including share it, change the owner, and delete it.

Sharing exceptions

* Be careful when using the **Share link** method of sharing documents.

  If you a share a document link with other people in your Dynatrace environment, link recipients could forward the link to others. No one outside your Dynatrace environment could use the link to access your document, of course, but anyone in your Dynatrace environment could use it, and they would have the same permissions (**Can edit** or **Can view**) that you selected when you created the link.

  The **Share access** method gives you tighter control (with a granularity down to the person) over who can view or edit your documents.
* Be careful when using the **Allow editors to share** option, which allows anyone with **Can edit** permission to share your document with others.

| **Permission** | **Can view** | **Can edit** | **Owner** |
| --- | --- | --- | --- |
| View the document | Applicable | Applicable | Applicable |
| Adjust the timeframe of the displayed data | Applicable | Applicable | Applicable |
| Refresh the document | Applicable | Applicable | Applicable |
| Adjust the automatic refresh rate | Applicable | Applicable | Applicable |
| Adjust the filter settings | Applicable | Applicable | Applicable |
| Maximize and minimize tiles | Applicable | Applicable | Applicable |
| Copy one or more tiles to the clipboard | Applicable | Applicable | Applicable |
| Save a copy of the document | Applicable | Applicable | Applicable |
| Export the JSON definition of the document | Applicable | Applicable | Applicable |
| Import the JSON definition of the document | Applicable | Applicable | Applicable |
| Edit the document | Not applicable | Applicable | Applicable |
| Change the layout | Not applicable | Applicable | Applicable |
| Rename the document | Not applicable | Applicable | Applicable |
| Add, change, and delete data | Not applicable | Applicable | Applicable |
| Add, change, and delete code | Not applicable | Applicable | Applicable |
| Add, change, and delete markdown | Not applicable | Applicable | Applicable |
| Add, change, and delete variables/filters | Not applicable | Applicable | Applicable |
| Share the document | Not applicable | Not applicable or Applicable\* | Applicable |
| Change owner of the document | Not applicable | Not applicable | Applicable |
| Delete the document | Not applicable | Not applicable | Applicable |

* If the document owner turns on **Allow editors to share**, anyone with **Can edit** permission can share the document with others.