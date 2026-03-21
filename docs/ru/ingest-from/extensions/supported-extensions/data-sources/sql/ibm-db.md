---
title: Управление расширениями IBM Database
source: https://www.dynatrace.com/docs/ingest-from/extensions/supported-extensions/data-sources/sql/ibm-db
scraped: 2026-03-04T21:37:15.660573
---

* Latest Dynatrace
* How-to guide
* 2-min read

Dynatrace предоставляет фреймворк, с помощью которого можно расширить наблюдаемость приложений за счёт данных, получаемых непосредственно с уровня IBM Database, чтобы отслеживать влияние задач сервера базы данных на ваше приложение.

Начните с проверки [Dynatrace Hub](https://www.dynatrace.com/hub/?query=ibm+db2), чтобы убедиться, что предоставляемое Dynatrace расширение IBM Database Server соответствует вашим требованиям.

## Прежде чем начать

Назначьте группу или группы ActiveGate, которые будут удалённо подключаться к серверу IBM Database для получения данных. Все ActiveGate в каждой назначенной группе должны иметь возможность подключиться к вашему серверу IBM Database.

## Управление расширениями IBM DB2

![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions")

### Extension Manager

Latest Dynatrace

Теперь для управления расширениями можно использовать специальное приложение Extensions. Оно обеспечивает аналогичный процесс активации и настройки, что и Dynatrace Hub в предыдущей версии Dynatrace. Кроме того, оно предоставляет прямой доступ к мониторингу работоспособности расширений.

* Чтобы воспользоваться приложением:

  + В Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") выберите и установите приложение.
  + В листинге Hub содержится информация о разрешениях, необходимых для работы с приложением (вкладка **Technical information** (Техническая информация)).

Dynatrace Hub предоставляет унифицированный процесс для включения и управления расширениями, которые будут принимать данные IBM Database в вашу среду Dynatrace.

Необходимое разрешение: **Change monitoring settings** (Изменить настройки мониторинга)

1. В Dynatrace Hub найдите и выберите расширение IBM DB2.
2. Выберите и установите нужное расширение. Это включает расширение в вашей среде мониторинга.
3. Добавьте конфигурацию мониторинга, чтобы расширение могло начать сбор данных.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Определить конечные точки**](ibm-db.md#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from IBM Database server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Группа ActiveGate**](ibm-db.md#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from IBM Database server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Активировать расширение**](ibm-db.md#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from IBM Database server.")

### Шаг 1: Определить конечные точки

1. Нажмите **Add IBM endpoint** (Добавить конечную точку IBM), чтобы задать серверы IBM Database, с которых нужно получать данные. Можно задать до 100 конечных точек. Укажите следующие данные для подключения:

* Host (Хост)
* Port (Порт)
* Database name (Имя базы данных)
* Authentication credentials (Учётные данные аутентификации)

  + Поддерживается только базовая аутентификация.
  + Данные аутентификации, передаваемые в Dynatrace при активации конфигурации мониторинга, скрываются, и их невозможно извлечь.
  + Для более надёжного хранения учётных данных пользователей и управления ими можно [использовать хранилище учётных данных](../../../develop-your-extensions/data-sources/sql/ibm-monitoring.md#authentication "IBM DB2 extensions in the Extensions framework.").
* Нажмите **Next step** (Следующий шаг).

### Шаг 2: Группа ActiveGate

1. Выберите группу ActiveGate, чтобы определить, какие ActiveGate будут запускать расширение.
2. Нажмите **Next step** (Следующий шаг).

### Шаг 3: Активировать расширение

1. Укажите итоговые детали конфигурации:

* **Description** (Описание)
  Текст с подробными сведениями об этой конкретной конфигурации мониторинга. При устранении неполадок мониторинга это поможет команде разобраться в ситуации.
* **Feature sets** (Наборы функций)
  В сильно сегментированных сетях наборы функций могут отражать сегменты вашей среды. С их помощью можно ограничить мониторинг определёнными сегментами. Наборы функций предопределены для каждого расширения.
* Нажмите **Activate** (Активировать).

## Конфигурация мониторинга в формате JSON

Мастер активации расширения содержит динамически обновляемые JSON-данные с конфигурацией мониторинга. Сведения об использовании этих данных для активации расширения через Dynatrace API см. в разделе [Manage Extensions](../../../manage-extensions.md "Learn how to manage extensions.").
