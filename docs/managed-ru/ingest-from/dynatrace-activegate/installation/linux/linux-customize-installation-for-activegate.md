---
title: Настройка установки ActiveGate на Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate
scraped: 2026-05-12T11:36:30.860044
---

# Настройка установки ActiveGate на Linux

# Настройка установки ActiveGate на Linux

* 6-min read
* Updated on Feb 11, 2026

Указывать параметры для команды установки не обязательно, если только не требуется настройка таких параметров, как расположение директорий, конфигурация прокси, SSL-сертификаты и т.д. Для настройки таких параметров можно использовать параметры командной строки и переменные окружения.

## Синтаксис команды установки

```
Dynatrace-ActiveGate-Linux-x86-<version>.sh [<parameter1>=<value1>]  [<parameter2>=<value2>] ...
```

Пробелы между именем параметра и его значением (вокруг знака `=`) в синтаксисе команды не допускаются.

## Конфигурация прокси

Конфигурация прокси задаётся в следующем формате. Это настроит прокси для ActiveGate для всех исходящих соединений (в разделе конфигурации `http.client`):

```
PROXY=<proxy scheme><user>:<password>@<server>:<port>
```

Где:

* Все компоненты необязательны, кроме `<server>`.
* Если ни `<user>`, ни `<password>` не указаны, символ `@` следует опустить.
* `<password>` можно указать только при наличии имени пользователя.
* Символ `:` после `<user>` можно указать даже при пустом поле пароля.
* `<proxy scheme>` необязателен и может быть `http://` или `https://`.
* `<user>` необязателен.
* `<server>` может быть IP-адресом или DNS-именем, но не путём. Например, если указано `1.2.3.4/textaferslash`, будет извлечена только IP-часть (`1.2.3.4`). Косая черта и следующий за ней текст будут проигнорированы.
* `<port>` необязателен.

## Конфигурация обратного прокси или балансировщика нагрузки для ActiveGate

На пути от ActiveGate к кластеру Dynatrace можно установить обратный прокси или балансировщик нагрузки. Это позволяет ActiveGate подключаться к любому доступному узлу кластера, распределяя нагрузку.
Для этого необходимо:

* Указать адрес обратного прокси/балансировщика нагрузки.
* Убедиться, что ActiveGate будет игнорировать информацию об адресе цели, поступающую от кластера Dynatrace, и подключаться только к указанному адресу.

Такие параметры конфигурации можно указать во время установки ActiveGate, задав следующие параметры командной строки для установщика:

```
--ignore-cluster-runtime-info SERVER=<address of reverse proxy>
```

Также можно настроить ActiveGate после установки, внеся изменения в [конфигурацию ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Узнайте, как настроить свойства ActiveGate для настройки обратного прокси или балансировщика нагрузки.").

## Конфигурация обратного прокси или балансировщика нагрузки для OneAgent

На пути от OneAgent к ActiveGate можно установить обратный прокси или балансировщик нагрузки. Для этого необходимо настроить URL балансировщика нагрузки на ActiveGate, чтобы OneAgent мог использовать эту конечную точку для подключения к ActiveGate.

Для указания адреса добавьте следующий параметр командной строки:

```
DNSENTRYPOINT=https://<DOMAIN>:<PORT>
```

где:

* `<DOMAIN>` — домен балансировщика нагрузки
* `<PORT>` — необязателен, по умолчанию `443`

Также можно настроить конечные точки после установки, внеся изменения в [конфигурацию ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent "Настройте свойства ActiveGate для настройки обратного прокси или балансировщика нагрузки для OneAgent.").

## Пользователь для службы ActiveGate

Для указания пользователя, от имени которого запускается служба ActiveGate, укажите следующий параметр командной строки:

```
USER=<user>
```

Установщик создаёт пользователя, если он ещё не существует в системе; пользователю не требуются привилегии root. Если параметр не указан, установщик создаёт пользователя `dtuserag` для запуска службы ActiveGate. Вместо группы по умолчанию `dynatrace` будет указана основная группа существующего пользователя. Однако можно использовать `USER=root` для принудительного запуска службы ActiveGate от имени root.

Параметр `USER=root` не поддерживается при установке [Synthetic-enabled ActiveGate](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.").

## Ограничения для расположения директорий и точек монтирования

Полный список расположений директорий ActiveGate см. [Файлы и директории ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.").

`<customizable directory>/gateway` (то есть `INSTALL/gateway`, `CONFIG/gateway`, `LOG/gateway`, `TEMP/gateway`, `PACKAGES_DIR/gateway`) не может быть родительской директорией для другой настраиваемой директории (`INSTALL`, `CONFIG`, `TEMP`, `LOG` или `PACKAGES_DIR`).

Например, **не** указывайте:

```
INSTALL=/dynatrace



LOG=/dynatrace/gateway/logs



CONFIG=/dynatrace/gateway/config



TEMP=/dynatrace/gateway/tmp
```

Аналогично, **не** указывайте:

```
CONFIG=/var/lib/dynatrace



PACKAGES_DIR=/var/lib/dynatrace/gateway/packages
```

Однако общий родительский каталог допустим, например:

```
INSTALL=/example/apps



CONFIG=/example/configs



LOG=/example/logs



TEMP=/example/tmp
```

Также см. раздел [Временная директория](#temporary).

### Выделенные директории

Каждая настраиваемая директория должна быть предназначена исключительно для ActiveGate.

Например, **не** указывайте:

```
INSTALL=/opt



CONFIG=/var/lib



LOG=/var/log



TEMP=/var/tmp
```

Вместо этого каждый путь должен включать поддиректорию, выделенную для ActiveGate, например:

```
INSTALL=/opt/activegate



CONFIG=/var/lib/activegate



LOG=/var/log/activegate



TEMP=/var/tmp/activegate
```

### Пробелы в пути директории

ActiveGate не поддерживает пробелы в пути директории.

Например, **не** указывайте:

```
CONFIG=/var/lib/dir\ with\ space
```

Аналогично, **не** указывайте:

```
CONFIG="/var/lib/dir with space"
```

### Точки монтирования

Во время установки ActiveGate необходимо создавать, удалять и изменять поддиректории в своих корневых директориях `INSTALL`, `CONFIG`, `LOG` и `TEMP`. В этих директориях не должно быть точек монтирования файловой системы.

Например, если указан следующий параметр `INSTALL`:

```
INSTALL=/opt/MyActiveGate
```

Установщик ActiveGate создаст поддиректорию `gateway` по указанному пути установки:
`/opt/MyActiveGate/gateway`

В результате:

* Точка монтирования `/opt/MyActiveGate` является **ДОПУСТИМОЙ**.
* Точка монтирования `/opt/MyActiveGate/gateway` является **НЕДОПУСТИМОЙ**.

## Директория установки

```
INSTALL=<directory>
```

Хранит файлы установки в указанной директории. Значение по умолчанию (если не указано): `/opt/dynatrace`. Этот параметр не разрешён при обновлении.

Директория установки

ActiveGate и OneAgent, установленные на одном хосте, **не должны** использовать одну и ту же директорию установки.

## Директория для хранения загружаемых пакетов

```
PACKAGES_DIR=<directory>
```

Хранит установочные файлы дополнительных возможностей в указанной директории. Значение по умолчанию (если не указано): `/var/lib/dynatrace/packages`. Не разрешён при обновлении.

## Директория журналов

```
LOG=<directory>
```

Хранит файлы журналов в указанной директории. Значение по умолчанию (если не указано): `/var/log/dynatrace`. Не разрешён при обновлении.

## Директория конфигурации

```
CONFIG=<directory>
```

Хранит файлы конфигурации в указанной директории. Значение по умолчанию (если не указано): `/var/lib/dynatrace`. Не разрешён при обновлении.

## Временная директория

```
TEMP=<directory>
```

Указывает временную директорию, используемую ActiveGate. Значение по умолчанию (если не указано): `/var/tmp/dynatrace`. Не разрешён при обновлении.

При настройке временной директории убедитесь, что она исключена из правил автоматической очистки. В противном случае это может повлиять на надёжную работу Synthetic-enabled ActiveGate.

### Использование `/temp` или `/tmp`

Из-за возможной автоматической очистки не рекомендуется использовать директории `/temp` или `/tmp` или их поддиректории для установки ActiveGate или хранения данных, генерируемых или используемых ActiveGate.

Обратите внимание, что для Synthetic-enabled ActiveGate, установленного на Ubuntu 20.04 LTS и 22.04 LTS ранее версии 1.331, доступ на запись в директорию `/tmp` необходим для установки snap-пакетов Chromium.

## CA-сертификат

Для добавления пользовательского CA-сертификата в хранилище сертификатов, поставляемое с ActiveGate, можно использовать параметры командной строки во время установки.
Таким образом можно указать прокси CA-сертификат (сертификат, используемый при подключении ActiveGate к кластеру Dynatrace). Это позволяет установить соединение с кластером Dynatrace во время установки, что позволяет установщику ActiveGate загрузить и установить необходимые дополнительные возможности.

Пароль сертификата указывается как [файл, из которого считывается пароль](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Узнайте, как настроить пользовательские доверенные корневые сертификаты на ActiveGate.").

Абсолютный путь к расположению пользовательского доверенного корневого сертификата(ов) для добавления:

```
--ca-certificate-file=<path>
```

Абсолютный путь к расположению файла, содержащего пароль сертификата:

```
--ca-certificate-password-file=<path>
```

Пример команды:

```
[root@host]# ./Dynatrace-ActiveGate-Linux-1.217.sh --ca-certificate-file=/home/fred/myCert.jks  --ca-certificate-password-file=/home/fred/myPwd.txt
```

### Ограничения для указания SSL-сертификата

Непосредственное указание SSL-сертификата для ActiveGate не применимо к Cluster ActiveGate.
Не пытайтесь настраивать SSL-сертификаты непосредственно на Cluster ActiveGate. Если вы это сделаете, сертификат будет перезаписан автоматическим управлением Dynatrace.
Для Cluster ActiveGate необходимо загружать сертификаты через [Cluster Management Console](/managed/managed-cluster/installation/ssl-certificate-cluster-activegate "Настройте пользовательский SSL-сертификат на Cluster ActiveGate.") или [Cluster REST API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status "Узнайте, как использовать Dynatrace API для хранения SSL-сертификата кластера.").

## Пользовательский SSL-сертификат

Во время установки можно указать сертификат аутентификации, который ActiveGate предоставляет подключающимся клиентам, таким как OneAgent или браузерные клиенты. Если такие сертификаты необходимы, это снижает усилия на постустановочную настройку. Подробнее см. [Пользовательский SSL-сертификат для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на ActiveGate.").

Пароль сертификата указывается как [файл, из которого считывается пароль](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate#known-limitations "Узнайте, как настроить SSL-сертификат на ActiveGate.").

Абсолютный путь к расположению сертификата аутентификации, который ActiveGate предоставляет подключающимся клиентам (OneAgent или браузерным клиентам, например RUM JavaScript):

```
--certificate-file=<path>
```

Абсолютный путь к расположению файла, содержащего пароль сертификата аутентификации:

```
--certificate-password-file=<path>
```

Пример команды:

```
[root@host]# ./Dynatrace-ActiveGate-Linux-x86-<version>.sh --certificate-file=/home/fred/myCert.p12  --certificate-password-file=/home/fred/myPwd.txt
```

## Сетевая зона

```
--set-network-zone=<name>
```

Определяет [сетевую зону](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace."), к которой принадлежит ActiveGate. ActiveGate может принадлежать только к одной сетевой зоне. Имя сетевой зоны — строка из буквенно-цифровых символов, дефисов (`-`), подчёркиваний (`_`) и точек (`.`). Точки используются как разделители, поэтому первым символом имени сетевой зоны не должна быть точка. Длина строки ограничена 256 символами.

Для изменения или удаления назначения сетевой зоны после установки используйте [Удалённое управление конфигурацией](/managed/ingest-from/bulk-configuration#configure-activegates "Выполняйте конфигурацию OneAgent и ActiveGate на хостах со страницы Deployment status или централизованно через Dynatrace API.") (выберите действие **modify network zone**).

Также можно указать сетевую зону в файле [`custom.properties`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настроить.").

## Группа

```
--set-group=<name>
```

Определяет группу ActiveGate, к которой принадлежит ActiveGate. ActiveGate может принадлежать только к одной группе. Имя группы ActiveGate — строка из буквенно-цифровых символов, дефисов (`-`), подчёркиваний (`_`) и точек (`.`). Точки используются как разделители, поэтому первым символом имени группы не должна быть точка. Длина строки ограничена 256 символами. Группы ActiveGate позволяют выполнять массовые действия на ActiveGate, например управлять [расширениями](/managed/ingest-from/extensions/develop-your-extensions "Разработайте собственные расширения Dynatrace."), запущенными на ActiveGate. Для назначения ActiveGate в группу см. [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Понять основные концепции групп ActiveGate.").

Для изменения или удаления назначения группы после установки используйте [Удалённое управление конфигурацией](/managed/ingest-from/bulk-configuration#configure-activegates "Выполняйте конфигурацию OneAgent и ActiveGate на хостах со страницы Deployment status или централизованно через Dynatrace API.") (выберите действие **modify ActiveGate group**).

Также можно указать группу ActiveGate в файле [`custom.properties`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настроить.").

## Таймаут подключения

```
DYNATRACE_ACTIVEGATE_SERVER_CONNECTION_TIMEOUT=<seconds>
```

Определяет максимальное количество секунд (по умолчанию: `120`, макс.: `240`), в течение которых установщик ожидает подключения к кластеру. В развёртываниях Linux этот параметр должен использоваться как переменная окружения.

Таймаут подключения, заданный переменной окружения `DYNATRACE_ACTIVEGATE_SERVER_CONNECTION_TIMEOUT=<seconds>`, используется на двух этапах установки:

* При загрузке дополнительных (необязательных) возможностей.
* При ожидании подключения к кластеру в конце установки ActiveGate: это подключение затем используется ActiveGate в штатной работе.

Если таймаут истекает во время загрузки возможностей, дополнительные возможности не будут загружены и установка завершится с ошибкой. Однако если таймаут истекает в конце процесса установки (то есть при запуске штатной работы ActiveGate), все компоненты ActiveGate уже будут установлены, и ActiveGate продолжит попытки подключения к кластеру. ActiveGate будет повторять попытки даже после завершения процесса установки. При успешном подключении ActiveGate начнёт работать в штатном режиме.

Для проверки успешности установки и подключения войдите в Dynatrace, в разделе **Settings** выберите **Deployment Status**, затем перейдите на вкладку **ActiveGates**.

Например:

```
[root@host]# export DYNATRACE_ACTIVEGATE_SERVER_CONNECTION_TIMEOUT=240



[root@host]# Dynatrace-ActiveGate-Linux-x86-1.0.0.sh <... other parameters>
```

или в одной строке:

```
[root@host]# export DYNATRACE_ACTIVEGATE_SERVER_CONNECTION_TIMEOUT=240 ; Dynatrace-ActiveGate-Linux-x86-1.0.0.sh <... other parameters>
```

## Соответствие требованиям FIPS

ActiveGate версии 1.315+

Для соответствия требованиям Federal Information Processing Standard (FIPS) можно включить режим, совместимый с FIPS, во время установки ActiveGate.

Режим совместимости с FIPS нельзя изменить после установки. Для изменения режима необходимо удалить ActiveGate и переустановить его с нужными настройками.

Пример команды:

```
[root@host]# ./Dynatrace-ActiveGate-Linux-x86-<version>.sh --fips-mode
```

где `--fips-mode` включает установку ActiveGate в режиме совместимости с FIPS.

Информацию о предварительных условиях, ограничениях и шагах проверки см. [ActiveGate, совместимый с FIPS, на основе хоста](/managed/ingest-from/dynatrace-activegate/activegate-fips-compliance#host-based-activegate-deployment "Узнайте о совместимости ActiveGate с FIPS.").