---
title: Настройка SSL-сертификата для Cluster ActiveGate
source: https://docs.dynatrace.com/managed/managed-cluster/installation/ssl-certificate-cluster-activegate
scraped: 2026-05-12T11:53:35.687443
---

# Настройка SSL-сертификата для Cluster ActiveGate

# Настройка SSL-сертификата для Cluster ActiveGate

* How-to guide
* 2-min read
* Updated on May 08, 2026

Всё взаимодействие с Cluster ActiveGate шифруется через SSL. Для внешней связи Cluster ActiveGate требует общедоступный IP-адрес и доменное имя с действующим SSL-сертификатом. Этот домен должен отличаться от домена веб-интерфейса.

Начиная с **17 апреля 2025 года** китайские регуляторные требования обязывают все общедоступные сервисы, использующие домен `dynatrace-managed.com`, иметь сертификацию ICP (Internet Content Provider). Поскольку Dynatrace не имеет сертификата ICP из-за отсутствия юридического лица в Китае, домены Dynatrace были заблокированы местными сетевыми провайдерами.

Для сохранения возможностей мониторинга используйте один из следующих вариантов:

* Используйте внутренние DNS или IP-адреса для конечных точек Cluster ActiveGate.
* Избегайте предоставления доступа к веб-интерфейсу Dynatrace или конечным точкам из публичных китайских сетей.

## Варианты управления сертификатами

После установки Cluster ActiveGate использует самоподписанный сертификат, сгенерированный Dynatrace. Доступны два варианта:

* **Предоставить управление доменом и сертификатом Dynatrace** — каждый Cluster ActiveGate с общедоступным IP-адресом получает выделенный поддомен `dynatrace-managed.com` с доверенным SSL-сертификатом, подписанным CA.
* **Использовать собственный домен и сертификат** — отключите автоматическое управление и загрузите собственный сертификат через Cluster Management Console или [Cluster REST API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status "Learn how to use the Dynatrace API to store cluster SSL certificate.").

Не загружайте сертификаты непосредственно на устройство

Не настраивайте SSL-сертификаты непосредственно на устройстве Cluster ActiveGate. Любой сертификат, загруженный таким образом, будет перезаписан автоматическим управлением Dynatrace.

Всегда загружайте сертификат через Cluster Management Console или [Cluster REST API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status "Learn how to use the Dynatrace API to store cluster SSL certificate.").

## Предоставление управления доменом и сертификатом Dynatrace

1. Войдите в **Cluster Management Console**.
2. Перейдите в **Deployment Status > ActiveGates**, выберите ActiveGate и укажите общедоступный IP-адрес.
3. Для узла Managed Cluster перейдите в **Settings > Public endpoints** и включите **Enable management of domain name and SSL certificates**.

## Использование собственного домена и сертификата

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Проверка требований**](/managed/managed-cluster/installation/ssl-certificate-cluster-activegate#review-requirements "Configure a custom SSL certificate on a Cluster ActiveGate instead of relying on Dynatrace-managed certificate automation.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Отключение автоматического управления сертификатами**](/managed/managed-cluster/installation/ssl-certificate-cluster-activegate#disable-auto-cert "Configure a custom SSL certificate on a Cluster ActiveGate instead of relying on Dynatrace-managed certificate automation.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Загрузка сертификата**](/managed/managed-cluster/installation/ssl-certificate-cluster-activegate#upload-certificate "Configure a custom SSL certificate on a Cluster ActiveGate instead of relying on Dynatrace-managed certificate automation.")

### Шаг 1. Проверка требований

Вам потребуются файлы SSL-сертификата и ключа, полученные от вашего центра сертификации (CA):

* Сертификат сервера (`.cer` или `.cert`)
* Корневые и промежуточные сертификаты (`.cer` или `.cert`)
* Закрытый ключ (`.pem`)

Зашифрованные закрытые ключи

Зашифрованные закрытые ключи не поддерживаются. Для расшифровки SSL-закрытого ключа выполните:

`openssl rsa -in encrypted.ssl.key -out decrypted.ssl.key`

* `encrypted.ssl.key` — ваш зашифрованный файл SSL-закрытого ключа.
* `decrypted.ssl.key` — выходной файл для расшифрованного ключа.

Команда запрашивает пароль и сохраняет расшифрованный ключ.

### Шаг 2. Отключение автоматического управления сертификатами

Для отключения автоматического управления сертификатами:

1. Войдите в **Cluster Management Console**.
2. Выберите узел Managed Cluster и перейдите в **Settings > Public endpoints**.
3. Отключите **Enable management of domain name and SSL certificates**.
4. Введите своё доменное имя в поле **Cluster ActiveGate URL**.

### Шаг 3. Загрузка сертификата

Загрузите или вставьте свой сертификат через Cluster Management Console или [Cluster REST API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status "Learn how to use the Dynatrace API to store cluster SSL certificate."). Для использования Cluster Management Console:

1. Войдите в **Cluster Management Console**.
2. На странице **Deployment Status** разверните ActiveGate, который необходимо настроить, и выберите **Configure**.
3. Выберите **Edit SSL certificate**.
4. Вставьте или загрузите файлы ключей, полученные от вашего CA.

   * **Private key**: ваш закрытый ключ.
   * **Public key certificate**: сертификат вашего сервера.
   * **Certificate chain**: ваши корневые и промежуточные сертификаты.

   Все ключи и сертификаты должны быть в формате PEM с полными заголовками `BEGIN` и `END`.

   **Формат ключа**:

   ```
   -----BEGIN PRIVATE KEY-----



   (Private Key)



   -----END PRIVATE KEY-----
   ```

   **Формат сертификата**:

   ```
   -----BEGIN CERTIFICATE-----



   (SSL Certificate)



   -----END CERTIFICATE-----
   ```
5. Выберите **Save**.

Ошибка несоответствия имени

Ваш сертификат привязан к конкретному имени хоста. Чтобы избежать ошибки несоответствия имени, убедитесь, что общее имя (CN) в сертификате совпадает с адресом, указанным в поле **Cluster ActiveGate URL**.