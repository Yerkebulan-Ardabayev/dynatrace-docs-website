---
title: Known limitations for Go support
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/go/support/go-known-limitations
---

# Known limitations for Go support

# Known limitations for Go support

* 11-min read
* Updated on Mar 30, 2026

Before you start using Go application monitoring, make sure that you are aware of the known limitations.

## Support limited to official, stable Go releases

Go support is limited to:

* Official, stable [Go releases﻿](https://dt-url.net/go-releases) compiled with the Golang toolchain.
* Stable [Go releases﻿](https://dt-url.net/go-releases) with [openssl-fips﻿](https://dt-url.net/golang-fips) modifications to support the Federal Information Processing Standards (OneAgent version 1.295+).

OneAgent doesn't support binaries compiled using other toolchains like

* [gccgo toolchain﻿](https://dt-url.net/gccgo-toolchain)

## Applications built with `-linkshared` option aren't supported

Go supports dynamic linking of the Go standard library. This build mode is rarely used, and OneAgent won't inject into applications built this way.

Example

Consider the following minimalistic Go application called `GoMinimal.go`:

```
go install -buildmode=shared -linkshared std



go build -linkshared GoMinimal.go
```

OneAgent will reject the resulting application binary.

## Applications built with `-buildmode=pie` option and CGO disabled aren't supported

This restriction applies only to Linux systems.

Building the application with `-buildmode=pie` and `CGO_ENABLED=0` results in a dynamically linked application binary but without `libc` system library dependency, `libc` is required by OneAgent.

Example and workaround

Consider the following Go application called `main.go`:

```
package main



import "fmt"



func main() {



fmt.Print("Enter text: ")



var input string



fmt.Scanln(&input)



fmt.Print(input)



}
```

Building the application with the following command results in a dynamically linked application binary that does not depend on `libc`, which is required by OneAgent:

```
CGO_ENABLED=0 go build -buildmode=pie main.go
```

As a workaround, there are several options:

* Remove `-buildmode=pie` option which results in a statically linked Go application (see [Go static monitoring](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/enable-go-monitoring#go-static-monitoring "Learn how you can enable Go monitoring in Dynatrace.")).

  ```
  CGO_ENABLED=0 go build main.go
  ```
* Use an external linker and do not disable CGO (`CGO_ENABLED=1` is the default).

  ```
  go build -ldflags="-linkmode=external" -buildmode=pie main.go
  ```

## Applications that load Go plugins aren't supported

A [Go plugin﻿](https://dt-url.net/eae3riv) is a package compiled using the `-buildmode=plugin` build flag to produce a shared object file. This build mode is rarely used, and OneAgent will disable deep monitoring when an application actually loads a Go plugin.

## Vendored third-party packages aren't supported

[Go vendoring﻿](https://dt-url.net/ubg3r7o) is used to include local copies of external dependencies in the project repository. This approach was used to pin versions of third-party packages before [Go module﻿](https://dt-url.net/nci3rry) support was added.

OneAgent will not monitor vendored packages. For example, gRPC services are supported only if you use Go modules or if you import [go-grpc﻿](https://dt-url.net/k6k3r67) directly without using a dependency management system.

## Possible limitations without a symbol table

By default, Go generates application binaries that contain a symbol table.

Currently there are no known limitations for stripped binaries in Dynatrace. However, we can't guarantee that all current features will continue to work in future Go versions or that all features added later will be supported in stripped binaries.

We therefore recommend that you build Go binaries that contain a symbol table and avoid the use of command line parameters or external tools that might suppress it.

* Don't use the external tool `strip` (`strip <Go binary>`).
* Don't compile with `go build -ldflags="-s"`. The `-s` flag strips away the symbol table.
* Don't run `go run <application>`. This rarely used command builds and runs applications on the fly. Because the output application file is temporary (the file is deleted automatically after the app termination), the application binary contains no symbol table.

In Dynatrace, monitoring of stripped binaries is enabled by default. However, you can disable the feature for the tenant by turning off **Go stripped binaries** on the [**OneAgent features**](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") settings page.

Non-stripped binaries on AArch64 are supported starting with OneAgent version 1.323. OneAgent version 1.327 adds support for stripped binaries on AArch64.

## Applications built with race detector enabled aren't supported

An application built with `-race` flag contains a built-in [data race detector﻿](https://golang.org/doc/articles/race_detector).
This build mode is mostly used in a development environment and OneAgent won't inject into applications built this way.

## Creation stack profiling of OS threads is disabled

OneAgent does not support the [predefined `threadcreate` profile﻿](https://golang.org/doc/diagnostics#profiling). Thread creation profiling results of Go applications monitored by OneAgent will contain empty stack traces only.

## Support for statically linked binaries (Linux only)

OneAgent version 1.203+

Prior to OneAgent version 1.203, statically linked binaries are not supported. See [below](#no-static-monitoring) for details.

After you [enable Go static monitoring](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/enable-go-monitoring#go-static-monitoring "Learn how you can enable Go monitoring in Dynatrace."), automatic injection for statically linked Go binaries is supported by OneAgent if

* The parent process is dynamically linked. This also applies to applications running as a container payload.

  Example

  In this example, the parent process is a `/bin/sh` shell that starts a statically linked Go binary. The following code launches the `/bin/sh` shell and executes the provided command.

  ```
  /bin/sh -c '/StaticGoMinimal <optional app arguments>'
  ```

  You can use the `file` command to verify if an application is dynamically or statically linked.

  ```
  $ file -L /bin/sh



  /bin/sh: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked



  $ file -L /StaticGoMinimal



  /StaticGoMinimal: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked
  ```
* [Kubernetes Classic full-stack injection](/managed/ingest-from/setup-on-k8s/how-it-works#classic "In-depth description on how the deployment on Kubernetes works.") The statically linked Go binary is running as a Docker container entrypoint.

  Example

  ```
  FROM alpine:3.11



  COPY StaticGoMinimal /



  ENTRYPOINT ["/StaticGoMinimal"]
  ```

If your setup is not supported by automatic injection, we recommend calling the static Go application via a shell (`/bin/sh -c '/StaticGoMinimal <optional app arguments>'`).

### Cloud-native full-stack injection

Automatic injection of statically linked Go applications running as container entrypoints is not supported when using the [cloud-native full-stack injection](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "In-depth description on how the deployment on Kubernetes works.") deployment option in Kubernetes.

Example

For example, in a cloud-native full-stack injection deployment, the following code starts an unsupported statically linked Go application.

```
FROM alpine:3.11



COPY StaticGoMinimal /



ENTRYPOINT ["/StaticGoMinimal"]
```

To overcome this limitation, you can change the container entrypoint from a statically linked Go application to a dynamically linked application such as a shell or `init`.

Workaround when a shell is available

Applies to container images that already contain a dynamically linked shell binary.

By changing the container entryproint from a statically linked Go application to a dynamically linked shell, we obtain the following code that launches `/bin/sh` and executes the `/StaticGoMinimal` command.

```
FROM alpine:3.11



COPY StaticGoMinimal /



ENTRYPOINT ["/bin/sh", "-c", "'/StaticGoMinimal'"]
```

Workaround when a shell is not available

Applies to container images where a shell is not available.

When the container image does not contain a shell, for example in [distroless images﻿](https://dt-url.net/up23q6j), another option is to use a minimal `init` binary like [tini﻿](https://dt-url.net/he03qck).
By adding tini and changing the container entryproint, we obtain the following code that executes `/StaticGoMinimal` while preserving proper signal forwarding.

```
# syntax=docker/dockerfile:1



FROM gcr.io/distroless/base



COPY StaticGoMinimal /



ARG TINI_VERSION=v0.19.0



ADD --checksum=sha256:93dcc18adc78c65a028a84799ecf8ad40c936fdfc5f2a57b1acda5a8117fa82c --chmod=555 \



https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-amd64 /tini



ENTRYPOINT [ "/tini", "--" ]



CMD ["/StaticGoMinimal"]
```

Note the parser directive specifying Dockerfile syntax version 1, which is required for using the `--checksum` and `--chmod` options with `ADD`. Without it, the image would have to provide the `chmod` binary so `tini` can be made executable.
There are several variants of tini available for glibc and musl, as well as amd64 and aarch64 architectures.

### Limitations

* Static Go applications that use cgo are not supported.

  OneAgent rejects monitoring of static Go binaries that use [cgo﻿](https://go.dev/blog/cgo) and, therefore, have a static dependency on the C system library libc. This is because the statically linked version of libc might conflict with the one used by OneAgent.

  Workaround

  To overcome this limitation, you can build the Go application as a [dynamically linked executable](/managed/ingest-from/technology-support/application-software/go/support/go-known-limitations#go-dynamic-linking "Learn the limitations for Go support and their workarounds.") that dynamically links to libc. This will ensure that both the Go application and OneAgent use the same version of libc, which is the one available on the host.
* OneAgent version 1.337+ Static Go monitoring requires either a Linux kernel that provides the
  `memfd_create` syscall (added in Linux 3.17, but backported to earlier versions on some distributions), or the
  `SYS_PTRACE` capability (see next point).
* OneAgent version 1.335 and earlier Static Go monitoring requires the `SYS_PTRACE` capability.

  The `SYS_PTRACE` capability is enabled by default for Docker 19.03.0+ and Linux Kernel 4.8+. It allows system calls between processes running in a container, which is a requirement for Go static monitoring.

  Workaround and example

  You can overcome this limitation for Docker versions earlier than 19.03.0 or Linux Kernel versions earlier than 4.8 by running the container with the `SYS_PTRACE` capability as shown below.

  ```
  docker run --cap-add=SYS_PTRACE <container> ...
  ```
* Docker images that don't provide a C system library are not supported.

  OneAgent requires a C system library to be available on the monitored host.

  Workaround and example

  To overcome this limitation, you can change the base image of a container to one that provides a C system library.

  An example of a Docker image that doesn't provide a C system library is the [scratch image﻿](https://dt-url.net/6083rfq).

  ```
  FROM scratch



  COPY StaticGoMinimal /



  CMD ["/StaticGoMinimal"]
  ```

  Examples of images that provide a C system library are the [Alpine image﻿](https://dt-url.net/ksa3rnj) or various [distroless images﻿](https://dt-url.net/up23q6j).

  ```
  FROM alpine:3.11



  COPY StaticGoMinimal /



  CMD ["/StaticGoMinimal"]
  ```

### Side effects

The file `proc/<pId>/exe` refers to an executable named `oneagentdynamizer` instead of the Go application binary, it is contained in the [proc﻿](https://dt-url.net/94c3rfn) pseudo-filesystem that provides an interface to kernel data structures of running processes. This may cause system tools like `ps` or `top` to display `oneagentdynamizer` instead of the Go binary name in their output.

### OneAgent versions without support for static monitoring

OneAgent version 1.201 and earlier

Prior to OneAgent version 1.203, statically linked binaries are not supported and dynamic linking is necessary for injection on Linux. There is no such limitation on Windows.

Dynamic linking is automatically applied when the application uses certain standard runtime library packages, for example, `net/http`.
In all other cases, you can enforce dynamic linking through the `-ldflags="-linkmode=external"` command line option. Note that disabling cgo, for example, using `CGO_ENABLED=0`, is not supported, and OneAgent will reject the resulting application binary.

Example

Consider the following minimalistic Go application called `GoMinimal.go`:

```
package main



import "fmt"



func main() {



fmt.Print("Enter text: ")



var input string



fmt.Scanln(&input)



fmt.Print(input)



}
```

Building the application results in a statically linked application binary:

```
$ go build GoMinimal.go



$ file GoMinimal



GoMinimal: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, not stripped
```

You can enforce dynamic linking with `-ldflags="-linkmode=external"`:

```
$ go build -ldflags="-linkmode=external" GoMinimal.go



$ file GoMinimal



GoMinimal: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32
```

## Support for musl libc

The musl libc library is a drop-in replacement for the glibc library. Dynatrace supports musl-based Go applications, such as those built on Alpine Linux.

There is one additional requirement for building a dynamically linked application binary. You should use the [Go toolchain for alpine (golang:<version>-alpine)﻿](https://dt-url.net/3gm3rwp) and add `-ldflags="-linkmode=external"` (or add `-linkmode=external` to an existing `-ldflags`) to the build command line to enforce usage of the system linker. This is not required for statically linked Go applications watched by [Go static monitoring](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/enable-go-monitoring#go-static-monitoring "Learn how you can enable Go monitoring in Dynatrace.").

Details

While musl libc does closely mimic the glibc functionalities, there are subtle behavioral differences between the two. Moreover, Go doesn't officially support the musl-based Go toolchain, which means Go toolchain binaries can't be downloaded from the [golang.org﻿](https://dt-url.net/go) website.

In addition, there is a [serious issue﻿](https://dt-url.net/6vq3rim) with how Go uses musl libc. This limits the extent to which Dynatrace can support musl-based applications. The Go toolchain includes an internal linker that generates musl-based application binaries that don't correctly initialize musl libc at application startup. This issue prevents Dynatrace from monitoring these applications. In such a case, the following message is displayed on the relevant application process page:  
**Activation of deep monitoring was unsuccessful, Monitoring of Go musl binaries built with Go internal linker is not supported**

If you use the system linker to generate the application binary, it adds startup code that correctly initializes shared objects. Also, adding `-ldflags="-linkmode=external"` to the build command line enforces usage of the system linker. The resulting binary will execute with a correctly initialized libc, allowing Dynatrace to monitor such an application.

Example

Consider the following minimalistic Go application called `GoMinimal.go`:

```
package main



import "fmt"



func main() {



fmt.Print("Enter text: ")



var input string



fmt.Scanln(&input)



fmt.Print(input)



}
```

The following multi-stage docker file yields a valid dynamically linked Go musl binary in stage 1 and runs the application in stage 2.

```
# --- Stage 1:



# Use Golang toolchain for alpine to build the application.



FROM golang:1.23.2-alpine as builder



RUN apk update && apk add gcc libc-dev



# Copy local code, for example, GoMinimal.go, to the container image.



COPY ./GoMinimal.go ./GoMinimal.go



# Build dynamically linked Go binary.



RUN go build -ldflags="-linkmode=external" GoMinimal.go



# or add '-linkmode=external' to existing ldflags:



# e.g.: go build -ldflags="-linkmode=external <other linker flags>" GoMinimal.go



# --- Stage 2:



# Use a Docker multi-stage build to create a lean production image.



FROM alpine:3.20



# Install ca-certificates and libc6-compat for Go programs to work properly.



RUN apk add --no-cache ca-certificates libc6-compat



# Copy the binary to the production image from the builder stage.



COPY --from=builder /go/GoMinimal /GoMinimal



# Run the application on container startup.



CMD ["/GoMinimal"]
```

Build the container and run the application:

```
docker build -t gominimal-alpine .



docker run --interactive gominimal-alpine
```

Additionally, there is an issue with the musl malloc implementation on machines that have 64 or more CPUs, which can result in high CPU overhead. This can be resolved by either

* Using a base image that uses glibc instead.
* Preloading an alternative malloc implementation, such as [tcmalloc﻿](https://dt-url.net/xz03zxt) or [jemalloc﻿](https://dt-url.net/9523zi0), as described below.

Preloading tcmalloc

To preload tcmalloc, take the Dockerfile from the example above and adjust Stage 2 as shown in the code block below.

```
# --- Stage 2:



# Use a Docker multi-stage build to create a lean production image.



FROM alpine:3.20



# Install ca-certificates and libc6-compat for Go programs to work properly.



RUN apk add --no-cache ca-certificates libc6-compat



# Install tcmalloc



RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing tcmalloc



# Preload tcmalloc



ENV LD_PRELOAD="/usr/lib/libtcmalloc.so.4"



# Copy the binary to the production image from the builder stage.



COPY --from=builder /go/GoMinimal /GoMinimal



# Run the application on container startup.



CMD ["/GoMinimal"]
```

Preloading jemalloc

To preload jemalloc, take the Dockerfile from the example above and adjust Stage 2 as shown in the code block below.

```
# --- Stage 2:



# Use a Docker multi-stage build to create a lean production image.



FROM alpine:3.20



# Install ca-certificates and libc6-compat for Go programs to work properly.



RUN apk add --no-cache ca-certificates libc6-compat



# Install jemalloc



RUN apk add --no-cache jemalloc



# Preload jemalloc



ENV LD_PRELOAD="/usr/lib/libjemalloc.so.2"



# Copy the binary to the production image from the builder stage.



COPY --from=builder /go/GoMinimal /GoMinimal



# Run the application on container startup.



CMD ["/GoMinimal"]
```