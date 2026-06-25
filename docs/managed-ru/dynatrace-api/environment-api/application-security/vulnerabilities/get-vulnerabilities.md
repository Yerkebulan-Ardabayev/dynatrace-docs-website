---
title: Vulnerabilities API - GET уязвимости
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/vulnerabilities/get-vulnerabilities
scraped: 2026-05-12T11:58:50.263120
---

# Vulnerabilities API - GET уязвимости

# Vulnerabilities API - GET уязвимости

* Reference
* Updated on Nov 09, 2023

Возвращает список уязвимостей сторонних компонентов и уязвимостей уровня кода, обнаруженных в ваших приложениях.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/securityProblems` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/securityProblems` |

## Аутентификация

Для выполнения запроса необходим access token со scope `securityProblems.read`.

О том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательность |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Если query-параметр **nextPageKey** не указан, всегда возвращается первая страница.  При указании **nextPageKey** для получения последующих страниц все остальные query-параметры должны быть опущены. | query | Необязательный |
| pageSize | integer | Количество проблем безопасности в одном payload ответа.  Максимально допустимый размер страницы 500.  Если не задано, используется 100. | query | Необязательный |
| securityProblemSelector | string | Определяет область запроса. В ответ попадают только проблемы безопасности, соответствующие указанным критериям.  Можно добавить один или несколько следующих критериев. Значения регистронезависимы, и по умолчанию используется оператор `EQUALS`, если не указано иначе.  * Статус: `status("value")`. Возможные значения см. в описании поля **status** ответа. Если не задано, возвращаются все проблемы безопасности. * Приглушено: `muted("value")`. Возможные значения: `TRUE` или `FALSE`. * Уровень риска: `riskLevel("value")`. Уровень риска Davis. Возможные значения см. в описании поля **riskLevel** ответа. * Минимальный балл риска: `minRiskScore("5.5")`. Минимальный балл риска Davis. Используется оператор `GREATER THAN OR EQUAL TO`. Укажите число от `1.0` до `10.0`. * Максимальный балл риска: `maxRiskScore("5.5")`. Максимальный балл риска Davis. Используется оператор `LESS THAN`. Укажите число от `1.0` до `10.0`. * Базовый уровень риска: `baseRiskLevel("value")`. Базовый уровень риска из CVSS. Возможные значения см. в описании поля **riskLevel** ответа. * Минимальный базовый балл риска: `minBaseRiskScore("5.5")`. Минимальный базовый балл риска из CVSS. Используется оператор `GREATER THAN OR EQUAL TO`. Укажите число от `1.0` до `10.0`. * Максимальный базовый балл риска: `maxBaseRiskScore("5.5")`. Максимальный базовый балл риска из CVSS. Используется оператор `LESS THAN`. Укажите число от `1.0` до `10.0`. * Внешний идентификатор уязвимости содержит: `externalVulnerabilityIdContains("id-1")`. Используется оператор `CONTAINS`. Максимальная длина значения 48 символов. * Внешний идентификатор уязвимости: `externalVulnerabilityId("id-1", "id-2")`. * Идентификатор CVE: `cveId("id")`. * Оценка риска: `riskAssessment("value-1", "value-2")`. Возможные значения: `EXPOSED`, `SENSITIVE`, `EXPLOIT`, `VULNERABLE_FUNCTION_IN_USE` и `ACCURACY_REDUCED`. * Идентификатор связанного хоста: `relatedHostIds("value-1", "value-2")`. Указывайте идентификаторы сущностей Dynatrace. * Имя связанного хоста: `relatedHostNames("value-1", "value-2")`. Значения регистрозависимы. * Имя связанного хоста содержит: `relatedHostNameContains("value-1")`. Используется оператор `CONTAINS`. * Идентификатор связанного кластера Kubernetes: `relatedKubernetesClusterIds("value-1", "value-2")`. Указывайте идентификаторы сущностей Dynatrace. * Имя связанного кластера Kubernetes: `relatedKubernetesClusterNames("value-1", "value-2")`. Значения регистрозависимы. * Имя связанного кластера Kubernetes содержит: `relatedKubernetesClusterNameContains("value-1")`. Используется оператор `CONTAINS`. * Идентификатор связанного workload Kubernetes: `relatedKubernetesWorkloadIds("value-1", "value-2")`. Указывайте идентификаторы сущностей Dynatrace. * Имя связанного workload Kubernetes: `relatedKubernetesWorkloadNames("value-1", "value-2")`. Значения регистрозависимы. * Имя связанного workload Kubernetes содержит: `relatedKubernetesWorkloadNameContains("value-1")`. Используется оператор `CONTAINS`. * Идентификатор зоны управления: `managementZoneIds("mzId-1", "mzId-2")`. * Имя зоны управления: `managementZones("name-1", "name-2")`. Значения регистрозависимы. * Идентификатор затронутого экземпляра группы процессов: `affectedPgiIds("pgiId-1", "pgiId-2")`. Указывайте идентификаторы сущностей Dynatrace. * Идентификатор затронутой группы процессов: `affectedPgIds("pgId-1", "pgId-2")`. Указывайте идентификаторы сущностей Dynatrace. * Имя затронутой группы процессов: `affectedPgNames("name-1", "name-2")`. Значения регистрозависимы. * Имя затронутой группы процессов содержит: `affectedPgNameContains("name-1")`. Используется оператор `CONTAINS`. * Идентификатор уязвимого компонента: `vulnerableComponentIds("componentId-1", "componentId-2")`. Указывайте идентификаторы компонентов. * Имя уязвимого компонента: `vulnerableComponentNames("name-1", "name-2")`. Значения регистрозависимы. * Имя уязвимого компонента содержит: `vulnerableComponentNameContains("name-1")`. Используется оператор `CONTAINS`. * Теги хостов: `hostTags("hostTag-1")`. Используется оператор `CONTAINS`. Максимальная длина значения 48 символов. * Теги групп процессов: `pgTags("pgTag-1")`. Используется оператор `CONTAINS`. Максимальная длина значения 48 символов. * Теги экземпляров групп процессов: `pgiTags("pgiTag-1")`. Используется оператор `CONTAINS`. Максимальная длина значения 48 символов. * Теги: `tags("tag-1")`. Используется оператор `CONTAINS`. Этот селектор одновременно выбирает хосты, группы процессов и экземпляры групп процессов. Максимальная длина значения 48 символов. * Отображаемый идентификатор: `displayIds("S-1234", "S-5678")`. Используется оператор `EQUALS`. * Идентификатор проблемы безопасности: `securityProblemIds("12544152654387159360", "5904857564184044850")`. Используется оператор `EQUALS`. * Технология: `technology("technology-1", "technology-2")`. Возможные значения см. в описании поля **technology** ответа. Используется оператор `EQUALS`. * Тип уязвимости: `vulnerabilityType("type-1", "type-2")`. Возможные значения: `THIRD_PARTY`, `CODE_LEVEL`, `RUNTIME`.  Балл риска и категория риска взаимоисключающие (нельзя использовать одновременно).  Чтобы задать несколько критериев, разделите их запятой (`,`). В ответ попадут только результаты, удовлетворяющие **всем** критериям.  Указывайте значение критерия как строку в кавычках. Следующие специальные символы внутри кавычек нужно экранировать тильдой (`~`):  * Тильда `~` * Кавычка `"` | query | Необязательный |
| sort | string | Указывает одно или несколько полей для сортировки списка проблем безопасности. Несколько полей можно объединять через запятую (`,`) (например, `+status,-timestamp`).  Доступна сортировка по следующим свойствам с префиксом знака для направления сортировки.  * `status`: Статус проблемы безопасности (`+` сначала открытые или `-` сначала разрешённые) * `muted`: Приглушённое состояние проблемы безопасности (`+` сначала не приглушённые или `-` сначала приглушённые) * `technology`: Технология проблемы безопасности * `firstSeenTimestamp`: Метка времени первого появления проблемы безопасности (`+` сначала новые или `-` сначала старые) * `lastUpdatedTimestamp`: Метка времени последнего обновления проблемы безопасности (`+` сначала недавно обновлённые или `-` сначала ранее обновлённые) * `securityProblemId`: Автоматически генерируемый идентификатор проблемы безопасности (`+` сначала меньший номер или `-` сначала больший номер) * `externalVulnerabilityId`: Идентификатор внешней уязвимости (`+` сначала меньший номер или `-` сначала больший номер) * `displayId`: Отображаемый идентификатор (`+` сначала меньший номер или `-` сначала больший номер) * `riskAssessment.riskScore`: Davis Security Score (`+` сначала меньший балл или `-` сначала больший балл) * `riskAssessment.riskLevel`: Уровень Davis Security Score (`+` сначала меньший уровень или `-` сначала больший уровень) * `riskAssessment.exposure`: Открыта ли проблема в интернет * `riskAssessment.baseRiskScore`: Балл CVSS (`+` сначала меньший балл или `-` сначала больший балл) * `riskAssessment.baseRiskLevel`: Уровень CVSS (`+` сначала меньший уровень или `-` сначала больший уровень) * `riskAssessment.dataAssets`: Затронуты ли активы с данными * `riskAssessment.vulnerableFunctionUsage`: Используются ли уязвимые функции * `riskAssessment.assessmentAccuracy`: Точность оценок (`+` сначала меньшая точность или `-` сначала большая точность) * `globalCounts.affectedNodes`: Количество затронутых узлов (`+` сначала меньший номер или `-` сначала больший номер) * `globalCounts.affectedProcessGroupInstances`: Количество затронутых экземпляров групп процессов (`+` сначала меньший номер или `-` сначала больший номер) * `globalCounts.affectedProcessGroups`: Количество затронутых групп процессов (`+` сначала меньший номер или `-` сначала больший номер) * `globalCounts.exposedProcessGroups`: Количество открытых групп процессов (`+` сначала меньший номер или `-` сначала больший номер) * `globalCounts.reachableDataAssets`: Количество доступных активов с данными (`+` сначала меньший номер или `-` сначала больший номер) * `globalCounts.relatedApplications`: Количество связанных приложений (`+` сначала меньший номер или `-` сначала больший номер) * `globalCounts.relatedAttacks`: Количество атак на проблему безопасности (`+` сначала меньший номер или `-` сначала больший номер) * `globalCounts.relatedHosts`: Количество связанных хостов (`+` сначала меньший номер или `-` сначала больший номер) * `globalCounts.relatedKubernetesClusters`: Количество связанных кластеров Kubernetes (`+` сначала меньший номер или `-` сначала больший номер) * `globalCounts.relatedKubernetesWorkloads`: Количество связанных workloads Kubernetes (`+` сначала меньший номер или `-` сначала больший номер) * `globalCounts.relatedServices`: Количество связанных сервисов (`+` сначала меньший номер или `-` сначала больший номер) * `globalCounts.vulnerableComponents`: Количество уязвимых компонентов (`+` сначала меньший номер или `-` сначала больший номер)  Если префикс не указан, используется `+`. | query | Необязательный |
| fields | string | Список дополнительных свойств проблемы безопасности, которые можно добавить в ответ.  Доступны следующие свойства (все остальные свойства возвращаются всегда и их нельзя убрать из ответа):  * `riskAssessment`: Оценка риска проблемы безопасности. * `managementZones`: Зона управления, в которой возникла проблема безопасности. * `codeLevelVulnerabilityDetails`: Детали уязвимости уровня кода. * `globalCounts`: Глобально подсчитанная статистика по проблеме безопасности. Информация о зоне управления не учитывается.  Чтобы добавить свойства, перечислите их через запятую и поставьте перед каждым знак плюс (например, `+riskAssessment,+managementZones`). | query | Необязательный |
| from | string | Начало запрашиваемого интервала времени.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный интервал от текущего момента назад. Формат: `now-NU/A`, где `N` это количество, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад с выравниванием по неделе.   Можно указать относительный интервал и без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного интервала: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный интервал 30 дней (`now-30d`). | query | Необязательный |
| to | string | Конец запрашиваемого интервала времени.  Можно использовать один из следующих форматов:  * Метка времени в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный интервал от текущего момента назад. Формат: `now-NU/A`, где `N` это количество, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это один год назад с выравниванием по неделе.   Можно указать относительный интервал и без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного интервала: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущая метка времени.  Конец интервала не может быть старше 365 дней. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SecurityProblemList](#openapi-definition-SecurityProblemList) | Успех. Ответ содержит список проблем безопасности. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SecurityProblemList`

Список проблем безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения последующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| securityProblems | [SecurityProblem[]](#openapi-definition-SecurityProblem) | Список проблем безопасности. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `SecurityProblem`

Параметры проблемы безопасности

| Элемент | Тип | Описание |
| --- | --- | --- |
| codeLevelVulnerabilityDetails | [CodeLevelVulnerabilityDetails](#openapi-definition-CodeLevelVulnerabilityDetails) | Детали уязвимости уровня кода. |
| cveIds | string[] | Список идентификаторов CVE для проблемы безопасности. |
| displayId | string | Отображаемый идентификатор проблемы безопасности. |
| externalVulnerabilityId | string | Внешний идентификатор уязвимости для проблемы безопасности. |
| firstSeenTimestamp | integer | Метка времени первого появления проблемы безопасности. |
| globalCounts | [GlobalCountsDto](#openapi-definition-GlobalCountsDto) | Глобально подсчитанная статистика по проблеме безопасности. Информация о зоне управления не учитывается. |
| lastOpenedTimestamp | integer | Метка времени последнего открытия проблемы безопасности. |
| lastResolvedTimestamp | integer | Метка времени последнего разрешения проблемы безопасности. |
| lastUpdatedTimestamp | integer | Метка времени последнего изменения проблемы безопасности. |
| managementZones | [ManagementZone[]](#openapi-definition-ManagementZone) | Список зон управления, к которым относятся затронутые сущности. |
| muted | boolean | Проблема безопасности приглушена (`true`) или нет (`false`). |
| packageName | string | Имя пакета проблемы безопасности. |
| riskAssessment | [RiskAssessment](#openapi-definition-RiskAssessment) | Оценка риска проблемы безопасности. |
| securityProblemId | string | Идентификатор проблемы безопасности. |
| status | string | Статус проблемы безопасности. Элемент может принимать значения * `OPEN` * `RESOLVED` |
| technology | string | Технология проблемы безопасности. Элемент может принимать значения * `DOTNET` * `GO` * `JAVA` * `KUBERNETES` * `NODE_JS` * `PHP` * `PYTHON` |
| title | string | Заголовок проблемы безопасности. |
| url | string | URL страницы с деталями проблемы безопасности. |
| vulnerabilityType | string | Тип уязвимости. Элемент может принимать значения * `CODE_LEVEL` * `RUNTIME` * `THIRD_PARTY` |

#### Объект `CodeLevelVulnerabilityDetails`

Детали уязвимости уровня кода.

| Элемент | Тип | Описание |
| --- | --- | --- |
| processGroupIds | string[] | Список закодированных MEIdentifier групп процессов. |
| processGroups | string[] | Список затронутых групп процессов. |
| shortVulnerabilityLocation | string | Расположение уязвимости в коде без указания пакета и параметров. |
| type | string | Тип уязвимости уровня кода. Элемент может принимать значения * `CMD_INJECTION` * `IMPROPER_INPUT_VALIDATION` * `SQL_INJECTION` * `SSRF` |
| vulnerabilityLocation | string | Расположение уязвимости в коде. |
| vulnerableFunction | string | Уязвимая функция данной уязвимости. |
| vulnerableFunctionInput | [VulnerableFunctionInput](#openapi-definition-VulnerableFunctionInput) | Описывает, что было передано в уязвимость уровня кода. |

#### Объект `VulnerableFunctionInput`

Описывает, что было передано в уязвимость уровня кода.

| Элемент | Тип | Описание |
| --- | --- | --- |
| inputSegments | [VulnerableFunctionInputSegment[]](#openapi-definition-VulnerableFunctionInputSegment) | Список входных сегментов. |
| type | string | Тип входных данных. Элемент может принимать значения * `COMMAND` * `HTTP_CLIENT` * `JNDI` * `SQL_STATEMENT` |

#### Объект `VulnerableFunctionInputSegment`

Описывает один сегмент, переданный в уязвимую функцию.

| Элемент | Тип | Описание |
| --- | --- | --- |
| type | string | Тип входного сегмента. Элемент может принимать значения * `MALICIOUS_INPUT` * `REGULAR_INPUT` * `TAINTED_INPUT` |
| value | string | Значение входного сегмента. |

#### Объект `GlobalCountsDto`

Глобально подсчитанная статистика по проблеме безопасности. Информация о зоне управления не учитывается.

| Элемент | Тип | Описание |
| --- | --- | --- |
| affectedNodes | integer | Количество затронутых узлов |
| affectedProcessGroupInstances | integer | Количество затронутых экземпляров групп процессов |
| affectedProcessGroups | integer | Количество затронутых групп процессов |
| exposedProcessGroups | integer | Количество открытых групп процессов |
| reachableDataAssets | integer | Количество открытых доступных активов с данными |
| relatedApplications | integer | Количество связанных приложений |
| relatedAttacks | integer | Количество атак на открытую проблему безопасности |
| relatedHosts | integer | Количество связанных хостов |
| relatedKubernetesClusters | integer | Количество связанных кластеров Kubernetes |
| relatedKubernetesWorkloads | integer | Количество связанных workloads Kubernetes |
| relatedServices | integer | Количество связанных сервисов |
| vulnerableComponents | integer | Количество уязвимых компонентов |

#### Объект `ManagementZone`

Краткое представление зоны управления.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | Идентификатор зоны управления. |
| name | string | Имя зоны управления. |

#### Объект `RiskAssessment`

Оценка риска проблемы безопасности.

| Элемент | Тип | Описание |
| --- | --- | --- |
| assessmentAccuracy | string | Точность оценки. Элемент может принимать значения * `FULL` * `NOT_AVAILABLE` * `REDUCED` |
| assessmentAccuracyDetails | [AssessmentAccuracyDetails](#openapi-definition-AssessmentAccuracyDetails) | Детали точности оценки. |
| baseRiskLevel | string | Уровень риска из оценки CVSS. Элемент может принимать значения * `CRITICAL` * `HIGH` * `LOW` * `MEDIUM` * `NONE` |
| baseRiskScore | number | Балл риска (1-10) из оценки CVSS. |
| baseRiskVector | string | Исходный вектор атаки оценки CVSS. |
| dataAssets | string | Доступность связанных активов с данными для затронутых сущностей. Элемент может принимать значения * `NOT_AVAILABLE` * `NOT_DETECTED` * `REACHABLE` |
| exposure | string | Уровень открытости затронутых сущностей. Элемент может принимать значения * `NOT_AVAILABLE` * `NOT_DETECTED` * `PUBLIC_NETWORK` |
| publicExploit | string | Статус доступности публичных эксплойтов. Элемент может принимать значения * `AVAILABLE` * `NOT_AVAILABLE` |
| riskLevel | string | Уровень риска Davis.  Вычисляется Dynatrace на основе оценки CVSS. Элемент может принимать значения * `CRITICAL` * `HIGH` * `LOW` * `MEDIUM` * `NONE` |
| riskScore | number | Балл риска Davis (1-10).  Вычисляется Dynatrace на основе оценки CVSS. |
| riskVector | string | Вектор атаки, вычисленный Dynatrace на основе вектора атаки CVSS. |
| vulnerableFunctionUsage | string | Состояние выполнения уязвимого кода. Элемент может принимать значения * `IN_USE` * `NOT_AVAILABLE` * `NOT_IN_USE` |

#### Объект `AssessmentAccuracyDetails`

Детали точности оценки.

| Элемент | Тип | Описание |
| --- | --- | --- |
| reducedReasons | string[] | Причина пониженной точности оценки. Элемент может принимать значения * `LIMITED_AGENT_SUPPORT` * `LIMITED_BY_CONFIGURATION` |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"securityProblems": [



{



"codeLevelVulnerabilityDetails": {



"processGroupIds": [



"string"



],



"processGroups": [



"string"



],



"shortVulnerabilityLocation": "string",



"type": "CMD_INJECTION",



"vulnerabilityLocation": "string",



"vulnerableFunction": "string",



"vulnerableFunctionInput": {



"inputSegments": [



{



"type": "MALICIOUS_INPUT",



"value": "string"



}



],



"type": "COMMAND"



}



},



"cveIds": [



"string"



],



"displayId": "string",



"externalVulnerabilityId": "string",



"firstSeenTimestamp": 1,



"globalCounts": {



"affectedNodes": 1,



"affectedProcessGroupInstances": 1,



"affectedProcessGroups": 1,



"exposedProcessGroups": 1,



"reachableDataAssets": 1,



"relatedApplications": 1,



"relatedAttacks": 1,



"relatedHosts": 1,



"relatedKubernetesClusters": 1,



"relatedKubernetesWorkloads": 1,



"relatedServices": 1,



"vulnerableComponents": 1



},



"lastOpenedTimestamp": 1,



"lastResolvedTimestamp": 1,



"lastUpdatedTimestamp": 1,



"managementZones": [



{



"id": "string",



"name": "string"



}



],



"muted": true,



"packageName": "string",



"riskAssessment": {



"assessmentAccuracy": "FULL",



"assessmentAccuracyDetails": {



"reducedReasons": [



"LIMITED_AGENT_SUPPORT"



]



},



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 1,



"baseRiskVector": "string",



"dataAssets": "NOT_AVAILABLE",



"exposure": "NOT_AVAILABLE",



"publicExploit": "AVAILABLE",



"riskLevel": "CRITICAL",



"riskScore": 1,



"riskVector": "string",



"vulnerableFunctionUsage": "IN_USE"



},



"securityProblemId": "string",



"status": "OPEN",



"technology": "DOTNET",



"title": "string",



"url": "string",



"vulnerabilityType": "CODE_LEVEL"



}



],



"totalCount": 1



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Пример

Запрос десяти наиболее значимых открытых уязвимостей, отсортированных по баллу риска по убыванию.

Обязательные фильтры:

* `fields=%2BriskAssessment`
* `securityProblemSelector=status(OPEN)`
* `sort=-riskAssessment.riskScore`

#### Curl

```
curl -L -X GET 'https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems?pageSize=10&fields=%2BriskAssessment&securityProblemSelector=status(OPEN)&sort=-riskAssessment.riskScore' \



-H 'Authorization: Api-Token [your_token]' \



-H 'Accept: application/json'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v2/securityProblems?pageSize=10&fields=%2BriskAssessment&securityProblemSelector=status(OPEN)&sort=-riskAssessment.riskScore
```

#### Тело ответа

```
{



"totalCount": 306,



"pageSize": 10,



"nextPageKey": "vu8XQiDj3q0SIU59KgHvowAAAX_qbpspAAABgITtYykAAAAKAQAxc3RhdHVzKE9QRU4pLCB2dWxuZXJhYmlsaXR5VHlwZShUSElSRF9QQVJUWV9TTllLKQI0VT4tJAUu9QMBAQEAAzguNjRVPi0kBS71AgEBAQATNzY3ODM5MzU0NDcwOTM2NjkzMAEADytyaXNrQXNzZXNzbWVudL7vF0Ig496t",



"securityProblems": [



{



"securityProblemId": "11497873967941161718",



"displayId": "S-3454",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-ORGAPACHELOGGINGLOG4J-2314720",



"vulnerabilityType": "THIRD_PARTY",



"title": "Remote Code Execution (RCE)",



"packageName": "org.apache.logging.log4j:log4j-core",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/11497873967941161718",



"technology": "JAVA",



"firstSeenTimestamp": 1639135014832,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 10.0,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 10.0,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/E:H",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2021-44228"



]



},



{



"securityProblemId": "7968806720724378002",



"displayId": "S-3352",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-CHQOSLOGBACK-31407",



"vulnerabilityType": "THIRD_PARTY",



"title": "Arbitrary Code Execution",



"packageName": "ch.qos.logback:logback-classic",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/7968806720724378002",



"technology": "JAVA",



"firstSeenTimestamp": 1629276816755,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 9.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "NOT_AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2017-5929"



]



},



{



"securityProblemId": "13131808379454186608",



"displayId": "S-3343",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-CHQOSLOGBACK-30208",



"vulnerabilityType": "THIRD_PARTY",



"title": "Arbitrary Code Execution",



"packageName": "ch.qos.logback:logback-core",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/13131808379454186608",



"technology": "JAVA",



"firstSeenTimestamp": 1629276816755,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 9.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "NOT_AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2017-5929"



]



},



{



"securityProblemId": "13080692565938470532",



"displayId": "S-3342",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-ORGAPACHELOGGINGLOG4J-31409",



"vulnerabilityType": "THIRD_PARTY",



"title": "Deserialization of Untrusted Data",



"packageName": "org.apache.logging.log4j:log4j-core",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/13080692565938470532",



"technology": "JAVA",



"firstSeenTimestamp": 1629276816755,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 9.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:F",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2017-5645"



]



},



{



"securityProblemId": "12458843765122204362",



"displayId": "S-3337",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-LOG4J-572732",



"vulnerabilityType": "THIRD_PARTY",



"title": "Deserialization of Untrusted Data",



"packageName": "log4j:log4j",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/12458843765122204362",



"technology": "JAVA",



"firstSeenTimestamp": 1629276816755,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 9.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:P",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2019-17571"



]



},



{



"securityProblemId": "10489033029364122206",



"displayId": "S-3457",



"status": "OPEN",



"muted": false,



"externalVulnerabilityId": "SNYK-JAVA-ORGAPACHELOGGINGLOG4J-2320014",



"vulnerabilityType": "THIRD_PARTY",



"title": "Remote Code Execution (RCE)",



"packageName": "org.apache.logging.log4j:log4j-core",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/10489033029364122206",



"technology": "JAVA",



"firstSeenTimestamp": 1639510404699,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "CRITICAL",



"riskScore": 9.0,



"riskVector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.0,



"baseRiskVector": "CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/RC:C",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2021-45046"



]



},



{



"securityProblemId": "16904121786356925180",



"displayId": "S-3534",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-ORGAPACHESTRUTS-30207",



"vulnerabilityType": "THIRD_PARTY",



"title": "Arbitrary Code Execution",



"packageName": "org.apache.struts:struts2-core",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/16904121786356925180",



"technology": "JAVA",



"firstSeenTimestamp": 1647434489381,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "HIGH",



"riskScore": 8.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/MAV:A/MC:L/MI:L",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 10.0,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/E:F/RL:O/RC:C",



"exposure": "NOT_DETECTED",



"dataAssets": "NOT_DETECTED",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "IN_USE"



},



"cveIds": [



"CVE-2017-5638"



]



},



{



"securityProblemId": "13912219969549620585",



"displayId": "S-3315",



"status": "OPEN",



"muted": false,



"externalVulnerabilityId": "SNYK-JAVA-COMGOOGLEPROTOBUF-173761",



"vulnerabilityType": "THIRD_PARTY",



"title": "Integer Overflow",



"packageName": "com.google.protobuf:protobuf-java",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/13912219969549620585",



"technology": "JAVA",



"firstSeenTimestamp": 1629276761566,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "HIGH",



"riskScore": 8.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",



"baseRiskLevel": "HIGH",



"baseRiskScore": 8.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",



"exposure": "PUBLIC_NETWORK",



"dataAssets": "REACHABLE",



"publicExploit": "NOT_AVAILABLE",



"vulnerableFunctionUsage": "NOT_AVAILABLE"



},



"cveIds": [



"CVE-2015-5237"



]



},



{



"securityProblemId": "1340823583484240022",



"displayId": "S-3630",



"status": "OPEN",



"muted": true,



"externalVulnerabilityId": "SNYK-JAVA-ORGSPRINGFRAMEWORK-2436751",



"vulnerabilityType": "THIRD_PARTY",



"title": "Remote Code Execution",



"packageName": "org.springframework:spring-beans",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/1340823583484240022",



"technology": "JAVA",



"firstSeenTimestamp": 1648683464474,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "HIGH",



"riskScore": 8.8,



"riskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/MAV:A",



"baseRiskLevel": "CRITICAL",



"baseRiskScore": 9.8,



"baseRiskVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:F",



"exposure": "NOT_DETECTED",



"dataAssets": "REACHABLE",



"publicExploit": "AVAILABLE",



"vulnerableFunctionUsage": "IN_USE"



},



"cveIds": [



"CVE-2022-22965"



]



},



{



"securityProblemId": "7678393544709366930",



"displayId": "S-3252",



"status": "OPEN",



"muted": false,



"externalVulnerabilityId": "SNYK-JAVA-ORGSPRINGFRAMEWORK-1009832",



"vulnerabilityType": "THIRD_PARTY",



"title": "Improper Input Validation",



"packageName": "org.springframework:spring-web",



"url": "https://mySampleEnv.live.dynatrace.com/ui/security/problem/7678393544709366930",



"technology": "JAVA",



"firstSeenTimestamp": 1629277776755,



"lastUpdatedTimestamp": 1651497109253,



"riskAssessment": {



"riskLevel": "HIGH",



"riskScore": 8.6,



"riskVector": "CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H",



"baseRiskLevel": "HIGH",



"baseRiskScore": 8.6,



"baseRiskVector": "CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H",



"exposure": "NOT_DETECTED",



"dataAssets": "REACHABLE",



"publicExploit": "NOT_AVAILABLE",



"vulnerableFunctionUsage": "NOT_IN_USE"



},



"cveIds": [



"CVE-2020-5421"



]



}



]



}
```

## Связанные темы

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Davis Security Advisor API](/managed/dynatrace-api/environment-api/application-security/davis-security-advice "Просмотр рекомендаций Davis Security Advisor через Dynatrace API.")