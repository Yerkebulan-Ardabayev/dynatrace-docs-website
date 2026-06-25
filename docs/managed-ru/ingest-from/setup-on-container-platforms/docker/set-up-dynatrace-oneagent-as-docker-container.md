---
title: Настройка Dynatrace OneAgent как Docker-контейнера
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container
scraped: 2026-05-12T11:11:04.917700
---

# Настройка Dynatrace OneAgent как Docker-контейнера

# Настройка Dynatrace OneAgent как Docker-контейнера

* 12-min read
* Updated on Jan 22, 2026

В этой статье описан запуск OneAgent как Docker-контейнера для full-stack injection. Используйте этот подход, если работаете с Docker runtime без платформы оркестрации.

## Поддерживаемые версии

Развёртывание OneAgent через Docker-контейнер поддерживается для Docker Engine версий 1.10 - 1.13.1, 17.03+ CE и EE и доступно только для Linux-хостов. Установка внутри контейнера не поддерживается. Подробнее об [ограничениях этой модели развёртывания](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как Docker-контейнера.").

## Требования

* Создайте [PaaS Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Концепция access token и его scopes.").
* Ваша Docker-среда должна разрешать контейнеру OneAgent работать в privileged-режиме.
* На хосте, где разворачивается контейнер OneAgent, должна существовать директория `/opt`.

Начиная с версии образа 1.11.1000, OneAgent Docker image больше не содержит установщик OneAgent внутри образа. Вместо этого установщик скачивается из вашего окружения при запуске образа. Образ forward-compatible с новыми версиями OneAgent: жёсткой связи между версией OneAgent и версией образа нет. Единственная зависимость — минимально поддерживаемая версия OneAgent для конкретной версии образа. Подробности в таблице ниже:

| **Версия образа** | **Минимально требуемая версия OneAgent** |
| --- | --- |
| 1.11.1000 - 1.12.1000 | 1.119 |
| 1.13.1000 - 1.21.1000 | 1.139 |
| >= 1.22.1000 | 1.157 |

## Определите URL установщика OneAgent

Первый шаг — получить значение для `ONEAGENT_INSTALLER_SCRIPT_URL`. Эта информация показывается при установке OneAgent.

Чтобы получить ваш `ONEAGENT_INSTALLER_SCRIPT_URL`:

1. Перейдите в **Deploy Dynatrace**.
2. Нажмите **Start installation** > **Linux**.

3. Определите URL установщика и токен из команды `wget`, предоставляемой в UI:

OneAgent container image версии 1.39.1000+

OneAgent container image версии 1.38.1000 и ранее

Это URL:

![OneAgent URL](https://dt-cdn.net/images/oneagent-url-570-2bbd3eb216.png)

OneAgent URL

Это токен:

![OneAgent token](https://dt-cdn.net/images/oneagent-token-569-399d827827.png)

OneAgent token

Замените значение параметра `arch` на `<arch>`. Параметр `flavor=default` игнорируйте.

Ваш URL должен выглядеть так:
`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=<arch>`

Это и есть ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

Вот ваш URL и API-токен.

![Страница установки OneAgent с URL для модификации](https://dt-cdn.net/images/oneagent-linux-install-url-734-22e9ac9a69.png)

Страница установки OneAgent с URL для модификации

Добавьте API-токен к URL через параметр `API-Token`. Ваш URL должен выглядеть так:

`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<token>`

Это и есть ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

## Запуск OneAgent как Docker-контейнера

Есть два варианта запуска OneAgent как Docker-контейнера.

Без AppArmor

С AppArmor

Выполните следующую команду `docker run` на всех Docker-хостах, передав в переменных окружения `ONEAGENT_INSTALLER_SCRIPT_URL` и `ONEAGENT_INSTALLER_DOWNLOAD_TOKEN` URL и токен, полученные ранее.

OneAgent container image версии 1.88.1000 (1.289) и выше

OneAgent container image версии ниже 1.88.1000 (1.289)

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

1. Перейдите в `/etc/apparmor.d` и создайте файл `oneagent` со следующим содержимым:

OneAgent container image версии 1.88.1000 (1.289) и выше

OneAgent container image версии ниже 1.88.1000 (1.289)

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

2. Выполните следующую команду, чтобы загрузить AppArmor-профиль:

```
apparmor_parser -r /etc/apparmor.d/oneagent
```

3. Выполните следующую команду `docker run` на всех Docker-хостах, передав в переменных окружения `ONEAGENT_INSTALLER_SCRIPT_URL` и `ONEAGENT_INSTALLER_DOWNLOAD_TOKEN` URL и токен, полученные ранее.

OneAgent container image версии 1.88.1000 (1.289) и выше

OneAgent container image версии ниже 1.88.1000 (1.289)

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

Для версий образа OneAgent container ранее 1.69.1000: если после выполнения этой команды появилась ошибка вроде `Container was not launched in host's cgroup namespace`, добавьте `--cgroupns=host` в параметры и запустите команду снова.

После запуска контейнера выполняется стандартный full-stack установщик OneAgent, и файлы OneAgent разворачиваются в файловую систему машины, на которой запущен контейнер. Установочный пакет и связанный shell-скрипт скачиваются из вашего окружения при старте контейнера по URL, указанному при запуске. Подпись установщика проверяется автоматически после скачивания. Когда контейнер успешно запущен, его статус будет помечен как `healthy`.

```
$ docker ps



CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS                   PORTS     NAMES



e3e1e513f0ff   dynatrace/oneagent   "/bin/bash /tmp/entr…"   2 minutes ago   Up 2 minutes (healthy)             stupefied_elgamal
```

## Развёртывание OneAgent через инструмент оркестрации контейнеров

Если вы используете инструмент оркестрации контейнеров, он может развернуть контейнер OneAgent за вас. Примеры ниже показывают, как использовать инструменты оркестрации для развёртывания OneAgent на всех узлах.

* [Запуск OneAgent с Mesos/Marathon](/managed/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon "Развёртывание OneAgent на Mesos/Marathon.")
* [Запуск OneAgent с Kubernetes](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace в Kubernetes")
* [Запуск OneAgent с Elastic Container Service](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs/deploy-oneagent-on-ecs "Мониторинг ECS-кластеров как daemon service с EC2 launch type.")
* [Настройка Dynatrace на Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Настройка Dynatrace на Cloud Foundry.")

## Кастомная установка с параметрами командной строки

Альтернативно можно выполнить [кастомную установку с параметрами командной строки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Использование Linux-установщика с параметрами командной строки.").

## Привилегии

Подробнее о привилегиях, нужных OneAgent при развёртывании как Docker-контейнера, смотрите [OneAgent privileges for container monitoring](/managed/ingest-from/setup-on-container-platforms/oneagent-privileges "Привилегии, нужные OneAgent в каждой модели развёртывания").

## Ограничения

* OneAgent имеет доступ только к дискам, смонтированным внутри контейнера, в котором он работает. Поэтому OneAgent может отчитываться по метрикам только этих дисков контейнера, а не дисков host-системы. Это связано с контекстом, в котором OneAgent выполняет команды сбора данных.
* Deep monitoring для нативных (не контейнеризованных) процессов на хостах отключён. Файл injection `ld.so.preload` в файловой системе хоста не изменяется, поэтому автоматический injection в процессы вне контейнеров невозможен.
* Из-за этого JMX extension может работать только с процессами внутри контейнеров. JMX extension тесно связано с deep monitoring Java-процессов.
* Перехват app crashes и core dumps через `oneagentdumpproc` не поддерживается.
* OneAgent не регистрируется в системном автозапуске. Жизненный цикл и старт контейнера с процессами OneAgent управляются Docker.
* Поддерживаются все [параметры командной строки установщика](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Использование Linux-установщика с параметрами командной строки."), кроме `INSTALL_PATH`, `LOG_PATH` и `DATA_STORAGE`.
* Существует зависимость по старту между контейнером, в котором развёрнут OneAgent, и контейнерами приложений, которые нужно инструментировать (то есть с включённым deep process monitoring). Контейнер OneAgent должен стартовать первым, и процесс `oneagenthelper` должен работать до запуска контейнера приложения, иначе приложение не получится правильно инструментировать.

## Обновление OneAgent в Docker-контейнерах

Чтобы обновить OneAgent в Docker-контейнерах, следуйте инструкции, соответствующей способу установки OneAgent.

* Если вы установили OneAgent на Linux, следуйте [инструкции по обновлению OneAgent на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Способы обновления OneAgent на Linux.").
* Если вы установили OneAgent на Windows, следуйте [инструкции по обновлению OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Способы обновления Dynatrace OneAgent на Windows.").
* Если вы развернули OneAgent как Docker-контейнер, перезапустите контейнер следующей командой

  `$ docker restart oneagent`

  при условии, что вы добавили параметр `--name=oneagent` в [соответствующую команду docker run](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#run-oneagent-as-a-docker-container "Установка и обновление Dynatrace OneAgent как Docker-контейнера."). OneAgent Docker image автоматически подтянет последнюю версию OneAgent.

  Если в [настройках обновления OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Способы обновления OneAgent на Linux.") вы указали версию OneAgent по умолчанию для новых хостов и приложений, OneAgent Docker image автоматически подтянет указанную версию OneAgent.

  Автообновление OneAgent не поддерживается, если OneAgent развёрнут как Docker image.

## Связанные темы