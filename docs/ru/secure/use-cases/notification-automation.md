---
title: Автоматизация уведомлений CSPM
source: https://www.dynatrace.com/docs/secure/use-cases/notification-automation
scraped: 2026-03-06T21:15:00.738663
---

# Автоматизация уведомлений CSPM

# Автоматизация уведомлений CSPM

* Latest Dynatrace
* Руководство
* Обновлено 31 января 2024

Early Adopter

Гиперскейлеры предоставляют такие решения, как [AWS Security Hub](https://dt-url.net/5l239zz), через которые события, связанные с безопасностью, дают представление о потенциальных угрозах. Эти события должны быть отсортированы, проанализированы и устранены владельцами затронутых ресурсов, и объём таких оповещений обычно достигает сотен тысяч.

* Объём этих событий в настоящее время означает, что не все из них могут получить должное внимание.
* Поскольку ответственность за ресурсы распределена, требуются значительные усилия по координации и администрированию, чтобы обеспечить реагирование на все события.

Dynatrace решает эти проблемы и улучшает управление состоянием облачной безопасности (CSPM), внедряя рабочий процесс автоматизации, который фильтрует результаты проверок безопасности, хранящиеся в Grail, и инициирует оповещения только для значимых событий.

## Целевая аудитория

Эта страница предназначена для команд безопасности, анализирующих результаты проверок безопасности.

## Сценарий

Далее мы рассмотрим сценарий, в котором ежедневно выдаётся 400 000 оповещений AWS.

Ручная обработка всех оповещений просто невозможна. Поэтому команда безопасности должна сосредоточиться только на высокоприоритетных событиях и создала собственные инструменты для частичной автоматизации создания тикетов в Jira.

* За год было вручную создано почти 1 100 тикетов безопасности из этих событий.
* Расследование этих тикетов потребовало участия около 300 человек для сбора дополнительной информации и анализа ситуации.

Иногда усилия тратятся впустую, и оповещения оказываются нерелевантными, но владелец ресурса всегда должен перепроверить решение с командой безопасности. Обеспечение реагирования на все оповещения требует значительных координационных усилий, оставляя меньше времени для фактической работы по обеспечению безопасности.

### Запрос

* Команда хочет иметь возможность исследовать все данные, но получать уведомления (тикеты) только для критических или высокоприоритетных событий и только для определённых релевантных учётных записей AWS.
* Уведомления должны включать тип оповещения, полный контекст, релевантные детали и рекомендации по устранению для обеспечения понимания, возможности действия и операционализации.
* Только владелец учётной записи должен быть проинформирован о проблеме (тикеты должны автоматически назначаться ему).
* Команда не хочет получать множество уведомлений по одной и той же проблеме, поэтому дублирующих тикетов быть не должно.

### Цель

**Эффективность**: Команда должна иметь возможность немедленно реагировать на всё, что имеет значение.

### Результат

**Автоматизация уведомлений Dynatrace CSPM** — это инструмент, предназначенный для решения проблем команды безопасности и значительного повышения её эффективности. Он позволяет команде продолжать мониторинг событий, не перегружаясь оповещениями; теперь они могут сосредоточиться только на том, что действительно важно и требует их экспертизы в области безопасности.

Более конкретно, из общего количества 400 000 оповещений в день, из которых только 40 000 являются релевантными, с помощью автоматизации уведомлений Dynatrace CSPM ежедневно создаётся лишь несколько тикетов Jira — только для значимых проблем.

## Как это работает

Автоматизация уведомлений Dynatrace CSPM состоит из двух этапов.

1. (Предварительное условие) Результаты проверок безопасности AWS из [AWS Security Hub](https://dt-url.net/5l239zz)
   загружаются в [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") посредством [загрузки логов Dynatrace](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding#aws-log-forwarding "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.").
2. (Собственно автоматизация) Предопределённый [рабочий процесс](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") оркестрирует процессы запросов, фильтрации и группировки данных и преобразует полученные результаты в тикеты Jira для устранения. См. раздел [Начало работы](#start) для описания шагов рабочего процесса.

![Как работает автоматизация CSPM](https://dt-cdn.net/images/2024-01-31-15-04-14-470-834fcfc1a2.png)

## Предварительные требования

Ниже описаны требования для [AWS](#aws) и [Dynatrace](#dt).

### Требования AWS

* [Настройте учётные записи AWS](https://dt-url.net/ng439wv), для которых вы хотите получать уведомления.
* [Настройте AWS Security Hub](https://dt-url.net/uh639rl) (собирает результаты проверок безопасности AWS).

### Требования Dynatrace

* Dynatrace версии 1.276+
* [Настройте загрузку логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-cloud-provider-log-forwarding#aws-log-forwarding "Configure AWS, Azure and Google Cloud log forwarding to stream log data to Dynatrace using API.") (загружает результаты проверок безопасности AWS в Grail).
* [Настройте Jira Connector](/docs/analyze-explore-automate/workflows/actions/jira#setup "Automate creating, transitioning, commenting, and assigning Jira issues on the events and schedules defined for your workflows.") (позволяет рабочему процессу преобразовывать результаты в тикеты Jira).
* Убедитесь, что включены следующие разрешения.

  + **Grail**: `storage:logs:read`. Инструкции см. в разделе [Назначение разрешений в Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").
  + ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**: Разрешения на доступ, просмотр, запись и выполнение рабочих процессов. Подробности см. в разделе [Авторизация](/docs/analyze-explore-automate/workflows#authorization "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

    Для доступа к разрешениям перейдите в меню **Settings** в правом верхнем углу ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** и выберите **Authorization settings**.

## Начало работы

После загрузки результатов проверок безопасности AWS в Grail (см. [Предварительные требования](#prerequisites)) вы можете настроить рабочий процесс автоматизации уведомлений CSPM.

Рабочий процесс состоит из нескольких шагов, которые вы можете адаптировать в соответствии с вашими потребностями. Для настройки вы можете начать с импорта предварительно заполненного рабочего процесса в вашу среду.

1. Импорт рабочего процесса

1. Скопируйте и сохраните JSON-файл ниже.

   ```
   {



   "id": "dcce961d-26a9-46e6-a9e4-14a0f7f2185c",



   "title": "CSPM Notification Automation",



   "description": "",



   "tasks": {



   "count_all_new_findings": {



   "name": "count_all_new_findings",



   "description": "Executes query to count all recently created AWS findings",



   "action": "dynatrace.automations:execute-dql-query",



   "active": true,



   "input": {



   "query": "fetch logs, from:now() - 24h, scanLimitGBytes: -1\n| filter aws.log_group == \"/aws/events/AWSSecurityHubLogGroup\"\n| fields timestamp\n| filter timestamp > now() - 24h                                                                        // Only filter created since last successful run         \n| summarize { count=count() }"



   },



   "position": {



   "x": -1,



   "y": 2



   },



   "predecessors": [



   "workflow_config_params"



   ],



   "conditions": {



   "states": {



   "workflow_config_params": "OK"



   }



   }



   },



   "log_new_findings_count": {



   "name": "log_new_findings_count",



   "description": "Logs total number of recently created AWS findings",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function () {\n\n  const ex = await execution();\n  const countResult = await ex.result(\"count_all_new_findings\");\n\n  console.log('======================================================================')\n  console.log('Total findings added since last run: ')\n  console.log(countResult.records[0].count)\n  console.log('')\n}"



   },



   "position": {



   "x": -1,



   "y": 3



   },



   "predecessors": [



   "count_all_new_findings"



   ],



   "conditions": {



   "states": {



   "count_all_new_findings": "OK"



   }



   }



   },



   "log_tickets_by_account": {



   "name": "log_tickets_by_account",



   "description": "Logs potentially created Jira issues for findings by account",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function () {\n  const ex = await execution();\n  const by_control_id = await ex.result(\"fetch_findings_by_account\");\n\n  console.log('=================================================================================================')\n  console.log(`Issues by accounts, ${by_control_id.records.length} findings`)\n  console.log('=================================================================================================')\n\n  for(let finding of by_control_id.records) {\n    console.log('')\n    console.log('=================================================================================================')\n    console.log(`Automatic Vulnerability Report for ${finding.controlId} - AWS account ${finding.awsAccountId}`)\n    console.log('=================================================================================================')\n    console.log('')\n    console.log('The following vulnerabilities were reported for your account via AWS Security Hub.')\n    console.log('')\n    console.log(`AWS Account: ${finding.awsAccountId}`)\n    console.log('')\n    console.log('Vulnerability:')\n    console.log(`${finding.controlId} - ${finding.title}`)\n    console.log(finding.severity)\n    console.log(finding.description)\n    console.log(finding.remediation[0].Recommendation.Url)\n    console.log('')\n    console.log('Affected resources:')\n    for(let resource of finding.resources) {\n      console.log(resource)\n    }\n    console.log('')          \n    console.log('=================================================================================================')\n    console.log('')\n    console.log('')\n  }\n  \n  return by_control_id.records;\n}"



   },



   "position": {



   "x": 0,



   "y": 3



   },



   "predecessors": [



   "fetch_findings_by_account"



   ],



   "conditions": {



   "states": {



   "fetch_findings_by_account": "OK"



   }



   }



   },



   "workflow_config_params": {



   "name": "workflow_config_params",



   "description": "Sets configuration parameters for the workflow run",



   "action": "dynatrace.automations:run-javascript",



   "input": {



   "script": "// This step sets up some configurational parameters for the workflow run \n// (e.g. which accounts, which finding types we are filtering for)\nexport default async function () {\n\n  // AWS accounts to filter for\n  const awsAccountIds = [\n    // add your AWS account ids here, e.g.\n    // \"1234567890\"\n  ]\n\n  // Findings that should be grouped by AWS account\n  const securityControlIdsToGroupByAccount = [\n    // add you control IDs here, e.g.\n    // \"S3.1\" // S3 Block Public Access setting should be enabled\n  ]\n\n  // Findings that should be grouped by AWS Resource\n  const securityControlIdsToGroupByResource = [\n    // add you control IDs here, e.g.\n    // \"EC2.13\" // Security groups should not allow ingress from 0.0.0.0/0 to port 22\n  ]\n  \n  return { awsAccountIds, securityControlIdsToGroupByAccount, securityControlIdsToGroupByResource }\n}"



   },



   "position": {



   "x": 0,



   "y": 1



   },



   "predecessors": []



   },



   "log_tickets_by_resource": {



   "name": "log_tickets_by_resource",



   "description": "Logs potentially created Jira issues for findings by resource",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function () {\n  const ex = await execution();\n  const by_resource = await ex.result(\"fetch_findings_by_resource\");\n\n  console.log('=================================================================================================')\n  console.log(`Issues by resource, ${by_resource.records.length} findings`)\n  console.log('=================================================================================================')\n\n  for(let finding of by_resource.records) {\n    console.log('')\n    console.log('=================================================================================================')\n    console.log(`Automatic Vulnerability Report for ${finding.resource.resourceId}`)\n    console.log('=================================================================================================')\n    console.log('')\n    console.log('The following vulnerabilities were reported for your resource via AWS Security Hub.')\n    console.log('')\n    console.log(`AWS Account: ${finding.aws.accountId}`)\n    console.log('')\n    console.log('Resource details:')\n    console.log(finding.resource.resourceType)\n    console.log(finding.resource.resourceId)\n    console.log('')\n    console.log('Vulnerabilities:')\n    for(let vulnerability of finding.vulnerabilities) {\n      console.log(`${vulnerability.controlId} - ${vulnerability.title}`)\n      console.log(vulnerability.severity)\n      console.log(vulnerability.description)\n      console.log(vulnerability.remediation[0].Recommendation.Url)      \n    }\n    console.log('=================================================================================================')\n    console.log('')\n    console.log('')\n  }\n  \n  return by_resource.records;\n}"



   },



   "position": {



   "x": 1,



   "y": 3



   },



   "predecessors": [



   "fetch_findings_by_resource"



   ],



   "conditions": {



   "states": {



   "fetch_findings_by_resource": "OK"



   }



   }



   },



   "create_issue_for_account": {



   "name": "create_issue_for_account",



   "description": "Creates new Jira issue or the vulnerable AWS account",



   "action": "dynatrace.jira:jira-create-issue",



   "active": false,



   "input": {



   "labels": [],



   "summary": "{{ _.item.summary }}",



   "components": [],



   "description": "{{ _.item.description }}",



   "fieldSetters": []



   },



   "position": {



   "x": 0,



   "y": 5



   },



   "predecessors": [



   "prepare_tickets_by_account"



   ],



   "conditions": {



   "states": {



   "prepare_tickets_by_account": "OK"



   }



   },



   "concurrency": 1,



   "withItems": "item in {{result(\"prepare_tickets_by_account\")}}"



   },



   "create_issue_for_resource": {



   "name": "create_issue_for_resource",



   "description": "Creates new issue for the vulnerable AWS resource",



   "action": "dynatrace.jira:jira-create-issue",



   "active": false,



   "input": {



   "labels": [],



   "summary": "{{ _.item.summary }}",



   "components": [],



   "description": "{{ _.item.description }}",



   "fieldSetters": []



   },



   "position": {



   "x": 1,



   "y": 5



   },



   "predecessors": [



   "prepare_tickets_by_resource"



   ],



   "conditions": {



   "states": {



   "prepare_tickets_by_resource": "OK"



   }



   },



   "concurrency": 1,



   "withItems": "item in {{result(\"prepare_tickets_by_resource\")}}"



   },



   "fetch_findings_by_account": {



   "name": "fetch_findings_by_account",



   "description": "Executes query to get relevant security findings grouped by AWS account",



   "action": "dynatrace.automations:execute-dql-query",



   "active": true,



   "input": {



   "query": "fetch logs, from:now() - 24h, scanLimitGBytes: -1\n| filter aws.log_group == \"/aws/events/AWSSecurityHubLogGroup\"\n| parse content, \"JSON:alert\"\n| fields timestamp,\n         awsRegion = toString(alert[detail][findings][0][Region]),\n         awsAccountId = toString(alert[detail][findings][0][AwsAccountId]),\n         resourceType = toString(alert[detail][findings][0][Resources][0][Type]),          \n         resource = toString(alert[detail][findings][0][Resources][0][Id]),\n         alertType = toString(alert[detail][findings][0][Types][0]),\n         id = toString(alert[detail][findings][0][Id]),\n         severity = toString(alert[detail][findings][0][FindingProviderFields][Severity][Label]),\n         title = toString(alert[detail][findings][0][Title]),\n         description = toString(alert[detail][findings][0][Description]),\n         complianceStatus = toString(alert[detail][findings][0][Compliance][Status]),\n         controlId = toString(alert[detail][findings][0][Compliance][SecurityControlId]),\n         remediation = alert[detail][findings][0][Remediation],\n         created = toTimestamp(alert[detail][findings][0][CreatedAt]),\n         lastObservedAt = toTimestamp(alert[detail][findings][0][LastObservedAt])\n| filter in(severity, array(\"HIGH\", \"CRITICAL\", \"MEDIUM\"))\n| filter created > now() - 24h\n| filter in(awsAccountId, array(\"{{ result('workflow_config_params').awsAccountIds | join('\",\"') }}\"))\n| filter in(controlId, array(\"{{ result('workflow_config_params').securityControlIdsToGroupByAccount | join('\",\"') }}\"))\n| summarize { count=count(),\n              lastObservedAt = max(lastObservedAt),\n              remediation = collectDistinct(remediation),\n              complianceStatus = takeLast(complianceStatus),\n              resources = collectDistinct(resource),\n              title = takeAny(title),\n              description = takeAny(description),\n              severity = takeAny(severity),\n              awsRegion = collectArray(awsRegion)\n            },\n            by:{\n              controlId, \n              awsAccountId\n           }\n| lookup\n  [ fetch dt.entity.aws_credentials \n    | fields awsAccountId, entity.name\n  ], lookupField:awsAccountId, sourceField:awsAccountId, prefix: \"aws.account.\"\n"



   },



   "position": {



   "x": 0,



   "y": 2



   },



   "predecessors": [



   "workflow_config_params"



   ],



   "conditions": {



   "states": {



   "workflow_config_params": "OK"



   }



   }



   },



   "fetch_findings_by_resource": {



   "name": "fetch_findings_by_resource",



   "description": "Executes query to get relevant security findings grouped by AWS resource",



   "action": "dynatrace.automations:execute-dql-query",



   "active": true,



   "input": {



   "query": "fetch logs, from:now() - 24h, scanLimitGBytes: -1\n| filter aws.log_group == \"/aws/events/AWSSecurityHubLogGroup\"\n| parse content, \"JSON:alert\"\n| fields timestamp,\n         awsRegion = toString(alert[detail][findings][0][Region]),\n         awsAccountId = toString(alert[detail][findings][0][AwsAccountId]),\n         resourceType = toString(alert[detail][findings][0][Resources][0][Type]),          \n         resourceId = toString(alert[detail][findings][0][Resources][0][Id]),\n         alertType = toString(alert[detail][findings][0][Types][0]),\n         id = toString(alert[detail][findings][0][Id]),\n         severity = toString(alert[detail][findings][0][FindingProviderFields][Severity][Label]),\n         title = toString(alert[detail][findings][0][Title]),\n         description = toString(alert[detail][findings][0][Description]),\n         complianceStatus = toString(alert[detail][findings][0][Compliance][Status]),\n         controlId = toString(alert[detail][findings][0][Compliance][SecurityControlId]),\n         remediation = alert[detail][findings][0][Remediation],\n         created = toTimestamp(alert[detail][findings][0][CreatedAt]),\n         lastObservedAt = toTimestamp(alert[detail][findings][0][LastObservedAt])\n| filter in(severity, array(\"HIGH\", \"CRITICAL\", \"MEDIUM\"))\n| filter created > now() - 24h\n| filter in(awsAccountId, array(\"{{ result('workflow_config_params').awsAccountIds | join('\",\"') }}\"))\n| filter in(controlId, array(\"{{ result('workflow_config_params').securityControlIdsToGroupByResource | join('\",\"') }}\"))\n| summarize { count=count(),\n              lastObservedAt = max(lastObservedAt),\n              remediation = collectDistinct(remediation),\n              complianceStatus = takeLast(complianceStatus)\n            },\n            by:{\n              alertType, \n              resourceType, \n              controlId, \n              title,\n              description, \n              severity, \n              resourceId, \n              awsAccountId,\n              created,\n              awsRegion\n           }\n| lookup\n  [ fetch dt.entity.aws_credentials \n    | fields id, awsAccountId, entity.name, tags, awsNameTag\n  ], lookupField:awsAccountId, sourceField:awsAccountId, prefix: \"aws.account.\"\n| fields aws = record(\n            accountId = awsAccountId,\n            name = aws.account.entity.name,\n            entity = aws.account.id\n         ), \n         resource = record(\n           resourceId = resourceId,\n           resourceType = resourceType\n         ),\n         region = awsRegion,\n         alert = record(controlId = controlId, \n           severity = severity, \n           complianceStatus = complianceStatus,\n           title = title,\n           description = description,\n           remediation = remediation\n         )\n| summarize {\n        count=count(),\n        vulnerabilities = collectDistinct(alert)\n      },\n      by:{\n        aws,\n        resource,\n        region\n      }"



   },



   "position": {



   "x": 1,



   "y": 2



   },



   "predecessors": [



   "workflow_config_params"



   ],



   "conditions": {



   "states": {



   "workflow_config_params": "OK"



   }



   }



   },



   "prepare_tickets_by_account": {



   "name": "prepare_tickets_by_account",



   "description": "Prepares payload of Jira tickets for vulnerable AWS accounts",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function () {\n    const ex = await execution();\n    const records = await ex.result(\"log_tickets_by_account\");\n\n    console.log(`${records.length} Tickets will be created!`)\n    const result = [];\n    for (const finding of records) {\n        console.log('------------------------------------- NEW TICKET -------------------------------------')\n        const resourcesList = finding.resources\n          .map( resource => `|${resource}|` )\n          .join('\\n')\n        const ticket =  {\n            summary: `Automatic Vulnerability Report for ${finding.controlId} - AWS Account ${finding.awsAccountId}`,\n            description: 'The following vulnerabilities were reported for your resource via AWS Security Hub:\\n\\n'\n              + '*AWS Account*:\\n'\n              + '||AWS Account Id||\\n'\n              +  `|${finding.awsAccountId}|\\n\\n`\n              + '*Vulnerability*:\\n'\n              + '||Id||Sev||Title||Description||Remediation Url||\\n'\n              + `|{noformat}${finding.controlId}{noformat}|{noformat}${finding.severity}{noformat}|${finding.title}|${finding.description}|[${finding.remediation[0].Recommendation.Url}]|\\n\\n`\n              + '*Affected Resources*:\\n'\n              + '||Resource Id||\\n'\n              + resourcesList\n              + '\\n\\n---\\nAutomatically generated by CSPM Notification Automation'\n        }\n        console.log(JSON.stringify(ticket))\n        result.push(ticket)\n    }\n\n    return result;\n}"



   },



   "position": {



   "x": 0,



   "y": 4



   },



   "predecessors": [



   "log_tickets_by_account"



   ],



   "conditions": {



   "states": {



   "log_tickets_by_account": "OK"



   }



   }



   },



   "prepare_tickets_by_resource": {



   "name": "prepare_tickets_by_resource",



   "description": "Prepares payload of Jira tickets for vulnerable AWS resources",



   "action": "dynatrace.automations:run-javascript",



   "active": true,



   "input": {



   "script": "import { execution } from '@dynatrace-sdk/automation-utils';\n\nexport default async function () {\n    const ex = await execution();\n    const records = await ex.result(\"log_tickets_by_resource\");\n\n    console.log(`${records.length} Tickets will be created!`)\n    const result = [];\n    for (const finding of records) {\n        console.log('------------------------------------- NEW TICKET -------------------------------------')\n        const vulnerabilitiesList = finding.vulnerabilities\n          .map( vuln => \n            `|{noformat}${vuln.controlId}{noformat}|{noformat}${vuln.severity}{noformat}|${vuln.title}|${vuln.description}|[${vuln.remediation[0].Recommendation.Url}]|`)\n          .join('\\n')\n        const ticket =  {\n            summary: `Automatic Vulnerability Report for ${finding.resource.resourceId}`,\n            description: 'The following vulnerabilities were reported for your resource via AWS Security Hub:\\n\\n'\n              + '*AWS Account*:\\n'\n              + '||AWS Account Id||\\n'\n              +  `|${finding.aws.accountId}|\\n\\n`\n              + '*Resource Details*:\\n'\n              + '||Resource Type||Resource Id||\\n'\n              + `|${finding.resource.resourceType}|${finding.resource.resourceId}|\\n\\n`\n              + '*Vulnerabilities*:\\n'\n              + '||Id||Sev||Title||Description||Remediation Url||\\n'\n              + vulnerabilitiesList\n              + '\\n\\n---\\nAutomatically generated by CSPM Notification Automation'\n        }\n        console.log(JSON.stringify(ticket))\n        result.push(ticket)\n    }\n\n    return result;\n}"



   },



   "position": {



   "x": 1,



   "y": 4



   },



   "predecessors": [



   "log_tickets_by_resource"



   ],



   "conditions": {



   "states": {



   "log_tickets_by_resource": "OK"



   }



   }



   }



   },



   "ownerType": "USER",



   "isPrivate": false,



   "trigger": {



   "schedule": {



   "rule": null,



   "trigger": {



   "type": "time",



   "time": "09:00"



   },



   "timezone": "Europe/Berlin",



   "isActive": true,



   "isFaulty": false,



   "nextExecution": "2023-10-03T07:00:00.000Z",



   "filterParameters": {



   "earliestStart": "2023-09-25"



   },



   "inputs": {}



   }



   },



   "schemaVersion": 3



   }
   ```
2. В ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** выберите **Upload** и загрузите файл.

2. Установите время

**Триггер фиксированного времени**: Устанавливает время запуска рабочего процесса (в данном случае рабочий процесс запускается каждый день в 9:00). Дополнительную информацию о планировании рабочего процесса см. в разделе [Планирование рабочих процессов](/docs/analyze-explore-automate/workflows/trigger/schedules "Guide to creating workflow automation schedule triggers in Dynatrace Workflows.").

Показать соответствующую задачу рабочего процесса

![Установка времени в рабочем процессе CSPM](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-79b6452375.png)

3. Определите параметры

**Параметры конфигурации рабочего процесса**: Определяет, какие результаты вы хотите фильтровать. В текущем сценарии команда хочет

* Получать уведомления только о результатах из важных учётных записей AWS, отбрасывая результаты из других учётных записей, например, из сред, не находящихся в продакшене.

  + В разделе `awsAccountIds` выберите учётные записи AWS, для которых вы хотите получать результаты.
* Группировать результаты для определённых [идентификаторов контролей безопасности](https://dt-url.net/nx8393z) в один тикет на учётную запись AWS.

  + В разделе `securityControlIdsToGroupByAccount` выберите идентификаторы контролей безопасности, которые вы хотите группировать по учётной записи AWS.
* Группировать результаты для определённых идентификаторов контролей безопасности в один тикет на ресурс AWS.

  + В разделе `securityControlIdsToGroupByResource` выберите идентификаторы контролей безопасности, которые вы хотите группировать по ресурсу AWS.

Показать соответствующую задачу рабочего процесса

![Определение параметров в рабочем процессе CSPM](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-711174cd7e.png)

4. Оркестрация результатов

По учётной записи AWS

По ресурсу AWS

Следующая последовательность задач оркестрирует группировку и преобразование полученных результатов в один тикет на учётную запись AWS.

1. **Получение результатов по учётной записи**: Выполняет [DQL-запрос](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts."), который получает результаты. Некоторая информация, получаемая для текущего случая и отображаемая в Jira, включает

   * Количество результатов для соответствующей учётной записи
   * Заголовок проблемы, включая идентификаторы контролей безопасности и имя учётной записи AWS
   * Краткое описание уязвимостей
   * Ссылка на AWS с инструкциями по устранению уязвимостей
   * Список затронутых ресурсов AWS
2. **Логирование тикетов по учётной записи**: Показывает потенциальное содержимое тикета перед его автоматическим созданием. Этот шаг обеспечивает правильность вашей конфигурации. Подробности см. в разделе [Проверка статистики перед созданием тикетов](#test).
3. **Подготовка тикетов по учётной записи**: Настраивает полезную нагрузку для тикета Jira.
4. **Создание задач для учётной записи**: Интегрируется с вашим подключением к Jira. В разделе **Input** выберите подключение к Jira, созданное в [Предварительных требованиях](#dt), и введите нужные параметры тикета Jira.

Показать соответствующую последовательность задач рабочего процесса

![Группировка результатов по учётной записи AWS](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-e9069605d2.png)

Следующая последовательность задач оркестрирует группировку и преобразование полученных результатов в один тикет на ресурс AWS.

1. **Получение результатов по ресурсу**: Выполняет [DQL-запрос](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts."), который получает результаты. Некоторая информация, получаемая для текущего случая и отображаемая в Jira, включает

   * Количество результатов для соответствующего ресурса
   * Заголовок проблемы, включая идентификаторы контролей безопасности и имя ресурса AWS
   * Имя учётной записи AWS для соответствующего ресурса
   * Детали ресурса
   * Краткое описание уязвимостей
   * Ссылка на AWS с инструкциями по устранению уязвимостей
2. **Логирование тикетов по ресурсу**: Показывает потенциальное содержимое тикета перед его автоматическим созданием. Этот шаг обеспечивает правильность вашей конфигурации. Подробности см. в разделе [Проверка статистики перед созданием тикетов](#test).
3. **Подготовка тикетов по ресурсу**: Настраивает полезную нагрузку для тикета Jira.
4. **Создание задач для ресурса**: Интегрируется с вашим подключением к Jira. В разделе **Input** выберите подключение к Jira, созданное в [Предварительных требованиях](#dt), и введите нужные параметры тикета Jira.

Показать соответствующую последовательность задач рабочего процесса

![Группировка результатов по ресурсу AWS](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-e30cc64df3.png)

5. Отображение статистики

Следующая последовательность задач отображает количество новых результатов с момента последнего запуска рабочего процесса.

1. **Подсчёт всех новых результатов**: Выполняет DQL-запрос, который получает количество результатов, созданных AWS Security Hub за последние 24 часа.
2. **Логирование количества новых результатов**: Отображает результат запроса.

Показать соответствующую последовательность задач рабочего процесса

![Отображение статистики в рабочем процессе CSPM](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-ac3fc24771.png)

После завершения настройки рабочего процесса выберите **Save**.

### Проверка статистики перед созданием тикетов

Для тестирования конфигурации перед отправкой тикетов Jira

1. Отключите задачи **Подготовка тикетов по учётной записи/ресурсу** и **Создание задач для учётной записи/ресурса**.

Показать соответствующие последовательности задач рабочего процесса

![Отключение задач для создания уведомлений](https://dt-cdn.net/images/441c8585-ef4b-4272-b62a-872410b504c7-896-ef757cb613.png)

Инструкции по отключению задачи см. в разделе [Отключение или включение задачи](/docs/analyze-explore-automate/workflows/building#disable-enable "Create and edit workflows in Dynatrace Workflows.").

2. Запустите рабочий процесс или выполните отдельные задачи, для которых вы хотите проверить вывод. Инструкции см. в разделе [Запуск и мониторинг рабочих процессов](/docs/analyze-explore-automate/workflows/running "Run and monitor workflows created in Dynatrace Workflows.").

## Интеллектуальная безопасность

Поздравляем! Вы настроили автоматизацию, которая расширяет возможности вашей команды безопасности. С помощью автоматизации уведомлений Dynatrace CSPM критические события упорядочены, усталость от оповещений минимизирована, а облачная безопасность усилена. Эффективность раскрыта!

## Дополнительные ресурсы

Ниже представлено руководство от внутреннего заказчика автоматизации уведомлений Dynatrace CSPM.

Автоматизация уведомлений CSPM с Dynatrace

## Связанные темы

* [Оповещения и уведомления](/docs/analyze-explore-automate/alerting-and-notifications "Utilize anomaly detection, problem detection, and workflows for external notifications to ensure that critical problems never go unnoticed.")
