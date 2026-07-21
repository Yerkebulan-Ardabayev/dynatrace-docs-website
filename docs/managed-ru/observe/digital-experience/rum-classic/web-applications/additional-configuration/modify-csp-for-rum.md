---
title: Изменение Content Security Policy для RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/modify-csp-for-rum
---

# Изменение Content Security Policy для RUM Classic

# Изменение Content Security Policy для RUM Classic

* Практическое руководство
* 5 мин чтения
* Обновлено 13 марта 2026 г.

[Content Security Policy (CSP)﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP), это веб-стандарт, разработанный для защиты приложений от межсайтового скриптинга и других атак с внедрением кода. Правила CSP чаще всего задаются с помощью заголовка ответа `Content-Security-Policy`. Также их можно задать с помощью тега `<meta>`, размещённого в разделе `<head>` HTML-документа.

Если в приложении заданы правила CSP, они могут блокировать выполнение RUM JavaScript или мешать отправке RUM beacon'ов на конечную точку beacon. На этой странице объясняется, как изменить CSP, чтобы RUM мог работать как задумано.

Использование CSP-nonce и хешей для RUM JavaScript не поддерживается. Если нужно проверить целостность кода мониторинга RUM, рекомендуется использовать вместо этого Subresource Integrity (SRI). Подробнее см. [Использование Subresource Integrity (SRI) для кода Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring Classic code.").

## Разрешение загрузки внешнего кода мониторинга

Если не используется формат сниппета [inline code](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") с отключённым Session Replay, хотя бы часть кода мониторинга включается в приложение в виде внешнего файла. Чтобы обеспечить корректную работу, правила CSP должны разрешать загрузку и выполнение скриптов из [источника кода мониторинга RUM](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-monitoring-code-source "Configure the Real User Monitoring Classic code source for your specific requirements.").

* Для **приложений без агента (agentless)** код мониторинга загружается из CDN.
* Для **автоматического внедрения (automatic injection)** код мониторинга по умолчанию предоставляется OneAgent, который инструментирует веб-сервер или сервер приложений. Однако его можно настроить так, чтобы он загружался из CDN. Подробнее см. [Запрос кода мониторинга из CDN](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring Classic code source for your specific requirements.").
* Если [RUM JavaScript вставляется вручную, даже несмотря на то, что группы процессов инструментированы OneAgent](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"), используется источник кода, настроенный для автоматического внедрения. Единственное исключение, формат сниппета [JavaScript tag](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case"), который всегда загружает код мониторинга из CDN.

Чтобы разрешить загрузку и выполнение кода мониторинга, директива `script-src` в правилах CSP должна включать ключевое слово `'self'`, если код предоставляется OneAgent, и URL CDN, если код мониторинга предоставляется оттуда.

## Разрешение выполнения инлайн-кода

Если используются форматы сниппета [inline code](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") или [code snippet](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#code-snippet "Select a format for the RUM JavaScript snippet that best fits your specific use case"), директива `script-src` в правилах CSP должна включать ключевое слово `'unsafe-inline'`, чтобы разрешить выполнение кода мониторинга.

## Разрешение отправки RUM beacon'ов

RUM beacon'ы отправляются на конечную точку beacon, при этом конечная точка по умолчанию зависит от типа приложения:

* Для **приложений без агента (agentless)** beacon'ы по умолчанию отправляются на Cluster ActiveGate.
* Для **приложений с автоматическим внедрением** beacon'ы по умолчанию отправляются на OneAgent, который инструментирует веб-сервер или сервер приложений, на котором размещено приложение.

Альтернативные варианты настройки описаны в [Настройка конечной точки beacon для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.").

Чтобы разрешить RUM JavaScript отправлять beacon'ы, нужно убедиться, что правила CSP включают соответствующую конечную точку в директиве `connect-src`.

* Используйте ключевое слово `'self'`, если конечная точка beacon, это OneAgent, который инструментирует приложение.
* Если в качестве конечной точки beacon настроен OneAgent, инструментирующий другой веб-сервер, укажите соответствующий URL.
* Если beacon'ы обрабатываются Cluster ActiveGate, используйте URL конечной точки beacon, показанный в интерфейсе.

Как найти URL для Cluster ActiveGate

1. Перейдите в раздел **Web**.
2. Выберите приложение, для которого настраиваются правила CSP.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **General settings** > **Beacon endpoint**.
5. Скопируйте URL рядом с полем **Configured beacon endpoint**.

## Разрешение Session Replay

Если используется Session Replay, правила CSP должны разрешать RUM JavaScript загружать код в виде blob. Подробнее см. [Изменение Content Security Policy для Session Replay](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-csp "Configure monitoring consumption and data privacy settings for Session Replay Classic.").

Кроме того, даже при использовании формата сниппета [inline code](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") нужно убедиться, что правила CSP [разрешают загрузку внешнего кода мониторинга](#allow-external-monitoring-code). Это важно, поскольку код мониторинга для Session Replay всегда запрашивается как внешний файл, независимо от формата сниппета.

## Примеры

Ниже базовый пример простого правила CSP:

```
Content-Security-Policy: script-src 'self'; connect-src 'self';
```

Следующие примеры показывают, как адаптировать это правило для разных сценариев RUM.

Примеры для автоматического внедрения

Если используется автоматическое внедрение с конфигурацией по умолчанию как для конечной точки бикона, так и для источника кода мониторинга, приведённого выше базового правила CSP достаточно, при условии что Session Replay не включён, а используется формат сниппета [OneAgent JavaScript tag](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case").

Если формат сниппета изменён на inline code или code snippet, нужно разрешить встроенные скрипты, добавив `'unsafe-inline'`:

```
Content-Security-Policy: script-src 'self' 'unsafe-inline'; connect-src 'self';
```

Если код мониторинга загружается с CDN, нужно соответствующим образом обновить директиву `script-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self';
```

Если конечная точка бикона изменена на Cluster ActiveGate, нужно обновить директиву `connect-src`:

```
Content-Security-Policy: script-src 'self'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

Если используется Session Replay, также нужно настроить директиву `worker-src`:

```
Content-Security-Policy: script-src 'self'; connect-src 'self';  worker-src blob:;
```

Примеры для agentless-мониторинга

Для agentless-мониторинга нужно скорректировать и `script-src`, и `connect-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

Если используется inline code, нужно включить `'unsafe-inline'` в `script-src`:

```
Content-Security-Policy: script-src 'self' 'unsafe-inline'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

Если используется формат code snippet, нужно включить в `script-src` и `'unsafe-inline'`, и URL источника кода:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com 'unsafe-inline'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

Если биконы отправляются на инструментированный веб- или app-сервер, нужно включить его URL в `connect-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self' http://www.example.com/rb_abcdefghi;
```

Если используется Session Replay, нужно настроить директиву `worker-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2; worker-src blob:;
```

Если используется Session Replay с форматом code snippet или inline code, нужно настроить директиву `worker-src` и включить в `script-src` и `'unsafe-inline'`, и URL источника кода:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com 'unsafe-inline'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2; worker-src blob:;
```