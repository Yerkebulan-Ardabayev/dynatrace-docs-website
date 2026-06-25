---
title: Загрузка наборов данных продукта z/OS
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets
scraped: 2026-05-12T12:04:49.492342
---

# Загрузка наборов данных продукта z/OS

# Загрузка наборов данных продукта z/OS

* Чтение: 5 мин
* Обновлено 3 ноября 2023 г.

PAX-файл, содержащий модули CICS, IMS, z/OS Java и zDC, можно загрузить двумя способами:

* Dynatrace версии 1.272+: загрузка через [Deployment API](#using-deploymentapi).
* Dynatrace версии 1.276+: загрузка через [веб-интерфейс](#using-webui).

Начиная с версии OneAgent 1.275, PAX-файл больше не публикуется на FTP-сервере.

## Загрузка PAX-файла

Можно загрузить последнюю или конкретную версию PAX-файла через веб-интерфейс или [Deployment API](/managed/dynatrace-api/environment-api/deployment/oneagent "Загрузка установщиков OneAgent через Dynatrace API.") OneAgent.

Версия PAX-файла должна быть меньше или равна версии модуля zRemote.

### Загрузка последней версии через веб-интерфейс

1. Перейдите в **Deploy Dynatrace** и выберите **Start installation**.
2. Выберите **z/OS** и **Download z/OS product datasets** для загрузки последней версии PAX-файла.

Имя файла `dynatrace-zos-1.nnn.m.pax` содержит номер основного выпуска `nnn` и номер дополнительного выпуска `m`.

### Загрузка конкретной версии через веб-интерфейс

Конкретную версию PAX-файла можно загрузить через веб-интерфейс следующим образом:

1. Перейдите в **Settings** > **Monitoring** > **Monitoring overview**.
2. Выберите **Download Dynatrace OneAgent or ActiveGate installer** и укажите нужную версию:

   1. Installer: `OneAgent - z/OS`
   2. Build: выберите нужный основной выпуск
   3. Revision: выберите нужный дополнительный выпуск

   ![zos monitoring overview](https://dt-cdn.net/images/zos-monitoring-overview-1289-aa537f3578.png)

   zos monitoring overview
3. Нажмите **Continue** и **Download z/OS product datasets** для загрузки выбранной версии PAX-файла.

   Имя файла `dynatrace-zos-1.nnn.m.pax` содержит номер основного выпуска `nnn` и номер дополнительного выпуска `m`.

### Загрузка последней версии через Deployment API

Последнюю версию PAX-файла можно загрузить через Deployment API следующим образом:

1. Создайте [токен доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для работы с Dynatrace API.") с областью видимости **PaaS integration - Installer download** (`InstallerDownload`).
2. Загрузите последний PAX-файл через [Deployment API - Download latest OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Загрузка последней версии установщика OneAgent через Dynatrace API."):

   | Метод HTTP | Окружение Dynatrace | Эндпоинт |
   | --- | --- | --- |
   | GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/latest` |
   | GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/zos/mainframe/latest` |

   Ниже приведён пример команды `curl` для окружения SaaS, загружающей последнюю версию PAX-файла через Deployment API:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/latest" -H "accept: */*" -H "Authorization: Api-Token <accessToken>" --output dynatrace-zos.pax
   ```

   Замените `<environment>` на идентификатор вашего окружения Dynatrace, а `<accessToken>` на сгенерированный токен доступа.

### Загрузка конкретной версии через Deployment API

Конкретную версию PAX-файла можно загрузить через Deployment API следующим образом:

1. Создайте [токен доступа](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для работы с Dynatrace API.") с областью видимости **PaaS integration - Installer download** (`InstallerDownload`).
2. Получите список всех доступных версий PAX-файла через [Deployment API - List available versions of OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "Получение списка доступных версий OneAgent через Dynatrace API.").

   | Метод HTTP | Окружение Dynatrace | Эндпоинт |
   | --- | --- | --- |
   | GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/versions/zos/mainframe` |
   | GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/versions/zos/mainframe` |

   Ниже приведён пример команды `curl` для окружения SaaS, получающей список всех доступных версий PAX-файла через Deployment API:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/versions/zos/mainframe" -H "accept: */*" -H "Authorization: Api-Token <accessToken>"
   ```

   Замените `<environment>` на идентификатор вашего окружения Dynatrace, а `<accessToken>` на сгенерированный токен доступа.
3. Загрузите конкретную версию PAX-файла через [Deployment API - Download OneAgent of specific version](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-version "Загрузка установщика OneAgent конкретной версии через Dynatrace API."):

   | Метод HTTP | Окружение Dynatrace | Эндпоинт |
   | --- | --- | --- |
   | GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/version/{version}` |
   | GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/zos/mainframe/version/{version}` |

   Ниже приведён пример команды `curl` для окружения SaaS, загружающей конкретную версию PAX-файла через Deployment API:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/version/<version>" -H "accept: */*" -H "Authorization: Api-Token <accessToken>" --output dynatrace-zos.pax
   ```

   Замените `<environment>` на идентификатор вашего окружения Dynatrace, `<version>` на выбранную версию PAX-файла, а `<accessToken>` на сгенерированный токен доступа.

## Извлечение наборов данных продукта

Наборы данных продукта можно извлечь из PAX-файла следующим образом:

1. Передайте PAX-файл в каталог z/OS USS в двоичном режиме.
2. Переименуйте PAX-файл из `dynatrace-zos-1.nnn.m.pax` в `dynatrace-zos.pax`.
3. Используйте задание `EXTRACT`, приведённое ниже, для извлечения наборов данных продукта из файлов установки. Перед запуском задания внесите следующие изменения:

   1. Определите нужный высокоуровневый квалификатор для имён наборов данных установки и задайте переменную `HLQ` соответствующим образом.
   2. Задайте переменной `MYUSS` путь к каталогу z/OS USS, в который помещён файл `dynatrace-zos.pax`. Если путь к каталогу превышает 42 символа, это может привести к ошибке в шаге `STEP3` задания. В таком случае нужно изменить JCL для использования символа продолжения.
   3. Измените серийный номер тома `VOLSER` в соответствии со стандартами вашего предприятия.

   Задание EXTRACT

   ```
   //EXTRACT JOB ('ACCTINFO'),'User name or comment',NOTIFY=&SYSUID,



   //             MSGLEVEL=(1,1),CLASS=A,MSGCLASS=X,REGION=0M,



   //             COND=(0,NE)



   //*



   //* !!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



   //*



   //* When upgrading the zDC to version 1.213+ while



   //* the CICS code module is enabled, it is important to follow



   //* the below steps in the given sequence.



   //*



   //* 1. Stop the zDC



   //* 2. Wait for 15 minutes for the CICS code module to



   //*    reset/cleanup the control blocks



   //* 3. Upgrade the zDC to newer version



   //* 4. Start the zDC



   //*



   //* !!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



   //*



   //* This job extracts the product installation datasets from



   //* the installation files at <MYUSS>/GIMZIP to



   //* <hlq>.<rel>.SZDT* libraries.



   //*



   //* Change the JOB card and the SET statements below to meet



   //* site standards.



   //*



   //* Verify if the SMPCPATH and SMPJHOME DD below points to the



   //* correct PATH to meet site standards.



   //*



   //* WARNING!



   //* This JCL must be in mixed case and sequence numbers are not allowed



   //*



   // EXPORT SYMLIST=*



   // SET HLQ='DT'             <== HLQ of the target PDS datasets



   // SET REL='R12770'         <== Release number



   // SET VOLSER='NSM001'      <== Volume of the target PDS datasets



   // SET MYUSS='/u/dt'        <== USS work directory



   //*



   //*



   //STEP1   EXEC PGM=IKJEFT01,DYNAMNBR=10



   //SYSPRINT DD SYSOUT=*



   //SYSTSPRT DD SYSOUT=*



   //STDOUT   DD SYSOUT=*



   //STDERR   DD SYSOUT=*



   //SYSIN    DD DUMMY



   //SYSTSIN  DD *,SYMBOLS=EXECSYS



   BPXBATCH SH rm -Rf &MYUSS/GIMZIP



   BPXBATCH SH cd &MYUSS &&  +



   pax -rvf dynatrace-zos.pax GIMZIP



   //*



   //*



   //STEP2    EXEC PGM=GIMUNZIP,PARM='HASH=YES'



   //SMPDIR   DD PATH='&MYUSS/GIMZIP/',PATHDISP=KEEP



   //SMPCPATH DD PATH='/usr/lpp/smp/classes/',PATHDISP=KEEP



   //SMPJHOME DD PATH='/usr/lpp/java/J8.0/',PATHDISP=KEEP



   //SMPOUT   DD SYSOUT=*



   //SYSPRINT DD SYSOUT=*



   //SYSUT3   DD UNIT=SYSALLDA,SPACE=(CYL,(25,5))



   //SYSUT4   DD UNIT=SYSALLDA,SPACE=(CYL,(25,5))



   //SYSIN    DD *,SYMBOLS=EXECSYS



   <GIMUNZIP>



   <ARCHDEF archid="AUTHLIB"



   replace="YES"



   volume="&VOLSER"



   newname="&HLQ..&REL..SZDTAUTH">



   </ARCHDEF>



   <ARCHDEF archid="LOAD"



   replace="YES"



   volume="&VOLSER"



   newname="&HLQ..&REL..SZDTLOAD">



   </ARCHDEF>



   <ARCHDEF archid="SAMPLE"



   replace="YES"



   volume="&VOLSER"



   newname="&HLQ..&REL..SZDTSAMP">



   </ARCHDEF>



   </GIMUNZIP>



   /*



   //*



   //STEP3   EXEC PGM=IKJEFT01,DYNAMNBR=10



   //SYSPRINT DD SYSOUT=*



   //SYSTSPRT DD SYSOUT=*



   //STDOUT   DD SYSOUT=*



   //STDERR   DD SYSOUT=*



   //SYSIN    DD DUMMY



   //SYSTSIN  DD *,SYMBOLS=EXECSYS



   BPXBATCH SH export ussdir=&MYUSS &&+



   cp ${ussdir}/GIMZIP/dynatrace-oneagent-zos-java.jar +



   ${ussdir}/dynatrace-oneagent-zos-java.jar



   //*



   //*



   //STEP4   EXEC PGM=IKJEFT01,DYNAMNBR=55



   //SYSPRINT DD SYSOUT=*



   //SYSTSPRT DD SYSOUT=*



   //STDOUT   DD SYSOUT=*



   //STDERR   DD SYSOUT=*



   //SYSIN    DD DUMMY



   //SYSTSIN  DD *,SYMBOLS=EXECSYS



   BPXBATCH SH rm -Rf &MYUSS/GIMZIP



   //
   ```

   Если задание завершается с кодом возврата `0`, извлечение прошло успешно.

   Необязательно: удалите `dynatrace-zos.pax` и `dynatrace-oneagent-zos-java.jar` (если они не нужны), чтобы освободить дисковое пространство.

### Наборы данных продукта

В результате извлечения создаются следующие наборы данных продукта (имена приведены для высокоуровневого квалификатора по умолчанию и версии выпуска `R1nnnx`):

* `DT.R1nnnx.SZDTAUTH`: содержит подсистему zDC и модуль IMS, включая IMS Connect
* `DT.R1nnnx.SZDTLOAD`: содержит модуль CICS
* `DT.R1nnnx.SZDTSAMP`: содержит образцы JCL и определения CICS RDO

Использование дискового пространства наборами данных продукта

В среднем наборы данных продукта и файлы установки в каталоге z/OS USS занимают следующий объём дискового пространства:

```
Dsname                Tracks(3390) %Used



---------------------------------------



DT.R1nnnm.SZDTAUTH      893          5



DT.R1nnnm.SZDTLOAD       61         27



DT.R1nnnm.SZDTSAMP     1221         24
```

```
./GIMZIP/                      8K



./dynatrace-zos-1.nnn.m.pax    5M
```

### Определение псевдонимов

Рекомендуется определять псевдоним `ALIAS` без номера версии для наборов данных продукта. Используйте эти `ALIAS` в заданиях внедрения модулей zDC, CICS и IMS. Это позволит выполнять техническое обслуживание без обновления заданий.

Например:

```
DEFINE ALIAS(NAME('DT.DYNTRC.SZDTAUTH') RELATE('DT.R12770.SZDTAUTH'))



DEFINE ALIAS(NAME('DT.DYNTRC.SZDTLOAD') RELATE('DT.R12770.SZDTLOAD'))
```