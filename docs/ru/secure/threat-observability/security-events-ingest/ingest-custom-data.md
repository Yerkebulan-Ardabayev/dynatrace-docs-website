---
title: Прием пользовательских событий безопасности через API
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-custom-data
scraped: 2026-03-06T21:24:11.399509
---

# Загрузка пользовательских событий безопасности через API


* Latest Dynatrace

Эта страница обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и необходимых действий для выполнения миграции описан в [руководстве по миграции таблицы безопасности Grail](../migration.md "Understand the changes in the new Grail security table and learn how to migrate to it.").

Загрузка событий безопасности от пользовательских сторонних продуктов через API.

## Начало работы

### Обзор

Далее вы узнаете, как загружать внешние события безопасности от пользовательских сторонних продуктов в [Grail](../../../platform/grail.md "Insights on what and how you can query Dynatrace data."), чтобы получать аналитику Dynatrace по результатам поиска уязвимостей из любого источника, поставщика или формата.

**Пользовательский сторонний продукт** — это любой продукт, для которого Dynatrace не предоставляет готовую интеграцию.

### Сценарии использования

С загруженными данными вы можете реализовать различные сценарии использования, такие как

* [Генерация событий безопасности из приложения Dynatrace Investigations через OpenPipeline](https://dt-url.net/r703qjx)
* [Загрузка и обработка пользовательских результатов сканирования безопасности](../../use-cases/ingest-and-process-custom-security-findings.md "Continuously ingest your container scan findings.")
* [Автоматизация и оркестрация результатов сканирования безопасности](../../use-cases/automate-and-orchestrate-security-findings.md "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")
* [Визуализация и анализ результатов сканирования безопасности](../../use-cases/visualize-and-analyze-security-findings.md "Visualize, prioritize, and analyze ingested security findings.")

### Требования

Для запроса загруженных данных вам необходимо разрешение `storage:security.events:read`.

## Активация и настройка

Для начала загрузки данных используйте один из вариантов ниже.

Встроенная конечная точка API

Пользовательская конечная точка API

Подробности о том, как выполнить загрузку через API, см. в разделе [Подробнее](https://dt-url.net/1r03q9s).

## Подробности

### Как это работает

Вы загружаете данные в Grail через [встроенную конечную точку API](#default) или [пользовательскую конечную точку API](#custom). Затем, в зависимости от выбранного варианта загрузки, вы можете либо анализировать данные в вашем формате, либо вручную сопоставить данные с [соглашениями Semantic Dictionary](https://dt-url.net/3q03pb0).

### Коды ответа

| Код | Описание |
| --- | --- |
| 202 | Принято |
| 400 | Неверный запрос (в случае отсутствия тела или неверного формата) |
| 401 | Не авторизован (в случае отсутствия или недействительного токена) |

### Примеры

Пример JSON

```
[


{


"imageId": {


"imageDigest": "sha256:9282579f5330ae90d22f21b1a9be944f893895f06e3bc1985f14d1cfc084c60c"


},


"imageScanFindings": {


"findingSeverityCounts": {


"HIGH": 125,


"MEDIUM": 188,


"LOW": 30,


"UNDEFINED": 13,


"INFORMATIONAL": 353,


"CRITICAL": 6


},


"findings": [


{


"attributes": [


{ "key": "CVSS3_SCORE", "value": "9.8" },


{ "key": "package_version", "value": "4.19.269-1" },


{ "key": "package_name", "value": "linux" },


{


"key": "CVSS3_VECTOR",


"value": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"


}


],


"description": "An issue was discovered in drivers/net/ethernet/intel/igb/igb_main.c in the IGB driver in the Linux kernel before 6.5.3. A buffer size may not be adequate for frames larger than the MTU.",


"name": "CVE-2023-45871",


"severity": "CRITICAL",


"uri": "https://security-tracker.debian.org/tracker/CVE-2023-45871 "


},


{


"attributes": [


{ "key": "CVSS3_SCORE", "value": "9.8" },


{ "key": "package_version", "value": "1:7.9p1-10+deb10u2" },


{ "key": "package_name", "value": "openssh" },


{


"key": "CVSS3_VECTOR",


"value": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"


}


],


"description": "The PKCS#11 feature in ssh-agent in OpenSSH before 9.3p2 has an insufficiently trustworthy search path, leading to remote code execution if an agent is forwarded to an attacker-controlled system. (Code in /usr/lib is not necessarily safe for loading into ssh-agent.) NOTE: this issue exists because of an incomplete fix for CVE-2016-10009.",


"name": "CVE-2023-38408",


"severity": "CRITICAL",


"uri": "https://security-tracker.debian.org/tracker/CVE-2023-38408 "


},


{


"attributes": [


{ "key": "CVSS3_SCORE", "value": "9.8" },


{ "key": "package_version", "value": "2.7.16-2+deb10u1" },


{ "key": "package_name", "value": "python2.7" },


{


"key": "CVSS3_VECTOR",


"value": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"


}


],


"description": "An XML External Entity (XXE) issue was discovered in Python through 3.9.1. The plistlib module no longer accepts entity declarations in XML plist files to avoid XML vulnerabilities.",


"name": "CVE-2022-48565",


"severity": "CRITICAL",


"uri": "https://security-tracker.debian.org/tracker/CVE-2022-48565 "


},


{


"attributes": [


{ "key": "CVSS3_SCORE", "value": "9.8" },


{ "key": "package_version", "value": "2.7.16-2+deb10u1" },


{ "key": "package_name", "value": "python2.7" },


{


"key": "CVSS3_VECTOR",


"value": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"


},


{ "key": "CVSS2_VECTOR", "value": "AV:N/AC:L/Au:N/C:P/I:P/A:P" },


{ "key": "CVSS2_SCORE", "value": "7.5" }


],


"description": "Python 3.x through 3.9.1 has a buffer overflow in PyCArg_repr in _ctypes/callproc.c, which may lead to remote code execution in certain Python applications that accept floating-point numbers as untrusted input, as demonstrated by a 1e300 argument to c_double.from_param. This occurs because sprintf is used unsafely.",


"name": "CVE-2021-3177",


"severity": "CRITICAL",


"uri": "https://security-tracker.debian.org/tracker/CVE-2021-3177 "


}


],


"imageScanCompletedAt": 1698376478,


"vulnerabilitySourceUpdatedAt": 1698343825


},


"imageScanStatus": {


"description": "The scan was completed successfully.",


"status": "COMPLETE"


},


"nextToken": "ukD72mdD/mC8b5xV3susmJzzaTgp3hKwR9nRUW1yZZ63B5NL+m8CiI+qgoiLO0t5s6Oi9w2CQBANPaxpQTFWXxF/Sq7shr/h//oNXvOJ2XuWPSF3ox6DgxQztXUFyKzeGw+HpbYZAAxpHjJVELVXXnhpxAScZkKhVG85CbbUGfSPyuKcSeeHoNvQPGBdxCWD6CaKl4nFxtXyUeFRs3RV+mkX5FUxosMnBJepE2JbaoM9elE1niY2Rpq3BZrp/QeOyWdmjeuySi+2KZO03915df+6OMIfXtt3zclPZ+BGcdMgWoETrte2fkh2y1RDO3PI4OCohgCbjlTk9X6fYLWrrxwkhfWAIRekqToQq+S8BHEm1o82jxDoyKO0Et9UrZVIEFOofBkvenm5U+8XvgQ4V5kvMZZLa9DZykVDteq28OF+KCgjo7WHTbXMy1yh7jyRJ6A77N12YJfxYgv16JjkVgmDqGjlM3YJEH2o55SYTAnSsiBXiMvvq1RK1hl567SIstgGPMK3c0v7TGDnCE6o3EhP4FC73As6mj2q4uGkLf8eMQLi9ogBJ1UAzKCiCl3bxeTKuMz1W8hokdPauwuAd9uKg0vLdHmM6iftfrVhsgbbioNLy3R5jOon7X61YbIGF7fUOkaj72o37fpPd/JG2g==",


"registryId": "123456789876",


"repositoryName": "unguard-frontend"


}


]
```

Пример конечного результата в Grail

Встроенная конечная точка API

Пользовательская конечная точка API

```
[


{


"timestamp": "2024-06-17T14:58:36.820000000+02:00",


"dt.ingest.source": "/platform/ingest/v1/security.events/",


"event.kind": "SECURITY_EVENT",


"imageId": "{\"imageDigest\":\"sha256:9282579f5330ae90d22f21b1a9be944f893895f06e3bc1985f14d1cfc084c60c\"}",


"imageScanFindings": "{\"findingSeverityCounts\":{\"HIGH\":125,\"MEDIUM\":188,\"LOW\":30,\"UNDEFINED\":13,\"INFORMATIONAL\":353,\"CRITICAL\":6},\"findings\":[{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"4.19.269-1\"},{\"key\":\"package_name\",\"value\":\"linux\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"An issue was discovered in drivers/net/ethernet/intel/igb/igb_main.c in the IGB driver in the Linux kernel before 6.5.3. A buffer size may not be adequate for frames larger than the MTU.\",\"name\":\"CVE-2023-45871\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2023-45871 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"1:7.9p1-10+deb10u2\"},{\"key\":\"package_name\",\"value\":\"openssh\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"The PKCS#11 feature in ssh-agent in OpenSSH before 9.3p2 has an insufficiently trustworthy search path, leading to remote code execution if an agent is forwarded to an attacker-controlled system. (Code in /usr/lib is not necessarily safe for loading into ssh-agent.) NOTE: this issue exists because of an incomplete fix for CVE-2016-10009.\",\"name\":\"CVE-2023-38408\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2023-38408 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"2.7.16-2+deb10u1\"},{\"key\":\"package_name\",\"value\":\"python2.7\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"An XML External Entity (XXE) issue was discovered in Python through 3.9.1. The plistlib module no longer accepts entity declarations in XML plist files to avoid XML vulnerabilities.\",\"name\":\"CVE-2022-48565\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2022-48565 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"2.7.16-2+deb10u1\"},{\"key\":\"package_name\",\"value\":\"python2.7\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"},{\"key\":\"CVSS2_VECTOR\",\"value\":\"AV:N/AC:L/Au:N/C:P/I:P/A:P\"},{\"key\":\"CVSS2_SCORE\",\"value\":\"7.5\"}],\"description\":\"Python 3.x through 3.9.1 has a buffer overflow in PyCArg_repr in _ctypes/callproc.c, which may lead to remote code execution in certain Python applications that accept floating-point numbers as untrusted input, as demonstrated by a 1e300 argument to c_double.from_param. This occurs because sprintf is used unsafely.\",\"name\":\"CVE-2021-3177\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2021-3177 \"}],\"imageScanCompletedAt\":1698376478,\"vulnerabilitySourceUpdatedAt\":1698343825}",


"imageScanStatus": "{\"description\":\"The scan was completed successfully.\",\"status\":\"COMPLETE\"}",


"nextToken": "ukD72mdD/mC8b5xV3susmJzzaTgp3hKwR9nRUW1yZZ63B5NL+m8CiI+qgoiLO0t5s6Oi9w2CQBANPaxpQTFWXxF/Sq7shr/h//oNXvOJ2XuWPSF3ox6DgxQztXUFyKzeGw+HpbYZAAxpHjJVELVXXnhpxAScZkKhVG85CbbUGfSPyuKcSeeHoNvQPGBdxCWD6CaKl4nFxtXyUeFRs3RV+mkX5FUxosMnBJepE2JbaoM9elE1niY2Rpq3BZrp/QeOyWdmjeuySi+2KZO03915df+6OMIfXtt3zclPZ+BGcdMgWoETrte2fkh2y1RDO3PI4OCohgCbjlTk9X6fYLWrrxwkhfWAIRekqToQq+S8BHEm1o82jxDoyKO0Et9UrZVIEFOofBkvenm5U+8XvgQ4V5kvMZZLa9DZykVDteq28OF+KCgjo7WHTbXMy1yh7jyRJ6A77N12YJfxYgv16JjkVgmDqGjlM3YJEH2o55SYTAnSsiBXiMvvq1RK1hl567SIstgGPMK3c0v7TGDnCE6o3EhP4FC73As6mj2q4uGkLf8eMQLi9ogBJ1UAzKCiCl3bxeTKuMz1W8hokdPauwuAd9uKg0vLdHmM6iftfrVhsgbbioNLy3R5jOon7X61YbIGF7fUOkaj72o37fpPd/JG2g==",


"registryId": "123456789876",


"repositoryName": "unguard-frontend"


}


]
```

```
{


"timestamp": "2024-06-17T14:58:36.820000000+02:00",


"dt.ingest.source": "/platform/ingest/v1/security.events/",


"imageId": "{\"imageDigest\":\"sha256:9282579f5330ae90d22f21b1a9be944f893895f06e3bc1985f14d1cfc084c60c\"}",


"imageScanFindings": "{\"findingSeverityCounts\":{\"HIGH\":125,\"MEDIUM\":188,\"LOW\":30,\"UNDEFINED\":13,\"INFORMATIONAL\":353,\"CRITICAL\":6},\"findings\":[{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"4.19.269-1\"},{\"key\":\"package_name\",\"value\":\"linux\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"An issue was discovered in drivers/net/ethernet/intel/igb/igb_main.c in the IGB driver in the Linux kernel before 6.5.3. A buffer size may not be adequate for frames larger than the MTU.\",\"name\":\"CVE-2023-45871\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2023-45871 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"1:7.9p1-10+deb10u2\"},{\"key\":\"package_name\",\"value\":\"openssh\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"The PKCS#11 feature in ssh-agent in OpenSSH before 9.3p2 has an insufficiently trustworthy search path, leading to remote code execution if an agent is forwarded to an attacker-controlled system. (Code in /usr/lib is not necessarily safe for loading into ssh-agent.) NOTE: this issue exists because of an incomplete fix for CVE-2016-10009.\",\"name\":\"CVE-2023-38408\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2023-38408 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"2.7.16-2+deb10u1\"},{\"key\":\"package_name\",\"value\":\"python2.7\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"An XML External Entity (XXE) issue was discovered in Python through 3.9.1. The plistlib module no longer accepts entity declarations in XML plist files to avoid XML vulnerabilities.\",\"name\":\"CVE-2022-48565\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2022-48565 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"2.7.16-2+deb10u1\"},{\"key\":\"package_name\",\"value\":\"python2.7\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"},{\"key\":\"CVSS2_VECTOR\",\"value\":\"AV:N/AC:L/Au:N/C:P/I:P/A:P\"},{\"key\":\"CVSS2_SCORE\",\"value\":\"7.5\"}],\"description\":\"Python 3.x through 3.9.1 has a buffer overflow in PyCArg_repr in _ctypes/callproc.c, which may lead to remote code execution in certain Python applications that accept floating-point numbers as untrusted input, as demonstrated by a 1e300 argument to c_double.from_param. This occurs because sprintf is used unsafely.\",\"name\":\"CVE-2021-3177\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2021-3177 \"}],\"imageScanCompletedAt\":1698376478,\"vulnerabilitySourceUpdatedAt\":1698343825}",


"imageScanStatus": "{\"description\":\"The scan was completed successfully.\",\"status\":\"COMPLETE\"}",


"nextToken": "ukD72mdD/mC8b5xV3susmJzzaTgp3hKwR9nRUW1yZZ63B5NL+m8CiI+qgoiLO0t5s6Oi9w2CQBANPaxpQTFWXxF/Sq7shr/h//oNXvOJ2XuWPSF3ox6DgxQztXUFyKzeGw+HpbYZAAxpHjJVELVXXnhpxAScZkKhVG85CbbUGfSPyuKcSeeHoNvQPGBdxCWD6CaKl4nFxtXyUeFRs3RV+mkX5FUxosMnBJepE2JbaoM9elE1niY2Rpq3BZrp/QeOyWdmjeuySi+2KZO03915df+6OMIfXtt3zclPZ+BGcdMgWoETrte2fkh2y1RDO3PI4OCohgCbjlTk9X6fYLWrrxwkhfWAIRekqToQq+S8BHEm1o82jxDoyKO0Et9UrZVIEFOofBkvenm5U+8XvgQ4V5kvMZZLa9DZykVDteq28OF+KCgjo7WHTbXMy1yh7jyRJ6A77N12YJfxYgv16JjkVgmDqGjlM3YJEH2o55SYTAnSsiBXiMvvq1RK1hl567SIstgGPMK3c0v7TGDnCE6o3EhP4FC73As6mj2q4uGkLf8eMQLi9ogBJ1UAzKCiCl3bxeTKuMz1W8hokdPauwuAd9uKg0vLdHmM6iftfrVhsgbbioNLy3R5jOon7X61YbIGF7fUOkaj72o37fpPd/JG2g==",


"registryId": "123456789876",


"repositoryName": "unguard-frontend"


}
```

### Лицензирование и стоимость

Информацию о биллинге см. в разделе [События на базе Grail](../../../license/capabilities/events.md "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## Связанные темы

* [OpenPipeline](../../../platform/openpipeline.md "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](../../../platform/grail/dynatrace-query-language.md "How to use Dynatrace Query Language.")
* [События безопасности](../../../semantic-dictionary/model/security-events.md "Get to know the Semantic Dictionary models related to security events.")
* [OpenPipeline Ingest API — POST Пользовательская конечная точка событий безопасности (новая)](../../../platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-custom-endpoint.md "Configure a custom security event endpoint via OpenPipeline Ingest API.")
* [OpenPipeline Ingest API — POST Встроенные события безопасности (новая)](../../../platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-builtin.md "Ingest security events from built-in endpoints via OpenPipeline Ingest API.")