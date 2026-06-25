---
title: Create a new environment
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/environments/create-managed-environment
scraped: 2026-05-12T11:05:46.662122
---

# Create a new environment

# Create a new environment

* Published Mar 09, 2021

Этот API-вызов создаёт новое окружение.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/environments`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| createToken | boolean | Если true, при создании нового окружения создаётся token management token со scope'ами 'apiTokens.read' и 'apiTokens.write' (для использования с token API v2) и 'TenantTokenManagement' (для использования с token API v1). Этот токен возвращается в теле ответа. Его можно использовать внутри созданного окружения для создания других токенов настройки этого окружения. | query | Optional |
| body | [Environment](#openapi-definition-Environment) | JSON-тело запроса. Тело не должно содержать ID, поскольку он автоматически назначается Dynatrace Server. | body | Required |

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
| **201** | [EnvironmentShortRepresentation](#openapi-definition-EnvironmentShortRepresentation) | Успех. Окружение создано и запущено. Тело ответа содержит сгенерированный ID окружения и токен со scope'ами 'apiTokens.read' и 'apiTokens.write' (для использования с token API v2) и 'TenantTokenManagement'. Заголовок location тоже содержит сгенерированный ID. |
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

Создаёт окружение с именем `MyNewTeam`, указывая детали по квоте лицензии, лимитам хранилища и retention данных.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/cluster/v2/environments?createToken=true" -H "accept: application/json; charset=utf-8" -H "Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890" -H "Content-Type: application/json; charset=utf-8" -d



"{\"name\":\"MyNewTeam\",\"state\":\"ENABLED\",\"tags\":[\"owner:john.wicked@dynatrace.com\",\"department:finance\"],\"trial\":false}, \"quotas\":{\"hostUnits\":{\"maxLimit\":1},\"demUnits\":{\"monthlyLimit\":1,\"annualLimit\":1},\"userSessions\":{\"totalMonthlyLimit\":1,\"totalAnnualLimit\":2},\"syntheticMonitors\":{\"monthlyLimit\":1,\"annualLimit\":1},\"davisDataUnits\":{\"monthlyLimit\":1,\"annualLimit\":2}},\"storage\":{\"transactionStorage\":{\"maxLimit\":1024},\"sessionReplayStorage\":{\"maxLimit\":2048},\"symbolFilesFromMobileApps\":{\"maxLimit\":5050},\"serviceRequestLevelRetention\":{\"maxLimitInDays\":35},\"serviceCodeLevelRetention\":{\"maxLimitInDays\":10},\"realUserMonitoringRetention\":{\"maxLimitInDays\":35},\"syntheticMonitoringRetention\":{\"maxLimitInDays\":35},\"sessionReplayRetention\":{\"maxLimitInDays\":35},\"userActionsPerMinute\":{\"maxLimit\":3500},\"transactionTrafficQuota\":{\"maxLimit\":1000}}}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/environments?createToken=true
```

#### Тело запроса

```
{



"name": "MyNewTeam",



"state": "ENABLED",



"tags": [



"owner:john.wicked@dynatrace.com",



"department:finance"



],



"trial": false,



"quotas": {



"hostUnits": {



"maxLimit": 1



},



"demUnits": {



"monthlyLimit": 1,



"annualLimit": 1



},



"userSessions": {



"totalMonthlyLimit": 1,



"totalAnnualLimit": 2



},



"syntheticMonitors": {



"monthlyLimit": 1,



"annualLimit": 1



},



"davisDataUnits": {



"monthlyLimit": 1,



"annualLimit": 2



}



},



"storage": {



"transactionStorage": {



"maxLimit": 1024



},



"sessionReplayStorage": {



"maxLimit": 2048



},



"symbolFilesFromMobileApps": {



"maxLimit": 5050



},



"serviceRequestLevelRetention": {



"maxLimitInDays": 35



},



"serviceCodeLevelRetention": {



"maxLimitInDays": 10



},



"realUserMonitoringRetention": {



"maxLimitInDays": 35



},



"syntheticMonitoringRetention": {



"maxLimitInDays": 35



},



"sessionReplayRetention": {



"maxLimitInDays": 35



},



"userActionsPerMinute": {



"maxLimit": 3500



},



"transactionTrafficQuota": {



"maxLimit": 1000



}



}



}
```

#### Тело ответа

Успех. Окружение создано и запущено. Тело ответа содержит сгенерированный ID окружения и токен с разрешением `Token management`. Заголовок location тоже содержит сгенерированный ID.

```
{



"id": "11a113a1-a11b-1234-123a-4df674c8eb8e",



"name": "MyNewTeam",



"tokenManagementToken":



"dt0c01.LJMAHMWOKCL5IPH3E2ORNHTR.<token-value>"



}
```

#### Код ответа

`201`