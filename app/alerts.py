import os
from datetime import datetime
from flask_socketio import SocketIO

# SocketIO singleton - asegúrate de que sea el mismo que usas en tu aplicación
socketio = SocketIO()

def trigger_alert(attack_type, src_ip, severity="alta"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert_data = {
        "type": attack_type,
        "src_ip": src_ip,
        "severity": severity,
        "timestamp": timestamp,
        "message": f"""
        ⚠️ ALERTA DE SEGURIDAD ⚠️
        - Tipo: {attack_type}
        - IP Origen: {src_ip}
        - Severidad: {severity}
        - Fecha: {timestamp}
        """
    }
    
    # Enviar notificación al navegador a través de Socket.IO
    socketio.emit('security_alert', alert_data)
    print(f"Alerta enviada al navegador: {attack_type} desde {src_ip}")