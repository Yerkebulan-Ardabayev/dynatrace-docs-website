---
title: List all existing environments
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/environments/list-managed-environments
scraped: 2026-05-12T11:06:13.613500
---

# List all existing environments

# List all existing environments

* Published Mar 09, 2021

Этот API-вызов возвращает список всех существующих окружений.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/environments`

## Параметр

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор следующей страницы результатов. Можно найти его в поле **nextPageKey** предыдущего ответа.  Первая страница возвращается всегда, если не указан query-параметр **nextPageKey**.  Когда **nextPageKey** задан для получения следующих страниц, все остальные query-параметры нужно опустить. | query | Optional |
| pageSize | integer | Количество окружений в одном payload ответа.  Максимально допустимый размер страницы 1000.  Если не задан, используется 100. | query | Optional |
| sort | string | Порядок сортировки. Возможные варианты:  * 'name' (без кавычек): сортировка по имени по возрастанию. * '-name' (без кавычек): сортировка по имени по убыванию. * 'creationDate' (без кавычек): сортировка по дате создания по возрастанию. * '-creationDate' (без кавычек): сортировка по имени по убыванию. | query | Optional |
| filter | string | Задаёт фильтр запроса.  Можно задать один или несколько критериев:  * Name: `name(string)`. Имя может быть подстрокой или полным именем окружения. Без учёта регистра. * Trial: `trial(true)` или `trial(false)`. Включает только trial-окружения если true, или только не-trial окружения если false. * State: `state(ENABLED)` или `state(DISABLED)`. * Tag: `tag(string)`. Чтобы фильтровать по нескольким тегам с OR-логикой, используйте `tag(string1,string2)`. Чтобы фильтровать по нескольким тегам с AND-логикой, используйте `tag(string1),tag(string2)`.   Чтобы задать несколько критериев, разделите их запятой (`,`). В ответ включаются только результаты, удовлетворяющие **всем** критериям. | query | Optional |
| includeConsumptionInfo | boolean | Если true, для каждого окружения возвращается информация о потреблении (лимиты, использование).  Возвращаемые данные потребления могут отставать на час. Чтобы получить более свежие данные, используйте параметр **includeUncachedConsumptionInfo**.  Эта опция недоступна для лицензионной модели DPS. | query | Optional |
| includeStorageInfo | boolean | Если true, для каждого окружения возвращается информация о хранилище (лимиты, использование). | query | Optional |
| includeUncachedConsumptionInfo | boolean | Если true, для каждого окружения возвращается некэшированная информация о потреблении (лимиты, использование).  Будет рассчитано актуальное потребление. Расчёт может быть длительным, поэтому рекомендуется использовать параметр **includeConsumptionInfo**.  Если заданы оба параметра, **includeUncachedConsumptionInfo** имеет приоритет.  Эта опция недоступна для лицензионной модели DPS. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EnvironmentList](#openapi-definition-EnvironmentList) | Операция выполнена успешно. |
| **422** | - | Информация о потреблении недоступна для лицензионной модели DPS. |

### Объекты тела ответа

#### Объект `EnvironmentList`

Список окружений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| environments | [Environment[]](#openapi-definition-Environment) | Список окружений. |
| nextPageKey | string | Курсор следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения следующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `Environment`

Базовая конфигурация окружения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| creationDate | string | Дата создания окружения в формате ISO 8601 (yyyy-MM-dd'T'HH:mm:ss.SSS'Z') |
| id | string | ID окружения. Должен соответствовать [a-zA-Z0-9\_-]{1,70} |
| name | string | Отображаемое имя окружения. |
| quotas | [EnvironmentQuotas](#openapi-definition-EnvironmentQuotas) | Информация о потреблении и квотах на уровне окружения. Возвращается только если параметр includeConsumptionInfo или includeUncachedConsumptionInfo равен true. Недоступно для лицензионной модели DPS. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. |
| state | string | Указывает, включено или выключено окружение. По умолчанию ENABLED. Возможные значения: * `DISABLED` * `ENABLED` |
| storage | [EnvironmentStorage](#openapi-definition-EnvironmentStorage) | Информация об использовании и лимитах хранилища на уровне окружения. Не возвращается, если параметр includeStorageInfo не равен true. Если опущено при редактировании через PUT, уже заданные лимиты сохраняются. |
| tags | string[] | Набор тегов, назначенных этому окружению. Каждый тег максимум 100 символов. |
| trial | boolean | Указывает, является ли окружение trial или не-trial. Создание trial-окружения возможно только если это позволяет лицензия. По умолчанию false (не-trial). |

#### Объект `EnvironmentQuotas`

Информация о потреблении и квотах на уровне окружения. Возвращается только если параметр includeConsumptionInfo или includeUncachedConsumptionInfo равен true. Недоступно для лицензионной модели DPS. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание |
| --- | --- | --- |
| customMetrics | [CustomMetricsQuota](#openapi-definition-CustomMetricsQuota) | Информация о потреблении и квоте Custom metrics на уровне окружения. Не задано (и не редактируется), если Custom metrics не включены. Не задано (и не редактируется), если включены Davis data units. Если опущено при редактировании через PUT, уже заданная квота сохраняется. |
| davisDataUnits | [DavisDataUnitsQuota](#openapi-definition-DavisDataUnitsQuota) | Информация о потреблении и квоте Davis data units на уровне окружения. Не задано (и не редактируется), если Davis data units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. |
| demUnits | [DemUnitsQuota](#openapi-definition-DemUnitsQuota) | Информация о потреблении и квоте DEM units на уровне окружения. Не задано (и не редактируется), если DEM units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. |
| hostUnits | [HostUnitQuota](#openapi-definition-HostUnitQuota) | Информация о потреблении и квоте Host units на уровне окружения. Если опущено при редактировании через PUT, уже заданная квота сохраняется. |
| logMonitoring | [LogMonitoringQuota](#openapi-definition-LogMonitoringQuota) | Информация о потреблении и квоте Log monitoring на уровне окружения. Не задано (и не редактируется), если Log monitoring не включён. Не задано (и не редактируется), если Log monitoring мигрирован на Davis data на уровне лицензии. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. |
| sessionProperties | [SessionPropertiesQuota](#openapi-definition-SessionPropertiesQuota) | Информация о потреблении User session properties на уровне окружения. |
| syntheticMonitors | [SyntheticQuota](#openapi-definition-SyntheticQuota) | Информация о потреблении и квоте Synthetic monitors на уровне окружения. Не задано (и не редактируется), если ни Synthetic, ни DEM units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. |
| userSessions | [UserSessionsQuota](#openapi-definition-UserSessionsQuota) | Информация о потреблении и квоте User sessions на уровне окружения. Если опущено при редактировании через PUT, уже заданные квоты сохраняются. |

#### Объект `CustomMetricsQuota`

Информация о потреблении и квоте Custom metrics на уровне окружения. Не задано (и не редактируется), если Custom metrics не включены. Не задано (и не редактируется), если включены Davis data units. Если опущено при редактировании через PUT, уже заданная квота сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| currentUsage | number | Текущее использование окружения. |
| maxLimit | integer | Параллельная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |

#### Объект `DavisDataUnitsQuota`

Информация о потреблении и квоте Davis data units на уровне окружения. Не задано (и не редактируется), если Davis data units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание |
| --- | --- | --- |
| annualLimit | integer | Годовая квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |
| consumedThisMonth | number | Месячное потребление окружения. Сбрасывается каждый календарный месяц. |
| consumedThisYear | number | Годовое потребление окружения. Сбрасывается каждый год в годовщину создания лицензии. |
| monthlyLimit | integer | Месячная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |

#### Объект `DemUnitsQuota`

Информация о потреблении и квоте DEM units на уровне окружения. Не задано (и не редактируется), если DEM units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание |
| --- | --- | --- |
| annualLimit | integer | Годовая квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |
| consumedThisMonth | number | Месячное потребление окружения. Сбрасывается каждый календарный месяц. |
| consumedThisYear | number | Годовое потребление окружения. Сбрасывается каждый год в годовщину создания лицензии. |
| monthlyLimit | integer | Месячная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |

#### Объект `HostUnitQuota`

Информация о потреблении и квоте Host units на уровне окружения. Если опущено при редактировании через PUT, уже заданная квота сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| currentUsage | number | Текущее использование окружения. |
| maxLimit | integer | Параллельная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |

#### Объект `LogMonitoringQuota`

Информация о потреблении и квоте Log monitoring на уровне окружения. Не задано (и не редактируется), если Log monitoring не включён. Не задано (и не редактируется), если Log monitoring мигрирован на Davis data на уровне лицензии. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание |
| --- | --- | --- |
| annualLimit | integer | Годовая квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |
| consumedThisMonth | number | Месячное потребление окружения. Сбрасывается каждый календарный месяц. |
| consumedThisYear | number | Годовое потребление окружения. Сбрасывается каждый год в годовщину создания лицензии. |
| monthlyLimit | integer | Месячная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |

#### Объект `SessionPropertiesQuota`

Информация о потреблении User session properties на уровне окружения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| consumedThisMonth | number | Месячное потребление окружения. Сбрасывается каждый календарный месяц. |
| consumedThisYear | number | Годовое потребление окружения. Сбрасывается каждый год в годовщину создания лицензии. |

#### Объект `SyntheticQuota`

Информация о потреблении и квоте Synthetic monitors на уровне окружения. Не задано (и не редактируется), если ни Synthetic, ни DEM units не включены. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание |
| --- | --- | --- |
| annualLimit | integer | Годовая квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |
| consumedThisMonth | number | Месячное потребление окружения. Сбрасывается каждый календарный месяц. |
| consumedThisYear | number | Годовое потребление окружения. Сбрасывается каждый год в годовщину создания лицензии. |
| monthlyLimit | integer | Месячная квота окружения. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |

#### Объект `UserSessionsQuota`

Информация о потреблении и квоте User sessions на уровне окружения. Если опущено при редактировании через PUT, уже заданные квоты сохраняются.

| Элемент | Тип | Описание |
| --- | --- | --- |
| consumedMobileSessionsThisMonth | number | Месячное потребление окружения по Mobile user sessions. Сбрасывается каждый календарный месяц. |
| consumedMobileSessionsThisYear | number | Годовое потребление окружения по Mobile user sessions. Сбрасывается каждый год в годовщину создания лицензии. |
| consumedUserSessionsWithMobileSessionReplayThisMonth | number | Месячное потребление окружения по Mobile user sessions с replay. Сбрасывается каждый календарный месяц. |
| consumedUserSessionsWithMobileSessionReplayThisYear | number | Годовое потребление окружения по Mobile user sessions с replay. Сбрасывается каждый год в годовщину создания лицензии. |
| consumedUserSessionsWithWebSessionReplayThisMonth | number | Месячное потребление окружения по Web user sessions с replay. Сбрасывается каждый календарный месяц. |
| consumedUserSessionsWithWebSessionReplayThisYear | number | Годовое потребление окружения по Web user sessions с replay. Сбрасывается каждый год в годовщину создания лицензии. |
| totalAnnualLimit | integer | Годовая общая квота окружения по User sessions. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |
| totalConsumedThisMonth | number | Месячное общее потребление окружения по User sessions. Сбрасывается каждый календарный месяц. |
| totalConsumedThisYear | number | Годовое общее потребление окружения по User sessions. Сбрасывается каждый год в годовщину создания лицензии. |
| totalMonthlyLimit | integer | Месячная общая квота окружения по User sessions. Не задано, если без лимита. При обновлении через PUT, опуская это поле, квота становится без лимита. |

#### Объект `EnvironmentStorage`

Информация об использовании и лимитах хранилища на уровне окружения. Не возвращается, если параметр includeStorageInfo не равен true. Если опущено при редактировании через PUT, уже заданные лимиты сохраняются.

| Элемент | Тип | Описание |
| --- | --- | --- |
| realUserMonitoringRetention | [RealUserMonitoringRetention](#openapi-definition-RealUserMonitoringRetention) | Настройки retention Real user monitoring на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. |
| rumNonAggregatedDataRetention | [RumNonAggregatedDataRetention](#openapi-definition-RumNonAggregatedDataRetention) | Настройки retention неагрегированных данных RUM на уровне окружения. Можно задать любое значение от 1 до 365 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. |
| serviceCodeLevelRetention | [ServiceCodeLevelRetention](#openapi-definition-ServiceCodeLevelRetention) | Настройки retention service code level на уровне окружения. Время retention service code level не может быть больше времени retention service request level, и оба не могут превышать один год. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. |
| serviceRequestLevelRetention | [ServiceRequestLevelRetention](#openapi-definition-ServiceRequestLevelRetention) | Настройки retention service request level на уровне окружения. Время retention service code level не может быть больше времени retention service request level, и оба не могут превышать один год. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. |
| sessionReplayRetention | [SessionReplayRetention](#openapi-definition-SessionReplayRetention) | Настройки retention Session replay на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. |
| sessionReplayStorage | [SessionReplayStorage](#openapi-definition-SessionReplayStorage) | Информация об использовании и лимите хранилища Session replay на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. |
| symbolFilesFromMobileApps | [SymbolFilesFromMobileApps](#openapi-definition-SymbolFilesFromMobileApps) | Информация об использовании и лимите хранилища symbol files от mobile apps на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. |
| syntheticMonitoringRetention | [SyntheticMonitoringRetention](#openapi-definition-SyntheticMonitoringRetention) | Настройки retention Synthetic monitoring на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. |
| transactionStorage | [TransactionStorage](#openapi-definition-TransactionStorage) | Информация об использовании и лимите хранилища Transaction на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. |
| transactionTrafficQuota | [TransactionTrafficQuota](#openapi-definition-TransactionTrafficQuota) | Максимальное количество новых отслеживаемых entry point PurePaths, захватываемых на process/minute, на уровне окружения. Можно задать любое значение от 100 до 100000. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. |
| userActionsPerMinute | [UserActionsPerMinute](#openapi-definition-UserActionsPerMinute) | Максимальное количество user actions, генерируемых в минуту, на уровне окружения. Можно задать любое значение от 1 до 2147483646 или оставить без лимита. Если опущено при редактировании через PUT, уже заданный лимит сохраняется. |

#### Объект `RealUserMonitoringRetention`

Настройки retention Real user monitoring на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] |
| maxLimitInDays | integer | Максимальный лимит retention [дни] |

#### Объект `RumNonAggregatedDataRetention`

Настройки retention неагрегированных данных RUM на уровне окружения. Можно задать любое значение от 1 до 365 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] |
| maxLimitInDays | integer | Максимальный лимит retention [дни] |

#### Объект `ServiceCodeLevelRetention`

Настройки retention service code level на уровне окружения. Время retention service code level не может быть больше времени retention service request level, и оба не могут превышать один год. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] |
| maxLimitInDays | integer | Максимальный лимит retention [дни] |

#### Объект `ServiceRequestLevelRetention`

Настройки retention service request level на уровне окружения. Время retention service code level не может быть больше времени retention service request level, и оба не могут превышать один год. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] |
| maxLimitInDays | integer | Максимальный лимит retention [дни] |

#### Объект `SessionReplayRetention`

Настройки retention Session replay на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] |
| maxLimitInDays | integer | Максимальный лимит retention [дни] |

#### Объект `SessionReplayStorage`

Информация об использовании и лимите хранилища Session replay на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| currentlyUsed | integer | Текущее использование хранилища [байты] |
| maxLimit | integer | Максимальный лимит хранилища [байты] |
| retentionReductionPercentage | string | Процент усечения для новых данных. |
| retentionReductionReason | string | Причина усечения. |

#### Объект `SymbolFilesFromMobileApps`

Информация об использовании и лимите хранилища symbol files от mobile apps на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| currentlyUsed | integer | Текущее использование хранилища [байты] |
| maxLimit | integer | Максимальный лимит хранилища [байты] |

#### Объект `SyntheticMonitoringRetention`

Настройки retention Synthetic monitoring на уровне окружения. Можно задать любое значение от 1 до 35 дней. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| currentlyUsedInDays | integer | Текущий возраст данных [дни] |
| currentlyUsedInMillis | integer | Текущий возраст данных [миллисекунды] |
| maxLimitInDays | integer | Максимальный лимит retention [дни] |

#### Объект `TransactionStorage`

Информация об использовании и лимите хранилища Transaction на уровне окружения. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| currentlyUsed | integer | Текущее использование хранилища [байты] |
| maxLimit | integer | Максимальный лимит хранилища [байты] |
| retentionReductionPercentage | string | Процент усечения для новых данных. |
| retentionReductionReason | string | Причина усечения. |

#### Объект `TransactionTrafficQuota`

Максимальное количество новых отслеживаемых entry point PurePaths, захватываемых на process/minute, на уровне окружения. Можно задать любое значение от 100 до 100000. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| maxLimit | integer | Максимальный трафик [units per minute] |

#### Объект `UserActionsPerMinute`

Максимальное количество user actions, генерируемых в минуту, на уровне окружения. Можно задать любое значение от 1 до 2147483646 или оставить без лимита. Если опущено при редактировании через PUT, уже заданный лимит сохраняется.

| Элемент | Тип | Описание |
| --- | --- | --- |
| maxLimit | integer | Максимальный трафик [units per minute] |

### JSON-модели тела ответа

```
{



"environments": [



{



"name": "example environment",



"state": "ENABLED",



"tags": [



"tag1",



"tag2"



],



"trial": false



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



}
```

## Пример

Возвращает два самых новых включённых окружения с их потреблением лицензии, отсортированных по имени.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/environments?pageSize=2&sort=-creationDate&filter=state%28ENABLED%29&includeConsumptionInfo=true" -H "accept: application/json; charset=utf-8" -H "Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/environments?pageSize=2&sort=-creationDate&filter=state%28ENABLED%29&includeConsumptionInfo=true
```

#### Тело ответа

```
{



"totalCount": 78,



"pageSize": 2,



"nextPageKey": "AAAAAQAAAAIBnldfkgldsjoeriKIDFL2AAABd3uuvIMBAA5zdGF0ZShFTkFCTEVEKQEADS1jcmVhdGlvbkRhdGU=",



"environments": [



{



"name": "AndroidApps",



"id": "be22c776-1414-00e0-a00a-00b0dcf56443321",



"trial": false,



"state": "ENABLED",



"tags": [],



"creationDate": "2021-02-09T11:03:17.732Z",



"quotas": {



"hostUnits": {



"maxLimit": 10,



"currentUsage": 0



},



"demUnits": {



"monthlyLimit": 50001,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"userSessions": {



"totalMonthlyLimit": null,



"totalAnnualLimit": null,



"totalConsumedThisMonth": 0,



"totalConsumedThisYear": 0,



"consumedMobileSessionsThisMonth": 0,



"consumedMobileSessionsThisYear": 0,



"consumedUserSessionsWithWebSessionReplayThisMonth": 0,



"consumedUserSessionsWithWebSessionReplayThisYear": 0,



"consumedUserSessionsWithMobileSessionReplayThisMonth": 0,



"consumedUserSessionsWithMobileSessionReplayThisYear": 0



},



"sessionProperties": {



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"syntheticMonitors": {



"monthlyLimit": null,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"customMetrics": null,



"davisDataUnits": {



"monthlyLimit": 18162,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"logMonitoring": null



}



},



{



"name": "Service Team",



"id": "881c4134-0000-0a00-aa0a-5b03ab7a34ed",



"trial": false,



"state": "ENABLED",



"tags": [],



"creationDate": "2021-02-07T08:49:45.091Z",



"quotas": {



"hostUnits": {



"maxLimit": null,



"currentUsage": 0



},



"demUnits": {



"monthlyLimit": null,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 62



},



"userSessions": {



"totalMonthlyLimit": null,



"totalAnnualLimit": null,



"totalConsumedThisMonth": 0,



"totalConsumedThisYear": 0,



"consumedMobileSessionsThisMonth": 0,



"consumedMobileSessionsThisYear": 0,



"consumedUserSessionsWithWebSessionReplayThisMonth": 0,



"consumedUserSessionsWithWebSessionReplayThisYear": 0,



"consumedUserSessionsWithMobileSessionReplayThisMonth": 0,



"consumedUserSessionsWithMobileSessionReplayThisYear": 0



},



"sessionProperties": {



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"syntheticMonitors": {



"monthlyLimit": null,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 62



},



"customMetrics": null,



"davisDataUnits": {



"monthlyLimit": null,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"logMonitoring": null



}



}



]



}
```

#### Код ответа

`200`