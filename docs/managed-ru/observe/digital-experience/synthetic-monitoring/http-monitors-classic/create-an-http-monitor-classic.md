---
title: Создание HTTP-монитора
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic
scraped: 2026-05-12T11:31:49.691189
---

# Создание HTTP-монитора

# Создание HTTP-монитора

* How-to guide
* 6-min read
* Published Aug 20, 2018

Вы можете создавать синтетические HTTP-мониторы для проверки доступности ваших ресурсов: веб-сайтов или API-эндпоинтов. Поскольку HTTP-мониторы могут выполняться через Environment ActiveGate, их можно использовать для проверки доступности внутренних ресурсов, недоступных за пределами вашей сети.

HTTP-мониторы можно запускать из глобальных [публичных](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Узнайте обо всех доступных публичных расположениях Synthetic Monitoring.") или [частных расположений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга."), а также из кластерных частных расположений в Dynatrace Managed.

Подробности об использовании ActiveGate для Synthetic Monitoring см. в разделе [Создание частного расположения Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга."). Подробности о поддерживаемых версиях Windows и Linux см. в разделе [Требования для частных расположений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые ОС, версии Chromium и требования к оборудованию для частных расположений.").

## Создание нового HTTP-монитора

1. Перейдите в **Synthetic Classic** > **Create a synthetic monitor** > **Create an HTTP monitor**.
2. **Name this HTTP monitor**: введите имя (до 500 символов) для синтетического монитора. Имя должно в общих чертах описывать все запросы этого HTTP-монитора.
3. Нажмите **Add tag**, чтобы применить вручную созданные теги к монитору. Вы можете выбрать из вариантов автодополнения при вводе или создать собственные. (После создания монитора управление тегами доступно на [странице деталей HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Узнайте о странице Synthetic details для HTTP-мониторов.").)
4. **Visual mode** (по умолчанию) позволяет просматривать и настраивать HTTP-запросы через элементы интерфейса. **Script mode** позволяет просматривать и редактировать параметры запросов в виде JSON-скрипта. Вы можете переключаться между режимами при настройке монитора.
5. Добавьте HTTP-запрос (**Add HTTP request**).

   1. Выберите тип запроса (**Choose request type**) и введите базовые параметры запроса.

      * **HTTP request**: введите **URL запроса**, укажите **Имя** запроса (если имя по умолчанию не подходит) и выберите **HTTP-метод**. Затем нажмите **Add HTTP request** для создания запроса и отображения расширенных настроек.

        Для повышения безопасности синтетических мониторов Dynatrace блокирует отправку мониторами запросов на локальный хост (например, `localhost` или `127.0.0.1`).
      * **OAuth2 authorization request**: введите **Access token URL** и укажите **Имя** запроса (если имя по умолчанию не подходит). Затем нажмите **Add OAuth2 authorization request** для создания запроса и отображения расширенных настроек.

        Подробности об использовании аутентификации OAuth 2.0 см. в разделе [Поддерживаемые методы аутентификации в Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication#oauth2 "Узнайте, как настроить методы аутентификации для мониторинга веб-приложений и API-эндпоинтов в Synthetic Monitoring.").

      После добавления запроса его тип изменить нельзя.
   2. После создания запроса в расширенных настройках полностью настройте [базовые параметры запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#basic-settings "Узнайте о настройке HTTP-мониторов."), включая опциональный **User agent** и условия прохождения/провала на основе **Response status code verification**.

      В расширенных настройках запроса можно добавить [токен-учётные данные](/managed/manage/credential-vault#token "Храните учётные данные и управляйте ими в хранилище credential vault.") в **URL HTTP-запроса**: подробности см. в разделе [Настройка HTTP-мониторов](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#basic-settings "Узнайте о настройке HTTP-мониторов.").

      ![Expanded request details](https://dt-cdn.net/images/httpmonitorcreationexpandedrequest-2240-0d5a93ac9f.png)

      Expanded request details
   3. Настройте **Additional options** для запроса: они зависят от типа запроса.

      Подробности см. в разделе [Настройка HTTP-мониторов](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#http-additional-options "Узнайте о настройке HTTP-мониторов.").
6. Вы можете добавить несколько HTTP-запросов: нажмите **Add HTTP request** ещё раз и повторите описанные выше шаги для дополнительного запроса.
7. После определения одного или нескольких запросов для данного HTTP-монитора нажмите **Next** в нижнем левом углу, чтобы задать частоту и расположения монитора.
8. Выберите частоту монитора. Прокрутите вниз для выбора расположений. Ваши частные и публичные расположения сгруппированы по континентам. Выбранные расположения отображаются на карте.

   Подробности о частоте и расположениях монитора см. в разделе [Настройка HTTP-мониторов](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#frequency-locations "Узнайте о настройке HTTP-мониторов.").
9. Нажмите **Next** для финальной проверки параметров монитора.
10. На странице **Summary** проверьте свойства HTTP-монитора и нажмите **Create HTTP monitor**, чтобы сохранить изменения и активировать монитор.

Откроется [страница деталей HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Узнайте о странице Synthetic details для HTTP-мониторов."), которая начнёт отображать данные мониторинга по мере их поступления.

Нажмите кнопку развёртывания ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") в быстрых ссылках в верхнем левом углу для доступа к настройкам монитора. (Или, если вы используете старую версию страницы деталей, нажмите кнопку **Browse** (**...**) > **Edit** для внесения изменений.)

Ряд дополнительных настроек, например обработка сбоев и пороговые значения производительности, доступен только после создания монитора. Подробности о настройках монитора см. в разделе [Настройка HTTP-мониторов](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.").

Хотя локальное воспроизведение HTTP-монитора недоступно, вы можете [выполнить его по запросу](/managed/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Выполняйте синтетические мониторы по запросу из публичных или частных расположений.") из назначенных расположений.

## Просмотр аналитики HTTP-монитора

1. Перейдите в **Synthetic Classic**.
2. Необязательно Выберите **HTTP** в левом меню для фильтрации по HTTP-мониторам.
3. В списке HTTP-мониторов выберите нужный монитор.

[Страница деталей](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Узнайте о странице Synthetic details для HTTP-мониторов.") каждого монитора отображает аналитику мониторинга, включая:

* Доступность
* Производительность (время отклика)
* Размер ответа
* HTTP-коды статуса

## Включение, отключение и удаление HTTP-монитора

По умолчанию мониторы включены при создании.

Отключение синтетического монитора приостанавливает дальнейшие выполнения, но сохраняет монитор и его данные измерений. При отключении монитора открытые проблемы производительности и доступности закрываются по тайм-ауту (подробности см. в разделе [Расчёты Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Узнайте о расчётах метрик Synthetic Monitoring.")). Удаление убирает монитор и связанные данные измерений; эта операция необратима. Перед удалением монитора рекомендуется сначала отключить его и убедиться, что данные измерений больше не нужны.

Отключение или удаление монитора

1. Перейдите в **Synthetic Classic**.
2. Переключитесь в режим отображения списком.
3. Необязательно Выберите **HTTP** в левом меню для фильтрации по HTTP-мониторам.
4. Установите флажок для монитора, который хотите удалить или отключить.
5. Нажмите **Delete** или **Disable** в нижнем левом углу.

   ![Disable or delete an HTTP monitor](https://dt-cdn.net/images/disabledeletehttpmonitor-1267-0be74becb5.png)

   Disable or delete an HTTP monitor

Отключить или удалить монитор также можно со [страницы деталей](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Узнайте о странице Synthetic details для HTTP-мониторов.").

1. Перейдите в **Synthetic Classic**.
2. Выберите нужный монитор.
3. Нажмите кнопку развёртывания ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") в быстрых ссылках в верхнем левом углу.

   Или, если вы используете старую версию страницы деталей, нажмите кнопку **Browse** (**...**) в верхнем правом углу.
4. Выберите **Disable** или **Delete**.

Аналогично можно включить ранее отключённый монитор.

* В **Synthetic Classic** переключитесь в режим отображения списком. Установите флажок рядом с отключённым монитором и нажмите **Enable** в нижнем левом углу.
* На [странице деталей HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Узнайте о странице Synthetic details для HTTP-мониторов.") нажмите кнопку развёртывания ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") в верхнем левом углу > **Enable**.

  Если вы используете старую версию страницы деталей, нажмите кнопку **Browse** (**...**) в верхнем правом углу > **Enable**.

[Выполнение синтетического монитора может быть отключено на время окна обслуживания](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Узнайте о расчётах метрик Synthetic Monitoring.") в настройках окна обслуживания.

## Дублирование HTTP-монитора

1. Перейдите в **Synthetic Classic**.
2. Переключитесь в режим отображения списком.
3. Необязательно Выберите **HTTP** в левом меню для фильтрации по HTTP-мониторам.
4. Установите флажок для монитора, который хотите продублировать.
5. Нажмите **Duplicate** в нижнем левом углу.

   Откроется страница дублированного монитора с номером, добавленным к исходному имени.
6. Чтобы изменить имя по умолчанию и внести другие правки конфигурации, нажмите кнопку развёртывания ![Expand](https://dt-cdn.net/images/expandbutton-40-e1f11ff81d.png "Expand") > **Edit**.

   Если вы используете старую версию страницы деталей, нажмите кнопку **Browse** (**...**) > **Edit**.

Обратите внимание, что дублированный монитор по умолчанию отключён. Для начала получения данных необходимо [его включить](#enable-disable).

## Массовое управление HTTP-мониторами

1. Перейдите в **Synthetic Classic**.
2. Необязательно Выберите **HTTP** в левом меню для фильтрации по HTTP-мониторам.
3. Установите флажки для мониторов, которыми хотите управлять.

   В нижнем левом углу страницы появятся доступные кнопки команд.
4. Выберите действие, которое хотите применить ко всем выбранным мониторам: **Delete**, **Disable**, **Enable**, **Duplicate** или **Edit**.

### Параметры массового управления мониторами

При выборе нескольких HTTP-мониторов для массового управления:

* Если кнопка недоступна, данный параметр неприменим ко всем выбранным мониторам. Например, если все выбранные мониторы активны, кнопка **Enable** будет неактивна.
* Кнопка **Duplicate** недоступна при выборе более одного монитора.
* Если выбраны как активные, так и неактивные мониторы, отображаются обе кнопки: **Enable** и **Disable**. При выборе одного из этих действий оно применяется только к соответствующим мониторам.
* Параметр массового редактирования **Edit** позволяет изменять лишь отдельные функции выбранных HTTP-мониторов: можно перезаписать частоту монитора, изменить или добавить расположения, добавить теги и изменить связанные приложения.

  ![Bulk edit options for HTTP monitors](https://dt-cdn.net/images/bulkedithttpmonitors-729-515d0a2a09.png)

  Bulk edit options for HTTP monitors

## Связанные темы

* [Synthetic Monitors API](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors "Управляйте синтетическими мониторами через Synthetic v1 API.")