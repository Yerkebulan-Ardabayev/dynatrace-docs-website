# Dynatrace Managed - Полная документация

Этот документ содержит полную документацию по Dynatrace Managed для загрузки в NotebookLM.

---

## Установка Dynatrace Managed

Dynatrace Managed — это самоуправляемая версия платформы мониторинга Dynatrace, которая устанавливается на ваших серверах.

### Требования к системе

#### Аппаратные требования
- CPU: минимум 8 ядер, рекомендуется 16+
- RAM: минимум 32 GB, рекомендуется 64+ GB
- Диск: минимум 500 GB SSD, рекомендуется 1+ TB NVMe

#### Программные требования
- ОС: RHEL 7+, CentOS 7+, Ubuntu 18.04+ (64-bit)
- Java: OpenJDK 11+ (включен в установщик)
- Сеть: статический IP, открытые порты 443, 8443, 9999

### Процесс установки

1. Загрузка установщика:
```bash
wget https://your-dynatrace-server/installer/dynatrace-managed-installer.sh
chmod +x dynatrace-managed-installer.sh
```

2. Запуск установки:
```bash
sudo ./dynatrace-managed-installer.sh
```

3. После установки откройте веб-интерфейс: https://<your-server-ip>:8443

---

## Настройка Dynatrace Managed

### Сетевые настройки
1. Откройте Cluster Management Console (CMC)
2. Перейдите в Settings → Network
3. Настройте DNS серверы, прокси (если требуется), SSL сертификаты

### Настройка хранилища
- Метрики: 35 дней по умолчанию
- Трассировки: 10 дней
- Логи: 35 дней
- Сессии: 35 дней

### Email уведомления
```yaml
smtp:
  host: smtp.example.com
  port: 587
  user: notifications@example.com
  ssl: true
```

### LDAP/Active Directory
1. Перейдите в Settings → Authentication
2. Выберите LDAP
3. Укажите LDAP URL, Base DN, Bind DN и пароль

---

## Обслуживание Dynatrace Managed

### Мониторинг кластера
Доступ к CMC: https://<cluster-ip>:8443/cmc

Основные метрики:
- CPU/RAM использование узлов
- Дисковое пространство
- Cassandra состояние
- Elastic Search индексы

### Проверка статуса
```bash
systemctl status dynatracemanaged
journalctl -u dynatracemanaged -f
```

### Регулярные задачи

Ежедневно:
- Проверка алертов в CMC
- Мониторинг дискового пространства

Еженедельно:
- Проверка логов ошибок
- Анализ производительности

Ежемесячно:
- Проверка обновлений
- Тестирование бэкапов
- Ревью безопасности

---

## Обновления Dynatrace Managed

### Перед обновлением
ВАЖНО: Всегда делайте полный бэкап перед обновлением!

Чек-лист:
- Бэкап конфигурации
- Бэкап данных Cassandra
- Проверка здоровья кластера
- Уведомление пользователей о maintenance

### Rolling Update (без простоя)
```bash
sudo /opt/dynatrace-managed/updater/update.sh
```

### Откат
```bash
sudo /opt/dynatrace-managed/rollback.sh
```

---

## Безопасность Dynatrace Managed

### Аутентификация
- Локальные пользователи: CMC → Settings → Users
- LDAP/Active Directory
- SAML SSO (Okta, Azure AD)

### Firewall порты
- 443: Web UI
- 8443: CMC
- 9999: Cluster communication
- 9200: Elasticsearch
- 7000-7199: Cassandra

### TLS/SSL
```bash
sudo /opt/dynatrace-managed/set-ssl.sh cert.pem key.pem
```

### Бест-практики
- Используйте сложные пароли
- Включите 2FA
- Ограничьте доступ к CMC
- Регулярно обновляйте
- Мониторьте логи аудита

---

## Бэкап Dynatrace Managed

### Экспорт конфигурации
```bash
/opt/dynatrace-managed/backup/export-config.sh /backup/config/
```

### Snapshot Cassandra
```bash
nodetool snapshot -t backup_$(date +%Y%m%d)
```

### Snapshot Elasticsearch
```bash
curl -X PUT "localhost:9200/_snapshot/backup/snap_$(date +%Y%m%d)"
```

### Автоматический бэкап (cron)
```bash
0 2 * * * /opt/dynatrace-managed/backup/full-backup.sh
```

### Восстановление
```bash
/opt/dynatrace-managed/backup/restore-config.sh /backup/config/
nodetool restore -t backup_20260209
```

---

## Кластер Dynatrace Managed

### Архитектура
Load Balancer → Node 1, Node 2, Node 3 (все Active)

### Добавление узла
1. Установите Dynatrace Managed на новый сервер
2. При установке укажите "Join existing cluster"
3. Введите IP первого узла кластера
4. Подтвердите в CMC

### Удаление узла
1. Откройте CMC
2. Cluster → Nodes
3. Выберите узел → Remove

ВНИМАНИЕ: Минимум 3 узла для production!

### Масштабирование
- Small (3 узла, 32 GB RAM): до 100 хостов
- Medium (5 узлов, 64 GB RAM): до 500 хостов
- Large (7+ узлов, 128 GB RAM): 1000+ хостов

---

## Лицензирование

### Модели
- По хостам: лицензия на каждый мониторируемый хост
- По потреблению (DPS): Davis Data Units (DDU)

### Активация
1. Откройте CMC
2. Settings → License
3. Введите лицензионный ключ

### Лимиты по планам
- Starter: 10 хостов, 7 дней retention, Email support
- Standard: 100 хостов, 35 дней retention, 24/7 support
- Enterprise: Unlimited хостов, Custom retention, Premium support

---

## Контакты

Dynatrace Support:
- Email: support@dynatrace.com
- Web: dynatrace.com/support
- Sales: sales@dynatrace.com
