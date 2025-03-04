from app.capture import start_capture
from app.web_interface import run_web_interface
from threading import Thread

if __name__ == "__main__":
    # Iniciar la captura de paquetes en un hilo separado
    capture_thread = Thread(target=start_capture, kwargs={"count": 0})
    capture_thread.start()

    # Iniciar la interfaz web
    run_web_interface()