---
title: Настройка модуля zRemote
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote
scraped: 2026-05-12T11:36:39.696814
---

# Настройка модуля zRemote

# Настройка модуля zRemote

* Чтение: 9 мин
* Обновлено 11 августа 2022 г.

Модуль zRemote можно настроить для включения необязательных функций и оптимизации его производительности.

## Файлы пользовательской конфигурации

Перечисленные ниже файлы конфигурации сохраняются при обновлении или удалении zRemote. Здесь можно вносить изменения.

Для применения новых настроек необходимо перезапустить службу zRemote.

### Пользовательская конфигурация модуля zRemote

Файл пользовательской конфигурации модуля zRemote (`zremoteagentuserconfig.conf`) позволяет переопределить настройки по умолчанию, заданные в `ruxitagent.conf`.

Linux

Windows

`/var/lib/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`

`C:/ProgramData/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`

### Пользовательская конфигурация watchdog

Dynatrace версии 1.277+ Файл пользовательской конфигурации watchdog (`watchdoguserconfig.conf`) позволяет переопределить настройки по умолчанию, заданные в `oneagentzwatchdog.ini`.

Linux

Windows

`/var/lib/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`

`C:/ProgramData/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`

Доступные параметры конфигурации:

| Параметр | Единица | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| -healthcheck.heartbeat.timeout | Секунды | 900 | Таймаут соединения между службой zRemote и вашим окружением Dynatrace |
| -healthcheck.memory.limit\_absolute | МиБ | 500 | Абсолютное значение для расчёта лимита памяти дочернего процесса |
| -healthcheck.memory.limit\_percentage | % | 20 | Процентное значение для расчёта лимита памяти дочернего процесса |

Расчёт эффективного лимита памяти

Эффективный лимит = процентный лимит × доступная физическая память системы + абсолютный лимит

Например:

0.2 × 5 ГиБ + 500 МиБ = 1,5 ГиБ эффективный лимит памяти

## Организация LPAR с помощью Host groups

**Host groups** полезны, когда нужно организовать несколько LPAR, подключённых к одному модулю zRemote. Чтобы назначить LPAR в Host group, задайте атрибут `[HostGroup]` в файле `zremoteagentuserconfig.conf`. LPAR может принадлежать только одной Host group.

Чтобы назначить LPAR в Host group, укажите имя группы между парой атрибутов `[HostGroup]`. Пара атрибутов `[HostGroup]` может располагаться в любом месте файла `zremoteagentuserconfig.conf`.

```
[HostGroup]



<LPAR_Name1>=<HostGroupName>



<LPAR_Name2>=<HostGroupName>



[HostGroup]
```

Имя LPAR -- это 8-символьное имя логического раздела, заданное в параметре `LPARNAME()` в элементе `IEASYMxx` в z/OS.

Имя LPAR также отображается в разделе `Properties and tags` на экране хоста.

К строке `<HostGroupName>` применяются следующие требования:

* Допустимы только буквенно-цифровые символы, дефисы (`-`), символы подчёркивания (`_`) и точки (`.`)
* Строка не должна начинаться с `dt.`
* Максимальная длина: 100 символов

Объединение трёх LPAR в одну Host group

В данном примере три LPAR (`LPARA`, `LPARB` и `LPARC`) добавляются в одну Host group `TEST_HOST`.

```
[HostGroup]



LPARA=TEST_HOST



LPARB=TEST_HOST



LPARC=TEST_HOST



[HostGroup]
```

Назначение трёх LPAR в разные Host groups

В данном примере каждая LPAR назначается в отдельную Host group.

```
[HostGroup]



LPARA=TEST_HOST



LPARB=PROD_HOST



LPARC=PERF_HOST



[HostGroup]
```

* В настройках хоста для Host group z/OS применяются только меню **General**, **Monitoring** и **Detected processes**.
* Храните настройки Host group только в файле `zremoteagentuserconfig.conf` и перенесите настройки Host group из файла `ruxitagent.conf`.
* Настройки Host group вступают в силу при запуске zRemote. После определения Host group в файле `zremoteagentuserconfig.conf` необходимо перезапустить модуль zRemote.

## Получение полных SQL-запросов из баз данных Db2

Dynatrace предоставляет аналитику по SQL-запросам на основе трассировки обращений к базам данных Db2 и DL/I. Эти SQL-запросы отображаются в Dynatrace, например, в следующем виде:

* **FETCH (PROGNAME;165;3)**
* **CLOSE (PROGNAME;441;2)**

Строка содержит имя программы (имя DBRM), номер строки и номер секции.

Пример перехваченных SQL-запросов

![zRemote SQL statement fetch off](https://dt-cdn.net/images/zremote-sql-fetch-off-1600-5beae13988.png)

zRemote SQL statement fetch off

Версия модуля zRemote 1.241+ Dynatrace предоставляет более глубокую аналитику по обращениям к базам данных Db2, получая полные SQL-запросы из каталога Db2. При включённой функции **SQL statement fetch** SQL-запросы отображаются в Dynatrace, например, в следующем виде:

* **FETCH (GETTAB INTO : H , : H , : H , : H , : H)**
* **CLOSE (GETTAB)**

Пример перехваченных SQL-запросов с включённой функцией SQL statement fetch

![zRemote SQL statement fetch on](https://dt-cdn.net/images/zremote-sql-fetch-on-1602-ff3d0f1c32.png)

zRemote SQL statement fetch on

### Включение функции SQL statement fetch

Функция **SQL statement fetch** отключена по умолчанию. Чтобы включить её:

1. Установите и настройте IBM Data Server Driver for ODBC and CLI на [Linux](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-linux-unix-operating-systems) или [Windows](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-windows-operating-systems). Дополнительно: [Информация по скачиванию и установке IBM Db2 ODBC CLI driver](https://www.ibm.com/support/pages/db2-odbc-cli-driver-download-and-installation-information).

   На шаге установки запомните расположение библиотеки CLI driver:

   * `libdb2.so` для Linux
   * `db2app64.dll` для Windows

   Перед настройкой driver может потребоваться обратиться к DBA для получения сведений о подключении к базе данных (учётных данных, местоположения, IP-адреса и порта). На шаге настройки запомните псевдонимы Db2 (или DSN).

   Оба значения потребуются в следующих шагах.

   * Модуль zRemote поддерживает только 64-битный CLI driver.
   * Настоятельно рекомендуем задавать таймаут соединения для каждого псевдонима БД, например ConnectTimeout=2
     для двух секунд в db2cli.ini на Linux
   * Обязательно протестируйте конфигурацию CLI driver для проверки подключения к Db2, например:

     ```
     \<cli-driver-path\>/bin/db2cli validate -connect -database \<db-location\>:\<ip\>:\<port\> -user \<id\> -passwd \<pw\>



     \<cli-driver-path\>/bin/db2cli validate -connect -dsn \<db-alias\>
     ```
   * Для настройки CLI driver необходимы учётные данные Db2 с доступом к соединениям Db2 (из распределённой среды через DDF/DRDA) и правами на SELECT по CATALOG, в частности по SYSPACKSTMT.
2. В файле `zremoteagentuserconfig.conf` модуля zRemote задайте библиотеку CLI driver и группу псевдонимов Db2 (аналогично определению Host groups), например:

   ```
   # Linux



   cli_driver_lib=/opt/IBM/CLIDRIVER/lib/libdb2.so



   # ... or Windows



   cli_driver_lib=C:/IBM/CLIDRIVER/bin/db2app64.dll



   [DbAlias]



   dbHost1.dbName1=alias1



   dbHost2.dbName2=alias2



   dbHostN.dbNameN=aliasN



   [DbAlias]



   # Beginning with zRemote 1.279 it is possible to set the new flag sqlStmtExtended, if



   # true the full (fetched) SQL statement is appended with its old (unfetched) format,



   # for example, from an example above "FETCH (GETTAB INTO : H , : H , : H , : H , : H)"



   # would be shown as "FETCH (GETTAB INTO : H , : H , : H , : H , : H) (PROGNAME;165;3)".



   # The default is false. Note: if enabled this setting would affect the aggregation count.



   sqlStmtExtended=false
   ```

   где `dbHost` -- это SMF ID системы z/OS, а `dbName` -- имя подсистемы Db2. Все значения чувствительны к регистру.
3. Необязательно Задайте, например, `sqlStmtCacheFileName=/tmp/sqlStmtCacheFileName`, чтобы кэшировать полученные SQL-запросы в файл и использовать этот кэш при перезапуске модуля zRemote, сокращая тем самым число обращений к Db2. Обязательно используйте полное квалифицированное имя файла.
4. Перезапустите модуль zRemote.

   * Модуль zRemote включит функцию **SQL statement fetch** только в том случае, если CLI driver успешно загружен и определён хотя бы один псевдоним DB2.
   * Если псевдоним Db2 впоследствии окажется недействительным, функция будет отключена.

## Включение защищённого соединения zLocal-zRemote

Версия модуля zRemote 1.267+

По умолчанию zLocal и zRemote используют собственный протокол обмена данными через обычные сокеты. Их можно настроить на обмен данными через TLS: для этого задайте AT-TLS для zLocal и установите флаги SSL для zRemote, как показано ниже.

### Конфигурация AT-TLS для zLocal

В зависимости от требований существуют различные способы настройки AT-TLS для zLocal. Подробнее см. раздел [Application Transparent Transport Layer Security data protection](https://www.ibm.com/docs/en/zos/2.5.0?topic=applications-application-transparent-transport-layer-security-data-protection) в документации IBM. Приведённый ниже пример конфигурации AT-TLS можно использовать как шаблон.

Пример конфигурации AT-TLS

```
TTLSRule                       <client-rule>



{



RemoteAddr                 <ALL | specific-ip-addr>



RemotePortRange            <zdclistenerport>



Direction                  Outbound



TTLSGroupActionRef         <group-action>



TTLSEnvironmentActionRef   <environment-action>



TTLSConnectionActionRef    <connection-action>



}



TTLSGroupAction                <group-action>



{



TTLSEnabled                On



Trace                       <trace-level>



}



TTLSEnvironmentAction          <environment-action>



{



HandshakeRole              Client



TTLSKeyringParmsRef        <keyring-parms>



TTLSCipherParmsRef         <cipher-parms>



}



TTLSKeyringParms               <keyring-parms>



{



#   A certificate matches that of the zRemote's certificate



#   must be loaded into RACF and connected to the Keyring here.



Keyring                    <pub-key-or-certificate>



}



TTLSCipherParms                <cipher-parms>



{



...



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384



...



}



TTLSConnectionAction           <connection-action>



{



TTLSConnectionAdvancedParmsRef  <connection-advanced-parms>



}



TTLSConnectionAdvancedParms    <connection-advanced-parms>



{



SSLv2                      Off



SSLv3                      Off



TLSv1                      Off



TLSv1.1                    Off



TLSv1.2                    On



TLSv1.3                    On



}
```

Убедитесь, что userId, используемый в задаче zDC, совпадает с владельцем сертификата.
В противном случае установление TLS-соединения завершится ошибкой (SSL accept error -1, код 5).

### Настройки SSL/TLS для zRemote

Чтобы включить SSL/TLS для zRemote:

1. Откройте файл `zremoteagentuserconfig.conf`.
2. Установите `sslEnabled` в значение `true`.
3. Укажите абсолютные пути к файлам PEM вашего закрытого ключа (`sslPrivateKey`) и сертификата (`sslCertificate`).
4. Необязательно Определите конкретные наборы шифров TLS. Сведения о допустимых именах наборов шифров и их строковом формате см. в [документации OpenSSL](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html).

Показать шаблон конфигурации

```
# Must be true to enable secure connection; all other SSL settings are ignored if false



sslEnabled=true



# Absolute paths to your private key (with the pass-phrase stripped) and certificate PEM files.



# Beginning with zRemote module version 1.301.0, multiple private-key/certificate pairs delimited



# by a semicolon can be specified. For example:



# sslPrivateKey=<private-key-1.pem; private-key-2.pem; ...; private-key-n.pem>



# sslCertificate=<certificate-1.pem; certificate-2.pem; ...; certificate-n.pem>



sslPrivateKey=<private-key.pem>



sslCertificate=<certificate.pem>



# Optional: TLS cipher suites allowed according to OpenSSL



# Example: sslCiphers=ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384



sslCiphers=<cipher-suites>
```

## Игнорирование недействительных попыток подключения

Если определённый процесс регулярно отправляет ping-запросы модулю zRemote для проверки его доступности и эти запросы достигают порта прослушивания zRemote, модуль zRemote фиксирует недействительную попытку подключения. Со временем такие попытки увеличивают размер лога zRemote.

Чтобы игнорировать попытки подключения от определённых процессов, перечислите их IP-адреса (через точку с запятой) в файле `zremoteagentuserconfig.conf`, например:

```
ignoreHandshakeEndpoints=192.168.0.1;10.0.0.2
```

## Отказ от нового расчёта идентификаторов процессов IMS MPR

Версия модуля zRemote 1.253+

Идентификаторы процессов региона обработки сообщений IMS (MPR) могут изменяться, что приводит к появлению новых сущностей процессов и служб в Dynatrace. Чтобы исключить такое изменение идентификаторов, введён более стабильный алгоритм расчёта: все сущности процессов и служб IMS MPR изменятся один раз, после чего останутся стабильными после обновления модуля zRemote до версии 1.253.

Чтобы отказаться от нового алгоритма расчёта идентификаторов процессов IMS MPR, задайте флагу `useOldImsPgiCalc` значение `true` в файле `zremoteagentuserconfig.conf`.

```
useOldImsPgiCalc=true
```