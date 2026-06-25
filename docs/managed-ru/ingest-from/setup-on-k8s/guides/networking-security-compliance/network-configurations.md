---
title: Сетевые конфигурации
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations
scraped: 2026-05-12T11:50:11.772217
---

# Сетевые конфигурации

# Сетевые конфигурации

* Чтение: 4 мин
* Опубликовано 25 марта 2024 г.

Настройте Dynatrace в окружениях с сетевыми ограничениями с помощью сетевых конфигураций, настроек proxy и исключений URL.

Network zones

Подробнее о настройке network zones и управлении ими, первоначальной настройке конечных точек и расширенных конфигурациях в окружениях с ограничениями см. [Использование network zones в Kubernetes](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones "Настройка и использование network zones в окружениях Kubernetes с помощью Dynatrace Operator.").

## Настройка proxy

Для мониторинга платформы Kubernetes с Dynatrace вам может понадобиться настроить proxy, который обеспечивает все исходящие соединения для компонентов Dynatrace Operator (таких как `csi-driver` и `operator`), OneAgent и ActiveGate.

В зависимости от конфигурации proxy, особенно в части учётных данных, существует два варианта настройки proxy в DynaKube:

Без учётных данных proxy

С учётными данными proxy

HTTPS-proxy поддерживаются для ActiveGate начиная с версии 1.289.
HTTPS-proxy поддерживаются для OneAgent начиная с версии 1.311.

Для proxy, не требующих учётных данных, укажите URL вашего proxy в поле `value`:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



proxy:



value: http://<my-super-proxy>
```

Для proxy, требующих учётных данных.

1. Создайте секрет Kubernetes, содержащий зашифрованный URL вашего proxy, включая учётные данные.

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret generic my-proxy-secret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
   ```

   ```
   oc -n dynatrace create secret generic my-proxy-secret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
   ```

   Правила для пароля proxy

   Убедитесь, что пароль proxy соответствует следующим критериям:

   | Требования | Соответствующие символы |
   | --- | --- |
   | Допустимые символы | [A-Za-z0-9] ! " # $ ( ) \* - . / : ; < > ? @ [ ] ^ \_ { | } |
   | Недопустимые символы | пробел ' ` , & = + % \ |

   Пароль в пользовательском ресурсе или секрете proxy должен быть закодирован в формате URL. Например, `password!"#$()*-./:;<>?@[]^_{|}~` превращается в `password!%22%23%24()*-.%2F%3A%3B%3C%3E%3F%40%5B%5D%5E_%7B%7C%7D~`.
2. Укажите имя секрета в разделе `valueFrom`.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



   proxy:



   valueFrom: my-proxy-secret
   ```

Dynatrace Operator версии 1.0.0+

Соединение между OneAgent, кодовыми модулями Dynatrace и ActiveGate всегда обходит proxy, обеспечивая прямую связь для этих компонентов.

Если вам нужно обойти proxy по другим причинам, см. следующий раздел.

### Исключение выбранных URL из конфигурации proxy

Чтобы задать список URL, исключаемых из конфигурации proxy, добавьте следующую аннотацию в пользовательский ресурс DynaKube.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/no-proxy: "some.url.com,other.url.com"
```

После этого Dynatrace Operator исключает перечисленные URL из настроек proxy. Это исключение применяется именно к Dynatrace Operator и CSI driver. Оно не влияет на настройки proxy для других компонентов, управляемых Dynatrace Operator, таких как OneAgent или ActiveGate.

## Добавление доверенных CA-сертификатов

### Компоненты ActiveGate, OneAgent и Dynatrace Operator

Чтобы добавить доверенные CA-сертификаты в ActiveGate, OneAgent и/или Dynatrace Operator, сертификаты необходимо предоставить через ConfigMap Kubernetes, на который ссылается ваша конфигурация DynaKube.

1. Создайте ConfigMap (замените `<ca-certificates>` на CA-сертификаты, которым нужно доверять).

   ```
   apiVersion: v1



   kind: ConfigMap



   metadata:



   name: mycaconfigmap



   namespace: dynatrace



   data:



   certs: |



   <ca-certificates>
   ```

   Например:

   ```
   data:



   certs: |



   -----BEGIN CERTIFICATE-----



   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



   -----END CERTIFICATE-----
   ```
2. Примените ConfigMap к вашему кластеру.

   ```
   kubectl apply -f my-ca-configmap.yaml
   ```
3. В вашем DynaKube сошлитесь на ConfigMap в поле `trustedCAs`.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



   trustedCAs: mycaconfigmap
   ```
4. Примените конфигурацию DynaKube к вашему кластеру.

   ```
   kubectl apply -f dynakube-config.yaml
   ```

### Использование `skipCertCheck` для обхода проверки сертификата

Чтобы игнорировать проверку сертификата для компонентов Dynatrace Operator (`operator` и `csi-driver`), задайте `skipCertCheck` в вашей конфигурации DynaKube. Эту настройку следует использовать только в том случае, если пользовательский удостоверяющий центр неизвестен или не может быть предоставлен Dynatrace Operator через поле `trustedCAs`.

В Dynatrace Operator версии 1.0.0 и более ранних настройка `skipCertCheck` не применялась в процессе загрузки образа.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



skipCertCheck: true
```

## Настройка серверного TLS-сертификата для ActiveGate

По умолчанию ActiveGate использует самоподписанный сертификат, который можно заменить самостоятельно управляемым сертификатом, как описано в разделе [Пользовательский SSL-сертификат для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на вашем ActiveGate.").

Чтобы настроить серверный TLS-сертификат для ActiveGate:

1. Создайте [секрет Kubernetes типа Opaque](https://dt-url.net/zm03qza), содержащий сертификат(ы) ActiveGate и закрытый ключ ActiveGate.

   ```
   kubectl -n dynatrace create secret generic mytlssecret --from-file=server.p12=<myag.p12> --from-file=server.crt=<myag.crt> --from-literal=password=<mypassword>
   ```

   Где:

   * `server.crt`: Dynatrace Operator распространяет сертификат(ы) ActiveGate из файла на OneAgent.
   * `server.p12`: сертификат(ы) ActiveGate и закрытый ключ ActiveGate; ActiveGate читает файл и настраивается на использование предоставленного закрытого ключа и сертификатов.
   * `password`: ActiveGate читает его и использует для расшифровки файла `server.p12`.

   Файлы `server.12` и `server.crt` должны содержать одни и те же сертификат(ы).
2. Укажите имя секрета через поле `tlsSecretName`.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   ...



   activeGate:



   tlsSecretName: <mytlssecret>



   ...
   ```