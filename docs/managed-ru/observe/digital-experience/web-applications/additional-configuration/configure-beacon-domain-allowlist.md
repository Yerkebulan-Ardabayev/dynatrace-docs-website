---
title: Настройка allowlist источников маяков для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist
scraped: 2026-05-12T11:19:43.824004
---

# Настройка allowlist источников маяков для веб-приложений

# Настройка allowlist источников маяков для веб-приложений

* How-to guide
* 3-min read
* Updated on Jan 23, 2024

Используйте allowlist источников маяков, чтобы задать источники, с которых [конечные точки маяков вашего приложения](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") должны принимать межисточниковые RUM-маяки.

## Маяки одного и разных источников

RUM JavaScript отправляет RUM-маяки для передачи собранных данных в Dynatrace. В зависимости от метода инъекции существуют два стандартных варианта:

* **Приложения с автоматической инъекцией > маяки одного источника**

  Когда [RUM JavaScript инжектируется автоматически](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), RUM-маяки отправляются обратно на веб-сервер или сервер приложений, на котором размещено приложение с автоматической инъекцией; OneAgent предоставляет конечную точку маяка.

  По умолчанию маяки приложений с автоматической инъекцией являются **маяками одного источника**, поскольку протокол, хост и порт запросов маяков совпадают со страницей, с которой они отправляются.

  Если выбрана одна из [альтернативных конфигураций конечной точки маяка](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server."), при которой маяки приложения с автоматической инъекцией отправляются в Cluster ActiveGate или на инструментированный сервер на другом домене, RUM-маяки являются **межисточниковыми маяками**.
* **Безагентные приложения > межисточниковые маяки**

  При использовании [безагентного мониторинга](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") RUM-маяки отправляются на конечную точку маяка, являющуюся частью Cluster ActiveGate.

  Для безагентных приложений RUM-маяки являются **межисточниковыми**, поскольку отправляются на другой домен.

Браузеры соблюдают политику одного источника, которая по умолчанию позволяет скриптам отправлять запросы только к тому же источнику. Для отправки межисточниковых запросов необходимо использовать Cross-Origin Resource Sharing (CORS), который позволяет серверам указывать источники, которым разрешён доступ к серверу. Таким образом, межисточниковые RUM-маяки должны использовать CORS. В этом случае:

* Браузер добавляет заголовок `Origin` к межисточниковому маяку.
* По умолчанию конечная точка маяка добавляет заголовок `Access-Control-Allow-Origin` к каждому ответу, разрешающий источник, указанный в заголовке `Origin`.

С помощью allowlist источников маяков можно указать, с каких источников конечные точки маяков должны принимать RUM-маяки.

## Указание источников маяков для CORS

Создайте правило источника маяка, чтобы указать, с каких источников OneAgent и Cluster ActiveGate должны принимать RUM-маяки.

Сразу после добавления первого правила источника маяка приложения, не соответствующие этому правилу, прекратят сбор данных RUM, если только их маяки не отправляются из того же источника и не обрабатываются OneAgent.

Чтобы добавить правило источника маяка:

1. Перейдите в **Settings** > **Web and mobile monitoring** > **Beacon origins for CORS**.
2. Выберите **Add item**.
3. Укажите правильный шаблон для источника, который нужно задать.

   ![Добавление правила источника маяка](https://dt-cdn.net/images/add-beacon-origin-rule-1912-783d3ea903.png)

   Добавление правила источника маяка

Можно добавить до 20 правил источников маяков на одну среду.

## Применение allowlist источников маяков в различных сценариях

![Блок-схема allowlist источников маяков](https://dt-cdn.net/images/beacon-origin-allowlist-after-settings-conversion-716-6a55b387ba.png)

Блок-схема allowlist источников маяков

На данной блок-схеме показано, как Dynatrace применяет allowlist источников маяков в различных сценариях. Используйте её, чтобы понять, разрешён ли конкретный источник маяков.

* Если allowlist источников маяков пуст, RUM-маяки из любого источника принимаются всеми конечными точками маяков.
* Если источник включён в allowlist, RUM-маяк с этого источника принимается. В межисточниковом случае источник копируется в заголовок `Access-Control-Allow-Origin` ответа, и ответ на маяк возвращает HTTP-статус `200 OK`.
* Если источник не включён в allowlist, межисточниковый RUM-маяк с этого источника отклоняется. Маяк завершается с кодом статуса `403 Forbidden` и сообщением вида `Value in Origin Header is not allowed`.
* OneAgent не применяет allowlist источников маяков к маякам одного источника.