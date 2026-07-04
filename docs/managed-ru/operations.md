# Обслуживание Dynatrace Managed

## Мониторинг кластера

CMC: `https://<cluster-ip>:8443/cmc`

Основные метрики: CPU/RAM узлов, дисковое пространство, состояние Cassandra и Elasticsearch.

```bash
systemctl status dynatracemanaged
journalctl -u dynatracemanaged -f
```

## Регулярные задачи

- **Ежедневно**: проверка алертов в CMC, мониторинг дисков
- **Еженедельно**: проверка логов ошибок, анализ производительности
- **Ежемесячно**: проверка обновлений, тестирование бэкапов, ревью безопасности

## Логи

| Лог | Путь |
|-----|------|
| Сервер | `/var/opt/dynatrace-managed/log/server/` |
| Cassandra | `/var/opt/dynatrace-managed/log/cassandra/` |
| Elastic | `/var/opt/dynatrace-managed/log/elasticsearch/` |

## Следующие шаги

- [Бэкап](backup.md)
- [Обновления](update.md)
