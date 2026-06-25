---
title: Set up Dynatrace OneAgent as a Docker container
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container
scraped: 2026-05-12T11:11:04.917700
---

# Set up Dynatrace OneAgent as a Docker container

# Set up Dynatrace OneAgent as a Docker container

* 12-min read
* Updated on Jan 22, 2026

This topic explains how to run OneAgent as a Docker container for full-stack injection. Follow this approach if you're using the Docker runtime without an orchestration platform.

## Supported versions

OneAgent deployment via Docker container is supported for Docker Engine versions 1.10 - 1.13.1, 17.03+ CE and EE and is available only for Linux-based hosts. Installation within the container isn't supported. For more information, see the [limitations of this deployment model](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container.").

## Requirements

* Create a [PaaS Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Your Docker environment must allow your OneAgent container to run in privileged mode.
* The `/opt` directory must exist on the host where you deploy your OneAgent container.

Starting from the image version 1.11.1000, OneAgent Docker image no longer ships with the OneAgent installer contained within it. Instead the installer is downloaded from your environment during the image startup process. The image is forward-compatible with new OneAgent versions and there's no specific link between the OneAgent version and the image version. The only dependency that exists is a requirement for a minimum supported OneAgent version for a given image version. For details, see the table below:

| **Image version** | **Minimum required OneAgent version** |
| --- | --- |
| 1.11.1000 - 1.12.1000 | 1.119 |
| 1.13.1000 - 1.21.1000 | 1.139 |
| >= 1.22.1000 | 1.157 |

## Locate your OneAgent installer URL

The first step is to obtain the location for `ONEAGENT_INSTALLER_SCRIPT_URL`. This information is presented to you during OneAgent installation.

To get your `ONEAGENT_INSTALLER_SCRIPT_URL`

1. Go to **Deploy Dynatrace**.
2. Select **Start installation** > **Linux**.

3. Determine the installer script URL and token from the UI-provided `wget` command:

OneAgent container image version 1.39.1000+

OneAgent container image version 1.38.1000 and earlier

This is the URL:

![OneAgent URL](https://dt-cdn.net/images/oneagent-url-570-2bbd3eb216.png)

OneAgent URL

This is the token:

![OneAgent token](https://dt-cdn.net/images/oneagent-token-569-399d827827.png)

OneAgent token

Replace the value of `arch` parameter with `<arch>`. Ignore the `flavor=default` parameter.

Your URL should look like this:
`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=<arch>`

This is your `ONEAGENT_INSTALLER_SCRIPT_URL`.

This your URL and API token.

![OneAgent installation page with URL to be modified](https://dt-cdn.net/images/oneagent-linux-install-url-734-22e9ac9a69.png)

OneAgent installation page with URL to be modified

Append the API token to the URL using the `API-Token` parameter. Your URL should look like this:

`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<token>`

This is your `ONEAGENT_INSTALLER_SCRIPT_URL`.

## Run OneAgent as a Docker container

To run OneAgent as a Docker container, you have two options.

Without AppArmor

With AppArmor

Execute the following `docker run` command on all your Docker hosts, making sure that you pass the URL and token you determined earlier as the values of `ONEAGENT_INSTALLER_SCRIPT_URL` and `ONEAGENT_INSTALLER_DOWNLOAD_TOKEN` environment variables.

OneAgent container image version 1.88.1000 (1.289) and higher

OneAgent container image version lower than 1.88.1000 (1.289)

```
docker run -d



--restart=on-failure:5



--read-only=true



--pid=host



--net=host



--cap-drop ALL



--cap-add CHOWN



--cap-add DAC_OVERRIDE



--cap-add DAC_READ_SEARCH



--cap-add FOWNER



--cap-add FSETID



--cap-add KILL



--cap-add NET_ADMIN



--cap-add NET_RAW



--cap-add SETFCAP



--cap-add SETGID



--cap-add SETUID



--cap-add SYS_ADMIN



--cap-add SYS_CHROOT



--cap-add SYS_PTRACE



--cap-add SYS_RESOURCE



--security-opt apparmor:unconfined



-v /:/mnt/root



-v <volume name>:/mnt/volume_storage_mount



-e ONEAGENT_ENABLE_VOLUME_STORAGE=true



-e ONEAGENT_INSTALLER_SCRIPT_URL=<REPLACE_WITH_YOUR_URL>



-e ONEAGENT_INSTALLER_DOWNLOAD_TOKEN=<Api-Token>



dynatrace/oneagent <INSTALLER_PARAMETERS>
```

```
docker run -d



--restart=on-failure:5



--pid=host



--net=host



--cap-drop ALL



--cap-add CHOWN



--cap-add DAC_OVERRIDE



--cap-add DAC_READ_SEARCH



--cap-add FOWNER



--cap-add FSETID



--cap-add KILL



--cap-add NET_ADMIN



--cap-add NET_RAW



--cap-add SETFCAP



--cap-add SETGID



--cap-add SETUID



--cap-add SYS_ADMIN



--cap-add SYS_CHROOT



--cap-add SYS_PTRACE



--cap-add SYS_RESOURCE



--security-opt apparmor:unconfined



-v /:/mnt/root



-e ONEAGENT_INSTALLER_SCRIPT_URL=<REPLACE_WITH_YOUR_URL>



-e ONEAGENT_INSTALLER_DOWNLOAD_TOKEN=<Api-Token>



dynatrace/oneagent <INSTALLER_PARAMETERS>
```

1. Go to `/etc/apparmor.d` and create `oneagent` file with the following content:

OneAgent container image version 1.88.1000 (1.289) and higher

OneAgent container image version lower than 1.88.1000 (1.289)

```
#include <tunables/global>



@{INITIAL_HOST_ROOT}=/mnt/root



@{VOLUME_MOUNT}=/mnt/volume_storage_mount



@{DOCKER_VOLUME_PATH}=/mnt/root/var/lib/docker/volumes/dynatrace_oneagent_storage/_data



@{HOST_ROOT}={/mnt/host_root,@{VOLUME_MOUNT}/host_root,@{DOCKER_VOLUME_PATH}/host_root}



@{INSTALL_PATH}=/opt/dynatrace/oneagent



@{CONFIG_PATH}=/var/lib/dynatrace/oneagent



@{LOG_PATH}=/var/log/dynatrace/oneagent



@{ENRICHMENT_PATH}=/var/lib/dynatrace/enrichment



@{CONTAINER_INIT_LOG_DIR}=/tmp/container_init



profile oneagent flags=(attach_disconnected,mediate_deleted) {



#include <abstractions/base>



#include <abstractions/dbus>



network,



file,



capability chown,



capability dac_override,



capability dac_read_search,



capability fowner,



capability fsetid,



capability kill,



capability net_admin,



capability net_raw,



capability setfcap,



capability setgid,



capability setuid,



capability sys_admin,



capability sys_chroot,



capability sys_ptrace,



capability sys_resource,



# Allow mounting volume paths to host root



mount options=(rw, bind) @{DOCKER_VOLUME_PATH}/ -> @{VOLUME_MOUNT}/,



mount options=(rw, rbind) @{VOLUME_MOUNT}/opt/ -> @{HOST_ROOT}@{INSTALL_PATH}/,



mount options=(rslave) -> @{HOST_ROOT}@{INSTALL_PATH}/,



mount options=(rw, rbind) @{VOLUME_MOUNT}/var/ -> @{HOST_ROOT}@{CONFIG_PATH}/,



mount options=(rslave) -> @{HOST_ROOT}@{CONFIG_PATH}/,



mount options=(rw, rbind) @{VOLUME_MOUNT}/var_log/ -> @{HOST_ROOT}@{LOG_PATH}/,



mount options=(rslave) -> @{HOST_ROOT}@{LOG_PATH}/,



mount options=(rw, rbind) @{VOLUME_MOUNT}/var_enrichment/ -> @{HOST_ROOT}@{ENRICHMENT_PATH}/,



mount options=(rslave) -> @{HOST_ROOT}@{ENRICHMENT_PATH}/,



mount options=(rw, bind) {@{VOLUME_MOUNT}/var_lib_helper/,/var_lib_helper/} -> @{HOST_ROOT}/var/lib/,



mount options=(rw, bind) {@{VOLUME_MOUNT}/var_log_helper/,/var_log_helper/} -> @{HOST_ROOT}/var/log/,



# Allow remounting host root to the new location



mount options=(rw, rbind) @{INITIAL_HOST_ROOT}/**/ -> @{HOST_ROOT}/*/,



mount options=(rw, bind) @{INITIAL_HOST_ROOT}/* -> @{HOST_ROOT}/*,



mount options=(rw, bind) @{INITIAL_HOST_ROOT}/**/* -> @{HOST_ROOT}/*,



mount options=(rslave) -> @{HOST_ROOT}/*/,



mount options=(rw, rbind) @{INITIAL_HOST_ROOT}/**/ -> @{HOST_ROOT}/opt/*/,



mount options=(rw, bind) @{INITIAL_HOST_ROOT}/**/* -> @{HOST_ROOT}/opt/*,



mount options=(rslave) -> @{HOST_ROOT}/opt/*/,



mount options=(rw, rbind) @{INITIAL_HOST_ROOT}/**/ -> @{HOST_ROOT}/var/lib/*/,



mount options=(rw, bind) @{INITIAL_HOST_ROOT}/**/* -> @{HOST_ROOT}/var/lib/*,



mount options=(rslave) -> @{HOST_ROOT}/var/lib/*/,



mount options=(rw, rbind) @{INITIAL_HOST_ROOT}/**/ -> @{HOST_ROOT}/var/log/*/,



mount options=(rw, bind) @{INITIAL_HOST_ROOT}/**/* -> @{HOST_ROOT}/var/log/*,



mount options=(rslave) -> @{HOST_ROOT}/var/log/*/,



mount options=(rw, rbind) @{INITIAL_HOST_ROOT}/sys/fs/cgroup/ -> @{HOST_ROOT}/sys/fs/cgroup/,



mount options=(rw, rbind) /sys/fs/cgroup -> @{HOST_ROOT}/sys/fs/cgroup/,



mount options=(rw) fstype=(proc) proc -> @{HOST_ROOT}/proc/,



mount options=(rw) fstype=(sysfs) sys -> @{HOST_ROOT}/sys/,



mount options=(rw) fstype=(securityfs) securityfs -> @{HOST_ROOT}/sys/kernel/security/,



mount options=(rw) fstype=(selinuxfs) selinuxfs -> @{HOST_ROOT}/sys/fs/selinux/,



mount options=(rw) fstype=(debugfs) debugfs -> @{HOST_ROOT}/sys/kernel/debug/,



umount @{INITIAL_HOST_ROOT}/,



# Allow mounting/unmounting tmpfs for initial logs



mount fstype=(tmpfs) tmpfs -> @{CONTAINER_INIT_LOG_DIR}/,



umount @{CONTAINER_INIT_LOG_DIR}/,



# Allow unmounting problematic mounts



umount @{HOST_ROOT}/var/lib/docker/aufs/,



umount @{HOST_ROOT}/var/lib/docker/devicemapper/,



umount @{HOST_ROOT}/var/lib/kubelet/plugins/kubernetes.io/csi/pv/pvc-*/globalmount/,



umount @{HOST_ROOT}/var/lib/kubelet/pods/*/volumes/kubernetes.io~{downward-api,empty-dir,csi,secret}/**,



umount @{HOST_ROOT}/var/lib/kubelet/pods/*/volume-subpaths/**,



umount @{HOST_ROOT}/run/netns/**,



umount @{HOST_ROOT}/run/containerd/io.containerd.grpc.v1.cri/sandboxes/**,



# Allow moving log agent service account mount point



mount options=(rw, move) {/run,/var/run}/secrets/kubernetes.io/serviceaccount/ -> @{HOST_ROOT}@{CONFIG_PATH}/agent/secrets/kubernetes.io/serviceaccount/,



# Allow moving log agent service account mount point



mount options=(rw, move) {/run,/var/run}/secrets/kubernetes.io/serviceaccount/ -> @{HOST_ROOT}@{CONFIG_PATH}/agent/secrets/kubernetes.io/serviceaccount/,



# Host (privileged) processes may send signals to container processes.



signal (receive) peer=unconfined,



# Container processes may send signals to injection process.



signal (send) peer=@{profile_name}//injection,



deny @{PROC}/* w,



deny @{PROC}/{[^1-9],[^1-9][^0-9],[^1-9s][^0-9y][^0-9s],[^1-9][^0-9][^0-9][^0-9/]*}/** w,



deny @{PROC}/sys/[^k]** w,



deny @{PROC}/sys/kernel/{?,??,[^s][^h][^m]**} w,



deny @{PROC}/sysrq-trigger rwklx,



deny @{PROC}/kcore rwklx,



deny /sys/[^f]*/** wklx,



deny /sys/f[^s]*/** wklx,



deny /sys/fs/[^c]*/** wklx,



deny /sys/fs/c[^g]*/** wklx,



deny /sys/fs/cg[^r]*/** wklx,



deny /sys/firmware/** rwklx,



deny /sys/kernel/security/** rwklx,



ptrace,



@{HOST_ROOT}@{INSTALL_PATH}/agent/lib64/oneagenthelper Cx -> injection,



profile injection flags=(attach_disconnected,mediate_deleted,chroot_relative) {



#include <abstractions/base>



#include <abstractions/dbus>



network,



file,



capability dac_override,



capability fowner,



capability fsetid,



capability sys_admin,



capability sys_chroot,



capability sys_ptrace,



# Allow mounting paths needed for container injection



mount options=(rw, rbind) @{INSTALL_PATH}/ -> /**/,



mount options=(rw, rbind) @{CONFIG_PATH}/agent/ -> /**/,



mount options=(rw, rbind) @{CONFIG_PATH}/datastorage/ -> /**/,



mount options=(rw, rbind) @{CONFIG_PATH}/agent/config/container.conf* -> /**,



mount options=(rw, rbind) @{CONFIG_PATH}/agent/runtime/.container.conf* -> /**,



mount options=(rw, rbind) @{CONFIG_PATH}/agent/config/ld.so.preload* -> /**,



mount options=(rw, rbind) @{CONFIG_PATH}/agent/runtime/.ld.so.preload* -> /**,



mount options=(rw, rbind) @{LOG_PATH}/ -> /**/,



mount options=(rw, rbind) @{ENRICHMENT_PATH}/ -> /**/,



mount options=(slave) -> /**,



mount options=(ro, remount, bind) -> /**,



# injection process may receive signals from parent process.



signal (receive) peer=oneagent,



ptrace,



}



}
```

```
#include <tunables/global>



@{INITIAL_HOST_ROOT}=/mnt/root



@{HOST_ROOT}=/mnt/host_root



@{DOCKER_VOLUME_PATH}=/mnt/root/var/lib/docker/volumes/dynatrace_oneagent_storage/_data



@{VOLUME_MOUNT}=/mnt/volume_storage_mount



@{INSTALL_PATH}=/opt/dynatrace/oneagent



@{CONFIG_PATH}=/var/lib/dynatrace/oneagent



@{LOG_PATH}=/var/log/dynatrace/oneagent



@{ENRICHMENT_PATH}=/var/lib/dynatrace/enrichment



profile oneagent flags=(attach_disconnected,mediate_deleted) {



#include <abstractions/base>



#include <abstractions/dbus>



network,



file,



capability chown,



capability dac_override,



capability dac_read_search,



capability fowner,



capability fsetid,



capability kill,



capability net_admin,



capability net_raw,



capability setfcap,



capability setgid,



capability setuid,



capability sys_admin,



capability sys_chroot,



capability sys_ptrace,



capability sys_resource,



# Allow mounting volume paths to host root



mount options=(rw, rbind) {@{VOLUME_MOUNT},@{DOCKER_VOLUME_PATH}}/opt/ -> @{HOST_ROOT}@{INSTALL_PATH}/,



mount options=(rslave) -> @{HOST_ROOT}@{INSTALL_PATH}/,



mount options=(rw, rbind) {@{VOLUME_MOUNT},@{DOCKER_VOLUME_PATH}}/var/ -> @{HOST_ROOT}@{CONFIG_PATH}/,



mount options=(rslave) -> @{HOST_ROOT}@{CONFIG_PATH}/,



mount options=(rw, rbind) {@{VOLUME_MOUNT},@{DOCKER_VOLUME_PATH}}/var_log/ -> @{HOST_ROOT}@{LOG_PATH}/,



mount options=(rslave) -> @{HOST_ROOT}@{LOG_PATH}/,



mount options=(rw, rbind) {@{VOLUME_MOUNT},@{DOCKER_VOLUME_PATH}}/var_enrichment/ -> @{HOST_ROOT}@{ENRICHMENT_PATH}/,



mount options=(rslave) -> @{HOST_ROOT}@{ENRICHMENT_PATH}/,



mount options=(rw, bind) /var_lib_helper/ -> @{HOST_ROOT}/var/lib/,



mount options=(rw, bind) /var_log_helper/ -> @{HOST_ROOT}/var/log/,



# Allow remounting host root to the new location



mount options=(rw, rbind) @{INITIAL_HOST_ROOT}/**/ -> @{HOST_ROOT}/*/,



mount options=(rw, bind) @{INITIAL_HOST_ROOT}/* -> @{HOST_ROOT}/*,



mount options=(rw, bind) @{INITIAL_HOST_ROOT}/**/* -> @{HOST_ROOT}/*,



mount options=(rslave) -> @{HOST_ROOT}/*/,



mount options=(rw, rbind) @{INITIAL_HOST_ROOT}/**/ -> @{HOST_ROOT}/opt/*/,



mount options=(rw, bind) @{INITIAL_HOST_ROOT}/**/* -> @{HOST_ROOT}/opt/*,



mount options=(rslave) -> @{HOST_ROOT}/opt/*/,



mount options=(rw, rbind) @{INITIAL_HOST_ROOT}/**/ -> @{HOST_ROOT}/var/lib/*/,



mount options=(rw, bind) @{INITIAL_HOST_ROOT}/**/* -> @{HOST_ROOT}/var/lib/*,



mount options=(rslave) -> @{HOST_ROOT}/var/lib/*/,



mount options=(rw, rbind) @{INITIAL_HOST_ROOT}/**/ -> @{HOST_ROOT}/var/log/*/,



mount options=(rw, bind) @{INITIAL_HOST_ROOT}/**/* -> @{HOST_ROOT}/var/log/*,



mount options=(rslave) -> @{HOST_ROOT}/var/log/*/,



mount options=(rw, rbind) @{INITIAL_HOST_ROOT}/sys/fs/cgroup/ -> @{HOST_ROOT}/sys/fs/cgroup/,



mount options=(rw, rbind) /sys/fs/cgroup -> @{HOST_ROOT}/sys/fs/cgroup/,



mount options=(rw) fstype=(proc) proc -> @{HOST_ROOT}/proc/,



mount options=(rw) fstype=(sysfs) sys -> @{HOST_ROOT}/sys/,



mount options=(rw) fstype=(securityfs) securityfs -> @{HOST_ROOT}/sys/kernel/security/,



mount options=(rw) fstype=(selinuxfs) selinuxfs -> @{HOST_ROOT}/sys/fs/selinux/,



mount options=(rw) fstype=(debugfs) debugfs -> @{HOST_ROOT}/sys/kernel/debug/,



umount @{INITIAL_HOST_ROOT}/,



# Allow unmounting problematic mounts



umount @{HOST_ROOT}/var/lib/docker/aufs/,



umount @{HOST_ROOT}/var/lib/docker/devicemapper/,



umount @{HOST_ROOT}/var/lib/kubelet/plugins/kubernetes.io/csi/pv/pvc-*/globalmount/,



umount @{HOST_ROOT}/var/lib/kubelet/pods/*/volumes/kubernetes.io~{downward-api,empty-dir,csi,secret}/**,



umount @{HOST_ROOT}/var/lib/kubelet/pods/*/volume-subpaths/**,



umount @{HOST_ROOT}/run/netns/**,



umount @{HOST_ROOT}/run/containerd/io.containerd.grpc.v1.cri/sandboxes/**,



# Host (privileged) processes may send signals to container processes.



signal (receive) peer=unconfined,



# Container processes may send signals amongst themselves.



signal (send,receive) peer=@{profile_name},



deny @{PROC}/* w,



deny @{PROC}/{[^1-9],[^1-9][^0-9],[^1-9s][^0-9y][^0-9s],[^1-9][^0-9][^0-9][^0-9/]*}/** w,



deny @{PROC}/sys/[^k]** w,



deny @{PROC}/sys/kernel/{?,??,[^s][^h][^m]**} w,



deny @{PROC}/sysrq-trigger rwklx,



deny @{PROC}/kcore rwklx,



deny /sys/[^f]*/** wklx,



deny /sys/f[^s]*/** wklx,



deny /sys/fs/[^c]*/** wklx,



deny /sys/fs/c[^g]*/** wklx,



deny /sys/fs/cg[^r]*/** wklx,



deny /sys/firmware/** rwklx,



deny /sys/kernel/security/** rwklx,



ptrace,



@{HOST_ROOT}@{INSTALL_PATH}/agent/lib64/oneagenthelper Cx,



profile @{HOST_ROOT}@{INSTALL_PATH}/agent/lib64/oneagenthelper flags=(attach_disconnected,mediate_deleted,chroot_relative) {



#include <abstractions/base>



#include <abstractions/dbus>



network,



file,



capability dac_override,



capability fowner,



capability fsetid,



capability sys_admin,



capability sys_chroot,



capability sys_ptrace,



# Allow mounting paths needed for container injection



mount options=(rw, rbind) @{INSTALL_PATH}/ -> /**/,



mount options=(rw, rbind) @{CONFIG_PATH}/agent/ -> /**/,



mount options=(rw, rbind) @{CONFIG_PATH}/datastorage/ -> /**/,



mount options=(rw, rbind) @{CONFIG_PATH}/agent/config/container.conf* -> /**,



mount options=(rw, rbind) @{CONFIG_PATH}/agent/runtime/.container.conf* -> /**,



mount options=(rw, rbind) @{CONFIG_PATH}/agent/config/ld.so.preload* -> /**,



mount options=(rw, rbind) @{CONFIG_PATH}/agent/runtime/.ld.so.preload* -> /**,



mount options=(rw, rbind) @{LOG_PATH}/ -> /**/,



mount options=(rw, rbind) @{ENRICHMENT_PATH}/ -> /**/,



mount options=(slave) -> /**,



mount options=(ro, remount, bind) -> /**,



ptrace,



}



}
```

2. Run the following command to load the AppArmor profile:

```
apparmor_parser -r /etc/apparmor.d/oneagent
```

3. Execute the following `docker run` command on all your Docker hosts, making sure that you pass the URL and token you determined earlier as the values of `ONEAGENT_INSTALLER_SCRIPT_URL` and `ONEAGENT_INSTALLER_DOWNLOAD_TOKEN` environment variables.

OneAgent container image version 1.88.1000 (1.289) and higher

OneAgent container image version lower than 1.88.1000 (1.289)

```
docker run -d



--restart=on-failure:5



--read-only=true



--pid=host



--net=host



--cap-drop ALL



--cap-add CHOWN



--cap-add DAC_OVERRIDE



--cap-add DAC_READ_SEARCH



--cap-add FOWNER



--cap-add FSETID



--cap-add KILL



--cap-add NET_ADMIN



--cap-add NET_RAW



--cap-add SETFCAP



--cap-add SETGID



--cap-add SETUID



--cap-add SYS_ADMIN



--cap-add SYS_CHROOT



--cap-add SYS_PTRACE



--cap-add SYS_RESOURCE



--security-opt apparmor:oneagent



-v /:/mnt/root



-v <volume name>:/mnt/volume_storage_mount



-e ONEAGENT_ENABLE_VOLUME_STORAGE=true



-e ONEAGENT_INSTALLER_SCRIPT_URL=<REPLACE_WITH_YOUR_URL>



-e ONEAGENT_INSTALLER_DOWNLOAD_TOKEN=<Api-Token>



dynatrace/oneagent <INSTALLER_PARAMETERS>
```

```
docker run -d



--restart=on-failure:5



--pid=host



--net=host



--cap-drop ALL



--cap-add CHOWN



--cap-add DAC_OVERRIDE



--cap-add DAC_READ_SEARCH



--cap-add FOWNER



--cap-add FSETID



--cap-add KILL



--cap-add NET_ADMIN



--cap-add NET_RAW



--cap-add SETFCAP



--cap-add SETGID



--cap-add SETUID



--cap-add SYS_ADMIN



--cap-add SYS_CHROOT



--cap-add SYS_PTRACE



--cap-add SYS_RESOURCE



--security-opt apparmor:oneagent



-v /:/mnt/root



-e ONEAGENT_INSTALLER_SCRIPT_URL=<REPLACE_WITH_YOUR_URL>



-e ONEAGENT_INSTALLER_DOWNLOAD_TOKEN=<Api-Token>



dynatrace/oneagent <INSTALLER_PARAMETERS>
```

For OneAgent container image versions earlier than 1.69.1000, if you get an error such as `Container was not launched in host's cgroup namespace` after running this command, add `--cgroupns=host` to the parameters and rerun it.

Once the container is started, a regular OneAgent full-stack installer is executed and OneAgent files are deployed to the underlying file system of the machine running the container. The installation package and associated shell script are downloaded from your environment upon container startup, using the URL provided for launching the container. The signature of the installer is verified automatically following the download. After you successfully started the container, the status will be marked as `healthy`.

```
$ docker ps



CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS                   PORTS     NAMES



e3e1e513f0ff   dynatrace/oneagent   "/bin/bash /tmp/entrâ¦"   2 minutes ago   Up 2 minutes (healthy)             stupefied_elgamal
```

## Deploy OneAgent via a container orchestration tool

If you use a container orchestration tool, your orchestrator can deploy the OneAgent container for you. The example snippets below show you how to take advantage of orchestration tools in deploying OneAgent to all your nodes.

* [Run OneAgent with Mesos/Marathon](/managed/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon "Learn how to deploy OneAgent on Mesos/Marathon.")
* [Run OneAgent with Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")
* [Run OneAgent with Elastic Container Service](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs/deploy-oneagent-on-ecs "Monitor ECS clusters as a daemon service, with the EC2 launch type.")
* [Set up Dynatrace on Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")

## Custom installation with command-line parameters

You can alternatively perform a [custom installation with command-line parameters](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").

## Privileges

For more information on privileges required by OneAgent deployed as a Docker container, see [OneAgent privileges for container monitoring](/managed/ingest-from/setup-on-container-platforms/oneagent-privileges "Learn the privileges required by OneAgent in each deployment model").

## Limitations

* OneAgent only has access to the disks that are mounted within the container that it runs in. Therefore OneAgent can only report metrics for these container disks and not the disks of underlying hosts. This is caused by the context in which OneAgent executes its commands for gathering data.
* Deep monitoring for native (i.e., non-containerized) processes on hosts is disabled. The injection file `ld.so.preload` on the host file system isn't modified, and therefore the automatic injection into processes running outside of containers isn't possible.
* Because of this, the JMX extension can only work with the processes that run inside containers. The JMX extension is tightly coupled with deep monitoring of Java processes.
* Capturing of application crashes and core dumps via `oneagentdumpproc` isn't supported.
* OneAgent isn't registered in the system's autostart. Lifetime and startup of the container with OneAgent processes is managed by Docker.
* All [command-line parameters of the installer](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.") are supported, with the exception of `INSTALL_PATH`, `LOG_PATH`, and `DATA_STORAGE`.
* There's a startup dependency between the container in which OneAgent is deployed and application containers to be instrumented (i.e., which have deep process monitoring enabled). The OneAgent container must be started and the `oneagenthelper` process must be running prior to the application container being launched so that the application can be properly instrumented.

## Update OneAgent on Docker containers

To update OneAgent on Docker containers follow the instructions that correspond to how you've installed OneAgent.

* If you've installed on Linux, follow the [instructions for updating OneAgent on Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux.").
* If you've installed on Windows, follow the [instructions for updating OneAgent on Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Learn about the different ways to update Dynatrace OneAgent on Windows.").
* If you've deployed OneAgent as a Docker container, restart the container using the following command

  `$ docker restart oneagent`

  provided that you've added the parameter `--name=oneagent` in the [appropriate Docker run command](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#run-oneagent-as-a-docker-container "Install and update Dynatrace OneAgent as a Docker container."). The OneAgent Docker image will automatically fetch the latest version of OneAgent.

  If you've specified a default OneAgent install version for new hosts and applications in your [OneAgent updates settings](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), the OneAgent Docker image will automatically fetch the defined default version of OneAgent.

  OneAgent auto-update isn't supported when OneAgent has been deployed as a Docker image.

## Related topics

* [Set up Dynatrace on Docker](/managed/ingest-from/setup-on-container-platforms/docker "Deploy OneAgent on Docker.")
* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")