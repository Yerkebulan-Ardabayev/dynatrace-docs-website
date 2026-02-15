---
title: Grail security table migration guide
source: https://www.dynatrace.com/docs/secure/threat-observability/migration
scraped: 2026-02-15T21:26:35.553829
---

# Grail security table migration guide

# Grail security table migration guide

* Latest Dynatrace
* How-to guide
* Updated on Sep 23, 2025

Dynatrace introduces a new `security.events` table in [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data."), improving how security event data is consumed, stored, and queried. This guide explains the benefits, access control adjustments, ingestion and query changes, and required user actions.

The migration to the new `security.events` table is expected to be completed by the end of December 2025. To prevent any disruptions in your workflows, please ensure your migration is finalized before this deadline.

Refer to this guide for detailed instructions on completing the transition.

## Why migrate?

The new `security.events` table enhances security data management with:

* **Simpler security event queries** â You can directly retrieve security events with the `fetch security.events` command (see [DQL examples for security data](/docs/secure/threat-observability/dql-examples "DQL examples for security data powered by Grail.")).
* **No-code query support** â Dashboards and notebooks enable security event analysis via user-friendly filters, requiring no previous DQL knowledge (see [Explore security events](/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data#explore-security-events "Explore your data with our point-and-click interface.")).
* **Stronger access control** â Separate permissions ensure table-level and record-level security without impacting other event tables (see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.")).
* **Improved query performance** â Queries only scan security events, reducing complexity and improving efficiency.
* **Enhanced data ingestion** â Supports native nested JSON and introduces dedicated fields for raw event data access.

## Whatâs changing and what you need to do

With the introduction of the `security.events` table, some updates take place automatically, while others require manual action. See below for an overview.

### Automatic updates

* **Default data access policies** â Updated to include security events.
* **Dynatrace-generated security events** â Written to old and new tables until the migration is complete.
* **Dynatrace-provided processors and pipelines** â Will be migrated and will work seamlessly with the new ingest scope.
* **![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, and ready-made documentation samples** â Adjusted to query the new security events table.

### Manual updates required

* **Custom access policies** â Update manually to grant permissions for the new `security.events` table (see [Access control updates](#access)).
* **Third-party product ingest URLs** â Change the ingest endpoint from `/events.security` to `/security.events` (see [Data ingestion updates](#data)).
* **Custom processing pipelines** â Manually migrate sources via ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Security events** (see [Data ingestion updates](#data)).
* **Custom queries** â Modify DQL queries to reference `security.events` instead of `events` (see [DQL query updates](#query)).
* **Migrating the connections for the integration apps/extensions** - If you've already installed and configured [security integrations](/docs/secure/threat-observability/security-events-ingest#ingest "Ingest external security data into Grail."), you need to do one of the following:

  + Reconfigure the third-party URL to point to `/security.events`. This allows existing connections to continue working and display data from the new table.
  + Recreate the connections and follow the on-screen setup instructions, which already include the updated endpoint.

## Access control updates

* (Automatic) Default access policies are automatically updated:

  + `All Grail data read access` â Read all Grail data, including security events.
  + `Read Security Events` â Read security events only.
  + `OpenPipeline Ingest` â Continue ingesting security events using existing permissions.
* (Manual) Custom policies require manual changes:

  + New:

    ```
    // previous security events within the events data table



    ALLOW storage:buckets:read WHERE storage:bucket-name IN ("default_security_events", "default_security_custom_events");



    ALLOW storage:events:read;



    // new table permissions



    ALLOW storage:buckets:read WHERE storage:table-name = 'security.events';



    ALLOW storage:security.events:read;
    ```
  + Previously:

    ```
    ALLOW storage:buckets:read WHERE storage:bucket-name IN ("default_security_events", "default_security_custom_events");



    ALLOW storage:events:read;
    ```
* (Manual) For more granular access control, use the new buckets:

  + Read Dynatrace-generated events:

    - New: `default_securityevents_builtin`
    - Previously: `default_security_events`
  + Read externally ingested events:

    - New: `default_securityevents`
    - Previously: `default_security_custom_events`

## Data ingestion updates

Dynatrace-generated events are stored in both the legacy and new tables until migration is complete. However, [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")-related events are no longer duplicated and are now available exclusively in the new `security.events` table. All other Dynatrace-generated events continue to be written to both tables during the migration period.

* (Automatic) Dynatrace-provided processors and pipelines work seamlessly with the new ingestion scope.
* (Manual) Update third-party product ingest URLs:

  + Default pipeline:

    - New: `/platform/ingest/v1/security.events`
    - Previously: `/platform/ingest/v1/events.security`
  + Custom pipeline:

    - New: `/platform/ingest/v1/security.events/<custom_ingest_source>`
    - Previously: `/platform/ingest/v1/events.security/<custom_ingest_source>`

    Example new default and custom pipelines

    New default and custom pipelines via **Settings** > **Process and contextualize** > **OpenPipeline** > **Security events (New)**:

    ![settings-openpipeline-security-events](https://dt-cdn.net/images/custom-settings-openpipeline-security-events-3382-de1282230f.png)
* (Manual) Migrate custom ingest sources via ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Security events**.
* (Manual) Copy over and adjust, if required, the existing custom processors in your custom pipelines into the new `security.events` OpenPipeline ingest scope.

## DQL query updates

* (Automatic) ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, and ready-made documentation samples delivered with Dynatrace apps and extensions now reference `security.events`.
* (Automatic) The pre-built queries in Dynatrace apps are updated automatically where applicable.
* (Manual) Update your custom queries in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, and ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** to fetch from `security.events` instead of `events`.

  + To query only recent data, switch completely to querying `security.events`.
  + To query both historical and new security events, modify queries to fetch from both tables.
  + To query only historical data, you can continue using the old queries.

  To bulk-update multiple queries in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, or ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, download the document JSON file and use a text editor for find and replace actions.

### Example query updates

#### Query all security events

* New:

```
fetch security.events
```

* Previously:

```
fetch events | filter event.kind == "SECURITY_EVENT"
```

#### Query Dynatrace-generated events

* New:

```
fetch security.events | filter dt.system.bucket=="default_securityevents_builtin"
```

* Previously:

```
fetch events | filter dt.system.bucket=="default_security_events"
```

#### Query ingested events

* New:

```
fetch security.events | filter dt.system.bucket=="default_securityevents"
```

* Previously:

```
fetch events | filter dt.system.bucket=="default_security_custom_events"
```

#### Query ingested events in both old and new security event tables

```
// Fetch all migrated security events



fetch security.events



| filter dt.system.bucket!="default_securityevents_builtin"



| append [



// Fetch all security events that were not migrated



fetch events



| filter event.kind == "SECURITY_EVENT"



// Exclude the by Dynatrace generated security events as they are written in both tables



| filter dt.system.bucket!="default_security_events"



]
```