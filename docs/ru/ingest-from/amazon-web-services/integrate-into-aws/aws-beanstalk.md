---
title: Monitor AWS Elastic Beanstalk
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk
scraped: 2026-03-06T21:17:54.642583
---

# Мониторинг AWS Elastic Beanstalk

# Мониторинг AWS Elastic Beanstalk

* Classic
* Практическое руководство
* Чтение: 1 мин.
* Опубликовано 19 июля 2017 г.

[AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/faqs/) — это сервис, предоставляемый Amazon Web Services (AWS), который позволяет развёртывать и автоматически масштабировать приложения и сервисы.

Поскольку данный тип установки существенно зависит от пользовательских настроек, не существует единого набора шагов, подходящего для всех сценариев. Ниже приведён обзор всего процесса с примерами, которые помогут вам создать собственное развёртывание.

## Предварительные условия

* Найдите `ONEAGENT_INSTALLER_SCRIPT_URL`. Эта информация предоставляется при установке Dynatrace OneAgent.

Как найти URL установщика

Чтобы получить `ONEAGENT_INSTALLER_SCRIPT_URL`

1. В Dynatrace Hub выберите **OneAgent**.
2. Выберите **Set up** > **Linux**.

3. Определите URL скрипта установщика и токен из команды `wget`, предоставленной в интерфейсе:

Образ контейнера OneAgent версии 1.39.1000+

Образ контейнера OneAgent версии 1.38.1000 и ранее

Вот URL:

![URL OneAgent](https://dt-cdn.net/images/oneagent-url-570-2bbd3eb216.png)

* Замените значение параметра `arch` на `<arch>`. Игнорируйте параметр `flavor=default`.
* В качестве значения `API-Token` вам необходим [PaaS-токен](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях действия.").

Ваш URL должен выглядеть так:
`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=<arch>`

Это ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

Вот ваш URL и API-токен.

![Страница установки OneAgent с URL, который нужно изменить](https://dt-cdn.net/images/oneagent-linux-install-url-734-22e9ac9a69.png)

Добавьте API-токен к URL, используя параметр `API-Token`. Ваш URL должен выглядеть так:

`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<token>`

Это ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

* Доступ к консоли AWS

Для конфигураций, в которых OneAgent уже является частью развёртывания вашего приложения, вам не нужно вручную устанавливать OneAgent или перезапускать серверы для включения мониторинга сервисов.

## Скачивание OneAgent

1. В Dynatrace Hub выберите **OneAgent**.
2. Выберите **Set up** > **Windows** или **Linux**.

Подробнее см. инструкции по установке OneAgent для [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows "Узнайте, как скачать и установить Dynatrace OneAgent на Windows.") или [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux "Узнайте, как скачать и установить Dynatrace OneAgent на Linux.").

## Настройка установки

* Убедитесь, что файлы конфигурации — корректные YAML-файлы.
* Не используйте табуляцию для отступов. Допускаются только пробелы.
* Имена файлов скриптов расширений Elastic Beanstalk важны — интерпретатор Amazon выполняет их в алфавитном порядке.

Linux

Windows

Для установки OneAgent вам понадобятся два файла конфигурации:

* Один файл для скачивания установщика OneAgent
* Другой файл для запуска установки и выполнения задач после установки.

1. В пакете развёртывания Beanstalk создайте каталог `.ebextensions` в том же каталоге, что и основной исходный код проекта Beanstalk. Два упомянутых выше файла конфигурации должны быть размещены в этом каталоге.
2. Создайте файл конфигурации для скачивания установщика с именем `0dynatraceDownload.config`.

   Файл должен содержать раздел `files`, который определяет:

   * Путь скачивания и имя целевого файла (например, `/tmp/dynatraceinstall.sh`)
   * Правильные настройки прав пользователя
   * URL скачивания OneAgent, указанный в предварительных условиях.

   Пример:

   ```
   files:



   "/tmp/dynatraceinstall.sh":



   mode: "000755"



   owner: root



   group: root



   source: "https://abcdefghij.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=abcdefghijklmnopqrstu"
   ```

   Обязательно замените шаблонные значения в приведённом выше примере на ваши собственные.
3. Создайте файл конфигурации для запуска установщика OneAgent и выполнения других задач, таких как перезапуск сервиса, с именем `1dynatraceInstallAndPost.config`.

   В примере ниже скрипт проверяет наличие существующей установки OneAgent и, если OneAgent не найден, выполняет установку из каталога `/tmp`, устанавливая параметр `--set-proxy=172.1.1.128:8080` для подключения агента к определённому прокси-серверу. Затем сервис `httpd` перезапускается.

   ```
   commands:



   install_dynatrace:



   cwd: /tmp



   command: "/bin/sh dynatraceinstall.sh --set-proxy=172.1.1.128:8080"



   restart_httpd:



   command: "service httpd restart"
   ```

   Если вы хотите добавить дополнительные параметры, разделяйте их пробелами. Подробнее о параметрах установки см. в разделе [настройка установки OneAgent на Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик Linux с параметрами командной строки.").

   Не используйте свойство `env` команды, так как оно перезаписывает, а не дополняет существующее окружение и приведёт к сбою установки OneAgent.
4. Необязательно: расширьте вашу конфигурацию.

   Вы также можете включить шаги скачивания OneAgent в вашу конфигурацию.

   Пример ниже включает скачивание OneAgent в конфигурацию. Хотя это необходимо для первой установки OneAgent, это может существенно увеличить время будущих обновлений приложения, так как скачивание OneAgent происходит при каждом запуске скрипта. Для улучшения конфигурации Beanstalk добавьте проверку наличия установленного OneAgent и настройте скрипты на скачивание OneAgent только при его отсутствии в системе.

   Внимательно изучите следующий пример конфигурации Linux перед созданием собственных скриптов. Интерпретатор Amazon чувствителен к синтаксическим ошибкам. Обращайте внимание на форматирование и экранирование специальных символов.

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

Для установки OneAgent вам понадобятся два файла конфигурации:

* Один файл для скачивания установщика OneAgent
* Другой файл для запуска установки и выполнения задач после установки.

1. Создайте файл конфигурации для скачивания установщика с именем `0dynatraceDownload.config`.

   Файл должен содержать раздел `sources`, который определяет:

   * Путь назначения для скачивания (например, ваш рабочий стол)
   * URL скачивания OneAgent, указанный в предварительных условиях.

   Пример:

   ```
   files:



   "C:/OneAgent/Dynatrace-OneAgent-Installer.exe":



   source: "https://abcdefghij.live.dynatrace.com/api/v1/deployment/installer/agent/windows/default/latest?Api-Token=abcdefghijklmnopqrstu&arch=x86&flavor=default"
   ```

   Обязательно замените шаблонные значения в приведённом выше примере на ваши собственные.
2. Создайте файл конфигурации для запуска установщика OneAgent и выполнения других задач, таких как перезапуск сервиса, с именем `1dynatraceInstallAndPost.config`.

   Файл должен содержать раздел `commands`, который определяет команду установки OneAgent.

   Не используйте свойство `env` команды, так как оно перезаписывает, а не дополняет существующее окружение и приведёт к сбою установки OneAgent.

   В примере ниже скрипт запускает установщик из папки администратора в тихом режиме (без графического интерфейса). Файл передаёт параметр установки `--set-proxy=172.1.1.128:8080` для подключения агента к определённому прокси-серверу.

   ```
   commands:



   install_oneagent:



   command: "C:/OneAgent/Dynatrace-OneAgent-Installer.exe --quiet --set-proxy=172.1.1.128:8080"
   ```

   Если вы хотите добавить дополнительные параметры, разделяйте их пробелами. Подробнее о параметрах установки см. в разделе [настройка установки OneAgent на Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows.").

   Вам не нужно добавлять дополнительные команды после установки OneAgent. Amazon самостоятельно перезапустит IIS после успешной загрузки всех файлов приложения.

## Настройка сетевых зон (необязательно)

Для настройки сетевых зон используйте следующий аргумент: `--set-network-zone=<your.network.zone>`. Подробнее см. в разделе [сетевые зоны](/docs/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").

## Потребление мониторинга

Для AWS Elastic Beanstalk потребление мониторинга рассчитывается на основе единиц хостов. Подробности см. в разделе [Мониторинг приложений и инфраструктуры (единицы хостов)](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Узнайте, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе единиц хостов.").

## Связанные темы

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Основные концепции OneAgent, а также установка и эксплуатация OneAgent на различных платформах.")
* [Ограничение вызовов API к AWS с помощью тегов](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Добавление и настройка тегов AWS для ограничения ресурсов AWS.")
* [Матрица поддержки платформ и возможностей OneAgent](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.")
