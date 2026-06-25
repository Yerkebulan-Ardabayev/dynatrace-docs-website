---
title: Изменение Content Security Policy для RUM
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/modify-csp-for-rum
scraped: 2026-05-12T11:34:29.332705
---

# Изменение Content Security Policy для RUM

# Изменение Content Security Policy для RUM

* How-to guide
* 5-min read
* Updated on Mar 13, 2026

[Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) — веб-стандарт, защищающий приложения от межсайтового скриптинга и других атак с внедрением кода. Правила CSP чаще всего задаются с помощью заголовка ответа `Content-Security-Policy`. Кроме того, их можно задать с помощью тега `<meta>`, размещённого в разделе `<head>` HTML-документа.

Если в приложении настроены правила CSP, они могут блокировать выполнение RUM JavaScript или предотвращать отправку RUM-маяков на конечную точку маяка.
На этой странице описано, как изменить CSP для обеспечения корректной работы RUM.

Использование одноразовых значений (nonce) и хешей CSP не поддерживается для RUM JavaScript. Если необходимо проверить целостность кода мониторинга RUM, рекомендуется использовать Subresource Integrity (SRI). Подробнее см. раздел [Использование Subresource Integrity (SRI) для кода Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring code.").

## Разрешение загрузки внешнего кода мониторинга

Если только не используется формат сниппета [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") с отключённым Session Replay, хотя бы часть кода мониторинга включается в приложение как внешний файл. Для корректной работы правила CSP должны разрешать загрузку и выполнение скриптов из [источника кода мониторинга RUM](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source "Configure the Real User Monitoring code source for your specific requirements.").

* Для **безагентных приложений** код мониторинга загружается из вашего CDN.
* При **автоматической инъекции** код мониторинга по умолчанию предоставляется OneAgent, инструментирующим веб-сервер или сервер приложений. Однако его можно настроить для загрузки из CDN. Подробнее см. раздел [Запрос кода мониторинга из CDN](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring code source for your specific requirements.").
* Если [RUM JavaScript вставляется вручную, несмотря на то что группы процессов инструментированы OneAgent](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications"), используется источник кода, настроенный для автоматической инъекции. Единственное исключение — формат сниппета [JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case"), который всегда загружает код мониторинга из CDN.

Чтобы разрешить загрузку и выполнение кода мониторинга, директива `script-src` в правилах CSP должна включать ключевое слово `'self'`, если код предоставляется OneAgent, и URL вашего CDN, если код мониторинга загружается оттуда.

## Разрешение выполнения встроенного кода

При использовании форматов сниппетов [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") или [code snippet](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#code-snippet "Select a format for the RUM JavaScript snippet that best fits your specific use case") директива `script-src` в правилах CSP должна включать ключевое слово `'unsafe-inline'` для разрешения выполнения кода мониторинга.

## Разрешение отправки RUM-маяков

RUM-маяки отправляются на конечную точку маяка, стандартная конечная точка которой зависит от типа приложения:

* Для **безагентных приложений** маяки по умолчанию отправляются в Cluster ActiveGate.
* Для **автоматически инжектированных приложений** маяки по умолчанию отправляются на OneAgent, инструментирующий веб-сервер или сервер приложений, на котором размещено приложение.

Альтернативные варианты настройки описаны в разделе [Настройка конечной точки маяка для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.").

Чтобы разрешить RUM JavaScript отправлять маяки, правила CSP должны включать соответствующую конечную точку в директиву `connect-src`.

* Используйте ключевое слово `'self'`, если конечная точка маяка — OneAgent, инструментирующий приложение.
* Если в качестве конечной точки маяка настроен OneAgent, инструментирующий другой веб-сервер, укажите соответствующий URL.
* Если маяки обрабатываются Cluster ActiveGate, используйте URL конечной точки маяка, отображаемый в UI.

Чтобы найти URL для Cluster ActiveGate:

1. Перейдите в **Web**.
2. Выберите приложение, для которого настраиваются правила CSP.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **General settings** > **Beacon endpoint**.
5. Скопируйте URL рядом с **Configured beacon endpoint**.

## Разрешение Session Replay

При использовании Session Replay правила CSP должны разрешать RUM JavaScript загружать код в виде blob. Подробнее см. раздел [Изменение Content Security Policy для Session Replay](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-csp "Configure monitoring consumption and data privacy settings for Session Replay.").

Кроме того, даже при использовании формата сниппета [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") убедитесь, что правила CSP [разрешают загрузку внешнего кода мониторинга](#allow-external-monitoring-code). Это важно, поскольку код мониторинга для Session Replay всегда запрашивается как внешний файл, независимо от формата сниппета.

## Примеры

Ниже приведён базовый пример простого правила CSP:

```
Content-Security-Policy: script-src 'self'; connect-src 'self';
```

В следующих примерах показано, как адаптировать это правило для различных сценариев RUM.

Примеры для автоматической инъекции

При использовании автоматической инъекции со стандартной конфигурацией как для конечной точки маяка, так и для источника кода мониторинга приведённое выше базовое правило CSP является достаточным — при условии, что Session Replay не включён и используется формат сниппета [OneAgent JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case").

При изменении формата сниппета на inline code или code snippet необходимо разрешить встроенные скрипты, добавив `'unsafe-inline'`:

```
Content-Security-Policy: script-src 'self' 'unsafe-inline'; connect-src 'self';
```

Если код мониторинга загружается из CDN, обновите директиву `script-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self';
```

Если конечная точка маяка изменена на Cluster ActiveGate, обновите директиву `connect-src`:

```
Content-Security-Policy: script-src 'self'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

При использовании Session Replay также необходимо настроить директиву `worker-src`:

```
Content-Security-Policy: script-src 'self'; connect-src 'self';  worker-src blob:;
```

Примеры для безагентного мониторинга

Для безагентного мониторинга необходимо скорректировать как `script-src`, так и `connect-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

При использовании inline code включите `'unsafe-inline'` в `script-src`:

```
Content-Security-Policy: script-src 'self' 'unsafe-inline'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

При использовании формата code snippet включите и `'unsafe-inline'`, и URL источника кода в `script-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com 'unsafe-inline'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2;
```

Если маяки отправляются на инструментированный веб-сервер или сервер приложений, включите его URL в `connect-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self' http://www.example.com/rb_abcdefghi;
```

При использовании Session Replay необходимо настроить директиву `worker-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2; worker-src blob:;
```

При использовании Session Replay с форматом code snippet или inline code необходимо настроить директиву `worker-src` и включить и `'unsafe-inline'`, и URL источника кода в `script-src`:

```
Content-Security-Policy: script-src 'self' https://cdn.example.com 'unsafe-inline'; connect-src 'self' https://abc123.dynatrace-managed.com:9999/bf/785754c9-f3b4-4e9c-aea8-e61405af01b2; worker-src blob:;
```