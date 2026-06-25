---
title: Интеграция через webhook для уведомлений безопасности
source: https://docs.dynatrace.com/managed/secure/application-security/application-protection/security-notifications-rap/webhook-integration
scraped: 2026-05-12T12:10:34.466052
---

# Интеграция через webhook для уведомлений безопасности

# Интеграция через webhook для уведомлений безопасности

* How-to guide
* Published Oct 21, 2021

Интегрируйте уведомления безопасности с Dynatrace для передачи проблем безопасности и/или атак вашим командам в целях оповещения и устранения.

Чтобы интегрировать уведомления безопасности с помощью webhook, следуйте инструкциям ниже.

## Настройка уведомлений об атаках

Чтобы настроить уведомления об атаках

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание профиля оповещения**](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/webhook-integration#profile "Интеграция уведомлений безопасности об уязвимостях и/или атаках с помощью webhook.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Привязка профиля оповещения**](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/webhook-integration#link "Интеграция уведомлений безопасности об уязвимостях и/или атаках с помощью webhook.")

### Шаг 1: Создание профиля оповещения

Создайте профиль оповещения для настройки правил фильтрации оповещений на основе состояния обнаруженных атак.

1. Перейдите в **Settings** и выберите **Alerting** > **Attack alerting profiles**.
2. Нажмите **Add alerting profile**.
3. Введите **Name** профиля, для которого необходимо получать уведомления безопасности.
4. Включите переключатель для любого статуса атаки, о котором необходимо получать уведомления. Можно выбрать несколько статусов.
5. Нажмите **Save changes** для сохранения конфигурации.

### Шаг 2: Привязка профиля оповещения к интеграции уведомлений безопасности через webhook

Привяжите профиль оповещения к интеграции уведомлений безопасности с помощью webhook. Можно определить интеграцию с webhook и настроить payload (в виде шаблона сообщения), который необходимо получать вместе с уведомлениями безопасности.

1. Перейдите в **Settings** и выберите **Integration** > **Security notifications**.
2. Нажмите **Add integration** и введите следующие сведения.

   * **Security alert type:** Выберите **Attack alert**.
   * **Notification type:** Выберите **Custom integration**.
   * **Display name:** Введите название для интеграции с webhook. Это название будет отображаться в **Settings** > **Integration** > **Security notifications** после сохранения конфигурации.
   * **Webhook endpoint URL:** Введите URL конечной точки webhook API.
3. Необязательно: Выберите, принимать ли любой SSL-сертификат.

   * **On** = Принимать любой SSL-сертификат (включая самоподписанные и недействительные)
   * **Off** = Dynatrace проверяет SSL-сертификат URL. (Рекомендуется)
4. Нажмите **Add HTTP header** для указания дополнительных полей HTTP-заголовка, например `Content-Type` или `Authorization`. Эти пользовательские поля HTTP-заголовка можно использовать, если целевой конечной точке требуется токен аутентификации в HTTP-заголовке или если необходимо отправить контент различных типов, таких как `application/json`, `application/xml`, `text/plain`.

   Поле **Content-Type** является обязательным; остальные — необязательны.
5. В поле **Custom payload** настройте формат и содержимое уведомления. После обнаружения атаки этот настраиваемый payload передаётся через **HTTP POST** в целевую систему. Нажмите значок **Info** для просмотра списка **Available placeholders**, которые можно использовать для этой интеграции. Заполнители автоматически заменяются информацией об атаке при формировании уведомления.

**Пример шаблона сообщения:**

```
{



"text": "Notification for ATTACK *{AttackDisplayId}*. \nTitle: *{Title} - ({Type}) - {State}*\n{AttackUrl}\n* Process group: {ProcessGroupId}, \n* Entry point: {EntryPoint}, \n* Timestamp: {Timestamp}, \n* Vulnerability: {VulnerabilityName}.  \n\n *from test system* :dynatrace:"



}
```

**Пример payload:**

![webhook-attacks](https://dt-cdn.net/images/image-4-640-79cfc484d6.png)

webhook-attacks

6. В списке **Alerting profile** выберите [профиль оповещения](#profile), для которого необходимо получать уведомления безопасности.
7. Необязательно: Для проверки конфигурации нажмите **Send test notification**. Если конфигурация верна:

   * Уведомление должно поступить на конечную точку вашей организации.
   * На странице настроек Dynatrace должно появиться следующее информационное сообщение: `Test notification sent successfully`.
8. **Save changes**.

## Проверка конфигурации

Чтобы убедиться в правильности настройки интеграции

1. Перейдите в **Settings** и выберите **Integration** > **Security notifications**.
2. Выберите **Details** для проверяемой интеграции.
3. Нажмите **Send test notification**. Если конфигурация неверна и тестовое уведомление не было отправлено на выбранную конечную точку вашей организации, появится сообщение об ошибке, которое поможет определить проблему.

## Связанные темы

* [Интеграция через webhook для уведомлений безопасности](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/webhook-integration "Интеграция уведомлений безопасности об уязвимостях и/или атаках с помощью webhook.")
* [FAQ по Application Security](/managed/secure/faq "Часто задаваемые вопросы о Dynatrace Application Security.")