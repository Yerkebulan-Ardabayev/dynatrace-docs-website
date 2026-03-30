---
title: Расширения
source: https://www.dynatrace.com/docs/ingest-from/extensions
scraped: 2026-03-06T21:12:40.260899
---

# Extensions

## Что такое Extensions?

Модульные пакеты, определяющие сбор и структурирование телеметрии из внешних источников. Выполняются контроллером Extension Execution Controller (EEC) в вашей среде.

## Возможности

- Сбор метрик, событий и логов из технологий, не поддерживаемых изначально
- Создание индивидуальной логики мониторинга
- Визуализация и анализ пользовательских данных

## Ключевые преимущества

- Автоматическое распространение на ActiveGate и OneAgent с механизмом отказоустойчивости
- Полное моделирование топологии с пользовательскими сущностями
- Декларативный YAML-формат (без программирования) или программируемые расширения на Python

## Сценарии использования

- **SNMP** — сетевые устройства
- **SQL** — базы данных различных производителей
- **Prometheus** — экспортеры Prometheus
- **WMI** — устройства Windows
- **JMX** — данные из JMX MBeans

## Начало работы

- [Обзор поддерживаемых Extensions](extensions/supported-extensions.md)
- [Разработка собственных Extensions](extensions/develop-your-extensions.md)
- [Управление Extensions](extensions/manage-extensions.md)
- [Обзор в Dynatrace Hub](https://www.dynatrace.com/hub/detail/extension-manager/)
