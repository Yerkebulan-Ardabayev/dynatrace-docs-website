---
title: Запись браузерного clickpath-а
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath
scraped: 2026-05-12T11:31:53.709030
---

# Запись браузерного clickpath-а

# Запись браузерного clickpath-а

* How-to guide
* 7-min read
* Updated on Nov 01, 2022

Ваше веб-приложение предоставляет клиентам ключевую функциональность, критически важную для успеха бизнеса. Мониторинг приложения с помощью браузерных clickpath-ов обеспечивает доступность этой функциональности для клиентов 24/7.

С помощью удобного Dynatrace Synthetic Recorder (расширения для Google Chrome) вы можете получить видимость доступности и производительности наиболее важной функциональности приложения, охватывающей все элементы IT-инфраструктуры, всего в несколько кликов.

Используйте Dynatrace Synthetic Recorder для записи точной последовательности взаимодействий, которой должны следовать имитируемые визиты пользователей. Рекордер захватывает события (такие как клики по кнопкам, прокрутка страницы или ввод данных) и преобразует их в скрипт, воспроизводимый при каждом запуске clickpath-а.

Каждый запуск монитора начинается в чистом состоянии: с очищенным кэшем браузера и пустым [локальным хранилищем](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

## Установка расширения Dynatrace Synthetic Recorder

Для начала необходимо установить Dynatrace Synthetic Recorder. После установки рекордер автоматически обновляется при появлении новых функций.

1. Перейдите в **Synthetic Classic**.
2. Нажмите **Create a synthetic monitor** > **Create a browser monitor**.
3. Новым пользователям будет предложено установить расширение Chrome: нажмите **Install Dynatrace Synthetic Recorder** внизу страницы.
4. На странице расширения нажмите **Add to Chrome** > **Add Extension**.

### Разрешить расширение в режиме инкогнито

После установки Dynatrace Synthetic Recorder необходимо включить разрешение **Allow in incognito**. Это нужно для обеспечения чистого состояния браузера при записи и локальном воспроизведении в режиме инкогнито Chrome.

1. Введите `chrome://extensions/` в адресную строку Chrome и нажмите Enter.
2. На плитке **Dynatrace Synthetic Recorder** нажмите **Details**.
3. Включите **Allow in incognito**.

## Запись браузерного clickpath-а

1. Перейдите в **Synthetic Classic**.
2. Нажмите **Create a synthetic monitor** > **Create a browser monitor**.
3. Введите корректный **URL** и проверьте имя по умолчанию (**Name**) для вашего clickpath-а на странице создания синтетического монитора.

   Для повышения безопасности синтетических мониторов Dynatrace блокирует отправку мониторами запросов на локальный хост (например, `localhost` или `127.0.0.1`).
4. Нажмите **Add tag**, чтобы применить вручную созданные теги к монитору. Вы можете выбрать из вариантов автодополнения при вводе или создать собственные. (После создания монитора управление тегами доступно на [странице Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.").)
5. Продолжите [настройку монитора](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов."): профиль устройства и дополнительные параметры, такие как куки и аутентификация.

   ![Configure a browser monitor](https://dt-cdn.net/images/configurebrowsermonitor1-1665-749a574062.png)

   Configure a browser monitor

   При первоначальной настройке браузерного clickpath-а **Enable global login authentication** не поддерживается для записи.

   * Для форм-аутентификации можно просто записать ввод учётных данных в веб-форму.
   * Для HTTP-based схем аутентификации нужно вручную ввести имя пользователя и пароль в собственном диалоге браузера при записи clickpath-а, а затем включить HTTP-аутентификацию в [событии Navigate](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#navigate "Узнайте о типах событий при записи браузерного clickpath-а.") в режиме редактирования.

   Дополнительную информацию см. в разделе [Поддерживаемые методы аутентификации в Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication "Узнайте, как настроить методы аутентификации для мониторинга веб-приложений и API-эндпоинтов в Synthetic Monitoring.").
6. Запишите или определите события clickpath-а.

   * Вы можете **Manually add clickpath events**. Также доступны **Play back clickpath**, **Record again** или **Cancel** — см. [Локальное воспроизведение](#playback).

     Опция **Record again** позволяет выбрать: перезаписать clickpath полностью или после воспроизведения до указанного события. Обратите внимание: при полной перезаписи с нуля все JavaScript-события, предшествующие начальному событию Navigate, будут удалены — см. [События браузерных clickpath-ов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#javascript "Узнайте о типах событий при записи браузерного clickpath-а.").

     + Для ручного создания clickpath-а можно редактировать в **Visual mode**, добавляя [события](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Узнайте о типах событий при записи браузерного clickpath-а.") в скрипт. Также необходимо [настроить параметры монитора](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов.").

       ![Manual clickpath creation by UI](https://dt-cdn.net/images/manualclickpathvisual-1646-9c8c648618.png)

       Manual clickpath creation by UI
     + Для ручного создания clickpath-а в [**Script mode**](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Создавайте и редактируйте браузерные мониторы в формате JSON.") все события и параметры, такие как куки и автовход, задаются в JSON.

       ![Manual clickpath script creation](https://dt-cdn.net/images/manualclickpathscript-1667-675cfdda17.png)

       Manual clickpath script creation
   * Для использования рекордера нажмите **Record clickpath**.

     Браузерные clickpath-ы имеют жёстко заданный тайм-аут в 5 минут. При записи убедитесь, что clickpath не превышает этот предел.

     1. В появившемся экземпляре браузера рекордера взаимодействуйте с приложением, имитируя важный сценарий использования (например, вход, поиск товара или оформление заказа). По мере взаимодействия каждое событие записывается для последующего воспроизведения.
     2. По окончании нажмите значок расширения Dynatrace на панели меню браузера, чтобы **Finish** запись.

        ![Finish recording a clickpath](https://dt-cdn.net/images/finishrecordclickpath-1420-6f9197a415.png)

        Finish recording a clickpath
     3. Отображаются события записанного clickpath-а. Вы можете [редактировать каждое событие](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов."), например, добавить валидацию контента или настроить время ожидания. Нажмите **Back** для начала настройки монитора с нуля. Также доступны **Play back clickpath** и **Record again** — см. [Локальное воспроизведение](#playback).

        Опция **Record again** позволяет выбрать: перезаписать clickpath полностью или после воспроизведения до указанного события. Обратите внимание: при полной перезаписи с нуля все JavaScript-события, предшествующие начальному событию Navigate, будут удалены — см. [События браузерных clickpath-ов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#javascript "Узнайте о типах событий при записи браузерного clickpath-а.").

        Если в записанном clickpath-е захвачены учётные данные, например пароль, вы получите уведомление и возможность сохранить их в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище."). На изображении ниже показан записанный clickpath с захваченным паролем. Подробнее об учётных данных см. в разделах [событие Navigate](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#navigate "Узнайте о типах событий при записи браузерного clickpath-а.") и [событие Keystroke](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#keystroke "Узнайте о типах событий при записи браузерного clickpath-а.").

        ![Captured credential](https://dt-cdn.net/images/clickpathcapturedpasswordkeystroke2-1617-0dc046deba.png)

        Captured credential
7. После завершения записи нажмите **Next** для продолжения настройки: выберите расположения монитора и частоту.

   Если вы нажмёте эту кнопку без записи clickpath-а или ручного определения событий, будет создан [браузерный монитор по одному URL](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Узнайте, как настроить браузерный монитор по одному URL для проверки доступности сайта.") для указанного URL.
8. Выберите частоту монитора. Прокрутите вниз для выбора расположений. Ваши выборы отображаются на карте. Нажмите **Next** для просмотра сводки монитора.

   ![Monitor frequency and locations](https://dt-cdn.net/images/syntheticfrequencylocations2-2223-297d2c4656.png)

   Monitor frequency and locations
9. На странице Summary вы можете проверить и изменить конфигурацию (**Change URL or name**; **Change configuration**) или отредактировать события clickpath-а (**Edit clickpath**).

   ![Clickpath summary](https://dt-cdn.net/images/summaryclickpath2-2245-f1f7857bcc.png)

   Clickpath summary

   * Объяснение разницы между действиями и событиями см. в разделе [Количество действий, потребляемых браузерными clickpath-ами](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths "Узнайте, сколько действий потребляет браузерный clickpath и чем они отличаются от событий.").
   * [Потребление действий Synthetic](/managed/license/monitoring-consumption-classic/digital-experience-monitoring-units "Узнайте, как рассчитывается потребление Dynatrace Digital Experience Monitoring на основе DEM Units.") является оценочным, исходя из среднего значения 730 часов в месяц.
10. Внизу страницы нажмите **Create browser monitor**. Через несколько минут вы [получите данные мониторинга](#view-the-analytics-of-a-browser-clickpath) для нового браузерного clickpath-а.

### Локальное воспроизведение

Вы можете воспроизвести clickpath локально после записи или ручного определения событий.

Если с браузерным монитором связаны учётные данные (публичные или только для владельца), пользователям нужно ввести учётные данные для локального воспроизведения. Однако если включить **Enable local playback of Synthetic browser monitors without entering credentials** в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище."), пользователи смогут воспроизводить браузерный монитор без ввода доступных им учётных данных.

Тайм-ауты для локального воспроизведения: 60 секунд для событий и 5 минут для мониторов. Эти значения нельзя изменить в веб-интерфейсе Dynatrace. Однако можно использовать метод [PUT configuration](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-configuration-v2/put-configuration "Обновляйте конфигурацию Synthetic Monitoring через Synthetic API v2.") Synthetic configuration API v2 для изменения тайм-аутов браузерных мониторов во всём окружении: для выполнения в частных расположениях, локального воспроизведения и времени ожидания.

Можно оставить окно воспроизведения открытым после завершения (**Keep window open after playback**), например, для отладки сбойного выполнения или добавления [события JavaScript](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Узнайте о типах событий при записи браузерного clickpath-а.").

* Локальное воспроизведение отличается от [выполнения монитора по запросу](/managed/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Выполняйте синтетические мониторы по запросу из публичных или частных расположений.") из назначенных расположений (публичных или частных).
* Локальное воспроизведение в Dynatrace работает в режиме эмуляции на основе профиля устройства и user agent, выбранных при настройке монитора. То есть воспроизведение эмулирует выбранное устройство. При переходе к тому же URL или выполнении той же транзакции вне Dynatrace впечатление может отличаться.

## Просмотр аналитики браузерного clickpath-а

1. Перейдите в **Synthetic Classic**.
2. Необязательно Отфильтруйте по **Browser clickpath** в левом меню.
3. В списке мониторов выберите нужный браузерный clickpath. Вы будете перенаправлены на [страницу Synthetic details](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.") для clickpath-а.

## Отключение или удаление браузерного clickpath-а

По умолчанию мониторы включены при создании.

Отключение синтетического монитора приостанавливает дальнейшие выполнения, но сохраняет монитор и его данные измерений. При отключении монитора открытые проблемы производительности и доступности закрываются по тайм-ауту (подробности см. в разделе [Расчёты Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Узнайте о расчётах метрик Synthetic Monitoring.")). Удаление убирает монитор и связанные данные измерений; эта операция необратима. Перед удалением монитора рекомендуется сначала отключить его и убедиться, что данные измерений больше не нужны.

Отключение или удаление монитора

1. Перейдите в **Synthetic Classic**.
2. Переключитесь в режим отображения списком.
3. Установите флажок для монитора, который хотите удалить или отключить.
4. Нажмите **Delete** или **Disable** в левом нижнем углу.

   ![Delete a clickpath](https://dt-cdn.net/images/deletedisableclickpath1-892-020ec7491d.jpg)

   Delete a clickpath

Отключить или удалить монитор также можно со [страницы деталей](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.").

1. Перейдите в **Synthetic Classic**.
2. Выберите нужный монитор.
3. Нажмите кнопку **Browse** (**...**) и выберите **Disable** или **Delete**.

[Выполнение синтетического монитора может быть отключено на время окна обслуживания](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations#m-windows-availability "Узнайте о расчётах метрик Synthetic Monitoring.") в настройках окна обслуживания.