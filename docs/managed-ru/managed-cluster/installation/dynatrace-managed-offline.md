---
title: Установка Dynatrace Managed в офлайн-режиме
source: https://docs.dynatrace.com/managed/managed-cluster/installation/dynatrace-managed-offline
scraped: 2026-05-12T11:53:33.227172
---

# Установка Dynatrace Managed в офлайн-режиме

# Установка Dynatrace Managed в офлайн-режиме

* How-to guide
* 8-min read
* Updated on May 08, 2026

Dynatrace Managed доступен в офлайн-версии. В офлайн-режиме Dynatrace Managed использует офлайн-лицензию, которая отключает все функции, требующие подключения к интернету, — такие как подключение к [Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") для отчётности по лицензиям и проверок работоспособности, а также получение автоматических обновлений кластера.

В офлайн-режиме вы самостоятельно несёте ответственность за поддержание Dynatrace Managed в актуальном состоянии и за отчётность по использованию лицензии в Dynatrace.

## Офлайн-режим vs. онлайн-режим

| Этап установки | Онлайн-режим | Офлайн-режим |
| --- | --- | --- |
| Установка — лицензия[1](#fn-1-1-def) | лицензионный ключ | файл лицензии |
| Установка — проверка подключения к Mission Control | Да (обязательно) | Нет (пропускается) |
| Установка — проверка лицензии через Mission Control[2](#fn-1-2-def) | Да (обязательно) | Использование лицензии необходимо отчитываться вручную через [Экспорт данных лицензии](/managed/managed-cluster/operation/export-license-data "Learn how to export license data from the Cluster Management Console.") |
| Установка — загрузка и установка самомониторинг-OneAgent | Да (необязательно) | Нет (пропускается) |
| Сервер — загрузка обновлений (включая OneAgent, RUM JavaScript, ActiveGate, смещения NGINX)[3](#fn-1-3-def) | Автоматически из Mission Control | Вручную из письма с обновлениями |
| Сервер — управление сертификатами | Автоматически из Mission Control | По умолчанию предоставляются только самоподписанные сертификаты |
| Сеть — требуемые порты | [Порты узла кластера](/managed/managed-cluster/installation/cluster-node-ports "Review the network ports required by Dynatrace Managed and configure your firewall for inbound and outbound communication.") | Те же, что и для онлайн-режима, за исключением подключения к Mission Control и hosted самомониторинга |
| Mission Control — обновления | Опубликованные обновления автоматически синхронизируются с Managed Cluster | URL опубликованных обновлений отправляются по электронной почте контактным лицам по лицензии |
| Mission Control — статистика проверок работоспособности | Проверка работоспособности обновляется каждые 5 минут | Статистика проверок недоступна |
| Mission Control — обновления лицензии | Обновления лицензии синхронизируются каждые 5 минут с Managed Cluster | Лицензия должна обновляться вручную через Cluster Management Console |
| Mission Control — определяет первичную (выжившую) часть кластера Premium HA | Автоматически из Mission Control | Не поддерживается |
| Политика поддержки Dynatrace | [3 месяца](/managed/whats-new/managed "Release notes for Dynatrace Managed") + 1 месяц с Enterprise Success and Support | [3 месяца](/managed/whats-new/managed "Release notes for Dynatrace Managed") + 1 месяц с Enterprise Success and Support |

1

Для установки в офлайн-режиме передайте файл лицензии с помощью параметра `--license-file <license-filename>`. Письмо с активацией содержит полную команду установки с этим параметром и прикреплённым файлом офлайн-лицензии. В журнале установки офлайн-режим подтверждается записями `offline mode is active`.

2

Сервер проверяет лицензию после запуска (не в процессе установки) с помощью подписи (хэша), включённой в файл лицензии. Установщик копирует файл лицензии в директорию `config` сервера. Запись `license.file` в файле `config.properties` сервера содержит путь к этому файлу.

3

Кластер Dynatrace не включает пакеты установки OneAgent или ActiveGate — в онлайн-режиме они загружаются автоматически из Mission Control. В офлайн-режиме их необходимо добавлять вручную. Ссылки для загрузки предоставляются в письме с активацией.

## Установка Managed Cluster в офлайн-режиме

Для установки Managed Cluster в офлайн-режиме следуйте приведённым ниже шагам.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Проверка требований**](/managed/managed-cluster/installation/dynatrace-managed-offline#review-requirements "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Загрузка файлов**](/managed/managed-cluster/installation/dynatrace-managed-offline#download-files "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Проверка установщика**](/managed/managed-cluster/installation/dynatrace-managed-offline#verify-installer "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Получение SBOM-файла**](/managed/managed-cluster/installation/dynatrace-managed-offline#retrieve-sbom "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Запуск установщика**](/managed/managed-cluster/installation/dynatrace-managed-offline#install-cluster "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Активация лицензии**](/managed/managed-cluster/installation/dynatrace-managed-offline#activate-license "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

**Загрузка пакета агентов**](/managed/managed-cluster/installation/dynatrace-managed-offline#upload-agents "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")

### Шаг 1. Проверка требований

Убедитесь, что ваша система соответствует [требованиям к аппаратному обеспечению](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.") и [системным требованиям](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.").

Не устанавливайте хранилища данных компонентов Dynatrace Managed на сетевые или удалённые диски — это может привести к проблемам с производительностью и стабильностью.

### Шаг 2. Загрузка файлов

Загрузите следующие файлы из письма с активацией и скопируйте их в директорию на вашем Linux-хосте, куда необходимо установить Dynatrace Managed:

* Файл лицензии (**license.lic**).
* Установщик Dynatrace Managed (**cluster installer**).
* Пакеты установки OneAgent, RUM JavaScript, ActiveGate и Synthetic (**agents bundle**).

Пример письма с активацией

![managed-activation-email](https://dt-cdn.net/images/managed-activation-email-1075-e07fd3fa2f.png)

managed-activation-email

### Шаг 3. Проверка установщика

Файл установщика Dynatrace Managed снабжён цифровой подписью. Совместно с OpenSSL и [корневым сертификатом Dynatrace](https://ca.dynatrace.com/dt-root.cert.pem) файл подписи подтверждает подлинность установщика. Файл подписи имеет то же имя, что и установщик, с расширением `.sig`.

1. Загрузите корневой сертификат Dynatrace и файл подписи установщика по ссылкам, указанным в письме с активацией.
2. Проверьте подпись файла установщика с помощью следующей команды:

   ```
   openssl cms -inform PEM -binary -verify -CAfile dt-root.cert.pem -in dynatrace-managed-<version>.sh.sig -content dynatrace-managed-<version>.sh > /dev/null
   ```

   Замените `<version>` на версию Dynatrace Managed.
3. При успешной проверке ответом будет `Verification successful`. При неудачной — `Verification failure` с подробностями.

### Шаг 4 (необязательно). Получение Software Bill of Materials

Следуйте инструкциям из шага 3 руководства по установке кластера для [получения SBOM-файла](/managed/managed-cluster/installation/install-managed-cluster#retrieve-sbom "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.").

### Шаг 5. Запуск установщика

Следуйте инструкциям из разделов [Запуск установщика](/managed/managed-cluster/installation/install-managed-cluster#run-installer "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") (шаг 4) и [Финализация](/managed/managed-cluster/installation/install-managed-cluster#finalize-setup "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.") (шаг 5) руководства по установке кластера. Используйте параметр `--license-file` вместо лицензионного ключа:

```
sudo /bin/sh dynatrace-managed-<version>.sh --license-file license.lic
```

Замените `<version>` на версию Dynatrace Managed.

### Шаг 6. Активация лицензии

После установки активируйте лицензию.

1. Войдите в **Cluster Management Console**.
2. Перейдите в **Licensing** и выберите **Activate license**.

   * При наличии доступа к интернету вы будете перенаправлены на внешнюю форму регистрации ([https://mcsvc.dynatrace.com/register.html](https://mcsvc.dynatrace.com/register.html)) с предзаполненными полями. Проверьте данные и отправьте форму.

     + При отсутствии доступа к интернету откройте `https://mcsvc.dynatrace.com/register.html` в браузере с доступом к интернету и заполните форму вручную.
     + Обязательно: **License key** и **Cluster identifier**
     + Необязательно: **Installed version** (текущая версия кластера) и **Cluster admin email address** (адрес электронной почты, по которому эксперты Dynatrace могут связаться с администраторами кластера в случае аварии)
3. Выберите **Activate license**. На следующей странице будет подтверждена активация лицензии.
4. На странице подтверждения выберите **Download license file** для загрузки файла `license-activated.lic`.
5. Выберите **Go to Licensing page**.
6. На странице **Licensing** выберите **More** (**…**) > **Apply license** в правом верхнем углу.
7. Выберите загруженный ранее файл `license-activated.lic`.

   * После применения лицензии её статус изменится на **Active**.

### Шаг 7. Загрузка пакета агентов

Для загрузки пакета агентов в кластер:

1. Войдите в **Cluster Management Console**.
2. Перейдите в **Settings** > **Automatic update**.
3. Выберите **Upload installation package** для загрузки пакета в кластер.

Альтернативно можно вручную скопировать пакет агентов в следующую директорию на вашем Linux-хосте:

```
/var/opt/dynatrace-managed/agents
```

## Обновление Managed Cluster в офлайн-режиме

Следуйте инструкциям по [полуавтоматическому обновлению Managed Cluster](/managed/managed-cluster/operation/update-cluster#semi-automatic-update "Learn how to update a Managed cluster and how to schedule an automatic update.") из руководства по обновлению.

## Часто задаваемые вопросы

Что делать при ошибке загрузки пакета установки?

Ошибка загрузки пакета установки, как правило, возникает при попытке загрузить полный пакет, содержащий установщик Managed, OneAgent, RUM JavaScript, ActiveGate и Synthetic. В этом случае размер пакета превышает ограничение на загрузку в 2 ГБ.

1. Войдите в **Cluster Management Console**.
2. Перейдите в **Settings** > **Automatic update**.
3. Выберите **Upload installation package** для загрузки только выбранных пакетов установки в кластер.

Альтернативно можно вручную скопировать пакеты установки в следующие директории на каждом узле кластера.

* Для кластера:

  ```
  /opt/dynatrace-managed/installer/upgrade
  ```
* Для OneAgent, RUM JavaScript, ActiveGate и Synthetic:

  ```
  /var/opt/dynatrace-managed/agents
  ```

Что делать при проблемах с лицензией?

Если файл лицензии повреждён, установка завершается, сервер запускается, но указывает на проблему с лицензией. В этом случае загрузите новую лицензию в **Cluster Management Console**. Подробности см. в разделе [Обновление офлайн-лицензии](#update-license).

Как обновить лицензию?

Для обновления лицензии:

1. Загрузите файл `license.lic` из письма с активацией.
2. Войдите в **Cluster Management Console**.
3. Перейдите в **Licensing** и примените новую лицензию.

Как получить диагностические данные для дальнейшего анализа?

В **Cluster Management Console** можно загрузить диагностические данные. Подробности см. в разделе [Диагностические архивы](/managed/managed-cluster/operation/diagnostic-archives-for-managed-installations "Learn how you can download a support archive that contains configuration and log files from all installed Dynatrace Managed components of a cluster node.").