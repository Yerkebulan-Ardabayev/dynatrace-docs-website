---
title: Журналы аудита через API
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/configuration/audit-logs-api
scraped: 2026-05-12T11:08:51.693218
---

# Журналы аудита через API

# Журналы аудита через API

* Практическое руководство
* Чтение 1 мин
* Updated on Apr 22, 2024

Журналы аудита необходимы для отслеживания изменений и событий, связанных с безопасностью. Dynatrace может регистрировать такие события, чтобы вы могли просматривать важные изменения: когда было сделано изменение, кем и что именно было изменено.

Регистрируются следующие события:

* Любое изменение конфигурации окружения Dynatrace
* Любое изменение API-токенов окружения
* Входы в Dynatrace
* Выходы из Dynatrace

Журналы аудита не включают изменения OAuth-токенов или изменения конфигурации управления аккаунтом, такие как SSO.

Журналы аудита содержат персональные данные (PII), например адреса электронной почты и IP-адреса пользователей Dynatrace.

## Включение журналирования аудита

🔴 По умолчанию отключено

Чтобы включить журналирование аудита:

1. Перейдите в **Settings** > **Preferences** > **Log audit events**.
2. Включите параметр **Log all audit-related system events**.

Dynatrace хранит журналы аудита в течение 30 дней и автоматически удаляет их по истечении этого срока.

Также можно включить журналы аудита через [API конфиденциальности данных](/managed/dynatrace-api/configuration-api/data-privacy-api/put-configuration "Редактирование конфигурации конфиденциальности данных через Dynatrace API.").

## Доступ к журналам аудита окружения Dynatrace

Доступ к журналам аудита на уровне окружения можно получить через вызов API [GET audit log](/managed/dynatrace-api/environment-api/audit-logs/get-log "Просмотр полного журнала аудита через Dynatrace API.").

## Доступ к журналам аудита кластера Dynatrace Managed

Доступ к журналам аудита кластера Dynatrace Managed можно получить, просматривая файлы журналов аудита, хранящиеся в файловой системе. Все файлы журналов аудита хранятся в папке logs. Путь к этой папке указан в разделе [Требования к оборудованию](/managed/managed-cluster/installation/managed-hardware-requirements "Ознакомьтесь с требованиями к оборудованию, хранилищу и многоузловому кластеру перед установкой Dynatrace Managed.").

Кроме того, Dynatrace Managed предлагает средство просмотра журналов аудита в Cluster Management Console (пункт **Audit log** в меню навигации).

## Связанные темы

* [API журналов аудита](/managed/dynatrace-api/environment-api/audit-logs "Чтение журналов аудита Dynatrace через Dynatrace API.")
* [API конфиденциальности данных — PUT configuration](/managed/dynatrace-api/configuration-api/data-privacy-api/put-configuration "Редактирование конфигурации конфиденциальности данных через Dynatrace API.")