---
title: GraalVM Native Image
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java/graalvm-native-image
scraped: 2026-02-18T21:18:11.739267
---

# GraalVM Native Image

# GraalVM Native Image

* Latest Dynatrace
* 8-min read
* Published Jul 02, 2024

OneAgent version 1.295+ Dynatrace version 1.295+

[GraalVM Native Imageï»¿](https://www.graalvm.org/latest/docs/getting-started/) is designed to achieve high performance when running applications written in Java and other languages by pre-compiling Java code into native images. AOT-compiled native images contain only the Java code required at runtime and exclude everything else from the libraries and frameworks.

Dynatrace provides end-to-end distributed tracing for your native Java applications pre-compiled as GraalVM Native Image running in virtualized, containerized, and K8s environments. Dynatrace automatically discovers your native Java apps' services and visualizes their dependencies from the website to containers, infrastructure, and the cloud. It diagnoses anomalies in real-time using AI and determines the root cause down to the broken code. Performance metrics give you insight into memory usage, garbage collection, and threads.

For the supported distributed tracing technologies, see [Java Native Image](/docs/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Dynatrace GraalVM Native Image observability requires a [Full-Stack Monitoring](/docs/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") license.

## Get started

The Dynatrace GraalVM Native Image module consists of a **build-time module** and a **runtime module**. The build-time module must be present during Native Image build-time. The runtime module must be present when the Native Image is executed to capture telemetry data.

* Both modules must be of the same version for compatibility reasons.
* The Dynatrace environment version must be equal to or later than the version of the GraalVM Native modules.
* No changes to your application code are required.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Integrate Dynatrace in your project**](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image#integration "Install, configure, and manage Dynatrace GraalVM Native Image module.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Activate Dynatrace observability**](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image#activate "Install, configure, and manage Dynatrace GraalVM Native Image module.")

### Step 1 Integrate Dynatrace in your project

#### Maven projects

To integrate Dynatrace in a Maven project

1. Add the following to your `pom.xml` file:

   ```
   <profile>



   <id>dynatrace-native</id>



   <build>



   <plugins>



   <plugin>



   <groupId>com.dynatrace.buildtools.graalnative</groupId>



   <artifactId>dynatrace-native-maven-plugin</artifactId>



   <version>2.1.0</version>



   <executions>



   <execution>



   <goals>



   <goal>setup-build-agent</goal>



   <goal>copy-runtime-agent</goal>



   </goals>



   <configuration>



   <agentDownload>



   <environmentUrl>ENVIRONMENT_URL</environmentUrl>



   <apiToken>API_TOKEN</apiToken>



   </agentDownload>



   </configuration>



   </execution>



   </executions>



   <extensions>true</extensions>



   </plugin>



   </plugins>



   </build>



   </profile>
   ```

   Replace `ENVIRONMENT_URL` and `API_TOKEN` according to your Dynatrace environment:

   * `ENVIRONMENT_URL` is the Dynatrace environment URL of your [monitoring environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
   * `API_TOKEN` is your access token and can, for example, be provided with an environment variable by using `<apiToken>${env.DT_API_TOKEN}</apiToken>`. This access token requires the **PaaS integration - Installer download** scope. To learn how to generate the token, see [Generate access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").

   This will automatically download and use the latest GraalVM Native Image module version available in your environment. To use a specific GraalVM Native Image module version, add `<agentVersion>AGENT_VERSION</agentVersion>` to the `agentDownload` configuration.

   Alternatively, you can also [manually download the GraalVM Native Image module](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image#manual-agent-download "Install, configure, and manage Dynatrace GraalVM Native Image module.") and use

   ```
   <configuration>



   <agentZip>PATH_TO_DOWNLOADED_ZIP</agentZip>



   </configuration>
   ```

   to configure the Dynatrace plugin. Replace `PATH_TO_DOWNLOADED_ZIP` with the absolute or relative path to the downloaded ZIP file.
2. Run `mvnw package -Pnative -Pdynatrace-native`. This will generate a Native Image, including Dynatrace. The `native` profile adds the [Maven plugin for GraalVM Native image buildingï»¿](https://graalvm.github.io/native-build-tools/latest/maven-plugin.html#configuration-registering-plugin).

   Typically, the resulting Native Image will be available in the `target` folder. In addition to the Native Image, there will be a `dynatrace` folder. It is required for monitoring at runtime. If you want to run the Native Image on another machine, copy the `dynatrace` folder along with the Native Image.

#### Gradle projects

Prerequisites

* Gradle 8.4+ runs on a supported [JVM](/docs/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") or [Native Image](/docs/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.") of Java version 17+.
* Gradle plugin `org.graalvm.buildtools:native-gradle-plugin` with version 0.10+ is applied to your project.

To integrate Dynatrace in a Gradle project

1. Add the following code to `settings.gradle`:

   ```
   pluginManagement {



   repositories {



   mavenCentral()



   }



   }
   ```
2. Add the following code to `build.gradle`:

   ```
   plugins {



   id 'com.dynatrace.buildtools.graalnative' version '2.1.0'



   }



   dynatrace {



   agentDownload {



   environmentUrl = "ENVIRONMENT_URL"



   apiToken = "API_TOKEN"



   }



   }
   ```

   Replace `ENVIRONMENT_URL` and `API_TOKEN` according to your Dynatrace environment:

   * `ENVIRONMENT_URL` is the Dynatrace environment URL of your [monitoring environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
   * `API_TOKEN` is your access token and can, for example, be provided with an environment variable by using `System.getenv("DT_API_TOKEN")`. This access token requires the **PaaS integration - Installer download** scope. To learn how to generate the token, see [Generate access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").

   This will automatically download and use the latest GraalVM Native Image module version available in your environment. To use a specific GraalVM Native Image module version, add `agentVersion = "AGENT_VERSION"` to the `agentDownload` configuration.

   Alternatively, you can also [manually download the GraalVM Native Image module](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image#manual-agent-download "Install, configure, and manage Dynatrace GraalVM Native Image module.") and use

   ```
   dynatrace {



   agentZip = "PATH_TO_DOWNLOADED_ZIP"



   }
   ```

   to configure the Dynatrace plugin. Replace `PATH_TO_DOWNLOADED_ZIP` with the absolute or relative path to the downloaded ZIP file.
3. Run `gradlew dynatraceNativeCompile` to generate a Native Image, including Dynatrace.

   Typically, the resulting Native Image is available in the folder `build/native/nativeCompile`. In addition to the Native Image, the folder contains a `dynatrace` folder. It is required for monitoring at runtime. If you want to run the Native Image on another machine, copy the `dynatrace` folder along with the Native Image.

#### Manually downloading the GraalVM Native Image module

You can also manually download the GraalVM Native Image module from [Dynatrace OneAgent Deployment API](/docs/dynatrace-api/environment-api/deployment/oneagent "Download OneAgent installers via Dynatrace API.") for your target platform.

An example API call using `curl`:

```
curl -X GET "$DT_TENANT_URL/api/v1/deployment/installer/agent/$OS_TYPE/paas/latest?flavor=default&arch=$ARCH&bitness=64&include=java-graal-native&skipMetadata=true" -H "accept: application/octet-stream"  -H "Authorization: Api-Token $DT_API_TOKEN" -o agent.zip
```

Replace `$DT_TENANT_URL`, `$OS_TYPE`, `$ARCH`, and `$DT_API_TOKEN` with your Dynatrace environment values.

* `$DT_TENANT_URL` is your Dynatrace environment URL.
* `$OS_TYPE` can be `unix` or `windows`.
* `$ARCH` can be `x86` or `arm`, while `arm` is only available for the OS type `unix`.
* `$DT_API_TOKEN` is your access token with the **PaaS integration - Installer download** scope. To learn how to generate the token, see [Generate access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").



### Step 2 optional Activate Dynatrace observability

If you already have OneAgent installed or use Dynatrace Operator for Kubernetes, the Dynatrace connection details are automatically applied and GraalVM Native Image observability activated.

To activate Dynatrace observability at runtime, define your Dynatrace connection details using the environment variables `DT_TENANT`, `DT_TENANTTOKEN`, and `DT_CONNECTION_POINT`. An example for Dynatrace SaaS:

```
export DT_TENANT=$DT_TENANT_ID



export DT_TENANTTOKEN=$DT_TENANTTOKEN



export DT_CONNECTION_POINT=$DT_CONNECTION_POINT



./$YOUR_APP_NAME
```

Replace `$DT_TENANT_ID`, `$DT_TENANTTOKEN`, and `$DT_CONNECTION_POINT` with your Dynatrace connection details. Replace `$YOUR_APP_NAME` with your application name.

You can retrieve your connection details via [View connectivity information for OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "View the connectivity information of OneAgent via Dynatrace API.") API call. You need the following fields of the response:

* **tenantUUID** for `$DT_TENANT_ID`
* **tenantToken** for `$DT_TENANTTOKEN`
* **communicationEndpoints** for `$DT_CONNECTION_POINT`

## Plugin configuration

### Maven plugin

The Maven plugin is configured via the `dynatrace-native` profile in the `pom.xml` file. For example:

```
<configuration>



<agentDownload>



<environmentUrl>${env.DT_TENANT_URL}</environmentUrl>



<apiToken>${env.DT_API_TOKEN}</apiToken>



</agentDownload>



<agentOptions>loglevelcon=info</agentOptions>



</configuration>
```

You can configure the following properties:

* `agentDownload` is used to configure the automatic GraalVM Native Image module download:

  + `environmentUrl` specifies the Dynatrace environment URL of your [monitoring environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
  + `apiToken` specifies the access token with **PaaS integration - Installer download** scope. To learn how to generate the token, see [Generate access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").
  + `agentVersion` specifies the GraalVM Native Image module version. If not set, the latest GraalVM Native Image module version is used.
* `agentZip` sets the absolute or relative path to the manually downloaded ZIP file.
* `agentOptions` defines the options for the Dynatrace build-time module (optional).

The following `agentOptions` are available:

* `loglevelcon` sets the console logging level. Possible values: `off` (default), `severe`, `warning`, and `info`.
* `agentconfigpath` sets the absolute path to a JSON configuration file (see the next section).

### Gradle plugin

The Gradle plugin is configured via a `dynatrace` block in `build.gradle`. For example:

```
dynatrace {



agentDownload {



environmentUrl = System.getenv("DT_TENANT_URL")



apiToken = System.getenv("DT_API_TOKEN")



}



agentOptions="loglevelcon=info"



}
```

You can configure the following properties:

* `agentDownload` is used to configure the automatic GraalVM Native Image module download:

  + `environmentUrl` specifies the Dynatrace environment URL of your [monitoring environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
  + `apiToken` specifies the access token with **PaaS integration - Installer download** scope. To learn how to generate the token, see [Generate access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").
  + `agentVersion` specifies the GraalVM Native Image module version. If not set, the latest GraalVM Native Image module version is used.
* `agentZip` sets the absolute or relative path to the manually downloaded ZIP file.
* `agentOptions` defines the options for the Dynatrace build-time module (optional).

The following `agentOptions` are available:

* `loglevelcon` sets the console logging level. Possible values: `off` (default), `severe`, `warning`, and `info`.
* `agentconfigpath` sets the absolute path to a JSON configuration file (see the next section).

## GraalVM Native Image module configuration

### Build-time module

The Dynatrace build-time module is preconfigured with recommended settings. If needed, you can override the defaults via a JSON configuration file at build time. For example:

```
{



"enabledSensors": [



"servlet"



]



}
```

The following `enabledSensors` (instrumentation points) are available:

* `servlet`: Incoming HTTP requests via Servlet API
* `netty`: Incoming HTTP requests via Netty
* `httpclient`: Outgoing HTTP requests
* `threading`: Context propagation for threads and executors
* `mongo`: MongoDB database calls

Remove a sensor from the `enabledSensors` list to deactivate it.

### Runtime module

#### FIPS mode

FIPS mode is disabled by default. To enable FIPS mode for the runtime module, delete the `agent/dt_fips_disabled.flag` file in the `dynatrace` folder next to the Native Image.

## Known limitations

### Limited GraalVM Native Image module feature set

The GraalVM Native Image module does not have all the features of the regular Java module. The technologies supported by the GraalVM Native Image module can be found in the [Java Native Image](/docs/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.") section of the technology support page.

Furthermore, the GraalVM Native Image module currently does not support:

* Application Security, including runtime vulnerability analytics, and runtime application protection
* Real-time updates for Java services
* CPU profiling
* Memory profiling
* Memory dump analysis
* Built-in metricsâlimited support; suspension time metrics are not reported

### Spring RestTemplate

This is expected to be no longer necessary in GraalVM versions 17.0.12+, 21.0.4+, and 22.0.2+.

If you are using Spring RestTemplate and get unconnected traces, please try the following workaround.

#### Maven projects

Configure in your `pom.xml` file:

```
<jvmArgs>



<arg>--add-opens=java.base/sun.net.www.protocol.http=ALL-UNNAMED</arg>



<arg>--add-opens=java.base/java.net=ALL-UNNAMED</arg>



<arg>--add-exports=java.base/sun.net.www=ALL-UNNAMED</arg>



</jvmArgs>
```

For reference, see [Maven plugin for GraalVM Native Image buildingï»¿](https://graalvm.github.io/native-build-tools/latest/maven-plugin.html#configuration-options).

#### Gradle projects

Configure in your `build.gradle` file:

```
graalvmNative {



binaries {



main {



jvmArgs.addAll(



'--add-opens', 'java.base/sun.net.www.protocol.http=ALL-UNNAMED',



'--add-opens', 'java.base/java.net=ALL-UNNAMED',



'--add-exports', 'java.base/sun.net.www=ALL-UNNAMED'



)



}



}



}
```