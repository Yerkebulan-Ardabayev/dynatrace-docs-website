---
title: Настройка источника кода Real User Monitoring Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-monitoring-code-source
---

# Настройка источника кода Real User Monitoring Classic

# Настройка источника кода Real User Monitoring Classic

* Практическое руководство
* Чтение 4 мин
* Обновлено 21 нояб. 2025 г.

В большинстве сценариев RUM браузер отправляет как минимум один дополнительный запрос за кодом мониторинга:

* Все форматы сниппетов, кроме [встроенного кода](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case"), включают код мониторинга в виде внешнего ресурса, который браузер запрашивает отдельно.
* Код мониторинга для Session Replay всегда запрашивается отдельно, даже если используемый формат тега, встроенный код.

URL-адрес запрашиваемого кода мониторинга по умолчанию зависит от метода внедрения, используемого для приложения.

* **Приложения без агента:** если выбран [мониторинг без агента](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."), код мониторинга запрашивается с CDN. В непроизводственных средах вместо этого можно использовать ActiveGate кластера. В случае формата тега [JavaScript tag](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") имя файла заканчивается на `_complete.js` и содержит идентификатор приложения (например, `7cab1abeacdfe1_complete.js`). Для всех остальных форматов оно начинается с `ruxitagent_` и содержит информацию об активных модулях кода и версии кода мониторинга (например, `ruxitagent_ICA7NQVfqrtux_10307250124095659.js`). Имя файла кода мониторинга Session Replay начинается с `ruxitagent_` (например, `ruxitagent_D_10307250124095659.js`) для всех форматов тегов.
* **Автоматическое внедрение:** если [JavaScript RUM внедряется автоматически](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), код мониторинга как RUM, так и Session Replay запрашивается с веб-сервера или сервера приложений с использованием URL-адреса относительно корня, где имя файла начинается с `ruxitagentjs_` и содержит информацию об активных модулях кода и версии кода мониторинга (например, `/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js` или `/myapplication/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`).
* **Ручная вставка для страниц приложения с автоматическим внедрением:** если [JavaScript RUM вставляется вручную, даже если группы процессов инструментированы с помощью OneAgent](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"), код мониторинга, как и при автоматическом внедрении, запрашивается с веб-сервера или сервера приложений с использованием URL-адреса относительно корня, где имя файла начинается с `ruxitagentjs_`. Единственное исключение здесь, формат тега JavaScript tag, при котором код мониторинга RUM запрашивается с CDN, а имя файла заканчивается на `_complete.js`. Код мониторинга Session Replay запрашивается с веб-сервера или сервера приложений и имеет имя файла, начинающееся с `ruxitagentjs_`, для всех форматов тегов.

Обычно делать это не требуется, но есть определённые сценарии, в которых может понадобиться альтернативная конфигурация источника кода мониторинга. Например:

* Если инфраструктура блокирует запросы кода мониторинга приложения с автоматическим внедрением из-за пути URL по умолчанию.
* Если предпочтительно, чтобы запросы кода мониторинга не обрабатывались веб-сервером или сервером приложений, на котором размещено приложение.
* Если нужно предотвратить блокировку кода мониторинга блокировщиками рекламы.

В следующих разделах описаны альтернативные конфигурации, позволяющие учесть эти ограничения.

## Приложение с автоматическим внедрением. Изменение пути URL кода мониторинга

В зависимости от инфраструктуры и её конфигурации возможно, что запросы кода мониторинга не могут пройти с автоматически выбранным путём URL и поэтому не могут быть обработаны OneAgent. Чтобы решить эту проблему, можно изменить часть URL, которая идёт перед префиксом `ruxitagentjs_`.

Чтобы изменить путь URL кода мониторинга RUM для приложения с автоматическим внедрением

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В верхнем правом углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Injection** > **Automatic injection**.
5. В раскрывающемся списке **Источник кода Real User Monitoring** выбрать **OneAgent**.
6. В поле **Specify path for RUM monitoring code** ввести относительный путь URL кода мониторинга.

Обратите внимание, что нельзя убрать сегмент пути с префиксом `ruxitagentjs_`, который необходим для идентификации запроса как запроса кода мониторинга.

#### Примеры

В следующих примерах предполагается, что код мониторинга по умолчанию запрашивается с `/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`.

* **URL относительно корня:** если настроен путь `/custompath`, код мониторинга будет запрашиваться с `/custompath/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`.
* **Относительный URL:** если настроен путь `./`, URL, с которого запрашивается код мониторинга, относителен текущей странице. Например:

  + Если текущая страница `/shop/index.html`, то код мониторинга запрашивается с `/shop/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`.
  + Если текущая страница `/account/dashboard/`, то код мониторинга запрашивается с `/account/dashboard/ruxitagentjs_ICA7NQVfqrtux_10307250124095659.js`.

Эта конфигурация действует не только для автоматического внедрения, но и для [ручной вставки для страниц приложения с автоматическим внедрением](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"). Единственное исключение, запрос `_complete.js` для формата тега JavaScript tag, который по-прежнему будет отправляться на CDN или ActiveGate кластера.

## Приложение с автоматическим внедрением. Запрос кода мониторинга с CDN

Обратите внимание, что все подключённые ActiveGate должны иметь версию ActiveGate 1.310+ в течение как минимум 30 дней, прежде чем эта функция станет доступна.

Если нужно, чтобы код мониторинга для приложения с автоматическим внедрением запрашивался с CDN или ActiveGate кластера, настроенного как описано в разделе [Настройка мониторинга без агента Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."), вместо OneAgent, выполните шаги ниже.

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В верхнем правом углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Injection** > **Automatic injection**.
5. В раскрывающемся списке **Источник кода Real User Monitoring** выбрать **CDN**.

Эта конфигурация действует как для автоматического внедрения, так и для [ручной вставки для страниц приложения с автоматическим внедрением](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"). При её использовании имена файлов, которые ранее начинались с `ruxitagentjs_`, будут начинаться с `ruxitagent_`.

## Настройка пользовательского префикса имени файла кода мониторинга

После изменения префикса имени файла кода мониторинга может временно снизиться объём собираемых данных RUM. Поэтому рекомендуется избегать частых изменений этой настройки.

По умолчанию имя файла кода мониторинга имеет префикс `ruxitagent` или `ruxitagentjs`, если не используется формат тега JavaScript tag. Также можно указать пользовательский префикс, который будет использоваться вместо него как для приложений без агента, так и для приложений с автоматическим внедрением, а также для кода мониторинга RUM и Session Replay.

Чтобы указать пользовательский префикс имени файла кода мониторинга

1. Перейти в **Settings** > **Web and mobile monitoring** > **RUM monitoring code filename**.
2. В поле **Custom filename prefix** ввести нужный пользовательский префикс.