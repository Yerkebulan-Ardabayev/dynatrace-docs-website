---
title: Наблюдаемость приложений с инъекцией во время выполнения пода
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/pod-runtime
scraped: 2026-05-12T11:52:43.553445
---

# Наблюдаемость приложений с инъекцией во время выполнения пода

# Наблюдаемость приложений с инъекцией во время выполнения пода

* Чтение: 7 мин
* Обновлено 17 октября 2025 г.

Внедрение модулей кода Dynatrace в контейнер во время его развёртывания.

Этот метод инструментирования приложений может не полностью связывать рабочие нагрузки Kubernetes с отслеживаемыми контейнерами и процессами. Для полноценных связей и сопоставления рассмотрите использование [автоматической инъекции только в приложение](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений в Kubernetes").

## Предварительные требования

* Ознакомьтесь со списком [поддерживаемых приложений и версий](/managed/ingest-from/technology-support "Найдите технические сведения, связанные с поддержкой Dynatrace для конкретных платформ и фреймворков разработки.").
* [Создайте токен доступа с областью `PaaS Integration - InstallerDownload`](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите понятие токена доступа и его областей.").
* Требования к хранилищу:

  + ~325 МБ для glibc
  + ~290 МБ для musl
  + ~650 МБ для glibc и musl вместе

Инъекция во время выполнения пода и cgroup v2

Если инъекция во время выполнения пода используется с [cgroup v2](https://kubernetes.io/docs/concepts/architecture/cgroups/), метрики `builtin:containers.*` передаются в Dynatrace только при соблюдении всех следующих условий:

* **Kubernetes API** доступен (см. [Предоставление роли viewer служебным учётным записям](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments#viewer "Упорядочивайте и фильтруйте отслеживаемые приложения, импортируя метки и аннотации из вашего окружения Kubernetes/OpenShift."))
* В поде запущен **один контейнер**

## Развёртывание

Чтобы интегрировать OneAgent в ваше приложение во время выполнения, выберите один из вариантов ниже в зависимости от вашей платформы.

Linux

Windows

OneAgent становится доступен контейнеру приложения через `initContainer`, ваш образ приложения остаётся незатронутым.

Чтобы интегрировать OneAgent в ваше приложение во время выполнения, расширьте шаблон развёртывания следующим образом.

```
# your application containers



containers:



- name: customer-app



image: tomcat



env:



- name: LD_PRELOAD



value: /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so



- name: DT_NETWORK_ZONE



value: <your_network_zone>



volumeMounts:



- mountPath: /opt/dynatrace/oneagent



name: oneagent



# initcontainer to download OneAgent



initContainers:



- name: install-oneagent



image: alpine:latest



command:



- /bin/sh



args:



- -c



- ARCHIVE=$(mktemp) && wget -O $ARCHIVE "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_PAAS_TOKEN&$DT_ONEAGENT_OPTIONS" && unzip -o -d /opt/dynatrace/oneagent $ARCHIVE && rm -f $ARCHIVE



env:



- name: DT_API_URL



value: https://<your-environment-id>.live.dynatrace.com/api



- name: DT_PAAS_TOKEN



value: <Access token with PaaS integration scopes (Dynatrace -> Access tokens)>



- name: DT_ONEAGENT_OPTIONS



value: flavor=<FLAVOR>&include=<TECHNOLOGY>



volumeMounts:



- mountPath: /opt/dynatrace/oneagent



name: oneagent



# Make OneAgent available as a volume



volumes:



- name: oneagent



emptyDir: {}
```

* В разделах `# initContainer to download OneAgent` и `# Make OneAgent available as a volume` добавьте `initContainer`, который загрузит OneAgent и сделает его доступным как том.
* В разделе `DT_ONEAGENT_OPTIONS` задайте модуль кода OneAgent, необходимый для вашего варианта компилятора (`FLAVOR`) и приложения (`TECHNOLOGY`).

  + Допустимые значения для `flavor`: `default`, `musl` или `multidistro`. Задайте `default`, чтобы загрузить двоичные файлы `glibc`, или задайте `musl`, чтобы загрузить двоичные файлы `musl`. Задайте `multidistro`, чтобы загрузить и двоичные файлы `musl`, и `glibc` и затем автоматически определять, какие из них использовать. Обратите внимание, что в этом случае размер образа будет больше, так как он включает оба варианта.
  + Допустимые значения для `technology`: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go` и `sdk`.
  + Для ARM используйте следующее значение: `flavor=default&arch=arm&include=<TECHNOLOGY>`. Для других архитектур см. [список допустимых значений](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest#parameters "Загрузите последнюю версию установщика OneAgent через Dynatrace API.") (прокрутите вниз до параметра `arch`).
  + Если необходимо указать несколько модулей кода, используйте следующий синтаксис: `&include=technology1&include=technology2`.

Если включить параметры поддержки конкретных технологий вместо параметров «поддержки всех технологий», вы получите пакет OneAgent меньшего размера.

Что делать, если мой образ Docker основан на Alpine Linux?

Dynatrace OneAgent поддерживает вариант `musl` для окружений на основе Alpine Linux.
Допустимые значения для `technology`: `all`, `dotnet`, `go`, `php`, `java`, `apache`, `nginx` и `nodejs`.

* В разделе `# your application containers` добавьте только что созданный том в контейнер вашего приложения. Также добавьте переменную окружения `LD_PRELOAD`.
* Необязательно. В разделе `# your application containers` настройте network zones:

```
containers:



env:



- name: DT_NETWORK_ZONE



value: <your_network_zone>
```

Подробнее см. [network zones](/managed/manage/network-zones "Узнайте, как работают network zones в Dynatrace.").

* Необязательно. Настройте адрес прокси.

Если вы используете окружение с прокси, необходимо задать переменную окружения `DT_PROXY` в контейнере приложения, чтобы передать учётные данные прокси в OneAgent.

Для контейнеров на основе Alpine Linux может потребоваться обновить `wget`, поставляемый с образом Alpine, чтобы разрешить аутентификацию прокси для загрузки OneAgent.

Расширьте шаблон развёртывания следующим образом.

Этот вариант относится к приложениям .NET в контейнерах Windows.

OneAgent версии 1.319 и ранее

```
# your application containers



apiVersion: apps/v1



kind: Deployment



metadata:



name: sample



labels:



app: sample



spec:



replicas: 1



template:



metadata:



name: sample



labels:



app: sample



spec:



nodeSelector:



"kubernetes.io/os": windows



containers:



- name: sample



image: mcr.microsoft.com/dotnet/framework/samples:aspnetapp



env:



#.NET Framework



- name: COR_ENABLE_PROFILING



value: "0x01"



- name: COR_PROFILER



value: "{B7038F67-52FC-4DA2-AB02-969B3C1EDA03}"



- name: COR_PROFILER_PATH_32



value: "C:\\oneagent\\agent\\lib\\oneagentloader.dll"



- name: COR_PROFILER_PATH_64



value: "C:\\oneagent\\agent\\lib64\\oneagentloader.dll"



#.NET Core



- name: CORECLR_ENABLE_PROFILING



value: "0x01"



- name: CORECLR_PROFILER



value: "{B7038F67-52FC-4DA2-AB02-969B3C1EDA03}"



- name: CORECLR_PROFILER_PATH_32



value: "C:\\oneagent\\agent\\lib\\oneagentloader.dll"



- name: CORECLR_PROFILER_PATH_64



value: "C:\\oneagent\\agent\\lib64\\oneagentloader.dll"



- name: DT_AGENTACTIVE



value: "true"



- name: DT_BLOCKLIST



value: "powershell*"



volumeMounts:



- mountPath: "C:\\OneAgent"



name: oneagent



# initcontainer to download OneAgent



initContainers:



- name: install-oneagent



image: mcr.microsoft.com/windows/servercore:ltsc2019



command:



- powershell



args:



- |



Write-Host "Trustng all certificates..."



add-type @"



using System.Net;



using System.Security.Cryptography.X509Certificates;



public class TrustAllCertsPolicy : ICertificatePolicy {



public bool CheckValidationResult(



ServicePoint srvPoint, X509Certificate certificate,



WebRequest request, int certificateProblem) {



return true;



}



}



"@



[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy



Write-Host "Downloading agent..."



Invoke-WebRequest -Uri "$Env:DT_API_URL/v1/deployment/installer/agent/windows/paas/latest?Api-Token=$Env:DT_PAAS_TOKEN&$Env:DT_ONEAGENT_OPTIONS" -OutFile "installer.zip"



Write-Host "Unpacking agent..."



Expand-Archive -Path "installer.zip" -DestinationPath "C:\OneAgent" -Force



Write-Host "Configuring agent..."



$manifest = Get-Content "C:\OneAgent\manifest.json" | ConvertFrom-Json



$config = New-Item -Path "C:\OneAgent\agent\conf" -Name "standalone.conf" -Force



Add-Content -Path $config -Value "tenant $($manifest.tenantUUID)"



Add-Content -Path $config -Value "tenanttoken $($manifest.tenantToken)"



Add-Content -Path $config -Value "server $($manifest.communicationEndpoints -Join ';')"



Add-Content -Path $config -Value "storage C:\OneAgent"



Add-Content -Path $config -Value "loglevelcon NONE"



env:



- name: DT_API_URL



value: https://<your-environment-id>.live.dynatrace.com/api



- name: DT_PAAS_TOKEN



value: <Access token with PaaS integration scopes (Dynatrace -> Access tokens)>



- name: DT_ONEAGENT_OPTIONS



value: arch=default&include=dotnet



volumeMounts:



- mountPath: "C:\\OneAgent"



name: oneagent



# Make OneAgent available as a volume



volumes:



- name: oneagent



emptyDir: {}



selector:



matchLabels:



app: sample



---



apiVersion: v1



kind: Service



metadata:



name: sample



spec:



type: LoadBalancer



ports:



- protocol: TCP



port: 80



selector:



app: sample
```

OneAgent версии 1.321+

```
# your application containers



apiVersion: apps/v1



kind: Deployment



metadata:



name: sample



labels:



app: sample



spec:



replicas: 1



template:



metadata:



name: sample



labels:



app: sample



spec:



nodeSelector:



"kubernetes.io/os": windows



containers:



- name: sample



image: mcr.microsoft.com/dotnet/framework/samples:aspnetapp



env:



#.NET Framework



- name: COR_ENABLE_PROFILING



value: "0x01"



- name: COR_PROFILER



value: "{B7038F67-52FC-4DA2-AB02-969B3C1EDA03}"



- name: COR_PROFILER_PATH_32



value: "C:\\oneagent\\agent\\bin\\current\\windows-x86-32\\oneagentdotnet.dll"



- name: COR_PROFILER_PATH_64



value: "C:\\oneagent\\agent\\bin\\current\\windows-x86-64\\oneagentdotnet.dll"



#.NET Core



- name: CORECLR_ENABLE_PROFILING



value: "0x01"



- name: CORECLR_PROFILER



value: "{B7038F67-52FC-4DA2-AB02-969B3C1EDA03}"



- name: CORECLR_PROFILER_PATH_32



value: "C:\\oneagent\\agent\\bin\\current\\windows-x86-32\\oneagentdotnet.dll"



- name: CORECLR_PROFILER_PATH_64



value: "C:\\oneagent\\agent\\bin\\current\\windows-x86-64\\oneagentdotnet.dll"



- name: DT_AGENTACTIVE



value: "true"



- name: DT_BLOCKLIST



value: "powershell*"



volumeMounts:



- mountPath: "C:\\OneAgent"



name: oneagent



# initcontainer to download OneAgent



initContainers:



- name: install-oneagent



image: mcr.microsoft.com/windows/servercore:ltsc2019



command:



- powershell



args:



- |



Write-Host "Trustng all certificates..."



add-type @"



using System.Net;



using System.Security.Cryptography.X509Certificates;



public class TrustAllCertsPolicy : ICertificatePolicy {



public bool CheckValidationResult(



ServicePoint srvPoint, X509Certificate certificate,



WebRequest request, int certificateProblem) {



return true;



}



}



"@



[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy



Write-Host "Downloading agent..."



Invoke-WebRequest -Uri "$Env:DT_API_URL/v1/deployment/installer/agent/windows/paas/latest?Api-Token=$Env:DT_PAAS_TOKEN&$Env:DT_ONEAGENT_OPTIONS" -OutFile "installer.zip"



Write-Host "Unpacking agent..."



Expand-Archive -Path "installer.zip" -DestinationPath "C:\OneAgent" -Force



Write-Host "Configuring agent..."



$manifest = Get-Content "C:\OneAgent\manifest.json" | ConvertFrom-Json



$config = New-Item -Path "C:\OneAgent\agent\conf" -Name "standalone.conf" -Force



Add-Content -Path $config -Value "tenant $($manifest.tenantUUID)"



Add-Content -Path $config -Value "tenanttoken $($manifest.tenantToken)"



Add-Content -Path $config -Value "server $($manifest.communicationEndpoints -Join ';')"



Add-Content -Path $config -Value "storage C:\OneAgent"



Add-Content -Path $config -Value "loglevelcon NONE"



env:



- name: DT_API_URL



value: https://<your-environment-id>.live.dynatrace.com/api



- name: DT_PAAS_TOKEN



value: <Access token with PaaS integration scopes (Dynatrace -> Access tokens)>



- name: DT_ONEAGENT_OPTIONS



value: arch=default&include=dotnet



volumeMounts:



- mountPath: "C:\\OneAgent"



name: oneagent



# Make OneAgent available as a volume



volumes:



- name: oneagent



emptyDir: {}



selector:



matchLabels:



app: sample



---



apiVersion: v1



kind: Service



metadata:



name: sample



spec:



type: LoadBalancer



ports:



- protocol: TCP



port: 80



selector:



app: sample
```

* В разделах `# initContainer to download OneAgent` и `# Make OneAgent available as a volume` добавьте `initContainer`, который загрузит OneAgent и сделает его доступным как том.
* Раздел `# your application containers` содержит переменные окружения, которые включают мониторинг приложений .NET Framework и .NET Core. Они могут быть заданы одновременно. Для .NET Core `COR_ prefix` меняется на `CORECLR_`, например `CORECLR_ENABLE_PROFILING`.

Чтобы сообщать корректные лимиты памяти в Kubernetes

1. Необходимо указать лимит в развёртывании.

   ```
   spec:



   containers:



   ...



   resources:



   limits:



   memory: "32Gi"



   requests:



   memory: "4Gi"
   ```
2. Необходимо включить доступ к Kubernetes API, чтобы OneAgent мог прочитать это значение.

## Обновление

Каждый раз, когда необходимо задействовать новую версию OneAgent, достаточно повторно развернуть поды. При инъекциях во время выполнения OneAgent загружается и внедряется внутри `initContainer`. По умолчанию загружается последняя версия OneAgent, но можно управлять тем, какая версия OneAgent загружается, указав её в URL-адресе загрузки.

## Удаление

Чтобы удалить OneAgent из мониторинга только приложений

1. Удалите YAML install-oneagent из шаблона развёртывания.

   ```
   # your application containers



   containers:



   - name: customer-app



   image: tomcat



   env:



   - name: LD_PRELOAD



   value: /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so



   volumeMounts:



   - mountPath: /opt/dynatrace/oneagent



   name: oneagent



   # initContainer to download OneAgent



   initContainers:



   - name: install-oneagent



   image: alpine:3.8



   command:



   - /bin/sh



   args:



   - -c



   - ARCHIVE=$(mktemp) && wget -O $ARCHIVE "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_PAAS_TOKEN&$DT_ONEAGENT_OPTIONS" && unzip -o -d /opt/dynatrace/oneagent $ARCHIVE && rm -f $ARCHIVE



   env:



   - name: DT_API_URL



   value: https://<Your-environment-ID>.live.dynatrace.com/api



   - name: DT_PAAS_TOKEN



   value: <paastoken>



   - name: DT_ONEAGENT_OPTIONS



   value: flavor=<FLAVOR>&include=<TECHNOLOGY>



   volumeMounts:



   - mountPath: /opt/dynatrace/oneagent



   name: oneagent



   # Make OneAgent available as a volume



   volumes:



   - name: oneagent



   emptyDir: {}
   ```
2. Повторно разверните ваше приложение.