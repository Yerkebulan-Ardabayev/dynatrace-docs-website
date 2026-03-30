---
title: Адаптация правил CSP для нового опыта RUM
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/adapt-csp-rules
scraped: 2026-03-05T21:31:37.283802
---

# Адаптация правил CSP для New RUM Experience


* Latest Dynatrace

[Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) — это веб-стандарт, предназначенный для защиты приложений от межсайтового скриптинга и других атак с внедрением кода. Правила CSP чаще всего определяются с помощью заголовка ответа `Content-Security-Policy`. Кроме того, их можно задать с помощью тега `<meta>`, размещённого в разделе `<head>` HTML-документа.

Если в вашем приложении настроены правила CSP, они могут блокировать выполнение RUM JavaScript или препятствовать отправке RUM-маяков (beacon) на конечную точку маяков.
На этой странице описано, как изменить CSP, чтобы обеспечить корректную работу RUM.

Использование CSP nonce и хешей не поддерживается для RUM JavaScript. Если вам необходимо проверить целостность кода мониторинга RUM, мы рекомендуем вместо этого использовать Subresource Integrity (SRI). Подробнее см. Использование Subresource Integrity (SRI) в New RUM Experience browser feature in the New RUM Experience to ensure the integrity of Real User Monitoring code.").

## Разрешение загрузки внешнего кода мониторинга

Если вы не используете формат фрагмента [встроенный код](snippet-formats.md#inline-code "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.") и Session Replay Classic отключён, как минимум часть кода мониторинга включается в ваше приложение как внешний файл. Для обеспечения корректной работы ваши правила CSP должны разрешать загрузку и выполнение скриптов из источника кода мониторинга RUM.

* Для **безагентных фронтендов** код мониторинга загружается из Dynatrace CDN.
* Для **автоматического внедрения** код мониторинга по умолчанию обслуживается OneAgent, который инструментирует ваш веб-сервер или сервер приложений. Однако вы можете настроить его загрузку из Dynatrace CDN. Подробнее см. [Запрос кода мониторинга из Dynatrace CDN](configure-monitoring-code-source.md#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring code source in the New RUM Experience to meet your specific requirements.").
* Если [RUM JavaScript вставлен вручную, хотя ваши группы процессов инструментированы OneAgent](configure-auto-injection.md#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your frontends in the New RUM Experience."), используется источник кода, настроенный для автоматического внедрения. Единственное исключение — формат фрагмента [JavaScript-тег](snippet-formats.md#js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."), который всегда загружает код мониторинга из Dynatrace CDN.

Чтобы разрешить загрузку и выполнение кода мониторинга, директива `script-src` в ваших правилах CSP должна включать ключевое слово `'self'`, если код обслуживается OneAgent, и `https://js-cdn.dynatracelabs.com`, если он обслуживается из Dynatrace CDN.

## Разрешение выполнения встроенного кода

Если вы используете формат фрагмента [встроенный код](snippet-formats.md#inline-code "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."), директива `script-src` в ваших правилах CSP должна включать ключевое слово `'unsafe-inline'`, чтобы разрешить выполнение кода мониторинга.

## Разрешение отправки RUM-маяков

RUM-маяки отправляются на конечную точку маяков (beacon endpoint), при этом конечная точка по умолчанию зависит от типа фронтенда:

* Для **безагентных фронтендов** маяки по умолчанию отправляются на Cluster ActiveGate, являющийся частью инфраструктуры Dynatrace SaaS.
* Для **автоматически инструментированных фронтендов** маяки по умолчанию отправляются на OneAgent, который инструментирует веб-сервер или сервер приложений, на котором размещено приложение.

Альтернативные конфигурации описаны в разделе Настройка конечной точки маяков для веб-фронтендов в New RUM Experience.

Чтобы разрешить RUM JavaScript отправлять маяки, убедитесь, что ваши правила CSP включают соответствующую конечную точку в директиве `connect-src`.

* Используйте ключевое слово `'self'`, если конечной точкой маяков является OneAgent, инструментирующий приложение.
* Если вы настроили OneAgent, инструментирующий другой веб-сервер, в качестве конечной точки маяков, укажите соответствующий URL.
* Если маяки обрабатываются Cluster ActiveGate, используйте URL конечной точки маяков, отображаемый в пользовательском интерфейсе.

Как найти URL для Cluster ActiveGate

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Выберите **Web** для просмотра всех веб-фронтендов.
3. Выберите фронтенд.
4. На вкладке **Settings** выберите ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
5. Перейдите в **Collect and capture** > **Frontend** > **Beacon endpoint**.
6. Скопируйте URL рядом с **Configured beacon endpoint**.

## Разрешение Session Replay Classic

Если вы используете Session Replay Classic, ваши правила CSP должны разрешать RUM JavaScript загружать код в виде blob. Подробнее см. Изменение Content Security Policy для Session Replay.

Кроме того, даже если вы используете формат фрагмента [встроенный код](snippet-formats.md#inline-code "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."), убедитесь, что ваши правила CSP [разрешают загрузку внешнего кода мониторинга](#allow-external-monitoring-code). Это важно, поскольку код мониторинга для Session Replay Classic всегда запрашивается как внешний файл, независимо от формата фрагмента.

## Примеры

Ниже приведён базовый пример простого правила CSP:

```
Content-Security-Policy: script-src 'self'; connect-src 'self';
```

Следующие примеры показывают, как это правило необходимо адаптировать для различных сценариев RUM.

Примеры для автоматического внедрения

Если вы используете автоматическое внедрение с конфигурацией по умолчанию для конечной точки маяков и источника кода мониторинга, базового правила CSP, указанного выше, достаточно — при условии, что Session Replay Classic не включён и используется формат фрагмента [OneAgent JavaScript tag](snippet-formats.md#oneagent-js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.").

Если формат фрагмента изменён на встроенный код, необходимо разрешить встроенные скрипты, добавив `'unsafe-inline'`:

```
Content-Security-Policy: script-src 'self' 'unsafe-inline'; connect-src 'self';
```

Если код мониторинга загружается из CDN, обновите директиву `script-src` соответствующим образом:

```
Content-Security-Policy: script-src 'self' https://js-cdn.dynatracelabs.com; connect-src 'self';
```

Если конечная точка маяков изменена на Cluster ActiveGate, обновите директиву `connect-src`:

```
Content-Security-Policy: script-src 'self'; connect-src 'self' https://ab12345cde.bf.dynatrace.com/bf;
```

Если вы используете Session Replay Classic, вам также необходимо настроить директиву `worker-src`:

```
Content-Security-Policy: script-src 'self'; connect-src 'self';  worker-src blob:;
```

Примеры для безагентного мониторинга

Для безагентного мониторинга необходимо настроить как `script-src`, так и `connect-src`:

```
Content-Security-Policy: script-src 'self' https://js-cdn.dynatracelabs.com; connect-src 'self' https://ab12345cde.bf.dynatrace.com/bf;
```

Если вы используете встроенный код, включите `'unsafe-inline'` в `script-src`:

```
Content-Security-Policy: script-src 'self' 'unsafe-inline'; connect-src 'self' https://ab12345cde.bf.dynatrace.com/bf;
```

Если маяки отправляются на инструментированный веб-сервер или сервер приложений, включите его URL в `connect-src`:

```
Content-Security-Policy: script-src 'self' https://js-cdn.dynatracelabs.com; connect-src 'self' http://www.example.com/rb_abcdefghi;
```

Если вы используете Session Replay Classic, необходимо настроить директиву `worker-src`:

```
Content-Security-Policy: script-src 'self' https://js-cdn.dynatracelabs.com; connect-src 'self' https://ab12345cde.bf.dynatrace.com/bf; worker-src blob:;
```

Если вы используете Session Replay Classic с форматом встроенного кода, необходимо настроить директиву `worker-src` и включить как `'unsafe-inline'`, так и URL источника кода в `script-src`:

```
Content-Security-Policy: script-src 'self' https://js-cdn.dynatracelabs.com 'unsafe-inline'; connect-src 'self' https://ab12345cde.bf.dynatrace.com/bf; worker-src blob:;
```