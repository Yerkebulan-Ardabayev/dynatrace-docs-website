---
title: Подписание расширений
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/sign-extensions
scraped: 2026-05-12T12:02:17.580563
---

# Подписание расширений

# Подписание расширений

* Практическое руководство
* Чтение: 2 мин
* Обновлено 27 апреля 2026 г.

Перед загрузкой расширения в окружение Dynatrace подпишите его для подтверждения подлинности. После подписания сохраните корневой сертификат в специальный каталог на каждом хосте, на котором выполняется расширение: OneAgent или ActiveGate.

* В среде разработки каждый разработчик должен иметь уникальный листовой сертификат. Это обеспечивает прослеживаемость изменений.
* В производственной среде каждое расширение должно быть подписано собственным листовым сертификатом. Это гарантирует подлинность каждого расширения.

## Подписание расширения

В зависимости от потребностей выберите один из следующих методов для подписания и сборки расширения:

* [`dt-extensions-sdk`](https://dynatrace-extensions.github.io/dt-extensions-python-sdk/cli/sign.html): универсальный инструмент командной строки. Рекомендуется
* [Расширение VSCode](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode "Введение в дополнение Dynatrace Extensions для VS Code"): универсальный инструмент на основе редактора. Рекомендуется
* [Использование OpenSSL](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions/manually-openssl "Подпишите расширение вручную с помощью OpenSSL."): стандартная криптографическая библиотека для ручного управления

Dynatrace CLI

Для подписания расширения также можно использовать Dynatrace CLI (`dt-cli`). Поскольку его функциональность полностью входит в состав CLI `dt-extensions-sdk`, применяйте его только как облегчённую альтернативу для сред CI/CD.

Подробнее о [`dt-cli` на GitHub](https://github.com/dynatrace-oss/dt-cli).

## Загрузка корневого сертификата

Загрузите корневой сертификат для повышения безопасности платформы Extensions.

Это позволяет:

* проверять подлинность распространяемых расширений;
* предотвращать возможное распространение вредоносных расширений злоумышленником, получившим контроль над окружением.

### Добавление сертификата в хранилище учётных данных

Добавьте корневой сертификат в [хранилище учётных данных](/managed/manage/credential-vault "Храните учётные данные и управляйте ими в хранилище учётных данных.") Dynatrace. Это необходимо сделать перед загрузкой ZIP-файла расширения в окружение.

При добавлении сертификата используйте следующие настройки:

* Тип учётных данных: `Public certificate`
* Область доступа учётных данных: `Extension validation`

Дополнение [VS Code](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode "Введение в дополнение Dynatrace Extensions для VS Code") выполняет это автоматически. При работе с несколькими окружениями (например, разработки и производства) необходимо добавить сертификат в хранилище учётных данных каждого окружения отдельно.

Для расширений JMX достаточно добавить сертификат в хранилище учётных данных. Сохранять сертификат в файловой системе хоста не нужно.

### Удалённые расширения

Загрузите корневой сертификат на каждый хост ActiveGate в группе ActiveGate, выбранной для выполнения расширений.

Сохраните файл сертификата `root.pem` в следующем расположении:

* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/`
* Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\certificates`

### Локальные расширения

Загрузите корневой сертификат на каждый хост OneAgent или каждый хост OneAgent в группе хостов, выбранной для выполнения расширений.

Сохраните файл сертификата `root.pem` в следующем расположении:

* Linux: `/var/lib/dynatrace/oneagent/agent/config/certificates`
* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config\certificates`

### Права доступа к файлу сертификата

Чтобы Extension Execution Controller мог правильно прочитать сертификат, убедитесь, что файл сертификата имеет корректные права доступа:

Windows:

* OneAgent: файл должен быть доступен для `LOCAL_SYSTEM`
* ActiveGate: файл должен быть доступен для `LOCAL_SERVICE`

Linux:

* OneAgent: файл должен быть доступен для `dtuser`
* ActiveGate: файл должен быть доступен для `dtuserag`

## Загрузка пользовательского расширения

После подписания расширения и загрузки корневого сертификата можно загрузить пользовательское расширение в окружение Dynatrace.

### Устранение ошибок прав доступа

При возникновении ошибок прав доступа при обращении к файлу сертификата (например, `Error opening file /var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/root.pem : Permission denied`):

1. Проверьте права доступа к файлу:

   * Linux:

     + OneAgent: `ls -l /var/lib/dynatrace/oneagent/agent/config/certificates/root.pem`
     + ActiveGate: `ls -l /var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/root.pem`
   * Windows: откройте свойства файла и перейдите на вкладку **Security**.
2. Убедитесь, что права доступа соответствуют описанным в разделе [Права доступа к файлу сертификата](#certificate-file-permissions).
3. После исправления прав доступа к файлу [перезапустите Extension Execution Controller](/managed/ingest-from/extensions/advanced-configuration/eec-custom-configuration#restart-eec "Настройте Extension Execution Controller (EEC)."), если расширение по-прежнему не работает.