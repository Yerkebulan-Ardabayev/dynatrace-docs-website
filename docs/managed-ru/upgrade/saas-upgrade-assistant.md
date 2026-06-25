---
title: SaaS Upgrade Assistant
source: https://docs.dynatrace.com/managed/upgrade/saas-upgrade-assistant
scraped: 2026-05-12T12:16:04.575549
---

# SaaS Upgrade Assistant

# SaaS Upgrade Assistant

* Updated on Dec 13, 2024

Latest Dynatrace

![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** импортирует конфигурацию вашей среды Dynatrace Managed и позволяет администраторам кластера Dynatrace Managed плавно перейти с локального развёртывания Dynatrace Managed на облачную модель SaaS. Администратор кластера может импортировать конфигурацию в целевую среду SaaS и скорректировать её в соответствии с требованиями среды SaaS. Приложение обеспечивает более быструю миграцию и минимизирует перебои в работе пользователей Dynatrace из-за некорректной конфигурации среды. Автоматизация устраняет трудоёмкие ручные операции, такие как обновление владельцев дашбордов или корректировка идентификаторов сущностей, изменившихся при смене среды.

## Что умеет SaaS Upgrade Assistant?

В настоящее время с помощью ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** вы можете:

* Отслеживать прогресс миграции конфигурации.
* Просматривать импортированные конфигурации и анализировать неудачные, помеченные красным цветом.
* Диагностировать неудачные и пропущенные конфигурации благодаря подробным сообщениям об ошибках.
* Исправлять отдельную конфигурацию через форму редактирования или обновлять сотни конфигураций одновременно в режиме массового редактирования. Для проверки корректности изменений доступен предварительный просмотр.
* Выбирать, какие конфигурации необходимо мигрировать, и выполнять частичное развёртывание.
* [Автоматически обновлять владельцев дашбордов](/managed/upgrade/saas-upgrade-assistant/sua-update-dashboard-owners "Update dashboard owners automatically with SaaS Upgrade Assistant.").

## Как экспортировать конфигурацию из Dynatrace Managed?

1. Войдите в **Cluster Management Console** Dynatrace Managed.
2. Перейдите в **Environments**.
3. Выберите среду, из которой хотите выполнить миграцию.
4. Выберите ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Export configuration**.
5. Подтвердите операцию и перейдите в целевую локальную директорию для сохранения архива.

Подробнее см. в разделе [Обновление конфигурации в SaaS Upgrade Assistant](/managed/upgrade/saas-upgrade-assistant/sua-update-config "Learn how to update configuration in SaaS Upgrade Assistant.").

## Как установить, обновить или удалить SaaS Upgrade Assistant?

Чтобы установить, обновить или удалить SaaS Upgrade Assistant, в [Dynatrace Hub](https://docs.dynatrace.com/docs/shortlink/hub) выберите ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant**, затем нажмите **Install**, **Update** или **Uninstall** для выполнения соответствующего действия в вашей среде.

При удалении ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** учтите следующее.

* Статус обновления и все загруженные конфигурации будут удалены через 30 дней бездействия. В течение этого времени можно переустановить приложение — данные будут сохранены. Если оставить приложение без использования, данные всё равно будут удалены через 30 дней.
* Конфигурации, уже развёрнутые с помощью ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant**, сохранятся.

## С какими версиями совместим SaaS Upgrade Assistant?

Рекомендуется работать с конфигурацией, экспортированной из одной и той же основной версии кластера Dynatrace Managed и среды SaaS, чтобы избежать лишних ложноположительных ошибок при миграции конфигурации. Например, кластер Dynatrace Managed должен быть версии 1.284.123, а среда SaaS — версии 1.284.89.