from scapy.all import sniff, IP, TCP
from datetime import datetime

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{timestamp}] Paquete detectado: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

        # Guardar el evento en el almacenamiento
        from app.storage import save_event
        save_event({
            "timestamp": timestamp,
            "src_ip": src_ip,
            "dst_ip": dst_ip,
            "src_port": src_port,
            "dst_port": dst_port,
            "type": "TCP Packet"
        })

def start_capture(interface="enp0s3", count=0):
    print(f"Iniciando captura en la interfaz {interface}...")
    sniff(iface=interface, prn=packet_callback, count=count)