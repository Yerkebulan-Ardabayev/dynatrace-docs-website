#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.38 — RU build for 12 Azure networking metric files.

Reuses the column-aware engine + byte-identical boilerplate from L4-IF.37
(_build_azure_metrics_l4if37.py). Only the table cells Description / Unit /
Recommended + header labels are translated; Name + Dimensions stay EN (Azure
Metrics API identifiers). No em-dash (CLAUDE.md §0).

Batch (networking family):
  traffic-manager, dns-zone, private-dns-zone, network-interface,
  network-watcher, firewall, gateway-load-balancer, standard-load-balancer,
  expressroute-circuit, virtual-network-gateways, public-ip-addresses,
  web-application-firewall-policies.
"""

import os
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "eng", os.path.join(os.path.dirname(__file__), "_build_azure_metrics_l4if37.py")
)
eng = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(eng)

EN_DIR = "docs/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"
RU_DIR = "docs/managed-ru/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics"

BATCH = [
    "monitor-azure-traffic-manager.md",
    "monitor-azure-dns-zone.md",
    "monitor-azure-private-dns-zone.md",
    "monitor-azure-network-interface.md",
    "monitor-azure-network-watcher.md",
    "monitor-azure-firewall.md",
    "monitor-azure-gateway-load-balancer.md",
    "monitor-azure-standard-load-balancer.md",
    "monitor-azure-expressroute-circuit.md",
    "monitor-azure-virtual-network-gateways.md",
    "monitor-azure-public-ip-addresses.md",
    "monitor-azure-web-application-firewall-policies.md",
]

TITLE_MAP = {
    "monitor-azure-traffic-manager.md": (
        "Azure Traffic Manager monitoring",
        "Мониторинг Azure Traffic Manager",
    ),
    "monitor-azure-dns-zone.md": (
        "Azure DNS Zone monitoring",
        "Мониторинг Azure DNS Zone",
    ),
    "monitor-azure-private-dns-zone.md": (
        "Azure Private DNS Zone monitoring",
        "Мониторинг Azure Private DNS Zone",
    ),
    "monitor-azure-network-interface.md": (
        "Azure Network Interface monitoring",
        "Мониторинг Azure Network Interface",
    ),
    "monitor-azure-network-watcher.md": (
        "Azure Network Watcher (Connection Monitor, Connection Monitor Preview) monitoring",
        "Мониторинг Azure Network Watcher (Connection Monitor, Connection Monitor Preview)",
    ),
    "monitor-azure-firewall.md": (
        "Azure Firewall monitoring",
        "Мониторинг Azure Firewall",
    ),
    "monitor-azure-gateway-load-balancer.md": (
        "Azure Gateway Load Balancer monitoring",
        "Мониторинг Azure Gateway Load Balancer",
    ),
    "monitor-azure-standard-load-balancer.md": (
        "Azure Standard Load Balancer monitoring",
        "Мониторинг Azure Standard Load Balancer",
    ),
    "monitor-azure-expressroute-circuit.md": (
        "Azure ExpressRoute Circuit monitoring",
        "Мониторинг Azure ExpressRoute Circuit",
    ),
    "monitor-azure-virtual-network-gateways.md": (
        "Azure Virtual Network Gateway monitoring",
        "Мониторинг Azure Virtual Network Gateway",
    ),
    "monitor-azure-public-ip-addresses.md": (
        "Azure Public IP Address monitoring",
        "Мониторинг Azure Public IP Address",
    ),
    "monitor-azure-web-application-firewall-policies.md": (
        "Azure Web Application Firewall (WAF) Policy on Azure CDN monitoring",
        "Мониторинг Azure Web Application Firewall (WAF) Policy on Azure CDN",
    ),
}

# ---- dates: base map + 2 new ----
DATE_MAP = dict(eng.DATE_MAP)
DATE_MAP.update(
    {
        "* Published Jun 25, 2020": "* Опубликовано 25 июня 2020 г.",
        "* Published Sep 18, 2020": "* Опубликовано 18 сентября 2020 г.",
    }
)

# ---- prose: base boilerplate + batch-specific ----
PROSE = list(eng.PROSE) + [
    ("* 2-min read", "* Чтение: 2 мин"),
    # load balancer "monitors a part of" note (gateway-/standard-load-balancer)
    (
        "This service monitors a part of Azure Load Balancer (Microsoft.Network/loadBalancers). While you have this service configured, you can't have Azure Load Balancers (built-in) service turned on.",
        "Этот сервис отслеживает часть Azure Load Balancer (Microsoft.Network/loadBalancers). Пока этот сервис настроен, вы не можете включить сервис Azure Load Balancers (built-in).",
    ),
    # virtual-network-gateways intro prose
    (
        "On the Azure Virtual Network Gateway overview page you can monitor connected workloads and performance to ensure that Azure Virtual Network Gateway is successfully connected.",
        "На странице обзора Azure Virtual Network Gateway вы можете отслеживать подключённые рабочие нагрузки и производительность, чтобы убедиться, что Azure Virtual Network Gateway успешно подключён.",
    ),
    (
        "Only the VPN gateway type can be monitored by Dynatrace. The ExpressRoute gateway type is not monitored.",
        "Dynatrace может отслеживать только шлюзы типа VPN. Шлюзы типа ExpressRoute не отслеживаются.",
    ),
]

HEADER_LABEL = dict(eng.HEADER_LABEL)
REC_MAP = dict(eng.REC_MAP)

# ---- units: base + compound unit+dimension cells (public-ip scraper merge) ----
UNIT_MAP = dict(eng.UNIT_MAP)
UNIT_MAP.update(
    {
        "Byte, Port, Direction": "Байт, Port, Direction",
        "Count, Port, Direction": "Количество, Port, Direction",
        "Percent, Port": "Процент, Port",
    }
)

# ---- networking metric Description cells (EN exact -> RU). Name + Dimensions EN. ----
NET_DESC = {
    # traffic-manager
    "Number of times a Traffic Manager endpoint was returned in the given time frame.": "Количество раз, когда конечная точка Traffic Manager была возвращена за указанный период времени.",
    "`1` if endpoint probe status is `Enabled`, otherwise `0`.": "`1`, если статус пробы конечной точки `Enabled`, иначе `0`.",
    # dns-zone
    "The volume of DNS queries": "Объём DNS-запросов",
    "The percentage utilization of the maximum limit of record sets for your DNS zone": "Процент использования максимального лимита наборов записей для вашей зоны DNS",
    "The count of DNS record sets within your DNS zone": "Количество наборов записей DNS в вашей зоне DNS",
    # private-dns-zone
    "Number of queries served for a DNS zone": "Количество запросов, обработанных для зоны DNS",
    "Number of Record Sets in a DNS zone": "Количество наборов записей в зоне DNS",
    "Percentage of Record Set capacity utilized by a DNS zone": "Процент использования ёмкости наборов записей зоной DNS",
    "Number of virtual networks associated with a private DNS zone": "Количество виртуальных сетей, связанных с частной зоной DNS",
    "Percentage of virtual network capacity utilized by a private DNS zone": "Процент ёмкости виртуальной сети, используемой частной зоной DNS",
    "Percentage of capacity utilization for a virtual network with automatic registration that is utilized by a private DNS zone": "Процент использования ёмкости для виртуальной сети с автоматической регистрацией, используемой частной зоной DNS",
    "Number of virtual networks that are linked to a private DNS zone and for which automatic registration is activated": "Количество виртуальных сетей, связанных с частной зоной DNS, для которых включена автоматическая регистрация",
    # network-interface
    "Number of bytes received by the network interface": "Количество байтов, полученных сетевым интерфейсом",
    "Number of bytes sent by the network interface": "Количество байтов, отправленных сетевым интерфейсом",
    "Number of packets received by the network interface": "Количество пакетов, полученных сетевым интерфейсом",
    "Number of packets sent by the network interface": "Количество пакетов, отправленных сетевым интерфейсом",
    # network-watcher
    "The average network round-trip time (ms) for connectivity monitoring probes sent between source and destination": "Среднее сетевое время кругового пути (мс) для проб мониторинга связности, отправляемых между источником и назначением",
    "The percentage of connectivity monitoring probes failed": "Процент неудавшихся проб мониторинга связности",
    "The average network RTT for connectivity monitoring probes sent between source and destination": "Среднее сетевое время кругового пути (RTT) для проб мониторинга связности, отправляемых между источником и назначением",
    "The percentage of failed checks for a test": "Процент неудавшихся проверок для теста",
    "The RTT for checks sent between source and destination": "Время кругового пути (RTT) для проверок, отправляемых между источником и назначением",
    # firewall
    "Number of times application rules were hit": "Количество срабатываний правил приложений",
    "Total amount of data processed by this firewall": "Общий объём данных, обработанных этим брандмауэром",
    "Indicates the overall health of this firewall": "Показывает общее состояние работоспособности этого брандмауэра",
    "Number of times network rules were hit": "Количество срабатываний сетевых правил",
    "Percentage of outbound SNAT ports currently in use": "Процент исходящих SNAT-портов, используемых в настоящее время",
    # load balancers (gateway + standard)
    "Average Load Balancer data path availability per time duration": "Средняя доступность пути данных Load Balancer за период времени",
    "Average Load Balancer health probe status per time duration": "Средний статус пробы работоспособности Load Balancer за период времени",
    "Total number of Bytes transmitted within time period": "Общее количество байтов, переданных за период времени",
    "Total number of Packets transmitted within time period": "Общее количество пакетов, переданных за период времени",
    "Total number of SYN Packets transmitted within time period": "Общее количество SYN-пакетов, переданных за период времени",
    "Total number of new SNAT connections created within time period": "Общее количество новых SNAT-подключений, созданных за период времени",
    "Total number of SNAT ports allocated within time period": "Общее количество SNAT-портов, выделенных за период времени",
    "Total number of SNAT ports used within time period": "Общее количество SNAT-портов, использованных за период времени",
    "Azure Cross-region Load Balancer backend health and status per time duration": "Работоспособность и статус бэкенда Azure Cross-region Load Balancer за период времени",
    # expressroute-circuit
    "ARP availability from MSEE towards all peers": "Доступность ARP от MSEE ко всем пирам",
    "BGP availability from MSEE towards all peers": "Доступность BGP от MSEE ко всем пирам",
    "Bits ingressing Azure per second": "Биты, входящие в Azure, в секунду",
    "Bits egressing Azure per second": "Биты, исходящие из Azure, в секунду",
    "Ingress bits of data dropped per second": "Входящие биты данных, отброшенные в секунду",
    "Egress bits of data dropped per second": "Исходящие биты данных, отброшенные в секунду",
    # virtual-network-gateways
    "Average site-to-site bandwidth of a gateway in bytes per second": "Средняя пропускная способность шлюза «сеть-сеть» в байтах в секунду",
    "Average point-to-site bandwidth of a gateway in bytes per second": "Средняя пропускная способность шлюза «точка-сеть» в байтах в секунду",
    "Point-to-site connection count of a gateway": "Количество подключений «точка-сеть» шлюза",
    "Average bandwidth of a tunnel in bytes per second": "Средняя пропускная способность туннеля в байтах в секунду",
    "Outgoing bytes of a tunnel": "Исходящие байты туннеля",
    "Outgoing packet drop count from traffic selector mismatch of a tunnel": "Количество исходящих пакетов туннеля, отброшенных из-за несоответствия селектора трафика",
    "Outgoing packet count of a tunnel": "Количество исходящих пакетов туннеля",
    "Incoming bytes of a tunnel": "Входящие байты туннеля",
    "Incoming packet drop count from traffic selector mismatch of a tunnel": "Количество входящих пакетов туннеля, отброшенных из-за несоответствия селектора трафика",
    "Incoming packet count of a tunnel": "Количество входящих пакетов туннеля",
    # public-ip-addresses + DDoS
    "Total number of bytes transmitted within time period": "Общее количество байтов, переданных за период времени",
    "Total number of packets transmitted within time period": "Общее количество пакетов, переданных за период времени",
    "Inbound bytes dropped DDoS": "Входящие отброшенные байты DDoS",
    "Inbound bytes forwarded DDoS": "Входящие пересланные байты DDoS",
    "Inbound bytes DDoS": "Входящие байты DDoS",
    "Inbound SYN packets to trigger DDoS mitigation": "Входящие SYN-пакеты для запуска подавления DDoS",
    "Inbound TCP packets to trigger DDoS mitigation": "Входящие пакеты TCP для запуска подавления DDoS",
    "Inbound UDP packets to trigger DDoS mitigation": "Входящие пакеты UDP для запуска подавления DDoS",
    "Under DDoS attack or not": "Находится ли под DDoS-атакой",
    "Inbound packets dropped DDoS": "Входящие отброшенные пакеты DDoS",
    "Inbound packets forwarded DDoS": "Входящие пересланные пакеты DDoS",
    "Inbound packets DDoS": "Входящие пакеты DDoS",
    "Inbound TCP bytes dropped DDoS": "Входящие отброшенные байты TCP DDoS",
    "Inbound TCP bytes forwarded DDoS": "Входящие пересланные байты TCP DDoS",
    "Inbound TCP bytes DDoS": "Входящие байты TCP DDoS",
    "Inbound TCP packets dropped DDoS": "Входящие отброшенные пакеты TCP DDoS",
    "Inbound TCP packets forwarded DDoS": "Входящие пересланные пакеты TCP DDoS",
    "Inbound TCP packets DDoS": "Входящие пакеты TCP DDoS",
    "Inbound UDP bytes dropped DDoS": "Входящие отброшенные байты UDP DDoS",
    "Inbound UDP bytes forwarded DDoS": "Входящие пересланные байты UDP DDoS",
    "Inbound UDP bytes DDoS": "Входящие байты UDP DDoS",
    "Inbound UDP packets dropped DDoS": "Входящие отброшенные пакеты UDP DDoS",
    "Inbound UDP packets forwarded DDoS": "Входящие пересланные пакеты UDP DDoS",
    "Inbound UDP packets DDoS": "Входящие пакеты UDP DDoS",
    "Average IP address availability per time duration": "Средняя доступность IP-адреса за период времени",
    # web-application-firewall-policies
    "The number of client requests processed by Web Application Firewall": "Количество клиентских запросов, обработанных Web Application Firewall",
}

# base wins for any shared EN string (cross-file consistency), net fills the rest
DESC_MAP = dict(eng.DESC_MAP)
for k, v in NET_DESC.items():
    DESC_MAP.setdefault(k, v)

warnings = []


def is_sep(cells):
    return all(set(c) <= set("-: ") for c in cells)


def tr_table_line(line, colmap, fname):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    out = []
    for i, cell in enumerate(cells):
        col = colmap[i] if i < len(colmap) else None
        if col == "Description":
            if cell and cell not in DESC_MAP:
                warnings.append("%s: untranslated DESC -> %r" % (fname, cell))
            out.append(DESC_MAP.get(cell, cell))
        elif col == "Unit":
            if cell not in UNIT_MAP:
                warnings.append("%s: unmapped UNIT -> %r" % (fname, cell))
            out.append(UNIT_MAP.get(cell, cell))
        elif col and col.startswith("Recommended"):
            if cell not in REC_MAP:
                warnings.append("%s: unmapped REC -> %r" % (fname, cell))
            out.append(REC_MAP.get(cell, cell))
        else:  # Name, Dimensions, unknown -> keep EN
            out.append(cell)
    return "| " + " | ".join(out) + " |"


def tr_header(line):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    out = [HEADER_LABEL.get(c, c) for c in cells]
    return "| " + " | ".join(out) + " |", cells


def build_one(fname):
    en = open(os.path.join(EN_DIR, fname), encoding="utf-8").read()
    en_title, ru_title = TITLE_MAP[fname]
    out_lines = []
    colmap = None
    for line in en.split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if is_sep(cells):
                out_lines.append(line)
            elif cells and cells[0] == "Name":
                tline, colmap = tr_header(line)
                out_lines.append(tline)
            elif colmap is not None:
                out_lines.append(tr_table_line(line, colmap, fname))
            else:
                out_lines.append(line)
        else:
            colmap = None
            s = line
            if en_title != ru_title:
                s = s.replace(en_title, ru_title)
            for k, v in DATE_MAP.items():
                s = s.replace(k, v)
            for k, v in PROSE:
                s = s.replace(k, v)
            out_lines.append(s)
    result = "\n".join(out_lines)
    out_path = os.path.join(RU_DIR, fname)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, "w", encoding="utf-8", newline="").write(result)
    return en, result


def main():
    ok = 0
    for fname in BATCH:
        en, ru = build_one(fname)
        en_n, ru_n = en.count("\n"), ru.count("\n")
        status = "OK" if en_n == ru_n else "LINE MISMATCH %d!=%d" % (en_n, ru_n)
        if en_n == ru_n:
            ok += 1
        print("%-22s  %s  (%d lines)" % (status, fname, ru_n + 1))
    print("\nline-parity OK: %d/%d" % (ok, len(BATCH)))
    if warnings:
        print("\n=== WARNINGS (%d) ===" % len(warnings))
        for w in warnings:
            print("  ", w)
    else:
        print("no warnings")


if __name__ == "__main__":
    main()
