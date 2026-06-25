---
title: Обновление конфигурации через редактируемые свойства
source: https://docs.dynatrace.com/managed/upgrade/saas-upgrade-assistant/sua-update-editable-properties
scraped: 2026-05-12T12:16:29.266369
---

# Обновление конфигурации через редактируемые свойства

# Обновление конфигурации через редактируемые свойства

* Published Dec 07, 2023

Latest Dynatrace

В ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** доступны два режима редактирования: одиночный и массовый.

## Обновление отдельной конфигурации

Для обновления отдельной конфигурации:

1. В Dynatrace Launcher выберите ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant**.
2. [**Запустите обновление с SaaS Upgrade Assistant**](/managed/upgrade/saas-upgrade-assistant/sua-get-started "Upload configuration and deploy with SaaS Upgrade Assistant.")
3. Выберите вкладку **Upgrade details: configuration**.
4. Отфильтруйте конфигурации с помощью селектора **Config type** и введите имя или ID конфигурации.
5. Выберите объект конфигурации из левой панели.
6. Выберите вкладку **Edit properties**.
7. Введите новое значение в поле ввода.
8. Выберите **Preview changes**.
9. Проверьте изменение и подтвердите, нажав **Save**.

## Обновление нескольких конфигураций

Для одновременного обновления нескольких конфигураций:

1. В Dynatrace Launcher выберите ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant**.
2. [**Запустите обновление с SaaS Upgrade Assistant**](/managed/upgrade/saas-upgrade-assistant/sua-get-started "Upload configuration and deploy with SaaS Upgrade Assistant.")
3. Выберите вкладку **Configuration**.
4. Отфильтруйте конфигурации с помощью селектора **Config type** и/или введите имя или ID конфигурации.
5. Выберите **Bulk edit**. Число в скобках указывает количество редактируемых свойств.
6. Выберите **Property group**.
7. Выберите значение для поиска из селектора.
8. Введите новое значение в поле ввода **Replace with**.
9. Выберите **Preview changes**.
10. Проверьте изменение и подтвердите, нажав **Save**.

## Пример: частная Synthetic-локация

Этот пример демонстрирует рекомендуемый подход к успешной миграции конфигурации.

Синтетические мониторы Dynatrace можно запускать из [частной Synthetic-локации](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") — локации в вашей частной сетевой инфраструктуре, где установлен один или несколько экземпляров ActiveGate с поддержкой Synthetic. Частная Synthetic-локация привязана к ActiveGate по ID ActiveGate. Для миграции этой конфигурации установите новый ActiveGate для вашей среды SaaS и получите его ID со страницы **Deployment status**. Затем используйте ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** для обновления конфигурации частной Synthetic-локации:

1. Выберите вкладку **Configuration**.
2. В поле **Config type** выберите `Synthetic location`.
3. Выберите объект конфигурации частной Synthetic-локации из левой панели.
4. Нажмите кнопку **Edit** ![Edit](https://dt-cdn.net/images/dashboards-app-dashboard-rename-a2875a87a2.svg "Edit").
5. Вставьте новый ID ActiveGate.
6. Нажмите кнопку **Preview changes**.
7. Проверьте изменение и подтвердите, нажав кнопку **Save**.
8. Выберите вкладку навигации **Overview**.
9. Выберите **Start upgrade**, чтобы развернуть изменения.