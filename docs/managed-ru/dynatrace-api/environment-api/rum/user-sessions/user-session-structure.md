---
title: User sessions API - User session structure
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/user-sessions/user-session-structure
scraped: 2026-05-12T12:00:09.015548
---

# User sessions API - User session structure

# User sessions API - User session structure

* Reference
* Updated on May 02, 2022

На этой странице приведены описания всех возможных полей, которые может включать пользовательская сессия.

#### Объект `UserSession`

[Пользовательская сессия](https://dt-url.net/xv183rb8?dt=m), охватывающая несколько пользовательских действий и дополнительную информацию о визите пользователя.

| Элемент | Тип | Описание |
| --- | --- | --- |
| appVersion | string | Версия приложения, в котором была записана пользовательская сессия.  Эта информация предоставляется другой интеграцией, например OpenKit. |
| applicationType | string | Тип приложения, используемого в пользовательской сессии. Возможные значения: * `CUSTOM_APPLICATION` * `MOBILE_APPLICATION` * `WEB_APPLICATION` |
| bounce | boolean | Пользовательская сессия содержит (`true`) или не содержит (`false`) отказ.  Отказ означает, что в пользовательской сессии есть только одно (или менее) пользовательское действие. |
| browserFamily | string | Семейство браузера, использованного для пользовательской сессии. |
| browserMajorVersion | string | Версия браузера, использованного для пользовательской сессии. |
| browserMonitorId | string | ID браузерного Synthetic-монитора, создавшего сессию. |
| browserMonitorName | string | Имя браузерного Synthetic-монитора, создавшего сессию. |
| browserType | string | Тип браузера, использованного для пользовательской сессии. |
| carrier | string | Информация об операторе мобильной пользовательской сессии. |
| city | string | Город, из которого происходит пользовательская сессия (на основе IP-адреса). |
| clientTimeOffset | integer | Смещение времени клиента в миллисекундах |
| clientType | string | Дополнительная информация о клиенте.  Это поле нельзя запросить через user session query language. Вместо него используйте поле **browserType**. |
| connectionType | string | Сериализованный тип подключения мобильной пользовательской сессии. Возможные значения: * `LAN` * `MOBILE` * `OFFLINE` * `UNKNOWN` * `WIFI` |
| continent | string | Континент, из которого происходит пользовательская сессия (на основе IP-адреса). |
| country | string | Страна, из которой происходит пользовательская сессия (на основе IP-адреса). |
| crashGroupId | string | Если мобильная сессия завершилась сбоем, это ID группы, к которой относится аварийная сессия.  Если сессия не завершилась сбоем или сессия не является мобильной, имеет значение `null`. |
| dateProperties | [DateProperty[]](#openapi-definition-DateProperty) | Список пользовательских свойств пользовательской сессии со значениями-датами. |
| device | string | Обнаруженное устройство, использованное для пользовательской сессии. |
| displayResolution | string | Обнаруженное разрешение экрана устройства, использованного для пользовательской сессии. Возможные значения: * `CGA` * `DCI2K` * `DCI4K` * `DVGA` * `FHD` * `FWVGA` * `FWXGA` * `GHDPlus` * `HD` * `HQVGA` * `HQVGA2` * `HSXGA` * `HUXGA` * `HVGA` * `HXGA` * `NTSC` * `PAL` * `QHD` * `QQVGA` * `QSXGA` * `QUXGA` * `QVGA` * `QWXGA` * `QXGA` * `SVGA` * `SXGA` * `SXGAMinus` * `SXGAPlus` * `UGA` * `UHD16K` * `UHD4K` * `UHD8K` * `UHDPlus` * `UNKNOWN` * `UWQHD` * `UXGA` * `VGA` * `WHSXGA` * `WHUXGA` * `WHXGA` * `WQSXGA` * `WQUXGA` * `WQVGA` * `WQVGA2` * `WQVGA3` * `WQXGA` * `WQXGA2` * `WSVGA` * `WSVGA2` * `WSXGA` * `WSXGAPlus` * `WUXGA` * `WVGA` * `WVGA2` * `WXGA` * `WXGA2` * `WXGA3` * `WXGAPlus` * `XGA` * `XGAPLUS` * `_1280x854` * `nHD` * `qHD` |
| doubleProperties | [DoubleProperty[]](#openapi-definition-DoubleProperty) | Список пользовательских свойств пользовательской сессии с числовыми значениями с плавающей точкой. |
| duration | integer | Длительность пользовательской сессии в миллисекундах.  Вычисляется как промежуток времени между началом первого пользовательского действия и концом последнего пользовательского действия. |
| endReason | string | Причина окончания пользовательской сессии. Возможные значения: * `DURATION_LIMIT` * `END_EVENT` * `EXTENDED_TIMEOUT` * `TEST_FAILED` * `TIMEOUT` * `USER_ACTION_LIMIT` |
| endTime | integer | Метка времени последнего пользовательского действия в пользовательской сессии в миллисекундах UTC. |
| errors | [UserSessionErrors[]](#openapi-definition-UserSessionErrors) | Список ошибок, записанных в пользовательской сессии. |
| events | [UserSessionEvents[]](#openapi-definition-UserSessionEvents) | Список дополнительных событий, записанных в пользовательской сессии. |
| hasCrash | boolean | Пользовательская сессия включает (`true`) или не включает (`false`) сбой. |
| hasError | boolean | Пользовательская сессия включает (`true`) или не включает (`false`) ошибку. |
| hasSessionReplay | boolean | Session Replay доступен (`true`) или недоступен (`false`) для сессии. |
| internalUserId | string | Уникальный ID пользователя, инициировавшего пользовательскую сессию. |
| ip | string | IP-адрес (IPv4 или IPv6), из которого происходит пользовательская сессия. |
| isp | string | Интернет-провайдер, от которого происходит пользовательская сессия (на основе IP-адреса). |
| longProperties | [LongProperty[]](#openapi-definition-LongProperty) | Список пользовательских свойств пользовательской сессии с целочисленными (short или long) значениями. |
| manufacturer | string | Обнаруженный производитель устройства, использованного для пользовательской сессии. |
| matchingConversionGoals | string[] | Список целей конверсии, достигнутых в пользовательской сессии.  Дополнительно можно задать цели конверсии для отдельного пользовательского действия. |
| matchingConversionGoalsCount | integer | Количество целей конверсии, достигнутых в пользовательской сессии. |
| networkTechnology | string | Информация о сетевой технологии мобильной пользовательской сессии. |
| newUser | boolean | Пользователь новый (`true`) или вернувшийся (`false`). |
| numberOfRageClicks | integer | Количество rage-кликов, обнаруженных в пользовательской сессии. |
| numberOfRageTaps | integer | Количество rage-тапов, обнаруженных в пользовательской сессии. |
| osFamily | string | Тип операционной системы, использованной для пользовательской сессии. |
| osVersion | string | Версия операционной системы, использованной для пользовательской сессии. |
| partNumber | integer | Пользовательские сессии могут разбиваться на несколько частей по разным техническим причинам (например, после 200 пользовательских действий). Этот `partNumber` представляет номер каждой части всей пользовательской сессии. |
| reasonForNoSessionReplay | string | Причина отсутствия Session Replay. Возможные значения: * `KILLED_EMERGENCY` * `KILLED_ERROR` * `KILLED_INVALID_RESPONSE` * `KILLED_MIN_JS_AGENT_VERSION` * `KILLED_NO_LICENSE` * `KILLED_WRONG_CONTENT_TYPE` * `MISCONFIGURED_CLUSTER` * `MODULE_DISABLED` * `NO_ACTIVITY` * `OPTED_OUT_SESSION` * `OPT_IN_MODE` * `ROBOT_DETECTED` * `SAMPLED_OUT` * `UNABLE_TO_LOAD_WORKER` * `UNHANDLED_EXCEPTION` * `UNKNOWN` * `UNKNOWN_DOC_LOADED` * `UNSUPPORTED_BROWSER` * `VIEW_EXCLUDED` |
| reasonForNoSessionReplayMobile | string | Причина отсутствия Session Replay на мобильных устройствах. Возможные значения: * `COST_CONTROL` * `CRASHES_OPTED_IN` * `DISABLED` * `FULL_STORAGE` * `INVALID_CONFIGURATION` * `NO_AGENT` * `OPTED_OUT` * `RETENTION_TIME` * `UNKNOWN` |
| region | string | Регион, из которого происходит пользовательская сессия (на основе IP-адреса). |
| replayEnd | integer | Метка времени окончания Session Replay в миллисекундах UTC. |
| replayStart | integer | Метка времени начала Session Replay в миллисекундах UTC. |
| rootedOrJailbroken | boolean | Мобильное устройство имеет root/jailbreak (`true`) или оригинальное (`false`).  Имеет значение `null`, если статус неизвестен или не определён. Пользовательские приложения всегда сообщают неизвестно/не определено. |
| screenHeight | integer | Обнаруженная высота экрана устройства, использованного для пользовательской сессии. |
| screenOrientation | string | Обнаруженная ориентация экрана устройства, использованного для пользовательской сессии. Возможные значения: * `LANDSCAPE` * `PORTRAIT` * `UNDEFINED` |
| screenWidth | integer | Обнаруженная ширина экрана устройства, использованного для пользовательской сессии. |
| startTime | integer | Метка времени первого пользовательского действия в пользовательской сессии в миллисекундах UTC. |
| stringProperties | [StringProperty[]](#openapi-definition-StringProperty) | Список пользовательских свойств пользовательской сессии со строковыми значениями. |
| syntheticEvents | [UserSessionSyntheticEvent[]](#openapi-definition-UserSessionSyntheticEvent) | Список synthetic-событий, записанных в пользовательской сессии. |
| tenantId | string | ID окружения Dynatrace, захватившего пользовательскую сессию.  Это поле нельзя запросить через User Session Query Language. |
| totalErrorCount | integer | Количество ошибок, обнаруженных в пользовательской сессии. |
| totalLicenseCreditCount | integer | Количество результирующих оплачиваемых сессий: [Dynatrace classic licensing](https://dt-url.net/u24c0pga?dt=m), [Dynatrace Platform Subscription](https://www.dynatrace.com/support/help/shortlink/dps-dem). |
| userActionCount | integer | Количество пользовательских действий в пользовательской сессии. |
| userActions | [UserSessionUserAction[]](#openapi-definition-UserSessionUserAction) | Список пользовательских действий, записанных в пользовательской сессии. |
| userExperienceScore | string | Оценка пользовательского опыта пользовательской сессии. Возможные значения: * `FRUSTRATED` * `SATISFIED` * `TOLERATED` * `UNDEFINED` |
| userId | string | ID пользователя, предоставленный для пользовательской сессии тегированием сессий. |
| userSessionId | string | Уникальный ID пользовательской сессии. |
| userType | string | Тип пользователя. Указывает либо реального человека (`REAL_USER`), либо робота (`ROBOT` или `SYNTHETIC`). Возможные значения: * `REAL_USER` * `ROBOT` * `SYNTHETIC` |

#### Объект `DateProperty`

Пользовательское свойство пользовательского действия со значением-датой.

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Пользовательский ключ свойства. |
| value | string | Значение свойства типа дата. |

#### Объект `DoubleProperty`

Пользовательское свойство пользовательского действия со значением Double.

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Пользовательский ключ свойства. |
| value | number | Числовое значение свойства с плавающей точкой. |

#### Объект `UserSessionErrors`

Ошибка пользовательской сессии.

| Элемент | Тип | Описание |
| --- | --- | --- |
| application | string | Имя приложения на основе настроенных правил обнаружения. |
| domain | string | DNS-домен, в котором была записана ошибка. |
| internalApplicationId | string | ID сущности Dynatrace приложения.  Эта информация полезна при вызове различных REST API, например, в качестве ключа для запросов временных рядов. |
| name | string | Имя ошибки. |
| startTime | integer | Метка времени ошибки в миллисекундах UTC. |
| type | string | Тип ошибки. Возможные значения: * `Behavioral` * `Crash` * `Error` * `PageChange` * `RageClick` * `RageTap` * `UserTag` * `UserTagFromMetaData` * `VisitTag` |

#### Объект `UserSessionEvents`

Внешнее событие пользовательской сессии.

| Элемент | Тип | Описание |
| --- | --- | --- |
| application | string | Имя приложения на основе настроенных правил обнаружения. |
| domain | string | DNS-домен, в котором было записано событие. |
| internalApplicationId | string | ID сущности Dynatrace приложения.  Эта информация полезна при вызове различных REST API, например, в качестве ключа для запросов временных рядов. |
| metadata | string | Метаданные, прикреплённые к событию. |
| name | string | Имя события. |
| page | string | Имя страницы, на которую перешёл пользователь во время события смены страницы. |
| pageGroup | string | Группа страниц автоматически выводится из страницы. |
| pageReferrer | string | Имя предыдущей страницы, с которой пользователь перешёл во время события смены страницы. |
| pageReferrerGroup | string | Группа реферера страницы автоматически выводится из реферера страницы. |
| startTime | integer | Метка времени события в миллисекундах UTC. |
| type | string | Тип события. Возможные значения: * `Behavioral` * `Crash` * `Error` * `PageChange` * `RageClick` * `RageTap` * `UserTag` * `UserTagFromMetaData` * `VisitTag` |

#### Объект `LongProperty`

Пользовательское свойство пользовательского действия со значением Long.

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Пользовательский ключ свойства. |
| value | integer | Значение свойства типа Long. |

#### Объект `StringProperty`

Пользовательское свойство пользовательского действия со строковым значением.

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Пользовательский ключ свойства. |
| value | string | Строковое значение свойства. |

#### Объект `UserSessionSyntheticEvent`

Synthetic-событие пользовательской сессии.

| Элемент | Тип | Описание |
| --- | --- | --- |
| errorCode | integer | Код ошибки, произошедшей во время этого события. |
| errorName | string | Описание ошибки, произошедшей во время этого события. |
| name | string | Имя synthetic-события. |
| sequenceNumber | integer | Порядковый номер synthetic-события в рамках полного браузерного монитора. |
| syntheticEventId | string | ID сущности Dynatrace для synthetic-события. |
| timestamp | integer | Метка времени, когда synthetic-событие было смоделировано, в миллисекундах UTC. |
| type | string | Тип synthetic-события. Например, click или keystroke. |

#### Объект `UserSessionUserAction`

Пользовательское действие.

Пользовательское действие это одно действие, выполняемое пользователем в рамках пользовательской сессии, например щелчок мышью.

| Элемент | Тип | Описание |
| --- | --- | --- |
| apdexCategory | string | [Индекс пользовательского опыта](https://dt-url.net/apdexdoc?dt=m) пользовательского действия. Возможные значения: * `FRUSTRATED` * `SATISFIED` * `TOLERATING` * `UNKNOWN` |
| application | string | Имя приложения, в котором было записано пользовательское действие. |
| cdnBusyTime | integer | Время ожидания CDN-ресурсов для пользовательского действия в миллисекундах. |
| cdnResources | integer | Количество ресурсов, полученных из CDN для пользовательского действия. |
| cumulativeLayoutShift | number | Cumulative layout shift (CLS) это суммарная величина всех отдельных оценок каждого неожиданного сдвига макета, происходящего в течение всего времени жизни страницы.  CLS это важная ориентированная на пользователя метрика для измерения визуальной стабильности. Она количественно оценивает, как часто пользователи сталкиваются с неожиданными сдвигами макета. Низкий CLS означает, что страница приятна в использовании. |
| customErrorCount | integer | Общее количество пользовательских ошибок во время пользовательского действия. |
| dateProperties | [DateProperty[]](#openapi-definition-DateProperty) | Список пользовательских свойств пользовательской сессии со значениями-датами. |
| documentInteractiveTime | integer | Время, прошедшее до того, как документ для пользовательского действия стал интерактивным, в миллисекундах. |
| domCompleteTime | integer | Время до завершения построения DOM-дерева в миллисекундах. |
| domContentLoadedTime | integer | Время до загрузки DOM-дерева в миллисекундах. |
| domain | string | DNS-домен, в котором было записано пользовательское действие. |
| doubleProperties | [DoubleProperty[]](#openapi-definition-DoubleProperty) | Список пользовательских свойств пользовательской сессии с числовыми значениями с плавающей точкой. |
| duration | integer | Длительность пользовательского действия в миллисекундах.  Вычисляется как промежуток времени между начальной и конечной метками времени пользовательского действия. |
| endTime | integer | Конечная метка времени пользовательского действия в миллисекундах UTC. |
| firstInputDelay | integer | First input delay (FID) это время (в миллисекундах), которое потребовалось браузеру для реакции на первый пользовательский ввод.  FID это важная ориентированная на пользователя метрика для измерения отзывчивости при загрузке. Она количественно оценивает пользовательский опыт при попытке взаимодействия с неотзывчивыми страницами. Низкий FID означает, что страница пригодна к использованию. |
| firstPartyBusyTime | integer | Время ожидания ресурсов с исходного сервера для пользовательского действия в миллисекундах. |
| firstPartyResources | integer | Количество ресурсов, полученных с исходного сервера для пользовательского действия. |
| frontendTime | integer | Время, затраченное на рендеринг на фронтенде для пользовательского действия, в миллисекундах. |
| hasCrash | boolean | Пользовательское действие содержит (`true`) или не содержит (`false`) сбой. |
| internalApplicationId | string | ID сущности Dynatrace приложения, в котором было записано пользовательское действие.  Эта информация полезна при вызове различных REST API, например в качестве ключа для запросов временных рядов. |
| internalKeyUserActionId | string | ID сущности Dynatrace ключевого пользовательского действия. |
| javascriptErrorCount | integer | Общее количество ошибок Javascript во время пользовательского действия. |
| keyUserAction | boolean | Действие является (`true`) или не является (`false`) ключевым действием. |
| largestContentfulPaint | integer | Largest contentful paint (LCP) это время (в миллисекундах), которое потребовалось для рендеринга самого крупного элемента на странице.  LCP это важная ориентированная на пользователя метрика для измерения скорости загрузки. Она отмечает момент, когда основное содержимое страницы, вероятно, загружено. Низкий LCP означает, что страница загружается быстро. |
| loadEventEnd | integer | Время до окончания события load в миллисекундах. |
| loadEventStart | integer | Время до начала события load в миллисекундах. |
| longProperties | [LongProperty[]](#openapi-definition-LongProperty) | Список пользовательских свойств пользовательской сессии с целочисленными (short или long) значениями. |
| matchingConversionGoals | string[] | Список целей конверсии, достигнутых пользовательским действием.  Дополнительно можно задать цели конверсии для пользовательской сессии в целом. |
| name | string | Имя пользовательского действия.  Обычно это имя страницы, загружаемой в рамках пользовательского действия, или текстовое описание действия, например щелчок мышью. |
| navigationStart | integer | Метка времени начала навигации в миллисекундах UTC. |
| networkTime | integer | Время, затраченное на передачу данных для пользовательского действия, в миллисекундах. |
| requestErrorCount | integer | Общее количество ошибок запросов во время пользовательского действия. |
| requestStart | integer | Время до начала запроса в миллисекундах. |
| responseEnd | integer | Время до окончания ответа в миллисекундах. |
| responseStart | integer | Время до начала ответа в миллисекундах. |
| serverTime | integer | Время, затраченное на серверную обработку для пользовательского действия, в миллисекундах. |
| speedIndex | integer | [Speed index](https://dt-url.net/qk1a3r19?dt=m) пользовательского действия в миллисекундах.  Вычисляется как среднее время отображения всех видимых частей страницы. |
| startTime | integer | Начальная метка времени пользовательского действия в миллисекундах UTC. |
| stringProperties | [StringProperty[]](#openapi-definition-StringProperty) | Список пользовательских свойств пользовательской сессии со строковыми значениями. |
| syntheticEvent | string | Имя [Synthetic-события](https://dt-url.net/dq1e3rmm?dt=m), инициировавшего пользовательское действие. |
| syntheticEventId | string | ID [Synthetic-события](https://dt-url.net/dq1e3rmm?dt=m), инициировавшего пользовательское действие. |
| targetUrl | string | Целевой URL пользовательского действия. |
| thirdPartyBusyTime | integer | Время ожидания сторонних ресурсов для пользовательского действия в миллисекундах. |
| thirdPartyResources | integer | Количество сторонних ресурсов, загруженных для пользовательского действия. |
| ~~totalBlockingTime~~ | integer | УСТАРЕЛО  Total blocking time это суммарное время (в миллисекундах) между first contentful paint и time to interactive, в течение которого браузер был заблокирован достаточно долго, чтобы помешать отзывчивости на ввод. |
| type | string | Тип пользовательского действия. Возможные значения: * `Custom` * `EndVisit` * `Error` * `Load` * `RageClick` * `SyntheticHiddenAction` * `UserSessionProperties` * `VisitTag` * `Xhr` |
| userActionPropertyCount | integer | Общее количество свойств в пользовательском действии. |
| visuallyCompleteTime | integer | Время до того, как страница станет [визуально завершённой](https://dt-url.net/qk1a3r19?dt=m), в миллисекундах. |

## Связанные темы

* [Пользовательские запросы, сегментация и агрегация данных сессий](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как обращаться к данным пользовательских сессий и запрашивать их с помощью ключевых слов, синтаксиса, функций и многого другого.")