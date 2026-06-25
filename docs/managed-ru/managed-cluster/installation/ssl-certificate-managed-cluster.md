---
title: Настройка SSL-сертификата для Managed Cluster
source: https://docs.dynatrace.com/managed/managed-cluster/installation/ssl-certificate-managed-cluster
scraped: 2026-05-12T11:25:06.214839
---

# Настройка SSL-сертификата для Managed Cluster

# Настройка SSL-сертификата для Managed Cluster

* How-to guide
* 3-min read
* Updated on May 08, 2026

По умолчанию Dynatrace управляет SSL за вас — каждый Managed Cluster получает выделенный поддомен `dynatrace-managed.com` с доверенным SSL-сертификатом. Чтобы использовать собственный сертификат, следуйте приведённым ниже шагам.

Начиная с **17 апреля 2025 года** китайские регуляторные требования обязывают все общедоступные сервисы, использующие домен `dynatrace-managed.com`, иметь сертификацию ICP (Internet Content Provider). Поскольку Dynatrace не имеет сертификата ICP из-за отсутствия юридического лица в Китае, затронутые домены были заблокированы местными сетевыми провайдерами.

Для сохранения возможностей мониторинга Dynatrace рекомендует следующее:

* Используйте внутренние DNS или IP-адреса для конечных точек Cluster ActiveGate.
* Избегайте предоставления доступа к веб-интерфейсу Dynatrace или конечным точкам из публичных китайских сетей.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Проверка требований**](/managed/managed-cluster/installation/ssl-certificate-managed-cluster#review-requirements "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Отключение автоматического управления сертификатами**](/managed/managed-cluster/installation/ssl-certificate-managed-cluster#disable-automanagement "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Загрузка сертификата**](/managed/managed-cluster/installation/ssl-certificate-managed-cluster#upload-certificate "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")

## Шаг 1. Проверка требований

Вам потребуются файлы SSL-сертификата и ключа, полученные от вашего центра сертификации (CA):

* Сертификат сервера (`.cer` или `.cert`)
* Корневые и промежуточные сертификаты (`.cer` или `.cert`)
* Закрытый ключ (`.pem`)

Зашифрованные закрытые ключи

Зашифрованные закрытые ключи не поддерживаются. Для расшифровки SSL-закрытого ключа выполните:

`openssl rsa -in encrypted.ssl.key -out decrypted.ssl.key`

* `encrypted.ssl.key`: ваш зашифрованный файл SSL-закрытого ключа.
* `decrypted.ssl.key`: выходной файл для расшифрованного ключа.

Команда запрашивает пароль и сохраняет расшифрованный ключ.

## Шаг 2. Отключение автоматического управления сертификатами

Для отключения автоматического управления сертификатами:

1. Войдите в **Cluster Management Console**.
2. Перейдите в **Settings > Preferences** и отключите **Manage domain name and SSL certificates**.

Без автоматического управления сертификатами Dynatrace переходит на самоподписанный сертификат. Самоподписанные сертификаты по умолчанию не являются доверенными для браузеров — при первом доступе появится предупреждение системы безопасности. Примите исключение в настройках безопасности браузера, затем установите доверенный сертификат, как описано в следующем шаге.

## Шаг 3. Загрузка сертификата

1. Войдите в **Cluster Management Console**.
2. На странице **Home** выберите узел Managed Cluster, которому требуется новый сертификат.
3. На странице **Node Details** выберите **Edit SSL certificate**.

   Пример страницы редактирования SSL-сертификатов

   ![Onprem ssl certificates](https://dt-cdn.net/images/onprem-ssl-certificates-1329-e9535c4e34.png)

   Onprem ssl certificates
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
5. Выберите **Save** для загрузки сертификатов.

Ошибка несоответствия имени

Ваш сертификат привязан к конкретному имени хоста. Чтобы избежать ошибки несоответствия имени, убедитесь, что общее имя (доменное имя) в сертификате совпадает с адресом, отображаемым в адресной строке браузера.