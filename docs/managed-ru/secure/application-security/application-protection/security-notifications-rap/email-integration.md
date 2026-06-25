---
title: Интеграция по email для уведомлений безопасности
source: https://docs.dynatrace.com/managed/secure/application-security/application-protection/security-notifications-rap/email-integration
scraped: 2026-05-12T12:10:32.546438
---

# Интеграция по email для уведомлений безопасности

# Интеграция по email для уведомлений безопасности

* How-to guide
* Published Aug 11, 2022

Интегрируйте уведомления безопасности с Dynatrace для передачи проблем безопасности и/или атак на ваш email в целях оповещения и устранения.

Чтобы интегрировать уведомления безопасности по email, следуйте инструкциям ниже.

## Настройка уведомлений об атаках

Чтобы настроить уведомления об атаках

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание профиля оповещения**](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/email-integration#profile "Интеграция уведомлений безопасности об уязвимостях по email.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Привязка профиля оповещения**](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/email-integration#link "Интеграция уведомлений безопасности об уязвимостях по email.")

### Шаг 1: Создание профиля оповещения

Создайте профиль оповещения для настройки правил фильтрации оповещений на основе состояния обнаруженных атак.

1. Перейдите в **Settings** и выберите **Alerting** > **Attack alerting profiles**.
2. Нажмите **Add alerting profile**.
3. Введите **Name** профиля, для которого необходимо получать уведомления безопасности.
4. Включите переключатель для любого статуса атаки, о котором необходимо получать уведомления. Можно выбрать несколько статусов.
5. Нажмите **Save changes** для сохранения конфигурации.

### Шаг 2: Привязка профиля оповещения к интеграции уведомлений безопасности по email

Привяжите профиль оповещения к интеграции уведомлений безопасности по email. Можно определить интеграцию с email и настроить payload (в виде шаблона сообщения), который необходимо получать вместе с уведомлениями безопасности.

1. Перейдите в **Settings** и выберите **Integration** > **Security notifications**.
2. Нажмите **Add integration** и введите следующие сведения.

   * **Security alert type:** Выберите **Attack alert**.
   * **Notification type:** Выберите **Email**.
   * **Display name:** Введите название для интеграции с email. Это название будет отображаться в **Settings** > **Integration** > **Security notifications** после сохранения конфигурации.
   * Нажмите **Add recipient** для добавления email получателя (обязательно), получателя для копии (необязательно) и получателя для скрытой копии (необязательно). Общее количество email-адресов не должно превышать 50.
   * **Subject:** Введите заголовок атаки.
   * **Body:** Введите описание атаки. Поддерживается HTML-форматирование.

   Помимо обычного текста, описание атаки может включать заполнители. Нажмите значок **Info** для просмотра списка **Available placeholders**, которые можно использовать для этой интеграции. Заполнители автоматически заменяются информацией об атаке при формировании уведомления.

   * **Alerting profile:** Выберите [профиль оповещения](#profile-create), для которого необходимо получать уведомления безопасности.
3. Необязательно: Для проверки конфигурации нажмите **Send test notification**. Если конфигурация верна:

   * Тестовое письмо должно поступить на указанный email
   * На странице настроек Dynatrace должно появиться следующее информационное сообщение: `Test notification sent successfully`.
4. **Save changes**.

**Пример email-уведомления**

![Email notification for attacks](https://dt-cdn.net/images/2023-04-19-10-25-55-1200-70c5af2e5c.png)

Email notification for attacks

## Проверка конфигурации

Чтобы убедиться в правильности настройки интеграции

1. Перейдите в **Settings** и выберите **Integration** > **Security notifications**.
2. Выберите **Details** для проверяемой интеграции.
3. Нажмите **Send test notification**. Если конфигурация неверна и тестовое уведомление не было отправлено по email, появится сообщение об ошибке, которое поможет определить проблему.

## Связанные темы

* [Интеграция по email для уведомлений безопасности](/managed/secure/application-security/vulnerability-analytics/security-notifications-rva/email-integration "Интеграция уведомлений безопасности об уязвимостях по email.")
* [FAQ по Application Security](/managed/secure/faq "Часто задаваемые вопросы о Dynatrace Application Security.")