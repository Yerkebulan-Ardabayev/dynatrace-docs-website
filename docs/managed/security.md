# Безопасность Dynatrace Managed

## Аутентификация

- **Локальные пользователи**: CMC → Settings → Users
- **LDAP/AD**:
  ```yaml
  ldap:
    url: ldaps://ldap.example.com:636
    base_dn: dc=example,dc=com
    user_filter: (sAMAccountName={0})
  ```
- **SAML SSO**: настройте IdP (Okta, Azure AD), импортируйте метаданные в CMC, настройте маппинг групп

## Firewall порты

| Порт | Назначение |
|------|------------|
| 443 | Web UI |
| 8443 | CMC |
| 9999 | Cluster communication |
| 9200 | Elasticsearch |
| 7000-7199 | Cassandra |

## TLS/SSL

```bash
sudo /opt/dynatrace-managed/set-ssl.sh cert.pem key.pem
```

## Аудит

Логи: `/var/opt/dynatrace-managed/log/audit/`

## Рекомендации

Сложные пароли, 2FA, ограничение доступа к CMC, регулярные обновления, мониторинг аудит-логов.
