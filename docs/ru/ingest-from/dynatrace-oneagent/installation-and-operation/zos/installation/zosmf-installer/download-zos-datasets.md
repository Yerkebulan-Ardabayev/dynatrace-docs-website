---
title: Загрузка наборов данных продуктов z/OS
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets
scraped: 2026-03-04T21:28:44.483728
---

# Загрузка наборов данных продукта z/OS


* Latest Dynatrace
* 5-min read

Вы можете загрузить PAX-файл, содержащий модули CICS, IMS, z/OS Java и zDC, двумя способами:

* Dynatrace версии 1.272+ Загрузка через [Deployment API](#using-deploymentapi).
* Dynatrace версии 1.276+ Загрузка через [веб-интерфейс](#using-webui).

Начиная с OneAgent версии 1.275, PAX-файл больше не публикуется на нашем FTP-сервере.

## Загрузка PAX-файла

Вы можете загрузить последнюю или конкретную версию PAX-файла через веб-интерфейс или Deployment API для OneAgent.

Версия PAX-файла должна быть меньше или равна версии модуля zRemote.

### Загрузка последней версии через веб-интерфейс

1. Найдите **Deploy OneAgent**
2. Выберите **z/OS** и **Download z/OS product datasets** для загрузки последней версии PAX-файла.

Имя файла `dynatrace-zos-1.nnn.m.pax` включает номер основной версии `nnn` и `m` — минорной.

### Загрузка конкретной версии через веб-интерфейс

Вы можете загрузить конкретную версию PAX-файла через веб-интерфейс следующим образом:

1. Перейдите в **Settings** > **Monitoring** > **Monitoring overview**.
2. Выберите **Download Dynatrace OneAgent or ActiveGate installer** и укажите предпочтительную версию:

   1. Installer: `OneAgent - z/OS`
   2. Build: выберите предпочтительную основную версию
   3. Revision: выберите предпочтительную минорную версию

   ![zos monitoring overview](https://dt-cdn.net/images/zos-monitoring-overview-1289-aa537f3578.png)
3. Выберите **Continue** и **Download z/OS product datasets** для загрузки указанной версии PAX-файла.

   Имя файла `dynatrace-zos-1.nnn.m.pax` включает номер основной версии `nnn` и `m` — минорной.

### Загрузка последней версии через Deployment API

Вы можете загрузить последнюю версию PAX-файла через Deployment API следующим образом:

1. Сгенерируйте [токен доступа](../../../../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью **PaaS integration - Installer download** (`InstallerDownload`).
2. Загрузите последнюю версию PAX-файла через Deployment API - Download latest OneAgent:

   Ниже приведён пример команды `curl` для SaaS-среды, использующей Deployment API для загрузки последней версии PAX-файла:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/latest" -H "accept: */*" -H "Authorization: Api-Token <accessToken>" --output dynatrace-zos.pax
   ```

   Замените `<environment>` на идентификатор вашей среды Dynatrace и `<accessToken>` на сгенерированный токен доступа.

### Загрузка конкретной версии через Deployment API

Вы можете загрузить конкретную версию PAX-файла через Deployment API следующим образом:

1. Сгенерируйте [токен доступа](../../../../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.") с областью **PaaS integration - Installer download** (`InstallerDownload`).
2. Получите список всех доступных версий PAX-файла через Deployment API - List available versions of OneAgent.

   Ниже приведён пример команды `curl` для SaaS-среды, использующей Deployment API для получения списка всех доступных версий PAX-файла:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/versions/zos/mainframe" -H "accept: */*" -H "Authorization: Api-Token <accessToken>"
   ```

   Замените `<environment>` на идентификатор вашей среды Dynatrace и `<accessToken>` на сгенерированный токен доступа.
3. Загрузите конкретную версию PAX-файла через Deployment API - Download OneAgent of specific version:

   Ниже приведён пример команды `curl` для SaaS-среды, использующей Deployment API для загрузки конкретной версии PAX-файла:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/version/<version>" -H "accept: */*" -H "Authorization: Api-Token <accessToken>" --output dynatrace-zos.pax
   ```

   Замените `<environment>` на идентификатор вашей среды Dynatrace, `<version>` на выбранную версию PAX-файла и `<accessToken>` на сгенерированный токен доступа.

## Извлечение наборов данных продукта

Вы можете извлечь наборы данных продукта из PAX-файла следующим образом:

1. Перенесите PAX-файл в каталог z/OS USS в бинарном режиме.
2. Переименуйте PAX-файл из `dynatrace-zos-1.nnn.m.pax` в `dynatrace-zos.pax`.
3. Используйте задание `EXTRACT`, приведённое ниже, для извлечения наборов данных продукта из установочных файлов. Перед запуском задания измените следующее:

   1. Определите желаемый верхнеуровневый квалификатор для имён наборов данных установки и задайте переменную `HLQ` соответствующим образом.
   2. Задайте `MYUSS` как путь к каталогу z/OS USS, куда вы поместили файл `dynatrace-zos.pax`. Если длина пути к каталогу превышает 42 символа, это может привести к ошибке на шаге `STEP3` задания. В таком случае необходимо изменить JCL для учёта символа продолжения.
   3. Измените серийный номер тома `VOLSER` в соответствии со стандартами площадки.

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

   Необязательно: удалите `dynatrace-zos.pax` и `dynatrace-oneagent-zos-java.jar` (если он не нужен) для освобождения дискового пространства.

### Наборы данных продукта

Процесс извлечения создаёт следующие наборы данных продукта (имена приведены для верхнеуровневого квалификатора по умолчанию и версии выпуска `R1nnnx`):

* `DT.R1nnnx.SZDTAUTH`: содержит подсистему zDC и модуль IMS, включая IMS Connect
* `DT.R1nnnx.SZDTLOAD`: содержит модуль CICS
* `DT.R1nnnx.SZDTSAMP`: включает примеры JCL и определения CICS RDO

Использование дискового пространства наборами данных продукта

В среднем наборы данных продукта и установочные файлы в каталоге z/OS USS используют следующее дисковое пространство:

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

Мы рекомендуем определить `ALIAS` без номера версии для наборов данных продукта. Используйте эти `ALIAS` в заданиях внедрения модулей zDC, CICS и IMS. Это позволит выполнять обслуживание без обновления заданий.

Например:

```
DEFINE ALIAS(NAME('DT.DYNTRC.SZDTAUTH') RELATE('DT.R12770.SZDTAUTH'))


DEFINE ALIAS(NAME('DT.DYNTRC.SZDTLOAD') RELATE('DT.R12770.SZDTLOAD'))
```