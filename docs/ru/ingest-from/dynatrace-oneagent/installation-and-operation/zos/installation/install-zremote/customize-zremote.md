---
title: Customize the zRemote module
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote
scraped: 2026-03-06T21:36:53.068278
---

# Настройка модуля zRemote

# Настройка модуля zRemote

* Последняя версия Dynatrace
* Чтение: 9 мин
* Обновлено 11.08.2022

Вы можете настроить модуль zRemote для включения дополнительных функций и оптимизации его производительности.

## Файлы пользовательской конфигурации

Следующие файлы конфигурации сохраняются при обновлении или удалении zRemote. Вы можете вносить изменения здесь.

Для применения новых настроек необходимо перезапустить службу zRemote.

### Пользовательская конфигурация модуля zRemote

Файл пользовательской конфигурации модуля zRemote (`zremoteagentuserconfig.conf`) позволяет переопределять конфигурацию по умолчанию, заданную в `ruxitagent.conf`.

Linux

Windows

`/var/lib/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`

`C:/ProgramData/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`

### Пользовательская конфигурация watchdog

Версия Dynatrace 1.277+ Файл пользовательской конфигурации watchdog (`watchdoguserconfig.conf`) позволяет переопределять конфигурацию по умолчанию, заданную в `oneagentzwatchdog.ini`.

Linux

Windows

`/var/lib/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`

`C:/ProgramData/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`

Доступные параметры конфигурации:

Расчёт эффективного лимита памяти

Эффективный лимит = процентный лимит x доступная физическая память системы + абсолютный лимит

Например:

0,2 x 5 ГиБ + 500 МиБ = 1,5 ГиБ эффективный лимит памяти

## Организация LPAR с помощью групп хостов

Группы хостов полезны, когда необходимо организовать несколько LPAR, подключающихся к одному модулю zRemote. LPAR можно назначить группе хостов, задав атрибут `[HostGroup]` в файле `zremoteagentuserconfig.conf`. LPAR может принадлежать только одной группе хостов.

Чтобы назначить LPAR группе хостов, укажите имя группы между парой атрибутов `[HostGroup]`. Пара атрибутов `[HostGroup]` может находиться в любом месте файла `zremoteagentuserconfig.conf`.

```
[HostGroup]



<LPAR_Name1>=<HostGroupName>



<LPAR_Name2>=<HostGroupName>



[HostGroup]
```

Имя LPAR — это 8-символьное имя логического раздела, определённое в параметре `LPARNAME()` в члене `IEASYMxx` в z/OS.

Имя LPAR также отображается в разделе `Properties and tags` на экране хоста.

К строке `<HostGroupName>` применяются следующие требования:

* Может содержать только буквенно-цифровые символы, дефисы (`-`), подчёркивания (`_`) и точки (`.`)
* Не должно начинаться с `dt.`
* Максимальная длина — 100 символов

Объединение трёх LPAR в одну группу хостов

В этом примере мы добавляем три LPAR — `LPARA`, `LPARB` и `LPARC` — в одну группу хостов `TEST_HOST`.

```
[HostGroup]



LPARA=TEST_HOST



LPARB=TEST_HOST



LPARC=TEST_HOST



[HostGroup]
```

Назначение трёх LPAR разным группам хостов

В этом примере мы назначаем каждый LPAR отдельной группе хостов.

```
[HostGroup]



LPARA=TEST_HOST



LPARB=PROD_HOST



LPARC=PERF_HOST



[HostGroup]
```

* В настройках хоста только меню **General**, **Monitoring** и **Detected processes** применимы для группы хостов z/OS.
* Храните настройки группы хостов только в файле `zremoteagentuserconfig.conf` и перенесите настройки группы хостов из файла `ruxitagent.conf`.
* Настройки группы хостов вступают в силу при запуске zRemote. Необходимо перезапустить модуль zRemote после определения группы хостов в файле `zremoteagentuserconfig.conf`.

## Получение полных SQL-выражений из баз данных Db2

Dynatrace может предоставлять информацию о SQL-выражениях на основе трассировки вызовов баз данных Db2 и DL/I. Эти SQL-выражения отображаются в Dynatrace, например, как:

* **FETCH (PROGNAME;165;3)**
* **CLOSE (PROGNAME;441;2)**

Строка представляет имя программы (имя DBRM), номер строки и номер секции.

Пример захваченных SQL-выражений

![zRemote SQL statement fetch off](https://dt-cdn.net/images/zremote-sql-fetch-off-1600-5beae13988.png)

Модуль zRemote версии 1.241+ Dynatrace может предоставлять более глубокую информацию о вызовах базы данных Db2, извлекая полные SQL-выражения из каталога Db2. С включённой функцией **получения SQL-выражений** SQL-выражения отображаются в Dynatrace, например, как:

* **FETCH (GETTAB INTO : H , : H , : H , : H , : H)**
* **CLOSE (GETTAB)**

Пример захваченных SQL-выражений с включённой функцией получения SQL-выражений

![zRemote SQL statement fetch on](https://dt-cdn.net/images/zremote-sql-fetch-on-1602-ff3d0f1c32.png)

### Включение получения SQL-выражений

Функция **получения SQL-выражений** отключена по умолчанию. Для её включения:

1. Установите и настройте программное обеспечение IBM Data Server Driver for ODBC and CLI на [Linux](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-linux-unix-operating-systems) или [Windows](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-windows-operating-systems). Дополнительная информация: [Информация о загрузке и установке драйвера IBM Db2 ODBC CLI](https://www.ibm.com/support/pages/db2-odbc-cli-driver-download-and-installation-information).

   На этапе установки запомните расположение библиотеки драйвера CLI:

   * `libdb2.so` для Linux
   * `db2app64.dll` для Windows

   Перед настройкой драйвера может потребоваться обратиться к администратору базы данных для получения информации о подключении к базе данных (например, учётные данные, расположение, IP-адрес и порт). На этапе настройки запомните псевдонимы Db2 (или DSN).

   Оба параметра потребуются на следующих шагах.

   * Модуль zRemote поддерживает только 64-битный драйвер CLI.
   * Мы настоятельно рекомендуем установить тайм-аут соединения для каждого псевдонима БД, например, ConnectTimeout=2
     для двух секунд в db2cli.ini на Linux.
   * Обязательно протестируйте конфигурацию драйвера CLI для обеспечения правильного соединения с Db2, например:

     ```
     \<cli-driver-path\>/bin/db2cli validate -connect -database \<db-location\>:\<ip\>:\<port\> -user \<id\> -passwd \<pw\>



     \<cli-driver-path\>/bin/db2cli validate -connect -dsn \<db-alias\>
     ```
   * Для настройки драйвера CLI необходимы учётные данные Db2 с правами доступа к соединениям Db2 (из распределённых с использованием DDF/DRDA) и правами на выборку из CATALOG, в частности из SYSPACKSTMT.
2. В файле `zremoteagentuserconfig.conf` модуля zRemote определите библиотеку драйвера CLI и группу псевдонимов Db2 (аналогично определению групп хостов), например:

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

   где `dbHost` — это SMF ID z/OS, а `dbName` — имя подсистемы Db2. Все значения чувствительны к регистру.
3. Необязательно: Определите `sqlStmtCacheFileName=/tmp/sqlStmtCacheFileName` (как пример) для кэширования полученных SQL-выражений в файл и использования его при перезапуске модуля zRemote, что сокращает взаимодействие с Db2. Обязательно используйте соответствующее полное имя файла.
4. Перезапустите модуль zRemote.

   * Модуль zRemote включит функцию **получения SQL-выражений** только если драйвер CLI может быть успешно загружен и определён хотя бы один псевдоним DB2.
   * Если впоследствии выяснится, что псевдоним Db2 недействителен, функция будет отключена.

## Включение безопасного соединения zLocal-zRemote

Модуль zRemote версии 1.267+

По умолчанию zLocal и zRemote используют проприетарный протокол связи через обычные сокеты. Вы можете настроить их для связи через TLS, настроив AT-TLS для zLocal и установив флаги SSL для zRemote, как показано ниже.

### Конфигурация AT-TLS для zLocal

В зависимости от ваших требований существуют различные способы настройки AT-TLS для zLocal. Подробнее см. [Защита данных Application Transparent Transport Layer Security](https://www.ibm.com/docs/en/zos/2.5.0?topic=applications-application-transparent-transport-layer-security-data-protection) в документации IBM. Вы можете использовать приведённый ниже пример конфигурации AT-TLS в качестве шаблона.

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

Убедитесь, что userId, используемый в задании zDC, совпадает с владельцем сертификата.
В противном случае соединение для рукопожатия TSL завершится ошибкой (с ошибкой SSL accept -1 и кодом 5).

### Настройки SSL/TLS для zRemote

Для включения SSL/TLS для zRemote:

1. Откройте файл `zremoteagentuserconfig.conf`.
2. Установите `sslEnabled` в значение `true`.
3. Укажите абсолютные пути к файлам PEM вашего закрытого ключа (`sslPrivateKey`) и сертификата (`sslCertificate`).
4. Необязательно: Определите конкретные наборы шифров TLS. Информацию о допустимых именах наборов шифров и их строковом формате см. в [документации OpenSSL](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html).

Шаблон конфигурации

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

Если определённый процесс регулярно проверяет доступность модуля zRemote, и эти проверки достигают порта прослушивания zRemote, модуль zRemote регистрирует недействительную попытку подключения. Эти недействительные попытки подключения увеличивают размер журнала zRemote со временем.

Чтобы игнорировать попытки подключения от определённых процессов, перечислите их IP-адреса (разделённые точкой с запятой) в файле `zremoteagentuserconfig.conf`, например:

```
ignoreHandshakeEndpoints=192.168.0.1;10.0.0.2
```

## Отказ от нового расчёта идентификатора процесса IMS MPR

Модуль zRemote версии 1.253+

Идентификаторы процессов IMS message processing region (MPR) могут измениться, что приведёт к появлению новых сущностей процессов и сервисов в Dynatrace. Чтобы предотвратить это изменение идентификатора процесса, мы ввели более стабильный расчёт идентификатора, в результате которого все сущности процессов и сервисов IMS MPR изменятся однократно, но затем останутся стабильными после обновления модуля zRemote до версии 1.253.

Чтобы отказаться от нового расчёта идентификатора процесса IMS MPR, установите флаг `useOldImsPgiCalc` в файле `zremoteagentuserconfig.conf` в значение `true`.

```
useOldImsPgiCalc=true
```