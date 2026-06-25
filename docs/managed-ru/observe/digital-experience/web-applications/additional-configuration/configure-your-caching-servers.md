---
title: Настройка серверов кэширования
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-your-caching-servers
scraped: 2026-05-12T11:34:16.302073
---

# Настройка серверов кэширования

# Настройка серверов кэширования

* How-to guide
* 8-min read
* Published Jul 19, 2017

Использование сервера кэширования совместно с Dynatrace Real User Monitoring иногда может приводить к неожиданным результатам. Наиболее очевидным симптомом проблем с кэшированием является коэффициент попаданий в кэш, близкий к нулю. Чаще всего это происходит при использовании стандартных настроек конфигурации сервера кэширования.

К счастью, с небольшой настройкой сервера кэширования обычно удаётся сохранить высокий коэффициент попаданий в кэш и при этом не терять покрытие мониторинга Dynatrace.

## Cookie и серверы кэширования

По умолчанию серверы кэширования, например Varnish Cache, консервативно подходят к определению данных, которые должны кэшироваться. Все запросы, содержащие cookie, и все ответы, включающие заголовок `Set-Cookie`, по умолчанию исключаются из кэша. За этим поведением стоит несколько устаревшее предположение о том, что такой запрашиваемый контент является пользовательским и поэтому не заслуживает кэширования. Это может стать источником проблем для таких сервисов, как Dynatrace, использующих cookie для корреляции веб-запросов с пользовательскими действиями.

## Обходное решение

Чтобы обойти эту проблему, **сервер кэширования должен быть настроен на игнорирование связанных с Dynatrace cookie в запросах и ответах**. При этом необходимо тщательно разграничить запросы, в которых cookie Dynatrace должны исключаться, и запросы, подлежащие кэшированию, чтобы Real User Monitoring не пострадал.

При правильно настроенных правилах сервера кэширования Real User Monitoring не пострадает от исключения cookie Dynatrace при кэшировании. Однако отображаемые нагрузки веб-сервера перестанут совпадать с нагрузками, зафиксированными для приложений на этих серверах, поскольку большинство запросов будет обрабатываться сервером кэширования.

## Пример конфигурации для Varnish Cache

Рассмотрим Varnish Cache как пример решения проблем с кэшированием в вашей среде.

Это не универсальное решение, подходящее для всех сред; для корректной адаптации этих инструкций к вашей конфигурации необходимо базовое понимание вашего сервера кэширования.

Varnish Cache (внешняя ссылка: [https://www.varnish-cache.org/](https://www.varnish-cache.org/)) — популярный HTTP-сервер кэширования и балансировщик нагрузки с широкими возможностями настройки на языке VCL (Varnish Configuration Language), напоминающем C. Необходимая конфигурация состоит главным образом из подпрограмм, вызываемых сервером на различных этапах конвейера обработки запросов.

В нашем примере используются три подпрограммы:

| Подпрограмма | Когда вызывается |
| --- | --- |
| `vcl_recv` | Вызывается в начале обработки запроса. |
| `vcl_miss` | Вызывается при промахе кэша. |
| `vcl_backend_response` | Вызывается после получения страницы с исходного сервера в результате промаха кэша. |

В примере используется синтаксис VCL 4.0; для более ранних версий потребуются незначительные изменения (см. ниже).

1. Убедитесь, что cookie Dynatrace исключаются до того, как Varnish принимает решение о поиске запрошенного контента в кэше. Используйте для этого подпрограмму `vcl_recv`. Внимание: маяки JavaScript-мониторинга Dynatrace никогда не должны кэшироваться, и cookie на них должны сохраняться. Маяки используют метод запроса POST, поэтому добавление логики исключения cookie только для не-POST запросов решает эту задачу. Ниже приведён VCL-код для этого:

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

   Приведённый выше код выполняет следующее:

   * Проверяет, является ли запрос POST-запросом и есть ли у него заголовок cookie (для VCL до версии 4.0 используйте `req.request` вместо `req.method`).
   * Удаляет все связанные с Dynatrace записи cookie с помощью регулярных выражений. Функция `regsuball` заменяет все вхождения, соответствующие regex, заданной строкой; в данном случае — все экземпляры cookie с именами `dtCookie`, `dtLatC`, `dtPC`, `dtVT`, `rxsession`, `rxpc`, `rxlatency` или `rxvt`.
   * Гарантирует с помощью функции `regsub`, что в начале заголовка не осталось лишней точки с запятой.
   * Проверяет, пуст ли заголовок cookie. Если да, весь заголовок удаляется. Не связанные с Dynatrace cookie сохраняются и по-прежнему могут предотвратить обслуживание запрошенного контента Varnish из кэша.
2. Описанная выше конфигурация Varnish достаточна для включения кэширования, однако необходимо решить ещё одну проблему: в случае промаха кэша и последующего обращения к исходному серверу необходимо включить cookie Dynatrace в запрос (убедитесь, что cookie сохраняются в запросах, которые не могут быть обслужены из кэша). Это даёт Dynatrace более полное понимание связей между приложениями и веб-серверами. Для этого расширьте конфигурацию следующим образом:

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

   Приведённый выше код выполняет следующее:

   * Добавляет условие в подпрограмму `vcl_recv`. Сначала оно проверяет, есть ли в заголовке cookie какие-либо cookie Dynatrace, и если есть, весь заголовок cookie копируется во временный заголовок. Затем код, как и прежде, удаляет специфические для Dynatrace cookie.
   * Добавляет подпрограмму `vcl_miss`, вызываемую при промахе кэша непосредственно перед передачей запроса на исходный сервер. Здесь необходимо восстановить заголовок cookie в исходное состояние с помощью созданного ранее резервного временного заголовка, после чего удалить временный заголовок. Теперь в любом запросе, который не может быть обслужен из кэша, cookie Dynatrace будут присутствовать.
3. Остался последний шаг. Необходимо удалить заголовок `Set-Cookie` Dynatrace из ответов исходного сервера, чтобы они могли кэшироваться. Если cookie Dynatrace является единственным устанавливаемым cookie или всегда является первым заголовком `Set-Cookie`, можно использовать следующую конфигурацию:

   ```
   sub vcl_backend_response {



   if (beresp.http.Cache-Control !~ "no-cache" && beresp.http.Set-Cookie



   && (beresp.http.Set-Cookie ~ "^dtCookie=.*" || beresp.http.Set-Cookie ~ "^rxsession=.*")) {



   unset beresp.http.Set-Cookie;



   }



   }
   ```

   Подпрограмма `vcl_backend_response` вызывается после получения контента с исходного сервера (в старых версиях VCL она называлась `vcl_fetch`). Перед удалением заголовка `Set-Cookie` необходимо убедиться, что он существует и относится к Dynatrace. Проверка заголовка `Cache-Control` на значение `no-cache` гарантирует сохранность ответов на запросы маяков Dynatrace. В целом рекомендуется избегать изменения ответов, которые не будут кэшированы.
4. Если имеется несколько заголовков `Set-Cookie` и нельзя гарантировать, что заголовок Dynatrace стоит первым, потребуется альтернативное решение. Из-за ограничений Varnish код выше учитывает только первый заголовок `Set-Cookie` в ответе и игнорирует остальные. Обойти это можно, установив модуль `libvmod-header`, доступный по адресу [https://github.com/varnish/libvmod-header](https://github.com/varnish/libvmod-header). Этот модуль содержит функцию `remove`, удаляющую все экземпляры `Set-Cookie`, соответствующие заданному параметру:

   ```
   import header;



   sub vcl_backend_response {



   if (beresp.http.Cache-Control !~ "no-cache") {



   header.remove(beresp.http.Set-Cookie, "dtCookie=");



   header.remove(beresp.http.Set-Cookie, "rxsession=");



   }



   }
   ```

Полная конфигурация

Приведённый код предназначен только для справки. Имейте в виду, что конкретная конфигурация может отличаться в зависимости от версии Varnish и отслеживаемого веб-сайта. Для серверов кэширования, отличных от Varnish, потребуются аналогичные правила в иных форматах.

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

## Тестирование конфигурации Varnish Cache

Чтобы убедиться, что конфигурация работает должным образом, можно использовать программу `varnishlog` для доступа к журналу Varnish (см. пример с фильтрацией ненужных строк с помощью grep). Ниже приведён пример команды и вывода, демонстрирующий корректно работающую конфигурацию Varnish (полный вывод сокращён для наглядности). Команда выводит каждый запрос (строки `ReqURL`) и принятые Varnish решения о кэшировании.

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

Как видно из вывода, первый запрос к веб-странице («/») правильно завершается промахом кэша. Страница затем загружается с исходного сервера, и следующий запрос к той же странице завершается попаданием в кэш. Запросы маяков Dynatrace (`/rb_1` в данном примере) корректно передаются дальше и не рассматриваются для кэширования.