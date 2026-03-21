---
title: Настройка и развертывание EdgeConnect
source: https://www.dynatrace.com/docs/ingest-from/edgeconnect
scraped: 2026-03-06T21:25:27.980148
---

Используйте EdgeConnect, чтобы приложения и рабочие процессы безопасно взаимодействовали с вашими системами. EdgeConnect доступен как контейнер Docker и может работать в любой среде выполнения контейнеров.

На следующей схеме стрелки указывают направление инициации соединения. EdgeConnect подключается к AppEngine и выполняет определенное пользователем подмножество HTTP(S)-запросов внутри нужной сети от имени среды выполнения Dynatrace.

![Схема подключения EdgeConnect](https://dt-cdn.net/images/edgeconnect-security-801-2e3e1a781e.webp)

EdgeConnect также может работать за HTTP-прокси:

![EdgeConnect за прокси](https://dt-cdn.net/images/edgeconnect-proxy-1000-f43df1adec.webp)

## Настройка EdgeConnect

1. Перейдите в **Settings** > **General** > **External Requests** > **EdgeConnect**.
2. Выберите **New EdgeConnect**.
3. Введите **Имя** и **Шаблоны хостов**.

### Права пользователей

Обычному пользователю платформы предоставляется доступ только для чтения к конфигурациям EdgeConnect через разрешение `app-engine:edge-connects:read`, привязанное к [политикам по умолчанию](../manage/identity-access-management/permission-management/default-policies.md#access "Справочник политик по умолчанию Dynatrace") Standard и Pro.

Если вы хотите настроить EdgeConnect для подключения к вашей среде, ваш пользователь должен принадлежать к группе, привязанной к политике с определенными разрешениями IAM.

[Политика по умолчанию](../manage/identity-access-management/permission-management/default-policies.md#access "Справочник политик по умолчанию Dynatrace") Admin уже содержит необходимые области видимости, поэтому пользователь-администратор может полностью управлять конфигурациями EdgeConnect по умолчанию.

Если вам нужно создать собственную политику для пользователей-администраторов, необходимо включить в нее следующие разрешения.

#### Чтение конфигураций EdgeConnect

```
ALLOW app-engine:edge-connects:read;
```

#### Создание новой конфигурации EdgeConnect

```
ALLOW app-engine:edge-connects:write, oauth2:clients:manage WHERE oauth2:scopes = "app-engine:edge-connects:connect";
```

Для создания клиента OAuth для нового EdgeConnect необходимо разрешение на управление клиентами OAuth.

#### Обновление конфигурации EdgeConnect:

```
ALLOW app-engine:edge-connects:write;
```

#### Ротация секрета клиента OAuth для EdgeConnect

```
ALLOW oauth2:clients:manage where oauth2:scopes="app-engine:edge-connects:connect";
```

#### Удаление EdgeConnect

```
ALLOW app-engine:edge-connects:delete, oauth2:clients:manage WHERE oauth2:scopes = "app-engine:edge-connects:connect";
```

Для удаления клиента OAuth для EdgeConnect необходимо разрешение на управление клиентами OAuth.

Для настройки политик и членства в группах пользователей перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Identity & access management** и выберите **People**, **Groups** или **Policies**. Подробнее см. [Управление политиками IAM](../manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt.md "Создание, редактирование, копирование и удаление политик IAM для управления разрешениями пользователей Dynatrace.").

### Создание новой конфигурации EdgeConnect

Перед [развертыванием EdgeConnect](#deploy) в вашей сети необходимо сопоставить определенные шаблоны хостов HTTP-запросов с конкретными экземплярами EdgeConnect.

1. Перейдите в **Settings** > **General** > **External Requests** > **EdgeConnect**.
2. Выберите **New EdgeConnect**.

   * Введите уникальное имя для экземпляра EdgeConnect.

     + Имя должно соответствовать [RFC 1123 Label Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names) с максимальной длиной 50 символов
   * Укажите шаблоны хостов запросов, которые должен обрабатывать экземпляр EdgeConnect.

     Вы можете использовать подстановочный знак для замены первых частей домена хоста. Например, `*.myapp.org` соответствует `staging.myapp.org` и `prod.myapp.org`.
3. Нажмите **Create**.
4. Скачайте созданный конфигурационный файл `edgeConnect.yaml`. Этот файл необходимо использовать для настройки образа EdgeConnect, который будет запущен [в следующем разделе](#config).

   Обратите внимание, что секрет клиента OAuth отображается только один раз и не может быть получен позже. В дальнейшем конфигурационный файл все еще можно скачать, но секрет клиента OAuth в нем уже не будет предустановлен.

Любой HTTP-запрос (из функций вашего приложения, рабочих процессов или специальных функций), соответствующий определенному шаблону хоста, обрабатывается экземпляром EdgeConnect, указанным в этой конфигурации.

Например, при шаблоне хоста `staging.myapp.org` в его конфигурации среда выполнения Dynatrace направит HTTP-запрос с URL `https://staging.myapp.org/test.html` на этот EdgeConnect.

Теперь вы готовы развернуть соответствующий EdgeConnect в вашей сети.

## Развертывание EdgeConnect

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Обеспечение связности**](#connectivity)[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка образа EdgeConnect**](#config)[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Получение образа контейнера EdgeConnect**](#image)[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Запуск контейнера**](#run)[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Проверка соединения**](#validate)

Выполните следующие шаги, чтобы запустить EdgeConnect.

### Шаг 1: Обеспечение связности

EdgeConnect должен иметь возможность подключаться к Dynatrace и вашим внутренним системам.

#### Связность с Dynatrace

EdgeConnect инициирует следующие подключения для работы.

* `https://sso.dynatrace.com/sso/oauth2/token`
* `https://<ваш ID среды>.apps.dynatrace.com`

EdgeConnect не требует никакого входящего подключения от Dynatrace.

#### Связность в вашей сети

EdgeConnect требует подключения к любому приложению в вашей сети, к которому вы хотите подключить Dynatrace для функций приложений, специальных функций или действий рабочих процессов. Если ваш EdgeConnect взаимодействует за прокси по HTTPS, вам также необходимо добавить доверенные сертификаты хостов, к которым подключается EdgeConnect. Если HTTP-прокси выполняет перехват TLS, вам также необходимо добавить сертификат этого прокси. Инструкции см. в разделе [сертификаты](#run-certificates).

### Шаг 2: Настройка образа EdgeConnect

Контейнеру Docker EdgeConnect требуется конфигурационный файл `edgeConnect.yaml`, который следует скачать из **Settings** > **General** > **External Requests** при первоначальном [создании конфигурации](#createconfiguration).
Вы ссылаетесь на этот файл при запуске образа Docker EdgeConnect.

Обратите внимание, что необходимо указать `name`, `oauth.client_id` и `oauth.client_secret` в соответствии с настройками в приложении. В противном случае EdgeConnect не сможет подключиться к платформе.

Пример `edgeConnect.yaml`

```
name: my-corporate-network


api_endpoint_host: abc12345.apps.dynatrace.com


oauth:


endpoint: https://sso.dynatrace.com/sso/oauth2/token


client_id: <DYNATRACE_TOKEN_PLACEHOLDER>


client_secret: *******


resource: urn:dtenvironment:abc12345


restrict_hosts_to:


- "internal.example.org"


- "*.example.com"


certificate_paths:


- "/path/to/some/certificate.cer"


- "/path/to/another/certificate.pem"


proxy:


server: proxy.example.org


port: 8037


exceptions:


- "*.foo.com"


- "noproxy.example.org"


auth:


user: "proxy-user"


password: "*******"


secrets:


- name: My secret


token: <DYNATRACE_TOKEN_PLACEHOLDER>.some-token-secret


from_env: MY_SECRET


restrict_hosts_to:


- dynatrace.com


- name: My other secret


token: <DYNATRACE_TOKEN_PLACEHOLDER>.another-token-secret


from_file: /path/to/my/other/secret


restrict_hosts_to:


- internal.example.com
```

Вы можете переопределить определенные значения конфигурации через переменные окружения.
Имена переменных окружения для каждого поля см. в таблице ниже.

#### Описание полей

Поля `edgeConnect.yaml` и имена соответствующих переменных окружения описаны в таблице ниже.
Обратите внимание, что некоторые имена переменных окружения используют как одинарное (`_`), так и двойное подчеркивание (`__`).

##### Секреты

При отправке запросов к службам за пределами платформы Dynatrace, скорее всего, потребуются секреты для аутентификации взаимодействия со службами (например, API-токены или секреты в URL вебхуков).
Однако ваши приложения и рабочие процессы никогда не должны содержать значения секретов в открытом виде, чтобы избежать непреднамеренной утечки.

Вместо этого EdgeConnect поддерживает токены-заполнители, которые вы можете использовать в параметрах запросов, заголовках и телах запросов.
EdgeConnect затем безопасно заменяет вхождения этих токенов на реальные значения секретов, которые вы настраиваете в файле `edgeConnect.yaml`.

В этом разделе описано, как настроить такие секреты.
EdgeConnect может читать секреты из двух источников: из переменных окружения или из файлов, смонтированных в контейнер EdgeConnect.

Если вы запускаете [EdgeConnect в Kubernetes через Dynatrace Operator](#kubernetes), указанные выше поля настраиваются с помощью параметров пользовательского ресурса Kubernetes, как описано в [Параметры EdgeConnect для Dynatrace Operator](setup-on-k8s/reference/edgeconnect-parameters.md "Список параметров конфигурации для EdgeConnect.").

### Шаг 3: Получение образа контейнера EdgeConnect

Для запуска контейнера EdgeConnect сначала необходимо получить образ.

#### Проверка образа контейнера EdgeConnect

Dynatrace предоставляет подписанные образы контейнеров для обеспечения подлинности и целостности, а также спецификацию состава программного обеспечения (SBOM), которая перечисляет все включенные программные компоненты.
Проверка подписей и анализ SBOM позволяет эффективно управлять уязвимостями и снижать риски.
Подробнее о проверке см. [Проверка аттестации спецификации состава программного обеспечения (SBOM)](setup-on-k8s/guides/container-registries/verify-image-signature.md#sbom-attestation-verification "Проверка подписей образов Dynatrace").

```
docker pull dynatrace/edgeconnect:latest
```

Рекомендуется всегда использовать (и регулярно обновлять до) последнюю доступную версию EdgeConnect.

После успешной загрузки вы получите уведомление.

```
Status: Downloaded image for dynatrace/edgeconnect:latest


docker.io/dynatrace/edgeconnect:latest
```

### Шаг 4: Запуск контейнера

1. Перейдите в каталог с созданным файлом `edgeConnect.yaml`.
2. Запустите контейнер.

   ```
   docker run \


   --mount type=bind,src=${PWD}/edgeConnect.yaml,dst=/edgeConnect.yaml \


   -d --restart always \


   dynatrace/edgeconnect \
   ```

Настройка расположения конфигурационного файла `edgeConnect.yaml`

Вы можете настроить расположение, из которого загружается конфигурационный файл, через переменную окружения `EDGE_CONNECT_CONFIG_PATH`.

Например, установка `EDGE_CONNECT_CONFIG_PATH` в `/etc/config` заставит EdgeConnect загрузить файл `/etc/config/edgeConnect.yaml` внутри файловой системы контейнера.

#### Пользовательские TLS-сертификаты

Для связи по каналам, зашифрованным TLS (HTTPS и безопасные WebSocket), EdgeConnect проверяет идентичность хоста на основе его сертификата.

Для связи с хостами, использующими пользовательские сертификаты, необходимо добавить пути к сертификатам в параметр `certificate_paths` файла `edgeConnect.yaml` (или в переменную окружения `EDGE_CONNECT_CERTIFICATE_PATHS`) и смонтировать сертификаты в контейнер EdgeConnect.
Сертификаты обычно монтируются в `/etc/edge_connect_certs` по соглашению, но вы также можете указать другой каталог.

EdgeConnect поддерживает файлы сертификатов в форматах PEM (".pem", ".crt" или ".cer") и DER (".der").

1. Отредактируйте файл `edgeConnect.yaml` и добавьте целевой путь в контейнере EdgeConnect, где хранятся сертификаты. Например:

   ```
   certificate_paths:


   - "/etc/edge_connect_certs/certificate.pem"
   ```
2. Смонтируйте пользовательский сертификат в контейнер EdgeConnect. Для этого можно использовать параметр `-v` при запуске контейнера. Например:

   ```
   docker run \


   --mount type=bind,src=${PWD}/edgeConnect.yaml,dst=/edgeConnect.yaml \


   -d --restart always \


   -v /host/path/to/certificate.pem:/etc/edge_connect_certs/certificate.pem


   dynatrace/edgeconnect \
   ```

   Где,

   * `/host/path/to/certificate.pem` -- путь к сертификату на хосте
   * `/etc/edge_connect_certs/certificate.pem` -- целевой путь в контейнере EdgeConnect, куда будет смонтирован файл сертификата

Прокси с перехватом TLS

Если вы используете EdgeConnect за HTTP-прокси, выполняющим перехват TLS, необходимо добавить сертификат прокси в поле `certificate_paths`, чтобы EdgeConnect мог проверить идентичность прокси.

##### Устранение неполадок

Если EdgeConnect прерывает HTTPS-соединение из-за ошибки проверки сертификата, это может быть вызвано неполной конфигурацией или недействительными SSL-сертификатами. В таблице ниже перечислены распространенные ошибки проверки сертификатов, которые могут появиться в журналах контейнера EdgeConnect.

#### Секреты

Выполните следующие шаги, чтобы EdgeConnect заменял токены секретов в ваших запросах:

1. Отредактируйте файл `edgeConnect.yaml` и добавьте соответствующую конфигурацию для ваших секретов (описание полей см. в [таблице выше](#edgeconnect-yaml-secrets-fields)). Следующий пример иллюстрирует конфигурацию, охватывающую секрет, загружаемый из переменной окружения, а также секрет, загружаемый из файла:

   ```
   secrets:


   - name: My secret


   token: <DYNATRACE_TOKEN_PLACEHOLDER>.some-token-secret


   from_env: MY_SECRET


   restrict_hosts_to:


   - dynatrace.com


   - name: My other secret


   token: <DYNATRACE_TOKEN_PLACEHOLDER>.another-token-secret


   from_file: /path/to/my/other/secret


   restrict_hosts_to:


   - internal.example.com
   ```
2. Предоставьте значения для секретных переменных окружения и секретных файлов в контейнер EdgeConnect. Для этого можно использовать параметр `-e` для настройки значений переменных окружения, передаваемых контейнеру, и параметр `-v` для монтирования секретных файлов. Например:

   ```
   docker run \


   --mount type=bind,src=${PWD}/edgeConnect.yaml,dst=/edgeConnect.yaml \


   -d --restart always \


   -e MY_SECRET=******* \


   -v /host/path/to/my/other/secret:/container/path/to/mounted/secret


   dynatrace/edgeconnect \
   ```

   Где,

   * `MY_SECRET` -- имя переменной окружения, содержащей секретное значение "My secret" (представлено как `"*******"`)
   * `/host/path/to/my/other/secret` -- путь к секретному файлу на хост-системе
   * `/container/path/to/mounted/secret` -- целевой путь в контейнере EdgeConnect, куда монтируется секретный файл

### Шаг 5: Проверка соединения

Проверьте, что EdgeConnect успешно подключился к платформе.

1. Перейдите в **Settings** > **General** > **External Requests** > **EdgeConnect**.
2. Проверьте столбец **Availability**. Он должен отображать **online**.

   * Если он все еще offline, проверьте журналы контейнера Docker на наличие сообщений об ошибках.
   * Если приложение показывает, что есть онлайн-экземпляры EdgeConnect, поздравляем! Вы безопасно подключили свою среду к платформе Dynatrace.

     Отныне любой HTTP-запрос, происходящий в рамках функции приложения, специальной функции или действия рабочего процесса, соответствующий шаблону хоста, будет прозрачно выполняться EdgeConnect вместо среды выполнения Dynatrace напрямую.

## Запуск EdgeConnect в Kubernetes

Dynatrace Operator обеспечивает специальную поддержку для запуска EdgeConnect через пользовательский ресурс EdgeConnect. Существует три сценария развертывания:

* Используйте Dynatrace Operator только для развертывания EdgeConnect, как описано в [Настройка EdgeConnect](setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect.md "Развертывание и настройка EdgeConnect в Kubernetes с помощью Dynatrace."). Вы по-прежнему создаете конфигурацию EdgeConnect в приложении и следуете инструкциям в **Actions** > **Deploy EdgeConnect** > **Deploy via Dynatrace Operator**.
* Позвольте Dynatrace Operator создать конфигурацию EdgeConnect, как описано в [Подготовка EdgeConnect для среды Dynatrace](setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect-provision.md "Подготовка EdgeConnect для среды Dynatrace."), чтобы Operator полностью управлял жизненным циклом EdgeConnect. Operator создаст конфигурацию самостоятельно, а шаблоны хостов EdgeConnect указываются в пользовательском ресурсе EdgeConnect. Эти конфигурации нельзя редактировать в приложении.
* Настройте EdgeConnect без Dynatrace Operator, как описано в <#no-operator>.

### Запуск EdgeConnect в Kubernetes без использования Dynatrace Operator

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Обеспечение связности**](#no-operator-connectivity)[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка развертывания EdgeConnect**](#no-operator-configure-deployment)[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Применение развертывания**](#no-operator-deployment)[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Проверка соединения**](#no-operator-validate)

Выполните следующие шаги для развертывания EdgeConnect в Kubernetes без Dynatrace Operator.

### Шаг 1: Обеспечение связности

Следуйте инструкциям в разделе [Обеспечение связности](#connectivity), чтобы убедиться, что Dynatrace доступен из вашего кластера Kubernetes.

### Шаг 2: Настройка развертывания EdgeConnect

Скачайте конфигурацию `edgeConnect.yaml` при [создании конфигурации](#createconfiguration), она содержит все значения конфигурации, необходимые для настройки EdgeConnect.
Сохраните пример ниже в файл `deployment.yaml` и замените значения, заключенные в `< >`, на значения из вашего `edgeConnect.yaml`.

```
apiVersion: v1


kind: Secret


metadata:


name: edge-connect-oauth


namespace: dynatrace


stringData:


oauth-client-id: <oauth.client_id from edgeConnect.yaml>


oauth-client-secret: <oauth.client_secret from edgeConnect.yaml>


---


apiVersion: v1


kind: Secret


metadata:


name: edge-connect-config


namespace: dynatrace


stringData:


edge-connect-config-file: |


certificate_paths:


- "/etc/edge_connect_certs/some_certificate.cer"


- "/etc/edge_connect_certs/another_certificate.pem"


secrets:


- name: My secret


token: <DYNATRACE_TOKEN_PLACEHOLDER>.some-token-secret


from_env: MY_SECRET


restrict_hosts_to:


- dynatrace.com


- name: My other secret


token: <DYNATRACE_TOKEN_PLACEHOLDER>.another-token-secret


from_file: /path/to/my/other/secret


restrict_hosts_to:


- internal.example.com


---


apiVersion: apps/v1


kind: Deployment


metadata:


name: example-edge-connect


namespace: dynatrace


spec:


replicas: 1


selector:


matchLabels:


app: edge-connect


template:


metadata:


labels:


app: edge-connect


spec:


containers:


- name: edge-connect


image: dynatrace/edgeconnect:latest


imagePullPolicy: IfNotPresent


env:


- name: EDGE_CONNECT_NAME


value: <name from edgeConnect.yaml>


- name: EDGE_CONNECT_API_ENDPOINT_HOST


value: <api_endpoint_host from edgeConnect.yaml>


- name: EDGE_CONNECT_OAUTH__ENDPOINT


value: <oauth.endpoint from edgeConnect.yaml>


- name: EDGE_CONNECT_OAUTH__RESOURCE


value: <oauth.resource from edgeConnect.yaml>


volumeMounts:


- name: secrets


mountPath: "/etc/edge_connect"


readOnly: true


- name: config


mountPath: "/edgeConnect.yaml"


subPath: "edgeConnect.yaml"


readOnly: true


volumes:


- name: secrets


secret:


secretName: edge-connect-oauth


items:


- key: oauth-client-id


path: oauth/client_id


- key: oauth-client-secret


path: oauth/client_secret


- name: config


secret:


secretName: edge-connect-config


items:


- key: edge-connect-config-file


path: edgeConnect.yaml
```

#### Настройка EdgeConnect в Kubernetes

Существует три способа настройки EdgeConnect в Kubernetes.
В приведенном выше примере используются все три для демонстрации.

##### Переменные окружения

Переменные окружения можно использовать для настройки большинства параметров EdgeConnect.
Подробнее см. таблицу в разделе [Описание полей](#edgeconnect-yaml-fields).

##### Смонтированные файлы

Файлы, смонтированные в папку `/etc/edge_connect`, будут сопоставлены со значениями конфигурации.
Путь файла в этой папке соответствует различным полям `.yaml`, например:

* `/etc/edge_connect/name` будет сопоставлен с полем `name` в `edgeConnect.yaml`, что эквивалентно установке переменной окружения `EDGE_CONNECT_NAME`.
* `/etc/edge_connect/oauth/client_id` будет сопоставлен с `oauth.client_id` в `edgeConnect.yaml`, что эквивалентно установке переменной окружения `EDGE_CONNECT_OAUTH__CLIENT_ID`.

Все значения конфигурации, которые можно задать через переменные окружения, как описано в [Описание полей](#edgeconnect-yaml-fields), также можно настроить с помощью смонтированных файлов.

##### Монтирование edgeConnect.yaml

Можно смонтировать `edgeConnect.yaml` непосредственно в контейнер EdgeConnect.
Обратите внимание, что некоторые настройки можно задать только таким образом, например `secrets` (см. [таблицу выше](#edgeconnect-yaml-secrets-fields)).

### Шаг 3: Применение развертывания

1. Перейдите в каталог с созданным файлом `deployment.yaml`.
2. Примените развертывание.

   ```
   kubectl apply -f ./deployment.yaml
   ```

### Шаг 4: Проверка соединения

Проверьте, что EdgeConnect успешно подключился к платформе.

1. Перейдите в **Settings** > **General** > **External Requests** > **EdgeConnect**.
2. Проверьте столбец **Availability**. Он должен отображать **online**.

   * Если он все еще offline, проверьте журналы контейнера на наличие сообщений об ошибках.
   * Если приложение показывает, что есть онлайн-экземпляры EdgeConnect, поздравляем! Вы безопасно подключили свою среду к платформе Dynatrace.

     Отныне любой HTTP-запрос, происходящий в рамках функции приложения, специальной функции или действия рабочего процесса, соответствующий шаблону хоста, будет прозрачно выполняться EdgeConnect вместо среды выполнения Dynatrace напрямую.

## Использование нескольких конфигураций и экземпляров EdgeConnect

Вы можете создать несколько конфигураций EdgeConnect в вашей среде, каждую со своей конфигурацией шаблонов хостов, как описано в разделе [Создание новой конфигурации EdgeConnect](#createconfiguration). Для каждой конфигурации EdgeConnect вы можете [развернуть](#deploy) несколько экземпляров для распределения нагрузки запросов EdgeConnect между несколькими экземплярами для балансировки нагрузки. В этом случае соответствующие запросы будут распределяться между экземплярами EdgeConnect, имеющими свободную емкость.

### Шаблоны хостов

Обратите внимание, что один шаблон хоста может использоваться только в одной конфигурации EdgeConnect, а не совместно между конфигурациями EdgeConnect. Например, при наличии конфигурации EdgeConnect с именем `staging`, содержащей `staging.myapp.org` в качестве шаблона хоста, вы не можете использовать тот же шаблон хоста в конфигурации EdgeConnect с именем `myapp`.

Однако вы можете использовать перекрывающийся шаблон хоста `*.myapp.org` в `myapp`. В этом случае среда выполнения Dynatrace JavaScript выберет конфигурацию EdgeConnect с наиболее конкретным шаблоном хоста для URL соответствующего запроса, поэтому запрос к `https://staging.myapp.org/test.html` всегда будет перенаправлен на экземпляры EdgeConnect конфигурации `staging`. Таким образом, выбор конфигурации EdgeConnect для данного URL является детерминированным.

#### Тестирование конфигураций

Чтобы заранее проверить, какой EdgeConnect будет обрабатывать данный URL на основе конфигураций EdgeConnect в вашей среде:

1. Перейдите в **Settings** > **General** > **External Requests** > **EdgeConnect**.
2. Выберите **URL verification**.

   * На вкладке **Find matching EdgeConnects** введите URL и нажмите **Match**, чтобы найти EdgeConnect для обработки вашего запроса.
   * На вкладке **Test HTTP request** введите HTTP-запрос и нажмите **Run test**, чтобы выполнить запрос в среде выполнения Dynatrace и проверить подключение к EdgeConnect.

### Сопоставление хостов

Описанное выше ограничение уникальности шаблона хоста для каждой конфигурации EdgeConnect создает проблему, если вы хотите администрировать различные конфигурации EdgeConnect, каждая из которых предназначена для доступа к различным внутренним службам с одинаковыми именами хостов, например к службам, работающим на общем имени хоста вроде `localhost`.

Другой распространенный пример -- доступ к API Kubernetes через `kubernetes.default.svc.cluster.local`, когда EdgeConnect развернут в кластере Kubernetes и предназначен для управления этим кластером через запросы из среды выполнения Dynatrace JavaScript. Вы можете иметь только одну конфигурацию EdgeConnect с шаблоном хоста `kubernetes.default.svc.cluster.local`; это невозможно, когда у вас есть несколько кластеров Kubernetes, которыми вы хотите управлять через EdgeConnect.

Решение этой проблемы -- использование *сопоставления хостов*, где вы настраиваете сопоставление от хоста, указанного в шаблонах хостов (который является уникальным для всех конфигураций, как упомянуто выше), и перезаписываете хост соответствующих запросов на нужное общее имя хоста перед передачей запроса контейнеру EdgeConnect.

#### Сопоставление хостов в настройках

Для настройки сопоставления хостов:

1. Перейдите в **Settings** > **General** > **External Requests** > **EdgeConnect**.
2. Выберите конфигурацию, которую хотите отредактировать.
3. В панели настроек выбранной конфигурации разверните **Host mappings**.
4. Определите одно или несколько правил (**From** и **To**) для сопоставления запросов, соответствующих одному из шаблонов хостов, с другим хостом. Любой запрос, хост которого совпадает с одним из хостов в **From**, будет перезаписан на хост в **To**.

##### Пример 1

В этом примере конфигурация EdgeConnect `service-a` определяет шаблон хоста `localhost-service-a` и настраивает сопоставление хоста `localhost-service-a` на `localhost`.

Запрос к `http://localhost-service-a/myservice` в среде выполнения Dynatrace JavaScript будет перенаправлен на эту конфигурацию EdgeConnect `service-a`. Однако хост запроса будет перезаписан, так что подключенный экземпляр EdgeConnect фактически выполнит запрос к `http://localhost/myservice`. Другая конфигурация EdgeConnect `service-b` может соответственно настроить шаблон хоста `localhost-service-b` и сопоставление хоста `localhost-service-b` на `localhost` для доступа к `http://localhost/otherservice` через запрос в среде выполнения Dynatrace JavaScript, направленный на `http://localhost-service-b/otherservice`.

##### Пример 2

В этом примере конфигурация EdgeConnect `k8-api-dev` определяет шаблон хоста `kubernetes-api-dev-cluster` и настраивает сопоставление хоста `kubernetes-api-dev-cluster` на `kubernetes.default.svc.cluster.local`.

Запрос к `https://kubernetes-api-dev-cluster/api/v1/pods` в среде выполнения Dynatrace JavaScript будет перенаправлен на экземпляры EdgeConnect с конфигурацией `k8-api-dev`. Однако хост запроса будет перезаписан, так что подключенный экземпляр EdgeConnect фактически выполнит запрос к `https://kubernetes.default.svc.cluster.local/api/v1/pods`.

Вы развертываете контейнеры EdgeConnect для этой конфигурации в кластере Kubernetes `dev` и можете надежно управлять этим кластером через HTTPS-запросы из среды выполнения Dynatrace. Одновременно у вас есть продуктовый кластер Kubernetes, которым вы хотите управлять аналогичным образом. Поэтому вы создаете другую конфигурацию EdgeConnect `k8-api-production` с шаблоном хоста `kubernetes-api-production-cluster` и сопоставлением хоста `kubernetes-api-production-cluster` на `kubernetes.default.svc.cluster.local` и развертываете ее экземпляры в продуктовом кластере Kubernetes. В результате вы можете обращаться к API Kubernetes нужного кластера, выполняя запрос к `https://kubernetes-api-dev-cluster/api/v1/pods` или `https://kubernetes-api-production-cluster/api/v1/pods`.

Подробнее об этом примере см. [Ручная настройка EdgeConnect для Kubernetes Connector](setup-on-k8s/guides/deployment-and-configuration/edgeconnect/kubernetes-automation/edge-connect-kubernetes-automation-manual-setup.md "Ручная настройка EdgeConnect для Kubernetes Connector для использования широкого спектра действий Kubernetes Connector в ваших рабочих процессах.").

## Системные требования

Для типичного развертывания EdgeConnect рекомендуется 1 ГБ памяти и 1 процессор. Требования к памяти могут варьироваться в зависимости от размера полезной нагрузки обрабатываемых запросов.
EdgeConnect требует следующей сетевой связности.

* HTTPS(443) к `https://sso.dynatrace.com/sso/oauth2/token`
* HTTPS(443) и безопасный WebSocket WSS(443) `https://<ваш ID среды>.apps.dynatrace.com`
  а также к любой целевой системе, к которой должны подключаться запросы EdgeConnect.

## Безопасность

Требования и рекомендации по конфигурации безопасности EdgeConnect основаны на принципе "минимальных привилегий".

### Что делает EdgeConnect

* EdgeConnect устанавливает безопасное WebSocket-соединение (WSS/443) с AppEngine и, таким образом, не требует никакого входящего соединения. Для этого EdgeConnect должен иметь возможность создать исходящее соединение WSS/443 к вашей среде Dynatrace.
* EdgeConnect работает в контексте среды и прозрачно выполняет все HTTP(S)-запросы в AppEngine, соответствующие определенным шаблонам хостов. Любой пользователь с соответствующими разрешениями для запуска функции приложения, специального JavaScript или рабочего процесса в среде может отправлять HTTP(S)-запросы на соответствующие хосты.

### Что следует сделать

* Ограничьте развертывание EdgeConnect сетью, необходимой для доступа только к предполагаемым системам.
* Определяйте конфигурацию шаблонов хостов EdgeConnect как можно более конкретно, чтобы пересылались только необходимые HTTP(S)-запросы.
* Используйте локальную конфигурацию EdgeConnect для ограничения доступных хостов ([см. необязательное свойство `restrict_hosts_to`](#config) в таблице выше). Определенные шаблоны хостов никогда не могут превышать локальное ограничение хостов. Одно только локальное ограничение хостов не приводит к пересылке HTTP(S)-запросов.

## Ограничения

Для обеспечения хорошей производительности EdgeConnect запросы и ответы EdgeConnect имеют следующие ограничения:

### Тайм-аут запроса

Для каждого запроса, выполняемого через EdgeConnect, установлен тайм-аут в 120 секунд. Обратите внимание, что это соответствует максимальному времени выполнения функций. Если функция завершается по тайм-ауту, все исходящие запросы будут автоматически отменены.

### Ограничение размера полезной нагрузки

Тело запроса или ответа, выполняемого через EdgeConnect, не может превышать 6 МБ. При превышении этого ограничения соответствующий запрос завершится с HTTP-кодом ошибки 400.

### Ограничение параллельных запросов

Существует ограничение в 20 параллельных запросов, которые один контейнер EdgeConnect может обрабатывать одновременно. Последующие запросы, скорее всего, завершатся по тайм-ауту. В качестве обходного решения разверните несколько контейнеров EdgeConnect.