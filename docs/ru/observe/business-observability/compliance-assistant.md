---
title: Помощник соответствия
source: https://www.dynatrace.com/docs/observe/business-observability/compliance-assistant
scraped: 2026-03-06T21:14:30.942740
---

# Compliance Assistant

# Compliance Assistant

* Последняя версия Dynatrace
* Приложение
* 3 мин. чтения
* Обновлено 4 февраля 2026 г.
* Предварительная версия

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** поддерживает и помогает вам:

* Отслеживать, управлять и автоматизировать соответствие требованиям в ИТ и бизнес-ландшафте.
* Получать актуальную видимость рисков соответствия с нормативными актами и сертификациями "из коробки".
* Следить за состоянием соответствия в критически важных бизнес-процессах для обеспечения непрерывного мониторинга и автоматической классификации инцидентов.

Предварительные требования

### Установка

Убедитесь, что приложение [установлено в вашей среде](../../manage/hub.md#install "Информация о Dynatrace Hub.").

### Разрешения

В следующей таблице описаны необходимые разрешения.

storage:buckets:read

Чтение bucket'ов

storage:events:read

Чтение событий

storage:entities:read

Чтение таблицы сущностей

storage:metrics:read

Требуется для правила обнаружения Istio findings

storage:filter-segments:read

Чтение filter-segments

settings:objects:read

Требуется для чтения настроек приёма журналов

settings:schemas:read

Чтение схем настроек

state:app-states:read

Требуется для чтения состояния приложения

hub:catalog:read

Требуется для чтения версии приложения

storage:security.events:read

Требуется для получения событий безопасности

### Настройка источников и приложений

Чтобы в полной мере воспользоваться **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant"), начните с [![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow**](business-flow.md "Мониторинг и анализ критически важных бизнес-процессов. Отслеживание ключевых показателей эффективности (KPI), обнаружение аномалий процессов и приоритизация возможностей оптимизации для улучшения бизнес-результатов.") для мониторинга и анализа бизнес-процессов, критически важных для соответствия требованиям.

Чтобы максимизировать ценность данных об управлении рисками, настройте источники данных для [событий безопасности](../../secure/threat-observability/concepts.md#security-data "Базовые понятия, связанные с Threat Observability") из отслеживаемой среды или сторонних источников. Данные, связанные с безопасностью, включают [события уязвимостей](../../secure/threat-observability/concepts.md#vuln-events "Базовые понятия, связанные с Threat Observability"), [события соответствия](../../secure/threat-observability/concepts.md#compliance "Базовые понятия, связанные с Threat Observability") и [события обнаружения угроз](../../secure/threat-observability/concepts.md#detection "Базовые понятия, связанные с Threat Observability").

![Получение видимости состояния соответствия в ИТ и бизнес-ландшафте](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.compliance.assistant/media/afdf37e4-9501-479f-803b-cf3cbecf62c1.png)![Картирование критических бизнес-процессов и выявление пробелов в соответствии с сигналами для конкретных фреймворков](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.compliance.assistant/media/81eb7b08-1a02-4d32-aa27-f7d5bb137496.png)![Автоматическое обнаружение и классификация инцидентов на основе нормативных порогов и критериев воздействия](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.compliance.assistant/media/a5d01e06-ec63-40bd-811e-d764651b8024.png)

1 из 3. Получение видимости состояния соответствия в ИТ и бизнес-ландшафте.

## Начало работы

**Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") предлагает возможности мониторинга и автоматизации, адаптированные к конкретным фреймворкам соответствия. Для начала управления соответствием настройте [фреймворк соответствия](#compliance-framework), применимый к вашей организации.

### Настройка фреймворка соответствия

1. В Dynatrace перейдите к **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant").
2. Выберите **Set up framework** (Настроить фреймворк).
3. Чтобы выбрать фреймворк соответствия для мониторинга, выберите нужный фреймворк. В настоящее время **DORA** — единственный доступный фреймворк в **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant").
4. Выберите **Next** (Далее).
5. Чтобы выбрать критически важные или важные функции (CIF), выберите все бизнес-процессы, критически важные для соответствия. Если CIF недоступны, создайте новый [бизнес-процесс с конфигурацией как сущность](business-flow/set-up-business-flow.md#set-a-business-flow-configuration-as-an-entity "Следуйте инструкциям по успешной настройке Business Flow.") в **Business Flow** ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow").
6. Выберите **Next** (Далее).
7. Чтобы в полной мере воспользоваться возможностями управления рисками ИКТ, убедитесь, что источники данных для [событий безопасности](../../secure/threat-observability/concepts.md#security-data "Базовые понятия, связанные с Threat Observability") правильно настроены в вашей среде.

#### Если уязвимости не включены

1. Выберите **Set up RVA** (Настроить RVA), чтобы перейти в **Vulnerability Analytics: General settings** и включить [Runtime Vulnerabilities Analytics](../../secure/application-security/vulnerability-analytics.md "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и на уровне кода, отслеживание прогресса устранения и создание правил мониторинга."). Там есть две вкладки: **Third-party Vulnerability Analytics** и **Code-level Vulnerability Analytics**. Вы можете включить одну или несколько опций.
2. Для мониторинга уязвимостей сторонних компонентов [включите обнаружение сторонних уязвимостей](../../secure/application-security/vulnerability-analytics.md#tpv-detection "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и на уровне кода, отслеживание прогресса устранения и создание правил мониторинга.").
3. Для мониторинга уязвимостей на уровне кода [включите обнаружение уязвимостей на уровне кода](../../secure/application-security/vulnerability-analytics.md#clv-detection "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и на уровне кода, отслеживание прогресса устранения и создание правил мониторинга.").
4. Для интеграции внешних данных безопасности в [Grail](../../platform/grail.md "Информация о том, что и как можно запрашивать в данных Dynatrace.") можно принимать [события уязвимостей](../../secure/threat-observability/concepts.md#vuln-events "Базовые понятия, связанные с Threat Observability") из сторонних продуктов. Список поддерживаемых интеграций см. в [Security integrations](../../secure/threat-observability/security-events-ingest.md "Приём внешних данных безопасности в Grail.").
5. Выберите **Done** (Готово).

#### Если результаты обнаружения угроз безопасности не включены

1. Выберите **Set up RAP** (Настроить RAP), чтобы перейти в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Analyze and alert** > **Application security** > **Application protection** и [включить Runtime Application Protection](../../secure/application-security/application-protection.md#start "Настройка и конфигурирование Dynatrace Runtime Application Protection для мониторинга атак и уязвимостей на уровне кода, вызванных атаками.").
2. Для интеграции внешних данных безопасности в Grail можно принимать [события обнаружения угроз](../../secure/threat-observability/concepts.md#detection "Базовые понятия, связанные с Threat Observability") из сторонних продуктов. Список поддерживаемых интеграций см. в [Security integrations](../../secure/threat-observability/security-events-ingest.md "Приём внешних данных безопасности в Grail.").
3. Выберите **Done** (Готово).

#### Если правила конфигурации активов ИКТ не включены

1. Выберите **Set up KSPM** (Настроить KSPM), чтобы перейти в **Security Posture Management: Kubernetes** и [включить Security Posture Management](../../ingest-from/setup-on-k8s/deployment/security-posture-management.md#enable "Настройка и включение Security Posture Management в Kubernetes.").
2. Для начала работы с Security Posture Management и настройки области оценки см. [Начало работы с Security Posture Management](../../secure/xspm.md#get-started "Обнаружение, управление и принятие мер по результатам безопасности и соответствия."). Чтобы включить DORA как поддерживаемый стандарт соответствия в области оценки, перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Analyze and alert** > **Application security** > **Security Posture Management** и включите DORA.
3. Для интеграции с внешними данными безопасности для приёма событий соответствия см. [Security integrations](../../secure/threat-observability/security-events-ingest.md "Приём внешних данных безопасности в Grail.").
4. Выберите **Done** (Готово).

### Удаление фреймворка соответствия

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Apps** > **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant").
2. В разделе соответствующего фреймворка соответствия, например **DORA**, выберите **Remove framework** (Удалить фреймворк).
3. Выберите **Remove** (Удалить) для подтверждения. Имейте в виду, что удаление фреймворка соответствия затрагивает всех пользователей **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant").

### Управление бизнес-процессами, критически важными для соответствия

**Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") позволяет сопоставлять ИТ-активы, релевантные для соответствия, со сквозными бизнес-процессами. **Compliance Assistant** интегрируется с [![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow") **Business Flow**](business-flow.md "Мониторинг и анализ критически важных бизнес-процессов.") для выявления бизнес-процессов, критически важных для соответствия, [настроенных как сущность](business-flow/set-up-business-flow.md#set-a-business-flow-configuration-as-an-entity "Следуйте инструкциям по успешной настройке Business Flow.").

#### Добавление критически важной или важной функции (CIF)

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Apps** > **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant").
2. В разделе фреймворка соответствия DORA выберите **Add CIFs** (Добавить CIF).
3. В таблице выберите бизнес-процессы для добавления в качестве CIF.
4. Выберите **Save** (Сохранить) для обновления фреймворка соответствия.

#### Удаление критически важной или важной функции (CIF)

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Apps** > **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant").
2. В разделе фреймворка соответствия DORA выберите значок меню того CIF, который нужно удалить.
3. В меню выберите **Remove CIF** (Удалить CIF).
4. Выберите **Remove** (Удалить) для подтверждения. Имейте в виду, что удаление CIF затрагивает всех пользователей **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant").

#### Редактирование расчётной стоимости инцидента в минуту

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Apps** > **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant").
2. В разделе фреймворка соответствия DORA выберите значок меню соответствующего CIF.
3. В меню выберите **Edit incident cost/min** (Изменить стоимость инцидента/мин).
4. Добавьте расчётную стоимость инцидента в минуту, используемую для расчёта экономического воздействия инцидентов, затрагивающих конкретный CIF.
5. Выберите **Save** (Сохранить).

### Управление инцидентами соответствия

**Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant"):

* Разработан для помощи в управлении инцидентами в соответствии с нормативными требованиями.
* Автоматически классифицирует инциденты на основе нормативных порогов воздействия и ускоряет отчётность о крупных инцидентах в соответствии с нормативными сроками.
* Упрощает оценку обнаруженных ИТ-системой инцидентов, затрагивающих бизнес-процессы, настроенные как CIF, разделяя их на [неклассифицированные проблемы](#unclassified-problems), [потенциальные крупные инциденты](#potential-major-incidents) и [классифицированные крупные инциденты](#classified-major-incidents).

#### Расследование и классификация потенциальных инцидентов соответствия

1. Перейдите к **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant").
2. В разделе **Incidents** (Инциденты) просмотрите таблицы [потенциальных крупных инцидентов](#potential-major-incidents) и [неклассифицированных проблем](#unclassified-problems).
3. Выберите соответствующий инцидент для просмотра следующих сведений о любом активированном пороге классификации согласно Регламенту ЕС DORA:

   * Критически важные или важные функции (CIF), затронутые инцидентом.
   * Продолжительность инцидента, рассчитанная на основе длительности основной проблемы в наносекундах. Порог существенности для данного критерия классификации достигается, когда продолжительность инцидента превышает 24 часа ([RTS по классификации инцидентов, связанных с ИКТ, и киберугроз](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401772)).
   * Экономическое воздействие инцидента рассчитывается на основе расчётной понесённой стоимости в минуту для затронутых CIF и продолжительности основной проблемы. Порог существенности для критерия классификации `Экономическое воздействие` достигается, когда затраты и потери финансовой организации из-за инцидента превысили или могут превысить €100 000 (RTS по классификации инцидентов, связанных с ИКТ, и киберугроз).
4. Чтобы классифицировать инцидент как крупный в соответствии с EU DORA, в представлении сведений об инциденте выберите **Classify as major** (Классифицировать как крупный).
5. Необязательно: добавьте комментарий для документирования своего решения. Этот комментарий добавляется к бизнес-событию классификации инцидента.
6. Выберите **Confirm** (Подтвердить).

   * Имейте в виду, что классификация запускает приём бизнес-события с деталями классифицированного инцидента соответствия, процесс может занять несколько секунд.
   * Классифицированный инцидент теперь доступен в **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") > **Incidents** > **Classified incidents** (Классифицированные инциденты).

## Понятия

### Фреймворк соответствия

Фреймворк соответствия — это структурированный набор требований, руководящих принципов и лучших практик для поддержки организаций в выполнении нормативных и отраслевых стандартов.

**Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") объединяет данные и функциональные возможности, адаптированные к конкретному фреймворку соответствия. В настоящее время **Compliance Assistant** предлагает возможности мониторинга и автоматизации для поддержки соответствия [Регламенту ЕС DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng).

### Оценка Dynatrace в снимке соответствия

Актуальная многоуровневая оценка, суммирующая текущее состояние рисков ИКТ в отношении потенциальных инцидентов, результатов обнаружения угроз, уязвимостей и неправильных конфигураций. Эта оценка является ориентировочным показателем, основанным на текущих данных и логике уровней. Она является высокоуровневым индикатором на основе актуальных данных наблюдаемости и автоматизированных систем и не заменяет комплексные или официальные оценки соответствия.

### Критически важные или важные функции (CIF)

Согласно [Регламенту ЕС DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng), финансовые организации должны выявлять, классифицировать и документировать бизнес-функции, поддерживаемые ИКТ, и их поддерживающие активы. CIF — это процессы, нарушение которых может существенно повлиять на финансовые результаты или непрерывность обслуживания.

**Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") позволяет сопоставлять ИТ-активы, релевантные для соответствия, со сквозными бизнес-процессами. Интегрируясь с **Business Flow** ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow"), вы можете выявлять бизнес-процессы, критически важные для соответствия, используя сущности Smartscape для расширенной видимости и контекста.

### Неклассифицированные проблемы

[Инциденты, обнаруженные ИТ-системой](../../../common/semantic-dictionary/model/davis.md "Знакомство с моделями семантического словаря, связанными с Davis AI."), затрагивают любой из бизнес-процессов, настроенных как CIF и отслеживаемых **Business Flow** ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow"). Инциденты считаются неклассифицированными проблемами, когда менее одного порога существенности для классификации крупных инцидентов нарушается. В соответствии с Регламентом ЕС DORA необходимо оценить, затрагивает ли инцидент сервисы ИКТ или сети и информационные системы, поддерживающие CIF [(RTS по классификации инцидентов, связанных с ИКТ, и киберугроз)](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401772).

### Потенциальные крупные инциденты

[Инциденты, обнаруженные ИТ-системой](../../../common/semantic-dictionary/model/davis.md "Знакомство с моделями семантического словаря, связанными с Davis AI."), затрагивают любой из бизнес-процессов, настроенных как CIF и отслеживаемых **Business Flow** ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow"). Инциденты считаются потенциальными крупными инцидентами, когда два или более отслеживаемых порога существенности для классификации крупных инцидентов нарушаются. В соответствии с Регламентом ЕС DORA инцидент считается крупным, когда выполняются два или более порога существенности ([RTS по классификации инцидентов, связанных с ИКТ, и киберугроз](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401772)).

### Классифицированные крупные инциденты

[Инциденты, обнаруженные ИТ-системой](../../../common/semantic-dictionary/model/davis.md "Знакомство с моделями семантического словаря, связанными с Davis AI."), затрагивают любой из бизнес-процессов, настроенных как CIF и отслеживаемых **Business Flow** ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow"), и были вручную классифицированы как крупные в соответствии с Регламентом ЕС DORA. После классификации инцидента как крупного Dynatrace автоматически создаёт бизнес-событие со снимком инцидента соответствия. Подробнее о [событиях классификации инцидентов соответствия](../../semantic-dictionary/model/business-analytics.md "Знакомство с моделями семантического словаря, связанными с Business Observability.").

### Уязвимости

**Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") опирается на [результаты обнаружения уязвимостей](../../secure/threat-observability/concepts.md#vuln-events "Базовые понятия, связанные с Threat Observability") для проактивного снижения рисков до их эскалации в инциденты. В соответствии с Регламентом ЕС DORA организации обязаны непрерывно оценивать уязвимости. Результат обнаружения уязвимости — это событие безопасности, фиксирующее обнаруженную слабость в системе, программном компоненте или среде.

### Результаты обнаружения угроз безопасности

**Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") опирается на [события обнаружения угроз](../../secure/threat-observability/concepts.md#detection "Базовые понятия, связанные с Threat Observability") для помощи в приоритизации киберрисков. В соответствии с Регламентом ЕС DORA организации обязаны непрерывно оценивать киберугрозы ([RTS по структуре управления рисками ИКТ](https://eur-lex.europa.eu/eli/reg_del/2024/1774/oj/eng)). Событие обнаружения угроз генерируется при обнаружении подозрительной активности вокруг объекта.

### Результаты конфигурации активов ИКТ

**Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") опирается на [события соответствия](../../secure/threat-observability/concepts.md#compliance "Базовые понятия, связанные с Threat Observability") для обнаружения потенциальных неправильных конфигураций. В соответствии с Регламентом ЕС DORA организации обязаны определять безопасную базовую конфигурацию для активов ИКТ, которая минимизирует подверженность киберугрозам, и регулярно проверять эффективное применение этих базовых конфигураций ([RTS по структуре управления рисками ИКТ](https://eur-lex.europa.eu/eli/reg_del/2024/1774/oj/eng)). События соответствия представляют собой оценку ресурса в контексте правила, указанного в стандарте соответствия.

## Варианты использования

Compliance Assistant позволяет достигать соответствия и управлять им в рамках поддерживаемых фреймворков:

* Выявлять и картировать ИТ-активы, релевантные для соответствия, путём анализа критически важных сквозных бизнес-процессов — способствуя межфункциональному согласованию ИТ, безопасности и бизнес-команд.
* Непрерывно отслеживать статус соответствия в соответствии с выбранным фреймворком и выявлять риски с помощью актуальных данных об уязвимостях, результатах обнаружения угроз и неправильных конфигурациях.
* Обнаруживать, классифицировать и ускорять отчётность об инцидентах, соответствующих нормативным порогам, автоматизируя шаги, необходимые для соблюдения жёстких нормативных сроков.

## Часто задаваемые вопросы

Как улучшить оценку Dynatrace в снимке соответствия?

Оценка Dynatrace — это актуальный индикатор, основанный на текущем состоянии рисков ИКТ и подверженный влиянию серьёзности выводов. Для улучшения оценки:

* Своевременно устраняйте потенциальные крупные инциденты и неклассифицированные проблемы.
* Устраняйте результаты обнаружения угроз и уязвимости. Для просмотра результатов обнаружения угроз и запуска углублённого анализа см. [Получение аналитических данных](../../secure/threats-and-exploits/gain-insights.md "Подробный анализ результатов обнаружения угроз."). Чтобы узнать, как исправить обнаруженные уязвимости, см. [Как исправить обнаруженные уязвимости?](../../secure/faq.md#fix "Часто задаваемые вопросы о Dynatrace Application Security.").
* Исправляйте неправильные конфигурации активов ИКТ, выявленные Security Posture Management. Рекомендации по исправлению выводов см. в [Соответствие требованиям с помощью Security Posture Management](../../secure/use-cases/stay-compliant.md "Соблюдение мер, политик и практик безопасности.").
* Обеспечьте надлежащий мониторинг и защиту в режиме реального времени для критически важных или важных функций (CIF).

Как часто обновляются данные о критически важных или важных функциях (CIF) в **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant")?

Данные о KPI конверсий и ошибок по CIF обновляются на основе настроенной частоты генерации мониторинга KPI в **Business Flow** ![Business Flow](https://dt-cdn.net/images/business-flow-480-362159ca2c.png "Business Flow"). Временной горизонт оценки для отслеживаемых KPI критически важных или важных функций (CIF) также определяется при настройке бизнес-конфигурации как сущности.

Чтобы обеспечить надёжную оценку KPI и избежать пропуска данных из длительных процессов, установите временной горизонт оценки не менее чем в три-четыре раза превышающим среднюю продолжительность процесса (например, если средняя продолжительность CIF составляет 5 минут, установите окно не менее 15–20 минут).

Почему настроенные критически важные или важные функции (CIF) не обновляются?

Если вы недавно отредактировали или добавили [бизнес-процессы, настроенные как сущность](business-flow/set-up-business-flow.md#set-a-business-flow-configuration-as-an-entity "Следуйте инструкциям по успешной настройке Business Flow.") и выбрали любой из них в качестве CIF в **Compliance Assistant** ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant"), обновление KPI мониторинга этих бизнес-процессов может занять до максимальной определённой частоты в **Compliance Assistant**. Частоту мониторинга можно изменить в конфигурации бизнес-потока.

## Связанные темы

* [Мониторинг бизнес-процессов](business-process-monitoring.md "Узнайте, как отслеживать бизнес-процессы.")
* [Runtime Application Protection](../../secure/application-security/application-protection.md "Настройка и конфигурирование Dynatrace Runtime Application Protection для мониторинга атак и уязвимостей на уровне кода, вызванных атаками.")
* [Security Posture Management](../../secure/application-security/spm.md "Оценка, управление и принятие мер по устранению неправильных конфигураций и нарушений стандартов безопасности и нормативных требований.")
* [Runtime Vulnerability Analytics](../../secure/application-security/vulnerability-analytics.md "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и на уровне кода, отслеживание прогресса устранения и создание правил мониторинга.")