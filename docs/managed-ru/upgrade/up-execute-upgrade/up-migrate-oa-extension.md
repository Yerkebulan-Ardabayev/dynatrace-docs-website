---
title: Миграция расширения OneAgent
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-oa-extension
scraped: 2026-05-12T12:13:57.548603
---

# Миграция расширения OneAgent

# Миграция расширения OneAgent

* Published Dec 08, 2023

При перенастройке или переустановке существующих OneAgent для перенаправления в среду SaaS папка `plugin_deployment` остаётся нетронутой в обоих сценариях. Поэтому повторное развёртывание пакета расширения не требуется. Единственный необходимый шаг — загрузка расширения в новую среду SaaS.

## Загрузка расширения OneAgent

Для загрузки расширения OneAgent:

1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
2. Выберите **Add new technology monitoring**.
3. В разделе **Monitor any technology** выберите **Add OneAgent extension**.
4. Загрузите пакет расширения.
5. После успешной загрузки расширение должно появиться на странице **Monitored technologies** в веб-интерфейсе Dynatrace на вкладке **Custom extensions**.

   ![Загрузка демонстрационного расширения](https://dt-cdn.net/images/demo-01-uploaded-plugin-1356-7a52b3cc3a.png "Загрузка демонстрационного расширения")

   Загрузка демонстрационного расширения

Обратите внимание, что загрузку в кластер Dynatrace можно автоматизировать с помощью [Extensions SDK](/managed/ingest-from/extensions/develop-your-extensions#upload-plugin-command "Develop your own Extensions in Dynatrace.") или [API Dynatrace](/managed/dynatrace-api/configuration-api/extensions-api/post-an-extension "Upload an extension file to your environment via the Dynatrace API.").

## Загрузка расширения Extensions 2.0

Для загрузки расширения Extensions 2.0:

1. Перейдите в **Extensions**.
2. Прокрутите страницу вниз и выберите **Upload custom Extension 2.0**.
3. Выберите архив расширения (или перетащите его) и загрузите в Dynatrace. Dynatrace Hub верифицирует архив и структуру расширения и автоматически активирует его после успешной загрузки.
4. Большинство полей заполняются автоматически на основе YAML-файла расширения. Можно добавить примечания к выпуску с информацией, поясняющей причину миграции.

## Развёртывание расширения из Dynatrace Hub

Многие расширения уже доступны в Dynatrace Hub. В этом случае их необходимо установить из Hub вашей среды SaaS.

Для установки расширения из Dynatrace Hub:

1. Перейдите в **Extensions**.
2. Найдите плитку расширения в разделе **Dynatrace Extensions 2.0 you can add to your environment**.
3. Выберите плитку, затем нажмите **Add to environment**.