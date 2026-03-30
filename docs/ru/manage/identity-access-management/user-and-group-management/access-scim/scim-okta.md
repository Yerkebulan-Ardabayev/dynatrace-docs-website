---
title: Настройка Okta SCIM для Dynatrace
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-okta
scraped: 2026-03-06T21:31:30.983595
---

* Latest Dynatrace
* How-to guide
* 1-min read

На этой странице описывается сторона IdP (**Okta**) в конфигурации **SCIM** SSO, а не сторона Dynatrace. Используйте её как часть полной процедуры настройки SCIM для Dynatrace SaaS при использовании Okta.

Несмотря на все усилия предоставить актуальную информацию, Dynatrace не контролирует изменения, которые могут вносить сторонние поставщики. Всегда обращайтесь к официальной документации стороннего поставщика (вашего IdP) как к основному источнику информации о сторонних продуктах.

Для интеграции Dynatrace SCIM в Okta вам потребуются базовый URL Dynatrace SCIM и секретный токен, полученные в процедуре [Получение конечной точки Dynatrace SCIM и создание секретного токена](../access-scim.md#scim-endpoint-secret-token "SCIM").

Okta предоставляет два варианта интеграции SCIM:

1. [Добавление подготовки SCIM к уже интегрированному приложению Okta с Dynatrace SSO](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_App_Integration_Wizard_SCIM.htm)
2. [Интеграция Dynatrace SCIM в отдельном приложении Okta для SCIM](https://developer.okta.com/docs/guides/build-provisioning-integration/prepare-app/)

   * Вы можете использовать [SCIM 2.0 Test App (Header Auth)](https://www.okta.com/integrations/scim-2-0-test-app-header-auth) или [SCIM 2.0 Test App (OAuth Bearer Token)](https://www.okta.com/integrations/scim-2-0-test-app-oauth-bearer-token)

Dynatrace SCIM поддерживает только аутентификацию по токену Bearer. В зависимости от типа приложения Okta при настройке учётных данных API токен должен быть указан с префиксом **Bearer**.
