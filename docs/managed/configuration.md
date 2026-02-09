# Настройка Dynatrace Managed

Настройка Dynatrace Managed после установки.

## Основные настройки

### Сетевые настройки

1. Откройте Cluster Management Console (CMC)
2. Перейдите в **Settings → Network**
3. Настройте:
   - DNS серверы
   - Прокси (если требуется)
   - SSL сертификаты

### Настройка хранилища

| Тип данных | Срок хранения по умолчанию |
|------------|---------------------------|
| Метрики | 35 дней |
| Трассировки | 10 дней |
| Логи | 35 дней |
| Сессии | 35 дней |

## Интеграции

### Email уведомления

```yaml
smtp:
  host: smtp.example.com
  port: 587
  user: notifications@example.com
  ssl: true
```

### LDAP/Active Directory

1. Перейдите в **Settings → Authentication**
2. Выберите **LDAP**
3. Укажите:
   - LDAP URL
   - Base DN
   - Bind DN и пароль

## Следующие шаги

- [Мониторинг кластера](operations.md)
- [Обновления](update.md)
