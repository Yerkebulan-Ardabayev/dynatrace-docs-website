# Безопасность Dynatrace Managed

Руководство по безопасности кластера.

## Аутентификация

### Локальные пользователи

Управление: **CMC → Settings → Users**

### LDAP/Active Directory

```yaml
ldap:
  url: ldaps://ldap.example.com:636
  base_dn: dc=example,dc=com
  user_filter: (sAMAccountName={0})
```

### SAML SSO

1. Настройте Identity Provider (Okta, Azure AD)
2. Импортируйте метаданные в CMC
3. Настройте маппинг групп

## Сетевая безопасность

### Firewall порты

| Порт | Назначение |
|------|------------|
| 443 | Web UI |
| 8443 | CMC |
| 9999 | Cluster communication |
| 9200 | Elasticsearch |
| 7000-7199 | Cassandra |

### TLS/SSL

```bash
# Установка сертификата
sudo /opt/dynatrace-managed/set-ssl.sh cert.pem key.pem
```

## Аудит

Логи аудита: `/var/opt/dynatrace-managed/log/audit/`

## Бест-практики

- ✅ Используйте сложные пароли
- ✅ Включите 2FA
- ✅ Ограничьте доступ к CMC
- ✅ Регулярно обновляйте
- ✅ Мониторьте логи аудита
