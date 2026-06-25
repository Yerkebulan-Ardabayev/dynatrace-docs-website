---
title: Мониторинг AWS Elastic Beanstalk
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk
scraped: 2026-05-12T11:14:21.482539
---

# Мониторинг AWS Elastic Beanstalk

# Мониторинг AWS Elastic Beanstalk

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 19 июля 2017 г.

[AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/faqs/), это сервис Amazon Web Services (AWS), который позволяет развёртывать и автоматически масштабировать приложения и сервисы.

Поскольку этот тип установки сильно зависит от пользовательских настроек, единого набора шагов, подходящего для всех сценариев, не существует. Ниже приведён общий обзор процесса с примерами, которые помогут вам создать собственное развёртывание.

## Предварительные требования

* Определите `ONEAGENT_INSTALLER_SCRIPT_URL`. Эта информация выдаётся при установке Dynatrace OneAgent.

Определите URL вашего установщика

Чтобы получить `ONEAGENT_INSTALLER_SCRIPT_URL`

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **Linux**.

3. Определите URL скрипта установщика и токен из команды `wget`, предоставленной в UI:

OneAgent container image версии 1.39.1000+

OneAgent container image версии 1.38.1000 и ниже

Это URL:

![OneAgent URL](https://dt-cdn.net/images/oneagent-url-570-2bbd3eb216.png)

OneAgent URL

* Замените значение параметра `arch` на `<arch>`. Игнорируйте параметр `flavor=default`.
* Для значения `API-Token` понадобится [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его области действия.").

Ваш URL должен выглядеть так:
`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=<arch>`

Это и есть ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

Это ваш URL и API-токен.

![Страница установки OneAgent с URL, который требуется изменить](https://dt-cdn.net/images/oneagent-linux-install-url-734-22e9ac9a69.png)

Страница установки OneAgent с URL, который требуется изменить

Добавьте API-токен к URL через параметр `API-Token`. Ваш URL должен выглядеть так:

`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<token>`

Это и есть ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

* Доступ к консоли AWS

Для конфигураций, где OneAgent уже включён в развёртывание вашего приложения, не нужно вручную устанавливать OneAgent или перезапускать серверы, чтобы включить мониторинг сервисов.

## Загрузка OneAgent

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **Windows** или **Linux**.

Подробнее см. в инструкциях по установке OneAgent для [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows "Узнайте, как скачать и установить Dynatrace OneAgent на Windows.") или [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux "Узнайте, как скачать и установить Dynatrace OneAgent на Linux.").

## Настройка установки

* Убедитесь, что конфигурационные файлы являются корректно отформатированными YAML-файлами.
* Не используйте табуляцию для отступов. Допустимы только пробелы.
* Имена файлов расширений Elastic Beanstalk важны, интерпретатор Amazon выполняет их в алфавитном порядке.

Linux

Windows

Для установки OneAgent понадобятся два конфигурационных файла:

* Один файл для загрузки установщика OneAgent
* Другой файл для запуска установки и пост-установочных задач.

1. В пакете развёртывания Beanstalk создайте директорию `.ebextensions` в той же папке, что и исходный код основного проекта Beanstalk. Упомянутые выше два конфигурационных файла должны быть размещены в этой директории.
2. Создайте конфигурационный файл для загрузки установщика с именем `0dynatraceDownload.config`.

   Файл должен содержать секцию `files`, определяющую:

   * Путь загрузки и имя целевого файла (например, `/tmp/dynatraceinstall.sh`)
   * Правильные настройки прав пользователя
   * URL для загрузки OneAgent, указанный в предварительных требованиях.

   Пример:

   ```
   files:



   "/tmp/dynatraceinstall.sh":



   mode: "000755"



   owner: root



   group: root



   source: "https://abcdefghij.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=abcdefghijklmnopqrstu"
   ```

   Не забудьте заменить шаблонные значения в примере выше на свои собственные.
3. Создайте конфигурационный файл для запуска установщика OneAgent и выполнения других задач, таких как перезапуск сервиса, с именем `1dynatraceInstallAndPost.config`.

   В примере ниже скрипт проверяет наличие установленного OneAgent и, если OneAgent не найден, запускает установку из директории `/tmp`, передавая параметр установки `--set-proxy=172.1.1.128:8080` для подключения агента к определённому прокси. Затем перезапускается сервис `httpd`.

   ```
   commands:



   install_dynatrace:



   cwd: /tmp



   command: "/bin/sh dynatraceinstall.sh --set-proxy=172.1.1.128:8080"



   restart_httpd:



   command: "service httpd restart"
   ```

   Если хотите добавить дополнительные параметры, разделяйте их пробелами. Подробнее о параметрах установки см. в разделе [как настроить установку OneAgent на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик Linux с параметрами командной строки.").

   Не используйте свойство `env` у команды, поскольку оно перезаписывает, а не дополняет существующее окружение, что приведёт к сбою установки OneAgent.
4. Опционально. Расширьте свою конфигурацию.

   В конфигурацию также можно включить шаги для загрузки OneAgent.

   В примере ниже загрузка OneAgent включена в конфигурацию. Это необходимо для первой установки OneAgent, но может существенно удлинить будущие обновления приложения, поскольку OneAgent будет загружаться при каждом запуске скрипта. Чтобы улучшить конфигурацию Beanstalk, добавьте проверку наличия установленного OneAgent и пусть ваши скрипты загружают OneAgent только тогда, когда он не найден в системе.

   Внимательно изучите приведённый ниже пример конфигурации для Linux перед созданием своих скриптов. Интерпретатор Amazon чувствителен к синтаксическим ошибкам. Будьте аккуратны с форматированием и экранированием специальных символов.

   ```
   files:



   "/tmp/dynatraceinstall.sh":



   mode: "000755"



   owner: root



   group: root



   content: |



   #!/bin/bash



   if [ ! -d /opt/dynatrace/oneagent ]; then



   wget -O /tmp/Dynatrace-OneAgent.sh "https://abcdefghij.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=abcdefghijklmnopqrstu"



   chmod 755 /tmp/Dynatrace-OneAgent.sh



   sudo chown root:root /tmp/Dynatrace-OneAgent.sh



   sudo /tmp/Dynatrace-OneAgent.sh



   fi



   commands:



   install_dynatrace:



   cwd: /tmp



   command: "/bin/sh dynatraceinstall.sh --set-proxy=172.1.1.128:8080"



   restart_nginx:



   command: service nginx restart



   ignoreErrors: true
   ```

Для установки OneAgent понадобятся два конфигурационных файла:

* Один файл для загрузки установщика OneAgent
* Другой файл для запуска установки и пост-установочных задач.

1. Создайте конфигурационный файл для загрузки установщика с именем `0dynatraceDownload.config`.

   Файл должен содержать секцию `sources`, определяющую:

   * Назначение загрузки (например, ваш рабочий стол)
   * URL для загрузки OneAgent, указанный в предварительных требованиях.

   Пример:

   ```
   files:



   "C:/OneAgent/Dynatrace-OneAgent-Installer.exe":



   source: "https://abcdefghij.live.dynatrace.com/api/v1/deployment/installer/agent/windows/default/latest?Api-Token=abcdefghijklmnopqrstu&arch=x86&flavor=default"
   ```

   Не забудьте заменить шаблонные значения в примере выше на свои собственные.
2. Создайте конфигурационный файл для запуска установщика OneAgent и выполнения других задач, таких как перезапуск сервиса, с именем `1dynatraceInstallAndPost.config`.

   Файл должен содержать секцию `commands`, определяющую команду установки OneAgent.

   Не используйте свойство `env` у команды, поскольку оно перезаписывает, а не дополняет существующее окружение, что приведёт к сбою установки OneAgent.

   В примере ниже скрипт запускает установщик из папки рабочего стола администратора в тихом режиме (без графического интерфейса). Файл передаёт параметр установки `--set-proxy=172.1.1.128:8080` для подключения агента к определённому прокси.

   ```
   commands:



   install_oneagent:



   command: "C:/OneAgent/Dynatrace-OneAgent-Installer.exe --quiet --set-proxy=172.1.1.128:8080"
   ```

   Если хотите добавить дополнительные параметры, разделяйте их пробелами. Подробнее о параметрах установки см. в разделе [как настроить установку OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows.").

   Не нужно добавлять дополнительные команды после установки OneAgent. Amazon самостоятельно перезапустит IIS после успешной загрузки всех файлов вашего приложения.

## Настройка сетевых зон Опционально

Чтобы настроить сетевые зоны, используйте следующий аргумент: `--set-network-zone=<your.network.zone>`. Подробнее см. в разделе [сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").

## Потребление ресурсов мониторинга

Для AWS Elastic Beanstalk потребление ресурсов мониторинга рассчитывается на основе host units. Подробности см. в разделе [Мониторинг приложений и инфраструктуры (Host Units)](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Узнайте, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе host units.").

## Связанные темы

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Изучите ключевые концепции OneAgent и узнайте, как устанавливать и эксплуатировать OneAgent на различных платформах.")
* [Ограничение API-вызовов к AWS с помощью тегов](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Добавьте и настройте теги AWS, чтобы ограничить ресурсы AWS.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на различных платформах.")