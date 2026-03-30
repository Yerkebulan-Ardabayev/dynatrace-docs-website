---
title: Руководство по источнику данных WMI
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial
scraped: 2026-03-04T21:28:59.832907
---

Это пошаговое руководство по созданию расширения на основе источника данных WMI. Вы создадите расширение WMI, которое работает на OneAgent и выполняет мониторинг хоста Windows.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание сертификата и ключа разработчика**](wmi-tutorial.md#generate-certificate-and-key "Learn about WMI extensions in the Extensions framework.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Распространение корневого сертификата на компоненты Dynatrace**](wmi-tutorial.md#distribute-root-certificate "Learn about WMI extensions in the Extensions framework.")

## Прежде чем начать

Для успешной разработки расширения Extensions и прохождения данного руководства необходимо выполнить следующие предварительные условия:

* Права администратора в среде Dynatrace SaaS или Managed версии 1.227+
* Хост Windows (виртуальная машина)
* OneAgent версии 1.227+, развёрнутый на хосте
* Dynatrace CLI

  + Python 3.10
  + Доступ к установщику пакетов pip для Python
  + Установите dt-cli

    ```
    pip install dt-cli
    ```

    Дополнительные сведения см. в разделе Подписание расширений.
* Ваш корневой сертификат, загруженный в Dynatrace и на хост OneAgent

## Шаг 1. Создание сертификата и ключа разработчика

```
dt extension genca


dt extension generate-developer-pem -o developer.pem --ca-crt ca.pem --ca-key ca.key --name 'JDoe'
```

Команда создаёт следующие файлы:

* `developer.pem` — ваш сертификат разработчика
* `ca.pem` — ваш корневой сертификат
* `ca.key` — ваш корневой ключ

## Шаг 2. Распространение корневого сертификата на компоненты Dynatrace

### Загрузка в Dynatrace Credential Vault

1. Перейдите в раздел **Credential Vault**.
2. Выберите **Add new credential**.
3. В поле **Credential type** выберите **Public Certificate**.
4. Выберите область действия учётных данных **Extension validation**.
5. Добавьте понятное **Credential name**.
6. Загрузите файл **Root certificate file**.
7. Нажмите **Save**.

### Загрузка на хост OneAgent, выполняющий расширение

1. Перейдите в следующий каталог:

   * Windows: `C:\ProgramData\dynatrace\oneagent\agent\config`
   * Linux: `/var/lib/dynatrace/oneagent/agent/config/`
2. Перейдите в папку `certificates` (создайте её, если она не существует)
3. Загрузите ваш корневой сертификат (`ca.pem`), созданный ранее

Ваша среда Dynatrace готова к созданию расширения WMI.

**Следующий шаг**: Пакет расширения
