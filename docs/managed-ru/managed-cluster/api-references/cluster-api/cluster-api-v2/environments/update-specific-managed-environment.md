---
title: "Update specific environment"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/environments/update-specific-managed-environment
updated: 2026-02-09
---

Этот API-вызов обновляет существующее окружение или создаёт новое.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.

## Endpoint

`/api/cluster/v2/environments`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID окружения для обновления.  Если ID задан и в теле запроса, он должен совпадать с этим ID. | path | Required |
| createToken | boolean | Если true, при создании нового окружения создаётся token management token со scope'ами 'apiTokens.read' и 'apiTokens.write' (для использования с token API v2) и 'TenantTokenManagement' (для использования с token API v1). Этот токен возвращается в теле ответа. Его можно использовать внутри созданного окружения для создания других токенов настройки этого окружения. | query | Optional |
| body | [Environment](#openapi-definition-Environment) | JSON-тело запроса с обновлёнными параметрами окружения. | body | Optional |

### Объекты тела запроса

#### Объект `Environment`

Базовая конфигурация окружения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| creationDate | string | Дата создания окружения в формате ISO 8601 (yyyy-MM-dd'T'HH:mm:ss.SSS'Z') | Optional |
| id | string | ID окружения. Должен соответствовать [a-zA-Z0-9\_-]{1,70} | Optional |
| name | string | Отображаемое имя окружения. | Required |
| quotas | [EnvironmentQuotas](#openapi-definition-EnvironmentQuotas) | Информация о потреблении и квотах на уровне окружения. Возвращается только если параметр includeConsumptionInfo или includeUncachedConsumptionInfo равен true. Недоступно для лицензионной модели DPS. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. | Optional |
| state | string | Указывает, включено или выключено окружение. По умолчанию ENABLED. Возможные значения: * `DISABLED` * `ENABLED` | Optional |
| storage | [EnvironmentStorage](#openapi-definition-EnvironmentStorage) | Информация об использовании и лимитах хранилища на уровне окружения. Не возвращается, если параметр includeStorageInfo не равен true. Если опущено при редактировании через PUT, уже заданные лимиты сохраняются. | Optional |
| tags | string[] | Набор тегов, назначенных этому окружению. Каждый тег максимум 100 символов. | Optional |
| trial | boolean | Указывает, является ли окружение trial или не-trial. Создание trial-окружения возможно только если это позволяет лицензия. По умолчанию false (не-trial). | Optional |

#### Объект `EnvironmentQuotas`

Информация о потреблении и квотах на уровне окружения. Возвращается только если параметр includeConsumptionInfo или includeUncachedConsumptionInfo равен true. Недоступно для лицензионной модели DPS. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| customMetrics | [CustomMetricsQuota](#openapi-definition-CustomMetricsQuota) | Информация о потреблении и квоте Custom metrics на уровне окружения. Не задано (и не редактируется), если Custom metrics не включены. Не задано (и не редактируется), если включены Davis data units. Если опущено при редактировании через PUT, уже заданная квота сохраняется. | Optional |
| davisDataUnits | [DavisDataUnitsQuota](#openapi-definition-DavisDataUnitsQuota) | Информация о потреблении и квоте Davis data units на уровне окружения. Не задано (и не редактируется), если Davis data units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. | Optional |
| demUnits | [DemUnitsQuota](#openapi-definition-DemUnitsQuota) | Информация о потреблении и квоте DEM units на уровне окружения. Не задано (и не редактируется), если DEM units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. | Optional |
| hostUnits | [HostUnitQuota](#openapi-definition-HostUnitQuota) | Информация о потреблении и квоте Host units на уровне окружения. Если опущено при редактировании через PUT, уже заданная квота сохраняется. | Optional |
| logMonitoring | [LogMonitoringQuota](#openapi-definition-LogMonitoringQuota) | Информация о потреблении и квоте Log monitoring на уровне окружения. Не задано (и не редактируется), если Log monitoring не включён. Не задано (и не редактируется), если Log monitoring мигрирован на Davis data на уровне лицензии. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. | Optional |
| sessionProperties | [SessionPropertiesQuota](#openapi-definition-SessionPropertiesQuota) | Информация о потреблении User session properties на уровне окружения. | Optional |
| syntheticMonitors | [SyntheticQuota](#openapi-definition-SyntheticQuota) | Информация о потреблении и квоте Synthetic monitors на уровне окружения. Не задано (и не редактируется), если ни Synthetic, ни DEM units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. | Optional |
| userSessions | [UserSessionsQuota](#openapi-definition-UserSessionsQuota) | Информация о потреблении и квоте User sessions на уровне окружения. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. | Optional |

#### Объект `CustomMetricsQuota`

Информация о потреблении и квоте Custom metrics на уровне окружения. Не задано (и не редактируется), если Custom metrics не включены. Не задано (и не редактируется), если включены Davis data units. Если опущено при редактировании через PUT, уже заданная квота сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| currentUsage | number | Текущее использование окружения. | Optional |
| maxLimit | integer | Параллельная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |

#### Объект `DavisDataUnitsQuota`

Информация о потреблении и квоте Davis data units на уровне окружения. Не задано (и не редактируется), если Davis data units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| annualLimit | integer | Годовая квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |
| consumedThisMonth | number | Месячное потребление окружения. Сбрасывается каждый календарный месяц. | Optional |
| consumedThisYear | number | Годовое потребление окружения. Сбрасывается каждый год в годовщину создания лицензии. | Optional |
| monthlyLimit | integer | Месячная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |

#### Объект `DemUnitsQuota`

Информация о потреблении и квоте DEM units на уровне окружения. Не задано (и не редактируется), если DEM units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| annualLimit | integer | Годовая квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |
| consumedThisMonth | number | Месячное потребление окружения. Сбрасывается каждый календарный месяц. | Optional |
| consumedThisYear | number | Годовое потребление окружения. Сбрасывается каждый год в годовщину создания лицензии. | Optional |
| monthlyLimit | integer | Месячная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |

#### Объект `HostUnitQuota`

Информация о потреблении и квоте Host units на уровне окружения. Если опущено при редактировании через PUT, уже заданная квота сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| currentUsage | number | Текущее использование окружения. | Optional |
| maxLimit | integer | Параллельная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |

#### Объект `LogMonitoringQuota`

Информация о потреблении и квоте Log monitoring на уровне окружения. Не задано (и не редактируется), если Log monitoring не включён. Не задано (и не редактируется), если Log monitoring мигрирован на Davis data на уровне лицензии. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| annualLimit | integer | Годовая квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |
| consumedThisMonth | number | Месячное потребление окружения. Сбрасывается каждый календарный месяц. | Optional |
| consumedThisYear | number | Годовое потребление окружения. Сбрасывается каждый год в годовщину создания лицензии. | Optional |
| monthlyLimit | integer | Месячная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |

#### Объект `SessionPropertiesQuota`

Информация о потреблении User session properties на уровне окружения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| consumedThisMonth | number | Месячное потребление окружения. Сбрасывается каждый календарный месяц. | Optional |
| consumedThisYear | number | Годовое потребление окружения. Сбрасывается каждый год в годовщину создания лицензии. | Optional |

#### Объект `SyntheticQuota`

Информация о потреблении и квоте Synthetic monitors на уровне окружения. Не задано (и не редактируется), если ни Synthetic, ни DEM units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| annualLimit | integer | Годовая квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |
| consumedThisMonth | number | Месячное потребление окружения. Сбрасывается каждый календарный месяц. | Optional |
| consumedThisYear | number | Годовое потребление окружения. Сбрасывается каждый год в годовщину создания лицензии. | Optional |
| monthlyLimit | integer | Месячная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |

#### Объект `UserSessionsQuota`

Информация о потреблении и квоте User sessions на уровне окружения. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| consumedMobileSessionsThisMonth | number | Месячное потребление окружения по Mobile user sessions. Сбрасывается каждый календарный месяц. | Optional |
| consumedMobileSessionsThisYear | number | Годовое потребление окружения по Mobile user sessions. Сбрасывается каждый год в годовщину создания лицензии. | Optional |
| consumedUserSessionsWithMobileSessionReplayThisMonth | number | Месячное потребление окружения по Mobile user sessions с replay. Сбрасывается каждый календарный месяц. | Optional |
| consumedUserSessionsWithMobileSessionReplayThisYear | number | Годовое потребление окружения по Mobile user sessions с replay. Сбрасывается каждый год в годовщину создания лицензии. | Optional |
| consumedUserSessionsWithWebSessionReplayThisMonth | number | Месячное потребление окружения по Web user sessions с replay. Сбрасывается каждый календарный месяц. | Optional |
| consumedUserSessionsWithWebSessionReplayThisYear | number | Годовое потребление окружения по Web user sessions с replay. Сбрасывается каждый год в годовщину создания лицензии. | Optional |
| totalAnnualLimit | integer | Годовая общая квота окружения по User sessions. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |
| totalConsumedThisMonth | number | Месячное общее потребление окружения по User sessions. Сбрасывается каждый календарный месяц. | Optional |
| totalConsumedThisYear | number | Годовое общее потребление окружения по User sessions. Сбрасывается каждый год в годовщину создания лицензии. | Optional |
| totalMonthlyLimit | integer | Месячная общая квота окружения по User sessions. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. | Optional |

#### Объект `EnvironmentStorage`

Информация об использовании и лимитах хранилища на уровне окружения. Не возвращается, если параметр includeStorageInfo не равен true. Если опущено при редактировании через PUT, уже заданные лимиты сохраняются.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| realUserMonitoringRetention | [RealUserMonitoringRetention](#openapi-definition-RealUserMonitoringRetention) | Настройки retention Real user monitoring на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. | Optional |
| rumNonAggregatedDataRetention | [RumNonAggregatedDataRetention](#openapi-definition-RumNonAggregatedDataRetention) | Настройки retention неагрегированных данных RUM на уровне окружения. Можно задать любое значение от 1 до 365 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. | Optional |
| serviceCodeLevelRetention | [ServiceCodeLevelRetention](#openapi-definition-ServiceCodeLevelRetention) | Настройки retention service code level на уровне окружения. Время retention service code level не может быть больше времени retention service request level, и оба не могут превышать один год. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. | Optional |
| serviceRequestLevelRetention | [ServiceRequestLevelRetention](#openapi-definition-ServiceRequestLevelRetention) | Настройки retention service request level на уровне окружения. Время retention service code level не может быть больше времени retention service request level, и оба не могут превышать один год. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. | Optional |
| sessionReplayRetention | [SessionReplayRetention](#openapi-definition-SessionReplayRetention) | Настройки retention Session replay на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. | Optional |
| sessionReplayStorage | [SessionReplayStorage](#openapi-definition-SessionReplayStorage) | Информация об использовании и лимите хранилища Session replay на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. | Optional |
| symbolFilesFromMobileApps | [SymbolFilesFromMobileApps](#openapi-definition-SymbolFilesFromMobileApps) | Информация об использовании и лимите хранилища symbol files от mobile apps на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. | Optional |
| syntheticMonitoringRetention | [SyntheticMonitoringRetention](#openapi-definition-SyntheticMonitoringRetention) | Настройки retention Synthetic monitoring на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. | Optional |
| transactionStorage | [TransactionStorage](#openapi-definition-TransactionStorage) | Информация об использовании и лимите хранилища Transaction на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. | Optional |
| transactionTrafficQuota | [TransactionTrafficQuota](#openapi-definition-TransactionTrafficQuota) | Максимальное количество новых отслеживаемых entry point PurePaths, захватываемых на process/minute, на уровне окружения. Можно задать любое значение от 100 до 100000. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. | Optional |
| userActionsPerMinute | [UserActionsPerMinute](#openapi-definition-UserActionsPerMinute) | Максимальное количество user actions, генерируемых в минуту, на уровне окружения. Можно задать любое значение от 1 до 2147483646 или оставить без лимита. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. | Optional |

#### Объект `RealUserMonitoringRetention`

Настройки retention Real user monitoring на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] | Optional |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] | Optional |
| maxLimitInDays | integer | Максимальный лимит retention [дни] | Optional |

#### Объект `RumNonAggregatedDataRetention`

Настройки retention неагрегированных данных RUM на уровне окружения. Можно задать любое значение от 1 до 365 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] | Optional |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] | Optional |
| maxLimitInDays | integer | Максимальный лимит retention [дни] | Optional |

#### Объект `ServiceCodeLevelRetention`

Настройки retention service code level на уровне окружения. Время retention service code level не может быть больше времени retention service request level, и оба не могут превышать один год. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] | Optional |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] | Optional |
| maxLimitInDays | integer | Максимальный лимит retention [дни] | Optional |

#### Объект `ServiceRequestLevelRetention`

Настройки retention service request level на уровне окружения. Время retention service code level не может быть больше времени retention service request level, и оба не могут превышать один год. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] | Optional |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] | Optional |
| maxLimitInDays | integer | Максимальный лимит retention [дни] | Optional |

#### Объект `SessionReplayRetention`

Настройки retention Session replay на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] | Optional |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] | Optional |
| maxLimitInDays | integer | Максимальный лимит retention [дни] | Optional |

#### Объект `SessionReplayStorage`

Информация об использовании и лимите хранилища Session replay на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| currentlyUsed | integer | Текущее использование хранилища [байты] | Optional |
| maxLimit | integer | Максимальный лимит хранилища [байты] | Optional |
| retentionReductionPercentage | string | Процент усечения для новых данных. | Optional |
| retentionReductionReason | string | Причина усечения. | Optional |

#### Объект `SymbolFilesFromMobileApps`

Информация об использовании и лимите хранилища symbol files от mobile apps на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| currentlyUsed | integer | Текущее использование хранилища [байты] | Optional |
| maxLimit | integer | Максимальный лимит хранилища [байты] | Optional |

#### Объект `SyntheticMonitoringRetention`

Настройки retention Synthetic monitoring на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] | Optional |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] | Optional |
| maxLimitInDays | integer | Максимальный лимит retention [дни] | Optional |

#### Объект `TransactionStorage`

Информация об использовании и лимите хранилища Transaction на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| currentlyUsed | integer | Текущее использование хранилища [байты] | Optional |
| maxLimit | integer | Максимальный лимит хранилища [байты] | Optional |
| retentionReductionPercentage | string | Процент усечения для новых данных. | Optional |
| retentionReductionReason | string | Причина усечения. | Optional |

#### Объект `TransactionTrafficQuota`

Максимальное количество новых отслеживаемых entry point PurePaths, захватываемых на process/minute, на уровне окружения. Можно задать любое значение от 100 до 100000. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| maxLimit | integer | Максимальный трафик [units per minute] | Optional |

#### Объект `UserActionsPerMinute`

Максимальное количество user actions, генерируемых в минуту, на уровне окружения. Можно задать любое значение от 1 до 2147483646 или оставить без лимита. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| maxLimit | integer | Максимальный трафик [units per minute] | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{


"name": "example environment",


"state": "ENABLED",


"tags": [


"tag1",


"tag2"


],


"trial": false


}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EnvironmentShortRepresentation](#openapi-definition-EnvironmentShortRepresentation) | Успех. Создано новое окружение. Тело ответа содержит ID, имя и token management token, если 'createToken' равен 'true'. |
| **204** | - | Успех. Окружение обновлено. Ответ без тела. |
| **400** | - | Сбой. Невалидный ввод. |

### Объекты тела ответа

#### Объект `EnvironmentShortRepresentation`

Краткое представление окружения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |
| tokenManagementToken | string | Токен с разрешением 'Token management'. Можно использовать внутри созданного окружения для создания других токенов настройки этого окружения. Это значение задаётся только если окружение было создано с query-параметром 'createToken=true'. |

### JSON-модели тела ответа

```
{


"description": "string",


"id": "string",


"name": "string",


"tokenManagementToken": "string"


}
```

## Пример

Отключает окружение с идентификатором `19a963a7-b19f-4382-964a-4df674c8eb8e`.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/cluster/v2/environments/19a963a7-b19f-4382-964a-4df674c8eb8e?createToken=false" -H "accept: application/json; charset=utf-8" -H "Authorization: Api-Token fSRCdB7PQDSdFVANvNfSF" -H "Content-Type: application/json; charset=utf-8" -d "


{\"name\":\"MyNewTeam\",\"id\":\"19a963a7-b19f-4382-964a-4df674c8eb8e\",\"trial\":false,\"state\":\"DISABLED\",\"tags\":[\"owner:john.wicked@dynatrace.com\",\"department:finance\"]}
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/environments/19a963a7-b19f-4382-964a-4df674c8eb8e?createToken=false
```

#### Тело запроса

```
{


"name": "MyNewTeam",


"state": "DISABLED"


}
```

#### Тело ответа

Ответ без тела.

#### Код ответа

`204`
