---
title: Применение Pod Security Standards
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/pod-security-standards
scraped: 2026-05-12T12:14:26.783657
---

# Применение Pod Security Standards

# Применение Pod Security Standards

* Чтение: 3 мин
* Обновлено 16 января 2024 г.

Kubernetes версии 1.25+

Можно задавать уровни изоляции подов на основе пространств имён с помощью [Pod Security Standards](https://dt-url.net/mp0345l), применяемые встроенным [контроллером допуска Pod Security](https://dt-url.net/19238ro). Эти стандарты задают перечень элементов управления, таких как возможности (capabilities), профили seccomp и типы томов.

Хотя контроллер допуска Pod Security является встроенной функцией Kubernetes, он не обязательно включён по умолчанию во всех дистрибутивах Kubernetes. Кроме того, для окружений, где требуются усиленные или иные политики безопасности, можно использовать сторонние альтернативы, такие как Open Policy Agent (OPA). Дополнительную информацию об использовании сторонних инструментов для применения стандартов безопасности подов см. в [применении стандартов безопасности подов со сторонними альтернативами](https://dt-url.net/ix038h9).

## Pod Security Standards

Pod Security Standards определяют три политики:

* [Privileged](https://dt-url.net/mv038z4): неограниченная политика.
* [Baseline](https://dt-url.net/4p238n8): минимально ограничивающая политика.
* [Restricted](https://dt-url.net/ut4387d): сильно ограничивающая политика.

Pod Security Standards являются встроенной функцией Kubernetes, и их нельзя расширить или настроить.

## Настройка безопасности подов для пространства имён

Стандарты безопасности подов применяются на уровне пространства имён при создании подов. Если применяемый по умолчанию профиль, заданный встроенным контроллером допуска, отличается от `privileged` (например, `baseline` или `restricted`), на [уровне встроенного контроллера допуска](https://dt-url.net/yo4383i) для вашего пространства имён необходимо настроить привилегированный профиль `privileged`. Dynatrace Operator поддерживает только привилегированную политику `privileged`, так как подам CSI driver и OneAgent требуется больше разрешений, чем допускают политики `baseline` или `restricted`.

Выполните следующую команду, чтобы задать для пространства имён `dynatrace` значение `privileged`:

```
kubectl label namespace dynatrace pod-security.kubernetes.io/enforce=privileged pod-security.kubernetes.io/audit=privileged pod-security.kubernetes.io/warn=privileged
```

### Режимы аудита и предупреждений

[Режимы аудита и предупреждений](https://dt-url.net/6l037ti) применяются к deployment, DaemonSet или другим ресурсам рабочих нагрузок для выявления нарушений, даже если под ещё не был создан.

## Устранение неполадок

Чтобы понять, почему поды OneAgent могут не создаваться при ограничивающей политике, используйте следующую команду.

```
kubectl -n dynatrace describe daemonset.apps/<dynakube>-oneagent
```

Следующий вывод событий показывает нарушение стандарта безопасности подов, препятствующее созданию пода. Именно на такой вывод следует обращать внимание при диагностике проблем развёртывания.

```
> Events:



>



> Type | Reason | Age| From| Message



> ---- |--------|---- |----|-------



> Warning|FailedCreate|15s|daemonset-controller|Error creating: pods "dynakube-oneagent-kp6sf" is forbidden: violates PodSecurity "restricted:latest": forbidden AppArmor profile (container.apparmor.security.beta.kubernetes.io/dynatrace-oneagent="unconfined"), host namespaces (hostNetwork=true, hostPID=true), allowPrivilegeEscalation != false (container "dynatrace-oneagent" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (container "dynatrace-oneagent" must not include "CHOWN", "DAC_OVERRIDE", "DAC_READ_SEARCH", "FOWNER", "FSETID", "KILL", "NET_ADMIN", "NET_RAW", "SETFCAP", "SETGID", "SETUID", "SYS_ADMIN", "SYS_CHROOT", "SYS_PTRACE", "SYS_RESOURCE" in securityContext.capabilities.add), restricted volume types (volume "host-root" uses restricted volume type "hostPath"), seccompProfile (pod or container "dynatrace-oneagent" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
```

Аналогично, чтобы проверить, почему поды CSI driver могут давать сбой при тех же условиях, используйте следующую команду.

```
kubectl -n dynatrace describe daemonset.apps/dynatrace-oneagent-csi-driver
```

```
> Events:



>



> Type| Reason | Age| From| Message



> ---- |--------|---- |----| -------



> Warning|FailedCreate|25m|daemonset-controller|Error creating: pods "dynatrace-oneagent-csi-driver-nh7p9" is forbidden: violates PodSecurity "restricted:latest": privileged (containers "server", "provisioner" must not set securityContext.privileged=true), allowPrivilegeEscalation != false (containers "server", "provisioner", "registrar" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (containers "csi-init", "server", "provisioner", "registrar", "liveness-probe" must set securityContext.capabilities.drop=["ALL"]), restricted volume types (volumes "registration-dir", "plugin-dir", "data-dir", "mountpoint-dir" use restricted volume type "hostPath"), runAsNonRoot != true (containers "csi-init", "server", "provisioner", "registrar", "liveness-probe" must not set securityContext.runAsNonRoot=false), runAsUser=0 (containers "csi-init", "server", "provisioner", "registrar", "liveness-probe" must not set runAsUser=0)
```