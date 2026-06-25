---
title: Управление пользователями и группами с помощью OpenID в Dynatrace Managed
source: https://docs.dynatrace.com/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-openid
scraped: 2026-05-12T11:24:25.249468
---

# Управление пользователями и группами с помощью OpenID в Dynatrace Managed

# Управление пользователями и группами с помощью OpenID в Dynatrace Managed

* Published Jul 17, 2018

Dynatrace Managed поддерживает интеграцию с [OpenID](https://openid.net/what-is-openid/) в качестве SSO IdP (провайдера идентификации единого входа) для управления пользователями и группами. Поддерживаются стандартные утверждения (email, profile, address), определённые в [спецификации OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims).

## Настройка redirect\_uri

`redirect_uri`, используемый для аутентификации, устанавливается следующим образом:

* `https://{dynatrace-server}/`  
  при открытии Cluster Management Console.
  Как проверить значение 'Dynatrace Web UI URL'

  1. Выберите значок пользователя в правом верхнем углу и нажмите **Cluster Management**.
  2. Перейдите в **Settings > Public endpoints** и просмотрите **Dynatrace Web UI URL**.
* `https://{dynatrace-server}/e/{environment-uuid}`  
  при открытии окружения.

Необходимо настроить эти URI в клиенте вашего OpenID-провайдера:

* Настройте один URI для Cluster Management Console.
* Настройте один URI для каждого окружения или используйте подстановочный знак (`https://{dynatrace-server}/e/*`) для сопоставления со всеми URI окружений.

## Настройка интеграции OpenID

1. В [меню пользователя](/managed/discover-dynatrace/get-started/dynatrace-ui#user "Навигация по платформе Dynatrace Managed") перейдите в **Cluster Management**.
2. Выберите **User authentication** > **Single sign-on settings**.
3. В поле **Select single sign-on technology** выберите **OpenID Connect**.
4. В поле **Select login page** выберите варианты входа, которые нужно предложить пользователям:

   * **Standard + SSO** отображает стандартную страницу входа Dynatrace, где пользователь может войти с помощью локальной учётной записи (настраиваемой через **User authentication > User accounts**) или перейти по ссылке **Log in using SSO** для аутентификации через SSO.
   * **SSO** пропускает страницу входа Dynatrace, исключая вход через локальную учётную запись, и перенаправляет на страницу входа IdP только для SSO-аутентификации.
5. Введите **Client ID** и **Client Secret** клиента из IdP, который будет использоваться для аутентификации.
6. Для подключения к IdP через интернет-прокси выберите **Use internet proxy for connection to IdP**.
7. Для проверки подписи токена ID и UserInfo выберите **Validate signature**.
8. В поле **Server discovery endpoint** введите URL конфигурации OpenID, предоставленный IdP, и нажмите **Import Configuration**.  
   При успешном импорте становится доступна кнопка **Save changes**. Сохраните конфигурацию.

## Настройка назначения в группы

Каждый пользователь Dynatrace Managed должен быть назначен хотя бы в одну группу пользователей, связанную хотя бы с одним [окружением мониторинга](/managed/discover-dynatrace/get-started/monitoring-environment "Понять и научиться работать с окружениями мониторинга."). Без такого сопоставления пользователь не сможет войти в Dynatrace Managed и получит сообщение об ошибке о том, что окружение не найдено.

Переключатель **Assign users to groups based on UserInfo response attribute** определяет способ управления назначением пользователей в группы:

* **Вручную**: отключите переключатель, если назначения пользователей в группы выполняются вручную из Dynatrace Managed. В этом случае Dynatrace Managed игнорирует список групп, отправленный в ответе аутентификации IdP.
* **Автоматически**: включите переключатель и введите имя группы в поле атрибута **User groups**, если назначение пользователей в группы должно выполняться автоматически. В этом случае любые назначения, сделанные в Dynatrace Managed, перезаписываются списком групп из ответа аутентификации IdP. Можно добавить пользовательский разделитель групп пользователей.