---
title: Network configurations
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations
scraped: 2026-03-05T21:38:19.578189
---

# Сетевые конфигурации

# Сетевые конфигурации

* Latest Dynatrace
* 4 мин. чтения
* Опубликовано 25 марта 2024 г.

Настройка Dynatrace в средах с сетевыми ограничениями с помощью сетевых конфигураций, параметров прокси и исключений URL.

Сетевые зоны

Подробности о настройке и управлении сетевыми зонами, начальной конфигурации конечных точек и расширенных настройках в ограниченных средах см. в [Использование сетевых зон в Kubernetes](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones "Настройка и использование сетевых зон в средах Kubernetes с Dynatrace Operator.").

## Настройка прокси

Для мониторинга платформы Kubernetes с Dynatrace вам может потребоваться настроить прокси, который обслуживает все исходящие соединения для компонентов Dynatrace Operator (таких как `csi-driver` и `operator`), OneAgent и ActiveGate.

В зависимости от конфигурации вашего прокси, особенно в части учётных данных, существует два варианта настройки прокси в DynaKube:

Без учётных данных прокси

С учётными данными прокси

HTTPS-прокси поддерживаются для ActiveGate начиная с версии 1.289.
HTTPS-прокси поддерживаются для OneAgent начиная с версии 1.311.

Для прокси без требований к учётным данным укажите URL вашего прокси в поле `value`:

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

Для прокси, требующих учётных данных.

1. Создайте секрет Kubernetes, содержащий зашифрованный URL вашего прокси, включая учётные данные.

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret generic my-proxy-secret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
   ```

   ```
   oc -n dynatrace create secret generic my-proxy-secret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
   ```

   Правила для пароля прокси

   Убедитесь, что пароль прокси соответствует следующим критериям:

   | Требования | Соответствующие символы |
   | --- | --- |
   | Допустимые символы | [A-Za-z0-9] ! " # $ ( ) \* - . / : ; < > ? @ [ ] ^ \_ { | } |
   | Недопустимые символы | пробел ' ` , & = + % \ |

   Пароль в пользовательском ресурсе или секрете прокси должен быть закодирован в URL-формате. Например, `password!"#$()*-./:;<>?@[]^_{|}~` становится `password!%22%23%24()*-.%2F%3A%3B%3C%3E%3F%40%5B%5D%5E_%7B%7C%7D~`.
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

Соединение между OneAgent и модулями кода Dynatrace с ActiveGate всегда будет обходить прокси, обеспечивая прямую связь для этих компонентов.

Если вам необходимо обойти прокси по другим причинам, см. следующий раздел.

### Исключение выбранных URL из конфигурации прокси

Чтобы задать список URL, исключаемых из конфигурации прокси, добавьте следующую аннотацию к пользовательскому ресурсу DynaKube.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/no-proxy: "some.url.com,other.url.com"
```

Dynatrace Operator исключает перечисленные URL из настроек прокси. Это исключение применяется только к Dynatrace Operator и драйверу CSI. Оно не влияет на настройки прокси для других компонентов, управляемых Dynatrace Operator, таких как OneAgent или ActiveGate.

## Добавление доверенных сертификатов CA

### ActiveGate, OneAgent и компоненты Dynatrace Operator

Для добавления доверенных сертификатов CA в ActiveGate, OneAgent и/или Dynatrace Operator сертификаты должны быть предоставлены через ConfigMap Kubernetes, на который ссылается конфигурация вашего DynaKube.

1. Создайте ConfigMap (замените `<ca-certificates>` на сертификаты CA, которым нужно доверять).

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
3. В вашем DynaKube укажите ссылку на ConfigMap в поле `trustedCAs`.

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

### Использование `skipCertCheck` для обхода проверки сертификатов

Чтобы игнорировать проверку сертификатов для компонентов Dynatrace Operator (`operator` и `csi-driver`), установите `skipCertCheck` в конфигурации вашего DynaKube. Этот параметр следует использовать только в случае, если пользовательский центр сертификации неизвестен или не может быть предоставлен Dynatrace Operator через поле `trustedCAs`.

В Dynatrace Operator версии 1.0.0 и ранее параметр `skipCertCheck` не применялся в процессе загрузки образов.

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

## Настройка TLS-сертификата сервера для ActiveGate

По умолчанию ActiveGate использует самоподписанный сертификат, который может быть заменён самостоятельно управляемым сертификатом, как описано в [Пользовательский SSL-сертификат для ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на вашем ActiveGate.").

Чтобы настроить TLS-сертификат сервера для ActiveGate:

1. Создайте [непрозрачный секрет Kubernetes (Opaque)](https://dt-url.net/zm03qza), содержащий сертификат(ы) ActiveGate и закрытый ключ ActiveGate.

   ```
   kubectl -n dynatrace create secret generic mytlssecret --from-file=server.p12=<myag.p12> --from-file=server.crt=<myag.crt> --from-literal=password=<mypassword>
   ```

   Где:

   * `server.crt` — Dynatrace Operator распространяет сертификат(ы) ActiveGate из файла к OneAgent.
   * `server.p12` — сертификат(ы) ActiveGate и закрытый ключ ActiveGate, ActiveGate читает файл и настраивает себя для использования предоставленного закрытого ключа и сертификатов.
   * `password` — ActiveGate читает его и использует для расшифровки файла `server.p12`.

   Файлы `server.p12` и `server.crt` должны содержать одинаковые сертификат(ы).
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
