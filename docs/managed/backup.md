# Бэкап Dynatrace Managed

Руководство по резервному копированию.

## Типы бэкапов

### Конфигурация

```bash
# Экспорт конфигурации
/opt/dynatrace-managed/backup/export-config.sh /backup/config/
```

### Данные Cassandra

```bash
# Snapshot
nodetool snapshot -t backup_$(date +%Y%m%d)
```

### Elasticsearch

```bash
# Создание snapshot
curl -X PUT "localhost:9200/_snapshot/backup/snap_$(date +%Y%m%d)"
```

## Автоматический бэкап

### Настройка cron

```bash
# Ежедневный бэкап в 2:00
0 2 * * * /opt/dynatrace-managed/backup/full-backup.sh
```

### Хранение

| Тип | Период хранения |
|-----|-----------------|
| Ежедневные | 7 дней |
| Еженедельные | 4 недели |
| Ежемесячные | 12 месяцев |

## Восстановление

```bash
# Восстановление конфигурации
/opt/dynatrace-managed/backup/restore-config.sh /backup/config/

# Восстановление Cassandra
nodetool restore -t backup_20260209
```

!!! danger "Важно"
    Тестируйте восстановление регулярно!
