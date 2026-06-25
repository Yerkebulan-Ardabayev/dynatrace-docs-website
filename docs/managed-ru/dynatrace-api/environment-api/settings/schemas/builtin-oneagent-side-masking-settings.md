---
title: Settings API - OneAgent side masking schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-oneagent-side-masking-settings
scraped: 2026-05-12T11:47:16.311990
---

# Settings API - OneAgent side masking schema table

# Settings API - OneAgent side masking schema table

* Published Feb 26, 2024

### Маскирование на стороне OneAgent (`builtin:oneagent.side.masking.settings)`

Используйте параметры на этой странице, чтобы исключить чувствительные данные из исключений и URL, захватываемых напрямую OneAgent, так чтобы они не покидали окружение. Параметры ниже выполняются непосредственно на OneAgent и исключают точки данных из отправки на серверы Dynatrace. Эти точки данных больше не будут доступны в Dynatrace.

Примечание: RUM JavaScript эти параметры **не** затрагивают!

Подробный справочник и журнал изменений см. [here](https://dt-url.net/kd039dm).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:oneagent.side.masking.settings` | * `group:preferences` * `group:privacy-settings` | `PROCESS_GROUP` - Process Group  `CLOUD_APPLICATION` - Kubernetes workload  `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.side.masking.settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:oneagent.side.masking.settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:oneagent.side.masking.settings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Email-адреса `isEmailMaskingEnabled` | boolean | Исключить email-адреса из URL и исключений.  Включает маскирование email и пользовательских данных в URL и исключениях.  Примеры: https://the-internet.com/mail/admin@the-internet.com/newItems -> https://the-internet.com/mail//newItems (`<your-dynatrace-url>/`)  ftp://user:hunter2@domain.com -> ftp://@domain.com (`<your-dynatrace-url>/`) (Домен не маскируется, так как распознан как часть authority.) | Required |
| Параметры запроса `isQueryMaskingEnabled` | boolean | Исключить параметры запроса из URL и web-запросов.  Включает маскирование значений параметров запроса в URL.  Пример: **?key1=value1&key2=value2** -> **?key1=&key2=**. | Required |
| Финансовые номера и номера платёжных карт `isFinancialMaskingEnabled` | boolean | Исключить IBAN и номера платёжных карт из URL и исключений.  Включает маскирование строк (чисел), похожих на IBAN и номера платёжных карт.  Пример: https://the-internet.com/CC/1234 4321 5678 8756/test (`<your-dynatrace-url>/`) -> https://the-internet.com/CC//test (`<your-dynatrace-url>/`) | Required |
| ID и числа `isNumbersMaskingEnabled` | boolean | Исключить шестнадцатеричные ID и последовательные числа длиной более 5 цифр из URL и исключений.  Между цифрами числа могут содержать символы **-**, **.**, **:**, ' '(пробел), они не учитываются. Максимальное значение: 255.  Пример: https://the-internet.com/IP/123:12:32:65 -> https://the-internet.com/IP/ (`<your-dynatrace-url>/`) | Required |