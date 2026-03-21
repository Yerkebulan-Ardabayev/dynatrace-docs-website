---
title: Автоматизация Red Hat Ansible
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-ansible
scraped: 2026-03-06T21:27:29.962658
---

# Red Hat Ansible Automation


* Latest Dynatrace
* Предварительная версия

Предварительная версия

При интеграции среды Dynatrace с контроллером Red Hat Ansible Automation с помощью коннектора Red Hat Ansible ![Red Hat Ansible for Workflows](https://dt-cdn.net/images/red-hat-ansible-for-workflows-257-cfabd1452d.png "Red Hat Ansible for Workflows") вы можете автоматически запускать шаблоны заданий на основе данных мониторинга.

## Настройка интеграции

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Предоставление разрешений для Workflows**](redhat-ansible.md#permissions "Автоматизация запуска заданий Ansible на основе данных мониторинга и событий.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создание API-ключа Red Hat Ansible**](redhat-ansible.md#api-key "Автоматизация запуска заданий Ansible на основе данных мониторинга и событий.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Настройка подключения Red Hat Ansible Automation**](redhat-ansible.md#connection "Автоматизация запуска заданий Ansible на основе данных мониторинга и событий.")[![Шаг 4 (необязательно)](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Шаг 4 (необязательно)")

**Настройка подключения EdgeConnect**](redhat-ansible.md#edgeconnect "Автоматизация запуска заданий Ansible на основе данных мониторинга и событий.")

### Шаг 1: Предоставление разрешений для Workflows

Для выполнения действий от вашего имени Workflows требуются определённые разрешения.

Для точной настройки разрешений, предоставленных Workflows:

1. Перейдите в **Workflows** и выберите **Settings** > **Authorization settings**.
2. Выберите следующие разрешения помимо общих разрешений Workflows.

* `app-settings:objects:read`
* `state:app-states:read`
* `state:app-states:write`
* `state:app-states:delete`

Подробнее об общих пользовательских разрешениях Workflows см. в разделе [Пользовательские разрешения для рабочих процессов](../../security.md#user-permission "Руководство по аспектам безопасности автоматизации рабочих процессов в Dynatrace Workflows").

### Шаг 2: Создание API-ключа Red Hat Ansible

Для взаимодействия с контроллером Red Hat Ansible Automation вам нужен API-ключ. Чтобы узнать, как его получить, см. [официальную документацию Red Hat](https://dt-url.net/q60398k).

### Шаг 3: Настройка подключения Red Hat Ansible

Вам необходимо настроить подключение для каждой среды Red Hat Automation.

Для настройки подключения к **Red Hat Ansible Automation Controller**:

1. Перейдите в **Settings** и выберите **Connections** > **Connectors** > **Red Hat Ansible**.
2. Выберите вкладку **Automation Controller**.
3. Выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") **Connection**.
4. Укажите понятное имя для вашего подключения.
5. Укажите URL API Red Hat Ansible. Например, `http://your-ansible-host.com/api/v2` (должен включать `api/v2`, без завершающего слеша).
6. Укажите ваш API-ключ Red Hat Ansible.
7. Выберите **Create**.

### Шаг 4 (необязательно): Настройка EdgeConnect

Если вы подключаетесь к самостоятельно размещённому контроллеру Red Hat Ansible Automation или экземпляру AWX, вам может потребоваться EdgeConnect для установления подключения за вашим файрволом.

Для настройки подключения EdgeConnect:

1. Перейдите в **Settings** > **General** > **External Requests** > **EdgeConnect**.
2. Выберите **New EdgeConnect**.
3. Введите **Name** для вашего EdgeConnect.
4. Введите **Host pattern** — URL-адрес.
5. Выберите **Create**.

Новое подключение EdgeConnect создано.

## Доступные действия

Для интеграции Red Hat Ansible Automation доступны следующие действия рабочих процессов.
Каждое действие соответствует конечной точке API Red Hat Ansible. Подробнее о конечных точках см. в [справочном руководстве по API Ansible Tower](https://dt-url.net/0w4392o).

## Запуск шаблона задания

Для запуска шаблона задания необходимо предоставить следующую информацию.

| Поле | Описание | Обязательность |
| --- | --- | --- |
| TemplateId | Идентификатор шаблона, который вы хотите запустить | Обязательно |
| ExtraVars | Дополнительные переменные для использования в шаблоне задания | Необязательно |

Подробнее о параметрах см. в [справочном руководстве по API Ansible Tower](https://dt-url.net/0w4392o) (`/api/v2/job_templates/{id}/launch/` "Запуск шаблона задания").

Для создания рабочего процесса, запускающего шаблон задания:

1. Перейдите в **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") и выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") для создания нового рабочего процесса.
2. На панели **Choose trigger** выберите триггер, наиболее подходящий для ваших потребностей.
3. На узле триггера выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") для просмотра доступных действий.
4. На одном из узлов извлечения информации выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить"), найдите `Ansible` и выберите **Launch job template**.
5. На каждом из оставшихся узлов извлечения информации выберите ![Добавить](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Добавить") и перетащите линию к действию **Launch job template**.
6. В действии **Launch job template** выберите [подключение](#connection) к вашему **Red Hat Ansible Automation Controller**.
7. Настройте поля ввода по необходимости. Чтобы узнать, как использовать выходные данные узлов извлечения информации, см. [Справочник по выражениям](../../reference.md "Познакомьтесь с выражениями рабочих процессов").
8. Для тестирования вашего рабочего процесса выберите **Run**.

## Устранение неполадок

Ниже приведены решения проблем, с которыми сталкиваются некоторые пользователи.

* [Red Hat Ansible for Workflows: ошибка отсутствия обязательных полей](https://dt-url.net/sq237zw)
* [Red Hat Ansible for Workflows: ошибка недостаточных разрешений](https://dt-url.net/3e63842)
