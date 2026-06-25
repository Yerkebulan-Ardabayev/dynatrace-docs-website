---
title: Правила мониторинга Runtime Application Protection
source: https://docs.dynatrace.com/managed/secure/application-security/application-protection/application-protection-rules
scraped: 2026-05-12T12:00:46.773146
---

# Правила мониторинга Runtime Application Protection

# Правила мониторинга Runtime Application Protection

* How-to guide
* Updated on Feb 23, 2026

Что вы найдёте на этой странице

* [Как определять правила управления атаками: блокировать, отслеживать или игнорировать](#handling-rules)
* [Как создавать правила исключений (allowlist) для атак, которые считаются безопасными](#exception-rules)
* [Часто задаваемые вопросы](#faq)

Правила Dynatrace Runtime Application Protection позволяют:

* [Настраивать детальные правила мониторинга для блокировки, отслеживания или игнорирования будущих атак](#handling-rules) на основе [атрибутов ресурсов](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями Dynatrace."), а также задавать несколько условий для одного правила. При создании правила можно проверить, применяются ли условия, и сколько групп процессов будет затронуто.
  Созданные правила переопределяют глобальные настройки управления атаками для выбранной технологии.
* [Добавлять атаки, которые не считаются опасными, в allowlist](#exception-rules) по исходным IP-адресам или шаблонам атак.

## Определение правил управления конкретными атаками

1. Перейдите в **Settings** > **Application security** > **Application Protection** > **Monitoring rules**.
2. Нажмите **Add new rule**.
3. Необязательно: Назовите правило (если название не задано, оно будет присвоено автоматически при создании правила на основе заданных критериев).
4. В поле **Attack control** укажите, как управлять атакой, соответствующей критериям правила:

   * `Off; incoming attacks NOT detected or blocked.`
   * `Monitor; incoming attacks detected only.`
   * `Block; incoming attacks detected and blocked.`
5. В поле **Attack type** выберите тип атаки, к которому применяется текущая конфигурация.
6. Необязательно: Если правило должно применяться только к части среды, в разделе **Specify where the rule is applied** нажмите **Add new condition** и укажите атрибуты ресурса для идентификации этой части среды (например, `dt.entity.process_group`, `aws.region`). Подробнее см. в разделе [Обогащение данных телеметрии полями Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями Dynatrace.").
7. Необязательно: Чтобы проверить применение правила, нажмите **Preview matching process group instances**. Отобразится список экземпляров групп процессов, соответствующих критериям.
8. Нажмите **Save changes**.
9. Перезапустите процессы.

Правила можно редактировать, отключать, включать или удалять в любое время.

## Определение правил исключений (allowlist)

1. Перейдите в **Settings** > **Application Security** > **Application Protection** > **Allowlist** и нажмите **Add new exception rule**.
2. В разделе **Define attack control for chosen criteria** выберите один из вариантов:

   * `Off; incoming attacks NOT detected or blocked` — для игнорирования атак на основе заданных критериев
   * `Monitor; incoming attacks detected only` — для мониторинга атак на основе заданных критериев без их блокировки
3. В разделе **Define the rule** нажмите **Add new condition**, чтобы задать детальные условия, которые должны выполняться для разрешения атаки.

   Большинство комбинаций ключ/сопоставитель в раскрывающемся списке требуют OneAgent версии 1.309+.

   Для версий OneAgent ниже 1.309 доступны только следующие параметры:

   * ключ: `entry_point.payload`, сопоставитель: `contains`
   * ключ: `actor.ip`, сопоставитель: `is part of IP CIDR`

   Для полноценного использования этой функциональности рекомендуется использовать последнюю версию OneAgent.
4. Необязательно: Если правило должно применяться только к части среды, в разделе **Specify where the rule is applied** нажмите **Add new condition** и укажите атрибуты ресурса для идентификации этой части среды (например, `dt.entity.process_group`, `aws.region`). Подробнее см. в разделе [Обогащение данных телеметрии полями Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями Dynatrace.").
5. Необязательно: Чтобы проверить применение правила, нажмите **Preview matching process group instances**. Отобразится список экземпляров групп процессов, соответствующих критериям.
6. Нажмите **Save changes**.

Правила можно редактировать, отключать, включать или удалять в любое время.

## FAQ

* [Как именно Dynatrace блокирует атаки?](/managed/secure/faq#block-attacks "Часто задаваемые вопросы о Dynatrace Application Security.")
* [Как определяется IP-адрес злоумышленника?](/managed/secure/faq#attacker "Часто задаваемые вопросы о Dynatrace Application Security.")

## Связанные темы

* [FAQ по Application Security](/managed/secure/faq "Часто задаваемые вопросы о Dynatrace Application Security.")