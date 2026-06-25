---
title: Установка OneAgent с помощью Ansible
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/deployment-orchestration/ansible
scraped: 2026-05-12T11:35:18.354639
---

# Установка OneAgent с помощью Ansible

# Установка OneAgent с помощью Ansible

* 5-min read
* Published Sep 25, 2020

Dynatrace предоставляет коллекцию Ansible, которую можно использовать для оркестрации развёртывания OneAgent в вашем окружении.

## Требования

* Ansible >= 2.15.0
* OneAgent версии 1.199+
* Dynatrace версии 1.204+
* Доступ к файлам установщика OneAgent через скрипт

## Зависимости

### Windows

* pywinrm 0.4.3+

## Установка коллекции Dynatrace Ansible

Проект коллекции Dynatrace Ansible размещён на [GitHub](https://github.com/Dynatrace/Dynatrace-OneAgent-Ansible) и доступен через [Ansible Galaxy](https://galaxy.ansible.com/ui/repo/published/dynatrace/oneagent/).
Для установки коллекции Ansible `dynatrace.oneagent` выполните следующую команду:

```
ansible-galaxy collection install dynatrace.oneagent
```

Коллекция состоит из одной роли Ansible, которая развёртывает OneAgent с использованием специальной конфигурации. Конфигурация гарантирует, что сервис OneAgent остаётся в рабочем состоянии. Подробнее смотрите в разделе [Использование коллекций](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) в документации Ansible.

## Настройка коллекции Dynatrace Ansible

Скрипт Ansible требует доступа к соответствующим файлам установщика OneAgent.

* Если управляющий узел Ansible имеет доступ к вашему окружению Dynatrace, можно настроить скрипт для непосредственной загрузки файлов установщика из окружения Dynatrace.
* Или можно самостоятельно загрузить нужные файлы установщика через веб-интерфейс Dynatrace и загрузить их на управляющий узел. Это предоставит скрипту локальные копии установщиков.

### Вариант 1: прямая загрузка из окружения Dynatrace

Скрипт использует [Deployment API](/managed/dynatrace-api/environment-api/deployment "Загрузка установщиков OneAgent и ActiveGate через API Dynatrace.") для загрузки установщиков для конкретных платформ на управляемые узлы. Для аутентификации вызова API необходимо задать следующие переменные:

* `oneagent_environment_url`:

  + **SaaS**: `https://{your-environment-id}.live.dynatrace.com`
  + **Managed**: `https://{your-domain}/e/{your-environment-id}`
* `oneagent_paas_token`

  + [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях.") вашего окружения

    Например:

    ```
    # Set environment variables



    oneagent_environment_url: 'https://your-environment.live.dynatrace.com'



    oneagent_paas_token: 'abcdefjhij1234567890'
    ```

Рекомендуем хранить PaaS-токен и Environment ID в безопасном месте, используя механизмы шифрования, такие как Ansible Vault. Подробности смотрите в разделе [Шифрование содержимого с помощью Ansible Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html).

### Вариант 2: использование локальных установщиков

Загрузите необходимые файлы установщика OneAgent через веб-интерфейс Dynatrace и загрузите их на управляющий узел. Скрипт Ansible скопирует файлы установщика на управляемые узлы при выполнении.

Используйте переменную `oneagent_local_installer`, чтобы указать роли Ansible путь к файлу установщика. Например:

```
oneagent_local_installer: /path/of/oneagent_linux_installer.sh
```

Обратите внимание, что Windows, Linux и AIX требуют собственных установщиков. Исходные имена установщиков, загружаемых из Dynatrace, включают обозначения целевых платформ. Если вы изменяете имена установщиков, убедитесь, что скрипт сможет их различить.

Если локальный установщик не указан, скрипт попытается использовать метод прямой загрузки.

Примеры использования смотрите в файле `local_installer.yml` в разделе [Примеры](#examples).

## Переменные

Роль Ansible для OneAgent поддерживает следующие переменные:

| Имя | Значение по умолчанию | Описание |
| --- | --- | --- |
| `oneagent_environment_url` | не задано | URL целевого окружения Dynatrace (SaaS или Managed) |
| `oneagent_paas_token` | не задано | [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях."), полученный со страницы **PaaS integration** |
| `oneagent_local_installer` | не задано | Путь к установщику OneAgent, хранящемуся на управляющем узле |
| `oneagent_installer_arch` | Linux: `x86` Windows: `x86` AIX: `ppc` | Архитектура установщика OneAgent |
| `oneagent_version` | `latest` | Требуемая версия OneAgent в формате 1.199.247.20200714-111723 |
| `oneagent_download_dir` | Linux/AIX: `$TEMP` или `/tmp` Windows: `%TEMP%` или `C:\Windows\Temp` | Директория загрузки установщика — для Linux и AIX директория не должна содержать пробелов. |
| `oneagent_install_args` | не задано | Параметры установки Dynatrace OneAgent, определённые в виде списка элементов |
| `oneagent_platform_install_args` | не задано | Дополнительный список платформо-специфичных параметров установки, добавляемых к `oneagent_install_args` при запуске на соответствующей платформе |
| `oneagent_preserve_installer` | `false` | Сохранять ли установщик на управляемом узле после установки OneAgent |
| `oneagent_package_state` | `present` | Желаемое состояние пакета OneAgent — укажите `present` или `latest` для установки. Укажите `absent` для удаления. |
| `oneagent_reboot_host` | `false` | Перезагружать ли управляемый узел после установки OneAgent |
| `oneagent_validate_certs` | `true` | Требовать ли наличия сертификатов — если `false`, разрешает загрузку OneAgent с сервера с небезопасным SSL-сертификатом (например, просроченным или самоподписанным). |
| `oneagent_reboot_timeout` | 3600 | Тайм-аут перезагрузки управляемого узла в секундах |

## Логирование

Вместо вывода в STDOUT логи, создаваемые Ansible, можно собирать в единый файл на управляемом узле. Для этого существует несколько способов через настройки конфигурации Ansible:

* Установите переменную окружения `ANSIBLE_LOG_PATH` на путь к файлу логов.
* Укажите переменную `log_path` в разделе `[default]` файла настроек конфигурации Ansible.

Уровень детализации логов можно контролировать с помощью параметра командной строки `-v`. Повторение параметра несколько раз увеличивает уровень детализации вплоть до уровня отладки подключения, который достигается при `-vvvv`.

## Примеры

Следующий пример плейбука:

* Загружает установщик OneAgent конкретной версии (`oneagent_version`) и сохраняет его в пользовательскую директорию (`oneagent_download_dir`).
* Использует переменную `vars_files` для указания на защищённый файл `credentials.yml`, в котором хранятся ваш Environment ID и PaaS-токен.
* Инструктирует скрипт развернуть OneAgent на группах хостов `linux_other` и `linux_arm` в вашем инвентаре.
* Инструктирует скрипт использовать `x86` в качестве архитектуры по умолчанию для группы хостов `linux_other`. В инвентарном файле для группы хостов `linux_arm` указан собственный параметр `oneagent_installer_arch`.
* Использует переменную `oneagent_install_args` для указания параметров установки OneAgent, которые назначают хосты группе хостов `My.HostGroup_123-456` и сетевой зоне `my.network.zone`.
* Устанавливает отличный параметр `USER` с помощью параметра `oneagent_platform_install_args` для каждой группы хостов в инвентаре.

```
---



- name: Download OneAgent installer in specific version to a custom



directory with additional OneAgent install parameters. Both linux_other



and linux_arm have different user specified by platform args parameter.



hosts: linux_other,linux_arm



collections:



- dynatrace.oneagent



vars_files:



- encrypted_credentials.yml



vars:



oneagent_download_dir: /home/user1



oneagent_version: 1.199.247.20200714-111723



oneagent_install_args:



- INSTALL_PATH=/opt/example



- --set-host-group=My.HostGroup_123-456



- --set-network-zone=my.network.zone



tasks:



- import_role:



name: oneagent
```

Дополнительные примеры плейбуков и инвентарных файлов можно найти в директории `examples` внутри роли Ansible. Директория содержит следующие плейбуки:

* `local_installer.yml` — установка OneAgent с использованием локального установщика.
* `advanced_config.yml` — установка OneAgent с пользовательским путём установки и директорией загрузки.
* `oneagentctl_config.yml` — настройка OneAgent с помощью команды `oneagentctl`.

Кроме того, каждая директория содержит инвентарный файл с базовой конфигурацией хостов для плейбуков.

Для решения проблем с путями при установке на Windows ознакомьтесь с разделом [Форматирование путей для Windows в документации Ansible](https://docs.ansible.com/ansible/latest/user_guide/windows_usage.html#path-formatting-for-windows).