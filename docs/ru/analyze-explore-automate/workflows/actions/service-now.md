---
title: ServiceNow
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/service-now
scraped: 2026-02-18T21:22:34.275335
---

# ServiceNow

# ServiceNow

* Последнее Dynatrace
* 7-минутное чтение
* Обновлено 18 ноября 2025 г.

Ваша среда Dynatrace может интегрироваться с средой ServiceNow с помощью коннектора ServiceNow ![ServiceNow для рабочих процессов](https://dt-cdn.net/images/servicenow-for-workflows-257-9349ea0329.png "ServiceNow для рабочих процессов"), что позволяет создавать инциденты на основе ваших данных мониторинга и событий автоматически. Кроме того, вы можете получать группы из ServiceNow и импортировать их как [команды владения](/docs/deliver/ownership/ownership-teams#import-teams "Определите команды с идентификаторами команд, описаниями, обязанностями и информацией о маршрутизации для владения сущностями.").

## Настройка интеграции

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Предоставить разрешения для рабочих процессов**](/docs/analyze-explore-automate/workflows/actions/service-now#permissions "Автоматизировать создание инцидентов в ServiceNow на основе ваших данных мониторинга и событий.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создать учетные данные аутентификации ServiceNow**](/docs/analyze-explore-automate/workflows/actions/service-now#authentication "Автоматизировать создание инцидентов в ServiceNow на основе ваших данных мониторинга и событий.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Настроить подключение к ServiceNow**](/docs/analyze-explore-automate/workflows/actions/service-now#connection "Автоматизировать создание инцидентов в ServiceNow на основе ваших данных мониторинга и событий.")

### Шаг 1: Предоставить разрешения для рабочих процессов

Некоторые разрешения необходимы рабочим процессам для выполнения действий от вашего имени. Другие разрешения необходимы действиями, которые поставляются с коннектором ServiceNow.

Чтобы тонко настроить разрешения, предоставленные рабочим процессам

1. Перейдите в **Рабочие процессы** и выберите **Настройки** > **Настройки авторизации**.
2. Выберите следующие разрешения, кроме общих разрешений для рабочих процессов.

   * Разрешения, необходимые для действий рабочего процесса ServiceNow:

     + `app-settings:objects:read`

Для получения более подробной информации о разрешениях пользователей для рабочих процессов см. [Разрешения пользователей для рабочих процессов](/docs/analyze-explore-automate/workflows/security#user-permission "Руководство по аспектам безопасности автоматизации рабочих процессов в Dynatrace Рабочих процессах").

### Шаг 2: Создать учетные данные аутентификации ServiceNow

Войдите в свою среду ServiceNow и создайте базовые учетные данные аутентификации с следующими разрешениями. Вам понадобятся эти учетные данные на следующем шаге.

Разрешения пользователя ServiceNow:

* Поиск, создание и обновление инцидентов (таблица инцидент)
* Чтение категорий (таблица sys\_choice, элемент category)
* Чтение подкатегорий (таблица sys\_choice, элемент subcategory)
* Чтение групп назначения (таблица sys\_user\_group)
* Чтение кодов разрешения (таблица sys\_choice, элемент close\_code)

### Шаг 3: Настроить подключение к ServiceNow

Вам необходимо настроить подключение для каждой из ваших сред ServiceNow.

Чтобы настроить подключение

1. Перейдите в **Настройки** и выберите **Подключения** > **Коннекторы** > **ServiceNow**.
2. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Подключение**
3. Опишите свое подключение к ServiceNow.

   * **Имя подключения**: Введите осмысленное имя для вашего подключения.
   * **URL экземпляра ServiceNow**: Добавьте URL вашей среды ServiceNow.
   * **Тип** Либо используйте базовую аутентификацию, либо учетные данные клиента.

     + Для **Базовой аутентификации** введите имя пользователя и пароль.
     + Для **Учетных данных клиента** введите идентификатор клиента и секрет клиента.
4. Выберите **Создать**.

## Доступные действия

Следующие действия рабочего процесса доступны для интеграции с ServiceNow. Каждое действие соответствует конечной точке API ServiceNow API.

Действие

Описание

Конечная точка API ServiceNow API

**Создать инцидент**

Создает инцидент в вашей среде ServiceNow. Инцидент представляет собой проблему или вопрос, который необходимо решить и устранить.

`POST /api/now/v2/table/incident`

**Создать уязвимый элемент**

Создает уязвимый элемент в вашей среде ServiceNow.

`POST /api/now/v2/table/sn_vul_vulnerable_item`

**Получить группы**

Получает группы из вашей среды ServiceNow.

`GET /api/now/v2/table/sys_user_group`

**Комментарий**

Создает комментарий к записи в вашей среде ServiceNow.

`PUT /api/now/v2/table/${tableName}/${sysId}`

**Комментарий к инциденту**

Добавляет новый комментарий к записи инцидента ServiceNow.

`PUT /api/now/v2/table/incident/${sys_id}`

**Поиск**

Общее действие поиска, которое позволяет искать вашу среду ServiceNow.

`GET /api/now/v2/table/${tableName}`

**Поиск инцидентов**

Запрашивает ServiceNow, чтобы получить список инцидентов, соответствующих заданным критериям.

`GET /api/now/v2/table/incident`

**Разрешить инцидент**

Обновляет инцидент ServiceNow, чтобы отметить его как разрешенный.

`PUT /api/now/v2/table/incident/${sys_id}`

**Создать запись**

Создает новую запись в указанной таблице ServiceNow.

`POST /api/now/v2/table/${tableName}`

**Обновить запись**

Обновляет существующую запись в указанной таблице ServiceNow.

`PUT /api/now/v2/table/${tableName}/${sys_id}`

## Создать инцидент ServiceNow

Чтобы создать инцидент ServiceNow в вашем рабочем процессе ![Рабочие процессы](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Рабочие процессы")

1. В панели **Выбрать действие** найдите ServiceNow и выберите **Создать инцидент**.
2. В действии **Создать инцидент** выберите [Подключение](#connection) к вашей среде ServiceNow.
3. Настройте поля ввода по мере необходимости.

   | Поле | Описание | Обязательно |
   | --- | --- | --- |
   | **Идентификатор корреляции** | Уникальный идентификатор (в большинстве случаев это идентификатор события Dynatrace). | Необязательно |
   | **Заявитель** | Пользователь, который сообщает об инциденте. | Необязательно |
   | **Категория** | Категория инцидента. Варианты категорий получаются путем запроса таблицы `sys_choice` с `sysparm_query: 'name=incident^element=category^inactive=false'`. | Обязательно |
   | **Подкатегория** | Подкатегория инцидента. Варианты подкатегорий получаются путем запроса таблицы `sys_choice` с `sysparm_query: 'name=incident^element=subcategory^inactive=false^dependent_value=${category}'`. | Обязательно |
   | **Воздействие** | Воздействие инцидента. | Обязательно |
   | **Срочность** | Срочность инцидента. | Обязательно |
   | **Группа назначения** | Группа, которая будет работать над инцидентом. Варианты групп назначения получаются путем запроса таблицы `sys_user_group` с `sysparm_display_value: 'all'`. | Обязательно |
   | **Элемент конфигурации** | Пострадавшая сущность. | Необязательно |
   | **Краткое описание** | Краткое описание инцидента. | Необязательно |
   | **Описание** | Подробное описание инцидента. | Необязательно |

   Для получения более подробной информации см. [официальную документацию ServiceNow](https://dt-url.net/vc039n0).

## Создать уязвимый элемент в ServiceNow

Чтобы создать уязвимый элемент ServiceNow в вашем рабочем процессе ![Рабочие процессы](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Рабочие процессы")

1. В панели **Выбрать действие** найдите ServiceNow и выберите **Создать уязвимый элемент**.
2. В действии **Создать уязвимый элемент** выберите [Подключение](#connection) к вашей среде ServiceNow.
3. Настройте поля ввода по мере необходимости.

   | Поле | Описание | Обязательно |
   | --- | --- | --- |
   | **Внешний идентификатор** | Идентификатор, связанный с уязвимым элементом | Необязательно |
   | **Описание** | Подробное описание уязвимого элемента | Необязательно |
   | **Краткое описание** | Краткое описание уязвимого элемента | Необязательно |
   | **Балл риска** | Балл риска уязвимого элемента | Необязательно |
   | **Рейтинг риска** | Рейтинг риска уязвимого элемента | Необязательно |
   | **Источник** | Источник, который обнаружил уязвимый элемент | Необязательно |
   | **Балл риска источника** | Балл риска в системе источника уязвимого элемента | Необязательно |
   | **Элемент конфигурации** | Пострадавшая сущность | Необязательно |
   | **Дата обнаружения** | Дата обнаружения | Необязательно |
   | **Приоритет** | Приоритет уязвимого элемента | Необязательно |

   Для получения более подробной информации см. [официальную документацию ServiceNow](https://dt-url.net/vc039n0).

## Получить группы из ServiceNow

Чтобы получить группы из ServiceNow в вашем рабочем процессе ![Рабочие процессы](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Рабочие процессы")

1. В панели **Выбрать действие** найдите ServiceNow и выберите **Получить группы**.
2. В действии **Получить группы** выберите [Подключение](#connection) к вашей среде ServiceNow.
3. Настройте поля ввода по мере необходимости.

   | Поле | Описание | Обязательно |
   | --- | --- | --- |
   | **SysParm Query** | Закодированный запрос, используемый для фильтрации набора результатов | Необязательно |
   | **Ограничение** | Максимальное количество результатов для возврата (по умолчанию: 100) | Необязательно |

   Для получения более подробной информации см. [официальную документацию ServiceNow](https://dt-url.net/vc039n0).

## Создать комментарий в ServiceNow

Чтобы создать комментарий к записи в таблице ServiceNow в вашем рабочем процессе ![Рабочие процессы](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Рабочие процессы")

1. В панели **Выбрать действие** найдите ServiceNow и выберите **Создать комментарий**.
2. В действии **Создать комментарий** выберите [Подключение](#connection) к вашей среде ServiceNow.
3. Настройте поля ввода по мере необходимости.

   | Поле | Описание | Обязательно |
   | --- | --- | --- |
   | **Таблица** | Имя таблицы записи, к которой будет добавлен комментарий | Обязательно |
   | **Уникальный идентификатор записи (sys\_id)** | Идентификатор sys\_id записи, к которой будет добавлен комментарий | Обязательно |
   | **Комментарий** | Комментарий, который будет создан | Обязательно |

   Для получения более подробной информации см. [официальную документацию ServiceNow](https://dt-url.net/vc039n0).

## Комментарий к инциденту в ServiceNow



To comment on an incident in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Comment on an incident**.
2. In the **Comment on an incident** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Incident Number** | The number of the incident to comment on | Required |
   | **Comment** | The comment that will be created | Required |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Search in ServiceNow

To search ServiceNow in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Search**.
2. In the **Search** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Table** | Select the table in which to search | Required |
   | **SysParm Query** | An encoded query used to filter the result set | Optional |
   | **SysParm Fields** | Comma-separated list of fields that limit the result | Optional |
   | **Query category** | Category to filter search results. | Optional |
   | **Limit** | Maximum number of results to return (Default: 100) | Optional |
   | **Offset** | Records to skip (Default: 0) | Optional |
   | **Order by asc** | Field name to sort results in ascending order | Optional |
   | **Order by desc** | Field name to sort results in descending order | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Search incidents in ServiceNow

To search for incidents in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Search incidents**.
2. In the **Search incidents** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **SysParm Query** | An encoded query used to filter the result set | Optional |
   | **SysParm Fields** | Comma-separated list of fields that limit the result | Optional |
   | **Limit** | Maximum number of results to return (Default: 100) | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Resolve incident in ServiceNow

To resolve an incident in your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Resolve incident**.
2. In the **Resolve incident** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Incident Number** | The number of the incident to resolve | Required |
   | **Resolution Notes** | Add notes for the resolution of the incident | Required |
   | **Resolution Code** | The close code for the resolution | Required |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Create record

To create a record in a ServiceNow Table from your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Create Record**.
2. In the **Create Record** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Table** | The name of the table in which to create a record | Required |
   | **Payload Fields** | Key-value pairs of table field names and their values | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Update record

To update a record in ServiceNow from your workflow ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows")

1. In the **Choose action** pane, search for ServiceNow and select **Update Record**.
2. In the **Update Record** action, select the [Connection](#connection) to your ServiceNow environment.
3. Configure the input fields as needed.

   | Field | Description | Required |
   | --- | --- | --- |
   | **Table** | The name of the table in which to create a record | Required |
   | **Unique record identifier (sys\_id)** | The sys\_id of the entry to comment on | Required |
   | **Payload Fields** | Key-value pairs of table field names and their values | Optional |

   For more details, see the [official ServiceNow documentationï»¿](https://dt-url.net/vc039n0).

## Troubleshooting

The following is a solution to a problem some people have.

* [ServiceNow for Workflows: Insufficient permissions errorï»¿](https://dt-url.net/hj637wm)