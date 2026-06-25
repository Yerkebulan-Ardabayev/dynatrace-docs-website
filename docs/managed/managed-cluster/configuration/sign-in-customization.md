---
title: Sign-in page customization
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/sign-in-customization
scraped: 2026-05-12T11:36:59.529090
---

# Sign-in page customization

# Sign-in page customization

* Published Jan 28, 2021

As the Dynatrace Managed cluster administrator, there are situations in which you would like to pass on information to cluster users before signing in to the cluster. You may want to display system information, authentication details, legal notes, or an administrator contact. To achieve that, you can customize the sign-in page to display specific information.

To customize the sign-in page, go to **User Authentication** > **Login screen** and modify the default messages (all messages are optional):

* **Title** - Text displayed under "Dynatrace Managed".
* **Introduction** - Text displayed in a smaller font under the title.
* **Details** - Initially collapsed text that can be expanded by the user. Can be set only if **Introduction** is defined.