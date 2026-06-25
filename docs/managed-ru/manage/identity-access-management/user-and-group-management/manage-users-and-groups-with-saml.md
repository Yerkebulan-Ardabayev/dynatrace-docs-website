---
title: Управление пользователями и группами с помощью SAML в Dynatrace Managed
source: https://docs.dynatrace.com/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-saml
scraped: 2026-05-12T11:24:28.009270
---

# Управление пользователями и группами с помощью SAML в Dynatrace Managed

# Управление пользователями и группами с помощью SAML в Dynatrace Managed

* Published Jul 19, 2017

Dynatrace Managed поддерживает интеграцию с SAML 2.0 в качестве SSO IdP (провайдера идентификации единого входа) для управления пользователями и группами. SAML может использовать привязки `HTTP POST` (предпочтительно) или `HTTP Redirect`. При наличии обоих используется `HTTP POST`.

## Настройка интеграции SAML 2.0

Эта процедура требует настройки в Dynatrace Managed и на вашем IdP.

### В Dynatrace Managed

1. В меню Cluster Management Console выберите **User authentication > Single sign-on settings**.

   Пример страницы `Single sign-on settings`

   ![Страница настройки SAML](https://dt-cdn.net/images/image-2293-3e9c99837a.png "Страница настройки SAML")

2. В поле **Select single sign-on technology** выберите `SAML 2.0`.
3. В поле **Select login page** выберите варианты входа, которые нужно предложить пользователям:

   * **Standard + SSO** отображает стандартную страницу входа Dynatrace, где пользователь может войти с помощью локальной учётной записи (настраиваемой через **User authentication > User accounts**) или перейти по ссылке **Log in using SSO** для аутентификации через SSO.
   * **SSO** пропускает страницу входа Dynatrace, исключая вход через локальную учётную запись, и перенаправляет на страницу входа IdP только для SSO-аутентификации.
4. Нажмите **Download SP metadata**, чтобы загрузить (в файл `sp.xml`) метаданные SAML, которые необходимо предоставить вашему SP.  
   Поле **XML metadata of a SAML 2.0 Service Provider** отображает эти метаданные.

### На сервере провайдера идентификации (IdP)

Подробнее о выполнении этих шагов см. в документации вашего IdP.

На сервере IdP

1. Используйте файл метаданных `sp.xml`, загруженный ранее, для настройки Dynatrace Managed в качестве поставщика услуг (SP).
2. Загрузите готовый файл метаданных конфигурации с сервера IdP.

### В Dynatrace Managed

Вернувшись в Cluster Management Console Dynatrace Managed

1. Вернитесь на страницу **Single sign-on settings** (**User authentication > Single sign-on settings**), чтобы продолжить с того места, где остановились.
2. Нажмите кнопку **Select file** и загрузите файл метаданных конфигурации IdP в Dynatrace Managed.  
   Поле **XML metadata of a SAML 2.0 Identity Provider** отображает эти метаданные.
3. В разделе **User attributes based on SAML 2.0 response attributes** введите атрибуты пользователя.

   * **First name attribute**
   * **Last name attribute**
   * **Email attribute**

## Настройка назначения в группы

Каждый пользователь Dynatrace Managed должен быть назначен хотя бы в одну группу пользователей, связанную хотя бы с одним [окружением мониторинга](/managed/discover-dynatrace/get-started/monitoring-environment "Понять и научиться работать с окружениями мониторинга."). Без такого сопоставления пользователь не сможет войти в Dynatrace Managed и получит сообщение об ошибке о том, что окружение не найдено.

Переключатель **Assign users to groups based on SAML 2.0 response attribute** определяет способ управления назначением пользователей в группы:

* Вручную: установите переключатель в положение **off**, если назначения пользователей в группы выполняются вручную из Dynatrace Managed. В этом случае Dynatrace Managed игнорирует список групп, отправленный в ответе аутентификации IdP.
* Автоматически: включите переключатель и введите имя группы в поле **User group attribute**, если назначение пользователей в группы должно выполняться автоматически. В этом случае любые назначения, сделанные в Dynatrace Managed, перезаписываются списком групп из ответа аутентификации IdP, например:

  ```
  <Attribute Name="gr">



  <AttributeValue>Admins</AttributeValue>



  <AttributeValue>Users</AttributeValue>



  </Attribute>
  ```

  в результате которого пользователь назначается в группы `Admins` и `Users`.

  + Если значение атрибута группы пользователей в SAML-ответе содержит запятые, Dynatrace воспринимает его как список групп, разделённых запятыми, и назначает пользователя в каждую из них. Например:

    ```
    <Attribute Name="gr">



    <AttributeValue>Admins,Users</AttributeValue>



    </Attribute>
    ```

    назначит пользователя в группы `Admins` и `Users`.
  + Убедитесь, что имена групп точно совпадают с именами существующих групп пользователей Dynatrace (с учётом регистра, без лишних пробелов). Например, `Admins` и `admins` — это две разные группы.

## Обновление сертификата подписи SAML

Для загрузки нового сертификата подписи SAML выполните PUT-запрос через Cluster Management API.

1. В Cluster Management Console получите токен `ServiceProviderAPI`.

   Как получить токен

   1. Выберите **Settings > API tokens**.
   2. Нажмите **Generate token**.
   3. Введите имя токена, включите **Service Provider API** и нажмите **Save**.
   4. В списке токенов разверните только что созданный токен и нажмите **Copy**, чтобы скопировать его значение.
2. Откройте **User menu** в правом верхнем углу и выберите **Cluster Management API**.
3. Отправьте токен.

   Как отправить токен

   1. Нажмите **Authorize**.
   2. Вставьте значение токена в поле ввода.
   3. Нажмите **Authorize**.
   4. Нажмите **Close**.

   Теперь вы авторизованы для выполнения необходимого API-запроса.
4. Разверните раздел **SSO configuration** и нажмите **PUT**.
5. Нажмите **Try it out**.  
   В разделе **Description** отображается ожидаемый формат тела PUT-запроса.

   ```
   {



   "privateKeyEncoded": "string",



   "publicKeyCertificateEncoded": "string"



   }
   ```
6. Вставьте содержимое приватного ключа RSA и сертификата вместо соответствующих заполнителей `privateKeyEncoded` и `publicKeyCertificateEncoded` (`string`). Обязательно включайте полные теги `BEGIN` и `END` каждого из них. В этом примере ключ и сертификат сокращены:

   ```
   {



   "privateKeyEncoded": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAp8RXe0PIuDwj1ZbYrShXRxjiFnq8xmLWZlWIYkScX/1KC69M\n...\nPM3kel4na+AGibenqRs7PA6rqFeXDg193pepzWqvqmJ98W8YYecZ\n-----END RSA PRIVATE KEY-----",



   "publicKeyCertificateEncoded": "-----BEGIN CERTIFICATE-----\nMIICzTCCAbWgAwIBAgIRAIpaHcbUOpvhKf6exsxJjVowDQYJKoZIhvcNAQELBQAw\n...\nuw==\n-----END CERTIFICATE-----"



   }
   ```
7. Нажмите **Execute** для отправки запроса.

   Коды ответов

   * `200` — обновление сертификата выполнено успешно.
   * `400` — некорректные входные данные. Проверьте, что вставлены полный ключ и сертификат, включая теги `BEGIN` и `END`, в тело запроса.
   * `510` — сбой операции. Проверьте логи сервера для получения подробностей.

## Настройка ADFS

При интеграции Dynatrace Managed с Active Directory Federation Services (ADFS) выполните следующие шаги на стороне ADFS, а затем в Dynatrace Managed.

### Настройка на стороне ADFS

1. Используйте **Add Relying Party Trust Wizard** для добавления нового доверия проверяющей стороны с использованием метаданных конфигурации Dynatrace SP.

   Пример мастера Add Relying Party Trust Wizard

   ![ADFS SAML provider](https://dt-cdn.net/images/adfs1-896-44cc5748c9.jpg "ADFS SAML provider")

2. На вкладке **Advanced** установите **Secure hash algorithm** в значение `SHA-1` или `SHA-256`.

   Пример вкладки Advanced

   ![ADFS SAML provider](https://dt-cdn.net/images/adfs2-495-a9ece8bd6b.jpg "ADFS SAML provider")

3. Добавьте политику выдачи утверждений к добавленному доверию проверяющей стороны.

   Пример Edit Claim Issuance Policy

   ![ADFS SAML provider](https://dt-cdn.net/images/adfs3-300-1a619dccbe.png "ADFS SAML provider")

4. Определите правило для отправки атрибутов LDAP как утверждений.

   Пример правила: отправка атрибутов LDAP как утверждений

   ![ADFS SAML provider](https://dt-cdn.net/images/adfs4-683-8d48924f8c.jpg "ADFS SAML provider")

5. Определите правила для преобразования атрибутов LDAP в `Name ID` (создайте правило, подходящее для ваших нужд).

   * Пример правила для преобразования атрибута LDAP `login` в `Name ID`.

     Пример правила: атрибут LDAP `login` → `Name ID`

     ![ADFS SAML provider](https://dt-cdn.net/images/adfs5-685-877105f0f1.jpg "ADFS SAML provider")

   * Пример правила для преобразования атрибута LDAP `email` в `Name ID`.

     Пример правила: атрибут LDAP `email` → `Name ID`

     ![ADFS SAML provider](https://dt-cdn.net/images/adfs6-680-e9f233c985.jpg "ADFS SAML provider")

### Настройка на стороне Dynatrace Managed

На странице **Single sign-on settings** Dynatrace Managed установите соответствующее значение **User group attribute**.

![ADFS SAML provider](https://dt-cdn.net/images/adfs7-937-6490c2d4eb.jpg "ADFS SAML provider")

## Часто задаваемые вопросы

Какой формат NameIdFormat использовать?

`NameId` — это логин на стороне Dynatrace Managed. Dynatrace Managed принимает все форматы, поэтому можно выбрать тот, который лучше соответствует вашим политикам.

Рекомендуемый `NameIdFormat`:  
`urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`

Почему при выходе из Dynatrace Managed я выхожу из всех сервисов?

При выходе запускается глобальный выход из системы, включая IdP, который затем каскадно применяется к другим сервисам. В противном случае вы бы вышли из Dynatrace Managed, но для повторной аутентификации было бы достаточно щёлкнуть ссылку **Log in using SSO** или ввести URL веб-интерфейса Dynatrace Managed в браузере (при настройке страницы входа в режиме SSO).

Если необходимо отключить глобальный выход (что нежелательно с точки зрения безопасности), отредактируйте метаданные, удалите все теги `SingleLogoutService` и загрузите обновлённые метаданные.

Могут ли метаданные содержать несколько сертификатов подписи?

Да, метаданные клиентского IdP могут содержать несколько сертификатов подписи. Dynatrace Managed проверяет, что сообщения SAML от клиентского IdP подписаны одним из них.

Добавляются ли пользователи SAML автоматически в Dynatrace Managed?

Да, пользователи добавляются после успешной аутентификации.

Что делать, если правила Content Security Policy нарушаются при входе или выходе?

Это может происходить, когда настроенный SSO IdP перенаправляет POST-запросы входа или выхода на другие хосты.

Для решения проблемы перейдите в **User authentication** > **Single sign-on settings** и добавьте URL-адреса перенаправления в раздел **SSO IdP redirect URLs**.