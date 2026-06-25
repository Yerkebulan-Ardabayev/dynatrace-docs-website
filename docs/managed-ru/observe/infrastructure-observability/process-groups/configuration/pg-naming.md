---
title: Именование групп процессов
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/configuration/pg-naming
scraped: 2026-05-12T11:17:25.395894
---

# Process group naming

# Именование групп процессов

* How-to guide
* 6-min read
* Published Mar 21, 2018

Dynatrace не только автоматически обнаруживает [группы процессов](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring."), но и присваивает им интуитивно понятные имена, удобные для DevOps-специалистов, занимающихся их развёртыванием и мониторингом. Однако во многих случаях автоматически сгенерированные имена могут быть слишком общими или не соответствовать вашим стандартам именования. Для изменения схем именования обнаруженных групп процессов необходимо использовать правила именования групп процессов.

## Определение нового правила именования групп процессов

Чтобы добавить новое правило именования групп процессов:

1. Перейдите в **Settings**.
2. Выберите **Processes and containers** > **Process group naming**.
3. Выберите **Add a new rule**.
4. Введите имя правила.
5. Определите **Process group name format**, включая любую статическую текстовую строку, описывающую именуемую группу процессов. Доступны необязательные заменители, позволяющие легко динамически включать конкретные свойства группы процессов в схему автоматического именования. При использовании одного из определённых заменителей можно добавить [регулярное выражение](/managed/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.") для извлечения части обнаруженного значения. Например, для извлечения чего-либо из `{ProcessGroup:DetectedName}` можно использовать `{ProcessGroup:DetectedName/REGEX}`. Регулярное выражение извлекает полное совпадение. Захватывающие группы не поддерживаются — только атомарные группы и группы lookaround.
6. Добавьте одно или несколько условий (Conditions) к правилу для сопоставления групп процессов, к которым должна применяться схема именования. Условия проверяют наличие различных типов атрибутов и значений состояний — от проверки образа Docker до проверки пространства CloudFoundry, в котором работает группа процессов.

   Пример условия ниже применяется только к Java-процессам, запускаемым через JAR-файл, имя которого начинается с `com.dynatrace.easytravel`. В **Process group name format** видно, что к JAR-файлу применяется регулярное выражение.

   ![Process group naming rule example](https://dt-cdn.net/images/pg-naming-rules1-1531-db88a8a9d8.png)

   Process group naming rule example
7. Используйте кнопку **Preview** для проверки того, что список возвращаемых сущностей, соответствующих новому правилу, включает только нужные сущности.

   ![Process group naming rule](https://dt-cdn.net/images/pg-naming-rules2-1133-0080ee5066.png)

   Process group naming rule

В отличие от правил обнаружения групп процессов, правила именования не требуют перезапуска процессов и не влияют на их идентификацию и группировку. Эти правила просто обеспечивают быстрый и удобный способ применения интуитивно понятных соглашений об именовании к вашим процессам.

## Использование пользовательских метаданных для обогащения правил именования

Мониторинг процессов в Dynatrace можно дополнительно обогатить, [включив собственные метаданные в условия правил](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment."). Пользовательские метаданные позволяют точнее формировать правила именования групп процессов. Пример выделен ниже.

![Examplepg](https://dt-cdn.net/images/2021-02-17-08-28-51-1724-16065e2f77.png)

Examplepg

![Custom metadata to enrich naming rules](https://dt-cdn.net/images/pg-naming-rules4-1527-667ccd721b.png)

Custom metadata to enrich naming rules

![Custom metadata to enrich naming rules](https://dt-cdn.net/images/pg-naming-rules5-1405-111b77a025.png)

Custom metadata to enrich naming rules

Включив пользовательские метаданные в правила именования групп процессов, можно применять собственные детализированные стандарты именования в масштабах всей системы.