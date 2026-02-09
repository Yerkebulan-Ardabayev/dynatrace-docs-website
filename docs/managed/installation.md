# Установка Dynatrace Managed

Dynatrace Managed — это самоуправляемая версия платформы мониторинга Dynatrace, которая устанавливается на ваших серверах.

## Требования к системе

### Аппаратные требования

| Компонент | Минимум | Рекомендуется |
|-----------|---------|---------------|
| CPU | 8 ядер | 16+ ядер |
| RAM | 32 GB | 64+ GB |
| Диск | 500 GB SSD | 1+ TB NVMe |

### Программные требования

- **ОС**: RHEL 7+, CentOS 7+, Ubuntu 18.04+ (64-bit)
- **Java**: OpenJDK 11+ (включен в установщик)
- **Сеть**: статический IP, открытые порты 443, 8443, 9999

## Процесс установки

### 1. Загрузка установщика

```bash
wget https://your-dynatrace-server/installer/dynatrace-managed-installer.sh
chmod +x dynatrace-managed-installer.sh
```

### 2. Запуск установки

```bash
sudo ./dynatrace-managed-installer.sh
```

### 3. Настройка начального узла

После установки откройте веб-интерфейс:
```
https://<your-server-ip>:8443
```

## Следующие шаги

- [Настройка кластера](configuration.md)
- [Добавление узлов](managed-cluster.md)
- [Бэкап данных](backup.md)

!!! tip "Совет"
    Всегда делайте бэкап перед обновлениями!
