---
title: Configure the beacon endpoint for web frontends in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-beacon-endpoint
scraped: 2026-03-06T21:35:43.809096
---

# Настройка конечной точки beacon для веб-фронтендов в New RUM Experience

# Настройка конечной точки beacon для веб-фронтендов в New RUM Experience

* Последняя версия Dynatrace
* Практическое руководство
* Обновлено 7 января 2026

RUM JavaScript отправляет beacon-сигналы в Dynatrace для передачи собранных данных. URL-адрес, на который доставляются эти beacon-сигналы, определяется конечной точкой beacon. В этом руководстве описана конечная точка beacon по умолчанию, подходящая для большинства сред, а затем перечислены доступные параметры конфигурации для сценариев, требующих настройки.

## Конечная точка beacon по умолчанию

По умолчанию конечная точка beacon зависит от метода инструментации, используемого для вашего приложения:

### Автоматически инжектируемые фронтенды

Если [RUM JavaScript инжектируется автоматически](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience."), beacon-сигналы отправляются на ваш веб-сервер или сервер приложений, где OneAgent предоставляет конечную точку beacon, которая перехватывает и перенаправляет их. Для этого используется относительный URL от корня, последний сегмент пути которого начинается с префикса `rb_`. Точный путь URL зависит от технологии:

* **Java или IIS:** Сегмент пути добавляется к корневому контексту, если он доступен, например: `/myapplication/rb_bf12345abc`.
* **Другие технологии или когда корневой контекст недоступен:** Сегмент пути добавляется к корню, например: `/rb_bf12345abc`. Это также поведение по умолчанию, если вы вручную вставляете RUM JavaScript, как описано в разделе [Использование ручной вставки для страниц автоматически инжектируемого фронтенда](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-auto-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience.").

### Безагентный мониторинг

Если вы используете [безагентный мониторинг](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring "Learn how to set up agentless RUM for your web frontends in the New RUM Experience."), данные отправляются на Cluster ActiveGate, который является частью SaaS-инфраструктуры Dynatrace.

## Параметры конфигурации

В определенных сценариях может потребоваться использование альтернативной конфигурации конечной точки beacon. Например:

* Если ваша инфраструктура блокирует beacon-сигналы автоматически инжектируемого фронтенда из-за их URL-пути по умолчанию.
* Если вы хотите, чтобы трафик мониторинга автоматически инжектируемого фронтенда обходил ваш CDN.
* Если вы предпочитаете, чтобы RUM beacon-сигналы не обрабатывались на веб-сервере или сервере приложений, на котором размещено ваше приложение.

В следующих разделах описаны альтернативные конфигурации конечной точки beacon, которые позволяют учесть эти и подобные ограничения.

### Автоматически инжектируемый фронтенд: изменение URL-пути конечной точки beacon

В зависимости от вашей инфраструктуры и ее конфигурации beacon-сигналы могут не проходить с автоматически выбранным URL и, следовательно, не могут быть обработаны OneAgent. Чтобы решить эту проблему, вы можете изменить часть URL-пути конечной точки beacon, которая идет перед префиксом `rb_`. Вы не можете удалить сегмент пути с префиксом `rb_`, так как он необходим для идентификации RUM beacon-сигналов агентом OneAgent.

Чтобы изменить URL конечной точки beacon для автоматически инжектируемого приложения

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Выберите **Web** для просмотра всех веб-фронтендов.
3. Выберите фронтенд, который хотите настроить.
4. На вкладке **Settings** выберите ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
5. Перейдите в **Collect and capture** > **Frontend** > **Beacon endpoint**.
6. В выпадающем списке **Type** выберите **OneAgent**.
7. В поле **URL** введите относительный URL или URL, относительный от корня.
8. Выберите **Save changes**.

#### Примеры

В следующих примерах предполагается, что RUM beacon-сигналы по умолчанию отправляются на `/rb_bf12345abc`.

* **URL, относительный от корня:** Если вы установите **URL** в значение `/custompath`, beacon-сигналы будут отправляться на `/custompath/rb_bf12345abc`.
* **Относительный URL:** Если вы установите **URL** в значение `./`, то URL, на который RUM JavaScript отправляет beacon-сигналы, будет относительным к текущей странице. Например:

  + Если текущая страница `/shop/index.html`, то beacon-сигналы отправляются на `/shop/rb_bf12345abc`.
  + Если текущая страница `/account/dashboard/`, то beacon-сигналы отправляются на `/account/dashboard/rb_bf12345abc`.

### Автоматически инжектируемый фронтенд: отправка beacon-сигналов в SaaS-инфраструктуру Dynatrace

Если вы хотите, чтобы RUM beacon-сигналы автоматически инжектируемого фронтенда обрабатывались SaaS-инфраструктурой Dynatrace вместо OneAgent, выполните следующие шаги.

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Выберите **Web** для просмотра всех веб-фронтендов.
3. Выберите фронтенд, который хотите настроить.
4. На вкладке **Settings** выберите ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
5. Перейдите в **Collect and capture** > **Frontend** > **Beacon endpoint**.
6. В выпадающем списке **Type** выберите **Cluster ActiveGate**.
7. Выберите **Save changes**.

При такой конфигурации Dynatrace применяет [список разрешенных источников beacon](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/configure-beacon-origin-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") к RUM beacon-сигналам вашего фронтенда.

### Автоматически инжектируемый фронтенд: отправка beacon-сигналов на другой веб-сервер

По умолчанию RUM beacon-сигналы автоматически инжектируемого фронтенда обрабатываются агентом OneAgent на одной из групп процессов, обслуживающих ваше приложение. В качестве альтернативы beacon-сигналы могут обрабатываться на любом другом инструментированном веб-сервере или сервере приложений технологии, указанной в [Поддержка технологий - Real User Monitoring - Веб-серверы и приложения](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Чтобы отправить beacon-сигналы автоматически инжектируемого фронтенда на другой инструментированный сервер

1. В инжектированном RUM JavaScript найдите `beaconUri` и скопируйте последний сегмент URL-пути, который начинается с `rb_`.
2. Добавьте это значение к URL инструментированного веб-сервера или сервера приложений.

   Например, если последний сегмент `beaconUri` равен `/rb_bf12345abc`, а URL сервера равен `http://www.my-server.com`, результирующий URL конечной точки beacon будет `http://www.my-server.com/rb_bf12345abc`.
3. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
4. Выберите **Web** для просмотра всех веб-фронтендов.
5. Выберите фронтенд, который хотите настроить.
6. На вкладке **Settings** выберите ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
7. Перейдите в **Collect and capture** > **Frontend** > **Beacon endpoint**.
8. В выпадающем списке **Type** выберите **OneAgent**.
9. В поле **URL** введите конечную точку beacon, определенную на шаге 2.
10. Включите **Send beacon data via CORS**.
11. Выберите **Save changes**.

При такой конфигурации Dynatrace применяет [список разрешенных источников beacon](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/configure-beacon-origin-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") к RUM beacon-сигналам вашего фронтенда.
