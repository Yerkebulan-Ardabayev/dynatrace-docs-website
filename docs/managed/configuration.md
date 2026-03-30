# Настройка Dynatrace Managed

## Сетевые настройки

**CMC → Settings → Network**: DNS, прокси, SSL сертификаты.

## Хранилище

| Тип данных | Срок хранения |
|------------|---------------|
| Метрики | 35 дней |
| Трассировки | 10 дней |
| Логи | 35 дней |
| Сессии | 35 дней |

## Интеграции

### Email (SMTP)

```yaml
smtp:
  host: smtp.example.com
  port: 587
  user: notifications@example.com
  ssl: true
```

### LDAP/Active Directory

**Settings → Authentication → LDAP**: укажите LDAP URL, Base DN, Bind DN и пароль.

## Следующие шаги

- [Мониторинг кластера](operations.md)
- [Обновления](update.md)
