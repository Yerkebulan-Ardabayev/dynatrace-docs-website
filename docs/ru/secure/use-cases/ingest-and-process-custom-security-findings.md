---
title: Ingest and process custom security findings
source: https://www.dynatrace.com/docs/secure/use-cases/ingest-and-process-custom-security-findings
scraped: 2026-02-26T21:31:18.610528
---

# Ingest and process custom security findings

# Ingest and process custom security findings

* Latest Dynatrace
* Tutorial
* Updated on Jun 17, 2025

In the following, you'll learn how to ingest and process custom security data while pushing the data from a third-party tool to Dynatrace, using the OpenPipeline ingest API for security events.

## Target audience

Security practitioners aiming to analyze, visualize, and automate custom security data with Dynatrace.

## Scenario

You're a security architect who uses Dynatrace to monitor the health of applications and services. As part of Software Development Lifecycle (SDLC) security practices, you need to ensure that developers scan container images before deploying them into production.

To achieve this, you want to

1. Ingest your container scan findings to Dynatrace continuously.
2. Connect the findings to the monitored production containers.
3. Create automatic Jira tickets to the dev-owners of the containers if there are missing security scans for the corresponding container images.

This article covers the first part: ingesting custom security findings and mapping them to Dynatrace Semantic Dictionary for security vulnerability findings.

Sample input for security findings - Trivy JSON scan report

```
{



"SchemaVersion": 2,



"CreatedAt": "2021-08-25T12:20:30.000000005Z",



"ArtifactName": "testdata/fixtures/images/alpine-39.tar.gz",



"ArtifactType": "container_image",



"Metadata": {



"OS": {



"Family": "alpine",



"Name": "3.9.4",



"EOSL": true



},



"ImageID": "sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1",



"DiffIDs": [



"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



],



"ImageConfig": {



"architecture": "amd64",



"container": "c10d36fa368a7ea673683682666758adf35efe98e10989505f4f566b5b18538f",



"created": "2019-05-11T00:07:03.510395965Z",



"docker_version": "18.06.1-ce",



"history": [



{



"created": "2019-05-11T00:07:03.358250803Z",



"created_by": "/bin/sh -c #(nop) ADD file:a86aea1f3a7d68f6ae03397b99ea77f2e9ee901c5c59e59f76f93adbb4035913 in / "



},



{



"created": "2019-05-11T00:07:03.510395965Z",



"created_by": "/bin/sh -c #(nop)  CMD [\"/bin/sh\"]",



"empty_layer": true



}



],



"os": "linux",



"rootfs": {



"type": "layers",



"diff_ids": [



"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



]



},



"config": {



"Cmd": [



"/bin/sh"



],



"Env": [



"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"



],



"Image": "sha256:09f2bbe58e774849d74dc1391c2e01731896c745c4aba1ecf69a283bdb4b537a",



"ArgsEscaped": true



}



}



},



"Results": [



{



"Target": "testdata/fixtures/images/alpine-39.tar.gz (alpine 3.9.4)",



"Class": "os-pkgs",



"Type": "alpine",



"Vulnerabilities": [



{



"VulnerabilityID": "CVE-2019-14697",



"PkgID": "musl@1.1.20-r4",



"PkgName": "musl",



"PkgIdentifier": {



"PURL": "pkg:apk/alpine/musl@1.1.20-r4?arch=x86_64\u0026distro=3.9.4",



"UID": "d6abd271e71d3ce2"



},



"InstalledVersion": "1.1.20-r4",



"FixedVersion": "1.1.20-r5",



"Status": "fixed",



"Layer": {



"Digest": "sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10",



"DiffID": "sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



},



"SeveritySource": "nvd",



"PrimaryURL": "https://avd.aquasec.com/nvd/cve-2019-14697",



"DataSource": {



"ID": "alpine",



"Name": "Alpine Secdb",



"URL": "https://secdb.alpinelinux.org/"



},



"Description": "musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code.",



"Severity": "CRITICAL",



"CweIDs": [



"CWE-787"



],



"VendorSeverity": {



"nvd": 4



},



"CVSS": {



"nvd": {



"V2Vector": "AV:N/AC:L/Au:N/C:P/I:P/A:P",



"V3Vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"V2Score": 7.5,



"V3Score": 9.8



}



},



"References": [



"http://www.openwall.com/lists/oss-security/2019/08/06/4",



"https://security.gentoo.org/glsa/202003-13",



"https://www.openwall.com/lists/musl/2019/08/06/1"



],



"PublishedDate": "2019-08-06T16:15:00Z",



"LastModifiedDate": "2020-03-14T19:15:00Z"



},



{



"VulnerabilityID": "CVE-2019-14697",



"PkgID": "musl-utils@1.1.20-r4",



"PkgName": "musl-utils",



"PkgIdentifier": {



"PURL": "pkg:apk/alpine/musl-utils@1.1.20-r4?arch=x86_64\u0026distro=3.9.4",



"UID": "8c341199f4077fc8"



},



"InstalledVersion": "1.1.20-r4",



"FixedVersion": "1.1.20-r5",



"Status": "fixed",



"Layer": {



"Digest": "sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10",



"DiffID": "sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



},



"SeveritySource": "nvd",



"PrimaryURL": "https://avd.aquasec.com/nvd/cve-2019-14697",



"DataSource": {



"ID": "alpine",



"Name": "Alpine Secdb",



"URL": "https://secdb.alpinelinux.org/"



},



"Description": "musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code.",



"Severity": "CRITICAL",



"CweIDs": [



"CWE-787"



],



"VendorSeverity": {



"nvd": 4



},



"CVSS": {



"nvd": {



"V2Vector": "AV:N/AC:L/Au:N/C:P/I:P/A:P",



"V3Vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"V2Score": 7.5,



"V3Score": 9.8



}



},



"References": [



"http://www.openwall.com/lists/oss-security/2019/08/06/4",



"https://security.gentoo.org/glsa/202003-13",



"https://www.openwall.com/lists/musl/2019/08/06/1"



],



"PublishedDate": "2019-08-06T16:15:00Z",



"LastModifiedDate": "2020-03-14T19:15:00Z"



}



]



}



]



}
```

## Prerequisites

* Your [containers are deployed in Kubernetes and monitored by Dynatrace](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes")
* Corresponding container images are scanned by a third-party tool (in this case, Trivy)

### Permissions

To add new sources and pipeline processing to OpenPipeline, you need both permissions below.

* `openpipeline:configurations:read`
* `openpipeline:configurations:write`

To learn how to set up the permissions, see [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

## Get started

For instructions on ingesting any type of event, see [How to ingest data (events)](/docs/platform/openpipeline/getting-started/how-to-ingestion "How to ingest data for a configuration scope in OpenPipeline.").

1. Configure endpoint in Dynatrace

1. Open **OpenPipeline**.
2. Go to **Events** > **Security events** > **Ingest sources**.
3. You have two ingest options:

   * Recommended Option 1 - Use the builtin security events endpoint Copy the URL of the builtin security events endpoint.

     ![copy URL of builtin security events endpoint](https://dt-cdn.net/images/2024-08-28-19-48-19-1855-96c02de135.png)
   * Option 2 - Create a custom endpoint Select  **Source** to [create a custom ingest source](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#ingest "Configure ingest sources, routes, and processing for your data in OpenPipeline."), then copy its URL.

   For more information about the ingest options, see [Security events ingest](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.").
4. Generate an [access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Learn the concept of a personal access token and its scopes.") with the required scope according to your ingest option selected in step 3.

   For details on the required scopes, see [Get started](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data#start "Ingest security events from custom third-party products via API.").

2. Feed data into Grail

Use the ingest endpoint URL and access token generated previously to configure the third-party product.

To work granularly later with the security findings ingested to Grail, aggregated reports should be broken into and ingested as individual findings.

In this case, we modified events before ingestion to include only a single container image, vulnerability, and vulnerable library.

Sample ingested event with a single vulnerability finding

```
{



"SchemaVersion": 2,



"CreatedAt": "2021-08-25T12:20:30.000000005Z",



"ArtifactName": "testdata/fixtures/images/alpine-39.tar.gz",



"ArtifactType": "container_image",



"Metadata": {



"OS": {



"Family": "alpine",



"Name": "3.9.4",



"EOSL": true



},



"ImageID": "sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1",



"DiffIDs": [



"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



],



"ImageConfig": {



"architecture": "amd64",



"container": "c10d36fa368a7ea673683682666758adf35efe98e10989505f4f566b5b18538f",



"created": "2019-05-11T00:07:03.510395965Z",



"docker_version": "18.06.1-ce",



"history": [



{



"created": "2019-05-11T00:07:03.358250803Z",



"created_by": "/bin/sh -c #(nop) ADD file:a86aea1f3a7d68f6ae03397b99ea77f2e9ee901c5c59e59f76f93adbb4035913 in / "



},



{



"created": "2019-05-11T00:07:03.510395965Z",



"created_by": "/bin/sh -c #(nop)  CMD [\"/bin/sh\"]",



"empty_layer": true



}



],



"os": "linux",



"rootfs": {



"type": "layers",



"diff_ids": [



"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



]



},



"config": {



"Cmd": [



"/bin/sh"



],



"Env": [



"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"



],



"Image": "sha256:09f2bbe58e774849d74dc1391c2e01731896c745c4aba1ecf69a283bdb4b537a",



"ArgsEscaped": true



}



}



},



"Results": [



{



"Target": "testdata/fixtures/images/alpine-39.tar.gz (alpine 3.9.4)",



"Class": "os-pkgs",



"Type": "alpine",



"Vulnerabilities": [



{



"VulnerabilityID": "CVE-2019-14697",



"PkgID": "musl@1.1.20-r4",



"PkgName": "musl",



"PkgIdentifier": {



"PURL": "pkg:apk/alpine/musl@1.1.20-r4?arch=x86_64\u0026distro=3.9.4",



"UID": "d6abd271e71d3ce2"



},



"InstalledVersion": "1.1.20-r4",



"FixedVersion": "1.1.20-r5",



"Status": "fixed",



"Layer": {



"Digest": "sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10",



"DiffID": "sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81"



},



"SeveritySource": "nvd",



"PrimaryURL": "https://avd.aquasec.com/nvd/cve-2019-14697",



"DataSource": {



"ID": "alpine",



"Name": "Alpine Secdb",



"URL": "https://secdb.alpinelinux.org/"



},



"Description": "musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code.",



"Severity": "CRITICAL",



"CweIDs": [



"CWE-787"



],



"VendorSeverity": {



"nvd": 4



},



"CVSS": {



"nvd": {



"V2Vector": "AV:N/AC:L/Au:N/C:P/I:P/A:P",



"V3Vector": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"V2Score": 7.5,



"V3Score": 9.8



}



},



"References": [



"http://www.openwall.com/lists/oss-security/2019/08/06/4",



"https://security.gentoo.org/glsa/202003-13",



"https://www.openwall.com/lists/musl/2019/08/06/1"



],



"PublishedDate": "2019-08-06T16:15:00Z",



"LastModifiedDate": "2020-03-14T19:15:00Z"



}



]



}



]



}
```

3. Validate data in Notebooks

To validate data, open [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and query the security events.

Sample DQL query:

This query has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

```
fetch security.events



| filter dt.system.bucket == "default_securityevents"



| sort timestamp desc
```

To clearly distinguish ingested data from other ingested events, you can add filters for the attributes you expect there.

Example:

```
| filter SchemaVersion == 2 AND ArtifactType == "container_image"
```

The query result should include the ingested event in the original format with a few enriched fields, such as `timestamp` and `event.kind`.

Sample query result

```
{



// enriched fields



"timestamp": "2024-08-02T14:38:53.854000000Z",



"event.kind": "SECURITY_EVENT",



// original fields



"SchemaVersion": 2,



"Results": [



"{\"Target\":\"testdata/fixtures/images/alpine-39.tar.gz (alpine 3.9.4)\",\"Class\":\"os-pkgs\",\"Type\":\"alpine\",\"Vulnerabilities\":[{\"VulnerabilityID\":\"CVE-2019-14697\",\"PkgID\":\"musl@1.1.20-r4\",\"PkgName\":\"musl\",\"PkgIdentifier\":{\"PURL\":\"pkg:apk/alpine/musl@1.1.20-r4?arch=x86_64&distro=3.9.4\",\"UID\":\"d6abd271e71d3ce2\"},\"InstalledVersion\":\"1.1.20-r4\",\"FixedVersion\":\"1.1.20-r5\",\"Status\":\"fixed\",\"Layer\":{\"Digest\":\"sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10\",\"DiffID\":\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"},\"SeveritySource\":\"nvd\",\"PrimaryURL\":\"https://avd.aquasec.com/nvd/cve-2019-14697\",\"DataSource\":{\"ID\":\"alpine\",\"Name\":\"Alpine Secdb\",\"URL\":\"https://secdb.alpinelinux.org/\"},\"Description\":\"musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code.\",\"Severity\":\"CRITICAL\",\"CweIDs\":[\"CWE-787\"],\"VendorSeverity\":{\"nvd\":4},\"CVSS\":{\"nvd\":{\"V2Vector\":\"AV:N/AC:L/Au:N/C:P/I:P/A:P\",\"V3Vector\":\"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\",\"V2Score\":7.5,\"V3Score\":9.8}},\"References\":[\"http://www.openwall.com/lists/oss-security/2019/08/06/4\",\"https://security.gentoo.org/glsa/202003-13\",\"https://www.openwall.com/lists/musl/2019/08/06/1\"],\"PublishedDate\":\"2019-08-06T16:15:00Z\",\"LastModifiedDate\":\"2020-03-14T19:15:00Z\"}]}"



],



"ArtifactType": "container_image",



"CreatedAt": "2021-08-25T12:20:30.000000005Z",



"Metadata": "{\"OS\":{\"Family\":\"alpine\",\"Name\":\"3.9.4\",\"EOSL\":true},\"ImageID\":\"sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1\",\"DiffIDs\":[\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"],\"ImageConfig\":{\"architecture\":\"amd64\",\"container\":\"c10d36fa368a7ea673683682666758adf35efe98e10989505f4f566b5b18538f\",\"created\":\"2019-05-11T00:07:03.510395965Z\",\"docker_version\":\"18.06.1-ce\",\"history\":[{\"created\":\"2019-05-11T00:07:03.358250803Z\",\"created_by\":\"/bin/sh -c #(nop) ADD file:a86aea1f3a7d68f6ae03397b99ea77f2e9ee901c5c59e59f76f93adbb4035913 in / \"},{\"created\":\"2019-05-11T00:07:03.510395965Z\",\"created_by\":\"/bin/sh -c #(nop)  CMD [\\\"/bin/sh\\\"]\",\"empty_layer\":true}],\"os\":\"linux\",\"rootfs\":{\"type\":\"layers\",\"diff_ids\":[\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"]},\"config\":{\"Cmd\":[\"/bin/sh\"],\"Env\":[\"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"],\"Image\":\"sha256:09f2bbe58e774849d74dc1391c2e01731896c745c4aba1ecf69a283bdb4b537a\",\"ArgsEscaped\":true}}}",



"ArtifactName": "testdata/fixtures/images/alpine-39.tar.gz"



}
```

In the current case, format isn't supported and data isn't mapped. If Dynatrace supports the format, it automatically maps it to the [Semantic Dictionary conventionsï»¿](https://dt-url.net/3q03pb0).

4. Map data to Dynatrace Semantic Dictionary

In simple cases, you can work with ingested events in their original format. However, this becomes difficult in more complex cases, as

* There are many nested fields
* You can't access findings from various tools and products uniformly
* Some fields are added to classify the findings correctly, and others are mapped to the conventions

In such complex cases, you need to manually map the ingested data to the Dynatrace Semantic Dictionary. When data is mapped, the original data persists alongside the mapped one, which allows you to benefit from the vendor-specific data in your analysis and automation or as an additional context.

1. In **OpenPipeline**, select **Pipelines** >  **Pipeline** to [create a custom pipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#process "Configure ingest sources, routes, and processing for your data in OpenPipeline."), and name it, for example, "Custom security findings".
2. Add a [processor](/docs/platform/openpipeline/concepts/processing#processor "Learn the core concepts of Dynatrace OpenPipeline processing.") of type **DQL** to your pipeline and configure it to parse the fields required by the [Semantic Dictionaryï»¿](https://dt-url.net/3q03pb0) (in our case, we want to map the vulnerability findings' basic fields and, as an extension, container image details). Enter the following data:

   * Processor name: For example, "Map Trivy fields"
   * Matching condition: `SchemaVersion == 2 AND ArtifactType == "container_image"` (this way, the mapping will be attempted only for the relevant events)
   * DQL processor definition (in the mapping, we assume that the result and vulnerability arrays already include single items):

   Sample DQL processor definition

   ```
   fieldsAdd event.type="VULNERABILITY_FINDING",



   event.provider="Trivy"



   | parse Results[0], """json:result"""



   | fieldsAdd vulnerability=result[Vulnerabilities][0]



   | parse vulnerability, """json:vulnerability"""



   | parse Metadata, """json:metadata"""



   | fieldsAdd



   finding.id=concat(ArtifactName,"/",metadata[ImageID],"/",vulnerability[PkgID]),



   finding.time.created=toTimestamp(CreatedAt),



   finding.severity=vulnerability[Severity]



   | fieldsAdd



   dt.security.risk.level=if(vulnerability[Severity]=="UNKNOWN","NOT_AVAILABLE",else:vulnerability[Severity]),



   dt.security.risk.score=if(vulnerability[Severity]=="CRITICAL",10,else:



   if(vulnerability[Severity]=="HIGH",8,else:



   if(vulnerability[Severity]=="MEDIUM",6,else:



   if(vulnerability[Severity]=="LOW",3,else:0))))



   | fieldsAdd



   object.id=concat(ArtifactName,"/",metadata[ImageID]),



   object.type="CONTAINER_IMAGE",



   object.name=ArtifactName



   | fieldsAdd



   vulnerability.id=vulnerability[VulnerabilityID],



   vulnerability.description=coalesce(vulnerability[Description],vulnerability[VulnerabilityID]),



   vulnerability.title=coalesce(vulnerability[Title],vulnerability[VulnerabilityID])



   | fieldsAdd



   component.name=vulnerability[PkgName],



   component.version=vulnerability[InstalledVersion]



   | fieldsAdd



   container_image.digest=vulnerability[Layer][Digest]



   | fieldsAdd artifact=splitString(ArtifactName,":")



   | fieldsAdd container_image.repository=artifact[0],



   container_image.tags=artifact[1]



   | fieldsRemove vulnerability, Metadata, artifact
   ```

   ![config dql processor](https://dt-cdn.net/images/2024-11-01-10-41-25-1694-e7c83279aa.png)

   Sample mapped result

   ```
   "timestamp": "2024-10-31T09:58:21.141000000Z",



   "event.provider": "Trivy",



   "event.type": "VULNERABILITY_FINDING",



   "dt.security.risk.score": 10,



   "dt.security.risk.level": "CRITICAL",



   "finding.id": "testdata/fixtures/images/alpine-39.tar.gz/sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1/musl@1.1.20-r4",



   "finding.time.created": "2021-08-25T12:20:30.000000005Z",



   "finding.severity": "CRITICAL",



   "object.id": "testdata/fixtures/images/alpine-39.tar.gz/sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1",



   "object.type": "CONTAINER_IMAGE",



   "object.name": "testdata/fixtures/images/alpine-39.tar.gz",



   "vulnerability.id": "CVE-2019-14697",



   "vulnerability.title": "CVE-2019-14697",



   "vulnerability.description": "musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code."



   "component.name": "musl",



   "component.version": "1.1.20-r4",



   "container_image.digest": "sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10",



   "container_image.tags": null,



   "container_image.repository": "testdata/fixtures/images/alpine-39.tar.gz",



   "metadata": "{\"OS\":{\"Family\":\"alpine\", \"Name\":\"3.9.4\", \"EOSL\":true}, \"ImageID\":\"sha256:055936d3920576da37aa9bc460d70c5f212028bda1c08c0879aedf03d7a66ea1\", \"DiffIDs\":[\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"], \"ImageConfig\":{\"architecture\":\"amd64\", \"container\":\"c10d36fa368a7ea673683682666758adf35efe98e10989505f4f566b5b18538f\", \"created\":\"2019-05-11T00:07:03.510395965Z\", \"docker_version\":\"18.06.1-ce\", \"history\":[{\"created\":\"2019-05-11T00:07:03.358250803Z\", \"created_by\":\"/bin/sh -c #(nop) ADD file:a86aea1f3a7d68f6ae03397b99ea77f2e9ee901c5c59e59f76f93adbb4035913 in / \"}, {\"created\":\"2019-05-11T00:07:03.510395965Z\", \"created_by\":\"/bin/sh -c #(nop)  CMD [\\\"/bin/sh\\\"]\", \"empty_layer\":true}], \"os\":\"linux\", \"rootfs\":{\"type\":\"layers\", \"diff_ids\":[\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"]}, \"config\":{\"Cmd\":[\"/bin/sh\"], \"Env\":[\"PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\"], \"Image\":\"sha256:09f2bbe58e774849d74dc1391c2e01731896c745c4aba1ecf69a283bdb4b537a\", \"ArgsEscaped\":true}}}",



   "CreatedAt": "2021-08-25T12:20:30.000000005Z",



   "result": "{\"Target\":\"testdata/fixtures/images/alpine-39.tar.gz (alpine 3.9.4)\", \"Class\":\"os-pkgs\", \"Type\":\"alpine\", \"Vulnerabilities\":[{\"VulnerabilityID\":\"CVE-2019-14697\", \"PkgID\":\"musl@1.1.20-r4\", \"PkgName\":\"musl\", \"PkgIdentifier\":{\"PURL\":\"pkg:apk/alpine/musl@1.1.20-r4?arch=x86_64&distro=3.9.4\", \"UID\":\"d6abd271e71d3ce2\"}, \"InstalledVersion\":\"1.1.20-r4\", \"FixedVersion\":\"1.1.20-r5\", \"Status\":\"fixed\", \"Layer\":{\"Digest\":\"sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10\", \"DiffID\":\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"}, \"SeveritySource\":\"nvd\", \"PrimaryURL\":\"https://avd.aquasec.com/nvd/cve-2019-14697\", \"DataSource\":{\"ID\":\"alpine\", \"Name\":\"Alpine Secdb\", \"URL\":\"https://secdb.alpinelinux.org/\"}, \"Description\":\"musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application\\'s source code.\", \"Severity\":\"CRITICAL\", \"CweIDs\":[\"CWE-787\"], \"VendorSeverity\":{\"nvd\":4}, \"CVSS\":{\"nvd\":{\"V2Vector\":\"AV:N/AC:L/Au:N/C:P/I:P/A:P\", \"V3Vector\":\"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\", \"V2Score\":7.5, \"V3Score\":9.8}}, \"References\":[\"http://www.openwall.com/lists/oss-security/2019/08/06/4\", \"https://security.gentoo.org/glsa/202003-13\", \"https://www.openwall.com/lists/musl/2019/08/06/1\"], \"PublishedDate\":\"2019-08-06T16:15:00Z\", \"LastModifiedDate\":\"2020-03-14T19:15:00Z\"}]}",



   "SchemaVersion": 2,



   "ArtifactName": "testdata/fixtures/images/alpine-39.tar.gz",



   "Results": [



   "{\"Target\":\"testdata/fixtures/images/alpine-39.tar.gz (alpine 3.9.4)\",\"Class\":\"os-pkgs\",\"Type\":\"alpine\",\"Vulnerabilities\":[{\"VulnerabilityID\":\"CVE-2019-14697\",\"PkgID\":\"musl@1.1.20-r4\",\"PkgName\":\"musl\",\"PkgIdentifier\":{\"PURL\":\"pkg:apk/alpine/musl@1.1.20-r4?arch=x86_64&distro=3.9.4\",\"UID\":\"d6abd271e71d3ce2\"},\"InstalledVersion\":\"1.1.20-r4\",\"FixedVersion\":\"1.1.20-r5\",\"Status\":\"fixed\",\"Layer\":{\"Digest\":\"sha256:e7c96db7181be991f19a9fb6975cdbbd73c65f4a2681348e63a141a2192a5f10\",\"DiffID\":\"sha256:f1b5933fe4b5f49bbe8258745cf396afe07e625bdab3168e364daf7c956b6b81\"},\"SeveritySource\":\"nvd\",\"PrimaryURL\":\"https://avd.aquasec.com/nvd/cve-2019-14697\",\"DataSource\":{\"ID\":\"alpine\",\"Name\":\"Alpine Secdb\",\"URL\":\"https://secdb.alpinelinux.org/\"},\"Description\":\"musl libc through 1.1.23 has an x87 floating-point stack adjustment imbalance, related to the math/i386/ directory. In some cases, use of this library could introduce out-of-bounds writes that are not present in an application's source code.\",\"Severity\":\"CRITICAL\",\"CweIDs\":[\"CWE-787\"],\"VendorSeverity\":{\"nvd\":4},\"CVSS\":{\"nvd\":{\"V2Vector\":\"AV:N/AC:L/Au:N/C:P/I:P/A:P\",\"V3Vector\":\"CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\",\"V2Score\":7.5,\"V3Score\":9.8}},\"References\":[\"http://www.openwall.com/lists/oss-security/2019/08/06/4\",\"https://security.gentoo.org/glsa/202003-13\",\"https://www.openwall.com/lists/musl/2019/08/06/1\"],\"PublishedDate\":\"2019-08-06T16:15:00Z\",\"LastModifiedDate\":\"2020-03-14T19:15:00Z\"}]}"



   ],



   "ArtifactType": "container_image"
   ```
3. Select **Dynamic routing** >  **Dynamic route** to [add a dynamic routing](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#route "Configure ingest sources, routes, and processing for your data in OpenPipeline.") to the new pipeline. Enter the following data:

   * Dynamic route name: For example, "Custom event"
   * Matching condition: `SchemaVersion == 2 AND ArtifactType == "container_image"`
   * Select the pipeline to which the dynamic routing will apply (in our case, `Custom security findings`)

   ![add dynamic routing](https://dt-cdn.net/images/2024-08-28-23-04-46-576-9e042f6845.png)

   For details on dynamic routing, see [Routing](/docs/platform/openpipeline/concepts/data-flow#routing "Learn how data flows in Dynatrace Platform, from ingestion to storage, via Dynatrace OpenPipeline.").



## Next steps

Now you can use the data to

* [Visualize container vulnerability findings with a sample dashboard](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")
* [Automate Jira ticket creation and Slack notifications with sample workflows](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")