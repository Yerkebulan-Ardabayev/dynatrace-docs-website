# Обслуживание Dynatrace Managed

Руководство по обслуживанию и мониторингу кластера Dynatrace Managed.

## Мониторинг кластера

### Cluster Management Console (CMC)

Доступ: `https://<cluster-ip>:8443/cmc`

**Основные метрики:**
- CPU/RAM использование узлов
- Дисковое пространство
- Cassandra состояние
- Elastic Search индексы

### Здоровье узлов

```bash
# Проверка статуса Dynatrace
systemctl status dynatracemanaged

# Просмотр логов
journalctl -u dynatracemanaged -f
```

## Регулярные задачи

### Ежедневно
- [ ] Проверка алертов в CMC
- [ ] Мониторинг дискового пространства

### Еженедельно
- [ ] Проверка логов ошибок
- [ ] Анализ производительности

### Ежемесячно
- [ ] Проверка обновлений
- [ ] Тестирование бэкапов
- [ ] Ревью безопасности

## Логи

| Лог | Путь |
|-----|------|
| Сервер | `/var/opt/dynatrace-managed/log/server/` |
| Cassandra | `/var/opt/dynatrace-managed/log/cassandra/` |
| Elastic | `/var/opt/dynatrace-managed/log/elasticsearch/` |

## Следующие шаги

- [Бэкап](backup.md)
- [Обновления](update.md)
