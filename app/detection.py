from collections import defaultdict

# Detectar posibles ataques DDoS
def detect_ddos(packet, threshold=100):
    packet_count = defaultdict(int)

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        packet_count[src_ip] += 1

        if packet_count[src_ip] > threshold:
            print(f"[ALERTA] Posible ataque DDoS desde {src_ip}")
            return True
    return False

# Detectar escaneo de puertos
def detect_port_scan(packet):
    if packet.haslayer(TCP) and packet[TCP].flags == 'S':  # SYN flag
        print(f"[ALERTA] Posible escaneo de puertos desde {packet[IP].src}")
        return True
    return False