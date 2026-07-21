---
title: Настройка кэширующих серверов в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-your-caching-servers
---

# Настройка кэширующих серверов в RUM Classic

# Настройка кэширующих серверов в RUM Classic

* Практическое руководство
* 8 минут на чтение
* Опубликовано 19 июля 2017 г.

Использование кэширующего сервера с Dynatrace Real User Monitoring Classic иногда может приводить к неожиданным результатам. Коэффициент попаданий в кэш, близкий к нулю, это самый очевидный симптом проблем, связанных с кэшированием. Чаще всего это происходит при использовании настроек кэширующего сервера по умолчанию.

К счастью, при небольшой настройке кэширующего сервера обычно удаётся сохранить высокий коэффициент попаданий в кэш, не теряя при этом покрытие мониторингом Dynatrace.

## Cookie и кэширующие серверы

По умолчанию серверы кэширования, такие как Varnish Cache, консервативно подходят к определению того, какие данные следует кэшировать. Все запросы, содержащие cookie, и все ответы, включающие заголовок `Set-Cookie`, по умолчанию исключаются из кэша. В основе такого поведения лежит несколько устаревшее предположение, что подобный запрашиваемый контент обычно уникален для конкретного пользователя и поэтому не заслуживает кэширования. Это может создавать проблемы для таких сервисов, как Dynatrace, которые используют cookie для сопоставления веб-запросов с действиями пользователей.

## Обходное решение

Чтобы обойти эту проблему, **кэширующему серверу нужно указать игнорировать связанные с Dynatrace cookie в запросах и ответах**. Важно аккуратно разграничить, для каких запросов cookie Dynatrace нужно отбрасывать, а какие запросы следует кэшировать, чтобы это не повлияло на Real User Monitoring.

При правильно настроенных правилах кэширующего сервера исключение cookie Dynatrace из кэширования не влияет на Real User Monitoring. Однако сообщаемые нагрузки веб-сервера больше не будут соответствовать нагрузкам, сообщаемым для приложений, работающих на этих серверах, поскольку основную часть запросов обрабатывает кэширующий сервер.

## Пример настройки для Varnish Cache

Рассмотрим Varnish Cache в качестве примера того, как можно решить проблемы кэширования в своём окружении.

Это не универсальное решение, подходящее для всех развёртываний: нужно базовое понимание собственного кэширующего сервера, чтобы правильно адаптировать эти инструкции под конфигурацию конкретного сайта.

Varnish Cache (внешняя ссылка: [https://www.varnish-cache.org/﻿](https://www.varnish-cache.org/)) это популярный HTTP-кэширующий сервер и балансировщик нагрузки, который можно гибко настраивать с помощью C-подобного языка VCL (Varnish Configuration Language). Необходимая конфигурация состоит в основном из подпрограмм, которые сервер вызывает в разных точках конвейера обработки запроса.

В примере конфигурации используются три подпрограммы:

| Подпрограмма | Когда вызывается |
| --- | --- |
| `vcl_recv` | Вызывается в начале обработки запроса. |
| `vcl_miss` | Вызывается при промахе кэша. |
| `vcl_backend_response` | Вызывается после получения страницы с исходного сервера из-за промаха кэша. |

В примере используется синтаксис VCL 4.0; для более ранних версий понадобятся небольшие изменения (см. ниже).

1. Нужно убедиться, что cookie Dynatrace отбрасываются до того, как Varnish решит, искать ли запрашиваемый контент в кэше. Для этого используется подпрограмма `vcl_recv`. Важно: маяки мониторинга Dynatrace JavaScript никогда не должны кэшироваться, и cookie в них нужно сохранять. Маяки используют метод запроса POST, поэтому добавление логики, отбрасывающей cookie только для запросов, не являющихся POST, должно решить задачу. Вот код VCL для этого:

   ```
   sub vcl_recv {



   if (req.method != "POST" && req.http.Cookie) {



   set req.http.Cookie = regsuball(req.http.Cookie, "(^|;\s*)dt(Cookie|LatC|PC|VT)=[^;]*", "");



   set req.http.Cookie = regsuball(req.http.Cookie, "(^|;\s*)rx(session|pc|latency|vt)=[^;]*", "");



   set req.http.Cookie = regsub(req.http.Cookie, "^;\s*", "");



   if (req.http.Cookie == "") {



   unset req.http.Cookie;



   }



   }



   }
   ```

   Приведённый выше пример кода делает следующее:

   * Проверяет, является ли запрос POST-запросом и содержит ли он заголовок cookie (для VCL версий до 4.0 вместо `req.method` используется `req.request`).
   * Удаляет все записи cookie, связанные с Dynatrace, с помощью небольшой магии регулярных выражений. Функция `regsuball` заменяет все совпадения с регулярным выражением на строку, переданную ей последним параметром; в данном случае, все экземпляры cookie с именами `dtCookie`, `dtLatC`, `dtPC`, `dtVT`, `rxsession`, `rxpc`, `rxlatency` или `rxvt`.
   * С помощью функции `regsub` гарантирует, что в начале заголовка не остаётся лишней точки с запятой.
   * Проверяет, пуст ли заголовок cookie. Если да, весь заголовок удаляется. Cookie, не относящиеся к Dynatrace, сохраняются и всё ещё могут помешать Varnish отдавать запрашиваемый контент из кэша.
2. Приведённой выше конфигурации Varnish достаточно, чтобы снова включить кэширование, но остаётся ещё одна проблема, которую нужно решить: в случае промаха кэша и последующего обращения к исходному серверу в запрос нужно включить cookie Dynatrace (нужно убедиться, что cookie сохраняются в запросах, которые нельзя обслужить из кэша). Это даёт Dynatrace более полное понимание связей между приложениями и веб-серверами. Для этого конфигурацию нужно расширить следующим образом:

   ```
   sub vcl_recv {



   if (req.method != "POST" && req.http.Cookie) {



   if (req.http.Cookie ~ "(^|;\s*)dt(Cookie|LatC|PC|VT)=[^;]*" || req.http.Cookie ~ "(^|;\s*)rx(session|pc|latency|vt)=[^;]*") {



   set req.http.X-tmp-cookie = req.http.Cookie;



   }



   set req.http.Cookie = regsuball(req.http.Cookie, "(^|;\s*)dt(Cookie|LatC|PC|VT)=[^;]*", "");



   set req.http.Cookie = regsuball(req.http.Cookie, "(^|;\s*)rx(session|pc|latency|vt)=[^;]*", "");



   set req.http.Cookie = regsub(req.http.Cookie, "^;\s*", "");



   if (req.http.Cookie == "") {



   unset req.http.Cookie;



   }



   }



   }



   sub vcl_miss {



   if (req.http.X-tmp-cookie) {



   set req.http.Cookie = req.http.X-tmp-cookie;



   unset req.http.X-tmp-cookie;



   }



   }
   ```

   Приведённый выше пример кода делает следующее:

   * Добавляет условие в подпрограмму `vcl_recv`. Оно сначала проверяет, есть ли в заголовке cookie какие-либо cookie Dynatrace, и если да, весь заголовок cookie копируется во временный заголовок. Далее код, как и прежде, удаляет специфичные для Dynatrace cookie.
   * Добавляет подпрограмму `vcl_miss`, которая вызывается при промахе кэша, непосредственно перед передачей запроса на исходный сервер. Нужно вернуть заголовку cookie исходное состояние, используя резервный временный заголовок, созданный ранее. После этого временный заголовок можно удалить. Теперь для любого запроса, который нельзя обслужить из кэша, cookie Dynatrace останутся нетронутыми.
3. Осталось сделать последнее. Нужно удалить заголовок `Set-Cookie` Dynatrace из ответов исходного сервера, чтобы их можно было кэшировать. Если cookie Dynatrace это единственный устанавливаемый cookie, либо он всегда идёт первым заголовком `Set-Cookie`, можно использовать следующую конфигурацию:

   ```
   sub vcl_backend_response {



   if (beresp.http.Cache-Control !~ "no-cache" && beresp.http.Set-Cookie



   && (beresp.http.Set-Cookie ~ "^dtCookie=.*" || beresp.http.Set-Cookie ~ "^rxsession=.*")) {



   unset beresp.http.Set-Cookie;



   }



   }
   ```

   Подпрограмма `vcl_backend_response` вызывается после получения контента с исходного сервера (в старых версиях VCL она называлась `vcl_fetch`). Перед удалением заголовка `Set-Cookie` нужно сначала убедиться, что он существует и что он связан с Dynatrace. Проверка того, что заголовок `Cache-Control` установлен в `no-cache`, гарантирует, что ответы на запросы маяков Dynatrace остаются нетронутыми. В целом хорошей практикой считается избегать изменения ответов, которые не будут кэшироваться.
4. Если имеется несколько заголовков `Set-Cookie` и нет уверенности, что заголовок Dynatrace идёт первым, нужно альтернативное решение. Из-за ограничений Varnish приведённый выше код учитывает только первый заголовок `Set-Cookie` в ответе, игнорируя остальные. Обойти это можно, установив модуль `libvmod-header`, доступный по адресу [https://github.com/varnish/libvmod-header﻿](https://github.com/varnish/libvmod-header). Этот модуль содержит функцию `remove`, которая удаляет все экземпляры `Set-Cookie`, соответствующие заданному параметру:

   ```
   import header;



   sub vcl_backend_response {



   if (beresp.http.Cache-Control !~ "no-cache") {



   header.remove(beresp.http.Set-Cookie, "dtCookie=");



   header.remove(beresp.http.Set-Cookie, "rxsession=");



   }



   }
   ```

Смотреть полную конфигурацию

Приведённый здесь код предназначен только для справки. Учитывайте, что необходимая конфигурация может отличаться в зависимости от версии Varnish и веб-сайта, который отслеживается. Кэширующие серверы, отличные от Varnish, потребуют аналогичных правил в другом формате.

```
sub vcl_recv {



# let Dynatrace beacons (and other POST stuff) through unmodified



if (req.method != "POST" && req.http.Cookie) {



if (req.http.Cookie ~ "(^|;\s*)dt(Cookie|LatC|PC|VT)=[^;]*" || req.http.Cookie ~ "(^|;\s*)rx(session|pc|latency|vt)=[^;]*") {



# store cookies for a possible cache miss



set req.http.X-tmp-cookie = req.http.Cookie;



}



# remove Dynatrace cookies



set req.http.Cookie = regsuball(req.http.Cookie, "(^|;\s*)dt(Cookie|LatC|PC|VT)=[^;]*", "");



set req.http.Cookie = regsuball(req.http.Cookie, "(^|;\s*)rx(session|pc|latency|vt)=[^;]*", "");



set req.http.Cookie = regsub(req.http.Cookie, "^;\s*", "");



if (req.http.Cookie == "") {



unset req.http.Cookie;



}



}



}



sub vcl_miss {



if (req.http.X-tmp-cookie) {



# set the cookies back

set req.http.Cookie = req.http.X-tmp-cookie;

unset req.http.X-tmp-cookie;

}

}

sub vcl_backend_response {

# NOTE:

# In case of multiple Set-Cookie headers, the following code will not work

# if the Dynatrace cookie is not the first one. In that case, you must

# install the libvmod-header (https://github.com/varnish/libvmod-header)

# and use the following:

# import header;

# sub vcl_backend_response {

#    if (beresp.http.Cache-Control !~ "no-cache") {

#        header.remove(beresp.http.Set-Cookie, "dtCookie=");

#        header.remove(beresp.http.Set-Cookie, "rxsession=");

#    }

# }

if (beresp.http.Cache-Control !~ "no-cache" && beresp.http.Set-Cookie

&& (beresp.http.Set-Cookie ~ "^dtCookie=.*" || beresp.http.Set-Cookie ~ "^rxsession=.*")) {

unset beresp.http.Set-Cookie;

}

}
```

## Проверка конфигурации Varnish Cache

Чтобы убедиться, что конфигурация работает как ожидается, можно использовать программу `varnishlog` для доступа к журналу вывода varnish (см. наш пример, объясняющий как отфильтровать ненужные строки с помощью grep). Ниже приведены пример команды и вывода, показывающие корректно работающую конфигурацию Varnish (полный вывод сокращён для наглядности). Команда выводит каждый запрос (строки `ReqURL`) и итоговые решения кеширования, принятые Varnish.

```
varnishlog | grep -e ReqURL -e "VCL_call\s*HIT" -e "VCL_call\s*MISS" -e "VCL_call\s*PASS"



-   ReqURL         /



-   VCL_call       MISS



-   ReqURL         /ruxitagentjs_2bfnqr_1430399197.js



-   VCL_call       MISS



-   ReqURL         /rb_1



-   VCL_call       PASS



-   ReqURL         /rb_1



-   VCL_call       PASS



-   ReqURL         /



-   VCL_call       HIT



-   ReqURL         /rb_1



-   VCL_call       PASS



-   ReqURL         /ruxitagentjs_2bfnqr_1430399197.js



-   VCL_call       HIT



-   ReqURL         /rb_1



-   VCL_call       PASS
```

Как видно, первый запрос веб-страницы («/») корректно приводит к промаху кеша. Затем страница получается с исходного сервера, и следующий запрос той же страницы приводит к попаданию в кеш. Запросы Dynatrace-маячка (`/rb_1` в этом примере) корректно пропускаются дальше и не рассматриваются для кеширования.