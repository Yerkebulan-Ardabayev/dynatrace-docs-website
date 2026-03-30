---
title: Dynatrace Hub
source: https://www.dynatrace.com/docs/manage/hub
scraped: 2026-03-06T21:10:19.637942
---

**Dynatrace Hub** — центральное место для поиска, активации и управления приложениями и расширениями Dynatrace.

## Где найти

Поиск "Hub" в [Launcher](../discover-dynatrace/get-started/dynatrace-ui.md#launcher) или раздел **Manage** в Launcher.

## Что представлено

- Технологии, поддерживаемые OneAgent
- Фреймворки Open Observability
- Расширения Dynatrace
- Приложения на базе AppEngine

### Приложения

Компактные решения для конкретных сценариев. Взаимодействуют между собой через концепцию интентов. Подробнее — см. AppEngine.

### Расширения

Extensions 2.0 — декларативный импорт метрик. Управление через [приложение Extensions](https://www.dynatrace.com/hub/detail/extension-manager/).

## Управление

### Установка

Требуется разрешение [app-engine:apps:install](identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements.md#app-engine-apps-install).

1. Откройте обзор приложения > **Install**.
2. После установки назначьте пользователям группы с нужными разрешениями.

**Без разрешения на установку:** используйте **Request install** — автоматический или ручной запрос.

### Включение автоматических запросов на установку

Настройте контакты администраторов:
- Hub > значок настроек > **Add admin** > **Save**
- Или Settings > **General** > **Hub Requests** > **Add admin** > **Save**

### Автоматические обновления

Все установленные приложения обновляются автоматически.

### Уведомления об обновлениях

Требуемые разрешения:

| Разрешение | Доступ |
| --- | --- |
| `storage:system:read` (обязательно) | Просмотр событий обновления |
| `storage:event.provider = "APP_REGISTRY"` (опционально) | Только события приложений |

Настройка: Hub > вкладка **Manage** > **Notify on app updates** > выберите приложения > **Apply**.

### Удаление

Требуется разрешение [app-engine:apps:delete](identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements.md#app-engine-apps-delete). Обзор приложения > **Uninstall**.

### Подписки Hub

Для специальных приложений/выпусков от Dynatrace. Активация через Channel ID:

1. Settings > **General** > **Hub subscriptions** > **Add subscription**.
2. Укажите название, Channel ID и описание.
3. **Save changes**.

Требуемая политика:
```
ALLOW settings:objects:read, settings:objects:write, settings:schemas:read
WHERE settings:schemaId = "builtin:hub-channel.subscriptions";
```

Активация может занять до 30 минут (кэширование).

## Верификация приложений

- **Подлинность** — информация о поставщике в каталоге; пользовательские приложения отмечены как "Custom apps"
- **Целостность** — приложение не изменено между выпуском и размещением
- **Подпись кода** — требуется действительный сертификат, проверяемый перед размещением
