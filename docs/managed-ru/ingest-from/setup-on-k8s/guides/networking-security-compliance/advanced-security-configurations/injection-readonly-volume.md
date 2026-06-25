---
title: Настройка томов CSI только для чтения
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/advanced-security-configurations/injection-readonly-volume
scraped: 2026-05-12T12:04:35.978215
---

# Настройка томов CSI только для чтения

# Настройка томов CSI только для чтения

* Чтение: 1 мин
* Обновлено 20 ноября 2025 г.
* Устарело

Dynatrace Operator версии 0.12.0+ и <1.7.0

Это актуально только для версии Operator после 0.12.0 и до 1.7.0.

Начиная с версии Operator 1.7.0, все тома CSI, внедряемые Operator, доступны только для чтения.

### Предварительные требования Устарело

* CSI driver Dynatrace Operator, установленный в кластере Kubernetes.
* DynaKube, настроенный на использование CSI driver. Например, убедитесь, что `applicationMonitoring` включён с `useCSIDriver: true`.

  `cloudNativeFullStack` не поддерживается на [BottleRocket](https://dt-url.net/4c0365f).

### Включение флага функции Устарело

При использовании этого флага функции функция отказоустойчивости нашего CSI driver работать не будет. Используйте версию Operator 1.7+, если требуются отказоустойчивые тома CSI только для чтения.

* Функция отказоустойчивости CSI driver: если нашему CSI driver не удаётся успешно предоставить монтирование внедрённому контейнеру в течение нескольких минут, он отступит, чтобы приложение пользователя могло запуститься, но без мониторинга.

Чтобы включить внедрение томов CSI только для чтения, задайте для флага функции `feature.dynatrace.com/injection-readonly-volume` значение `true`. Когда флаг функции включён, внедряемый том CSI становится доступным только для чтения.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/injection-readonly-volume: "true"
```

Это позволяет использовать CSI driver даже на платформах [BottleRocket](https://dt-url.net/4c0365f), где OneAgent в режиме host monitoring не работает. Для поддержки этой функции добавляется дополнительное эфемерное хранилище, чтобы внедрённый OneAgent мог хранить логи и дополнительные конфигурации.

Недостаток этого подхода в том, что если ваши поды завершатся неожиданно или будут удалены иным образом, любые логи, хранящиеся в эфемерном хранилище, будут потеряны.