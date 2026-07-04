# Установка Dynatrace Managed

Самоуправляемая версия платформы мониторинга, устанавливаемая на ваши серверы.

## Требования

### Аппаратные

| Компонент | Минимум | Рекомендуется |
|-----------|---------|---------------|
| CPU | 8 ядер | 16+ ядер |
| RAM | 32 GB | 64+ GB |
| Диск | 500 GB SSD | 1+ TB NVMe |

### Программные

- **ОС**: RHEL 7+, CentOS 7+, Ubuntu 18.04+ (64-bit)
- **Java**: OpenJDK 11+ (включен в установщик)
- **Сеть**: статический IP, порты 443, 8443, 9999

## Установка

```bash
wget https://your-dynatrace-server/installer/dynatrace-managed-installer.sh
chmod +x dynatrace-managed-installer.sh
sudo ./dynatrace-managed-installer.sh
```

Веб-интерфейс после установки: `https://<your-server-ip>:8443`

## Следующие шаги

- [Настройка кластера](configuration.md)
- [Добавление узлов](managed-cluster.md)
- [Бэкап данных](backup.md)

!!! tip "Совет"
    Всегда делайте бэкап перед обновлениями!
