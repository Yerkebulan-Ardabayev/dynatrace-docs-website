# Бэкап Dynatrace Managed

## Типы бэкапов

### Конфигурация

```bash
/opt/dynatrace-managed/backup/export-config.sh /backup/config/
```

### Cassandra

```bash
nodetool snapshot -t backup_$(date +%Y%m%d)
```

### Elasticsearch

```bash
curl -X PUT "localhost:9200/_snapshot/backup/snap_$(date +%Y%m%d)"
```

## Автоматический бэкап

```bash
# cron: ежедневно в 2:00
0 2 * * * /opt/dynatrace-managed/backup/full-backup.sh
```

| Тип | Хранение |
|-----|----------|
| Ежедневные | 7 дней |
| Еженедельные | 4 недели |
| Ежемесячные | 12 месяцев |

## Восстановление

```bash
/opt/dynatrace-managed/backup/restore-config.sh /backup/config/
nodetool restore -t backup_20260209
```

!!! danger "Важно"
    Тестируйте восстановление регулярно!
