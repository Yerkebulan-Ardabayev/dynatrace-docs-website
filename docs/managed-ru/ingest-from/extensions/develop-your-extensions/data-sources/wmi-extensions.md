---
title: Источник данных WMI
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions
scraped: 2026-05-12T11:50:08.777265
---

# Источник данных WMI

# Источник данных WMI

* Практическое руководство
* Чтение: 3 мин
* Обновлено 4 марта 2026 г.

Dynatrace предоставляет платформу для расширения наблюдаемости с помощью данных, получаемых напрямую с устройств под мониторингом Windows Management Instrumentation (WMI).

Предполагается следующее:

* У вас достаточно знаний по Windows и WMI для создания расширения WMI.
* Вы знакомы с [основными концепциями Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.") и общей структурой [YAML-файла расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать файл YAML расширения с помощью платформы Extensions framework.").

## Предварительные требования и поддержка

Изучите предварительные требования и область поддерживаемых технологий. Об ограничениях, применяемых к расширению, см. в разделе [Ограничения Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.").

### Поддерживаемые версии Dynatrace

* Dynatrace версии 1.215+
* ActiveGate среды на базе Windows версии 1.215+
* OneAgent версии 1.221+ (локальные расширения)

### Отслеживаемый хост

Локальные расширения WMI можно запускать на любом хосте Windows, поддерживаемом OneAgent, без дополнительных требований. Убедитесь, что Extension Execution Controller (EEC) включён на уровне среды или выбранного хоста. Дополнительные сведения см. в разделе [Extension Execution Controller](/managed/ingest-from/extensions/concepts#eec "Подробнее о концепции Dynatrace Extensions.").

Хост, который требуется отслеживать с помощью удалённого расширения WMI, должен соответствовать описанным ниже требованиям, включая включённые удалённые разрешения и настроенные параметры подключения, позволяющие ActiveGate получать доступ к данным мониторинга WMI.

#### Разрешение на удалённое подключение на хосте

На отслеживаемом хосте должно быть установлено разрешение **Remote enable**.

1. В консоли Microsoft [Server Manager](https://docs.microsoft.com/en-us/windows-server/administration/server-manager/server-manager) откройте **Administrative Tools** > **Computer Management**.
2. Разверните **Services and Applications**, щёлкните правой кнопкой мыши **WMI Control** и выберите **Properties**.
3. Выберите вкладку **Security**, затем нажмите кнопку **Security**.
4. Добавьте пользователя, который будет использоваться для вызовов WMI, и выберите **Remote Enable** в столбце **Allow**.

Дополнительные сведения см. в документации Microsoft: [Allowing Users Access to a Specific WMI Namespace](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection#allowing-users-access-to-a-specific-wmi-namespace).

#### Настройка брандмауэра для доступа к удалённому WMI

Для настройки брандмауэра для доступа к удалённому WMI выполните следующие команды:

```
netsh advfirewall firewall set rule group="windows management instrumentation (wmi)" new enable=yes
```

и

```
netsh firewall set service RemoteAdmin enable
```

Дополнительные сведения см. в документации Microsoft: [Setting up a Remote WMI Connection](https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista).

#### Отключение удалённого UAC

Отключите удалённый UAC при использовании локальной учётной записи администратора (без Active Directory).

```
New-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LocalAccountTokenFilterPolicy -PropertyType DWord -Value 1 -Force
```

Дополнительные сведения см. в документации Microsoft: [Handling Remote Connections Under UAC](https://docs.microsoft.com/en-us/windows/win32/wmisdk/user-account-control-and-wmi#handling-remote-connections-under-uac).

#### Настройка локального пользователя

Для подключения к удалённому хосту WMI используйте стандартного пользователя или пользователя с правами администратора в зависимости от требуемых данных. Этот пользователь добавляется в [конфигурацию мониторинга](#monitoring-configuration). Рекомендуется создать выделенную локальную группу пользователей или учётную запись на целевом компьютере специально для удалённых подключений.

Для ограничения прав пользователя доступом только к удалённому подключению к WMI

1. В Windows выполните команду `DCOMCNFG`.
2. Откройте **Component Services** > **Computers**, щёлкните правой кнопкой мыши **My Computer** и выберите **Properties**.
3. Выберите вкладку **COM Security**.
4. В разделе **Launch and Activation Permissions** выберите **Edit Limits**.
5. В поле **Group or user names** выберите **ANONYMOUS LOGON**. В разделе **Permissions for ANONYMOUS LOGON** выберите **Remote Launch** и **Remote Activation** в столбце **Allow**.
6. Выберите **OK** для сохранения.

Дополнительные сведения см. в документации Microsoft:

* [Securing a Remote WMI Connection](https://docs.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection)
* [Limiting access to WMI namespaces](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-namespace-security-with-the-wmi-control)
* [Access to WMI Namespaces](https://docs.microsoft.com/en-us/windows/win32/wmisdk/access-to-wmi-namespaces)

#### Настройка фиксированного порта для WMI

1. В командной строке введите:
   `winmgmt -standalonehost`
2. Остановите службу WMI:
   `net stop winmgmt`
3. Перезапустите службу WMI в новом хосте службы:
   `net start winmgmt`
4. Задайте новый номер порта для службы WMI:
   `netsh firewall add portopening TCP 24158 WMIFixedPort`

Дополнительные сведения см. в документации Microsoft: [Setting Up a Fixed Port for WMI](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-up-a-fixed-port-for-wmi).