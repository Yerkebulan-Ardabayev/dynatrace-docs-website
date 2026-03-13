---
title: WMI data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions
scraped: 2026-03-03T21:24:12.065610
---

# Источник данных WMI

# Источник данных WMI

* Latest Dynatrace
* Руководство
* Чтение: 3 мин.
* Опубликовано 21 апреля 2021 г.

Dynatrace предоставляет фреймворк, который вы можете использовать для расширения наблюдаемости с помощью данных, получаемых непосредственно от устройств, мониторимых через Windows Management Instrumentation (WMI).

Мы предполагаем следующее:

* Вы обладаете достаточной экспертизой в области Windows и WMI для создания расширения WMI.
* Вы знакомы с [основными концепциями расширений](../../concepts.md "Узнайте больше о концепции расширений Dynatrace.") и общей структурой [YAML-файла расширения](../extension-yaml.md "Узнайте, как создать YAML-файл расширения с помощью фреймворка Extensions.").

## Предварительные требования и поддержка

Ознакомьтесь с предварительными требованиями и областью поддерживаемых технологий. Информацию об ограничениях, применимых к вашему расширению, см. в разделе [Ограничения расширений](../../concepts.md "Узнайте больше о концепции расширений Dynatrace.").

### Поддерживаемые версии Dynatrace

* Dynatrace версии 1.215+
* Environment ActiveGate на основе Windows версии 1.215+
* OneAgent версии 1.221+ (локальные расширения)

### Мониторимый хост

Локальные расширения WMI могут выполняться на любом поддерживаемом OneAgent хосте Windows без каких-либо специальных требований. Убедитесь, что Extension Execution Controller (EEC) включён на уровне среды или выбранного хоста. Для получения дополнительной информации см. [Extension Execution Controller](../../concepts.md#eec "Узнайте больше о концепции расширений Dynatrace.").

Хост, который вы хотите мониторить с помощью удалённого расширения WMI, должен соответствовать требованиям, описанным ниже, включая включённые удалённые разрешения и настроенные параметры подключения, чтобы ваш ActiveGate мог получить доступ к данным мониторинга WMI.

#### Разрешение удалённого доступа на хосте

На мониторимом хосте должно быть установлено разрешение **Remote enable**.

1. В консоли Microsoft [Server Manager](https://docs.microsoft.com/en-us/windows-server/administration/server-manager/server-manager) перейдите в **Administrative Tools** > **Computer Management**.
2. Раскройте **Services and Applications**, щёлкните правой кнопкой мыши **WMI Control** и выберите **Properties**.
3. Выберите вкладку **Security**, а затем нажмите кнопку **Security**.
4. Добавьте пользователя, которого вы будете использовать для вызова WMI, и затем выберите **Remote Enable** в столбце **Allow**.

Для получения дополнительной информации см. [Разрешение доступа пользователей к определённому пространству имён WMI](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection#allowing-users-access-to-a-specific-wmi-namespace) в документации Microsoft.

#### Настройка файрвола для доступа к удалённому WMI

Чтобы настроить файрвол для доступа к удалённому WMI, выполните следующие команды:

```
netsh advfirewall firewall set rule group="windows management instrumentation (wmi)" new enable=yes
```

и

```
netsh firewall set service RemoteAdmin enable
```

Для получения дополнительной информации см. [Настройка удалённого подключения WMI](https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista) в документации Microsoft.

#### Отключение удалённого UAC

Отключите удалённый UAC при использовании учётной записи локального администратора (без Active Directory).

```
New-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LocalAccountTokenFilterPolicy -PropertyType DWord -Value 1 -Force
```

Для получения дополнительной информации см. [Обработка удалённых подключений под UAC](https://docs.microsoft.com/en-us/windows/win32/wmisdk/user-account-control-and-wmi#handling-remote-connections-under-uac) в документации Microsoft.

#### Настройка локального пользователя

Для установления подключения к удалённому хосту WMI необходимо использовать либо стандартного пользователя, либо пользователя с правами администратора, в зависимости от типа данных, которые вы хотите получить. Вы добавите этого пользователя в [конфигурации мониторинга](#monitoring-configuration). Мы рекомендуем создать выделенную локальную группу пользователей или учётную запись пользователя на целевом компьютере специально для удалённых подключений.

Чтобы ограничить привилегии пользователя для доступа только к удалённому подключению к WMI:

1. В Windows выполните команду `DCOMCNFG`.
2. Перейдите в **Component Services** > **Computers**, щёлкните правой кнопкой мыши **My Computer** и выберите **Properties**.
3. Выберите вкладку **COM Security**.
4. В разделе **Launch and Activation Permissions** нажмите **Edit Limits**.
5. Выберите имя **ANONYMOUS LOGON** в списке **Group or user names**. В разделе **Permissions for ANONYMOUS LOGON** выберите **Remote Launch** и **Remote Activation** в столбце **Allow**.
6. Нажмите **OK** для сохранения.

Для получения дополнительной информации см. документацию Microsoft:

* [Защита удалённого подключения WMI](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection)
* [Ограничение доступа к пространствам имён WMI](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-namespace-security-with-the-wmi-control)
* [Доступ к пространствам имён WMI](https://docs.microsoft.com/en-us/windows/win32/wmisdk/access-to-wmi-namespaces)

#### Настройка фиксированного порта для WMI

1. В командной строке введите:
   `winmgmt -standalonehost`
2. Остановите службу WMI:
   `net stop winmgmt`
3. Перезапустите службу WMI в новом хосте службы:
   `net start winmgmt`
4. Установите новый номер порта для службы WMI:
   `netsh firewall add portopening TCP 24158 WMIFixedPort`

Для получения дополнительной информации см. [Настройка фиксированного порта для WMI](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-up-a-fixed-port-for-wmi) в документации Microsoft.
