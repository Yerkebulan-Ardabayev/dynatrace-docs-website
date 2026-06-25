---
title: Настройка источника кода Real User Monitoring
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source
scraped: 2026-05-12T11:23:51.229887
---

# Настройка источника кода Real User Monitoring

# Настройка источника кода Real User Monitoring

* How-to guide
* 4-min read
* Updated on Nov 21, 2025

В большинстве сценариев RUM браузер отправляет как минимум один дополнительный запрос на получение кода мониторинга:

* Все форматы сниппетов, кроме [встроенного кода](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case"), включают код мониторинга как внешний ресурс, запрашиваемый браузером отдельно.
* Код мониторинга для Session Replay всегда запрашивается отдельно, даже если используется формат тега со встроенным кодом.

URL-адрес запрашиваемого кода мониторинга по умолчанию зависит от метода инъекции вашего приложения.

* **Безагентные приложения:** при использовании [безагентного мониторинга](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") код мониторинга запрашивается из вашего CDN. В непроизводственных средах вместо него можно использовать Cluster ActiveGate. В случае формата тега [JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") имя файла заканчивается на `_complete.js` и содержит идентификатор приложения (например, `7cab1abeacdfe1_complete.js`). Для всех остальных форматов имя файла начинается с `ruxitagent_` и содержит информацию об активных модулях кода и версии кода мониторинга (например, `ruxitagent_ICA7NQVfqrtux_10307250124095659.js`). Имя файла кода мониторинга Session Replay начинается с `ruxitagent_` (например, `ruxitagent_D_10307250124095659.js`) для всех форматов тегов.
* **Автоматическая инъекция:** если [RUM JavaScript инжектируется автоматически](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), код мониторинга RUM и Session Replay запрашивается с вашего веб-сервера или сервера приложений через корневой относительный URL, где имя файла начинается с `ruxitagentjs_` и содержит информацию об активных модулях кода и версии кода мониторинга (например, `/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js` или `/myapplication/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`).
* **Ручная вставка для страниц приложения с автоматической инъекцией:** если [RUM JavaScript вставляется вручную, несмотря на то что группы процессов инструментированы OneAgent](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"), код мониторинга, как и при автоматической инъекции, запрашивается с вашего веб-сервера или сервера приложений через корневой относительный URL с именем файла, начинающимся на `ruxitagentjs_`. Единственное исключение — формат тега JavaScript tag, при котором код мониторинга RUM запрашивается из CDN, а имя файла заканчивается на `_complete.js`. Код мониторинга Session Replay запрашивается с вашего веб-сервера или сервера приложений, и его имя файла начинается с `ruxitagentjs_` для всех форматов тегов.

Как правило, эту настройку изменять не требуется, однако существуют сценарии, когда может понадобиться альтернативная конфигурация источника кода мониторинга. Например:

* Если ваша инфраструктура блокирует запросы кода мониторинга приложения с автоматической инъекцией из-за стандартного URL-пути.
* Если нежелательно, чтобы запросы кода мониторинга обрабатывались на веб-сервере или сервере приложений, на котором размещено приложение.
* Если необходимо предотвратить блокировку кода мониторинга блокировщиками рекламы.

В следующих разделах описаны альтернативные конфигурации для учёта этих ограничений.

## Приложение с автоматической инъекцией: изменение URL-пути кода мониторинга

В зависимости от конфигурации инфраструктуры возможна ситуация, когда запросы кода мониторинга не проходят по автоматически выбранному URL-пути и поэтому не могут быть обработаны OneAgent. Для решения этой проблемы можно изменить часть URL, предшествующую префиксу `ruxitagentjs_`.

Чтобы изменить URL-путь кода мониторинга RUM для приложения с автоматической инъекцией:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Automatic injection**.
5. В раскрывающемся списке **Real User Monitoring code source** выберите **OneAgent**.
6. В поле **Specify path for RUM monitoring code** введите относительный URL-путь к коду мониторинга.

Обратите внимание, что нельзя убрать сегмент пути с префиксом `ruxitagentjs_`, необходимый для идентификации запроса как запроса на получение кода мониторинга.

#### Примеры

В следующих примерах предполагается, что по умолчанию код мониторинга запрашивается из `/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`.

* **Корневой относительный URL:** если задать путь `/custompath`, код мониторинга будет запрашиваться из `/custompath/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`.
* **Относительный URL:** если задать путь `./`, URL запроса кода мониторинга будет относительным по отношению к текущей странице. Например:

  + Если текущая страница — `/shop/index.html`, код мониторинга будет запрашиваться из `/shop/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`.
  + Если текущая страница — `/account/dashboard/`, код мониторинга будет запрашиваться из `/account/dashboard/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`.

Эта конфигурация действует не только для автоматической инъекции, но и для [ручной вставки для страниц приложения с автоматической инъекцией](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"). Единственное исключение — запрос `_complete.js` для формата тега JavaScript tag, который по-прежнему будет выполняться из CDN или Cluster ActiveGate.

## Приложение с автоматической инъекцией: запрос кода мониторинга из CDN

Обратите внимание, что все подключённые ActiveGate должны иметь версию 1.310 или выше не менее 30 дней, прежде чем эта функция станет доступной.

Если необходимо, чтобы код мониторинга для приложения с автоматической инъекцией запрашивался из CDN или Cluster ActiveGate, настроенного согласно инструкциям в разделе [Настройка безагентного Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."), а не из OneAgent, выполните следующие шаги.

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Automatic injection**.
5. В раскрывающемся списке **Real User Monitoring code source** выберите **CDN**.

Эта конфигурация действует как для автоматической инъекции, так и для [ручной вставки для страниц приложения с автоматической инъекцией](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"). При её использовании имена файлов, ранее начинавшиеся с `ruxitagentjs_`, будут начинаться с `ruxitagent_`.

## Настройка пользовательского префикса имени файла кода мониторинга

После изменения префикса имени файла кода мониторинга возможно временное снижение объёма собираемых данных RUM. Поэтому рекомендуется избегать частых изменений этого параметра.

По умолчанию имя файла кода мониторинга начинается с префикса `ruxitagent` или `ruxitagentjs`, если только не используется формат тега JavaScript tag. В качестве альтернативы можно указать пользовательский префикс, который будет применяться вместо стандартного как для безагентных, так и для автоматически инжектированных приложений, а также для кода мониторинга RUM и Session Replay.

Чтобы задать пользовательский префикс имени файла кода мониторинга:

1. Перейдите в **Settings** > **Web and mobile monitoring** > **RUM monitoring code filename**.
2. В поле **Custom filename prefix** введите желаемый пользовательский префикс.