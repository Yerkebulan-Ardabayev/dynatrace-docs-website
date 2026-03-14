---
title: Расширение Varnish Cache
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/extensions/varnish-cache-1
scraped: 2026-03-05T21:25:45.341800
---

# Расширение Varnish Cache


* Последняя версия Dynatrace
* Расширение
* Обновлено 04 дек. 2025 г.

Мониторинг производительности Varnish Cache для оптимизации доставки контента и сокращения времени отклика.

## Начало работы

### Обзор

Мониторинг статистики экземпляров Varnish Cache.

### Сценарии использования

* Мониторинг состояния экземпляров Varnish Cache.
* Обнаружение аномального поведения и оповещение о нём.
* Анализ нагрузки и операционной производительности кэша.

### Требования

* OneAgent должен быть установлен на хосте с экземпляром Varnish Cache, подлежащим мониторингу.
* На хосте должен присутствовать бинарный файл `varnishstat`.
* Пользователь OneAgent должен иметь возможность выполнять этот бинарный файл на хосте.
* Перед выполнением команды `sudo varnishstat` убедитесь, что `dtuser` имеет права sudo и настроен для доступа без пароля в файле `sudoers`.

### Информация о совместимости

Varnish версии 6.2.1+.

## Подробности

* Метрики из коробки

Системные метрики производительности Varnish Cache (CPU, память и другое) доступны без дополнительной настройки при использовании OneAgent на сервере с Dynatrace OneAgent.

Вы также получаете информацию о сетевом трафике, TCP-запросах и подключении, а также метрики качества, такие как повторные передачи, время приёма-передачи (RTT) и пропускная способность.

* Расширенные метрики сервера Varnish Cache, такие как

  + Производительность кэша
  + Метрики бэкенда
  + Метрики клиента
  + Метрики потоков, **недоступны** в Dynatrace из коробки.

Это расширение собирает вышеуказанные расширенные метрики сервера Varnish Cache путём выполнения команды `varnishstat` и последующей отправки результирующего вывода обратно в Dynatrace.

### Лицензирование и стоимость

* DPS:

`((20 * #_of_backends) + (7 * #_of_malloc_stevedores) + (7 * #_of_umem_stevedores) + (10 * #_of_file_stevedores) + 198)`

* DDU:

`((20 * #_of_backends) + (7 * #_of_malloc_stevedores) + (7 * #_of_umem_stevedores) + (10 * #_of_file_stevedores) + 198) * 0.001`

## Наборы функций

При активации расширения с помощью [конфигурации мониторинга](#monitoring-configuration) можно ограничить мониторинг одним из наборов функций. Для корректной работы расширение должно собирать хотя бы одну метрику после активации.

В сильно сегментированных сетях наборы функций могут отражать сегменты вашей среды. Тогда при создании конфигурации мониторинга можно выбрать набор функций и соответствующую группу ActiveGate, которая может подключаться к этому конкретному сегменту.

Все метрики, не отнесённые ни к одному набору функций, считаются набором по умолчанию и всегда отображаются.

Метрика наследует набор функций подгруппы, которая, в свою очередь, наследует набор функций группы. Кроме того, набор функций, определённый на уровне метрики, имеет приоритет над набором функций, определённым на уровне подгруппы, который, в свою очередь, имеет приоритет над набором функций, определённым на уровне группы.

main

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| stat summ operations | varnish.cache.main.summs.count | Количество раз, когда статистика по потокам суммировалась в глобальные счётчики. |
| Child process uptime | varnish.cache.main.uptime.count | Время работы дочернего процесса. |
| Sessions accepted | varnish.cache.main.sess\_conn.count | Количество успешно принятых сессий. |
| Session accept failures | varnish.cache.main.sess\_fail.count | Количество неудачных попыток принять TCP-соединение. Этот счётчик является суммой счётчиков sess\_fail\_\*, которые дают более подробную информацию. |
| Session accept failures: connection aborted | varnish.cache.main.sess\_fail\_econnaborted.count | Подробная причина sess\_fail: соединение прервано клиентом, обычно безвредно. |
| Session accept failures: interrupted system call | varnish.cache.main.sess\_fail\_eintr.count | Подробная причина sess\_fail: вызов accept() был прерван, обычно безвредно. |
| Session accept failures: too many open files | varnish.cache.main.sess\_fail\_emfile.count | Подробная причина sess\_fail: файловый дескриптор недоступен. Рассмотрите возможность увеличения RLIMIT\_NOFILE (см. ulimit -n). |
| Session accept failures: bad file descriptor | varnish.cache.main.sess\_fail\_ebadf.count | Подробная причина sess\_fail: файловый дескриптор прослушивающего сокета недействителен. Не должно происходить никогда. |
| Session accept failures: not enough memory | varnish.cache.main.sess\_fail\_enomem.count | Подробная причина sess\_fail: скорее всего, недостаточно памяти буфера сокета. Не должно происходить никогда. |
| Session accept failures: other | varnish.cache.main.sess\_fail\_other.count | Подробная причина sess\_fail: ни одна из вышеуказанных, см. лог SessError (varnishlog -g raw -i SessError). |
| Client requests received, subject to 400 errors | varnish.cache.main.client\_req\_400.count | 400 означает, что не удалось разобрать запрос — он был сформирован неправильно. |
| Client requests received, subject to 417 errors | varnish.cache.main.client\_req\_417.count | 417 означает, что произошла ошибка с заголовком Expect. |
| Good client requests received | varnish.cache.main.client\_req.count | Количество разобранных клиентских запросов. |
| ESI subrequests | varnish.cache.main.esi\_req.count | Количество сделанных ESI-подзапросов. |
| Cache hits | varnish.cache.main.cache\_hit.count | Количество попаданий в кэш. Попадание в кэш означает, что объект был доставлен клиенту без обращения к бэкенд-серверу. |
| Cache grace hits | varnish.cache.main.cache\_hit\_grace.count | Количество попаданий в кэш с отсрочкой. Попадание в кэш с отсрочкой — это попадание в кэш, при котором срок действия объекта истёк. Такие попадания также включаются в счётчик cache\_hit. |
| Cache hits for pass. | varnish.cache.main.cache\_hitpass.count | Количество попаданий для pass. Попадание для pass означает, что Varnish передаст запрос бэкенду, и это решение было закэшировано само по себе. Считает, сколько раз используется закэшированное решение. |
| Cache hits for miss. | varnish.cache.main.cache\_hitmiss.count | Количество попаданий для miss. Попадание для miss означает, что Varnish обработает запрос как промах кэша без объединения запросов, и это решение было закэшировано. Считает, сколько раз используется закэшированное решение. |
| Cache misses | varnish.cache.main.cache\_miss.count | Количество промахов кэша. Промах кэша означает, что объект был получен с бэкенда перед доставкой клиенту. |
| Uncacheable backend responses | varnish.cache.main.beresp\_uncacheable.count | Количество ответов бэкенда, признанных некэшируемыми. |
| Shortlived objects | varnish.cache.main.beresp\_shortlived.count | Количество объектов, созданных с ttl+grace+keep меньше параметра выполнения 'shortlived'. |
| Backend conn. success | varnish.cache.main.backend\_conn.count | Количество успешно установленных соединений с бэкендом. |
| Backend conn. not attempted | varnish.cache.main.backend\_unhealthy.count | Соединение с бэкендом не предпринималось. |
| Backend conn. too many | varnish.cache.main.backend\_busy.count | Слишком много соединений с бэкендом. |
| Backend conn. failures | varnish.cache.main.backend\_fail.count | Сбои соединений с бэкендом. |
| Backend conn. reuses | varnish.cache.main.backend\_reuse.count | Количество повторных использований соединений с бэкендом. Счётчик увеличивается при каждом повторном использовании переработанного соединения. |
| Backend conn. recycles | varnish.cache.main.backend\_recycle.count | Количество переработанных соединений с бэкендом. Счётчик увеличивается при каждом возврате keep-alive-соединения в пул соединений. Соединение ещё не использовалось, но может быть использовано, если бэкенд его не закроет. |
| Backend conn. retry | varnish.cache.main.backend\_retry.count | Повторная попытка соединения с бэкендом. |
| Fetch no body (HEAD) | varnish.cache.main.fetch\_head.count | beresp без тела, так как запрос является HEAD. |
| Fetch with Length | varnish.cache.main.fetch\_length.count | beresp.body с Content-Length. |
| Fetch chunked | varnish.cache.main.fetch\_chunked.count | beresp.body с Chunked. |
| Fetch EOF | varnish.cache.main.fetch\_eof.count | beresp.body с EOF. |
| Fetch bad T-E | varnish.cache.main.fetch\_bad.count | Длина/выборка beresp.body не могла быть определена. |
| Fetch no body | varnish.cache.main.fetch\_none.count | beresp.body пустой. |
| Fetch no body (1xx) | varnish.cache.main.fetch\_1xx.count | beresp без тела из-за ответа 1XX. |
| Fetch no body (204) | varnish.cache.main.fetch\_204.count | beresp без тела из-за ответа 204. |
| Fetch no body (304) | varnish.cache.main.fetch\_304.count | beresp без тела из-за ответа 304. |
| Fetch failed (all causes) | varnish.cache.main.fetch\_failed.count | Сбой выборки beresp. |
| Background fetch failed (no thread) | varnish.cache.main.bgfetch\_no\_thread.count | Фоновая выборка, инициированная попаданием с отсрочкой, завершилась неудачей — нет доступного потока. |
| Number of thread pools | varnish.cache.main.pools | Количество пулов потоков. См. также параметр thread\_pools. Примечание: в настоящее время пулы не могут быть удалены после создания. |
| Total number of threads | varnish.cache.main.threads | Количество потоков во всех пулах. См. также параметры thread\_pools, thread\_pool\_min и thread\_pool\_max. |
| Threads hit max | varnish.cache.main.threads\_limited.count | Количество раз, когда требовалось больше потоков, но был достигнут лимит в пуле потоков. См. также параметр thread\_pool\_max. |
| Threads created | varnish.cache.main.threads\_created.count | Общее количество созданных потоков во всех пулах. |
| Threads destroyed | varnish.cache.main.threads\_destroyed.count | Общее количество уничтоженных потоков во всех пулах. |
| Thread creation failed | varnish.cache.main.threads\_failed.count | Количество неудачных попыток создания потока. См. VSL::Debug для диагностики. См. также параметр thread\_fail\_delay. |
| Length of session queue | varnish.cache.main.thread\_queue\_len | Длина очереди сессий, ожидающих потоков. Примечание: обновляется только раз в секунду. См. также параметр thread\_queue\_limit. |
| Number of requests sent to sleep on busy objhdr | varnish.cache.main.busy\_sleep.count | Количество запросов, отправленных в режим ожидания без рабочего потока из-за обнаружения занятого объекта. |
| Number of requests woken after sleep on busy objhdr | varnish.cache.main.busy\_wakeup.count | Количество запросов, снятых со списка ожидания занятого объекта и перепланированных. |
| Number of requests killed after sleep on busy objhdr | varnish.cache.main.busy\_killed.count | Количество запросов, удалённых из списка ожидания занятого объекта из-за нехватки ресурсов. |
| Sessions queued for thread | varnish.cache.main.sess\_queued.count | Количество раз, когда сессия ставилась в очередь в ожидании потока. См. также параметр thread\_queue\_limit. |
| Sessions dropped for thread | varnish.cache.main.sess\_dropped.count | Количество раз, когда HTTP/1-сессия была отброшена из-за слишком длинной очереди. См. также параметр thread\_queue\_limit. |
| Requests dropped | varnish.cache.main.req\_dropped.count | Количество раз, когда HTTP/2-поток был отклонён из-за слишком длинной очереди. См. также параметр thread\_queue\_limit. |
| object structs made | varnish.cache.main.n\_object | Приблизительное количество HTTP-объектов (заголовки + тело, при наличии) в кэше. |
| unresurrected objects | varnish.cache.main.n\_vampireobject | Количество невосстановленных объектов. |
| objectcore structs made | varnish.cache.main.n\_objectcore | Приблизительное количество элементов метаданных объектов в кэше. Каждый объект требует objectcore; дополнительные objectcore используются для hit-for-miss, hit-for-pass и занятых объектов. |
| objecthead structs made | varnish.cache.main.n\_objecthead | Приблизительное количество различных хэш-записей в кэше. |
| Number of backends | varnish.cache.main.n\_backend | Количество известных нам бэкендов. |
| Number of expired objects | varnish.cache.main.n\_expired.count | Количество объектов, удалённых из кэша по истечении срока действия. |
| Number of LRU nuked objects | varnish.cache.main.n\_lru\_nuked.count | Количество объектов, принудительно удалённых из хранилища для освобождения места под новый объект. |
| Number of LRU moved objects | varnish.cache.main.n\_lru\_moved.count | Количество операций перемещения в списке LRU. |
| Reached nuke\_limit | varnish.cache.main.n\_lru\_limited.count | Количество раз, когда требовалось больше дискового пространства, но был достигнут лимит nuke\_limit. См. также параметр nuke\_limit. |
| HTTP header overflows | varnish.cache.main.losthdr.count | Переполнения HTTP-заголовков. |
| Total sessions seen | varnish.cache.main.s\_sess.count | Всего обработанных сессий. |
| Number of ongoing pipe sessions | varnish.cache.main.n\_pipe | Количество текущих pipe-сессий. |
| Pipes hit pipe\_sess\_max | varnish.cache.main.pipe\_limited.count | Количество раз, когда требовалось больше pipe, но был достигнут лимит. См. также параметр pipe\_sess\_max. |
| Total pipe sessions seen | varnish.cache.main.s\_pipe.count | Всего обработанных pipe-сессий. |
| Total pass-ed requests seen | varnish.cache.main.s\_pass.count | Всего обработанных pass-запросов. |
| Total backend fetches initiated | varnish.cache.main.s\_fetch.count | Всего инициированных выборок бэкенда, включая фоновые выборки. |
| Total backend background fetches initiated | varnish.cache.main.s\_bgfetch.count | Всего инициированных фоновых выборок бэкенда. |
| Total synthetic responses made | varnish.cache.main.s\_synth.count | Всего созданных синтетических ответов. |
| Request header bytes | varnish.cache.main.s\_req\_hdrbytes.count | Всего получено байт заголовков запросов. |
| Request body bytes | varnish.cache.main.s\_req\_bodybytes.count | Всего получено байт тела запросов. |
| Response header bytes | varnish.cache.main.s\_resp\_hdrbytes.count | Всего передано байт заголовков ответов. |
| Response body bytes | varnish.cache.main.s\_resp\_bodybytes.count | Всего передано байт тела ответов. |
| Pipe request header bytes | varnish.cache.main.s\_pipe\_hdrbytes.count | Всего получено байт запросов для pipe-сессий. |
| Piped bytes from client | varnish.cache.main.s\_pipe\_in.count | Всего перенаправлено байт от клиентов в pipe-сессиях. |
| Piped bytes to client | varnish.cache.main.s\_pipe\_out.count | Всего перенаправлено байт клиентам в pipe-сессиях. |
| Session Closed | varnish.cache.main.sess\_closed.count | Закрытых сессий. |
| Session Closed with error | varnish.cache.main.sess\_closed\_err.count | Всего сессий, закрытых с ошибками. См. счётчики диагностики sc\_\* для подробной разбивки. |
| Session Read Ahead | varnish.cache.main.sess\_readahead.count | Опережающее чтение сессии. |
| Session herd | varnish.cache.main.sess\_herd.count | Количество срабатываний timeout\_linger. |
| Session OK REM\_CLOSE | varnish.cache.main.sc\_rem\_close.count | Количество закрытий сессий с REM\_CLOSE (клиент закрыл соединение). |
| Session OK REQ\_CLOSE | varnish.cache.main.sc\_req\_close.count | Количество закрытий сессий с REQ\_CLOSE (клиент запросил закрытие). |
| Session Err REQ\_HTTP10 | varnish.cache.main.sc\_req\_http10.count | Количество закрытий сессий с ошибкой REQ\_HTTP10 (Proto < HTTP/1.1). |
| Session Err RX\_BAD | varnish.cache.main.sc\_rx\_bad.count | Количество закрытий сессий с ошибкой RX\_BAD (получен плохой запрос/ответ). |
| Session Err RX\_BODY | varnish.cache.main.sc\_rx\_body.count | Количество закрытий сессий с ошибкой RX\_BODY (ошибка получения тела запроса). |
| Session Err RX\_JUNK | varnish.cache.main.sc\_rx\_junk.count | Количество закрытий сессий с ошибкой RX\_JUNK (получены мусорные данные). |
| Session Err RX\_OVERFLOW | varnish.cache.main.sc\_rx\_overflow.count | Количество закрытий сессий с ошибкой RX\_OVERFLOW (переполнение буфера приёма). |
| Session Err RX\_TIMEOUT | varnish.cache.main.sc\_rx\_timeout.count | Количество закрытий сессий с ошибкой RX\_TIMEOUT (таймаут приёма). |
| Session Err RX\_CLOSE\_IDLE | varnish.cache.main.sc\_rx\_close\_idle.count | Количество закрытий сессий с ошибкой RX\_CLOSE\_IDLE: превышено время ожидания timeout\_idle при ожидании запроса от клиента. |
| Session OK TX\_PIPE | varnish.cache.main.sc\_tx\_pipe.count | Количество закрытий сессий с TX\_PIPE (транзакция через pipe). |
| Session Err TX\_ERROR | varnish.cache.main.sc\_tx\_error.count | Количество закрытий сессий с ошибкой TX\_ERROR (ошибочная транзакция). |
| Session OK TX\_EOF | varnish.cache.main.sc\_tx\_eof.count | Количество закрытий сессий с TX\_EOF (передача с EOF). |
| Session OK RESP\_CLOSE | varnish.cache.main.sc\_resp\_close.count | Количество закрытий сессий с RESP\_CLOSE (бэкенд/VCL запросил закрытие). |
| Session Err OVERLOAD | varnish.cache.main.sc\_overload.count | Количество закрытий сессий с ошибкой OVERLOAD (нехватка какого-либо ресурса). |
| Session Err PIPE\_OVERFLOW | varnish.cache.main.sc\_pipe\_overflow.count | Количество закрытий сессий с ошибкой PIPE\_OVERFLOW (переполнение pipe сессии). |
| Session Err RANGE\_SHORT | varnish.cache.main.sc\_range\_short.count | Количество закрытий сессий с ошибкой RANGE\_SHORT (недостаточно данных для диапазона). |
| Session Err REQ\_HTTP20 | varnish.cache.main.sc\_req\_http20.count | Количество закрытий сессий с ошибкой REQ\_HTTP20 (HTTP2 не принят). |
| Session Err VCL\_FAILURE | varnish.cache.main.sc\_vcl\_failure.count | Количество закрытий сессий с ошибкой VCL\_FAILURE (сбой VCL). |
| Delivery failed due to insufficient workspace. | varnish.cache.main.client\_resp\_500.count | Количество раз, когда не удалось отправить ответ из-за нехватки памяти рабочего пространства во время доставки. |
| workspace\_backend overflows | varnish.cache.main.ws\_backend\_overflow.count | Количество раз, когда заканчивалось место в workspace\_backend. |
| workspace\_client overflows | varnish.cache.main.ws\_client\_overflow.count | Количество раз, когда заканчивалось место в workspace\_client. |
| workspace\_thread overflows | varnish.cache.main.ws\_thread\_overflow.count | Количество раз, когда заканчивалось место в workspace\_thread. |
| workspace\_session overflows | varnish.cache.main.ws\_session\_overflow.count | Количество раз, когда заканчивалось место в workspace\_session. |
| SHM records | varnish.cache.main.shm\_records.count | Количество записей лога, записанных в лог разделяемой памяти. |
| SHM writes | varnish.cache.main.shm\_writes.count | Количество отдельных операций записи в лог разделяемой памяти. Одна операция записи может объединять несколько записей для буферизованных задач. |
| SHM flushes due to overflow | varnish.cache.main.shm\_flushes.count | Количество операций записи, выполненных до завершения буферизованной задачи, поскольку добавление записи в пакет превысило бы vsl\_buffer. |
| SHM lock contention | varnish.cache.main.shm\_cont.count | Количество раз, когда операции записи приходилось ждать блокировки. |
| SHM cycles through VSL space | varnish.cache.main.shm\_cycles.count | Количество раз, когда запись записей лога достигала конца лога разделяемой памяти, возвращаясь к началу. |
| SHM bytes | varnish.cache.main.shm\_bytes.count | Количество байт, записанных в лог разделяемой памяти. |
| Backend requests made | varnish.cache.main.backend\_req.count | Выполнено запросов к бэкенду. |
| Number of loaded VCLs in total | varnish.cache.main.n\_vcl | Общее количество загруженных VCL. |
| Number of VCLs available | varnish.cache.main.n\_vcl\_avail | Количество доступных VCL. |
| Number of discarded VCLs | varnish.cache.main.n\_vcl\_discard | Количество отброшенных VCL. |
| VCL failures | varnish.cache.main.vcl\_fail.count | Количество сбоев, препятствовавших завершению VCL. |
| Count of bans | varnish.cache.main.bans | Количество всех блокировок в системе, включая блокировки, замещённые более новыми, и блокировки, уже проверенные ban-lurker. |
| Number of bans marked 'completed' | varnish.cache.main.bans\_completed | Количество блокировок, которые больше не активны: либо проверены ban-lurker, либо замещены идентичными более новыми блокировками. |
| Number of bans using obj.\* | varnish.cache.main.bans\_obj | Количество блокировок, использующих переменные obj.\*. Эти блокировки могут быть обработаны ban-lurker. |
| Number of bans using req.\* | varnish.cache.main.bans\_req | Количество блокировок, использующих переменные req.\*. Эти блокировки не могут быть обработаны ban-lurker. |
| Bans added | varnish.cache.main.bans\_added.count | Счётчик блокировок, добавленных в список блокировок. |
| Bans deleted | varnish.cache.main.bans\_deleted.count | Счётчик блокировок, удалённых из списка блокировок. |
| Bans tested against objects (lookup) | varnish.cache.main.bans\_tested.count | Количество проверок блокировок и объектов друг против друга при поиске по хэшу. |
| Objects killed by bans (lookup) | varnish.cache.main.bans\_obj\_killed.count | Количество объектов, уничтоженных блокировками при поиске объектов. |
| Bans tested against objects (lurker) | varnish.cache.main.bans\_lurker\_tested.count | Количество проверок блокировок и объектов друг против друга ban-lurker. |
| Ban tests tested against objects (lookup) | varnish.cache.main.bans\_tests\_tested.count | Количество проверок тестов и объектов друг против друга при поиске. 'ban req.url == foo && req.http.host == bar' считается одним в 'bans\_tested' и двумя в 'bans\_tests\_tested'. |
| Ban tests tested against objects (lurker) | varnish.cache.main.bans\_lurker\_tests\_tested.count | Количество проверок тестов и объектов друг против друга ban-lurker. 'ban req.url == foo && req.http.host == bar' считается одним в 'bans\_tested' и двумя в 'bans\_tests\_tested'. |
| Objects killed by bans (lurker) | varnish.cache.main.bans\_lurker\_obj\_killed.count | Количество объектов, уничтоженных ban-lurker. |
| Objects killed by bans for cutoff (lurker) | varnish.cache.main.bans\_lurker\_obj\_killed\_cutoff.count | Количество объектов, уничтоженных ban-lurker для поддержания количества блокировок ниже ban\_cutoff. |
| Bans superseded by other bans | varnish.cache.main.bans\_dups.count | Количество блокировок, замещённых более поздними идентичными блокировками. |
| Lurker gave way for lookup | varnish.cache.main.bans\_lurker\_contention.count | Количество раз, когда ban-lurker приходилось ждать операций поиска. |
| Bytes used by the persisted ban lists | varnish.cache.main.bans\_persisted\_bytes | Количество байт, использованных постоянными списками блокировок. |
| Extra bytes in persisted ban lists due to fragmentation | varnish.cache.main.bans\_persisted\_fragmentation | Количество дополнительных байт, накопленных из-за отброшенных и завершённых блокировок в постоянных списках блокировок. |
| Number of purge operations executed | varnish.cache.main.n\_purges.count | Количество выполненных операций очистки. |
| Number of purged objects | varnish.cache.main.n\_obj\_purged.count | Количество очищенных объектов. |
| Number of objects mailed to expiry thread | varnish.cache.main.exp\_mailed.count | Количество объектов, переданных потоку истечения срока действия для обработки. |
| Number of objects received by expiry thread | varnish.cache.main.exp\_received.count | Количество объектов, полученных потоком истечения срока действия для обработки. |
| HCB Lookups without lock | varnish.cache.main.hcb\_nolock.count | Поиск в HCB без блокировки. |
| HCB Lookups with lock | varnish.cache.main.hcb\_lock.count | Поиск в HCB с блокировкой. |
| HCB Inserts | varnish.cache.main.hcb\_insert.count | Вставки в HCB. |
| ESI parse errors (unlock) | varnish.cache.main.esi\_errors.count | Ошибки разбора ESI (разблокировка). |
| ESI parse warnings (unlock) | varnish.cache.main.esi\_warnings.count | Предупреждения разбора ESI (разблокировка). |
| Loaded VMODs | varnish.cache.main.vmods | Загруженные VMOD. |
| Gzip operations | varnish.cache.main.n\_gzip.count | Операции gzip. |
| Gunzip operations | varnish.cache.main.n\_gunzip.count | Операции gunzip. |
| Test gunzip operations | varnish.cache.main.n\_test\_gunzip.count | Эти операции происходят, когда Varnish получает сжатый объект от бэкенда. Они выполняются для проверки потока gzip при его добавлении в хранилище. |
| Premature iovec flushes | varnish.cache.main.http1\_iovs\_flush.count | Количество дополнительных операций записи, выполненных для HTTP1-соединений, поскольку количество IO-векторов было слишком мало для передачи всего возможного IO за один раз. Этот параметр настраивается через параметр http1\_iovs для клиентских соединений и неявно определяется количеством свободного рабочего пространства для бэкенд-соединений. |

mempool

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| In use | varnish.cache.mempool.live | Используется. |
| In Pool | varnish.cache.mempool.pool | В пуле. |
| Size requested | varnish.cache.mempool.sz\_wanted | Запрошенный размер. |
| Size allocated | varnish.cache.mempool.sz\_actual | Выделенный размер. |
| Allocations | varnish.cache.mempool.allocs.count | Выделения памяти. |
| Frees | varnish.cache.mempool.frees.count | Освобождения памяти. |
| Recycled from pool | varnish.cache.mempool.recycle.count | Переработано из пула. |
| Timed out from pool | varnish.cache.mempool.timeout.count | Таймаут из пула. |
| Too small to recycle | varnish.cache.mempool.toosmall.count | Слишком мало для переработки. |
| Too many for pool | varnish.cache.mempool.surplus.count | Слишком много для пула. |
| Pool ran dry | varnish.cache.mempool.randry.count | Пул исчерпан. |

lck

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Created locks | varnish.cache.lck.creat.count | Созданные блокировки. |
| Destroyed locks | varnish.cache.lck.destroy.count | Уничтоженные блокировки. |
| Lock Operations | varnish.cache.lck.locks.count | Операции блокировки. |
| Contended lock operations | varnish.cache.lck.dbg\_busy.count | Если установлен бит отладки lck: операции блокировки, вернувшие EBUSY при первой попытке. Если бит отладки lck не установлен, этот счётчик никогда не будет увеличиваться, даже если операции блокировки конкурируют. |
| Contended trylock operations | varnish.cache.lck.dbg\_try\_fail.count | Если установлен бит отладки lck: операции trylock, вернувшие EBUSY. Если бит отладки lck не установлен, этот счётчик никогда не будет увеличиваться, даже если операции блокировки конкурируют. |

vbe

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Happy health probes | varnish.cache.vbe.happy | Представляет последние результаты проб в виде битовой маски. Успешные пробы — биты, установленные в 1, неуспешные — в 0. Старшие биты представляют старейшие пробы. |
| Request header bytes | varnish.cache.vbe.bereq\_hdrbytes.count | Всего отправлено байт заголовков запросов бэкенда. |
| Request body bytes | varnish.cache.vbe.bereq\_bodybytes.count | Всего отправлено байт тела запросов бэкенда. |
| Response header bytes | varnish.cache.vbe.beresp\_hdrbytes.count | Всего получено байт заголовков ответов бэкенда. |
| Response body bytes | varnish.cache.vbe.beresp\_bodybytes.count | Всего получено байт тела ответов бэкенда. |
| Pipe request header bytes | varnish.cache.vbe.pipe\_hdrbytes.count | Всего отправлено байт запросов для pipe-сессий. |
| Piped bytes to backend | varnish.cache.vbe.pipe\_out.count | Всего перенаправлено байт к бэкенду в pipe-сессиях. |
| Piped bytes from backend | varnish.cache.vbe.pipe\_in.count | Всего перенаправлено байт от бэкенда в pipe-сессиях. |
| Concurrent connections used | varnish.cache.vbe.conn | Количество текущих используемых соединений с бэкендом. Это число всегда меньше или равно количеству соединений с бэкендом (например, отображаемых как ESTABLISHED для TCP-соединений в netstat) из-за пула соединений. |
| Backend requests sent | varnish.cache.vbe.req.count | Отправлено запросов к бэкенду. |
| Fetches not attempted due to backend being unhealthy | varnish.cache.vbe.unhealthy.count | Выборки не предпринимались из-за нездорового бэкенда. |
| Fetches not attempted due to backend being busy | varnish.cache.vbe.busy.count | Количество раз, когда был достигнут лимит max\_connections. |
| Connections failed | varnish.cache.vbe.fail.count | Счётчик неудачных открытий. Подробные причины указаны в счётчиках fail\_\* (уровень DIAG) и в логе под тегом FetchError. Этот счётчик является суммой всех счётчиков fail\_\*. Все счётчики fail\_\* могут быть слегка неточными из соображений эффективности. |
| Connections failed with EACCES or EPERM | varnish.cache.vbe.fail\_eacces.count | Сбои соединений с EACCES или EPERM. |
| Connections failed with EADDRNOTAVAIL | varnish.cache.vbe.fail\_eaddrnotavail.count | Сбои соединений с EADDRNOTAVAIL. |
| Connections failed with ECONNREFUSED | varnish.cache.vbe.fail\_econnrefused.count | Сбои соединений с ECONNREFUSED. |
| Connections failed with ENETUNREACH | varnish.cache.vbe.fail\_enetunreach.count | Сбои соединений с ENETUNREACH. |
| Connections failed ETIMEDOUT | varnish.cache.vbe.fail\_etimedout.count | Сбои соединений с ETIMEDOUT. |
| Connections failed for other reason | varnish.cache.vbe.fail\_other.count | Сбои соединений по другой причине. |
| Connection opens not attempted | varnish.cache.vbe.helddown.count | Соединения не предпринимались в течение интервала backend\_local\_error\_holddown или backend\_remote\_error\_holddown после фундаментальной проблемы соединения. |

mgt

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Management process uptime | varnish.cache.mgt.uptime.count | Время работы процесса управления в секундах. |
| Child process started | varnish.cache.mgt.child\_start.count | Количество запусков дочернего процесса. |
| Child process normal exit | varnish.cache.mgt.child\_exit.count | Количество чистых остановок дочернего процесса. |
| Child process unexpected exit | varnish.cache.mgt.child\_stop.count | Количество завершений дочернего процесса с неожиданным кодом возврата. |
| Child process died (signal) | varnish.cache.mgt.child\_died.count | Количество смертей дочернего процесса из-за сигналов. |
| Child process core dumped | varnish.cache.mgt.child\_dump.count | Количество дамп-файлов ядра, созданных дочерним процессом. |
| Child process panic | varnish.cache.mgt.child\_panic.count | Количество раз, когда процесс управления перехватывал панику дочернего процесса. |

default

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Return code | varnish.cache.returncode | Код возврата команды varnishstat. |

smf

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Allocator requests | varnish.cache.smf.c\_req.count | Количество обращений к хранилищу для предоставления сегмента. |
| Allocator failures | varnish.cache.smf.c\_fail.count | Количество отказов хранилища в предоставлении сегмента. |
| Bytes allocated | varnish.cache.smf.c\_bytes.count | Всего байт, выделенных этим хранилищем. |
| Bytes freed | varnish.cache.smf.c\_freed.count | Всего байт, возвращённых этому хранилищу. |
| Allocations outstanding | varnish.cache.smf.g\_alloc | Количество незавершённых выделений хранилища. |
| Bytes outstanding | varnish.cache.smf.g\_bytes | Количество байт, выделенных из хранилища. |
| Bytes available | varnish.cache.smf.g\_space | Количество байт, оставшихся в хранилище. |
| N struct smf | varnish.cache.smf.g\_smf | N структур smf. |
| N small free smf | varnish.cache.smf.g\_smf\_frag | N небольших свободных smf. |
| N large free smf | varnish.cache.smf.g\_smf\_large | N больших свободных smf. |

smu

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Allocator requests | varnish.cache.smu.c\_req.count | Количество обращений к хранилищу для предоставления сегмента. |
| Allocator failures | varnish.cache.smu.c\_fail.count | Количество отказов хранилища в предоставлении сегмента. |
| Bytes allocated | varnish.cache.smu.c\_bytes.count | Всего байт, выделенных этим хранилищем. |
| Bytes freed | varnish.cache.smu.c\_freed.count | Всего байт, возвращённых этому хранилищу. |
| Allocations outstanding | varnish.cache.smu.g\_alloc | Количество незавершённых выделений хранилища. |
| Bytes outstanding | varnish.cache.smu.g\_bytes | Количество байт, выделенных из хранилища. |
| Bytes available | varnish.cache.smu.g\_space | Количество байт, оставшихся в хранилище. |

sma

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Allocator requests | varnish.cache.sma.c\_req.count | Количество обращений к хранилищу для предоставления сегмента. |
| Allocator failures | varnish.cache.sma.c\_fail.count | Количество отказов хранилища в предоставлении сегмента. |
| Bytes allocated | varnish.cache.sma.c\_bytes.count | Всего байт, выделенных этим хранилищем. |
| Bytes freed | varnish.cache.sma.c\_freed.count | Всего байт, возвращённых этому хранилищу. |
| Allocations outstanding | varnish.cache.sma.g\_alloc | Количество незавершённых выделений хранилища. |
| Bytes outstanding | varnish.cache.sma.g\_bytes | Количество байт, выделенных из хранилища. |
| Bytes available | varnish.cache.sma.g\_space | Количество байт, оставшихся в хранилище. |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Изучить в Dynatrace Hub

Мониторинг статистики экземпляров Varnish Cache.](https://www.dynatrace.com/hub/detail/varnish-cache-1/)
