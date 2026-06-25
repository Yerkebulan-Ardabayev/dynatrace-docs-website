---
title: Ротация токенов
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/token-rotation
scraped: 2026-05-12T12:14:24.881177
---

# Ротация токенов

# Ротация токенов

* Опубликовано 3 ноября 2025 г.

Окружения Dynatrace предоставляют [API](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Ротация токенов тенанта Dynatrace."), который обеспечивает ротацию токенов тенанта. При запуске этот API создаёт новые токены для OneAgent и ActiveGate.

После ротации токена тенанта:

* Dynatrace Operator автоматически обнаруживает и применяет новый токен.
* Экземпляры ActiveGate автоматически перезапускаются.
* Экземпляры OneAgent автоматически перезапускаются.
* Поды Log Monitoring автоматически перезапускаются.

Кодовые модули не перезапускаются автоматически. Внедрённые поды приложений необходимо перезапустить вручную.

## Токены связи, управляемые Operator

Dynatrace Operator создаёт токены связи и управляет ими, обеспечивая безопасную связь между компонентами Dynatrace:

* Токен ActiveGate-Node Collection Controller
* Токен ActiveGate-Extension Execution Controller
* Токен EEC-Dynatrace Collector

## Ручная ротация токенов, управляемых Operator

Если вам нужно выполнить ротацию любого из токенов связи, управляемых Operator, следуйте приведённым ниже инструкциям.

1. Удалите существующие секреты.

   ```
   kubectl delete secret <dynakube>-kspm-token -n dynatrace



   kubectl delete secret <dynakube>-extension-token -n dynatrace



   kubectl delete secret <dynakube>-activegate-auth-token-secret -n dynatrace
   ```
2. После удаления секрета Dynatrace Operator автоматически создаёт новый токен и пересоздаёт секрет.

   Проверить пересоздание секрета можно с помощью:

   ```
   kubectl get secrets -n dynatrace
   ```
3. Перезапустите компоненты, которые используют токен.

   ```
   kubectl rollout restart statefulset <dynakube>-activegate -n dynatrace



   kubectl rollout restart statefulset <dynakube>-extension-controller -n dynatrace



   kubectl rollout restart statefulset <dynakube>-otel-collector -n dynatrace



   kubectl rollout restart daemonset <dynakube>-node-config-collector -n dynatrace
   ```