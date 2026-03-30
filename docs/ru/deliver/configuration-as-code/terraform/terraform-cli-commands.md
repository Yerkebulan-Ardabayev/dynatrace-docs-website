---
title: Terraform команды CLI
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/terraform-cli-commands
scraped: 2026-03-06T21:25:48.138678
---

# Команды Terraform CLI

Подробная документация: [Terraform docs](https://developer.hashicorp.com/terraform/docs).

## Основные команды

* `init` — подготовка рабочего каталога
* `validate` — проверка корректности конфигурации
* `plan` — показ необходимых изменений
* `apply` — создание/обновление инфраструктуры
* `destroy` — удаление инфраструктуры

Дополнительная команда Dynatrace:
* `export` — экспорт существующих ресурсов из среды Dynatrace

## Экспорт конфигурации

### Предварительные требования

* Установленный Terraform CLI с Dynatrace Provider в `PATH`
* Платформенный токен или OAuth-клиент с необходимыми правами

### Использование

1. Задайте переменные окружения (см. раздел Поддержка API и управление правами доступа). Опционально задайте `DYNATRACE_TARGET_FOLDER` (по умолчанию `.configuration`).
2. Найдите исполняемый файл Provider в `.terraform/providers/registry.terraform.io/dynatrace-oss/dynatrace/{version}/{os}/`.
3. Запустите:

   ```
   # Windows
   terraform-provider-dynatrace.exe -export [-ref] [-migrate] [-import-state] [-id] [-flat] [-exclude] [<resourcename>[=<id>]]

   # Linux
   ./terraform-provider-dynatrace -export [-ref] [-migrate] [-import-state] [-id] [-flat] [-exclude] [<resourcename>[=<id>]]
   ```

### Команда list-exclusions

Показывает ресурсы, исключённые из экспорта по умолчанию (например, `dynatrace_json_dashboard`):

```
# Windows
terraform-provider-dynatrace.exe -export -list-exclusions

# Linux
./terraform-provider-dynatrace -export -list-exclusions
```

### Флаги

* `-ref` — включает ресурсы с источниками данных и зависимостями
* `-migrate` — включает зависимости без источников данных
* `-import-state` — инициализирует модули и импортирует в состояние
* `-id` — закомментированный вывод ID в файлах
* `-flat` — без модульной структуры
* `-exclude` — исключает указанные ресурсы

## Дополнительная информация

При экспорте некорректные файлы перемещаются в:
* `.flawed` — устаревшие или требующие модификации
* `.required_attention` — отсутствует существенная информация (например, конфиденциальные данные `dynatrace_credentials`)
