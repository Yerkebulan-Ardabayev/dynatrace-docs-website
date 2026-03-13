---
title: Distribute custom dashboards with your extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/advanced-configuration/custom-dashboards
scraped: 2026-03-03T21:22:34.358051
---

# Распространение пользовательских дашбордов вместе с расширениями

# Распространение пользовательских дашбордов вместе с расширениями

* Latest Dynatrace
* Руководство
* Чтение: 3 мин.
* Обновлено 7 августа 2025 г.

После того как ваше расширение начнёт отправлять данные в Dynatrace, вы можете создать пользовательский дашборд, экспортировать его определение в JSON-файл и добавить JSON в архив расширения.

## Dashboards **Dashboards**

Если вы используете [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создавайте интерактивные настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени."), следуйте этим процедурам.

Вы можете экспортировать определение дашборда через веб-интерфейс Dynatrace.

### Экспорт JSON дашборда

Чтобы скачать (экспортировать) дашборд из боковой панели ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**

1. Перейдите в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. В разделе **Last opened by you** наведите курсор на имя дашборда, который хотите экспортировать, и выберите  **Download** из меню . Дашборд будет загружен в локальный JSON-файл, который можно загрузить.

   Если вашего дашборда нет в списке **Last opened by you**, выберите  **All dashboards**, чтобы отобразить таблицу всех дашбордов, к которым у вас есть доступ (ваши дашборды или дашборды, предоставленные вам). Из таблицы вы можете найти нужный дашборд и выбрать  **Download** из меню .

Чтобы скачать (экспортировать) текущий отображаемый дашборд в формате JSON

1. В верхней части дашборда откройте меню  справа от имени дашборда.
2. Выберите  **Download** из меню.

   Определение текущего дашборда будет загружено в локальный JSON-файл.

### Добавление дашборда в пакет расширения

После создания дашборда, использующего данные вашего расширения, и экспорта JSON дашборда, как описано выше, вы можете добавить дашборд в пакет расширения.

1. Переименуйте JSON-файл дашборда в соответствии с шаблоном `<string>.dashboard.json`. Например, `device-health.dashboard.json`.
2. Добавьте JSON в [пакет расширения](/docs/ingest-from/extensions/concepts#package "Узнайте больше о концепции расширений Dynatrace.").

   Например,

   ```
   extension.zip



   |   extension.yaml



   |



   +---documents



   |   device-health.dashboard.json
   ```
3. Объявите JSON в [YAML-файле расширения](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать YAML-файл расширения с помощью фреймворка расширений.").

   Например,

   ```
   documents:



   dashboards:



   - displayName: "My Dashboard"



   path: "documents/device-health.dashboard.json"
   ```
4. Загрузите расширение в среду Dynatrace.

   Ваш дашборд теперь доступен в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

Вы также можете получить доступ к дашборду из ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**.

1. Перейдите в ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**.
2. Выберите ваше расширение.
3. На вкладке **Configure** выберите **Extension content**.

   * Ваш дашборд будет указан с типом `DOCUMENT_DASHBOARD`.
   * Вы можете установить **Filter By Type** в `DOCUMENT_DASHBOARD`, чтобы отобразить только дашборды.

## Dashboards Classic

Если вы используете [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Узнайте, как создавать, управлять и использовать Dynatrace Dashboards Classic."), следуйте этим процедурам.

После того как ваше расширение начнёт отправлять данные в Dynatrace, вы можете [создать пользовательский дашборд](/docs/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать дашборды Dynatrace."), а затем экспортировать его определение в JSON-файл и добавить в архив расширения. Вы можете экспортировать определение дашборда через веб-интерфейс Dynatrace или Dynatrace API.

### Экспорт JSON дашборда через веб-интерфейс

1. Перейдите в ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. В строке дашборда, который хотите экспортировать, выберите **More** (**...**) > **Export**.
   JSON-файл с именем дашборда будет загружен на ваш компьютер.
   Для получения дополнительной информации см. [Редактирование JSON дашборда Dynatrace](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json "Узнайте, как экспортировать, редактировать и импортировать JSON дашборда Dynatrace.").

### Экспорт JSON дашборда через API

1. Перейдите в ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** и откройте дашборд.
2. В URL дашборда найдите параметр `id` (например, `id=d996b25e-593c-4213-8ad3-c87319a8830a`) и сохраните значение параметра.
3. Используйте конечную точку [Get a dashboard](/docs/dynatrace-api/configuration-api/dashboards-api/get-dashboard "Просмотр дашборда через Dynatrace Classic API.") API для получения JSON-определения дашборда.
   Выполните следующую команду для получения определения дашборда. В этом примере мы используем URL Dynatrace SaaS:

   ```
   curl -X GET "https://{env-id}.live.dynatrace.com/api/config/v1/dashboards/{dashboard-id}" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token `{api-token}"
   ```

   Замените:

   * `{env-id}` на ваш [идентификатор среды](/docs/discover-dynatrace/get-started/monitoring-environment "Понимание и работа со средами мониторинга.").
   * `{api-token}` на [API-токен](/docs/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.") с необходимыми [разрешениями](/docs/ingest-from/extensions/manage-extensions#permissions "Узнайте, как управлять расширениями.").
   * `{dashboard-id}` на идентификатор дашборда, определённый на предыдущем шаге.
4. Вызов вернёт JSON-полезную нагрузку с определением дашборда. Сохраните её как JSON-файл.

### Добавление дашборда в пакет расширения

Добавьте JSON-файл дашборда в пакет расширения и укажите ссылку на него в YAML-файле расширения.

Для следующей структуры пакета:

```
extension.zip



|   extension.yaml



|



+---alerts



|   |   alert.json



|



+---dashboards



|   dashboard.json
```

Используйте следующую ссылку на верхнем уровне вашего [YAML-файла](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать YAML-файл расширения с помощью фреймворка расширений."):

```
dashboards:



- path: dashboards/dashboard.json



alerts:



- path: alerts/alert.json
```
