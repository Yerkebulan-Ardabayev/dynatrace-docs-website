---
title: Устранение проблем мониторинга
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/troubleshooting/monitoring-troubleshooting
scraped: 2026-05-12T12:12:06.126238
---

# Устранение проблем мониторинга

# Устранение проблем мониторинга

* Чтение: 1 мин
* Опубликовано 28 июля 2023 г.

В этом руководстве приведены общие шаги по устранению неполадок и рекомендации для распространённых проблем, возникающих при использовании Dynatrace с Kubernetes. Оно охватывает доступ к отладочным логам, использование подкоманды `troubleshoot` и создание архива поддержки.

Если требуется вручную собрать файлы или логи OneAgent непосредственно с узлов Kubernetes, точные пути хранения см. в разделе [Требования к хранилищу](/managed/ingest-from/setup-on-k8s/reference/storage "Подробный обзор требований к хранилищу для различных режимов развёртывания Dynatrace Operator в окружениях Kubernetes").

* [Поды зависают в состоянии `Terminating` после обновления](https://dt-url.net/lga38l5)
* [Не удаётся получить полный список серверных API](https://dt-url.net/9m838d0)
* [`CrashLoopBackOff`: понижение версии OneAgent не поддерживается, сначала удалите старую версию](https://dt-url.net/3n838mb)
* [Цикл сбоев на подах при установке OneAgent](https://dt-url.net/tv0382u)
* [Развёртывание кажется успешным, но контейнер `dynatrace-oneagent` не отображается как готовый](https://dt-url.net/ss638y7)
* [Развёртывание кажется успешным, однако образ `dynatrace-oneagent` не удаётся загрузить](https://dt-url.net/lw238h9)
* [Развёртывание кажется успешным, но контейнер `dynatrace-oneagent` не выдаёт содержательных логов](https://dt-url.net/38438k2)
* [Развёртывание кажется успешным, но контейнер `dynatrace-oneagent` не запущен](https://dt-url.net/6r638b3)
* [Развёртывание прошло успешно, но данные мониторинга недоступны в Dynatrace](https://dt-url.net/wg237zk)
* [На узлах control-plane не запланированы поды](https://dt-url.net/fk038ey)
* [Ошибка при применении пользовательского ресурса в GKE](https://dt-url.net/6ye38x5)
* [`CannotPullContainerError`](https://dt-url.net/df837qz)
* [Ограничение временного интервала логов](https://dt-url.net/lr6370p)
* [Создание сервиса Dynatrace Kubernetes завершается с ошибкой при включённом Istio](https://dt-url.net/qd038te)
* [Поды приложения зависают в состоянии terminating](https://dt-url.net/pf03ng8)
* [Устранение неполадок node-pools AKS WASM](https://dt-url.net/qa03q47)