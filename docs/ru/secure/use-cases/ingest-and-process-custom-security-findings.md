---
title: Загрузка и обработка пользовательских данных о безопасности
source: https://www.dynatrace.com/docs/secure/use-cases/ingest-and-process-custom-security-findings
scraped: 2026-03-06T21:15:06.393399
---

# Загрузка и обработка пользовательских данных о безопасности

# Загрузка и обработка пользовательских данных о безопасности

* Последняя версия Dynatrace
* Руководство
* Обновлено 17 июня 2025 г.

В следующем руководстве вы узнаете, как загружать и обрабатывать пользовательские данные безопасности, передавая данные из стороннего инструмента в Dynatrace с помощью API загрузки OpenPipeline для событий безопасности.

## Целевая аудитория

Специалисты по безопасности, стремящиеся анализировать, визуализировать и автоматизировать пользовательские данные безопасности с помощью Dynatrace.

## Сценарий

Вы — архитектор по безопасности, использующий Dynatrace для мониторинга работоспособности приложений и сервисов. В рамках практик безопасности жизненного цикла разработки программного обеспечения (SDLC) вам необходимо обеспечить проверку образов контейнеров разработчиками перед развёртыванием в производственной среде.

Для этого вы хотите:

1. Непрерывно загружать результаты сканирования контейнеров в Dynatrace.
2. Сопоставлять результаты с мониторируемыми производственными контейнерами.
3. Автоматически создавать тикеты Jira для разработчиков-владельцев контейнеров при отсутствии необходимых проверок безопасности для соответствующих образов контейнеров.

Эта статья охватывает первую часть: загрузку пользовательских данных о безопасности и их сопоставление с Dynatrace Semantic Dictionary для находок уязвимостей безопасности.

Пример входных данных для находок безопасности — отчёт Trivy JSON

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

## Предварительные условия

* Ваши [контейнеры развёрнуты в Kubernetes и отслеживаются Dynatrace](/docs/ingest-from/setup-on-k8s/deployment "Развертывание Dynatrace Operator на Kubernetes")
* Соответствующие образы контейнеров сканируются сторонним инструментом (в данном случае, Trivy)

### Разрешения

Чтобы добавить новые источники и конвейерную обработку в OpenPipeline, вам необходимы оба следующих разрешения.

* `openpipeline:configurations:read`
* `openpipeline:configurations:write`

Чтобы узнать, как настроить разрешения, см. [Разрешения в Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Узнайте, как назначать разрешения для корзин и таблиц в Grail.").

## Начало работы

Инструкции по загрузке любого типа событий см. в разделе [Как загружать данные (события)](/docs/platform/openpipeline/getting-started/how-to-ingestion "Как загружать данные для области конфигурации в OpenPipeline.").

1. Настройка конечной точки в Dynatrace

1. Откройте **OpenPipeline**.
2. Перейдите в **Events** > **Security events** > **Ingest sources**.
3. У вас есть два варианта загрузки:

   * Рекомендуемый вариант 1 — использование встроенной конечной точки событий безопасности. Скопируйте URL встроенной конечной точки событий безопасности.

     ![copy URL of builtin security events endpoint](https://dt-cdn.net/images/2024-08-28-19-48-19-1855-96c02de135.png)
   * Вариант 2 — создание пользовательской конечной точки. Выберите **Source** для [создания пользовательского источника загрузки](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#ingest "Настройка источников загрузки, маршрутов и обработки данных в OpenPipeline."), затем скопируйте его URL.

   Подробнее о вариантах загрузки см. [Загрузка событий безопасности](/docs/secure/threat-observability/security-events-ingest "Загрузка внешних данных безопасности в Grail.").
4. Создайте [токен доступа](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Изучите концепцию персонального токена доступа и его области.") с необходимой областью в соответствии с выбранным вариантом загрузки из шага 3.

   Подробнее о необходимых областях см. [Начало работы](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data#start "Загрузка событий безопасности из пользовательских сторонних продуктов через API.").

2. Передача данных в Grail

Используйте URL конечной точки загрузки и ранее созданный токен доступа для настройки стороннего продукта.

Чтобы в дальнейшем работать гранулярно с данными о безопасности, загруженными в Grail, агрегированные отчёты должны быть разбиты и загружены как отдельные находки.

В данном случае события были изменены перед загрузкой, чтобы включить только один образ контейнера, одну уязвимость и одну уязвимую библиотеку.

Пример загруженного события с одной находкой об уязвимости

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

3. Проверка данных в Notebooks

Для проверки данных откройте [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь результатами из ваших данных наблюдаемости.") и выполните запрос событий безопасности.

Пример DQL-запроса:

Этот запрос был обновлён в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и необходимых действий для миграции см. в [руководстве по миграции таблицы безопасности Grail](/docs/secure/threat-observability/migration "Изучите изменения в новой таблице безопасности Grail и узнайте, как выполнить миграцию.").

```
fetch security.events



| filter dt.system.bucket == "default_securityevents"



| sort timestamp desc
```

Чтобы чётко отличить загруженные данные от других загруженных событий, вы можете добавить фильтры для ожидаемых атрибутов.

Пример:

```
| filter SchemaVersion == 2 AND ArtifactType == "container_image"
```

Результат запроса должен включать загруженное событие в исходном формате с несколькими обогащёнными полями, такими как `timestamp` и `event.kind`.

Пример результата запроса

```
{



// обогащённые поля



"timestamp": "2024-08-02T14:38:53.854000000Z",



"event.kind": "SECURITY_EVENT",



// исходные поля



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

В текущем случае формат не поддерживается и данные не сопоставлены. Если Dynatrace поддерживает формат, он автоматически сопоставляет его с [конвенциями Semantic Dictionary](https://dt-url.net/3q03pb0).

4. Сопоставление данных с Dynatrace Semantic Dictionary

В простых случаях вы можете работать с загруженными событиями в исходном формате. Однако в более сложных случаях это затруднительно, поскольку:

* Есть много вложенных полей
* Нет возможности единообразно получать доступ к данным из различных инструментов и продуктов
* Некоторые поля добавляются для правильной классификации данных, а другие сопоставляются с конвенциями

В таких сложных случаях необходимо вручную сопоставить загруженные данные с Dynatrace Semantic Dictionary. При сопоставлении данных исходные данные сохраняются вместе с сопоставленными, что позволяет использовать специфичные для поставщика данные в анализе и автоматизации или в качестве дополнительного контекста.

1. В **OpenPipeline** выберите **Pipelines** > **Pipeline** для [создания пользовательского конвейера](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#process "Настройка источников загрузки, маршрутов и обработки данных в OpenPipeline.") и назовите его, например, "Custom security findings".
2. Добавьте [процессор](/docs/platform/openpipeline/concepts/processing#processor "Изучите основные концепции обработки Dynatrace OpenPipeline.") типа **DQL** в ваш конвейер и настройте его для разбора полей, необходимых [Semantic Dictionary](https://dt-url.net/3q03pb0) (в нашем случае мы хотим сопоставить основные поля находок уязвимостей и, в качестве расширения, данные образа контейнера). Введите следующие данные:

   * Имя процессора: Например, "Map Trivy fields"
   * Условие соответствия: `SchemaVersion == 2 AND ArtifactType == "container_image"` (таким образом, сопоставление будет выполняться только для соответствующих событий)
   * Определение DQL-процессора (при сопоставлении предполагается, что массивы результатов и уязвимостей уже содержат отдельные элементы):

   Пример определения DQL-процессора

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

   Пример сопоставленного результата

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



   "ArtifactType": "container_image"
   ```
3. Выберите **Dynamic routing** > **Dynamic route** для [добавления динамической маршрутизации](/docs/platform/openpipeline/getting-started/tutorial-configure-processing#route "Настройка источников загрузки, маршрутов и обработки данных в OpenPipeline.") к новому конвейеру. Введите следующие данные:

   * Имя динамического маршрута: Например, "Custom event"
   * Условие соответствия: `SchemaVersion == 2 AND ArtifactType == "container_image"`
   * Выберите конвейер, к которому будет применяться динамическая маршрутизация (в нашем случае — `Custom security findings`)

   ![add dynamic routing](https://dt-cdn.net/images/2024-08-28-23-04-46-576-9e042f6845.png)

   Подробнее о динамической маршрутизации см. [Маршрутизация](/docs/platform/openpipeline/concepts/data-flow#routing "Изучите поток данных в Dynatrace Platform.").

## Дальнейшие шаги

Теперь вы можете использовать данные для:

* [Визуализации находок уязвимостей контейнеров с помощью примерного дашборда](/docs/secure/use-cases/visualize-and-analyze-security-findings "Визуализация, приоритизация и анализ загруженных данных о безопасности.")
* [Автоматизации создания тикетов Jira и уведомлений Slack с помощью примерных рабочих процессов](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Регулярная проверка критических данных о безопасности и автоматические тикеты Jira или оповещения Slack.")
