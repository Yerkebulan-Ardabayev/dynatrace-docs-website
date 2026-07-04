---
title: Известные ограничения поддержки Go
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/go/support/go-known-limitations
scraped: 2026-05-12T12:03:59.705830
---

# Известные ограничения поддержки Go

# Известные ограничения поддержки Go

* Чтение: 11 мин
* Обновлено 30 марта 2026 г.

Перед началом использования мониторинга приложений Go необходимо ознакомиться с известными ограничениями.

## Поддержка ограничена официальными стабильными релизами Go

Поддержка Go ограничена:

* официальными стабильными [релизами Go](https://dt-url.net/go-releases), скомпилированными с помощью инструментария Golang;
* стабильными [релизами Go](https://dt-url.net/go-releases) с модификациями [openssl-fips](https://dt-url.net/golang-fips) для поддержки стандартов FIPS (OneAgent версии 1.295+).

OneAgent не поддерживает исполняемые файлы, скомпилированные с помощью других инструментариев, например:

* [инструментарий gccgo](https://dt-url.net/gccgo-toolchain)

## Приложения, собранные с параметром `-linkshared`, не поддерживаются

Go поддерживает динамическое связывание стандартной библиотеки Go. Этот режим сборки используется редко, и OneAgent не выполняет инъекцию в приложения, собранные таким образом.

Пример

Рассмотрим следующее минималистичное Go-приложение с именем `GoMinimal.go`:

```
go install -buildmode=shared -linkshared std



go build -linkshared GoMinimal.go
```

OneAgent отклонит полученный исполняемый файл приложения.

## Приложения, собранные с параметром `-buildmode=pie` и отключённым CGO, не поддерживаются

Это ограничение применяется только к системам Linux.

Сборка приложения с `-buildmode=pie` и `CGO_ENABLED=0` создаёт динамически связанный исполняемый файл приложения, но без зависимости от системной библиотеки `libc`, которая необходима OneAgent.

Пример и обходное решение

Рассмотрим следующее приложение Go под названием `main.go`:

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

Сборка приложения следующей командой создаёт динамически связанный исполняемый файл приложения без зависимости от `libc`, которая необходима OneAgent:

```
CGO_ENABLED=0 go build -buildmode=pie main.go
```

В качестве обходного решения доступны несколько вариантов:

* Удалить параметр `-buildmode=pie`, что приведёт к созданию статически связанного приложения Go (см. [Статический мониторинг Go](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/enable-go-monitoring#go-static-monitoring "Узнайте, как включить мониторинг Go в Dynatrace.")).

  ```
  CGO_ENABLED=0 go build main.go
  ```
* Использовать внешний компоновщик и не отключать CGO (по умолчанию `CGO_ENABLED=1`).

  ```
  go build -ldflags="-linkmode=external" -buildmode=pie main.go
  ```

## Приложения, загружающие плагины Go, не поддерживаются

Плагин Go ([Go plugin](https://dt-url.net/eae3riv)), это пакет, скомпилированный с использованием флага сборки `-buildmode=plugin` для создания файла общего объекта. Этот режим сборки используется редко, и OneAgent отключает глубокий мониторинг, когда приложение фактически загружает плагин Go.

## Сторонние пакеты с вендорингом не поддерживаются

[Go vendoring](https://dt-url.net/ubg3r7o) используется для включения локальных копий внешних зависимостей в репозиторий проекта. Этот подход применялся для фиксации версий сторонних пакетов до добавления поддержки [Go module](https://dt-url.net/nci3rry).

OneAgent не выполняет мониторинг пакетов с вендорингом. Например, сервисы gRPC поддерживаются только при использовании Go modules или при прямом импорте [go-grpc](https://dt-url.net/k6k3r67) без применения системы управления зависимостями.

## Возможные ограничения при отсутствии таблицы символов

По умолчанию Go создаёт исполняемые файлы приложений, содержащие таблицу символов.

На данный момент в Dynatrace нет известных ограничений для бинарных файлов со stripped-символами. Однако нельзя гарантировать, что все текущие функции продолжат работать в будущих версиях Go или что все добавленные позднее функции будут поддерживаться в stripped-бинарных файлах.

Рекомендуется собирать бинарные файлы Go, содержащие таблицу символов, и избегать использования параметров командной строки или внешних инструментов, которые могут её удалить.

* Не используйте внешний инструмент `strip` (`strip <Go binary>`).
* Не компилируйте с `go build -ldflags="-s"`. Флаг `-s` удаляет таблицу символов.
* Не запускайте `go run <application>`. Эта редко используемая команда собирает и запускает приложения на лету. Поскольку выходной файл приложения является временным (файл удаляется автоматически после завершения работы приложения), исполняемый файл приложения не содержит таблицу символов.

В Dynatrace мониторинг stripped-бинарных файлов включён по умолчанию. При необходимости функцию можно отключить для тенанта, выключив **Go stripped binaries** на странице настроек [**OneAgent features**](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Управление функциями OneAgent глобально и на уровне группы процессов.").

Non-stripped бинарные файлы на AArch64 поддерживаются начиная с OneAgent версии 1.323. Поддержка stripped бинарных файлов на AArch64 добавлена в OneAgent версии 1.327.

## Приложения, собранные с включённым детектором гонок, не поддерживаются

Приложение, собранное с флагом `-race`, содержит встроенный [детектор гонок данных](https://golang.org/doc/articles/race_detector).
Этот режим сборки в основном используется в среде разработки, и OneAgent не выполняет инъекцию в приложения, собранные таким образом.

## Профилирование стека создания потоков ОС отключено

OneAgent не поддерживает [предопределённый профиль `threadcreate`](https://golang.org/doc/diagnostics#profiling). Результаты профилирования создания потоков приложений Go, отслеживаемых OneAgent, будут содержать только пустые трассы стека.

## Поддержка статически связанных бинарных файлов (только Linux)

OneAgent версии 1.203+

До OneAgent версии 1.203 статически связанные бинарные файлы не поддерживаются. Подробности в разделе [ниже](#no-static-monitoring).

После [включения статического мониторинга Go](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/enable-go-monitoring#go-static-monitoring "Узнайте, как включить мониторинг Go в Dynatrace.") OneAgent поддерживает автоматическую инъекцию для статически связанных бинарных файлов Go при выполнении следующих условий:

* Родительский процесс является динамически связанным. Это также распространяется на приложения, работающие в качестве полезной нагрузки контейнера.

  Пример

  В данном примере родительским процессом является оболочка `/bin/sh`, запускающая статически связанный исполняемый файл Go. Следующий код запускает оболочку `/bin/sh` и выполняет указанную команду.

  ```
  /bin/sh -c '/StaticGoMinimal <optional app arguments>'
  ```

  Для проверки того, является ли приложение динамически или статически связанным, можно использовать команду `file`.

  ```
  $ file -L /bin/sh



  /bin/sh: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked



  $ file -L /StaticGoMinimal



  /StaticGoMinimal: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked
  ```
* [Kubernetes Classic full-stack injection](/managed/ingest-from/setup-on-k8s/how-it-works#classic "Подробное описание развёртывания в Kubernetes."). Статически связанный исполняемый файл Go запущен как точка входа контейнера Docker.

  Пример

  ```
  FROM alpine:3.11



  COPY StaticGoMinimal /



  ENTRYPOINT ["/StaticGoMinimal"]
  ```

Если автоматическая инъекция не поддерживается для вашей конфигурации, рекомендуется вызывать статическое приложение Go через оболочку (`/bin/sh -c '/StaticGoMinimal <optional app arguments>'`).

### Cloud-native full-stack injection

Автоматическая инъекция статически связанных приложений Go, работающих в качестве точек входа контейнеров, не поддерживается при использовании варианта развёртывания [cloud-native full-stack injection](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание развёртывания в Kubernetes.") в Kubernetes.

Пример

Например, при развёртывании с cloud-native full-stack injection следующий код запускает неподдерживаемое статически связанное приложение Go.

```
FROM alpine:3.11



COPY StaticGoMinimal /



ENTRYPOINT ["/StaticGoMinimal"]
```

Для устранения этого ограничения можно изменить точку входа контейнера со статически связанного приложения Go на динамически связанное приложение, например оболочку или `init`.

Обходное решение при наличии оболочки

Применяется к образам контейнеров, которые уже содержат динамически связанный исполняемый файл оболочки.

Изменив точку входа контейнера со статически связанного приложения Go на динамически связанную оболочку, получим следующий код, который запускает `/bin/sh` и выполняет команду `/StaticGoMinimal`.

```
FROM alpine:3.11



COPY StaticGoMinimal /



ENTRYPOINT ["/bin/sh", "-c", "'/StaticGoMinimal'"]
```

Обходное решение при отсутствии оболочки

Применяется к образам контейнеров, в которых оболочка недоступна.

Если образ контейнера не содержит оболочку, например в случае [distroless images](https://dt-url.net/up23q6j), можно использовать минимальный бинарный файл `init`, например [tini](https://dt-url.net/he03qck).
Добавив tini и изменив точку входа контейнера, получим следующий код, который выполняет `/StaticGoMinimal` с сохранением корректной пересылки сигналов.

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

Обратите внимание на директиву парсера, задающую синтаксис Dockerfile версии 1, которая необходима для использования параметров `--checksum` и `--chmod` с командой `ADD`. Без неё образ должен предоставлять бинарный файл `chmod`, чтобы сделать `tini` исполняемым.
Для glibc и musl, а также архитектур amd64 и aarch64 доступны несколько вариантов tini.

### Ограничения

* Статические приложения Go, использующие cgo, не поддерживаются.

  OneAgent отклоняет мониторинг статических бинарных файлов Go, использующих [cgo](https://go.dev/blog/cgo) и, следовательно, имеющих статическую зависимость от системной библиотеки C libc. Это связано с тем, что статически связанная версия libc может конфликтовать с версией, используемой OneAgent.

  Обходное решение

  Для устранения этого ограничения можно собрать приложение Go как [динамически связанный исполняемый файл](/managed/ingest-from/technology-support/application-software/go/support/go-known-limitations#go-dynamic-linking "Ограничения поддержки Go и их обходные решения."), который динамически связывается с libc. Это гарантирует, что приложение Go и OneAgent используют одну и ту же версию libc, доступную на хосте.
* OneAgent версии 1.337+ для статического мониторинга Go требуется либо ядро Linux, предоставляющее
  системный вызов `memfd_create` (добавлен в Linux 3.17, но перенесён в более ранние версии в некоторых дистрибутивах), либо
  возможность `SYS_PTRACE` (см. следующий пункт).
* OneAgent версии 1.335 и более ранних для статического мониторинга Go требуется возможность `SYS_PTRACE`.

  Возможность `SYS_PTRACE` по умолчанию включена для Docker 19.03.0+ и ядра Linux 4.8+. Она разрешает системные вызовы между процессами, работающими в контейнере, что является требованием для статического мониторинга Go.

  Обходное решение и пример

  Для версий Docker ранее 19.03.0 или ядра Linux ранее 4.8 можно устранить это ограничение, запустив контейнер с возможностью `SYS_PTRACE`, как показано ниже.

  ```
  docker run --cap-add=SYS_PTRACE <container> ...
  ```
* Образы Docker, не предоставляющие системную библиотеку C, не поддерживаются.

  OneAgent требует наличия системной библиотеки C на отслеживаемом хосте.

  Обходное решение и пример

  Для устранения этого ограничения можно изменить базовый образ контейнера на тот, который предоставляет системную библиотеку C.

  Пример образа Docker, не предоставляющего системную библиотеку C: [scratch image](https://dt-url.net/6083rfq).

  ```
  FROM scratch



  COPY StaticGoMinimal /



  CMD ["/StaticGoMinimal"]
  ```

  Примеры образов, предоставляющих системную библиотеку C: [Alpine image](https://dt-url.net/ksa3rnj) и различные [distroless images](https://dt-url.net/up23q6j).

  ```
  FROM alpine:3.11



  COPY StaticGoMinimal /



  CMD ["/StaticGoMinimal"]
  ```

### Побочные эффекты

Файл `proc/<pId>/exe` ссылается на исполняемый файл с именем `oneagentdynamizer` вместо бинарного файла приложения Go. Он содержится в псевдофайловой системе [proc](https://dt-url.net/94c3rfn), предоставляющей интерфейс к структурам данных ядра для запущенных процессов. Это может приводить к тому, что системные инструменты, такие как `ps` или `top`, отображают `oneagentdynamizer` вместо имени бинарного файла Go.

### Версии OneAgent без поддержки статического мониторинга

OneAgent версии 1.201 и более ранних

До OneAgent версии 1.203 статически связанные бинарные файлы не поддерживаются, и для инъекции в Linux необходимо динамическое связывание. В Windows такого ограничения нет.

Динамическое связывание применяется автоматически, когда приложение использует определённые пакеты стандартной библиотеки времени выполнения, например `net/http`.
Во всех остальных случаях динамическое связывание можно принудительно задать с помощью параметра командной строки `-ldflags="-linkmode=external"`. Обратите внимание, что отключение cgo, например с помощью `CGO_ENABLED=0`, не поддерживается, и OneAgent отклонит полученный исполняемый файл приложения.

Пример

Рассмотрим следующее минималистичное Go-приложение с именем `GoMinimal.go`:

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

Сборка приложения создаёт статически связанный исполняемый файл приложения:

```
$ go build GoMinimal.go



$ file GoMinimal



GoMinimal: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, not stripped
```

Динамическое связывание можно принудительно задать с помощью `-ldflags="-linkmode=external"`:

```
$ go build -ldflags="-linkmode=external" GoMinimal.go



$ file GoMinimal



GoMinimal: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32
```

## Поддержка musl libc

Библиотека musl libc является прямой заменой библиотеки glibc. Dynatrace поддерживает приложения Go на основе musl, например собранные на Alpine Linux.

Для сборки динамически связанного исполняемого файла приложения есть одно дополнительное требование. Необходимо использовать [инструментарий Go для alpine (golang:<version>-alpine)](https://dt-url.net/3gm3rwp) и добавить `-ldflags="-linkmode=external"` (или добавить `-linkmode=external` к существующему `-ldflags`) в командную строку сборки для принудительного использования системного компоновщика. Это не требуется для статически связанных приложений Go, отслеживаемых [статическим мониторингом Go](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/enable-go-monitoring#go-static-monitoring "Узнайте, как включить мониторинг Go в Dynatrace.").

Подробности

Хотя musl libc точно имитирует функции glibc, между ними есть тонкие поведенческие различия. Кроме того, Go официально не поддерживает инструментарий Go на основе musl, а значит, бинарные файлы инструментария Go нельзя загрузить с веб-сайта [golang.org](https://dt-url.net/go).

Кроме того, существует [серьёзная проблема](https://dt-url.net/6vq3rim) с тем, как Go использует musl libc. Это ограничивает возможности Dynatrace по поддержке приложений на основе musl. Инструментарий Go включает внутренний компоновщик, который создаёт бинарные файлы приложений на основе musl, не инициализирующие musl libc правильно при запуске приложения. Эта проблема не позволяет Dynatrace отслеживать такие приложения. В этом случае на странице соответствующего процесса приложения отображается следующее сообщение:
**Активация глубокого мониторинга завершилась неудачно. Мониторинг бинарных файлов Go musl, собранных с внутренним компоновщиком Go, не поддерживается**

При использовании системного компоновщика для создания бинарного файла приложения он добавляет стартовый код, правильно инициализирующий общие объекты. Добавление `-ldflags="-linkmode=external"` в командную строку сборки принудительно задаёт использование системного компоновщика. Полученный бинарный файл будет выполняться с правильно инициализированным libc, что позволяет Dynatrace отслеживать такое приложение.

Пример

Рассмотрим следующее минималистичное Go-приложение с именем `GoMinimal.go`:

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

Следующий многоэтапный Dockerfile создаёт допустимый динамически связанный бинарный файл Go musl на этапе 1 и запускает приложение на этапе 2.

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

Соберите контейнер и запустите приложение:

```
docker build -t gominimal-alpine .



docker run --interactive gominimal-alpine
```

Кроме того, существует проблема с реализацией musl malloc на машинах с 64 и более ЦП, которая может привести к высокой нагрузке на ЦП. Это можно решить следующими способами:

* использование базового образа на основе glibc;
* предварительная загрузка альтернативной реализации malloc, например [tcmalloc](https://dt-url.net/xz03zxt) или [jemalloc](https://dt-url.net/9523zi0), как описано ниже.

Предварительная загрузка tcmalloc

Для предварительной загрузки tcmalloc возьмите Dockerfile из приведённого выше примера и скорректируйте этап 2, как показано в блоке кода ниже.

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

Предварительная загрузка jemalloc

Для предварительной загрузки jemalloc возьмите Dockerfile из приведённого выше примера и скорректируйте этап 2, как показано в блоке кода ниже.

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