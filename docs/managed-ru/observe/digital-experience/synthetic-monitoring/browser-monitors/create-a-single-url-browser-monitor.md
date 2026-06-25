---
title: Создание браузерного монитора по одному URL
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor
scraped: 2026-05-12T11:31:43.050448
---

# Создание браузерного монитора по одному URL

# Создание браузерного монитора по одному URL

* How-to guide
* 3-min read
* Updated on Aug 19, 2025

Синтетический мониторинг позволяет создавать два вида браузерных мониторов: по одному URL и clickpath-ы, для проверки доступности и производительности веб-приложения через регулярные интервалы. Браузерные мониторы по одному URL выполняют тесты доступности одной страницы вашего сайта или веб-приложения. Также можно проверять производительность.

## Создание браузерного монитора по одному URL

1. Перейдите в **Synthetic Classic**.
2. Нажмите **Create a synthetic monitor** в правом верхнем углу > **Create a browser monitor**.
3. На странице Configure a browser monitor введите **URL** для мониторинга и либо используйте имя по умолчанию (**Name**), либо задайте своё.

   Для повышения безопасности синтетических мониторов Dynatrace блокирует отправку мониторами запросов на локальный хост (например, `localhost` или `127.0.0.1`).
4. Нажмите **Add tag**, чтобы применить вручную созданные теги к монитору. Вы можете выбрать из вариантов автодополнения при вводе или создать собственные. (После создания монитора управление тегами доступно на [странице Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.").)
5. [Настройте монитор](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов.") соответствующим образом: выберите профиль эмулируемого устройства, аутентификацию и другие параметры.

   ![Configure a browser monitor](https://dt-cdn.net/images/configurebrowsermonitor1-1665-749a574062.png)

   Configure a browser monitor

   Аутентификация через веб-форму больше не поддерживается для браузерных мониторов по одному URL. Вместо этого создайте [браузерный clickpath](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.") для сценариев, требующих веб-формы входа. Ранее настроенные мониторы по одному URL продолжат работу, однако рекомендуется перезаписать их как clickpath-ы, чтобы чётко разделить каждый шаг входа.

   Перезапись обязательна, если вы хотите изменить любую часть настроек монитора. Сохранить изменения в текущем формате больше нельзя.

   Начиная с Dynatrace версии 1.324+, мониторы по одному URL с формой входа будут автоматически обновлены путём добавления бесплатного шага JavaScript для поддержки процесса входа.
6. Нажмите **Next** для продолжения настройки: выберите расположения монитора и частоту. Подробности см. в разделе [Настройка браузерных мониторов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов.").

   ![Monitor frequency and locations](https://dt-cdn.net/images/syntheticfrequencylocations2-2223-297d2c4656.png)

   Monitor frequency and locations
7. Нажмите **Next** внизу страницы для просмотра сводки монитора.
8. На странице Summary вы можете проверить и изменить конфигурацию (**Change URL or name**; **Change configuration**).

   ![Single-URL browser monitor summary](https://dt-cdn.net/images/summarysingleurl-2246-6f4d67b798.png)

   Single-URL browser monitor summary
9. Внизу страницы нажмите **Create browser monitor**. Через несколько минут вы [получите данные мониторинга](#view-the-analytics-of-a-browser-monitor) для нового браузерного монитора.

Хотя локальное воспроизведение монитора по одному URL недоступно, вы можете [выполнить его по запросу](/managed/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Выполняйте синтетические мониторы по запросу из публичных или частных расположений.") из назначенных расположений.

## Просмотр аналитики браузерного монитора

1. Перейдите в **Synthetic Classic**.
2. Необязательно Выберите **Browser** в левом меню для фильтрации по браузерным мониторам по одному URL.
3. В списке мониторов выберите нужный браузерный монитор. Вы будете перенаправлены на [страницу Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.") для этого монитора.

Страница деталей каждого монитора содержит подробные результаты, например, метрики доступности и обнаруженные проблемы.

## Отключение или удаление браузерного монитора

По умолчанию мониторы включены при создании.

Отключение синтетического монитора приостанавливает дальнейшие выполнения, но сохраняет монитор и его данные измерений. При отключении монитора открытые проблемы производительности и доступности закрываются по тайм-ауту (подробности см. в разделе [Расчёты Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Узнайте о расчётах метрик Synthetic Monitoring.")). Удаление убирает монитор и связанные данные измерений; эта операция необратима. Перед удалением монитора рекомендуется сначала отключить его и убедиться, что данные измерений больше не нужны.

Отключение или удаление монитора

1. Перейдите в **Synthetic Classic**.
2. Переключитесь в режим отображения списком.
3. Установите флажок для монитора, который хотите удалить или отключить.
4. Нажмите **Delete** или **Disable** в левом нижнем углу.

   ![Disable browser monitor](https://dt-cdn.net/images/disabledeletemonitor1-891-3c3e768323.png)

   Disable browser monitor

Отключить или удалить монитор также можно со [страницы деталей](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.").

1. Перейдите в **Synthetic Classic**.
2. Выберите нужный монитор.
3. Нажмите кнопку **Browse** (**...**) и выберите **Disable** или **Delete**.

[Выполнение синтетического монитора может быть отключено на время окна обслуживания](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Узнайте о расчётах метрик Synthetic Monitoring.") в настройках окна обслуживания.

## Связанные темы

* [Synthetic Monitors API](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors "Управляйте синтетическими мониторами через Synthetic v1 API.")