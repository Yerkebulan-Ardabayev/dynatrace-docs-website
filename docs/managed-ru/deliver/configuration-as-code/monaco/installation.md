---
title: Установка Dynatrace Configuration as Code через Monaco
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/installation
scraped: 2026-05-12T11:21:35.690179
---

# Install Dynatrace Configuration as Code via Monaco

# Install Dynatrace Configuration as Code via Monaco

* How-to guide
* 3-min read
* Published Oct 25, 2022

Данное руководство описывает загрузку и установку Dynatrace Configuration as Code через Monaco (Dynatrace Monaco CLI).

## Установка Dynatrace Monaco CLI

### Linux

Linux 64-bit (AMD)

Linux 64-bit (ARM)

Linux 32-bit

1. Загрузите последнюю версию CLI-инструмента Dynatrace Configuration as Code.

   ```
   curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-amd64 -o monaco-linux-amd64
   ```
2. Необязательно: проверьте загруженный бинарный файл с помощью контрольной суммы.

   Для проверки корректности загруженного бинарного файла:

   1. Загрузите файл контрольной суммы.

      ```
      curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-amd64.sha256 -o monaco.sha256
      ```

   2. Проверьте загруженный бинарный файл по контрольной сумме.

      ```
      shasum -c monaco.sha256
      ```

      Должен появиться следующий вывод:

      ```
      monaco-linux-amd64: OK
      ```

      Для этого `monaco-linux-amd64` и `monaco.sha256` должны находиться в одной директории, что выполняется при следовании шагам выше.
3. Переименуйте исполняемый файл в `monaco`.

   ```
   mv monaco-linux-amd64 monaco
   ```
4. Сделайте бинарный файл исполняемым.

   ```
   chmod +x monaco
   ```
5. Необязательно: установите CLI Dynatrace Configuration as Code в центральное место в вашем `PATH`.

   ```
   sudo mv monaco /usr/local/bin/
   ```

   Эта команда предполагает, что бинарный файл загружен в текущую папку командой `curl` из шага 1, и что `$PATH` включает `/usr/local/bin`.

1. Загрузите последнюю версию Dynatrace Configuration as Code.

   ```
   curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-arm64 -o monaco-linux-arm64
   ```
2. Необязательно: проверьте загруженный бинарный файл с помощью контрольной суммы.

   1. Загрузите файл контрольной суммы.

      ```
      curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-arm64.sha256 -o monaco.sha256
      ```

   2. Проверьте загруженный бинарный файл.

      ```
      shasum -c monaco.sha256
      ```

      Должен появиться следующий вывод:

      ```
      monaco-linux-arm64: OK
      ```
3. Переименуйте исполняемый файл в `monaco`.

   ```
   mv monaco-linux-arm64 monaco
   ```
4. Сделайте бинарный файл исполняемым.

   ```
   chmod +x monaco
   ```
5. Необязательно: установите в `PATH`.

   ```
   sudo mv monaco /usr/local/bin/
   ```

1. Загрузите последнюю версию CLI-инструмента Dynatrace Configuration as Code.

   ```
   curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-386 -o monaco-linux-386
   ```
2. Необязательно: проверьте загруженный бинарный файл.

   1. Загрузите файл контрольной суммы.

      ```
      curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-386.sha256 -o monaco.sha256
      ```

   2. Проверьте бинарный файл.

      ```
      shasum -c monaco.sha256
      ```

      Должен появиться следующий вывод:

      ```
      monaco-linux-386: OK
      ```
3. Переименуйте исполняемый файл в `monaco`.

   ```
   mv monaco-linux-386 monaco
   ```
4. Сделайте бинарный файл исполняемым.

   ```
   chmod +x monaco
   ```
5. Необязательно: установите в `PATH`.

   ```
   sudo mv monaco /usr/local/bin/
   ```

### macOS

Apple Silicon (серия M)

Intel 64-bit

1. Загрузите последнюю версию CLI-инструмента Dynatrace Configuration as Code.

   ```
   curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-darwin-arm64 -o monaco-darwin-arm64
   ```
2. Необязательно: проверьте загруженный бинарный файл.

   1. Загрузите файл контрольной суммы.

      ```
      curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-darwin-arm64.sha256 -o monaco.sha256
      ```

   2. Проверьте бинарный файл.

      ```
      shasum -c monaco.sha256
      ```

      Должен появиться следующий вывод:

      ```
      monaco-darwin-arm64: OK
      ```
3. Переименуйте исполняемый файл в `monaco`.

   ```
   mv monaco-darwin-arm64 monaco
   ```
4. Сделайте бинарный файл исполняемым.

   ```
   chmod +x monaco
   ```
5. Необязательно: установите в `PATH`.

   ```
   sudo mv monaco /usr/local/bin/
   ```

1. Загрузите последнюю версию CLI-инструмента Dynatrace Configuration as Code.

   ```
   curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-darwin-amd64 -o monaco-darwin-amd64
   ```
2. Необязательно: проверьте загруженный бинарный файл.

   1. Загрузите файл контрольной суммы.

      ```
      curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-darwin-amd64.sha256 -o monaco.sha256
      ```

   2. Проверьте бинарный файл.

      ```
      shasum -c monaco.sha256
      ```

      Должен появиться следующий вывод:

      ```
      monaco-darwin-amd64: OK
      ```
3. Переименуйте исполняемый файл в `monaco`.

   ```
   mv monaco-darwin-amd64 monaco
   ```
4. Сделайте бинарный файл исполняемым.

   ```
   chmod +x monaco
   ```
5. Необязательно: установите в `PATH`.

   ```
   sudo mv monaco /usr/local/bin/
   ```

### Windows

Windows 64-bit

Windows 32-bit

1. Откройте Windows PowerShell.
2. Загрузите последнюю версию CLI-инструмента Dynatrace Configuration as Code.

   ```
   Invoke-WebRequest -URI https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-windows-amd64.exe -OutFile monaco.exe
   ```

   Данный исполняемый файл подписан Dynatrace.
3. Необязательно: добавьте Monaco в центральное место в вашем `PATH`.

   1. Переместите monaco в папку, которую хотите добавить в `PATH`.
   2. Перейдите в **Environment Variables** в системных настройках.
   3. Прокрутите системные переменные до нахождения `PATH`.
   4. Отредактируйте соответствующим образом.

      * Используйте точку с запятой в качестве разделителя между предыдущей записью и новым путём (`c:\path;<your-new-path>`).
   5. Откройте новую консоль, чтобы настройки вступили в силу.

1. Откройте Windows PowerShell.
2. Загрузите последнюю версию CLI-инструмента Dynatrace Configuration as Code.

   ```
   Invoke-WebRequest -URI https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-windows-386.exe -OutFile monaco.exe
   ```

   Данный исполняемый файл подписан Dynatrace.
3. Необязательно: добавьте Monaco в `PATH` (аналогично 64-bit варианту выше).

## Образ контейнера

Образ контейнера Dynatrace Monaco CLI доступен для упрощения использования в CI/CD-пайплайнах.

Образы доступны через [Docker Hub](https://dt-url.net/config-as-code-container):

```
docker pull dynatrace/dynatrace-configuration-as-code:latest
```

По умолчанию команды в образе контейнера выполняются из рабочей директории `/monaco`. При монтировании конфигураций в контейнер через Docker volume удобнее всего монтировать том в эту директорию.

В следующем примере мы проверяем проект в `/your/path/to/project` с `manifest.yaml`, считывающим токен доступа для развёртывания из переменной `ACCESS_TOKEN`.

```
docker run \



--env ACCESS_TOKEN=XXX \



--mount type=bind,src="/your/path/to/project",target=/monaco \



dynatrace/dynatrace-configuration-as-code:latest deploy -d manifest.yaml
```

Образ контейнера использует исполняемый файл `monaco` в качестве точки входа, поэтому все входные данные передаются непосредственно ему.

Однако некоторые инструменты CI/CD (например, GitLab CI/CD) требуют обычной оболочки в качестве точки входа. Для работы образа контейнера с такими инструментами необходимо переопределить точку входа на `sh`.

* GitLab CI/CD

  Подробности об использовании образа с GitLab CI/CD см. в документации GitLab [Override the entrypoint of an image](https://docs.gitlab.com/ee/ci/docker/using_docker_images.html#override-the-entrypoint-of-an-image).
* `docker run`

  Общую информацию о переопределении точек входа контейнеров с помощью `docker run` см. в [документации Docker](https://docs.docker.com/engine/reference/commandline/run/).

### Проверка подписи образа

Dynatrace Monaco CLI версии 2.2.0+

Образ контейнера подписан, что позволяет проверить его подлинность.

Проверка подписи образа контейнера

Подпись можно проверить с помощью [cosign](https://docs.sigstore.dev/cosign/) и ключа `cosign.pub`, который можно загрузить со [страницы релиза GitHub](https://dt-url.net/get-configuration-as-code).

Для проверки подписи конкретной версии:

1. Установите соответствующую версию cosign для вашей операционной системы согласно [инструкциям по установке](https://docs.sigstore.dev/cosign/installation/).
2. Загрузите публичный ключ `cosign.pub` со [страницы релиза GitHub](https://dt-url.net/get-configuration-as-code) нужной версии.
3. Проверьте образ контейнера проверяемой версии:

   ```
   cosign verify --key cosign.pub dynatrace/dynatrace-configuration-as-code:[VERSION]
   ```

   Например, для проверки версии `2.2.0`:

   ```
   cosign verify --key cosign.pub dynatrace/dynatrace-configuration-as-code:2.2.0
   ```

## Запуск monaco

Выполните команду `monaco` для проверки загруженного CLI.

```
> monaco



Tool used to deploy dynatrace configurations via the cli



Examples:



Deploy configuration defined in a manifest



monaco deploy service.yaml



Deploy a specific environment within an manifest



monaco deploy service.yaml -e dev



Usage:



monaco <command> [flags]



monaco [command]



Available Commands:



account     Manage account management resources



completion  Generate the autocompletion script for the specified shell



delete      Delete configurations defined in delete.yaml from the environments defined in the manifest



deploy      Deploy configurations to Dynatrace environments



download    Download configuration from Dynatrace



generate    Generate offers several sub-commands to generate files - take a look at the sub-commands for usage



help        Help about any command



version     Prints out the version of the monaco cli



Flags:



-h, --help              help for monaco



--support-archive   Create support archive



-v, --verbose           Enable debug logging



Use "monaco [command] --help" for more information about a command.
```

## Что дальше

* Узнайте, как доступная память и CPU влияют на развёртывания, в [Аппаратные требования Dynatrace Monaco CLI](/managed/deliver/configuration-as-code/monaco/reference/hardware-requirements "Hardware requirements for Dynatrace Configuration as Code via Monaco").

## Связанные темы

* [Обзор конфигурации Monaco](/managed/deliver/configuration-as-code/monaco/configuration "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.")
* [Миграция конфигурации с Monaco 1.x на 2.x](/managed/deliver/configuration-as-code/monaco/guides/migrating-to-v2 "Migrate existing Monaco 1.x projects to version 2.x.")
* [Аппаратные требования Dynatrace Monaco CLI](/managed/deliver/configuration-as-code/monaco/reference/hardware-requirements "Hardware requirements for Dynatrace Configuration as Code via Monaco")