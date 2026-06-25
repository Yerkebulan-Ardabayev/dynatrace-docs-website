---
title: Распределение пользовательских панелей мониторинга с расширениями
source: https://docs.dynatrace.com/managed/ingest-from/extensions/advanced-configuration/custom-dashboards
scraped: 2026-05-12T11:09:16.118906
---

# Распределение пользовательских панелей мониторинга с расширениями

# Распределение пользовательских панелей мониторинга с расширениями

* Практическое руководство
* Чтение: 3 мин
* Обновлено 7 августа 2025 г.

После того как расширение начнёт отправлять данные в Dynatrace, можно создать пользовательскую панель мониторинга, экспортировать её определение в JSON-файл и добавить JSON в архив расширения.

## Dashboards Classic

При использовании [Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать, управлять и использовать Dynatrace Dashboards Classic.") следуйте приведённым ниже процедурам.

После того как расширение начнёт отправлять данные в Dynatrace, можно [создать пользовательскую панель мониторинга](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать панели мониторинга Dynatrace."), затем экспортировать её определение в JSON-файл и добавить в архив расширения. Экспортировать определение панели можно через веб-интерфейс Dynatrace или Dynatrace API.

### Экспорт JSON панели мониторинга через веб-интерфейс

1. Откройте **Dashboards**.
2. В строке нужной панели мониторинга выберите **More** (**…**) > **Export**.
   На локальный компьютер будет загружен JSON-файл с именем панели мониторинга.
   Дополнительные сведения см. в разделе [Редактирование JSON панели мониторинга Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json "Узнайте, как экспортировать, редактировать и импортировать JSON панели мониторинга Dynatrace.").

### Экспорт JSON панели мониторинга через API

1. Откройте **Dashboards** и перейдите к нужной панели мониторинга.
2. В URL панели мониторинга найдите параметр `id` (например, `id=d996b25e-593c-4213-8ad3-c87319a8830a`) и сохраните его значение.
3. Используйте эндпоинт API [Get a dashboard](/managed/dynatrace-api/configuration-api/dashboards-api/get-dashboard "Просмотр панели мониторинга через Dynatrace Classic API.") для получения JSON-определения панели.
   Выполните следующую команду для получения определения панели мониторинга. В данном примере используется URL Dynatrace SaaS:

   ```
   curl -X GET "https://{env-id}.live.dynatrace.com/api/config/v1/dashboards/{dashboard-id}" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token `{api-token}"
   ```

   Замените:

   * `{env-id}` на [идентификатор окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Знакомство с окружениями мониторинга и работа с ними.").
   * `{api-token}` на [API-токен](/managed/dynatrace-api/basics/dynatrace-api-authentication "Как пройти аутентификацию для использования Dynatrace API.") с необходимыми [разрешениями](/managed/upgrade/unavailable-in-managed "Выбранный вариант недоступен в Dynatrace Managed.").
   * `{dashboard-id}` на идентификатор панели мониторинга, определённый на предыдущем шаге.
4. Вызов возвращает JSON-полезную нагрузку с определением панели мониторинга. Сохраните её как JSON-файл.

### Добавление панели мониторинга в пакет расширения

Добавьте JSON-файл панели мониторинга в пакет расширения и укажите на него в файле YAML расширения.

Для следующей структуры пакета:

```
extension.zip



│   extension.yaml



│



└───alerts



│   |   alert.json



│



└───dashboards



│   dashboard.json
```

Используйте следующую ссылку на верхнем уровне [файла YAML](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать файл YAML расширения с помощью Extensions framework."):

```
dashboards:



- path: dashboards/dashboard.json



alerts:



- path: alerts/alert.json
```