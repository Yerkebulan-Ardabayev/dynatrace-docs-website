---
title: Задание пользовательских имён хостов
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments
scraped: 2026-05-12T11:45:00.000000
---

# Set custom host names in dynamic environments

# Задание пользовательских имён хостов

* How-to guide
* 3-min read
* Updated on Apr 18, 2024

Dynatrace, как правило, присваивает обнаруженным хостам имена на основе их DNS-имён, точно так, как они определяются OneAgent. В динамических средах с часто меняющимися экземплярами и именами хостов может быть полезно переопределить эти имена, создав пользовательские.

## Ручное переименование хоста

Чтобы вручную изменить имя хоста:

1. Перейдите в **Hosts** и выберите нужный хост.
2. На странице обзора хоста выберите **More** (**…**) > **Settings**.
3. В разделе **Host name** введите пользовательское имя.
4. Нажмите **Save changes**.

## Автоматизация именования хостов с помощью правил

Можно создать правила именования хостов, применяемые ко всем хостам в среде. Правила применяются в порядке их расположения в списке. Первое совпавшее правило будет использовано для присвоения имени хосту.

Чтобы создать правило именования хостов:

1. Перейдите в **Settings** > **Monitoring** > **Host naming**.
2. Нажмите **Add new rule**.
3. Введите **Rule name**.
4. Выберите **Conditions** для применения правила.
5. Создайте **Name format** (формат имени), используя следующие заменители:

   * `{Host:DetectedName}` — имя, обнаруженное OneAgent.
   * `{Host:Environment}` — среда мониторинга.
   * `{Host:HostGroup}` — группа хостов.
   * `{Host:AWSInstanceId}` — идентификатор экземпляра AWS.
   * `{Host:AWSAutoScalingGroup}` — группа Auto Scaling AWS.
   * `{Host:AWSAvailabilityZone}` — зона доступности AWS.
   * `{Host:AzureScaleSet}` — масштабируемый набор Azure.
   * `{Host:AzureRegion}` — регион Azure.
   * `{Host:GCPZone}` — зона GCP.
   * `{Host:GCPProject}` — проект GCP.
   * `{Host:GCEInstanceId}` — идентификатор экземпляра GCE.
   * `{Host:GCEInstanceName}` — имя экземпляра GCE.
   * `{Host:Tag:[tag_key]}` — значение тега с указанным ключом.
   * `{Host:CustomMetaData:[key]}` — значение пользовательских метаданных с указанным ключом.

6. Нажмите **Save changes**.

## Задание имён хостов через командную строку

### Параметры командной строки OneAgent

OneAgent version 1.189+

Чтобы задать или изменить имя хоста, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-name=my-custom-host-name`
* **Windows**
  `.\oneagentctl.exe --set-host-name=my-custom-host-name`

Чтобы сбросить имя хоста до обнаруженного автоматически, выполните:

* **Linux** и **AIX**
  `./oneagentctl --set-host-name=`
* **Windows**
  `.\oneagentctl.exe --set-host-name=`

Подробнее о `oneagentctl` см. в разделе [Конфигурация OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-name "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Редактирование файла конфигурации имени хоста

OneAgent version 1.187 и ниже

При установке OneAgent на хост создаётся файл конфигурации `hostname.conf`. В Windows файл расположен в `%PROGRAMDATA%\dynatrace\oneagent\agent\config`, в Linux — в `/var/lib/dynatrace/oneagent/agent/config`.

Чтобы задать пользовательское имя хоста, добавьте его в файл `hostname.conf`. Файл должен содержать только одну строку с именем хоста. Например:

```
my-custom-host-name
```

OneAgent считывает имя хоста из этого файла при каждом запуске или перезапуске.