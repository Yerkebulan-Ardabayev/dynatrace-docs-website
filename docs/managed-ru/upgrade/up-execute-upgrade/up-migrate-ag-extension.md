---
title: Миграция расширения ActiveGate
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-ag-extension
scraped: 2026-05-12T12:13:58.722587
---

# Миграция расширения ActiveGate

# Миграция расширения ActiveGate

* Published Dec 08, 2023

Если в вашей среде Dynatrace Managed есть расширение Extensions 1.0 или Extensions 2.0 для ActiveGate и его необходимо перенести в среду SaaS, может потребоваться повторное развёртывание пакета расширения, проверка и корректировка конфигурации ActiveGate, а также загрузка расширения в среду SaaS.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Развёртывание пакета расширения**](/managed/upgrade/up-execute-upgrade/up-migrate-ag-extension#deploy-extension "Migrate your ActiveGate extension to SaaS.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Проверка свойств ActiveGate**](/managed/upgrade/up-execute-upgrade/up-migrate-ag-extension#review-properties-new-host "Migrate your ActiveGate extension to SaaS.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Загрузка расширения**](/managed/upgrade/up-execute-upgrade/up-migrate-ag-extension#upload-extension-new-host "Migrate your ActiveGate extension to SaaS.")

## Шаг 1. Развёртывание пакета расширения

Шаги миграции расширений ActiveGate зависят от выбранного метода миграции ActiveGate.

* Если хост ActiveGate не меняется при миграции, директория `plugin_deployment` остаётся нетронутой, и повторное развёртывание пакета расширения не требуется.
* Если хост ActiveGate меняется, скопируйте пакет расширения в директорию развёртывания ActiveGate (`%PROGRAMFILES%\dynatrace\remotepluginmodule\plugin_deployment` или `/opt/dynatrace/remotepluginmodule/plugin_deployment`).

## Шаг 2. Проверка свойств ActiveGate

В разделе **Deployment Status** > **ActiveGates** отфильтруйте по группе ActiveGate, убедитесь, что модули расширений включены, и при необходимости перезапустите службы ActiveGate и Extensions Execution Controller (EEC). Имена свойств для **Module: Extension 1.0** и **Module: Extension 2.0** можно найти в разделе [свойства конфигурации и параметры](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").

## Шаг 3. Загрузка расширения

### Расширение Extensions 1.0

Для загрузки расширения Extensions 1.0 в новую среду SaaS:

1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
2. Выберите **Add new technology monitoring**.
3. В разделе **Monitor remote technologies** выберите **Add ActiveGate extension**.
4. Загрузите пакет расширения.
5. После успешной загрузки расширение должно появиться на странице **Monitored technologies** в веб-интерфейсе Dynatrace на вкладке **Custom extensions**.

   ![Загрузка демонстрационного расширения](https://dt-cdn.net/images/demo-01-uploaded-plugin-1356-7a52b3cc3a.png "Загрузка демонстрационного расширения")

   Загрузка демонстрационного расширения

Обратите внимание, что загрузку в кластер Dynatrace можно автоматизировать с помощью [Extensions SDK](/managed/ingest-from/extensions/develop-your-extensions#upload-plugin-command "Develop your own Extensions in Dynatrace.") или [API Dynatrace](/managed/dynatrace-api/configuration-api/extensions-api/post-an-extension "Upload an extension file to your environment via the Dynatrace API.").

### Расширение Extensions 2.0

Для загрузки расширения Extensions 2.0 в новую среду SaaS:

1. Перейдите в **Extensions**.
2. Прокрутите страницу вниз и выберите **Upload custom Extension 2.0**.
3. Выберите архив расширения (или перетащите его) и загрузите в Dynatrace.

   Dynatrace Hub верифицирует архив и структуру расширения, затем автоматически активирует его после успешной загрузки.
4. Большинство полей заполняются автоматически на основе YAML-файла расширения. Можно добавить примечания к выпуску с информацией, поясняющей причину миграции.

## Развёртывание расширения из Dynatrace Hub

Многие расширения уже доступны в Dynatrace Hub. В этом случае их необходимо установить непосредственно из Dynatrace Hub в вашей среде SaaS.

Для развёртывания расширения из Dynatrace Hub в среде SaaS:

1. Перейдите в **Extensions**.
2. Найдите плитку расширения в разделе **Dynatrace Extensions 2.0 you can add to your environment**.
3. Выберите плитку, затем нажмите **Add to environment**.