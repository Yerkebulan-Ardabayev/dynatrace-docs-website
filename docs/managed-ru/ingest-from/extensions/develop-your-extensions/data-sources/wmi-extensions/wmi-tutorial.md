---
title: Учебное руководство по источнику данных WMI
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial
scraped: 2026-05-12T12:13:27.019453
---

# Учебное руководство по источнику данных WMI

# Учебное руководство по источнику данных WMI

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 30 марта 2022 г.

Это пошаговое учебное руководство по созданию расширения на основе источника данных WMI. В нём создаётся расширение WMI, работающее на OneAgent и выполняющее мониторинг хоста Windows.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание разработческого сертификата и ключа**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial#generate-certificate-and-key "Узнайте о расширениях WMI в платформе Extensions framework.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Распространение корневого сертификата на компоненты Dynatrace**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial#distribute-root-certificate "Узнайте о расширениях WMI в платформе Extensions framework.")

## Перед началом работы

Для успешного создания расширения Extensions и прохождения этого руководства необходимо выполнить следующие предварительные требования:

* Доступ администратора к среде Dynatrace SaaS или Managed версии 1.227+
* Хост Windows (виртуальная машина)
* OneAgent версии 1.227+, развёрнутый на хосте
* Dynatrace CLI

  + Python 3.10 или 3.14
  + Доступ к установщику пакетов pip для Python
  + Установите dt-cli

    ```
    pip install dt-cli
    ```

    Дополнительные сведения см. в разделе [Подписание расширений](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.").
* Корневой сертификат загружен в Dynatrace и на хост OneAgent

## Шаг 1. Создание разработческого сертификата и ключа

```
dt extension genca



dt extension generate-developer-pem -o developer.pem --ca-crt ca.pem --ca-key ca.key --name 'JDoe'
```

Команда создаёт следующие файлы:

* `developer.pem`: разработческий сертификат
* `ca.pem`: корневой сертификат
* `ca.key`: корневой ключ

## Шаг 2. Распространение корневого сертификата на компоненты Dynatrace

### Загрузка в хранилище учётных данных Dynatrace

1. Откройте **Credential Vault**.
2. Выберите **Add new credential**.
3. В поле **Credential type** выберите **Public Certificate**.
4. Выберите область доступа к учётным данным **Extension validation**.
5. Добавьте понятное **Credential name**.
6. Загрузите **Root certificate file**.
7. Выберите **Save**.

### Загрузка на хост OneAgent, на котором выполняется расширение

1. Перейдите в следующий каталог:

   * Windows: `C:\ProgramData\dynatrace\oneagent\agent\config`
   * Linux: `/var/lib/dynatrace/oneagent/agent/config/`
2. Перейдите в папку `certificates` (создайте её, если она не существует)
3. Загрузите корневой сертификат (`ca.pem`), сгенерированный ранее

Среда Dynatrace готова к созданию расширения WMI.

**Следующий шаг**: [Пакет расширения](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01 "Узнайте о расширениях WMI в платформе Extensions framework.")