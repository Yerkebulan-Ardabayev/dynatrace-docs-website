---
title: Install Dynatrace Configuration as Code via Monaco
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/installation
---

# Install Dynatrace Configuration as Code via Monaco

# Install Dynatrace Configuration as Code via Monaco

* How-to guide
* 3-min read
* Published Oct 25, 2022

This guide shows you how to download and install Dynatrace Configuration as Code via Monaco (the Dynatrace Monaco CLI).

## Install the Dynatrace Monaco CLI

### Linux

Linux 64-bit (AMD)

Linux 64-bit (ARM)

Linux 32-bit

1. Download the latest version of the Dynatrace Configuration as Code CLI tool.

   ```
   curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-amd64 -o monaco-linux-amd64
   ```
2. Optional Verify the downloaded binary using the checksum.

   To verify that the downloaded binary is valid, do the following steps:

   1. Download its checksum file.

      ```
      curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-amd64.sha256 -o monaco.sha256
      ```

   2. Verify the downloaded binary using the checksum.

      ```
      shasum -c monaco.sha256
      ```

      You should see the following output.

      ```
      monaco-linux-amd64: OK
      ```

      This requires `monaco-linux-amd64` and `monaco.sha256` to be in the same directory, which they are if you followed the steps above.
3. Rename the specific executable to `monaco`.

   ```
   mv monaco-linux-amd64 monaco
   ```
4. Make the binary executable.

   ```
   chmod +x monaco
   ```
5. Optional Install Dynatrace Configuration as Code CLI to a central location in your `PATH`.

   ```
   sudo mv monaco /usr/local/bin/
   ```

   This command assumes that you downloaded the binary to the current folder with the `curl` command described in step 1 and that your `$PATH` includes `/usr/local/bin`.

1. Download the latest version of the Dynatrace Configuration as Code.

   ```
   curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-arm64 -o monaco-linux-arm64
   ```
2. Optional Verify the downloaded binary using the checksum.

   To verify that the downloaded binary is valid, do the following steps:

   1. Download its checksum file.

      ```
      curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-arm64.sha256 -o monaco.sha256
      ```

   2. Verify the downloaded binary using the checksum.

      ```
      shasum -c monaco.sha256
      ```

      You should see the following output.

      ```
      monaco-linux-arm64: OK
      ```

      This requires `monaco-linux-arm64` and `monaco.sha256` to be in the same directory, which they're if you followed the steps above.
3. Rename the specific executable to `monaco`.

   ```
   mv monaco-linux-arm64 monaco
   ```
4. Make the binary executable.

   ```
   chmod +x monaco
   ```
5. Optional Install Dynatrace Configuration as Code CLI to a central location in your `PATH`.

   ```
   sudo mv monaco /usr/local/bin/
   ```

   This command assumes that you downloaded the binary to the current folder with the `curl` command described in step 1 and that your `$PATH` includes `/usr/local/bin`.

1. Download the latest version of the Dynatrace Configuration as Code CLI tool.

   ```
   curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-386 -o monaco-linux-386
   ```
2. Optional Verify the downloaded binary using the checksum.

   To verify that the downloaded binary is valid, do the following steps:

   1. Download its checksum file.

      ```
      curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-386.sha256 -o monaco.sha256
      ```

   2. Verify the downloaded binary using the checksum.

      ```
      shasum -c monaco.sha256
      ```

      You should see the following output.

      ```
      monaco-linux-386: OK
      ```

      This requires `monaco-linux-386` and `monaco.sha256` to be in the same directory, which they are if you followed the steps above.
3. Rename the specific executable to `monaco`.

   ```
   mv monaco-linux-386 monaco
   ```
4. Make the binary executable.

   ```
   chmod +x monaco
   ```
5. Optional Install Dynatrace Configuration as Code CLI to a central location in your `PATH`.

   ```
   sudo mv monaco /usr/local/bin/
   ```

   This command assumes that you downloaded the binary to the current folder with the `curl` command described in step 1 and that your `$PATH` includes `/usr/local/bin`.

### macOS

Apple Silicon (M-series)

Intel 64-bit

1. Download the latest version of the Dynatrace Configuration as Code CLI tool.

   ```
   curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-darwin-arm64 -o monaco-darwin-arm64
   ```
2. Optional Verify the downloaded binary using the checksum.

   To verify that the downloaded binary is valid, do the following steps:

   1. Download its checksum file.

      ```
      curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-darwin-arm64.sha256 -o monaco.sha256
      ```

   2. Verify the downloaded binary using the checksum.

      ```
      shasum -c monaco.sha256
      ```

      You should see the following output.

      ```
      monaco-darwin-arm64: OK
      ```

      This requires `monaco-darwin-arm64` and `monaco.sha256` to be in the same directory, which they are if you followed the steps above.
3. Rename the specific executable to `monaco`.

   ```
   mv monaco-darwin-arm64 monaco
   ```
4. Make the binary executable.

   ```
   chmod +x monaco
   ```
5. Optional Install Dynatrace Configuration as Code CLI to a central location in your `PATH`.

   ```
   sudo mv monaco /usr/local/bin/
   ```

   This command assumes that you downloaded the binary to the current folder with the `curl` command described in step 1 and that your `$PATH` includes `/usr/local/bin`.

1. Download the latest version of the Dynatrace Configuration as Code CLI tool.

   ```
   curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-darwin-amd64 -o monaco-darwin-amd64
   ```
2. Optional Verify the downloaded binary using the checksum.

   To verify that the downloaded binary is valid, do the following steps:

   1. Download its checksum file.

      ```
      curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-darwin-amd64.sha256 -o monaco.sha256
      ```

   2. Verify the downloaded binary using the checksum.

      ```
      shasum -c monaco.sha256
      ```

      You should see the following output.

      ```
      monaco-darwin-amd64: OK
      ```

      This requires `monaco-darwin-amd64` and `monaco.sha256` to be in the same directory, which they are if you followed the steps above.
3. Rename the specific executable to `monaco`.

   ```
   mv monaco-darwin-amd64 monaco
   ```
4. Make the binary executable.

   ```
   chmod +x monaco
   ```
5. Optional Install Dynatrace Configuration as Code CLI to a central location in your `PATH`.

   ```
   sudo mv monaco /usr/local/bin/
   ```

   This command assumes that you downloaded the binary to the current folder with the `curl` command described in step 1 and that your `$PATH` includes `/usr/local/bin`.

### Windows

Windows 64-bit

Windows 32-bit

1. Open Windows PowerShell.
2. Download the latest version of the Dynatrace Configuration as Code CLI tool.

   ```
   Invoke-WebRequest -URI https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-windows-amd64.exe -OutFile monaco.exe
   ```

   This executable is signed by Dynatrace.
3. Optional Add Monaco to a central location in your `PATH`.

   1. Move monaco to the folder you want to add your `PATH`.
   2. Go to **Environment Variables** in your system settings.
   3. Scroll through system variables until you find `PATH`.
   4. Edit and change accordingly.

      * Use a semicolon delimiter between the previous entry and your new path (`c:\path;<your-new-path>`).
   5. Launch a new console for the settings to take effect.

1. Open Windows PowerShell.
2. Download the latest version of the Dynatrace Configuration as Code CLI tool.

   ```
   Invoke-WebRequest -URI https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-windows-386.exe -OutFile monaco.exe
   ```

   This executable is signed by Dynatrace.
3. Optional Add Monaco to a central location in your `PATH`.

   1. Move monaco to the folder you want to add your `PATH`.
   2. Go to **Environment Variables** in your system settings.
   3. Scroll through system variables until you find `PATH`.
   4. Edit and change accordingly.

      * Use a semicolon delimiter between the previous entry and your new path (`c:\path;<your-new-path>`).
   5. Launch a new console for the settings to take effect.

## Container image

A container image of the Dynatrace Monaco CLI is available to simplify usage in CI/CD pipelines.

Images are available via [Docker Hub﻿](https://dt-url.net/config-as-code-container):

```
docker pull dynatrace/dynatrace-configuration-as-code:latest
```

By default, commands run in the container image are running from a `/monaco` working directory. If you map your configurations into the container as a Docker volume, it's easiest to map the volume to this directory.

In the following example, we validate a project contained in `/your/path/to/project` with a `manifest.yaml` reading the deployment access token from an `ACCESS_TOKEN` variable.

```
docker run \



--env ACCESS_TOKEN=XXX \



--mount type=bind,src="/your/path/to/project",target=/monaco \



dynatrace/dynatrace-configuration-as-code:latest deploy -d manifest.yaml
```

The container image uses the `monaco` executable as its entrypoint, so any inputs are passed directly to it.

However, some CI/CD tools (for example, GitLab CI/CD) need a regular shell as entrypoint. To make the container image work with these tools, you need to overwrite the entrypoint with `sh`.

* GitLab CI/CD

  For details on how to use the image with GitLab CI/CD, follow the [Override the entrypoint of an image﻿](https://docs.gitlab.com/ee/ci/docker/using_docker_images.html#override-the-entrypoint-of-an-image) GitLab documentation.
* `docker run`

  For general information on overwriting container entrypoints when using `docker run`, see the [Docker documentation﻿](https://docs.docker.com/engine/reference/commandline/run/).

### Verify the image signature

Dynatrace Monaco CLI version 2.2.0+

The container image is signed to allow you to verify its authenticity.

Verify the container image signature

You can verify the signature using [cosign﻿](https://docs.sigstore.dev/cosign/) and the `cosign.pub` key that can be downloaded from the [GitHub release page﻿](https://dt-url.net/get-configuration-as-code).

To verify the signature of a given version

1. Install the applicable version of cosign for your operating system, following the [installation instructions﻿](https://docs.sigstore.dev/cosign/installation/).
2. Download the `cosign.pub` public key from the [GitHub release page﻿](https://dt-url.net/get-configuration-as-code) of the version you wish to verify.
3. Verify the container image of the version you wish to check:

   ```
   cosign verify --key cosign.pub dynatrace/dynatrace-configuration-as-code:[VERSION]
   ```

   For example, to verify version `2.2.0`:

   ```
   cosign verify --key cosign.pub dynatrace/dynatrace-configuration-as-code:2.2.0
   ```

## Run monaco

Execute the `monaco` command to try out the downloaded CLI.

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

## What's next

* Learn how available memory and CPU impact deployments in [Hardware requirements for Dynatrace Monaco CLI](/managed/deliver/configuration-as-code/monaco/reference/hardware-requirements "Hardware requirements for Dynatrace Configuration as Code via Monaco").

## Related topics

* [Monaco configuration overview](/managed/deliver/configuration-as-code/monaco/configuration "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.")
* [Migrate configuration from Monaco 1.x to 2.x](/managed/deliver/configuration-as-code/monaco/guides/migrating-to-v2 "Migrate existing Monaco 1.x projects to version 2.x.")
* [Hardware requirements for Dynatrace Monaco CLI](/managed/deliver/configuration-as-code/monaco/reference/hardware-requirements "Hardware requirements for Dynatrace Configuration as Code via Monaco")