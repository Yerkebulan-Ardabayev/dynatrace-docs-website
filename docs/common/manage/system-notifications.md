---
title: "System notifications"
source: https://docs.dynatrace.com/docs/manage/system-notifications
updated: 2026-02-09
---

# System notifications

# System notifications

* Explanation
* 2-min read
* Published Feb 23, 2022

The **Notifications** table displays notifications of Dynatrace system updates.

## Display notifications

To display the **Notifications** page, go to **Notifications**.

The **Notifications** page is available only to system administrators. If you don't see **Notifications** in Dynatrace, you don't have system administrator permission.

## Filter the table

To filter the table, set a filter in the filter bar:

* `Severity` can be set to `SEVERE`, `WARNING`, or `INFO`.
* `Message` is a search string for the message contents. For example, enter `agent` to display OneAgent updates and other notifications containing `agent` in the message.

## Sort the table

To sort the table, select the appropriate column header. You can sort by:

* **Received**âthe date and time on which the notification was received
* **Severity**âthe severity assigned to the notification (`SEVERE`, `WARNING`, or `INFO`)

## Resolve issues

Some notifications have a direct link to another page in the Dynatrace web UI. Select the link to go to the page and verify or change related settings.

## Clear notifications

Some notifications expire and are removed from the list when the system recovers to a healthy state. There is no global expiration for all notifications, so if the system doesn't recover to a healthy state, the notification will not be removed from the list until you select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the **Clear** column.

* To clear a single notification, select ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the **Clear** column.
* To clear multiple notifications, select their checkboxes and then select **Clear selected**.

### Notes

* Notifications are cleared per user: if multiple people use the **Notifications** page, clearing your notifications won't affect how others see the page.
* If you clear a notification but the conditions that generated the notification persist or reoccur, the notification (or a new copy of it) may come back.
