---
title: Средства контроля безопасности данных
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-security/data-security-controls
scraped: 2026-03-05T21:37:27.232057
---

* Latest Dynatrace

## Обзор средств контроля безопасности данных

![data-security-overview-saas-v2](https://dt-cdn.net/images/data-security-overview-saas-v2-3982-b71494b7fa.png)

## Хранение данных

Данные хранятся в дата-центрах Amazon Web Services (AWS), Microsoft Azure или Google Cloud. Доступные регионы перечислены ниже.

#### Регионы AWS

* US East (N. Virginia)
* US West (Oregon)
* Europe (Ireland)
* Asia Pacific (Sydney)
* Europe (London)[1](#fn-1-1-def)
* Europe (Frankfurt)[1](#fn-1-1-def)
* Canada (Central)[1](#fn-1-1-def)
* South America (São Paulo)[1](#fn-1-1-def)
* Asia Pacific (Singapore)[1](#fn-1-1-def)
* Asia Pacific (Mumbai)[1](#fn-1-1-def)
* Asia Pacific (Tokyo)[1](#fn-1-1-def)
* Middle East (Tel Aviv)[1](#fn-1-1-def)

1

Доступно по запросу. Обратитесь к вашему менеджеру по продажам Dynatrace.

#### Регионы Azure[1](#fn-2-1-def)

* East US (Virginia)
* West US 3 (Arizona)
* West Europe (Netherlands)
* Canada Central (Toronto)
* UAE (Dubai)
* Switzerland North (Zurich)
* Australia East (Sydney)

1

Доступно по запросу. Обратитесь к вашему менеджеру по продажам Dynatrace.

#### Регионы Google Cloud[1](#fn-3-1-def)

* us-east4 (N. Virginia)
* europe-west3 (Frankfurt)

1

Доступно по запросу. Обратитесь к вашему менеджеру по продажам Dynatrace.

Также см. [Сроки хранения данных](../data-privacy/data-retention-periods.md "Проверьте сроки хранения различных типов данных.").

## Компоненты Dynatrace

[Dynatrace OneAgent](../../../platform/oneagent.md "Узнайте о возможностях мониторинга OneAgent.") собирает все данные мониторинга в вашей контролируемой среде. При необходимости все данные, собранные OneAgent, могут маршрутизироваться через [Dynatrace ActiveGate](../../../ingest-from/dynatrace-activegate.md "Ознакомьтесь с основными концепциями ActiveGate."), который работает как прокси-сервер между Dynatrace OneAgent и кластером Dynatrace. При отсутствии ActiveGate данные, собранные OneAgent, отправляются напрямую в кластер Dynatrace.

![saas-dynatrace-components](https://dt-cdn.net/images/saas-dynatrace-components-2690-a37591adb1.png)

## Разделение данных между клиентскими средами

Dynatrace SaaS использует мультитенантную архитектуру с высокой доступностью. Dynatrace выделяет каждому клиенту тенант — так называемую среду Dynatrace. Клиенты также могут управлять несколькими средами в системе управления учётными записями Dynatrace. Каждая среда получает собственный индивидуальный домен.

В последней версии Dynatrace все данные платформы Dynatrace в состоянии покоя, включая данные из Grail, AppEngine и AutomationEngine, хранятся в отдельном выделенном хранилище. Одна среда Dynatrace SaaS, размещённая на AWS, использует выделенное хранилище AWS S3. Среды, размещённые на Azure, используют выделенные учётные записи хранилища Azure. Другие данные, такие как [данные хранилища учётных данных Dynatrace](../../../../common/manage/credential-vault.md "Храните и управляйте учётными данными в хранилище учётных данных.") или [данные учётной записи Dynatrace](../../account-management.md "Управляйте лицензией, учётными записями, внедрением платформы и состоянием среды Dynatrace."), хранятся в базах данных с использованием логического разделения данных.

Прикладной уровень, на котором данные обрабатываются перед сохранением в состоянии покоя, размещён на высокомасштабируемой общей облачной инфраструктуре.

Отдельное хранилище в настоящее время доступно для Dynatrace SaaS на AWS и Azure. Поддержка Dynatrace SaaS на Google Cloud планируется.

![Разделение данных на платформе Dynatrace](https://dt-cdn.net/images/dynatrace-platform-data-separation-doc-2662-d52d653a45.png)

## Шифрование данных в состоянии покоя

Все данные мониторинга Dynatrace SaaS шифруются в состоянии покоя с использованием AES-256. В последней версии Dynatrace все данные платформы Dynatrace, включая данные из Grail, AppEngine и AutomationEngine, хранятся в отдельном выделенном хранилище. Каждое хранилище шифруется уникальным ключом шифрования, который ротируется каждые 365 дней. Dynatrace управляет ключами шифрования.

Отдельное хранение данных и уникальные ключи шифрования в настоящее время доступны для Dynatrace SaaS на AWS и Azure. Поддержка Dynatrace SaaS на Google Cloud планируется.

![Шифрование данных платформы Dynatrace SaaS в состоянии покоя](https://dt-cdn.net/images/dynatrace-platform-data-encryption-doc-2772-2da248ac18.png)

## Шифрование данных при передаче

Все данные, передаваемые между OneAgent, ActiveGate и кластером Dynatrace, шифруются при передаче. Данные сериализуются и десериализуются с использованием Google Protocol Buffers.

Dynatrace SaaS поддерживает TLS 1.2 и TLS 1.3 (оценка SSL Labs A+).

![dynatrace-data-security-encryption-in-transit](https://dt-cdn.net/images/dynatrace-data-security-encryption-in-transit-2690-c09d771883.png)

## Аутентификация пользователей

Вы можете управлять пользователями, настраивая [группы пользователей и разрешения](../../identity-access-management/permission-management/role-based-permissions.md "Разрешения на основе ролей") и [SAML](../../identity-access-management/user-and-group-management/access-saml.md "SAML").

![dynatrace-data-security-user-authentication](https://dt-cdn.net/images/dynatrace-data-security-user-authentication-2690-9a645c42f8.png)

## Проверка целостности компонентов Dynatrace

Компоненты Dynatrace подписываются с помощью сертификатов подписи кода в конвейере непрерывной доставки и интеграции (CI/CD).

Сертификаты подписи кода хранятся на аппаратных токенах с сертификатами расширенной проверки (EV) для подписи кода Windows. Проверка подписи выполняется автоматически перед обновлением или установкой. При первой установке компонента проверка подписи должна быть выполнена вручную.

![dynatrace-data-security-integrity-verification](https://dt-cdn.net/images/dynatrace-data-security-integrity-verification-2905-53a43d8705.png)

## Непрерывность бизнеса и высокая доступность

Dynatrace SaaS использует кластерную архитектуру, множество зон доступности (дата-центров) и механизмы автоматического переключения при отказе для обеспечения высокой доступности ([SLA доступности 99,5%](https://www.dynatrace.com/company/trust-center/sla/saas/)).

![dynatrace-data-security-high-availability](https://dt-cdn.net/images/dynatrace-data-security-high-availability-2772-a154b24478.png)

## Резервное копирование данных и аварийное восстановление

* **AWS:** Каждые 24 часа Dynatrace SaaS на AWS выполняет резервное копирование данных в другую учётную запись AWS в том же регионе AWS. Резервная копия включает данные, собранные как минимум за последние 30 дней. Максимальная целевая точка восстановления (RPO) для полного кластера составляет 24 часа. Целевое время восстановления (RTO) составляет до 24 часов в зависимости от размера кластера.
* **Azure:** Каждые 24 часа Dynatrace SaaS на Azure выполняет резервное копирование данных в другую подписку Azure в том же регионе Azure. Резервная копия включает данные, собранные как минимум за последние 30 дней. Максимальная целевая точка восстановления (RPO) для полного кластера составляет 24 часа. Целевое время восстановления (RTO) составляет до 24 часов в зависимости от размера кластера.
* **Google Cloud:** Каждые 24 часа Dynatrace SaaS на Google Cloud выполняет резервное копирование данных в другой проект Google Cloud в том же регионе Google Cloud. Резервная копия включает данные, собранные как минимум за последние 30 дней. Максимальная целевая точка восстановления (RPO) для полного кластера составляет 24 часа. Целевое время восстановления (RTO) составляет до 24 часов в зависимости от размера кластера.

![dynatrace-data-security-backup](https://dt-cdn.net/images/dynatrace-data-security-backup-2690-e30ecd18aa.png)

## Мониторинг инфраструктуры

Выделенный кластер самомониторинга Dynatrace отслеживает доступность, производительность и безопасность всех SaaS-кластеров. При обнаружении проблемы команда Dynatrace ACE (Autonomous Cloud Enablement), работающая в режиме 24/7, немедленно уведомляется. Операционный статус и инциденты всегда доступны на [dynatrace.status.io](https://dynatrace.status.io/).

![dynatrace-data-security-infrastructure-monitoring](https://dt-cdn.net/images/dynatrace-data-security-infrastructure-monitoring-2612-10a1faea42.png)

## Развёртывание обновлений и исправлений

Используя полностью автоматизированный конвейер CI/CD, Dynatrace может развёртывать обновления и исправления в течение нескольких часов. Архитектура Dynatrace обеспечивает обновление кластеров без простоев.

Новые функции выпускаются каждые две недели. Обновления Dynatrace ActiveGate и OneAgent могут выполняться автоматически или вручную.

![dynatrace-data-security-rollout-updates](https://dt-cdn.net/images/dynatrace-data-security-rollout-updates-2892-9efe1ac573.png)

## Журналы аудита

Dynatrace записывает в журнал события, связанные с безопасностью, такие как изменения конфигурации и доступ к среде. Вы можете просматривать эти журналы аудита в [Dynatrace](../configuration/audit-logs-api.md "Узнайте, как управлять журналами аудита с помощью API.") или скачивать их для дальнейшего использования через вызов API [GET audit log](../../../dynatrace-api/environment-api/audit-logs/get-log.md "Просмотр полного журнала аудита через API Dynatrace.").

![dynatrace-data-security-audit-logs](https://dt-cdn.net/images/dynatrace-data-security-audit-logs-2635-7349637e51.png)

## Доступ к данным для службы поддержки Dynatrace

Доступ к средам Dynatrace SaaS основан на ролях. Изменения ролей требуют обоснования и одобрения командой Dynatrace ACE (Autonomous Cloud Enablement). Доступ ограничен корпоративной сетью Dynatrace и требует многофакторной аутентификации при удалённом доступе. Каждый доступ и все изменения [записываются в журнал аудита](../configuration/audit-logs-api.md "Узнайте, как управлять журналами аудита с помощью API.") и полностью доступны для просмотра.

![dynatrace-data-security-data-access-support](https://dt-cdn.net/images/dynatrace-data-security-data-access-support-2791-ebcc4e889e.png)

## Предотвращение утечки секретов Dynatrace

Dynatrace может обнаруживать и предотвращать утечку секретов Dynatrace в репозиториях исходного кода на GitHub. Эти секреты могут включать токены платформы или API, которые были случайно отправлены в репозиторий исходного кода. При обнаружении утечки секрета мы свяжемся с вами и поможем с мерами по устранению.

Подробнее о сообщении о проблеме безопасности см. [Сообщить о проблеме, связанной с безопасностью](report-a-security-related-concern.md "Узнайте, как сообщить об уязвимостях и к кому обращаться при возникновении проблем безопасности.").

![dynatrace-data-security-secret-leak-prevention](https://dt-cdn.net/images/dynatrace-data-security-secret-leak-prevention-2575-f100e468bf.png)

## Соответствие требованиям, сертификации и аудиты

Dynatrace ежегодно проходит независимые сторонние аудиты и проводит тесты на проникновение и оценку Red Team с участием независимых фирм по информационной безопасности.

Наличие множества глобальных и локальных сертификаций и аккредитаций демонстрирует, что мы соблюдаем наиболее признанные международные стандарты управления безопасностью.

Dynatrace также пользуется преимуществами защищённых дата-центров Amazon, Azure и Google, которые сертифицированы по ISO 27001, PCI-DSS Level 1 и SOC 1/SSAE-16.

Полный список сертификаций см. в [Центре доверия](https://www.dynatrace.com/company/trust-center/).

## Защита во время выполнения

Dynatrace SaaS защищается с помощью [Dynatrace Application Security](https://www.dynatrace.com/platform/application-security/).

Вредоносная активность блокируется с помощью функции [Runtime Application Protection](../../../secure/application-security/application-protection.md "Настройте Dynatrace Runtime Application Protection для мониторинга атак и уязвимостей на уровне кода, генерируемых атаками.").

Уязвимости сторонних компонентов и кода [обнаруживаются в реальном времени и автоматически сообщаются](../../../secure/application-security/vulnerability-analytics.md "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и кода, отслеживание хода устранения и создание правил мониторинга.") команде безопасности Dynatrace.

![Защита данных Dynatrace](https://dt-cdn.net/images/data-security-dynatrace-protection-1915-5d93f4245d.png)
