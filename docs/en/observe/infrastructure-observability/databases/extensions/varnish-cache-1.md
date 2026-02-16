---
title: Varnish Cache extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/extensions/varnish-cache-1
scraped: 2026-02-16T09:20:21.860727
---

# Varnish Cache extension

# Varnish Cache extension

* Latest Dynatrace
* Extension
* Updated on Dec 04, 2025

Monitor Varnish Cache performance to optimize content delivery and reduce response times.

## Get started

### Overview

Monitor the statistics of Varnish Cache instances.

### Use cases

* Monitor the health and state of Varnish cache instances.
* Detect and alert on anomalous behavior.
* Understand the load and operational performance of the cache.

### Requirements

* OneAgent must be installed on the host with the Varnish Cache instance to be monitored.
* `varnishstat` binary must be present on the host.
* OneAgent user must be able to execute the binary on the host.
* Before running the `sudo varnishstat` command, make sure `dtuser` has sudo permissions and is set up for passwordless access in the `sudoers` file.

### Compatibility information

Varnish version 6.2.1+.

## Details

* Out-of-the-box metrics

Varnish Cache system performance metrics (CPU, memory, and more) are available with no additional configuration when using OneAgent on a server running Dynatrace OneAgent.

You also get details about network traffic, TCP requests, and connectivity, along with quality metrics such as retransmissions, round-trip time, and throughput.

* Advanced Varnish Cache server metrics such as

  + Cache performance
  + Backend metrics
  + Client metrics
  + Thread metrics are **not** available out of the box in Dynatrace.

This extension collects the above advanced Varnish Cache server metrics by executing the `varnishstat` command and then sending the resulting output back to Dynatrace.

### Licensing and cost

* DPS:

`((20 * #_of_backends) + (7 * #_of_malloc_stevedores) + (7 * #_of_umem_stevedores) + (10 * #_of_file_stevedores) + 198)`

* DDUs:

`((20 * #_of_backends) + (7 * #_of_malloc_stevedores) + (7 * #_of_umem_stevedores) + (10 * #_of_file_stevedores) + 198) * 0.001`

## Feature sets

When activating your extension using [monitoring configuration](#monitoring-configuration), you can limit monitoring to one of the feature sets. To work properly, the extension has to collect at least one metric after the activation.

In highly segmented networks, feature sets can reflect the segments of your environment. Then, when you create a monitoring configuration, you can select a feature set and a corresponding ActiveGate group that can connect to this particular segment.

All metrics that aren't categorized into any feature set are considered to be the default and are always reported.

A metric inherits the feature set of a subgroup, which in turn inherits the feature set of a group. Also, the feature set defined on the metric level overrides the feature set defined on the subgroup level, which in turn overrides the feature set defined on the group level.

mempool

| Metric name | Metric key | Description |
| --- | --- | --- |
| In use | varnish.cache.mempool.live | In use |
| In Pool | varnish.cache.mempool.pool | In Pool |
| Size requested | varnish.cache.mempool.sz\_wanted | Size requested |
| Size allocated | varnish.cache.mempool.sz\_actual | Size allocated |
| Allocations | varnish.cache.mempool.allocs.count | Allocations |
| Frees | varnish.cache.mempool.frees.count | Frees |
| Recycled from pool | varnish.cache.mempool.recycle.count | Recycled from pool |
| Timed out from pool | varnish.cache.mempool.timeout.count | Timed out from pool |
| Too small to recycle | varnish.cache.mempool.toosmall.count | Too small to recycle |
| Too many for pool | varnish.cache.mempool.surplus.count | Too many for pool |
| Pool ran dry | varnish.cache.mempool.randry.count | Pool ran dry |

lck

| Metric name | Metric key | Description |
| --- | --- | --- |
| Created locks | varnish.cache.lck.creat.count | Created locks |
| Destroyed locks | varnish.cache.lck.destroy.count | Destroyed locks |
| Lock Operations | varnish.cache.lck.locks.count | Lock Operations |
| Contended lock operations | varnish.cache.lck.dbg\_busy.count | If the lck debug bit is set: Lock operations which returned EBUSY on the first locking attempt. If the lck debug bit is unset, this counter will never be incremented even if lock operations are contended. |
| Contended trylock operations | varnish.cache.lck.dbg\_try\_fail.count | If the lck debug bit is set: Trylock operations which returned EBUSY. If the lck debug bit is unset, this counter will never be incremented even if lock operations are contended. |

vbe

| Metric name | Metric key | Description |
| --- | --- | --- |
| Happy health probes | varnish.cache.vbe.happy | Represents the last probe results as a bitmap. Happy probes are bits set to 1, and the unhappy ones are set to 0. The highest bits represent the oldest probes. |
| Request header bytes | varnish.cache.vbe.bereq\_hdrbytes.count | Total backend request header bytes sent |
| Request body bytes | varnish.cache.vbe.bereq\_bodybytes.count | Total backend request body bytes sent |
| Response header bytes | varnish.cache.vbe.beresp\_hdrbytes.count | Total backend response header bytes received |
| Response body bytes | varnish.cache.vbe.beresp\_bodybytes.count | Total backend response body bytes received |
| Pipe request header bytes | varnish.cache.vbe.pipe\_hdrbytes.count | Total request bytes sent for piped sessions |
| Piped bytes to backend | varnish.cache.vbe.pipe\_out.count | Total number of bytes forwarded to backend in pipe sessions |
| Piped bytes from backend | varnish.cache.vbe.pipe\_in.count | Total number of bytes forwarded from backend in pipe sessions |
| Concurrent connections used | varnish.cache.vbe.conn | The number of currently used connections to the backend. This number is always less or equal to the number of connections to the backend (as, for example shown as ESTABLISHED for TCP connections in netstat) due to connection pooling. |
| Backend requests sent | varnish.cache.vbe.req.count | Backend requests sent |
| Fetches not attempted due to backend being unhealthy | varnish.cache.vbe.unhealthy.count | Fetches not attempted due to backend being unhealthy |
| Fetches not attempted due to backend being busy | varnish.cache.vbe.busy.count | Number of times the max\_connections limit was reached .. === Anything below is actually per VCP entry, but collected per === backend for simplicity |
| Connections failed | varnish.cache.vbe.fail.count | Counter of failed opens. Detailed reasons are given in the fail\_\* counters (DIAG level) and in the log under the FetchError tag. This counter is the sum of all detailed fail\_\* counters. All fail\_\* counters may be slightly inaccurate for efficiency. |
| Connections failed with EACCES or EPERM | varnish.cache.vbe.fail\_eacces.count | Connections failed with EACCES or EPERM |
| Connections failed with EADDRNOTAVAIL | varnish.cache.vbe.fail\_eaddrnotavail.count | Connections failed with EADDRNOTAVAIL |
| Connections failed with ECONNREFUSED | varnish.cache.vbe.fail\_econnrefused.count | Connections failed with ECONNREFUSED |
| Connections failed with ENETUNREACH | varnish.cache.vbe.fail\_enetunreach.count | Connections failed with ENETUNREACH |
| Connections failed ETIMEDOUT | varnish.cache.vbe.fail\_etimedout.count | Connections failed ETIMEDOUT |
| Connections failed for other reason | varnish.cache.vbe.fail\_other.count | Connections failed for other reason |
| Connection opens not attempted | varnish.cache.vbe.helddown.count | Connections not attempted during the backend\_local\_error\_holddown or backend\_remote\_error\_holddown interval after a fundamental connection issue. |

mgt

| Metric name | Metric key | Description |
| --- | --- | --- |
| Management process uptime | varnish.cache.mgt.uptime.count | Uptime in seconds of the management process |
| Child process started | varnish.cache.mgt.child\_start.count | Number of times the child process has been started |
| Child process normal exit | varnish.cache.mgt.child\_exit.count | Number of times the child process has been cleanly stopped |
| Child process unexpected exit | varnish.cache.mgt.child\_stop.count | Number of times the child process has exited with an unexpected return code |
| Child process died (signal) | varnish.cache.mgt.child\_died.count | Number of times the child process has died due to signals |
| Child process core dumped | varnish.cache.mgt.child\_dump.count | Number of times the child process has produced core dumps |
| Child process panic | varnish.cache.mgt.child\_panic.count | Number of times the management process has caught a child panic |

default

| Metric name | Metric key | Description |
| --- | --- | --- |
| Return code | varnish.cache.returncode | Return code of the varnishstat command |

smf

| Metric name | Metric key | Description |
| --- | --- | --- |
| Allocator requests | varnish.cache.smf.c\_req.count | Number of times the storage has been asked to provide a storage segment. |
| Allocator failures | varnish.cache.smf.c\_fail.count | Number of times the storage has failed to provide a storage segment. |
| Bytes allocated | varnish.cache.smf.c\_bytes.count | Number of total bytes allocated by this storage. |
| Bytes freed | varnish.cache.smf.c\_freed.count | Number of total bytes returned to this storage. |
| Allocations outstanding | varnish.cache.smf.g\_alloc | Number of storage allocations outstanding. |
| Bytes outstanding | varnish.cache.smf.g\_bytes | Number of bytes allocated from the storage. |
| Bytes available | varnish.cache.smf.g\_space | Number of bytes left in the storage. |
| N struct smf | varnish.cache.smf.g\_smf | N struct smf |
| N small free smf | varnish.cache.smf.g\_smf\_frag | N small free smf |
| N large free smf | varnish.cache.smf.g\_smf\_large | N large free smf |

smu

| Metric name | Metric key | Description |
| --- | --- | --- |
| Allocator requests | varnish.cache.smu.c\_req.count | Number of times the storage has been asked to provide a storage segment. |
| Allocator failures | varnish.cache.smu.c\_fail.count | Number of times the storage has failed to provide a storage segment. |
| Bytes allocated | varnish.cache.smu.c\_bytes.count | Number of total bytes allocated by this storage. |
| Bytes freed | varnish.cache.smu.c\_freed.count | Number of total bytes returned to this storage. |
| Allocations outstanding | varnish.cache.smu.g\_alloc | Number of storage allocations outstanding. |
| Bytes outstanding | varnish.cache.smu.g\_bytes | Number of bytes allocated from the storage. |
| Bytes available | varnish.cache.smu.g\_space | Number of bytes left in the storage. |

sma

| Metric name | Metric key | Description |
| --- | --- | --- |
| Allocator requests | varnish.cache.sma.c\_req.count | Number of times the storage has been asked to provide a storage segment. |
| Allocator failures | varnish.cache.sma.c\_fail.count | Number of times the storage has failed to provide a storage segment. |
| Bytes allocated | varnish.cache.sma.c\_bytes.count | Number of total bytes allocated by this storage. |
| Bytes freed | varnish.cache.sma.c\_freed.count | Number of total bytes returned to this storage. |
| Allocations outstanding | varnish.cache.sma.g\_alloc | Number of storage allocations outstanding. |
| Bytes outstanding | varnish.cache.sma.g\_bytes | Number of bytes allocated from the storage. |
| Bytes available | varnish.cache.sma.g\_space | Number of bytes left in the storage. |

main

| Metric name | Metric key | Description |
| --- | --- | --- |
| stat summ operations | varnish.cache.main.summs.count | Number of times per-thread statistics were summed into the global counters. |
| Child process uptime | varnish.cache.main.uptime.count | How long the child process has been running. |
| Sessions accepted | varnish.cache.main.sess\_conn.count | Count of sessions successfully accepted |
| Session accept failures | varnish.cache.main.sess\_fail.count | Count of failures to accept TCP connection. This counter is the sum of the sess\_fail\_\* counters, which give more detailed information. |
| Session accept failures: connection aborted | varnish.cache.main.sess\_fail\_econnaborted.count | Detailed reason for sess\_fail: Connection aborted by the client, usually harmless. |
| Session accept failures: interrupted system call | varnish.cache.main.sess\_fail\_eintr.count | Detailed reason for sess\_fail: The accept() call was interrupted, usually harmless |
| Session accept failures: too many open files | varnish.cache.main.sess\_fail\_emfile.count | Detailed reason for sess\_fail: No file descriptor was available. Consider raising RLIMIT\_NOFILE (see ulimit -n). |
| Session accept failures: bad file descriptor | varnish.cache.main.sess\_fail\_ebadf.count | Detailed reason for sess\_fail: The listen socket file descriptor was invalid. Should never happen. |
| Session accept failures: not enough memory | varnish.cache.main.sess\_fail\_enomem.count | Detailed reason for sess\_fail: Most likely insufficient socket buffer memory. Should never happen |
| Session accept failures: other | varnish.cache.main.sess\_fail\_other.count | Detailed reason for sess\_fail: neither of the above, see SessError log (varnishlog -g raw -i SessError). |
| Client requests received, subject to 400 errors | varnish.cache.main.client\_req\_400.count | 400 means we couldn't make sense of the request, it was malformed in some drastic way. |
| Client requests received, subject to 417 errors | varnish.cache.main.client\_req\_417.count | 417 means that something went wrong with an Expect: header. |
| Good client requests received | varnish.cache.main.client\_req.count | The count of parseable client requests seen. |
| ESI subrequests | varnish.cache.main.esi\_req.count | Number of ESI subrequests made. |
| Cache hits | varnish.cache.main.cache\_hit.count | Count of cache hits. A cache hit indicates that an object has been delivered to a client without fetching it from a backend server. |
| Cache grace hits | varnish.cache.main.cache\_hit\_grace.count | Count of cache hits with grace. A cache hit with grace is a cache hit where the object is expired. Note that such hits are also included in the cache\_hit counter. |
| Cache hits for pass. | varnish.cache.main.cache\_hitpass.count | Count of hits for pass. A cache hit for pass indicates that Varnish is going to pass the request to the backend and this decision has been cached in it self. This counts how many times the cached decision is being used. |
| Cache hits for miss. | varnish.cache.main.cache\_hitmiss.count | Count of hits for miss. A cache hit for miss indicates that Varnish is going to proceed as for a cache miss without request coalescing, and this decision has been cached. This counts how many times the cached decision is being used. |
| Cache misses | varnish.cache.main.cache\_miss.count | Count of misses. A cache miss indicates the object was fetched from the backend before delivering it to the client. |
| Uncacheable backend responses | varnish.cache.main.beresp\_uncacheable.count | Count of backend responses considered uncacheable. |
| Shortlived objects | varnish.cache.main.beresp\_shortlived.count | Count of objects created with ttl+grace+keep shorter than the 'shortlived' runtime parameter. |
| Backend conn. success | varnish.cache.main.backend\_conn.count | How many backend connections have successfully been established. |
| Backend conn. not attempted | varnish.cache.main.backend\_unhealthy.count | Backend conn. not attempted |
| Backend conn. too many | varnish.cache.main.backend\_busy.count | Backend conn. too many |
| Backend conn. failures | varnish.cache.main.backend\_fail.count | Backend conn. failures |
| Backend conn. reuses | varnish.cache.main.backend\_reuse.count | Count of backend connection reuses. This counter is increased whenever we reuse a recycled connection. |
| Backend conn. recycles | varnish.cache.main.backend\_recycle.count | Count of backend connection recycles. This counter is increased whenever we have a keep-alive connection that is put back into the pool of connections. It has not yet been used, but it might be, unless the backend closes it. |
| Backend conn. retry | varnish.cache.main.backend\_retry.count | Backend conn. retry |
| Fetch no body (HEAD) | varnish.cache.main.fetch\_head.count | beresp with no body because the request is HEAD. |
| Fetch with Length | varnish.cache.main.fetch\_length.count | beresp.body with Content-Length. |
| Fetch chunked | varnish.cache.main.fetch\_chunked.count | beresp.body with Chunked. |
| Fetch EOF | varnish.cache.main.fetch\_eof.count | beresp.body with EOF. |
| Fetch bad T-E | varnish.cache.main.fetch\_bad.count | beresp.body length/fetch could not be determined. |
| Fetch no body | varnish.cache.main.fetch\_none.count | beresp.body empty |
| Fetch no body (1xx) | varnish.cache.main.fetch\_1xx.count | beresp with no body because of 1XX response. |
| Fetch no body (204) | varnish.cache.main.fetch\_204.count | beresp with no body because of 204 response. |
| Fetch no body (304) | varnish.cache.main.fetch\_304.count | beresp with no body because of 304 response. |
| Fetch failed (all causes) | varnish.cache.main.fetch\_failed.count | beresp fetch failed. |
| Background fetch failed (no thread) | varnish.cache.main.bgfetch\_no\_thread.count | A bgfetch triggered by a grace hit failed, no thread available. |
| Number of thread pools | varnish.cache.main.pools | Number of thread pools. See also parameter thread\_pools. NB: Presently pools cannot be removed once created. |
| Total number of threads | varnish.cache.main.threads | Number of threads in all pools. See also parameters thread\_pools, thread\_pool\_min and thread\_pool\_max. |
| Threads hit max | varnish.cache.main.threads\_limited.count | Number of times more threads were needed, but limit was reached in a thread pool. See also parameter thread\_pool\_max. |
| Threads created | varnish.cache.main.threads\_created.count | Total number of threads created in all pools. |
| Threads destroyed | varnish.cache.main.threads\_destroyed.count | Total number of threads destroyed in all pools. |
| Thread creation failed | varnish.cache.main.threads\_failed.count | Number of times creating a thread failed. See VSL::Debug for diagnostics. See also parameter thread\_fail\_delay. |
| Length of session queue | varnish.cache.main.thread\_queue\_len | Length of session queue waiting for threads. NB: Only updates once per second. See also parameter thread\_queue\_limit. |
| Number of requests sent to sleep on busy objhdr | varnish.cache.main.busy\_sleep.count | Number of requests sent to sleep without a worker thread because they found a busy object. |
| Number of requests woken after sleep on busy objhdr | varnish.cache.main.busy\_wakeup.count | Number of requests taken off the busy object sleep list and rescheduled. |
| Number of requests killed after sleep on busy objhdr | varnish.cache.main.busy\_killed.count | Number of requests killed from the busy object sleep list due to lack of resources. |
| Sessions queued for thread | varnish.cache.main.sess\_queued.count | Number of times session was queued waiting for a thread. See also parameter thread\_queue\_limit. |
| Sessions dropped for thread | varnish.cache.main.sess\_dropped.count | Number of times an HTTP/1 session was dropped because the queue was too long already. See also parameter thread\_queue\_limit. |
| Requests dropped | varnish.cache.main.req\_dropped.count | Number of times an HTTP/2 stream was refused because the queue was too long already. See also parameter thread\_queue\_limit. |
| object structs made | varnish.cache.main.n\_object | Approximate number of HTTP objects (headers + body, if present) in the cache. |
| unresurrected objects | varnish.cache.main.n\_vampireobject | Number of unresurrected objects |
| objectcore structs made | varnish.cache.main.n\_objectcore | Approximate number of object metadata elements in the cache. Each object needs an objectcore, extra objectcores are for hit-for-miss, hit-for-pass and busy objects. |
| objecthead structs made | varnish.cache.main.n\_objecthead | Approximate number of different hash entries in the cache. |
| Number of backends | varnish.cache.main.n\_backend | Number of backends known to us. |
| Number of expired objects | varnish.cache.main.n\_expired.count | Number of objects that expired from cache because of old age. |
| Number of LRU nuked objects | varnish.cache.main.n\_lru\_nuked.count | How many objects have been forcefully evicted from storage to make room for a new object. |
| Number of LRU moved objects | varnish.cache.main.n\_lru\_moved.count | Number of move operations done on the LRU list. |
| Reached nuke\_limit | varnish.cache.main.n\_lru\_limited.count | Number of times more storage space were needed, but limit was reached in a nuke\_limit. See also parameter nuke\_limit. |
| HTTP header overflows | varnish.cache.main.losthdr.count | HTTP header overflows |
| Total sessions seen | varnish.cache.main.s\_sess.count | Total sessions seen |
| Number of ongoing pipe sessions | varnish.cache.main.n\_pipe | Number of ongoing pipe sessions |
| Pipes hit pipe\_sess\_max | varnish.cache.main.pipe\_limited.count | Number of times more pipes were needed, but the limit was reached. See also parameter pipe\_sess\_max. |
| Total pipe sessions seen | varnish.cache.main.s\_pipe.count | Total pipe sessions seen |
| Total pass-ed requests seen | varnish.cache.main.s\_pass.count | Total pass-ed requests seen |
| Total backend fetches initiated | varnish.cache.main.s\_fetch.count | Total backend fetches initiated, including background fetches. |
| Total backend background fetches initiated | varnish.cache.main.s\_bgfetch.count | Total backend background fetches initiated |
| Total synthetic responses made | varnish.cache.main.s\_synth.count | Total synthetic responses made |
| Request header bytes | varnish.cache.main.s\_req\_hdrbytes.count | Total request header bytes received |
| Request body bytes | varnish.cache.main.s\_req\_bodybytes.count | Total request body bytes received |
| Response header bytes | varnish.cache.main.s\_resp\_hdrbytes.count | Total response header bytes transmitted |
| Response body bytes | varnish.cache.main.s\_resp\_bodybytes.count | Total response body bytes transmitted |
| Pipe request header bytes | varnish.cache.main.s\_pipe\_hdrbytes.count | Total request bytes received for piped sessions |
| Piped bytes from client | varnish.cache.main.s\_pipe\_in.count | Total number of bytes forwarded from clients in pipe sessions |
| Piped bytes to client | varnish.cache.main.s\_pipe\_out.count | Total number of bytes forwarded to clients in pipe sessions |
| Session Closed | varnish.cache.main.sess\_closed.count | Session Closed |
| Session Closed with error | varnish.cache.main.sess\_closed\_err.count | Total number of sessions closed with errors. See sc\_\* diag counters for detailed breakdown |
| Session Read Ahead | varnish.cache.main.sess\_readahead.count | Session Read Ahead |
| Session herd | varnish.cache.main.sess\_herd.count | Number of times the timeout\_linger triggered |
| Session OK REM\_CLOSE | varnish.cache.main.sc\_rem\_close.count | Number of session closes with REM\_CLOSE (Client Closed) |
| Session OK REQ\_CLOSE | varnish.cache.main.sc\_req\_close.count | Number of session closes with REQ\_CLOSE (Client requested close) |
| Session Err REQ\_HTTP10 | varnish.cache.main.sc\_req\_http10.count | Number of session closes with Error REQ\_HTTP10 (Proto < HTTP/1.1) |
| Session Err RX\_BAD | varnish.cache.main.sc\_rx\_bad.count | Number of session closes with Error RX\_BAD (Received bad req/resp) |
| Session Err RX\_BODY | varnish.cache.main.sc\_rx\_body.count | Number of session closes with Error RX\_BODY (Failure receiving req.body) |
| Session Err RX\_JUNK | varnish.cache.main.sc\_rx\_junk.count | Number of session closes with Error RX\_JUNK (Received junk data) |
| Session Err RX\_OVERFLOW | varnish.cache.main.sc\_rx\_overflow.count | Number of session closes with Error RX\_OVERFLOW (Received buffer overflow) |
| Session Err RX\_TIMEOUT | varnish.cache.main.sc\_rx\_timeout.count | Number of session closes with Error RX\_TIMEOUT (Receive timeout) |
| Session Err RX\_CLOSE\_IDLE | varnish.cache.main.sc\_rx\_close\_idle.count | Number of session closes with Error RX\_CLOSE\_IDLE: timeout\_idle has been exceeded while waiting for a client request. |
| Session OK TX\_PIPE | varnish.cache.main.sc\_tx\_pipe.count | Number of session closes with TX\_PIPE (Piped transaction) |
| Session Err TX\_ERROR | varnish.cache.main.sc\_tx\_error.count | Number of session closes with Error TX\_ERROR (Error transaction) |
| Session OK TX\_EOF | varnish.cache.main.sc\_tx\_eof.count | Number of session closes with TX\_EOF (EOF transmission) |
| Session OK RESP\_CLOSE | varnish.cache.main.sc\_resp\_close.count | Number of session closes with RESP\_CLOSE (Backend/VCL requested close) |
| Session Err OVERLOAD | varnish.cache.main.sc\_overload.count | Number of session closes with Error OVERLOAD (Out of some resource) |
| Session Err PIPE\_OVERFLOW | varnish.cache.main.sc\_pipe\_overflow.count | Number of session closes with Error PIPE\_OVERFLOW (Session pipe overflow) |
| Session Err RANGE\_SHORT | varnish.cache.main.sc\_range\_short.count | Number of session closes with Error RANGE\_SHORT (Insufficient data for range) |
| Session Err REQ\_HTTP20 | varnish.cache.main.sc\_req\_http20.count | Number of session closes with Error REQ\_HTTP20 (HTTP2 not accepted) |
| Session Err VCL\_FAILURE | varnish.cache.main.sc\_vcl\_failure.count | Number of session closes with Error VCL\_FAILURE (VCL failure) |
| Delivery failed due to insufficient workspace. | varnish.cache.main.client\_resp\_500.count | Number of times we failed a response due to running out of workspace memory during delivery. |
| workspace\_backend overflows | varnish.cache.main.ws\_backend\_overflow.count | Number of times we ran out of space in workspace\_backend. |
| workspace\_client overflows | varnish.cache.main.ws\_client\_overflow.count | Number of times we ran out of space in workspace\_client. |
| workspace\_thread overflows | varnish.cache.main.ws\_thread\_overflow.count | Number of times we ran out of space in workspace\_thread. |
| workspace\_session overflows | varnish.cache.main.ws\_session\_overflow.count | Number of times we ran out of space in workspace\_session. |
| SHM records | varnish.cache.main.shm\_records.count | Number of log records written to the shared memory log. |
| SHM writes | varnish.cache.main.shm\_writes.count | Number of individual writes to the shared memory log. A single write may batch multiple records for bufferred tasks. |
| SHM flushes due to overflow | varnish.cache.main.shm\_flushes.count | Number of writes performed before the end of a bufferred task because adding a record to a batch would exceed vsl\_buffer. |
| SHM lock contention | varnish.cache.main.shm\_cont.count | Number of times a write had to wait for the lock. |
| SHM cycles through VSL space | varnish.cache.main.shm\_cycles.count | Number of times a write of log records would reach past the end of the shared memory log, cycling back to the beginning. |
| SHM bytes | varnish.cache.main.shm\_bytes.count | Number of bytes written to the shared memory log. |
| Backend requests made | varnish.cache.main.backend\_req.count | Backend requests made |
| Number of loaded VCLs in total | varnish.cache.main.n\_vcl | Number of loaded VCLs in total |
| Number of VCLs available | varnish.cache.main.n\_vcl\_avail | Number of VCLs available |
| Number of discarded VCLs | varnish.cache.main.n\_vcl\_discard | Number of discarded VCLs |
| VCL failures | varnish.cache.main.vcl\_fail.count | Count of failures which prevented VCL from completing. |
| Count of bans | varnish.cache.main.bans | Number of all bans in system, including bans superseded by newer bans and bans already checked by the ban-lurker. |
| Number of bans marked 'completed' | varnish.cache.main.bans\_completed | Number of bans which are no longer active, either because they got checked by the ban-lurker or superseded by newer identical bans. |
| Number of bans using obj.\* | varnish.cache.main.bans\_obj | Number of bans which use obj.\* variables. These bans can possibly be washed by the ban-lurker. |
| Number of bans using req.\* | varnish.cache.main.bans\_req | Number of bans which use req.\* variables. These bans can not be washed by the ban-lurker. |
| Bans added | varnish.cache.main.bans\_added.count | Counter of bans added to ban list. |
| Bans deleted | varnish.cache.main.bans\_deleted.count | Counter of bans deleted from ban list. |
| Bans tested against objects (lookup) | varnish.cache.main.bans\_tested.count | Count of how many bans and objects have been tested against each other during hash lookup. |
| Objects killed by bans (lookup) | varnish.cache.main.bans\_obj\_killed.count | Number of objects killed by bans during object lookup. |
| Bans tested against objects (lurker) | varnish.cache.main.bans\_lurker\_tested.count | Count of how many bans and objects have been tested against each other by the ban-lurker. |
| Ban tests tested against objects (lookup) | varnish.cache.main.bans\_tests\_tested.count | Count of how many tests and objects have been tested against each other during lookup. 'ban req.url == foo && req.http.host == bar' counts as one in 'bans\_tested' and as two in 'bans\_tests\_tested' |
| Ban tests tested against objects (lurker) | varnish.cache.main.bans\_lurker\_tests\_tested.count | Count of how many tests and objects have been tested against each other by the ban-lurker. 'ban req.url == foo && req.http.host == bar' counts as one in 'bans\_tested' and as two in 'bans\_tests\_tested' |
| Objects killed by bans (lurker) | varnish.cache.main.bans\_lurker\_obj\_killed.count | Number of objects killed by the ban-lurker. |
| Objects killed by bans for cutoff (lurker) | varnish.cache.main.bans\_lurker\_obj\_killed\_cutoff.count | Number of objects killed by the ban-lurker to keep the number of bans below ban\_cutoff. |
| Bans superseded by other bans | varnish.cache.main.bans\_dups.count | Count of bans replaced by later identical bans. |
| Lurker gave way for lookup | varnish.cache.main.bans\_lurker\_contention.count | Number of times the ban-lurker had to wait for lookups. |
| Bytes used by the persisted ban lists | varnish.cache.main.bans\_persisted\_bytes | Number of bytes used by the persisted ban lists. |
| Extra bytes in persisted ban lists due to fragmentation | varnish.cache.main.bans\_persisted\_fragmentation | Number of extra bytes accumulated through dropped and completed bans in the persistent ban lists. |
| Number of purge operations executed | varnish.cache.main.n\_purges.count | Number of purge operations executed |
| Number of purged objects | varnish.cache.main.n\_obj\_purged.count | Number of purged objects |
| Number of objects mailed to expiry thread | varnish.cache.main.exp\_mailed.count | Number of objects mailed to expiry thread for handling. |
| Number of objects received by expiry thread | varnish.cache.main.exp\_received.count | Number of objects received by expiry thread for handling. |
| HCB Lookups without lock | varnish.cache.main.hcb\_nolock.count | HCB Lookups without lock |
| HCB Lookups with lock | varnish.cache.main.hcb\_lock.count | HCB Lookups with lock |
| HCB Inserts | varnish.cache.main.hcb\_insert.count | HCB Inserts |
| ESI parse errors (unlock) | varnish.cache.main.esi\_errors.count | ESI parse errors (unlock) |
| ESI parse warnings (unlock) | varnish.cache.main.esi\_warnings.count | ESI parse warnings (unlock) |
| Loaded VMODs | varnish.cache.main.vmods | Loaded VMODs |
| Gzip operations | varnish.cache.main.n\_gzip.count | Gzip operations |
| Gunzip operations | varnish.cache.main.n\_gunzip.count | Gunzip operations |
| Test gunzip operations | varnish.cache.main.n\_test\_gunzip.count | Those operations occur when Varnish receives a compressed object from a backend. They are done to verify the gzip stream while it's inserted in storage. |
| Premature iovec flushes | varnish.cache.main.http1\_iovs\_flush.count | Number of additional writes performed on HTTP1 connections because the number of IO vectors was too small to submit all possible IO in one go. This number is configured through the http1\_iovs parameter for client connections and implicitly defined by the amount of free workspace for backend connections. |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Monitor the statistics of your Varnish Cache instances.](https://www.dynatrace.com/hub/detail/varnish-cache-1/)