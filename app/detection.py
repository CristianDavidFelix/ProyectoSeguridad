from collections import defaultdict
from app.alerts import trigger_alert

# Umbrales para ataques
DDOS_THRESHOLD = 100  # Paquetes por segundo
PORT_SCAN_THRESHOLD = 50  # Puertos escaneados

packet_count = defaultdict(int)
port_scan_counter = defaultdict(int)

def detect_ddos(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        packet_count[src_ip] += 1

        if packet_count[src_ip] > DDOS_THRESHOLD:
            trigger_alert("DDoS", src_ip, "crítica")
            return True
    return False

def detect_port_scan(packet):
    if packet.haslayer("TCP") and packet["TCP"].flags == 'S':
        src_ip = packet["IP"].src
        port_scan_counter[src_ip] += 1

        if port_scan_counter[src_ip] > PORT_SCAN_THRESHOLD:
            trigger_alert("Escaneo de Puertos", src_ip, "media")
            return True
    return False

def detect_mitm(packet):
    # Lógica para detectar ARP spoofing
    if packet.haslayer("ARP") and packet["ARP"].op == 2:  # ARP Response
        if packet["ARP"].hwsrc != packet["ARP"].hwdst:
            trigger_alert("MITM (ARP Spoofing)", packet["ARP"].psrc, "alta")
            return True
    return False