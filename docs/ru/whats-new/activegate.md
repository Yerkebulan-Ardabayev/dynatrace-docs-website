---
title: Примечания к выпуску ActiveGate
---

# Примечания к выпуску ActiveGate

Выпускается каждый второй спринт. Развертывание занимает до 4 недель.

---

## Версия 1.327

**Развертывание:** 18 ноября 2025 | **Обновлено:** 28 января 2026

### Новое

- Улучшена производительность парсинга OpenMetrics для Kubernetes
- Автоматическое освобождение простаивающих соединений
- Ручная установка Chrome for Testing (Amazon Linux 2023, Ubuntu 24.04, Oracle Linux 9.5)
- Маскирование чувствительных данных Kubernetes (env, command, args) в YAML
- Метрики kube-state-metrics обогащены `k8s.cluster.uid`

### Исправления

- Исправлен прием данных для Kubernetes Enhanced Object Visibility Preview

---

## Версия 1.325

**Развертывание:** 21 октября 2025

### Новое

- `agctl create-support-archive --stdout` — потоковый вывод архива

### Важно

- **1.325 — последняя версия** Synthetic-enabled ActiveGate для Red Hat / Oracle Linux / Rocky Linux 8
- Synthetic 1.325+ требует Chromium 126+

---

## Поддержка

| Платформа | Стандартная | Корпоративная |
| --- | --- | --- |
| ActiveGate | 9 месяцев | 12 месяцев |

## Обновление

1. **Dynatrace -> Manage -> Deployment status -> ActiveGates**
2. Скачайте новую версию или используйте автообновление
3. Linux: установка с правами root; Windows: от администратора

Рекомендуется тестировать обновление перед production.
