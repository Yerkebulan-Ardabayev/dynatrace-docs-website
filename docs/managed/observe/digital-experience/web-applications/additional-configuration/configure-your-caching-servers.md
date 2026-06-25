---
title: Configure your caching servers
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-your-caching-servers
scraped: 2026-05-12T11:34:16.302073
---

# Configure your caching servers

# Configure your caching servers

* How-to guide
* 8-min read
* Published Jul 19, 2017

Using a caching server with Dynatrace Real User Monitoring can sometimes lead to unexpected results. A cache hit rate close to zero is the most obvious symptom of cache-related problems. This is most likely to happen when you rely on default caching-server configuration settings.

Fortunately, with a little caching-server configuration, it's usually possible to maintain a high cache hit rate while preserving Dynatrace monitoring coverage.

## Cookies and caching servers

By default, cache servers like Varnish Cache are conservative in determining what data should be cached. All requests that contain cookies and all responses that include a `Set-Cookie` header are dropped from the cache by default. The somewhat outdated assumption behind this behavior is that such requested content is typically user-specific and therefore not worthy of caching. This can be a source of trouble for services like Dynatrace that use cookies to correlate web requests with user actions.

## Workaround

To work around this problem, **your cache server must be instructed to ignore Dynatrace-related cookies in requests and responses**. You'll need to take care in differentiating which requests Dynatrace cookies need to be dropped and which requests are to be cached to ensure that Real User Monitoring isn't affected.

With proper caching server rules in place, Real User Monitoring isn't affected by bypassing Dynatrace cookies for caching. However, reported web server loads will no longer match the loads reported for the applications running on the servers because the cache server is taking care of most requests.

## Example configuration for Varnish Cache

Let's take a look at Varnish Cache as an example of how you might solve caching problems in your environment.

This isn't a "one-size-fits-all" solution that works for all deployments; you need a basic understanding of your own cache server to correctly adapt these instructions to your site-specific configuration.

Varnish Cache (external link: [https://www.varnish-cache.org/ï»¿](https://www.varnish-cache.org/)) is a popular HTTP cache server and load balancer that can be extensively configured using a C-like language called VCL (Varnish Configuration Language). The required configuration consists mainly of subroutines that are called by the server at different points during the request processing pipeline.

Our example configuration uses three subroutines:

| Subroutine | When it's called |
| --- | --- |
| `vcl_recv` | Called at the beginning of request processing. |
| `vcl_miss` | Called when a cache miss occurs. |
| `vcl_backend_response` | Called after a page is fetched from the originating server due to a cache miss. |

Our example uses VCL 4.0 syntax; you'll need to make some minor changes for earlier versions (see below).

1. Make sure that Dynatrace cookies are dropped before Varnish decides whether or not to search for the requested content from the cache. Use the `vcl_recv` subroutine for this. Be careful, Dynatrace JavaScript monitoring beacons should never be cached and the cookies on them should be preserved. The beacons use the POST request method, so adding logic to only perform cookie dropping on non-POST requests should do the trick. Here is the VCL code for that:

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

   The code sample above does the following:

   * Checks if the request is a POST request and if it has a cookie header (for pre-v4.0 VCL, use `req.request` instead of `req.method`).
   * Removes all Dynatrace-related cookie entries using a little regular expression magic. The function `regsuball` replaces all occurrences matching the regex with the string given to it as the last parameter; in this case, all instances of cookies named `dtCookie`, `dtLatC`, `dtPC`, `dtVT`, `rxsession`, `rxpc`, `rxlatency`, or `rxvt`.
   * Makes sure, with the `regsub` function, that there is no leftover semicolon at the beginning of the header.
   * Checks if the cookie header is empty. If it is, the entire header is removed. The non-Dynatrace cookies are preserved and may still prevent Varnish from serving the requested content from the cache.
2. The above Varnish configuration is sufficient for turning caching on again, but there's one more problem we need to address: In the case of a cache miss and a subsequent call to the originating server, you need to include the Dynatrace cookie in the request (make sure cookies are preserved in requests that can't be served from cache). This gives Dynatrace a better understanding of the connections between your applications and web servers. You need to extend your configuration in the following way to achieve this:

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

   The code sample above does the following:

   * Adds a condition to the `vcl_recv` subroutine. This initially checks if there are any Dynatrace cookies in the cookie header and, if there are, the whole cookie header is copied to a temporary header. The code then proceeds as before in removing Dynatrace-specific cookies.
   * Adds the `vcl_miss` subroutine, which is called in the case of a cache miss, right before the request is passed to the originating server. We want to reset the cookie header to its original state using the backup temporary header that we created earlier. After that we can remove the temporary header. Now any request that cannot be served from the cache will find the Dynatrace cookies intact.
3. There's one last thing to do. Remove the Dynatrace `Set-Cookie` header from the originating server responses so that they can be cached. If the Dynatrace cookie is the only cookie being set, or if it always is the first `Set-Cookie` header that is set, we can use the following configuration:

   ```
   sub vcl_backend_response {



   if (beresp.http.Cache-Control !~ "no-cache" && beresp.http.Set-Cookie



   && (beresp.http.Set-Cookie ~ "^dtCookie=.*" || beresp.http.Set-Cookie ~ "^rxsession=.*")) {



   unset beresp.http.Set-Cookie;



   }



   }
   ```

   The `vcl_backend_response` subroutine is called after some content has been fetched from the originating server (in older VCL versions this was called `vcl_fetch`). Before removing the `Set-Cookie` header, we first need to make sure that it exists and that it is Dynatrace-related. The check if the `Cache-Control` header is set to `no-cache` ensures that the responses for Dynatrace beacon requests stay intact. It's generally a good idea to avoid changing responses that will not be cached.
4. In case we have multiple `Set-Cookie` headers and we cannot be sure that the one for Dynatrace is the first, we need an alternative solution. Due to limitations with Varnish, the code above will only consider the first `Set-Cookie` header in the response and ignore the rest. We can work around this by installing the `libvmod-header` module, available from [https://github.com/varnish/libvmod-headerï»¿](https://github.com/varnish/libvmod-header). This module contains a `remove` function that removes any instances of `Set-Cookie` that match the given parameter:

   ```
   import header;



   sub vcl_backend_response {



   if (beresp.http.Cache-Control !~ "no-cache") {



   header.remove(beresp.http.Set-Cookie, "dtCookie=");



   header.remove(beresp.http.Set-Cookie, "rxsession=");



   }



   }
   ```

See entire configuration

The code included here is intended only as a reference. Keep in mind that your required configuration may differ based on Varnish versions and the web site that you're monitoring. Caching servers other than Varnish will require similar rules in varying formats.

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

## Test your Varnish Cache configuration

To make sure that the configuration works as expected, you can use the `varnishlog`  program to access varnish log output (see our example explaining how to filter out unnecessary lines using grep). Below is an example command and output that shows a correctly functioning Varnish configuration (full output trimmed for demonstration purposes). The command prints out each request (the `ReqURL` lines) and the resulting caching decisions made by Varnish.

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

As you can see, the first request for the web page (â/â) correctly results in a cache miss. The page is then fetched from the originating server and the next request for the same page results in a cache hit. The Dynatrace beacon requests (`/rb_1` in this example) are correctly passed forward and aren't considered for caching.